"""Offline rule, persistence, async, planner-gating and H0 isolation regressions."""

from copy import deepcopy
import json
from threading import Event

import pytest

from go2_demo.memory import AsyncMemory, MemoryRules, PACKET_KEYS, read_state, state_packet
from go2_demo.memory_planning import MemoryPlanningHarness, PublicObservationAdapter
from go2_demo.models import APIModel
from go2_demo.types import Decision, ToolCall


def evidence(frame="f1", x=2.0, confidence=0.95, source="rgbd_detector"):
    return {"object_id": "landmark-1", "category": "unclassified_landmark",
            "pose": {"frame": "episode_start", "position_m": [x, 0.]},
            "pose_covariance": None, "confidence": confidence, "source": source,
            "frame_id": frame, "anchor_node": None, "visual_feature": None}


def plan(preconditions=None, completion=None):
    return {"subgoals": [{"subgoal_id": "approach", "description": "Approach landmark",
                          "preconditions": preconditions or [], "completion": completion or []}],
            "branches": [{"on": "skill_stuck", "subgoal_id": "approach"}], "recovery": "observe again"}


def confirmed_rules():
    rules = MemoryRules()
    rules.update({"step": 0, "objects": [evidence()]})
    rules.update({"step": 1, "objects": [evidence("f2")]})
    return rules


def test_multiframe_confirmation_and_repeat_reads_are_not_new_evidence():
    rules = MemoryRules()
    rules.update({"step": 0, "objects": [evidence()]})
    assert rules.state["objects"][0]["state"] == "unknown"
    rules.update({"step": 1, "objects": [evidence()]})
    assert len(rules.state["ledger"]) == 1
    assert rules.state["objects"][0]["last_seen"] == 0
    rules.update({"step": 2, "objects": [evidence("f2", x=2.1)]})
    obj = rules.state["objects"][0]
    assert obj["state"] == "confirmed" and obj["pose"]["position_m"] == [2.1, 0.]
    assert obj["last_seen"] == 2 and obj["source"] == "rgbd_detector"
    assert len(obj["evidence_ids"]) == 2


def test_multisensor_evidence_can_confirm_same_frame():
    rules = MemoryRules()
    rules.update({"step": 0, "objects": [evidence(), evidence(source="depth_detector")]})
    assert rules.state["objects"][0]["state"] == "confirmed"


def test_loss_prediction_unknown_stale_and_no_deletion():
    rules = confirmed_rules()
    for step, expected in [(3, "confirmed"), (4, "predicted"), (7, "unknown"), (11, "stale")]:
        rules.update({"step": step})
        assert rules.state["objects"][0]["state"] == expected
    assert len(rules.state["objects"]) == 1
    assert len(rules.state["ledger"]) == 5


def test_reacquisition_needs_recent_independent_support():
    rules = confirmed_rules()
    rules.update({"step": 11})
    rules.update({"step": 12, "objects": [evidence("f3")]})
    assert rules.state["objects"][0]["state"] == "unknown"
    rules.update({"step": 13, "objects": [evidence("f4")]})
    assert rules.state["objects"][0]["state"] == "confirmed"


def test_positive_relocation_invalidates_dependents_and_retains_old_position():
    rules = confirmed_rules()
    rules.set_plan("plan-1", plan([{"object_id": "landmark-1"}]))
    prefix = deepcopy(rules.state["ledger"])
    rules.update({"step": 2, "objects": [evidence("f3", x=4.)]})
    obj = rules.state["objects"][0]
    assert obj["state"] == "contradicted" and obj["pose"]["position_m"] == [2., 0.]
    assert obj["candidate_pose"]["position_m"] == [4., 0.]
    assert rules.state["plans"][0]["subgoals"][0]["status"] == "已失效"
    assert rules.state["ledger"][:len(prefix)] == prefix
    assert {e["kind"] for e in rules.state["events"]} >= {"replan_required", "target_state_changed"}
    assert state_packet(rules.state)["objects"] == []
    rules.update({"step": 3, "objects": [evidence("f4", x=4.)]})
    assert obj["state"] == "confirmed" and obj["pose"]["position_m"] == [4., 0.]
    assert rules.state["plans"][0]["subgoals"][0]["status"] == "已失效"


def test_old_plan_subgoals_are_inactive_not_deleted():
    rules = confirmed_rules()
    rules.set_plan("p1", plan())
    rules.set_plan("p2", plan())
    assert not rules.state["plans"][0]["active"]
    assert not rules.state["plans"][0]["subgoals"][0]["active"]
    assert {g["plan_id"] for g in state_packet(rules.state)["active_beliefs"]} == {"p2"}


def test_completion_requires_measurements_and_can_be_invalidated():
    rules = MemoryRules()
    rules.set_plan("p1", plan(completion=[{"measurement": "pose.x_m", "op": "ge", "value": 1.}]))
    action = {"tool": "finish", "status": "succeeded", "plan_id": "p1", "subgoal_id": "approach"}
    rules.update({"step": 1, "actions": [action]})
    goal = rules.state["plans"][0]["subgoals"][0]
    assert goal["status"] == "进行中"
    rules.update({"step": 2, "measurements": {"pose.x_m": {"value": 1.1, "source": "odometry"}}})
    assert goal["status"] == "已完成" and goal["evidence_ids"]
    rules.update({"step": 3, "measurements": {"pose.x_m": {"value": 0.8, "source": "odometry"}}})
    assert goal["status"] == "已失效"


def test_verifier_reports_stuck_blocked_and_constraint_events_without_false_small_motion_alarm():
    rules = MemoryRules()
    rules.update({"step": 1, "actions": [{"tool": "move_relative", "status": "succeeded"}]})
    assert not rules.state["events"]
    rules.update({"step": 2, "actions": [
        {"tool": "move_relative", "status": "failed", "error_code": "DYNAMIC_OBSTACLE"},
        {"tool": "turn", "status": "failed", "error_code": "MEMORY_CONSTRAINT"}]})
    assert {e["kind"] for e in rules.state["events"]} >= {
        "skill_stuck", "dynamic_obstacle_blocked", "key_precondition_invalidated", "replan_required"}
    assert [e["kind"] for e in rules.state["ledger"]] == ["action_executed", "action_failed", "action_failed"]


@pytest.mark.parametrize("change", [
    {"source": ""}, {"confidence": float("nan")},
    {"pose": {"frame": "episode_start", "position_m": [float("inf"), 0.]}},
    {"pose_covariance": [[-1., 0.], [0., 1.]]},
])
def test_bad_evidence_never_enters_beliefs(change):
    rules = MemoryRules()
    with pytest.raises(ValueError):
        rules.update({"step": 0, "objects": [{**evidence(), **change}]})
    assert rules.state["objects"] == []


def test_packet_filters_ledger_old_plans_stale_objects_and_limits_provenance():
    rules = confirmed_rules()
    for step in range(2, 24):
        rules.update({"step": step, "objects": [evidence(f"f{step+1}")]})
    packet = state_packet(rules.state)
    assert set(packet) == set(PACKET_KEYS)
    assert "ledger" not in packet and "plans" not in packet
    assert len(packet["objects"][0]["evidence_ids"]) == 2
    assert len(packet["events"]) <= 16
    assert state_packet(rules.state, 33)["objects"] == []
    assert state_packet(rules.state, 33)["pose"] is None


def test_md_roundtrip_empty_future_sections_and_append_only_history(tmp_path):
    path = tmp_path / "memory.md"
    with_memory = AsyncMemory(path)
    try:
        with_memory.submit({"step": 0, "objects": [evidence()]})
        with_memory.flush()
        first = read_state(path.read_text())
        with_memory.submit({"step": 1, "objects": [evidence("f2")]})
        with_memory.flush()
        document = path.read_text()
        assert document.endswith("## 操作经验\n\n## 程序工具\n")
        state = read_state(document)
        assert state == with_memory.snapshot()
        assert state["ledger"][:len(first["ledger"])] == first["ledger"]
        with pytest.raises(FileExistsError):
            AsyncMemory(path)
    finally:
        with_memory.close()


def test_slow_writer_does_not_block_snapshot_or_planning_and_shutdown_drains(tmp_path, monkeypatch):
    memory = AsyncMemory(tmp_path / "memory.md")
    entered, release = Event(), Event()
    publish = memory._publish

    def delayed():
        entered.set()
        assert release.wait(5)
        publish()

    monkeypatch.setattr(memory, "_publish", delayed)
    try:
        memory.submit({"step": 1, "objects": [evidence()]})
        assert entered.wait(2)
        # This code cannot reach release if packet/context waits on the writer.
        packet = MemoryPlanningHarness(memory).context("task", 1)["memory_state"]
        assert packet["world"]["revision"] == 0
        assert packet["world"]["snapshot_lag_steps"] == 1
        assert read_state(memory.path.read_text())["world"]["revision"] == 0
    finally:
        release.set()
        memory.close()
    assert read_state(memory.path.read_text())["world"]["step"] == 1


def test_disk_failure_exposes_event_and_prevents_motion(tmp_path, monkeypatch):
    memory = AsyncMemory(tmp_path / "memory.md")
    monkeypatch.setattr(memory, "_publish", lambda: (_ for _ in ()).throw(OSError("private error text")))
    try:
        memory.submit({"step": 1})
        with pytest.raises(RuntimeError):
            memory.flush()
        planner = MemoryPlanningHarness(memory)
        decision = Decision([ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.})],
                            assistant_content=json.dumps({"plan": plan(), "subgoal_id": "approach"}))
        feedback, _ = planner.prepare(decision, 1)
        assert feedback["error_code"] == "MEMORY_CONSTRAINT"
        assert planner.context("task", 1)["memory_state"]["events"][-1]["kind"] == "memory_write_failed"
        assert "private error text" not in json.dumps(planner.context("task", 1))
    finally:
        with pytest.raises(RuntimeError):
            memory.close()


def test_precondition_gating_blocks_false_unknown_predicted_and_stale_evidence(tmp_path):
    memory = AsyncMemory(tmp_path / "memory.md")
    planner = MemoryPlanningHarness(memory)
    try:
        memory.submit({"step": 0, "objects": [evidence()]})
        memory.submit({"step": 1, "objects": [evidence("f2")]})
        memory.flush()
        decision = Decision([ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.})],
                            assistant_content=json.dumps({"plan": plan([{"object_id": "landmark-1"}]),
                                                          "subgoal_id": "approach"}))
        assert planner.prepare(decision, 1)[0] is None
        memory.flush()
        decision.assistant_content = json.dumps({"plan_id": planner.plan_id, "subgoal_id": "approach"})
        assert planner.prepare(decision, 2)[0]["error_code"] == "MEMORY_CONSTRAINT"  # lag
        for step in (4, 7, 11):
            memory.submit({"step": step})
            memory.flush()
            assert planner.prepare(decision, step)[0]["error_code"] == "MEMORY_CONSTRAINT"
    finally:
        memory.close()


def test_model_messages_use_only_current_memory_no_old_state_or_camera():
    model = APIModel("https://example.invalid/v1", "test", "", trust_env=False)
    observation = {"task": "task", "memory_state": state_packet(MemoryRules().state)}
    messages = model.build_messages(observation, "", [{"observation": {"old": "INVALIDATED_SECRET"}}])
    assert len(messages) == 2
    current = json.loads(messages[1]["content"])
    assert current['task'] == observation['task']
    assert set(current['memory_state']) == set(observation['memory_state'])
    assert current['memory_state']['objects'] == []
    assert current['memory_state']['world']['decision_step'] == 0
    assert len(messages[1]['content']) <= 12000
    assert "INVALIDATED_SECRET" not in json.dumps(messages)
    assert "image_url" not in json.dumps(messages)


def test_public_adapter_uses_local_odometry_and_never_semantically_labels_points():
    observation = {"local_odometry": {"translation_m": [10., 20.], "yaw_rad": 1.5707963267948966,
                                       "source": "odometry"}, "image_id": "f1", "image_size": {},
                   "tracked_points": [{"point_id": "p1", "valid": True, "relative_xy_m": [2., 0.],
                                       "confidence": 0.9, "source": "rgbd", "image_id": "f1", "pixel_uv": [2., 3.]}],
                   "robot_state": {"hidden_target": [99., 99.], "body_joint": 12.}}
    result = PublicObservationAdapter().payload(observation, 0)
    assert result["objects"][0]["pose"]["position_m"] == pytest.approx([10., 22.])
    assert result["objects"][0]["category"] == "unclassified_landmark"
    assert "hidden_target" not in json.dumps(result) and "body_joint" not in json.dumps(result)


def test_external_positive_disturbance_invalidates_belief_and_dependent_goal():
    rules = confirmed_rules()
    rules.set_plan("p1", plan([{"object_id": "landmark-1"}]))
    rules.update({"step": 2, "disturbances": [{"source": "independent_depth_sensor",
        "object_id": "landmark-1", "disproves": True, "blocked": True}]})
    assert rules.state["objects"][0]["state"] == "contradicted"
    assert rules.state["plans"][0]["subgoals"][0]["status"] == "已失效"
    assert any(e["kind"] == "external_disturbance" for e in rules.state["ledger"])
    assert any(e["kind"] == "dynamic_obstacle_blocked" for e in rules.state["events"])


def test_rejected_plan_is_kept_in_ledger_but_never_becomes_active(tmp_path):
    memory = AsyncMemory(tmp_path / "memory.md")
    try:
        planner = MemoryPlanningHarness(memory)
        decision = Decision([ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.})],
            assistant_content=json.dumps({"plan": plan([{"object_id": "missing"}]), "subgoal_id": "approach"}))
        feedback, binding = planner.prepare(decision, 0)
        assert feedback["error_code"] == "MEMORY_CONSTRAINT" and binding["plan_id"] == "plan-0001"
        assert "fresh confirmed evidence" in feedback["constraint_feedback"]
        memory.flush()
        state = memory.snapshot()
        assert state["world"]["active_plan_id"] is None
        assert state["plans"][0]["subgoals"][0]["status"] == "已失效"
        assert any(e["kind"] == "plan_rejected" for e in state["ledger"])
        assert memory.packet(0)["active_beliefs"] == []
        assert memory.packet(0)["invalidated"][0]["plan_id"] == binding["plan_id"]
    finally:
        memory.close()


@pytest.mark.parametrize("tool,arguments", [("stop", {}), ("abort", {"reason": "recover"})])
def test_stop_abort_remain_available_even_with_malformed_plan(tmp_path, tool, arguments):
    memory = AsyncMemory(tmp_path / "memory.md")
    try:
        feedback, _ = MemoryPlanningHarness(memory).prepare(
            Decision([ToolCall("safe", tool, arguments)], assistant_content="invalid JSON"), 0)
        assert feedback is None
    finally:
        memory.close()


def test_explicitly_disproved_measurement_returns_specific_constraints(tmp_path):
    memory = AsyncMemory(tmp_path / "memory.md")
    try:
        memory.submit({"step": 0, "measurements": {"clearance_m": {"value": 0.1, "source": "depth"}}})
        memory.flush()
        decision = Decision([ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.})],
            assistant_content=json.dumps({"plan": plan([{"measurement": "clearance_m", "op": "ge", "value": 0.5}]),
                                          "subgoal_id": "approach"}))
        feedback, _ = MemoryPlanningHarness(memory).prepare(decision, 0)
        assert feedback["constraint_feedback"] == "Memory disproves a required precondition"
    finally:
        memory.close()

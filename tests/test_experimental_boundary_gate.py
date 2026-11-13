"""Temporary simulator-GT safety interlock: offline tests, no API or key access."""
from copy import deepcopy
import json
import math
from types import SimpleNamespace

import numpy as np
import pytest

from go2_demo.experimental_boundary_gate import (
    EXPERIMENTAL_SUPPORT_MARGIN_M, experimental_boundary_gate,
    experimental_boundary_memory_results,
)
from go2_demo.harness import Harness
from go2_demo.memory import AsyncMemory, MemoryRules, read_state
from go2_demo.memory_planning import MemoryPlanningHarness, PublicObservationAdapter
from go2_demo.runner import run_episode
from go2_demo.scenarios import get_scenario
from go2_demo.types import Decision, ToolCall
from test_harness import RecordingBackend
from test_runner import EpisodeBackend


SCENE = get_scenario("memory_ab_occluded_v1")


def refusal(pose=(0., 5.5, math.pi / 2), forward=.3, lateral=0., scenario=SCENE):
    return experimental_boundary_gate(scenario, pose, forward_m=forward, lateral_m=lateral)


@pytest.mark.parametrize("pose,edge", [
    ((7.6, 0., 0.), "east"), ((-7.6, 0., math.pi), "west"),
    ((0., 5.6, math.pi / 2), "north"), ((0., -5.6, -math.pi / 2), "south"),
])
def test_outward_move_is_refused_with_direction_distance_and_gt_provenance(pose, edge):
    result = refusal(pose)
    assert result["status"] == "failed" and result["error_code"] == "BOUNDARY_BLOCKED"
    detail = result["constraint_feedback"]
    assert detail["blocked_directions"] == [edge]
    assert detail["requested_distance_m"] == pytest.approx(.3)
    assert 0 <= detail["safe_distance_along_request_m"] < .3
    assert detail["experimental"] and not detail["executed"]
    assert detail["source"] == "simulator_ground_truth_boundary_safety_interlock"
    assert detail["navigation_measurement"] is False


def test_center_only_inside_endpoint_still_needs_support_reserve():
    assert 5.5 + .3 < SCENE.floor_half_size_m[1]
    assert refusal()["error_code"] == "BOUNDARY_BLOCKED"
    assert EXPERIMENTAL_SUPPORT_MARGIN_M == .35


def test_body_lateral_command_is_rotated_and_rectangle_corner_checked():
    result = refusal((7.6, 5.6, 0.), forward=.2, lateral=.2)
    assert set(result["constraint_feedback"]["blocked_directions"]) == {"east", "north"}
    assert refusal((0., 5.6, 0.), forward=0., lateral=.3)["error_code"] == "BOUNDARY_BLOCKED"


def test_inside_path_and_retreat_from_existing_reserve_are_allowed():
    assert refusal((0., 0., .7), forward=.4, lateral=.2) is None
    assert refusal((0., 5.8, math.pi / 2), forward=-.2) is None
    assert refusal((0., 5.8, 0.), forward=.2) is None


def test_dimensions_are_read_from_scenario_and_infinite_floor_is_unchanged():
    small = SimpleNamespace(floor_half_size_m=(2., 1.))
    assert refusal((0., .5, math.pi / 2), scenario=small)["error_code"] == "BOUNDARY_BLOCKED"
    assert refusal((0., .5, math.pi / 2)) is None
    assert refusal((999., 999., 0.), scenario=None) is None
    assert refusal((999., 999., 0.), scenario=SimpleNamespace(floor_half_size_m=None)) is None


def test_real_dispatch_refusal_is_cached_without_motion_refresh_or_observation_leak():
    backend = RecordingBackend(); backend.scenario = SCENE
    backend.pose[:] = (0., 5.5, math.pi / 2)
    harness = Harness(backend, "offline")
    before = deepcopy(harness.observation())
    call = ToolCall("blocked", "move_relative", {"forward_m": .3, "lateral_m": 0.})
    first = harness.dispatch(call); second = harness.dispatch(call)
    assert first["error_code"] == second["error_code"] == "BOUNDARY_BLOCKED"
    assert second["deduplicated"]
    assert backend.moves == [] and backend.capture_count == 1
    assert harness.observation() == before and harness.termination is None
    assert backend.stops == backend.evaluations == 0
    assert harness.dispatch(ToolCall("recover", "move_relative", {"forward_m": -.2, "lateral_m": 0.}))["status"] == "succeeded"
    assert backend.moves == [(-.2, 0.)]
    assert harness.dispatch(ToolCall("turn", "turn", {"yaw_rad": -.4}))["status"] == "succeeded"


def test_inside_move_reaches_backend_and_invalid_argument_precedence_is_unchanged():
    backend = RecordingBackend(); backend.scenario = SCENE
    harness = Harness(backend, "offline")
    assert harness.dispatch(ToolCall("ok", "move_relative", {"forward_m": .3, "lateral_m": .1}))["status"] == "succeeded"
    assert backend.moves == [(.3, .1)]
    assert harness.dispatch(ToolCall("bad", "move_relative", {"forward_m": .7, "lateral_m": 0.}))["error_code"] == "INVALID_ARGUMENTS"
    assert len(backend.moves) == 1


def plan():
    return {"subgoals": [{"subgoal_id": "leg", "description": "explore", "preconditions": [],
                          "completion": []}], "branches": [], "recovery": "choose another action"}


def test_repeated_refusals_do_not_write_boundary_memory_or_change_plan_but_clock_advances():
    rules = MemoryRules(); reference = MemoryRules()
    for item in (rules, reference):
        item.set_plan("p", plan())
        for step in range(1,4):
            item.update({"step": step, "actions": [{"tool": "turn", "status": "succeeded"}]})
    result = {"tool": "move_relative", "call_id": "blocked", **refusal(), "plan_id": "p", "subgoal_id": "leg"}
    original = deepcopy(result)
    for step in range(4,16):
        rules.update({"step": step, "actions": experimental_boundary_memory_results([result])})
        reference.update({"step": step, "actions": []})
    assert result == original and rules.state == reference.state
    assert rules.state["plans"][0]["active"]
    assert rules.state["plans"][0]["subgoals"][0]["status"] == "待做"
    assert rules.state["world"]["exploration"]["successful_turns_without_search_progress"] == 3
    assert rules.state["world"]["exploration"]["decisions_since_task_novelty"] == 15
    assert [r["step"] for r in rules.state["ledger"] if r["kind"] == "search_review_due"] == [12]
    assert not any(e["kind"] in {"skill_stuck", "key_precondition_invalidated"} for e in rules.state["events"])
    assert "BOUNDARY_BLOCKED" not in rules.document()
    assert "support_margin" not in rules.document()
    other = {"tool": "track_point", "status": "failed", "error_code": "PERCEPTION_ERROR"}
    assert experimental_boundary_memory_results([other]) == [other]


def test_feedback_uses_existing_last_tool_feedback_only_and_does_not_write_md(tmp_path):
    memory = AsyncMemory(tmp_path / "memory.md")
    try:
        planner = MemoryPlanningHarness(memory)
        before_md = memory.path.read_bytes(); before_packet = planner.context("offline", 0)
        result = {"call_id": "b", "tool": "move_relative", **refusal()}
        planner.note_results([ToolCall("b", "move_relative", {"forward_m": .3, "lateral_m": 0.})], [result])
        after_packet = planner.context("offline", 0)
        feedback = after_packet["memory_state"]["world"].pop("last_tool_feedback")
        before_packet["memory_state"]["world"].pop("last_tool_feedback")
        assert after_packet == before_packet
        assert feedback[0]["error_code"] == "BOUNDARY_BLOCKED"
        assert feedback[0]["constraint_feedback"]["blocked_directions"] == ["north"]
        assert memory.path.read_bytes() == before_md
    finally:
        memory.close()


def test_runner_repeated_refusals_reach_planner_not_memory_and_are_not_executed(tmp_path):
    class Backend(EpisodeBackend):
        scenario = SCENE

        def capture(self):
            frame = super().capture()
            frame.base_xy_yaw[:] = (0., 5.5, math.pi / 2)
            return frame

    class Model:
        count = 0
        received_feedback = []

        def decide(self, observation, *args, **kwargs):
            self.count += 1
            feedback = observation["memory_state"]["world"].get("last_tool_feedback", [])
            if self.count > 1:
                assert feedback[0]["error_code"] == "BOUNDARY_BLOCKED"
                assert feedback[0]["constraint_feedback"]["blocked_directions"] == ["north"]
                self.received_feedback.append(feedback)
            envelope = {"plan": plan(), "subgoal_id": "leg"} if self.count == 1 else {"plan_id": "plan-0001", "subgoal_id": "leg"}
            return Decision([ToolCall(f"b{self.count}", "move_relative", {"forward_m": .3, "lateral_m": 0.})],
                            planning_envelope=envelope)

    backend = Backend(score_success=False); model = Model()
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path, memory_v1=True, max_model_calls=12)
    assert metrics["termination"] == "budget_exhausted" and metrics["decision_calls"] == 12
    assert metrics["motion_calls"] == 0 and backend.moves == []
    state = read_state((tmp_path / "memory.md").read_text())
    assert "BOUNDARY_BLOCKED" not in json.dumps(state)
    assert state["plans"][0]["active"] and state["plans"][0]["subgoals"][0]["status"] == "待做"
    assert state["world"]["exploration"]["review_count"] == 1
    assert not any(e["kind"] == "skill_stuck" for e in state["events"])
    events = [json.loads(s) for s in (tmp_path / "events.jsonl").read_text().splitlines()]
    results = [r for r in events if r["event"] == "tool_results"]
    assert len(results) == 12 and len(model.received_feedback) == 11
    assert all(r["results"][0]["error_code"] == "BOUNDARY_BLOCKED" for r in results)

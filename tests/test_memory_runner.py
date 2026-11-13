"""Memory opt-in integration uses injected fakes only; no API or MuJoCo demo."""

import json

from go2_demo import __main__ as cli
from go2_demo.memory import read_state
from go2_demo.runner import run_episode
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend, EpisodeModel


def test_rejected_plan_never_reaches_motion_backend(tmp_path):
    class Planner:
        model = "offline-memory-fixture"

        def decide(self, observation, image, tools, history, **kwargs):
            assert set(observation) == {"task", "memory_state"}
            assert image == "" and history == []
            return Decision([ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.})],
                            assistant_content=json.dumps({"plan": {
                                "subgoals": [{"subgoal_id": "s1", "description": "missing landmark",
                                    "preconditions": [{"object_id": "nonexistent"}], "completion": []}],
                                "branches": [], "recovery": "observe"}, "subgoal_id": "s1"}))

    backend = EpisodeBackend()
    metrics = run_episode(backend, Planner(), mode="api", run_dir=tmp_path,
                          memory_v1=True, max_model_calls=1)
    assert backend.moves == [] and metrics["motion_calls"] == 0
    assert metrics["termination"] == "budget_exhausted" and not metrics["success"]
    state = read_state((tmp_path / "memory.md").read_text())
    assert any(row["kind"] == "action_failed" for row in state["ledger"])
    assert any(row["kind"] == "replan_required" for row in state["events"])
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest["external_memory"] and manifest["memory_protocol"] == "rule_md_async_v1"


def test_h0_default_does_not_create_memory_and_keeps_manifest(tmp_path):
    metrics = run_episode(EpisodeBackend(), EpisodeModel(), mode="api", run_dir=tmp_path)
    assert metrics["success"]
    assert not (tmp_path / "memory.md").exists()
    assert json.loads((tmp_path / "manifest.json").read_text())["external_memory"] is False


def test_memory_does_not_promote_finish_to_independent_success(tmp_path):
    class Planner:
        def decide(self, *args, **kwargs):
            return Decision([ToolCall("finish", "finish", {})], assistant_content=json.dumps({
                "plan": {"subgoals": [{"subgoal_id": "s", "description": "model claims complete",
                                       "preconditions": [], "completion": []}],
                         "branches": [], "recovery": "observe"}, "subgoal_id": "s"}))

    metrics = run_episode(EpisodeBackend(score_success=False), Planner(), mode="api", run_dir=tmp_path,
                          memory_v1=True)
    assert metrics["termination"] == "finish" and not metrics["success"]
    state = read_state((tmp_path / "memory.md").read_text())
    assert state["plans"][0]["subgoals"][0]["status"] != "已完成"


def test_memory_flag_and_compatible_settings_reach_cli_without_loading_model(monkeypatch, tmp_path):
    seen = []

    def run(args, scenario, run_dir):
        seen.append(args)
        return {"success": True, "termination": "finish"}, 0

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main(["--memory-v1", "--provider", "compatible", "--model-name", "deepseek-v4.1-flash",
                     "--api-key-file", "/home/nuonuosenlin/deepseekapi.txt", "--runs-dir", str(tmp_path)]) == 0
    assert seen[0].memory_v1 and seen[0].provider == "compatible"


def test_memory_listing_never_loads_credentials_or_simulator(monkeypatch):
    monkeypatch.setattr(cli, "_make_model", lambda *a: (_ for _ in ()).throw(AssertionError("API started")))
    assert cli.main(["--memory-v1", "--list-tasks"]) == 0


def test_memory_writer_failure_is_visible_in_metrics_and_closes_resources(tmp_path, monkeypatch):
    from go2_demo.memory import AsyncMemory

    publish = AsyncMemory._publish
    counter = [0]

    def fail_on_worker(self):
        counter[0] += 1
        if counter[0] > 1:
            raise OSError("private write exception")
        publish(self)

    monkeypatch.setattr(AsyncMemory, "_publish", fail_on_worker)
    backend, model = EpisodeBackend(), EpisodeModel(tool="observe")
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path,
                          memory_v1=True, max_model_calls=1)
    assert metrics["termination"] == "memory_error" and not metrics["success"]
    assert backend.closed and model.closed
    assert "private write exception" not in json.dumps(metrics)

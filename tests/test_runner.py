"""Exit-path tests avoid importing MuJoCo and use injected model/backend contracts."""

import json

import numpy as np
import pytest

from go2_demo.models import ModelError
from go2_demo.runner import run_episode
from go2_demo.types import Decision, SensorFrame, ToolCall


class EpisodeBackend:
    def __init__(self, *, score_success=True, stop_results=None):
        self.score_success = score_success
        self.stop_results = list(stop_results or [])
        self.stops = 0
        self.closed = False
        self.frames = 0
        self.moves = []
        self.trajectory = []

    def capture(self):
        self.frames += 1
        return SensorFrame(
            frame_id=f"frame-{self.frames}", sim_time_s=self.frames * 0.01,
            rgb=np.zeros((20, 30, 3), np.uint8), depth_m=np.full((20, 30), 2., np.float32),
            intrinsics=np.array([[30., 0., 15.], [0., 30., 10.], [0., 0., 1.]]),
            camera_to_world=np.eye(4), base_xy_yaw=np.zeros(3),
            robot_state={"speed_mps": 0.0, "hidden_target": [100., 200., 300.]},
        )

    def stop(self):
        self.stops += 1
        result = self.stop_results.pop(0) if self.stop_results else {"status": "succeeded"}
        if isinstance(result, BaseException):
            raise result
        return result

    def evaluate(self, *, standoff_m, tolerance_m):
        assert self.stops > 0, "Evaluation must occur after a stop attempt"
        return {"success": self.score_success, "distance_m": 1.0}

    def close(self):
        self.closed = True

    def move_relative(self, **arguments):
        self.moves.append(arguments)
        return {"status": "succeeded"}


class EpisodeModel:
    model = "injected-test-model"

    def __init__(self, *, exception=None, tool="finish", after_decision=None):
        self.exception = exception
        self.tool = tool
        self.closed = False
        self.after_decision = after_decision

    def decide(self, *args, **kwargs):
        if self.exception is not None:
            raise self.exception
        if self.after_decision:
            self.after_decision()
        arguments = {"forward_m": 0.2, "lateral_m": 0.0} if self.tool == "move_relative" else {}
        return Decision([ToolCall("test-call", self.tool, arguments)], model=self.model)

    def close(self):
        self.closed = True


@pytest.mark.parametrize("exception,termination", [
    (ModelError("simulated provider timeout", "MODEL_TIMEOUT"), "model_error"),
    (KeyboardInterrupt(), "interrupted"),
])
def test_model_failure_and_interrupt_stop_close_and_cannot_succeed(tmp_path, exception, termination):
    backend = EpisodeBackend(score_success=True)
    model = EpisodeModel(exception=exception)
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path)
    assert metrics["termination"] == termination
    assert metrics["success"] is False
    assert backend.stops == 1
    assert backend.closed and model.closed
    assert json.loads((tmp_path / "metrics.json").read_text(encoding="utf-8"))["success"] is False


def test_premature_finish_still_fails_independent_evaluation(tmp_path):
    backend = EpisodeBackend(score_success=False)
    model = EpisodeModel()
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path)
    assert metrics["termination"] == "finish"
    assert metrics["success"] is False
    assert backend.stops >= 1
    assert backend.closed and model.closed


@pytest.mark.parametrize("final_stop", [
    {"status": "failed", "error_code": "STOP_NOT_SETTLED"},
    RuntimeError("Stop controller failed"),
])
def test_failed_final_stop_overrides_otherwise_successful_finish(tmp_path, final_stop):
    backend = EpisodeBackend(stop_results=[{"status": "succeeded"}, final_stop])
    model = EpisodeModel()
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path)
    assert metrics["termination"] == "finish"
    assert metrics["success"] is False
    assert metrics["final_stop"]["status"] == "failed"
    assert backend.closed and model.closed


def test_call_budget_exhaustion_stops_and_closes(tmp_path):
    backend = EpisodeBackend()
    model = EpisodeModel(tool="observe")
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path, max_model_calls=1)
    assert metrics["termination"] == "budget_exhausted"
    assert metrics["success"] is False
    assert metrics["model_calls"] == 1
    assert backend.stops == 1
    assert backend.closed and model.closed


def test_late_model_response_does_not_execute_motion(tmp_path, monkeypatch):
    clock = [0.0]
    monkeypatch.setattr("go2_demo.runner.time.monotonic", lambda: clock[0])
    backend = EpisodeBackend()
    model = EpisodeModel(tool="move_relative", after_decision=lambda: clock.__setitem__(0, 2.0))
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path, max_wall_seconds=1.0)
    assert metrics["termination"] == "budget_exhausted"
    assert backend.moves == []
    assert backend.closed and model.closed


def test_logs_keep_hidden_truth_out_of_model_input_and_redact_api_key(tmp_path, monkeypatch):
    secret = "test-key-DO-NOT-LOG"
    monkeypatch.setenv("MODEL_API_KEY", secret)
    backend = EpisodeBackend()
    model = EpisodeModel(exception=ModelError(f"Request failed for {secret}"))
    metrics = run_episode(backend, model, mode="api", run_dir=tmp_path)
    assert secret not in json.dumps(metrics)
    text = (tmp_path / "events.jsonl").read_text(encoding="utf-8")
    assert secret not in text
    records = [json.loads(line) for line in text.splitlines()]
    inputs = [row for row in records if row["event"] == "model_input"]
    assert len(inputs) == 1
    assert "hidden_target" not in json.dumps(inputs[0])
    assert (tmp_path / inputs[0]["image_path"]).exists()
    assert metrics["simulation_mode"] == "paused_during_model_inference"


def test_reasoning_is_preserved_in_retained_turns_but_only_counts_are_logged(tmp_path):
    reasoning = [f"PRIVATE-REASONING-FIXTURE-{index}-" + "x" * 20000 for index in range(3)]

    class ThinkingModel:
        def __init__(self):
            self.turn = 0

        def decide(self, observation, image, tools, history, **kwargs):
            assert image.startswith("data:image/png;base64,")
            if self.turn:
                assert len(history) == 1
                assert history[0]["reasoning_content"] == reasoning[self.turn - 1]
                assert history[0]["assistant_content"] == f"assistant-{self.turn - 1}"
            else:
                assert history == []
            index = self.turn
            self.turn += 1
            return Decision([ToolCall(f"call-{index}", "finish" if index == 2 else "observe", {})],
                            reasoning_content=reasoning[index], assistant_content=f"assistant-{index}")

    metrics = run_episode(EpisodeBackend(), ThinkingModel(), mode="api", run_dir=tmp_path,
                          history_turns=1)
    assert metrics["success"]
    assert metrics["reasoning_responses"] == 3
    assert metrics["reasoning_characters"] == sum(map(len, reasoning))
    events = (tmp_path / "events.jsonl").read_text()
    assert "PRIVATE-REASONING-FIXTURE" not in events
    assert "PRIVATE-REASONING-FIXTURE" not in (tmp_path / "metrics.json").read_text()


def test_non_api_mode_is_rejected_before_any_decision_or_motion(tmp_path):
    backend = EpisodeBackend()
    with pytest.raises(ValueError, match="Only API"):
        run_episode(backend, EpisodeModel(), mode="scripted", run_dir=tmp_path)
    assert backend.stops == 0 and backend.moves == []

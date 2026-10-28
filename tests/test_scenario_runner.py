"""The selected scenario must reach both model context and independent scoring."""

from dataclasses import replace
import json

import numpy as np

from go2_demo.runner import build_manifest, run_episode
from go2_demo.scenarios import get_scenario
from go2_demo.types import Decision, SensorFrame, ToolCall


class ScenarioBackend:
    def __init__(self):
        self.scenario = replace(get_scenario("go_to_blue_ball"), standoff_m=1.4, distance_tolerance_m=0.21)
        self.task_instruction = self.scenario.instruction
        self.frames = 0
        self.closed = False
        self.evaluation_arguments = None
        self.trajectory = []

    def capture(self):
        self.frames += 1
        return SensorFrame(frame_id=f"frame-{self.frames}", sim_time_s=self.frames * 0.01,
                           rgb=np.zeros((20, 30, 3), np.uint8), depth_m=np.full((20, 30), 2.0, np.float32),
                           intrinsics=np.array([[30.0, 0.0, 15.0], [0.0, 30.0, 10.0], [0.0, 0.0, 1.0]]),
                           camera_to_world=np.eye(4), base_xy_yaw=np.zeros(3), robot_state={"speed_mps": 0.0})

    def stop(self):
        return {"status": "succeeded"}

    def evaluate(self, **kwargs):
        self.evaluation_arguments = kwargs
        return {"success": True}

    def close(self):
        self.closed = True


class FinishModel:
    def __init__(self):
        self.observations = []
        self.closed = False

    def decide(self, observation, image, tools, history, **kwargs):
        self.observations.append(observation)
        return Decision([ToolCall("finish-selected-task", "finish", {})])

    def close(self):
        self.closed = True


def test_selected_instruction_and_scoring_are_consistent_without_goal_truth_leak(tmp_path):
    backend, model = ScenarioBackend(), FinishModel()
    result = run_episode(backend, model, mode="api", run_dir=tmp_path)
    assert result["success"]
    assert result["task_id"] == "go_to_blue_ball"
    assert model.observations[0]["task"] == backend.scenario.instruction
    assert "target_xy" not in json.dumps(model.observations)
    assert backend.evaluation_arguments == {"standoff_m": 1.4, "tolerance_m": 0.21}
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest["task"] == backend.scenario.instruction
    assert manifest["task_id"] == "go_to_blue_ball"
    assert manifest["evaluation"]["standoff_m"] == 1.4
    assert manifest["scenario_source"] == backend.scenario.source
    assert backend.closed and model.closed


def test_explicit_episode_instruction_override_is_logged_and_sent_consistently(tmp_path):
    backend, model = ScenarioBackend(), FinishModel()
    instruction = "Select the blue sphere and stop at the configured evaluation distance."
    run_episode(backend, model, mode="api", run_dir=tmp_path, task=instruction)
    assert model.observations[0]["task"] == instruction
    assert json.loads((tmp_path / "manifest.json").read_text())["task"] == instruction


def test_passage_manifest_records_crossing_instead_of_standoff_requirements():
    backend = ScenarioBackend()
    backend.scenario = get_scenario("go_through_red_triangle_tunnel")
    backend.task_instruction = backend.scenario.instruction
    manifest = build_manifest("api", 0, {}, backend, FinishModel())
    criteria = manifest["evaluation"]
    assert criteria["goal_kind"] == "passage" and criteria["requires_forward_crossing"]
    assert criteria["passage_x_m"] == backend.scenario.passage_x
    assert criteria["finish_x_min_m"] == backend.scenario.finish_x_min
    assert criteria["heading_tolerance_rad"] is None and criteria["standoff_m"] is None

"""Dispatch tests assert that invalid or repeated calls have no motion side effects."""

import json
import math

import numpy as np
import pytest

from go2_demo.harness import Harness
from go2_demo.types import SensorFrame, ToolCall


class RecordingBackend:
    def __init__(self):
        self.capture_count = 0
        self.moves = []
        self.turns = []
        self.stops = 0
        self.evaluations = 0
        self.pose = np.array([0., 0., 0.])

    def capture(self):
        self.capture_count += 1
        transform = np.eye(4)
        transform[:3, :3] = [[0., 0., 1.], [-1., 0., 0.], [0., -1., 0.]]
        return SensorFrame(
            frame_id=f"frame-{self.capture_count}", sim_time_s=self.capture_count * 0.1,
            rgb=np.zeros((80, 100, 3), np.uint8), depth_m=np.full((80, 100), 2., np.float32),
            intrinsics=np.array([[100., 0., 50.], [0., 100., 40.], [0., 0., 1.]]),
            camera_to_world=transform, base_xy_yaw=self.pose.copy(),
            robot_state={"speed_mps": 0., "target_position": [99., 99., 99.], "oracle_success": True},
        )

    def move_relative(self, forward_m, lateral_m):
        self.moves.append((forward_m, lateral_m))
        return {"status": "succeeded", "measured": {"forward_m": forward_m, "lateral_m": lateral_m}}

    def turn(self, yaw_rad):
        self.turns.append(yaw_rad)
        return {"status": "succeeded"}

    def stop(self):
        self.stops += 1
        return {"status": "succeeded"}

    def evaluate(self):
        self.evaluations += 1
        return {"success": False}


@pytest.fixture
def setup_harness():
    backend = RecordingBackend()
    return Harness(backend, "Approach the visible red marker."), backend


@pytest.mark.parametrize("value", [True, float("nan"), float("inf"), -float("inf"), "0.2", 0.61, -0.61])
def test_bad_translation_does_not_move_robot(setup_harness, value):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("bad", "move_relative", {"forward_m": value, "lateral_m": 0.0}))
    assert result["status"] == "failed"
    assert backend.moves == []


def test_vector_norm_limit_rejects_diagonal_overreach(setup_harness):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("diagonal", "move_relative", {"forward_m": 0.5, "lateral_m": 0.5}))
    assert result["error_code"] == "INVALID_ARGUMENTS"
    assert backend.moves == []


@pytest.mark.parametrize("args", [{"forward_m": 0.2}, {"forward_m": 0.2, "lateral_m": 0., "speed": 9.}])
def test_schema_errors_do_not_move_robot(setup_harness, args):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("schema", "move_relative", args))
    assert result["status"] == "failed"
    assert backend.moves == []


def test_turn_limit_is_enforced(setup_harness):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("turn", "turn", {"yaw_rad": 0.7}))
    assert result["status"] == "failed"
    assert backend.turns == []


def test_duplicate_call_returns_cached_result_without_second_motion(setup_harness):
    harness, backend = setup_harness
    call = ToolCall("move-1", "move_relative", {"forward_m": 0.2, "lateral_m": 0.0})
    first = harness.dispatch(call)
    second = harness.dispatch(call)
    assert first["status"] == second["status"] == "succeeded"
    assert second["deduplicated"] is True
    assert backend.moves == [(0.2, 0.0)]


def test_reused_call_id_with_new_arguments_is_rejected(setup_harness):
    harness, backend = setup_harness
    harness.dispatch(ToolCall("same", "move_relative", {"forward_m": 0.2, "lateral_m": 0.0}))
    result = harness.dispatch(ToolCall("same", "move_relative", {"forward_m": -0.2, "lateral_m": 0.0}))
    assert result["error_code"] == "CALL_ID_REUSED"
    assert backend.moves == [(0.2, 0.0)]


def test_parallel_finish_and_motion_execute_neither(setup_harness):
    harness, backend = setup_harness
    results = harness.dispatch_many([
        ToolCall("finish", "finish", {}),
        ToolCall("move", "move_relative", {"forward_m": 0.2, "lateral_m": 0.0}),
    ])
    assert len(results) == 2
    assert all(r["error_code"] == "ONE_TOOL_PER_TURN" for r in results)
    assert backend.moves == []
    assert backend.stops == 0
    assert harness.termination is None


def test_no_target_truth_or_evaluator_score_in_observation(setup_harness):
    harness, backend = setup_harness
    observation = harness.observation()
    assert observation["robot_state"] == {"speed_mps": 0.0}
    assert "target_position" not in str(observation)
    assert "oracle_success" not in str(observation)
    assert backend.evaluations == 0


def test_finish_stops_but_does_not_claim_independent_success(setup_harness):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("finish", "finish", {}))
    assert harness.termination == "finish"
    assert backend.stops == 1
    assert backend.evaluations == 0
    assert "success" not in result
    assert backend.evaluate()["success"] is False
    after = harness.dispatch(ToolCall("late", "move_relative", {"forward_m": 0.2, "lateral_m": 0.0}))
    assert after["error_code"] == "EPISODE_ENDED"
    assert backend.moves == []


def test_abort_stops_without_claiming_finish(setup_harness):
    harness, backend = setup_harness
    harness.dispatch(ToolCall("abort", "abort", {"reason": "Target is not visible"}))
    assert harness.termination == "abort"
    assert backend.stops == 1


def test_unimplemented_posture_is_explicitly_rejected(setup_harness):
    harness, backend = setup_harness
    result = harness.dispatch(ToolCall("posture", "set_posture", {"body_height_m": 0.2, "body_pitch_rad": 0.0}))
    assert result["error_code"] == "UNSUPPORTED_CAPABILITY"
    assert backend.moves == [] and backend.stops == 0


def test_stale_image_cannot_register_a_point(setup_harness):
    harness, _ = setup_harness
    old_image_id = harness.observation()["image_id"]
    harness.refresh()
    result = harness.dispatch(ToolCall("point", "track_point", {"image_id": old_image_id, "u": 50., "v": 40.}))
    assert result["status"] == "failed"
    assert "STALE_IMAGE" in result["message"]
    assert harness.observation()["tracked_points"] == []


def test_odometry_starts_at_zero_without_exposing_absolute_pose():
    backend = RecordingBackend()
    backend.pose[:] = [1234.5, -4321.5, 1.2]
    harness = Harness(backend, "Go through the visible opening.")
    observation = harness.observation()
    assert observation["local_odometry"] == {
        "translation_m": [0., 0.], "yaw_rad": 0.,
        "reference": "episode_start_body_horizontal",
        "source": "simulated_proprioception",
    }
    encoded = json.dumps(observation, allow_nan=False)
    assert "1234.5" not in encoded and "-4321.5" not in encoded
    assert "base_xy_yaw" not in encoded and "camera_to_world" not in encoded
    assert "target_position" not in encoded and "oracle_success" not in encoded
    assert backend.evaluations == 0


def test_odometry_uses_initial_body_axes_and_keeps_its_origin():
    backend = RecordingBackend()
    backend.pose[:] = [10., 20., math.pi / 2]
    harness = Harness(backend, "Move through the opening.")
    backend.pose[:] = [8., 23., math.pi]
    odometry = harness.refresh()["local_odometry"]
    assert odometry["translation_m"] == pytest.approx([3., 2.])
    assert odometry["yaw_rad"] == pytest.approx(math.pi / 2)
    assert all(type(value) is float for value in odometry["translation_m"])
    assert type(odometry["yaw_rad"]) is float
    assert harness.refresh()["local_odometry"] == odometry


@pytest.mark.parametrize("initial_yaw,current_yaw,expected", [
    (math.pi - 0.05, -math.pi + 0.05, 0.1),
    (-math.pi + 0.05, math.pi - 0.05, -0.1),
])
def test_odometry_wraps_yaw_at_pi(initial_yaw, current_yaw, expected):
    backend = RecordingBackend()
    backend.pose[2] = initial_yaw
    harness = Harness(backend, "Turn.")
    backend.pose[2] = current_yaw
    assert harness.refresh()["local_odometry"]["yaw_rad"] == pytest.approx(expected)


def test_odometry_reports_actual_cumulative_travel_instead_of_command_sum():
    class ShortTravelBackend(RecordingBackend):
        def move_relative(self, forward_m, lateral_m):
            super().move_relative(forward_m, lateral_m)
            measured = np.array([forward_m, lateral_m]) * 0.88
            yaw = self.pose[2]
            self.pose[:2] += np.array([[math.cos(yaw), -math.sin(yaw)],
                                       [math.sin(yaw), math.cos(yaw)]]) @ measured
            return {"status": "succeeded", "measured": {"translation_start_frame_m": measured.tolist()}}

    backend = ShortTravelBackend()
    backend.pose[:] = [9., -4., math.pi / 2]
    harness = Harness(backend, "Move through the opening.")
    for index in range(2):
        result = harness.dispatch(ToolCall(str(index), "move_relative", {"forward_m": 0.6, "lateral_m": 0.}))
        assert result["status"] == "succeeded"
        assert result["measured"]["translation_start_frame_m"] == pytest.approx([0.528, 0.])
    assert harness.observation()["local_odometry"]["translation_m"] == pytest.approx([1.056, 0.])
    assert sum(forward for forward, _ in backend.moves) == pytest.approx(1.2)
    assert harness.refresh()["local_odometry"]["translation_m"] == pytest.approx([1.056, 0.])


def test_calibration_and_completion_requirements_only_expose_public_schema():
    backend = RecordingBackend()
    backend.sensor_calibration = {
        "camera_frame": "front_rgbd_optical", "body_frame": "base",
        "camera_position_in_body_m": [0.32, 0., 0.08],
        "camera_optical_to_body_rotation": [[0., 0., 1.], [-1., 0., 0.], [0., -1., 0.]],
        "optical_axes": "x right, y down, z forward", "body_axes": "x forward, y left, z up",
        "camera_to_world": [[99.]], "target_position": [99., 99.],
    }
    backend.public_task_spec = {
        "goal_kind": "passage", "reference_body": "base", "required_clearance_m": 0.8,
        "stop_required": True, "collision_free_required": True,
        "standoff_m": 1., "distance_tolerance_m": 0.18, "heading_tolerance_rad": 0.1,
        "max_stopped_speed_mps": 0.03, "max_stopped_yaw_rate_radps": 0.05,
        "passage_x": 2.2, "finish_x_min": 3., "success": True,
        "target_position": [99., 99.],
    }
    observation = Harness(backend, "Go through the visible opening.").observation()
    assert observation["sensor_calibration"] == {
        key: value for key, value in backend.sensor_calibration.items()
        if key not in {"camera_to_world", "target_position"}
    }
    assert observation["completion_requirements"] == {
        key: value for key, value in backend.public_task_spec.items()
        if key not in {"passage_x", "finish_x_min", "success", "target_position"}
    }
    encoded = json.dumps(observation, allow_nan=False)
    for private_field in ("target_position", "camera_to_world", "passage_x", "finish_x_min", '"success"'):
        assert private_field not in encoded
    observation["sensor_calibration"]["camera_position_in_body_m"][0] = 99.
    assert backend.sensor_calibration["camera_position_in_body_m"][0] == 0.32
    assert backend.evaluations == 0


@pytest.mark.parametrize("invalid,valid_calibration", [
    (True, False), (float("nan"), False), (float("inf"), False),
    (-0.1, True), ("0.8", False), ({"target_position": [99., 99.]}, False),
])
def test_malformed_public_requirements_do_not_enter_observation(invalid, valid_calibration):
    backend = RecordingBackend()
    backend.public_task_spec = {"required_clearance_m": invalid, "stop_required": "yes"}
    backend.sensor_calibration = {
        "camera_position_in_body_m": [0.32, invalid, 0.08],
        "camera_optical_to_body_rotation": [[1., 0., 0.], [0., invalid, 0.], [0., 0., 1.]],
        "body_frame": {"target_position": [99., 99.]},
    }
    observation = Harness(backend, "Go through the visible opening.").observation()
    assert "completion_requirements" not in observation
    if valid_calibration:
        # Negative coordinates are valid static mount/rotation coefficients.
        assert "sensor_calibration" in observation
    else:
        assert "sensor_calibration" not in observation

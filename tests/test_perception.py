"""Sensor geometry tests use synthetic RGB-D, never a simulator target pose."""

import math

import numpy as np
import pytest

from go2_demo.perception import PerceptionError, PointTracker, backproject, relative_xy
from go2_demo.types import SensorFrame


def make_frame(frame_id="frame-1", *, yaw=0.0, pitch=0.0, base_xy=(0.0, 0.0), depth=2.0):
    # Camera optical coordinates: right, down, forward. World: forward, left, up.
    optical_to_body = np.array([[0., 0., 1.], [-1., 0., 0.], [0., -1., 0.]])
    cy, sy = math.cos(yaw), math.sin(yaw)
    cp, sp = math.cos(pitch), math.sin(pitch)
    yaw_rotation = np.array([[cy, -sy, 0.], [sy, cy, 0.], [0., 0., 1.]])
    pitch_rotation = np.array([[cp, 0., -sp], [0., 1., 0.], [sp, 0., cp]])
    transform = np.eye(4)
    transform[:3, :3] = yaw_rotation @ pitch_rotation @ optical_to_body
    transform[:3, 3] = [*base_xy, 0.4]
    rng = np.random.default_rng(9)
    rgb = rng.integers(0, 256, (80, 100, 3), dtype=np.uint8)
    return SensorFrame(
        frame_id=frame_id, sim_time_s=0.0, rgb=rgb,
        depth_m=np.full((80, 100), depth, dtype=np.float32),
        intrinsics=np.array([[100., 0., 50.], [0., 100., 40.], [0., 0., 1.]]),
        camera_to_world=transform, base_xy_yaw=np.array([*base_xy, yaw]),
        robot_state={"body_height_m": 0.4},
    )


def test_optical_depth_is_z_and_image_right_is_robot_right():
    frame = make_frame()
    world = backproject(frame, 60.0, 30.0)
    np.testing.assert_allclose(world, [2.0, -0.2, 0.6], atol=1e-8)
    np.testing.assert_allclose(relative_xy(frame, world), [2.0, -0.2], atol=1e-8)


def test_heading_frame_removes_world_translation_and_yaw():
    frame = make_frame(yaw=math.pi / 2, base_xy=(1.0, 2.0))
    world = backproject(frame, 50.0, 40.0)
    np.testing.assert_allclose(world, [1.0, 4.0, 0.4], atol=1e-8)
    np.testing.assert_allclose(relative_xy(frame, world), [2.0, 0.0], atol=1e-8)


def test_pitch_changes_horizontal_range_without_tilting_motion_frame():
    frame = make_frame(pitch=math.pi / 6)
    world = backproject(frame, 50.0, 40.0)
    np.testing.assert_allclose(world, [math.sqrt(3), 0.0, 1.4], atol=1e-8)
    np.testing.assert_allclose(relative_xy(frame, world), [math.sqrt(3), 0.0], atol=1e-8)


@pytest.mark.parametrize("depth", [0.0, 0.079, 12.01, float("nan"), float("inf")])
def test_unusable_depth_cannot_become_a_tracked_position(depth):
    tracker = PointTracker()
    tracker.update(make_frame(depth=depth))
    with pytest.raises(PerceptionError, match="depth"):
        tracker.add("frame-1", 50.0, 40.0)
    assert tracker.geometry() == []


@pytest.mark.parametrize("uv", [(-1.0, 40.0), (100.0, 40.0), (50.0, 80.0), (float("nan"), 40.0)])
def test_out_of_frame_point_is_rejected(uv):
    with pytest.raises(PerceptionError):
        backproject(make_frame(), *uv)


def test_old_image_selection_is_rejected_without_mutating_tracks():
    tracker = PointTracker()
    tracker.update(make_frame("frame-1"))
    tracker.update(make_frame("frame-2"))
    with pytest.raises(PerceptionError, match="STALE_IMAGE"):
        tracker.add("frame-1", 50.0, 40.0)
    assert tracker.geometry() == []


def test_lost_depth_removes_metric_feedback_instead_of_reusing_old_position(monkeypatch):
    tracker = PointTracker()
    tracker.update(make_frame())
    tracker.add("frame-1", 50.0, 40.0)

    def stationary_flow(previous_image, current_image, points, unused, **kwargs):
        return points.copy(), np.ones((len(points), 1), np.uint8), np.zeros((len(points), 1), np.float32)

    monkeypatch.setattr("go2_demo.perception.cv2.calcOpticalFlowPyrLK", stationary_flow)
    tracker.update(make_frame("frame-2", depth=float("nan")))
    point = tracker.geometry()[0]
    assert point["valid"] is False
    assert point["relative_xy_m"] is None
    assert point["range_m"] is None
    assert point["bearing_rad"] is None
    assert point["confidence"] == 0.0
    assert point["image_id"] == "frame-2"


def test_geometry_feedback_exposes_relative_measurements_not_world_pose():
    tracker = PointTracker()
    tracker.update(make_frame(base_xy=(100.0, 200.0)))
    point = tracker.add("frame-1", 50.0, 40.0)
    assert point["relative_xy_m"] == [2.0, 0.0]
    assert "world" not in point
    assert "camera_to_world" not in point
    assert "base_xy_yaw" not in point



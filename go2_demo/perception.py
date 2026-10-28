"""RGB-D point tracking. No task labels, target poses or simulator object IDs enter here."""

from dataclasses import dataclass
import math

import cv2
import numpy as np

from .types import SensorFrame


class PerceptionError(ValueError):
    pass


def backproject(frame: SensorFrame, u: float, v: float) -> np.ndarray:
    """Use optical-z depth; return a world point internally (never exposed to the model)."""
    h, w = frame.depth_m.shape
    if not (math.isfinite(u) and math.isfinite(v) and 0 <= u < w and 0 <= v < h):
        raise PerceptionError("Pixel outside the current image")
    x, y = int(round(u)), int(round(v))
    x, y = min(x, w - 1), min(y, h - 1)
    depth = float(frame.depth_m[y, x])
    if not math.isfinite(depth) or not 0.08 <= depth <= 12.0:
        raise PerceptionError("No usable depth at the selected pixel")
    ray = np.linalg.solve(frame.intrinsics, np.array([u, v, 1.0]))
    point = frame.camera_to_world @ np.r_[ray * depth, 1.0]
    if not np.isfinite(point).all():
        raise PerceptionError("Invalid camera calibration")
    return point[:3]


def relative_xy(frame: SensorFrame, world: np.ndarray) -> np.ndarray:
    x, y, yaw = frame.base_xy_yaw
    dx, dy = world[:2] - [x, y]
    return np.array([math.cos(yaw) * dx + math.sin(yaw) * dy,
                     -math.sin(yaw) * dx + math.cos(yaw) * dy])


@dataclass
class TrackedPoint:
    point_id: str
    pixel: np.ndarray
    world: np.ndarray
    valid: bool = True
    confidence: float = 1.0
    reason: str | None = None


class PointTracker:
    """Sparse LK tracking between decision frames, with explicit loss instead of oracle recovery."""

    def __init__(self, max_points: int = 8):
        self.max_points = max_points
        self.frame: SensorFrame | None = None
        self.gray: np.ndarray | None = None
        self.points: dict[str, TrackedPoint] = {}
        self.counter = 0

    def update(self, frame: SensorFrame) -> None:
        gray = cv2.cvtColor(frame.rgb, cv2.COLOR_RGB2GRAY)
        active = [p for p in self.points.values() if p.valid]
        if self.frame is not None and self.gray is not None and active:
            if frame.frame_id == self.frame.frame_id:
                return
            previous = np.array([p.pixel for p in active], np.float32).reshape(-1, 1, 2)
            params = dict(winSize=(31, 31), maxLevel=3,
                          criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))
            try:
                current, status, _ = cv2.calcOpticalFlowPyrLK(self.gray, gray, previous, None, **params)
                if current is None:
                    raise ValueError("No flow")
                backward, back_status, _ = cv2.calcOpticalFlowPyrLK(gray, self.gray, current, None, **params)
                if backward is None:
                    raise ValueError("No reverse flow")
                for i, point in enumerate(active):
                    if not status[i, 0] or not back_status[i, 0]:
                        self._lose(point, "optical_flow_lost")
                        continue
                    error = float(np.linalg.norm(previous[i] - backward[i]))
                    if not math.isfinite(error) or error > 1.5:
                        self._lose(point, "inconsistent_flow")
                        continue
                    uv = current[i, 0]
                    try:
                        world = backproject(frame, float(uv[0]), float(uv[1]))
                    except PerceptionError:
                        self._lose(point, "invalid_depth_or_out_of_view")
                        continue
                    # This demo tracks static scene points. Reject depth jumps / occluders.
                    if float(np.linalg.norm(world - point.world)) > 0.25:
                        self._lose(point, "geometry_jump")
                        continue
                    point.pixel = uv.copy()
                    point.world = world
                    point.confidence = max(0.0, 1.0 - error / 1.5)
            except (ValueError, cv2.error):
                for point in active:
                    self._lose(point, "optical_flow_lost")
        self.frame, self.gray = frame, gray

    @staticmethod
    def _lose(point: TrackedPoint, reason: str) -> None:
        point.valid, point.confidence, point.reason = False, 0.0, reason

    def add(self, image_id: str, u: float, v: float) -> dict:
        if self.frame is None or self.frame.frame_id != image_id:
            raise PerceptionError("STALE_IMAGE: select a pixel in the latest image_id")
        world = backproject(self.frame, u, v)
        if len(self.points) >= self.max_points:
            lost = next((k for k, p in self.points.items() if not p.valid), None)
            if lost is None:
                raise PerceptionError("Maximum tracked points reached")
            del self.points[lost]
        self.counter += 1
        point = TrackedPoint(f"point-{self.counter:03d}", np.array([u, v], np.float32), world)
        self.points[point.point_id] = point
        return self.describe(point)

    def describe(self, point: TrackedPoint) -> dict:
        assert self.frame is not None
        xy = relative_xy(self.frame, point.world) if point.valid else None
        return {
            "point_id": point.point_id,
            "image_id": self.frame.frame_id,
            "timestamp_s": self.frame.sim_time_s,
            "valid": point.valid,
            "pixel_uv": [round(float(x), 2) for x in point.pixel] if point.valid else None,
            "relative_xy_m": [round(float(x), 4) for x in xy] if xy is not None else None,
            "range_m": round(float(np.linalg.norm(xy)), 4) if xy is not None else None,
            "bearing_rad": round(math.atan2(float(xy[1]), float(xy[0])), 4) if xy is not None else None,
            "confidence": round(point.confidence, 3),
            "loss_reason": point.reason,
            "source": "rgbd_optical_flow",
        }

    def geometry(self) -> list[dict]:
        return [self.describe(p) for p in self.points.values()]



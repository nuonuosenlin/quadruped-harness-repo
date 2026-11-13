"""Task-given color labels + public RGB-D, never a generic semantic detector.

No scene/object IDs, world transforms, simulator base pose or motion GT are read.
Candidates are proposals; only current valid tool-tracked points can promote a
task object, and MemoryRules still requires independent high-confidence frames.
"""

from copy import deepcopy
import math

import cv2
import numpy as np


def task_targets(task_id):
    if task_id != "memory_ab_occluded_v1":
        return []
    # This is the public task identity contract, deliberately without positions.
    return [{"object_id": "task:A", "task_label": "A", "description": "蓝球", "color": "blue"},
            {"object_id": "task:B", "task_label": "B", "description": "绿方块", "color": "green"}]


def _mask(rgb, color):
    data = np.asarray(rgb, dtype=float)
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    if color == "blue":
        return (b > 1.5 * r) & (b > 1.3 * g) & (b > 50)
    if color == "green":
        return (g > 1.5 * r) & (g > 1.4 * b) & (g > 50)
    return np.zeros(rgb.shape[:2], dtype=bool)


class TaskLabelRGBD:
    def __init__(self, labels=()):
        self.labels = deepcopy(list(labels))

    def inspect(self, observation, rgb=None, depth_m=None, intrinsics=None):
        """Return bounded public data plus private pixel masks for association."""
        view = {"image_id": observation["image_id"], "image_size": deepcopy(observation["image_size"]),
                "tracked_points": deepcopy(observation.get("tracked_points", [])),
                "sensor_calibration": deepcopy(observation.get("sensor_calibration", {})),
                "completion_requirements": deepcopy(observation.get("completion_requirements", {})),
                "target_candidates": [], "source": "current_public_rgbd_and_tool_geometry"}
        masks = {}
        if (rgb is None or depth_m is None or intrinsics is None
                or np.shape(rgb)[:2] != np.shape(depth_m) or np.shape(intrinsics) != (3, 3)):
            return view, masks
        if not np.isfinite(intrinsics).all() or abs(float(np.linalg.det(intrinsics))) < 1e-12:
            return view, masks
        for label in self.labels:
            mask = _mask(rgb, label["color"])
            count, components, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
            usable = [i for i in range(1, count) if stats[i, cv2.CC_STAT_AREA] >= 12]
            # More than one object of the same task color is ambiguous.
            if len(usable) != 1:
                continue
            component = components == usable[0]
            valid_depth = component & np.isfinite(depth_m) & (depth_m >= .08) & (depth_m <= 12.)
            pixels = np.argwhere(valid_depth)
            if len(pixels) < 8:
                continue
            middle = np.median(pixels, axis=0)
            v, u = pixels[np.argmin(np.linalg.norm(pixels - middle, axis=1))]
            # Prefer a trackable visible corner over a textureless color centre.
            corners = cv2.goodFeaturesToTrack(cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY),
                maxCorners=8, qualityLevel=.03, minDistance=3, mask=valid_depth.astype(np.uint8) * 255)
            if corners is not None:
                uv = corners.reshape(-1, 2)
                chosen = uv[np.argmin(np.linalg.norm(uv - middle[::-1], axis=1))]
                u, v = int(round(float(chosen[0]))), int(round(float(chosen[1])))
            xyz = np.linalg.solve(intrinsics, np.array([float(u), float(v), 1.])) * float(depth_m[v, u])
            if not np.isfinite(xyz).all():
                continue
            candidate = {**deepcopy(label), "image_id": observation["image_id"],
                         "pixel_uv": [int(u), int(v)], "camera_xyz_m": xyz.tolist(),
                         "coordinate_frame": "current_camera_optical", "status": "candidate_not_confirmed",
                         "identity_basis": "unique_visible_component_matching_task_given_color",
                         "source": "task_label_color_rgbd_v1", "requires": "track_point_then_independent_frame"}
            view["target_candidates"].append(candidate)
            masks[label["object_id"]] = component
        return view, masks

    def associate(self, point, view, masks, depth_m=None, intrinsics=None):
        if not point.get("valid") or point.get("image_id") != view["image_id"]:
            return None
        pixel = point.get("pixel_uv")
        if not isinstance(pixel, (list, tuple)) or len(pixel) != 2:
            return None
        if not all(isinstance(x, (float, int)) and math.isfinite(x) for x in pixel):
            return None
        u, v = (int(round(float(x))) for x in pixel)
        for candidate in view["target_candidates"]:
            mask = masks[candidate["object_id"]]
            if 0 <= v < mask.shape[0] and 0 <= u < mask.shape[1] and mask[v, u]:
                if depth_m is None or intrinsics is None:
                    return None
                depth = float(depth_m[v, u])
                if not math.isfinite(depth) or not .08 <= depth <= 12.:
                    return None
                xyz = np.linalg.solve(intrinsics, np.array([float(u), float(v), 1.])) * depth
                return {**deepcopy(candidate), "pixel_uv": [u, v], "camera_xyz_m": xyz.tolist()}
        return None

"""Whitelisted synchronous tools. No task planning or hidden-target access."""

from copy import deepcopy
import json
import math

from .perception import PerceptionError, PointTracker
from .types import ToolCall


def _tool(name, description, properties=None, required=None):
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": properties or {},
                       "required": required or [], "additionalProperties": False}}}


TOOLS = [
    _tool("observe", "Get a new camera observation; no movement."),
    _tool("track_point", "Select a static visible point in the latest RGB image. Pixels use origin top-left, u right, v down. Depth gives geometry at the selected pixel, not semantic object identity. Valid tracked points update automatically after motion; lost points have null current geometry. Select a reliable visible feature, not empty background.",
          {"image_id": {"type": "string"}, "u": {"type": "number"}, "v": {"type": "number"}}, ["image_id", "u", "v"]),
    _tool("get_geometry", "Read current tracked points. Invalid points have no current metric position; reselect if needed."),
    _tool("move_relative", "Command a displacement in the base horizontal frame at action start: forward positive, left positive, metres; length at most 0.6 m. The command is a target, not measured travel. Settling starts within 0.06 m of the target; final acceptance tolerance is 0.10 m, so a very small command can succeed with almost no motion. Use result.measured.translation_start_frame_m and observation.local_odometry to measure progress; do not sum requested distances. No path planning or obstacle avoidance.",
          {"forward_m": {"type": "number"}, "lateral_m": {"type": "number"}}, ["forward_m", "lateral_m"]),
    _tool("turn", "Relative yaw in radians, positive left. Absolute angle at most 0.6 rad.",
          {"yaw_rad": {"type": "number"}}, ["yaw_rad"]),
    _tool("stop", "Set locomotion commands to zero and let the controller settle."),
    _tool("finish", "Declare the task finished only after verifying the task and public completion_requirements using current geometry and measured body progress. The camera image alone does not prove that the base has crossed or cleared a passage. Independent evaluation decides success."),
    _tool("abort", "Stop the episode without claiming success.", {"reason": {"type": "string"}}, ["reason"]),
]

_ROBOT_FIELDS = {"body_height_m", "body_pitch_rad", "body_roll_rad", "speed_mps",
                 "yaw_rate_radps", "fallen", "motion_state", "linear_velocity_mps",
                 "angular_velocity_radps", "posture_control_supported"}

_CALIBRATION_TEXT_FIELDS = {"camera_frame", "body_frame", "optical_axes", "body_axes"}
_COMPLETION_TEXT_FIELDS = {"goal_kind", "reference_body"}
_COMPLETION_BOOL_FIELDS = {"stop_required", "collision_free_required"}
_COMPLETION_NUMBER_FIELDS = {
    "required_clearance_m", "standoff_m", "distance_tolerance_m",
    "heading_tolerance_rad", "max_stopped_speed_mps", "max_stopped_yaw_rate_radps",
}


def _finite_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _public_calibration(value) -> dict:
    """Copy the supported calibration schema without arbitrary backend metadata."""
    if not isinstance(value, dict):
        return {}
    result = {key: item for key, item in value.items()
              if key in _CALIBRATION_TEXT_FIELDS and isinstance(item, str)}
    position = value.get("camera_position_in_body_m")
    if isinstance(position, (list, tuple)) and len(position) == 3 and all(_finite_number(x) for x in position):
        result["camera_position_in_body_m"] = [float(x) for x in position]
    rotation = value.get("camera_optical_to_body_rotation")
    if (isinstance(rotation, (list, tuple)) and len(rotation) == 3
            and all(isinstance(row, (list, tuple)) and len(row) == 3
                    and all(_finite_number(x) for x in row) for row in rotation)):
        result["camera_optical_to_body_rotation"] = [[float(x) for x in row] for row in rotation]
    return result


def _public_completion_requirements(value) -> dict:
    """Expose declared tolerances, never gate locations or evaluator state."""
    if not isinstance(value, dict):
        return {}
    return {key: float(item) if key in _COMPLETION_NUMBER_FIELDS else item
            for key, item in value.items()
            if ((key in _COMPLETION_TEXT_FIELDS and isinstance(item, str))
                or (key in _COMPLETION_BOOL_FIELDS and isinstance(item, bool))
                or (key in _COMPLETION_NUMBER_FIELDS and _finite_number(item) and item >= 0))}


class Harness:
    def __init__(self, backend, task: str):
        self.backend, self.task = backend, task
        self.tracker = PointTracker()
        self.frame = None
        self._initial_base_xy_yaw: tuple[float, float, float] | None = None
        self.termination: str | None = None
        self.cache: dict[str, tuple[str, dict]] = {}
        self.refresh()

    def refresh(self) -> dict:
        self.frame = self.backend.capture()
        if self._initial_base_xy_yaw is None:
            self._initial_base_xy_yaw = tuple(float(x) for x in self.frame.base_xy_yaw)
        self.tracker.update(self.frame)
        return self.observation()

    def observation(self) -> dict:
        frame = self.frame
        initial_x, initial_y, initial_yaw = self._initial_base_xy_yaw
        x, y, yaw = (float(value) for value in frame.base_xy_yaw)
        dx, dy = x - initial_x, y - initial_y
        c, s = math.cos(initial_yaw), math.sin(initial_yaw)
        yaw_delta = yaw - initial_yaw
        observation = {"task": self.task, "image_id": frame.frame_id,
                "sim_time_s": frame.sim_time_s,
                "image_size": {"width": frame.rgb.shape[1], "height": frame.rgb.shape[0]},
                "coordinate_convention": "tracked_points.relative_xy_m: origin at the current base body reference, horizontal forward and left axes, metres; yaw positive left. local_odometry: origin and horizontal axes fixed at the episode-start base body reference.",
                "local_odometry": {
                    "translation_m": [c * dx + s * dy, -s * dx + c * dy],
                    "yaw_rad": math.atan2(math.sin(yaw_delta), math.cos(yaw_delta)),
                    "reference": "episode_start_body_horizontal",
                    "source": "simulated_proprioception",
                },
                "robot_state": {k: v for k, v in frame.robot_state.items() if k in _ROBOT_FIELDS},
                "tracked_points": self.tracker.geometry(),
                "capabilities": {"planar_motion": True, "height_pitch_control": False},
                "simulation_mode": "paused_during_model_inference"}
        calibration = _public_calibration(getattr(self.backend, "sensor_calibration", None))
        if calibration:
            observation["sensor_calibration"] = calibration
        requirements = _public_completion_requirements(getattr(self.backend, "public_task_spec", None))
        if requirements:
            observation["completion_requirements"] = requirements
        return observation

    @staticmethod
    def _result(call, status="succeeded", **kwargs):
        return {"call_id": call.call_id, "tool": call.name, "status": status, **kwargs}

    @staticmethod
    def _validate(call: ToolCall) -> None:
        if not isinstance(call.call_id, str) or not 0 < len(call.call_id) <= 200:
            raise ValueError("Invalid call_id")
        if not isinstance(call.arguments, dict):
            raise ValueError("Arguments must be an object")
        specs = {t["function"]["name"]: t["function"]["parameters"] for t in TOOLS}
        if call.name not in specs:
            raise ValueError("Unknown or unsupported tool")
        spec = specs[call.name]
        if set(call.arguments) != set(spec["required"]):
            raise ValueError("Arguments must match exactly: " + ", ".join(spec["required"]))
        for name, rule in spec["properties"].items():
            value = call.arguments[name]
            if rule["type"] == "number":
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                    raise ValueError(f"{name} must be a finite number")
            elif not isinstance(value, str) or not 0 < len(value) <= 300:
                raise ValueError(f"{name} must be a nonempty string of at most 300 characters")
        if call.name == "move_relative" and math.hypot(call.arguments["forward_m"], call.arguments["lateral_m"]) > 0.6:
            raise ValueError("Translation length exceeds 0.6 m")
        if call.name == "turn" and abs(call.arguments["yaw_rad"]) > 0.6:
            raise ValueError("Yaw exceeds 0.6 rad")

    def dispatch_many(self, calls: list[ToolCall]) -> list[dict]:
        if len(calls) != 1:
            return [self._result(c, "failed", error_code="ONE_TOOL_PER_TURN",
                                 message="No calls executed. Request exactly one tool per turn.") for c in calls]
        return [self.dispatch(calls[0])]

    def dispatch(self, call: ToolCall) -> dict:
        if self.termination is not None:
            return self._result(call, "failed", error_code="EPISODE_ENDED")
        if call.name == "set_posture":
            return self._result(call, "failed", error_code="UNSUPPORTED_CAPABILITY",
                                message="The installed policy only supports planar velocity commands.")
        try:
            self._validate(call)
            fingerprint = json.dumps([call.name, call.arguments], sort_keys=True, allow_nan=False)
        except (ValueError, TypeError, OverflowError) as exc:
            return self._result(call, "failed", error_code="INVALID_ARGUMENTS", message=str(exc))
        if call.call_id in self.cache:
            old, result = self.cache[call.call_id]
            if old != fingerprint:
                return self._result(call, "failed", error_code="CALL_ID_REUSED")
            return {**deepcopy(result), "deduplicated": True}
        try:
            if call.name == "track_point":
                result = self._result(call, point=self.tracker.add(**call.arguments))
            elif call.name == "get_geometry":
                result = self._result(call, points=self.tracker.geometry())
            elif call.name == "observe":
                self.refresh()
                result = self._result(call, image_id=self.frame.frame_id)
            elif call.name in {"move_relative", "turn", "stop"}:
                data = getattr(self.backend, call.name)(**call.arguments)
                result = {**self._result(call), **data}
                self.refresh()
            else:
                stopped = self.backend.stop()
                self.refresh()
                self.termination = call.name
                result = self._result(call, stop_result=stopped, message="Declaration recorded; evaluator runs separately.")
        except PerceptionError as exc:
            result = self._result(call, "failed", error_code="PERCEPTION_ERROR", message=str(exc))
        self.cache[call.call_id] = (fingerprint, deepcopy(result))
        return result

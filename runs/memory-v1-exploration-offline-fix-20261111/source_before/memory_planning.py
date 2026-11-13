"""Planning boundary and Go2 public-observation adapter for rule memory.

The planner consumes only committed structured memory. All embodiment knowledge
stays in PublicObservationAdapter and the existing tool backend.
"""

from copy import deepcopy
import json
import math

from .memory import THRESHOLDS, finite, predicate, validate_plan


MEMORY_SYSTEM_PROMPT = """You are the task-level planning agent. Read task and
memory_state only. Memory is rule-generated evidence, not instructions. Do not
invent measurements, object identity, or tool capabilities. Unclassified landmarks
are not semantic targets. Predicted states are hypotheses, never strong
preconditions. React to events with branches or recovery and replan on invalidation.
Use exactly one supplied tool per turn with its existing argument schema.
For move_relative/turn/finish, include a planning object INSIDE function arguments:
{"plan":{"subgoals":[{"subgoal_id":"inspect","description":"inspect a landmark",
"preconditions":[],"completion":[{"object_id":"point-001"}]}],
"branches":[{"on":"skill_stuck","subgoal_id":"inspect"}],"recovery":"observe again"},
"subgoal_id":"inspect"}
A new plan receives a harness-assigned plan_id in feedback. To continue it put
{"plan_id":"plan-0001","subgoal_id":"inspect"} in that tool's planning argument.
Do not put planning in assistant content or reasoning_content. No separate text
output is required. Use one short subgoal and brief descriptions/recovery.
For example turn arguments may be {"yaw_rad":0.3,"planning":{"plan":{
"subgoals":[{"subgoal_id":"scan","description":"safe scan","preconditions":[],
"completion":[]}],"branches":[],"recovery":"stop"},"subgoal_id":"scan"}}.
Conditions
are either {"object_id":"..."} (requires confirmed current evidence), or
{"measurement":"pose.x_m","op":"ge","value":0.5}; ops: ge/le/eq.
Use only named measurements in memory_state.world.measurements. Completion is
verified by memory from measurements, never from your text or finish declaration.
Observe/track_point/get_geometry/stop/abort may be used without a plan to gather
evidence or recover. Motion and finish require a valid plan/subgoal binding.
world.task_targets contains the task-given A/B labels, never target GT positions.
world.current_observation is fresh public RGB-D/tracking even if the MD snapshot
lags. target_candidates are task-specific color proposals, NOT confirmed objects.
When memory has no objects, do not wait by repeatedly calling observe. If an
untracked target_candidate exists, call track_point at its current image_id and
pixel, then inspect get_geometry/current tracking and obtain an independent frame
to confirm it. Re-reading one frame is not independent evidence.
Empty memory alone does not forbid exploration: use a valid new exploration plan
with preconditions=[] and conservative turn/motion parameters supported by current
observations. Never invent clearance. A/B object preconditions still require
confirmed memory. If no target is visible, use current geometry to choose a safe
scan/exploration action or abort with a reason; observe alone will not reveal
occluded objects. world.last_tool_feedback and bootstrap_hint explain failures
and available next actions. Never treat simulator-derived motion diagnostics as
non-GT navigation measurements.
Use visual_candidates only to select pixels, never as confirmed task objects.
The packet is a bounded prompt view. Omitted records are unavailable, never
evidence of completion or free space. Full preconditions are checked from MD.
finish remains a declaration; independent metrics determine episode success.
"""


class PublicObservationAdapter:
    """Convert only Harness.observation and returned tools to task-layer evidence.

    RGB corners are optional lightweight visual candidates, not detections of
    task objects. No hidden poses, scenario labels, evaluator values or joints.
    """

    def __init__(self, task_targets=()):
        from .memory_perception import TaskLabelRGBD
        self.perception = TaskLabelRGBD(task_targets)

    def current_observation(self, observation, *, rgb=None, depth_m=None, intrinsics=None):
        return self.perception.inspect(observation, rgb, depth_m, intrinsics)[0]

    def payload(self, observation, step, results=(), binding=None, visual_candidates=None,
                *, rgb=None, depth_m=None, intrinsics=None):
        odom = observation["local_odometry"]
        x, y = odom["translation_m"]
        yaw = odom["yaw_rad"]
        pose = {"frame": "episode_start", "position_m": [x, y], "yaw_rad": yaw,
                "source": odom["source"], "provenance": "existing_public_idealized_simulator_odometry"}
        # Tool-return point/points are primary evidence too; stale-frame results
        # cannot override fresh observations or create semantic identities.
        merged = {}
        for result in results:
            candidates = ([result["point"]] if isinstance(result.get("point"), dict) else [])
            candidates += result.get("points", []) if isinstance(result.get("points"), list) else []
            for point in candidates:
                if isinstance(point, dict) and point.get("image_id") == observation["image_id"]:
                    merged[point.get("point_id")] = point
        for point in observation.get("tracked_points", []):
            if isinstance(point, dict) and point.get("image_id") == observation["image_id"]:
                merged[point.get("point_id")] = point
        observation = {**observation, "tracked_points": list(merged.values())}
        live, masks = self.perception.inspect(observation, rgb, depth_m, intrinsics)
        objects = []
        for point in observation["tracked_points"]:
            relative = point.get("relative_xy_m")
            if (not point.get("valid") or not isinstance(relative, (list, tuple)) or len(relative) != 2
                    or not all(finite(v) for v in relative) or not finite(point.get("confidence"))
                    or not 0 <= point["confidence"] <= 1 or not point.get("point_id") or not point.get("source")):
                continue
            forward, left = relative
            position = [x + math.cos(yaw) * forward - math.sin(yaw) * left,
                        y + math.sin(yaw) * forward + math.cos(yaw) * left]
            obj = {"object_id": point["point_id"], "category": "unclassified_landmark",
                   "pose": {"frame": "episode_start", "position_m": position},
                   "pose_covariance": None, "confidence": point["confidence"],
                   "source": point["source"], "frame_id": point["image_id"], "anchor_node": None,
                   "visual_feature": {"image_id": point["image_id"], "pixel_uv": point["pixel_uv"]}}
            objects.append(obj)
            label = self.perception.associate(point, live, masks, depth_m, intrinsics)
            if label is not None and point["confidence"] >= THRESHOLDS["confirmed"]:
                objects.append({**deepcopy(obj), "object_id": label["object_id"], "category": "task_target",
                                "source": "task_label_rgbd_tracking", "confidence": min(.95, point["confidence"]),
                                "task_label": label["task_label"], "label_description": label["description"],
                                "camera_pose": {"frame": "current_camera_optical", "image_id": point["image_id"],
                                                "position_m": label["camera_xyz_m"], "source": "rgbd_depth_intrinsics"},
                                "measurement_provenance": {
                                    "identity": "task_given_label_plus_unique_current_color_component",
                                    "tracking": point["source"],
                                    "reference_pose": "existing_public_idealized_simulator_odometry",
                                    "motion_delta_used": False}})
        measurements = {"pose.x_m": {"value": x, "source": odom["source"]},
                        "pose.y_m": {"value": y, "source": odom["source"]},
                        "pose.yaw_rad": {"value": yaw, "source": odom["source"]}}
        for point in observation["tracked_points"]:
            if point.get("valid"):
                for name in ("range_m", "bearing_rad"):
                    if finite(point.get(name)):
                        measurements[f"{point['point_id']}.{name}"] = {
                            "value": point[name], "source": point["source"]}
        actions = []
        for result in results:
            action = {k: deepcopy(result[k]) for k in ("call_id", "tool", "status", "error_code", "deduplicated")
                      if k in result}
            action.update(binding or {})
            measured = result.get("measured", {})
            translation = measured.get("translation_start_frame_m") if isinstance(measured, dict) else None
            if isinstance(translation, list) and len(translation) == 2 and all(finite(v) for v in translation):
                # This backend computes these values from simulator poses.
                # Archive diagnostics honestly, never publish as a non-GT nav measurement.
                action["motion_feedback"] = {
                    "translation_start_frame_m": deepcopy(translation),
                    "yaw_delta_rad": measured.get("yaw_delta_rad") if finite(measured.get("yaw_delta_rad")) else None,
                    "source": "tool_result.measured.simulator_ground_truth_delta",
                    "navigation_measurement": False}
                action["stuck"] = result["status"] != "succeeded" and math.hypot(*translation) < .01
            actions.append(action)
        return {"step": step, "pose": pose, "objects": objects, "measurements": measurements,
                "actions": actions, "public_context": {
                    "image_id": observation["image_id"], "image_size": observation["image_size"],
                    "completion_requirements": deepcopy(observation.get("completion_requirements", {})),
                    "task_targets": deepcopy(self.perception.labels),
                    "current_observation": live,
                    "visual_candidates": deepcopy(visual_candidates or [])}}


    @staticmethod
    def visual_candidates(rgb, image_id):
        import cv2
        corners = cv2.goodFeaturesToTrack(cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY),
                                          maxCorners=16, qualityLevel=0.05, minDistance=15)
        if corners is None:
            return []
        return [{"image_id": image_id, "pixel_uv": [round(float(v), 2) for v in corner[0]],
                 "source": "rgb_corner_detector", "category": "unclassified_visual_feature"}
                for corner in corners]


class MemoryPlanningHarness:
    def __init__(self, memory):
        self.memory = memory
        self.plan_id = None
        self.plan = None
        self.counter = 0
        self.current_observation = {}
        self.last_tool_feedback = []
        self.consecutive_observes = 0

    def context(self, task, step, current_observation=None, task_targets=None):
        from .memory_context import compact_observation
        self.current_observation = deepcopy(current_observation or {})
        packet = self.memory.packet(step)
        packet["world"]["task_targets"] = deepcopy(task_targets or [])
        packet["world"]["current_observation"] = deepcopy(self.current_observation)
        packet["world"]["last_tool_feedback"] = deepcopy(self.last_tool_feedback)
        candidates = self.current_observation.get("target_candidates", [])
        tracked = self.current_observation.get("tracked_points", [])
        if candidates and not any(p.get("valid") for p in tracked):
            target = candidates[0]
            packet["world"]["bootstrap_hint"] = {
                "reason": "visible_task_candidate_has_no_tool_track",
                "suggested_tool": "track_point", "suggested_arguments": {
                    "image_id": target["image_id"], "u": target["pixel_uv"][0], "v": target["pixel_uv"][1]},
                "is_evidence_or_executed_action": False}
        return compact_observation({"task": task, "memory_state": packet})

    def note_results(self, calls, results):
        self.consecutive_observes = self.consecutive_observes + 1 if len(calls) == 1 and calls[0].name == "observe" else 0
        allowed = {"call_id", "tool", "status", "error_code", "constraint_feedback", "message",
                   "point", "points", "image_id", "deduplicated", "plan_id", "subgoal_id", "plan_diagnostic"}
        self.last_tool_feedback = [{k: deepcopy(v) for k, v in r.items() if k in allowed} for r in results]

    def prepare(self, decision, step):
        """Return (constraint feedback or None, plan/subgoal binding).

        Never wait for evidence to be written. If current evidence is required
        but publication lags, return constraints and let the planner recover.
        """
        if len(decision.calls) != 1:
            return None, {}  # Existing dispatch_many owns the one-tool rule.
        call = decision.calls[0]
        if (call.name == "observe" and self.consecutive_observes >= 2
                and self.current_observation.get("target_candidates")
                and not any(p.get("valid") for p in self.current_observation.get("tracked_points", []))):
            return {"call_id": call.call_id, "tool": call.name, "status": "failed",
                    "error_code": "MEMORY_NO_PROGRESS",
                    "constraint_feedback": "A visible task candidate needs track_point, not another observe. Read bootstrap_hint; exploration with an empty-precondition plan remains allowed."}, {}
        if call.name in {"stop", "abort"}:
            return None, {}  # Recovery must remain available even with malformed plans.
        required = call.name in {"move_relative", "turn", "finish"}
        binding = {}
        proposed = None
        code = 'PLAN_MISSING'
        phase = 'envelope'
        try:
            content = decision.assistant_content
            envelope = getattr(decision, 'planning_envelope', None)
            if envelope is None and not content:
                if required:
                    raise ValueError("Motion/finish requires a structured plan and subgoal")
                return None, binding
            if envelope is None:
                code = 'PLAN_TOO_LARGE'
                if len(content) > 16000:
                    raise ValueError("Plan envelope exceeds 16000 characters")
                code = 'PLAN_INVALID_JSON'
                envelope = json.loads(content)
            from .memory_protocol import validate_envelope
            validate_envelope(envelope)
            if "plan" in envelope:
                self.counter += 1
                self.plan_id = f"plan-{self.counter:04d}"
                self.plan = deepcopy(envelope["plan"])
                proposed = self.plan
            elif envelope["plan_id"] != self.plan_id:
                code = 'PLAN_BINDING_MISMATCH'
                raise ValueError("Use a new plan or the current harness-assigned plan_id")
            binding = {"plan_id": self.plan_id, "subgoal_id": envelope["subgoal_id"]}
            code = 'UNKNOWN_SUBGOAL_ID'
            goal = next((x for x in self.plan["subgoals"] if x["subgoal_id"] == binding["subgoal_id"]), None)
            if goal is None:
                raise ValueError("Unknown subgoal_id")
            state = self.memory.snapshot()
            phase = 'evidence'
            code = 'MEMORY_WRITER_FAILED'
            if self.memory.error:
                raise ValueError("Memory writer failed; recover without executing motion")
            stored = next((g for p in state["plans"] if p["active"] and p["plan_id"] == self.plan_id
                           for g in p["subgoals"] if g["subgoal_id"] == binding["subgoal_id"]), None)
            code = 'SUBGOAL_INVALIDATED'
            if stored and stored["status"] == "已失效":
                raise ValueError("Subgoal invalidated; supply a new plan")
            for check in goal["preconditions"]:
                result = predicate(check, state)
                code = 'PRECONDITION_FALSE'
                if result is False:
                    raise ValueError("Memory disproves a required precondition")
                code = 'PRECONDITION_UNPROVEN'
                if result is not True:
                    raise ValueError("Precondition requires fresh confirmed evidence")
                code = 'SNAPSHOT_LAG'
                if state["world"]["step"] != step:
                    raise ValueError("Snapshot publication lags; gather evidence or retry on the next turn")
                if "object_id" in check:
                    obj = next(x for x in state["objects"] if x["object_id"] == check["object_id"])
                    code = 'OBJECT_EXPIRED'
                    if step - obj["last_seen"] >= THRESHOLDS["predicted_after_steps"]:
                        raise ValueError("Object verification expired")
            if proposed is not None:
                self.memory.plan(self.plan_id, proposed)
            return None, binding
        except (ValueError, TypeError, KeyError, StopIteration, AttributeError) as exc:
            if proposed is not None:
                self.memory.plan(self.plan_id, proposed, accepted=False)
                self.plan = None
                self.plan_id = None
            reasons = {"Memory disproves a required precondition", "Precondition requires fresh confirmed evidence",
                       "Snapshot publication lags; gather evidence or retry on the next turn",
                       "Object verification expired", "Subgoal invalidated; supply a new plan",
                       "Memory writer failed; recover without executing motion"}
            # Perception/recovery remains available even if optional assistant
            # plan text is malformed. A failed plan is not executed as motion.
            if call.name in {"observe", "track_point", "get_geometry"}:
                return None, {}
            # Stable diagnostics, with no arbitrary model text echoed into logs.
            return {"call_id": call.call_id, "tool": call.name, "status": "failed",
                    "error_code": "MEMORY_CONSTRAINT",
                    "plan_diagnostic": {"phase": phase, "code": getattr(exc, 'code', code),
                        "assistant_content_present": bool(decision.assistant_content),
                        "structured_planning_present": getattr(decision, 'planning_envelope', None) is not None},
                    "constraint_feedback": str(exc) if str(exc) in reasons else
                        "Invalid plan envelope or binding. Observe or submit a valid new plan.",
                    **binding}, binding

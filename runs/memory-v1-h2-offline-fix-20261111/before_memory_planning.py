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
Also output a JSON object as assistant content (no Markdown):
{"plan":{"subgoals":[{"subgoal_id":"inspect","description":"inspect a landmark",
"preconditions":[],"completion":[{"object_id":"point-001"}]}],
"branches":[{"on":"skill_stuck","subgoal_id":"inspect"}],"recovery":"observe again"},
"subgoal_id":"inspect"}
A new plan receives a harness-assigned plan_id in feedback. To continue it use
{"plan_id":"plan-0001","subgoal_id":"inspect"} with one tool call. Conditions
are either {"object_id":"..."} (requires confirmed current evidence), or
{"measurement":"pose.x_m","op":"ge","value":0.5}; ops: ge/le/eq.
Use only named measurements in memory_state.world.measurements. Completion is
verified by memory from measurements, never from your text or finish declaration.
Observe/track_point/get_geometry/stop/abort may be used without a plan to gather
evidence or recover. Motion and finish require a valid plan/subgoal binding.
Use visual_candidates only to select pixels, never as confirmed task objects.
finish remains a declaration; independent metrics determine episode success.
"""


class PublicObservationAdapter:
    """Convert only Harness.observation and returned tools to task-layer evidence.

    RGB corners are optional lightweight visual candidates, not detections of
    task objects. No hidden poses, scenario labels, evaluator values or joints.
    """

    def payload(self, observation, step, results=(), binding=None, visual_candidates=None):
        odom = observation["local_odometry"]
        x, y = odom["translation_m"]
        yaw = odom["yaw_rad"]
        pose = {"frame": "episode_start", "position_m": [x, y], "yaw_rad": yaw,
                "source": odom["source"]}
        objects = []
        for point in observation["tracked_points"]:
            if not point["valid"] or point["relative_xy_m"] is None:
                continue
            forward, left = point["relative_xy_m"]
            position = [x + math.cos(yaw) * forward - math.sin(yaw) * left,
                        y + math.sin(yaw) * forward + math.cos(yaw) * left]
            objects.append({"object_id": point["point_id"], "category": "unclassified_landmark",
                            "pose": {"frame": "episode_start", "position_m": position},
                            # Sensor covariance is not calibrated; never invent one.
                            "pose_covariance": None, "confidence": point["confidence"],
                            "source": point["source"], "frame_id": point["image_id"],
                            "anchor_node": None,
                            "visual_feature": {"image_id": point["image_id"], "pixel_uv": point["pixel_uv"]}})
        measurements = {"pose.x_m": {"value": x, "source": odom["source"]},
                        "pose.y_m": {"value": y, "source": odom["source"]},
                        "pose.yaw_rad": {"value": yaw, "source": odom["source"]}}
        for point in observation["tracked_points"]:
            if point["valid"]:
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
            translation = measured.get("translation_start_frame_m")
            if isinstance(translation, list) and len(translation) == 2 and all(finite(v) for v in translation):
                displacement = math.hypot(*translation)
                measurements["execution.displacement_m"] = {"value": displacement, "source": "execution_feedback"}
                # A small accepted command can legitimately have negligible travel.
                action["stuck"] = result["status"] != "succeeded" and displacement < 0.01
            actions.append(action)
        return {"step": step, "pose": pose, "objects": objects, "measurements": measurements,
                "actions": actions, "public_context": {
                    "image_id": observation["image_id"], "image_size": observation["image_size"],
                    "completion_requirements": deepcopy(observation.get("completion_requirements", {})),
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

    def context(self, task, step):
        return {"task": task, "memory_state": self.memory.packet(step)}

    def prepare(self, decision, step):
        """Return (constraint feedback or None, plan/subgoal binding).

        Never wait for evidence to be written. If current evidence is required
        but publication lags, return constraints and let the planner recover.
        """
        if len(decision.calls) != 1:
            return None, {}  # Existing dispatch_many owns the one-tool rule.
        call = decision.calls[0]
        if call.name in {"stop", "abort"}:
            return None, {}  # Recovery must remain available even with malformed plans.
        required = call.name in {"move_relative", "turn", "finish"}
        binding = {}
        proposed = None
        try:
            content = decision.assistant_content
            if not content:
                if required:
                    raise ValueError("Motion/finish requires a structured plan and subgoal")
                return None, binding
            if len(content) > 16000:
                raise ValueError("Plan envelope exceeds 16000 characters")
            envelope = json.loads(content)
            if not isinstance(envelope, dict):
                raise ValueError("Plan envelope must be a JSON object")
            if "plan" in envelope:
                if set(envelope) != {"plan", "subgoal_id"}:
                    raise ValueError("New envelope requires plan and subgoal_id")
                validate_plan(envelope["plan"])
                if envelope["subgoal_id"] not in {x["subgoal_id"] for x in envelope["plan"]["subgoals"]}:
                    raise ValueError("Unknown subgoal_id")
                self.counter += 1
                self.plan_id = f"plan-{self.counter:04d}"
                self.plan = deepcopy(envelope["plan"])
                proposed = self.plan
            elif set(envelope) != {"plan_id", "subgoal_id"} or envelope["plan_id"] != self.plan_id:
                raise ValueError("Use a new plan or the current harness-assigned plan_id")
            binding = {"plan_id": self.plan_id, "subgoal_id": envelope["subgoal_id"]}
            goal = next((x for x in self.plan["subgoals"] if x["subgoal_id"] == binding["subgoal_id"]), None)
            if goal is None:
                raise ValueError("Unknown subgoal_id")
            state = self.memory.snapshot()
            if self.memory.error:
                raise ValueError("Memory writer failed; recover without executing motion")
            stored = next((g for p in state["plans"] if p["active"] and p["plan_id"] == self.plan_id
                           for g in p["subgoals"] if g["subgoal_id"] == binding["subgoal_id"]), None)
            if stored and stored["status"] == "已失效":
                raise ValueError("Subgoal invalidated; supply a new plan")
            for check in goal["preconditions"]:
                result = predicate(check, state)
                if result is False:
                    raise ValueError("Memory disproves a required precondition")
                if result is not True:
                    raise ValueError("Precondition requires fresh confirmed evidence")
                if state["world"]["step"] != step:
                    raise ValueError("Snapshot publication lags; gather evidence or retry on the next turn")
                if "object_id" in check:
                    obj = next(x for x in state["objects"] if x["object_id"] == check["object_id"])
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
            # Stable diagnostics, with no arbitrary model text echoed into logs.
            return {"call_id": call.call_id, "tool": call.name, "status": "failed",
                    "error_code": "MEMORY_CONSTRAINT",
                    "constraint_feedback": str(exc) if str(exc) in reasons else
                        "Invalid plan envelope or binding. Observe or submit a valid new plan.",
                    **binding}, binding

"""Rule-only, embodiment-neutral memory and asynchronous Markdown publication.

Only public sensor/execution adapters may submit evidence. Model plans never
create observations or mark a subgoal complete. No LLM, simulator, or graph API.
"""

from copy import deepcopy
import json
import math
from pathlib import Path
from queue import Queue
from threading import Thread


THRESHOLDS = {"confirmed": 0.8, "predicted_after_steps": 3,
              "unknown_after_steps": 6, "stale_after_steps": 10,
              "relocation_distance_m": 0.5}
SCAN_TURN_LIMIT = 6
PACKET_KEYS = ("world", "pose", "objects", "active_beliefs", "invalidated",
               "events", "topology", "confidence_thresholds")


def encoded(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2)


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def valid_pose(pose):
    return (isinstance(pose, dict) and isinstance(pose.get("frame"), str)
            and isinstance(pose.get("position_m"), list) and len(pose["position_m"]) in (2, 3)
            and all(finite(x) for x in pose["position_m"]))


def predicate(check, state):
    """Three-valued task-layer checks: True / False / None (insufficient evidence)."""
    if "object_id" in check:
        obj = next((x for x in state["objects"] if x["object_id"] == check["object_id"]), None)
        if obj is None or obj["state"] in {"unknown", "stale"}:
            return None
        if obj["state"] == "contradicted":
            return False
        if obj["state"] != "confirmed":
            return None
        return obj["confidence"] >= state["confidence_thresholds"]["confirmed"]
    item = state.get("measurements", {}).get(check.get("measurement"))
    if not item or item["step"] != state["world"]["step"]:
        return None
    value, expected = item["value"], check["value"]
    return {"ge": value >= expected, "le": value <= expected,
            "eq": value == expected}[check["op"]]


def validate_check(check):
    if not isinstance(check, dict):
        raise ValueError("Each condition must be an object")
    if set(check) == {"object_id"} and isinstance(check["object_id"], str) and check["object_id"]:
        return
    if (set(check) == {"measurement", "op", "value"}
            and isinstance(check["measurement"], str) and check["measurement"]
            and check["op"] in {"ge", "le", "eq"} and finite(check["value"])):
        return
    raise ValueError("Condition requires object_id or measurement/op/value")


def validate_plan(plan):
    if not isinstance(plan, dict) or set(plan) != {"subgoals", "branches", "recovery"}:
        raise ValueError("Plan requires subgoals, branches, recovery")
    if (not isinstance(plan["subgoals"], list) or not 1 <= len(plan["subgoals"]) <= 32
            or not isinstance(plan["branches"], list) or len(plan["branches"]) > 32
            or not isinstance(plan["recovery"], str) or len(plan["recovery"]) > 2000):
        raise ValueError("Invalid plan size or recovery strategy")
    seen = set()
    for goal in plan["subgoals"]:
        if not isinstance(goal, dict) or set(goal) != {"subgoal_id", "description", "preconditions", "completion"}:
            raise ValueError("Subgoal requires ID, description, preconditions, completion")
        sid = goal["subgoal_id"]
        if not isinstance(sid, str) or not sid or len(sid) > 100 or sid in seen:
            raise ValueError("Subgoal IDs must be unique nonempty strings")
        seen.add(sid)
        if not isinstance(goal["description"], str) or len(goal["description"]) > 2000:
            raise ValueError("Invalid subgoal description")
        for name in ("preconditions", "completion"):
            if not isinstance(goal[name], list) or len(goal[name]) > 32:
                raise ValueError("Invalid conditions")
            for check in goal[name]:
                validate_check(check)
    for branch in plan["branches"]:
        if (not isinstance(branch, dict) or set(branch) != {"on", "subgoal_id"}
                or not isinstance(branch["on"], str) or branch["subgoal_id"] not in seen):
            raise ValueError("Branch requires event name and existing subgoal_id")
    encoded(plan)


class MemoryRules:
    """Single-writer evidence ledger and verifier. Steps count returned tool turns."""

    def __init__(self):
        self.state = {"world": {"step": 0, "revision": 0, "active_plan_id": None},
                      "pose": None, "objects": [], "active_beliefs": [], "invalidated": [],
                      "events": [], "topology": None, "confidence_thresholds": deepcopy(THRESHOLDS),
                      "measurements": {}, "plans": [], "ledger": []}
        self._seen = set()
        self._supports = {}
        self._scan_targets_seen = set()
        self._scan_turn_evidence = []
        self._scan_turn_count = 0
        self._scan_stall_latched = False

    def record(self, kind, source, **data):
        entry = {"evidence_id": f"e{len(self.state['ledger']) + 1:06d}",
                 "kind": kind, "source": source, "step": self.state["world"]["step"], **deepcopy(data)}
        self.state["ledger"].append(entry)
        return entry["evidence_id"]

    def event(self, kind, evidence_ids, **data):
        self.state["events"].append({"event_id": f"event-{len(self.state['events']) + 1}",
                                     "kind": kind, "step": self.state["world"]["step"],
                                     "evidence_ids": evidence_ids, **data})

    def invalidate(self, object_id, reason, evidence_id):
        for plan in self.state["plans"]:
            if not plan["active"]:
                continue
            for goal in plan["subgoals"]:
                if (goal["active"] and any(x.get("object_id") == object_id
                                          for x in goal["preconditions"] + goal["completion"])):
                    goal.update(status="已失效", evidence_ids=[evidence_id])
                    self.event("key_precondition_invalidated", [evidence_id],
                               plan_id=plan["plan_id"], subgoal_id=goal["subgoal_id"], reason=reason)
        self.event("replan_required", [evidence_id], object_id=object_id, reason=reason)

    def set_plan(self, plan_id, plan, accepted=True):
        validate_plan(plan)
        for old in self.state["plans"]:
            old["active"] = False
            for goal in old["subgoals"]:
                goal["active"] = False
        row = deepcopy(plan)
        row.update(plan_id=plan_id, active=accepted)
        for goal in row["subgoals"]:
            goal.update(active=accepted, status="待做" if accepted else "已失效", evidence_ids=[])
        self.state["plans"].append(row)
        self.state["world"]["active_plan_id"] = plan_id if accepted else None
        eid = self.record("plan_registered" if accepted else "plan_rejected", "planning_harness", plan_id=plan_id)
        if not accepted:
            for goal in row["subgoals"]:
                goal["evidence_ids"] = [eid]
            self.event("replan_required", [eid], plan_id=plan_id)
        self.state["world"]["revision"] += 1

    def _observe(self, item, step):
        required = {"object_id", "category", "pose", "pose_covariance", "confidence",
                    "source", "frame_id", "anchor_node", "visual_feature"}
        if (not isinstance(item, dict) or not required.issubset(item)
                or any(not isinstance(item[k], str) or not item[k]
                       for k in ("object_id", "category", "source", "frame_id"))
                or not finite(item["confidence"]) or not 0 <= item["confidence"] <= 1
                or not valid_pose(item["pose"])):
            raise ValueError("Object evidence needs identity, source, frame, finite pose/confidence")
        covariance = item["pose_covariance"]
        n = len(item["pose"]["position_m"])
        if covariance is not None and (not isinstance(covariance, list) or len(covariance) != n
                or any(not isinstance(row, list) or len(row) != n or not all(finite(x) for x in row)
                       for row in covariance) or any(covariance[i][i] < 0 for i in range(n))):
            raise ValueError("Invalid pose covariance")
        identity = (item["object_id"], item["source"], item["frame_id"])
        if identity in self._seen:
            return
        self._seen.add(identity)
        eid = self.record("observation_confirmed", item["source"], observation=item)
        obj = next((x for x in self.state["objects"] if x["object_id"] == item["object_id"]), None)
        if obj is None:
            obj = {k: deepcopy(item[k]) for k in required if k != "frame_id"}
            obj.update(state="unknown", last_seen=step, evidence_ids=[], candidate_pose=None)
            self.state["objects"].append(obj)
        previous_state = obj["state"]
        if step - obj["last_seen"] >= THRESHOLDS["predicted_after_steps"]:
            self._supports.pop(item["object_id"], None)
        candidate = obj.get('candidate_pose')
        if (candidate and candidate['frame'] == obj['pose']['frame'] == item['pose']['frame']
                and len(candidate['position_m']) == len(obj['pose']['position_m']) == n
                and math.dist(item['pose']['position_m'], obj['pose']['position_m']) <= THRESHOLDS['relocation_distance_m']
                and math.dist(item['pose']['position_m'], candidate['position_m']) > THRESHOLDS['relocation_distance_m']
                and item['confidence'] >= THRESHOLDS['confirmed']):
            # Returning to the retained pose disproves the *pending* candidate.
            # It is not another relocation. Require fresh independent support;
            # invalidated dependent goals are never automatically restored.
            self.record('relocation_candidate_rejected', 'memory_rules', object_id=item['object_id'],
                        rejected_pose=candidate, supporting_observation=eid)
            obj['candidate_pose'] = None
            self._supports.pop(item['object_id'], None)
        reference = obj.get("candidate_pose") or obj["pose"]
        distance = (math.dist(reference["position_m"], item["pose"]["position_m"])
                    if reference["frame"] == item["pose"]["frame"]
                    and len(reference["position_m"]) == n else None)
        obj["evidence_ids"].append(eid)
        if (distance is not None and distance > THRESHOLDS["relocation_distance_m"]
                and item["confidence"] >= THRESHOLDS["confirmed"]):
            obj.update(state="contradicted", last_seen=step, candidate_pose=deepcopy(item["pose"]),
                       confidence=item["confidence"], source=item["source"])
            self._supports[item["object_id"]] = {identity}
            relocation = self.record("target_relocated", item["source"], object_id=item["object_id"],
                                     old_pose=obj["pose"], new_pose=item["pose"], evidence_ids=[eid])
            self.event("target_state_changed", [eid, relocation], object_id=item["object_id"])
            self.invalidate(item["object_id"], "positive_position_contradiction", eid)
            return
        if distance is None:
            # Unrelated coordinate frames cannot establish a stable position.
            self._supports[item["object_id"]] = set()
        support = self._supports.setdefault(item["object_id"], set())
        if item["confidence"] >= THRESHOLDS["confirmed"]:
            support.add(identity)
        else:
            support.clear()
        obj.update({k: deepcopy(item[k]) for k in required if k != "frame_id"})
        for key in ("task_label", "label_description", "camera_pose", "measurement_provenance"):
            if key in item:
                obj[key] = deepcopy(item[key])
        obj.update(last_seen=step, candidate_pose=None,
                   state="confirmed" if len(support) >= 2 else "unknown")
        if previous_state != obj["state"]:
            self.event("target_state_changed", [eid], object_id=obj["object_id"], state=obj["state"])

    def update(self, payload):
        """Evidence payload is task semantic, already stripped by the backend adapter."""
        step = payload["step"]
        if type(step) is not int or step < self.state["world"]["step"]:
            raise ValueError("Memory steps must be monotonic integers")
        self.state["world"]["step"] = step
        if "public_context" in payload:
            self.state["world"]["public_context"] = deepcopy(payload["public_context"])
        if payload.get("pose") is not None:
            if not valid_pose(payload["pose"]) or not payload["pose"].get("source"):
                raise ValueError("Pose requires a coordinate frame and source")
            self.state["pose"] = deepcopy(payload["pose"])
        for item in payload.get("objects", []):
            self._observe(item, step)
        for obj in self.state["objects"]:
            age = step - obj["last_seen"]
            old = obj["state"]
            if age >= THRESHOLDS["stale_after_steps"]:
                obj["state"] = "stale"
            elif old != "contradicted" and age >= THRESHOLDS["unknown_after_steps"]:
                obj["state"] = "unknown"
            elif old == "confirmed" and age >= THRESHOLDS["predicted_after_steps"]:
                # Adapter landmarks are static; this is a short static-world prediction.
                obj["state"] = "predicted"
            if age >= THRESHOLDS["predicted_after_steps"]:
                self._supports.pop(obj["object_id"], None)
            if old != obj["state"]:
                eid = self.record("belief_state_changed", "memory_rules", object_id=obj["object_id"],
                                  old_state=old, state=obj["state"], unobserved_steps=age)
                self.event("target_state_changed", [eid], object_id=obj["object_id"], state=obj["state"])
                if obj["state"] == "stale":
                    self.invalidate(obj["object_id"], "verification_expired", eid)
        for name, item in payload.get("measurements", {}).items():
            if not finite(item.get("value")) or not item.get("source"):
                raise ValueError("Measurements require finite values and sources")
            eid = self.record("measurement", item["source"], name=name, value=item["value"])
            self.state["measurements"][name] = {**deepcopy(item), "step": step, "evidence_ids": [eid]}
        for disturbance in payload.get("disturbances", []):
            if not isinstance(disturbance.get("source"), str) or not disturbance["source"]:
                raise ValueError("Disturbances require a source")
            eid = self.record("external_disturbance", disturbance["source"], **{
                k: v for k, v in disturbance.items() if k != "source"})
            self.event("external_disturbance", [eid])
            if disturbance.get("blocked") is True:
                self.event("dynamic_obstacle_blocked", [eid])
            if disturbance.get("disproves") is True:
                obj = next((x for x in self.state["objects"]
                            if x["object_id"] == disturbance.get("object_id")), None)
                if obj:
                    obj.update(state="contradicted", source=disturbance["source"])
                    obj["evidence_ids"].append(eid)
                    self._supports.pop(obj["object_id"], None)
                    self.event("target_state_changed", [eid], object_id=obj["object_id"], state="contradicted")
                    self.invalidate(obj["object_id"], "external_positive_contradiction", eid)
        action_evidence = []
        for action in payload.get("actions", []):
            if action.get("deduplicated"):
                continue
            eid = self.record("action_executed" if action["status"] == "succeeded" else "action_failed",
                              "execution_feedback", action=action)
            action_evidence.append((action, eid))
            if action.get("error_code") in {"BLOCKED", "DYNAMIC_OBSTACLE", "COLLISION"}:
                self.event("dynamic_obstacle_blocked", [eid])
            if (action["tool"] in {"move_relative", "turn"} and action["status"] != "succeeded"
                    or action.get("stuck") is True):
                self.event("skill_stuck", [eid])
            if action.get("error_code") == "MEMORY_CONSTRAINT":
                self.event("key_precondition_invalidated", [eid])
                self.event("replan_required", [eid])
            for plan in self.state["plans"]:
                if plan["active"] and plan["plan_id"] == action.get("plan_id"):
                    for goal in plan["subgoals"]:
                        if (goal["subgoal_id"] == action.get("subgoal_id") and goal["status"] == "待做"
                                and action.get("error_code") not in {"MEMORY_CONSTRAINT", "INVALID_ARGUMENTS",
                                                                     "ONE_TOOL_PER_TURN", "CALL_ID_REUSED"}):
                            goal.update(status="进行中", evidence_ids=[eid])
        self._search_progress(payload, action_evidence)
        for plan in self.state["plans"]:
            if not plan["active"]:
                continue
            for goal in plan["subgoals"]:
                if goal["status"] == "已失效":
                    continue
                if (goal["status"] == "已完成" and any(predicate(x, self.state) is False
                                                      for x in goal["completion"])):
                    eid = self.record("completion_invalidated", "memory_verifier", plan_id=plan["plan_id"],
                                      subgoal_id=goal["subgoal_id"])
                    goal.update(status="已失效", evidence_ids=[eid])
                    self.event("replan_required", [eid], plan_id=plan["plan_id"])
                    continue
                if any(predicate(x, self.state) is False for x in goal["preconditions"]):
                    eid = self.record("precondition_failed", "memory_verifier", plan_id=plan["plan_id"],
                                      subgoal_id=goal["subgoal_id"])
                    goal.update(status="已失效", evidence_ids=[eid])
                    self.event("key_precondition_invalidated", [eid], subgoal_id=goal["subgoal_id"])
                    self.event("replan_required", [eid], plan_id=plan["plan_id"])
                elif (goal["status"] == "进行中" and goal["completion"]
                      and all(predicate(x, self.state) is True for x in goal["completion"])):
                    ids = []
                    for check in goal["completion"]:
                        if "object_id" in check:
                            ids += next(x["evidence_ids"][-2:] for x in self.state["objects"]
                                        if x["object_id"] == check["object_id"])
                        else:
                            ids += self.state["measurements"][check["measurement"]]["evidence_ids"]
                    goal.update(status="已完成", evidence_ids=ids)
        self.state["world"]["revision"] += 1

    def _search_progress(self, payload, action_evidence):
        """Task-search stall, distinct from a failed physical skill.

        Successful tool feedback is an attempt/progress signal, not a measured
        displacement. Neither simulator motion deltas nor target GT are read.
        Re-selecting landmarks, observing, and replacing plans do not reset it.
        """
        view = payload.get('public_context', {}).get('current_observation', {})
        targets = {c['object_id'] for c in view.get('target_candidates', []) if c.get('object_id')}
        targets.update(o['object_id'] for o in payload.get('objects', []) if o.get('category') == 'task_target')
        new_targets = targets - self._scan_targets_seen
        self._scan_targets_seen.update(targets)
        translated = any(a['tool'] == 'move_relative' and a['status'] == 'succeeded' for a, _ in action_evidence)
        if new_targets or translated:
            self._scan_turn_count = 0
            self._scan_turn_evidence = []
            self._scan_stall_latched = False
        for action, eid in action_evidence:
            if action['tool'] == 'turn' and action['status'] == 'succeeded':
                self._scan_turn_count += 1
                self._scan_turn_evidence = (self._scan_turn_evidence + [eid])[-SCAN_TURN_LIMIT:]
        stalled = self._scan_turn_count >= SCAN_TURN_LIMIT
        self.state['world']['exploration'] = {
            'successful_turns_without_search_progress': self._scan_turn_count,
            'turn_limit': SCAN_TURN_LIMIT, 'stalled': stalled,
            'progress_basis': 'successful_translation_tool_or_first_task_observation_not_motion_gt',
            'evidence_ids': list(self._scan_turn_evidence),
            'recovery': 'change_viewpoint_with_translation; inspect_geometry_or_abort_if_motion_unsupported'}
        if stalled and not self._scan_stall_latched:
            ids = list(self._scan_turn_evidence)
            eid = self.record('search_stalled', 'memory_verifier', reason='repeated_turns_without_search_progress',
                              turn_count=self._scan_turn_count, action_evidence_ids=ids)
            self.event('skill_stuck', [eid], reason='repeated_turns_without_search_progress',
                       recovery='explore_viewpoint_or_abort')
            self.event('replan_required', [eid], reason='search_stalled')
            self._scan_stall_latched = True

    def document(self):
        return ("# 记忆库 · memory v1\n\n## 现场状态\n\n"
                "规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。\n\n"
                "```json\n" + encoded(self.state) + "\n```\n\n"
                "## 操作经验\n\n## 程序工具\n")


def read_state(document):
    section = document.split("## 现场状态\n", 1)[1].split("\n## 操作经验", 1)[0]
    return json.loads(section.split("```json\n", 1)[1].split("\n```", 1)[0])


def state_packet(state, decision_step=None):
    """No ledger, old plans, invalid positions, or stale measurements in model context."""
    packet = {k: deepcopy(state[k]) for k in PACKET_KEYS}
    step = state["world"]["step"] if decision_step is None else decision_step
    objects = []
    for obj in state["objects"]:
        age = step - obj["last_seen"]
        if obj["state"] == "confirmed" and age < THRESHOLDS["predicted_after_steps"]:
            objects.append(deepcopy(obj))
        elif obj["state"] in {"confirmed", "predicted"} and age < THRESHOLDS["unknown_after_steps"]:
            predicted = deepcopy(obj)
            predicted.update(state="predicted", confidence=obj["confidence"] * 0.5,
                             prediction_basis="static_landmark_short_occlusion")
            objects.append(predicted)
    packet["objects"] = objects
    packet["active_beliefs"] = []
    packet["world"]["active_plan"] = None
    packet["invalidated"] = [{"object_id": x["object_id"], "state": x["state"],
                              "evidence_ids": x["evidence_ids"][-2:]}
                             for x in state["objects"] if x["state"] in {"contradicted", "stale"}]
    for plan in state["plans"]:
        if plan["active"]:
            packet["world"]["active_plan"] = {k: deepcopy(plan[k]) for k in ("plan_id", "branches", "recovery")}
            for goal in plan["subgoals"]:
                target = "invalidated" if goal["status"] == "已失效" else "active_beliefs"
                packet[target].append({"plan_id": plan["plan_id"], **deepcopy(goal)})
        elif plan is state["plans"][-1]:
            packet["invalidated"].extend({"plan_id": plan["plan_id"], "subgoal_id": g["subgoal_id"],
                                          "status": g["status"], "evidence_ids": g["evidence_ids"]}
                                         for g in plan["subgoals"] if g["status"] == "已失效")
    packet["world"]["decision_step"] = step
    packet["world"]["snapshot_lag_steps"] = max(0, step - state["world"]["step"])
    packet["world"]["measurements"] = {k: deepcopy(v) for k, v in state["measurements"].items()
                                         if v["step"] == step}
    if packet["world"]["snapshot_lag_steps"]:
        packet["pose"] = None
    packet["events"] = packet["events"][-16:]
    # Keep context bounded even though provenance and history remain complete on disk.
    for obj in packet["objects"]:
        obj["evidence_ids"] = obj["evidence_ids"][-2:]
    return packet


class AsyncMemory:
    """FIFO worker owns rules and disk I/O; planner reads the last committed MD snapshot.

    Only close/flush (shutdown and offline tests) waits for the worker. Publishing
    happens after atomic rename and re-reading the actual MD. Exceptions are
    exposed to the planner; no execution is allowed on a failed memory writer.
    """

    def __init__(self, path: Path):
        self.path = Path(path)
        self.rules = MemoryRules()
        self.error = None
        self.closed = False
        self.queue = Queue()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            raise FileExistsError("Use a fresh run directory; memory ledger cannot be overwritten")
        self._publish()
        self.worker = Thread(target=self._work, name="memory-v1", daemon=True)
        self.worker.start()

    def _publish(self):
        temporary = self.path.with_suffix(".md.tmp")
        temporary.write_text(self.rules.document(), encoding="utf-8")
        temporary.replace(self.path)
        self._published = read_state(self.path.read_text(encoding="utf-8"))

    def _work(self):
        while True:
            command = self.queue.get()
            try:
                if command is None:
                    return
                if self.error is not None:
                    continue
                kind, args = command
                if kind == "plan":
                    self.rules.set_plan(*args)
                else:
                    self.rules.update(args)
                self._publish()
            except Exception as exc:
                # Do not log arbitrary evidence/exception text (may contain secrets).
                self.error = type(exc).__name__
            finally:
                self.queue.task_done()

    def submit(self, payload):
        self._enqueue(("update", deepcopy(payload)))

    def plan(self, plan_id, plan, accepted=True):
        validate_plan(plan)
        self._enqueue(("plan", (plan_id, deepcopy(plan), accepted)))

    def _enqueue(self, command):
        if self.closed:
            raise RuntimeError("Memory is closed")
        self.queue.put_nowait(command)

    def snapshot(self):
        return deepcopy(self._published)

    def packet(self, step):
        packet = state_packet(self.snapshot(), step)
        if self.error:
            packet["events"].append({"kind": "memory_write_failed", "error_type": self.error})
        return packet

    def flush(self):
        self.queue.join()
        if self.error:
            raise RuntimeError("Memory worker failed: " + self.error)

    def close(self):
        if not self.closed:
            self.closed = True
            self.queue.put_nowait(None)
            self.worker.join()
        if self.error:
            raise RuntimeError("Memory worker failed: " + self.error)

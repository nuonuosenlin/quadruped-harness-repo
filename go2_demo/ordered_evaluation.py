"""Privileged ordered-checkpoint scoring. Never part of planner observations.

An accepted request is not evidence. Only measured, confirmed stopped snapshots
can latch A. B must be reached after A and remain valid at the final snapshot;
the episode runner additionally requires finish, budgets and final-stop success.
"""

from copy import deepcopy
import math


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


class OrderedStandoffEvaluator:
    def __init__(self, target_a, target_b):
        self.targets = {"A": tuple(target_a), "B": tuple(target_b)}
        self.a_witness = None
        self.best_a_attempt = None
        self.last_stop = None
        self.stop_index = 0
        self.premature_b_stops = 0

    def measure(self, label, sample):
        values = [*sample["base_xy_m"], sample["yaw_rad"], sample["speed_mps"],
                  sample["abs_yaw_rate_radps"], sample["sim_time_s"]]
        valid = all(_finite(x) for x in values)
        distance = heading = None
        if valid:
            dx = self.targets[label][0] - sample["base_xy_m"][0]
            dy = self.targets[label][1] - sample["base_xy_m"][1]
            distance = math.hypot(dx, dy)
            difference = math.atan2(dy, dx) - sample["yaw_rad"]
            heading = abs(math.atan2(math.sin(difference), math.cos(difference)))
        reasons = []
        if not valid:
            reasons.append("INVALID_MEASUREMENT")
        else:
            if not .82 - 1e-12 <= distance <= 1.18 + 1e-12:
                reasons.append("DISTANCE_OUT_OF_RANGE")
            if heading > .25 + 1e-12:
                reasons.append("HEADING_OUT_OF_RANGE")
            if sample["speed_mps"] >= .12 or sample["abs_yaw_rate_radps"] >= .25:
                reasons.append("NOT_STOPPED")
        if not sample.get("stop_confirmed", False):
            reasons.append("STOP_NOT_CONFIRMED")
        if sample["collision"]:
            reasons.append("COLLISION")
        if sample["fallen"]:
            reasons.append("FALLEN")
        return {"label": label, "target_xy_m": list(self.targets[label]),
                "base_xy_m": list(sample["base_xy_m"]) if valid else None,
                "distance_to_target_center_m": distance, "heading_error_rad": heading,
                "speed_mps": sample["speed_mps"] if valid else None,
                "abs_yaw_rate_radps": sample["abs_yaw_rate_radps"] if valid else None,
                "sim_time_s": sample["sim_time_s"] if valid else None,
                "stop_confirmed": bool(sample.get("stop_confirmed", False)),
                "stopped": bool(valid and sample["speed_mps"] < .12 and sample["abs_yaw_rate_radps"] < .25),
                "collision": bool(sample["collision"]), "fallen": bool(sample["fallen"]),
                "criteria_pass": not reasons, "failure_reasons": reasons,
                "source": "privileged_simulator_evaluator"}

    def note_stop(self, sample):
        """Called by the backend after its bounded settling, never by a model."""
        self.stop_index += 1
        self.last_stop = deepcopy(sample)
        a = self.measure("A", sample)
        a["stop_index"] = self.stop_index
        if self.a_witness is None:
            candidate = (abs(a["distance_to_target_center_m"] - 1.), a["heading_error_rad"]) if a["distance_to_target_center_m"] is not None else (math.inf, math.inf)
            previous = self.best_a_attempt
            old = ((abs(previous["distance_to_target_center_m"] - 1.), previous["heading_error_rad"])
                   if previous and previous["distance_to_target_center_m"] is not None else (math.inf, math.inf))
            if previous is None or candidate < old:
                self.best_a_attempt = deepcopy(a)
            if a["criteria_pass"]:
                self.a_witness = deepcopy(a)
            elif self.measure("B", sample)["criteria_pass"]:
                self.premature_b_stops += 1

    def evaluate(self, sample):
        # A historical confirmed stop may establish A; a fresh final confirmed
        # stop at B is still required. Merely visiting B earlier never suffices.
        fresh_stop = (self.last_stop is not None and self.last_stop.get("stop_confirmed")
                      and self.last_stop["sim_time_s"] == sample["sim_time_s"]
                      and self.last_stop["base_xy_m"] == sample["base_xy_m"]
                      and self.last_stop["yaw_rad"] == sample["yaw_rad"])
        current = {**sample, "stop_confirmed": bool(fresh_stop and sample.get("stop_confirmed"))}
        b = self.measure("B", current)
        eligible = bool(self.a_witness is not None and self.stop_index > self.a_witness["stop_index"]
                        and sample["sim_time_s"] > self.a_witness["sim_time_s"])
        if not eligible:
            b["failure_reasons"].append("A_NOT_CONFIRMED_BEFORE_B")
        safe = not sample["collision"] and not sample["fallen"]
        a = deepcopy(self.a_witness or self.best_a_attempt or self.measure("A", current))
        a.update(achieved_at_checkpoint=self.a_witness is not None,
                 passed=bool(self.a_witness is not None and safe))
        if not safe and "GLOBAL_SAFETY_FAILURE" not in a["failure_reasons"]:
            a["failure_reasons"].append("GLOBAL_SAFETY_FAILURE")
        b.update(eligible=eligible, passed=bool(b["criteria_pass"] and eligible and safe))
        return {"success": bool(a["passed"] and b["passed"] and safe),
                "goal_kind": "ordered_standoff", "checkpoints": {"A": a, "B": b},
                "checkpoint_order": ["A", "B"], "order_satisfied": eligible,
                "premature_b_stops_ignored": self.premature_b_stops,
                "requires_finish": True, "finish_enforced_by": "episode_runner",
                "standoff_m": 1., "distance_tolerance_m": .18, "heading_tolerance_rad": .25,
                "collision": bool(sample["collision"]), "fallen": bool(sample["fallen"]),
                "stopped": b["stopped"], "source": "privileged_simulator_evaluator"}

"""EXPERIMENTAL local demo safety interlock, pending the group-meeting decision.

Temporary experiment, NOT the final boundary design. Replace after the meeting
chooses scene boundaries, an execution interlock, or planner boundary inputs.
The input base pose is SIMULATOR GROUND TRUTH, the same provenance gap as the
backend's measured motion deltas. This is a safety interlock, not a navigation
measurement or a non-GT cliff detector. No memory writer or planner is called.
"""

import math


# Explicit heuristic reserve for support/feet and settling uncertainty, NOT a
# proven robot swept footprint. A center-only endpoint check misses the recorded
# fall. Platform dimensions themselves always come from the scenario definition.
EXPERIMENTAL_SUPPORT_MARGIN_M = 0.35
EXPERIMENTAL_BOUNDARY_CODE = "BOUNDARY_BLOCKED"


def experimental_boundary_gate(scenario, base_xy_yaw, *, forward_m, lateral_m):
    """Return refusal feedback or None; never execute/clip an action or mutate state.

    base_xy_yaw is the current captured simulator GT pose. Physics is paused
    between tools in this harness. Rotate body-relative commands into the scene
    frame and check the straight requested segment against the inset rectangle.
    An inward/tangential escape remains allowed when already inside the reserve.
    This preflight is not a guarantee against controller drift, rotation near an
    edge, dynamic falls, or collisions. It neither plans a route nor adds a map.
    """
    half_size = getattr(scenario, "floor_half_size_m", None)
    if half_size is None:
        return None  # Existing infinite-floor tasks keep their execution path.
    half_x, half_y = (float(v) for v in half_size)
    x, y, yaw = (float(v) for v in base_xy_yaw)
    c, s = math.cos(yaw), math.sin(yaw)
    dx, dy = c * forward_m - s * lateral_m, s * forward_m + c * lateral_m
    length = math.hypot(forward_m, lateral_m)
    margin = EXPERIMENTAL_SUPPORT_MARGIN_M
    blocked = []
    fractions = []
    for edge, start, delta, half in (("east", x, dx, half_x),
                                     ("west", -x, -dx, half_x),
                                     ("north", y, dy, half_y),
                                     ("south", -y, -dy, half_y)):
        limit = max(0., half - margin)
        # Convex segment: an inside start and endpoint imply an inside segment.
        # If already close to an edge, block only movement farther toward it;
        # allow retreat without requiring a large single step out of the reserve.
        if delta > 1e-12 and start + delta > limit + 1e-12:
            blocked.append({"edge": edge,
                            "excess_beyond_safety_limit_m": start + delta - limit})
            fractions.append(max(0., min(1., (limit - start) / delta)))
    if not blocked:
        return None
    return {"status": "failed", "error_code": EXPERIMENTAL_BOUNDARY_CODE,
            "message": "Experimental boundary safety interlock refused this move before execution. "
                       "Turn or choose a different/inward displacement; no motion was executed. "
                       "The interlock uses simulator ground truth, not non-GT perception.",
            # This existing feedback field survives the normal planner whitelist.
            # No absolute pose, platform map, or new memory_state field is added.
            "constraint_feedback": {
                "code": EXPERIMENTAL_BOUNDARY_CODE, "experimental": True,
                "source": "simulator_ground_truth_boundary_safety_interlock",
                "navigation_measurement": False, "executed": False,
                "blocked_directions": [item["edge"] for item in blocked],
                "requested_body_displacement_m": [forward_m, lateral_m],
                "requested_distance_m": length,
                "safe_distance_along_request_m": min(fractions) * length,
                "support_margin_m": margin, "blocked_edges": blocked}}


def experimental_boundary_memory_results(results):
    """Keep a non-executed refusal out of memory action/evidence entries.

    runner still logs and delivers the ORIGINAL feedback to the planner, and
    submits the ordinary observation and logical step to memory. The unchanged
    search clocks therefore advance without a false successful translation or
    physical skill_stuck. No boundary geometry/GT is written to the memory MD.
    """
    return [result for result in results
            if not (result.get("tool") == "move_relative"
                    and result.get("error_code") == EXPERIMENTAL_BOUNDARY_CODE)]

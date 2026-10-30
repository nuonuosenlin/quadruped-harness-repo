"""Pure geometry and text-only function schemas (Python 3.8 compatible)."""
import numpy as np


def vec3(value):
    a = np.asarray(value, dtype=float)
    if a.shape != (3,) or not np.isfinite(a).all():
        raise ValueError('Expected finite xyz in world metres')
    return a


def unit(value):
    a = vec3(value)
    if np.linalg.norm(a) < 1e-9:
        raise ValueError('Zero direction')
    return a / np.linalg.norm(a)


def relation_geometry(a, b, relation):
    """Points are {position:[x,y,z], axis:[x,y,z] (optional)}.

    collinear projects A onto the infinite line through B along B.axis.
    parallel aligns A.axis with B.axis, preserving A.position.
    Only touch/adjust are admitted for robot execution in this milestone.
    """
    pa, pb = vec3(a['position']), vec3(b['position'])
    if relation in ('touch', 'adjust'):
        delta = pb - pa
        distance = float(np.linalg.norm(delta))
        desired = pb - unit(delta) * 0.02 if distance > 0.02 else pa.copy()
        horizon = 0.08 if relation == 'touch' else 0.05
        move = desired - pa
        desired = pa + move * min(1.0, horizon / max(np.linalg.norm(move), 1e-9))
        return {'position': desired.tolist(), 'distance_before_m': distance,
                'relation': relation, 'execution_verified': False}
    if relation == 'collinear':
        axis = unit(b['axis'])
        return {'position': (pb + axis * np.dot(pa - pb, axis)).tolist(),
                'relation': relation, 'execution_verified': False, 'scope': 'geometry_only'}
    if relation == 'parallel':
        unit(a['axis'])
        return {'position': pa.tolist(), 'axis': unit(b['axis']).tolist(),
                'relation': relation, 'execution_verified': False, 'scope': 'geometry_only'}
    raise ValueError('Unknown relation')


def tool(name, description, properties, required):
    return {'type': 'function', 'function': {'name': name, 'description': description,
        'parameters': {'type': 'object', 'properties': properties,
                       'required': required, 'additionalProperties': False}}}


TOOLS = [
    tool('track_keypoint', 'Track alphabet_soup_1 visible surface from a top-left pixel bbox. Returns world xyz metres; never images.',
         {'bbox': {'type': 'array', 'items': {'type': 'integer'}, 'minItems': 4, 'maxItems': 4},
          'name': {'type': 'string', 'enum': ['alphabet_soup_1']}}, ['bbox', 'name']),
    tool('solve_constraint', 'Generate bounded trajectory from current eef to tracked target. First use touch, then adjust after execution until success. Returns traj ID. collinear/parallel geometry only, not executable.',
         {'keypoint_A': {'type': 'string', 'enum': ['eef']},
          'keypoint_B': {'type': 'string', 'enum': ['alphabet_soup_1']},
          'relation': {'type': 'string', 'enum': ['touch', 'adjust', 'collinear', 'parallel']}},
         ['keypoint_A', 'keypoint_B', 'relation']),
    tool('execute_trajectory', 'Execute a previously returned traj ID exactly once using OSC_POSE; cannot accept raw model-generated actions.',
         {'traj': {'type': 'string'}}, ['traj']),
    tool('check_success', 'Return success bool, newly observed keypoints, distance and separate original BDDL result.', {}, [])
]

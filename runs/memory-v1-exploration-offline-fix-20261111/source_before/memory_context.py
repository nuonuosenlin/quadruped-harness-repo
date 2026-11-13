"""Bounded, rule-only planning projection. The MD ledger is never truncated."""
from copy import deepcopy
import json
import math

STATE_CHAR_LIMIT = 12000
RETRY_STATE_CHAR_LIMIT = 6000
PACKET_KEYS = ('world', 'pose', 'objects', 'active_beliefs', 'invalidated',
               'events', 'topology', 'confidence_thresholds')


def _small(value, depth=0):
    if depth > 7:
        return None
    if isinstance(value, str):
        return value[:256]
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float)):
        return value if math.isfinite(value) else None
    if isinstance(value, list):
        return [_small(v, depth+1) for v in value[:32]]
    if isinstance(value, dict):
        return {k: _small(v, depth+1) for k, v in list(value.items())[:32]
                if isinstance(k, str) and len(k) <= 256}
    return None


def _fields(item, keys):
    return {k: _small(item[k]) for k in keys if k in item}


def _recent(items, limit):
    return [_small(x) for x in items[-limit:] if isinstance(x, dict)]


def compact_observation(observation, *, retry=False):
    """Preserve the eight-key contract and fresh evidence, with a hard size cap.

    This is a lossy *prompt view*, never evidence or verification authority.
    Preconditions are still checked against the full committed MD snapshot.
    """
    state = observation.get('memory_state', {})
    world = state.get('world', {})
    retry = retry or bool(world.get('context_limits', {}).get('retry'))
    public = world.get('public_context', {})
    live = world.get('current_observation', public.get('current_observation', {}))
    limit = RETRY_STATE_CHAR_LIMIT if retry else STATE_CHAR_LIMIT
    count = 4 if retry else 8
    w = _fields(world, ('step', 'revision', 'decision_step', 'snapshot_lag_steps',
                         'active_plan_id', 'active_plan', 'bootstrap_hint'))
    w['task_targets'] = _recent(world.get('task_targets', public.get('task_targets', [])), 4)
    w['completion_requirements'] = _small(public.get('completion_requirements',
        world.get('completion_requirements', live.get('completion_requirements', {}))))
    current = _fields(live, ('image_id', 'image_size', 'sensor_calibration', 'source'))
    current['target_candidates'] = [_fields(c, ('object_id', 'task_label', 'description',
        'image_id', 'pixel_uv', 'camera_xyz_m', 'coordinate_frame', 'status', 'source'))
        for c in live.get('target_candidates', [])[:(2 if retry else 4)]]
    # Repeated selections of exactly the same geometry are one prompt landmark.
    points, seen = [], set()
    for p in live.get('tracked_points', []):
        if not p.get('valid') or p.get('image_id') != live.get('image_id'):
            continue
        identity = json.dumps([p.get('pixel_uv'), p.get('relative_xy_m')], sort_keys=True)
        if identity in seen:
            continue
        seen.add(identity)
        points.append(_fields(p, ('point_id', 'image_id', 'valid', 'pixel_uv', 'relative_xy_m',
                                  'range_m', 'bearing_rad', 'confidence', 'source')))
        if len(points) >= (3 if retry else 6):
            break
    current['tracked_points'] = points
    current['visual_candidates'] = [_fields(c, ('image_id', 'pixel_uv', 'category', 'source'))
        for c in live.get('visual_candidates', public.get('visual_candidates', []))
        if c.get('image_id') == live.get('image_id')][:(3 if retry else 6)]
    w['current_observation'] = current
    feedback = []
    for r in world.get('last_tool_feedback', [])[-1:]:
        feedback.append(_fields(r, ('tool', 'status', 'error_code', 'constraint_feedback',
                                    'plan_diagnostic', 'plan_id', 'subgoal_id', 'image_id')))
    w['last_tool_feedback'] = feedback
    objects = [o for o in state.get('objects', []) if o.get('state') in {'confirmed', 'predicted'}]
    step = world.get('decision_step', world.get('step', 0))
    thresholds = state.get('confidence_thresholds', {})
    age_limit = thresholds.get('unknown_after_steps', 6)
    objects = [o for o in objects if isinstance(o.get('last_seen'), int)
               and 0 <= step-o['last_seen'] < age_limit]
    objects.sort(key=lambda o: (o.get('category') != 'task_target', -o['last_seen']))
    selected = []
    for obj in objects[:count]:
        item = _fields(obj, ('object_id', 'category', 'state', 'pose', 'pose_covariance',
            'last_seen', 'confidence', 'source', 'task_label', 'label_description',
            'camera_pose', 'measurement_provenance', 'prediction_basis', 'anchor_node', 'visual_feature'))
        item['evidence_ids'] = _small(obj.get('evidence_ids', [])[-2:])
        if item['state'] == 'confirmed' and step-item['last_seen'] >= thresholds.get('predicted_after_steps', 3):
            item.update(state='predicted', confidence=item['confidence']*.5,
                        prediction_basis='static_landmark_short_occlusion')
        selected.append(item)
    beliefs = []
    for g in state.get('active_beliefs', [])[:count]:
        if g.get('status') == '已失效':
            continue
        item = _fields(g, ('plan_id', 'subgoal_id', 'description', 'status', 'preconditions', 'completion'))
        item['evidence_ids'] = _small(g.get('evidence_ids', [])[-2:])
        beliefs.append(item)
    measures = world.get('measurements', {})
    # Retain named measurements referenced by visible progress before extras.
    names = [c.get('measurement') for g in beliefs for name in ('preconditions', 'completion')
             for c in g.get(name, []) if isinstance(c, dict) and c.get('measurement')]
    names += [k for k in measures if k.startswith('pose.')]
    ids = {p.get('point_id') for p in points}
    names += [k for k in measures if k.split('.')[0] in ids]
    w['measurements'] = {k: _small(measures[k]) for k in dict.fromkeys(names)
                         if k in measures and measures[k].get('step') == step}
    packet = {'world': w, 'pose': _small(state.get('pose')), 'objects': selected,
        'active_beliefs': beliefs, 'invalidated': _recent(state.get('invalidated', []), 2 if retry else 4),
        'events': _recent(state.get('events', []), 2 if retry else 4), 'topology': None,
        'confidence_thresholds': _small(thresholds)}
    w['context_limits'] = {'state_char_limit': limit, 'retry': retry,
        'projection': 'bounded_prompt_view_full_checks_in_md', 'omitted_items': 0}
    # Remove whole records, never cut JSON or turn an omitted condition into evidence.
    groups = [packet['events'], packet['invalidated'], current['visual_candidates'], packet['active_beliefs'],
              packet['objects'], current['target_candidates'], current['tracked_points']]
    def size():
        return len(json.dumps(packet, ensure_ascii=False, separators=(',', ':'), allow_nan=False))
    for group in groups:
        while group and size() > limit:
            group.pop()
            w['context_limits']['omitted_items'] += 1
    while w['measurements'] and size() > limit:
        w['measurements'].pop(next(reversed(w['measurements'])))
        w['context_limits']['omitted_items'] += 1
    if size() > limit:
        # Oversized arbitrary world metadata must not bypass the hard cap.
        for key in ('active_plan', 'bootstrap_hint', 'last_tool_feedback'):
            w.pop(key, None)
        current.pop('sensor_calibration', None)
        w['task_targets'] = [_fields(t, ('object_id', 'task_label', 'description'))
                             for t in w['task_targets'][:2]]
    if size() > limit:
        raise ValueError('Essential memory context exceeds bounded projection')
    return {'task': deepcopy(observation.get('task', '')), 'memory_state': packet}

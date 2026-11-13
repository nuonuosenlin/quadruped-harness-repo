"""Synthetic public RGB-D/tool evidence only, no simulator or paid API."""
from copy import deepcopy
import json

import numpy as np
import pytest

from go2_demo.memory import AsyncMemory, MemoryRules, PACKET_KEYS, read_state, state_packet
from go2_demo.memory_perception import task_targets
from go2_demo.memory_planning import MemoryPlanningHarness, PublicObservationAdapter
from go2_demo.runner import run_episode
from go2_demo.scenarios import get_scenario
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend


def sensors(frame='f1'):
    rgb = np.zeros((80, 100, 3), np.uint8)
    rgb[18:38, 12:32] = [10, 25, 220]
    rgb[20:46, 60:86] = [10, 210, 20]
    depth = np.full((80, 100), 2., dtype=float)
    k = np.array([[100., 0., 50.], [0., 100., 40.], [0., 0., 1.]])
    obs = {'image_id': frame, 'image_size': {'width': 100, 'height': 80}, 'tracked_points': [],
           'local_odometry': {'translation_m': [0., 0.], 'yaw_rad': 0., 'source': 'simulated_proprioception'},
           'robot_state': {'hidden_target': [99., 99.]}}
    return obs, {'rgb': rgb, 'depth_m': depth, 'intrinsics': k}


def adapter():
    return PublicObservationAdapter(task_targets('memory_ab_occluded_v1'))


def point_for(candidate, frame='f1', point_id='p1', confidence=.99):
    return {'point_id': point_id, 'image_id': frame, 'pixel_uv': candidate['pixel_uv'],
            'relative_xy_m': [2., .3], 'valid': True, 'confidence': confidence,
            'range_m': 2.02, 'bearing_rad': .15, 'source': 'rgbd_optical_flow'}


def test_public_task_labels_have_no_positions_and_candidates_are_not_beliefs():
    a = adapter()
    obs, sensor = sensors()
    current = a.current_observation(obs, **sensor)
    assert {x['task_label'] for x in current['target_candidates']} == {'A', 'B'}
    assert all(x['status'] == 'candidate_not_confirmed' for x in current['target_candidates'])
    assert 'hidden_target' not in json.dumps(current)
    assert 'xy' not in json.dumps(task_targets('memory_ab_occluded_v1'))
    assert task_targets('unknown-task') == []
    rules = MemoryRules()
    rules.update(a.payload(obs, 0, **sensor))
    assert rules.state['objects'] == []


@pytest.mark.parametrize('label', ['A', 'B'])
def test_track_and_geometry_promote_task_label_only_after_independent_frames(label, tmp_path):
    a = adapter()
    obs, sensor = sensors()
    candidate = next(c for c in a.current_observation(obs, **sensor)['target_candidates'] if c['task_label'] == label)
    point = point_for(candidate)
    rules = MemoryRules()
    rules.update(a.payload(obs, 1, [{'tool': 'track_point', 'status': 'succeeded', 'point': point}], **sensor))
    obj = next(o for o in rules.state['objects'] if o['object_id'] == f'task:{label}')
    assert obj['state'] == 'unknown' and obj['task_label'] == label
    # Re-reading the same frame via get_geometry is not new evidence.
    rules.update(a.payload(obs, 2, [{'tool': 'get_geometry', 'status': 'succeeded', 'points': [point]}], **sensor))
    assert obj['state'] == 'unknown' and len(obj['evidence_ids']) == 1
    obs2 = {**obs, 'image_id': 'f2'}
    point2 = {**point, 'image_id': 'f2'}
    rules.update(a.payload(obs2, 3, [{'tool': 'get_geometry', 'status': 'succeeded', 'points': [point2]}], **sensor))
    assert obj['state'] == 'confirmed' and len(obj['evidence_ids']) == 2
    assert obj['source'] == 'task_label_rgbd_tracking'
    u, v = point['pixel_uv']
    assert obj['camera_pose']['position_m'] == pytest.approx([(u - 50) * .02, (v - 40) * .02, 2.])
    assert obj['measurement_provenance']['motion_delta_used'] is False
    assert 'idealized_simulator' in obj['measurement_provenance']['reference_pose']
    assert next(o for o in state_packet(rules.state)['objects'] if o['object_id'] == f'task:{label}')['state'] == 'confirmed'
    path = tmp_path / 'memory.md'
    path.write_text(rules.document())
    assert next(o for o in read_state(path.read_text())['objects'] if o['object_id'] == f'task:{label}')['task_label'] == label


@pytest.mark.parametrize('case', ['ambiguous_color', 'invalid_depth', 'low_confidence', 'stale_frame', 'wrong_pixel'])
def test_unsupported_identity_or_geometry_never_creates_a_task_object(case):
    a = adapter()
    obs, sensor = sensors()
    c = next(c for c in a.current_observation(obs, **sensor)['target_candidates'] if c['task_label'] == 'B')
    p = point_for(c)
    if case == 'ambiguous_color':
        sensor['rgb'][55:70, 60:80] = [10, 210, 20]
    elif case == 'invalid_depth':
        sensor['depth_m'][:] = float('nan')
    elif case == 'low_confidence':
        p['confidence'] = .5
    elif case == 'stale_frame':
        p['image_id'] = 'old-frame'
    elif case == 'wrong_pixel':
        p['pixel_uv'] = [50, 60]
    payload = a.payload(obs, 0, [{'tool': 'track_point', 'status': 'succeeded', 'point': p}], **sensor)
    assert not any(o['object_id'] == 'task:B' for o in payload['objects'])


def test_motion_gt_feedback_is_archived_with_honest_source_not_promoted_to_navigation():
    obs, sensor = sensors()
    payload = adapter().payload(obs, 0, [{'tool': 'move_relative', 'status': 'succeeded',
        'measured': {'translation_start_frame_m': [.5, -.1], 'yaw_delta_rad': .02}}], **sensor)
    assert 'execution.displacement_m' not in payload['measurements']
    record = payload['actions'][0]['motion_feedback']
    assert record['source'] == 'tool_result.measured.simulator_ground_truth_delta'
    assert record['navigation_measurement'] is False
    rules = MemoryRules(); rules.update(payload)
    assert 'execution.displacement_m' not in state_packet(rules.state)['world']['measurements']


def test_empty_md_still_has_task_labels_fresh_candidates_and_safe_action_paths(tmp_path):
    memory = AsyncMemory(tmp_path / 'memory.md')
    try:
        a = adapter(); obs, sensor = sensors()
        planner = MemoryPlanningHarness(memory)
        context = planner.context('A then B', 0, a.current_observation(obs, **sensor), a.perception.labels)
        packet = context['memory_state']
        assert set(packet) == set(PACKET_KEYS)
        assert packet['objects'] == [] and len(packet['world']['task_targets']) == 2
        hint = packet['world']['bootstrap_hint']
        selection = Decision([ToolCall('select', 'track_point', hint['suggested_arguments'])],
                             assistant_content='Select a visible task-given target.')
        assert planner.prepare(selection, 0)[0] is None
        plan = {'subgoals': [{'subgoal_id': 'explore', 'description': 'scan current view',
                              'preconditions': [], 'completion': []}], 'branches': [], 'recovery': 'stop'}
        move = Decision([ToolCall('turn', 'turn', {'yaw_rad': .3})],
                        assistant_content=json.dumps({'plan': plan, 'subgoal_id': 'explore'}))
        assert planner.prepare(move, 0)[0] is None
        observe = ToolCall('observe', 'observe', {})
        for _ in range(2):
            planner.note_results([observe], [{'tool': 'observe', 'status': 'succeeded'}])
        feedback, _ = planner.prepare(Decision([observe]), 0)
        assert feedback['error_code'] == 'MEMORY_NO_PROGRESS'
        planner.note_results([observe], [feedback])
        assert planner.context('A then B', 0)['memory_state']['world']['last_tool_feedback'][0]['error_code'] == 'MEMORY_NO_PROGRESS'
    finally:
        memory.close()


def test_end_to_end_offline_bootstrap_tracks_confirms_then_moves_without_gt(tmp_path):
    class Backend(EpisodeBackend):
        def __init__(self):
            super().__init__()
            self.scenario = get_scenario('memory_ab_occluded_v1')

        def capture(self):
            frame = super().capture()
            _, sensor = sensors(frame.frame_id)
            frame.rgb = sensor['rgb']; frame.depth_m = sensor['depth_m']; frame.intrinsics = sensor['intrinsics']
            return frame

    class Planner:
        def __init__(self): self.turn = 0

        def decide(self, observation, image, tools, history, **kwargs):
            world = observation['memory_state']['world']
            assert image == '' and world['task_targets']
            current = world['current_observation']
            if self.turn == 0:
                c = next(c for c in current['target_candidates'] if c['task_label'] == 'B')
                call = ToolCall('pick', 'track_point', {'image_id': c['image_id'], 'u': c['pixel_uv'][0], 'v': c['pixel_uv'][1]})
                content = None
            elif self.turn == 1:
                assert world['last_tool_feedback'][0]['tool'] == 'track_point'
                call, content = ToolCall('fresh', 'observe', {}), None
            else:
                call = ToolCall('explore', 'move_relative', {'forward_m': .2, 'lateral_m': 0.})
                content = json.dumps({'plan': {'subgoals': [{'subgoal_id': 'scan', 'description': 'explore',
                    'preconditions': [], 'completion': []}], 'branches': [], 'recovery': 'stop'}, 'subgoal_id': 'scan'})
            self.turn += 1
            return Decision([call], assistant_content=content)

    backend = Backend()
    result = run_episode(backend, Planner(), mode='api', run_dir=tmp_path, memory_v1=True, max_model_calls=3)
    assert len(backend.moves) == 1
    state = read_state((tmp_path / 'memory.md').read_text())
    target = next(o for o in state['objects'] if o['object_id'] == 'task:B')
    assert target['state'] == 'confirmed'
    assert result['success'] is False  # A task score never comes from memory self-report.

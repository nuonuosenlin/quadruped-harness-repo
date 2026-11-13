"""Audit existing return-to-start data and geometry. Never execute a task.

Run from repository with the existing .venv. Optional --output-dir permits a
fresh reproduction without replacing earlier evidence. No API, key access,
policy stepping, task implementation, or changes to scene/source files.
"""

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

import mujoco
import numpy as np

ROOT = Path('/home/nuonuosenlin/Agent-harness')
assert Path.cwd().resolve() == ROOT
sys.path.insert(0, str(ROOT))
from go2_demo.memory import MemoryRules, state_packet
from go2_demo.memory_planning import PublicObservationAdapter
from go2_demo.scenarios import get_scenario

BASELINE = ROOT / 'runs/dashscope-validation-20261109-132737-c60cc5/20261109-212737-api-go_to_blue_ball-s0-e43663'
OLD_CHECK = ROOT / 'runs/memory-v1-demo-feasibility/candidate_preflight.py'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes():
    return {str(p.relative_to(ROOT)): digest(p)
            for folder in ('go2_demo', 'tests', 'scripts', 'docs')
            for p in sorted((ROOT / folder).rglob('*'))
            if p.is_file() and p.suffix in ('.py', '.sh', '.md')}


def rotation(yaw):
    return np.array([[math.cos(yaw), -math.sin(yaw)], [math.sin(yaw), math.cos(yaw)]])


def wrap(value):
    return math.atan2(math.sin(value), math.cos(value))


def body_rotation(yaw, state):
    # Native body_pitch_rad = asin(R[2,0]), opposite ZYX pitch sign.
    pitch, roll = -state['body_pitch_rad'], state['body_roll_rad']
    cp, sp, cr, sr, cy, sy = math.cos(pitch), math.sin(pitch), math.cos(roll), math.sin(roll), math.cos(yaw), math.sin(yaw)
    return np.array([[cy, -sy, 0.], [sy, cy, 0.], [0., 0., 1.]]) @ np.array(
        [[cp, 0., sp], [0., 1., 0.], [-sp, 0., cp]]) @ np.array(
        [[1., 0., 0.], [0., cr, -sr], [0., sr, cr]])


def source_location(filename, needle):
    p = ROOT / filename
    lines = p.read_text().splitlines()
    return {'path': str(p), 'line': next(i + 1 for i, line in enumerate(lines) if needle in line),
            'needle': needle}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'runs/memory-v1-demo-feasibility')
    args = parser.parse_args()
    out = args.output_dir.resolve()
    assert out.is_relative_to(ROOT / 'runs')
    out.mkdir(parents=True, exist_ok=True)
    for suffix in ('md', 'json'):
        assert not (out / f'return_to_start_preflight.{suffix}').exists(), 'Use a fresh --output-dir'
    branch = subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip()
    assert branch == 'memory-v1'
    before = source_hashes()
    status_before = subprocess.check_output(['git', 'status', '--porcelain'], text=True)

    manifest = json.loads((BASELINE / 'manifest.json').read_text())
    metrics = json.loads((BASELINE / 'metrics.json').read_text())
    rows = [json.loads(line) for line in (BASELINE / 'events.jsonl').read_text().splitlines()]
    trajectory = [json.loads(line) for line in (BASELINE / 'trajectory.jsonl').read_text().splitlines()]
    inputs = {r['turn']: (line, r) for line, r in enumerate(rows, 1) if r['event'] == 'model_input'}
    responses = {r['turn']: (line, r) for line, r in enumerate(rows, 1) if r['event'] == 'model_response'}
    results = {r['turn']: (line, r) for line, r in enumerate(rows, 1) if r['event'] == 'tool_results'}
    assert metrics['success'] and metrics['model_calls'] == 12
    assert manifest['model'] == 'deepseek-v4.1-flash' and manifest['seed'] == 0
    assert manifest['budgets']['history_turns'] == 6 and len(inputs) == len(responses) == len(results) == 12
    assert all(inputs[i][1]['history_turns'] == min(i, 6) for i in inputs)
    baseline_files = {name: digest(BASELINE / name) for name in ('manifest.json', 'metrics.json', 'events.jsonl', 'trajectory.jsonl')}

    # Recover the scoring-only world origin from simultaneous logged odometry
    # and privileged trajectory samples. This never becomes a planner input.
    origins, matched_world = [], {}
    for i, (_, row) in results.items():
        obs = row['next_observation']
        nearest = min(trajectory, key=lambda t: abs(t['sim_time_s'] - obs['sim_time_s']))
        if abs(nearest['sim_time_s'] - obs['sim_time_s']) > 1e-8:
            continue
        odom = obs['local_odometry']
        initial_yaw = wrap(nearest['yaw_rad'] - odom['yaw_rad'])
        initial_xy = np.array(nearest['base_xyz_m'][:2]) - rotation(initial_yaw) @ odom['translation_m']
        origins.append((initial_xy, initial_yaw))
        matched_world[i] = nearest
    start_xy, start_yaw = origins[0]
    origin_spread = max(float(np.linalg.norm(xy - start_xy)) for xy, _ in origins)
    assert origin_spread < 1e-10

    command_xy, measured_xy, command_yaw, measured_yaw = np.zeros(2), np.zeros(2), 0., 0.
    adapter = PublicObservationAdapter()
    rules = MemoryRules()
    first_obs = inputs[0][1]['observation']
    rules.update(adapter.payload(first_obs, 0))
    turns, motion_rows = [], []
    first_blue_pass = None
    target_xy = np.array(metrics['evaluation']['target_xy_m'])
    for i in range(12):
        call = responses[i][1]['calls'][0]
        result = results[i][1]['results'][0]
        obs = results[i][1]['next_observation']
        odom = obs['local_odometry']
        payload = adapter.payload(obs, i + 1, [result])
        rules.update(payload)
        measured = result.get('measured')
        if measured is not None and call['name'] in ('move_relative', 'turn'):
            measured_xy += rotation(measured_yaw) @ measured['translation_start_frame_m']
            measured_yaw = wrap(measured_yaw + measured['yaw_delta_rad'])
            arguments = call['arguments']
            command_xy += rotation(command_yaw) @ [arguments.get('forward_m', 0.), arguments.get('lateral_m', 0.)]
            command_yaw = wrap(command_yaw + arguments.get('yaw_rad', 0.))
            motion_rows.append({'decision': i + 1, 'tool': call['name'], 'arguments': arguments,
                'measured': measured, 'memory_adapter_action': payload['actions'][0],
                'command_vs_measured_position_error_m': measured['position_error_m'],
                'integrated_command_error_m': float(np.linalg.norm(command_xy - odom['translation_m'])),
                'integrated_measured_error_m': float(np.linalg.norm(measured_xy - odom['translation_m']))})
        world_xy = start_xy + rotation(start_yaw) @ odom['translation_m']
        delta = target_xy - world_xy
        distance = float(np.linalg.norm(delta))
        heading_error = abs(wrap(math.atan2(delta[1], delta[0]) - start_yaw - odom['yaw_rad']))
        robot = obs['robot_state']
        blue_pass = (abs(distance - 1.) <= .18 and heading_error <= .25
                     and robot['speed_mps'] < .12 and abs(robot['yaw_rate_radps']) < .25
                     and not robot['fallen'] and not metrics['evaluation']['collision'])
        if first_blue_pass is None and blue_pass:
            first_blue_pass = i + 1
        turns.append({'decision': i + 1, 'zero_based_turn': i, 'tool': call['name'],
                      'arguments': call['arguments'], 'status': result['status'],
                      'history_turns_logged': inputs[i][1]['history_turns'],
                      'retained_raw_decisions_at_input': list(range(max(1, i - 5), i + 1)),
                      'input_jsonl_line': inputs[i][0], 'response_jsonl_line': responses[i][0],
                      'result_jsonl_line': results[i][0], 'next_local_odometry': odom,
                      'blue_distance_m': distance, 'blue_heading_error_rad': heading_error,
                      'blue_geometric_and_stop_criteria_pass': bool(blue_pass),
                      'distance_to_start_m': float(np.linalg.norm(odom['translation_m'])),
                      'command_integration_error_m': float(np.linalg.norm(command_xy - odom['translation_m'])),
                      'measured_integration_error_m': float(np.linalg.norm(measured_xy - odom['translation_m']))})

    # Replay only recorded public evidence into the current pure memory rules;
    # no episode, dispatch or tool backend is run.
    ledger_actions = [e['action'] for e in rules.state['ledger'] if e['kind'] in ('action_executed', 'action_failed')]
    packet = state_packet(rules.state, 12)
    first_point = results[0][1]['results'][0]['point']
    memory_evidence = {'initial_observation_tracked_points': first_obs['tracked_points'],
                      'first_track_point_request': responses[0][1]['calls'][0],
                      'first_track_point_public_result': first_point,
                      'public_point_has_xyz': any(k in first_point for k in ('world', 'xyz_m', 'relative_xyz_m')),
                      'public_point_has_xy': 'relative_xy_m' in first_point,
                      'raw_motion_call_count_including_rejected': sum(t['tool'] in ('move_relative', 'turn') for t in turns),
                      'executed_measured_motion_count': len(motion_rows),
                      'motion_raw_and_memory_adapter_comparison': motion_rows,
                      'memory_action_ledger_sample': ledger_actions,
                      'memory_object_pose_dimensions': {o['object_id']: len(o['pose']['position_m']) for o in rules.state['objects']},
                      'memory_objects_at_return_boundary': [{k: o[k] for k in ('object_id', 'state', 'last_seen', 'pose', 'visual_feature')}
                                                            for o in rules.state['objects']],
                      'planner_packet_contains_ledger': 'ledger' in packet,
                      'planner_packet_object_ids': [o['object_id'] for o in packet['objects']],
                      'gaps': ['Runner has call arguments and full measured signed translation/yaw, but adapter receives only results and discards arguments/full vector/yaw.',
                               'Initial observation has zero tracked points. First selected point belongs to the blue goal, not a home landmark.',
                               'TrackedPoint.world is internal 3D; track_point/get_geometry expose only XY, and memory objects store two coordinates.',
                               'No saved origin landmark descriptor/relocalization path; visual_feature is only image_id/pixel_uv.',
                               'Current planner packet omits the action ledger and filters stale home candidates; no route/old-landmark retrieval tool exists.']}

    # Import the prior audit helper without executing its main(). Builds the
    # same static MuJoCo model; no policy stepping and no scene modification.
    spec = importlib.util.spec_from_file_location('existing_visibility_preflight', OLD_CHECK)
    geometry = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(geometry)
    checker = geometry.SceneCheck(get_scenario('go_to_blue_ball'))
    calibration = first_obs['sensor_calibration']

    def set_logged_pose(obs, turn=None, delta_yaw=0.):
        odom = obs['local_odometry']
        world_xy = start_xy + rotation(start_yaw) @ odom['translation_m']
        yaw = start_yaw + odom['yaw_rad'] + delta_yaw
        matrix = body_rotation(yaw, obs['robot_state'])
        quaternion = np.empty(4)
        mujoco.mju_mat2Quat(quaternion, matrix.reshape(-1))
        checker.data.qpos[:3] = [*world_xy, obs['robot_state']['body_height_m']]
        checker.data.qpos[3:7] = quaternion
        checker.data.qpos[checker.qids] = geometry.DEFAULT_ANGLES
        checker.data.qvel[:] = 0.
        mujoco.mj_forward(checker.model, checker.data)
        return world_xy, yaw

    def project_and_ray(point):
        origin = checker.data.cam_xpos[checker.camera_id].copy()
        orient = checker.data.cam_xmat[checker.camera_id].reshape(3, 3) @ np.diag([1., -1., -1.])
        difference = np.array(point) - origin
        camera = orient.T @ difference
        uv = ([319.5 + checker.focal * camera[0] / camera[2],
               179.5 + checker.focal * camera[1] / camera[2]] if camera[2] > .01 else None)
        hit_id = np.array([-1], dtype=np.int32)
        length = float(np.linalg.norm(difference))
        hit = mujoco.mj_ray(checker.model, checker.data, origin, difference / length,
                             checker.geomgroup, 1, -1, hit_id)
        hit_name = (mujoco.mj_id2name(checker.model, mujoco.mjtObj.mjOBJ_GEOM, int(hit_id[0]))
                    or f'unnamed_robot_geom_{int(hit_id[0])}') if hit_id[0] >= 0 else None
        return {'point_world_xyz_m': list(point), 'camera_coordinates_m': camera.tolist(),
                'inside_frustum': bool(uv is not None and 0 <= uv[0] < 640 and 0 <= uv[1] < 360),
                'pixel_uv_if_in_front': uv, 'ray_first_hit_geom': hit_name,
                'ray_first_hit_geom_id': int(hit_id[0]),
                'ray_hit_distance_m': float(hit), 'ray_target_distance_m': length,
                'ray_reaches_point_without_earlier_occluder': bool(hit < 0 or hit >= length - .005)}

    # Initial selected point can be identified by an offline scene ray. This
    # scoring/diagnostic GT point is not present in the public tool result.
    set_logged_pose(first_obs)
    camera_origin = checker.data.cam_xpos[checker.camera_id].copy()
    opt_rotation = checker.data.cam_xmat[checker.camera_id].reshape(3, 3) @ np.diag([1., -1., -1.])
    uv = first_point['pixel_uv']
    optical_ray = np.array([(uv[0] - 319.5) / checker.focal, (uv[1] - 179.5) / checker.focal, 1.])
    ray = opt_rotation @ optical_ray
    ray /= np.linalg.norm(ray)
    gid = np.array([-1], dtype=np.int32)
    length = mujoco.mj_ray(checker.model, checker.data, camera_origin, ray, checker.geomgroup, 1, -1, gid)
    first_point_gt = camera_origin + length * ray
    memory_evidence['first_selected_point_offline_identity'] = {
        'method': 'Diagnostic MuJoCo ray at the logged initial pixel; not data available to memory/planner',
        'first_hit_geom': mujoco.mj_id2name(checker.model, mujoco.mjtObj.mjOBJ_GEOM, int(gid[0])),
        'world_xyz_m': first_point_gt.tolist(),
        'horizontal_distance_to_start_m': float(np.linalg.norm(first_point_gt[:2] - start_xy))}

    # Inspect origin and its entire 1m disk. A negative camera-depth maximum
    # is a continuous proof that the whole ground disk is behind the camera,
    # independent of finite surface samples and independent of occlusion.
    visibility_poses = []
    checkpoints = [('first_blue_criteria', first_blue_pass - 1),
                   ('explicit_stop_before_finish', 10), ('after_finish_stop', 11)]
    for name, turn in checkpoints:
        obs = results[turn][1]['next_observation']
        for yaw_delta in (0., .6, -.6):
            world_xy, yaw = set_logged_pose(obs, turn, yaw_delta)
            origin = checker.data.cam_xpos[checker.camera_id].copy()
            orient = checker.data.cam_xmat[checker.camera_id].reshape(3, 3) @ np.diag([1., -1., -1.])
            forward = orient[:, 2]
            home = np.r_[start_xy, 0.]
            max_depth_disk = float(forward @ (home - origin) + np.linalg.norm(forward[:2]))
            max_depth_cylinder = max_depth_disk + max(0., float(forward[2]))
            # All fixed non-floor objects that could be called landmarks are
            # also checked, explicitly distinguishing the blue goal from home.
            object_views = {label['label']: checker.visible(label) for label in checker.labels}
            visibility_poses.append({'name': name, 'decision': turn + 1, 'turn_rad': yaw_delta,
                'body_world_xy_m': world_xy.tolist(), 'body_world_yaw_rad': yaw,
                'camera_world_xyz_m': origin.tolist(), 'origin_point': project_and_ray(home),
                'home_disk_radius_m': 1., 'home_disk_max_camera_forward_depth_m': max_depth_disk,
                'entire_home_disk_behind_camera': max_depth_disk < 0.,
                'home_region_height_range_m': [0., 1.],
                'home_cylinder_max_camera_forward_depth_m': max_depth_cylinder,
                'entire_home_cylinder_behind_camera': max_depth_cylinder < 0.,
                'initial_selected_point_projection': project_and_ray(first_point_gt),
                'existing_named_object_views': object_views})
    assert all(p['entire_home_disk_behind_camera'] for p in visibility_poses)
    assert all(p['entire_home_cylinder_behind_camera'] for p in visibility_poses)

    odom_before_finish = inputs[11][1]['observation']['local_odometry']
    translation = np.array(odom_before_finish['translation_m'])
    return_vector = -rotation(odom_before_finish['yaw_rad']).T @ translation
    point1_history = {'result': '通过', 'baseline_run': str(BASELINE), 'model': manifest['model'],
        'seed': 0, 'model_calls': metrics['model_calls'], 'history_turns': 6, 'turns': turns,
        'logged_input_history_sizes': [inputs[i][1]['history_turns'] for i in range(12)],
        'retained_before_decision_12': list(range(6, 12)),
        'hypothetical_retained_after_decision_12': list(range(7, 13)),
        'dropped_after_decision_12': list(range(1, 7)),
        'first_physical_blue_acceptance_decision': first_blue_pass,
        'history_if_return_started_after_first_acceptance': list(range(max(1, first_blue_pass - 5), first_blue_pass + 1)),
        'notes': ['12 is the observed run length including track requests, one rejected motion, stop and finish; not a minimum motion count.',
                  'Existing finish terminates the episode; a return transition is not implemented or run.',
                  'Raw early turns are truncated, but current cumulative odometry remains. Logged private reasoning has only counts, so no claim that all old facts are forgotten.']}
    point2_visibility = {'result': '通过', 'start_world_xy_m_scoring_only': start_xy.tolist(),
        'start_world_yaw_rad_scoring_only': start_yaw, 'origin_reconstruction_spread_m': origin_spread,
        'no_unique_start_marker': True,
        'fixed_scene_objects': ['scenario_target (blue sphere)', 'wrong_color_object (red box)', 'floor (repeating checker texture)'],
        'floor_material': {'builtin': 'checker', 'texrepeat': '12 12'},
        'poses': visibility_poses,
        'scope': 'Actual logged baseline blue-stop poses. All ground points within 1m of the start have negative optical depth even after +/-0.6rad. Existing goal objects can remain visible but are not home markers.',
        'limitations': ['No unique home descriptor is present; checker texture is repetitive.',
                       'Robot joints were not logged: frozen model uses default joints and logged body pose; behind-camera disk proof does not depend on joints.',
                       'This is offline geometry using archived GT for diagnostics, not a navigation implementation.']}
    point3_memory = {'result': '不通过', **memory_evidence}

    start_to_target = float(np.linalg.norm(target_xy - start_xy))
    final_distance = float(np.linalg.norm(np.array(metrics['evaluation']['base_xy_m']) - start_xy))
    point4_scoring = {'result': '通过', 'feasible_not_implemented': True,
        'origin_definition': 'First Harness capture after 1s initialization settling, not nominal reset [0,0].',
        'formula': 'norm(current_base_xy_GT - saved_initial_base_xy_GT) <= 1.0',
        'return_radius_m': 1., 'start_to_blue_center_m': start_to_target,
        'minimum_start_distance_of_any_blue_standoff_pose_m': start_to_target - 1.18,
        'blue_end_score_distance_to_start_m': final_distance,
        'return_radius_overlaps_blue_acceptance_region': start_to_target - 1.18 <= 1.,
        'required_phase_and_stop_gates': ['First pass blue independent distance/heading/stop/no-collision/no-fall checkpoint.',
            'Only then evaluate return distance <=1m, stopped speed<0.12m/s, abs yaw rate<0.25rad/s, no collision/fall over the whole round.',
            'Do not count the initial pose inside the 1m disk as return success; model finish is only a declaration.'],
        'interpretation': '1m is a meaningful coarse return region, not precise pose or visual relocalization. Independent GT scoring remains meaningful even if navigation drifts.'}
    drift = {'successful_move_translation_error_m': [x['measured']['position_error_m'] for x in motion_rows if x['tool'] == 'move_relative'],
        'successful_turn_yaw_error_rad': [x['measured']['heading_error_rad'] for x in motion_rows if x['tool'] == 'turn'],
        'command_integrated_xy_m': command_xy.tolist(), 'command_integrated_yaw_rad': command_yaw,
        'measured_motion_integrated_xy_m': measured_xy.tolist(), 'measured_motion_integrated_yaw_rad': measured_yaw,
        'command_error_before_explicit_stop_m': turns[9]['command_integration_error_m'],
        'measured_error_before_explicit_stop_m': turns[9]['measured_integration_error_m'],
        'command_error_after_finish_m': turns[11]['command_integration_error_m'],
        'measured_motion_error_after_stop_and_finish_m': turns[11]['measured_integration_error_m'],
        'command_yaw_error_before_stop_rad': abs(wrap(command_yaw - turns[9]['next_local_odometry']['yaw_rad'])),
        'critical_distinction': 'Execution tracking error is not odometry measurement drift. Signed measured feedback and cumulative odometry are computed from ideal simulator poses, not a noisy estimator.',
        'risk_assessment': 'Command-only integration already differs by about 0.30m outbound; blindly reversing commands has no guaranteed round-trip bound. Current ideal measured feedback removes observed motion accumulation error, except stop/finish settling not included in motion results. One seed/outbound log cannot estimate return noise, covariance or success probability. A 1m independent scoring disk remains meaningful but broad; current GT-derived cumulative odometry makes it an easy closed-loop signal for H0 as well.'}
    nav = {'recommended_if_data_were_complete': 'Measured-motion dead reckoning as primary; visual corrections only after real home landmarks are saved and relocalization is supported.',
        'command_inverse_only': 'Technically can issue inverse bounded move_relative/turn commands, but requested displacement differs from measured travel; full directional measured ledger and frame composition are required, not scalar length sums.',
        'visual_homing_current_status': 'Unavailable: no initial home track, no exposed XYZ, no distinctive saved descriptor or lost-track relocalization, and stale landmarks are filtered.',
        'combined_current_status': 'Not supported by current memory state and tools without additional data plumbing/retrieval/relocalization. No changes made.',
        'public_current_odometry_bypass': {'observation_before_finish': odom_before_finish,
            'home_vector_in_current_body_frame_m': return_vector.tolist(),
            'distance_from_current_observation_m': float(np.linalg.norm(return_vector)),
            'formula': '-R(local_yaw).T @ local_translation',
            'requires_early_history_or_memory': False,
            'source_audit': 'backend.capture uses _base_pose(); Harness.observation subtracts initial ground-truth base pose and rotates into initial yaw. Both H0 and H2 receive this ideal cumulative odometry.',
            'requires_private_evaluator_GT_access': False,
            'cumulative_pose_is_ideal_GT_derived': True,
            'strict_ban_on_ideal_cumulative_pose_would_be_met': False},
        'no_private_GT_navigation_possible_with_public_feedback': True,
        'memory_directional_route_retrieval_implemented': False,
        'GT_boundary_note': 'Public sensor/tool feedback is permitted by the existing interface. Simulator-derived measurements do not by themselves mean secret evaluator-GT access. The ideal cumulative start-relative pose nevertheless bypasses memory and makes this unsuitable as a memory-necessity or realistic drift test.'}

    locations = {
        'history_crop_runner': source_location('go2_demo/runner.py', 'history = history[-history_turns:]'),
        'history_crop_model': source_location('go2_demo/models.py', 'selected = history[-self.history_turns:]'),
        'initial_origin_private_storage': source_location('go2_demo/harness.py', 'self._initial_base_xy_yaw = tuple'),
        'public_ideal_odom': source_location('go2_demo/harness.py', 'initial_x, initial_y, initial_yaw ='),
        'sensor_frame_from_true_pose': source_location('go2_demo/backend.py', 'base_xy_yaw=np.array'),
        'measured_motion_from_true_pose': source_location('go2_demo/backend.py', 'translation_start_frame_m'),
        'internal_3d_backprojection': source_location('go2_demo/perception.py', 'def backproject'),
        'public_point_xy_only': source_location('go2_demo/perception.py', 'def describe'),
        'adapter_drops_full_motion_and_arguments': source_location('go2_demo/memory_planning.py', 'action = {k: deepcopy(result[k])'),
        'memory_packet_filters_history': source_location('go2_demo/memory.py', 'def state_packet'),
        'scoring_true_base_pose': source_location('go2_demo/backend.py', 'def evaluate')}
    after = source_hashes()
    assert before == after
    assert status_before == subprocess.check_output(['git', 'status', '--porcelain'], text=True)
    assert baseline_files == {name: digest(BASELINE / name) for name in baseline_files}
    conclusion = '不通过'
    report = {'conclusion': conclusion, 'branch': branch, 'api_calls': 0, 'key_reads': 0,
        'task_implemented': False, 'demo_executed': False, 'scene_modified': False,
        'baseline': {'run_dir': str(BASELINE), 'file_sha256': baseline_files, 'metrics': {
            k: metrics[k] for k in ('success', 'termination', 'model_calls', 'motion_calls', 'usage')},
            'initial_image': str(BASELINE / inputs[0][1]['image_path']),
            'blue_stop_image': str(BASELINE / inputs[11][1]['image_path'])},
        'checks': {'1_history_window': point1_history, '2_start_visibility': point2_visibility,
                   '3_memory_data': point3_memory, '4_independent_scoring': point4_scoring},
        'navigation': nav, 'drift': drift, 'source_locations': locations,
        'source_sha256_before': before, 'source_sha256_after': after,
        'reasons': ['Required directional command/result memory ledger is incomplete in current adapter.',
                    'Initial home tracks with exposed 3D position do not exist, and visual home relocalization/retrieval is missing.',
                    'Current H0 already receives ideal start-relative cumulative pose through its permitted public sensor interface, so history truncation does not establish external-memory necessity. If GT-only-scoring is intended to exclude this ideal cumulative channel, the current observation contract also fails that stricter condition.']}
    with (out / 'return_to_start_preflight.json').open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

    md = f'''# 回起点 demo 离线复核

结论：**不通过**。

本轮仅在 `{branch}` 分支读取本地源码与既有蓝球 seed 0 日志，做日志重放、静态视锥／射线计算和数据流核对；没有实现任务、运行 demo、执行运动策略、调用 API、读取密钥、修改场景或共享文档。源码哈希、git 状态与基线日志哈希在复核前后均一致。

## 四项必需条件

| 项目 | 结果 | 依据 |
|---|---|---|
| 1. 六回合历史窗口 | 通过 | 成功基线确为 12 次决策；早期原始回合确已裁掉，但累计里程计没有消失。 |
| 2. 起点不可见 | 通过 | 无唯一的起点标记；蓝球三个已达标日志姿态及各自 ±0.6rad 转向下，整个起点 1m 地面圆盘都在相机后方。 |
| 3. 记忆可记所需数据 | 不通过 | 原始调用／结果存在于 runner 日志，但当前记忆适配器丢掉指令参数、实测位移向量和 yaw；没有初始起点地标与公开 XYZ，也没有视觉重定位或路线检索出口。 |
| 4. 独立返回评分 | 通过 | 仿真能保存首帧真实机身位置并计算返回距离；≤1m 可作为粗粒度返回标准，须加阶段、停止和全程无碰撞跌倒门控。 |

## 1. 用真实基线核对历史

基线：[{BASELINE.name}]({BASELINE})。`metrics.json` 为 success=true、termination=finish、model_calls=12、motion_calls=6，模型 deepseek-v4.1-flash、seed 0；manifest 的 history_turns=6。逐次输入实际记录的历史长度为 `{point1_history['logged_input_history_sizes']}`。

| 决策（从 1 开始） | 工具 | 结果 | 输入历史长度 |
|---:|---|---|---:|
'''
    for t in turns:
        md += f"| {t['decision']} | {t['tool']} | {t['status']} | {t['history_turns_logged']} |\n"
    md += f'''
第 12 次输入保留第 6–11 次完整回合；若第 12 次之后有回程决策，则只剩第 7–12 次，原始第 1–6 次被裁掉，包括初始选点、第一次转向、第一段移动。这里第 5 次位移请求因向量长度超限而被拒绝，不能当成真实移动。

12 是这条基线的实际总决策数，并非几何上必须移动 12 次：按日志姿态与停止速度复算，第 **{first_blue_pass} 次**已首次满足蓝球距离／朝向／停止条件。若此时进入回程，原始第 1–3 次仍已掉出窗口。现有 finish 会结束 episode，因此“finish 后继续回程”只是窗口分析，未实现或执行。私有 reasoning 文本本来不落盘，不能宣称后续推理绝不复述旧事实；本报告只确认原始回合裁剪。

## 2. 起点与地标的视锥／遮挡检查

用与 candidate_preflight 相同的原始 MuJoCo 场景构造器和 mj_ray，不新增标记／遮挡物。通过既有 trajectory 与同一时刻 local_odometry 重建首个观测时刻的世界起点（仅供离线几何和评分）：XY=`{start_xy.tolist()}`，yaw=`{start_yaw:.9f}` rad。多次独立重建最大差异 `{origin_spread:.3g}` m。起点采用初始化站稳后的首帧，不能武断等同 reset 的 `[0,0]`。

现有固定物体只有蓝球、红色干扰方块和重复棋盘地面。没有 home／start 唯一标记；重复棋盘纹理不能作为唯一的回家标签。初始追踪到的蓝球也不等于起点地标。

| 蓝球日志检查点 | 原地转向 rad | 起点 1m 地面圆盘的最大相机前向深度 m | 结论 |
|---|---:|---:|---|
'''
    for p in visibility_poses:
        md += f"| {p['name']}（第 {p['decision']} 次） | {p['turn_rad']:+.1f} | {p['home_disk_max_camera_forward_depth_m']:.6f} | 整个圆盘在相机后方 |\n"
    md += f'''
深度上界采用 `forward·(home_center-camera) + 1m·norm(forward_xy)`，对圆盘是连续域上界；均小于 0，故不是“有限采样没找到”的推断。再加 `max(0, forward_z·1m)` 检查地面到 1m 高的整个起点圆柱，也全部在相机后方，涵盖起点机身参考点高度。JSON 另存起点、初始选点的投影和最近射线命中，以及现有固定物体的可见性；起点方向的数学射线可能先撞到相机后方的机器人自身，但视锥已经排除该方向，不能把这类射线当作相机观测。初始蓝球选点离起点约 `{memory_evidence['first_selected_point_offline_identity']['horizontal_distance_to_start_m']:.3f}` m，不是 home 地标，即使还在视野里也不能直接认作起点。

静态模型使用日志机身高度／俯仰／横滚与重建 yaw；日志没有关节角，故机器人关节沿用默认配置。圆盘在相机后方的证明不依赖关节遮挡，也不把静态几何当作实际回航成功。

## 3. 数据来源逐项核对

### (a) 移动账本

原始数据确实存在：runner 的 model_response.calls 保存工具名称、call_id 与 arguments；tool_results 保存 status、error_code、measured.translation_start_frame_m、measured.yaw_delta_rad、执行／停止反馈。共 7 次运动请求，其中 1 次被拒绝、6 次有真实运动测量（4 次 move_relative、2 次 turn）。

但当前 PublicObservationAdapter.payload 只接收 observation/results，不接收 decision.calls。它仅把 call_id/tool/status/error_code/deduplicated 和 stuck 等少量字段记为 action；实测平移只取模长 execution.displacement_m，丢失符号、二维向量及转角。MemoryRules 追加的是这个缩减后的 action，不是完整指令／结果账本。JSON 对每次运动并列保留原始指令、原始测量及实际 adapter action，不能把 events.jsonl 的完整运行日志冒充 memory.md 的记忆数据。

此外，state_packet 不传 ledger，当前工具没有读取旧路线或检索旧地标的接口。即使磁盘账本补全，也还需要任务层可检索的航迹／返回状态，而不是将全部历史塞入 prompt。本轮未补这些功能。

### (b) 起点地标及三维位置

最初 model_input 的 tracked_points 是 `[]`。第 1 次 track_point 选中的是蓝球上的 point-001，公开 relative_xy_m=`{first_point['relative_xy_m']}`；没有起点附近的地标被追踪。

PointTracker.backproject 内部能用深度与标定得到 3D world，但 describe／track_point／get_geometry 只公开 relative_xy_m、水平 range、bearing、pixel_uv 和 confidence，不公开 XYZ。记忆适配器 pose.position_m 也只写两维，不能声称已保存三维起点地图。初始 RGB 图像会写 PNG，深度与完整 SensorFrame 不落入这条基线日志；公开标定也没有内参 K。

当前 visual_feature 只有 image_id/pixel_uv，没有外观描述子；丢失点返回 null 几何，重新选点会生成新 ID，没有视觉重定位／关联到旧 home 点。point-001 在第 3 次决策后就丢失；离线重放到第 12 次时为 `{next(o['state'] for o in rules.state['objects'] if o['object_id']=='point-001')}`，过时对象也不会进入规划的有效 objects。

因此第 3 项不通过。二维地图足以支持平面航位推算，但这不等于满足本次明确要求的“初始起点地标及其三维位置”，也不能补上缺失的方向账本。

## 4. 独立评分与 1m 阈值

可用 `_base_pose()` 的真值记录首帧 `start_xy_GT`，评分时计算 `norm(current_xy_GT-start_xy_GT)`；相关真值只进入评估路径，不把目标坐标／成功布尔值提供给规划。当前 backend.evaluate 尚只评分单目标，本轮没有添加返回任务或修改 evaluator。

建议返回标准：先由独立测量确认蓝球点通过，再要求距起点 ≤1.0m、速度 <0.12m/s、绝对 yaw rate <0.25rad/s，且整轮无碰撞／跌倒。必须阶段门控，否则初始就在成功圆盘内会被误记为返回成功；finish 自述不计。

起点距蓝球中心 `{start_to_target:.6f}` m；蓝球任一合格 standoff 位姿距起点至少 `{start_to_target-1.18:.6f}` m，大于 1m。基线最终距起点 `{final_distance:.6f}` m，停在蓝球处不会直接通过返回条件。1m 是有效但较宽松的粗粒度返回阈值，不代表精确回到同一位姿或视觉闭环定位。

## 导航方式、GT 边界与漂移

从现有工具语义看，回程应优先用**带方向的实测运动航位推算**，有可靠 home 特征并能重定位时再用视觉修正。原则上只用原始公开工具的实测平移／转角即可组合 SE(2) 航迹、计算返回方向，不需要规划去读私有 `_base_pose()` 或 evaluator 真值；不能只累加请求值或标量路长。move_relative / turn 可输出有界原子动作，track_point / get_geometry 可以提供当前有效点的几何；但当前 memory.md 到规划的数据链没有完整方向账本，不能据此宣称该记忆回航已经可用。视觉回航缺初始 home 特征／重定位，二者结合也缺少上述数据与检索环节。

只反向重放请求值不可靠。四次成功平移相对请求的终点误差分别为 `{[round(x,6) for x in drift['successful_move_translation_error_m']]}` m；两次转向误差 `{[round(x,6) for x in drift['successful_turn_yaw_error_rad']]}` rad。命令航位推算在最后一次运动后的位置误差为 **{drift['command_error_before_explicit_stop_m']:.6f}m**、yaw 误差 `{drift['command_yaw_error_before_stop_rad']:.6f}` rad。相反，累加实测向量／实测转角，在该时刻误差仅 `{drift['measured_error_before_explicit_stop_m']:.3g}` m；这是因为这些反馈本来就是从仿真真值差分计算的，不是证明了真实里程计无漂移。专门 stop 与 finish 的站稳运动不含在 move/turn 测量中，合计带来约 `{drift['measured_motion_error_after_stop_and_finish_m']:.6f}` m 的账本缺口。

一条去程日志不能给出回程漂移上界、噪声模型或成功率；反向动作的噪声可能不对称，不能假设自动抵消。1m 真值评分仍然有意义，漂移只影响能否通过；但不能据此宣称视觉回航或精确导航。无需在本轮凭空添加噪声模型或重跑仿真。

**额外的关键混杂因素：现有 H0 的当前观测已经含起点相对累计里程计。** 在第 12 次决策输入里，translation=`{translation.tolist()}`，yaw=`{odom_before_finish['yaw_rad']:.9f}`。只用这一帧即可算回起点向量 `-R(yaw)^T·translation = {return_vector.tolist()}` m，距起点 `{float(np.linalg.norm(return_vector)):.6f}` m，不需要早期历史、外部记忆或可见起点标记。

其来源不是带噪声估计器：backend.capture 把真实 `_base_pose()` 放入 SensorFrame.base_xy_yaw，Harness.observation 与首帧真值作差并旋转，manifest 也标为 idealized_simulated_proprioception_relative_to_episode_start。原始 move/turn 实测反馈同样由真实起止位姿差分得到。**这些是现有协议明确允许的公开传感器／工具反馈；使用它们，不等于规划偷偷读取私有评分 GT。** 保留现状，原则上可只凭公开反馈闭环回航而不另读私有 GT；问题是这条累计位姿通道对 H0 也开放，绕过了外部记忆需求，并且不能用来验证真实估计器漂移。若“GT 只评分”的含义还包括排除理想累计位姿通道，则当前观察协议不满足该更严格边界；不能把它改称为带噪声的真实里程计。本轮不擅自改变观察协议。

## 证据与复现

- [JSON 证据]({out / 'return_to_start_preflight.json'})：12 回合、历史边界、射线／连续域深度上界、原始与适配器账本对照、离线记忆重放、积分误差、源码定位和哈希。
- [复现脚本]({out / 'return_to_start_preflight.py'})；从仓库根目录使用既有环境运行：`.venv/bin/python runs/memory-v1-demo-feasibility/return_to_start_preflight.py --output-dir runs/memory-v1-demo-feasibility/return-recheck`。新目录避免覆盖证据。
- 原始蓝球 [events.jsonl]({BASELINE / 'events.jsonl'})、[metrics.json]({BASELINE / 'metrics.json'})、[trajectory.jsonl]({BASELINE / 'trajectory.jsonl'})。

结论：**不通过**。第 3 项必需数据链不完整；另外，H0 的当前理想累计里程计绕过了历史遗忘／外部记忆需求。若要求连理想累计位姿也不得用于决策，则现有观察协议还不满足这一更严格边界。按要求停在离线复核，不改场景、不实现任务、不跑 demo、不调用 API。
'''
    with (out / 'return_to_start_preflight.md').open('x', encoding='utf-8') as stream:
        stream.write(md)
    destination = out / 'return_to_start_preflight.py'
    if Path(__file__).resolve() != destination:
        shutil.copyfile(__file__, destination)
    print(json.dumps({'conclusion': conclusion, 'checks': {k: v['result'] for k, v in report['checks'].items()},
        'baseline_decisions': 12, 'first_blue_acceptance_decision': first_blue_pass,
        'command_error_before_stop_m': drift['command_error_before_explicit_stop_m'],
        'measured_error_before_stop_m': drift['measured_error_before_explicit_stop_m'],
        'output_markdown': str(out / 'return_to_start_preflight.md')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

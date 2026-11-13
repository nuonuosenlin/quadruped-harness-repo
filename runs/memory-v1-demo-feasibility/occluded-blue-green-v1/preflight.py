"""Offline scene audit. No model, credentials, sequential task, or ablation.

Run geometry first. --physical is a separate, explicitly gated sensor/dynamics
fixture using fixed local waypoints, not a planner or a task episode.
"""

import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import shutil
import sys

os.environ.setdefault('MUJOCO_GL', 'egl')
import mujoco
import numpy as np

ROOT = Path('/home/nuonuosenlin/Agent-harness')
assert Path.cwd().resolve() == ROOT
sys.path.insert(0, str(ROOT))
from go2_demo.backend import MujocoGo2Backend, wrap_angle
from go2_demo.harness import Harness
from go2_demo.scenarios import get_scenario, list_scenarios
from go2_demo.types import ToolCall

OUT = ROOT / 'runs/memory-v1-demo-feasibility/occluded-blue-green-v1'
REFERENCE_OUT = OUT
SCENE = get_scenario('memory_ab_occluded_v1')


def save(name, data):
    with (OUT / name).open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def prior_helper():
    path = OUT.parent / 'candidate_preflight.py'
    spec = importlib.util.spec_from_file_location('prior_scene_audit', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_original_catalog():
    before = json.loads((OUT / 'before.json').read_text())['scenarios']
    now = json.loads(json.dumps([asdict(s) for s in list_scenarios()]))
    for row in now:
        assert row.pop('floor_half_size_m') is None
        assert row.pop('offline_only') is False
    assert now == before
    return {'original_catalog_entries_unchanged': len(now),
            'original_supported_scenes_unchanged': sum(s.supported for s in list_scenarios()),
            'demo_excluded_from_default_catalog_and_suite': SCENE.task_id not in [s.task_id for s in list_scenarios()]}


def make_checker():
    prior = prior_helper()

    class Checker(prior.SceneCheck):
        def make_labels(self, xy):
            return [self.label('A_blue_sphere', xy, ['scenario_target']),
                    self.label('B_green_box', [1.8, .6], ['memory_goal_b'])]

    return Checker(SCENE)


def geometry_audit():
    catalog = verify_original_catalog()
    checker = make_checker()
    a, b = checker.labels
    assert a['xy'] == [6.4, 0.] and b['xy'] == [1.8, .6]
    initial_b = checker.visible(b)
    mount_norm = float(np.linalg.norm(checker.model.cam_pos[checker.camera_id]))
    camera_radius = 1.18 + mount_norm
    # Enclose every camera XY regardless of stop azimuth, heading error,
    # camera orientation or subsequent rotation (even a full 360 degrees).
    cx = [6.4 - camera_radius, 6.4 + camera_radius]
    cy = [-camera_radius, camera_radius]
    bx, by = [1.72, 1.88], [.42, .78]
    plane = 3.8
    fractions = [(plane - x_b) / (x_c - x_b) for x_b, x_c in itertools.product(bx, cx)]
    ts = [min(fractions), max(fractions)]
    crossings = [(1 - t) * y_b + t * y_c for t, y_b, y_c in itertools.product(ts, by, cy)]
    cross_y = [min(crossings), max(crossings)]
    wall_id = checker.names['memory_drawers_body']
    wall_position = checker.data.geom_xpos[wall_id]
    wall_size = checker.model.geom_size[wall_id]
    np.testing.assert_allclose(wall_position, [3.8, 0., 1.], atol=1e-12)
    np.testing.assert_allclose(wall_size, [.22, 2., 1.])
    # Kinematic upper bound for a grounded stop: root-to-foot link lengths
    # plus contact sphere radius, then full camera mounting displacement.
    foot_bounds = []
    for gid in range(checker.model.ngeom):
        body = int(checker.model.geom_bodyid[gid])
        name = mujoco.mj_id2name(checker.model, mujoco.mjtObj.mjOBJ_BODY, body) or ''
        if (not name.endswith('_calf') or checker.model.geom_type[gid] != mujoco.mjtGeom.mjGEOM_SPHERE
                or abs(float(checker.model.geom_size[gid, 0]) - .022) > 1e-8):
            continue
        bound = float(np.linalg.norm(checker.model.geom_pos[gid])) + .022
        while body != checker.base_id:
            bound += float(np.linalg.norm(checker.model.body_pos[body]))
            body = int(checker.model.body_parentid[body])
        foot_bounds.append(bound)
    assert len(foot_bounds) == 4
    camera_height_bound = max(foot_bounds) + mount_norm
    proof = {'camera_mount_full_norm_m': mount_norm, 'camera_xy_disk_radius_m': camera_radius,
        'camera_x_interval_m': cx, 'camera_y_interval_m': cy,
        'B_x_interval_m': bx, 'B_y_interval_m': by, 'B_z_interval_m': [0., .4],
        'separating_cabinet_plane_x_m': plane, 'segment_fraction_interval': ts,
        'all_possible_ray_crossing_y_interval_m': cross_y,
        'cabinet_body_position_m': wall_position.tolist(), 'cabinet_body_half_size_m': wall_size.tolist(),
        'grounded_root_height_bound_m': max(foot_bounds),
        'grounded_camera_height_bound_m': camera_height_bound,
        'cabinet_height_m': 2., 'minimum_y_edge_margin_m': min(2. + cross_y[0], 2. - cross_y[1]),
        'top_margin_m': 2. - max(.4, camera_height_bound),
        'continuous_domain': 'r in [0.82,1.18], all azimuths, heading error in [-0.25,0.25], turn in [-0.6,0.6]; bound actually covers every yaw.',
        'proof': 'All B-to-camera line segments cross x=3.8 strictly inside the solid cabinet Y/Z bounds. Thus every B surface is occluded, regardless of camera frustum. Camera height is bounded by grounded robot kinematics; if a camera were below z=0, the finite ground platform blocks the ray instead.',
        'scope': 'Physically grounded planar locomotion stops on the flat platform; no airborne/teleported poses or new height-control capabilities.'}
    proof['passed'] = bool(bx[1] < plane < cx[0] and cross_y[0] > -2. and cross_y[1] < 2.
                           and camera_height_bound < 2.)

    # A ray sweep is supplementary evidence, not a universal proof.
    views, visible_views, first_hits = 0, 0, {}
    sample_points = []
    gid = checker.names['memory_goal_b']
    size = checker.model.geom_size[gid]
    position = checker.data.geom_xpos[gid].copy()
    for axis in range(3):
        other = [i for i in range(3) if i != axis]
        for sign in (-1, 1):
            for u, v in itertools.product((-.8, 0., .8), repeat=2):
                p = position.copy()
                p[axis] += sign * size[axis]
                p[other[0]] += u * size[other[0]]
                p[other[1]] += v * size[other[1]]
                sample_points.append(p)
    for alpha in np.linspace(0, 2 * math.pi, 72, endpoint=False):
        for radius, error, turn in itertools.product((.82, 1., 1.18), (-.25, 0., .25), (-.6, 0., .6)):
            xy = [6.4 - radius * math.cos(alpha), -radius * math.sin(alpha)]
            checker.set_pose(xy, alpha + error + turn)
            origin = checker.data.cam_xpos[checker.camera_id].copy()
            optical = checker.data.cam_xmat[checker.camera_id].reshape(3, 3) @ np.diag([1., -1., -1.])
            positive = False
            for p in sample_points:
                camera = optical.T @ (p - origin)
                if camera[2] <= .01:
                    continue
                u, v = 319.5 + checker.focal * camera[0] / camera[2], 179.5 + checker.focal * camera[1] / camera[2]
                if not (0 <= u < 640 and 0 <= v < 360):
                    continue
                direction = p - origin
                direction /= np.linalg.norm(direction)
                hit = np.array([-1], dtype=np.int32)
                mujoco.mj_ray(checker.model, checker.data, origin, direction, checker.geomgroup, 1, -1, hit)
                hit_name = mujoco.mj_id2name(checker.model, mujoco.mjtObj.mjOBJ_GEOM, int(hit[0])) if hit[0] >= 0 else 'none'
                first_hits[hit_name or 'unnamed_robot_geom'] = first_hits.get(hit_name or 'unnamed_robot_geom', 0) + 1
                positive |= int(hit[0]) == gid
            views += 1
            visible_views += int(positive)

    start_distance = math.dist([0., 0.], a['xy'])
    travel = start_distance - 1.18
    history = {'start_to_A_center_m': start_distance, 'minimum_net_travel_to_A_region_m': travel,
               'tool_requested_translation_limit_m': .6, 'successful_position_error_limit_m': .1,
               'maximum_net_translation_per_successful_motion_m': .7,
               'minimum_successful_motion_decisions': math.ceil(travel / .7),
               'request_length_only_lower_bound': math.ceil(travel / .6),
               'passed': travel > 6 * .7,
               'scope': 'Normal successful bounded motions; not a bound for uncontrolled failed actions. Actual physical probe call count is reported separately.'}
    paths = {'to_A': [[0., 0.], [0., -2.8], [5.4, -2.8], [5.4, 0.]],
             'to_B': [[5.4, 0.], [5.4, -2.8], [.8, -2.8], [.8, .6]]}
    contact_failures, outside = [], []
    samples = 0
    for label, points in paths.items():
        for start, end in zip(points, points[1:]):
            for fraction in np.linspace(0, 1, math.ceil(math.dist(start, end) / .1) + 1):
                xy = (1 - fraction) * np.array(start) + fraction * np.array(end)
                checker.set_pose(xy, 0.)
                samples += 1
                if not checker.contact_free():
                    contact_failures.append({'path': label, 'xy': xy.tolist()})
                if abs(xy[0]) > 7.2 or abs(xy[1]) > 5.2:
                    outside.append(xy.tolist())
    reachable = {'paths_in_initial_local_coordinates_m': paths, 'static_pose_samples': samples,
                 'environment_contact_failures': contact_failures, 'platform_clearance_failures': outside,
                 'passed': not contact_failures and not outside,
                 'cabinet_lower_route_lateral_gap_m': .8,
                 'note': 'Static geometric clearance is preliminary; dynamic movement is checked separately.'}
    passed = bool(initial_b['visible_positive_certificate'] and proof['passed'] and visible_views == 0
                  and history['passed'] and reachable['passed'])
    report = {'conclusion': '通过' if passed else '不通过', 'scene_id': SCENE.task_id, 'seed': 0,
              'scene': asdict(SCENE), 'platform_dimensions_m': [16., 12.],
              'target_asset_dimensions_unchanged': True, 'cabinet_source': 'existing _PROPS[drawers] with size/position scaling',
              'A_B_center_distance_m': math.dist(a['xy'], b['xy']),
              'initial_B_visibility': initial_b, 'continuous_occlusion_proof': proof,
              'supplementary_ray_sweep': {'view_count': views, 'B_visible_view_count': visible_views,
                                          'frustum_ray_first_hits': first_hits},
              'history_window': history, 'reachability_geometry': reachable, 'original_catalog': catalog,
              'api_calls': 0, 'key_reads': 0, 'sequential_task_implemented': False}
    save('scene.json', asdict(SCENE))
    mujoco.mj_saveLastXML(str(OUT / 'scene.xml'), checker.model)
    save('geometry_preflight.json', report)
    # Scaled plan view; a code-native diagram, not a synthetic camera image.
    (OUT / 'layout.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="650" viewBox="0 0 900 650">
<rect width="900" height="650" fill="#fafafa"/><g transform="translate(450 325) scale(48 -48)">
<rect x="-8" y="-6" width="16" height="12" fill="#edf2f6" stroke="#526474" stroke-width=".03"/>
<polyline points="0,0 0,-2.8 5.4,-2.8 5.4,0 5.4,-2.8 .8,-2.8 .8,.6" fill="none" stroke="#b7701b" stroke-width=".055" stroke-dasharray=".15,.1"/>
<rect x="3.58" y="-2" width=".44" height="4" fill="#8f694d"/>
<circle cx="6.4" cy="0" r="1.18" fill="none" stroke="#678ae3" stroke-width=".025"/>
<circle cx="6.4" cy="0" r=".82" fill="none" stroke="#678ae3" stroke-width=".025"/>
<circle cx="6.4" cy="0" r=".12" fill="#163fda"/><rect x="1.72" y=".42" width=".16" height=".36" fill="#149e35"/>
<circle cx="0" cy="0" r=".1" fill="#222"/>
</g><g font-family="sans-serif" font-size="16" fill="#263542">
<text x="25" y="30">Offline scene: 16 x 12 m flat platform; existing blue/green assets</text>
<text x="420" y="315">Start (0,0)</text><text x="520" y="280">B (1.8,0.6)</text>
<text x="714" y="300">A (6.4,0)</text><text x="572" y="215">Cabinet: 0.44 x 4 x 2 m</text>
<text x="455" y="490">Dashed route: offline clearance/dynamics fixture only</text></g></svg>''', encoding='utf-8')
    print(json.dumps({'conclusion': report['conclusion'], 'initial_B_visible': initial_b['visible_positive_certificate'],
        'continuous_proof': proof, 'ray_sweep': report['supplementary_ray_sweep'], 'history': history,
        'reachability_geometry': reachable}, ensure_ascii=False, indent=2), flush=True)
    return 0 if passed else 1


def physical_audit():
    geometry = json.loads((OUT / 'geometry_preflight.json').read_text())
    assert geometry['conclusion'] == '通过', 'Stop: geometry requirement failed'
    assert not (OUT / 'physical_preflight.json').exists(), 'Do not rerun/overwrite a physical audit'
    from PIL import Image
    backend = harness = None
    actions, points, checkpoints = [], [], []
    report = {'conclusion': '不通过', 'seed': 0, 'api_calls': 0, 'key_reads': 0,
              'probe_type': 'offline fixed-waypoint sensor/dynamics fixture, not a sequential task implementation',
              'navigation_data': 'existing public local_odometry only; known fixed local clearance waypoints; no private GT in controller',
              'GT_scope': 'Static geometry and independent checkpoint distance/heading diagnostics only. Existing public odometry remains ideal simulator-derived; its design is unchanged.',
              'actions': actions, 'points': points, 'checkpoint_diagnostics': checkpoints}
    count = 0

    def call(name, arguments):
        nonlocal count
        count += 1
        result = harness.dispatch(ToolCall(f'offline-probe-{count:03d}', name, arguments))
        actions.append({'index': count, 'tool': name, 'arguments': arguments, 'result': result,
                        'local_odometry': harness.observation()['local_odometry']})
        if result['status'] != 'succeeded':
            raise RuntimeError(f'Offline probe tool {name} failed: {result.get("error_code")}')
        return result

    def track_color(label, color):
        rgb = harness.frame.rgb.astype(float)
        if color == 'green':
            mask = (rgb[:, :, 1] > 1.5 * rgb[:, :, 0]) & (rgb[:, :, 1] > 1.4 * rgb[:, :, 2]) & (rgb[:, :, 1] > 50)
        else:
            mask = (rgb[:, :, 2] > 1.5 * rgb[:, :, 0]) & (rgb[:, :, 2] > 1.3 * rgb[:, :, 1]) & (rgb[:, :, 2] > 50)
        pixels = np.argwhere(mask)
        if len(pixels) < 8:
            raise RuntimeError(f'Given task color {color} is not visible at {label}')
        center = np.median(pixels, axis=0)
        v, u = pixels[np.argmin(np.linalg.norm(pixels - center, axis=1))]
        Image.fromarray(harness.frame.rgb).save(OUT / f'{label}.png')
        result = call('track_point', {'image_id': harness.frame.frame_id, 'u': int(u), 'v': int(v)})
        geometries = call('get_geometry', {})['points']
        point = next(p for p in geometries if p['point_id'] == result['point']['point_id'])
        if not point['valid'] or point['relative_xy_m'] is None:
            raise RuntimeError(f'No valid current geometry for {label}')
        points.append({'label': label, 'color_fixture': color,
                       'method': 'Task-given color mask only, not a generic semantic detector or scene-GT pixel selector',
                       'pixel_uv': [int(u), int(v)], 'point': point})

    def waypoint(xy):
        for _ in range(30):
            obs = harness.observation()
            odom = obs['local_odometry']
            delta = np.array(xy) - odom['translation_m']
            if np.linalg.norm(delta) <= .105:
                return
            yaw = odom['yaw_rad']
            if abs(yaw) > .08:
                call('turn', {'yaw_rad': float(np.clip(-yaw, -.5, .5))})
                continue
            command = np.array([[math.cos(yaw), math.sin(yaw)], [-math.sin(yaw), math.cos(yaw)]]) @ delta
            command *= min(1., .55 / np.linalg.norm(command))
            call('move_relative', {'forward_m': float(command[0]), 'lateral_m': float(command[1])})
        raise RuntimeError('Fixed waypoint fixture did not converge')

    def scoring_diagnostic(label, target_xy):
        # Deliberately only here: private GT never feeds waypoint/track logic.
        position, yaw, _ = backend._base_pose()
        delta = np.array(target_xy) - position[:2]
        distance = float(np.linalg.norm(delta))
        heading = abs(wrap_angle(math.atan2(delta[1], delta[0]) - yaw))
        speed = float(np.linalg.norm(backend.data.qvel[:2]))
        yaw_rate = abs(float(backend.data.qvel[5]))
        row = {'label': label, 'distance_m': distance, 'heading_error_rad': heading,
               'speed_mps': speed, 'abs_yaw_rate_radps': yaw_rate,
               'collision': bool(backend._collision_steps), 'fallen': bool(backend._fallen_ever),
               'base_xy_m_scoring_only': position[:2].tolist(),
               'target_xy_m_scoring_only': list(target_xy),
               'checkpoint_criteria_pass': bool(abs(distance - 1.) <= .18 and heading <= .25
                    and speed < .12 and yaw_rate < .25 and not backend._collision_steps and not backend._fallen_ever),
               'not_a_task_success_metric': True}
        checkpoints.append(row)
        if not row['checkpoint_criteria_pass']:
            raise RuntimeError(f'Offline checkpoint diagnostic {label} fails: distance={distance}, heading={heading}')

    try:
        backend = MujocoGo2Backend(ROOT / 'assets', seed=0, viewer=False, scenario=SCENE)
        harness = Harness(backend, SCENE.instruction)
        backend.deadline_monotonic = __import__('time').monotonic() + 240.
        backend.sim_deadline_s = harness.frame.sim_time_s + 300.
        track_color('initial_B', 'green')
        for xy in geometry['reachability_geometry']['paths_in_initial_local_coordinates_m']['to_A'][1:]:
            waypoint(xy)
        call('stop', {})
        report['successful_motion_calls_before_A'] = sum(a['tool'] in ('move_relative', 'turn') for a in actions)
        track_color('at_A', 'blue')
        scoring_diagnostic('A', [6.4, 0.])
        if report['successful_motion_calls_before_A'] <= 6:
            raise RuntimeError('A physical probe used <=6 motion calls')
        for xy in geometry['reachability_geometry']['paths_in_initial_local_coordinates_m']['to_B'][1:]:
            waypoint(xy)
        call('stop', {})
        track_color('at_B', 'green')
        scoring_diagnostic('B', [1.8, .6])
        report['conclusion'] = '通过'
    except Exception as exc:
        report['failure'] = {'type': type(exc).__name__, 'message': str(exc)}
    finally:
        if backend is not None:
            try:
                report['cleanup_stop'] = backend.stop()
                report['physics_trace_rows'] = len(backend.trajectory)
                report['total_collision_steps'] = backend._collision_steps
                report['fallen'] = backend._fallen_ever
            finally:
                backend.close()
        save('physical_preflight.json', report)
    print(json.dumps({k: report[k] for k in report if k not in ('actions', 'points')}, ensure_ascii=False, indent=2), flush=True)
    return 0 if report['conclusion'] == '通过' else 1


def main():
    global OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--physical', action='store_true')
    parser.add_argument('--output-dir', type=Path, default=OUT,
                        help='fresh sibling directory for reproduction without overwriting evidence')
    args = parser.parse_args()
    OUT = args.output_dir.resolve()
    assert OUT.parent == REFERENCE_OUT.parent, 'Use a sibling directory under memory-v1-demo-feasibility'
    OUT.mkdir(parents=True, exist_ok=True)
    if not (OUT / 'before.json').exists():
        shutil.copyfile(REFERENCE_OUT / 'before.json', OUT / 'before.json')
    destination = OUT / 'preflight.py'
    if Path(__file__).resolve() != destination:
        shutil.copyfile(__file__, destination)
    return physical_audit() if args.physical else geometry_audit()


if __name__ == '__main__':
    raise SystemExit(main())

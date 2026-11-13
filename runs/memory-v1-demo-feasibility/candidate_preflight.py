"""Offline counterexample certificates for unchanged existing demo scenes.

No model client, key file, policy execution, renderer, GUI, or network. Uses the
exact local scene builder and MuJoCo ray intersections including static objects,
robot visual meshes, glyphs, and rotated furniture/gate geometries.
"""

from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

import mujoco
import numpy as np

ROOT = Path.cwd().resolve()
assert ROOT == Path('/home/nuonuosenlin/Agent-harness')
sys.path.insert(0, str(ROOT))
from go2_demo.backend import MujocoGo2Backend, wrap_angle
from go2_demo.scenarios import list_scenarios

OUTPUT = ROOT / 'runs/memory-v1-demo-feasibility'
BODY_HEIGHT = .34
DEFAULT_ANGLES = np.array([.1, .8, -1.5, -.1, .8, -1.5, .1, 1., -1.5, -.1, 1., -1.5])


def code_hashes():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for folder in ('go2_demo', 'tests', 'scripts', 'docs')
            for p in sorted((ROOT / folder).rglob('*'))
            if p.is_file() and p.suffix in ('.py', '.sh', '.md')}


def write_new(path, value):
    with path.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def surface_points(model, gid, glyph=False):
    size = model.geom_size[gid]
    kind = model.geom_type[gid]
    if glyph:
        return [np.array([-size[0], y * size[1], z * size[2]])
                for y in (-.6, 0., .6) for z in (-.6, 0., .6)]
    if kind == mujoco.mjtGeom.mjGEOM_BOX:
        points = []
        for axis in range(3):
            other = [i for i in range(3) if i != axis]
            for sign in (-1, 1):
                for u, v in itertools.product(np.linspace(-.95, .95, 5), repeat=2):
                    p = np.zeros(3)
                    p[axis] = sign * size[axis]
                    p[other[0]], p[other[1]] = u * size[other[0]], v * size[other[1]]
                    points.append(p)
        return points
    if kind == mujoco.mjtGeom.mjGEOM_SPHERE:
        return [size[0] * np.array([math.sin(phi) * math.cos(theta),
                                    math.sin(phi) * math.sin(theta), math.cos(phi)])
                for phi in np.linspace(.15, math.pi - .15, 9)
                for theta in np.linspace(0, 2 * math.pi, 24, endpoint=False)]
    if kind == mujoco.mjtGeom.mjGEOM_CYLINDER:
        r, h = size[:2]
        points = [np.array([r * math.cos(t), r * math.sin(t), z])
                  for t in np.linspace(0, 2 * math.pi, 32, endpoint=False)
                  for z in (-.95 * h, 0., .95 * h)]
        points.extend(np.array([fraction * r * math.cos(t), fraction * r * math.sin(t), sign * h])
                      for sign in (-1, 1) for fraction in (0., .5, .95)
                      for t in np.linspace(0, 2 * math.pi, 16, endpoint=False))
        return points
    raise ValueError(f'Unsupported target surface type {kind}')


class SceneCheck:
    def __init__(self, scenario):
        # Build the existing scene unchanged, without initializing a locomotion
        # policy, stepping physics, opening a renderer, or loading credentials.
        self.scenario = scenario
        backend = MujocoGo2Backend.__new__(MujocoGo2Backend)
        backend.asset_dir = ROOT / 'assets'
        backend.scenario = scenario
        backend._target_xy = np.array(scenario.target.xy, dtype=float)
        if scenario.target_jitter_m:
            backend._target_xy += np.random.default_rng(0).uniform(
                -scenario.target_jitter_m, scenario.target_jitter_m, size=2)
        backend._environment_geom_names = []
        self.model = backend._make_model()
        self.data = mujoco.MjData(self.model)
        self.names = {mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_GEOM, gid): gid
                      for gid in range(self.model.ngeom)
                      if mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_GEOM, gid)}
        self.environment = {self.names[n] for n in backend._environment_geom_names}
        self.base_id = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_BODY, 'base')
        self.camera_id = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_CAMERA, 'front_rgbd')
        self.qids = [self.model.jnt_qposadr[mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_JOINT, n)]
                     for n in MujocoGo2Backend.joint_names]
        self.geomgroup = mujoco.MjvOption().geomgroup.copy()
        self.focal = 180 / math.tan(math.radians(float(self.model.cam_fovy[self.camera_id])) / 2)
        self.set_pose([0., 0.], 0.)
        self.labels = self.make_labels(backend._target_xy)
        for label in self.labels:
            points = []
            for gid in label['visibility_ids']:
                rotation = self.data.geom_xmat[gid].reshape(3, 3)
                for p in surface_points(self.model, gid, label['kind'] == 'letter'):
                    points.append((gid, self.data.geom_xpos[gid] + rotation @ p))
            label['samples'] = points

    def label(self, label, xy, names, kind='object'):
        ids = {self.names[n] for n in names}
        visible = ids
        if kind == 'letter':
            visible = {gid for n, gid in self.names.items()
                       if any(n.startswith(prefix + '_glyph_') for prefix in names)}
            assert visible
        return {'label': label, 'xy': [float(x) for x in xy], 'geom_ids': ids,
                'visibility_ids': visible, 'geom_names': names, 'kind': kind}

    def make_labels(self, target_xy):
        scenario = self.scenario
        if scenario.category == 'distinguish':
            letters = [self.label(scenario.target.letter, target_xy, ['scenario_target'], 'letter')]
            letters.extend(self.label(o.letter, o.position[:2], [o.name], 'letter')
                           for o in scenario.objects if o.letter)
            return sorted(letters, key=lambda x: x['label'])
        if scenario.category == 'go_avoid':
            prop = scenario.task_id.removeprefix('go_avoid_texture_')
            names = [o.name for o in scenario.objects if o.name != 'target_support']
            return [self.label(prop, [1.65, 0.], names, 'furniture'),
                    self.label('red_marker', target_xy, ['scenario_target'])]
        if scenario.category == 'go_through':
            return [self.label('gate', [scenario.passage_x, scenario.passage_center_y],
                               [o.name for o in scenario.objects if o.name.startswith('gate_')], 'gate'),
                    self.label('reference_marker', target_xy, ['scenario_target'])]
        primary = f'{scenario.target.color}_{scenario.target.kind}'
        other = next(o for o in scenario.objects if o.role == 'distractor')
        return [self.label(primary, target_xy, ['scenario_target']),
                self.label(other.name, other.position[:2], [other.name])]

    def set_pose(self, xy, yaw):
        self.data.qpos[:3] = [*xy, BODY_HEIGHT]
        self.data.qpos[3:7] = [math.cos(yaw / 2), 0., 0., math.sin(yaw / 2)]
        self.data.qpos[self.qids] = DEFAULT_ANGLES
        self.data.qvel[:] = 0.
        mujoco.mj_forward(self.model, self.data)

    def contact_free(self):
        return not any(int(c.geom1) in self.environment or int(c.geom2) in self.environment
                       for c in self.data.contact)

    def visible(self, label):
        origin = self.data.cam_xpos[self.camera_id].copy()
        rotation = self.data.cam_xmat[self.camera_id].reshape(3, 3) @ np.diag([1., -1., -1.])
        evidence, blockers, pixels, hit_geoms = [], Counter(), set(), set()
        frustum_count = 0
        us, vs = [], []
        for intended_gid, point in label['samples']:
            camera = rotation.T @ (point - origin)
            if camera[2] <= .01:
                continue
            u = 319.5 + self.focal * camera[0] / camera[2]
            v = 179.5 + self.focal * camera[1] / camera[2]
            us.append(float(u)); vs.append(float(v))
            if not (2 <= u < 638 and 2 <= v < 358):
                continue
            frustum_count += 1
            direction = point - origin
            direction /= np.linalg.norm(direction)
            hit_id = np.array([-1], dtype=np.int32)
            distance = mujoco.mj_ray(self.model, self.data, origin, direction,
                                     self.geomgroup, 1, -1, hit_id)
            gid = int(hit_id[0])
            if distance >= 0 and gid in label['visibility_ids']:
                pixels.add((round(u), round(v)))
                hit_geoms.add(gid)
                if len(evidence) < 6:
                    evidence.append({'sample_world_xyz_m': point.tolist(), 'pixel_uv': [float(u), float(v)],
                                     'ray_first_hit': mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_GEOM, gid),
                                     'ray_distance_m': float(distance)})
            else:
                blocker = mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_GEOM, gid) if gid >= 0 else 'no_hit'
                blockers[blocker or f'robot_geom_{gid}'] += 1
        # Positive evidence must span multiple pixels; a letter also needs three
        # separate glyph cells. No finite negative sampling result is a proof.
        positive = len(pixels) >= 12 and (label['kind'] != 'letter' or len(hit_geoms) >= 3)
        return {'visible_positive_certificate': positive, 'frustum_surface_samples': frustum_count,
                'unoccluded_unique_sampled_pixels': len(pixels), 'visible_geom_count': len(hit_geoms),
                'B_projected_u_range': [min(us), max(us)] if us else None,
                'B_projected_v_range': [min(vs), max(vs)] if vs else None,
                'occluding_geom_samples': dict(blockers), 'unoccluded_rays': evidence,
                'camera_world_xyz_m': origin.tolist()}

    def counterexample(self, first, second):
        nominal = math.atan2(first['xy'][1], first['xy'][0])
        relative = [0., .4, -.4, .8, -.8, 1.2, -1.2, math.pi/2, -math.pi/2, math.pi]
        angles = [nominal + x for x in relative] + list(np.linspace(-math.pi, math.pi, 73))
        checked = 0
        for alpha in angles:
            for radius in (1., 1.17, .83):
                xy = [first['xy'][0] - radius * math.cos(alpha),
                      first['xy'][1] - radius * math.sin(alpha)]
                for error in (0., .24, -.24):
                    yaw = alpha + error
                    self.set_pose(xy, yaw)
                    if not self.contact_free():
                        continue
                    for turn in (0., .6, -.6):
                        # Require collision-free intermediate static orientations
                        # too. This does not claim an executed locomotion result.
                        if turn:
                            if not all(self.rotation_clear(xy, yaw + t)
                                       for t in np.linspace(0, turn, 7)):
                                continue
                        self.set_pose(xy, yaw + turn)
                        checked += 1
                        result = self.visible(second)
                        if result['visible_positive_certificate']:
                            measured_distance = math.dist(first['xy'], xy)
                            measured_error = abs(wrap_angle(math.atan2(first['xy'][1] - xy[1],
                                first['xy'][0] - xy[0]) - yaw))
                            assert .82 <= measured_distance <= 1.18 and measured_error <= .25 + 1e-9
                            return {'body_xy_m': xy, 'yaw_before_turn_rad': wrap_angle(yaw),
                                    'turn_rad': turn, 'yaw_after_turn_rad': wrap_angle(yaw + turn),
                                    'A_distance_m': measured_distance, 'A_heading_error_rad': measured_error,
                                    'A_distance_heading_pass_before_turn': True,
                                    'static_environment_contact_free': True,
                                    'velocity_set_to_zero': True, 'body_height_m': BODY_HEIGHT,
                                    'evaluated_view_count': checked, **result}
        return {'evaluated_view_count': checked, 'visible_positive_certificate': False}

    def rotation_clear(self, xy, yaw):
        self.set_pose(xy, yaw)
        return self.contact_free()

    def check_pairs(self):
        pairs = []
        for first, second in itertools.permutations(self.labels, 2):
            self.set_pose([0., 0.], 0.)
            initial = self.visible(second)
            witness = self.counterexample(first, second)
            rejected = witness['visible_positive_certificate']
            row = {'A': first['label'], 'B': second['label'], 'A_xy_m': first['xy'], 'B_xy_m': second['xy'],
                   'target_separation_m': math.dist(first['xy'], second['xy']),
                   'B_geom_names': second['geom_names'],
                   'condition_a_positive_certificate': initial['visible_positive_certificate'],
                   'condition_b_rejected_by_counterexample': rejected,
                   'condition_c_scene_unchanged': True,
                   'status': 'rejected_b' if rejected else 'uncertified_requires_continuous_proof',
                   'reason': ('B has unobstructed rays inside the frustum at a valid A stop pose'
                              + (' after one permitted turn' if witness.get('turn_rad') else ' without turning'))
                             if rejected else 'No positive witness found; finite sampling cannot certify universal invisibility',
                   'poses': [{'name': 'initial', 'body_xy_m': [0., 0.], 'yaw_rad': 0., **initial},
                             {'name': 'A_stop_counterexample', **witness}]}
            pairs.append(row)
            print(f'{self.scenario.task_id}: {row["A"]} -> {row["B"]}: {row["status"]}, '
                  f'initial_B={initial["visible_positive_certificate"]}, turn={witness.get("turn_rad")}', flush=True)
        return pairs


def main():
    branch = subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip()
    assert branch == 'memory-v1'
    before = code_hashes()
    status_before = subprocess.check_output(['git', 'status', '--porcelain'], text=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    assert not (OUTPUT / 'candidate_preflight.json').exists(), 'Do not overwrite earlier audit'
    reports = []
    scenes = sorted((s for s in list_scenarios() if s.supported),
                    key=lambda s: ({'distinguish': 0, 'go_avoid': 1}.get(s.category, 2), s.task_id))
    for scenario in scenes:
        checker = SceneCheck(scenario)
        report = {'method': 'Unmodified MuJoCo model + actual camera frustum + nearest-surface ray intersections',
                  'scene_id': scenario.task_id, 'category': scenario.category, 'seed': 0,
                  'camera_horizontal_half_fov_deg': math.degrees(math.atan(320 / checker.focal)),
                  'pairs': checker.check_pairs()}
        write_new(OUTPUT / f'geometry_preflight_{scenario.task_id}.json', report)
        reports.append(report)
    after = code_hashes()
    assert before == after, 'Source files changed during audit'
    assert status_before == subprocess.check_output(['git', 'status', '--porcelain'], text=True)
    rows = [p for scene in reports for p in scene['pairs']]
    summary = {'method': 'Offline visibility counterexample audit, not an API episode or policy success claim',
               'seed': 0, 'branch': branch, 'scene_count': len(reports), 'ordered_pair_count': len(rows),
               'rejected_by_positive_counterexample': sum(p['condition_b_rejected_by_counterexample'] for p in rows),
               'certified_valid_pairs': [], 'scene_models_modified': False, 'api_calls': 0,
               'candidate_scope': 'Named existing targets, labelled A/B/C signs, distractor objects, furniture assemblies and gate assemblies within each unchanged scene; no cross-scene merges, no support/handle/glyph cells as independent goals; blue-ball/green-cube pair excluded.',
               'unsupported_scenes_excluded': [s.task_id for s in list_scenarios() if not s.supported],
               'proof_notes': ['To disprove universal condition (b), one valid A pose with unoccluded visible B rays suffices.',
                               'Letters require direct first-hit rays to multiple glyph cells, not only to a blank sign back.',
                               'Negative surface/pose sampling is never treated as proof of invisibility.',
                               'Body z=0.34 m, existing reset joint configuration, zero velocity; static collision checks exclude environment contacts at A and during sampled turn orientations. No gait/stop stability, reachability, or complete task success is claimed.'],
               'source_sha256_before': before, 'source_sha256_after': after,
               'scenes': reports}
    assert all(p['condition_b_rejected_by_counterexample'] for p in rows), 'Unresolved candidates need additional proof'
    write_new(OUTPUT / 'candidate_preflight.json', summary)
    text = ['# Existing-scene memory demo feasibility audit', '',
            f'Branch: `{branch}`. Seed: 0. {len(reports)} unchanged scenes, {len(rows)} ordered pairs.', '',
            'All candidates fail universal condition (b) by an explicit positive visibility counterexample. '
            'No candidate certified; stage 2 not started. No API calls, key reads, viewer, or scene edits.', '',
            'MuJoCo rays use the unchanged actual scene including furniture rotations, sign glyphs, floor and robot geometry. '
            'Letters require glyph visibility. Static poses are geometry checks, not executed policy episodes.', '',
            '| Scene | First A | Second B | B visible from start (positive certificate) | Turn at A | Distance to A | Heading error | Rejection |',
            '|---|---|---|---|---:|---:|---:|---|']
    for scene in reports:
        for p in scene['pairs']:
            w = p['poses'][1]
            text.append(f'| {scene["scene_id"]} | {p["A"]} | {p["B"]} | '
                        f'{p["condition_a_positive_certificate"]} | {w["turn_rad"]:+.2f} | '
                        f'{w["A_distance_m"]:.3f} | {w["A_heading_error_rad"]:.3f} | {p["reason"]} |')
    text.extend(['', 'Support geometries and arbitrary points on the floor were not promoted to task targets. '
                 'Crawl tasks remain unsupported and were excluded. The rejected blue-ball/green-cube composition was not reused.', '',
                 'Full evidence: candidate_preflight.json and geometry_preflight_<scene_id>.json. '
                 'Each positive witness includes pose, turn, camera position, image coordinates, first-hit geometry and ray distance.', '',
                 'Source hashes and git status verified unchanged.'])
    with (OUTPUT / 'candidate_preflight.md').open('x', encoding='utf-8') as stream:
        stream.write('\n'.join(text) + '\n')
    shutil.copyfile(__file__, OUTPUT / 'candidate_preflight.py')
    print(json.dumps({k: summary[k] for k in ('scene_count', 'ordered_pair_count',
          'rejected_by_positive_counterexample', 'certified_valid_pairs', 'api_calls')}, indent=2))


if __name__ == '__main__':
    main()

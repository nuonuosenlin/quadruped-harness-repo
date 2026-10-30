"""One LIBERO touch/adjust episode. LLM sees text and numeric keypoints only."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time

import cv2
import mujoco
import numpy as np
from PIL import Image

from geometry import TOOLS, relation_geometry, vec3
from text_client import TextClient
from protocol import Progress

ROOT = Path(r'D:\RoboHarnessSim')
TARGET = 'alphabet_soup_1'
THRESHOLD = 0.03


def dump(value):
    return json.dumps(value, ensure_ascii=True, allow_nan=False,
        default=lambda x: x.tolist() if isinstance(x, np.ndarray) else x.item())


class Harness:
    def __init__(self, out):
        from libero.libero import benchmark, get_libero_path
        from libero.libero.envs import OffScreenRenderEnv
        from robosuite.utils import camera_utils
        self.camera_utils = camera_utils
        self.out = out
        self.env = None
        self.steps = 0
        self.trajectories = {}
        self.used = set()
        self.anchor = None
        self.keypoint = None
        self.executions = 0
        self.touch_solved = False
        suite = benchmark.get_benchmark_dict()['libero_10']()
        self.task = suite.get_task(0)
        try:
            self.env = OffScreenRenderEnv(bddl_file_name=os.path.join(get_libero_path('bddl_files'),
                self.task.problem_folder, self.task.bddl_file), camera_heights=256,
                camera_widths=256, camera_depths=True, camera_segmentations='instance')
            self.env.seed(0)
            self.env.reset()
            self.obs = self.env.set_init_state(suite.get_task_init_states(0)[0])
            for _ in range(10):
                self.obs, _, _, _ = self.env.step(np.zeros(7))
            self.robot = self.env.robots[0]
            self.controller = self.robot.controller
            c = self.controller
            if not c.use_delta or c.control_dim != 6 or len(self.env.env.action_spec[0]) != 7:
                raise RuntimeError('Unexpected controller contract')
            if not np.allclose(c.output_max[:3], [0.05]*3):
                raise RuntimeError('Unverified translation scaling')
            self.mask_id = list(self.env.env.model.instances_to_ids).index(TARGET) + 1
            self.K = camera_utils.get_camera_intrinsic_matrix(self.env.sim, 'agentview', 256, 256)
            self.T = camera_utils.get_camera_extrinsic_matrix(self.env.sim, 'agentview')
            self.start_orientation = self.env.sim.data.site_xmat[self.robot.eef_site_id].reshape(3,3).copy()
            self.snapshot('before')
        except Exception:
            if self.env is not None:
                self.env.close()
            raise

    def event(self, value):
        with (self.out / 'simulation.jsonl').open('a', encoding='utf-8') as f:
            f.write(dump(value) + '\n')

    def aligned(self):
        seg = np.squeeze(self.obs['agentview_segmentation_instance'])[::-1].copy()
        depth = np.squeeze(self.camera_utils.get_real_depth_map(self.env.sim,
            self.obs['agentview_depth']))[::-1].copy()
        return seg, depth

    def bbox(self):
        seg, _ = self.aligned()
        y, x = np.where(seg == self.mask_id)
        if not len(x):
            raise ValueError('Target not visible')
        return [int(x.min()), int(y.min()), int(x.max()+1), int(y.max()+1)]

    def track_keypoint(self, bbox, name):
        if name != TARGET or len(bbox) != 4 or any(type(x) is not int for x in bbox):
            raise ValueError('Only target name and integer bbox supported')
        x0, y0, x1, y1 = bbox
        if not (0 <= x0 < x1 <= 256 and 0 <= y0 < y1 <= 256):
            raise ValueError('Invalid top-left xyxy bbox')
        seg, depth = self.aligned()
        visible = (seg == self.mask_id).astype(np.uint8)
        # Erode silhouettes to reject depth/mask mixed boundary pixels.
        valid = cv2.erode(visible, np.ones((3,3), np.uint8)).astype(bool)
        roi = np.zeros_like(valid)
        roi[y0:y1, x0:x1] = True
        valid &= roi & np.isfinite(depth) & (depth > 0) & (depth < 5)
        y, x = np.where(valid)
        if len(x) < 5:
            raise ValueError('Insufficient unoccluded target depth pixels')
        pixels = np.vstack([x, y, np.ones(len(x))])
        camera_points = (np.linalg.inv(self.K) @ pixels) * depth[y,x]
        world = (self.T @ np.vstack([camera_points, np.ones(len(x))]))[:3].T
        reference = self.eef() if self.anchor is None else self.anchor
        index = int(np.argmin(np.linalg.norm(world - reference, axis=1)))
        # Pick an actual eroded visible surface pixel; no object pose/centroid truth.
        point = world[index]
        if self.anchor is not None and np.linalg.norm(point - self.anchor) > 0.03:
            raise ValueError('Target surface anchor lost/occluded (>3cm association gate)')
        if self.anchor is None:
            self.anchor = point.copy()
        self.keypoint = {'name': TARGET, 'position': point.tolist(), 'frame': 'world',
            'unit': 'm', 'pixel_uv': [int(x[index]), int(y[index])], 'bbox': list(bbox),
            'visible_pixels': int(len(x)), 'anchor_drift_m': float(np.linalg.norm(point-self.anchor)),
            'source': 'privileged_instance_mask_and_metric_depth'}
        return self.keypoint.copy()

    def eef(self):
        return vec3(self.obs['robot0_eef_pos']).copy()

    def ik(self, points):
        # Separate MjData: planning never teleports or advances the live environment.
        model = self.env.sim.model._model
        data = mujoco.MjData(model)
        data.qpos[:] = self.env.sim.data.qpos
        c = self.controller
        qp, qv = np.asarray(c.qpos_index), np.asarray(c.qvel_index)
        limits = model.jnt_range[np.asarray(c.joint_index)]
        sid = self.robot.eef_site_id
        solutions = []
        for target in points:
            for _ in range(100):
                mujoco.mj_forward(model, data)
                current = data.site_xmat[sid].reshape(3,3)
                rot_error = 0.5 * sum(np.cross(current[:,i], self.start_orientation[:,i]) for i in range(3))
                error = np.r_[target-data.site_xpos[sid], rot_error]
                if np.linalg.norm(error[:3]) <= 0.003 and np.linalg.norm(error[3:]) <= 0.04:
                    break
                jp, jr = np.zeros((3,model.nv)), np.zeros((3,model.nv))
                mujoco.mj_jacSite(model, data, jp, jr, sid)
                J = np.vstack([jp[:,qv], jr[:,qv]])
                dq = J.T @ np.linalg.solve(J @ J.T + 0.001*np.eye(6), error)
                data.qpos[qp] = np.clip(data.qpos[qp] + np.clip(dq,-0.08,0.08), limits[:,0]+0.001, limits[:,1]-0.001)
            mujoco.mj_forward(model, data)
            residual = float(np.linalg.norm(target-data.site_xpos[sid]))
            if residual > 0.008:
                raise ValueError('IK position residual exceeds 8mm: %.6f' % residual)
            solutions.append({'qpos_rad': data.qpos[qp].tolist(), 'position_residual_m': residual})
        return solutions

    def solve_constraint(self, keypoint_A, keypoint_B, relation):
        if keypoint_A != 'eef' or keypoint_B != TARGET or self.keypoint is None:
            raise ValueError('Track target first; use eef and alphabet_soup_1')
        if relation not in ('touch', 'adjust'):
            return {'status': 'not_robot_validated', 'relation': relation,
                    'detail': 'Geometry functions implemented/tested; axis keypoints and IK execution not validated. No trajectory issued.'}
        if self.executions == 0 and relation != 'touch':
            raise ValueError('First approach must use touch')
        if self.executions > 0 and relation != 'adjust':
            raise ValueError('Use adjust for subsequent approach correction')
        geometry = relation_geometry({'position': self.eef()}, self.keypoint, relation)
        goal = vec3(geometry['position'])
        if np.any(goal < [-0.45,-0.4,0.43]) or np.any(goal > [0.4,0.4,1.0]):
            raise ValueError('Goal outside conservative workspace')
        start = self.eef()
        count = max(1, int(np.ceil(np.linalg.norm(goal-start)/0.01)))
        points = [start+(goal-start)*i/count for i in range(1,count+1)]
        solutions = self.ik(points)
        traj = 'traj_%03d' % (len(self.trajectories)+1)
        record = {'traj': traj, 'relation': relation, 'start': start.tolist(),
            'goal': goal.tolist(), 'waypoints_world_m': [p.tolist() for p in points],
            'ik': solutions, 'orientation_world': self.start_orientation.tolist(),
            'created_sim_step': self.steps, 'collision_checked': False}
        self.trajectories[traj] = record
        (self.out / (traj+'.json')).write_text(dump(record), encoding='utf-8')
        return {'traj': traj, 'relation': relation, 'waypoints': count,
                'goal_world_m': np.round(goal,5).tolist(), 'ik_max_residual_m': max(x['position_residual_m'] for x in solutions)}

    def execute_trajectory(self, traj):
        if traj not in self.trajectories or traj in self.used:
            raise ValueError('Unknown or consumed trajectory')
        record = self.trajectories[traj]
        if record['created_sim_step'] != self.steps:
            raise ValueError('Stale trajectory; replan')
        self.used.add(traj)
        before = self.eef()
        start_step = self.steps
        for point in record['waypoints_world_m']:
            target = vec3(point)
            for _ in range(12):
                if self.steps >= 900:
                    raise RuntimeError('Simulation control step ceiling reached')
                delta = target-self.eef()
                if np.linalg.norm(delta) < 0.003:
                    break
                rotation = self.env.sim.data.site_xmat[self.robot.eef_site_id].reshape(3,3)
                rot_error = 0.5 * sum(np.cross(rotation[:,i], self.start_orientation[:,i]) for i in range(3))
                desired = np.r_[np.clip(delta,-0.0125,0.0125), np.clip(rot_error,-0.05,0.05)]
                c = self.controller
                arm = (desired-(c.output_max+c.output_min)/2) / ((c.output_max-c.output_min)/(c.input_max-c.input_min)) + (c.input_max+c.input_min)/2
                action = np.r_[np.clip(arm,c.input_min,c.input_max), -1.0]
                self.obs, reward, done, info = self.env.step(action)
                self.steps += 1
                self.event({'sim_step': self.steps, 'traj': traj, 'action_osc_pose': action,
                            'eef_world_m': self.eef(), 'reward': float(reward), 'done': bool(done)})
                if not np.isfinite(self.eef()).all():
                    raise RuntimeError('Nonfinite robot state')
                if done:
                    raise RuntimeError('Environment terminated; no further action')
        self.executions += 1
        return {'traj': traj, 'executed_control_steps': self.steps-start_step,
                'eef_before_m': np.round(before,5).tolist(), 'eef_after_m': np.round(self.eef(),5).tolist(),
                'waypoint_goal_error_m': float(np.linalg.norm(self.eef()-np.array(record['goal'])))}

    def check_success(self):
        tracked = self.track_keypoint(self.bbox(), TARGET)
        distance = float(np.linalg.norm(self.eef()-np.array(tracked['position'])))
        return {'success': bool(distance <= THRESHOLD), 'distance_m': distance,
                'threshold_m': THRESHOLD, 'criterion': 'eef_to_tracked_visible_surface_distance',
                'keypoints': {'eef': np.round(self.eef(),6).tolist(), TARGET: np.round(tracked['position'],6).tolist()},
                'bddl_success': bool(self.env.check_success()), 'physical_contact_claimed': False}

    def state(self, last):
        check = self.check_success()
        return {'scene': self.task.name, 'goal': 'Approach soup visible surface; distance <=0.03m. Basket goal is not the subtask.',
                'frame': 'world', 'unit': 'm', 'bbox_xyxy_top_left': self.bbox(),
                'keypoints': check['keypoints'], 'distance_m': round(check['distance_m'],6),
                'success': check['success'], 'executions': self.executions,
                'available_traj': [x for x in self.trajectories if x not in self.used], 'last_tool_result': last}

    def snapshot(self, label):
        Image.fromarray(self.obs['agentview_image'][::-1]).save(self.out / (label+'_rgb.png'))
        seg, depth = self.aligned()
        np.savez_compressed(str(self.out / (label+'_geometry.npz')), depth_m=depth, instance_mask=seg, K=self.K, T_camera_to_world=self.T)

    def close(self):
        self.env.close()


SYSTEM = """You decide actions for one LIBERO distance subtask using exactly one function call per turn. All inputs are text and numeric coordinates, world metres. Success is EEF within 0.03m of the soup visible surface, not contact or basket completion. The observation contains persistent workflow state: treat its phase as authoritative and NEVER restart the workflow. phase=track: obtain track_keypoint using supplied bbox. phase=plan: solve_constraint(eef,alphabet_soup_1) using workflow.legal_relation exactly. phase=execute: execute workflow.pending_traj exactly. After any execution the next planning relation is adjust, never touch. Use observed results; do not invent trajectory IDs or actions. check_success may refresh evidence but two calls without phase progress stop the episode. Prior function result and any persistent error are supplied. Local tools handle geometry, IK and control; you make decisions only."""


def main():
    if shutil.disk_usage(str(ROOT)).free < 10*1024**3:
        raise RuntimeError('Disk reserve below 10 GiB')
    candidates = sorted((ROOT/'harness/runs').glob('api_*/result.json'), reverse=True)
    if not candidates:
        raise RuntimeError('No API preflight result; run harness/run-api-probe.ps1 first')
    preflight_path = candidates[0]
    preflight = json.loads(preflight_path.read_text(encoding='utf-8'))
    if preflight['status'] != 'passed':
        raise RuntimeError('API preflight gate failed')
    out = ROOT/'harness/runs'/('touch_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    out.mkdir(parents=True, exist_ok=False)
    source = out/'source'
    source.mkdir()
    manifest = []
    for path in sorted(Path(__file__).resolve().parent.glob('*.py')):
        shutil.copy2(str(path),str(source/path.name))
        manifest.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (out/'source_manifest.json').write_text(dump(manifest),encoding='utf-8')
    client = TextClient(preflight['model'])
    progress = Progress()
    report = {'status': 'initializing', 'revision': 'persistent_phase_v2',
        'model': client.model, 'api_preflight': str(preflight_path),
        'previous_episode': None, # Historical original-machine evidence is described in reports.
        'episode_count': 1, 'seed': 0, 'initial_state_index': 0, 'max_llm_steps': 12,
        'text_only': True, 'threshold_m': THRESHOLD, 'steps': [], 'success': False,
        'privileged_information': ['instance mask truth and semantic name association',
        'simulated depth and camera K/T', 'EEF/joint state', 'MuJoCo kinematic model for IK', 'BDDL success predicate'],
        'collinear_parallel': 'pure geometry tested; robot trajectory execution not validated',
        'collision_planning': 'not implemented; bounded local Cartesian approach only',
        'physical_contact_claimed': False, 'original_basket_task_claimed': False,
        'budget': {'max_completion_tokens':384, 'max_actual_request_tokens':6000, 'max_total_tokens':15000},
        'repeat_guard': {'same_error_limit':2, 'no_phase_progress_limit':2}}
    harness = None
    started = time.monotonic()
    previous_exchange = []
    def save():
        report['tokens'] = {'prompt':client.prompt, 'completion':client.completion, 'total':client.total}
        report['api_calls'] = client.calls
        report['llm_steps'] = len(report['steps'])
        report['workflow'] = progress.summary()
        report['elapsed_seconds'] = round(time.monotonic()-started,3)
        (out/'result.json').write_text(dump(client.redact(report)), encoding='utf-8')
    try:
        save()
        harness = Harness(out)
        report['scene'] = harness.task.name
        report['calibration'] = {'K':harness.K, 'T_camera_to_world':harness.T,
            'image_origin':'top-left; RGB/depth/mask flipped together', 'camera_axes':'OpenCV', 'mask_id':harness.mask_id}
        report['initial_check'] = harness.check_success()
        if report['initial_check']['success']:
            raise RuntimeError('Subtask already satisfied; cannot claim an action loop')
        report['status'] = 'running'
        save()
        for step in range(1,13):
            if shutil.disk_usage(str(ROOT)).free < 10*1024**3:
                raise RuntimeError('Disk reserve below 10 GiB')
            state = harness.state(None)
            state.pop('last_tool_result', None)
            state['workflow'] = progress.summary()
            observation = dump(state)
            messages = [{'role':'system','content':SYSTEM}] + previous_exchange + [{'role':'user','content':observation}]
            active_tools = progress.tools()
            payload = client.payload(messages, active_tools)
            entry = {'step':step, 'workflow_before':progress.summary(), 'observation_text':observation, 'request':payload}
            report['steps'].append(entry)
            save()
            response, usage_error = client.complete(payload)
            entry['response'] = response
            save()
            if usage_error:
                raise RuntimeError(usage_error)
            choices = response.get('choices',[])
            if len(choices)!=1 or choices[0].get('finish_reason')!='tool_calls':
                raise RuntimeError('Expected complete function call; no text-action fallback')
            assistant = choices[0].get('message',{})
            calls = assistant.get('tool_calls',[])
            if len(calls)!=1 or calls[0].get('type')!='function' or not calls[0].get('id'):
                raise RuntimeError('Expected exactly one valid tool call')
            fn = calls[0]['function']
            name = fn['name']
            args = json.loads(fn['arguments'])
            entry['tool_call'] = {'id':calls[0]['id'], 'name':name, 'arguments':args}
            try:
                progress.validate(name,args)
                result = getattr(harness,name)(**args)
            except ValueError as exc:
                result = {'error':str(exc), 'required_workflow':progress.summary()}
            entry['tool_result'] = result
            repeat_error = progress.record(name,args,result)
            entry['workflow_after'] = progress.summary()
            check = harness.check_success()
            entry['check'] = check
            previous_exchange = [
                {'role':'assistant','content':assistant.get('content'), 'tool_calls':calls},
                {'role':'tool','tool_call_id':calls[0]['id'],'content':dump(result)}]
            report['success'] = check['success']
            report['final_check'] = check
            report['simulation_control_steps'] = harness.steps
            save()
            with (out/'steps.jsonl').open('a',encoding='utf-8') as f:
                f.write(dump(client.redact(entry))+'\n')
            print(dump({'step':step,'tool':name,'relation':args.get('relation'),
                        'phase':progress.phase,'distance_m':round(check['distance_m'],6),
                        'success':check['success'],'tokens_total':client.total}), flush=True)
            if check['success']:
                report['status'] = 'passed'
                break
            if repeat_error:
                raise RuntimeError(repeat_error)
        else:
            report['status'] = 'step_limit'
    except Exception as exc:
        report['status'] = 'stopped'
        report['failure'] = str(exc)
    finally:
        if harness is not None:
            try:
                harness.snapshot('after')
                report['simulation_control_steps'] = harness.steps
                report['final_check'] = harness.check_success()
                if report['status'] == 'passed' and not report['final_check']['success']:
                    report['status'] = 'stopped'
                    report['success'] = False
                    report['failure'] = 'Final observation no longer meets success criterion'
            except Exception as exc:
                report['final_observation_error'] = str(exc)
                report['success'] = False
                report['status'] = 'stopped'
            finally:
                harness.close()
        save()
        print(dump({'status':report['status'],'success':report['success'],'llm_steps':len(report['steps']),
            'tokens':report['tokens'],'result':str(out/'result.json'),'failure':report.get('failure')}), flush=True)
    return 0 if report['status']=='passed' else 1


if __name__ == '__main__':
    sys.exit(main())

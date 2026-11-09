"""Optional single-can grasp/lift tail for the existing LIBERO approach."""
import cv2
import numpy as np

from libero_loop import Harness, TARGET, dump
from protocol import Progress


RELATION = 'grasp_lift'
UP = np.array([0., 0., 1.])


class GraspProgress(Progress):
    harness = None

    @property
    def relation(self):
        if self.harness is not None and self.harness.approach_ready:
            return RELATION
        return super().relation

    def tools(self):
        tools = super().tools()
        if self.phase != 'plan' or self.relation != RELATION:
            return tools
        tools = [tool for tool in tools if tool['function']['name'] != 'track_keypoint']
        for tool in tools:
            if tool['function']['name'] == 'solve_constraint':
                tool['function']['description'] = 'Plan one top-down grasp and vertical lift. Then execute the returned trajectory ID.'
        return tools


class GraspHarness(Harness):
    def __init__(self, out, initial_state_index=0):
        self.approach_ready = False
        self.approach_check = None
        self.grasp_result = None
        self.grasp_stage = 'approach'
        super().__init__(out, initial_state_index)

    def visual_can(self, label):
        mask, depth = self.aligned()
        eroded = cv2.erode((mask == self.mask_id).astype(np.uint8), np.ones((3, 3), np.uint8))
        y, x = np.where(eroded & np.isfinite(depth) & (depth > 0) & (depth < 5))
        if len(x) < 20:
            raise ValueError('Insufficient visible can depth pixels')
        camera = (np.linalg.inv(self.K) @ np.vstack([x, y, np.ones(len(x))])) * depth[y, x]
        world = (self.T @ np.vstack([camera, np.ones(len(x))]))[:3].T
        low, high = np.percentile(world, [2, 98], axis=0)
        point = np.r_[(low[:2] + high[:2]) / 2, high[2]]
        self.snapshot(label)
        return {'point_world_m': point, 'visible_width_xy_m': high[:2]-low[:2],
                'visible_pixels': len(x), 'eef_world_m': self.eef(),
                'finger_qpos_m': self.env.sim.data.qpos[self.robot._ref_gripper_joint_pos_indexes].copy()}

    def solve_constraint(self, keypoint_A, keypoint_B, relation):
        if relation != RELATION:
            return super().solve_constraint(keypoint_A, keypoint_B, relation)
        self.grasp_stage = 'grasp_plan'
        if not self.approach_ready or self.grasp_result is not None or (keypoint_A, keypoint_B) != ('eef', TARGET):
            raise ValueError('Grasp requires a completed approach and the tracked soup can')
        visual = self.visual_can('grasp_plan')
        top = visual['point_world_m']
        if np.linalg.norm(top - self.eef()) > .07 or self.start_orientation[2, 2] > -.98:
            raise ValueError('Can or approach orientation outside grasp envelope')
        jaw_width = float(visual['visible_width_xy_m'] @ np.abs(self.start_orientation[:2, 1]))
        if jaw_width > .072:
            raise ValueError('Estimated can width leaves insufficient open-jaw clearance')
        # Panda pad centres are about 3.6 mm proximal to the TCP.
        grip = top - .020 * UP
        clearance_z = max(self.eef()[2], top[2] + .045)
        above_current = np.r_[self.eef()[:2], clearance_z]
        above_can = np.r_[top[:2], clearance_z]
        stages = [('clear', above_current), ('align', above_can), ('descend', grip),
                  ('lift_mid', grip + .030 * UP), ('lift', grip + .060 * UP)]
        start = self.eef()
        records = []
        for stage, target in stages:
            count = max(1, int(np.ceil(np.linalg.norm(target - start) / .010)))
            points = [start + (target-start)*i/count for i in range(1, count+1)]
            records.append({'stage': stage, 'target': target, 'points': points, 'ik': self.ik(points)})
            start = target
        traj = 'traj_%03d' % (len(self.trajectories)+1)
        record = {'traj': traj, 'relation': RELATION, 'stages': records, 'visual': visual,
                  'estimated_jaw_width_m': jaw_width, 'orientation_world': self.start_orientation,
                  'created_sim_step': self.steps}
        self.trajectories[traj] = record
        (self.out/(traj+'.json')).write_text(dump(record), encoding='utf-8')
        return {'traj': traj, 'relation': RELATION, 'grip_world_m': grip.tolist(), 'lift_m': .060}

    def grasp_step(self, traj, stage, target, jaw):
        if self.steps >= 900:
            raise RuntimeError('Simulation control step ceiling reached')
        rotation = self.env.sim.data.site_xmat[self.robot.eef_site_id].reshape(3, 3)
        rot_error = .5 * sum(np.cross(rotation[:, i], self.start_orientation[:, i]) for i in range(3))
        desired = np.r_[np.clip(target-self.eef(), -.0125, .0125), np.clip(rot_error, -.05, .05)]
        c = self.controller
        arm = (desired-(c.output_max+c.output_min)/2) / ((c.output_max-c.output_min)/(c.input_max-c.input_min)) + (c.input_max+c.input_min)/2
        action = np.r_[np.clip(arm, c.input_min, c.input_max), jaw]
        self.obs, reward, done, _ = self.env.step(action)
        self.steps += 1
        self.event({'sim_step': self.steps, 'traj': traj, 'grasp_stage': stage,
                    'action_osc_pose': action, 'eef_world_m': self.eef(),
                    'reward': float(reward), 'done': bool(done)})
        if done or not np.isfinite(self.eef()).all():
            raise RuntimeError('Invalid or terminated simulator state during grasp')

    def execute_trajectory(self, traj):
        record = self.trajectories.get(traj)
        if not record or record['relation'] != RELATION:
            return super().execute_trajectory(traj)
        if traj in self.used or record['created_sim_step'] != self.steps:
            raise ValueError('Unknown, consumed, or stale grasp trajectory')
        self.used.add(traj)
        start_step = self.steps
        samples = {}

        def sample(label):
            samples[label] = self.visual_can(label)
            (self.out/'grasp_measurements.json').write_text(dump(samples), encoding='utf-8')

        for entry in record['stages']:
            stage = entry['stage']
            self.grasp_stage = stage
            jaw = +1.0 if stage.startswith('lift') else -1.0
            for point in entry['points']:
                for _ in range(12):
                    if np.linalg.norm(point-self.eef()) < .003:
                        break
                    self.grasp_step(traj, stage, point, jaw)
            if np.linalg.norm(entry['target']-self.eef()) > .008:
                raise RuntimeError('Grasp stage position error exceeds 8 mm: '+stage)
            if stage == 'descend':
                self.grasp_stage = 'close'
                sample('before_close')
                for _ in range(25):
                    self.grasp_step(traj, 'close', entry['target'], +1.0)
                sample('after_close')
            if stage.startswith('lift'):
                sample(stage)
        self.grasp_stage = 'hold'
        for _ in range(12):
            self.grasp_step(traj, 'hold', record['stages'][-1]['target'], +1.0)
        sample('hold')
        base = samples['after_close']
        initial_offset = base['point_world_m'] - base['eef_world_m']
        measurements = {}
        for label in ('lift_mid', 'lift', 'hold'):
            current = samples[label]
            object_motion = current['point_world_m'] - base['point_world_m']
            eef_motion = current['eef_world_m'] - base['eef_world_m']
            offset = current['point_world_m'] - current['eef_world_m']
            measurements[label] = {'object_rise_m': float(object_motion[2]),
                                   'eef_rise_m': float(eef_motion[2]),
                                   'relative_drift_m': float(np.linalg.norm(offset-initial_offset))}
        mid, lift, hold = (measurements[key] for key in ('lift_mid', 'lift', 'hold'))
        mid_follows = mid['eef_rise_m'] >= .020 and mid['object_rise_m'] >= .015 and mid['relative_drift_m'] <= .015
        success = mid_follows and all(m['eef_rise_m'] >= .050 and m['object_rise_m'] >= .040 and
                                     m['relative_drift_m'] <= .015 for m in (lift, hold))
        failure = None if success else ('dropped_after_acquisition' if mid_follows else
                    'no_acquisition' if mid['object_rise_m'] < .010 and lift['object_rise_m'] < .010
                    else 'other_inconclusive_tracking_or_slip')
        self.grasp_result = {'success': bool(success), 'failure_category': failure, 'measurements': measurements,
                             'executed_control_steps': self.steps-start_step, 'traj': traj}
        self.executions += 1
        self.grasp_stage = 'verified' if success else 'verification_failed'
        return self.grasp_result

    def check_success(self):
        if not self.approach_ready:
            check = super().check_success()
            self.approach_check = check
            self.approach_ready = bool(self.executions and check['success'])
        check = dict(self.approach_check)
        check['approach_success'] = check['success']
        check['success'] = bool(self.grasp_result and self.grasp_result['success'])
        check['criterion'] = 'visual_can_rise_and_eef_relative_stability'
        check['grasp'] = self.grasp_result
        check['bddl_success'] = bool(self.env.check_success())
        return check

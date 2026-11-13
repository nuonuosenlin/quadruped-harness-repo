"""Ordering, measured stopping, final-pose and safety tests: no model or physics."""

from copy import deepcopy
import json
from types import SimpleNamespace

import numpy as np
import pytest

from go2_demo.backend import MujocoGo2Backend
from go2_demo.harness import Harness
from go2_demo.ordered_evaluation import OrderedStandoffEvaluator
from go2_demo.runner import run_episode
from go2_demo.scenarios import get_scenario
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend


def sample(x=5.4, y=0., yaw=0., time=1., **overrides):
    return {"base_xy_m": [x, y], "yaw_rad": yaw, "sim_time_s": time,
            "speed_mps": 0., "abs_yaw_rate_radps": 0., "stop_confirmed": True,
            "collision": False, "fallen": False, **overrides}


def evaluator():
    return OrderedStandoffEvaluator([6.4, 0.], [1.8, .6])


def test_direct_b_is_ineligible_until_a_has_measured_stopped_evidence():
    e = evaluator()
    b = sample(.8, .6)
    e.note_stop(b)
    result = e.evaluate(b)
    assert not result['success'] and not result['checkpoints']['A']['passed']
    assert result['checkpoints']['B']['criteria_pass']
    assert not result['checkpoints']['B']['passed']
    assert 'A_NOT_CONFIRMED_BEFORE_B' in result['checkpoints']['B']['failure_reasons']
    assert result['premature_b_stops_ignored'] == 1


def test_b_then_a_does_not_reuse_the_old_b_visit():
    e = evaluator()
    e.note_stop(sample(.8, .6))
    a = sample(time=2.)
    e.note_stop(a)
    assert not e.evaluate(a)['success']
    b = sample(.8, .6, time=3.)
    # Teleporting a sample without a fresh confirmed stop is insufficient.
    assert not e.evaluate(b)['success']
    e.note_stop(b)
    assert e.evaluate(b)['success']


def test_a_is_historical_b_must_be_valid_at_final_position():
    e = evaluator()
    e.note_stop(sample())
    b = sample(.8, .6, time=2.)
    e.note_stop(b)
    assert e.evaluate(b)['success']
    away = sample(.1, -.5, time=3.)
    e.note_stop(away)
    result = e.evaluate(away)
    assert result['checkpoints']['A']['passed']
    assert not result['checkpoints']['B']['passed'] and not result['success']


@pytest.mark.parametrize('overrides,reason', [
    ({'stop_confirmed': False}, 'STOP_NOT_CONFIRMED'),
    ({'speed_mps': .12}, 'NOT_STOPPED'),
    ({'abs_yaw_rate_radps': .25}, 'NOT_STOPPED'),
    ({'collision': True}, 'COLLISION'), ({'fallen': True}, 'FALLEN'),
])
def test_unconfirmed_moving_or_unsafe_a_cannot_latch(overrides, reason):
    e = evaluator()
    e.note_stop(sample(**overrides))
    result = e.evaluate(sample(**overrides))
    assert not result['checkpoints']['A']['passed']
    assert reason in result['checkpoints']['A']['failure_reasons']


@pytest.mark.parametrize('distance,angle,passed', [
    (.82, .25, True), (1.18, -.25, True), (.819, 0., False),
    (1.181, 0., False), (1., .251, False),
])
def test_checkpoint_distance_and_heading_boundaries(distance, angle, passed):
    e = evaluator()
    row = sample(6.4 - distance, 0., yaw=angle)
    e.note_stop(row)
    assert e.evaluate(row)['checkpoints']['A']['passed'] is passed


@pytest.mark.parametrize('flag', ['collision', 'fallen'])
def test_later_global_safety_failure_invalidates_previously_achieved_a(flag):
    e = evaluator()
    e.note_stop(sample())
    b = sample(.8, .6, time=2., **{flag: True})
    e.note_stop(b)
    result = e.evaluate(b)
    assert result['checkpoints']['A']['achieved_at_checkpoint']
    assert not result['checkpoints']['A']['passed'] and not result['success']


def test_nan_measurement_never_counts_as_a_checkpoint_or_enters_json():
    e = evaluator()
    bad = sample(yaw=float('nan'))
    e.note_stop(bad)
    result = e.evaluate(bad)
    assert not result['success']
    assert 'INVALID_MEASUREMENT' in result['checkpoints']['A']['failure_reasons']
    json.dumps(result, allow_nan=False)


def test_backend_stop_records_privately_and_returns_no_scoring_or_goal_truth():
    backend = object.__new__(MujocoGo2Backend)
    backend._viewer = None
    backend._fallen_ever = False
    backend._collision_steps = 0
    backend._ordered_evaluator = evaluator()
    backend.data = SimpleNamespace(qvel=np.zeros(6), time=1.)
    backend._base_pose = lambda: (np.array([5.4, 0., .35]), 0., np.eye(3))
    backend._advance_zero = lambda seconds: setattr(backend.data, 'time', backend.data.time + seconds)
    result = backend.stop()
    assert backend._ordered_evaluator.a_witness is not None
    assert set(result) == {'status', 'error_code', 'speed_mps', 'yaw_rate_radps'}
    assert 'checkpoints' not in result and 'target_xy_m' not in result


class SequenceBackend(EpisodeBackend):
    def __init__(self):
        super().__init__()
        self.scenario = get_scenario('memory_ab_occluded_v1')
        self.task_instruction = self.scenario.instruction
        self.position = [5.4, 0.]
        self.time = 1.
        self.scorer = evaluator()

    def capture(self):
        frame = super().capture()
        frame.base_xy_yaw = np.array([*self.position, 0.])
        frame.sim_time_s = self.time
        return frame

    def stop(self):
        self.stops += 1
        self.time += .6
        self.scorer.note_stop(sample(*self.position, time=self.time))
        return {'status': 'succeeded'}

    def move_relative(self, **arguments):
        self.moves.append(arguments)
        self.position = [.8, .6]
        self.stop()
        return {'status': 'succeeded'}

    def evaluate(self, **kwargs):
        return self.scorer.evaluate(sample(*self.position, time=self.time))


class SequenceModel:
    def __init__(self, last):
        self.tools = iter(['stop', 'move_relative', last])
        self.turn = 0

    def decide(self, observation, *args, **kwargs):
        # The privileged stage/witness/goal coordinates never enter the prompt.
        text = json.dumps(observation)
        for hidden in ('checkpoints', 'target_xy_m', 'a_witness', 'order_satisfied'):
            assert hidden not in text
        name = next(self.tools)
        self.turn += 1
        arguments = {'forward_m': .2, 'lateral_m': 0.} if name == 'move_relative' else {}
        return Decision([ToolCall(f'c{self.turn}', name, arguments)])


@pytest.mark.parametrize('last,success', [('finish', True), ('stop', False)])
def test_runner_reports_both_checkpoints_but_requires_finish(tmp_path, last, success):
    backend = SequenceBackend()
    result = run_episode(backend, SequenceModel(last), mode='api', run_dir=tmp_path, max_model_calls=3)
    assert result['success'] is success
    assert result['checkpoints']['A']['passed'] and result['checkpoints']['B']['passed']
    assert result['order_satisfied']
    saved = json.loads((tmp_path / 'metrics.json').read_text())
    assert saved['checkpoints'] == result['checkpoints']
    manifest = json.loads((tmp_path / 'manifest.json').read_text())
    assert manifest['evaluation']['checkpoint_order'] == ['A', 'B']

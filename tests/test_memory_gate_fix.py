"""Offline wire-to-gate regression tests; no API or credential loading."""
from copy import deepcopy
import json
from types import SimpleNamespace

import httpx
import pytest

from go2_demo.harness import TOOLS
from go2_demo.memory import AsyncMemory, PACKET_KEYS, read_state
from go2_demo.memory_context import compact_observation, STATE_CHAR_LIMIT, RETRY_STATE_CHAR_LIMIT
from go2_demo.memory_planning import MemoryPlanningHarness
from go2_demo.memory_protocol import planning_tools
from go2_demo.models import APIModel, ModelProtocolError
from go2_demo.runner import run_episode
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend


OBS = {'task': 'A then B', 'memory_state': {'world': {}, 'objects': []}}


def plan(checks=None):
    return {'plan': {'subgoals': [{'subgoal_id': 'scan', 'description': 'safe exploration',
        'preconditions': checks or [], 'completion': []}], 'branches': [], 'recovery': 'stop'},
        'subgoal_id': 'scan'}


def reply(tool='turn', envelope=True):
    args = {'yaw_rad': .3} if tool == 'turn' else {}
    if envelope:
        args['planning'] = plan()
    return {'model': 'offline', 'choices': [{'finish_reason': 'tool_calls', 'message': {
        'content': None, 'reasoning_content': 'synthetic-private', 'tool_calls': [
            {'id': 'c1', 'type': 'function', 'function': {'name': tool, 'arguments': json.dumps(args)}}]}}],
        'usage': {'prompt_tokens': 10, 'completion_tokens': 2, 'total_tokens': 12}}


def truncated():
    r = reply()
    r['choices'][0] = {'finish_reason': 'length', 'message': {
        'role': 'assistant', 'content': '', 'reasoning_content': 'synthetic reasoning'}}
    r['usage'] = {'prompt_tokens': 6308, 'completion_tokens': 8192, 'total_tokens': 14500}
    return r


class Backend(EpisodeBackend):
    def __init__(self):
        super().__init__(score_success=False)
        self.turns = []

    def turn(self, **kwargs):
        self.turns.append(kwargs)
        return {'status': 'succeeded'}


def test_null_assistant_content_with_wire_plan_executes_real_gate_and_strips_wrapper(tmp_path):
    original = deepcopy(TOOLS)
    seen = []
    model = APIModel('https://example.invalid/v1', 'offline', '', transport=httpx.MockTransport(
        lambda req: seen.append(json.loads(req.content)) or httpx.Response(200, json=reply())))
    backend = Backend()
    result = run_episode(backend, model, mode='api', run_dir=tmp_path, memory_v1=True, max_model_calls=1)
    assert backend.turns and backend.turns[0]['yaw_rad'] == .3
    assert 'planning' not in backend.turns[0]
    assert result['motion_calls'] == 1 and result['success'] is False
    wire = next(t for t in seen[0]['tools'] if t['function']['name'] == 'turn')
    assert 'planning' in wire['function']['parameters']['required']
    assert TOOLS == original
    rows = [json.loads(line) for line in (tmp_path/'events.jsonl').read_text().splitlines()]
    response = next(r for r in rows if r['event'] == 'model_response')
    assert response['planning_envelope'] == plan() and not response['assistant_content_present']
    assert 'synthetic-private' not in json.dumps(rows)
    assert read_state((tmp_path/'memory.md').read_text())['plans']


def test_valid_wire_plan_does_not_bypass_unknown_object_precondition(tmp_path):
    body = reply()
    body['choices'][0]['message']['tool_calls'][0]['function']['arguments'] = json.dumps({
        'yaw_rad': .3, 'planning': plan([{'object_id': 'task:A'}])})
    model = APIModel('https://example.invalid/v1', 'offline', '', transport=httpx.MockTransport(
        lambda req: httpx.Response(200, json=body)))
    backend = Backend()
    result = run_episode(backend, model, mode='api', run_dir=tmp_path, memory_v1=True, max_model_calls=1)
    assert not backend.turns and result['motion_calls'] == 0
    rows = [json.loads(line) for line in (tmp_path/'events.jsonl').read_text().splitlines()]
    feedback = next(r['results'][0] for r in rows if r['event']=='tool_results')
    assert feedback['plan_diagnostic']['code'] == 'PRECONDITION_UNPROVEN'


@pytest.mark.parametrize('content,code', [(None, 'PLAN_MISSING'), ('{bad', 'PLAN_INVALID_JSON'),
    ('[]', 'PLAN_NOT_OBJECT'), ('{}', 'PLAN_ENVELOPE_FIELDS'),
    (json.dumps({'plan_id': 'unknown', 'subgoal_id': 'scan'}), 'PLAN_BINDING_MISMATCH')])
def test_gate_reports_specific_format_or_binding_condition(tmp_path, content, code):
    memory = AsyncMemory(tmp_path/'memory.md')
    try:
        gate = MemoryPlanningHarness(memory)
        feedback, _ = gate.prepare(Decision([ToolCall('c', 'turn', {'yaw_rad': .3})],
                                            assistant_content=content), 0)
        assert feedback['error_code'] == 'MEMORY_CONSTRAINT'
        assert feedback['plan_diagnostic']['phase'] == 'envelope'
        assert feedback['plan_diagnostic']['code'] == code
        gate.note_results([ToolCall('c', 'turn', {'yaw_rad': .3})], [feedback])
        assert gate.context('task', 0)['memory_state']['world']['last_tool_feedback'][0]['plan_diagnostic']['code'] == code
    finally:
        memory.close()


def test_missing_wire_plan_is_repaired_before_any_tool_executes():
    seen = []
    model = APIModel('https://example.invalid/v1', 'offline', '', transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(200, json=reply(envelope=len(seen)>1))))
    result = model.decide(OBS, '', TOOLS, [])
    assert result.request_attempts == 2
    assert result.protocol_diagnostics[0]['kind'] == 'MISSING_PLANNING_ENVELOPE'
    assert result.planning_envelope == plan() and result.assistant_content is None
    assert result.calls[0].arguments == {'yaw_rad': .3}


def test_wire_plan_continues_only_with_assigned_binding(tmp_path):
    seen=[]
    def handler(req):
        seen.append(req)
        body=reply()
        if len(seen)==2:
            body['choices'][0]['message']['tool_calls'][0]['id']='c2'
            body['choices'][0]['message']['tool_calls'][0]['function']['arguments']=json.dumps({
                'yaw_rad':.2,'planning':{'plan_id':'plan-0001','subgoal_id':'scan'}})
        return httpx.Response(200,json=body)
    backend=Backend()
    model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(handler))
    result=run_episode(backend,model,mode='api',run_dir=tmp_path,memory_v1=True,max_model_calls=2)
    assert len(backend.turns)==result['motion_calls']==2


def test_invalid_wire_envelope_never_becomes_an_automatic_exploration_plan():
    body=reply()
    body['choices'][0]['message']['tool_calls'][0]['function']['arguments']=json.dumps({
        'yaw_rad':.3,'planning':{'plan':plan()['plan'],'plan_id':'invented','subgoal_id':'scan'}})
    model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(
        lambda req:httpx.Response(200,json=body)))
    with pytest.raises(ModelProtocolError) as caught:
        model.decide(OBS,'',TOOLS,[],max_requests=1)
    assert caught.value.protocol_diagnostics[0]['plan_code']=='PLAN_ENVELOPE_FIELDS'


def bloated():
    s = {'world': {'step': 100, 'decision_step': 100, 'task_targets': [
        {'object_id': 'task:B', 'task_label': 'B', 'description': 'green cube'}],
        'public_context': {'duplicate': 'X'*100000}, 'measurements': {},
        'current_observation': {'image_id': 'f100', 'tracked_points': [], 'target_candidates': []}},
        'objects': [], 'events': [], 'active_beliefs': [], 'invalidated': [],
        'pose': {'frame': 'episode_start', 'position_m': [0., 0.]},
        'confidence_thresholds': {'unknown_after_steps': 6}}
    for i in range(100):
        s['objects'].append({'object_id': f'p{i}', 'category': 'unclassified_landmark',
            'state': 'confirmed', 'last_seen': 100, 'confidence': .95,
            'pose': {'frame': 'episode_start', 'position_m': [i, 0.]},
            'evidence_ids': ['large-identifier']*1000, 'source': 'rgbd'})
        s['events'].append({'kind': 'action_failed', 'description': 'Y'*10000, 'step': i})
        s['world']['current_observation']['tracked_points'].append({'point_id': f'p{i}',
            'image_id': 'f100', 'pixel_uv': [12, 20], 'relative_xy_m': [1., 2.],
            'valid': True, 'confidence': 1.})
    s['objects'].insert(0, {'object_id': 'task:B', 'category': 'task_target', 'state': 'confirmed',
        'last_seen': 100, 'confidence': .95, 'pose': {'frame': 'episode_start', 'position_m': [1.7,.7]},
        'evidence_ids': ['e1','e2'], 'source': 'task_label_rgbd_tracking'})
    s['objects'].append({'object_id': 'old', 'state': 'stale', 'last_seen': 1})
    return {'task': 'A then B', 'memory_state': s}


@pytest.mark.parametrize('retry,cap', [(False, STATE_CHAR_LIMIT), (True, RETRY_STATE_CHAR_LIMIT)])
def test_prompt_projection_bounds_growth_keeps_task_target_and_does_not_mutate_md(retry, cap):
    original = bloated(); before = deepcopy(original)
    compact = compact_observation(original, retry=retry)
    state = compact['memory_state']
    assert len(json.dumps(state, ensure_ascii=False, separators=(',', ':'))) <= cap
    assert set(state) == set(PACKET_KEYS)
    assert state['objects'][0]['object_id'] == 'task:B'
    assert 'old' not in [o['object_id'] for o in state['objects']]
    assert len(state['world']['current_observation']['tracked_points']) == 1
    assert 'public_context' not in state['world']
    assert original == before
    assert compact_observation(compact) == compact  # retry cap survives build_messages


def test_projection_never_strengthens_aged_beliefs_or_sends_old_measurements():
    observation=bloated()
    state=observation['memory_state']
    state['objects'][0]['last_seen']=96
    state['world']['measurements']={
        'pose.x_m':{'value':9.,'step':99,'source':'old'},
        'pose.y_m':{'value':0.,'step':100,'source':'current'}}
    projected=compact_observation(observation)['memory_state']
    target=next(o for o in projected['objects'] if o['object_id']=='task:B')
    assert target['state']=='predicted' and target['confidence']==.475
    assert 'pose.x_m' not in projected['world']['measurements']
    assert projected['world']['measurements']['pose.y_m']['value']==0.


def test_projection_retains_bounded_fresh_generic_visual_proposals():
    observation=deepcopy(OBS)
    observation['memory_state']['world']={
        'current_observation':{'image_id':'f2'},
        'public_context':{'visual_candidates':[
            {'image_id':'old','pixel_uv':[0,0],'source':'rgb_corner'},
            {'image_id':'f2','pixel_uv':[1,2],'source':'rgb_corner'}]}}
    candidates=compact_observation(observation)['memory_state']['world']['current_observation']['visual_candidates']
    assert candidates==[{'image_id':'f2','pixel_uv':[1,2],'source':'rgb_corner'}]


def test_length_retries_once_with_smaller_input_and_all_usage_accounted():
    seen = []
    model = APIModel('https://example.invalid/v1', 'offline', '', transport=httpx.MockTransport(
        lambda req: seen.append(json.loads(req.content)) or httpx.Response(200,
            json=truncated() if len(seen)==1 else reply())))
    result = model.decide(bloated(), '', TOOLS, [])
    assert result.request_attempts == 2 and len(seen) == 2
    assert len(seen[1]['messages'][1]['content']) < len(seen[0]['messages'][1]['content'])
    retry = json.loads(seen[1]['messages'][1]['content'])['memory_state']
    assert retry['world']['context_limits']['retry'] is True
    assert retry['world']['context_limits']['state_char_limit'] == RETRY_STATE_CHAR_LIMIT
    assert result.protocol_diagnostics[0]['kind'] == 'TRUNCATED_RESPONSE'
    assert result.usage['total_tokens'] == 14512 and result.reasoning_response_count == 2
    assert 'synthetic reasoning' not in json.dumps(seen[1])
    assert all(p['max_tokens']==8192 for p in seen)


@pytest.mark.parametrize('budget,requests,termination', [(1,1,'model_error'), (2,2,'budget_exhausted')])
def test_length_retry_respects_runner_call_budget_and_records_tokens(tmp_path,budget,requests,termination):
    seen=[]
    model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(200,json=truncated() if len(seen)==1 else reply())))
    backend=Backend()
    metrics=run_episode(backend,model,mode='api',run_dir=tmp_path,memory_v1=True,max_model_calls=budget)
    assert metrics['model_calls']==len(seen)==requests
    assert metrics['decision_calls']==1 and metrics['protocol_retries']==requests-1
    assert metrics['usage']['total_tokens']==14500+(12 if requests==2 else 0)
    assert metrics['termination']==termination
    assert len(backend.turns)==requests-1


def test_second_length_stops_without_third_request():
    seen=[]
    model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(200,json=truncated())))
    with pytest.raises(ModelProtocolError) as caught:
        model.decide(OBS,'',TOOLS,[])
    assert len(seen)==caught.value.request_attempts==2
    assert caught.value.usage['total_tokens']==29000


def test_length_retry_does_not_get_a_new_time_budget(monkeypatch):
    import go2_demo.models as models
    clock=[0.]
    monkeypatch.setattr(models,'time',SimpleNamespace(monotonic=lambda:clock[0]))
    client=APIModel('https://example.invalid/v1','offline','')
    timeouts=[]
    def once(*args,**kwargs):
        timeouts.append(kwargs['timeout_s'])
        client._last_protocol_metadata={'kind':'TRUNCATED_RESPONSE','usage':{'total_tokens':14500}}
        clock[0]=1.1
        raise ModelProtocolError('synthetic length')
    monkeypatch.setattr(client,'_decide_once',once)
    with pytest.raises(Exception) as caught:
        client.decide(OBS,'',TOOLS,[],timeout_s=1.)
    assert caught.value.code=='MODEL_TIMEOUT' and timeouts==[1.]
    assert caught.value.request_attempts==1 and caught.value.usage['total_tokens']==14500


def test_h0_tool_definitions_and_auto_request_are_unchanged():
    original=deepcopy(TOOLS)
    assert planning_tools(TOOLS)!=TOOLS and TOOLS==original
    seen=[]
    model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(
        lambda req:seen.append(json.loads(req.content)) or httpx.Response(200,json=reply(envelope=False))))
    decision=model.decide({'task':'H0'},'data:image/png;base64,aW1hZ2U=',TOOLS,[])
    assert seen[0]['tools']==original and seen[0]['tool_choice']=='auto'
    assert decision.calls[0].arguments=={'yaw_rad':.3} and decision.planning_envelope is None

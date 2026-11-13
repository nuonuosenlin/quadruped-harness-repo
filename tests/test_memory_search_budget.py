"""Cross-tool review clock: offline fixtures only, no simulation or paid API."""
from copy import deepcopy
import json

import httpx
import pytest

from go2_demo.harness import TOOLS
from go2_demo.memory import AsyncMemory, MemoryRules, SEARCH_REVIEW_INTERVAL, state_packet
from go2_demo.memory_context import compact_observation, STATE_CHAR_LIMIT, RETRY_STATE_CHAR_LIMIT
from go2_demo.memory_planning import MemoryPlanningHarness, MEMORY_SYSTEM_PROMPT
from go2_demo.models import APIModel
from go2_demo.types import Decision, ToolCall
from test_memory_exploration import action, evidence


def reviews(rules):return [r for r in rules.state['ledger'] if r['kind']=='search_review_due']


def candidate(identity='task:B'):
    return {'public_context':{'current_observation':{'target_candidates':[
        {'object_id':identity,'status':'candidate_not_confirmed'}]}}}


def leg(checks=None):
    return {'subgoals':[{'subgoal_id':'leg','description':'keep direction relative to tracked p until range <=1m',
        'preconditions':checks or [],'completion':[{'measurement':'p.range_m','op':'le','value':1.}]}],
        'branches':[{'on':'search_review_due','subgoal_id':'leg'}],
        'recovery':'review direction and reference; continue evidenced leg or select another supported branch'}


def test_alternating_moves_and_perception_do_not_reset_clock_or_create_failures():
    rules=MemoryRules();rules.update({'step':0,**candidate()})
    tools=['turn','move_relative','track_point','observe','get_geometry','move_relative']
    for step in range(1,26):
        rules.update({'step':step,'actions':[action(tools[(step-1)%len(tools)])],**candidate()})
        if step%3==0:rules.set_plan(f'p{step}',leg())
    status=rules.state['world']['exploration']
    assert status['decisions_since_task_novelty']==25 and status['review_due']
    assert [r['step'] for r in reviews(rules)]==[12,24]
    assert status['review_count']==2 and status['last_task_novelty_step']==0
    assert all(r['advisory_only'] for r in reviews(rules))
    assert not any(e['kind'] in {'skill_stuck','key_precondition_invalidated'} for e in rules.state['events'])
    assert all(g['status']!='已失效' for p in rules.state['plans'] for g in p['subgoals'])


def test_failed_and_deduplicated_tool_decisions_still_spend_global_budget():
    rules=MemoryRules()
    for step in range(1,13):
        rules.update({'step':step,'actions':[action('track_point',status='failed') if step%2 else
                                            action('move_relative',deduplicated=True)]})
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==12
    assert len(reviews(rules))==1


def test_same_decision_multiple_results_publications_and_new_plans_do_not_double_count_or_spam():
    rules=MemoryRules()
    rules.update({'step':12,'actions':[action('observe'),action('get_geometry')]})
    for n in range(5):
        rules.set_plan(f'p{n}',leg())
        rules.update({'step':12})
    assert len(reviews(rules))==1
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==12
    rules.update({'step':24})
    assert [r['window_index'] for r in reviews(rules)]==[1,2]


@pytest.mark.parametrize('first_kind',['candidate','object'])
def test_only_first_task_identity_resets_clock_not_reappearance_or_confirmation(first_kind):
    rules=MemoryRules();rules.update({'step':0,**candidate()})
    for step in range(1,14):
        rules.update({'step':step,'actions':[action('track_point')],**candidate()})
    assert rules.state['world']['exploration']['review_due']
    new=(candidate('task:A') if first_kind=='candidate' else {'objects':[evidence('a1',identity='task:A')]})
    rules.update({'step':14,**new})
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==0
    assert not rules.state['world']['exploration']['review_due']
    packet=compact_observation({'task':'search','memory_state':state_packet(rules.state,14)})
    assert not packet['memory_state']['world']['exploration']['review_due']
    assert packet['memory_state']['world']['exploration']['review_evidence_id'] is None
    rules.update({'step':15,'objects':[evidence('a2',identity='task:A')],**candidate('task:A')})
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==1
    rules.update({'step':16,'objects':[evidence('a3',identity='task:A')],**candidate('task:B')})
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==2
    assert len(reviews(rules))==1  # Prior ledger is retained after novelty.


def test_new_unclassified_point_ids_and_claimed_plan_progress_cannot_reset_clock():
    rules=MemoryRules()
    for step in range(1,14):
        obj={**evidence(f'f{step}',identity=f'point-{step}'),'category':'unclassified_landmark'}
        rules.update({'step':step,'objects':[obj],'actions':[action('track_point')]})
        rules.set_plan(f'p{step}',leg())
    assert rules.state['world']['exploration']['decisions_since_task_novelty']==13
    assert len(reviews(rules))==1


@pytest.mark.parametrize('retry,cap',[(False,STATE_CHAR_LIMIT),(True,RETRY_STATE_CHAR_LIMIT)])
def test_persistent_review_survives_event_noise_and_projection_caps(retry,cap):
    rules=MemoryRules();rules.update({'step':12,'actions':[action('move_relative')]})
    rules.state['events'] += [{'kind':'target_state_changed','description':'noise'*1000} for _ in range(30)]
    view=compact_observation({'task':'search','memory_state':state_packet(rules.state,12)},retry=retry)
    status=view['memory_state']['world']['exploration']
    assert status['review_due'] and status['decisions_since_task_novelty']==12
    assert len(json.dumps(view['memory_state'],ensure_ascii=False,separators=(',',':')))<=cap


def test_normal_long_leg_may_continue_past_reviews_and_complete_by_measurement(tmp_path):
    memory=AsyncMemory(tmp_path/'memory.md')
    try:
        gate=MemoryPlanningHarness(memory)
        move=ToolCall('move','move_relative',{'forward_m':.3,'lateral_m':0.})
        for step in range(30):
            envelope={'plan':leg(),'subgoal_id':'leg'} if step==0 else {'plan_id':gate.plan_id,'subgoal_id':'leg'}
            feedback,binding=gate.prepare(Decision([move],planning_envelope=envelope),step)
            assert feedback is None
            memory.submit({'step':step+1,'actions':[action('move_relative',**binding)],
                'measurements':{'p.range_m':{'value':round(7.-.2*(step+1),3),'source':'synthetic_rgbd'}}})
            memory.flush()  # Offline synchronization only, never added to live loop.
        snapshot=memory.snapshot()
        assert snapshot['plans'][0]['subgoals'][0]['status']=='已完成'
        assert snapshot['world']['exploration']['decisions_since_task_novelty']==30
        assert [r['step'] for r in snapshot['ledger'] if r['kind']=='search_review_due']==[12,24]
        assert not any(e['kind'] in {'skill_stuck','key_precondition_invalidated'} for e in snapshot['events'])
    finally:memory.close()


def test_review_does_not_relax_fresh_unknown_object_preconditions(tmp_path):
    memory=AsyncMemory(tmp_path/'memory.md')
    try:
        memory.submit({'step':0,'objects':[evidence('a0',identity='task:A')]})
        memory.submit({'step':12,'objects':[evidence('a12',identity='task:A')],'actions':[action('observe')]})
        memory.flush()
        assert memory.snapshot()['world']['exploration']['review_due']
        assert memory.snapshot()['objects'][0]['state']=='unknown'
        gate=MemoryPlanningHarness(memory)
        move=ToolCall('move','move_relative',{'forward_m':.2,'lateral_m':0.})
        denied,_=gate.prepare(Decision([move],planning_envelope={
            'plan':leg([{'object_id':'task:A'}]),'subgoal_id':'leg'}),12)
        assert denied['plan_diagnostic']['code']=='PRECONDITION_UNPROVEN'
        assert gate.prepare(Decision([move],planning_envelope={'plan':leg(),'subgoal_id':'leg'}),12)[0] is None
    finally:memory.close()


def test_review_reaches_model_and_a_different_leg_can_pass_existing_wire_and_gate(tmp_path):
    memory=AsyncMemory(tmp_path/'memory.md')
    try:
        memory.submit({'step':12,'actions':[action('move_relative')]});memory.flush()
        gate=MemoryPlanningHarness(memory)
        observation=gate.context('search for unseen target',12,{'image_id':'f12','tracked_points':[]})
        def handler(req):
            payload=json.loads(req.content);view=json.loads(payload['messages'][1]['content'])
            assert view['memory_state']['world']['exploration']['review_due']
            assert 'A long productive exploration leg may continue' in payload['messages'][0]['content']
            proposal=leg();proposal['subgoals'][0]['description']='keep observed reference on the right; reassess at range endpoint'
            return httpx.Response(200,json={'choices':[{'finish_reason':'tool_calls','message':{
                'content':None,'reasoning_content':'synthetic','tool_calls':[{'id':'leg','type':'function','function':{
                'name':'move_relative','arguments':json.dumps({'forward_m':.2,'lateral_m':0.,
                    'planning':{'plan':proposal,'subgoal_id':'leg'}})}}]}}]})
        client=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(handler))
        decision=client.decide(observation,'',TOOLS,[])
        assert gate.prepare(decision,12)[0] is None
    finally:memory.close()

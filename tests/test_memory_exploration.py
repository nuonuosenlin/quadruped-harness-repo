"""Offline search-policy contract tests; no model API, MuJoCo or key files."""
from copy import deepcopy
import json

import httpx
import pytest

from go2_demo.harness import Harness, TOOLS
from go2_demo.memory import AsyncMemory, MemoryRules, SCAN_TURN_LIMIT, THRESHOLDS, predicate, state_packet
from go2_demo.memory_context import compact_observation, STATE_CHAR_LIMIT, RETRY_STATE_CHAR_LIMIT
from go2_demo.memory_planning import MemoryPlanningHarness, MEMORY_SYSTEM_PROMPT
from go2_demo.models import APIModel
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend


def action(tool='turn',status='succeeded',**extra):
    return {'tool':tool,'status':status,**extra}


def evidence(frame='f0',position=(1.,.2),identity='task:B'):
    return {'object_id':identity,'category':'task_target','pose':{'frame':'episode_start','position_m':list(position)},
        'pose_covariance':None,'confidence':.95,'source':'synthetic_public_rgbd','frame_id':frame,
        'anchor_node':None,'visual_feature':{'image_id':frame,'pixel_uv':[10.,20.]}}


def plan(checks=None):
    return {'subgoals':[{'subgoal_id':'explore_viewpoint','description':'change viewing position',
        'preconditions':checks or [],'completion':[]}],'branches':[],'recovery':'stop and inspect a new view'}


def stalled_rules():
    rules=MemoryRules()
    for step in range(1,SCAN_TURN_LIMIT+1):
        rules.update({'step':step,'actions':[action()]})
    return rules


def test_successful_scan_emits_nonblocking_stall_once_even_after_observe_retracking_and_replans():
    rules=MemoryRules()
    for i in range(SCAN_TURN_LIMIT+2):
        rules.update({'step':2*i,'actions':[action()], 'objects':[
            {**evidence(f'f{i}',identity=f'point-{i}'),'category':'unclassified_landmark'}]})
        rules.set_plan(f'p{i}',plan())
        rules.update({'step':2*i+1,'actions':[action('observe')]})
    progress=rules.state['world']['exploration']
    assert progress['stalled'] and progress['successful_turns_without_search_progress']==8
    stalls=[e for e in rules.state['events'] if e['kind']=='skill_stuck']
    assert len(stalls)==1 and stalls[0]['reason']=='repeated_turns_without_search_progress'
    record=next(r for r in rules.state['ledger'] if r['kind']=='search_stalled')
    assert len(record['action_evidence_ids'])==SCAN_TURN_LIMIT
    assert all(next(r for r in rules.state['ledger'] if r['evidence_id']==eid)['kind']=='action_executed'
               for eid in record['action_evidence_ids'])


@pytest.mark.parametrize('extra',[{'status':'failed'}, {'status':'succeeded','deduplicated':True}])
def test_failed_or_deduplicated_translation_does_not_clear_scan_stall_even_with_motion_gt(extra):
    rules=stalled_rules()
    rules.update({'step':7,'actions':[{'tool':'move_relative','motion_feedback':{
        'translation_start_frame_m':[999.,999.],'source':'simulator_ground_truth','navigation_measurement':False},**extra}]})
    assert rules.state['world']['exploration']['stalled']


def test_successful_translation_resets_search_counter_and_rearms_single_stall_event():
    rules=stalled_rules()
    rules.update({'step':7,'actions':[action('move_relative')]})
    assert not rules.state['world']['exploration']['stalled']
    for step in range(8,14):rules.update({'step':step,'actions':[action()]})
    assert rules.state['world']['exploration']['stalled']
    assert sum(e['kind']=='skill_stuck' for e in rules.state['events'])==2


def test_first_task_candidate_resets_search_budget_but_reobserving_it_does_not_confirm_or_reset():
    rules=stalled_rules()
    candidate={'object_id':'task:B','status':'candidate_not_confirmed'}
    public={'current_observation':{'target_candidates':[candidate]}}
    rules.update({'step':7,'public_context':public})
    assert not rules.state['world']['exploration']['stalled'] and rules.state['objects']==[]
    for step in range(8,14):rules.update({'step':step,'public_context':public,'actions':[action()]})
    assert rules.state['world']['exploration']['stalled'] and rules.state['objects']==[]


@pytest.mark.parametrize('retry,cap',[(False,STATE_CHAR_LIMIT),(True,RETRY_STATE_CHAR_LIMIT)])
def test_scan_stall_survives_event_noise_and_bounded_prompt_projection(retry,cap):
    state=stalled_rules().state
    state['events'] += [{'kind':'replan_required','step':6,'description':'noise'*1000} for _ in range(30)]
    observation={'task':'A then B','memory_state':state_packet(state,6)}
    packet=compact_observation(observation,retry=retry)['memory_state']
    assert packet['world']['exploration']['stalled']
    assert len(json.dumps(packet,ensure_ascii=False,separators=(',',':')))<=cap


def test_stalled_context_can_select_wire_exploration_move_and_pass_real_gate_with_no_target(tmp_path):
    memory=AsyncMemory(tmp_path/'memory.md')
    try:
        for step in range(1,7):memory.submit({'step':step,'actions':[action()]})
        memory.flush()  # Offline fixture only; live planner remains asynchronous.
        gate=MemoryPlanningHarness(memory)
        current={'image_id':'f6','tracked_points':[],'target_candidates':[]}
        observation=gate.context('find unseen A',6,current)
        seen=[]
        def local_planner(request):
            packet=json.loads(request.content)
            view=json.loads(packet['messages'][1]['content'])
            assert view['memory_state']['world']['exploration']['stalled']
            assert view['memory_state']['objects']==[]
            assert 'Do not require seeing A before moving' in packet['messages'][0]['content']
            seen.append(packet)
            return httpx.Response(200,json={'choices':[{'finish_reason':'tool_calls','message':{
                'content':None,'reasoning_content':'synthetic', 'tool_calls':[{
                    'id':'explore','type':'function','function':{'name':'move_relative','arguments':json.dumps({
                        'forward_m':.2,'lateral_m':0.,'planning':{'plan':plan(),'subgoal_id':'explore_viewpoint'}})}}]}}]})
        client=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(local_planner))
        decision=client.decide(observation,'',TOOLS,[])
        feedback,binding=gate.prepare(decision,6)
        assert feedback is None and binding['plan_id']=='plan-0001'
        backend=EpisodeBackend(score_success=False)
        harness=Harness(backend,'offline exploration')
        assert harness.dispatch_many(decision.calls)[0]['status']=='succeeded'
        assert backend.moves[0]['forward_m']==.2 and 'planning' not in backend.moves[0]
        assert len(seen)==1
    finally:memory.close()


def test_stall_does_not_allow_unknown_target_as_a_strong_precondition(tmp_path):
    memory=AsyncMemory(tmp_path/'memory.md')
    try:
        memory.submit({'step':0,'objects':[evidence(identity='task:A')]})
        for step in range(1,7):memory.submit({'step':step,'actions':[action()]})
        memory.flush()
        gate=MemoryPlanningHarness(memory)
        move=ToolCall('move','move_relative',{'forward_m':.2,'lateral_m':0.})
        invalid=Decision([move],planning_envelope={'plan':plan([{'object_id':'task:A'}]),'subgoal_id':'explore_viewpoint'})
        feedback,_=gate.prepare(invalid,6)
        assert feedback['error_code']=='MEMORY_CONSTRAINT'
        assert feedback['plan_diagnostic']['code']=='PRECONDITION_UNPROVEN'
        valid=Decision([move],planning_envelope={'plan':plan(),'subgoal_id':'explore_viewpoint'})
        assert gate.prepare(valid,6)[0] is None
    finally:memory.close()


def test_prompt_has_a_move_exploration_recovery_instead_of_scan_only_dependency():
    assert '"forward_m":0.2' in MEMORY_SYSTEM_PROMPT
    assert 'explore_viewpoint may have preconditions=[]' in MEMORY_SYSTEM_PROMPT
    assert 'approach_A still requires confirmed task:A' in MEMORY_SYSTEM_PROMPT
    assert 'do not repeat another scan-only plan' in MEMORY_SYSTEM_PROMPT


@pytest.mark.parametrize('return_step',[3,13])
def test_return_to_retained_pose_rejects_pending_candidate_without_second_relocation(return_step):
    rules=MemoryRules()
    for step in (0,1):rules.update({'step':step,'objects':[evidence(f'f{step}')]})
    rules.set_plan('depends',plan([{'object_id':'task:B'}]))
    rules.update({'step':2,'objects':[evidence('outlier',(2.5,.2))]})
    assert rules.state['objects'][0]['state']=='contradicted'
    if return_step>3:rules.update({'step':12})
    rules.update({'step':return_step,'objects':[evidence('return',(1.01,.2))]})
    obj=rules.state['objects'][0]
    assert obj['candidate_pose'] is None and obj['state']=='unknown'
    assert sum(r['kind']=='target_relocated' for r in rules.state['ledger'])==1
    assert sum(r['kind']=='relocation_candidate_rejected' for r in rules.state['ledger'])==1
    assert rules.state['plans'][0]['subgoals'][0]['status']=='已失效'
    assert predicate({'object_id':'task:B'},rules.state) is None
    rules.update({'step':return_step+1,'objects':[evidence('return2',(1.02,.2))]})
    assert obj['state']=='confirmed'
    assert rules.state['plans'][0]['subgoals'][0]['status']=='已失效'
    assert THRESHOLDS['relocation_distance_m']==.5


def test_consistent_independent_new_position_still_confirms_real_relocation():
    rules=MemoryRules()
    for step in (0,1):rules.update({'step':step,'objects':[evidence(f'f{step}')]})
    rules.update({'step':2,'objects':[evidence('new1',(2.5,.2))]})
    rules.update({'step':3,'objects':[evidence('new2',(2.51,.2))]})
    obj=rules.state['objects'][0]
    assert obj['state']=='confirmed' and obj['pose']['position_m']==[2.51,.2]
    assert sum(r['kind']=='target_relocated' for r in rules.state['ledger'])==1

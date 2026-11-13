import hashlib
import json
from pathlib import Path
import sys
import os
import runpy

import httpx
import pytest

ROOT = Path('/home/nuonuosenlin/Agent-harness')
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'tests'))
from monitor import install
from go2_demo.harness import TOOLS
from go2_demo.models import APIModel,ModelProtocolError
from go2_demo.runner import run_episode
from go2_demo.types import Decision,ToolCall
from test_runner import EpisodeBackend


def test_startup_flag_is_not_inherited_by_glfw_probe_children(monkeypatch,tmp_path):
    import monitor
    seen=[]
    monkeypatch.setenv('MEMORY_H2_RUN_ARTIFACTS',str(tmp_path))
    monkeypatch.setattr(monitor,'install',lambda out,guard:seen.append((out,guard)))
    runpy.run_path(str(Path(__file__).with_name('sitecustomize.py')))
    assert seen==[(str(tmp_path),True)]
    assert 'MEMORY_H2_RUN_ARTIFACTS' not in os.environ


def body(length=False):
    r={'choices':[{'finish_reason':'length' if length else 'tool_calls','message':{
        'content':None,'reasoning_content':'synthetic',
        'tool_calls':[{'id':'one','type':'function','function':{'name':'observe','arguments':'{}'}}]}}],
        'usage':{'prompt_tokens':10,'completion_tokens':2,'total_tokens':12}}
    if length:r['choices'][0]['message'].pop('tool_calls')
    return r


def test_error_captured_in_full_and_default_retry_works(tmp_path):
    undo=install(tmp_path)
    try:
        raw=json.dumps(body(True)).encode(); seen=[]
        model=APIModel('https://example.invalid/v1','offline','synthetic-key',transport=httpx.MockTransport(
            lambda req:seen.append(req) or httpx.Response(200,content=raw if len(seen)==1 else json.dumps(body()).encode())))
        decision=model.decide({'task':'offline','memory_state':{'world':{'decision_step':4}}},'',TOOLS,[])
        assert len(seen)==decision.request_attempts==2
        assert decision.usage['total_tokens']==24
        capture=json.loads((tmp_path/'protocol_errors/captures.jsonl').read_text())
        assert capture['decision']==5 and capture['diagnostic']['kind']=='TRUNCATED_RESPONSE'
        assert Path(capture['raw_response_file']).read_bytes()==raw
        assert capture['original_sha256']==capture['stored_sha256']==hashlib.sha256(raw).hexdigest()
    finally:undo()


def test_both_failed_responses_are_saved_and_no_third_request(tmp_path):
    undo=install(tmp_path)
    try:
        raw=json.dumps(body(True)).encode(); seen=[]
        model=APIModel('https://example.invalid/v1','offline','',transport=httpx.MockTransport(
            lambda req:seen.append(req) or httpx.Response(200,content=raw)))
        with pytest.raises(ModelProtocolError) as caught:
            model.decide({'task':'offline','memory_state':{'world':{}}},'',TOOLS,[])
        assert caught.value.request_attempts==len(seen)==2
        captures=[json.loads(s) for s in (tmp_path/'protocol_errors/captures.jsonl').read_text().splitlines()]
        assert len(captures)==2 and all(Path(c['raw_response_file']).read_bytes()==raw for c in captures)
    finally:undo()


def feedback(turn,tool='move_relative',blocked=True,xy=(0.,0.)):
    return {'turn':turn,'results':[{'tool':tool,'status':'failed' if blocked else 'succeeded',
        'error_code':'BOUNDARY_BLOCKED' if blocked else None}],
        'next_observation':{'local_odometry':{'translation_m':list(xy)}}}


def test_five_boundary_attempts_stop_even_with_intervening_observation_and_turn(tmp_path):
    from go2_demo.runner import RunLog
    undo=install(tmp_path)
    log=RunLog(tmp_path/'episode')
    try:
        for i in range(4):
            log.write('tool_results',**feedback(i*2))
            log.write('tool_results',**feedback(i*2+1,tool='observe' if i%2 else 'turn',blocked=False))
        assert not (tmp_path/'stop_reason.json').exists()
        with pytest.raises(KeyboardInterrupt):log.write('tool_results',**feedback(8))
        reason=json.loads((tmp_path/'stop_reason.json').read_text())
        assert reason['threshold']==5 and reason['last_decision']==9
        assert len((tmp_path/'episode/events.jsonl').read_text().splitlines())==9
    finally:log.close();undo()


def test_successful_move_or_meaningful_translation_resets_loop(tmp_path):
    from go2_demo.runner import RunLog
    undo=install(tmp_path);log=RunLog(tmp_path/'episode')
    try:
        for i in range(4):log.write('tool_results',**feedback(i))
        log.write('tool_results',**feedback(4,blocked=False,xy=(.2,0.)))
        for i in range(5,9):log.write('tool_results',**feedback(i,xy=(.2,0.)))
        assert not (tmp_path/'stop_reason.json').exists()
        log.write('tool_results',**feedback(9,tool='turn',blocked=False,xy=(.35,0.)))
        log.write('tool_results',**feedback(10,xy=(.35,0.)))
        assert log._boundary_streak==1
    finally:log.close();undo()


def test_only_first_task_identity_resets_loop(tmp_path):
    from go2_demo.runner import RunLog
    undo=install(tmp_path);log=RunLog(tmp_path/'episode')
    try:
        def observation(label):return {'observation':{'memory_state':{'world':{'current_observation':{
            'target_candidates':[{'object_id':label}]}}}}}
        log.write('model_input',**observation('task:B'))
        for i in range(4):log.write('tool_results',**feedback(i))
        log.write('model_input',**observation('task:B'))
        assert log._boundary_streak==4
        log.write('model_input',**observation('task:A'))
        assert log._boundary_streak==0
        log.write('tool_results',**feedback(4))
        assert log._boundary_streak==1
    finally:log.close();undo()

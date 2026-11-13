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


def test_two_consecutive_gate_rejections_stop_after_logging_and_before_third_call(tmp_path):
    undo=install(tmp_path)
    try:
        class Model:
            count=0
            def decide(self,*args,**kwargs):
                self.count+=1
                return Decision([ToolCall(f'c{self.count}','turn',{'yaw_rad':.3})],planning_envelope={
                    'plan':{'subgoals':[{'subgoal_id':'s','description':'missing target',
                        'preconditions':[{'object_id':'unseen'}],'completion':[]}],
                        'branches':[],'recovery':'observe'},'subgoal_id':'s'})
        model=Model()
        metrics=run_episode(EpisodeBackend(),model,mode='api',run_dir=tmp_path/'episode',memory_v1=True,max_model_calls=10)
        assert model.count==metrics['model_calls']==2 and metrics['termination']=='interrupted'
        assert metrics['motion_calls']==0 and not metrics['success']
        rows=[json.loads(s) for s in (tmp_path/'episode/events.jsonl').read_text().splitlines()]
        assert sum(r['event']=='tool_results' for r in rows)==2
        assert json.loads((tmp_path/'stop_reason.json').read_text())['last_decision']==2
    finally:undo()

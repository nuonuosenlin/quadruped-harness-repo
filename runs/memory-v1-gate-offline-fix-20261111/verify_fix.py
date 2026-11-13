"""Reproduce diagnostics from existing logs and a local MockTransport only."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from go2_demo.harness import TOOLS
from go2_demo.memory import AsyncMemory, read_state
from go2_demo.memory_context import compact_observation
from go2_demo.memory_planning import MemoryPlanningHarness
from go2_demo.models import APIModel
import httpx

OUT = Path(__file__).parent
OLD = ROOT/'runs/memory-v1-h2-rerun-20261111-s0'
EPISODE = OLD/'H2/20261111-013742-api-memory_ab_occluded_v1-s0-9d3a30'


def text(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def main():
    rows = [json.loads(line) for line in (EPISODE/'events.jsonl').read_text().splitlines()]
    inputs = [r for r in rows if r['event']=='model_input']
    reductions = []
    for r in inputs:
        original = r['observation']
        normal = compact_observation(original)
        retry = compact_observation(original,retry=True)
        reductions.append({'decision':r['turn']+1,'before_input_chars':len(text(original)),
            'normal_input_chars':len(text(normal)), 'retry_input_chars':len(text(retry)),
            'normal_state_chars':len(text(normal['memory_state'])),
            'retry_state_chars':len(text(retry['memory_state']))})
    constraints = [{'decision':r['turn']+1, 'feedback':x,
        'input_active_plan_id':inputs[r['turn']]['observation']['memory_state']['world'].get('active_plan_id'),
        'input_objects':[{k:o[k] for k in ('object_id','state','last_seen','confidence')}
            for o in inputs[r['turn']]['observation']['memory_state']['objects']]}
        for r in rows if r['event']=='tool_results' for x in r['results']
        if x.get('error_code')=='MEMORY_CONSTRAINT']
    md=read_state((EPISODE/'memory.md').read_text())
    raw=(OLD/'protocol_error/response.raw').read_bytes()
    capture=json.loads((OLD/'protocol_error/capture.json').read_text())
    assert hashlib.sha256(raw).hexdigest()==capture['stored_sha256']
    wire=json.loads(raw); choice=wire['choices'][0]; msg=choice['message']
    envelope={'plan':{'subgoals':[{'subgoal_id':'scan','description':'offline safe scan',
        'preconditions':[],'completion':[]}],'branches':[],'recovery':'stop'},'subgoal_id':'scan'}
    good={'model':'offline-replay','choices':[{'finish_reason':'tool_calls','message':{
        'content':None,'reasoning_content':'synthetic','tool_calls':[{'id':'replay', 'type':'function',
        'function':{'name':'turn','arguments':text({'yaw_rad':.3,'planning':envelope})}}]}}],
        'usage':{'prompt_tokens':10,'completion_tokens':2,'total_tokens':12}}
    seen=[]
    def handle(request):
        seen.append(json.loads(request.content))
        return httpx.Response(200,content=raw) if len(seen)==1 else httpx.Response(200,json=good)
    model=APIModel('https://example.invalid/v1','offline-replay','',transport=httpx.MockTransport(handle))
    decision=model.decide(inputs[-1]['observation'],'',TOOLS,[])
    assert decision.request_attempts==2 and decision.planning_envelope==envelope
    assert decision.usage['total_tokens']==14512
    old_prompt=(EPISODE/'system_prompt.txt').read_text()
    old_tools=json.loads((EPISODE/'tools.json').read_text())
    prompt_chars={'scope':'serialized messages+tools only; characters, not token estimates',
        'before':len(text({'messages':[{'role':'system','content':old_prompt},
            {'role':'user','content':text(inputs[-1]['observation'])}],'tools':old_tools})),
        'normal':len(text({k:seen[0][k] for k in ('messages','tools')})),
        'retry':len(text({k:seen[1][k] for k in ('messages','tools')}))}
    # Use a fresh evidence snapshot for an explicit empty-precondition scan;
    # no target GT, previous model reasoning, or physical simulation is involved.
    replay_dir=OUT/'replay'
    replay_dir.mkdir(exist_ok=True)
    path=replay_dir/'memory.md'
    if path.exists():
        # AsyncMemory is append-only; use another local artifact for each replay.
        index=1
        while (replay_dir/f'memory-{index}.md').exists(): index+=1
        path=replay_dir/f'memory-{index}.md'
    memory=AsyncMemory(path)
    try:
        feedback,binding=MemoryPlanningHarness(memory).prepare(decision,0)
        assert feedback is None and binding['plan_id']=='plan-0001'
    finally:
        memory.close()
    before=json.loads((OUT/'before_hashes.json').read_text())
    after={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
           for p in sorted((ROOT/'go2_demo').glob('*.py'))}
    unchanged={name:before[name]==after[name] for name in [
        'go2_demo/scenarios.py','go2_demo/backend.py','go2_demo/harness.py',
        'go2_demo/ordered_evaluation.py','go2_demo/__main__.py','go2_demo/memory_perception.py',
        'go2_demo/memory.py']}
    assert all(unchanged.values())
    result={'old_episode':str(EPISODE),'raw_error_sha256':hashlib.sha256(raw).hexdigest(),
        'raw_error_structure':{'valid_json':True,'finish_reason':choice['finish_reason'],
            'content_chars':len(msg.get('content') or ''),'tool_calls_present':'tool_calls' in msg,
            'usage':wire['usage']},
        'constraint_evidence':constraints,'old_md_plan_count':len(md['plans']),
        'exact_old_envelope_subcase_recoverable':False,
        'old_input_max_chars':max(r['before_input_chars'] for r in reductions),
        'old_input_decrease_count':sum(b['before_input_chars']<a['before_input_chars'] for a,b in zip(reductions,reductions[1:])),
        'input_reductions':reductions,
        'decision45_prompt_char_comparison':prompt_chars,
        'offline_raw_response_replay':{'network':'MockTransport only','requests':len(seen),
            'usage':decision.usage,'diagnostics':decision.protocol_diagnostics,
            'retry_user_message_chars':len(seen[1]['messages'][1]['content']),
            'first_user_message_chars':len(seen[0]['messages'][1]['content']),
            'plan_gate_feedback':feedback,'plan_binding':binding},
        'unchanged_contract_hashes':unchanged,
        'changed_product_files':[name for name in after if before.get(name)!=after[name]],
        'after_hashes':after}
    (OUT/'evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'decision45':reductions[-1], 'old_input_max_chars':result['old_input_max_chars'],
        'old_input_decrease_count':result['old_input_decrease_count'],
        'constraint_count':len(constraints), 'replay':result['offline_raw_response_replay'],
        'prompt_char_comparison':prompt_chars,
        'unchanged_contracts':unchanged,'changed_product_files':result['changed_product_files']},ensure_ascii=False))


if __name__=='__main__': main()

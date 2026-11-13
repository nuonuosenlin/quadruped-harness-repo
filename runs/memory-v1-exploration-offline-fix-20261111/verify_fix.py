"""Pure data replay of saved public feedback. No API, keys, or simulation."""
from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from go2_demo.memory import MemoryRules, state_packet
from go2_demo.memory_context import compact_observation


def main():
    saved=json.loads((ROOT/'runs/memory-v1-h2-gate-rerun-20261111-s0/evidence.json').read_text())
    episode=Path(saved['episode'])
    rows=[json.loads(s) for s in (episode/'events.jsonl').read_text().splitlines()]
    inputs={r['turn']:r['observation']['memory_state']['world'] for r in rows if r['event']=='model_input'}
    results={r['turn']+1:r['next_observation'] for r in rows if r['event']=='tool_results'}
    # Original MD entries retain each adapter observation and tool-feedback source.
    from go2_demo.memory import read_state
    md=read_state((episode/'memory.md').read_text())
    per_step=defaultdict(lambda:{'objects':[],'actions':[],'measurements':{}})
    plans=defaultdict(list)
    for r in md['ledger']:
        step=r['step']
        if r['kind']=='observation_confirmed':per_step[step]['objects'].append(r['observation'])
        elif r['kind'] in {'action_executed','action_failed'}:per_step[step]['actions'].append(r['action'])
        elif r['kind']=='measurement':per_step[step]['measurements'][r['name']]={'value':r['value'],'source':r['source']}
        elif r['kind']=='plan_registered':plans[step].append(r['plan_id'])
    original_plans={p['plan_id']:{'subgoals':[{k:g[k] for k in ('subgoal_id','description','preconditions','completion')}
                    for g in p['subgoals']],'branches':p['branches'],'recovery':p['recovery']} for p in md['plans']}
    spec=importlib.util.spec_from_file_location('before_exploration_rules',OUT/'source_before/memory.py')
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    spec_plan=importlib.util.spec_from_file_location('go2_demo._exploration_before_planning',OUT/'source_before/memory_planning.py')
    old_planning=importlib.util.module_from_spec(spec_plan);spec_plan.loader.exec_module(old_planning)
    from go2_demo.types import Decision,ToolCall
    class Snapshot:
        error=None
        def __init__(self):self.rules=old.MemoryRules()
        def snapshot(self):return deepcopy(self.rules.state)
        def plan(self,*args,**kwargs):self.rules.set_plan(*args,**kwargs)
    envelope={'plan':{'subgoals':[{'subgoal_id':'explore_viewpoint','description':'offline viewpoint change',
        'preconditions':[],'completion':[]}],'branches':[],'recovery':'stop'},'subgoal_id':'explore_viewpoint'}
    original_gate_feedback,_=old_planning.MemoryPlanningHarness(Snapshot()).prepare(
        Decision([ToolCall('proof','move_relative',{'forward_m':.2,'lateral_m':0.})],planning_envelope=envelope),0)
    assert original_gate_feedback is None
    before=old.MemoryRules();after=MemoryRules()
    snapshots=[]
    for step in range(121):
        world=inputs.get(step,md['world']['public_context'])
        view=world['current_observation']
        payload={**deepcopy(per_step[step]),'step':step,'public_context':{'current_observation':view}}
        for rules in (before,after):
            rules.update(payload)
            for pid in plans[step]:rules.set_plan(pid,original_plans[pid])
        snapshots.append({'step':step,'exploration':deepcopy(after.state['world']['exploration'])})
    def summarize(rules):
        return {'B_relocations':[r for r in rules.state['ledger'] if r['kind']=='target_relocated' and r['object_id']=='task:B'],
            'candidate_rejections':[r for r in rules.state['ledger'] if r['kind']=='relocation_candidate_rejected'],
            'search_stalls':[r for r in rules.state['ledger'] if r['kind']=='search_stalled'],
            'replan_reasons':dict(Counter(r.get('reason','other') for r in rules.state['events'] if r['kind']=='replan_required')),
            'skill_stuck_count':sum(r['kind']=='skill_stuck' for r in rules.state['events'])}
    before_summary=summarize(before);after_summary=summarize(after)
    assert len(before_summary['B_relocations'])==6
    assert before_summary['replan_reasons']=={'positive_position_contradiction':6,'verification_expired':24}
    assert before_summary['skill_stuck_count']==0
    assert len(after_summary['B_relocations'])==3 and len(after_summary['candidate_rejections'])==3
    assert after_summary['search_stalls'][0]['step']==10
    assert len(after_summary['search_stalls'])==1
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((ROOT/'go2_demo').glob('*.py'))}
    baseline=json.loads((OUT/'before_hashes.json').read_text())
    unchanged={name:hashes[name]==baseline[name] for name in [
        'go2_demo/scenarios.py','go2_demo/backend.py','go2_demo/harness.py','go2_demo/ordered_evaluation.py',
        'go2_demo/runner.py','go2_demo/models.py','go2_demo/__main__.py','go2_demo/memory_perception.py']}
    assert all(unchanged.values())
    packet=compact_observation({'task':'offline replay','memory_state':state_packet(after.state,120)})
    assert packet['memory_state']['world']['exploration']['stalled']
    evidence={'replay_source':str(episode),'source':'saved adapter observations and public tool feedback only',
        'archived_original_gate_accepts_target_free_exploration':original_gate_feedback is None,
        'before':before_summary,'after':after_summary,'progress_snapshots':snapshots,
        'unchanged_contract_hashes':unchanged,'changed_product_files':[p for p in hashes if hashes[p]!=baseline.get(p)],
        'after_hashes':hashes,'final_prompt_state':packet['memory_state']}
    (OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    (OUT/'replay_memory.md').write_text(after.document())
    print(json.dumps({'before_relocations':len(before_summary['B_relocations']),
        'after_relocations':len(after_summary['B_relocations']),
        'after_candidate_rejections':len(after_summary['candidate_rejections']),
        'first_search_stall_step':after_summary['search_stalls'][0]['step'],
        'before_replan_reasons':before_summary['replan_reasons'],
        'after_replan_reasons':after_summary['replan_reasons'],
        'before_skill_stuck':before_summary['skill_stuck_count'],
        'after_skill_stuck':after_summary['skill_stuck_count'],
        'changed_product_files':evidence['changed_product_files'],
        'unchanged_contract_hashes':unchanged},ensure_ascii=False))


if __name__=='__main__':main()

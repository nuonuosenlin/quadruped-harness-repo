"""Pure saved-data replay and source audit; no model, key or dynamics."""
from collections import defaultdict,Counter
from copy import deepcopy
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
import go2_demo.memory as memory
from go2_demo.memory_context import compact_observation


def main():
    ep=ROOT/'runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417'
    md=memory.read_state((ep/'memory.md').read_text())
    rows=[json.loads(s) for s in (ep/'events.jsonl').read_text().splitlines()]
    inputs={r['turn']:r['observation']['memory_state']['world'] for r in rows if r['event']=='model_input'}
    grouped=defaultdict(lambda:{'objects':[],'actions':[],'measurements':{}});registered=defaultdict(list)
    plans={p['plan_id']:{'subgoals':[{k:g[k] for k in ('subgoal_id','description','preconditions','completion')}
        for g in p['subgoals']],'branches':p['branches'],'recovery':p['recovery']} for p in md['plans']}
    for r in md['ledger']:
        if r['kind']=='observation_confirmed':grouped[r['step']]['objects'].append(r['observation'])
        elif r['kind'] in {'action_executed','action_failed'}:grouped[r['step']]['actions'].append(r['action'])
        elif r['kind']=='measurement':grouped[r['step']]['measurements'][r['name']]={'value':r['value'],'source':r['source']}
        elif r['kind']=='plan_registered':registered[r['step']].append(r['plan_id'])
    spec=importlib.util.spec_from_file_location('before_search_clock',OUT/'source_before/memory.py')
    before=importlib.util.module_from_spec(spec);spec.loader.exec_module(before)
    def replay(rules):
        history=[]
        for step in range(121):
            world=inputs.get(step,md['world']['public_context'])
            rules.update({'step':step,**deepcopy(grouped[step]),'public_context':{
                'current_observation':world['current_observation']}})
            for pid in registered[step]:rules.set_plan(pid,plans[pid])
            history.append({'after_decision':step,'exploration':deepcopy(rules.state['world']['exploration'])})
        return history
    old=before.MemoryRules();replay(old)
    assert not any(r['kind']=='search_review_due' for r in old.state['ledger'])
    variants={};original_interval=memory.SEARCH_REVIEW_INTERVAL
    try:
        for interval in (12,16,20):
            memory.SEARCH_REVIEW_INTERVAL=interval
            rule=memory.MemoryRules();history=replay(rule)
            due=[r for r in rule.state['ledger'] if r['kind']=='search_review_due']
            variants[str(interval)]={'review_steps':[r['step'] for r in due],
                'final_age':history[-1]['exploration']['decisions_since_task_novelty'],
                'search_stalled_steps':[r['step'] for r in rule.state['ledger'] if r['kind']=='search_stalled'],
                'event_counts':dict(Counter(e['kind'] for e in rule.state['events']))}
            if interval==12:chosen=rule;chosen_history=history;chosen_due=due
    finally:memory.SEARCH_REVIEW_INTERVAL=original_interval
    assert variants['12']['review_steps']==list(range(12,121,12))
    assert variants['12']['final_age']==120
    assert variants['12']['search_stalled_steps']==[]
    assert variants['12']['event_counts'].get('skill_stuck',0)==0
    assert variants['12']['event_counts'].get('key_precondition_invalidated',0)==sum(e['kind']=='key_precondition_invalidated' for e in old.state['events'])
    assert [p['subgoals'] for p in chosen.state['plans']]==[p['subgoals'] for p in old.state['plans']] or all(
        [g['status'] for g in p['subgoals']]==[g['status'] for g in q['subgoals']]
        for p,q in zip(chosen.state['plans'],old.state['plans']))
    # Whole ledger IDs change with appended advisory events; compare goal states.
    def method(path,name):
        tree=ast.parse(path.read_text())
        return next(n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==name)
    ast_unchanged={name:ast.dump(method(OUT/'source_before/memory.py',name),include_attributes=False)==
        ast.dump(method(ROOT/'go2_demo/memory.py',name),include_attributes=False)
        for name in ('predicate','validate_plan','validate_check')}
    ast_unchanged['planning_prepare']=ast.dump(method(OUT/'source_before/memory_planning.py','prepare'),include_attributes=False)==ast.dump(
        method(ROOT/'go2_demo/memory_planning.py','prepare'),include_attributes=False)
    assert all(ast_unchanged.values())
    baseline=json.loads((OUT/'before_hashes.json').read_text())
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('go2_demo','tests','scripts','docs')
        for p in sorted((ROOT/folder).rglob('*')) if p.is_file() and p.suffix in ('.py','.sh','.md')}
    changed=[p for p in hashes if baseline.get(p)!=hashes[p]]
    assert sorted(p for p in changed if p.startswith('go2_demo/'))==['go2_demo/memory.py','go2_demo/memory_planning.py']
    evidence={'source_episode':str(ep),'scope':'saved public feedback/observations; no tool execution or geometry truth used by clock',
        'threshold_candidates':variants,'chosen_interval':12,'chosen_review_ledger':chosen_due,
        'chosen_clock_history':chosen_history,'unchanged_gate_ast':ast_unchanged,
        'plan_goal_statuses_unchanged_in_data_replay':True,'changed_files':changed,'after_hashes':hashes,
        'product_hashes':{k:v for k,v in hashes.items() if k.startswith('go2_demo/')},
        'final_compact_state':compact_observation({'task':'offline data replay','memory_state':memory.state_packet(chosen.state,120)})}
    (OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    (OUT/'replay_memory.md').write_text(chosen.document())
    print(json.dumps({'threshold_candidates':variants,'unchanged_gate_ast':ast_unchanged,'changed_files':changed},ensure_ascii=False,indent=2))


if __name__=='__main__':main()

"""Offline evidence collection. Never calls a model or reads credentials."""
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path('/home/nuonuosenlin/Agent-harness')
OUT = ROOT/'runs/memory-v1-h2-search-budget-rerun-20261111-s0'
sys.path.insert(0,str(ROOT))
from go2_demo.memory import read_state


def main():
    episodes=[p for p in (OUT/'H2').iterdir() if (p/'events.jsonl').exists()]
    assert len(episodes)==1, 'Only one real episode is authorized'
    ep=episodes[0]
    assert (ep/'metrics.json').exists(), 'Episode has not ended'
    metrics=json.loads((ep/'metrics.json').read_text())
    rows=[json.loads(s) for s in (ep/'events.jsonl').read_text().splitlines()]
    inputs=[r for r in rows if r['event']=='model_input']
    responses=[r for r in rows if r['event']=='model_response']
    results=[r for r in rows if r['event']=='tool_results']
    xy=[[0.,0.]]+[r['next_observation']['local_odometry']['translation_m'] for r in results]
    route={'source':'existing_public_idealized_simulator_odometry; offline diagnosis only',
        'x_bounds_m':[min(p[0] for p in xy),max(p[0] for p in xy)],
        'y_bounds_m':[min(p[1] for p in xy),max(p[1] for p in xy)],
        'final_xy_m':xy[-1],'max_radius_from_start_m':max(math.hypot(*p) for p in xy),
        'final_radius_from_start_m':math.hypot(*xy[-1])}
    protocols=[r for r in rows if r['event']=='model_protocol']
    md=read_state((ep/'memory.md').read_text())
    config=json.loads((OUT/'config.json').read_text())
    current={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted((ROOT/'go2_demo').glob('*.py'))}
    assert current==config['code_sha256'], 'Source changed during run'
    manifest=json.loads((ep/'manifest.json').read_text())
    h0path=ROOT/config['H0_reference']
    h0=json.loads(h0path.read_text())
    h0manifest=json.loads((h0path.parent/'manifest.json').read_text())
    comparison={k:manifest[k]==h0manifest[k] for k in ('task','task_id','seed','model','budgets','evaluation','asset_lock_sha256')}
    comparison['api_settings']=all(manifest['api_settings'][k]==h0manifest['api_settings'][k]
                                   for k in ('timeout_s','max_output_tokens','thinking'))
    assert all(comparison.values()), comparison
    def first(tool,successful=True):
        for row in results:
            if any(r['tool']==tool and (not successful or r['status']=='succeeded') for r in row['results']):
                return row['turn']+1
    captures=[]
    capturefile=OUT/'protocol_errors/captures.jsonl'
    if capturefile.exists():
        for line in capturefile.read_text().splitlines():
            capture=json.loads(line)
            if capture['body_available']:
                raw=Path(capture['raw_response_file']).read_bytes()
                assert hashlib.sha256(raw).hexdigest()==capture['stored_sha256']
                try:wire=json.loads(raw)
                except (ValueError,UnicodeError):capture['response_structure']={'valid_json':False}
                else:
                    choices=wire.get('choices') if isinstance(wire,dict) else None
                    summaries=[]
                    for c in choices if isinstance(choices,list) else []:
                        if not isinstance(c,dict):continue
                        msg=c.get('message') or {}
                        if not isinstance(msg,dict):continue
                        summaries.append({'finish_reason':c.get('finish_reason'),
                            'content_chars':len(msg.get('content') or '') if isinstance(msg.get('content'),str) else None,
                            'tool_calls':msg.get('tool_calls')})
                    capture['response_structure']={'valid_json':True,'choices':summaries,
                        'usage':wire.get('usage') if isinstance(wire,dict) else None}
            captures.append(capture)
    retries=[{'decision':r['turn']+1,'attempts':r['request_attempts'],
              'diagnostics':r['diagnostics'],'recovered':r['diagnostics'][-1]['kind']=='OK'}
             for r in protocols if r['request_attempts']>1]
    a=metrics.get('checkpoints',{}).get('A',{})
    a_time=a.get('sim_time_s') if a.get('passed') else None
    a_decision=next((r['turn']+1 for r in results if a_time is not None and
                    r['next_observation']['sim_time_s']>=a_time-1e-8),None)
    target_reads={}
    for label in ('A','B'):
        target_reads[label]=[{'decision':r['turn']+1,'object':o}
            for r in inputs for o in r['observation']['memory_state']['objects'] if o['object_id']==f'task:{label}']
    target_objects=[o for o in md['objects'] if o['object_id'].startswith('task:')]
    target_ledger=[r for r in md['ledger'] if r.get('object_id','').startswith('task:') or
                    r.get('observation',{}).get('object_id','').startswith('task:')]
    search_stalls=[r for r in md['ledger'] if r['kind']=='search_stalled']
    stall_inputs=[{'decision':r['turn']+1,'exploration':r['observation']['memory_state']['world'].get('exploration'),
                   'events':r['observation']['memory_state']['events']}
                 for r in inputs if r['observation']['memory_state']['world'].get('exploration',{}).get('stalled')]
    first_stall_decision=stall_inputs[0]['decision'] if stall_inputs else None
    followup=[{'decision':r['turn']+1,'calls':r['calls'],'planning_envelope':r.get('planning_envelope')}
              for r in responses if first_stall_decision is not None and r['turn']+1>=first_stall_decision]
    tool_counts=Counter(r['tool'] for row in results for r in row['results'])
    failures=Counter(r.get('error_code','unspecified') for row in results for r in row['results'] if r['status']=='failed')
    stop_path=OUT/'stop_reason.json'
    first_objects=next(({'decision':r['turn']+1,'objects':r['observation']['memory_state']['objects']}
                       for r in inputs if r['observation']['memory_state']['objects']),None)
    evidence={'episode':str(ep),'metrics_file':str(ep/'metrics.json'),'memory_file':str(ep/'memory.md'),
        'metrics':metrics,'config':config,'real_api_episodes':1,
        'public_odometry_route_summary':route,
        'nonempty_reasoning_missing_decisions':[r['turn']+1 for r in responses if not r['reasoning_present']],
        'startup_failure':json.loads((OUT/'startup_failure.json').read_text()) if (OUT/'startup_failure.json').exists() else None,
        'source_unchanged':True,'H0_condition_comparison':comparison,
        'H0_metrics':h0,'H0_metrics_sha256':hashlib.sha256(h0path.read_bytes()).hexdigest(),
        'first_successful_turn_decision':first('turn'),'first_successful_translation_decision':first('move_relative'),
        'first_translation_attempt_decision':first('move_relative',False),
        'search_stall_ledger':search_stalls,'stalled_inputs':stall_inputs,
        'max_turns_without_progress_in_inputs':max((r['observation']['memory_state']['world'].get('exploration',{}).get(
            'successful_turns_without_search_progress',0) for r in inputs),default=0),
        'requested_translation_path_m':sum(math.hypot(c['arguments']['forward_m'],c['arguments']['lateral_m'])
            for r in responses for c in r['calls'] if c['name']=='move_relative'),
        'first_stalled_input_decision':first_stall_decision,'responses_from_first_stall':followup,
        'all_move_results':[{'decision':r['turn']+1,'result':x}
                            for r in results for x in r['results'] if x['tool']=='move_relative'],
        'all_stop_abort_results':[{'decision':r['turn']+1,'result':x}
                                  for r in results for x in r['results'] if x['tool'] in {'stop','abort','finish'}],
        'tool_counts':dict(tool_counts),'failure_counts':dict(failures),
        'finish_decisions':[r['turn']+1 for r in responses if any(c['name']=='finish' for c in r['calls'])],
        'first_valid_objects':first_objects,'target_reads':target_reads,'target_objects_in_md':target_objects,
        'target_evidence_ledger':target_ledger,'ledger_size':len(md['ledger']),
        'B_relocation_count':sum(r.get('kind')=='target_relocated' and r.get('object_id')=='task:B' for r in target_ledger),
        'plans_in_md':md['plans'],'final_pose_in_md':md['pose'],
        'A_candidate_input_count':sum(any(c.get('task_label')=='A' for c in
            r['observation']['memory_state']['world']['current_observation']['target_candidates']) for r in inputs),
        'memory_event_counts':dict(Counter(r['kind'] for r in md['events'])),
        'requested_turn_yaw_sum_rad':sum(c['arguments']['yaw_rad'] for r in responses for c in r['calls'] if c['name']=='turn'),
        'A_checkpoint_decision_by_sim_time':a_decision,'B_reads_after_A':[
            r for r in target_reads['B'] if a_decision is not None and r['decision']>a_decision],
        'protocol_error_count':len(captures),'length_count':sum(c.get('diagnostic',{}).get('kind')=='TRUNCATED_RESPONSE' for c in captures),
        'protocol_captures':captures,'successful_repair_decisions':retries,
        'user_stop':json.loads(stop_path.read_text()) if stop_path.exists() else None,
        'last_results':results[-6:], 'last_plans':[{'decision':r['turn']+1,'planning_envelope':r.get('planning_envelope')}
            for r in responses[-6:]],
        'last_input_world':inputs[-1]['observation']['memory_state']['world'] if inputs else None}
    (OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    summary={k:evidence[k] for k in ('episode','first_successful_turn_decision','first_successful_translation_decision',
        'first_translation_attempt_decision','tool_counts','failure_counts','protocol_error_count','length_count',
        'successful_repair_decisions','A_checkpoint_decision_by_sim_time','user_stop')}
    summary['B_read_decisions']=[r['decision'] for r in target_reads['B']]
    summary['B_read_decisions_after_A']=[r['decision'] for r in evidence['B_reads_after_A']]
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    print(json.dumps(metrics,ensure_ascii=False,indent=2))


if __name__=='__main__':main()

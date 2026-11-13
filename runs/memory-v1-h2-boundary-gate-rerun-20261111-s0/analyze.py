"""Post-run evidence only; no API, simulation, or credential access."""
from pathlib import Path
import json,math,sys
from collections import Counter
import collect

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
sys.path.insert(0,str(ROOT))
from go2_demo.memory import read_state
from go2_demo.scenarios import get_scenario


def main():
    collect.main()
    evidence=json.loads((OUT/'evidence.json').read_text())
    ep=Path(evidence['episode'])
    rows=[json.loads(s) for s in (ep/'events.jsonl').read_text().splitlines()]
    inputs=[r for r in rows if r['event']=='model_input']
    responses=[r for r in rows if r['event']=='model_response']
    results=[r for r in rows if r['event']=='tool_results']
    md=read_state((ep/'memory.md').read_text())
    scene=get_scenario('memory_ab_occluded_v1')
    trajectory=[json.loads(s) for s in (ep/'trajectory.jsonl').read_text().splitlines()]
    interventions=[]
    for index,row in enumerate(results):
        for result in row['results']:
            if result.get('error_code')!='BOUNDARY_BLOCKED':continue
            response=next(r for r in responses if r['turn']==row['turn'])
            call=next(c for c in response['calls'] if c['name']=='move_relative')
            before_time=results[index-1]['next_observation']['sim_time_s'] if index else trajectory[0]['sim_time_s']
            point=min(trajectory,key=lambda p:abs(p['sim_time_s']-before_time))
            x,y,_=point['base_xyz_m'];yaw=point['yaw_rad']
            f,l=call['arguments']['forward_m'],call['arguments']['lateral_m']
            endpoint=[x+math.cos(yaw)*f-math.sin(yaw)*l,y+math.sin(yaw)*f+math.cos(yaw)*l]
            following=next(({'decision':r['turn']+1,'result':z} for r in results[index+1:]
                for z in r['results'] if z['tool']=='move_relative' and z['status']=='succeeded'),None)
            nextinput=next((r for r in inputs if r['turn']==row['turn']+1),None)
            interventions.append({'decision':row['turn']+1,'call':call,'refusal':result,
                'recorded_gt_pose_before':[x,y,yaw],'pose_time_error_s':abs(point['sim_time_s']-before_time),
                'nominal_center_endpoint_xy_m':endpoint,
                'nominal_center_would_exit_platform':abs(endpoint[0])>scene.floor_half_size_m[0] or abs(endpoint[1])>scene.floor_half_size_m[1],
                'next_input_feedback':nextinput['observation']['memory_state']['world'].get('last_tool_feedback') if nextinput else None,
                'next_successful_translation':following})
    reviews=[r for r in md['ledger'] if r['kind']=='search_review_due']
    route=[{'decision':0,'xy_m':[0.,0.]}]+[{'decision':r['turn']+1,'xy_m':r['next_observation']['local_odometry']['translation_m']} for r in results]
    for point in route:point['distance_to_A_m']=math.dist(point['xy_m'],scene.target.xy)
    monitor=OUT/'boundary_monitor.jsonl'
    audits=[json.loads(s) for s in monitor.read_text().splitlines()] if monitor.exists() else []
    memory_boundary_actions=[r for r in md['ledger'] if (r.get('action') or {}).get('error_code')=='BOUNDARY_BLOCKED']
    assert not memory_boundary_actions
    lines=(ep/'memory.md').read_text().splitlines()
    mdrefs={obj['object_id']:[i+1 for i,s in enumerate(lines) if '\"object_id\": \"'+obj['object_id']+'\"' in s][:2]
            for obj in md['objects'] if obj['object_id'].startswith('task:')}
    extended={'boundary_interventions':interventions,'boundary_block_count':len(interventions),
        'boundary_monitor':audits,'maximum_blocked_move_attempt_streak':max((a['consecutive_blocked_move_attempts'] for a in audits),default=0),
        'boundary_actions_written_to_memory':memory_boundary_actions,
        'search_review_ledger':reviews,'search_review_due_input_decisions':[r['turn']+1 for r in inputs if r['observation']['memory_state']['world'].get('exploration',{}).get('review_due')],
        'route_decision_points':route,'minimum_route_distance_to_A':min(route,key=lambda r:r['distance_to_A_m']),
        'final_route_distance_to_A_m':route[-1]['distance_to_A_m'],
        'first_A_candidate_input_decision':next((r['turn']+1 for r in inputs if any(c.get('task_label')=='A' for c in r['observation']['memory_state']['world']['current_observation']['target_candidates'])),None),
        'successful_translation_count':sum(z['tool']=='move_relative' and z['status']=='succeeded' for r in results for z in r['results']),
        'memory_object_line_references':mdrefs,
        'truth_disclosure':'temporary experimental safety interlock uses simulator GT base pose + scene platform bounds; not non-GT perception or navigation measurement',
        'experimental':True,'final_design_pending_group_meeting_decision':True,
        'boundary_fall_aversion_claim':'only observed command refusals and actual fallen flag can be reported; no counterfactual physics run'}
    evidence.update(extended)
    (OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    summary={k:extended[k] for k in ['boundary_block_count','maximum_blocked_move_attempt_streak','first_A_candidate_input_decision','minimum_route_distance_to_A','successful_translation_count']}
    summary.update(metrics=evidence['metrics'],episode=str(ep),memory_file=str(ep/'memory.md'),
        finish_decisions=evidence['finish_decisions'],protocol_error_count=evidence['protocol_error_count'],length_count=evidence['length_count'],user_stop=evidence['user_stop'])
    (OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print('Boundary block decisions:',[x['decision'] for x in interventions])
    print('Review steps:',[r['step'] for r in reviews])
    print('A candidate first:',extended['first_A_candidate_input_decision'])
    print('Route minimum A distance:',extended['minimum_route_distance_to_A'])
    print('Boundary feedback absent from memory actions:',not memory_boundary_actions)


if __name__=='__main__':main()

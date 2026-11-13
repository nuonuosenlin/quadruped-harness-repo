"""Post-run analysis only: no policy, mj_step, model client, credentials or edits."""
from collections import Counter
import csv
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT=Path('/home/nuonuosenlin/Agent-harness')
OUT=ROOT/'runs/memory-v1-route-review-20261111'
EP=ROOT/'runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417'
sys.path.insert(0,str(ROOT))
import numpy as np
import mujoco
from go2_demo.scenarios import get_scenario


def hashes():
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
        for folder in ('go2_demo','tests','scripts','docs') for p in sorted((ROOT/folder).rglob('*'))
        if p.is_file() and p.suffix in ('.py','.sh','.md')}


def wrap(a):return math.atan2(math.sin(a),math.cos(a))


def main():
    OUT.mkdir(exist_ok=True)
    initial=hashes()
    recorded=json.loads((EP/'manifest.json').read_text())['code_sha256']
    assert all(initial[k]==v for k,v in recorded.items())
    rows=[json.loads(s) for s in (EP/'events.jsonl').read_text().splitlines()]
    inputs={r['turn']+1:r['observation'] for r in rows if r['event']=='model_input'}
    results={r['turn']+1:r for r in rows if r['event']=='tool_results'}
    responses={r['turn']+1:r for r in rows if r['event']=='model_response'}
    trace=[json.loads(s) for s in (EP/'trajectory.jsonl').read_text().splitlines()]
    by_time={round(r['sim_time_s'],5):r for r in trace}
    # Recover episode-to-world transform from a saved matched timestamp.
    transforms=[]
    for r in results.values():
        obs=r['next_observation'];t=by_time.get(round(obs['sim_time_s'],5))
        if t is None:continue
        od=obs['local_odometry'];yaw0=wrap(t['yaw_rad']-od['yaw_rad'])
        c,s=math.cos(yaw0),math.sin(yaw0);dx,dy=od['translation_m']
        transforms.append((t['base_xyz_m'][0]-c*dx+s*dy,t['base_xyz_m'][1]-s*dx-c*dy,yaw0))
    p0=transforms[0]
    assert max(math.dist(p0[:2],p[:2]) for p in transforms)<1e-7
    assert max(abs(wrap(p[2]-p0[2])) for p in transforms)<1e-7
    def world(od):
        c,s=math.cos(p0[2]),math.sin(p0[2]);x,y=od['translation_m']
        return [p0[0]+c*x-s*y,p0[1]+s*x+c*y]
    poses={0:{'xy':[p0[0],p0[1]],'yaw':p0[2],'z':.34}}
    for k,r in results.items():
        obs=r['next_observation']; od=obs['local_odometry'];t=by_time.get(round(obs['sim_time_s'],5))
        poses[k]={'xy':world(od),'yaw':wrap(od['yaw_rad']+p0[2]),'z':t['base_xyz_m'][2] if t else .34}
    A=np.array([6.4,0.]);moves=[]
    for k,r in responses.items():
        call=r['calls'][0]
        if call['name']!='move_relative':continue
        pre,post=poses[k-1],poses[k];b=np.array(pre['xy']);a=np.array(post['xy']);delta=a-b
        d0=float(np.linalg.norm(A-b));d1=float(np.linalg.norm(A-a))
        args=call['arguments'];yy=pre['yaw']
        requested=[math.cos(yy)*args['forward_m']-math.sin(yy)*args['lateral_m'],
                   math.sin(yy)*args['forward_m']+math.cos(yy)*args['lateral_m']]
        moves.append({'decision':k,'forward_m':args['forward_m'],'lateral_m':args['lateral_m'],
            'yaw_before_deg':math.degrees(yy),'before_xy':pre['xy'],'after_xy':post['xy'],
            'actual_delta_xy':delta.tolist(),'requested_world_delta_xy':requested,
            'distance_A_before_m':d0,'distance_A_after_m':d1,'distance_A_reduction_m':d0-d1,
            'heading_error_to_A_deg':math.degrees(wrap(math.atan2(A[1]-b[1],A[0]-b[0])-yy)),
            'status':results[k]['results'][0]['status'],
            'plan':r.get('planning_envelope')})
    # Static geometry only; constructor uses _make_model + mj_forward, no policy/dynamics.
    spec=importlib.util.spec_from_file_location('static_scene_check',ROOT/'runs/memory-v1-demo-feasibility/candidate_preflight.py')
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    class Checker(helper.SceneCheck):
        def make_labels(self,xy):return [self.label('A',xy,['scenario_target'])]
    checker=Checker(get_scenario('memory_ab_occluded_v1'))
    np.testing.assert_allclose(checker.data.geom_xpos[checker.names['scenario_target']],[6.4,0.,.12],atol=1e-10)
    np.testing.assert_allclose(checker.model.geom_size[checker.names['scenario_target']][0],.12,atol=1e-10)
    np.testing.assert_allclose(checker.data.geom_xpos[checker.names['memory_drawers_body']],[3.8,0.,1.],atol=1e-10)
    np.testing.assert_allclose(checker.model.geom_size[checker.names['memory_drawers_body']],[.22,2.,1.],atol=1e-10)
    visibility=[]
    for k,p in poses.items():
        checker.set_pose(p['xy'],p['yaw'])
        v=checker.visible(checker.labels[0])
        visibility.append({'after_decision':k,'base_xy':p['xy'],'yaw_deg':math.degrees(p['yaw']),**v})
    # A continuous enclosure proves occlusion regardless of heading or body tilt.
    # Trace xyz is privileged POSTHOC evidence, never sent to a planner.
    base_xyz=np.array([r['base_xyz_m'] for r in trace]+[[p0[0],p0[1],.34]])
    mount=float(np.linalg.norm(checker.model.cam_pos[checker.camera_id]))
    camera_lo=base_xyz.min(axis=0)-mount;camera_hi=base_xyz.max(axis=0)+mount
    target_lo=np.array([6.28,-.12,0.]);target_hi=np.array([6.52,.12,.24])
    plane=3.8
    fractions=[(plane-cx)/(ax-cx) for cx,ax in itertools.product(
        [camera_lo[0],camera_hi[0]],[target_lo[0],target_hi[0]])]
    crossings_y=[(1-t)*cy+t*ay for t,cy,ay in itertools.product(
        [min(fractions),max(fractions)],[camera_lo[1],camera_hi[1]],[target_lo[1],target_hi[1]])]
    crossings_z=[(1-t)*cz+t*az for t,cz,az in itertools.product(
        [min(fractions),max(fractions)],[max(0.,camera_lo[2]),camera_hi[2]],[target_lo[2],target_hi[2]])]
    proof={'camera_xy_box_m':[camera_lo[:2].tolist(),camera_hi[:2].tolist()],
        'camera_z_upper_m':float(camera_hi[2]),'cabinet_plane_x_m':plane,
        'ray_crossing_y_interval_m':[min(crossings_y),max(crossings_y)],
        'ray_crossing_z_interval_m':[min(crossings_z),max(crossings_z)],
        'occluded_for_all_yaws':bool(camera_hi[0]<3.58 and 6.28>4.02 and
            min(crossings_y)>-2 and max(crossings_y)<2 and max(crossings_z)<2),
        'scope':'all recorded trajectory xyz expanded by full camera mount norm; arbitrary yaw/tilt; positive-height cameras; below-ground rays are floor-blocked'}
    assert proof['occluded_for_all_yaws']
    # Spatial coverage is a descriptive diagnostic, not free-space evidence.
    cells={(math.floor(p['xy'][0]/.5),math.floor(p['xy'][1]/.5)) for p in poses.values()}
    turn_run=0;run_max=0
    for k,r in responses.items():
        if r['calls'][0]['name']=='turn':turn_run+=1
        elif r['calls'][0]['name']=='move_relative':turn_run=0
        run_max=max(run_max,turn_run)
    no_candidate_ages=[];seen=set();last_new=0
    for k,obs in inputs.items():
        ids={c['object_id'] for c in obs['memory_state']['world']['current_observation']['target_candidates']}
        if ids-seen:last_new=k
        seen|=ids
        no_candidate_ages.append({'decision':k,'since_first_new_task_candidate_decisions':k-last_new})
    turns=[r['calls'][0]['arguments']['yaw_rad'] for r in responses.values() if r['calls'][0]['name']=='turn']
    summary={'episode':str(EP),'source_scope':'public odometry + tool calls; trace/scenario GT and rays used only for posthoc visibility diagnosis',
        'matches_episode_product_hashes':True,
        'turn_direction_counts':{'positive':sum(a>0 for a in turns),'negative':sum(a<0 for a in turns)},
        'translation_request_distribution':dict(Counter(m['forward_m'] for m in moves)),
        'episode_to_world':p0,'moves':moves,'move_count':len(moves),
        'moves_reducing_A_distance':[m['decision'] for m in moves if m['distance_A_reduction_m']>.001],
        'moves_increasing_A_distance':[m['decision'] for m in moves if m['distance_A_reduction_m']<-.001],
        'total_requested_translation_m':sum(math.hypot(m['forward_m'],m['lateral_m']) for m in moves),
        'sum_observed_move_chords_m':sum(math.hypot(*m['actual_delta_xy']) for m in moves),
        'initial_distance_A_m':math.dist(p0[:2],A),'final_distance_A_m':math.dist(poses[120]['xy'],A),
        'minimum_A_distance_at_decision_views_m':min(math.dist(p['xy'],A) for p in poses.values()),
        'base_xyz_bounds_m':[base_xyz.min(axis=0).tolist(),base_xyz.max(axis=0).tolist()],
        'observed_halfmetre_cells':len(cells),'max_turns_between_translation':run_max,
        'no_new_candidate_ages':no_candidate_ages,'A_visibility_at_nominal_grounded_views':visibility,
        'frustum_nonempty_view_count':sum(v['frustum_surface_samples']>0 for v in visibility),
        'visible_positive_view_count':sum(v['visible_positive_certificate'] for v in visibility),
        'sampled_ray_blockers':dict(sum((Counter(v['occluding_geom_samples']) for v in visibility),Counter())),
        'continuous_occlusion_proof':proof,'source_hashes_before':initial,'source_unchanged':hashes()==initial}
    assert summary['source_unchanged']
    (OUT/'evidence.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    with (OUT/'moves.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['decision','forward','yaw_deg','before_x','before_y','after_x','after_y','A_distance_before','A_distance_after','A_distance_reduction'])
        for m in moves:writer.writerow([m['decision'],m['forward_m'],m['yaw_before_deg'],*m['before_xy'],*m['after_xy'],m['distance_A_before_m'],m['distance_A_after_m'],m['distance_A_reduction_m']])
    draw_map(poses,moves)
    print(json.dumps({k:v for k,v in summary.items() if k not in ['moves','A_visibility_at_nominal_grounded_views','source_hashes_before','no_new_candidate_ages']},ensure_ascii=False,indent=2))
    for m in moves:print(m['decision'],*[round(v,3) for v in [*m['before_xy'],*m['after_xy'],m['distance_A_reduction_m']]],round(m['yaw_before_deg'],1))


def draw_map(poses,moves):
    # Engineering plan diagram; coordinates are POSTHOC world metres.
    svg=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width='1600',height='760',viewBox='0 0 1600 760')
    defs=ET.SubElement(svg,'defs')
    marker=ET.SubElement(defs,'marker',id='arrow',viewBox='0 0 10 10',refX='8',refY='5',markerWidth='5',markerHeight='5',orient='auto-start-reverse')
    ET.SubElement(marker,'path',d='M 0 0 L 10 5 L 0 10 z',fill='#c2410c')
    ET.SubElement(svg,'rect',width='1600',height='760',fill='white')
    def text(x,y,t,size=15):
        el=ET.SubElement(svg,'text',x=str(x),y=str(y),fill='#172033',style=f'font:{size}px sans-serif');el.text=t
    text(30,32,'H2 route review — recorded movement, not a navigation plan',22)
    for origin,scale,limits,title in [((45,430),95,(-2.7,7.,-2.5,3.),'Scene overview'),((1060,610),165,(-2.3,.4,-.3,2.2),'Route detail')]:
        ox,oy=origin
        def xy(p):return ox+scale*(p[0]-limits[0]),oy-scale*p[1]
        text(ox,65,title,18)
        for i in range(math.ceil(limits[0]),math.floor(limits[1])+1):
            x1,y1=xy((i,limits[2]));x2,y2=xy((i,limits[3]))
            ET.SubElement(svg,'line',x1=str(x1),y1=str(y1),x2=str(x2),y2=str(y2),stroke='#e2e8f0')
            text(x1+2,xy((0,limits[2]))[1]+18,str(i),11)
        for j in range(math.ceil(limits[2]),math.floor(limits[3])+1):
            x1,y1=xy((limits[0],j));x2,y2=xy((limits[1],j))
            ET.SubElement(svg,'line',x1=str(x1),y1=str(y1),x2=str(x2),y2=str(y2),stroke='#e2e8f0')
        if scale==95:
            x,y=xy((3.58,2.));ET.SubElement(svg,'rect',x=str(x),y=str(y),width=str(.44*scale),height=str(4*scale),fill='#64748b')
            text(x+30,y+20,'Cabinet (occluder)',12)
            x,y=xy((6.4,0));ET.SubElement(svg,'circle',cx=str(x),cy=str(y),r='9',fill='#2563eb');text(x-25,y-18,'A (6.4, 0)',13)
            x,y=xy((1.8,.6));ET.SubElement(svg,'rect',x=str(x-7),y=str(y-7),width='14',height='14',fill='#16a34a');text(x-25,y-18,'B',13)
        points=' '.join(f'{xy(p["xy"])[0]:.2f},{xy(p["xy"])[1]:.2f}' for p in poses.values())
        ET.SubElement(svg,'polyline',points=points,fill='none',stroke='#ea580c',attrib={'stroke-width':'2'})
        for m in moves:
            bx,by=xy(m['before_xy']);ax,ay=xy(m['after_xy'])
            ET.SubElement(svg,'line',x1=str(bx),y1=str(by),x2=str(ax),y2=str(ay),stroke='#c2410c',attrib={'stroke-width':'2','marker-end':'url(#arrow)'})
            x,y=xy(m['after_xy']);ET.SubElement(svg,'circle',cx=str(x),cy=str(y),r='3',fill='#c2410c')
            if scale!=95 or m['decision'] in [9,41,85,116]:text(x+4,y-5,str(m['decision']),10)
        x,y=xy(poses[0]['xy']);ET.SubElement(svg,'circle',cx=str(x),cy=str(y),r='5',fill='#111827');text(x+8,y+15,'start',12)
    text(35,725,'Orange: recorded decision-to-decision route. Labels: move_relative decision numbers. Scenario GT is for diagnosis only.',13)
    ET.ElementTree(svg).write(OUT/'route.svg',encoding='unicode',xml_declaration=True)


if __name__=='__main__':main()

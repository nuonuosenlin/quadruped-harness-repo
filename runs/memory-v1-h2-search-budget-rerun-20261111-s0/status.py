from pathlib import Path
import json,sys
from collections import Counter
sys.path.insert(0,'/home/nuonuosenlin/Agent-harness')
from go2_demo.memory import read_state
out=Path(__file__).resolve().parent
ep=next((out/'H2').iterdir())
rows=[]
for s in (ep/'events.jsonl').read_text().splitlines():
 try: rows.append(json.loads(s))
 except ValueError: pass
inputs=[r for r in rows if r['event']=='model_input']
responses=[r for r in rows if r['event']=='model_response']
results=[r for r in rows if r['event']=='tool_results']
md=read_state((ep/'memory.md').read_text())
reviews=[r for r in md['ledger'] if r['kind']=='search_review_due']
print(json.dumps({'completed_decisions':len(results),'latest_request':inputs[-1]['turn']+1 if inputs else None,'tools':dict(Counter(x['tool'] for r in results for x in r['results'])),'failures':[{'decision':r['turn']+1,'result':x} for r in results for x in r['results'] if x['status']=='failed'],'first_move':next((r['turn']+1 for r in responses if any(c['name']=='move_relative' for c in r['calls'])),None),'review_steps':[r['step'] for r in reviews],'latest_exploration':inputs[-1]['observation']['memory_state']['world'].get('exploration') if inputs else None,'task_objects':[{k:o.get(k) for k in ('object_id','state','last_seen','evidence_ids')} for o in md['objects'] if o['object_id'].startswith('task:')],'last_plan':responses[-1].get('planning_envelope') if responses else None,'last_xy':results[-1]['next_observation'].get('local_odometry') if results else None,'protocol_error_count':len((out/'protocol_errors/captures.jsonl').read_text().splitlines()) if (out/'protocol_errors/captures.jsonl').exists() else 0,'ended':(ep/'metrics.json').exists()},ensure_ascii=False,indent=2))

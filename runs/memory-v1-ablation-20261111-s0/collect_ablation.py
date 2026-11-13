"""Read sanitized local run artifacts only; never open credentials or call APIs."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path('/home/nuonuosenlin/Agent-harness')
sys.path.insert(0, str(ROOT))
from go2_demo.memory import read_state

OUT = ROOT / 'runs/memory-v1-ablation-20261111-s0'
config = json.loads((OUT / 'ablation_config.json').read_text())
assert config['code_sha256'] == {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in sorted((ROOT / 'go2_demo').glob('*.py'))}


def arm(name):
    files = list((OUT / name).glob('*/metrics.json'))
    if not files:
        return {'status': 'not_run_or_not_finished'}
    assert len(files) == 1, 'Expected at most one episode per arm'
    path = files[0]
    metrics = json.loads(path.read_text())
    manifest = json.loads((path.parent / 'manifest.json').read_text())
    assert manifest['seed'] == 0 and manifest['model'] == config['model']
    assert manifest['task_id'] == config['task']
    assert manifest['budgets'] == {k: config['budgets'][k] for k in
                                  ('max_model_calls', 'max_wall_seconds', 'max_sim_seconds', 'history_turns')}
    events = [json.loads(line) for line in (path.parent / 'events.jsonl').read_text().splitlines()]
    inputs = [e for e in events if e['event'] == 'model_input']
    calls = [c for e in events if e['event'] == 'model_response' for c in e['calls']]
    failures = [r for e in events if e['event'] == 'tool_results' for r in e['results'] if r['status'] != 'succeeded']
    result = {'status': 'completed', 'metrics_path': str(path),
              **{k: metrics.get(k) for k in ('success', 'termination', 'model_calls', 'motion_calls', 'usage',
                  'reasoning_responses', 'reasoning_characters', 'checkpoints', 'order_satisfied', 'error')},
              'independent_evaluation': metrics.get('evaluation'),
              'tool_counts': dict(Counter(c['name'] for c in calls)),
              'failed_tool_counts': dict(Counter(r.get('error_code', r['status']) for r in failures)),
              'model_input_count': len(inputs)}
    memory = path.parent / 'memory.md'
    if memory.exists():
        state = read_state(memory.read_text())
        result['memory'] = {'path': str(memory), 'written_revision': state['world']['revision'],
                            'ledger_entries': len(state['ledger']), 'object_count': len(state['objects']),
                            'object_categories': dict(Counter(o['category'] for o in state['objects'])),
                            'state_packet_inputs': sum('memory_state' in e['observation'] for e in inputs),
                            'inputs_with_objects': sum(bool(e['observation'].get('memory_state', {}).get('objects')) for e in inputs),
                            'max_snapshot_lag_steps': max((e['observation'].get('memory_state', {}).get('world', {}).get('snapshot_lag_steps', 0)
                                                           for e in inputs), default=0),
                            'event_counts': dict(Counter(e['kind'] for e in state['events']))}
    return result


summary = {'config': config, 'H0': arm('H0'), 'H2': arm('H2')}
if summary['H0'].get('success'):
    assert summary['H2']['status'] == 'not_run_or_not_finished', 'H0 success requires stopping before H2'
    summary['H2']['status'] = 'not_run_H0_passed_stop_condition'
    summary['conclusion'] = 'H0 passed; task did not isolate external memory; H2 not run.'
elif summary['H2']['status'] == 'completed':
    summary['conclusion'] = 'Both authorized arms finished; inspect independent checkpoint scores and memory diagnostics.'
else:
    summary['conclusion'] = 'H0 completed without success; H2 not completed yet.'
tmp = OUT / 'ablation_summary.json.tmp'
tmp.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
tmp.replace(OUT / 'ablation_summary.json')
print(json.dumps(summary, ensure_ascii=False, indent=2))

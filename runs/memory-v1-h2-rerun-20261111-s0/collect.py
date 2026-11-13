"""Offline evidence collection for the single authorized repaired H2 episode."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path('/home/nuonuosenlin/Agent-harness')
OUT = ROOT / 'runs/memory-v1-h2-rerun-20261111-s0'
sys.path.insert(0, str(ROOT))
from go2_demo.memory import read_state


def main():
    episodes = list((OUT / 'H2').glob('*-api-memory_ab_occluded_v1-s0-*'))
    assert len(episodes) == 1, episodes
    episode = episodes[0]
    metrics_file = episode / 'metrics.json'
    assert metrics_file.exists(), 'Episode still running; do not collect final report yet'
    metrics = json.loads(metrics_file.read_text())
    rows = [json.loads(line) for line in (episode / 'events.jsonl').read_text().splitlines()]
    inputs = [r for r in rows if r['event'] == 'model_input']
    responses = [r for r in rows if r['event'] == 'model_response']
    results = [r for r in rows if r['event'] == 'tool_results']
    memory = read_state((episode / 'memory.md').read_text())
    config = json.loads((OUT / 'config.json').read_text())
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted((ROOT / 'go2_demo').glob('*.py'))}
    assert hashes == config['code_sha256'], 'Product source changed during episode'

    def first_tool(name, succeeded_only=False):
        for row in results:
            if any(r['tool'] == name and (not succeeded_only or r['status'] == 'succeeded')
                   for r in row['results']):
                return row['turn'] + 1

    object_inputs = [{'decision': row['turn'] + 1,
                      'objects': row['observation']['memory_state']['objects']}
                     for row in inputs if row['observation']['memory_state']['objects']]
    target_inputs = {label: [row['turn'] + 1 for row in inputs if any(
        o['object_id'] == f'task:{label}' for o in row['observation']['memory_state']['objects'])]
        for label in ('A', 'B')}
    tools = Counter(r['tool'] for row in results for r in row['results'])
    failures = Counter(r.get('error_code', 'unspecified') for row in results
                       for r in row['results'] if r['status'] == 'failed')
    failed_motion = [{'decision': row['turn'] + 1, 'tool': r['tool'],
                      'error_code': r.get('error_code'),
                      'constraint_feedback': r.get('constraint_feedback')}
                     for row in results for r in row['results']
                     if r['tool'] in {'turn', 'move_relative'} and r['status'] == 'failed']
    target_objects = [o for o in memory['objects'] if o['object_id'].startswith('task:')]
    target_ledger = [r for r in memory['ledger'] if r.get('object_id', '').startswith('task:')
                     or r.get('observation', {}).get('object_id', '').startswith('task:')]
    checkpoints = metrics.get('checkpoints', {})
    a_passed = checkpoints.get('A', {}).get('passed', False)
    capture_path = OUT / 'protocol_error/capture.json'
    capture = json.loads(capture_path.read_text()) if capture_path.exists() else None
    response_structure = None
    if capture and capture.get('response_body_available'):
        raw = Path(capture['response_body_file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == capture['stored_sha256']
        try:
            wire = json.loads(raw)
        except (ValueError, UnicodeError):
            response_structure = {'valid_json': False}
        else:
            choices = wire.get('choices') if isinstance(wire, dict) else None
            response_structure = {'valid_json': True, 'response_type': type(wire).__name__,
                'choices_type': type(choices).__name__, 'choices_count': len(choices) if isinstance(choices, list) else None,
                'usage': wire.get('usage') if isinstance(wire, dict) else None, 'choices': []}
            for choice in choices or []:
                if not isinstance(choice, dict):
                    continue
                msg = choice.get('message') or {}
                response_structure['choices'].append({'finish_reason': choice.get('finish_reason'),
                    'message_keys': list(msg) if isinstance(msg, dict) else None,
                    'content_type': type(msg.get('content')).__name__,
                    'content_chars': len(msg.get('content') or ''),
                    'reasoning_chars': len(msg.get('reasoning_content') or ''),
                    'tool_calls': msg.get('tool_calls')})
    h0_path = ROOT / config['H0_reference']
    h0 = json.loads(h0_path.read_text())
    manifest = json.loads((episode / 'manifest.json').read_text())
    h0_manifest = json.loads((h0_path.parent / 'manifest.json').read_text())
    comparable_fields = ['task', 'task_id', 'seed', 'model', 'budgets', 'package_versions',
                         'evaluation', 'asset_lock_sha256']
    comparison = {k: manifest[k] == h0_manifest[k] for k in comparable_fields}
    comparison['api_settings'] = all(manifest['api_settings'][k] == h0_manifest['api_settings'][k]
                                    for k in ['timeout_s', 'max_output_tokens', 'thinking'])
    assert all(comparison.values()), comparison
    evidence = {'episode': str(episode), 'metrics_file': str(metrics_file),
        'memory_file': str(episode / 'memory.md'), 'config': config,
        'H0_condition_comparison': comparison,
        'product_source_unchanged_during_run': True, 'real_episodes_this_request': 1,
        'metrics': metrics, 'parsed_model_responses': len(responses),
        'first_nonempty_object_input': object_inputs[0] if object_inputs else None,
        'task_target_read_decisions': target_inputs,
        'first_track_point_decision': first_tool('track_point'),
        'first_turn_attempt_decision': first_tool('turn'),
        'first_successful_turn_decision': first_tool('turn', True),
        'first_move_relative_attempt_decision': first_tool('move_relative'),
        'first_successful_move_relative_decision': first_tool('move_relative', True),
        'finish_tool_decisions': [r['turn']+1 for r in results if any(x['tool']=='finish' for x in r['results'])],
        'tool_counts': dict(tools), 'failure_counts': dict(failures), 'failed_motion': failed_motion,
        'plans_in_md': memory['plans'], 'target_objects_in_md': target_objects,
        'target_evidence_ledger': target_ledger,
        'ledger_size': len(memory['ledger']), 'final_pose_in_memory': memory['pose'],
        'B_return_stage_reached': bool(a_passed),
        'protocol_capture': capture, 'protocol_response_structure': response_structure,
        'H0_reference_metrics': {'path': str(h0_path), 'sha256': hashlib.sha256(h0_path.read_bytes()).hexdigest(),
                                 'metrics': h0}}
    (OUT / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: evidence[k] for k in ['episode', 'parsed_model_responses',
        'task_target_read_decisions', 'first_track_point_decision', 'first_turn_attempt_decision',
        'first_successful_turn_decision', 'first_move_relative_attempt_decision',
        'first_successful_move_relative_decision', 'tool_counts', 'failure_counts',
        'B_return_stage_reached']}, ensure_ascii=False))
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    if response_structure:
        print('protocol_response_structure', json.dumps(response_structure, ensure_ascii=False))


if __name__ == '__main__':
    main()

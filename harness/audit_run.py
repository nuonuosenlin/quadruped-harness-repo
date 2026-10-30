"""Audit a v2 saved episode. No API calls or simulator initialization."""
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from protocol import Progress


def audit(path):
    root = Path(r'D:\RoboHarnessSim\harness\runs').resolve()
    run = Path(path).resolve()
    if root not in run.parents:
        raise ValueError('Run must be inside harness/runs')
    r = json.loads((run/'result.json').read_text(encoding='utf-8'))
    steps = r['steps']
    assert r['revision'] == 'persistent_phase_v2'
    assert r['max_llm_steps'] == 12 and len(steps) <= 12
    assert r['budget']['max_total_tokens'] == 15000
    assert r['api_calls'] == len(steps)
    assert sum(s['response']['usage']['total_tokens'] for s in steps) == r['tokens']['total'] <= 15000
    assert sum(s['response']['usage']['prompt_tokens'] for s in steps) == r['tokens']['prompt']
    assert sum(s['response']['usage']['completion_tokens'] for s in steps) == r['tokens']['completion']
    progress = Progress()
    previous = None
    for s in steps:
        request = s['request']
        assert request['model'] == r['model'] == s['response']['model']
        assert request['tools'] == progress.tools()
        assert request['max_tokens'] == 384 and not request['enable_thinking']
        assert progress.summary() == s['workflow_before']
        for m in request['messages']:
            assert m.get('content') is None or isinstance(m['content'], str)
            assert set(m) <= {'role','content','tool_calls','tool_call_id'}
        payload = json.dumps(request).lower()
        assert not any(k in payload for k in ('image_url','input_image','base64','data:image','input_audio','authorization'))
        if previous:
            assert [m['role'] for m in request['messages']] == ['system','assistant','tool','user']
            assert request['messages'][1]['tool_calls'] == previous['response']['choices'][0]['message']['tool_calls']
            assert request['messages'][2]['tool_call_id'] == previous['tool_call']['id']
            assert json.loads(request['messages'][2]['content']) == previous['tool_result']
        else:
            assert [m['role'] for m in request['messages']] == ['system','user']
        call = s['tool_call']
        progress.validate(call['name'],call['arguments'])
        assert 'error' not in s['tool_result']
        assert progress.record(call['name'],call['arguments'],s['tool_result']) is None
        assert progress.summary() == s['workflow_after']
        check = s['check']
        distance = np.linalg.norm(np.array(check['keypoints']['eef'])-np.array(check['keypoints']['alphabet_soup_1']))
        assert abs(distance-check['distance_m']) < 2e-6
        assert check['success'] == (check['distance_m'] <= 0.03)
        previous = s
    actions = [json.loads(line) for line in (run/'simulation.jsonl').read_text().splitlines()]
    assert len(actions) == r['simulation_control_steps']
    for i, action in enumerate(actions,1):
        a = action['action_osc_pose']
        assert action['sim_step'] == i and len(a) == 7 and np.isfinite(a).all()
        assert max(abs(x) for x in a) <= 1 and a[6] == -1
    data = np.load(run/'after_geometry.npz')
    u,v = steps[0]['tool_result']['pixel_uv']
    assert data['instance_mask'][v,u] == r['calibration']['mask_id']
    pc = data['depth_m'][v,u] * (np.linalg.inv(data['K']) @ np.array([u,v,1]))
    world = (data['T_camera_to_world'] @ np.r_[pc,1])[:3]
    final = r['final_check']
    assert np.linalg.norm(world-np.array(final['keypoints']['alphabet_soup_1'])) < 2e-6
    raw_distance = np.linalg.norm(np.array(actions[-1]['eef_world_m'])-world)
    assert abs(raw_distance-final['distance_m']) < 1e-10
    assert r['success'] and final['success'] and raw_distance <= 0.03 and not final['bddl_success']
    manifest = json.loads((run/'source_manifest.json').read_text())
    for entry in manifest:
        snapshot = run/'source'/Path(entry['path']).name
        assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == entry['sha256']
    summary = {'audit':'passed','llm_steps':len(steps), 'tokens':r['tokens'],
        'logged_control_steps':len(actions),'pure_text_requests':len(steps),
        'standard_tool_context_verified':True,'phase_contracts_verified':True,
        'source_snapshots_verified':True,'distance_from_saved_depth_and_actual_eef_m':float(raw_distance),
        'subtask_success':True,'bddl_success':False}
    (run/'audit.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    audit(sys.argv[1])

"""Text-only DashScope preflight. Standard library only; no simulation imports."""
import datetime
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

ROOT = Path(r'D:\RoboHarnessSim')
BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
OUT = ROOT / 'harness' / 'runs' / ('api_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    key = os.environ.get('DASHSCOPE_API_KEY', '').strip()
    report = {'status': 'running', 'base_url': BASE_URL, 'model': None,
              'console_verified': False, 'text_only': True, 'simulation_started': False,
              'requests': [], 'total_tokens': 0, 'completion_requests': 0}

    def clean(value):
        if isinstance(value, str):
            return value.replace(key, '[REDACTED]') if key else value
        if isinstance(value, list):
            return [clean(x) for x in value]
        if isinstance(value, dict):
            return {k: clean(v) for k, v in value.items()}
        return value

    def save():
        (OUT / 'result.json').write_text(json.dumps(clean(report), indent=2, ensure_ascii=False), encoding='utf-8')

    def request(path, payload=None):
        req = urllib.request.Request(BASE_URL + path,
            data=None if payload is None else json.dumps(payload).encode('utf-8'),
            headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'},
            method='GET' if payload is None else 'POST')
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                raw = response.read(2 * 1024 * 1024 + 1)
                if len(raw) > 2 * 1024 * 1024:
                    raise RuntimeError('Response exceeds 2 MiB; stopped.')
                return json.loads(raw)
        except urllib.error.HTTPError as exc:
            # Do not print headers, credentials, or raw exception representations.
            raw = exc.read(8192).decode('utf-8', errors='replace')
            try:
                error = json.loads(raw).get('error', {})
                report['api_error'] = clean({'http_status': exc.code, 'code': error.get('code'), 'message': error.get('message')})
            except (ValueError, AttributeError):
                report['api_error'] = {'http_status': exc.code, 'message': 'Non-JSON HTTP error body omitted'}
            raise RuntimeError('API HTTP failure: ' + str(exc.code)) from None
        except urllib.error.URLError:
            raise RuntimeError('Network or TLS failure; no retry performed.') from None

    def completion(label, messages, tools=None):
        payload = {'model': report['model'], 'messages': messages,
                   'max_tokens': 256, 'stream': False, 'enable_thinking': False}
        if tools:
            payload['tools'] = tools
            payload['tool_choice'] = 'auto'
        report['completion_requests'] += 1
        save()
        response = request('/chat/completions', payload)
        item = {'label': label, 'request': payload, 'response': response}
        report['requests'].append(item)
        usage = response.get('usage', {})
        tokens = usage.get('total_tokens')
        if not isinstance(tokens, int) or tokens < 0:
            save()
            raise RuntimeError('Missing or invalid token usage; stopped for review.')
        report['total_tokens'] += tokens
        save()
        if tokens > 2000 or report['total_tokens'] > 4000:
            raise RuntimeError('Unexpected token usage; stopped for user review.')
        choices = response.get('choices', [])
        if len(choices) != 1 or choices[0].get('finish_reason') == 'length':
            raise RuntimeError('Missing choice or truncated completion.')
        message = choices[0].get('message', {})
        if message.get('role') != 'assistant':
            raise RuntimeError('Invalid assistant message.')
        return message

    try:
        if not key:
            raise RuntimeError('DASHSCOPE_API_KEY missing from process environment.')
        catalog = request('/models')
        ids = [x.get('id') for x in catalog.get('data', []) if isinstance(x, dict)]
        candidates = [x for x in ids if isinstance(x, str) and 'qwen3.8' in x.lower() and ('flash' in x.lower() or 'next' in x.lower())]
        report['matching_model_ids'] = candidates
        if 'qwen3.8-flash-next' in ids:
            report['model'] = 'qwen3.8-flash-next'
        elif 'qwen3.8-flash' in ids:
            report['model'] = 'qwen3.8-flash'
        else:
            raise RuntimeError('Requested model absent from accessible model catalog; no alternative selected.')
        report['model_selection_evidence'] = 'Authenticated /models catalog, not console UI'
        save()
        ordinary = completion('ordinary_chat', [{'role': 'user', 'content': 'Reply with exactly API_OK. This is a text-only connectivity test.'}])
        if ordinary.get('content', '').strip() != 'API_OK' or ordinary.get('tool_calls'):
            raise RuntimeError('Ordinary chat response did not match API_OK.')
        tool = {'type': 'function', 'function': {'name': 'echo_keypoint',
            'description': 'Echo one supplied 3D point for an API parsing test. Does not control any robot.',
            'parameters': {'type': 'object', 'properties': {
                'name': {'type': 'string'},
                'xyz': {'type': 'array', 'items': {'type': 'number'}, 'minItems': 3, 'maxItems': 3}},
                'required': ['name', 'xyz'], 'additionalProperties': False}}}
        message = completion('function_call', [{'role': 'user', 'content': 'Call echo_keypoint exactly once with name="probe" and xyz=[0.1,0.2,0.3]. Do not answer in prose.'}], [tool])
        calls = message.get('tool_calls', [])
        if len(calls) != 1 or calls[0].get('type') != 'function' or not calls[0].get('id'):
            raise RuntimeError('Expected exactly one valid tool call.')
        fn = calls[0].get('function', {})
        args = json.loads(fn.get('arguments', ''))
        if fn.get('name') != 'echo_keypoint' or args != {'name': 'probe', 'xyz': [0.1, 0.2, 0.3]}:
            raise RuntimeError('Tool name or parsed arguments do not match expected values.')
        report['parsed_tool_call'] = {'name': fn['name'], 'arguments': args, 'local_result': args}
        report['status'] = 'passed'
    except Exception as exc:
        report['status'] = 'failed'
        report['failure'] = clean(str(exc))
    save()
    print(json.dumps({'status': report['status'], 'model': report['model'],
        'total_tokens': report['total_tokens'], 'completion_requests': report['completion_requests'],
        'failure': report.get('failure'), 'api_error': report.get('api_error'),
        'result': str(OUT / 'result.json')}, ensure_ascii=True))
    return 0 if report['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())

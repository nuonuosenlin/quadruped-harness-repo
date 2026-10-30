"""Bounded, text-only OpenAI-compatible Chat Completions HTTP transport."""
import json
import os
import urllib.request
import urllib.error

BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'


class TextClient:
    MAX_TOTAL_TOKENS = 15000
    MAX_CALLS = 12
    def __init__(self, model):
        self.model = model
        self.key = os.environ.get('DASHSCOPE_API_KEY', '').strip()
        if not self.key:
            raise RuntimeError('Missing DASHSCOPE_API_KEY')
        self.total = 0
        self.prompt = 0
        self.completion = 0
        self.calls = 0

    def redact(self, obj):
        if isinstance(obj, str):
            return obj.replace(self.key, '[REDACTED]')
        if isinstance(obj, dict):
            return {k: self.redact(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self.redact(v) for v in obj]
        return obj

    def payload(self, messages, tools):
        if self.calls >= self.MAX_CALLS:
            raise RuntimeError('STEP_REVIEW: 12 API calls already used')
        # This is the sole network payload builder. Reject multimodal content.
        for m in messages:
            if m.get('role') not in ('system', 'user', 'assistant', 'tool'):
                raise ValueError('Invalid role')
            if m.get('content') is not None and not isinstance(m['content'], str):
                raise ValueError('Only text content is allowed')
            if any(k not in ('role', 'content', 'tool_calls', 'tool_call_id') for k in m):
                raise ValueError('Unsupported message field')
        payload = {'model': self.model, 'messages': messages, 'tools': tools,
                   'tool_choice': 'auto', 'max_tokens': 384, 'enable_thinking': False,
                   'stream': False}
        # Conservative pre-request ceiling. No automatic retries.
        estimate = len(json.dumps(payload, ensure_ascii=False).encode('utf-8')) + 384
        if estimate > 6000 or self.total + estimate > self.MAX_TOTAL_TOKENS:
            raise RuntimeError('TOKEN_REVIEW: estimated request or episode ceiling reached')
        return payload

    def complete(self, payload):
        self.calls += 1
        request = urllib.request.Request(BASE_URL + '/chat/completions',
            data=json.dumps(payload).encode('utf-8'),
            headers={'Authorization': 'Bearer ' + self.key, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read(1024 * 1024 + 1)
            if len(raw) > 1024 * 1024:
                raise RuntimeError('Response too large')
            response = json.loads(raw)
        except urllib.error.HTTPError as exc:
            raise RuntimeError('API HTTP %s; stopped without retry' % exc.code) from None
        except urllib.error.URLError:
            raise RuntimeError('API network/TLS failure; stopped without retry') from None
        usage = response.get('usage', {})
        for k in ('prompt_tokens', 'completion_tokens', 'total_tokens'):
            if type(usage.get(k)) is not int or usage[k] < 0:
                return response, 'TOKEN_REVIEW: missing/invalid usage'
        self.total += usage['total_tokens']
        self.prompt += usage['prompt_tokens']
        self.completion += usage['completion_tokens']
        if usage['total_tokens'] > 6000 or self.total > self.MAX_TOTAL_TOKENS:
            return response, 'TOKEN_REVIEW: actual usage ceiling reached'
        return response, None


"""In-memory-only validation of the run-specific error evidence hook."""
import json
from pathlib import Path
import sys

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).parent))
from launch import CaptureAndStopModel
from go2_demo.harness import TOOLS
from go2_demo.models import ModelProtocolError


def test_full_error_body_saved_and_no_automatic_retry(tmp_path):
    body = {'model': 'offline', 'choices': [{'message': {'content': 'synthetic content',
            'reasoning_content': 'synthetic reasoning ' * 500, 'tool_calls': []}, 'finish_reason': 'stop'}],
            'usage': {'prompt_tokens': 10, 'completion_tokens': 20, 'total_tokens': 30}, 'extra': {'not_truncated': True}}
    raw = json.dumps(body).encode()
    seen = []
    model = CaptureAndStopModel('https://example.invalid/v1', 'offline', '', capture_dir=tmp_path,
        transport=httpx.MockTransport(lambda r: seen.append(r) or httpx.Response(200, content=raw)))
    with pytest.raises(ModelProtocolError):
        model.decide({'memory_state': {}}, '', TOOLS, [], max_requests=2)
    assert len(seen) == 1 and (tmp_path / 'response.raw').read_bytes() == raw
    assert not json.loads((tmp_path / 'capture.json').read_text())['credential_redactions_applied']


def test_credentials_never_saved_even_if_echoed_by_response(tmp_path):
    secret = 'SYNTHETIC-CAPTURE-KEY'
    raw = json.dumps({'choices': [{'message': {'content': secret, 'tool_calls': []}}]}).encode()
    model = CaptureAndStopModel('https://example.invalid/v1', 'offline', secret, capture_dir=tmp_path,
        transport=httpx.MockTransport(lambda r: httpx.Response(200, content=raw)))
    with pytest.raises(ModelProtocolError):
        model.decide({'memory_state': {}}, '', TOOLS, [])
    assert secret.encode() not in (tmp_path / 'response.raw').read_bytes()
    assert secret not in (tmp_path / 'capture.json').read_text()
    assert json.loads((tmp_path / 'capture.json').read_text())['credential_redactions_applied']


def test_malformed_json_bytes_are_preserved_without_decode_or_truncation(tmp_path):
    raw = b'{malformed:' + bytes([255, 254, 0])
    model = CaptureAndStopModel('https://example.invalid/v1', 'offline', '', capture_dir=tmp_path,
        transport=httpx.MockTransport(lambda r: httpx.Response(200, content=raw)))
    with pytest.raises(ModelProtocolError):
        model.decide({'memory_state': {}}, '', TOOLS, [])
    assert (tmp_path / 'response.raw').read_bytes() == raw

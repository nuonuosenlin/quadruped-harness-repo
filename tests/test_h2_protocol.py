"""In-memory transport/stub tests only; no network or credential files."""
from copy import deepcopy
import json
from types import SimpleNamespace

import httpx
import pytest

from go2_demo.harness import TOOLS
from go2_demo.models import APIModel, ModelError, ModelProtocolError
from go2_demo.runner import run_episode
from go2_demo.types import Decision, ToolCall
from test_runner import EpisodeBackend


OBS = {'task': 'A then B', 'memory_state': {'world': {}, 'objects': []}}


def response():
    return {'model': 'offline-test', 'choices': [{'finish_reason': 'tool_calls', 'message': {
        'content': None, 'reasoning_content': 'SYNTHETIC-PRIVATE-REASONING',
        'tool_calls': [{'id': 'c1', 'type': 'function', 'function': {'name': 'observe', 'arguments': '{}'}}]}}],
        'usage': {'prompt_tokens': 10, 'completion_tokens': 2, 'total_tokens': 12}}


def broken(case):
    body = response(); msg = body['choices'][0]['message']
    if case == 'missing': msg.pop('tool_calls')
    elif case == 'none': msg['tool_calls'] = None
    elif case == 'non_list': msg['tool_calls'] = 'not a list'
    elif case == 'empty': msg['tool_calls'] = []
    elif case in ('too_many', 'multiple'):
        msg['tool_calls'] = [deepcopy(msg['tool_calls'][0]) for _ in range(17 if case == 'too_many' else 2)]
    elif case == 'bad_args_json': msg['tool_calls'][0]['function']['arguments'] = '{bad-json'
    elif case == 'unknown_tool': msg['tool_calls'][0]['function']['name'] = 'fly'
    elif case == 'missing_parameter': msg['tool_calls'][0]['function'] = {'name': 'move_relative', 'arguments': '{"forward_m":0.2}'}
    return body


@pytest.mark.parametrize('case,kind', [
    ('missing', 'MISSING_TOOL_CALLS'), ('none', 'NON_LIST_TOOL_CALLS'),
    ('non_list', 'NON_LIST_TOOL_CALLS'), ('empty', 'EMPTY_TOOL_CALLS'),
    ('too_many', 'TOO_MANY_TOOL_CALLS'), ('multiple', 'MULTIPLE_TOOL_CALLS'),
    ('bad_args_json', 'INVALID_ARGUMENT_JSON'), ('unknown_tool', 'UNKNOWN_TOOL'),
    ('missing_parameter', 'PARAMETERS_MISMATCH'),
])
def test_h2_repairs_one_bad_response_without_executing_or_echoing_it(case, kind):
    seen = []

    def handler(request):
        seen.append(json.loads(request.content))
        return httpx.Response(200, json=broken(case) if len(seen) == 1 else response())

    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(handler))
    decision = client.decide(OBS, '', TOOLS, [])
    assert len(seen) == decision.request_attempts == 2
    assert decision.calls[0].name == 'observe'
    assert decision.protocol_diagnostics[0]['kind'] == kind
    assert decision.usage == {'prompt_tokens': 20, 'completion_tokens': 4, 'total_tokens': 24}
    assert decision.reasoning_response_count == 2
    for payload in seen:
        assert payload['tool_choice'] == 'required' and payload['parallel_tool_calls'] is False
    assert kind in seen[1]['messages'][-1]['content']
    assert 'SYNTHETIC-PRIVATE-REASONING' not in json.dumps(decision.protocol_diagnostics)
    assert 'SYNTHETIC-PRIVATE-REASONING' not in json.dumps(seen[1]['messages'])


def test_invalid_outer_json_has_specific_diagnostic_and_one_repair():
    count = [0]

    def handler(request):
        count[0] += 1
        return httpx.Response(200, content=b'{bad') if count[0] == 1 else httpx.Response(200, json=response())

    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(handler))
    result = client.decide(OBS, '', TOOLS, [])
    assert count[0] == 2 and result.protocol_diagnostics[0]['kind'] == 'INVALID_RESPONSE_JSON'
    assert result.usage['total_tokens'] == 12  # malformed bytes contain no recoverable counters


def test_two_bad_responses_stop_and_preserve_known_usage_but_no_private_body():
    seen = []
    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(200, json=broken('empty'))))
    with pytest.raises(ModelProtocolError) as caught:
        client.decide(OBS, '', TOOLS, [])
    error = caught.value
    assert len(seen) == error.request_attempts == 2
    assert error.usage['total_tokens'] == 24 and error.reasoning_response_count == 2
    assert [x['kind'] for x in error.protocol_diagnostics] == ['EMPTY_TOOL_CALLS', 'EMPTY_TOOL_CALLS']
    assert 'SYNTHETIC-PRIVATE-REASONING' not in str(error)


def test_one_remaining_request_slot_never_retries():
    seen = []
    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(200, json=broken('empty'))))
    with pytest.raises(ModelProtocolError) as caught:
        client.decide(OBS, '', TOOLS, [], max_requests=1)
    assert len(seen) == caught.value.request_attempts == 1


def test_h0_stays_single_request_auto_choice_without_forced_parallel_flag():
    seen = []
    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(
        lambda req: seen.append(json.loads(req.content)) or httpx.Response(200, json=broken('empty'))))
    with pytest.raises(ModelProtocolError):
        client.decide({'task': 'H0'}, 'data:image/png;base64,aW1hZ2U=', TOOLS, [])
    assert len(seen) == 1 and seen[0]['tool_choice'] == 'auto'
    assert 'parallel_tool_calls' not in seen[0]


def test_transport_failure_is_not_a_protocol_retry():
    seen = []
    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(
        lambda req: seen.append(req) or httpx.Response(503)))
    with pytest.raises(ModelError) as caught:
        client.decide(OBS, '', TOOLS, [])
    assert len(seen) == caught.value.request_attempts == 1


def test_retry_uses_remaining_total_timeout(monkeypatch):
    import go2_demo.models as models
    clock = [0.]
    monkeypatch.setattr(models, 'time', SimpleNamespace(monotonic=lambda: clock[0]))
    client = APIModel('https://example.invalid/v1', 'offline-test', '')
    timeouts = []

    def once(*args, **kwargs):
        timeouts.append(kwargs['timeout_s'])
        client._last_protocol_metadata = {'kind': 'EMPTY_TOOL_CALLS', 'usage': {}}
        if len(timeouts) == 1:
            clock[0] = .6
            raise ModelProtocolError('invalid synthetic response')
        return Decision([ToolCall('ok', 'observe', {})])

    monkeypatch.setattr(client, '_decide_once', once)
    assert client.decide(OBS, '', TOOLS, [], timeout_s=1.).request_attempts == 2
    assert timeouts == pytest.approx([1., .4])


@pytest.mark.parametrize('budget,expected_requests,termination', [(1, 1, 'model_error'), (2, 2, 'budget_exhausted')])
def test_runner_counts_repair_requests_and_usage_inside_model_call_budget(tmp_path, budget, expected_requests, termination):
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=broken('empty') if len(seen) == 1 else response())

    client = APIModel('https://example.invalid/v1', 'offline-test', '', transport=httpx.MockTransport(handler))
    result = run_episode(EpisodeBackend(score_success=False), client, mode='api', run_dir=tmp_path,
                         memory_v1=True, max_model_calls=budget)
    assert result['termination'] == termination
    assert len(seen) == result['model_calls'] == expected_requests
    assert result['decision_calls'] == 1 and result['protocol_retries'] == expected_requests - 1
    assert result['usage']['total_tokens'] == expected_requests * 12
    assert result['reasoning_responses'] == expected_requests
    if budget == 1:
        assert result['error']['protocol_diagnostics'][0]['kind'] == 'EMPTY_TOOL_CALLS'

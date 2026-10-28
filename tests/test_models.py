"""Model protocol tests use only local HTTP mocks; never a paid endpoint."""

import asyncio
import json
import os
import time

import httpx
import pytest

from go2_demo.models import APIModel, MAX_RESPONSE_BYTES, ModelError, ModelProtocolError, redact_message


IMAGE = "data:image/png;base64,aW1hZ2U="
OBS = {"task": "Approach the red marker", "observation_id": "obs-1"}
TOOLS = [{"type": "function", "function": {"name": "observe", "parameters": {"type": "object", "properties": {}}}}]


def response(calls=None, **overrides):
    message = {"role": "assistant", "content": None, "reasoning_content": "synthetic reasoning state", "tool_calls": calls if calls is not None else [
        {"id": "call-1", "type": "function", "function": {"name": "observe", "arguments": "{}"}}
    ]}
    value = {"model": "vision-test", "choices": [{"message": message, "finish_reason": "tool_calls"}],
             "usage": {"prompt_tokens": 17, "completion_tokens": 4, "total_tokens": 21}}
    value.update(overrides)
    return value


def model(handler, **kwargs):
    return APIModel("https://example.invalid/v1", "vision-test", "SECRET-KEY", transport=httpx.MockTransport(handler), **kwargs)


def history_turn(index):
    return {"observation": {"observation_id": f"obs-{index}"},
            "calls": [{"call_id": f"call-{index}", "name": "observe", "arguments": {}}],
            "results": [{"call_id": f"call-{index}", "status": "succeeded"}]}


def test_wire_format_and_whole_turn_history_window():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=response())

    client = model(handler, history_turns=1)
    decision = client.decide(OBS, IMAGE, TOOLS, [history_turn(0), history_turn(1)])
    assert len(seen) == 1
    request = seen[0]
    assert str(request.url) == "https://example.invalid/v1/chat/completions"
    assert request.headers["authorization"] == "Bearer SECRET-KEY"
    payload = json.loads(request.content)
    messages = payload["messages"]
    assert [message["role"] for message in messages] == ["system", "user", "assistant", "tool", "user"]
    assert "obs-0" not in json.dumps(messages)
    assert messages[2]["tool_calls"][0]["id"] == messages[3]["tool_call_id"] == "call-1"
    assert messages[-1]["content"][1]["image_url"]["url"] == IMAGE
    assert sum("image_url" in json.dumps(message) for message in messages) == 1
    assert decision.calls[0].name == "observe"
    assert decision.usage["total_tokens"] == 21


def test_multiple_calls_are_preserved_and_history_results_all_paired():
    calls = [{"id": f"call-{i}", "type": "function", "function": {"name": "observe", "arguments": "{}"}} for i in range(2)]
    client = model(lambda request: httpx.Response(200, json=response(calls)))
    decision = client.decide(OBS, IMAGE, TOOLS, [])
    assert [item.call_id for item in decision.calls] == ["call-0", "call-1"]
    turn = {"observation": OBS, "calls": [history_turn(i)["calls"][0] for i in range(2)],
            "results": [{"call_id": f"call-{i}", "status": "rejected"} for i in range(2)]}
    messages = client.build_messages(OBS, IMAGE, [turn])
    assert [item["tool_call_id"] for item in messages if item["role"] == "tool"] == ["call-0", "call-1"]


@pytest.mark.parametrize("arguments", ['{"x":NaN}', '{"x":Infinity}', '{"x":1e999}', '{"x":1,"x":2}', '[]', '{bad}', '"move"'])
def test_invalid_arguments_rejected_before_any_execution(arguments):
    calls = [{"id": "bad", "type": "function", "function": {"name": "move_relative", "arguments": arguments}}]
    client = model(lambda request: httpx.Response(200, json=response(calls)))
    with pytest.raises(ModelProtocolError):
        client.decide(OBS, IMAGE, TOOLS, [])


@pytest.mark.parametrize("body", [response([]), {"choices": []}, {"choices": [{"message": {"content": "done"}}]}])
def test_missing_calls_are_not_silently_treated_as_finish(body):
    client = model(lambda request: httpx.Response(200, json=body))
    with pytest.raises(ModelProtocolError):
        client.decide(OBS, IMAGE, TOOLS, [])


def test_timeout_is_total_deadline_and_request_is_not_retried():
    requested = []

    async def handler(request):
        requested.append(request)
        await asyncio.sleep(0.2)
        return httpx.Response(200, json=response())

    client = model(handler)
    start = time.monotonic()
    with pytest.raises(ModelError) as error:
        client.decide(OBS, IMAGE, TOOLS, [], timeout_s=0.03)
    assert error.value.code == "MODEL_TIMEOUT"
    assert time.monotonic() - start < 0.18
    assert len(requested) == 1


def test_http_errors_never_echo_secrets_body_or_url():
    client = model(lambda request: httpx.Response(401, text="invalid key SECRET-KEY confidential diagnostic"))
    with pytest.raises(ModelError) as error:
        client.decide(OBS, IMAGE, TOOLS, [])
    assert "HTTP 401" in str(error.value)
    assert "SECRET-KEY" not in str(error.value)
    assert "confidential" not in str(error.value)


def test_transport_errors_are_sanitized():
    def handler(request):
        raise httpx.ConnectError("SECRET-KEY endpoint details", request=request)

    with pytest.raises(ModelError) as error:
        model(handler).decide(OBS, IMAGE, TOOLS, [])
    assert error.value.code == "MODEL_TRANSPORT_ERROR"
    assert "SECRET-KEY" not in str(error.value)


def test_response_size_is_bounded():
    client = model(lambda request: httpx.Response(200, content=b"x" * (MAX_RESPONSE_BYTES + 1)))
    with pytest.raises(ModelProtocolError):
        client.decide(OBS, IMAGE, TOOLS, [])


def test_history_wrong_result_pair_is_rejected():
    turn = history_turn(0)
    turn["results"][0]["call_id"] = "other-call"
    client = model(lambda request: pytest.fail("Malformed history must not reach HTTP"))
    with pytest.raises(ModelProtocolError):
        client.decide(OBS, IMAGE, TOOLS, [turn])


def test_zero_history_turns_omits_all_old_turns():
    client = model(lambda request: httpx.Response(200, json=response()), history_turns=0)
    assert len(client.build_messages(OBS, IMAGE, [history_turn(0)])) == 2


def test_redirect_is_not_followed_with_credentials():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(307, headers={"location": "https://another.invalid/chat/completions"})

    with pytest.raises(ModelError):
        model(handler).decide(OBS, IMAGE, TOOLS, [])
    assert len(seen) == 1


def test_full_endpoint_and_local_server_without_auth():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=response())

    client = APIModel("http://localhost:8000/v1/chat/completions", "local-vlm", "", transport=httpx.MockTransport(handler))
    client.decide(OBS, IMAGE, TOOLS, [])
    assert str(seen[0].url) == "http://localhost:8000/v1/chat/completions"
    assert "authorization" not in seen[0].headers


def test_environment_missing_credentials_fails_without_network(monkeypatch):
    for name in ("MODEL_BASE_URL", "MODEL_NAME", "MODEL_API_KEY"):
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(ModelError) as error:
        APIModel.from_env()
    assert error.value.code == "MODEL_CONFIG_ERROR"


def test_redacts_secret_echoed_in_valid_model_response():
    body = response()
    body["choices"][0]["message"]["content"] = "SECRET-KEY"
    decision = model(lambda request: httpx.Response(200, json=body)).decide(OBS, IMAGE, TOOLS, [])
    assert decision.raw_text == "[REDACTED]"


@pytest.fixture
def clean_api_environment(monkeypatch, tmp_path):
    for name in ("MODEL_BASE_URL", "MODEL_NAME", "MODEL_API_KEY", "MODEL_API_KEY_FILE"):
        monkeypatch.delenv(name, raising=False)
    fallback = tmp_path / "deepseekapi.txt"
    monkeypatch.setattr("go2_demo.models.DEFAULT_DEEPSEEK_KEY_FILE", fallback)
    return fallback


def test_compatible_profile_can_read_a_bom_key_file_without_exporting_secret(clean_api_environment, monkeypatch):
    key_file = clean_api_environment
    key_file.write_text("\ufeffFILE-PRIVATE-CREDENTIAL\n", encoding="utf-8")
    monkeypatch.setenv("MODEL_BASE_URL", "https://example.invalid/v1")
    monkeypatch.setenv("MODEL_NAME", "vision-test")
    monkeypatch.setenv("MODEL_API_KEY_FILE", str(key_file))
    seen = []
    client = APIModel.from_env(transport=httpx.MockTransport(lambda request: seen.append(request) or httpx.Response(200, json=response())))
    client.decide(OBS, IMAGE, TOOLS, [])
    assert seen[0].headers["authorization"] == "Bearer FILE-PRIVATE-CREDENTIAL"
    assert "MODEL_API_KEY" not in os.environ


def test_explicit_key_file_overrides_both_environment_credential_sources(clean_api_environment, monkeypatch):
    clean_api_environment.write_text("EXPLICIT-FILE-CREDENTIAL")
    monkeypatch.setenv("MODEL_BASE_URL", "https://example.invalid/v1")
    monkeypatch.setenv("MODEL_NAME", "vision-test")
    monkeypatch.setenv("MODEL_API_KEY", "ENVIRONMENT-CREDENTIAL")
    monkeypatch.setenv("MODEL_API_KEY_FILE", str(clean_api_environment.parent / "missing.txt"))
    client = APIModel.from_env(api_key_file=clean_api_environment)
    assert client._api_key == "EXPLICIT-FILE-CREDENTIAL"


def test_environment_key_precedes_implicit_key_file(clean_api_environment, monkeypatch):
    monkeypatch.setenv("MODEL_BASE_URL", "https://example.invalid/v1")
    monkeypatch.setenv("MODEL_NAME", "vision-test")
    monkeypatch.setenv("MODEL_API_KEY", "DIRECT-ENVIRONMENT-CREDENTIAL")
    monkeypatch.setenv("MODEL_API_KEY_FILE", str(clean_api_environment.parent / "missing.txt"))
    assert APIModel.from_env()._api_key == "DIRECT-ENVIRONMENT-CREDENTIAL"


@pytest.mark.parametrize("payload", [b"", b"FIRST-FILE-SECRET SECOND-FILE-SECRET", b"FIRST-FILE-SECRET\nSECOND-FILE-SECRET", b"\xff", b"CONTROL\0SECRET"])
def test_invalid_key_files_never_echo_their_contents(clean_api_environment, payload):
    clean_api_environment.write_bytes(payload)
    with pytest.raises(ModelError) as error:
        APIModel.from_env(provider="deepseek", api_key_file=clean_api_environment)
    assert error.value.code == "MODEL_CONFIG_ERROR"
    assert "FIRST-FILE-SECRET" not in str(error.value)
    assert "SECOND-FILE-SECRET" not in str(error.value)
    assert "CONTROL" not in str(error.value)


def test_missing_explicit_key_file_does_not_fall_back_to_environment(clean_api_environment, monkeypatch):
    monkeypatch.setenv("MODEL_API_KEY", "VALID-ENVIRONMENT-CREDENTIAL")
    with pytest.raises(ModelError, match="Cannot read API key file"):
        APIModel.from_env(provider="deepseek", api_key_file=clean_api_environment)


def test_deepseek_profile_uses_its_official_endpoint_and_default_key_file(clean_api_environment, monkeypatch):
    clean_api_environment.write_text("DEFAULT-DEEPSEEK-CREDENTIAL")
    monkeypatch.setenv("MODEL_BASE_URL", "https://unrelated.invalid/v1")
    client = APIModel.from_env(provider="deepseek")
    assert client.endpoint == "https://api.deepseek.com/chat/completions"
    assert client.model == "deepseek-flash"
    assert client._api_key == "DEFAULT-DEEPSEEK-CREDENTIAL"
    assert client.extra_body == {"thinking": {"type": "enabled"}}


def test_deepseek_profile_sends_images_and_tools_with_thinking_enabled(clean_api_environment):
    clean_api_environment.write_text("MOCK-DEEPSEEK-CREDENTIAL")
    seen = []
    client = APIModel.from_env(provider="deepseek", api_key_file=clean_api_environment,
                               extra_body={"thinking": {"type": "enabled"}, "temperature": 0},
                               transport=httpx.MockTransport(lambda request: seen.append(request) or httpx.Response(200, json=response())))
    client.decide(OBS, IMAGE, TOOLS, [])
    payload = json.loads(seen[0].content)
    assert payload["model"] == "deepseek-flash"
    assert payload["thinking"] == {"type": "enabled"}
    assert payload["max_tokens"] == 8192
    assert "enable_thinking" not in payload
    assert payload["tools"] == TOOLS
    assert payload["messages"][-1]["content"][1]["image_url"]["url"] == IMAGE
    assert payload["temperature"] == 0


def test_reasoning_and_assistant_content_survive_a_second_tool_request_without_truncation(clean_api_environment):
    clean_api_environment.write_text("THINKING-HISTORY-CREDENTIAL")
    seen = []
    reasoning = "synthetic state " * 1000
    assistant_content = "synthetic assistant text " * 300

    def handler(request):
        payload = json.loads(request.content)
        seen.append(payload)
        if len(seen) == 2:
            assistants = [message for message in payload["messages"] if message["role"] == "assistant"]
            assert len(assistants) == 1
            assert assistants[0]["reasoning_content"] == reasoning
            assert assistants[0]["content"] == assistant_content
            assert assistants[0]["tool_calls"][0]["id"] == "call-1"
            tool = next(message for message in payload["messages"] if message["role"] == "tool")
            assert tool["tool_call_id"] == "call-1"
        body = response()
        body["choices"][0]["message"].update(reasoning_content=reasoning, content=assistant_content)
        return httpx.Response(200, json=body)

    client = APIModel.from_env(provider="deepseek", transport=httpx.MockTransport(handler))
    first = client.decide(OBS, IMAGE, TOOLS, [])
    assert first.reasoning_content == reasoning and first.assistant_content == assistant_content
    assert len(first.raw_text) == 4096
    assert reasoning not in repr(first) and assistant_content not in repr(first)
    turn = history_turn(0)
    turn["calls"][0]["call_id"] = turn["results"][0]["call_id"] = "call-1"
    turn.update(reasoning_content=first.reasoning_content, assistant_content=first.assistant_content)
    client.decide(OBS, IMAGE, TOOLS, [turn])
    assert len(seen) == 2


def test_whole_turn_window_preserves_each_retained_reasoning_state(clean_api_environment):
    clean_api_environment.write_text("WINDOWED-THINKING-CREDENTIAL")
    client = APIModel.from_env(provider="deepseek", history_turns=2)
    turns = []
    for index in range(3):
        turn = history_turn(index)
        turn.update(reasoning_content=f"retained-state-{index}", assistant_content=None)
        turns.append(turn)
    messages = client.build_messages(OBS, IMAGE, turns)
    assistants = [message for message in messages if message["role"] == "assistant"]
    assert [message["reasoning_content"] for message in assistants] == ["retained-state-1", "retained-state-2"]
    assert [message["tool_call_id"] for message in messages if message["role"] == "tool"] == ["call-1", "call-2"]
    assert "retained-state-0" not in json.dumps(messages)


def test_deepseek_missing_reasoning_history_is_rejected_before_http(clean_api_environment):
    clean_api_environment.write_text("REASONING-REQUIRED-CREDENTIAL")
    client = APIModel.from_env(provider="deepseek", transport=httpx.MockTransport(lambda request: pytest.fail("network")))
    with pytest.raises(ModelProtocolError, match="history requires complete reasoning_content"):
        client.decide(OBS, IMAGE, TOOLS, [history_turn(0)])


@pytest.mark.parametrize("reasoning", [None, 17, {"text": "bad"}])
def test_deepseek_rejects_missing_or_malformed_response_reasoning(clean_api_environment, reasoning):
    clean_api_environment.write_text("RESPONSE-REASONING-CREDENTIAL")
    body = response()
    body["choices"][0]["message"]["reasoning_content"] = reasoning
    client = APIModel.from_env(provider="deepseek", transport=httpx.MockTransport(lambda request: httpx.Response(200, json=body)))
    with pytest.raises(ModelProtocolError, match="reasoning_content"):
        client.decide(OBS, IMAGE, TOOLS, [])


def test_generic_thinking_api_can_omit_provider_specific_reasoning_field():
    body = response()
    body["choices"][0]["message"].pop("reasoning_content")
    decision = model(lambda request: httpx.Response(200, json=body)).decide(OBS, IMAGE, TOOLS, [])
    assert decision.reasoning_content is None


@pytest.mark.parametrize("extra", [
    {"thinking": {"type": "disabled"}}, {"thinking": {}}, {"enable_thinking": False},
    {"reasoning_effort": "none"}, {"max_tokens": 1},
])
def test_non_thinking_or_token_limit_overrides_are_rejected(extra):
    with pytest.raises(ModelError):
        APIModel("https://example.invalid", "vision-test", "mock-key", extra_body=extra)


@pytest.mark.parametrize("limit", [0, -1, True, 1.5, 65537])
def test_invalid_output_token_budgets_are_rejected(limit):
    with pytest.raises(ModelError, match="max_output_tokens"):
        APIModel("https://example.invalid", "vision-test", "mock-key", max_output_tokens=limit)


def test_configured_thinking_budget_reaches_the_request():
    seen = []
    client = model(lambda request: seen.append(json.loads(request.content)) or httpx.Response(200, json=response()),
                   max_output_tokens=16384)
    client.decide(OBS, IMAGE, TOOLS, [])
    assert seen[0]["max_tokens"] == client.max_output_tokens == 16384


def test_truncated_thinking_response_never_yields_tools():
    body = response()
    body["choices"][0]["finish_reason"] = "length"
    with pytest.raises(ModelProtocolError, match="truncated"):
        model(lambda request: httpx.Response(200, json=body)).decide(OBS, IMAGE, TOOLS, [])


def test_private_reasoning_is_redacted_but_not_exposed_by_decision_repr():
    body = response()
    body["choices"][0]["message"]["reasoning_content"] = "synthetic SECRET-KEY state"
    decision = model(lambda request: httpx.Response(200, json=body)).decide(OBS, IMAGE, TOOLS, [])
    assert decision.reasoning_content == "synthetic [REDACTED] state"
    assert "synthetic" not in repr(decision)


def test_explicit_model_name_overrides_environment_model(clean_api_environment, monkeypatch):
    clean_api_environment.write_text("MODEL-OVERRIDE-CREDENTIAL")
    monkeypatch.setenv("MODEL_NAME", "environment-model")
    assert APIModel.from_env(provider="deepseek", model_name="explicit-model").model == "explicit-model"


def test_file_loaded_credentials_are_registered_for_runner_error_redaction(clean_api_environment):
    clean_api_environment.write_text("FILE-ONLY-REGISTERED-CREDENTIAL")
    APIModel.from_env(provider="deepseek", api_key_file=clean_api_environment)
    assert "MODEL_API_KEY" not in os.environ
    assert redact_message("failure: FILE-ONLY-REGISTERED-CREDENTIAL") == "failure: [REDACTED]"


def test_unknown_provider_is_rejected_before_reading_any_credential(clean_api_environment):
    with pytest.raises(ModelError, match="Unknown model provider"):
        APIModel.from_env(provider="not-a-provider")


def test_explicit_no_env_proxy_setting_reaches_the_http_client(monkeypatch):
    original = httpx.AsyncClient
    settings = []

    def client_factory(**kwargs):
        settings.append(kwargs)
        return original(**kwargs)

    monkeypatch.setattr(httpx, "AsyncClient", client_factory)
    client = model(lambda request: httpx.Response(200, json=response()), trust_env=False)
    client.decide(OBS, IMAGE, TOOLS, [])
    assert client.trust_env is False
    assert settings[0]["trust_env"] is False


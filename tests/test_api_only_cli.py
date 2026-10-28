"""Public execution must use the API and cannot disable model thinking."""

from pathlib import Path
from types import SimpleNamespace

import pytest

from go2_demo import __main__ as cli
from go2_demo.models import APIModel


def test_default_entry_uses_deepseek_api_and_new_scene_without_reading_credentials(monkeypatch):
    seen = []

    def run(args, scenario, run_dir):
        seen.append((args, scenario))
        return {"success": True, "termination": "finish"}, 0

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main([]) == 0
    args, scenario = seen[0]
    assert args.mode == "api" and args.provider == "deepseek"
    assert args.max_output_tokens == 8192 and args.api_timeout == 90
    assert scenario.task_id == "go_to_blue_ball"


@pytest.mark.parametrize("arguments", [["--mode", "scripted"], ["--disable-thinking"]])
def test_removed_modes_are_rejected_before_loading_a_model(monkeypatch, arguments):
    monkeypatch.setattr(cli, "_run_single", lambda *args: pytest.fail("invalid option started a model"))
    with pytest.raises(SystemExit) as error:
        cli.main(arguments)
    assert error.value.code == 2


@pytest.mark.parametrize("budget", ["0", "65537", "not-a-number"])
def test_invalid_output_budget_is_rejected_before_loading_credentials(monkeypatch, budget):
    monkeypatch.setattr(cli, "_run_single", lambda *args: pytest.fail("invalid budget started a model"))
    with pytest.raises(SystemExit) as error:
        cli.main(["--max-output-tokens", budget])
    assert error.value.code == 2


def test_api_factory_forwards_reasoning_budget_timeout_and_proxy_configuration(monkeypatch):
    settings = []
    sentinel = object()

    def from_env(**kwargs):
        settings.append(kwargs)
        return sentinel

    monkeypatch.setattr(APIModel, "from_env", from_env)
    args = SimpleNamespace(provider="deepseek", api_key_file=Path("test-credential.txt"),
                           model_name="deepseek-flash", no_env_proxy=True, api_timeout=120,
                           history_turns=4, max_output_tokens=16384)
    assert cli._make_model(args, object()) is sentinel
    assert settings == [{"provider": "deepseek", "api_key_file": Path("test-credential.txt"),
                         "model_name": "deepseek-flash", "trust_env": False,
                         "timeout_s": 120, "history_turns": 4, "max_output_tokens": 16384}]


def test_output_budget_override_reaches_selected_api_run(monkeypatch):
    budgets = []

    def run(args, scenario, run_dir):
        budgets.append((args.max_output_tokens, args.api_timeout))
        return {"success": True, "termination": "finish"}, 0

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main(["--mode", "api", "--max-output-tokens", "16384", "--api-timeout", "120"]) == 0
    assert budgets == [(16384, 120)]

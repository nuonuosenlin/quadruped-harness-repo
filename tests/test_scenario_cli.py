"""Scenario selection and suite accounting must not silently reuse the baseline."""

import json
from pathlib import Path

import pytest

from go2_demo import __main__ as cli


def _summary(directory):
    paths = list(directory.glob("*/summary.json"))
    assert len(paths) == 1
    return json.loads(paths[0].read_text(encoding="utf-8"))


def test_list_new_tasks_does_not_load_credentials_or_run_backend(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(cli, "_make_model", lambda *args: pytest.fail("listing read credentials"))
    monkeypatch.setattr(cli, "_run_single", lambda *args: pytest.fail("listing started a simulation"))
    assert cli.main(["--mode", "api", "--api-key-file", str(tmp_path / "missing.txt"), "--list-tasks"]) == 0
    output = capsys.readouterr().out
    assert "go_to_blue_ball" in output and "distinguish_texture_a" in output
    assert "go_through_green_rectangle_tunnel" in output
    assert "crawl_red_gate2 | crawl | unsupported" in output


def test_selected_task_is_forwarded_instead_of_original_red_marker(monkeypatch, tmp_path):
    selected = []

    def run(args, scenario, run_dir):
        selected.append((scenario, run_dir))
        return {"success": True, "termination": "finish"}, 0

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main(["--task", "go_to_blue_ball", "--runs-dir", str(tmp_path)]) == 0
    assert selected[0][0].task_id == "go_to_blue_ball"
    assert "蓝色球体" in selected[0][0].instruction
    assert "go_to_blue_ball" in selected[0][1].name


def test_unsupported_crawl_never_starts_a_model_or_simulator(monkeypatch, capsys):
    monkeypatch.setattr(cli, "_run_single", lambda *args: pytest.fail("unsupported task ran"))
    assert cli.main(["--mode", "api", "--task", "crawl_red_gate2"]) == 2
    assert "Unsupported task crawl_red_gate2" in capsys.readouterr().err


def test_suite_runs_new_cases_and_never_counts_unsupported_as_success(monkeypatch, tmp_path):
    seen = []

    def run(args, scenario, run_dir):
        seen.append(scenario.task_id)
        success = scenario.task_id != "go_to_blue_ball"
        return {"success": success, "termination": "finish", "model_calls": 2,
                "usage": {"total_tokens": 10}}, 0 if success else 1

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main(["--suite", "quard-planar", "--mode", "api", "--runs-dir", str(tmp_path)]) == 1
    report = _summary(tmp_path)
    assert len(seen) == 13 and "red_marker" not in seen
    assert report["runnable_cases"] == report["completed_cases"] == 13
    assert report["successes"] == 12 and report["failures"] == 1
    assert report["skipped_cases"] == 2 and report["not_run_cases"] == 0
    assert report["model_calls"] == 26 and report["usage"]["total_tokens"] == 130
    assert not report["is_official_quard_benchmark"]
    assert all(case["success"] is None for case in report["cases"] if case["status"] == "skipped")


@pytest.mark.parametrize("termination,code", [("interrupted", 130), ("configuration_error", 2)])
def test_suite_preserves_unrun_cases_when_execution_must_stop(monkeypatch, tmp_path, termination, code):
    attempts = []

    def run(args, scenario, run_dir):
        attempts.append(scenario.task_id)
        return {"success": False, "termination": termination}, code

    monkeypatch.setattr(cli, "_run_single", run)
    assert cli.main(["--suite", "quard-planar", "--runs-dir", str(tmp_path)]) == code
    report = _summary(tmp_path)
    assert len(attempts) == 1
    assert report["completed_cases"] == 1 and report["not_run_cases"] == 12
    assert report["skipped_cases"] == 2 and report["successes"] == 0
    assert all(case["success"] is None for case in report["cases"] if case["status"] in {"skipped", "not_run"})


def test_task_and_suite_cannot_accidentally_override_each_other():
    with pytest.raises(SystemExit) as error:
        cli.main(["--task", "red_marker", "--suite", "quard-planar"])
    assert error.value.code == 2

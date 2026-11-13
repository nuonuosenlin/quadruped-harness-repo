"""Run MuJoCo scenarios through a thinking-capable model API."""

import argparse
from datetime import datetime
import math
from pathlib import Path
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_SOURCE = "local_mujoco_adaptation_not_official_QUARD_environment"


def positive_number(value):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return value


def _write_json(path: Path, data: dict) -> None:
    from .runner import json_text
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json_text(data) + "\n", encoding="utf-8")
    temporary.replace(path)


def _make_model(args, scenario):
    from .models import APIModel
    return APIModel.from_env(provider=args.provider, api_key_file=args.api_key_file,
                             model_name=args.model_name, trust_env=not args.no_env_proxy,
                             timeout_s=args.api_timeout, history_turns=args.history_turns,
                             max_output_tokens=args.max_output_tokens)


def _run_single(args, scenario, run_dir: Path) -> tuple[dict, int]:
    from .models import ModelError
    from .runner import run_episode, _safe_error
    backend, model = None, None
    print(f"Task: {scenario.task_id} | {scenario.title}", flush=True)
    print(f"Instruction: {scenario.instruction}", flush=True)
    print(f"Scenario source: {scenario.source}", flush=True)
    try:
        model = _make_model(args, scenario)
        from .backend import MujocoGo2Backend
        backend = MujocoGo2Backend(args.assets_dir, seed=args.seed, viewer=args.viewer, scenario=scenario)
        print(f"Mode: {args.mode} | Real MuJoCo Go2 dynamics | API waiting pauses physics", flush=True)
        print(f"Logs: {run_dir}", flush=True)
        metrics = run_episode(backend, model, mode=args.mode, run_dir=run_dir, seed=args.seed,
                              max_model_calls=args.max_model_calls, max_wall_seconds=args.max_wall_seconds,
                              max_sim_seconds=args.max_sim_seconds, history_turns=args.history_turns,
                              task=scenario.instruction, memory_v1=args.memory_v1)
        backend, model = None, None  # run_episode closed both owned resources.
        print(f"Success: {metrics['success']} | Termination: {metrics['termination']}", flush=True)
        if metrics.get("error"):
            print(f"Error: {metrics['error']}", file=sys.stderr)
        code = 130 if metrics["termination"] == "interrupted" else (0 if metrics["success"] else 1)
        return metrics, code
    except KeyboardInterrupt:
        metrics = {"success": False, "termination": "interrupted", "task_id": scenario.task_id,
                   "scenario_source": scenario.source, "mode": args.mode, "is_llm_result": args.mode == "api"}
        _write_json(run_dir / "metrics.json", metrics)
        print("Interrupted during setup.", file=sys.stderr)
        return metrics, 130
    except Exception as exc:
        is_config = isinstance(exc, ModelError) and getattr(exc, "code", None) == "MODEL_CONFIG_ERROR"
        metrics = {"success": False, "termination": "configuration_error" if is_config else "startup_error",
                   "task_id": scenario.task_id, "scenario_source": scenario.source,
                   "mode": args.mode, "is_llm_result": args.mode == "api", "error": _safe_error(exc)}
        _write_json(run_dir / "metrics.json", metrics)
        print(f"Startup error: {metrics['error']}", file=sys.stderr)
        return metrics, 2
    finally:
        if backend is not None:
            try:
                backend.stop()
            except Exception as exc:
                print(f"Cleanup stop error: {_safe_error(exc)}", file=sys.stderr)
            finally:
                try:
                    backend.close()
                except Exception as exc:
                    print(f"Cleanup close error: {_safe_error(exc)}", file=sys.stderr)
        if model is not None and hasattr(model, "close"):
            model.close()


def _suite_summary(args, scenarios, results) -> dict:
    completed = [item for item in results if item["status"] in {"completed", "error"}]
    successes = sum(item.get("success") is True for item in completed)
    usage = {}
    for item in completed:
        for key, value in item.get("metrics", {}).get("usage", {}).items():
            if isinstance(value, (int, float)):
                usage[key] = usage.get(key, 0) + value
    runnable = sum(scenario.supported for scenario in scenarios)
    return {
        "suite": args.suite, "mode": args.mode, "seed": args.seed,
        "scenario_source": SCENARIO_SOURCE, "is_official_quard_benchmark": False,
        "is_llm_result": args.mode == "api", "total_cases": len(scenarios),
        "runnable_cases": runnable, "completed_cases": len(completed),
        "successes": successes, "failures": len(completed) - successes,
        "skipped_cases": sum(item["status"] == "skipped" for item in results),
        "not_run_cases": sum(item["status"] == "not_run" for item in results),
        "success_rate_completed": successes / len(completed) if completed else None,
        "success_rate_all_runnable": successes / runnable if runnable else None,
        "model_calls": sum(item.get("metrics", {}).get("model_calls", 0) for item in completed),
        "usage": usage, "cases": results,
    }


def _run_suite(args, scenarios) -> int:
    directory = args.runs_dir / (datetime.now().strftime("%Y%m%d-%H%M%S") +
                                f"-suite-{args.suite}-{args.mode}-s{args.seed}-" + uuid.uuid4().hex[:6])
    results = [{"task_id": scenario.task_id, "title": scenario.title, "category": scenario.category,
                "status": "not_run" if scenario.supported else "skipped", "success": None,
                **({"reason": scenario.unsupported_reason} if not scenario.supported else {})}
               for scenario in scenarios]
    print(f"Suite: {args.suite} | local MuJoCo adaptations | Summary: {directory / 'summary.json'}", flush=True)
    _write_json(directory / "summary.json", _suite_summary(args, scenarios, results))
    exit_code = 0
    for index, scenario in enumerate(scenarios):
        if not scenario.supported:
            print(f"SKIPPED {scenario.task_id}: {scenario.unsupported_reason}", flush=True)
            continue
        run_dir = directory / scenario.task_id
        metrics, code = _run_single(args, scenario, run_dir)
        results[index].update(status="error" if code == 2 else "completed", success=bool(metrics["success"]),
                              metrics=metrics, run_dir=str(run_dir))
        _write_json(directory / "summary.json", _suite_summary(args, scenarios, results))
        if code == 130:
            exit_code = 130
            break
        if metrics.get("termination") == "configuration_error":
            exit_code = 2
            break
        if code and exit_code == 0:
            exit_code = 1
    summary = _suite_summary(args, scenarios, results)
    _write_json(directory / "summary.json", summary)
    print(f"Suite result: {summary['successes']}/{summary['completed_cases']} completed cases succeeded; "
          f"{summary['skipped_cases']} skipped, {summary['not_run_cases']} not run.", flush=True)
    print(f"Summary: {directory / 'summary.json'}", flush=True)
    return exit_code


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Go2 thinking API harness: select a MuJoCo task or run a suite")
    parser.add_argument("--mode", choices=("api",), default="api", help="API is the only runtime mode")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--task", help="scenario ID; default: go_to_blue_ball; see --list-tasks")
    selection.add_argument("--suite", choices=("quard-planar",), help="run 13 local adaptations and report two unsupported crawl cases")
    parser.add_argument("--list-tasks", action="store_true", help="list visible scenarios without loading credentials or the simulator")
    parser.add_argument("--provider", choices=("compatible", "deepseek"), default="deepseek")
    parser.add_argument("--api-key-file", type=Path)
    parser.add_argument("--model-name")
    parser.add_argument("--no-env-proxy", action="store_true")
    parser.add_argument("--viewer", action="store_true", help="show each scenario in the MuJoCo third-person viewer")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--assets-dir", type=Path, default=ROOT / "assets")
    parser.add_argument("--runs-dir", type=Path, default=ROOT / "runs")
    parser.add_argument("--max-model-calls", type=int, default=30)
    parser.add_argument("--max-wall-seconds", type=positive_number, default=300)
    parser.add_argument("--max-sim-seconds", type=positive_number, default=120)
    parser.add_argument("--api-timeout", type=positive_number, default=90)
    parser.add_argument("--max-output-tokens", type=int, default=8192,
                        help="per-request output budget, including model reasoning (default: 8192)")
    parser.add_argument("--history-turns", type=int, default=6)
    parser.add_argument("--memory-v1", action="store_true",
                        help="enable asynchronous rule memory and task-level planning; H0 remains default")
    args = parser.parse_args(argv)
    if not 1 <= args.max_model_calls <= 1000 or not 0 <= args.history_turns <= 100:
        parser.error("max-model-calls must be 1..1000 and history-turns 0..100")
    if not 1 <= args.max_output_tokens <= 65536:
        parser.error("max-output-tokens must be 1..65536")
    from .scenarios import get_scenario, list_scenarios
    if args.list_tasks:
        print("Task ID | category | status | visible scenario")
        for scenario in list_scenarios(include_demo=True):
            status = ("offline-only: sequential task not implemented" if scenario.offline_only else
                      "supported" if scenario.supported else "unsupported: " + scenario.unsupported_reason)
            print(f"{scenario.task_id} | {scenario.category} | {status} | {scenario.title}")
        print("Source: local MuJoCo adaptations, not the original QUARD simulator or published evaluation split.")
        return 0
    if args.suite:
        return _run_suite(args, [scenario for scenario in list_scenarios() if scenario.task_id != "red_marker"])
    try:
        scenario = get_scenario(args.task or "go_to_blue_ball")
    except ValueError as exc:
        parser.error(str(exc))
    if scenario.offline_only:
        print(f"Offline-only scene {scenario.task_id}: sequential task execution and scoring are not implemented.", file=sys.stderr)
        return 2
    if not scenario.supported:
        print(f"Unsupported task {scenario.task_id}: {scenario.unsupported_reason}", file=sys.stderr)
        return 2
    run_dir = args.runs_dir / (datetime.now().strftime("%Y%m%d-%H%M%S") +
                              f"-{args.mode}-{scenario.task_id}-s{args.seed}-" + uuid.uuid4().hex[:6])
    _, code = _run_single(args, scenario, run_dir)
    return code


if __name__ == "__main__":
    raise SystemExit(main())

"""Episode orchestration and an independent, privileged final evaluator."""

import base64
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import importlib.metadata
from io import BytesIO
import json
from pathlib import Path
import time

from PIL import Image

from .harness import Harness, TOOLS
from .models import APIModel, ModelError, SYSTEM_PROMPT, redact_message


TASK = "找到红色标记，移动到距离标记约 1 米的位置，朝向标记并停止，然后调用 finish。距离按机身参考点到标记的水平距离理解。"


def _json_default(value):
    if hasattr(value, "tolist"):
        return value.tolist()
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def json_text(data) -> str:
    return json.dumps(data, ensure_ascii=False, allow_nan=False, default=_json_default)


def _safe_error(exc: BaseException) -> dict:
    message = redact_message(str(exc))
    return {"type": type(exc).__name__, "code": getattr(exc, "code", "RUNTIME_ERROR"), "message": message[:1000]}


class RunLog:
    def __init__(self, directory: Path):
        self.directory = directory
        (directory / "frames").mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.events = (directory / "events.jsonl").open("w", encoding="utf-8")
        self.write_error = None

    def write(self, event: str, **data):
        line = json_text({"event": event, "wall_elapsed_s": time.monotonic()-self.started, **data}) + "\n"
        try:
            self.events.write(line)
            self.events.flush()
        except OSError as exc:
            # Preserve the resource cleanup path even if the disk becomes full.
            self.write_error = _safe_error(exc)

    def save_frame(self, frame, prefix: str) -> str:
        path = Path("frames") / f"{prefix}-{frame.frame_id}.png"
        Image.fromarray(frame.rgb).save(self.directory / path)
        return path.as_posix()

    def close(self):
        try:
            self.events.close()
        except OSError as exc:
            self.write_error = _safe_error(exc)


def image_data_url(rgb) -> str:
    buffer = BytesIO()
    Image.fromarray(rgb).save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")


def _task_context(backend, task: str | None = None) -> dict:
    scenario = getattr(backend, "scenario", None)
    return {
        "instruction": task or getattr(backend, "task_instruction", None) or getattr(scenario, "instruction", TASK),
        "task_id": getattr(scenario, "task_id", "red_marker"),
        "source": getattr(scenario, "source", "original_go2_demo"),
        "category": getattr(scenario, "category", "baseline"),
        "goal_kind": getattr(scenario, "goal_kind", "standoff"),
        "standoff_m": getattr(scenario, "standoff_m", 1.0),
        "distance_tolerance_m": getattr(scenario, "distance_tolerance_m", 0.18),
    }


def build_manifest(mode, seed, budgets, backend, model, *, task: str | None = None) -> dict:
    root = Path(__file__).resolve().parents[1]
    code_hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted((root / "go2_demo").glob("*.py"))}
    versions = {}
    for package in ("mujoco", "numpy", "torch", "opencv-python", "httpx", "Pillow"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = "not_recorded"
    context = _task_context(backend, task)
    passage = context["goal_kind"] == "passage"
    evaluation = {"goal_kind": context["goal_kind"],
                  "standoff_m": None if passage else context["standoff_m"],
                  "distance_tolerance_m": None if passage else context["distance_tolerance_m"],
                  "heading_tolerance_rad": None if passage else 0.25,
                  "max_speed_mps": 0.12, "max_yaw_rate_radps": 0.25,
                  "requires_finish": True, "no_collision_or_fall": True}
    if passage:
        scenario = backend.scenario
        evaluation.update({"passage_x_m": scenario.passage_x,
                           "passage_center_y_m": scenario.passage_center_y,
                           "passage_half_width_m": scenario.passage_half_width,
                           "finish_x_min_m": scenario.finish_x_min,
                           "requires_forward_crossing": True})
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(), "mode": mode, "seed": seed,
        "task": context["instruction"], "task_id": context["task_id"],
        "scenario_source": context["source"], "category": context["category"],
        "model": getattr(model, "model", "unknown_api_model"),
        "simulation_mode": "paused_during_model_inference", "backend": type(backend).__name__,
        "observation_protocol": "rgb_tracked_geometry_local_odometry_v2",
        "action_protocol": "bounded_relative_planar_motion_v1",
        "completion_contract": "public_body_reference_and_clearance_v2",
        "odometry_source": "idealized_simulated_proprioception_relative_to_episode_start",
        "posture_control_supported": False, "task_agent": False, "external_memory": False,
        "budgets": budgets, "package_versions": versions, "code_sha256": code_hashes,
        "api_settings": {"timeout_s": getattr(model, "timeout_s", None),
                         "max_output_tokens": getattr(model, "max_output_tokens", 8192),
                         "thinking": getattr(model, "extra_body", {}).get("thinking"),
                         "reasoning_history": "complete_retained_assistant_turns_in_memory",
                         "reasoning_logged": False},
        "asset_lock_sha256": hashlib.sha256((root / "assets.lock.json").read_bytes()).hexdigest()
            if (root / "assets.lock.json").exists() else None,
        "evaluation": evaluation,
    }


def run_episode(backend, model, *, mode: str, run_dir: Path, seed: int = 0,
                max_model_calls: int = 30, max_wall_seconds: float = 300,
                max_sim_seconds: float = 120, history_turns: int = 6,
                task: str | None = None) -> dict:
    """Both owned resources are stopped/closed on normal, failure and interrupt exits."""
    if mode != "api":
        raise ValueError("Only API-driven episodes are supported")
    log = RunLog(run_dir)
    budgets = {"max_model_calls": max_model_calls, "max_wall_seconds": max_wall_seconds,
               "max_sim_seconds": max_sim_seconds, "history_turns": history_turns}
    termination, error, final_stop = "runtime_error", None, None
    history, usage = [], {}
    calls_made, motion_calls = 0, 0
    reasoning_responses, reasoning_characters = 0, 0
    harness = None
    deadline = time.monotonic() + max_wall_seconds
    start_sim = None
    metrics = {}
    context = _task_context(backend, task)
    try:
        backend.deadline_monotonic = deadline
        manifest = build_manifest(mode, seed, budgets, backend, model, task=context["instruction"])
        (run_dir / "manifest.json").write_text(json_text(manifest), encoding="utf-8")
        (run_dir / "tools.json").write_text(json_text(TOOLS), encoding="utf-8")
        (run_dir / "system_prompt.txt").write_text(SYSTEM_PROMPT, encoding="utf-8")
        harness = Harness(backend, context["instruction"])
        start_sim = harness.frame.sim_time_s
        backend.sim_deadline_s = start_sim + max_sim_seconds
        for index in range(max_model_calls):
            remaining = deadline - time.monotonic()
            if remaining <= 0 or harness.frame.sim_time_s-start_sim >= max_sim_seconds:
                termination = "budget_exhausted"
                break
            observation = harness.observation()
            frame_path = log.save_frame(harness.frame, f"{index:03d}")
            log.write("model_input", turn=index, observation=observation, image_path=frame_path,
                      history_turns=min(len(history), history_turns))
            calls_made += 1
            started = time.monotonic()
            decision = model.decide(observation, image_data_url(harness.frame.rgb), TOOLS,
                                    history, timeout_s=remaining)
            reasoning = getattr(decision, "reasoning_content", None)
            reasoning_chars = len(reasoning) if isinstance(reasoning, str) else 0
            reasoning_responses += int(reasoning_chars > 0)
            reasoning_characters += reasoning_chars
            calls = [asdict(call) for call in decision.calls]
            log.write("model_response", turn=index, calls=calls, usage=decision.usage,
                      model=decision.model, latency_s=time.monotonic()-started,
                      reasoning_present=reasoning_chars > 0, reasoning_chars=reasoning_chars)
            for key, value in decision.usage.items():
                if isinstance(value, (int, float)):
                    usage[key] = usage.get(key, 0) + value
            if time.monotonic() >= deadline:
                termination = "budget_exhausted"
                log.write("discarded_response", reason="wall_deadline_exceeded")
                break
            results = harness.dispatch_many(decision.calls)
            motion_calls += sum(c.name in {"move_relative", "turn"} and not r.get("deduplicated")
                                and r.get("error_code") not in {"INVALID_ARGUMENTS", "ONE_TOOL_PER_TURN", "CALL_ID_REUSED"}
                                for c, r in zip(decision.calls, results))
            history.append({"observation": observation, "calls": calls, "results": results,
                            "reasoning_content": reasoning,
                            "assistant_content": getattr(decision, "assistant_content", None)})
            history = history[-history_turns:] if history_turns else []
            log.write("tool_results", turn=index, results=results,
                      next_observation=harness.observation())
            print(f"[{index+1:02d}] " + ", ".join(f"{r['tool']}: {r['status']}" for r in results), flush=True)
            if time.monotonic() >= deadline or harness.frame.sim_time_s-start_sim >= max_sim_seconds:
                termination = "budget_exhausted"
                break
            if harness.termination is not None:
                termination = harness.termination
                break
            # A fall/collision ends the run; these are proprioception/execution events, not goal truth.
            if any(r.get("error_code") in {"ROBOT_FELL", "COLLISION"} for r in results):
                termination = "execution_failure"
                break
        else:
            termination = "budget_exhausted"
    except KeyboardInterrupt:
        termination = "interrupted"
    except ModelError as exc:
        termination, error = "model_error", _safe_error(exc)
    except Exception as exc:
        termination, error = "runtime_error", _safe_error(exc)
    finally:
        # A simulator continues stepping under zero velocity for a bounded settling interval.
        # Do not equate successful submission of zero velocity with confirmed stopping.
        try:
            final_stop = backend.stop()
            log.write("final_stop", result=final_stop)
        except BaseException as exc:
            final_stop = {"status": "failed", "error_code": "STOP_EXCEPTION", "detail": _safe_error(exc)}
            log.write("final_stop", result=final_stop)
        try:
            final_frame = backend.capture()
            log.save_frame(final_frame, "final")
            evaluation = backend.evaluate(standoff_m=context["standoff_m"],
                                          tolerance_m=context["distance_tolerance_m"])
            sim_elapsed = final_frame.sim_time_s - (start_sim if start_sim is not None else 0)
            if termination == "finish" and (sim_elapsed > max_sim_seconds or time.monotonic() > deadline):
                termination = "budget_exhausted"
            if log.write_error is not None:
                termination, error = "logging_error", log.write_error
            metrics = {
                "mode": mode, "seed": seed, "termination": termination,
                "task_id": context["task_id"], "scenario_source": context["source"],
                "success": bool(termination == "finish" and evaluation["success"]
                                and final_stop.get("status") == "succeeded"
                                and sim_elapsed <= max_sim_seconds
                                and time.monotonic() <= deadline),
                "error": error, "final_stop": final_stop,
                "model_calls": calls_made, "motion_calls": motion_calls, "usage": usage,
                "reasoning_responses": reasoning_responses, "reasoning_characters": reasoning_characters,
                "wall_elapsed_s": time.monotonic()-log.started, "sim_elapsed_s": sim_elapsed,
                "evaluation": evaluation,
                "simulation_mode": "paused_during_model_inference",
                "is_llm_result": mode == "api",
            }
            (run_dir / "metrics.json").write_text(json_text(metrics), encoding="utf-8")
            with (run_dir / "trajectory.jsonl").open("w", encoding="utf-8") as stream:
                for row in getattr(backend, "trajectory", []):
                    stream.write(json_text(row) + "\n")
            log.write("episode_end", metrics=metrics)
        except BaseException as exc:
            metrics = {"success": False, "termination": "evaluation_error", "original_termination": termination,
                       "task_id": context["task_id"], "scenario_source": context["source"],
                       "error": _safe_error(exc), "final_stop": final_stop, "is_llm_result": mode == "api"}
            (run_dir / "metrics.json").write_text(json_text(metrics), encoding="utf-8")
            log.write("episode_end", metrics=metrics)
        finally:
            try:
                if hasattr(model, "close"):
                    model.close()
            finally:
                try:
                    backend.close()
                finally:
                    log.close()
    return metrics

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
    result = {"type": type(exc).__name__, "code": getattr(exc, "code", "RUNTIME_ERROR"), "message": message[:1000]}
    diagnostics = getattr(exc, "protocol_diagnostics", None)
    if diagnostics:
        result["protocol_diagnostics"] = diagnostics
    return result


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
    if context["goal_kind"] == "ordered_standoff":
        evaluation.update(checkpoint_order=["A", "B"],
                          checkpoint_labels={"A": "blue sphere", "B": "green box"},
                          checkpoint_A="historical measured confirmed stop", checkpoint_B="final measured confirmed stop",
                          sequence_protocol="ordered_standoff_v1")
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
                task: str | None = None, memory_v1: bool = False) -> dict:
    """Both owned resources are stopped/closed on normal, failure and interrupt exits."""
    if mode != "api":
        raise ValueError("Only API-driven episodes are supported")
    log = RunLog(run_dir)
    budgets = {"max_model_calls": max_model_calls, "max_wall_seconds": max_wall_seconds,
               "max_sim_seconds": max_sim_seconds, "history_turns": history_turns}
    termination, error, final_stop = "runtime_error", None, None
    history, usage = [], {}
    calls_made, motion_calls = 0, 0
    decision_calls = protocol_retries = 0
    reasoning_responses, reasoning_characters = 0, 0
    harness = None
    memory = planner = adapter = None
    deadline = time.monotonic() + max_wall_seconds
    start_sim = None
    metrics = {}
    context = _task_context(backend, task)
    try:
        backend.deadline_monotonic = deadline
        manifest = build_manifest(mode, seed, budgets, backend, model, task=context["instruction"])
        if memory_v1:
            manifest.update(external_memory=True, task_agent=True,
                            memory_protocol="rule_md_async_v1", planning_history="current_memory_snapshot_only")
            manifest["api_settings"]["reasoning_history"] = "not_sent_current_memory_snapshot_only"
        (run_dir / "manifest.json").write_text(json_text(manifest), encoding="utf-8")
        (run_dir / "tools.json").write_text(json_text(TOOLS), encoding="utf-8")
        system_prompt = SYSTEM_PROMPT
        if memory_v1:
            from .memory_planning import MEMORY_SYSTEM_PROMPT
            system_prompt = MEMORY_SYSTEM_PROMPT
        (run_dir / "system_prompt.txt").write_text(system_prompt, encoding="utf-8")
        harness = Harness(backend, context["instruction"])
        if memory_v1:
            from .memory import AsyncMemory
            from .memory_planning import MemoryPlanningHarness, PublicObservationAdapter
            memory = AsyncMemory(run_dir / "memory.md")
            from .memory_perception import task_targets
            adapter = PublicObservationAdapter(task_targets(context["task_id"]))
            planner = MemoryPlanningHarness(memory)
            memory.submit(adapter.payload(harness.observation(), 0, visual_candidates=
                adapter.visual_candidates(harness.frame.rgb, harness.frame.frame_id),
                rgb=harness.frame.rgb, depth_m=harness.frame.depth_m, intrinsics=harness.frame.intrinsics))
        start_sim = harness.frame.sim_time_s
        backend.sim_deadline_s = start_sim + max_sim_seconds
        for index in range(max_model_calls):
            remaining = deadline - time.monotonic()
            if calls_made >= max_model_calls or remaining <= 0 or harness.frame.sim_time_s-start_sim >= max_sim_seconds:
                termination = "budget_exhausted"
                break
            observation = (planner.context(context["instruction"], index,
                adapter.current_observation(harness.observation(), rgb=harness.frame.rgb,
                    depth_m=harness.frame.depth_m, intrinsics=harness.frame.intrinsics),
                adapter.perception.labels) if planner else harness.observation())
            frame_path = log.save_frame(harness.frame, f"{index:03d}")
            log.write("model_input", turn=index, observation=observation, image_path=frame_path,
                      history_turns=0 if planner else min(len(history), history_turns))
            request_slots = max_model_calls - calls_made
            calls_made += 1
            decision_calls += 1
            started = time.monotonic()
            request_options = {"timeout_s": remaining}
            if planner and isinstance(model, APIModel):
                request_options["max_requests"] = min(2, request_slots)
            decision = model.decide(observation, "" if planner else image_data_url(harness.frame.rgb), TOOLS,
                                    [] if planner else history, **request_options)
            extra_requests = max(0, getattr(decision, "request_attempts", 1) - 1)
            calls_made += extra_requests
            protocol_retries += extra_requests
            reasoning = getattr(decision, "reasoning_content", None)
            reasoning_chars = len(reasoning) if isinstance(reasoning, str) else 0
            response_count = getattr(decision, "reasoning_response_count", None)
            character_count = getattr(decision, "reasoning_character_count", None)
            reasoning_responses += response_count if response_count is not None else int(reasoning_chars > 0)
            reasoning_characters += character_count if character_count is not None else reasoning_chars
            if planner:
                log.write("model_protocol", turn=index, request_attempts=getattr(decision, "request_attempts", 1),
                          diagnostics=getattr(decision, "protocol_diagnostics", []))
            calls = [asdict(call) for call in decision.calls]
            planning_log = ({'planning_envelope': getattr(decision, 'planning_envelope', None),
                'assistant_content_present': bool(getattr(decision, 'assistant_content', None)),
                'assistant_content_chars': len(getattr(decision, 'assistant_content', None) or '')}
                if planner else {})
            log.write("model_response", turn=index, calls=calls, usage=decision.usage,
                      model=decision.model, latency_s=time.monotonic()-started,
                      reasoning_present=reasoning_chars > 0, reasoning_chars=reasoning_chars, **planning_log)
            for key, value in decision.usage.items():
                if isinstance(value, (int, float)):
                    usage[key] = usage.get(key, 0) + value
            if time.monotonic() >= deadline:
                termination = "budget_exhausted"
                log.write("discarded_response", reason="wall_deadline_exceeded")
                break
            feedback, binding = planner.prepare(decision, index) if planner else (None, {})
            results = [feedback] if feedback else harness.dispatch_many(decision.calls)
            if planner:
                results = [{**result, **binding} for result in results]
                planner.note_results(decision.calls, results)
                memory.submit(adapter.payload(harness.observation(), index + 1, results, binding,
                    adapter.visual_candidates(harness.frame.rgb, harness.frame.frame_id),
                    rgb=harness.frame.rgb, depth_m=harness.frame.depth_m, intrinsics=harness.frame.intrinsics))
            motion_calls += sum(c.name in {"move_relative", "turn"} and not r.get("deduplicated")
                                and r.get("error_code") not in {"INVALID_ARGUMENTS", "ONE_TOOL_PER_TURN", "CALL_ID_REUSED", "MEMORY_CONSTRAINT"}
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
        extra_requests = max(0, getattr(exc, "request_attempts", 1) - 1)
        calls_made += extra_requests
        protocol_retries += extra_requests
        for key, value in getattr(exc, "usage", {}).items():
            usage[key] = usage.get(key, 0) + value
        reasoning_responses += getattr(exc, "reasoning_response_count", 0)
        reasoning_characters += getattr(exc, "reasoning_character_count", 0)
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
        if memory is not None:
            try:
                memory.close()  # Drain only on shutdown, never between planner decisions.
            except Exception as exc:
                termination, error = "memory_error", _safe_error(exc)
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
                "model_calls": calls_made, "decision_calls": decision_calls,
                "protocol_retries": protocol_retries, "motion_calls": motion_calls, "usage": usage,
                "reasoning_responses": reasoning_responses, "reasoning_characters": reasoning_characters,
                "wall_elapsed_s": time.monotonic()-log.started, "sim_elapsed_s": sim_elapsed,
                "evaluation": evaluation,
                "simulation_mode": "paused_during_model_inference",
                "is_llm_result": mode == "api",
            }
            if "checkpoints" in evaluation:
                metrics["checkpoints"] = evaluation["checkpoints"]
                metrics["order_satisfied"] = evaluation["order_satisfied"]
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

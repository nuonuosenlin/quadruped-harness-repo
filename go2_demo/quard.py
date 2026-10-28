"""Pinned QUARD clips for offline data validation, separate from simulation scores.

The source ``depth/*.png`` files are 8-bit visualizations, not calibrated metric
depth. Raw command heights are offsets in the upstream locomotion interface.
Neither is silently converted into this demo's sensor or motion protocol.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
import hashlib
import io
import json
import math
from pathlib import Path, PurePosixPath
import pickle
import re
import sys

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK = ROOT / "datasets/quard.lock.json"
DEFAULT_DATA = ROOT / "data/quard"
COMMAND_FIELDS = ("x_vel_cmd", "y_vel_cmd", "yaw_vel_cmd", "body_height_cmd", "pitch_cmd")
_STATE_SHAPES = {"joint_pos": (12,), "joint_vel": (12,), "body_pos": (3,),
                 "body_quat": (4,), "body_linear_vel": (3,),
                 "body_angular_vel": (3,), "contact_states": (4,)}


class QuardDataError(ValueError):
    """Missing, corrupted or incompatible offline data."""


class _NumpyDictionaryReader(pickle.Unpickler):
    """Read upstream NumPy dictionaries without allowing arbitrary pickle globals."""

    def find_class(self, module: str, name: str):
        allowed = {
            ("numpy", "ndarray"): np.ndarray,
            ("numpy", "dtype"): np.dtype,
            ("numpy.core.multiarray", "_reconstruct"): np.core.multiarray._reconstruct,
            ("numpy.core.multiarray", "scalar"): np.core.multiarray.scalar,
            ("numpy._core.multiarray", "_reconstruct"): np.core.multiarray._reconstruct,
            ("numpy._core.multiarray", "scalar"): np.core.multiarray.scalar,
        }
        if (module, name) not in allowed:
            raise QuardDataError(f"Forbidden NumPy pickle global: {module}.{name}")
        return allowed[module, name]


def load_numpy_dictionary(path: Path) -> dict:
    """Load the source scalar object array using a minimal NumPy-only allowlist."""
    try:
        data = Path(path).read_bytes()
        if len(data) > 4_000_000:
            raise QuardDataError(f"NumPy dictionary exceeds the size limit: {path}")
        stream = io.BytesIO(data)
        version = np.lib.format.read_magic(stream)
        if version == (1, 0):
            shape, _, dtype = np.lib.format.read_array_header_1_0(stream)
        elif version == (2, 0):
            shape, _, dtype = np.lib.format.read_array_header_2_0(stream)
        else:
            raise QuardDataError(f"Unsupported NumPy format version: {version}")
        if shape != () or dtype != np.dtype("O"):
            raise QuardDataError(f"Expected a scalar NumPy object dictionary: {path}")
        value = _NumpyDictionaryReader(stream).load()
        if stream.read(1) or not isinstance(value, np.ndarray) or value.shape != () or value.dtype != dtype:
            raise QuardDataError(f"Invalid NumPy dictionary payload: {path}")
        result = value.item()
        if not isinstance(result, dict) or not result or not all(isinstance(key, str) for key in result):
            raise QuardDataError(f"Expected string dictionary keys: {path}")
        # Object-valued or nested data is outside the published numeric schema.
        for key, item in result.items():
            array = np.asarray(item)
            if array.dtype.kind not in "biuf" or not np.isfinite(array).all():
                raise QuardDataError(f"Non-finite or non-numeric NumPy field {key!r}: {path}")
        return result
    except QuardDataError:
        raise
    except (OSError, ValueError, TypeError, EOFError, pickle.UnpicklingError, OverflowError) as exc:
        raise QuardDataError(f"Cannot read NumPy dictionary {path}: {exc}") from exc


def _safe_relative(value: str) -> PurePosixPath:
    if not isinstance(value, str) or "\\" in value:
        raise QuardDataError("Dataset paths must be relative POSIX paths")
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or str(path) != value:
        raise QuardDataError(f"Unsafe dataset path: {value!r}")
    return path


def load_lock(lock_path: Path = DEFAULT_LOCK) -> dict:
    try:
        lock = json.loads(Path(lock_path).read_text(encoding="utf-8"))
        if lock["schema_version"] != 1 or not isinstance(lock["tasks"], list) or not lock["tasks"]:
            raise QuardDataError("Unsupported or empty QUARD lock")
        hz, frames = lock["sample_hz"], lock["frames"]
        if isinstance(hz, bool) or not isinstance(hz, (int, float)) or not math.isfinite(hz) or hz <= 0:
            raise QuardDataError("sample_hz must be positive and finite")
        if not isinstance(frames, list) or len(frames) != 4 or any(type(frame) is not int or frame < 0 for frame in frames):
            raise QuardDataError("A QUARD clip must contain four nonnegative integer frame indices")
        if any(first >= second for first, second in zip(frames, frames[1:])):
            raise QuardDataError("Frame indices must increase strictly")
        if not math.isclose((frames[-1] - frames[0]) / hz, 2.0, abs_tol=1 / hz):
            raise QuardDataError("Four-frame clips must span a two-second source window")
        task_ids = set()
        for task in lock["tasks"]:
            task_id, episode_id = task["task_id"], task["episode_id"]
            if any(len(_safe_relative(value).parts) != 1 for value in (task_id, episode_id)) or task_id in task_ids:
                raise QuardDataError("Task/episode identifiers must be unique single path components")
            task_ids.add(task_id)
            if not isinstance(task["instruction"], str) or not task["instruction"].strip():
                raise QuardDataError(f"Missing instruction for {task_id}")
            prefix = f"{task_id}/{episode_id}/"
            required = {prefix + "info.csv"}
            required.update(prefix + f"{folder}/{frame:03d}.{suffix}" for frame in frames
                            for folder, suffix in (("image", "png"), ("depth", "png"),
                                                   ("command", "npy"), ("action", "npy")))
            paths = set()
            for entry in task["files"]:
                path = str(_safe_relative(entry["path"]))
                if not path.startswith(prefix) or path in paths:
                    raise QuardDataError(f"Duplicate or mismatched file path: {path}")
                paths.add(path)
                if type(entry["bytes"]) is not int or entry["bytes"] <= 0 or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
                    raise QuardDataError(f"Invalid file checksum metadata: {path}")
            if not required.issubset(paths):
                raise QuardDataError(f"Lock is missing required four-frame files for {task_id}")
        return lock
    except QuardDataError:
        raise
    except (OSError, ValueError, TypeError, KeyError) as exc:
        raise QuardDataError(f"Cannot read QUARD lock {lock_path}: {exc}") from exc


def verify_task_files(data_dir: Path, task: dict) -> dict[str, Path]:
    root, verified = Path(data_dir).resolve(), {}
    for entry in task["files"]:
        relative = str(_safe_relative(entry["path"]))
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise QuardDataError(f"Dataset symlink escapes data directory: {relative}")
        if not path.is_file():
            raise QuardDataError(f"Missing QUARD sample: {relative}. Run python scripts/fetch_quard.py --task {task['task_id']}")
        data = path.read_bytes()
        if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise QuardDataError(f"QUARD sample checksum mismatch: {relative}; rerun scripts/fetch_quard.py")
        verified[relative] = path
    return verified


@dataclass
class QuardClip:
    task_id: str
    category: str
    instruction: str
    episode_id: str
    source_robot: str
    source_trajectory_frames: int
    frame_ids: tuple[int, ...]
    timestamps_s: np.ndarray
    rgb: np.ndarray
    depth_visualization: np.ndarray
    commands: np.ndarray
    proprioception: list[dict]
    world_ego_motion: np.ndarray


def _numeric(value, shape: tuple[int, ...], name: str) -> np.ndarray:
    array = np.asarray(value)
    if array.shape != shape or array.dtype.kind not in "biuf" or not np.isfinite(array).all():
        raise QuardDataError(f"Invalid numeric field {name}: expected finite shape {shape}")
    return array


def load_clip(data_dir: Path, task_id: str, *, lock_path: Path = DEFAULT_LOCK) -> QuardClip:
    lock = load_lock(lock_path)
    task = next((item for item in lock["tasks"] if item["task_id"] == task_id), None)
    if task is None:
        raise QuardDataError(f"Unknown QUARD task: {task_id}")
    files = verify_task_files(data_dir, task)
    prefix = f"{task_id}/{task['episode_id']}/"
    try:
        with files[prefix + "info.csv"].open(newline="", encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream))
        if len(rows) != 1 or rows[0]["instruction"] != task["instruction"]:
            raise QuardDataError(f"Recorded CSV instruction disagrees with lock: {task_id}")
        trajectory_length = float(rows[0]["traj_len"])
        if not math.isfinite(trajectory_length) or not trajectory_length.is_integer() or trajectory_length <= lock["frames"][-1]:
            raise QuardDataError(f"Clip exceeds recorded trajectory length: {task_id}")
        images, depths, commands, states = [], [], [], []
        for frame in lock["frames"]:
            image_path = files[prefix + f"image/{frame:03d}.png"]
            depth_path = files[prefix + f"depth/{frame:03d}.png"]
            with Image.open(image_path) as image:
                if image.mode != "RGB":
                    raise QuardDataError(f"Expected original RGB image: {image_path}")
                images.append(np.asarray(image).copy())
            with Image.open(depth_path) as depth:
                if depth.mode != "L" or depth.size != (images[-1].shape[1], images[-1].shape[0]):
                    raise QuardDataError(f"Expected matching 8-bit source depth visualization: {depth_path}")
                depths.append(np.asarray(depth).copy())
            command = load_numpy_dictionary(files[prefix + f"command/{frame:03d}.npy"])
            commands.append([float(_numeric(command[key], (), key)) for key in COMMAND_FIELDS])
            state = load_numpy_dictionary(files[prefix + f"action/{frame:03d}.npy"])
            for key, shape in _STATE_SHAPES.items():
                _numeric(state[key], shape, key)
            quaternion_norm = float(np.linalg.norm(state["body_quat"]))
            if not math.isclose(quaternion_norm, 1.0, abs_tol=0.01):
                raise QuardDataError(f"Invalid source body quaternion: {task_id}/{frame:03d}")
            states.append(state)
        rgb, depth_visualization = np.stack(images), np.stack(depths)
        positions = np.stack([state["body_pos"] for state in states])
        quaternions = np.stack([state["body_quat"] for state in states])
        # IsaacGym stores quaternions as x,y,z,w. Dego in the paper is a world-
        # frame pose difference; this is an offline label, not a model input.
        x, y, z, w = quaternions.T
        yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
        yaw_delta = (yaw - yaw[0] + np.pi) % (2 * np.pi) - np.pi
        ego_motion = np.column_stack((positions[:, :2] - positions[0, :2], yaw_delta))
        return QuardClip(task_id=task_id, category=task["category"], instruction=rows[0]["instruction"],
                         episode_id=task["episode_id"], source_robot=rows[0].get("urdf") or "not_recorded",
                         source_trajectory_frames=int(trajectory_length), frame_ids=tuple(lock["frames"]),
                         timestamps_s=np.asarray(lock["frames"], dtype=float) / lock["sample_hz"],
                         rgb=rgb, depth_visualization=depth_visualization, commands=np.asarray(commands),
                         proprioception=states, world_ego_motion=ego_motion)
    except QuardDataError:
        raise
    except (OSError, KeyError, TypeError, ValueError) as exc:
        raise QuardDataError(f"Invalid QUARD clip {task_id}: {exc}") from exc


def validate_dataset(data_dir: Path = DEFAULT_DATA, *, task_ids: list[str] | None = None,
                     lock_path: Path = DEFAULT_LOCK) -> dict:
    lock = load_lock(lock_path)
    selected = task_ids or [task["task_id"] for task in lock["tasks"]]
    if len(selected) != len(set(selected)):
        raise QuardDataError("Select each QUARD task only once")
    results = []
    for task_id in selected:
        clip = load_clip(data_dir, task_id, lock_path=lock_path)
        results.append({
            "task_id": clip.task_id, "category": clip.category, "episode_id": clip.episode_id,
            "instruction": clip.instruction, "data_valid": True,
            "source_robot": clip.source_robot, "source_trajectory_frames": clip.source_trajectory_frames,
            "frames": list(clip.frame_ids), "source_timestamps_s": clip.timestamps_s.tolist(),
            "window_seconds": float(clip.timestamps_s[-1] - clip.timestamps_s[0]),
            "rgb_shape": list(clip.rgb.shape), "depth_visualization_shape": list(clip.depth_visualization.shape),
            "command_fields": list(COMMAND_FIELDS), "source_commands": clip.commands.tolist(),
            "world_ego_motion_since_first_frame": clip.world_ego_motion.tolist(),
        })
    return {
        "evaluation_type": "offline_dataset_validation", "dataset": lock["dataset"],
        "revision": lock["revision"], "license": lock.get("license"),
        "sample_hz": lock["sample_hz"], "task_count": len(results),
        "category_counts": dict(Counter(item["category"] for item in results)),
        "source_robot_counts": dict(Counter(item["source_robot"] for item in results)),
        "frame_count": sum(len(item["frames"]) for item in results),
        "data_valid": True, "is_closed_loop_result": False, "is_llm_result": False,
        "task_success_rate": None,
        "integrity_scope": "pinned_revision_and_locked_member_sha256; full_archive_not_downloaded_or_hashed",
        "depth_semantics": "8_bit_visualization_without_metric_calibration",
        "command_height_semantics": "raw_upstream_offset_command_not_absolute_body_height",
        "sample_scope": "public_tasks_in_five_paper_categories; exact_CerebVLA_subset_and_Uv_Ul_splits_not_reproduced",
        "tasks": results,
    }


def _write_report(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    try:
        temporary.write_text(json.dumps(report, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate real QUARD clips offline; this does not measure navigation success.")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--lock-path", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--task", action="append", help="task ID; repeat to select several (default: all)")
    parser.add_argument("--report", type=Path, default=ROOT / "runs/quard/report.json")
    args = parser.parse_args(argv)
    try:
        selected = None if not args.task or args.task == ["all"] else args.task
        report = validate_dataset(args.data_dir, task_ids=selected, lock_path=args.lock_path)
        _write_report(args.report, report)
        print(f"QUARD offline data validation: {report['task_count']} tasks, {report['frame_count']} frames, all valid.")
        print(f"Report: {args.report}")
        return 0
    except (QuardDataError, OSError) as exc:
        failure = {"evaluation_type": "offline_dataset_validation", "data_valid": False,
                   "is_closed_loop_result": False, "is_llm_result": False, "task_success_rate": None,
                   "selected_tasks": args.task or "all", "tasks": [],
                   "error": {"type": type(exc).__name__, "message": str(exc)[:1000]}}
        try:
            _write_report(args.report, failure)
        except OSError as report_error:
            print(f"Cannot write QUARD failure report: {report_error}", file=sys.stderr)
        print(f"QUARD validation error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

"""Offline QUARD tests: source labels and files never imply closed-loop success."""
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
import pytest

from go2_demo.quard import (COMMAND_FIELDS, QuardDataError, load_clip, load_lock,
                            load_numpy_dictionary, main, validate_dataset)


def _entry(path, data_dir):
    data = path.read_bytes()
    return {"path": path.relative_to(data_dir).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


@pytest.fixture
def sample(tmp_path):
    data_dir = tmp_path / "data"
    root = data_dir / "go_to_red_cube/000099"
    root.mkdir(parents=True)
    with (root / "info.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("instruction", "traj_len", "urdf"))
        writer.writerow(("go to the red cube, slowly", "150.0", "wr2"))
    for index, frame in enumerate((0, 33, 67, 100)):
        for folder in ("image", "depth", "command", "action"):
            (root / folder).mkdir(exist_ok=True)
        Image.new("RGB", (8, 6), (180, index, 0)).save(root / f"image/{frame:03d}.png")
        Image.new("L", (8, 6), index).save(root / f"depth/{frame:03d}.png")
        command = {key: np.float32(index + column * 0.1) for column, key in enumerate(COMMAND_FIELDS)}
        command["body_height_cmd"] = np.float32(-0.06)
        np.save(root / f"command/{frame:03d}.npy", command)
        yaw = np.deg2rad(179 + index * 2)
        state = {"joint_pos": np.zeros(12, np.float32), "joint_vel": np.zeros(12, np.float32),
                 "body_pos": np.array([10 + index, 20 + index * 2, 0.25], np.float32),
                 "body_quat": np.array([0, 0, np.sin(yaw / 2), np.cos(yaw / 2)], np.float32),
                 "body_linear_vel": np.zeros(3, np.float32), "body_angular_vel": np.zeros(3, np.float32),
                 "contact_states": np.array([True, False, True, False])}
        np.save(root / f"action/{frame:03d}.npy", state)
    lock = {"schema_version": 1, "dataset": "Tong314/QUARD", "revision": "a" * 40,
            "license": "mit", "sample_hz": 50, "frames": [0, 33, 67, 100], "tasks": [{
                "task_id": "go_to_red_cube", "category": "go_to", "episode_id": "000099",
                "instruction": "go to the red cube, slowly",
                "archive": {"url": "https://example.invalid/pinned.tar.gz", "bytes": 1, "sha256": "b" * 64},
                "files": [_entry(path, data_dir) for path in sorted(root.rglob("*")) if path.is_file()],
            }]}
    lock_path = tmp_path / "quard.lock.json"
    lock_path.write_text(json.dumps(lock), encoding="utf-8")
    return data_dir, lock_path, root, lock


def _rewrite_lock(lock_path, lock):
    lock_path.write_text(json.dumps(lock), encoding="utf-8")


def _update_file_metadata(data_dir, lock_path, lock, path):
    for entry in lock["tasks"][0]["files"]:
        if entry["path"] == path.relative_to(data_dir).as_posix():
            entry.update(_entry(path, data_dir))
    _rewrite_lock(lock_path, lock)


def test_temporal_clip_maps_raw_commands_and_wraps_source_world_yaw(sample):
    data_dir, lock_path, _, _ = sample
    clip = load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)
    assert clip.instruction == "go to the red cube, slowly"
    assert clip.source_robot == "wr2" and clip.source_trajectory_frames == 150
    assert clip.rgb.shape == (4, 6, 8, 3)
    assert clip.depth_visualization.dtype == np.uint8
    np.testing.assert_allclose(clip.timestamps_s, [0, 0.66, 1.34, 2.0])
    np.testing.assert_allclose(clip.commands[:, 0], [0, 1, 2, 3])
    np.testing.assert_allclose(clip.commands[:, 3], -0.06)
    np.testing.assert_allclose(clip.commands[0, [1, 2, 4]], [0.1, 0.2, 0.4])
    np.testing.assert_allclose(clip.world_ego_motion[:, :2], [[0, 0], [1, 2], [2, 4], [3, 6]])
    np.testing.assert_allclose(clip.world_ego_motion[:, 2], np.deg2rad([0, 2, 4, 6]), atol=1e-6)


def test_report_marks_data_integrity_separate_from_model_and_task_success(sample):
    data_dir, lock_path, _, _ = sample
    report = validate_dataset(data_dir, lock_path=lock_path)
    assert report["data_valid"]
    assert report["task_count"] == 1 and report["frame_count"] == 4
    assert report["source_robot_counts"] == {"wr2": 1}
    assert report["task_success_rate"] is None
    assert report["evaluation_type"] == "offline_dataset_validation"
    assert not report["is_llm_result"] and not report["is_closed_loop_result"]
    assert "not_absolute_body_height" in report["command_height_semantics"]
    assert "without_metric_calibration" in report["depth_semantics"]


def test_corrupted_locked_data_fails_before_loading_source_labels(sample):
    data_dir, lock_path, root, _ = sample
    (root / "command/000.npy").write_bytes(b"changed")
    with pytest.raises(QuardDataError, match="checksum mismatch"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


def test_missing_sample_explains_fetch_command(sample):
    data_dir, lock_path, root, _ = sample
    (root / "image/000.png").unlink()
    with pytest.raises(QuardDataError, match=r"fetch_quard.py --task go_to_red_cube"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


@pytest.mark.parametrize("bad_path", ["../../outside.npy", "/tmp/outside.npy", "go_to_red_cube\\bad.npy"])
def test_lock_rejects_path_traversal_and_non_posix_paths(sample, bad_path):
    _, lock_path, _, lock = sample
    lock["tasks"][0]["files"][0]["path"] = bad_path
    _rewrite_lock(lock_path, lock)
    with pytest.raises(QuardDataError, match="path"):
        load_lock(lock_path)


def test_symlink_cannot_escape_data_directory(sample, tmp_path):
    data_dir, lock_path, root, _ = sample
    path = root / "action/000.npy"
    outside = tmp_path / "outside.npy"
    path.rename(outside)
    path.symlink_to(outside)
    with pytest.raises(QuardDataError, match="symlink escapes"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


@pytest.mark.parametrize("frames", [[0, 33, 33, 100], [0, 1, 2, 3], [0, 33, True, 100], [0, 50, 100]])
def test_rejects_invalid_temporal_windows(sample, frames):
    _, lock_path, _, lock = sample
    lock["frames"] = frames
    _rewrite_lock(lock_path, lock)
    with pytest.raises(QuardDataError):
        load_lock(lock_path)


def test_csv_instruction_must_match_pinned_clip_metadata(sample):
    data_dir, lock_path, root, lock = sample
    info = root / "info.csv"
    info.write_text("instruction,traj_len\ngo to the green cube,150\n")
    _update_file_metadata(data_dir, lock_path, lock, info)
    with pytest.raises(QuardDataError, match="instruction disagrees"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


def test_observations_must_fit_original_recorded_trajectory(sample):
    data_dir, lock_path, root, lock = sample
    info = root / "info.csv"
    info.write_text('instruction,traj_len\n"go to the red cube, slowly",100\n')
    _update_file_metadata(data_dir, lock_path, lock, info)
    with pytest.raises(QuardDataError, match="trajectory length"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


def test_array_nonfinite_values_are_rejected(sample):
    data_dir, lock_path, root, lock = sample
    path = root / "command/000.npy"
    np.save(path, {key: np.float32(np.nan if key == "x_vel_cmd" else 0) for key in COMMAND_FIELDS})
    _update_file_metadata(data_dir, lock_path, lock, path)
    with pytest.raises(QuardDataError, match="Non-finite"):
        load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)


def test_restricted_numpy_loader_never_executes_pickle_globals(tmp_path):
    import os

    sentinel = tmp_path / "pickle_was_executed"

    class Payload:
        def __reduce__(self):
            return os.system, (f"touch {sentinel}",)

    path = tmp_path / "untrusted.npy"
    np.save(path, {"payload": Payload()})
    with pytest.raises(QuardDataError, match="Forbidden NumPy pickle global"):
        load_numpy_dictionary(path)
    assert not sentinel.exists()


@pytest.mark.parametrize("payload", [b"not a NumPy file", b"\x93NUMPY\x01\x00"])
def test_rejects_malformed_numpy_files(tmp_path, payload):
    path = tmp_path / "broken.npy"
    path.write_bytes(payload)
    with pytest.raises(QuardDataError):
        load_numpy_dictionary(path)


def test_cli_reports_missing_data_without_claiming_success(sample, tmp_path, capsys):
    _, lock_path, _, _ = sample
    report_path = tmp_path / "report.json"
    result = main(["--lock-path", str(lock_path), "--data-dir", str(tmp_path / "missing"),
                   "--report", str(report_path)])
    assert result == 2
    assert "Missing QUARD sample" in capsys.readouterr().err
    report = json.loads(report_path.read_text())
    assert not report["data_valid"] and report["task_success_rate"] is None


def test_cli_writes_an_explicit_offline_report(sample, tmp_path):
    data_dir, lock_path, _, _ = sample
    report_path = tmp_path / "reports/quard.json"
    assert main(["--lock-path", str(lock_path), "--data-dir", str(data_dir),
                 "--report", str(report_path), "--task", "go_to_red_cube"]) == 0
    assert json.loads(report_path.read_text())["task_success_rate"] is None


def test_source_robot_is_optional_for_custom_clips_but_never_assumed_go2(sample):
    data_dir, lock_path, root, lock = sample
    info = root / "info.csv"
    info.write_text('instruction,traj_len\n"go to the red cube, slowly",150\n')
    _update_file_metadata(data_dir, lock_path, lock, info)
    clip = load_clip(data_dir, "go_to_red_cube", lock_path=lock_path)
    assert clip.source_robot == "not_recorded"


def test_failed_rerun_supersedes_previous_valid_report(sample, tmp_path):
    data_dir, lock_path, root, _ = sample
    report_path = tmp_path / "report.json"
    args = ["--lock-path", str(lock_path), "--data-dir", str(data_dir), "--report", str(report_path)]
    assert main(args) == 0
    assert json.loads(report_path.read_text())["data_valid"]
    (root / "image/000.png").write_bytes(b"corrupt after first validation")
    assert main(args) == 2
    report = json.loads(report_path.read_text())
    assert not report["data_valid"]
    assert "checksum mismatch" in report["error"]["message"]
    assert not report_path.with_name("report.json.tmp").exists()

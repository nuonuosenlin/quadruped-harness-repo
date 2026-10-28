"""Exercise the dataset adapter on real, locked upstream clips without network I/O."""

import os
from pathlib import Path

import numpy as np
import pytest

from go2_demo.quard import DEFAULT_DATA, load_clip, load_lock


TASKS = load_lock()["tasks"]


@pytest.mark.dataset
@pytest.mark.parametrize("task", TASKS, ids=[task["task_id"] for task in TASKS])
def test_real_quard_temporal_clip_and_expert_labels(task):
    data_dir = Path(os.environ.get("QUARD_DATA_DIR", DEFAULT_DATA))
    if not (data_dir / task["task_id"]).exists():
        pytest.skip(f"QUARD sample absent; run python scripts/fetch_quard.py --task {task['task_id']}")

    # Loading includes checksums, recorded instruction, source trajectory bounds,
    # and the upstream command/proprioception schema. Partial data must fail.
    clip = load_clip(data_dir, task["task_id"])
    assert clip.instruction == task["instruction"]
    assert clip.category in {"distinguish", "go_to", "go_avoid", "go_through", "crawl"}
    assert clip.rgb.shape == (4, 480, 640, 3)
    assert clip.rgb.dtype == np.uint8
    assert clip.depth_visualization.shape == (4, 480, 640)
    assert clip.depth_visualization.dtype == np.uint8
    assert np.all(np.diff(clip.timestamps_s) > 0)
    assert clip.timestamps_s[-1] - clip.timestamps_s[0] == pytest.approx(2.0)
    assert clip.commands.shape == (4, 5)
    assert np.isfinite(clip.commands).all()
    assert len(clip.proprioception) == 4
    assert clip.world_ego_motion.shape == (4, 3)
    np.testing.assert_allclose(clip.world_ego_motion[0], np.zeros(3), atol=1e-6)
    assert np.all(np.abs(clip.world_ego_motion[:, 2]) <= np.pi + 1e-6)

#!/usr/bin/env python3
"""Write synthetic rule evidence to runs/<run-dir>/memory.md; no model/simulator.

Run from the repository: .venv/bin/python scripts/write_memory_example.py
"""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from go2_demo.memory import AsyncMemory


def observed(frame, x):
    return {"object_id": "marker-1", "category": "marker",
            "pose": {"frame": "task_local", "position_m": [x, 0.]},
            "pose_covariance": [[0.01, 0.], [0., 0.01]], "confidence": 0.95,
            "source": "synthetic_offline_detector", "frame_id": frame,
            "anchor_node": None, "visual_feature": {"description": "synthetic example marker"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, default=ROOT / "runs" / "memory-v1-offline-example")
    args = parser.parse_args()
    memory = AsyncMemory(args.run_dir / "memory.md")
    try:
        memory.submit({"step": 0, "objects": [observed("f0", 2.)]})
        memory.submit({"step": 1, "objects": [observed("f1", 2.)]})
        memory.plan("plan-0001", {"subgoals": [{"subgoal_id": "approach", "description": "接近标记",
            "preconditions": [{"object_id": "marker-1"}], "completion": [
                {"measurement": "marker-1.range_m", "op": "le", "value": 1.1}]}],
            "branches": [{"on": "target_state_changed", "subgoal_id": "approach"}],
            "recovery": "重新观察目标，确认新位置后重新规划"})
        memory.submit({"step": 2, "actions": [{"tool": "move_relative", "status": "failed",
            "error_code": "DYNAMIC_OBSTACLE", "plan_id": "plan-0001", "subgoal_id": "approach"}]})
        memory.submit({"step": 4})  # Three tool steps without new object evidence -> predicted.
        memory.submit({"step": 5, "objects": [observed("f5", 4.)]})  # Positive contradiction.
        memory.submit({"step": 6, "objects": [observed("f6", 4.)]})  # Reconfirm new pose.
        memory.plan("plan-0002", {"subgoals": [{"subgoal_id": "recover", "description": "新位置恢复接近",
            "preconditions": [{"object_id": "marker-1"}], "completion": [
                {"measurement": "marker-1.range_m", "op": "le", "value": 1.1}]}],
            "branches": [], "recovery": "若再次受阻则停止并重新观察"})
        memory.submit({"step": 7, "objects": [observed("f7", 4.)],
            "actions": [{"tool": "move_relative", "status": "succeeded", "plan_id": "plan-0002",
                         "subgoal_id": "recover"}],
            "measurements": {"marker-1.range_m": {"value": 1.05, "source": "synthetic_offline_range_sensor"}}})
    finally:
        memory.close()
    print(memory.path)


if __name__ == "__main__":
    main()

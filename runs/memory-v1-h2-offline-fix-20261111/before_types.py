"""Internal sensor data and model decisions. SensorFrame is never sent as-is to a model."""

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class SensorFrame:
    frame_id: str
    sim_time_s: float
    rgb: np.ndarray
    depth_m: np.ndarray
    intrinsics: np.ndarray
    camera_to_world: np.ndarray
    base_xy_yaw: np.ndarray
    robot_state: dict[str, Any]


@dataclass
class ToolCall:
    call_id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class Decision:
    calls: list[ToolCall]
    usage: dict[str, Any] = field(default_factory=dict)
    latency_s: float = 0.0
    model: str = "unknown"
    raw_text: str = ""
    reasoning_content: str | None = field(default=None, repr=False)
    assistant_content: str | None = field(default=None, repr=False)

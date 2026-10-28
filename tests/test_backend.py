"""Backend state contracts can be checked without a viewer or model API."""

import json
from types import SimpleNamespace

import numpy as np
import pytest

from go2_demo.backend import MujocoGo2Backend


@pytest.mark.parametrize("height,tilt_cos,position_value,expected", [
    (0.34, 1.0, 0.0, False),
    (0.15, 1.0, 0.0, True),
    (0.34, 0.5, 0.0, True),
    (0.34, 1.0, float("nan"), True),
    (0.34, 1.0, float("inf"), True),
])
def test_fall_state_is_correct_and_serializable_for_api_observations(height, tilt_cos, position_value, expected):
    backend = object.__new__(MujocoGo2Backend)
    backend.data = SimpleNamespace(qpos=np.array([position_value, 0.0, height]))
    tilt_sin = np.sqrt(1 - tilt_cos**2)
    rotation = np.array([[1.0, 0.0, 0.0], [0.0, tilt_cos, -tilt_sin], [0.0, tilt_sin, tilt_cos]])
    backend._base_pose = lambda: (np.array([0.0, 0.0, height]), 0.0, rotation)

    state = backend._fallen()
    assert state is expected
    assert json.loads(json.dumps({"fallen": state}))["fallen"] is expected

"""New geometry is opt-in and must never silently enter API runs or H0 suites."""

from pathlib import Path

import mujoco
import numpy as np
import pytest

from go2_demo import __main__ as cli
from go2_demo.backend import MujocoGo2Backend
from go2_demo.scenarios import get_scenario, list_scenarios


def test_scene_registration_preserves_default_suite_and_reuses_target_assets():
    legacy = list_scenarios()
    scene = get_scenario('memory_ab_occluded_v1')
    assert len(legacy) == 16 and sum(s.supported for s in legacy) == 14
    assert scene not in legacy and scene in list_scenarios(include_demo=True)
    assert not scene.offline_only and scene.supported
    assert scene.goal_kind == "ordered_standoff"
    blue = get_scenario('go_to_blue_ball').target
    green = get_scenario('go_to_green_cube').target
    assert (scene.target.kind, scene.target.color, scene.target.half_size, scene.target.z) == (
        blue.kind, blue.color, blue.half_size, blue.z)
    second = next(o for o in scene.objects if o.name == 'memory_goal_b')
    assert second.kind == green.kind and second.size == green.half_size and second.position[2] == green.z
    assert all(s.floor_half_size_m is None and not s.offline_only for s in legacy)


def test_ordered_demo_cli_is_selectable_but_listing_never_constructs_a_model(monkeypatch, capsys):
    selected = []

    def run(args, scene, directory):
        selected.append(scene)
        return {"success": True, "termination": "finish"}, 0

    monkeypatch.setattr(cli, '_run_single', run)
    monkeypatch.setattr(cli, '_make_model', lambda *args: pytest.fail('Listing loaded a model'))
    assert cli.main(['--task', 'memory_ab_occluded_v1']) == 0
    assert selected[0].goal_kind == 'ordered_standoff'
    assert cli.main(['--list-tasks']) == 0
    listing = capsys.readouterr().out
    assert 'memory_ab_occluded_v1 | memory_demo | supported' in listing


def test_new_scene_has_finite_flat_ground_without_changing_legacy_floor():
    assets = Path(__file__).resolve().parents[1] / 'assets'
    if not (assets / 'go2_rl_lab/resources/robots/go2/go2.xml').exists():
        pytest.skip('Pinned assets are not installed')

    def compile_scene(task):
        backend = object.__new__(MujocoGo2Backend)
        backend.asset_dir = assets
        backend.scenario = get_scenario(task)
        backend._target_xy = np.asarray(backend.scenario.target.xy)
        backend._environment_geom_names = []
        return backend._make_model()

    model = compile_scene('memory_ab_occluded_v1')
    floor = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, 'floor')
    assert model.geom_type[floor] == mujoco.mjtGeom.mjGEOM_BOX
    np.testing.assert_allclose(model.geom_size[floor], [8., 6., .1])
    assert model.geom_pos[floor, 2] + model.geom_size[floor, 2] == 0.
    for name in ('scenario_target', 'memory_goal_b', 'memory_drawers_body'):
        gid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, name)
        assert gid >= 0 and model.geom_contype[gid] != 0
    legacy = compile_scene('go_to_blue_ball')
    legacy_floor = mujoco.mj_name2id(legacy, mujoco.mjtObj.mjOBJ_GEOM, 'floor')
    assert legacy.geom_type[legacy_floor] == mujoco.mjtGeom.mjGEOM_PLANE

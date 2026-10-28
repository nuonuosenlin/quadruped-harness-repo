"""Passage task instructions expose completion rules without hidden scene poses."""

from dataclasses import replace
import re

import pytest

from go2_demo.scenarios import get_scenario, list_scenarios


PASSAGES = tuple(task for task in list_scenarios() if task.goal_kind == "passage")


@pytest.mark.parametrize("task", PASSAGES, ids=lambda task: task.task_id)
def test_passage_instruction_states_base_clearance_and_measurement_requirements(task):
    assert task.passage_clearance_m == 0.8
    instruction = task.instruction
    assert "机身 base 原点" in instruction
    assert "开口内" in instruction and "不得碰到门框" in instruction
    assert "至少0.8米" in instruction
    assert "停止并调用 finish" in instruction
    assert "前方0.32米" in instruction
    assert "门框移出画面不代表机身已经穿过" in instruction
    assert "local_odometry" in instruction and "实测位移" in instruction
    assert "门框点丢失时不得据此判定通过" in instruction
    assert "门框厚度、测量误差和运动跟踪误差" in instruction
    assert "不要求停在距该标记1米处" in instruction


@pytest.mark.parametrize("task", PASSAGES, ids=lambda task: task.task_id)
def test_passage_instructions_do_not_reveal_world_gate_or_finish_coordinates(task):
    numbers = set(re.findall(r"(?<![\d.])\d+(?:\.\d+)?(?![\d.])", task.instruction))
    assert not numbers.intersection({"2.2", "3.0", "4.4"})
    assert (task.passage_x, task.finish_x_min, task.passage_half_width) == (2.2, 3.0, 0.60)
    assert task.target.xy == (4.4, 0.0)


def test_public_passage_clearance_tracks_scoring_bounds_without_an_independent_threshold():
    passage = get_scenario("go_through_red_triangle_tunnel")
    relocated = replace(passage, passage_x=7.0, finish_x_min=8.25)
    assert relocated.passage_clearance_m == 1.25
    assert replace(passage, passage_x=None).passage_clearance_m is None
    assert replace(passage, finish_x_min=None).passage_clearance_m is None
    assert get_scenario("go_to_blue_ball").passage_clearance_m is None

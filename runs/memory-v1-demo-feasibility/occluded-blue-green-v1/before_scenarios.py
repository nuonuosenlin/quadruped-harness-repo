"""Visible MuJoCo task adaptations; these are not the original QUARD simulator."""

from dataclasses import dataclass, replace
import math


COLORS = {
    "red": (0.85, 0.035, 0.025, 1.0), "green": (0.04, 0.75, 0.10, 1.0),
    "blue": (0.04, 0.12, 0.85, 1.0), "yellow": (0.95, 0.80, 0.04, 1.0),
    "white": (0.95, 0.95, 0.95, 1.0),
}
LETTER_PATTERNS = {
    "A": ("01110", "11011", "11011", "11111", "11011", "11011", "11011"),
    "B": ("11110", "11011", "11011", "11110", "11011", "11011", "11110"),
    "C": ("01111", "11000", "11000", "11000", "11000", "11000", "01111"),
}


@dataclass(frozen=True)
class TargetSpec:
    kind: str
    color: str
    xy: tuple[float, float]
    z: float = 0.5
    half_size: tuple[float, float, float] = (0.08, 0.20, 0.5)
    letter: str | None = None


@dataclass(frozen=True)
class SceneObject:
    name: str
    kind: str
    position: tuple[float, float, float]
    size: tuple[float, ...]
    rgba: tuple[float, float, float, float]
    role: str = "obstacle"
    euler: tuple[float, float, float] | None = None
    letter: str | None = None


@dataclass(frozen=True)
class Scenario:
    task_id: str
    title: str
    category: str
    instruction: str
    target: TargetSpec
    objects: tuple[SceneObject, ...] = ()
    goal_kind: str = "standoff"
    standoff_m: float = 1.0
    distance_tolerance_m: float = 0.18
    passage_x: float | None = None
    passage_center_y: float = 0.0
    passage_half_width: float = 0.65
    finish_x_min: float | None = None
    target_jitter_m: float = 0.0
    unsupported_reason: str | None = None
    source: str = "local_mujoco_adaptation_not_official_QUARD_environment"

    @property
    def supported(self) -> bool:
        return self.unsupported_reason is None

    @property
    def passage_clearance_m(self) -> float | None:
        """Declared forward clearance, derived from the unchanged scoring bounds."""
        if self.goal_kind != "passage" or self.passage_x is None or self.finish_x_min is None:
            return None
        return round(self.finish_x_min - self.passage_x, 6)


_STOP = "到距离目标中心约1米处，面向目标并停止，然后调用 finish。"
_SCENARIOS = [Scenario(
    "red_marker", "原始红色标记", "baseline", "找到红色标记，移动" + _STOP,
    TargetSpec("box", "red", (3.0, 0.55)),
    objects=(SceneObject("blue_distractor", "box", (3.0, -1.3, 0.4), (0.12, 0.18, 0.4), COLORS["blue"], "distractor"),),
    target_jitter_m=0.15, source="original_go2_demo",
)]

for task_id, title, color, kind, xy in (
    ("go_to_blue_ball", "接近蓝色球体", "blue", "sphere", (3.0, -0.55)),
    ("go_to_green_cube", "接近绿色方块", "green", "box", (3.2, 0.5)),
    ("go_to_red_cube", "接近红色方块", "red", "box", (2.8, -0.35)),
):
    _SCENARIOS.append(Scenario(task_id, title, "go_to", "找到" + title.removeprefix("接近") + "，移动" + _STOP,
        TargetSpec(kind, color, xy, z=0.12 if kind == "sphere" else 0.20,
                   half_size=(0.12, 0.12, 0.12) if kind == "sphere" else (0.08, 0.18, 0.20)),
        objects=(SceneObject("wrong_color_object", "box", (3.0, -xy[1] * 1.8, 0.22),
                             (0.12, 0.15, 0.22), COLORS["red" if color != "red" else "green"], "distractor"),)))

for letter, target_y in (("A", 0.8), ("B", 0.0), ("C", -0.8)):
    others = tuple(SceneObject("sign_" + other, "sign", (3.2, other_y, 0.65), (0.025, 0.20, 0.25),
                              COLORS["white"], "distractor", letter=other)
                   for other, other_y in (("A", 0.8), ("B", 0.0), ("C", -0.8)) if other != letter)
    others += tuple(SceneObject("sign_support_" + other, "box", (3.2, y, 0.20), (0.025, 0.025, 0.20),
                                (0.25, 0.25, 0.25, 1.0)) for other, y in (("A", 0.8), ("B", 0.0), ("C", -0.8)))
    _SCENARIOS.append(Scenario("distinguish_texture_" + letter.lower(), "识别字母 " + letter, "distinguish",
        f"图中有三块白色字母标牌。只选择字母 {letter} 的标牌，移动" + _STOP,
        TargetSpec("sign", "white", (3.2, target_y), z=0.65, half_size=(0.025, 0.20, 0.25), letter=letter), others))

_GRAY = (0.32, 0.36, 0.42, 1.0)
_DARK = (0.06, 0.07, 0.08, 1.0)
_PROPS = {
    "cooker": (SceneObject("cooker_body", "box", (1.65, 0.0, 0.25), (0.23, 0.32, 0.25), _GRAY),
               SceneObject("cooker_top", "box", (1.65, 0.0, 0.515), (0.24, 0.33, 0.015), _DARK)),
    "drawers": (SceneObject("drawers_body", "box", (1.65, 0.0, 0.28), (0.22, 0.33, 0.28), (0.55, 0.33, 0.14, 1.0)),
                *(SceneObject(f"drawer_handle_{i}", "box", (1.42, 0.0, 0.12 + i * 0.17), (0.02, 0.14, 0.02), _DARK)
                  for i in range(3))),
    "fan": (SceneObject("fan_base", "box", (1.65, 0.0, 0.08), (0.24, 0.28, 0.08), _DARK),
            SceneObject("fan_stand", "cylinder", (1.65, 0.0, 0.27), (0.035, 0.22), _GRAY),
            SceneObject("fan_head", "cylinder", (1.65, 0.0, 0.45), (0.24, 0.055), _GRAY, euler=(0.0, math.pi / 2, 0.0))),
    "sofa": (SceneObject("sofa_seat", "box", (1.65, 0.0, 0.20), (0.32, 0.48, 0.20), (0.40, 0.20, 0.09, 1.0)),
             SceneObject("sofa_back", "box", (1.91, 0.0, 0.40), (0.07, 0.48, 0.15), (0.52, 0.29, 0.13, 1.0)),
             *(SceneObject(f"sofa_arm_{i}", "box", (1.65, y, 0.35), (0.32, 0.07, 0.15), (0.52, 0.29, 0.13, 1.0))
               for i, y in enumerate((-0.45, 0.45)))),
}
for prop, chinese in (("cooker", "炉台"), ("drawers", "抽屉柜"), ("fan", "落地扇"), ("sofa", "沙发")):
    _SCENARIOS.append(Scenario("go_avoid_texture_" + prop, "绕过" + chinese, "go_avoid",
        f"绕过前方的{chinese}，不得接触它。找到其后方的红色标记，移动" + _STOP,
        TargetSpec("box", "red", (3.5, 0.0), z=0.8, half_size=(0.06, 0.14, 0.55)),
        _PROPS[prop] + (SceneObject("target_support", "box", (3.5, 0.0, 0.125), (0.025, 0.04, 0.125), _GRAY),)))

for color, shape, chinese in (("green", "rectangle", "绿色矩形"), ("red", "triangle", "红色三角形"), ("yellow", "triangle", "黄色三角形")):
    if shape == "rectangle":
        gate = tuple(SceneObject(f"gate_post_{i}", "box", (2.2, y, 0.65), (0.10, 0.10, 0.65), COLORS[color])
                     for i, y in enumerate((-0.80, 0.80))) + (SceneObject("gate_top", "box", (2.2, 0.0, 1.35), (0.10, 0.90, 0.08), COLORS[color]),)
    else:
        gate = tuple(SceneObject(f"gate_slope_{i}", "box", (2.2, y, 0.85), (0.10, 0.08, math.hypot(0.85, 0.60)),
                                 COLORS[color], euler=(sign * math.atan2(0.60, 0.85), 0.0, 0.0))
                     for i, (y, sign) in enumerate(((-0.60, -1), (0.60, 1))))
    gate += (SceneObject("target_support", "box", (4.4, 0.0, 0.075), (0.02, 0.04, 0.075), _GRAY),)
    _passage = Scenario(f"go_through_{color}_{shape}_tunnel", "穿过" + chinese + "门框", "go_through", "",
        TargetSpec("box", color, (4.4, 0.0), z=0.6, half_size=(0.06, 0.16, 0.45)), gate,
        goal_kind="passage", passage_x=2.2, passage_half_width=0.60, finish_x_min=3.0)
    _SCENARIOS.append(replace(_passage, instruction=(
        f"从{chinese}门框的开口中穿过，不得碰到门框。以机身 base 原点为完成判据："
        "机身原点跨过门框平面时须位于开口内，随后沿穿门方向继续前进至少"
        f"{_passage.passage_clearance_m:g}米，再停止并调用 finish。"
        "为门框厚度、测量误差和运动跟踪误差留出保守余量。"
        "前置相机在机身原点前方0.32米；门框移出画面不代表机身已经穿过。"
        "趁门框仍可见时，用可靠的门框表面选点估计门框平面，结合后续 local_odometry "
        "与实际运动反馈确认机身是否越过平面并达到余量，不能累加命令距离代替实测位移。"
        "已跟踪点会自动更新；门框点丢失时不得据此判定通过。"
        "开口后方同色带白色十字的标记仅为视觉参照，本任务不要求停在距该标记1米处。"
    )))

for suffix in ("2", "3"):
    _SCENARIOS.append(Scenario("crawl_red_gate" + suffix, "低姿态穿过红色横杆 " + suffix, "crawl",
        "降低机身并从低矮横杆下爬过。", TargetSpec("box", "red", (3.0, 0.0)),
        unsupported_reason="当前预训练步态不支持行走中保持高度／俯仰目标，不能执行低姿态爬行。"))


def list_scenarios() -> tuple[Scenario, ...]:
    return tuple(_SCENARIOS)


def get_scenario(task_id: str) -> Scenario:
    for scenario in _SCENARIOS:
        if scenario.task_id == task_id:
            return scenario
    raise ValueError(f"Unknown task {task_id!r}; use --list-tasks")

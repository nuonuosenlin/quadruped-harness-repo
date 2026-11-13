"""Assemble the offline scene evidence; performs no simulation or model calls."""
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path('/home/nuonuosenlin/Agent-harness')
sys.path.insert(0, str(ROOT))
from go2_demo.scenarios import get_scenario

OUT = ROOT / 'runs/memory-v1-demo-feasibility/occluded-blue-green-v1'
g = json.loads((OUT / 'geometry_preflight.json').read_text())
p = json.loads((OUT / 'physical_preflight.json').read_text())
legacy = json.loads((OUT / 'legacy_scene_compatibility.json').read_text())
before = json.loads((OUT / 'before.json').read_text())
now = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in before['sha256']}
changed = [name for name in now if now[name] != before['sha256'][name]]
assert set(changed) == {'go2_demo/scenarios.py', 'go2_demo/backend.py', 'go2_demo/__main__.py'}
assert g['conclusion'] == p['conclusion'] == '通过'
assert legacy['all_legacy_compiled_geometry_unchanged']
assert p['total_collision_steps'] == 0 and not p['fallen']
v = {'conclusion': '通过', 'geometry_conclusion': g['conclusion'], 'physical_conclusion': p['conclusion'],
     'pytest': {'command': 'source .venv/bin/activate && python -m pytest -q', 'passed': 248, 'skipped': 15,
                'new_tests': 3, 'original_245_tests_passed': True},
     'list_tasks': {'command': './scripts/run_deepseek.sh --list-tasks', 'exit_code': 0,
                    'demo_entry': 'memory_ab_occluded_v1 | memory_demo | offline-only: sequential task not implemented'},
     'legacy_geometry': {'supported_scenes': 14, 'exact_compiled_comparison_passed': True},
     'changed_source_files_this_turn': changed, 'new_test_file': 'tests/test_memory_scene.py',
     'prior_memory_source_files_unchanged': True, 'source_sha256_before': before['sha256'], 'source_sha256_after': now,
     'api_calls': 0, 'key_reads': 0, 'sequential_task_implemented': False, 'ablation_runs': 0,
     'limitations': ['Grounded planar stops only, using a kinematic camera-height bound; no teleported/airborne poses.',
                     'Geometry/history requirements pass; no empirical claim that H0 must fail or that H2 memory improves results.',
                     'Robot dynamics used a fixed local-waypoint offline fixture with existing public ideal local_odometry; no private GT in its controller.',
                     'The unresolved memory data-chain and ideal-odometry design questions were not changed.']}
with (OUT / 'verification.json').open('x', encoding='utf-8') as stream:
    stream.write(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
proof = g['continuous_occlusion_proof']
a, b = p['checkpoint_diagnostics']
text = f'''# 遮挡 A→B 新场景：离线搭建与可行性复核

结论：**通过本轮场景可行性复核**。

本轮在 memory-v1 分支新增独立场景 `memory_ab_occluded_v1`，没有实现双目标任务、顺序阶段机或双目标正式评分器，没有 LLM 决策、API 调用、密钥读取、消融、在线文档访问或远程 push。下文物理检查是本轮明确要求的离线传感器／步态探针，不是模型 demo 或记忆收益实验。

## 新场景

- 有限平地：16×12m，范围 X∈[-8,8]、Y∈[-6,6]，顶面 z=0、厚度 0.2m；只改变本新场景，旧场景仍用原平面。
- 起点：沿用原机器人 reset 和 1s 站稳初始化，名义位置 (0,0)，朝 +X。
- 蓝球 A：中心 XY=(6.4,0)，球半径 0.12m，中心 z=0.12m；形状、颜色、尺寸均复用 go_to_blue_ball。
- 绿方块 B：中心 XY=(1.8,0.6)，半尺寸 (0.08,0.18,0.20)m，中心 z=0.20m；均复用 go_to_green_cube。A/B 中心相距 **{g['A_B_center_distance_m']:.6f}m**。
- 一件柜体：复用已有 drawers_body 和三个 drawer_handle，平移／缩放到中心 (3.8,0,1.0)m，实体柜身尺寸 0.44×4×2m；没有新建机器人或下载资产。
- 名义绕行路线：从柜体下方 Y=-2.8m 绕行，柜边 Y=-2m，预留 0.8m 横向间隙。

注册使用 `offline_only=True`，可通过 `get_scenario()` 和 `--list-tasks` 找到；默认 `list_scenarios()` 与 quard-planar 套件仍只返回原来的 16 条（14 个可运行、2 个不支持爬行）。公开 CLI 选择该新条目会在创建模型／读取凭据前返回“仅离线场景”，防止把单目标旧评分误当成双目标完成。

## 布局条件逐项验证

### 1. 起点能看到 B：通过

使用原始 MuJoCo 场景和相机视锥、最近表面射线检查，初始 B 存在无遮挡正向证据：{g['initial_B_visibility']['unoccluded_unique_sampled_pixels']} 个不同采样像素。实际物理初始化后，也用初始 RGB 的绿色掩膜选点，track_point / get_geometry 返回有效 B 几何，见 initial_B.png 和 physical_preflight.json。

### 2. 所有 A 合格停止位姿及 ±0.6rad 都看不到 B：通过

不是用有限网格代替全称证明。机身距 A 的允许范围为 [0.82,1.18]m；将完整相机安装偏移范数 {proof['camera_mount_full_norm_m']:.9f}m 加入后，所有相机 XY 必落在 A 中心半径 **{proof['camera_xy_disk_radius_m']:.9f}m** 的圆盘内，不依赖停止方位角、朝向误差或转向 yaw。

相机 X 范围为 {proof['camera_x_interval_m']}；B 的整个体积 X 范围为 [1.72,1.88]m。因此相机与 B 之间的每条线段都穿过柜内平面 X=3.8m。对相机圆盘的外接矩形及 B 全体积做保守区间运算，所有穿越点 Y 都处于 **[{proof['all_possible_ray_crossing_y_interval_m'][0]:.9f}, {proof['all_possible_ray_crossing_y_interval_m'][1]:.9f}]m**，严格落在柜身 [-2,2]m 内，最小侧边余量 **{proof['minimum_y_edge_margin_m']:.6f}m**。

对正常触地停止的 Go2，按四条腿的根节点到足端连杆长度总和与足接触半径求保守机身高度上界，再加完整相机偏移，得到相机高度不超过 **{proof['grounded_camera_height_bound_m']:.6f}m**；柜高 2m，最小顶边余量 **{proof['top_margin_m']:.6f}m**。B 位于 z∈[0,0.4]m，故正高度相机到 B 的所有射线也在柜身高度范围内。如果相机低于地面，则会先被平台遮挡。

证明覆盖正常平地、触地、无跌倒的机器人停止位姿；不包含任意抬升／传送到空中的反常位姿，不新增本体高度能力。该遮挡实际上不依赖 yaw，所以不只是 ±0.6rad，原地完整转一圈仍被柜体挡住。

补充 MuJoCo 射线扫查：3 个距离×72 个方位×3 个朝向误差×3 个转向，共 **{g['supplementary_ray_sweep']['view_count']} 个视角**，对 B 表面采样检查，无可见反例；进入视锥的 **{sum(g['supplementary_ray_sweep']['frustum_ray_first_hits'].values())} 条射线**首先命中柜身。连续证明承担全称结论，网格仅作交叉检查。

### 3. 去程超过 6 次决策：通过

起点到 A 中心 6.4m，进入 A 允许停止圆环至少净移动 5.22m。单次请求长度上限 0.6m，成功动作的终点误差容许 0.1m，因此正常成功单步的净移动上界取 0.7m；至少需要 **8 次成功运动调用**，大于 6 回合。只按请求长度计算则下界为 9 次。此界不适用于失控失败动作；没有改变工具界限来强造结果。

实际固定路线探针到 A 前用了 **{p['successful_motion_calls_before_A']} 次成功运动调用**，足以让早期原始回合掉出窗口。这不是 LLM 最短路线或预算预测；未来 demo 的预算仍待单独决定。

### 4. 场景合法与可达：通过

场景成功编译／加载。固定局部航点路径经 {g['reachability_geometry']['static_pose_samples']} 个静态姿态检查，无环境接触或平台越界；实际 pretrained Go2 步态探针沿绕柜路线可分别抵达 A、B。整段 {p['physics_trace_rows']} 行控制轨迹的碰撞步数为 **0**，fallen=false，清理 stop 成功。

探针不调用私有真值规划路线：路线是已知离线局部航点，控制只读既有公开 local_odometry，选点只看当前 RGB 的任务给定蓝／绿颜色。现有公开里程计本身仍是理想仿真来源，未在本轮改变或假装变成真实估计器。

## 工具定位与评分诊断

传感器检查仅按本场景给定的蓝／绿标签作颜色掩膜选像素，不是通用语义检测器，也不从 simulator target_id 反投影像素。initial_B、at_A、at_B 三个检查点都完成 track_point，随后 get_geometry 得到 valid=true、非空 relative_xy_m。

独立距离／朝向诊断才读取 `_base_pose()` 和预置目标位置，数据不反馈到控制器：

| 检查点 | 距目标中心 m | 朝向误差 rad | 速度 m/s | 绝对角速度 rad/s | 碰撞／跌倒 | 原标准 |
|---|---:|---:|---:|---:|---|---|
| A 蓝球 | {a['distance_m']:.6f} | {a['heading_error_rad']:.6f} | {a['speed_mps']:.6f} | {a['abs_yaw_rate_radps']:.6f} | 无／无 | 通过 |
| B 绿方块 | {b['distance_m']:.6f} | {b['heading_error_rad']:.6f} | {b['speed_mps']:.6f} | {b['abs_yaw_rate_radps']:.6f} | 无／无 | 通过 |

标准保持为距离 1.0±0.18m、朝向误差≤0.25rad、速度<0.12m/s、绝对角速度<0.25rad/s、无碰撞跌倒。此处只有离线检查点数值，**不是正式双目标 metrics.json 或整轮成功声明**；顺序任务、plan、阶段判定及正式双目标 evaluator 均未实现。

## 回归与保留范围

- pytest：**248 passed，15 skipped**；新增 3 项测试，原 245 项仍通过。
- 原 `./scripts/run_deepseek.sh --list-tasks` 正常，并额外列出 offline-only 新条目。
- 本轮改动前后逐项比较原 14 个可运行场景编译后的几何、碰撞属性、相机、机器人位置／旋转／尺寸和模型名称，全部完全一致；原 16 条场景定义去除新增默认元数据后也完全一致。
- 默认 H0、原套件范围、工具语义、记忆核心及其既有数据链均未改动。此前未解决的记忆数据来源和理想累计里程计设计问题仍保留，不因为场景通过而声称已解决。
- 本轮源码只改 scenarios.py、backend.py、__main__.py，新增 tests/test_memory_scene.py；其余本轮开始前的源码哈希均不变。

## 文件与复现

- scene.json：场景定义；scene.xml：实际编译保存的 MuJoCo XML。XML 仍复用仓库已安装的原始 mesh，非独立新模型包。
- layout.svg：俯视布局；initial_B.png、at_A.png、at_B.png：实际传感器图像。
- geometry_preflight.json：连续遮挡证明、射线、历史下界与静态可达性。
- physical_preflight.json：固定路径真实步态／工具返回、独立评分诊断和清理结果。
- legacy_scene_compatibility.json、verification.json：旧场景兼容性、测试与源码哈希。
- preflight.py：复现脚本；before.json 与 before_*.py 为本轮变更前本地快照。

从仓库根目录使用现有 `.venv`，在新目录先几何、通过后再物理：

```bash
.venv/bin/python runs/memory-v1-demo-feasibility/occluded-blue-green-v1/preflight.py \\
  --output-dir runs/memory-v1-demo-feasibility/occluded-blue-green-recheck
.venv/bin/python runs/memory-v1-demo-feasibility/occluded-blue-green-v1/preflight.py \\
  --physical --output-dir runs/memory-v1-demo-feasibility/occluded-blue-green-recheck
```

脚本对已有证据拒绝覆盖，且物理检查必须先有通过的几何报告。本轮未再执行以上复现命令，实际只做了一次物理探针。

本轮结论只说明所列场景约束、可达性、工具及评分可行性通过；不是“无记忆必败”的证明。H0 仍可能离开 A 区域后绕柜搜索 B，是否有记忆收益必须以后用同预算消融验证。本轮没有进行该实验。
'''
with (OUT / 'preflight.md').open('x', encoding='utf-8') as stream:
    stream.write(text)
shutil.copyfile(__file__, OUT / 'write_report.py')
print(json.dumps({'conclusion': v['conclusion'], 'report': str(OUT / 'preflight.md'),
                  'changed_source_files': changed, 'pytest': v['pytest']}, ensure_ascii=False, indent=2))

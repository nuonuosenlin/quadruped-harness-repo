"""Reproduce the local diagnosis and rule-only evidence. No API or dynamics."""
from collections import Counter
import ast
import hashlib
import json
from pathlib import Path
import shutil
import sys

import numpy as np

ROOT = Path('/home/nuonuosenlin/Agent-harness')
sys.path.insert(0, str(ROOT))
from go2_demo.memory import MemoryRules, read_state, state_packet
from go2_demo.memory_perception import task_targets
from go2_demo.memory_planning import PublicObservationAdapter

OUT = ROOT / 'runs/memory-v1-h2-offline-fix-20261111'
before = json.loads((OUT / 'before.json').read_text())
now = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
       for p in sorted((ROOT / 'go2_demo').glob('*.py'))}
unchanged = ['go2_demo/' + x for x in ('scenarios.py', 'backend.py', 'harness.py',
              'ordered_evaluation.py', '__main__.py', 'perception.py')]
assert all(before['source_sha256'][name] == now[name] for name in unchanged)
assert all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest
           for name, digest in before['old_H2_files_sha256'].items())

def assigned_string(path, name):
    module = ast.parse(path.read_text())
    return next(ast.literal_eval(node.value) for node in module.body if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == name for t in node.targets))

assert assigned_string(OUT / 'before_models.py', 'SYSTEM_PROMPT') == assigned_string(ROOT / 'go2_demo/models.py', 'SYSTEM_PROMPT')
run = ROOT / 'runs/memory-v1-ablation-20261111-s0/H2/20261111-005143-api-memory_ab_occluded_v1-s0-ec98dc'
rows = [json.loads(x) for x in (run / 'events.jsonl').read_text().splitlines()]
inputs = [r for r in rows if r['event'] == 'model_input']
responses = [r for r in rows if r['event'] == 'model_response']
calls = [c for r in responses for c in r['calls']]
old_memory = read_state((run / 'memory.md').read_text())
old = {'inputs': len(inputs), 'successfully_parsed_responses': len(responses),
       'last_input_zero_based_turn': inputs[-1]['turn'],
       'last_parsed_response_zero_based_turn': responses[-1]['turn'],
       'tool_counts': dict(Counter(c['name'] for c in calls)),
       'file_object_count': len(old_memory['objects']), 'ledger_entries': len(old_memory['ledger']),
       'inputs_with_task_target_labels': sum(bool(r['observation'].get('memory_state', {}).get('world', {}).get('task_targets')) for r in inputs),
       'inputs_with_fresh_current_observation': sum('current_observation' in r['observation'].get('memory_state', {}).get('world', {}) for r in inputs),
       'inputs_with_last_tool_feedback': sum('last_tool_feedback' in r['observation'].get('memory_state', {}).get('world', {}) for r in inputs),
       'raw_error_response_retained': False,
       'historical_error_exact_subcase': 'unknown: missing/non-list/empty/or over-16 tool_calls; raw response unavailable',
       'historical_error_not_this_branch': ['outer bad JSON', 'tool argument bad JSON', 'unknown tool name', 'missing tool parameters']}

# Explicitly synthetic observations, never retroactive claims about the old run.
rgb = np.zeros((80, 100, 3), np.uint8)
rgb[18:38, 12:32] = [10, 25, 220]
rgb[20:46, 60:86] = [10, 210, 20]
depth = np.full((80, 100), 2., dtype=float)
k = np.array([[100., 0., 50.], [0., 100., 40.], [0., 0., 1.]])
a = PublicObservationAdapter(task_targets('memory_ab_occluded_v1'))
rules = MemoryRules()
transitions = []
for frame, step in [('synthetic-f1', 0), ('synthetic-f1', 1), ('synthetic-f2', 2)]:
    obs = {'image_id': frame, 'image_size': {'width': 100, 'height': 80}, 'tracked_points': [],
           'local_odometry': {'translation_m': [0., 0.], 'yaw_rad': 0., 'source': 'synthetic_public_odometry'}}
    current = a.current_observation(obs, rgb=rgb, depth_m=depth, intrinsics=k)
    points = [{'point_id': 'synthetic-' + c['task_label'], 'image_id': frame, 'pixel_uv': c['pixel_uv'],
               'relative_xy_m': [2., .3 if c['task_label'] == 'B' else -.3], 'confidence': .99,
               'source': 'synthetic_rgbd_tracking', 'valid': True} for c in current['target_candidates']]
    result = {'tool': 'get_geometry' if step else 'track_point', 'status': 'succeeded', 'points': points}
    rules.update(a.payload(obs, step, [result], rgb=rgb, depth_m=depth, intrinsics=k))
    transitions.append({'step': step, 'frame': frame,
                         'task_objects': {o['object_id']: o['state'] for o in rules.state['objects'] if o['category'] == 'task_target'}})
assert list(transitions[0]['task_objects'].values()) == ['unknown', 'unknown']
assert list(transitions[1]['task_objects'].values()) == ['unknown', 'unknown']
assert list(transitions[2]['task_objects'].values()) == ['confirmed', 'confirmed']
(OUT / 'synthetic_memory.md').write_text(rules.document())

evidence = {'diagnosis': old, 'synthetic_rule_transitions': transitions,
            'synthetic_effective_task_objects': [o for o in state_packet(rules.state)['objects'] if o['category'] == 'task_target'],
            'task_scene_scoring_files_unchanged': unchanged, 'H0_system_prompt_unchanged': True,
            'previous_experiment_files_unchanged': True,
            'pytest': {'passed': 295, 'skipped': 15, 'new_tests': 28},
            'list_tasks': 'passed', 'actual_API_requests_this_turn': 0,
            'real_key_files_read': 0, 'demo_or_ablation_runs': 0,
            'source_sha256_before': before['source_sha256'], 'source_sha256_after': now}
(OUT / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
report = f'''# H2 离线诊断与修复

本轮仅在 memory-v1 分支离线读旧日志、改实现和跑测试。没有访问在线文档、读取真实密钥、调用真实 API、执行物理 demo 或消融，也没有改写旧 H2 证据。

## 旧问题的确切链路

旧 H2 有 {old['inputs']} 次模型输入、{old['successfully_parsed_responses']} 个成功解析响应；返回工具计数为 `{old['tool_counts']}`。没有 track_point 或 get_geometry，原 PointTracker 从未建立任何点，适配器因而一直送入 objects=[]。MemoryRules 的两帧确认规则本身并未收到可确认的对象，不是把已有合格 A/B 证据错误过滤掉。

原适配器也没有任务标签关联器：即使有追踪点，也只会生成 unclassified_landmark。它只看 observation.tracked_points，没有合并工具返回的 point/points。原规划状态中 task_targets、实时 current_observation、last_tool_feedback 的出现次数分别为 {old['inputs_with_task_target_labels']}、{old['inputs_with_fresh_current_observation']}、{old['inputs_with_last_tool_feedback']}。任务文本虽仍有蓝球／绿方块，结构化观测却只有未分类角点；没有 RGB 图像、颜色标签候选或可用的前一步工具反馈。反复 observe 并不会自动选点或产生语义对象。

门控并非“空记忆一律禁止运动”：空前置条件的合法探索计划原来就能通过。但可选 assistant plan 文本错误也会挡住安全感知调用；再加输入缺口和反复 observe 没有行动提示，形成了空转链路。

## 对象与当前观测修复

新增 memory_perception.py，只为该任务读取公开身份契约 A=蓝球、B=绿方块，不含位置或仿真对象 ID。它使用当前 RGB 的任务指定颜色连通分量、RGB-D 深度及相机内参提出候选，优先给出可跟踪角点；同色多对象、无效深度等不明确情况不绑定身份。这是任务特定的标签规则，不是通用语义检测器，更不声称靠颜色验证了所有物体形状。

候选本身不是 confirmed 对象。必须有当前有效工具追踪点，像素落在唯一匹配颜色分量中且 confidence≥0.8，才提出稳定 object_id=task:A／task:B 的观测；MemoryRules 仍要求独立高置信帧，重读同一帧不会增加支持证据。track_point.point、get_geometry.points 和 observation.tracked_points 都进入关联，旧帧结果不能覆盖当前帧。MD 保存任务标签、描述、来源、证据引用、当前相机系 XYZ 及坐标参考的来源说明。

结构化包仍严格保留八个顶层字段 world / pose / objects / active_beliefs / invalidated / events / topology / confidence_thresholds。world 额外提供任务标签、当前公开 RGB-D 候选／追踪几何、上一步工具反馈和 bootstrap_hint；即使 MD 写入滞后或有效对象为 0，这些当前事实仍可用，不等待后台写入。unknown／stale 没有被冒充 confirmed。

感知调用可不带计划，可选 plan 文本错误不阻断 observe／track_point／get_geometry；运动与 finish 仍须合法计划，失效或不满足的强前置条件仍被拒绝。有未追踪可见目标却连续两次 observe 后，再次 observe 会返回 MEMORY_NO_PROGRESS，明确引导选点；不会暗中替模型执行工具。空记忆仍允许基于当前观测的合法探索计划与有界原子动作。真实 LLM 能否执行好这些提示，本轮没有调用 API 验证。

## 真值来源边界

没有新增读取 camera_to_world、base_xy_yaw、场景目标坐标或评分真值用于新标签关联。相机系 XYZ 由当前深度和内参反投影得到。

现有公开 local_odometry 仍是理想仿真来源；原二维 episode_start 坐标参考保留，并明确标注 existing_public_idealized_simulator_odometry，未偷偷替换成“真实无漂移传感器”。工具已有 measured.translation_start_frame_m／yaw_delta_rad 只作为诊断归档，来源明确为 tool_result.measured.simulator_ground_truth_delta、navigation_measurement=false；不再把其模长写为普通 execution.displacement_m 导航测量，也不把它用于新的目标位置估计。该设计决策本身未在本轮改动。

## 第 83 次协议错误与修复

旧第 83 次原始响应没有落盘：只有最后输入、清理 stop 和脱敏错误，旧适配器仅在成功解析 Decision 后记录 model_response。因此无法再确定是 tool_calls 缺失、非列表、为空还是超过 16 个。该报错所在分支并非坏外层 JSON、未知工具名或缺参数的校验分支；不能凭空选定某个具体格式。本轮未向服务端重发请求或伪造旧原始响应。

现在 H2 强制 tool_choice=required、parallel_tool_calls=false，校验唯一工具及参数；遇到可修复的响应协议错误最多补一次修复请求。H0 仍保持原单次请求、tool_choice=auto 和原解析路径。新增诊断区分坏响应 JSON、缺失／空／超量工具、坏参数 JSON、未知工具、参数缺失和非法参数值等，记录结构类别、数量、已知 usage 及 reasoning 字符计数，不存原始私有正文或密钥。

两次尝试共用同一超时，重试计入 max_model_calls；只有一个请求名额时不重试，传输／配置错误不按格式错误重试。首次失败响应中可解析的 usage 和 reasoning 计数也保留；若整个响应都是坏 JSON，则其用量仍不可恢复，不能编造。metrics 新增 decision_calls、protocol_retries，model_calls 计实际尝试请求数。

## 测试与 H0 是否重跑

全量 pytest：**295 passed，15 skipped**，新增 28 项测试，原 267 项仍通过；`./scripts/run_deepseek.sh --list-tasks` 正常。覆盖 A/B 独立帧确认、同帧重复、歧义／无效／低置信拒绝、空 MD 下实时选点与探索移动、真实工具链的离线假后端重放、测量来源、重试修复／失败、一次上限、时间与请求预算、H0 请求不变，以及失败响应计数。所有传输测试均为进程内 mock，不连接远端；测试中的凭据均为合成夹具，未读取真实密钥。

任务、场景、指令、工具定义及正式评分语义均未改：scenarios.py、backend.py、harness.py、ordered_evaluation.py、__main__.py、perception.py 的哈希与本轮开始前完全相同；H0 SYSTEM_PROMPT 相同，单请求契约由测试覆盖。**按本次“任务／评分语义是否改变”的标准，H0 不用重跑。** 仅 H2 的感知输入、记忆标签、门控恢复及协议重试增强；若未来做新 H2 实验，应注明它是修复后的版本，且重试不能作为免费调用。

## 文件与证据

- 修改：go2_demo/memory.py、memory_planning.py、models.py、runner.py、types.py。
- 新增：go2_demo/memory_perception.py、tests/test_h2_perception.py、tests/test_h2_protocol.py。
- evidence.json：旧日志计数、合成规则轨迹、源码与旧成果哈希。
- synthetic_memory.md：仅由明确标记为 synthetic 的伪造 RGB-D／工具证据生成；A/B 先 unknown，同帧复读仍 unknown，独立下一帧才 confirmed，不是改写旧实验或一次新 demo。
- verify_fix.py：复现本地诊断与规则示例，不运行模型或物理动作；全量回归命令仍是现有 `.venv/bin/python -m pytest -q`。

限制：仍是任务特定颜色关联，不含通用检测器、长期失效证据的重定位或持久路线检索；原 stale／predicted 门控保留。本轮只证明离线数据链和恢复路径可用，不宣称实测任务成功率或记忆收益。
'''
(OUT / 'report.md').write_text(report, encoding='utf-8')
destination = OUT / 'verify_fix.py'
if Path(__file__).resolve() != destination:
    shutil.copyfile(__file__, destination)
print(json.dumps({'report': str(OUT / 'report.md'), 'old_diagnosis': old,
                  'task_scoring_unchanged': True, 'H0_rerun_required': False,
                  'synthetic_transitions': transitions}, ensure_ascii=False, indent=2))

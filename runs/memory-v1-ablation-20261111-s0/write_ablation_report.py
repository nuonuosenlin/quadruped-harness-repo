"""Summarize the completed, single-seed local experiment; no model calls."""
import json
from pathlib import Path

ROOT = Path('/home/nuonuosenlin/Agent-harness')
OUT = ROOT / 'runs/memory-v1-ablation-20261111-s0'
s = json.loads((OUT / 'ablation_summary.json').read_text())
h0, h2 = s['H0'], s['H2']
assert h0['status'] == 'completed'
assert h0['success'] or h2['status'] == 'completed'


def failure(arm):
    if arm.get('success'):
        return '独立 A/B 检查点、顺序、最终停止和 finish 均通过。'
    if arm.get('error'):
        return f"运行错误：{arm['error']}"
    e = arm.get('independent_evaluation') or {}
    if e.get('collision') or e.get('fallen'):
        return f"独立安全判定失败：collision={e.get('collision')}，fallen={e.get('fallen')}。"
    cp = arm.get('checkpoints') or {}
    if not cp.get('A', {}).get('passed'):
        return ('A 未通过独立检查点，不能把本轮失败归因为“到 A 后忘记 B”。'
                f" termination={arm['termination']}；A 原因={cp.get('A', {}).get('failure_reasons')}。")
    if not cp.get('B', {}).get('passed'):
        return f"A 已通过，但最终 B 未通过；B 原因={cp.get('B', {}).get('failure_reasons')}。仅凭评分不能断言原因就是遗忘。"
    return f"检查点通过但结束条件未通过：termination={arm['termination']}。"


text = '''# memory_ab_occluded_v1：正式任务与 seed 0 消融

本轮完成双目标顺序任务与正式独立评分，先离线验证，再按 H0→有条件 H2 的顺序运行。没有 push、访问或修改在线共享文档。密钥仅由既有模型适配器内部读取；本报告与日志不保存密钥内容，也不保存私有 reasoning 正文。

## 任务与评分

工具名称、参数、单回合一个调用及原有 6 回合 H0 历史不变。目标身份仅来自任务给定的“蓝球 A／绿方块 B”标签，未新增通用语义检测器，也未把目标真值坐标或通过标志放入模型观测。

独立 evaluator 在 backend 的真实停止确认后采样：A 需距离 0.82–1.18m、朝向误差≤0.25rad、速度<0.12m/s、绝对角速度<0.25rad/s、无碰撞跌倒。A 的合格停止证据保留为历史检查点；B 必须在 A 之后且在最终位置满足同一标准。提前访问 B 被忽略；访问 B 后离开也不能过。后来发生碰撞或跌倒会使整轮失败。runner 额外要求 finish 结束、最终 stop 成功且未超预算。

原 14 场景、quard-planar 套件和 H0 默认入口保持原行为，新 demo 仅通过显式 task ID 选择。此前 memory v1 的数据链与理想里程计设计问题未在本轮修改。

## 离线验证与冻结配置

- pytest：267 passed，15 skipped；新增 19 个顺序、边界、停止、安全、最终位置、finish 门控及真值隔离测试。
- `./scripts/run_deepseek.sh --list-tasks` 正常，memory_ab_occluded_v1 已为 supported。
- 模型：百炼 compatible，deepseek-v4.1-flash；seed 0；viewer=true。
- 每轮统一预算：120 次模型决策，2400s 墙钟，600s 仿真，history_turns=6，api_timeout=90s，max_output_tokens=8192，thinking enabled。
- 源码哈希与预算保存在 ablation_config.json，并由 collect_ablation.py 校验；两轮之间未改源码、提示或预算，没有重跑其它 seed 或任务。

## 运行结果

| 轮次 | 独立整轮成功 | A 通过 | B 通过 | 决策次数 | 输入 token | 输出 token | 合计 token | reasoning 返回 |
|---|---|---|---|---:|---:|---:|---:|---|
'''
for name, arm in [('H0', h0), ('H2', h2)]:
    if arm['status'] != 'completed':
        text += f'| {name} | 未运行（H0 通过，触发停止条件） | — | — | — | — | — | — | — |\n'
        continue
    u = arm.get('usage') or {}
    c = arm.get('checkpoints') or {}
    text += (f"| {name} | {arm['success']} | {c.get('A', {}).get('passed')} | {c.get('B', {}).get('passed')} | "
             f"{arm['model_calls']} | {u.get('prompt_tokens', 0)} | {u.get('completion_tokens', 0)} | {u.get('total_tokens', 0)} | "
             f"{arm.get('reasoning_responses', 0)}/{arm['model_calls']} 次，{arm.get('reasoning_characters', 0)} 字符计数 |\n")

for name, arm in [('H0', h0), ('H2', h2)]:
    if arm['status'] != 'completed':
        continue
    text += f"\n### {name}\n\n{failure(arm)}\n\n"
    text += f"终止：`{arm['termination']}`；工具分布：`{arm['tool_counts']}`；失败工具：`{arm['failed_tool_counts']}`。\n\n"
    text += f"[metrics.json]({arm['metrics_path']})。成绩来自正式独立评分，未以模型是否自述 finish 代替。\n"
    memory = arm.get('memory')
    if memory:
        text += (f"\n记忆文件：[memory.md]({memory['path']})。最终 revision={memory['written_revision']}，"
                 f"账本 {memory['ledger_entries']} 条，对象 {memory['object_count']} 个；"
                 f"{memory['state_packet_inputs']}/{arm['model_input_count']} 个模型输入含 memory_state，"
                 f"其中 {memory['inputs_with_objects']} 次有有效对象，最大快照滞后 {memory['max_snapshot_lag_steps']} 步。"
                 f"对象类别：`{memory['object_categories']}`。\n")
        if not arm['success']:
            if not memory['ledger_entries']:
                text += '\n记忆诊断：未形成有效写入账本。\n'
            elif not memory['state_packet_inputs']:
                text += '\n记忆诊断：有写入，但规划输入没有读到 memory_state。\n'
            else:
                text += ('\n记忆诊断：已写、已读，不能归类为“文件没写”或“规划没读”。'
                         '当前规则适配器只提供未分类追踪点／角点，没有蓝球 A、绿方块 B 的语义绑定或完整持久导航路线；'
                         '因此不能声称规划忽略了已经可用的 A/B 目标记忆。具体失败还应结合工具序列、有效对象次数和快照滞后判断。\n')

if h0['success']:
    text += '\n## 停止条件\n\nH0 已通过，按用户要求没有启动 H2。该 demo 本轮未能隔离外部记忆作用；不继续消耗第二轮 token。\n'
else:
    text += '\n## 停止条件\n\nH0 未通过，已按冻结配置完成唯一一轮 H2。至此停止，没有重复尝试、其它任务或其它 seed。单次实验只报告本次结果，不作统计显著性或泛化结论。\n'
text += '''
## 文件

- ablation_config.json：冻结配置及源码哈希。
- ablation_summary.json：机器可读汇总、完整检查点与记忆诊断。
- H0/、H2/：各自运行目录，含 manifest、events、frames、metrics、trajectory；H2 若运行还含 memory.md。
- collect_ablation.py：只读本地成果的汇总器；不读取凭据或调用模型。

本轮源码涉及 scenarios.py、backend.py、runner.py、新增 ordered_evaluation.py；测试涉及 test_memory_scene.py 与新增 test_ordered_evaluation.py。
'''
tmp = OUT / 'ablation_report.md.tmp'
tmp.write_text(text, encoding='utf-8')
tmp.replace(OUT / 'ablation_report.md')
print(OUT / 'ablation_report.md')

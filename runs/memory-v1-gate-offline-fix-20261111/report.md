# MEMORY_CONSTRAINT 与输出截断：离线诊断及修复

日期：2026-11-11；本地分支：`memory-v1`。本轮没有调用真实 API、读取真实密钥、运行 demo/消融、访问在线文档、修改共享文档或 push。使用已有 `.venv`，未安装依赖。

## 结论

修复了 H2 的计划传输契约：运动/finish 现在把结构化计划放进同一个工具调用的 `planning` 参数，适配器校验、提取后交给原有记忆门控，后端收到的原子工具参数不变。没有关闭前置条件门控，也没有自动替模型生成空前置条件计划。

正常规划状态包上限为 12000 个 JSON 字符，重试上限为 6000；只缩减 prompt 投影，完整 MD 及追加账本不裁剪。`finish_reason=length` 明确走最多一次修复重试，使用更小的状态包，仍计入原有调用/时间/token 预算。输出上限保持 8192，thinking 设置保持不变。

最终 `python -m pytest -q`：**315 passed、15 skipped**（原 295 项仍通过，新增 20 项）。`--list-tasks` 与 `git diff --check` 正常。任务、场景、独立评分语义不变，H0 不用重跑。

## 1. 门控拒绝：证据能确认什么

旧运行：`runs/memory-v1-h2-rerun-20261111-s0/H2/20261111-013742-api-memory_ab_occluded_v1-s0-9d3a30`。

首次拒绝发生在第 3 次决策（日志 turn=2）：

```json
{
  "tool_call": {"name": "turn", "arguments": {"yaw_rad": 0.55}},
  "input_active_plan_id": null,
  "input_objects": [
    {"object_id": "point-001", "state": "confirmed", "last_seen": 2, "confidence": 1.0},
    {"object_id": "task:B", "state": "confirmed", "last_seen": 2, "confidence": 0.95}
  ],
  "feedback": {
    "error_code": "MEMORY_CONSTRAINT",
    "constraint_feedback": "Invalid plan envelope or binding. Observe or submit a valid new plan."
  }
}
```

0.55 rad 本身满足原工具的 0.6 rad 上限。全部 26 次转向反馈都是上述格式/绑定错误；旧 MD 的 plans=[]，没有成功通过结构校验并建立的计划。

旧 [MemoryPlanningHarness.prepare](/home/nuonuosenlin/Agent-harness/go2_demo/memory_planning.py:205) 在任何对象前置条件检查之前，要求：

```python
required = call.name in {"move_relative", "turn", "finish"}
if not decision.assistant_content and required:
    raise ValueError("Motion/finish requires a structured plan and subgoal")
# 非空正文必须可解析为 JSON，且严格为：
# {plan, subgoal_id} 或 {plan_id, subgoal_id}
# 新 plan 必须通过 validate_plan；继续计划的 plan_id 必须匹配已接受计划。
```

原代码对 `Memory disproves a required precondition`、`Precondition requires fresh confirmed evidence`、`Snapshot publication lags...` 等证据失败会返回相应的专用文字；26 次实际返回的是其余异常使用的通用格式/绑定反馈。因此可确认拒绝发生在计划封装/绑定边界，不能把原因归为“task:B 置信度不足”或“转角超限”。

**不能恢复的部分**：旧事件日志只保存 calls/usage/推理长度，没有保存这 26 次响应的 assistant_content；第 45 次原始响应也不能补回前 44 次正文。无法进一步逐次区分“正文为空”“坏计划 JSON”“字段不合”“使用未知 plan_id”。本报告不把缺失信息推断为既成事实。`evidence.json.constraint_evidence` 保存了全部 26 次拒绝及对应输入状态。

能直接验证的设计缺口是：旧系统提示要求 assistant content 另带计划，但 H2 的 API 强制的是工具调用；解析器允许 content=None 且照常返回合法 turn。于是工具调用有效，计划没有受传输 schema 约束，后续门控再拒绝。离线测试可用 content=None 的合法转向确定复现这一路径。仅增加提示或放松对象置信度不能补齐这一契约。

## 2. 门控修复

- 新增 [memory_protocol.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory_protocol.py:35)：仅 H2 的 move_relative/turn/finish wire schema 增加必填 `planning` 对象。observe/track_point/get_geometry/stop/abort 保持原 schema。
- 更新 H2 系统提示，明确计划放在工具参数中，不要求同时输出正文。仍只输出一个原子工具调用；不是额外套一个规划 LLM 或额外执行动作。
- [APIModel](/home/nuonuosenlin/Agent-harness/go2_demo/models.py:436) 验证 planning 结构，保存为 Decision.planning_envelope，并在原工具参数校验、分发之前剥离该字段。缺失计划归类 `MISSING_PLANNING_ENVELOPE`，非法结构归类 `INVALID_PLANNING_ENVELOPE`，由原协议修复预算约束。不会降级成“默认允许探索”。
- 记忆门控读取这个结构化字段，继续检查计划 ID、子目标 ID、失效状态、测量值、对象确认、时效和快照滞后。兼容离线注入模型已有的 assistant_content 计划形式。
- 门控反馈新增稳定 `plan_diagnostic.phase/code`，区分 PLAN_MISSING、PLAN_INVALID_JSON、PLAN_ENVELOPE_FIELDS、PLAN_BINDING_MISMATCH、PRECONDITION_UNPROVEN、PRECONDITION_FALSE、SNAPSHOT_LAG、OBJECT_EXPIRED 等。恢复反馈会送入下一次上下文。
- [runner.py](/home/nuonuosenlin/Agent-harness/go2_demo/runner.py:226) 仅在 H2 记录已经解析并脱敏的 planning_envelope，以及正文是否存在/长度；工具反馈记录具体拒绝码。不会记录 reasoning 正文。这样未来能核对计划和拒绝条件。

明确的 wire 变化示例：

```json
{
  "yaw_rad": 0.3,
  "planning": {
    "plan": {
      "subgoals": [{"subgoal_id": "scan", "description": "safe scan", "preconditions": [], "completion": []}],
      "branches": [], "recovery": "stop"
    },
    "subgoal_id": "scan"
  }
}
```

通过规则门控后，后端仍仅收到原来的 yaw_rad 等参数。新计划由 Harness 分配 plan_id，继续执行必须使用该 ID。空前置条件探索是原本已允许的路径，模型必须显式给出合法计划；未知或过时对象不能作为强前置条件使用。

## 3. 输入增长与截断诊断

对旧 45 次 model_input 按实际请求使用的紧凑 JSON 编码计算字符数（不假装是 token 估算）：

| 决策 | 旧 task+memory_state 字符数 |
|---|---:|
| 1 | 6369 |
| 3 | 8426 |
| 21 | 13202 |
| 38 | 16579 |
| 45 | 13940 |

峰值为 17950 字符，45 次输入中出现 12 次下降，**不是每轮单调增长**。第 45 次 memory_state 本身为 13641 字符，其中 world 为 11449；world.public_context 5721、world.current_observation 3191、world.measurements 1979。public_context 重复存了一份观察；重复选点积累相同几何的 point ID；事件和对象字段也有重复。完整逐轮证据在 `input_growth_before.json` 和 `evidence.json`。

原始第 45 次响应可解析为 JSON，finish_reason=length，content 为空，未产生 tool_calls；8192 completion token 全为 reasoning token。它证明模型输出预算耗尽，不能单独证明输入膨胀是唯一原因。反复的计划门控失败、输出契约不匹配也可能影响推理；离线不能作更强因果断言。

## 4. 有界状态投影与 length 重试

新增 [memory_context.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory_context.py:37)，在规划入口及 API 请求构造边界应用规则投影：

- 顶层继续使用 world / pose / objects / active_beliefs / invalidated / events / topology / confidence_thresholds。
- 保留任务标签、当前姿态、当前有效/短期预测对象及证据、当前任务进度、必要测量、最新反馈和少量最近事件。任务目标优先于普通地标。
- 删除重复 world.public_context；当前观测仅保留有界候选、当前有效追踪几何、传感器标定与评分公开标准。相同像素和几何的重复追踪点在 prompt 中合并。通用的当前帧角点候选仍保留，避免破坏无任务标签时的选点能力。
- 对象证据 ID 仅传最近两个；旧/未知/失效对象不作为有效对象提供；已过新鲜期的 confirmed 防御性降为 predicted，不抬高置信度；旧测量不作为当前测量发送。
- 正常状态包最多 8 个对象/子目标、4 条事件；重试缩至 4 个对象/子目标、2 条事件，并进一步缩减追踪点和候选。通过移除完整记录实现序列化状态包 12000/6000 字符硬上限，不切断 JSON；保留省略标记，明确省略不代表完成或空闲空间。
- MD、账本和规则实际验证使用的完整快照完全不裁剪。门控从完整 MD 检查前置条件，摘要中的省略不能削弱门控。

最终版本对旧第 45 次输入的重放结果：

| 范围（JSON 字符数） | 修复前 | 正常投影 | 重试投影 |
|---|---:|---:|---:|
| task + memory_state | 13940 | 4163 | 3621 |
| memory_state | 13641 | 3864 | 3322 |
| messages + tools（含提示与 H2 新 schema） | 21325 | 15710 | 15545 |

重试总 messages+tools 还包含额外的修复提示。旧 45 次输入在最终规则投影下的峰值为正常 7884、重试 5673 个 task+memory_state 字符。字符数不等于真实模型 token；本轮没有调用 API 来测新 token。

原通用协议重试已经把 length 归为 `TRUNCATED_RESPONSE`，但上轮专用 launcher 为满足“协议错误即停”把 max_requests 固定为 1，所以没有重试。本次明确让包括 length 在内的协议修复使用更小的状态投影，并补齐这一子情况的回归测试；正常入口最多 2 个请求，预算只剩 1 个槽位或时间耗尽时不会重试，第二次仍失败就终止。不应复用旧运行目录里强制禁用重试的 launcher 来验证默认修复入口。

## 5. 离线验证

最终命令与结果：

```text
.venv/bin/python -m pytest -q
315 passed, 15 skipped

./scripts/run_deepseek.sh --list-tasks
正常，memory_ab_occluded_v1 仍为 supported。

git diff --check
通过。
```

新增 20 个离线用例覆盖：正文为空但带结构化 wire 计划可成功转向；后端不收到 planning 字段；已分配计划 ID 可继续；未知对象强前置条件仍拒绝；格式/绑定诊断；缺失/非法 wire 计划不放行；正常/重试状态包上限与去重；陈旧证据/测量过滤；保留当前通用角点；length 一次重试、失败停止、剩余调用和共享时间预算；H0 请求工具 schema 和 auto 选择不变。

此外 `verify_fix.py` 把上轮完整原始响应作为 MockTransport 的第一份响应，再返回一份本地构造的合法计划响应：实际进入现有 API 解析器，两次请求合计已知 total_tokens=14512，错误响应的 token 也被计入；第二次得到的计划通过记忆门控。这里的“请求”都是内存 MockTransport 调用，不是网络 API。脚本验证原始响应 SHA256 不变，不打印其 reasoning 正文，不读取密钥。

离线重放只能证明协议、门控与预算路径可达和规则正确；不能证明真实模型下一轮一定按 schema 输出，或 H2 导航任务已经通过。

## 6. 文件与 H0 可比性

本轮修改/新增产品文件：

- `go2_demo/memory_protocol.py`（新增）：H2 wire schema 和结构校验。
- `go2_demo/memory_context.py`（新增）：规则投影与硬上限。
- `go2_demo/memory_planning.py`：H2 提示、结构化计划消费、具体拒绝诊断、上下文入口。
- `go2_demo/models.py`：H2 schema 包装、提取计划、缩小重试输入。
- `go2_demo/types.py`：Decision.planning_envelope。
- `go2_demo/runner.py`：仅 H2 的计划诊断日志。
- `tests/test_memory_gate_fix.py`（新增）：20 项离线用例。
- `tests/test_memory.py`：原上下文测试改为验证有界投影和原隔离目标，未删除测试。

`before_hashes.json` 与 `evidence.json.after_hashes` 记录修复前后源码 SHA256。scenarios.py、backend.py、harness.py、ordered_evaluation.py、__main__.py、memory_perception.py、memory.py 均逐文件哈希一致。未改任务指令、布局、评分顺序、距离/朝向/停止/finish/碰撞规则，没有引入新的 GT 决策字段。

**H2 传输层工具 schema 新增 planning；后端工具语义不变，H0 发送的原工具定义和单请求 auto 路径不变。任务/评分语义未改，历史 H0 继续可作对照，不需要重跑。**

复现：在仓库下执行 `.venv/bin/python runs/memory-v1-gate-offline-fix-20261111/verify_fix.py`。此脚本只读旧运行数据并生成本地重放证据；重复执行使用新的 replay/memory-N.md，避免覆盖追加账本。

本目录产物：`report.md`、`evidence.json`、`before_hashes.json`、`input_growth_before.json`、`verify_fix.py`、`pytest.txt`、`list_tasks.txt`、`replay/`。旧 H0/H2 运行记录和原始响应均未修改。已停在离线修复与验证阶段。

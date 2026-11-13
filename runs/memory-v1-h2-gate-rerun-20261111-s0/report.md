# H2 门控修复后单轮重跑（2026-11-11，seed 0）

结论：**H2 失败，A/B 均未通过，120 次调用预算耗尽，未调用 finish。** 第 2 次决策开始成功转向，89 次转向全部成功，但全程未调用 move_relative。没有门控拒绝、工具调用协议错误或 length 截断，因而没有重试。主要运行表现是规划探索停滞，没有进入回找 B 阶段，不能证明记忆对回找 B 起到了作用。

## 独立评分与用量

唯一进入模型决策循环的本轮目录：

`/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f`

| 指标 | 本轮 H2 | 历史 H0（读取旧记录，未重跑） |
|---|---:|---:|
| A 通过 | 否 | 是，第 89 次决策 |
| B 通过 | 否 | 否 |
| success | false | false |
| termination | budget_exhausted | budget_exhausted |
| 决策调用次数 | 120 | 120 |
| 实际模型请求次数 | 120 | 120 |
| 协议重试请求数 | 0 | 0 |
| 输入 token | 552,887 | 1,867,189 |
| 输出 token | 66,105 | 117,884 |
| 总 token | 618,992 | 1,985,073 |
| 非空 reasoning_content 响应 | 119/120 | 120/120 |
| reasoning_content 字符总数 | 221,831 | 373,249 |
| finish | 未调用 | 未调用 |
| 最终距 B | 1.939618 m | 4.090894 m |

第 9 次响应的日志为 reasoning_present=false、reasoning_chars=0；其余 119 次非空。正常响应只记录该统计，无法区分第 9 次是未返回、null 还是空字符串；请求仍使用 thinking enabled。

H2 墙钟 688.990621 秒、仿真 235.720000 秒，均未到时间上限，耗尽的是 120 次模型请求预算。两个 checkpoint 按 metrics 的独立评分读取：

- A passed=false。评分保留的未通过停止见证距离 6.339696 m、朝向误差 0.345206 rad，失败码 DISTANCE_OUT_OF_RANGE / HEADING_OUT_OF_RANGE。这是 A 的历史见证，不是最终姿态距离。
- B passed=false、eligible=false。最终距离 1.939618 m、朝向误差 0.087533 rad，失败码 DISTANCE_OUT_OF_RANGE / A_NOT_CONFIRMED_BEFORE_B。
- 无碰撞、无跌倒；最终清理 stop 成功。清理 stop 不是模型的 finish，也不会令任务成功。

H0 到达过 A，本轮 H2 没有到达 A；较低总 token 不能解释为记忆提高了导航效率。

## 三个问题

### 1. 规划器是否动起来了，何时首次移动？

若“运动”包含旋转，第 **2 次决策**首次 turn 成功；第 1 次是 track_point 成功。若“移动”指平移导航，**全程没有 move_relative 请求**，不存在首次平移决策。

完整工具计数：turn 89、track_point 20、observe 10、get_geometry 1；全部返回 succeeded。metrics.motion_calls=89，均为转向。请求转角累计 41.55 rad（仅为指令之和，不当作实测转角）；机器人在执行转向时仍有少量步态漂移，不能把“没有平移指令”写成“机身绝对没有平移”。

因此本轮验证了 planning 参数链路与门控不再阻挡合法转向，但没有验证规划器能完成向 A 移动、绕遮挡和向 B 回航。

### 2. 记忆在回找 B 时有没有起到作用？

**无法验证回找作用：A 从未通过，B 回找阶段没有开始。** 不能把记忆文档中出现 B 等同于利用记忆完成导航。

写入与读取有明确证据：

- [memory.md 的 B 对象条目](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md:414)：object_id=task:B、task_label=B、label_description=绿方块、source=task_label_rgbd_tracking；最终 state=confirmed、confidence=0.95、last_seen=120，episode_start 位置为 [1.7288048201410928, 0.38353183834067883]。
- [账本 e000005](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md:2276)：第 1 步记录 B 的初始观测位置 [1.7354,0.7421]。单帧记录不等于当时已经 confirmed。
- [e000188](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md:4523) 与 [e000200](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md:4698) 支持了第 42 次规划输入中的 confirmed B；当次读到的位置为 [1.7353858588714828,0.7419368256821057]。
- 有效 B 对象进入规划输入的决策为 42–46、61–66、101–104，共 **15 次**。最后 MD 的 confirmed 条目是在第 120 次工具执行后更新的，不能据此说第 120 次规划输入已经读到了最终确认状态。
- A 的候选输入次数为 0，MD 没有 task:A 对象。B 身份来自任务给定标签与 RGB-D/有效追踪点关联，不是通用语义检测器。

也有记忆质量问题，不能把“写读通了”说成“记忆完全正确”：B 位置观测发生 6 次超过阈值的跳变，被账本规则记录为 target_relocated。例如 e000035 在 step 6 将位置从 [1.7393738185676924,0.382003556520252] 标记到 [2.4023327436808373,1.0034175641810097]。这代表规则收到不一致位置证据，不代表固定场景里的 B 实际移动。全部相关条目保存在 evidence.json.target_evidence_ledger。

### 3. 是否再次触发协议错误或 length 截断，重试是否生效？

- 协议错误 **0 次**。
- length 截断 **0 次**。
- 重试 **0 次**，没有真实请求需要修复，不能声称本轮实测验证了“重试救回”。
- 使用默认 `python -m go2_demo` 与默认 APIModel.decide，最多两个请求/决策；没有复用旧 max_requests=1 launcher。监控不修改请求/重试参数。
- 本轮未发生协议错误，所以没有错误原始响应需要存档，也没有遗漏已发生的错误响应。运行前 4 项离线监控测试覆盖：完整捕获单次错误且默认重试正常、两份失败响应都保存且无第三次请求、连续门控拒绝及时停止、GLFW 子进程不继承监控激活标记。

## 失败原因：主要是规划探索停滞，另有记忆证据不稳定

执行层返回的 120 份工具反馈全部成功，独立评分无碰撞/跌倒；本轮没有 MEMORY_CONSTRAINT/MEMORY_NO_PROGRESS，也没有模型解析失败。因此没有证据把失败归于门控拒绝或物理执行失败。

规划侧有直接停滞证据：全程 89 次转向、0 次平移，全部输入中 A 候选为 0，始终没向 A 建立有效运动进展。[memory.md 最终 plan-0004](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md:2217) 中：

```json
{
  "scan_A": {
    "description": "turn conservatively to search for blue ball A",
    "preconditions": [], "completion": [], "status": "进行中"
  },
  "approach_A": {
    "description": "stand 1.0 m from A facing it, then stop",
    "preconditions": [{"object_id": "task:A"}],
    "completion": [], "status": "待做"
  },
  "recovery": "stop, observe current view, then resume conservative scanning or abort if no target visible"
}
```

这个子目标组合持续等待 A 出现，却没有选择移动探索来改变遮挡关系。前 3 个计划也都是同类 scan_A。MD 有 30 条 replan_required 事件、44 条 target_state_changed，skill_stuck 为 0；并未形成有效的“扫描无进展→移动绕遮挡”恢复。B 的不一致位置证据可能增加重规划噪声；仅凭这一轮不能判定它是探索停滞的唯一原因，也不能排除当前结构化感知缺少有用通行空间信息的影响。

归类：**主要是规划/探索未推进；记忆有位置证据质量和进度监督方面的问题；没有观察到工具物理执行失败。** 没有达到 A，因此本轮也不能用来隔离外部记忆对 B 回找的因果作用。

## 条件、启动记录与范围

- 分支 memory-v1；任务 memory_ab_occluded_v1；seed 0；memory-v1 与 viewer 均开启。
- provider compatible；MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1；MODEL_NAME=deepseek-v4.1-flash。
- 预算与旧 H0 一致：max_model_calls=120、max_wall_seconds=2400、max_sim_seconds=600、history_turns=6、api_timeout=90、max_output_tokens=8192、thinking enabled。重试若发生，仍计入这些预算。
- manifest 中任务指令、seed、模型、预算、评分、资产锁及 API 输出/超时/thinking 参数与旧 H0 逐项一致，比较结果见 evidence.json.H0_condition_comparison。
- 本轮产品源码未修改；冻结与结束 SHA256 一致。只在本运行目录保存监控、测试、配置、日志、离线收集和报告。
- 连续门控拒绝提前停止阈值为相邻两次决策；实际拒绝 0 次，未触发该停止条件。

透明记录一次模型请求之前的启动失败：首次启动时，运行监控激活环境标记被 GLFW 的 Python 库探测子进程继承，触发启动保护，导致 GLFW 初始化失败。该次尚未进入 run_episode，没有 events.jsonl，也没有 HTTP 请求或 token 消耗；记录在 startup_failure.json、console-startup-failed.log 和 H2/20261111-083814-api-memory_ab_occluded_v1-s0-87fc41/metrics.json。修正的仅是运行目录内 sitecustomize.py 的标记继承范围，然后进入上面列出的唯一真实 API episode；没有额外 H0、seed 或第二轮模型实验。

密钥仅由默认客户端读取用户指定文件鉴权，未打印或记录内容。未 push，未访问在线文档，未修改共享文档，未安装依赖，未做后续修复或额外任务。

## 产物与离线复现

- [本轮 metrics.json](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/metrics.json)
- [本轮 memory.md](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-gate-rerun-20261111-s0/H2/20261111-083939-api-memory_ab_occluded_v1-s0-76696f/memory.md)
- `evidence.json`：评分、真实工具计数、目标读入决策、MD 目标条目/账本、计划、协议统计、源码和 H0 配置对比。
- `collect.py`：只读既有运行结果的离线证据收集脚本，可在仓库下执行 `.venv/bin/python runs/memory-v1-h2-gate-rerun-20261111-s0/collect.py`，不会调用 API 或读取密钥。
- `instrumentation/`：仅本轮使用的监控及 4 项离线测试，不是产品入口替代，也没有覆写 APIModel.decide 或 CLI 模型工厂。
- `config.json`、`started.json`、`console.log`、`startup_failure.json` 等保存本轮边界和启动审计。不要再启动本轮命令。

已停止；没有继续其他任务、H0、其他 seed 或第二轮 API 实验。

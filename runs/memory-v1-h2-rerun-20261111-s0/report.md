# 修复后 H2 单轮重跑结果（2026-11-11，seed 0）

结论：H2 失败，已按停止条件在第 45 次响应发生工具协议错误时立即终止；没有重试或再跑其他轮次。A、B 均未通过，没有调用 finish。对象写入与读取已得到实测验证；主要运行阻塞发生在规划与计划门控之间，运动工具未获执行，随后模型输出达到上限而终止。

## 条件与范围

- 分支 `memory-v1`；任务 `memory_ab_occluded_v1`；`--memory-v1 --viewer`；seed 0。
- provider compatible，模型 `deepseek-v4.1-flash`，端点 `https://dashscope.aliyuncs.com/compatible-mode/v1`。
- 使用现有 `.venv`，未安装依赖。密钥仅由运行客户端从用户指定文件加载，未打印或写入日志。
- 决策/API 请求预算 120，墙钟 2400 秒，仿真 600 秒，history_turns 6，API timeout 90 秒，max_output_tokens 8192，thinking enabled。
- 与历史 H0 的 manifest 逐项核对：任务指令、task_id、seed、模型、预算、依赖、评分配置、资产锁一致。H2 上下文按既有实现只传当前结构化记忆，H0 保留六轮历史；这是既有两种模式的区别。
- 用户要求协议错误立即停止，因此本轮专用 launcher 将最多一次修复请求关闭（每次决策最多一个 API 请求）。产品源码、提示词、场景、工具和评分均未修改。启动与结束源码 SHA256 一致。
- 本轮只发起一个真实 H2 episode；没有跑 H0，没有额外 seed，没有 push，没有访问在线文档或修改共享文档。

## 独立评分与用量

| 指标 | 本轮 H2 | 历史 H0（仅读旧结果） |
|---|---:|---:|
| A 通过 | 否 | 是，第 89 次决策 |
| B 通过 | 否 | 否 |
| 整轮 success | false | false |
| termination | model_error | budget_exhausted |
| 决策/API 请求次数 | 45 | 120 |
| 成功解析的模型响应 | 44 | 120 |
| 协议重试 | 0 | 0 |
| 输入 token | 249,016 | 1,867,189 |
| 输出 token | 142,352 | 117,884 |
| 总 token | 391,368 | 1,985,073 |
| reasoning_content 非空响应 | 45/45 | 120/120 |
| reasoning_content 字符总数 | 569,564 | 373,249 |
| finish | 未调用 | 未调用 |
| 最终距 B | 1.888279 m | 4.090894 m |

H2 的 token 与 reasoning 统计包含第 45 次错误响应。两轮都失败且 H2 提前终止，不能用较低总 token 宣称导航效率提升。

H2 A：最终距离 6.393433 m，朝向误差 0.025552 rad，因距离不合格未通过。H2 B：最终距离 1.888279 m，朝向误差 0.294167 rad，距离与朝向都不合格，且 A 尚未通过，B 无计分资格。最终清理 stop 成功，无碰撞/跌倒；清理 stop 不等于模型调用 finish，也不能使任务通过。墙钟 787.326501 秒；仿真只在最终清理阶段前进 0.6 秒。

## 三个问题

### 1. 有效对象是否大于 0，何时首次出现？

是。第 1 次决策 track_point 成功，在 frame-00001 追踪绿方块候选；第 2 次 observe 得到独立 frame-00002，记忆在 step 2 确认。第 3 次决策输入首次有两个有效对象：未分类地标 `point-001` 和语义目标 `task:B`，均为 confirmed。A 没有有效语义对象条目。

`task:B` 被写入模型输入的决策编号为 3–6、21–26、38–43，共 16 次。全部 45 次模型输入都有 memory_state；只有目标条目存在且符合时效规则时，才进入有效对象列表。

### 2. 规划器是否动起来了？

第 1 次决策首次选点；第 3 次首次尝试 turn。但 26 次 turn 全部返回 `MEMORY_CONSTRAINT`，反馈均为 `Invalid plan envelope or binding. Observe or submit a valid new plan.`。没有任何 move_relative 请求，也没有成功的 turn。工具结果总数 44：track_point 8、observe 10、turn 26；metrics.motion_calls=0，MD 的 plans=[]。

因此“已能选点”成立，“已能运动”不成立。失败位于规划输出与计划门控的衔接，不是机器人步态/碰撞等物理执行失败。现有事件日志没有保存这 26 个正常工具响应的 assistant_content，而门控反馈将具体格式异常归并成统一字符串，无法仅凭本轮日志进一步断言是缺 content、坏计划 JSON、字段不符还是绑定无效；不得把推测当作已确认原因。

### 3. 回找 B 时记忆有无起作用？

本轮没有到达 A，未进入回找 B 阶段，无法验证记忆对回航导航的实际作用，也不能声称 H2 已利用记忆完成回找。

但写入和读取链路已证实。以下为 memory.md 的真实条目：

```json
{
  "object_id": "task:B",
  "category": "task_target",
  "task_label": "B",
  "label_description": "绿方块",
  "pose": {"frame": "episode_start", "position_m": [1.7354, 0.7421]},
  "source": "task_label_rgbd_tracking",
  "confidence": 0.95
}
```

- 账本 `e000005`：step 1、frame-00001 的绿方块观测。
- 账本 `e000013`：step 2、frame-00002 的独立观测；第 3 次规划输入读到 confirmed、evidence_ids=[e000005,e000013]。
- 身份来自任务给定标签与当前唯一颜色组件，经有效追踪点关联；不是通用语义检测器。camera_pose 来自 RGB-D 深度与内参，二维 episode_start 位置沿用公开的理想仿真里程计，并显式记录 provenance；`motion_delta_used=false`，未将 measured 仿真位移伪装成非真值导航测量。
- 最终 `task:B` 状态为 unknown、last_seen=37，旧证据仍保留；step 44 距最近验证已七步，不再作为有效对象送入第 45 次输入。账本共 643 条，只有 B 有任务目标条目，A 无条目。

## 第 45 次协议错误与完整原始响应

确认不是坏 JSON 或错误工具名：完整 HTTP 响应体可解析为 JSON，choices 数量为 1，`finish_reason="length"`，message.content 为空，message 没有 tool_calls。该响应输出 8192 token，provider 明细为 reasoning_tokens=8192、text_tokens=0；reasoning_content 非空、34352 字符。模型在输出工具调用前耗尽输出上限。

原始响应完整保存在本目录 `protocol_error/response.raw`，共 **35789 字节**；原始与落盘 SHA256 相同：

`9467272783801588e779f3f535e7c586b963d0ce06cf646cc1e20e2cac516736`

未发生凭据回显，未作任何内容删改或截断。客户端禁止执行此错误响应，并立即结束；没有发起自动重试。`protocol_error/capture.json` 保存捕获元数据，evidence.json 保存不含推理正文的响应结构诊断。

## 文件与复核

- [本轮 metrics.json](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-rerun-20261111-s0/H2/20261111-013742-api-memory_ab_occluded_v1-s0-9d3a30/metrics.json)
- [本轮 memory.md](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-rerun-20261111-s0/H2/20261111-013742-api-memory_ab_occluded_v1-s0-9d3a30/memory.md)
- [完整错误响应](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-rerun-20261111-s0/protocol_error/response.raw)
- [错误响应捕获元数据](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-rerun-20261111-s0/protocol_error/capture.json)
- `evidence.json`、`collect.py`：离线结果收集与原始记录引用。collect.py 只读现有结果，可以在仓库下运行 `.venv/bin/python runs/memory-v1-h2-rerun-20261111-s0/collect.py` 重建证据，不发起 API。
- `config.json`、`started.json`、`console.log`、`launch.py`：冻结配置、单次启动标记、控制台记录、仅本轮的协议错误捕获入口。不要重新运行 launch.py；重复启动保护也会拒绝已有 started.json。
- 启动前已有测试 295 passed、15 skipped；另外 3 项离线 mock 测试验证完整响应捕获、凭据脱敏和首次协议错误即停。`--list-tasks` 正常。产品文件无新改动，未修改任务或评分语义，历史 H0 继续有效。

已停止；没有继续其他任务、H0 或其他 seed。

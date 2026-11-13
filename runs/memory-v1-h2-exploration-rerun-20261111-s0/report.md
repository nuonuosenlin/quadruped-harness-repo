# H2 探索修复后单轮重跑（2026-11-11，seed 0）

结论：**H2 失败，A/B 均未通过，120 次调用预算耗尽，未调用 finish。** “只转不走”已改变：第 9 次首次 move_relative，全程 25 次平移与 44 次转向均成功，但没有建立 A 的观测或有效导航进展。search_stalled 没有触发，不能声称本轮验证了规划器对该事件的响应。没有门控拒绝、协议错误或 length 截断，也没有重试。

## 运行条件与范围

- 唯一真实 API episode：`runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417`。
- 本地分支 memory-v1；任务 memory_ab_occluded_v1；seed 0；启用 --memory-v1、--viewer。
- 默认 `.venv/bin/python -m go2_demo` 入口，provider compatible，模型 deepseek-v4.1-flash，端点 https://dashscope.aliyuncs.com/compatible-mode/v1。
- 与旧 H0 相同：max_model_calls=120、max_wall_seconds=2400、max_sim_seconds=600、history_turns=6、api_timeout=90、max_output_tokens=8192、thinking enabled。默认最多两个请求/决策，重试若发生仍计入这些预算。
- 未复用 max_requests=1 launcher。只附加运行目录内的完整错误响应存档与连续两次门控拒绝停止监控，不改 APIModel.decide、CLI 工厂或重试参数。
- 本轮产品源码未改，启动冻结哈希与结束哈希一致，且与探索离线修复的 after_hashes 一致。未跑 H0、其他 seed 或第二轮模型实验；没有启动故障或额外 API 尝试。
- 密钥只由默认客户端读取用户指定文件鉴权，未打印或记录其内容。未 push、未改共享文档、未访问在线文档，未安装依赖。

## metrics.json 与历史 H0 对照

| 指标 | 本轮 H2 | 历史 H0（只读旧记录） |
|---|---:|---:|
| A passed | false | true，第 89 次决策 |
| B passed | false | false |
| success | false | false |
| termination | budget_exhausted | budget_exhausted |
| decision_calls | 120 | 120 |
| model_calls（实际请求） | 120 | 120 |
| protocol_retries | 0 | 0 |
| 输入 token | 615,167 | 1,867,189 |
| 输出 token | 123,949 | 117,884 |
| 总 token | 739,116 | 1,985,073 |
| 非空 reasoning_content | 120/120 | 120/120 |
| reasoning_content 字符总数 | 462,406 | 373,249 |
| finish | 未调用 | 未调用 |
| 最终距 B | 3.656421 m | 4.090894 m |

H2 墙钟 916.923376 秒、仿真 177.960000 秒，未到时间上限，耗尽的是模型调用预算。

独立评分：

- A 未到达；没有成功 checkpoint。A 评分记录保留的是一份未通过停止见证（距离 6.386702 m、朝向误差 1.015797 rad），不是最终姿态距离。失败码 DISTANCE_OUT_OF_RANGE / HEADING_OUT_OF_RANGE。
- B 未通过、eligible=false；最终距离 3.656421 m、朝向误差 2.933941 rad。失败码 DISTANCE_OUT_OF_RANGE / HEADING_OUT_OF_RANGE / A_NOT_CONFIRMED_BEFORE_B。
- 无碰撞、无跌倒，最终清理 stop 成功。清理 stop 不等于模型调用 finish。

模型自述和 plan 中的 approach_A 描述没有被当作通过证据。H0 到达过 A，本轮 H2 没有；不能把较低 token 直接解释成记忆提高了导航效率。

## 四个问题

### 1. 这次动起来了吗？首次 move_relative 是哪次？

**第 9 次决策首次调用 move_relative，且成功。** 请求参数 forward_m=0.3、lateral_m=0.0；计划 plan-0002 / explore_A_translate，preconditions=[]。该步没有依赖未确认的 task:A，也没有被门控拒绝。

其显式计划描述为：

> short forward translation along clear floor (tracked point at ~1.18 m ahead-right) to gain parallax for locating blue ball A

这是模型的几何判断文本，不把它当作独立证明整条通道安全。工具成功与无碰撞由实际执行反馈和评分另行核对。

完整工具计数：move_relative 25、turn 44、track_point 40、observe 6、get_geometry 5，全部 succeeded。相比前一轮 89 次转向、0 次平移，这一轮已经能执行探索平移；仍未实现 A→B 导航。

### 2. search_stalled 触发了吗？规划器回应了吗？

**0 次。** MD 无 search_stalled 账本，无 stalled=true 的规划输入，也无对应 skill_stuck 搜索事件。规划输入中的最高计数是 4，未到阈值 6。

首次平移在第 9 次发生，当时此前只有 4 次成功转向；之后的成功平移又持续重置该计数。因此不存在“第几次读到 search_stalled 后改为移动”的真实样本。

可以确认模型在触发阈值前采用了合法探索计划：plan-0001 已有 explore_A（change viewpoint with short safe translation if scanning stalls）；第 9 次以 plan-0002 实际执行了平移。**这证明移动计划路径已被真实调用，不证明本轮验证了停滞事件响应或其因果效果。**

本轮也暴露出规则范围的限制：成功平移足以重置扫描计数，但不一定代表搜索覆盖增加或接近 A。这条规则针对连续转向，不检测“转向与短移交替却没有新目标”的整个搜索策略停滞。

### 3. 是否到达 A？

**没有。** 全部规划输入中 A 候选次数为 0，memory.md 没有 task:A 对象，独立 A checkpoint 从未通过。

公开累计里程计的结束后摘要显示，工具结果时刻的活动范围约为：x ∈ [-1.999,0.015] m、y ∈ [0,1.832] m，距起点最远约 2.430 m。说明发生了真实局部位移，但没有形成找到 A 的有效覆盖。该数据来源是原有公开理想仿真里程计，仅用于本次结束后的诊断；没有新增里程计来源、将它冒充非真值测量，或用其干预本轮决策。

### 4. 记忆在回找 B 时有没有起到作用？

**无法验证：A 未通过，没有进入 A 后回找 B 的阶段。** B 曾被记住、曾有效读入，不能等同于利用记忆完成回找。

具体证据来自 [本轮 memory.md](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417/memory.md)：

- [e000005](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417/memory.md:3932)：第 1 步 B 的初始观测位置 [1.7354,0.7421]，source=task_label_rgbd_tracking。
- e000018：第 3 步独立帧观测。第 4 次规划输入读到 confirmed 的 task:B，evidence_ids=[e000005,e000018]，位置 [1.8071006378272325,0.4154377771249777]。
- 有效 B 进入输入的决策为 4–9、39–42、102–108，共 **17 次**。A 之后的 B 读取次数为 0，因为没有 A checkpoint。
- [最终 B 对象条目](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417/memory.md:405)：task_label=B、label_description=绿方块，保留位置 [1.7337469027696255,0.6316866157030975]，last_seen=102，最终 state=stale。旧证据保留，但不得作为强前置条件。

该身份来自任务给定标签、当前 RGB-D 颜色候选与有效追踪点关联，不是通用语义检测器；位置沿用既有公开里程计参考，measurement_provenance.motion_delta_used=false。本轮 B 账本仍有 2 次 target_relocated；不能把已接通的写读链路说成定位证据完全稳定。

## 协议错误、截断与提前停止

- ModelProtocolError：0 次。
- finish_reason=length：0 次。
- 修复重试：0 次，故本轮无法验证真实重试救回效果。
- MEMORY_CONSTRAINT / MEMORY_NO_PROGRESS：0 次，未触发连续拒绝停止。
- 所有 120 份工具反馈成功，未发生需原始响应存档的协议错误；本轮没有错误原始响应可保存，也没有已发生但遗漏的错误响应。

默认最多两次请求的逻辑保留；启动前 4 项离线监控测试通过，验证捕获完整错误体、保留默认重试、两次失败均存档及连续拒绝停止。它们使用 MockTransport，不计作真实 API 实验。

## 失败归类与结论边界

本轮的主要表现是**规划/探索策略没有形成有效目标覆盖**：确实移动了，却始终没有 A 的候选或对象证据；预算耗尽。不是门控拦截，也没有观察到物理动作失败、碰撞、跌倒或模型解析错误。

记忆侧的搜索监督也有明确盲区：移动工具返回成功会清零搜索计数，因此“转向—短移—继续搜索”可以长期不触发 search_stalled，即使没有发现新的任务目标。最后的 B 记录又已 stale。仅这一轮不能进一步区分搜索路线选择、结构化感知信息不足与长期记忆读取策略各自的因果贡献，更不能宣称已证明外部记忆对 B 导航有益。

本轮只检验既有修复，没有现场改提示、改规则、补地图、加入 GT 导航或追加实验。原 H0 继续作为对照，无需重跑。

## 产物

- [metrics.json](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417/metrics.json)
- [memory.md](/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-exploration-rerun-20261111-s0/H2/20261111-133025-api-memory_ab_occluded_v1-s0-bab417/memory.md)
- evidence.json：评分、停滞事件/输入、平移结果、目标读入、MD 目标条目、显式计划、公开里程计路线摘要、源码哈希及 H0 配置对比。
- collect.py：只读本地结果，可用 `.venv/bin/python runs/memory-v1-h2-exploration-rerun-20261111-s0/collect.py` 重建证据，不调用 API、不读密钥。
- config.json、started.json、console.log、summary.txt、instrumentation/：冻结配置、单次启动、控制台和运行监控审计。

已停止，没有继续其他任务、H0 或其他 seed。

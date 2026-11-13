# H2：临时实验边界门控后单轮重跑

2026-11-11，本地 memory-v1。**A/B 均未通过；120 次决策/请求预算耗尽，未 finish；无跌倒、无碰撞，最终停止确认成功。** 第 114 次发生唯一一次 BOUNDARY_BLOCKED；第 115 次规划器成功向内撤离，没有形成拒绝循环。

**这是等待按组会决定替换的临时本地实验，不是最终设计。门控使用仿真当前底盘位姿 GT 与场景边界作安全联锁，不是非真值悬崖感知或导航测量。任何本轮结论都须保留这一真值来源说明。** 本任务没有替组会确定最终方案。

## 运行与可比性

唯一 episode：`/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-boundary-gate-rerun-20261111-s0/H2/20261111-204056-api-memory_ab_occluded_v1-s0-ceafa1`。

默认 `.venv/bin/python -m go2_demo`；provider compatible，MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1，MODEL_NAME=deepseek-v4.1-flash，thinking enabled；--task memory_ab_occluded_v1、--memory-v1、--seed 0、--viewer。

与历史 H0 相同：max_model_calls=120、max_wall_seconds=2400、max_sim_seconds=600、history_turns=6、api_timeout=90、max_output_tokens=8192。默认每次决策最多 2 个请求，重试共享预算；没有调用旧的 max_requests=1 launcher。实际没有重试，每次决策恰好一个请求。

密钥仅由默认客户端读取 ~/deepseekapi.txt 鉴权，没有打印、记录内容。未 push、未访问/修改在线或共享文档、未改网络配置、未重建环境/装包；未跑 H0、其他任务、其他 seed 或第二个 episode。当前轮产品源码未修改。

启动 17 项 go2_demo 源码哈希与第一部分离线通过版本完全一致，结束哈希与启动相同。第一部分 pytest=352 passed+15 skipped、任务列表正常；本轮只新增运行目录监视器，离线监控自检 6 passed。最终 git diff --check 干净。manifest 的 task/task_id/seed/model/budgets/evaluation/asset_lock_sha256 及 timeout/output/thinking 均与历史 H0 一致；新安全联锁是本轮明确标记的实验执行差异。

## metrics.json

| 指标 | 本轮 H2 |
|---|---:|
| A passed / B passed | false / false |
| success / termination | false / budget_exhausted |
| decision_calls / model_calls | 120 / 120 |
| 输入 token | 678,620 |
| 输出 token | 162,239 |
| 合计 token | 840,859 |
| 非空 reasoning_content | 120/120 |
| reasoning_content 字符 | 579,291 |
| protocol_retries | 0 |
| finish | 未调用 |
| 墙钟 / 仿真秒 | 1032.342083 / 125.460000 |
| collision / fallen | false / false |
| final_stop | succeeded |

启动前说明的完整一轮预估是约 60–74 万 token；**实际 840,859 高于该历史估计**。这不是额外一轮或重试造成：只有 120 个请求；输入/输出合计如上。

A 未通过独立 checkpoint；B eligible=false，失败原因含 A_NOT_CONFIRMED_BEFORE_B，最终距 B 6.871168 m。A 评分中 5.258059 m 是保留的一次未通过停止见证，不是最终 A 距离。独立评分按原协议，未把模型自述当成功。

## 门控触发与恢复

边界来自场景 floor_half_size_m=(8,6)，实验支撑余量仍为 0.35 m，没有现场调整。GT 坐标只用于联锁及结束后诊断，未额外加入规划状态包。

**第 114 次决策：** 请求 move_relative(forward_m=0.5,lateral_m=-0.05)，plan-0036 / explore_viewpoint_034。门控 GT 起始底盘姿态为 [-3.001338652,5.566859067,3.052709339]；名义终点 [-3.494926575,5.661044854]。中心终点仍在真实 y=6 平台内，但进入北侧 0.35 m 支撑余量，超出余量界约 0.011045 m，因此执行前返回 BOUNDARY_BLOCKED / north。

拒因包含 executed=false、requested_distance_m=0.502494、safe_distance_along_request_m=0.443568、GT source 和 experimental=true；没有裁剪并执行剩余距离，也没有刷新/推进物理来伪造成功。原始结果完整保存在 events.jsonl。

**第 115 次决策：** 规划输入确实读到结构化拒因，模型新建 shift_south_viewpoint，描述明确说“North edge is boundary-blocked”，改为 forward_m=-0.25、lateral_m=0.35，工具成功，实测起始体坐标位移 [-0.201291,0.285896]，停止确认成功。公开累计北向位移从约 5.614826 m 降到 5.309030 m。第 117 次又成功向西侧改变视点。

这证明真实模型能收到拒因并换方向，执行链路恢复了。**不能声称已经证实挡住一次必然跌落：本轮实际无跌落，但没有执行被拒动作的反事实物理对照，且其中心名义终点仍在平台内。准确结论是拦截了 1 次进入实验安全余量的移动，并随后撤离。**

连续边界拒绝尝试最高为 1，未满足连续 5 次无进展的提前停止条件；stop_reason.json 不存在。监控将观察/追踪/原地转向视为非移动尝试，不单独清零拒绝序列；执行过非拒绝移动、累计位移至少 0.10 m 或首次发现新任务身份才解除旧序列。该监控只读现有反馈/里程计，不写模型输入或记忆。

## 搜索、A 与 B 记忆

首次 move_relative 在第 8 次成功。工具总数：move_relative 39（37 成功、1 次记忆约束拒绝、1 次边界拒绝）；turn 15（14 成功、1 次记忆约束拒绝）；track_point 35、observe 10、get_geometry 21，均成功。motion_calls=51，不把执行前拒绝算作已执行运动。

search_review_due 共 10 次：12、24、36、48、60、72、84、96、108、120。末次是预算结束后的记忆更新，没有第 121 次规划读取。规划器持续移动，但没有首次 A 任务身份重置搜索时钟。

**A 从未出现：0 个候选，MD 无 task:A，对应 checkpoint 未通过。** 工具结果时刻的公开累计里程计范围：x∈[-3.123258,1.707894]，y∈[-0.029698,5.614826] m。先东北、后北、再西北/西侧；最近一次到 A 的距离约 5.232526 m（第 26 次，结束后只读里程计诊断），最后该诊断约 10.915924 m。未形成有效找到 A 的路线。

**B 回找收益仍无法验证，因为没有 A 后回找阶段。** 具体 memory.md 证据：

- e000005（第 4713 行）：step 1，B 位置 [1.7354,0.7421]，source=task_label_rgbd_tracking。
- e000030：step 5，独立 frame-00003 再次观测 B；e000042：step 7 的后续证据。
- confirmed B 有效进入规划输入 11 次：第 8–15、20–22 次。A 后读取次数为 0。
- 最终 task:B 条目（第 416 行附近）state=stale、last_seen=22，保留 position_m=[2.284607331,0.911856583]，candidate_pose≈[1.735394380,0.741404450]，证据仍包括 e000005/e000030/.../e000146。位置矛盾和 stale 说明写读存在但定位质量不稳定，不能据此证明导航收益。

门控本身没有把 BOUNDARY_BLOCKED 写成记忆 action/边界观测条目，未新增边界状态字段或门控引起的 physical skill_stuck。正常 planner.note_results 经原有 last_tool_feedback 返回拒因。模型第 115 次的新计划描述随后会按原有规则记入 MD；其中包含对 north boundary 的模型计划文本。这不等于联锁写入了一个 GT 边界对象，也不能把整个 MD 说成“没有任何提到边界的文字”。

## 失败归类

**主要是规划/探索失败。** 预算用尽前始终没有 A 候选，路线逐渐远离 A；软复核没有带来有效目标覆盖。运动实际执行均成功，无碰撞/跌倒，最终停止成功，不能归为本轮物理执行故障。

另有 2 次普通 MEMORY_CONSTRAINT：第 2 次 turn、第 37 次 move_relative，均为 PRECONDITION_UNPROVEN；不是 API 协议错误，之后第 3/38 次分别恢复正常转向/移动，没有连续拒绝成环。B 记忆位置矛盾/老化是明确限制，但没有进入回找阶段，不能将本轮定位为“记忆回找失败”，也不能分离路线选择与可用感知信息不足的因果份额。

临时安全联锁只处理边缘执行风险，不负责发现 A 或规划通路；本轮验证了拒因响应，demo 仍未跑通。

## 协议错误和原始响应

120 份 model_protocol 记录各含 1 个 OK；ModelProtocolError=0，finish_reason=length=0，protocol_retries=0。完整错误原始响应捕获已启用，MockTransport 自检验证首个/两个失败体的完整保留与默认修复重试；本轮实际没有这类错误体需要存档，不能声称真实重试效果得到验证。

正常工具拒绝保存在 events.jsonl，不与协议错误混为一类。monitor_tests.txt、validation.json 和 evidence.json 记录了检查结果。

## 证据与停止

本轮父目录包含 report.md、metrics 所在唯一 episode、memory.md、events.jsonl、trajectory.jsonl、manifest.json、evidence.json、summary.json、config.json、started.json、console.log、boundary_monitor.jsonl、monitor_tests.txt、validation.json、instrumentation/、collect.py、analyze.py。

Windows 审阅副本：D:/codex_project/output/memory-v1-h2-boundary-gate-rerun-20261111-s0/。原始 WSL 文件保留，副本逐项 SHA256 校验。

已停止，不追加任何任务、seed、H0 或第二轮 API，不改产品源码、共享文档或远程仓库。

# H2：方案 A 搜索复核修复后单轮重跑

2026-11-11，memory-v1 本地分支，seed 0。**A/B 均未通过；第 99 次决策的 move_relative 返回 ROBOT_FELL，终止为 execution_failure。并非预算耗尽。未调用 finish，没有重跑。**

## 条件与范围

唯一 episode：`/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-search-budget-rerun-20261111-s0/H2/20261111-152723-api-memory_ab_occluded_v1-s0-62de9d`。

默认 `.venv/bin/python -m go2_demo` 入口；--provider compatible、MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1、MODEL_NAME=deepseek-v4.1-flash；--task memory_ab_occluded_v1、--memory-v1、--seed 0、--viewer。

沿用历史 H0 条件：max_model_calls=120、max_wall_seconds=2400、max_sim_seconds=600、history_turns=6、api_timeout=90、max_output_tokens=8192、thinking enabled。默认每次决策最多两个请求，重试共享调用预算；没有使用 max_requests=1 launcher。实际 99 次决策各一个请求。

密钥由默认客户端从 ~/deepseekapi.txt 读取，仅供鉴权，未打印或记录内容。无在线文档访问、共享文档修改、push、H0 重跑、额外 seed 或额外 episode；未安装依赖、未改产品源码或现场提示。运行目录内只附加错误原始响应存档和连续两次门控拒绝停止监控，不覆盖 APIModel.decide 或重试策略。

启动源码 16 项哈希与方案 A 离线 evidence.json.product_hashes 完全一致；结束哈希与启动一致。manifest 中 task、task_id、seed、model、budgets、evaluation、asset_lock_sha256 以及 timeout/output/thinking 设置均与旧 H0 一致。工作区原有实现改动保留，未提交。监视器离线检查 4 passed；git diff --check 正常。

## metrics.json

| 指标 | 本轮 H2 |
|---|---:|
| A passed / B passed | false / false |
| success / termination | false / execution_failure |
| decision_calls / model_calls | 99 / 99 |
| 输入 token | 555,810 |
| 输出 token | 137,608 |
| 合计 token | 693,418 |
| 非空 reasoning_content | 99/99 |
| reasoning_content 字符 | 493,125 |
| protocol_retries | 0 |
| finish | 未调用 |
| 墙钟 / 仿真秒 | 916.967564 / 108.240000 |
| collision / fallen | false / true |
| 最终停止 | STOP_NOT_CONFIRMED |

A 没有成功 checkpoint，B eligible=false、A_NOT_CONFIRMED_BEFORE_B。A 评分里距离 4.917280 m 的记录是保留的未通过停止见证，不是最终距离；B 最终评分距离为 6.039049 m。工具结果时刻的公开里程计路线距 A 最小 4.844459 m（决策 59），最后结果时刻约 8.340884 m；这两者与评分采样/清理停止时刻不同，不混用。

历史 H0 继续沿用：A 第 89 次决策通过，B 未通过；120 次决策、1,985,073 token、最终距 B 4.090894 m、budget_exhausted、未 finish。本轮不能因 token 较少就判定记忆提高效率。

## 1. 规划器动起来了吗？

**第 7 次决策首次 move_relative，forward_m=0.25、lateral_m=0，成功。** 计划 plan-0001 / viewpoint_move。发生在首次复核之前，不能归因于第 12 步的复核。

全部工具：track_point 37、turn 14、move_relative 28、get_geometry 12、observe 8。平移 27 次成功、最后 1 次跌倒失败；14 次转向全部成功，其中正向 9 次、负向 5 次。第 35/36/38 次 track_point 返回 PERCEPTION_ERROR（No usable depth at the selected pixel），之后恢复观察和运动。

## 2. search_review_due 是否触发、规划器是否响应、是否离开西北回绕？

**共 8 次：第 12、24、36、48、60、72、84、96 步工具反馈之后。** 首次账本 e000082；最早在第 13 次规划输入可见，之后第 13–99 次输入保持 review_due=true。一直没有新的任务身份，搜索年龄没有因平移、重复 B、观察或换计划而清零。局部 search_stalled 为 0。

规划器有可核查的行为响应：第 13 次先追踪新点；第 14 次新建 advance_viewpoint_for_A 计划、平移 0.3 m，描述使用 point-006 的真实 range/bearing，completion 是 point-006.range_m <=1.42，显式包含 search_review_due 分支；第 17 次改向右扫。第 31 次后多次复用/延续移动腿，而非上一轮的同向转弯后短移。新计划中多次写入该分支，但同名事件分支在触发前也已存在；仅凭一轮不能证明软事件是路线改变的唯一原因，更不能把“包含分支”视为充分策略复核。

**确实离开上一轮西北侧局部回绕。** 工具结果时刻的公开累计里程计范围：x∈[0,2.490386] m、y∈[-0.029698,6.180561] m，最大离起点 6.231995 m。先向东北，随后向北、再向西北，最后到北侧平台边缘。不是上一轮 x<0 的局部西北循环；但后半程持续远离 A，搜索仍未有效找到目标。

这些位姿和 A 距离只用于结束后诊断；没有把 A 坐标、柜体地图或事后路线分析注入本轮决策。完整路线点、复核账本、输入序号与显式分支计划保存在 evidence.json。

## 3. 是否到达 A？

**没有。** 全部规划输入的 A 候选次数为 0，memory.md 无 task:A 对象，独立 A checkpoint 未通过。规划文本声称“reveal cabinet-occluded sectors”不是实测覆盖证据。

## 4. 记忆在回找 B 时是否有作用？

**无法验证：没有通过 A，未进入 A 后回找 B 阶段。** 可以确认 B 的写入与部分读取链路存在：

- memory.md 第 3974 行 e000005：step 1，task:B 初始观测，position_m=[1.7354,0.7421]，source=task_label_rgbd_tracking。
- 第 4212 行 e000023：step 4，独立 frame-00003，再次观测 B。后续 e000035（step 6）继续提供证据。
- confirmed B 进入有效规划输入共 10 次：第 7–9、12–16、25–26 次。A 后 B 读取为 0。
- 最终 task:B 条目保留 position_m=[1.8852620242737823,0.735033009777705]、last_seen=30、state=stale，evidence_ids 仍包含 e000005/e000023/.../e000205。旧证据未删除，但 stale 不作为强前置条件。

B 观测位置曾多次矛盾/重新确认，说明写读链路不等于定位稳定，更不等于成功回找。身份来自任务给定标签+当前 RGB-D 候选/追踪关联，reference_pose 为既有公开理想仿真里程计，motion_delta_used=false；不声称通用语义识别或新增真实里程计能力。

## 协议、截断和停止

ModelProtocolError=0、finish_reason=length=0、protocol_retries=0；没有真实重试样本，不能声称验证了真实修复成功。未发生需存档的协议错误/截断原始响应，因此没有遗漏或待保存的错误体。运行监视器已启用完整 .raw 捕获（若出现密钥回显则脱敏），四项 MockTransport/停止测试通过。

MEMORY_CONSTRAINT / MEMORY_NO_PROGRESS=0，未发生连续门控拒绝，stop_reason.json 不存在。本轮没有为失败追加第二个 episode，也没有继续用完剩余 21 次预算。

## 失败归因

**直接终止原因是执行失败；之前已有规划/探索失败，无法将本轮失败归为单纯记忆故障。**

第 99 次请求 forward_m=0.3，仍用一个 floor ray 的 range/bearing 支持持续前进；返回 ROBOT_FELL，实际位移/转角显著偏离，内层停止及最终清理停止均未确认。独立评分 fallen=true、collision=false。

离线控制轨迹显示：首次 fallen 在仿真 108.04 s，base_xyz≈[0.66394,5.96292,0.14677]，高度低于后端 0.16 m 阈值；场景为有限 16×12 m 平台，北边界 y=6。之后位置继续落到平台外且高度为负。结合位置和下坠，支持“北缘附近失去支撑后跌落”的判断；未重新仿真，不进一步断言控制器和边缘接触的因果份额。MUJOCO_LOG.TXT 另记录 109.10 s ACTUATOR 2 出现 Nan/Inf/huge CTRL 警告，晚于首次跌倒，不能直接把该警告当作最初根因。

规划层虽摆脱了上一轮西北局部循环，却持续走向北侧边缘，始终没获得 A 的候选；软复核可见且被写入计划，但不足以保证正确的搜索方向或安全通道。记忆保存 B 和复核账本的证据成立，B 回找收益没有测试到；本轮不能分离感知信息不足、路线选择、边缘风险判断各自的因果贡献。

## 文件

- 原始 metrics.json / memory.md / events.jsonl / trajectory.jsonl / manifest.json 均在上述唯一 episode。
- report.md、evidence.json、config.json、started.json、console.log、MUJOCO_LOG.TXT、run.sh、instrumentation/ 均在本轮父目录。
- Windows 可读副本：D:/codex_project/output/memory-v1-h2-search-budget-rerun-20261111-s0/，包含报告、metrics、memory、证据、原始事件/控制轨迹及配置/监视器。副本哈希逐项校验一致，源 WSL 文件保留。

已停止：不跑 H0、不加 seed、不跑其他任务、不 push、不修改共享/在线文档。

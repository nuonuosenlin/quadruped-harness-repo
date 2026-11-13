# H2 离线诊断与修复

本轮仅在 memory-v1 分支离线读旧日志、改实现和跑测试。没有访问在线文档、读取真实密钥、调用真实 API、执行物理 demo 或消融，也没有改写旧 H2 证据。

## 旧问题的确切链路

旧 H2 有 83 次模型输入、82 个成功解析响应；返回工具计数为 `{'observe': 83}`。没有 track_point 或 get_geometry，原 PointTracker 从未建立任何点，适配器因而一直送入 objects=[]。MemoryRules 的两帧确认规则本身并未收到可确认的对象，不是把已有合格 A/B 证据错误过滤掉。

原适配器也没有任务标签关联器：即使有追踪点，也只会生成 unclassified_landmark。它只看 observation.tracked_points，没有合并工具返回的 point/points。原规划状态中 task_targets、实时 current_observation、last_tool_feedback 的出现次数分别为 0、0、0。任务文本虽仍有蓝球／绿方块，结构化观测却只有未分类角点；没有 RGB 图像、颜色标签候选或可用的前一步工具反馈。反复 observe 并不会自动选点或产生语义对象。

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

## 旧门控拒绝记录

- 第 17 次：Invalid plan envelope or binding. Observe or submit a valid new plan.
- 第 33 次：Invalid plan envelope or binding. Observe or submit a valid new plan.
- 第 40 次：Invalid plan envelope or binding. Observe or submit a valid new plan.
- 第 72 次：Invalid plan envelope or binding. Observe or submit a valid new plan.
- 第 78 次：Invalid plan envelope or binding. Observe or submit a valid new plan.

以上是工具结果中的既有约束反馈，不是重建私有 reasoning；安全感知工具现在可以在可选计划无效时继续收集证据，运动/finish 的强前置条件仍保留。

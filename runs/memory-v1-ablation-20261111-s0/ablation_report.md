# memory_ab_occluded_v1：正式任务与 seed 0 消融

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
| H0 | False | True | False | 120 | 1867189 | 117884 | 1985073 | 120/120 次，373249 字符计数 |
| H2 | False | False | False | 83 | 218231 | 11720 | 229951 | 81/83 次，35950 字符计数 |

### H0

A 已通过，但最终 B 未通过；B 原因=['DISTANCE_OUT_OF_RANGE', 'HEADING_OUT_OF_RANGE']。仅凭评分不能断言原因就是遗忘。

终止：`budget_exhausted`；工具分布：`{'observe': 1, 'track_point': 25, 'turn': 73, 'move_relative': 21, 'get_geometry': 1, 'stop': 1}`；失败工具：`{'INVALID_ARGUMENTS': 2, 'ONE_TOOL_PER_TURN': 4, 'PERCEPTION_ERROR': 1}`。

[metrics.json](/home/nuonuosenlin/Agent-harness/runs/memory-v1-ablation-20261111-s0/H0/20261111-002934-api-memory_ab_occluded_v1-s0-dcae9e/metrics.json)。成绩来自正式独立评分，未以模型是否自述 finish 代替。

### H2

运行错误：{'type': 'ModelProtocolError', 'code': 'MODEL_PROTOCOL_ERROR', 'message': 'Model must return at least one bounded tool call.'}

终止：`model_error`；工具分布：`{'observe': 83}`；失败工具：`{'MEMORY_CONSTRAINT': 5, 'ONE_TOOL_PER_TURN': 2}`。

[metrics.json](/home/nuonuosenlin/Agent-harness/runs/memory-v1-ablation-20261111-s0/H2/20261111-005143-api-memory_ab_occluded_v1-s0-ec98dc/metrics.json)。成绩来自正式独立评分，未以模型是否自述 finish 代替。

记忆文件：[memory.md](/home/nuonuosenlin/Agent-harness/runs/memory-v1-ablation-20261111-s0/H2/20261111-005143-api-memory_ab_occluded_v1-s0-ec98dc/memory.md)。最终 revision=89，账本 338 条，对象 0 个；83/83 个模型输入含 memory_state，其中 0 次有有效对象，最大快照滞后 1 步。对象类别：`{}`。

记忆诊断：已写、已读，不能归类为“文件没写”或“规划没读”。当前规则适配器只提供未分类追踪点／角点，没有蓝球 A、绿方块 B 的语义绑定或完整持久导航路线；因此不能声称规划忽略了已经可用的 A/B 目标记忆。具体失败还应结合工具序列、有效对象次数和快照滞后判断。

## 停止条件

H0 未通过，已按冻结配置完成唯一一轮 H2。至此停止，没有重复尝试、其它任务或其它 seed。单次实验只报告本次结果，不作统计显著性或泛化结论。

## 文件

- ablation_config.json：冻结配置及源码哈希。
- ablation_summary.json：机器可读汇总、完整检查点与记忆诊断。
- H0/、H2/：各自运行目录，含 manifest、events、frames、metrics、trajectory；H2 若运行还含 memory.md。
- collect_ablation.py：只读本地成果的汇总器；不读取凭据或调用模型。

本轮源码涉及 scenarios.py、backend.py、runner.py、新增 ordered_evaluation.py；测试涉及 test_memory_scene.py 与新增 test_ordered_evaluation.py。

## 最终失败诊断补充

H0 在第 89 次决策形成 A 合格停止证据；此后 31 个模型输入中，任务给定绿色掩膜均未见足量 B 像素，后续为 20 次 turn、5 次 move_relative、4 次 track_point、1 次 get_geometry、1 次 stop。最终 B 距离 4.090894m、朝向误差 1.942088rad，未 finish，120 次决策耗尽。这说明本轮回找／绕行到 B 未完成，不能仅据此证明原因就是遗忘。

H2 的直接终止原因是第 83 次响应未提供数量合规的工具调用列表，报 MODEL_PROTOCOL_ERROR；此前 82 个成功解析响应中，所有工具调用均为 observe（其中一次双调用被拒绝），无 track_point 或移动。记忆有 338 条账本、revision 89，83 个输入都包含 memory_state，但有效 objects 始终为 0。当前 H2 输入不含 RGB 原图，仅有未分类角点；没有建立蓝球 A／绿方块 B 的语义绑定。这是目标感知到有效记忆的数据内容缺口，不能说文件没写或规划完全没读，也不能说它忽略了已经存在的有效 A/B 记忆。

H2 的 metrics token 为 218231 输入、11720 输出、229951 合计；非空 reasoning 计数为 81 次。最后一次协议错误响应未返回 Decision，故其 usage／reasoning 未纳入现有 metrics，实际账单用量未知。H0 的 120 次均正常解析并有非空 reasoning。两轮输入形式本就不同（H0 RGB+历史、H2 结构化状态），本次也未补通语义感知，因此不能把 token 差异或失败差异解释为单独的记忆增益。

两轮均已停止，没有事后修补后重跑、延长预算或增加 seed。

协议诊断精度说明：本地适配器在 tool_calls 缺失／非列表、为空或超过 16 个时均抛出同一错误；原始错误响应未留存，不能进一步确定具体子情况。最终结论仅采用 MODEL_PROTOCOL_ERROR，不把某个子情况当成已确认事实。

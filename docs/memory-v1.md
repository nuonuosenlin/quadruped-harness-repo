# Memory v1（本地实现说明）

默认 H0 路径保持关闭记忆。仅在显式添加 `--memory-v1` 后启用规则记忆；原工具名称、参数、单回合一个工具调用和独立 `metrics.json` 评分不变。H0 默认仍保留 6 回合历史。

## 数据流与边界

`Harness.observation()` 与工具结果 → `PublicObservationAdapter` → `AsyncMemory` FIFO 后台线程 → `runs/<run-dir>/memory.md` → `MemoryPlanningHarness` → 规划模型 → 原工具后端。

核心记忆不导入模型、MuJoCo 或本体状态，不访问任务隐藏真值和独立评分器。不实现图增强；`topology` 为 `null`，`anchor_node` 暂为空。没有新增依赖。

后台线程更新规则并通过临时文件 + 原子替换发布 MD，再从真实文件读取“现场状态”作为已提交快照。决策线程仅复制最新已提交快照，不等待队列或磁盘；只有退出清理和离线测试允许 drain。快照带 revision、step 和 snapshot_lag_steps。落盘滞后时不沿用陈旧位置作为强前置条件，规划可继续观察或恢复。写入出错向规划暴露事件并拒绝需要执行的规划；退出汇报 memory_error，不能算成功。每轮使用新目录，禁止覆盖已有账本。

MD 的“现场状态”保存对象、所有计划（含非活跃旧计划）、测量证据、事件和只追加账本。每次重写快照保持既有账本前缀不变；失效用状态表示，不删除历史。后两节“操作经验”“程序工具”仅保留空标题。当前 v1 没有经验提炼和脚本库。

## 证据与状态

每个对象包含 object_id / category / state / pose / pose_covariance / last_seen / confidence / anchor_node / visual_feature / evidence_ids，另有明确 source。`last_seen` 用工具回合步数；pose 包含坐标系。无法标定的协方差写 `null`，不伪造数字。

一条高置信观测仍为 unknown；两条不同帧或不同传感器的高置信证据（>= 0.8）才 confirmed。同一对象、来源、帧的重复读取不产生新证据，不刷新 last_seen。再次观测更新位置、置信度及来源。自最后观测起，3 步不可见变 predicted（仅静态地标的短期预测），6 步变 unknown，10 步变 stale；predicted 不能作为强前置条件。过期后重新确认需要新的多帧证据。

同坐标系高置信观测偏离旧位置超过 0.5 m 时，把旧位置标记 contradicted，记录候选新位置、重定位账本及 replan_required；依赖对象的子目标变“已失效”。后续独立证据确认新位置后可恢复对象 confirmed，旧子目标不会自动复活。外界扰动只能由可信传感器适配器提交，正向 disproves 证据同样传播失效。

当前 Go2 适配器仅使用公开局部里程计、RGB-D 追踪点和执行反馈。追踪点 category 固定为 unclassified_landmark；不能凭追踪置信度认定是任务目标。轻量 RGB 角点模块提供带来源和 image_id 的像素候选，供 track_point 使用，不把角点当成已确认的语义对象。v1 不新增完整语义检测器，不能据此宣称具备 13 项任务的目标识别能力。接入其它本体或语义检测器时替换适配器，给规则层提交同样的任务层证据结构。

## 规划协议与验证器

记忆模式的模型上下文只有任务和当前结构化状态包：world / pose / objects[] / active_beliefs[] / invalidated[] / events[] / topology / confidence_thresholds。过滤 unknown、contradicted、stale 对象位置及非活跃旧计划；predicted 带减半置信度和预测依据。账本和全部历史不进入 prompt；事件只保留最近 16 条、对象证据引用只取最近两条。无相机原图和历史模型推理输入。公开测量及视觉候选位于 world，滞后时不输出旧测量为当前测量。

规划输出仍恰好一个原有工具调用；assistant content 为 JSON 计划信封：

```json
{"plan":{"subgoals":[{"subgoal_id":"inspect","description":"验证地标","preconditions":[],"completion":[{"object_id":"point-001"}]}],"branches":[{"on":"skill_stuck","subgoal_id":"inspect"}],"recovery":"重新观察"},"subgoal_id":"inspect"}
```

Harness 分配 plan-0001 等 ID；后续继续该计划用 `{"plan_id":"plan-0001","subgoal_id":"inspect"}`。新计划使旧计划和所有旧子目标非活跃。被拒绝的新计划仍有 ID 和拒绝证据，但不活跃。子目标状态只有“待做／进行中／已完成／已失效”，完成须由规则检查测量条件，模型自述或 finish 不算证据。已完成条件被正向测量推翻也失效。

条件仅支持 `{"object_id":"point-001"}`（当前 confirmed 证据）或 `{"measurement":"pose.x_m","op":"ge","value":0.5}`，比较支持 ge/le/eq。可用测量名由 world.measurements 提供；未知测量不能满足条件。运动和 finish 要绑定计划；已被记忆否定、失效、过期或证据不足的前置条件返回 MEMORY_CONSTRAINT，动作不下发。observe/track_point/get_geometry 可无计划收集证据，stop/abort 始终可通过原工具校验执行恢复。

记忆侧验证目标状态变化、技能执行失败/卡住、障碍阻塞和前置条件失效，形成 target_state_changed / skill_stuck / dynamic_obstacle_blocked / key_precondition_invalidated / replan_required 等带证据事件。很小的成功位移不会误报卡住。规划负责选择分支及恢复策略，记忆不自动替模型执行策略。

## 离线验证与下一步

使用现有 `.venv`：

```bash
source .venv/bin/activate
python -m pytest -q
./scripts/run_deepseek.sh --list-tasks
python scripts/write_memory_example.py
```

最后一条仅用合成证据写 runs/memory-v1-offline-example/memory.md，不启动模型或仿真；已有文件时拒绝覆盖。示例证据明确标 synthetic，包含确认、短期预测、阻塞失败、重定位失效、恢复计划及测量完成。

尚未运行真实 API、demo 或消融。将来获准运行时，在现有命令追加 `--memory-v1 --provider compatible --model-name deepseek-v4.1-flash --api-key-file ~/deepseekapi.txt`，并按会话要求设置 `MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1`、`MODEL_NAME=deepseek-v4.1-flash`。本次未读取密钥、未改 provider 默认值或脚本默认值、未修改 pip 配置。

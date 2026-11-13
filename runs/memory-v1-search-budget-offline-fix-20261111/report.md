# 方案 A：跨工具搜索预算时钟与探索腿提示

2026-11-11，本地分支 memory-v1。已完成本轮离线实现与验证；未调用 API、读取真实密钥、运行 demo/消融、访问在线文档、修改共享文档或 push。使用现有 `.venv`，未安装依赖。**方案 B 未实施。**

## 结果

- 原有六次成功转向的局部 search_stalled 检测保留。
- 新增每 **12 次逻辑决策**的 search_review_due 软复核：跨所有工具类型，普通平移、观察、重选点、重复看到同一 B、换 plan_id 都不清零。
- 仅首次观察到新的任务候选/对象身份会重置。候选升级为同一对象的 confirmed、同一对象换帧/换来源，不算发现新任务身份；也不会因此提高对象确认权限。
- 预算超时只追加账本和事件，并在 world.exploration 中持续提供状态；不设置子目标失败/失效，不禁止运动，不自动移动或强制 abort。
- 探索提示要求持续方向、真实观测参照和可验证的局部终止条件，避免反复同向转弯后短移；当前几何不足时仍不能编造通行空间。
- 最终 pytest：**339 passed、15 skipped**，原 328 项保留通过，新增 11 项；`--list-tasks` 与 `git diff --check` 正常。
- 任务、场景、原子工具后端和评分语义未改，**H0 不用重跑**。

## 1. 新旧两个计数的语义

### 局部六次转向规则：保持原样

它仍累计成功 turn；成功 move_relative 或首次任务观测可重置。到 6 次追加 search_stalled、skill_stuck、replan_required，一个停滞周期只发一次。普通观察、重选点、换计划不清零。

这条规则只识别“只转不走”，不再被描述为完整搜索进度的度量。原有测试和旧路线重放都保留其行为，本轮旧路线仍未触发这个局部信号。

### 全局搜索预算：不因普通动作清零

[memory.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory.py:387) 使用现有 payload.step——返回工具结果的逻辑决策序号——计算距上次首次任务观测的步数。初始化观测为 step 0，正常每轮返回工具结果后加一；同一步的重复发布或一个决策里的多个结果不会重复计时，API 内部协议重试也不会被当作新的探索步。

下列行为都不重置时钟：

- 成功平移、转向、observe、get_geometry、stop 等普通工具调用；
- 工具失败、缓存去重调用所消耗的逻辑决策；
- 新选普通 point_id、重复追踪同一 B、候选升级为同一个已知任务对象；
- 替换计划、模型自述已覆盖或完成探索腿。

唯一重置条件是首次出现新的任务身份，来源限于适配器给出的当前任务候选/任务对象，而不是模型生成的计划文本。该注册表与既有候选/对象链共享身份去重，不改变多帧确认或强前置条件规则。

## 2. 阈值为什么选 12

对同一旧探索序列做 12/16/20 窗口比较，未执行动作或模型：

| 窗口 | 首次复核（工具返回后） | 120 步固定数据中的事件次数 |
|---:|---:|---:|
| **12（采用）** | **12** | **10** |
| 16 | 16 | 7 |
| 20 | 20 | 6 |

旧路线初始化时已经看到 B；之后没有新的 A，所以旧数据重放的全局年龄最终为 120。第 12 步前已完成 4 次转向、4 次选点、2 次平移（第 9/11 次）、2 次观察；具备复核一次探索方向的条件。12 比 6 更能容纳初始化选点和短扫视，又能在第 15 次继续同方向移动前提醒。16/20 会更晚才复核，分别已走完三/四次初始偏西北平移。

12 是当前最小版本的初始预算，不宣称是通用最优阈值。正常长探索腿不被误伤主要靠**软信号语义与不改门控**，不是声称正常路线一定能在 12 次内看到目标。

第 12 次工具返回后在记忆侧生成记录；其发布后的下一次规划读取可以看见，最早为第 13 次决策。真实运行仍异步、不等待写盘，本轮没有进行真实模型验证，不能保证具体墙钟时刻或模型响应。

## 3. 账本、事件和状态包

每个 12 步窗口最多追加一次 `search_review_due` 账本和同名事件，source=memory_verifier、advisory_only=true。既不伪装成物理 skill_stuck，也不自动产生 key_precondition_invalidated 或 replan_required。

若仍没有新任务身份，下一窗口会再次提醒；同一步重复发布不会刷屏。若离线输入跳过多个窗口，只对当前超时窗口记一次，不伪造中间执行事件。

world.exploration 中新增：

```json
{
  "decisions_since_task_novelty": 12,
  "last_task_novelty_step": 0,
  "review_interval_decisions": 12,
  "review_due": true,
  "review_count": 1,
  "last_review_step": 12,
  "review_evidence_id": "对应追加账本ID",
  "review_semantics": "advisory_strategy_review_not_failure_or_motion_prohibition"
}
```

review_due 在首次新任务身份到来前持续为 true；新观测重置当前状态后，旧账本和事件仍保留为历史。提示明确要求以当前标志为准，不能因旧事件残留就认定新阶段仍然超时。

现有有界投影已能保留整个 world.exploration，因此无需修改 memory_context.py。正常 12000 / 重试 6000 字符上限、顶层八字段与异步发布均不变。计时器不读取里程计、位姿、执行位移真值、A 坐标、柜体地图或事后覆盖网格。

## 4. 探索腿提示

[memory_planning.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory_planning.py:74) 新增的约束是：

- 探索腿要承诺一个持续方向/分支，以稳定的当前观测参照执行到可验证的局部终点，然后再扫描或切换。
- 复核时检查证据是否支持当前腿继续；有测量进展的长腿可继续，不因软提醒自动失败。缺乏进展时改变方向、分支或参照，不能只换 plan_id 或再走一个同类短步。
- 描述需包含方向、观测参照和终点；有可用测量时采用非空 completion，如实际跟踪点的 range/bearing 条件，而不是把“已经看到 A”设成用于发现 A 的探索腿终点。
- 点丢失或几何未知不代表完成；重观测、另选有证据的分支，或停止/中止。
- 已尝试分支是计划意图，不是实测覆盖地图。单个追踪射线不能证明整个通道可通行。

完整示例仍是 move_relative + planning，示范的完成条件为 point-001.range_m <=1.5；提示明确规定只有当前确实存在该测量、阈值确有局部几何意义时才能使用，否则选择别的受观测支持的条件。它不是实际测量、目标坐标或通行证据，也不是强制运动脚本。

探索 preconditions=[] 仍合法；未知/预测/过时对象不能作为强前置条件。没有新增硬性探索计划字段或额外门控条件，以免把暂时证据不足的正常探索全部挡住。

## 5. 离线验证结果

### 旧路线固定数据重放

只把已保存的适配器观测、工具反馈、逻辑步序号和计划送入 MemoryRules，不运行 MuJoCo，不执行旧指令，不调用模型。

- 新复核事件出现在 12、24、36、48、60、72、84、96、108、120。
- 原局部 search_stalled 仍为 0，符合旧路线成功平移不断重置局部计数的情况。
- 原有状态事件保留：target_state_changed=71、replan_required=42、key_precondition_invalidated=2；新加的只有 10 条 search_review_due。
- 固定数据重放中的计划/子目标状态与旧规则相同，没有因新软信号增添失效。

这验证新计数能看见旧盲区，不是对真实规划器已经改好路线的证明；固定动作重放不会响应新提示。

### 新增 11 项测试

- 混合 turn/move/track/observe/get_geometry、换计划和重复 B 均不能清零；按窗口产生有限软事件，不产生新的失败/禁令。
- 工具失败和去重调用仍消耗逻辑预算；同一步多结果/多次发布不重复计时。
- 任务候选先出现或任务对象先出现，都按同一身份只重置一次；后续确认、重现不清零，旧账本保留。
- 新普通 point_id 与模型计划更名不能伪装任务新颖性。
- 正常/重试投影与大量事件噪声下仍保留当前 review_due，字符上限不变；新身份重置后当前标志为 false，旧事件仍保留。
- **30 步正常长探索腿**：每次通过真实记忆门控，经历第 12/24 步提醒后继续，最后由合成 RGB-D 范围测量完成；没有 skill_stuck 或子目标失效。
- 软复核时新鲜但 unknown 的 task:A 仍被强前置条件检查拒绝；无对象依赖的合法探索可通过。
- MockTransport 规划 fixture 实际读到复核状态，返回带参照/终点的另一探索腿，经原 API 解析和门控通过。无真实网络，不能据此声称 LLM 一定执行覆盖策略。

最终命令：

```text
.venv/bin/python -m pytest -q
339 passed, 15 skipped

./scripts/run_deepseek.sh --list-tasks
正常，memory_ab_occluded_v1 仍为 supported

git diff --check
通过
```

门控 AST 审计确认 predicate、validate_plan、validate_check、MemoryPlanningHarness.prepare 与本轮修复前完全相同。

## 6. 改动与可比性

产品改动仅：

- `go2_demo/memory.py`：12 步跨工具时钟、窗口去重的软事件与持久状态；局部六次转向规则保留。
- `go2_demo/memory_planning.py`：软复核语义与持续方向/观测参照/可验证终点的探索提示。
- 新增 `tests/test_memory_search_budget.py`；原有测试未删改。

memory_context.py、memory_perception.py、memory_protocol.py、runner.py、models.py、harness.py、backend.py、scenarios.py、ordered_evaluation.py、__main__.py 等与本轮开始时相同。没有实施方案 B，没有新增 RGB-D 边界、通行扇区或语义检测模块。

**任务、场景、工具后端语义、独立评分及默认 H0 路径均未改；历史 H0 不需要重跑。** 当前只证明方案 A 的规则、提示接口和门控兼容性，不保证真实模型下一轮能找到 A 或完成 A→B。

## 产物与复现

本目录包含 report.md、evidence.json、replay_memory.md、replay_summary.json、before_hashes.json、source_before/、pytest.txt、list_tasks.txt、verify_fix.py。evidence.json.after_hashes 是源文件审计，product_hashes 单列 go2_demo 产品哈希，供后续冻结运行配置。

离线复现：在仓库下运行 `.venv/bin/python runs/memory-v1-search-budget-offline-fix-20261111/verify_fix.py`。脚本只重建本地重放证据；窗口比较临时改变的是该诊断进程内的常量值，不改源码，退出前恢复为 12。

已停在离线实现与验证阶段，没有 demo、消融或真实模型调用。

# Experimental boundary gate：第一部分离线验收

2026-11-11，分支 memory-v1。**第一部分通过，已停在离线检查点。未开始第二部分；没有调用真实 API、读取密钥、启动新仿真 episode、安装包、访问在线文档、改网络/共享文档或 push。**

这是等待今晚 20:30 组会决定最终方案的临时本地实验，不是最终边界安全设计；会后按会上选定的方案替换。只为本地 demo 探索执行层安全联锁的形状，不声称已经跑通 demo。

## 验收结果

| 检查 | 结果 |
|---|---|
| .venv/bin/python -m pytest -q | 352 passed，15 skipped；原 339 项保留通过，新增 13 项 |
| ./scripts/run_deepseek.sh --list-tasks | 正常，memory_ab_occluded_v1 supported |
| git diff --check | 通过，输出为空 |
| 前 10 次移动记录回放 | 全部放行：决策 7、14、21、27、29、32、33、40、42、44 |
| 原第 99 次致命移动 | BOUNDARY_BLOCKED，north |
| 原轨迹全部 28 次移动判断 | 会拒绝第 91、94、97、99 次，其余放行 |
| 连续拒因与记忆隔离 | 不作废计划、不判子目标失败、不新增 physical skill_stuck；搜索时钟继续 |
| 原有场景/评分/记忆/提示相关哈希 | 受保护文件完全一致；评分/清理块及 Harness 非 dispatch 方法不变 |

使用已有 Python 3.11.15 / .venv；没有重建环境或重装依赖。pytest 使用离线假后端/MockTransport；本次没有真实模型请求。

## 真值来源与边界

**必须注明：门控的底盘位姿来自 harness 当前捕获的仿真底盘位姿 frame.base_xy_yaw，是 simulator ground truth。** 它与现有后端 measured 位移字段有相同的真值来源缺口。它是安全联锁，不是非真值悬崖感知，也不是导航测量。代码模块 docstring、反馈的 source/navigation_measurement 字段和本报告均明确注明。

平台尺寸读取 scenario.floor_half_size_m，不另行硬编码 16/12 或 y=6。当前场景定义半尺寸 (8,6)，对应有限 16×12 m 平台。没有给规划器增加平台地图或绝对底盘位置。

## 临时门控行为

新增 `go2_demo/experimental_boundary_gate.py`，核心函数 `experimental_boundary_gate`。把 body-relative forward/lateral 指令用当前仿真 GT yaw 旋转到场景坐标，检查名义直线段相对于矩形边界的边缘余量。

明确采用 **0.35 m 实验性支撑/落脚和停止余量**。这只是当前实验的保守启发值，不是从模型证明得到的全机器人 swept footprint，也不声称对所有动态误差有效。边界坐标仍完全来自场景定义；余量是单独命名的 EXPERIMENTAL_SUPPORT_MARGIN_M，可在会上方案确定后替换。

为什么不能只查底盘中心是否越界：原第 99 次开始仿真 GT pose=[0.8329699063,5.7825081520,2.6938054505]；forward=0.3，名义中心终点=[0.5625476901,5.9123997413]，仍在 y=6 内。原动态轨迹却在北缘跌落。只做中心终点范围检查会错误放行，因此本实验对边缘保留支撑余量。0.35 m 的选择公开记录，尚未做真实运行验证或参数比较。

危险移动在调用 backend.move_relative 之前返回 status=failed、error_code=BOUNDARY_BLOCKED，附结构化 constraint_feedback：blocked_directions、请求方向/距离、safe_distance_along_request_m、超出安全余量的距离、experimental、GT source、executed=false。没有静默吞掉、裁剪指令、自动改方向或伪造成功；转向、观察和其他动作保留原路径。

已在余量区内时，允许向内退离，或不继续靠近该边缘的切向移动，避免要求“一步退够余量”造成恢复死锁。现有参数校验和 call_id 去重在门控之前；重复 call_id 返回原拒因并标记 deduplicated。无有限平台定义的原有任务直接沿用既有执行路径。

这是 preflight 联锁，不证明运动闭环全程不会漂移/跌倒，不检查转向的落脚安全，也不解决柜体碰撞、路线覆盖或寻找 A。允许切向/内退是恢复规则，不构成对当前边缘姿态稳定性的保证。

## 拒因反馈、记忆和搜索时钟

Harness 把拒因作为正常工具结果返回，层级与 PERCEPTION_ERROR 相同；原始拒因完整保留于 events.jsonl 的 tool_results。MemoryPlanningHarness 原有白名单支持 constraint_feedback，无需改提示或状态包字段。规划器只在已有 world.last_tool_feedback 中读取这次拒因；没有添加其他边界状态或导航信息。

现有 memory.py 会把任何失败移动写成 action_failed 并产生 skill_stuck。为了保持该模块哈希与行为不变，同时满足本任务的“拒因不写记忆、不当系统故障”，runner 在调用 adapter.payload 前使用 `experimental_boundary_memory_results`，仅从记忆动作输入中过滤这个未执行的 BOUNDARY_BLOCKED。原始工具结果仍交给 planner.note_results 和运行日志。

普通 observation、候选、逻辑 step 均照常提交，记忆更新与原来“同一步没有执行动作”的状态完全相同：

- 拒因不产生 boundary/action_failed/action_executed 的记忆条目，不加入平台几何、GT pose 或新的 memory_state 字段；
- 不将其当成功平移，不清空局部转向计数，不新增拒因所致的 skill_stuck；
- 全局 12 决策复核时钟仍然推进，到期按原规则发 search_review_due；
- 已有合法计划保持 active，子目标不因连续拒绝被判失败或失效；普通观测造成的正常老化、测量判定仍遵守原规则；
- runner.motion_calls 不把 BOUNDARY_BLOCKED 算作实际执行的运动。它仍占用逻辑决策/模型预算，不能免费重试。

“门控不改 memory_state”指除正常拒因反馈外不增加/修改边界状态；不阻止原有 step、对象老化和复核事件随时间更新。测试将连续拒因的记忆与相同步数、空 actions 的对照逐项比较，完全一致；另验证 gate 本身不改变 Harness observation，planner.note_results 不改 MD 字节。

## 改动与保护审计

修改现有文件只有：

1. go2_demo/harness.py：dispatch 的 move_relative 前置安全检查；拒因不执行 backend、不刷新/推进物理。
2. go2_demo/runner.py：拒因工具反馈照常保留，记忆 action 输入过滤、实际运动计数排除。

新增：

- go2_demo/experimental_boundary_gate.py：临时安全判断和拒因记忆分流函数。
- tests/test_experimental_boundary_gate.py：13 项离线测试。

以下文件前后 SHA256 完全一致：scenarios.py、backend.py、ordered_evaluation.py、__main__.py、memory_perception.py、memory.py、memory_planning.py、memory_context.py、memory_protocol.py、models.py、types.py。Harness 除 dispatch 外所有方法 AST 不变，TOOLS 描述和参数未改。runner 除 run_episode 接线外其他函数 AST 不变；独立评分/异常清理代码块逐字不变。原有 tests 文件哈希全部不变。

因此任务、场景、工具参数、独立评分、记忆规则和规划提示语义不变；改变的是有限平台上的移动安全联锁和拒因记账接线。历史 H0 不重跑，也不把旧 H0 说成已经经过新联锁。

完整前后哈希在 before_hashes.json / after_hashes.json；与本轮开始时相比的准确增量在 changes.patch（不依赖仓库中原有未提交的 memory v1 改动）。source_before/ 与 source_after/ 保留审计副本。

## 回放方法与证据边界

来源为 Plan A 重跑目录 runs/memory-v1-h2-search-budget-rerun-20261111-s0/，唯一 episode H2/20261111-152723-api-memory_ab_occluded_v1-s0-62de9d。

只读取其 events.jsonl 与 trajectory.jsonl，按每个移动前的上一份工具观测 sim_time_s 精确匹配控制轨迹的 GT pose（时间差小于 1e-7 s），将原指令交给同一个门控函数。未调用 MuJoCo、未执行旧动作、未新增 episode。原始输入文件 SHA256 写入 replay.json。

原第 99 次请求拒因：north，requested_distance_m=0.3，safe_distance_along_request_m=0，因为开始已在 0.35 m 余量区内，名义终点超出余量界约 0.262400 m。原边界 y=6 并未改变。

这验证“在记录的姿态下会拒绝致命请求”，不等于已经实测挡住一次跌落。原轨迹第 91 次就会被拒，真实启用门控后的后续路线将不同；对原第 94/97/99 步的判断只是逐姿态反事实检查，不是可连续执行的新路线。

复现（只离线）：

```text
.venv/bin/python runs/memory-v1-boundary-gate-offline-fix-20261111/verify_fix.py
.venv/bin/python -m pytest -q
./scripts/run_deepseek.sh --list-tasks
git diff --check
```

## 停止位置

第一部分全部验收通过。**未开始第二部分，等待用户明确说“继续”。** 没有 H2 新 metrics/memory 可以汇报，也没有用模型 finish 证明成功。之后若获准只跑一轮 H2，会先说明预计约 60–74 万 token，使用默认每决策最多 2 请求、120 次预算、seed 0；连续 5 次移动尝试都因边界被拒且无进展时提前停止。这些 API 运行与运行监控配置本次尚未启动。

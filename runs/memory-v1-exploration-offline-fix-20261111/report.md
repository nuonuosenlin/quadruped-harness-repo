# H2 只转不走：离线诊断与最小修复

2026-11-11，本地分支 `memory-v1`。本轮仅改记忆/规划层，未调用 API、读取真实密钥、运行 demo/消融、访问在线文档或修改共享文档，未 push。使用现有 `.venv`，未安装依赖。

## 结论

**move_relative 原本就允许无确认目标的探索计划，并没有被 task:A 前置条件堵死。** 已直接加载本轮存档的旧门控，在对象为空时提交 preconditions=[] 的 move_relative，校验通过。上一轮 0 次 move_relative 是规划器没有选择它。

可确认的结构问题是：旧计划恢复基本仍是扫视；scan_A 的 completion=[] 不会由规则自动完成；旧 skill_stuck 仅检测动作失败/执行反馈卡住，识别不了“转向成功但搜索没进展”。因此 89 次成功转向不会触发扫描停滞事件。旧提示虽然允许探索，却未规定扫视预算和必须换视点的恢复策略。

最小修复：增加六次成功转向的非阻断搜索停滞信号，并持续放进有界状态包；提示明确区分不依赖目标的 explore_viewpoint 和需要确认目标的 approach_A，给出移动探索格式，要求停滞时改变视点或说明不能移动后停止/中止。**不自动执行移动，不关闭门控，不编造通行空间。**

次要修复：B 的六条重定位中有三条是回到保留位置时仍对照异常 candidate_pose，导致重复反证。修正为否定待验证候选，并重新要求独立多帧确认。0.5 m 阈值不变；剩余三次新追踪点采样异常没有掩盖。

最终测试：**328 passed、15 skipped**（原 315 项通过，新增 13 项）。`--list-tasks` 和 `git diff --check` 正常。任务、场景、工具后端与评分语义未改，H0 不用重跑。

## 1. 逐条核对：是不是没有合法移动计划？

### 门控没有普遍要求确认目标

修复前代码完整存档在 source_before/。[旧 prepare](/home/nuonuosenlin/Agent-harness/runs/memory-v1-exploration-offline-fix-20261111/source_before/memory_planning.py:265) 的强前置条件检查仅遍历模型声明的条件：

```python
for check in goal["preconditions"]:
    result = predicate(check, state)
    if result is False:
        raise ValueError("Memory disproves a required precondition")
    if result is not True:
        raise ValueError("Precondition requires fresh confirmed evidence")
    # 随后仍检查快照时效、对象验证是否过期。
```

前面的要求是有效 plan/subgoal 绑定，而不是 move_relative 必须绑定某个 confirmed 对象。preconditions=[] 不会进入这个循环。旧提示也明确写了：

> Empty memory alone does not forbid exploration: use a valid new exploration plan with preconditions=[]

`verify_fix.py` 加载存档的旧 MemoryPlanningHarness，使用空对象快照和一个 forward_m=0.2 / lateral_m=0.0 的合法探索计划，门控反馈为 None。初次诊断证据还保存在 diagnosis_before.json、baseline_empty_precondition_memory.md。这只校验计划，不执行运动。

**结论：不需要放宽未知对象检查，也不需要取消门控。** 模型可以为搜索选择无对象依赖的探索移动；真正接近 A 时继续要求 confirmed task:A。

### 实际计划把恢复收敛到了继续扫视

旧 memory.md 中四个计划的恢复文本原样如下：

| plan_id | recovery |
|---|---|
| plan-0001 | observe and re-plan a safe scan |
| plan-0002 | observe, then continue safe scan or replan exploration |
| plan-0003 | observe current view, then continue safe scan or abort if no target appears |
| plan-0004 | stop, observe current view, then resume conservative scanning or abort if no target visible |

plan-0002 文字提过 replan exploration，但没有对应移动探索子目标。最终 plan-0004 的实际结构是：

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
  "branches": [{"on": "skill_stuck", "subgoal_id": "scan_A"}]
}
```

approach_A 等确认目标是合理的；缺的是“目标尚不可见时，移动改变视点”的搜索子目标。120 份输入中 A 候选始终为 0，实际响应选择了 turn 89、track_point 20、observe 10、get_geometry 1，没有选择 move_relative。

### 为什么 skill_stuck 恢复没有触发

[旧记忆规则](/home/nuonuosenlin/Agent-harness/runs/memory-v1-exploration-offline-fix-20261111/source_before/memory.py:271) 的条件是：

```python
if (action["tool"] in {"move_relative", "turn"} and action["status"] != "succeeded"
        or action.get("stuck") is True):
    self.event("skill_stuck", [eid])
```

旧适配器 stuck 也要求动作失败且返回位移很小。本轮工具全部 succeeded，所以这个条件没有触发；它只是在检查物理技能失败，没有检查搜索目标是否取得进展。

另外，[完成规则](/home/nuonuosenlin/Agent-harness/runs/memory-v1-exploration-offline-fix-20261111/source_before/memory.py:302) 要求 goal.completion 非空，才用测量判定进行中的子目标完成。scan_A 的 completion=[] 不会自动结束。替换计划、重新选点都能继续扫描，没有累计预算提醒。

旧提示唯一完整的原子运动参数例子是 [turn 扫视](/home/nuonuosenlin/Agent-harness/runs/memory-v1-exploration-offline-fix-20261111/source_before/memory_planning.py:29)，允许“safe scan/exploration action or abort”，但没有无进展时的切换条件。H2 同时只读结构化状态，不接收 H0 的完整 RGB/六轮历史；本轮并无完整通行空间表示。上述是可核对的接口、计划和反馈缺口，不等于能够从未保存的 reasoning 正文恢复模型每次选 turn 的内部理由。本报告不把提示示例认定为唯一因果原因。

## 2. 最小修复内容

只修改三个产品文件：

1. [memory.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory.py:335)：新增搜索进度规则。
   - 累计成功 turn 工具反馈；首次观察到新的任务候选/对象，或 move_relative 返回成功时重置。
   - 普通观察、重复追踪、重复看到同一个 B、替换计划，以及失败/去重的动作，都不会重置扫描预算。
   - 到六次时追加 search_stalled 账本、skill_stuck(reason=repeated_turns_without_search_progress) 和 replan_required(reason=search_stalled)。一个停滞周期只发一次，避免事件洪泛。
   - world.exploration 持续保留计数、阈值、stalled、动作证据 ID 与恢复方向。它不是强制执行器，不拒绝工具、不生成隐藏运动。
   - 成功移动工具返回只作为搜索策略进展信号，**不冒充实测位移**；不读取 motion_feedback 的仿真真值向量。转向时的机身漂移也不会清零扫描计数。
2. [memory_context.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory_context.py:51)：保留 world.exploration，正常与重试的有界投影都能读到，避免被大量 B 状态事件淹没。顶层八字段和 12000/6000 字符上限不变。
3. [memory_planning.py](/home/nuonuosenlin/Agent-harness/go2_demo/memory_planning.py:57)：补齐规划侧契约。
   - explore_viewpoint 可以 preconditions=[]；approach_A 仍要求 confirmed task:A。
   - 不要为了发现 A，反过来把“已看到 A”设为探索移动的前提。
   - 明确停滞时不能再只复制扫描计划，应据当前几何选择短距离 move_relative，再检查新视点；若几何不足则补测，仍不能支持移动时停止/中止，不能继续无限转圈。
   - 完整运动格式例子改为移动探索，而不是只有转向例子；其中 0.2 m 只是参数格式示例，不能被当作通行证据。

规划仍负责显式选择计划、分支和原子指令参数；记忆只给规则信号。未知/预测/过时对象没有获得强前置条件权限。没有新增 GT、地图、语义检测器或路径规划器，也没有修改工具后端。真实移动方向仍需当前观测支持；本次最小修复不宣称已解决全部空间感知问题。

## 3. B 六条重定位的来源及有限修复

六条全部发生于新 track_point 选择，不是同一追踪点连续漂移。旧 TaskLabelRGBD.associate 仅以当前有效点、像素落在颜色组件内、深度有效等条件关联任务标签；新 point_id 的采样不会通过 PointTracker 的跨帧同点几何跳变检查。

| step | 原账本 ID | 新 point_id | 新位置距保留位置 | 分类 |
|---:|---|---|---:|---|
| 6 | e000035 | point-003 | 0.908664 m | 新采样大跳变 |
| 20 | e000100 | point-004 | 0.012373 m | 回到保留位置，却仍比较异常候选 |
| 66 | e000323 | point-011 | 1.071976 m | 新采样大跳变 |
| 78 | e000381 | point-012 | 0.016407 m | 回到保留位置，却仍比较异常候选 |
| 80 | e000397 | point-013 | 1.855486 m | 新采样大跳变 |
| 82 | e000412 | point-014 | 0.280371 m | 回到保留位置附近，却仍比较异常候选 |

旧规则使用 `reference = obj.get("candidate_pose") or obj["pose"]`，但 target_relocated.old_pose 记录的是保留 pose。一次异常先设置 candidate_pose；下次正常点回到保留位置，即便只差 1–2 cm，仍可能距异常 candidate 超过 0.5 m，于是又生成“重定位”。因此不是把 0.5 m 调大就能正确解释六条事件。

[本次修正](/home/nuonuosenlin/Agent-harness/go2_demo/memory.py:191)：若当前高置信观测接近保留位置、且推翻待验证候选，则追加 relocation_candidate_rejected、清除 pending candidate、清空其确认支持，按新独立帧重新建立确认。首个返回帧仍是 unknown，第二个独立帧才可 confirmed；已失效的依赖子目标不会自动恢复。若新位置持续被独立观测支持，真正的重定位仍能被确认。阈值保持 0.5 m。

**未修掉的三条**：point-003/011/013 分别带来 0.91/1.07/1.86 m 的新采样跳变，显然不是阈值附近的微小抖动。它们属于跨追踪点提升为同一 task:B 时的位置不一致。旧日志有选点像素及 RGB-D 单点位置，没有整帧深度邻域，不能进一步可靠区分边缘深度采样、颜色组件关联或选点位置问题；本轮没有改感知算法来掩盖这些异常。

干扰量化：旧 MD 有 6 条 positive_position_contradiction 和 24 条 verification_expired 重规划事件，合计 30；其中 task:B 共 12 条，其余是 18 个普通地标失效。120 次输入中，110 次带过 replan_required。key_precondition_invalidated 为 0，四个扫描计划没有依赖 B，因此这些事件没有把移动门控硬性锁住。它们会占用上下文，但仅凭一轮记录不能量化对模型决策的因果影响。

## 4. 离线重放与测试

`verify_fix.py` 只把旧工具反馈、适配器观测、公开当前候选和计划送入旧/新 MemoryRules；不创建 MuJoCo，不执行旧工具指令，不重演物理轨迹，也不调用模型。

| 同一旧数据重放 | 修复前规则 | 修复后规则 |
|---|---:|---:|
| B target_relocated | 6 | 3 |
| relocation_candidate_rejected | 0 | 3 |
| 搜索停滞 skill_stuck | 0 | 1 |
| 首个 search_stalled | 无 | step 10 |
| 位置反证 replan_required | 6 | 3 |
| 失效超时 replan_required | 24 | 24 |
| 搜索停滞 replan_required | 0 | 1 |

step 10 对应旧序列第六次成功转向；新的动作会随模型响应而改变，所以这不是一轮新任务结果。真实异步循环仍只读最新已发布快照，没有新增中途 flush/等待。

新增 13 项离线用例覆盖：

- 成功扫视仍可触发搜索停滞；观察、重新选普通地标、换计划不能清零，单周期只发一次。
- 失败或去重移动不能清零，即使记录里塞入很大的仿真位移诊断也不采用；成功工具返回或首次新任务候选可重置，候选不会因此成为 confirmed。
- 状态投影在事件噪声与重试缩减后仍保留停滞信号，字符上限不变。
- 合成规划器读取 stalled 上下文，返回 move_relative + 无目标依赖探索计划；经真实 API 解析器、记忆门控和伪后端完整链路可执行。该响应来自本地 MockTransport，不是实际 LLM。
- 停滞时未知 task:A 仍不能作为强前置条件；无对象依赖的探索计划可通过。
- 返回原位置的候选恢复、跨 stale 间隔恢复、多帧重新确认、依赖目标不自动复活，以及持续新位置仍可确认重定位。

验证结果：

```text
.venv/bin/python -m pytest -q
328 passed, 15 skipped

./scripts/run_deepseek.sh --list-tasks
正常；memory_ab_occluded_v1 仍为 supported

git diff --check
通过
```

离线测试证明状态、协议、门控和规则恢复路径可用，不能证明真实 LLM 下次一定会选移动或任务一定通过。本轮按要求没有 API、demo 或消融。

## 文件与 H0 可比性

产品改动仅 `go2_demo/memory.py`、`go2_demo/memory_planning.py`、`go2_demo/memory_context.py`。新增测试 `tests/test_memory_exploration.py`，原有测试未删改。

before_hashes.json 与 evidence.json.after_hashes 可逐文件核对；scenarios.py、backend.py、harness.py、ordered_evaluation.py、runner.py、models.py、__main__.py、memory_perception.py 等均与本轮开始时相同。H0 不启用记忆，不走本次新规则；默认入口、任务、场景、原子工具后端语义与独立评分完全未变。**历史 H0 不需要重跑。**

本目录：report.md、diagnosis_before.json、evidence.json、before_hashes.json、source_before/、replay_memory.md、verify_fix.py、pytest.txt、list_tasks.txt，以及基线合法性校验生成的记忆文档。旧运行文件未修改。

离线复现：在仓库下执行 `.venv/bin/python runs/memory-v1-exploration-offline-fix-20261111/verify_fix.py`。已停在离线修复与验证阶段。

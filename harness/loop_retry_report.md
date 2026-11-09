# LIBERO touch/adjust 闭环补测报告

日期：2026-10-28（Asia/Shanghai）。用户在首次预算停止后明确授权修复并额外运行 1 次。本次只新增 1 个 episode，没有自动重试。

## 结论

**最小 LLM 闭环与指定距离子任务均通过。** 最终实际 EEF 到汤罐可见表面关键点距离 **0.0220016774 m（2.20cm）≤3cm**。成功来自最后一次 env.step 后的新观测和本地 check_success，不是规划目标或模型口头判断。

- 实际请求/返回模型：qwen3.8-flash；端点为 https://dashscope.aliyuncs.com/compatible-mode/v1。
- 9 个 LLM 决策步/API 请求，4 条轨迹，117 个动作控制步（另有初始 10 个零动作稳定步）。
- 本次输入 9,093 tokens，输出 410 tokens，**合计 9,503 tokens**。
- 授权限制：最多 12 个决策步，累计 15,000 tokens；本次未触发上限。
- 仿真与调用总用时约 39.08 秒。
- 初始距离 22.49cm，最终距离 2.20cm。
- 原始 BDDL success=false；不声称完成物理接触、抓取或两物装篮。
- 本次未发生重复错误、非法阶段调用或无进展停止。

先前首次失败使用 26,253 tokens；两次仿真闭环共 35,756 tokens。另有纯 API 测试 456 tokens，整个阶段合计 36,212 tokens。这里只新增本次 9,503 tokens。

模型标识此前通过认证 /models 列表核验，未见 qwen3.8-flash-next；控制台 UI 未核验，不将 API 结果描述为控制台确认。

## 修复内容

1. protocol.py 持久保存 track / plan / execute 阶段、执行次数和待执行轨迹 ID。执行一次后，后续合法规划关系固定为 adjust。
2. 每次请求保留上一轮标准 assistant tool_calls 与 role=tool 结果，并附当前观测及持久 workflow 摘要；移除每轮重新开始的提示方式。
3. 动态限制各阶段可用工具和参数；执行工具只能接受当前待执行轨迹 ID。模型仍负责发出 function call，本地负责几何、IK 和 OSC 动作。
4. 相同错误累计两次或连续两次调用无阶段进展时停止，避免重复调用消耗预算。
5. 限制改为 12 步 / 15,000 tokens；保留原 384 completion tokens/请求、纯文本传输和不自动重试策略。

本次策略由 harness 阶段合同约束，并非完全开放的自主任务规划。没有训练模型或新增动作头。几何目标、深度反投影、IK、OSC 控制与原 3cm 判据沿用首次实现，未通过放宽成功条件获得通过。

## 每步日志摘要

| 步 | 工具/关系 | 结果 | 校验距离 cm | 本步 tokens |
|---|---|---|---:|---:|
| 1 | track_keypoint | 汤罐表面关键点 | 22.49 | 868 |
| 2 | solve_constraint / touch | traj_001 | 22.49 | 1223 |
| 3 | execute_trajectory | 46 控制步 | 14.70 | 982 |
| 4 | solve_constraint / adjust | traj_002 | 14.70 | 1162 |
| 5 | execute_trajectory | 29 控制步 | 9.90 | 981 |
| 6 | solve_constraint / adjust | traj_003 | 9.90 | 1162 |
| 7 | execute_trajectory | 24 控制步 | 5.14 | 981 |
| 8 | solve_constraint / adjust | traj_004 | 5.14 | 1163 |
| 9 | execute_trajectory | 18 控制步，距离判据成功 | 2.20 | 981 |

check_success 每步由本地主循环自动调用；本次 LLM 主动选择了其余三个工具，没有主动调用 check_success。这不影响其接口实现或观测闭环，但不能声称 LLM 在本次选用了四种工具。

## 独立核验

修复后的 8 项离线检查通过，覆盖原几何计算、动态阶段关系、当前轨迹 ID 约束、共享 schema 不被修改、重复调用保护、12 步 / 15,000 token 预算及图像消息拒绝。

随后 audit_run.py 对保存记录做离线审计并通过，未调用 API 或初始化仿真：

- 核对 9 个请求/响应的实际模型、token 求和、文本消息类型与无多模态字段。
- 核对标准 assistant/tool 上下文与前一步真实结果一致，阶段合同和轨迹 ID 合法。
- 核对 117 个动作为有限数值、7 维、范围 [-1,1]，夹爪保持开启。
- 用最终保存深度、mask、K/T 重建关键点，再与最后一个实际 EEF 控制记录算距离，得到 0.02200167741224471 m，与最终判定一致。
- 核对运行时源码快照 SHA256。首次失败记录与原版源码仍保留。

## 仿真特权信息及边界

使用实例 mask 真值及名称映射/bbox、模拟器米制深度和相机 K/T、机器人 EEF/关节状态、MuJoCo 运动学模型和独立 BDDL 判断。未用物体位姿真值生成目标关键点。视觉全部在本地；9 个请求均只发送文本与数值坐标，RGB/深度/mask 不发送给模型。

跟踪仍是基于可见表面和初始锚点的最小关联实现；尚不能替代真实 Geometry Tracker。IK 在独立 MjData 上规划，OSC_POSE 通过 env.step 执行；没有完整碰撞规划、物理接触保证或最终姿态残差独立验收。

collinear/parallel 只有纯几何离线检查通过，轴关键点与机器人轨迹执行仍未验证。完整装篮、BEHAVIOR 接入、真实视觉替换及遮挡处理待后续开展。本次不依赖 BEHAVIOR 家庭资产，没有下载资产、安装依赖、升级环境、接真机或修改飞书。

## 代码与证据

代码与说明位于 D:\RoboHarnessSim\harness，所有新增文件/缓存仍在该根目录。D 盘结束时约余 41.02 GiB，高于 10 GiB 保留线。未修改官方仓库核心或已验证探针。

复跑单次 episode（会产生新的 API 费用；本报告完成后没有再执行）：

```powershell
& 'D:\RoboHarnessSim\harness\run-libero-loop.ps1'
```

本次结果：runs/touch_20261028_203317/result.json。
逐步日志：同目录 steps.jsonl；动作日志 simulation.jsonl；轨迹 traj_001.json 至 traj_004.json；独立审计 audit.json；运行源码 source/ 和 source_manifest.json；本地前后图像与几何数据 before/after_rgb.png、before/after_geometry.npz。

首次失败：runs/touch_20261028_202556/，详见 loop_report.md；原版源码已补存于其 source/。

仅复查已保存结果（不调用 API、不跑仿真）：

```powershell
. 'D:\RoboHarnessSim\scripts\env.ps1'
& 'D:\RoboHarnessSim\envs\libero\python.exe' -B 'D:\RoboHarnessSim\harness\audit_run.py' 'D:\RoboHarnessSim\harness\runs\touch_20261028_203317'
```

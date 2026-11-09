# Quadruped Harness Reproduction

目前实现的仿真与最小 LLM 闭环复现。

**基于 LIBERO / BEHAVIOR，新增自研 harness 与千问 API 闭环。** LLM 只负责决策；本地工具处理视觉几何、IK 和仿真动作。不训练模型，不新增动作头，不向 LLM 发送图像。

touch+adjust 量化 10/10（初始状态索引 0-9，预算 12 步/15000 tokens），抓取单步验证 3/4（单一初始状态索引 0，预算 20 步/30000 tokens），BDDL 仍为 false，搬运/释放/番茄酱未做。

## 已验证与待完成

| 内容 | 状态 |
|---|---|
| LIBERO 官方 demo、RGB-D、实例 mask、动作接口 | 已验证 |
| BEHAVIOR v3.9.1 empty/Fetch demo 和感知/动作探针 | 已验证；仅机器人资产 |
| 百炼 qwen3.8-flash 普通对话与 function call | 已验证 |
| LIBERO touch + adjust 距离子任务 | 已验证：9 个决策步、4 条轨迹、117 个控制步，距离 2.20cm ≤3cm，9,503 tokens |
| 汤罐抓取、提起与保持 | 单步验证 3/4，包含一次接近阶段工具调用缺失 |
| 装篮、消融实验 | 待完成 |
| BEHAVIOR 家庭任务、四足机器人任务、真机适配 | 待完成 |


## 上游项目与固定版本

| 项目 | 来源 | 本次版本 |
|---|---|---|
| LIBERO | https://github.com/Lifelong-Robot-Learning/LIBERO | commit `8f1084e3132a39270c3a13ebe37270a43ece2a01` |
| BEHAVIOR-1K | https://github.com/StanfordVL/BEHAVIOR-1K | v3.9.1，commit `26f2c7ef7b9cf96bd0414f81e1e751e493762779` |
| robosuite / MuJoCo | https://github.com/ARISE-Initiative/robosuite / https://github.com/google-deepmind/mujoco | 1.4.0 / 2.3.7 |
| RoboHarness（参考目标） | https://github.com/BinceQu/RoboHarness | 参考其接口及仿真依赖；未声称完整复现其端到端基准 |

本仓库不包含上述官方源码树、资产或第三方安装包。来源与许可证边界见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 目录

```text
harness/   千问客户端、四个工具、阶段协议、闭环与离线测试
scripts/   启动器、最小依赖、历史版本快照、Windows 补丁、密钥检查
reports/   仿真搭建报告、闭环补测报告与整理检查记录
```

代码仓库放在 `D:\quadruped-harness-repo`；原仿真工作区仍在 `D:\RoboHarnessSim`。环境、上游源码、资产、缓存与运行输出留在原工作区，均不提交。选定运行的 JSON 已备份到 docs/evidence/，清单及 SHA256 见 docs/evidence/manifest.json。图像、视频、深度/分割数组和逐控制步 JSONL 未备份，报告中的其他历史路径仍指向原机器。

## 复跑：已有环境

在仓库根目录打开 PowerShell。以下命令使用现有 D 盘环境，不重新安装：

```powershell
. .\scripts\env.ps1
& 'D:\RoboHarnessSim\envs\libero\python.exe' -B .\harness\test_offline.py
```

复跑官方示例或探针（每次只启动一个仿真）：

```powershell
& .\scripts\run-libero.ps1 -Mode all
# 如需检查 BEHAVIOR 最小环境，另行运行：
# & .\scripts\run-behavior.ps1 -Mode all
```

API 密钥由运行者自行设置环境变量 `DASHSCOPE_API_KEY`。代码只读环境变量；不要将密钥写入脚本、命令示例、配置文件或提交记录。

```powershell
# 下面两条会产生 API 调用；按需要手动执行，不会自动重试。
& .\harness\run-api-probe.ps1
& .\harness\run-libero-loop.ps1
```

端点：`https://dashscope.aliyuncs.com/compatible-mode/v1`。历史实测模型为 `qwen3.8-flash`，由认证模型列表和实际响应核验，未核验控制台界面。API 探针按既有规则选择精确可用标识；闭环读取最新一次 API 探针结果，结果未通过则停止。

闭环最多 12 个决策步、15,000 tokens；每次输出最多 384 tokens。相同错误累计两次或连续两次无阶段进展即停止。所有运行结果写入 `D:\RoboHarnessSim\harness\runs`。仓库启动器调用本仓库代码，运行时源码快照也取自本仓库。

## 新机器环境准备

这是 Windows 适配记录，不是一键通用安装器。本次仓库整理没有重新安装或重新调用 API/仿真。已验证运行数据来自原工作区；仓库副本仅调整启动路径、API 结果发现及源码快照位置，并进行离线检查。

1. 准备 Git、micromamba 和 D 盘工作目录；micromamba 可按[官方安装说明](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#windows)放在 `D:\RoboHarnessSim\tools\Library\bin\micromamba.exe`。不要使用系统默认 Python 替代独立环境。
2. 下载 LIBERO 官方源码并固定版本（已有对应目录时跳过，勿覆盖已有安装）：

   ```powershell
   git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git D:\RoboHarnessSim\LIBERO
   git -C D:\RoboHarnessSim\LIBERO checkout 8f1084e3132a39270c3a13ebe37270a43ece2a01
   ```

3. 加载 `scripts/env.ps1`，确认空间。下载/安装需核算峰值体积，并至少保留 10GiB。`scripts/setup-libero.ps1` 记录了 Python 3.8.13、仿真依赖子集、editable 安装和 Windows 补丁步骤；它会安装软件，只在新环境准备时手动运行。完整历史包版本见 `scripts/libero-freeze.txt`，不要把旧 freeze 当作跨机器无条件可安装的通用锁文件。
4. 确认 `D:\RoboHarnessSim\home\.libero\config.yaml` 的路径正确。仓库提供 `scripts/libero-config.example.yaml`；仅在配置不存在时按示例创建，勿覆盖已有配置。没有下载训练演示数据。
5. BEHAVIOR 最小环境使用独立 Python 3.11.18、Isaac Sim 5.1.0.0、Torch 2.7.0+cu126 和机器人资产。安装过程与已知冲突见[仿真报告](reports/simulation_report.md)，依赖记录在 `scripts/behavior-*.txt`。BEHAVIOR 的 freeze 含原机器 wheel 路径，不可直接视为可移植 requirements。NVIDIA 软件许可须由运行者自行阅读和接受；empty 启动器会设置 EULA 接受标记。家庭数据许可与解密 key 尚未申请/获取，家庭资产未安装。

本仓库未打包 BEHAVIOR 的完整自动安装流程。现有环境有明确的兼容补丁和依赖声明冲突，不应随意升级。新机器上是否可复现相同结果仍需实际验证。

## 本人新增的 harness

- `track_keypoint(bbox, name)`：mask + 米制深度反投影，得到可见表面关键点；视觉始终在本地。
- `solve_constraint(A, B, relation)`：touch/adjust 几何目标、独立 MuJoCo 状态上的数值 IK、局部轨迹。
- `execute_trajectory(traj)`：校验当前轨迹 ID，通过 7 维 OSC_POSE 执行。
- `check_success()`：重新观测并校验 3cm 判据，单独返回原始 BDDL 结果。

阶段协议持久记录 track/plan/execute，保留上一步标准 assistant/tool 消息，首次执行后只允许 adjust。本次成功运行中，check_success 由主循环每步自动调用，LLM 未主动选择该工具。

## 报告与提交前检查

- [仿真搭建报告](reports/simulation_report.md)
- [闭环补测报告](reports/loop_retry_report.md)：含首次失败、阶段修复和 9 步成功记录



## 2026-11-09 代码与证据备份

工作副本 harness 的文件按原内容同步，包含 -InitialStateIndex、-Grasp、grasp_lift、cli_args/tool_args 隔离和仅抓取模式的 20 步/30000 tokens 预算。默认接近模式仍为 12 步/15000 tokens。仓库中保留了工作副本原有的 D:\RoboHarnessSim 路径和固定 API preflight 路径。删除原工作区后，需要重建环境、资产及路径，并将备份的 API preflight 结果恢复到预期位置后才能运行。

抓取三次通过均为相同初始状态。第四次在接近阶段因未返回工具调用而中止。保留了 args 覆盖中止轮、旧预算中止轮与新预算下四轮结果。备份未重新运行仿真或调用模型。

[完整备份清单](docs/evidence/manifest.json) 包含每个已复制文件的路径、字节数及 SHA256。缺少原始图像和深度数组时，无法独立重做全部几何审计。

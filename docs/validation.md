# 验证记录

**当前入口已切换为仅 API、固定开启思考。** 下方早期 Windows、规则策略和非思考 API 结果均为历史记录；其中的旧模式命令不适用于当前版本。最新接入验证见本文末尾“仅 API 与思考模式验证”。

日期：2026-10-27。测试在本地 Windows、Python 3.11.5 下完成；未连接物理机器人，未调用真实大模型 API。

核心版本：MuJoCo 3.2.5、PyTorch 2.5.1+cpu、NumPy 1.26.4、OpenCV 4.11.0、Pillow 11.3.0。项目以 editable 方式安装成功。21 个固定版本资产全部通过 SHA-256 校验。Ubuntu 的 EGL / OSMesa 和桌面 viewer 尚未在目标电脑验证。

## 自动测试

```bash
python -m pytest -q
```

结果：**65 passed**。覆盖 Chat Completions 请求与图像格式、完整工具历史、超时和脱敏、RGB-D 回投和姿态变换、丢点、过期图像、参数限幅、调用去重、独立评分，以及异常退出后的停止与资源释放。

HTTP 测试使用注入的测试传输，不消耗模型 API，也不能证明任一具体模型的视觉／工具能力。

## 真实物理仿真闭环

```bash
python -m go2_demo --mode scripted --seed 0 --runs-dir runs/validation-final
python -m go2_demo --mode scripted --seed 1 --runs-dir runs/validation-final
python -m go2_demo --mode scripted --seed 2 --runs-dir runs/validation-final
```

下表使用真实 Go2 关节动力学、已有步态策略、渲染图像和深度。规则策略只从 RGB 选取红色目标，再通过公开工具获取几何反馈；评测器的目标真值不进入策略。

| 种子 | 结果 | 决策轮数 | 最终中心距离 | 朝向误差 | 仿真耗时 |
| --- | --- | --- | --- | --- | --- |
| 0 | 成功 | 8 | 1.156 m | 0.062 rad | 16.98 s |
| 1 | 成功 | 8 | 1.156 m | 0.050 rad | 17.30 s |
| 2 | 成功 | 8 | 1.158 m | 0.063 rad | 16.52 s |

三次都确认停止，未记录跌倒或红／蓝障碍碰撞；每轮工具均返回成功。机载相机初始和最终图像已检查。验收距离为 1.0±0.18 m，详细阈值见 [运行说明](demo.md)。这三个小范围场景仅是冒烟验证，不构成模型能力或通用导航成功率统计。

原始日志分别位于：

- [种子 0](../runs/validation-final/20261027-172647-scripted-s0-699041/metrics.json)
- [种子 1](../runs/validation-final/20261027-172646-scripted-s1-3935e1/metrics.json)
- [种子 2](../runs/validation-final/20261027-172647-scripted-s2-26491a/metrics.json)

`runs/` 默认被 Git 忽略，复制项目时需自行保留这些验证证据。

## 预算退出

```bash
python -m go2_demo --mode scripted --seed 0 --max-sim-seconds 1
```

实测返回 `budget_exhausted`，进程退出码为 1，成功标记为 false，最终停止确认成功。停止收敛会消耗额外的短段仿真时间，预算到期后仍执行停止，不继续执行新的任务动作。

## 环境适配与局限

本机旧 Anaconda 环境加载 MuJoCo 3.2.7 和 3.3.7 的插件 DLL 时失败，3.2.5 可以正常导入，因此项目锁定 3.2.5。中文路径通过内存加载网格和 TorchScript 处理。

调试早期，种子 2 的一次小位移因原 4.5 cm 到达阈值触发超时；原记录保留于 `runs/backend-validation/`。根据低速策略的实际跟踪能力，将进入停止收敛的平移阈值校准为 6 cm，停止后的 10 cm 验证阈值保持不变；上表为校准后、最终代码下的重测结果。所有动作仍返回实测误差，超时不会被改写成成功。

尚未验证：真实模型 API、真实 Go2、实时运行模式、姿态控制、复杂地形、传感器噪声与里程计漂移。

## WSL2 运行环境验证（2026-10-28）

本次在当前 WSL2 / Ubuntu 24.04.4 LTS 工作区完成安装与实测。系统自带 Python 3.12.3；通过已有的 `uv` 在用户目录安装 Python 3.11.15，并创建独立 Linux `.venv`。原有 Windows `.venv` 保留为 `.venv.windows-backup/`，没有复用其中的 Windows 包。

核心版本：MuJoCo 3.2.5、PyTorch 2.5.1+cpu、NumPy 1.26.4、OpenCV 4.11.0.86、Pillow 11.3.0、HTTPX 0.28.1、pytest 8.4.2。项目通过 `pip install -e '.[test]'` 安装，CPU 版 PyTorch 与此前 Windows 验证版本一致。

本机已有 WSLg、可连接的 X11 显示及所需 GL/X11 动态库，直接使用默认 GLFW。以下命令均在项目目录执行：

```bash
.venv/bin/python -m pip check
.venv/bin/python -m pytest -q
.venv/bin/python scripts/fetch_assets.py --verify
env -u MUJOCO_GL .venv/bin/python -m go2_demo --mode scripted --seed 0 --runs-dir runs/wsl-validation/glfw
env -u MUJOCO_GL .venv/bin/python -m go2_demo --mode scripted --viewer --seed 0 --runs-dir runs/wsl-validation/viewer
```

依赖检查通过，**65 项测试全部通过**，**21 个固定资产全部通过 SHA-256 校验**。真实物理闭环结果如下，两次都经过 8 轮决策并以 `finish` 正常结束，确认停止，没有跌倒或障碍碰撞：

| 运行方式 | 结果 | 最终中心距离 | 朝向误差 | 仿真耗时 | 墙钟耗时 |
| --- | --- | --- | --- | --- | --- |
| GLFW，无第三人称窗口 | 成功 | 1.155 m | 0.061 rad | 16.98 s | 1.88 s |
| GLFW，WSLg viewer | 成功 | 1.154 m | 0.038 rad | 16.66 s | 18.89 s |

运行日志：[默认 GLFW](../runs/wsl-validation/glfw/20261028-173748-scripted-s0-9cc010/metrics.json)、[WSLg viewer](../runs/wsl-validation/viewer/20261028-173800-scripted-s0-1418c6/metrics.json)。viewer 最终机载相机图像已检查，红色目标和白色十字正常渲染。viewer 在任务结束后自动关闭。

本次 GLFW 无窗口运行仍使用 WSLg 显示连接；没有验证完全无显示服务器的 EGL / OSMesa。本次运行均为 `scripted` 工程验证，没有调用真实模型 API。

安装时发现当前 shell 的小写 `http_proxy`、`https_proxy`、`all_proxy` 指向不可达代理，而大写代理可用。本次安装通过 `env -u http_proxy -u https_proxy -u all_proxy ...` 临时移除小写变量。若在同一 shell 中继续安装依赖并遇到代理超时，可使用：

```bash
env -u http_proxy -u https_proxy -u all_proxy .venv/bin/python -m pip install -e '.[test]'
```

## QUARD 样本接入验证（2026-10-28）

从官方 QUARD 固定版本提取了五类 15 个任务的小样本，共 60 帧、255 个文件、1,386,042 字节。逐文件 SHA-256 校验通过；新增 43 项数据下载和加载单元测试、15 项真实数据回归测试。完整运行 `python -m pytest -q` 的结果为 **123 passed**，没有跳过真实数据测试。

`python -m go2_demo.quard --report runs/quard/report.json` 验证了全部 15 段四帧时序窗口及原始控制标签。该报告只记录数据接入的有效性，不记录导航成功率，也不作为论文未公开的 Uv／Ul 划分复现。数据范围和重跑命令见 [QUARD 测试说明](quard.md)。

## DeepSeek 真实 API 验证（2026-10-28）

已接入工作区上一级目录的 `deepseekapi.txt`。密钥按单个凭据读取，文件权限设为 `600`，并添加忽略规则；运行命令、代码、清单和日志不记录密钥值。文件密钥也参与统一错误脱敏。通用模式额外支持 `MODEL_API_KEY_FILE` 和显式 `--api-key-file`。

使用官方端点 `https://api.deepseek.com` 和 `deepseek-flash`，通过 `thinking={"type":"disabled"}` 关闭思考，以匹配当前工具历史格式。官方模型列表实测返回 HTTP 200，声明该模型支持文本和图片。随后发送真实仿真相机图像与工具定义，返回 HTTP 200，正确报告红色目标及其中心像素；像素落在图像中的红色标记范围内。探针记录见 [probe.json](../runs/deepseek-validation/probe.json)。

从项目目录运行：

```bash
./scripts/run_deepseek.sh --seed 0 --max-model-calls 20 --max-wall-seconds 180 --runs-dir runs/deepseek-validation/episodes
```

成功记录为 [20261028-180730-api-s0-a7ca59/metrics.json](../runs/deepseek-validation/episodes/20261028-180730-api-s0-a7ca59/metrics.json)：

| 指标 | 实测结果 |
| --- | --- |
| 模式／模型 | `api` / `deepseek-flash`，真实模型请求 |
| 最终判定 | `success=true`，`termination=finish` |
| 决策调用／实际运动 | 9 次／5 次 |
| 最终目标中心距离 | 1.128 m |
| 朝向误差 | 0.0314 rad |
| 最终速度 | 0.00422 m/s，确认停止 |
| 仿真／墙钟耗时 | 14.62 s／9.65 s |
| 碰撞／跌倒 | 均为 false |
| Token 用量 | 输入 28,907，输出 602，总计 29,509 |

模型的两次移动请求超过 0.6 米向量长度限制，均被工具校验拒绝；模型读取反馈后自行调整，最终通过独立评分。没有放宽动作限制或评分阈值。

首次 API 闭环在转向后遇到本地序列化错误，原始失败记录保留在 [20261028-180512-api-s0-437751](../runs/deepseek-validation/episodes/20261028-180512-api-s0-437751/metrics.json)。原因是跌倒检测返回 NumPy 布尔值，运动后该类型进入 API 观测；已将后端状态统一为 Python 布尔值，并加入 5 项正常姿态、跌倒和非有限状态的 JSON 回归测试。修复后重跑得到上表结果。

最终全套测试为 **143 passed**。项目文本和运行日志的密钥扫描未发现凭据值。以上为单个种子的 API 接入与闭环冒烟验证；仿真仍在模型等待期间暂停，不属于论文 QUARD 成功率或实时控制复现。

## 新场景闭环接入（2026-10-28）

新增 13 个实际可运行的 MuJoCo 场景：3 项不同颜色物体到达、3 项 A/B/C 字母辨别、4 项家具绕障、3 项门框穿越。场景有独立几何、指令和评分，`--task` 选择单项，`--suite quard-planar` 批量执行。DeepSeek 启动脚本未指定任务时默认运行蓝色球体；`--list-tasks` 可查看全部样例。原始场景仍可用 `--task red_marker` 单独运行。

所有 13 个新场景均已运行真实物理闭环。种子 0、每项 25 轮预算下，规则策略通过 9/13，DeepSeek 通过 1/13（红色三角形门框）；两项爬行因不支持姿态控制而跳过，没有计入成功。实际失败包含预算退出、碰撞和距离未合格，没有将未运行或未声明完成的任务算为通过。

新增场景构建、目标选择、穿门轨迹评分、运行入口和批次统计的回归测试。当前全套结果为 **185 passed**，字母 B 的 WSLg 窗口模式也验证通过。任务列表、真实批次汇总与命令见 [新场景测试](scenarios.md)。本次场景是在现有 Go2/MuJoCo 中制作的改编任务，未声称复现原始 Isaac Gym 场景或论文划分。

## 仅 API 与思考模式验证（2026-10-28）

按新的运行要求，已移除规则策略、颜色／字母规则决策器及关闭思考的运行入口。机器人决策仅使用 API；DeepSeek 请求固定发送 `thinking={"type":"enabled"}`。默认输出预算为 8192 token，单次 API 超时为 90 秒。缺少凭据时明确报错，不切换为本地规则策略。单元测试的注入模型和 QUARD 离线数据校验继续用于验证代码与数据，不属于机器人决策模式。

适配器完整保留每个响应的 `reasoning_content` 和助手消息，并在后续请求中回传当前历史窗口内的完整消息。思考内容只在进程内用于后续 API 请求；日志记录长度与是否存在，不记录原文。新增回归测试覆盖长思考内容、多轮回传、完整历史窗口、缺失思考字段、截断响应、禁止关闭思考及仅 API 入口。

本次完整测试结果为 **209 passed**。真实验证命令：

```bash
./scripts/run_deepseek.sh --task go_through_red_triangle_tunnel --max-model-calls 20 --max-wall-seconds 300 --runs-dir runs/thinking-validation
```

实测连续 12 次 API 响应均含有思考内容，未发生历史回传或 HTTP 协议错误；累计思考长度为 12,425 字符，墙钟耗时 37.78 秒，输入 67,684 token、输出 4,041 token、总计 71,725 token。清单确认 `thinking.type=enabled`、`max_output_tokens=8192`。

该次场景最终判为 **失败**：模型过早调用 `finish`，机身停在门框前，尚未穿过开口或到达出口区域。停止确认成功，未碰撞、未跌倒。该结果说明思考 API 的多轮连接已正常工作，不意味着穿门能力验证通过。记录见 [thinking metrics](../runs/thinking-validation/20261028-184825-api-go_through_red_triangle_tunnel-s0-88626c/metrics.json)。

### 穿门失败的离线诊断

将该次记录的全部工具调用在相同场景、策略和物理后端中离线重放，最终位置及评分与原记录完全一致。重放证据见 [replay.json](../runs/passage-diagnosis/replay.json)。

- 机身最终前向坐标为 2.11924 m，轨迹最大值也只有 2.12905 m；门框平面在 2.2 m，因此机身始终没有穿过门。模型随后依次调用 `stop` 和 `finish`，结束不是由预算或执行异常触发。
- 相机安装在机身前方 0.32 m。重放中第四次移动后，相机坐标已达 2.43886 m，而机身只有 2.11850 m。最终图像看不到门框；相机视野中的通过不能证明机身或整机通过。门框还会在相机接近时离开视场，因此单凭“门不在画面中”不能判定完成。
- 四次请求均为前进 0.6 m，实际分别前进约 0.528、0.532、0.531、0.531 m，合计 2.12157 m。每次位置误差约 0.07 m，在允许的 0.10 m 范围内，因此工具返回成功；应按反馈中的实测位移判断进度，不能将请求的 2.4 m 当作已完成位移。
- 两个门框跟踪点在前两次移动后均失效。后续一次选点落在远处地板，另一次选中黑色背景并深度失败。出口后的白十字参照点持续有效，但没有新的可靠门框测量来支持完成声明。

任务接口也存在需要明确的内容：提示只写“到达门框另一侧后停止”，评分额外要求机身到达门后 0.8 m 的停止区域；观测没有明确公开相机前置偏移，工具说明也未强调动作成功允许位置误差。这些说明缺口可能增加误判，但由于未保存思考原文，不能据此断言模型具体采用了哪一种错误推理。本次机身连门框平面都未越过，失败判定本身成立。

本次诊断没有改变场景、控制器、提示词或评分；优先修正方向是公开机身／相机参考关系、实际位移语义及穿门后的停止余量，再验证模型是否会基于测量确认通过。

## 穿门观测与完成条件修复验证（2026-10-28）

已按诊断修正模型接口：公开从 MuJoCo 模型读取的相机／机身标定、相对本轮起点的实际机身里程计，以及从原有评分条件派生的门后 0.8 米完成余量。工具说明明确 6 cm 进入停车、10 cm 最终验收容差；系统指令要求使用实测位移、复用可靠跟踪点，并在门框离开视野后按测量确认整机净空。

新观测标记为 `rgb_tracked_geometry_local_odometry_v2`。里程计来自理想化仿真本体位姿，模型没有收到门的世界坐标、目标坐标或通过布尔值。步态控制器、原有动作执行、门框几何、出口位置和评分条件均保持原值。方法依据与接口字段见 [穿门修复说明](passage-solution.md)。

种子 0，每项仍为最多 20 次调用、300 秒墙钟预算；全部使用 DeepSeek 思考 API：

| 任务 | 调用次数 | 最终机身 x | 通过开口／达到停止区 | 结果 |
| --- | --- | --- | --- | --- |
| 红色三角门 | 17 | 3.279 m | true／true | 成功 |
| 绿色矩形门 | 17 | 3.237 m | true／true | 成功 |
| 黄色三角门 | 19 | 3.103 m | true／true | 成功 |

三项均确认停止，没有碰撞或跌倒。原始记录：[红色三角门](../runs/passage-solution-validation/20261028-194237-api-go_through_red_triangle_tunnel-s0-261d77/metrics.json)、[绿色矩形门](../runs/passage-solution-validation/20261028-194514-api-go_through_green_rectangle_tunnel-s0-96af90/metrics.json)、[黄色三角门](../runs/passage-solution-validation/20261028-194514-api-go_through_yellow_triangle_tunnel-s0-3939e2/metrics.json)、[批次汇总](../runs/passage-solution-validation/summary.json)。

完整自动测试 **230 passed**。这是新增公开观测协议下的三次本地冒烟测试，不是同一观测条件下的模型成功率对比，也不代表真实机器人或原始 QUARD 环境的可靠性结果。此前失败记录保留，评分没有因模型误判而放宽。

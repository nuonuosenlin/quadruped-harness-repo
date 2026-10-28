# Demo 运行与接口说明

## 1. 实现范围

本 demo 运行 Unitree Go2 的 MuJoCo 动力学模型，使用已有 TorchScript 步态策略与 PD 关节控制。现支持原始红色标记与 13 个新场景，包括不同颜色物体、字母牌、家具障碍和直立穿越门框。场景列表与运行命令见 [新场景测试](scenarios.md)。低姿态爬行、楼梯和动态障碍尚未支持。

```text
机载 RGB 图像 + 允许的本体状态
    → 开启思考的模型 API 选择工具
    → 像素选点 / RGB-D 跟踪 / 短程移动
    → 预训练步态控制器 → MuJoCo 物理仿真
    → 新观测和执行结果
```

独立评测器读取仿真目标位置和轨迹；模型上下文不读取评测器结果，也不接收目标世界坐标。感知模块内部使用仿真相机标定与机身位姿转换坐标，再输出相对几何信息。这仍是理想定位条件下的仿真，不能等同于实机视觉定位。

当前机器人运行入口只使用模型 API，默认 DeepSeek，并固定开启思考。模型返回的思考内容在进程内保留，用于后续工具调用的历史回传。

## 2. 环境与资产

推荐 Ubuntu、Python 3.11。项目固定 MuJoCo 版本，其他包的兼容范围见 [pyproject.toml](../pyproject.toml)。若机器上已有可用环境，也可在该环境中 `pip install -e '.[test]'`；避免混用不同环境的 `python` 和 `pip`。

桌面窗口模式：

```bash
source .venv/bin/activate
unset MUJOCO_GL
./scripts/run_deepseek.sh --viewer
```

NVIDIA 无桌面模式：

```bash
MUJOCO_GL=egl ./scripts/run_deepseek.sh
```

如 EGL 不可用，可在 Ubuntu 安装 OSMesa 后使用 CPU 离屏渲染：

```bash
sudo apt-get install libosmesa6
MUJOCO_GL=osmesa ./scripts/run_deepseek.sh
```

OSMesa 需要额外系统依赖，性能可能较低。`MUJOCO_GL` 必须在 Python 启动前设置。桌面 viewer 需要显示环境，SSH 无显示时请去掉 `--viewer`。

资产源固定为 `wty-yy/go2_rl_lab` 的 commit `24859ea57953624de8208ddc11b606ebfec5c99c`，策略为 `go2_cts_150k.pt`；各文件下载地址、长度和 SHA-256 记录于 [assets.lock.json](../assets.lock.json)。

```bash
python scripts/fetch_assets.py
python scripts/fetch_assets.py --verify
```

自定义资产位置时，下载脚本使用单数 `--asset-dir`，运行器使用复数 `--assets-dir`：

```bash
python scripts/fetch_assets.py --asset-dir /data/go2-demo-assets
./scripts/run_deepseek.sh --assets-dir /data/go2-demo-assets
```

仓库代码、模型与策略的来源说明和许可见 [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)。校验失败时重新运行下载脚本，不要关闭哈希检查。

## 3. API 配置

当前工作区的 DeepSeek 启动方式：

```bash
./scripts/run_deepseek.sh --viewer --seed 0
```

脚本使用 `.venv/bin/python`，从工作区的 `../deepseekapi.txt` 读取密钥，并设置 `--provider deepseek --model-name deepseek-flash --no-env-proxy`。它使用官方 `https://api.deepseek.com/chat/completions`，固定以 `thinking={"type":"enabled"}` 运行；密钥不出现在命令参数或日志中。DeepSeek 的图片能力与参数说明见 [官方视觉文档](https://api-docs.deepseek.com/guides/vision/)和[思考模式文档](https://api-docs.deepseek.com/guides/thinking_mode/)。

需要使用环境代理时，可直接运行 `python -m go2_demo --viewer`；通用入口默认遵循代理环境变量。`--api-key-file` 可指定其他密钥文件，`--model-name` 可覆盖模型名。默认任务为蓝色球体，原始红色标记可通过 `--task red_marker` 选择。

其他兼容服务使用 `--provider compatible`，并配置以下环境变量：

| 变量 | 含义 |
| --- | --- |
| `MODEL_BASE_URL` | Chat Completions 兼容 API 根地址，包含服务商要求的前缀 |
| `MODEL_NAME` | 服务端实际支持的模型标识 |
| `MODEL_API_KEY` | 服务凭据；不要写进代码或日志 |
| `MODEL_API_KEY_FILE` | 代替环境密钥，从文件读取单个非空凭据；支持 UTF-8 BOM 和末尾换行 |

显式 `--api-key-file` 优先于 `MODEL_API_KEY`，后者优先于 `MODEL_API_KEY_FILE`。DeepSeek 配置在没有其他凭据来源时读取 `../deepseekapi.txt`，并固定官方服务地址。

模型需要同时支持图像、`tools`、`tool_calls`、`thinking={"type":"enabled"}` 和非流式返回。适配器直接使用 HTTP，不依赖服务商 SDK，也不自动加载 `.env`。每次决策只发送一张当前 RGB 图像；历史保留完整的助手消息、思考字段、工具调用与对应结果，不重复携带旧图。

所有运行入口固定开启思考。DeepSeek 工具轮次返回的完整 `reasoning_content` 和助手内容只在内存中保留，并随对应历史消息回传；历史窗口按完整轮次裁剪。日志仅记录思考字符数，避免保存原始思考文本。其他服务商若使用不同推理协议，需要单独适配。

当前观测协议为 `rgb_tracked_geometry_local_odometry_v2`。除图像、本体状态和跟踪点外，还提供 `sensor_calibration`、起点机身水平坐标系下的 `local_odometry`，以及公开容差 `completion_requirements`。里程计来自理想化仿真状态，不是已验证的真实机器人定位器；观测不携带目标或门框的世界坐标、隐藏通过状态或评分。具体穿门判定与改动依据见 [穿门修复说明](passage-solution.md)。

调用超时、HTTP 错误、非 JSON 参数、无工具响应、截断响应等会记录为模型错误；不会把文本“完成”自动转换为任务成功。一次 API 请求不会自动重试，防止在不知情的情况下增加费用或重复决策。工具只由本地白名单执行，不执行模型生成的 Python 或 shell。

协议依据：[千问视觉兼容接口](https://help.aliyun.com/zh/model-studio/qwen-vl-compatible-with-openai)、[DeepSeek 工具调用格式](https://api-docs.deepseek.com/guides/tool_calls/)。兼容格式相同不代表每个模型都具备视觉与工具能力，运行前请确认实际端点支持。

## 4. 工具、坐标与执行

每轮允许一个工具调用。若模型同时返回多个工具，本轮全部拒绝并逐项反馈，不静默执行其中一部分。

| 工具 | 参数与行为 |
| --- | --- |
| `observe` | 获取当前观测，不移动 |
| `track_point` | `image_id, u, v`；在最新图像中选点，读取该点深度 |
| `get_geometry` | 读取当前跟踪点的相对位置、平面距离、方位、置信度和有效状态 |
| `move_relative` | `forward_m, lateral_m`；相对位移总长度不超过 0.6 米 |
| `turn` | `yaw_rad`；相对转角绝对值不超过 0.6 弧度 |
| `stop` | 速度指令归零并检查停止情况 |
| `finish` | 停止并声明完成，随后由独立评测器评分 |
| `abort` | `reason`；停止并结束，不声明成功 |

像素原点在左上，`u` 向右、`v` 向下。移动使用**动作开始时**机身朝向在水平面的投影：前为正、左为正，单位米；转向向左为正，单位弧度。执行器根据实测位姿跟踪局部目标，没有全局路径规划或自动绕障。

当前控制器在位置误差小于 0.06 米、朝向误差小于 0.045 弧度时进入零速收敛；继续运行 0.6 秒后，位置误差不超过 0.10 米、朝向误差不超过 0.10 弧度且确认停止，动作才返回 `succeeded`。这些是该步态策略的 demo 容差，工具结果保留实测误差，不能理解为精确到达。未达到要求时明确返回超时或失败。

跟踪点是静态场景中的像素特征，通过光流和深度更新。观测包含 `image_id` 和仿真时间；旧帧选点、无效深度、越界像素会被拒绝。跟踪失败时，当前相对坐标返回空值并标记失效，不能当作最新测量继续使用。

当前预训练策略只接收平面速度指令。`set_posture` 不在公开工具列表中；若仍收到调用，会返回 `UNSUPPORTED_CAPABILITY`。观测中的高度、俯仰只是本体测量，不代表可控制能力。

## 5. 预算与评分

示例：

```bash
./scripts/run_deepseek.sh --seed 0 \
  --max-model-calls 30 --max-wall-seconds 300 --max-sim-seconds 120 \
  --api-timeout 90 --max-output-tokens 8192 --history-turns 6 --runs-dir runs
```

默认每次请求最多输出 8192 token，包含思考与工具调用；默认 API 超时 90 秒、每项墙钟预算 300 秒。输出被截断时不会执行该次工具请求，应结合日志决定是否增加输出或时间预算。

模型等待期间仿真暂停，运行模式明确记录为 `paused_during_model_inference`。动作执行期间物理仿真与低层控制继续推进。模型调用耗时仍计入墙钟预算；仿真时间另行记录。首版尚不模拟动态环境在 API 等待期间继续变化的情况。

几何验收以目标标记中心的水平距离为基准，要求：

- 距离为 1.0 米，误差不超过 0.18 米；
- 面向目标的角度误差不超过 0.25 弧度；
- 水平速度小于 0.12 米／秒，偏航角速度小于 0.25 弧度／秒；
- 没有摔倒或与红色目标、蓝色干扰物发生碰撞。碰撞标志累计保留；当前未单独统计非足部触地，跌倒由机身高度与倾斜阈值判定。

跟踪点可能位于目标表面，因此其距离与评测器的目标中心距离并不完全相同。运行器还会记录是否正常声明 `finish`、是否超预算或发生错误；查看最终 `metrics.json`，不要仅凭窗口画面或模型的完成声明判断成功。

## 6. 日志与排错

| 文件 | 用途 |
| --- | --- |
| `manifest.json` | 运行模式、预算、种子和版本信息 |
| `events.jsonl` | 允许观测、决策、思考字符数、工具反馈和异常；不保存原始思考文本 |
| `trajectory.jsonl` | 物理轨迹与控制命令，供事后分析；包含评测用信息 |
| `metrics.json` | 最终成功判定、结束原因、几何误差及时间／调用统计 |
| `frames/*.png` | 机载 RGB 图像，帮助排查目标选择与跟踪问题 |

常见问题：

- **缺少资产或校验失败：**运行 `python scripts/fetch_assets.py`，确认运行器和脚本指向同一资产目录。
- **GLFW／EGL 初始化失败：**桌面 viewer 使用默认 GLFW；无桌面去掉 viewer，设置 EGL 或安装 OSMesa。不要同时混用。
- **HTTP 401／403：**检查 Key、地域、业务空间和模型权限；错误日志不会显示认证内容。
- **HTTP 400：**检查 API 根路径、模型是否同时支持视觉、工具与思考参数，以及思考字段的历史回传格式。
- **没有工具调用：**确认模型支持 Function Calling；当前适配器不把自然语言答案自动转换成动作。
- **丢点或反复重新选点：**查看图像和 `loss_reason`；纹理少、位移大、遮挡或深度不连续都会影响稀疏光流。不会用目标真值自动修复。
- **预算耗尽：**先看 API 耗时与动作失败原因，再决定是否增加预算。增加预算后的结果应与原设置分开记录。

## 7. 后续扩展顺序

先固定模型与控制器，比较“图像＋运动工具”和“增加几何跟踪”的差异；随后再考虑关系约束工具、任务 Agent、外部记忆。高度／俯仰与低隧道任务须先取得支持姿态目标并能保持姿态行走的控制器，不能仅增加 JSON 字段。

原有研究背景、实验设计和后续计划保留于 [design-plan.md](design-plan.md)。该文件是初始设计归档，其中的拟实现功能不表示当前 demo 已具备。

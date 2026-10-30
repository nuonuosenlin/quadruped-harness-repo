> 历史报告副本：本文描述原工作区的已验证结果。原始 JSON、日志、图像、视频和安装文件保留在 D:\RoboHarnessSim，未包含在本代码仓库。报告中的历史命令指向原工作区；运行本仓库副本请使用根目录 README 的命令。

# BEHAVIOR-1K 与 LIBERO 仿真搭建报告

## 1. 完成状态与证据

| 项目 | 当前状态 | 证据 |
|---|---|---|
| LIBERO 官方 README 最小示例 | passed，10 步 | `libero_official/result.json`、`../logs/libero-official-demo.log` |
| LIBERO RGB-D / mask / 动作 | passed，60 步、20Hz，EEF 净位移 0.084431m | `libero_probe/result.json`、动作视频 |
| BEHAVIOR 最小 RGB-D / 动作 | passed | `behavior_probe/result.json`与引擎日志 |
| BEHAVIOR 官方 empty demo | passed | `behavior_official/result.json` |
| 家庭资产、训练演示、策略权重 | 未下载 | 下载清单和空间审计 |
| LLM / RoboHarness E2E / 真机 | 本阶段不执行 | 无相应服务、任务或硬件调用 |

LIBERO 加载 `LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket`。最小示例执行零动作，扩展验收执行小幅平移，`done=false` 属于预期。**“通过”仅表示仿真、感知、动作可运行，不表示完成抓取任务。**

（本地证据：LIBERO RGB，原路径 `libero_probe/before_agentview_rgb.png`；未随仓库上传）

（本地证据：LIBERO 深度预览，原路径 `libero_probe/before_agentview_depth_preview.png`；未随仓库上传）

（本地证据：LIBERO 实例分割，原路径 `libero_probe/before_agentview_mask_preview.png`；未随仓库上传）

（本地证据：动作视频，原路径 `libero_probe/action_demo.mp4`；未随仓库上传）。深度伪彩色和 mask 彩图仅供查看；几何计算使用数值 NPY。

## 2. 本机信息、路径与存储策略

**实测：**Windows 11 25H2 / build 26200；RTX 4060 Laptop、8188MiB 显存、驱动 566.24；物理内存约 15.78GiB。预装默认 Python 3.12.11 位于 `D:\msys2\mingw64\bin\python.exe`。`nvidia-smi` 的 CUDA 12.7 是驱动支持上限，不等于安装了 Toolkit；未找到 nvcc。注册表历史 ProductName 仍显示 Windows 10，系统判定以 build/平台信息为准。

```text
D:\RoboHarnessSim\
├── LIBERO\               # 官方源码，commit 8f1084e3132a39270c3a13ebe37270a43ece2a01
├── BEHAVIOR-1K\          # v3.9.1，commit 26f2c7ef7b9cf96bd0414f81e1e751e493762779，稀疏检出
├── envs\libero\          # Python 3.8.13，独立 prefix
├── envs\behavior\        # Python 3.11，独立 prefix
├── assets\               # 最小仿真资产；libero-datasets 为空
├── downloads\            # 安装包、断点、校验文件
├── cache\                # pip/conda/HF/Torch/Numba/Omniverse
├── home\                 # 本任务 .condarc、LIBERO 配置
├── tools\                # micromamba、固定提交 LeRobot 库源码
├── tmp\                  # 安装临时文件
├── scripts\              # 启动、验收、补丁、审计脚本
├── logs\                 # 安装、失败和运行原始日志
└── reports\              # 本报告、JSON、图像、视频和版本锁定
```

`scripts/env.ps1` 设置进程级 TEMP/TMP、PIP_CACHE_DIR、HF_HOME、HF_HUB_CACHE、HF_DATASETS_CACHE、TORCH_HOME、MAMBA_ROOT_PREFIX、CONDA_PKGS_DIRS、LIBERO_CONFIG_PATH、OMNIGIBSON_DATA_PATH、OMNIGIBSON_APPDATA_PATH 等，均位于该 D 盘根目录。新终端必须重新加载启动脚本。没有修改系统 PATH、Windows 安全设置或全局 PowerShell 配置，未安装 WSL/新显卡驱动。

末次审计已知 C 盘 pip/HuggingFace/Omniverse/NVIDIA 缓存目录，自任务开始以来更新文件数均为0，见 c_drive_cache_audit.json。这是已知目录的只读时间戳审计，不等于对整个 C 盘的因果保证；未清理已有用户缓存。实际 D 盘占用见 storage_usage.json。

采用 micromamba 的 conda prefix 管理，只使用 conda-forge。没有使用 Anaconda defaults，也没有自动接受 Anaconda TOS。来源：[micromamba 官方 Windows 说明](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#windows)。

## 3. BEHAVIOR-1K vs LIBERO

| 维度 | BEHAVIOR-1K | LIBERO |
|---|---|---|
| 底座 | OmniGibson + Isaac Sim/Omniverse + BDDL3 | robosuite 1.4.0 + MuJoCo 2.3.7 + BDDL 1.0.1 |
| 物理引擎 | PhysX；最小方案关闭 GPU dynamics，RTX 仍用于渲染 | MuJoCo；不是 iGibson |
| 任务类型 | 家庭活动、移动操作、状态变化、长程任务 | 桌面机械臂、多任务/终身学习操作任务 |
| 动作 | 随机器人/控制器变化，可含底盘、躯干、机械臂、夹爪 | 本次 OSC_POSE 6 维 + 夹爪 1 维 |
| 安装难度（推断） | 高：引擎、驱动、资产、版本和依赖耦合 | 中：历史版本和 Windows EGL/路径适配 |
| 磁盘/下载 | 家庭包 31.46GB / 解压 34.74GB；机器人 0.64GB / 解压 2.93GB；另需引擎、Torch、缓存 | 本次用源码自带资产与依赖，不需要训练演示；实际占用另见 storage_usage.json |
| 与目标 RoboHarness 关联 | 直接：目标仓库固定 v3.9.1；Fetch/empty 不能替代 R1 Pro 家庭任务 | 独立的仿真/感知/动作练习；后续移植需要 adapter |
| 本机状态 | 以实际 demo 和日志为准；硬件低于 Isaac 当前配置表 | 已跑通 RGB-D、mask、动作和视频 |

官方依据：[BEHAVIOR 固定版本安装指南](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/docs/getting_started/installation.md)、[LIBERO README](https://github.com/Lifelong-Robot-Learning/LIBERO)、[目标 RoboHarness](https://github.com/BinceQu/RoboHarness)。

RoboHarness 专指 **BinceQu/RoboHarness / arXiv:2610.14018**。本轮只读取其仿真要求，未运行其 Agent/模型安装脚本。其 main 会更新，本机仿真版本另以 commit 锁定。

## 4. LIBERO 分步搭建与复跑

1. 官方仓库 shallow clone 到 `D:\RoboHarnessSim\LIBERO`，保存 commit。
2. 官方 micromamba 放到 `tools\Library\bin\micromamba.exe`；以 `--prefix D:\RoboHarnessSim\envs\libero` 创建 Python 3.8.13 / pip 24.3.1，包缓存位于 D 盘。
3. 首先尝试官方 requirements。PyPI 大文件超时后增加超时重试；其后 `robomimic -> egl_probe` 的 Linux 构建在 Windows 失败，原始日志均保留。
4. 本阶段仅仿真，采用官方版本的仿真依赖子集，排除 wandb、transformers、robomimic、thop。额外固定 MuJoCo 2.3.7、Numba 0.58.1 / llvmlite 0.41.1，补充导入实际需要的 termcolor 2.4.0。Torch 使用 PyPI 1.11.0；本阶段无模型推理。
5. Editable 安装 LIBERO；`home\.libero\config.yaml` 将 BDDL、init states、assets 和未来可选 datasets 都指定到 D 盘；没有下载演示数据。
6. 创建 robosuite 官方支持的私有宏：关闭硬编码 /tmp 文件日志，控制台输出由启动脚本保存到 D 盘；关闭强制 EGL 覆盖，使用 Windows GLFW OpenGL 上下文。后者不等于软件渲染。
7. 两处 Windows 兼容修复：从实际 mujoco 包加载 DLL；用 os.path.isabs 判断绝对路径。备份在 `scripts/vendor-originals`，diff 见 `libero-windows-compat.patch`，未改变物理参数或任务。
8. `libero_official_demo.py` 按 README task 示例执行 seed 0 / 任务 0 / 初态 0 / 10 步，补齐示例省略的 import 并记录结果。
9. `libero_interface_probe.py` 开启双相机 RGB、深度、实例分割，执行 60 步小幅动作；输出标定、轨迹、原始观测和视频。
10. 校验目标 mask 非空，RGB PNG、单独深度/mask NPY 统一左上原点；原始 observations.npz 保留原始 OpenGL 行序，已单独标明。
11. 版本锁定见 `libero-freeze.txt`；`libero-pip-check.txt` 实测为 No broken requirements found。

PowerShell 复跑：

```powershell
& 'D:\RoboHarnessSim\scripts\run-libero.ps1' -Mode all
```

可分别选择 official 或 probe。不要使用系统默认 Python 运行这些脚本。

来源：[官方 Task 示例](https://github.com/Lifelong-Robot-Learning/LIBERO#task)、[官方 requirements](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/requirements.txt)、[robosuite 1.4.0](https://github.com/ARISE-Initiative/robosuite/tree/v1.4.0)。Windows 补丁/依赖子集为本次适配，不声称等同原论文训练环境。

## 5. BEHAVIOR 预算、最小方案及硬件限制

### 5.1 体量审计（实测）

HuggingFace 官方文件清单给出压缩大小；HTTP Range 仅读取 ZIP 中央目录，累计 file_size 得到解压逻辑大小。Isaac wheel 从 NVIDIA HEAD 与 ZIP 目录核算；未下载整个家庭包。JSON 证据：`behavior_space_audit.json`、`behavior_unpacked_audit.json`，明细在 sources/*.filelist.json。GB 为十进制。

| 官方文件 | 下载 GB | 解压 GB |
|---|---:|---:|
| 2026-challenge-task-instances.zip | 0.109 | 0.577 |
| behavior-1k-assets-3.9.0.zip | 31.458 | 34.742 |
| omnigibson-robot-assets-3.8.2.zip | 0.641 | 2.927 |
| omniverse_kit-107.3.1.206797.whl | 0.087 | 0.319 |
| isaacsim_kernel-5.1.0.0.whl | 0.050 | 0.126 |
| isaacsim_asset-5.1.0.0.whl | 0.027 | 0.089 |
| isaacsim_extscache_kit-5.1.0.0.whl | 3.422 | 6.487 |
| isaacsim_extscache_kit_sdk-5.1.0.0.whl | 0.666 | 1.537 |

Isaac 行仅为大文件审计；26 个官方 wheel 已下载共 4.372GB、解压逻辑体量 8.931GB。Torch 主 wheel 下载 2.771GB、解压 5.045GB，机器人包下载 0.641GB、解压 2.927GB。小依赖、环境和缓存另计，实际占用见 storage_usage.json；完整清单为 `isaac_download_manifest.json`。下载量、解压量、运行缓存和磁盘余量不能混为一项。

### 5.2 目前安装的最小方案

用户已于本轮明确接受 NVIDIA Isaac Sim EULA 并同意尝试 empty 场景。预计新增约 25–30GB 是预算，不是测量保证；安装全程保留 10GiB。该方案不具备家庭任务全资产。

- 固定 BEHAVIOR v3.9.1，与 RoboHarness 的子模块一致。该版本使用 Python 3.11、Isaac Sim 5.1.0.0、Kit 107.3.1；数据匹配机器人 3.8.2 / 家庭 3.9.0。
- 源码稀疏检出保留 OmniGibson、bddl3、启动 logo 和必要脚本，跳过约 409MB 文档资源，未改变固定 commit。
- 独立环境 `envs\behavior`。已安装 Torch 2.7.0+cu126 / torchvision 0.22.0+cu126 / torchaudio 2.7.0+cu126，选择官方脚本允许的 CUDA 12.6 变体，匹配当前驱动；这不是参考 cu128 环境。未安装 cuRobo 或完整 CUDA Toolkit。
- NVIDIA wheel 保存在 downloads/isaacsim-5.1.0；官方机器人包解压到 assets/behavior/omnigibson-robot-assets；不下载 31.46GB 家庭包。
- 分块下载保存断点并校验 Content-Range、长度、ZIP CRC；Torch 对照官方索引 SHA256，机器人包对照官方 LFS SHA256。SSL EOF 时保留已完成分块并退避重试，不关闭证书验证。
- BDDL 3.7.0 从仓库 bddl3 安装，不能从 PyPI 退回旧版，也不能与 LIBERO 的 1.0.1 混在一个环境。
- 即使不采集数据，OG 初始化仍导入 LeRobotDataWrapper。所需库源码固定在 RoboHarness 记录的 commit 436812bd8ee39b768c645c248c91f1330834e687；仅补足导入依赖，不运行记录/评估/模型。Windows TorchCodec 与 Torch 2.7 的约束差异另行记录，视频使用 PyAV。
- 最小验收基于官方 robot_control_example 的 empty/Fetch 配置；RGB-D 探测只增加低分辨率外部相机。没有把空场景写成“家庭任务已就绪”。
- 家庭数据集许可与解密 key 未申请/下载；训练演示集和策略权重未下载。

来源：[固定版本安装脚本](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/setup.ps1)、[资产版本/下载实现](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/utils/asset_utils.py)、[官方资产清单](https://huggingface.co/datasets/behavior-1k/zipped-datasets/tree/main)、[官方 empty demo](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/examples/robots/robot_control_example.py)。

### 5.3 安装完成记录与复跑

1. 官方 micromamba 以 --prefix 创建 `D:\RoboHarnessSim\envs\behavior`，Python 3.11.18；与 LIBERO 分离。
2. 从 v3.9.1 源码安装本地 BDDL 3.7.0、核心依赖。安装 Torch/cu126 后运行 GPU 张量探针，CUDA available=true。
3. 下载并校验 26 个 NVIDIA 官方 Isaac Sim 5.1.0.0 wheel。普通 Windows 路径安装长 SDK 资源触发 MAX_PATH；使用 `\\?\D:\RoboHarnessSim\envs\behavior\python.exe` 直接启动 pip 解决，未改注册表。micromamba run 不能启动该扩展路径，因此只在长路径安装时直接调用；普通短依赖仍用常规路径。
4. Isaac kernel 精确依赖 Pillow 11.3.0 与 OG 的 ~=11.0.0 冲突；按目标 RoboHarness 对共享环境的 runtime-pins 方法使用 --no-deps 安装 SDK，再显式安装缺失库。采用 Pillow 11.0.0、warp 1.12.0、pyarrow 25.0.0、packaging 25.0、websockets 17.0.1、click 8.4.2 等 runtime pins。**SDK 声明的旧精确依赖仍有冲突，pip check 不会全绿；用实际 demo 验证，不能称作纯官方无冲突安装。**约束见 scripts/behavior-constraints.txt，原始冲突与解决日志均保留。
5. LeRobot sparse clone 需补 setup.py 才能生成动态 readme 元数据；固定提交后 --no-deps --no-build-isolation 安装 LeRobot 0.5.2 与 OmniGibson 3.9.1。Windows TorchCodec 与 Torch 2.7 组合未装；本轮用 PyAV，未运行数据集管道。
6. 仅解压官方机器人资产。创建空的 systems/objects 注册目录以满足空场景初始化的目录检查，目录说明为 MINIMAL_EMPTY_SCENE_ONLY；这些空目录不代表家庭资产已装。
7. 启动脚本指定 EULA 接受、headless、D 盘 appdata/portable root，关闭空场景不需要的 GPU dynamics、物体状态和 transition rules；保留 RTX 渲染。HF 离线模式防止无意触发模型下载。
8. 官方 robot_control_example 本体未改，程序选择 empty / Fetch / random，固定默认 IK 等控制器并执行 short_exec=100；独立探针在相同底座添加 256×256 外部 RGB-D 相机，记录 mask、关节与底盘动作。

复跑：

```powershell
& 'D:\RoboHarnessSim\scripts\run-behavior.ps1' -Mode all
```

可选择 official 或 probe。若需要重新安装，依次参照已保存的 requirements、constraints、下载清单及安装日志；不运行官方 -Dataset 默认全量下载。版本清单见 behavior-freeze.txt，声明冲突见 behavior-pip-check.txt。

依据：[RoboHarness setup/runtime pins](https://github.com/BinceQu/RoboHarness/blob/main/docs/setup.md)、[evaluator-runtime.txt](https://github.com/BinceQu/RoboHarness/blob/main/requirements/evaluator-runtime.txt)。本机选择 cu126、Windows 路径适配及最小资产属于本次工程适配。

### 5.4 硬件差距

BEHAVIOR v3.9.1 文档列 RAM 32GB+ / VRAM 8GB+；Isaac Sim 5.1 当前配置表列 RAM 32GB、VRAM 16GB、Windows 测试驱动 580.88。本机约 16GB RAM / 8GB VRAM / 566.24，低于底座配置表。Torch CUDA 12.6 张量计算已实测通过（behavior_torch_probe.json）；这只能证明 CUDA 运算可用，场景验收另看结果。未升级驱动。来源：[Isaac requirements](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/requirements.html)。

## 6. 接口说明

### 6.1 LIBERO（本机已实测）

| 项目 | 能提供/接受什么 | 对接注意点 |
|---|---|---|
| RGB | agentview_image、robot0_eye_in_hand_image，256×256×3 uint8 | RGB 而非 BGR；双相机各自保存 K/T |
| 深度 | camera_depths=True；原始深度是 [0,1] 透视缓冲 | 用 get_real_depth_map 转成米，不能直接反投影原始缓冲 |
| mask | camera_segmentations=instance，返回 *_segmentation_instance | 0 为背景，其余为模型实例顺序+1；记录名称映射，不能跨场景硬编码 |
| 状态 | 关节位置/速度、EEF 位置/四元数、夹爪 qpos/qvel、物体状态 | 长度米、角度弧度；obs 四元数 xyzw，MuJoCo XML 常为 wxyz，不能混用 |
| 动作 | 7 维 [-1,1]，OSC_POSE 6 维加夹爪 | 前三维平移增量，后三维轴角旋转增量，最后夹爪；不是 7 个关节角 |
| 缩放 | 本次输出平移 ±0.05m、旋转 ±0.5rad，use_delta=True | 是目标增量缩放，不是 m/s、绝对坐标或保证实际位移 |
| 时间 | 控制频率 20Hz | 区分控制步与 MuJoCo 物理子步 |
| 协议 | reset -> obs；step -> obs,reward,done,info | 旧 Gym 4 元组，不能按 Gymnasium 5 元组直接解包 |

实测目标 mask：alphabet_soup / tomato_sauce / basket 的像素 ID 是 1 / 3 / 8，初始可见像素为 442 / 790 / 4418。这仅对当前场景实例排序有效。分割 ID、标定、动作上下界和状态形状均在 result.json。

导出 PNG/单独 NPY 已统一左上角原点并对齐；observations.npz 保留原始 OpenGL 行序。外参由 camera_utils 返回 camera-to-world，并修正了 MuJoCo OpenGL 轴到 OpenCV 光学轴。使用图像平面深度时：

```text
p_camera = depth_m * inverse(K) * [u, v, 1]^T
p_world  = T_camera_to_world * [p_camera, 1]^T
```

不能将 camera-to-world 当 world-to-camera，不能把径向距离当 image-plane depth。物体真值与 mask 属于仿真特权信息，下一阶段要核对基准允许使用哪些信息。

来源：[env_wrapper](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/libero/libero/envs/env_wrapper.py)、[camera_utils](https://github.com/ARISE-Initiative/robosuite/blob/v1.4.0/robosuite/utils/camera_utils.py)、[OSC 控制器](https://github.com/ARISE-Initiative/robosuite/blob/v1.4.0/robosuite/controllers/osc.py)，本机 JSON 与 vendor-originals 是实际运行证据。

### 6.2 BEHAVIOR（源码确认；验收状态单独看 JSON）

**官方能力：**VisionSensor 支持 RGB、深度、语义/实例/prim 分割、法线、光流、相机参数等；需显式启用并读取标签映射。depth 是到相机中心的距离；depth_linear 是到图像平面的距离，几何意义不同。

env.get_obs / robot.get_obs 返回嵌套 robot/sensor/task 观测；reset 返回 obs,info；step 返回 obs,reward,terminated,truncated,info。连续动作维数、归一化、控制分组取决于机器人，读取 action_dim、controller_order、controller_action_idx 后再拆分。不得照搬 LIBERO 7 维。

get_position_orientation 可选 world/scene frame；位置米、角度弧度，机器人 API 四元数 xyzw 与底层其他表示需分别确认。源码存在这些能力不等于本机已验收，实际结果见 behavior_probe/result.json。

来源：[VisionSensor](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/sensors/vision_sensor.py)、[Environment](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/envs/env_base.py)、[Robot](https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/robots/robot.py)。

**工程建议（未实现）：**分别提供 adapter，统一 RGB、米制 image-plane depth、K/T、frame、状态与步号；动作请求明确 frame、单位、增量/绝对目标和执行步数，再转换为各仿真的 controller。动作调用完成和任务目标达成应分字段记录。

## 7. 踩坑记录

| 问题 | 证据 | 处理与边界 |
|---|---|---|
| 默认 MSYS2 Python 3.12 与 LIBERO 历史版本不匹配 | host_probe.json | 用 D 盘独立 prefix，不改系统解释器 |
| 默认安装/缓存可能写 C | env.ps1、home/.condarc | 所有本任务路径定向 D；新进程须重新加载 |
| CIM 受限查询失败 | 初始检测 | 用内存 API 获取实际 RAM，不把失败当作无内存 |
| PyPI 读取超时 | libero-dependencies.log | 延长超时、保留缓存重试 |
| egl_probe Linux 构建失败 | libero-dependencies-retry.log | 仿真依赖子集 + Windows GLFW |
| 缺少 termcolor | libero-official-demo-attempt-1.log | 补 2.4.0 |
| /tmp 日志硬编码 | attempt-2.log | 私有宏关闭文件日志，D 盘收集控制台 |
| MuJoCo DLL 路径错误 | attempt-3.log | 指向已安装 mujoco 包，补丁/备份留档 |
| Windows 绝对路径识别 | libero-windows-compat.patch | 用 os.path.isabs；不改物理行为 |
| 原始图像行序与 PNG 方向不同 | export_convention.json | 同步转换单独 RGB/depth/mask；保留原始 NPZ |
| Gym 弃用提示 | LIBERO 运行日志 | 保持官方历史版本，不在本阶段迁移接口 |
| 完整家庭安装峰值超空间 | space audit JSON | 不下载家庭包，先按最小 empty |
| GitHub clone 停滞 | behavior-clone.log | 保留失败目录，HTTP/1.1 + sparse checkout |
| SSL EOF / 连接中断 | 下载和 core 安装日志 | 断点、减少并发、退避重试；不关闭证书校验 |
| PyPI 无 BDDL 3.7.0 | behavior-core-install 日志 | 用同一仓库 bddl3 安装 |
| Isaac EULA | isaac-eula-authorization.txt | 不扩展为家庭数据许可 |
| Isaac SDK 长路径 | isaac-local-install 日志 | 扩展路径直接运行 pip，未修改系统长路径策略 |
| SDK Pillow / 精确版本冲突 | dependency-conflict 与 runtime-pins 日志 | 采用目标仓库 runtime pins，保留 pip check 冲突并以实际运行验证 |
| UNC 下旧 wheel 的 ../../Scripts 失败 | behavior-sdk-and-wrapper-runtime.log | 短依赖改回普通 D 盘路径安装 |
| LeRobot sparse 缺 setup.py | editable-install 日志 | 补固定提交的 setup.py 后安装，未执行训练/采集 |
| HDF5 入口 H5Tdecode 缺失弹窗 | behavior-hdf5-compat-fix.log | h5py 3.16 自带 HDF5 2.0，与 SDK 旧 DLL 冲突；固定 h5py 3.11.0，未替换系统 DLL |
| 随机 OSC 控制器 Singular matrix | behavior-official-demo-attempt-1-osc.log | 固定选择官方默认 IK/底盘/夹爪控制器，保留随机动作 |
| 空场景分割缺 floors 类别 | behavior-interface-probe-attempt-2-floor-category.log | 在本地探针中显式注册官方 STRUCTURE_CATEGORIES 并清语义映射缓存；不创建伪家庭模型 |
| 原生 depth_linear 全零 | behavior-interface-probe-attempt-3/4 日志及 native NPY | 早期运行全零；最终原生双深度有效。保留数据检查与 K 几何换算备用分支，最终没有使用备用分支，根因未完全定位 |
| Conda TOS | conda-forge 配置 | 未使用 defaults，无自动接受 Anaconda TOS |
| HF / GitHub 访问 | 下载来源清单 | 当前公开资源，无账号/密钥请求 |

h5py 官方说明：[3.16 wheel 改用 HDF5 2.0](https://docs.h5py.org/en/stable/whatsnew/3.16.html)；本机原 DLL 探针实测版本 2.0.0 且无 H5Tdecode，固定后 HDF5 1.14.2 且该符号存在（behavior_hdf5_probe.json）。启动日志中的旧 RTX lidar/radar DLL 加载失败与此冲突有关；修复后官方 100 步运行日志已无这些 DLL 加载错误，旧弹窗已关闭。

本轮没有使用 trusted-host、TLS 验证关闭或浏览器安全绕过。后续实际新错误追加在原始 logs 与运行结果中。

## 8. 下一阶段准备度

- [x] 机器检测、D 盘 prefix 和缓存策略。
- [x] LIBERO 官方 demo、RGB-D、mask、动作、位移和视频。
- [x] LIBERO 标定、图像方向、mask 映射、版本与补丁留档。
- [x] BEHAVIOR 版本和压缩/解压预算。
- [x] BEHAVIOR 最小方案及 NVIDIA EULA 已获同意。
- [x] BEHAVIOR 官方 empty demo / 原生 RGB-D / mask / 动作已通过；家庭任务仍未准备。
- [ ] 完整家庭资产和单任务资源；下载前重新核算空间。
- [ ] R1 Pro 与目标 RoboHarness 的精确控制器、相机和坐标协议。
- [ ] 如需严格参考复现，核对 Linux/依赖/模型/Agent/感知配置；Windows 最小 demo 不替代该验证。
- [ ] 自研 harness adapters 和闭环错误反馈。
- [ ] LLM/API/端到端：下一阶段，本轮未做。
- [ ] 真机通信和动作验证：下一阶段，本轮未做。
原生 depth_linear 曾全零的底层原因本轮未完全定位，不能直接断言由驱动造成。

## 9. BEHAVIOR 本机最终验收

官方 empty/Fetch 示例 100 步通过；接口探针 256×256 RGB/深度/实例分割与 60 步底盘动作通过。最终深度来源：**原生 depth_linear，前后两次均有效；未使用备用换算**。

底盘 XY 净位移 0.284362m；动作维数 12，控制器顺序 ['base', 'trunk', 'camera', 'arm_0', 'gripper_0']。base=[0,1]、trunk=[2]、camera=[3,4]、arm_0=[5..10]、gripper_0=[11]；本次是归一化底盘输入0.1、其余为0，不代表0.1m或0.1m/s。

线性深度前后有效像素为35267/35314，机器人 mask 为3621/3772像素。原生径向距离与线性深度按 K 验证，几何相对误差中位数约0.069%，详见 export_validation.json；并已人工查看RGB/深度/分割预览。

若原生平面深度无效，探针备用公式 z = r / sqrt(1 + ((u-cx)/fx)^2 + ((v-cy)/fy)^2)。r 是原生相机中心距离，K 是同一传感器实际内参；天空无命中像素保留 inf。raw radial、raw depth_linear、输出平面深度分别保存，每次读取 depth_evidence，不能默认为原生或换算。早期全零日志保留，最终通过不代表该启动问题彻底定位。

相机位姿使用 USD 相机轴（+X右、+Y上、-Z前）；接 OpenCV 光学轴需乘 diag(1,-1,-1)，并区分pose与view transform。实际K=[[207.2874,0,128],[0,207.2874,128],[0,0,1]]；世界位姿xyzw、mask标签映射和关节状态见 behavior_probe/result.json。

（本地证据：BEHAVIOR RGB，原路径 `behavior_probe/before_rgb.png`；未随仓库上传）

（本地证据：BEHAVIOR 深度预览，原路径 `behavior_probe/before_depth_preview.png`；未随仓库上传）

（本地证据：BEHAVIOR 实例分割，原路径 `behavior_probe/before_mask_preview.png`；未随仓库上传）

（本地证据：底盘动作视频，原路径 `behavior_probe/action_demo.mp4`；未随仓库上传）。只证明最小空场景感知与控制可用，家庭场景、R1 Pro、BDDL任务与RoboHarness端到端仍未验证。

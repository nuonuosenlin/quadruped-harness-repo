# QUARD 数据集回归测试

本项目接入 [QUARD 官方公开数据](https://huggingface.co/datasets/Tong314/QUARD)的小样本，用于检查真实数据的读取、指令、时序和控制标签。数据与当前 Go2 MuJoCo 闭环分别测试；离线数据检查不计算导航成功率。

要在窗口里运行新场景，请使用 [新场景测试入口](scenarios.md)：`./scripts/run_deepseek.sh --task distinguish_texture_b --viewer`。本页的 `go2_demo.quard` 命令只检查离线数据，不切换仿真场景。

依据本地 [CerebVLA 论文](../../QUAR_VLA_ICRA_2027.pdf)第 IV-A 节，论文从 QUARD 中选择 15 个任务，覆盖纹理辨别、目标到达、避障、隧道穿行和低姿态爬行；训练时每任务采样 100 条轨迹，并使用覆盖 2 秒的 4 帧视觉窗口。论文没有提供确切的 15 任务清单及训练／评测划分。本项目选择公开原始数据中属于这五类的 15 个任务，作为可复现的本地回归子集。

## 下载与运行

在项目目录激活已有 WSL 环境后执行：

```bash
source .venv/bin/activate
python scripts/fetch_quard.py --list
python scripts/fetch_quard.py
python scripts/fetch_quard.py --verify
python -m pytest -q tests/test_quard_dataset.py
python -m go2_demo.quard --report runs/quard/report.json
```

也可只下载和检查一个任务：

```bash
python scripts/fetch_quard.py --task go_to_red_cube
python -m go2_demo.quard --task go_to_red_cube --report runs/quard/red-cube-report.json
```

下载器从固定版本的官方压缩包中流式读取小样本，不下载全部约 125 GB 的原始数据。每个任务保留一个 episode 的 4 帧 RGB、深度、command、action 和原始 `info.csv`；如需调整下载限额，可传入 `--max-download-mb 128`。

本机 shell 曾出现小写代理变量指向失效端口的问题。若下载超时，可使用已验证的大写代理配置运行：

```bash
env -u http_proxy -u https_proxy -u all_proxy python scripts/fetch_quard.py
```

完整测试仍使用 `python -m pytest -q`。没有安装本地数据时，依赖真实 QUARD 文件的测试会明确跳过；跳过不代表数据检查通过。下载后的检查结果写入 `runs/quard/report.json`，可与运行日志一同保存。

本机于 2026-10-28 完成验证：15 段真实轨迹、60 帧、255 个文件，样本内容共 1,386,042 字节（约 1.4 MB）。全部文件通过校验，15 项真实数据回归测试通过；加上 43 项下载器／加载器单元测试及原有 65 项测试，完整测试结果为 **123 passed**。报告中 `data_valid=true`、`is_closed_loop_result=false`、`task_success_rate=null`；完整报告见 [runs/quard/report.json](../runs/quard/report.json)。

## 数据版本与覆盖范围

源数据固定为 Hugging Face revision `375cbd77d6b8e96ff82e1529f0c44caa5c182d5e`。来源、任务清单和文件校验信息记录在 [datasets/quard.lock.json](../datasets/quard.lock.json)。

| 类别 | 公开原始任务 |
| --- | --- |
| 纹理／字母辨别 | `distinguish_texture_a`、`distinguish_texture_b`、`distinguish_texture_c` |
| 目标到达 | `go_to_blue_ball`、`go_to_green_cube`、`go_to_red_cube` |
| 避障 | `go_avoid_texture_cooker`、`go_avoid_texture_drawers`、`go_avoid_texture_fan`、`go_avoid_texture_sofa` |
| 隧道穿行 | `go_through_green_rectangle_tunnel`、`go_through_red_triangle_tunnel`、`go_through_yellow_triangle_tunnel` |
| 低姿态爬行 | `crawl_red_gate2`、`crawl_red_gate3` |

每段样本按原始模拟数据的 50 Hz 频率选取帧 `0、33、67、100`，对应 `0、0.66、1.34、2.00` 秒。这是本项目固定的小样本采样规则；论文没有公开这四个具体帧号。指令直接保留 `info.csv` 中的原文，包括速度修饰词。

```text
data/quard/
└── <task>/<episode>/
    ├── info.csv
    ├── image/{000,033,067,100}.png
    ├── depth/{000,033,067,100}.png
    ├── command/{000,033,067,100}.npy
    └── action/{000,033,067,100}.npy
```

下载样本保留文件 SHA-256，`--verify` 用于检查本地样本是否完整或被修改。源压缩包 SHA-256 作为来源元数据保留；由于仅读取压缩流的一部分，**不能据此声称已校验完整源压缩包**。

三个隧道压缩包内的任务目录在 `tunnel` 前使用空格。锁文件用 `source_path` 保留原始压缩包路径，`path` 指向本地统一使用下划线的目录；下载器按这份显式映射读取文件，文件内容保持原样。

## 标签与评测边界

原始 RGB 为 `640×480` 的 8 位三通道图像；深度 PNG 为 8 位单通道图像，样本没有提供米制尺度和相机标定。深度数据用于格式检查，不直接作为当前几何跟踪器的米制深度输入。

command 与 action 为 NumPy object 数组包装的字典，加载器采用受限解析方式。用于对应论文五维控制量的字段为：

| 原始字段 | 含义 |
| --- | --- |
| `x_vel_cmd` | 前向速度指令 |
| `y_vel_cmd` | 横向速度指令 |
| `yaw_vel_cmd` | 偏航角速度指令 |
| `body_height_cmd` | 原始控制器的机身高度偏移，可为负数，不是绝对离地高度 |
| `pitch_cmd` | 原始控制器的俯仰指令 |

其他原始字段保留其含义。例如 `gait ` 的字段名含尾随空格；action 中的 `body_angular_vel_cmd` 也不能按名称直接假设为三维角速度。原始 `info.csv` 的机器人标识为 `wr2`；本次没有将该数据的控制命令直接下发给 Go2 步态策略。

论文表 I 中的未见纹理任务 `distinguish_texture_d/e` 没有包含在该公开原始数据版本中；论文生成的 XML CoT 标注和 300 条实机适配轨迹也未提供公开下载链接。因此这些回归测试不复现论文原始数据划分、UV／UL 成功率、异步控制模型或实机实验。当前结果只能说明数据接入与离线检查的状态。

来源：[QUART-Online 官方项目](https://quart-online.github.io/)、[固定版本数据目录](https://huggingface.co/datasets/Tong314/QUARD/tree/375cbd77d6b8e96ff82e1529f0c44caa5c182d5e)、[官方原始数据预处理代码](https://github.com/yuan48/QUART-Online/blob/da8a0d3c3c4e8663d414b952c078d29b4316b7c4/preprocess/1_quart_data_process.py)。许可和署名见 [第三方说明](../THIRD_PARTY_NOTICES.md)。

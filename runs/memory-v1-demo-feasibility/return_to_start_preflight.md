# 回起点 demo 离线复核

结论：**不通过**。

本轮仅在 `memory-v1` 分支读取本地源码与既有蓝球 seed 0 日志，做日志重放、静态视锥／射线计算和数据流核对；没有实现任务、运行 demo、执行运动策略、调用 API、读取密钥、修改场景或共享文档。源码哈希、git 状态与基线日志哈希在复核前后均一致。

## 四项必需条件

| 项目 | 结果 | 依据 |
|---|---|---|
| 1. 六回合历史窗口 | 通过 | 成功基线确为 12 次决策；早期原始回合确已裁掉，但累计里程计没有消失。 |
| 2. 起点不可见 | 通过 | 无唯一的起点标记；蓝球三个已达标日志姿态及各自 ±0.6rad 转向下，整个起点 1m 地面圆盘都在相机后方。 |
| 3. 记忆可记所需数据 | 不通过 | 原始调用／结果存在于 runner 日志，但当前记忆适配器丢掉指令参数、实测位移向量和 yaw；没有初始起点地标与公开 XYZ，也没有视觉重定位或路线检索出口。 |
| 4. 独立返回评分 | 通过 | 仿真能保存首帧真实机身位置并计算返回距离；≤1m 可作为粗粒度返回标准，须加阶段、停止和全程无碰撞跌倒门控。 |

## 1. 用真实基线核对历史

基线：[20261109-212737-api-go_to_blue_ball-s0-e43663](/home/nuonuosenlin/Agent-harness/runs/dashscope-validation-20261109-132737-c60cc5/20261109-212737-api-go_to_blue_ball-s0-e43663)。`metrics.json` 为 success=true、termination=finish、model_calls=12、motion_calls=6，模型 deepseek-v4.1-flash、seed 0；manifest 的 history_turns=6。逐次输入实际记录的历史长度为 `[0, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6]`。

| 决策（从 1 开始） | 工具 | 结果 | 输入历史长度 |
|---:|---|---|---:|
| 1 | track_point | succeeded | 0 |
| 2 | turn | succeeded | 1 |
| 3 | move_relative | succeeded | 2 |
| 4 | track_point | succeeded | 3 |
| 5 | move_relative | failed | 4 |
| 6 | move_relative | succeeded | 5 |
| 7 | track_point | succeeded | 6 |
| 8 | move_relative | succeeded | 6 |
| 9 | move_relative | succeeded | 6 |
| 10 | turn | succeeded | 6 |
| 11 | stop | succeeded | 6 |
| 12 | finish | succeeded | 6 |

第 12 次输入保留第 6–11 次完整回合；若第 12 次之后有回程决策，则只剩第 7–12 次，原始第 1–6 次被裁掉，包括初始选点、第一次转向、第一段移动。这里第 5 次位移请求因向量长度超限而被拒绝，不能当成真实移动。

12 是这条基线的实际总决策数，并非几何上必须移动 12 次：按日志姿态与停止速度复算，第 **9 次**已首次满足蓝球距离／朝向／停止条件。若此时进入回程，原始第 1–3 次仍已掉出窗口。现有 finish 会结束 episode，因此“finish 后继续回程”只是窗口分析，未实现或执行。私有 reasoning 文本本来不落盘，不能宣称后续推理绝不复述旧事实；本报告只确认原始回合裁剪。

## 2. 起点与地标的视锥／遮挡检查

用与 candidate_preflight 相同的原始 MuJoCo 场景构造器和 mj_ray，不新增标记／遮挡物。通过既有 trajectory 与同一时刻 local_odometry 重建首个观测时刻的世界起点（仅供离线几何和评分）：XY=`[-0.0014892782250553998, 0.006127374862611664]`，yaw=`0.018345315` rad。多次独立重建最大差异 `1.24e-16` m。起点采用初始化站稳后的首帧，不能武断等同 reset 的 `[0,0]`。

现有固定物体只有蓝球、红色干扰方块和重复棋盘地面。没有 home／start 唯一标记；重复棋盘纹理不能作为唯一的回家标签。初始追踪到的蓝球也不等于起点地标。

| 蓝球日志检查点 | 原地转向 rad | 起点 1m 地面圆盘的最大相机前向深度 m | 结论 |
|---|---:|---:|---|
| first_blue_criteria（第 9 次） | +0.0 | -1.231274 | 整个圆盘在相机后方 |
| first_blue_criteria（第 9 次） | +0.6 | -0.898972 | 整个圆盘在相机后方 |
| first_blue_criteria（第 9 次） | -0.6 | -0.896096 | 整个圆盘在相机后方 |
| explicit_stop_before_finish（第 11 次） | +0.0 | -1.220794 | 整个圆盘在相机后方 |
| explicit_stop_before_finish（第 11 次） | +0.6 | -1.016842 | 整个圆盘在相机后方 |
| explicit_stop_before_finish（第 11 次） | -0.6 | -0.760111 | 整个圆盘在相机后方 |
| after_finish_stop（第 12 次） | +0.0 | -1.225804 | 整个圆盘在相机后方 |
| after_finish_stop（第 12 次） | +0.6 | -1.010476 | 整个圆盘在相机后方 |
| after_finish_stop（第 12 次） | -0.6 | -0.772471 | 整个圆盘在相机后方 |

深度上界采用 `forward·(home_center-camera) + 1m·norm(forward_xy)`，对圆盘是连续域上界；均小于 0，故不是“有限采样没找到”的推断。再加 `max(0, forward_z·1m)` 检查地面到 1m 高的整个起点圆柱，也全部在相机后方，涵盖起点机身参考点高度。JSON 另存起点、初始选点的投影和最近射线命中，以及现有固定物体的可见性；起点方向的数学射线可能先撞到相机后方的机器人自身，但视锥已经排除该方向，不能把这类射线当作相机观测。初始蓝球选点离起点约 `2.938` m，不是 home 地标，即使还在视野里也不能直接认作起点。

静态模型使用日志机身高度／俯仰／横滚与重建 yaw；日志没有关节角，故机器人关节沿用默认配置。圆盘在相机后方的证明不依赖关节遮挡，也不把静态几何当作实际回航成功。

## 3. 数据来源逐项核对

### (a) 移动账本

原始数据确实存在：runner 的 model_response.calls 保存工具名称、call_id 与 arguments；tool_results 保存 status、error_code、measured.translation_start_frame_m、measured.yaw_delta_rad、执行／停止反馈。共 7 次运动请求，其中 1 次被拒绝、6 次有真实运动测量（4 次 move_relative、2 次 turn）。

但当前 PublicObservationAdapter.payload 只接收 observation/results，不接收 decision.calls。它仅把 call_id/tool/status/error_code/deduplicated 和 stuck 等少量字段记为 action；实测平移只取模长 execution.displacement_m，丢失符号、二维向量及转角。MemoryRules 追加的是这个缩减后的 action，不是完整指令／结果账本。JSON 对每次运动并列保留原始指令、原始测量及实际 adapter action，不能把 events.jsonl 的完整运行日志冒充 memory.md 的记忆数据。

此外，state_packet 不传 ledger，当前工具没有读取旧路线或检索旧地标的接口。即使磁盘账本补全，也还需要任务层可检索的航迹／返回状态，而不是将全部历史塞入 prompt。本轮未补这些功能。

### (b) 起点地标及三维位置

最初 model_input 的 tracked_points 是 `[]`。第 1 次 track_point 选中的是蓝球上的 point-001，公开 relative_xy_m=`[2.8799, -0.5823]`；没有起点附近的地标被追踪。

PointTracker.backproject 内部能用深度与标定得到 3D world，但 describe／track_point／get_geometry 只公开 relative_xy_m、水平 range、bearing、pixel_uv 和 confidence，不公开 XYZ。记忆适配器 pose.position_m 也只写两维，不能声称已保存三维起点地图。初始 RGB 图像会写 PNG，深度与完整 SensorFrame 不落入这条基线日志；公开标定也没有内参 K。

当前 visual_feature 只有 image_id/pixel_uv，没有外观描述子；丢失点返回 null 几何，重新选点会生成新 ID，没有视觉重定位／关联到旧 home 点。point-001 在第 3 次决策后就丢失；离线重放到第 12 次时为 `stale`，过时对象也不会进入规划的有效 objects。

因此第 3 项不通过。二维地图足以支持平面航位推算，但这不等于满足本次明确要求的“初始起点地标及其三维位置”，也不能补上缺失的方向账本。

## 4. 独立评分与 1m 阈值

可用 `_base_pose()` 的真值记录首帧 `start_xy_GT`，评分时计算 `norm(current_xy_GT-start_xy_GT)`；相关真值只进入评估路径，不把目标坐标／成功布尔值提供给规划。当前 backend.evaluate 尚只评分单目标，本轮没有添加返回任务或修改 evaluator。

建议返回标准：先由独立测量确认蓝球点通过，再要求距起点 ≤1.0m、速度 <0.12m/s、绝对 yaw rate <0.25rad/s，且整轮无碰撞／跌倒。必须阶段门控，否则初始就在成功圆盘内会被误记为返回成功；finish 自述不计。

起点距蓝球中心 `3.052575` m；蓝球任一合格 standoff 位姿距起点至少 `1.872575` m，大于 1m。基线最终距起点 `1.932186` m，停在蓝球处不会直接通过返回条件。1m 是有效但较宽松的粗粒度返回阈值，不代表精确回到同一位姿或视觉闭环定位。

## 导航方式、GT 边界与漂移

从现有工具语义看，回程应优先用**带方向的实测运动航位推算**，有可靠 home 特征并能重定位时再用视觉修正。原则上只用原始公开工具的实测平移／转角即可组合 SE(2) 航迹、计算返回方向，不需要规划去读私有 `_base_pose()` 或 evaluator 真值；不能只累加请求值或标量路长。move_relative / turn 可输出有界原子动作，track_point / get_geometry 可以提供当前有效点的几何；但当前 memory.md 到规划的数据链没有完整方向账本，不能据此宣称该记忆回航已经可用。视觉回航缺初始 home 特征／重定位，二者结合也缺少上述数据与检索环节。

只反向重放请求值不可靠。四次成功平移相对请求的终点误差分别为 `[0.066938, 0.068563, 0.072654, 0.072257]` m；两次转向误差 `[0.038937, 0.044101]` rad。命令航位推算在最后一次运动后的位置误差为 **0.300363m**、yaw 误差 `0.106154` rad。相反，累加实测向量／实测转角，在该时刻误差仅 `3.14e-16` m；这是因为这些反馈本来就是从仿真真值差分计算的，不是证明了真实里程计无漂移。专门 stop 与 finish 的站稳运动不含在 move/turn 测量中，合计带来约 `0.012367` m 的账本缺口。

一条去程日志不能给出回程漂移上界、噪声模型或成功率；反向动作的噪声可能不对称，不能假设自动抵消。1m 真值评分仍然有意义，漂移只影响能否通过；但不能据此宣称视觉回航或精确导航。无需在本轮凭空添加噪声模型或重跑仿真。

**额外的关键混杂因素：现有 H0 的当前观测已经含起点相对累计里程计。** 在第 12 次决策输入里，translation=`[1.898825086820971, -0.2572085822984704]`，yaw=`-0.253561847`。只用这一帧即可算回起点向量 `-R(yaw)^T·translation = [-1.9026319463380248, -0.22734256513604612]` m，距起点 `1.916166` m，不需要早期历史、外部记忆或可见起点标记。

其来源不是带噪声估计器：backend.capture 把真实 `_base_pose()` 放入 SensorFrame.base_xy_yaw，Harness.observation 与首帧真值作差并旋转，manifest 也标为 idealized_simulated_proprioception_relative_to_episode_start。原始 move/turn 实测反馈同样由真实起止位姿差分得到。**这些是现有协议明确允许的公开传感器／工具反馈；使用它们，不等于规划偷偷读取私有评分 GT。** 保留现状，原则上可只凭公开反馈闭环回航而不另读私有 GT；问题是这条累计位姿通道对 H0 也开放，绕过了外部记忆需求，并且不能用来验证真实估计器漂移。若“GT 只评分”的含义还包括排除理想累计位姿通道，则当前观察协议不满足该更严格边界；不能把它改称为带噪声的真实里程计。本轮不擅自改变观察协议。

## 证据与复现

- [JSON 证据](/home/nuonuosenlin/Agent-harness/runs/memory-v1-demo-feasibility/return_to_start_preflight.json)：12 回合、历史边界、射线／连续域深度上界、原始与适配器账本对照、离线记忆重放、积分误差、源码定位和哈希。
- [复现脚本](/home/nuonuosenlin/Agent-harness/runs/memory-v1-demo-feasibility/return_to_start_preflight.py)；从仓库根目录使用既有环境运行：`.venv/bin/python runs/memory-v1-demo-feasibility/return_to_start_preflight.py --output-dir runs/memory-v1-demo-feasibility/return-recheck`。新目录避免覆盖证据。
- 原始蓝球 [events.jsonl](/home/nuonuosenlin/Agent-harness/runs/dashscope-validation-20261109-132737-c60cc5/20261109-212737-api-go_to_blue_ball-s0-e43663/events.jsonl)、[metrics.json](/home/nuonuosenlin/Agent-harness/runs/dashscope-validation-20261109-132737-c60cc5/20261109-212737-api-go_to_blue_ball-s0-e43663/metrics.json)、[trajectory.jsonl](/home/nuonuosenlin/Agent-harness/runs/dashscope-validation-20261109-132737-c60cc5/20261109-212737-api-go_to_blue_ball-s0-e43663/trajectory.jsonl)。

结论：**不通过**。第 3 项必需数据链不完整；另外，H0 的当前理想累计里程计绕过了历史遗忘／外部记忆需求。若要求连理想累计位姿也不得用于决策，则现有观察协议还不满足这一更严格边界。按要求停在离线复核，不改场景、不实现任务、不跑 demo、不调用 API。

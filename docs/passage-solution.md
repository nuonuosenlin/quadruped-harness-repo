# 穿门提前结束的解决办法

当前修复把模型的完成判断从“门框已经离开画面”改为结合可见门框的测量、实际机身里程计和公开完成条件进行判断。机器人仍由开启思考的 API 选择每一步动作，没有增加自动穿门或代替模型声明完成的程序。

## 实际改动

1. 公开传感器标定 `sensor_calibration`：相机相对机身的位置和光学轴方向由 MuJoCo 模型读取。当前相机向前偏移 0.32 米；相机过门和机身过门是不同条件。
2. 提供 `local_odometry`：以本轮开始时的机身位置和水平朝向为原点，连续报告机身实际平移和偏航。它由理想化仿真本体状态计算，未加入真实定位噪声，不提供门、目标的世界坐标或评测结果。
3. 公开 `completion_requirements`：穿门时机身基准点须从开口内部跨过门框，再沿穿门方向至少前进 0.8 米并停止；该余量直接从已有评分条件推导。目标到达任务也公开距离、朝向和停止容差。
4. 明确动作反馈：请求移动距离是目标值；控制器在约 6 cm 误差内开始停车，最终允许 10 cm 误差。模型应使用 `measured.translation_start_frame_m` 和累计里程计，不能将请求值累加为已经走过的距离。
5. 修改选点与完成指令：门框可见时先测量可靠特征；有效跟踪点会自动更新；深度和跟踪置信度不证明语义选点正确。门框移出视野后，应结合已测几何和实际机身进度确认净空，并为测量与门框厚度保留余量。

评分仍要求实际轨迹从开口内部通过、机身达到原有出口阈值、停止且没有碰撞或跌倒。后端没有放宽评分、改变步态策略或追加运动动作。单轮多个工具请求仍全部拒绝。

## 依据与适用范围

机体坐标系和相机光学坐标系的轴约定不同，应显式保留两者的变换；本项目的说明与 [ROS REP 103 官方原文](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst)一致。局部里程计适合维持短时间连续运动的参考，但真实系统会产生漂移，见 [ROS REP 105](https://github.com/ros-infrastructure/rep/blob/master/rep-0105.rst)。MuJoCo 的相机位置和朝向相对于其所在机体定义，见 [相机配置说明](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera)。这里使用这些坐标约定，不需要安装 ROS。

新增信息会改变模型的可用观测，清单已标为 `rgb_tracked_geometry_local_odometry_v2`；执行协议仍是 `bounded_relative_planar_motion_v1`。旧版结果和新版结果分别保留，不能作为严格的同观测条件模型能力比较。

DeepSeek 继续固定 `thinking.type=enabled` 并回传历史思考字段，协议见 [官方思考模式说明](https://api-docs.deepseek.com/guides/thinking_mode/)。官方 Chat Completions 参数没有列出 `parallel_tool_calls`，因此本次没有加入该未验证参数。

## 运行

```bash
./scripts/run_deepseek.sh --task go_through_red_triangle_tunnel --viewer
./scripts/run_deepseek.sh --task go_through_green_rectangle_tunnel --viewer
./scripts/run_deepseek.sh --task go_through_yellow_triangle_tunnel --viewer
```

本次验证统一使用种子 0、每项最多 20 次 API 调用、300 秒墙钟预算，模型与评分条件沿用之前的穿门测试。具体批次结果见 [验证记录](validation.md)。单次通过不构成可靠性统计，真实里程计漂移及更复杂门框布局仍需单独测试。

## 本轮验证结果（2026-10-28）

| 场景 | API 调用 | 最终机身前向坐标 | 原出口阈值 | 结果 |
| --- | --- | --- | --- | --- |
| 红色三角门 | 17 | 3.279 m | ≥3.000 m | 通过 |
| 绿色矩形门 | 17 | 3.237 m | ≥3.000 m | 通过 |
| 黄色三角门 | 19 | 3.103 m | ≥3.000 m | 通过 |

三次均由真实思考 API 自行调用 `finish`，独立评分确认实际轨迹穿过开口并到达停止区；没有碰撞或跌倒。坐标仅在此用于事后检查，没有提供给模型。全部 53 个 API 响应均包含思考字段。原始汇总和每项日志见 [summary.json](../runs/passage-solution-validation/summary.json)。

自动测试结果为 **230 passed**。本轮新增旋转起点、累计实际位移、相机标定、公开完成余量与敏感字段过滤的验证，并保留“机身未过门时仍判失败”的回归测试。

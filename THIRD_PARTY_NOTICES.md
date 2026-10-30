# Third-party sources and scope

本仓库整理本人课程项目中的新增 harness、启动/探针脚本和复现记录，不声称拥有上游仿真系统或模型。

- LIBERO: https://github.com/Lifelong-Robot-Learning/LIBERO ，固定 commit 8f1084e3132a39270c3a13ebe37270a43ece2a01。官方最小示例包装器依据其 Task 示例编写；上游许可证见 https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/LICENSE 。
- BEHAVIOR-1K / OmniGibson: https://github.com/StanfordVL/BEHAVIOR-1K ，v3.9.1，commit 26f2c7ef7b9cf96bd0414f81e1e751e493762779。empty 示例包装器调用现有官方示例；源码树、家庭/机器人资产、Isaac 二进制均未打包。各软件与数据的许可仍须分别确认，接受 NVIDIA EULA 不代表取得家庭数据许可。
- robosuite: https://github.com/ARISE-Initiative/robosuite/tree/v1.4.0 。scripts/libero-windows-compat.patch 是针对其 Windows DLL/绝对路径问题的两处局部补丁；并附有私有宏设置脚本，不包含完整源码。
- MuJoCo: https://github.com/google-deepmind/mujoco ，本机版本 2.3.7。
- RoboHarness: https://github.com/BinceQu/RoboHarness ，参考接口与运行依赖，不代表已完整复现原项目 Agent/基准。
- LeRobot: https://github.com/wensi-ai/lerobot ，BEHAVIOR 环境导入依赖记录中的固定 commit 436812bd8ee39b768c645c248c91f1330834e687；不包含该源码或训练数据。

新增部分包括：千问纯文本客户端、几何工具、独立 IK/OSC 闭环、阶段协议、离线测试与检查。官方示例调用和兼容适配不能描述为自研仿真引擎。

本次未替新增代码选择开源许可证。公开仓库的可见性设置与代码授权是不同事项；后续如需授予复用权，再明确新增代码许可证并保留第三方要求。

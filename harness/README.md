# Harness

接口、运行命令、已验证结果和局限见仓库根目录 [README](../README.md)。

- api_probe.py / text_client.py：纯文本百炼 API 连通性和工具调用。
- geometry.py / libero_loop.py：关键点、几何、IK、轨迹执行及观测闭环。
- protocol.py：阶段合同、合法轨迹 ID 和重复调用停止机制。
- test_offline.py：不调用 API、不启动仿真的回归检查。
- audit_run.py：复查原工作区保存的 v2 运行记录；无原始数据时不能执行该审计。

启动器执行本目录代码，环境和输出仍位于 D:\RoboHarnessSim。仓库没有上传运行日志、原始请求响应、图像或资产。运行 API 探针和闭环会产生新调用；整理仓库时没有执行它们。

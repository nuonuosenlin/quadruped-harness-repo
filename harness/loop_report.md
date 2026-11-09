> 历史记录：这是首次失败运行。用户随后批准的单次补测已成功，最新结果见 [补测报告](loop_retry_report.md)，9步、9503 tokens、最终距离2.20cm。以下保留原始报告。

# LIBERO 首次 LLM 闭环报告

日期：2026-10-28（Asia/Shanghai）。仅执行 1 次 LIBERO 仿真 episode；本次停止后未再发起 API 请求或重跑。

## 结果

**调用链已实测贯通，子任务未成功。** qwen3.8-flash 返回工具调用，本地几何/IK 生成轨迹，OSC_POSE 经 env.step 执行，随后用新观测计算距离。末端到汤罐可见表面关键点距离从 0.224926 m 降至 0.051355 m，仍超过用户指定的 0.03 m。

原始 BDDL：false。不声称物理接触、抓取或装篮完成。

- 场景：LIBERO-10 task 0，LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket。
- seed=0，初态索引=0。
- LLM 决策步/API 调用：23（最多允许 30）。
- 执行轨迹：3，分别为 touch、adjust、adjust。
- 仿真动作：99 个控制步，20 Hz；另有初始 10 个零动作稳定步。
- 闭环 tokens：输入 24,854，输出 1,399，合计 **26,253**。
- 先前纯 API 测试另有 456 tokens；两阶段合计 **26,709**。
- 第 24 次请求前，保守估计将超过累计 30,000 token 预算，触发 TOKEN_REVIEW 停止；该请求没有发送。实际用量未超过 30,000。
- 结束时 D 盘空闲约 41.02 GiB；未安装新依赖、下载资产或升级现有包。

API 实际请求和返回模型均为 qwen3.8-flash。此前认证 /models 列表包含该 ID、不含 qwen3.8-flash-next；没有核验控制台 UI，不将 API 列表描述为控制台确认。密钥只从环境变量读，不写入源码或日志。

## 逐步摘要

每步执行后均在本地自动调用 check_success；LLM 本轮未主动选择 check_success 工具。

| 步 | LLM 工具/关系 | 本地结果 | 距离 cm | 本步 tokens |
|---|---|---|---:|---:|
| 1 | track_keypoint | 追踪汤罐可见表面 | 22.49 | 1042 |
| 2 | solve_constraint / touch | traj_001，IK 通过 | 22.49 | 1201 |
| 3 | execute_trajectory | 46 控制步 | 14.70 | 1127 |
| 4 | track_keypoint | 刷新关键点 | 14.70 | 1184 |
| 5 | solve_constraint / touch | 拒绝：后续应使用 adjust | 14.70 | 1200 |
| 6 | track_keypoint | 刷新关键点 | 14.70 | 1075 |
| 7 | solve_constraint / touch | 同上拒绝 | 14.70 | 1200 |
| 8 | track_keypoint | 刷新关键点 | 14.70 | 1075 |
| 9 | solve_constraint / touch | 同上拒绝 | 14.70 | 1213 |
| 10 | track_keypoint | 刷新关键点 | 14.70 | 1075 |
| 11 | solve_constraint / touch | 同上拒绝 | 14.70 | 1200 |
| 12 | solve_constraint / adjust | traj_002，IK 通过 | 14.70 | 1079 |
| 13 | execute_trajectory | 29 控制步 | 9.90 | 1124 |
| 14 | solve_constraint / touch | 同上拒绝 | 9.90 | 1164 |
| 15 | track_keypoint | 刷新关键点 | 9.90 | 1079 |
| 16 | solve_constraint / touch | 同上拒绝 | 9.90 | 1228 |
| 17 | track_keypoint | 刷新关键点 | 9.90 | 1075 |
| 18 | solve_constraint / touch | 同上拒绝 | 9.90 | 1252 |
| 19 | track_keypoint | 刷新关键点 | 9.90 | 1090 |
| 20 | solve_constraint / touch | 同上拒绝 | 9.90 | 1213 |
| 21 | solve_constraint / adjust | traj_003，IK 通过 | 9.90 | 1073 |
| 22 | execute_trajectory | 24 控制步 | 5.14 | 1117 |
| 23 | track_keypoint | 刷新关键点 | 5.14 | 1167 |

## 停止原因及待批准修复

证据显示 8 次 touch 被阶段校验拒绝，9 次 track_keypoint；几何规划与已执行轨迹没有出现 IK/控制异常。3 次轨迹的最终目标误差约 2.12 / 2.00 / 2.32 mm。

当前编排每轮只发送新观测和上一个工具结果，且 system prompt 每次都包含 Begin by track_keypoint。虽然观测含 executions，未充分保留阶段约束；模型多次重新选择 touch，错误结果又被后续追踪结果覆盖。这是本次编排不足；原因判断来自日志，尚未通过修复后的新运行验证。

建议先修复阶段上下文、按阶段收紧可选关系，并对重复无效调用及时停止，再申请额外 1 次测试。不得仅提高预算或悄悄自动重跑。建议新测试最多 12 个决策步、累计 15,000 tokens，继续保持单任务、纯文本和原 3cm 判据。本轮没有实施这些运行逻辑修改，也没有发起第二次 episode，等待用户决定。

## 四工具实现与验证状态

- track_keypoint(bbox,name)：mask 腐蚀 1 像素，米制平面深度，K 反投影、OpenCV camera-to-world T；选择实际可见表面像素，后续以初始锚点做近邻关联和 3cm 门控。本次锚点约 [-0.088328,-0.125282,0.517661] m，pixel=[81,131]，全程目标关联未漂移。不使用物体位姿真值来生成目标。
- solve_constraint(A,B,relation)：touch 单次进展上限 8cm，adjust 5cm，朝目标前 2cm 的位置规划；Cartesian 路点 + 独立 MjData 上的阻尼数值 IK。关节解保存为规划证据，实机执行接口不在本任务范围。当前 IK 验收拒绝位置残差大于 8mm；保存初始姿态并加入姿态误差，但还缺少最终姿态残差的独立验收字段。
- execute_trajectory(traj)：只接受已生成且未使用、未过期的轨迹 ID，通过本地反馈转换为 7 维 OSC_POSE。3 条轨迹共 99 步已实测。没有完整碰撞规划或接触保证。
- check_success()：自动重新观测关键点，计算实际 EEF 与关键点距离并返回 bool、新关键点和单独 BDDL bool。所有 23 步距离判据核对一致；本次 false。
- collinear / parallel：纯几何投影/方向算法通过离线检查；轴关键点、IK 轨迹及机器人执行尚未验证，工具不会为这两个关系发出可执行轨迹。

## 仿真特权信息与纯文本审计

使用了：实例 mask 真值、语义名称关联和 bbox；模拟器深度与 K/T；机器人 EEF/关节状态；IK 使用 MuJoCo 运动学模型；原始 BDDL 成功谓词。后续须替换为本地真实检测/跟踪、实际 RGB-D 标定和机器人状态接口。当前实现只是基于可见表面的最小近邻关联，并不等同完整 Geometry Tracker。

23 个实际请求的 messages 均为纯字符串内容，payload 不含 image_url、input_image、base64、音频字段。RGB/深度/mask 只作为本地感知或证据保存，不发送给模型。不调用 VLM API、不训练模型、不新增动作头、不运行 BEHAVIOR、不操作真机、不修改飞书。未修改官方仓库核心或已验证探针。

验证：5 项离线测试通过；另对实际记录做只读审计，核对 23 次请求 token 求和、纯文本 payload、99 个动作的维度/数值/范围和距离成功判据，均通过。运行后的纯文本审计结果不能替代任务成功。

## 交付与复跑

代码：harness/libero_loop.py、geometry.py、text_client.py。

```powershell
& 'D:\RoboHarnessSim\harness\run-libero-loop.ps1'
```

上述命令会新建 episode 并产生 API 费用；本轮停止后不自动执行。完整接口、限制及离线检查命令见 README.md。

证据目录：runs/touch_20261028_202556/。result.json 保存全部逐步请求、响应、工具结果和校验；steps.jsonl 是逐步日志；simulation.jsonl 是控制动作日志；traj_*.json 是轨迹与 IK；before/after_rgb.png、before/after_geometry.npz 是仅本地观测证据。

下一步优先修复阶段编排和重复错误保护，再验证 3cm 成功；随后补姿态残差、遮挡/跟踪、碰撞规划、collinear/parallel 机器人验证。完整装篮和 BEHAVIOR 接入另行开展；BEHAVIOR 家庭资产不是本次 LIBERO 的依赖。


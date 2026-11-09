# Qwen API preflight report

Date: 2026-10-28 (Asia/Shanghai)

## Result

- Status: passed; simulation has not started.
- Endpoint: https://dashscope.aliyuncs.com/compatible-mode/v1
- Actual requested and returned model: qwen3.8-flash.
- Authenticated GET /models included qwen3.8-flash and did not include qwen3.8-flash-next. Console UI was not inspected; catalog evidence does not constitute console verification.
- Ordinary chat returned API_OK: 39 prompt + 2 completion = 41 tokens.
- Function call returned finish_reason=tool_calls and one echo_keypoint call. Its arguments parsed as JSON and exactly matched name=probe, xyz=[0.1,0.2,0.3]. Usage: 363 prompt + 52 completion = 415 tokens.
- Total: 2 Chat Completion requests, 456 tokens. The pure local echo tool result was recorded; no extra post-tool model request was made.
- No image, video, audio or simulator observations were sent. All message content was plain text.
- Credential read only from DASHSCOPE_API_KEY; launcher inherits the Windows User environment value when the process value is absent. No credential is stored in source or logs.
- Standard-library HTTP client; existing LIBERO Python 3.8 environment reused. No package install or official source/probe modification.
- Disk free at preflight: 41.02 GiB. Existing env.ps1 guards a 10 GiB reserve.

## Evidence

runs/api_20261028_201720/result.json contains both requests, responses, token usage and parsed tool arguments. No authorization header is recorded.

## Re-run (incurs two new API completion requests)

```powershell
& 'D:\RoboHarnessSim\harness\run-api-probe.ps1'
```

The script has no retries and stops on any failure. Each completion requests max_tokens=256 with thinking disabled. A missing usage record, more than 2000 tokens per request, or more than 4000 total tokens fails the preflight for review.

## Pending user decision

The verified LIBERO scene's original BDDL objective is to put both alphabet soup and tomato sauce into the basket. The requested touch/adjust first loop also permits a simpler distance-based objective. These are different success claims. Before implementing or running the one allowed simulation episode, confirm whether to use a named touch/adjust subtask (EEF within 0.03 m of a visible-surface keypoint on alphabet_soup_1; not a physical contact or BDDL completion claim), or the original two-object basket objective.

No harness geometry tool or simulation loop has been implemented or run yet. No BDDL or task success is claimed. Once the task is selected, implement the four tools and log privileged masks, simulator calibration, robot state and IK model use explicitly. Track BDDL success separately from distance-based subtask success. Validate collinear/parallel separately and keep BEHAVIOR out of scope.

## Official references

- https://help.aliyun.com/en/model-studio/qwen3-8-flash
- https://help.aliyun.com/en/model-studio/qwen-function-calling

## Subsequent progress
The user selected the touch/adjust distance subtask. One episode was run and stopped by the token budget guard before success; see loop_report.md. Do not interpret the earlier pending-decision section as the current state.

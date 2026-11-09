# LIBERO text-only Qwen harness

This harness reuses D:\RoboHarnessSim and the verified LIBERO environment. No package installation, model training, action head, VLM call or official repository/probe modification is required.

## Commands

Run the offline checks (no API calls, no simulator episode):

```powershell
. 'D:\RoboHarnessSim\scripts\env.ps1'
& 'D:\RoboHarnessSim\envs\libero\python.exe' -B 'D:\RoboHarnessSim\harness\test_offline.py'
```

Run one new simulation episode (makes billable API calls; do not run a batch):

```powershell
& 'D:\RoboHarnessSim\harness\run-libero-loop.ps1'
```

The launcher imports env.ps1 and uses the existing micromamba LIBERO prefix. Python reads DASHSCOPE_API_KEY from the process environment only; when absent, the PowerShell launcher inherits the Windows User environment variable. Do not put credentials in code, CLI arguments, logs or documents.

The successful API preflight is a prerequisite; its result is referenced explicitly by libero_loop.py. To perform a separate new preflight:

```powershell
& 'D:\RoboHarnessSim\harness\run-api-probe.ps1'
```

## Subtask and limits

The user selected a touch/adjust distance subtask in the verified LIBERO-10 task-0 scene, with seed 0 and initial state 0. Success means the actual EEF reference point is within 0.03 m of the currently tracked visible soup surface keypoint. It does not establish physical contact or completion of the original two-object basket BDDL task. BDDL success is recorded separately.

One process initializes exactly one simulation episode and sends at most 12 Chat Completion requests. Each request allows one function call and at most 384 completion tokens, with thinking disabled. Each actual request is limited to 6000 total tokens and the episode to 15000 total tokens; a conservative byte-based pre-request estimate may stop earlier. No retry or fallback model is used. Simulation is capped at 900 post-warmup control steps; initial settling uses 10 zero actions. env.ps1 and the loop guard a 10 GiB disk reserve.

## Files and interfaces

- geometry.py: tool schemas, bounded touch/adjust geometry; pure collinear/parallel geometry helpers.
- protocol.py: persistent workflow phase, legal tools/arguments and repeated-call guards.
- text_client.py: the sole network transport; only plain string message content accepted, no multimodal fields. Uses POST /chat/completions at the user-specified DashScope endpoint.
- libero_loop.py: local perception, numerical IK, trajectory store, OSC execution, observation checks, and LLM loop.
- test_offline.py: offline geometry, transport and syntax checks.
- runs/touch_*/: per-episode evidence and results.

track_keypoint(bbox, name) uses a top-left-origin integer bbox [x0,y0,x1,y1), privileged instance mask, and metric image-plane depth. The mask is eroded by 1 pixel. It backprojects actual surviving pixels with K and OpenCV-camera-to-world T. The initial selected surface pixel is nearest to the current EEF. Later observations associate visible points to this initial anchor with a 0.03 m gate; missing/occluded observations cannot count as success. This is a minimal association tracker, not a real visual tracker.

solve_constraint(keypoint_A, keypoint_B, relation) resolves keypoint IDs eef and alphabet_soup_1. touch allows at most 0.08 m progress, adjust 0.05 m, towards a point 0.02 m short of the target along the approach direction. Waypoints are spaced at most 0.01 m apart. A damped Jacobian IK uses an independent MuJoCo MjData, joint limits and the initial EEF orientation. It does not set live simulation state. It stores joint solutions as planning evidence and returns an opaque trajectory ID.

execute_trajectory(traj) accepts only an issued, unused, current-state trajectory ID. A local feedback servo follows Cartesian waypoints with the verified OSC_POSE scaling (translation +/-0.05 m, rotation +/-0.5 rad per normalized unit), normalized action bounds and open gripper. Joint IK solutions validate the Cartesian path; joint angles are not sent as OSC actions. Actual motion occurs only through env.step. There is no full collision planner or contact guarantee.

check_success() returns a bool, new keypoints, measured distance, threshold and separate BDDL bool. It refreshes depth/mask observations and never infers success from the planned goal.

## LLM contract and logs

The model selects tools and relations; it never emits direct low-level robot actions. Every request contains the current observation as text, keypoint numbers, bounding box, available trajectory IDs and persistent workflow phase. The previous assistant function call and tool result are retained as a standard assistant/tool exchange. Earlier history is summarized by persistent workflow state; the initial instruction is not restarted on every turn. Legal relation enums are restricted to touch before the first execution and adjust afterwards. Repeating the same invalid call twice, or making two calls without phase progress, stops the episode. All requests, responses, parsed function arguments, local results and post-tool success checks are retained in result.json and steps.jsonl. simulation.jsonl records every post-warmup OSC action and measured EEF state. traj_*.json stores waypoints and IK solutions. before/after RGB and aligned depth/mask/calibration are local artifacts only and are never network payloads.

## Privileged information and remaining work

Privileged: instance mask/name association and bbox extraction, simulated depth, camera K/T, EEF/joint state, the MuJoCo kinematic model and BDDL predicate. Object pose truth is not used to construct the tracked target. Replace mask/name association with a real local detector/tracker, calibrate real RGB-D and validate occlusion handling before transfer.

collinear projects a point onto a line; parallel specifies a normalized target direction. These pure geometry routines have offline checks. Axis tracking, rotation planning and robot execution for these relations are not validated or exposed as executable trajectories in this milestone. Original BDDL basket completion and BEHAVIOR integration are future work. BEHAVIOR family assets are unrelated to this LIBERO subtask and are not downloaded.


## Latest measured result

The authorized single retry passed: 9 LLM steps, 9503 tokens, 117 control steps, final surface distance 0.0220016774 m. Original BDDL remains false. See [retry report](loop_retry_report.md) and runs/touch_20261028_203317/result.json. The first failed run remains in runs/touch_20261028_202556. Offline audit: audit_run.py (no API or simulator).


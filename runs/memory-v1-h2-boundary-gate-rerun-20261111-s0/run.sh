#!/usr/bin/env bash
set -euo pipefail
cd /home/nuonuosenlin/Agent-harness
export MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
export MODEL_NAME=deepseek-v4.1-flash
export PYTHONPATH="/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-boundary-gate-rerun-20261111-s0/instrumentation:$PWD"
export MEMORY_H2_RUN_ARTIFACTS="/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-boundary-gate-rerun-20261111-s0"
.venv/bin/python -m go2_demo --mode api --provider compatible --no-env-proxy --api-key-file "$HOME/deepseekapi.txt" --model-name deepseek-v4.1-flash --task memory_ab_occluded_v1 --memory-v1 --seed 0 --max-model-calls 120 --max-wall-seconds 2400 --max-sim-seconds 600 --history-turns 6 --api-timeout 90 --max-output-tokens 8192 --viewer --runs-dir "/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-boundary-gate-rerun-20261111-s0/H2" 2>&1 | tee "/home/nuonuosenlin/Agent-harness/runs/memory-v1-h2-boundary-gate-rerun-20261111-s0/console.log"

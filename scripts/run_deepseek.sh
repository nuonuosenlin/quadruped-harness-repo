#!/usr/bin/env bash
set -euo pipefail

# The Python entry point enforces API-only execution with thinking enabled.

project_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
selection=()
for argument in "$@"; do
  case "$argument" in
    --task|--task=*|--suite|--suite=*|--list-tasks) selection=(selected); break ;;
  esac
done
if [ "${#selection[@]}" -eq 0 ]; then
  selection=(--task go_to_blue_ball)
else
  selection=()
fi
exec "$project_dir/.venv/bin/python" -m go2_demo \
  --mode api --provider deepseek --no-env-proxy \
  --model-name deepseek-flash --api-key-file "$project_dir/../deepseekapi.txt" "${selection[@]}" "$@"

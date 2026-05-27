#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="${REPO_ROOT}/.venv"
DEFAULT_ENGINE_PATH="/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64"

echo "==> Setting up Python environment in ${VENV_PATH}"
rm -rf "${VENV_PATH}"
python3 -m venv "${VENV_PATH}"

source "${VENV_PATH}/bin/activate"

# Ensure pip exists even if the base image's venv bootstrap is incomplete.
python -m ensurepip --upgrade
python -m pip install --upgrade pip

echo "==> Installing dependencies from requirements.txt"
python -m pip install -r "${REPO_ROOT}/requirements.txt"

LOCAL_SDK_PATH="/home/acald-creator/go/src/github.com/acald-creator/luckyrobots"
if [[ -d "${LOCAL_SDK_PATH}" ]]; then
  echo "==> Installing local LuckyRobots fork from ${LOCAL_SDK_PATH}"
  python -m pip install -e "${LOCAL_SDK_PATH}"
fi

if [[ -z "${LUCKYENGINE_PATH:-}" ]]; then
  if [[ -d "${DEFAULT_ENGINE_PATH}" ]]; then
    export LUCKYENGINE_PATH="${DEFAULT_ENGINE_PATH}"
    echo "==> Using detected LuckyEngine path:"
    echo "    LUCKYENGINE_PATH=${LUCKYENGINE_PATH}"
  else
    echo "==> LuckyEngine path is not set."
    echo "Set it before running the simulator:"
    echo "  export LUCKYENGINE_PATH=/absolute/path/to/LuckyEngine-2026.1-Linux-x64"
  fi
else
  echo "==> Using existing LUCKYENGINE_PATH=${LUCKYENGINE_PATH}"
fi

echo
echo "Setup complete."
echo "Next steps:"
echo "  source .venv/bin/activate"
echo "  python run_lucky_robots.py"

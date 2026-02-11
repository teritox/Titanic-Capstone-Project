#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_NAME="titanic-capstone-env"

if ! command -v conda >/dev/null 2>&1; then
  echo "Error: conda is not installed or not on PATH."
  exit 1
fi

cd "$ROOT_DIR"

echo "Updating Conda environment: $ENV_NAME"
conda env update -f environment.yml

echo "Installing project package in editable mode"
conda run -n "$ENV_NAME" python -m pip install -e .

echo "Installing git hooks with pre-commit"
conda run -n "$ENV_NAME" pre-commit install --install-hooks

echo "Running pre-commit on all files (pass 1: apply fixes if needed)"
if ! conda run -n "$ENV_NAME" pre-commit run --all-files; then
  echo "Pre-commit changed files. Running pass 2 to verify everything is clean."
fi

echo "Running pre-commit on all files (pass 2: verify clean state)"
conda run -n "$ENV_NAME" pre-commit run --all-files

echo "Setup complete."
echo "Activate the environment with: conda activate $ENV_NAME"

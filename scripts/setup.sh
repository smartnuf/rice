#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/_common.sh
source "${SCRIPT_DIR}/_common.sh"

require_repo_root

echo "Setting up RICE development environment"

PYTHON_BIN=""
for candidate in python3.12 python3.11 python3; do
    mapfile -t candidate_paths < <(type -P -a "${candidate}" 2>/dev/null | awk '!seen[$0]++')
    for candidate_path in "${candidate_paths[@]}"; do
        case "${candidate_path}" in
            "${PWD}/.venv/"*) continue ;;
        esac
        if "${candidate_path}" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' >/dev/null 2>&1; then
            PYTHON_BIN="${candidate_path}"
            break
        fi
    done
    [[ -n "${PYTHON_BIN}" ]] && break
done

if [[ -z "${PYTHON_BIN}" ]]; then
    echo "Error: Python 3.11 or newer is required, but no suitable interpreter was found." >&2
    exit 1
fi

echo "Selected base Python:"
"${PYTHON_BIN}" -c 'import sys; print("  executable:", sys.executable); print("  version:", sys.version.split()[0])'

run "${PYTHON_BIN}" -m venv .venv
run .venv/bin/python -m pip install --upgrade pip setuptools wheel
run .venv/bin/python -m pip install -e ".[dev]"

echo
echo "Virtual environment Python:"
.venv/bin/python -c 'import sys; print("  executable:", sys.executable); print("  version:", sys.version.split()[0])'

echo
echo "Import smoke test:"
.venv/bin/python - <<'PY'
import sys

import networkx
import pytest
import rice

print("python", sys.executable)
print("networkx", networkx.__version__)
print("pytest", pytest.__version__)
print("rice", rice.__file__)
PY

echo
echo "Setup complete."

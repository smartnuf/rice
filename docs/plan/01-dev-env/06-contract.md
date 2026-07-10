# 01-dev-env / 06 — Align Makefile, scripts, README, and AGENTS.md

Status: `done`

## Goal

Ensure there is one development contract, not several subtly different ones.

## Required contract

- Linux/WSL/Codex: `make setup`, `make test`, `make check` may be used.
- Windows PowerShell: `./scripts/setup.ps1`, `./scripts/test.ps1`, `./scripts/check.ps1` must be available and must not depend on Make.
- All paths use `.venv` explicitly.
- README and AGENTS.md must agree.

## Done means

- A fresh contributor can follow README.
- Codex can follow AGENTS.md.
- Both paths run equivalent commands.

## Progress notes

- The Linux/WSL Make path and Bash script path are aligned: Make delegates
  setup, test, lint, check, and clean to `scripts/*.sh`.
- README and AGENTS.md document the non-Make Bash path and require explicit
  `.venv/bin/python` usage on Linux/WSL.
- Native PowerShell scripts now provide the Windows path without Make, Bash,
  WSL, or activation, using `.venv\Scripts\python.exe` explicitly.
- README and AGENTS.md document the native PowerShell commands and the same
  check ordering as `scripts/check.sh`: lint, tests, support census, bundle
  assignment census, labeling census, legacy LC count, and legacy generic count.
- Evidence: the native Windows PowerShell path successfully ran `setup.ps1`,
  `test.ps1`, `lint.ps1`, and the complete `check.ps1` validation sequence.

- 2026-07-10: Hardened setup and cleanup scripts after PR review: Bash scripts
  avoid Bash-4-only helpers such as `mapfile`, setup probes require working
  `venv` support before selecting Python, Windows setup accepts forward-compatible
  `py -3` launcher runtimes, and Windows cleanup skips directory reparse points
  before recursion. Added regression coverage for script parsing and selection
  behavior.

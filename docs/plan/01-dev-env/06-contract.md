# 01-dev-env / 06 — Align Makefile, scripts, README, and AGENTS.md

Status: `todo`

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

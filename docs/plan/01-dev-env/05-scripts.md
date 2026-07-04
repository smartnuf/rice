# 01-dev-env / 05 — Create scripts under `scripts/`

Status: `todo`

## Goal

Make Windows-native development first-class without requiring `make`.

## Proposed script set

```text
scripts/
  setup.ps1
  test.ps1
  lint.ps1
  check.ps1
  clean.ps1
  setup.sh
  test.sh
  lint.sh
  check.sh
  clean.sh
```

## Requirements

- PowerShell scripts are the canonical Windows-native path.
- Shell scripts are the non-Make Linux/macOS/WSL path.
- Scripts must use `.venv` explicitly.
- Scripts must print the Python executable they use.
- Scripts must fail clearly if run from the wrong directory.

## Done means

- Windows users can run `./scripts/setup.ps1` and `./scripts/test.ps1` without installing Make.
- Linux/WSL users can run `./scripts/setup.sh` and `./scripts/test.sh` without Make.
- Make targets can delegate to these scripts where practical.

# 08-docs / 01 — Document developer workflow

Status: `prog`

## Goal

Make the development workflow easy to follow.

## Required sections

- WSL2/Linux setup.
- Windows PowerShell setup.
- Codex instructions.
- Test commands.
- Slow/full enumeration commands.
- Cleaning and rebuilding `.venv`.

## Done means

- README and AGENTS.md are consistent.
- New contributors do not need to infer the workflow.

## Progress notes

- 2026-07-09: Documented CLI argument-placement expectations in `AGENTS.md`,
  README examples, and support-census docs. Future argument-parsing changes
  should verify both top-level and subcommand help before handoff.

- 2026-07-10: Documented exact long-option parsing, zero-budget census
  boundary behaviour, and the tested `networkx>=3.2` dependency floor.

## Progress notes

- 2026-07-11: Documented change-aware validation in README and AGENTS.md,
  including lightweight documentation validation, full-validation escalation for
  unknown/tooling changes, and the rule not to duplicate checks already included
  in `make check`.

- 2026-10-03: Added the explicit candidate-HEAD Codex review checkpoint to
  `AGENTS.md` for bounded engineering work, preserving exploratory research and
  separate mathematical/evidential checking. Automatic review is not assumed;
  the author requests review of a genuine candidate and revalidates material
  corrections. Broader developer-workflow documentation remains in progress.

- 2026-10-03: Reconciled the checkpoint so every post-review commit requires
  fresh independent review of its exact HEAD, including non-material edits.
  Materiality determines affected validation and self-review, not whether the
  new candidate needs review. The broader documentation task remains in progress.

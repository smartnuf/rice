# 04-tests / 04 — Regression tests for cleanup

Status: `todo`

## Goal

Ensure removing legacy implementation and generic `X` support does not silently break intended behaviour.

## Tasks

- Preserve tests for still-supported R/L/C behaviour.
- Remove tests that only assert deleted behaviour.
- Add tests for clear failure on removed syntax where useful.
- Confirm docs examples run or at least parse.

## Done means

- Cleanup removes only intended behaviour.
- Test failures guide users away from removed APIs.

# 02-cleanup / 03 — Remove generic `X` implementation, tests, and docs

Status: `todo`

## Goal

Remove the generic `X` element if it is no longer part of the intended public model.

## Tasks

- Find source references to `X`.
- Find tests that exercise generic `X` behaviour.
- Find docs/examples that mention generic `X`.
- Decide whether any concept should be replaced by explicit R, L, or C handling.
- Remove the implementation and update tests.

## Done means

- Generic `X` is absent from the public API and docs.
- Tests cover the intended R/L/C-only behaviour.
- Failure messages are clear if old `X` syntax is encountered.

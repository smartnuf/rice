# 04-tests / 02 — Golden-count tests

Status: `todo`

## Goal

Use stable generated counts to detect accidental changes.

## Initial golden targets

- Very small hand-checkable cases.
- Explicit subset: `R <= 2`, `L+C <= 3`.
- Ladenheim comparison slice, including `R=3`, `L+C=2`.

## Done means

- Golden counts are stored in machine-readable form.
- Tests fail when counts change unexpectedly.
- There is a documented process for intentionally updating golden counts.

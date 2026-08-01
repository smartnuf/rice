# 07-tests / 02 — Golden-count tests

Status: `prog`

## Goal

Use stable generated counts to detect accidental changes.

## Initial golden targets

- Very small hand-checkable cases.
- Explicit subset: `R <= 2`, `L+C <= 3`.
- Ladenheim structural slice: `R+L+C <= 5` and `L+C <= 2`, including the
  four-resistor/one-reactive cases present in the historical 148 starting set.
- Ladenheim 108 comparison budget: `R <= 3`, `L+C <= 2`, and `R+L+C <= 5`.

## Done means

- Golden counts are stored in machine-readable form.
- Tests fail when counts change unexpectedly.
- There is a documented process for intentionally updating golden counts.

## Progress notes

- Golden tests now exist for the phase-1 support-census table through
  `max_edges=8` (the Python helper name; CLI examples use `--max-support-edges`), the phase-2 raw simple-bundle assignment table and
  `1,166,714` leaf total, and the phase-3 canonical bundle-labeling table with
  total `830,094`. The legacy multiset-bundle counter (both its `lc` and
  previously-removed `generic` modes) has been removed in full
  (`docs/plan/02-cleanup/02-legacy.md`, following
  `docs/plan/02-cleanup/03-generic-x.md`); its historical totals are recorded
  only as a labelled historical citation in `docs/results.md`, not as a live
  golden test.
- The reduced-model `R <= 2`, `L+C <= 3` golden output is stored in
  `data/counts/small-r2-x3.json` and tested for exact equality against CLI JSON.
  Its regeneration command is `.venv/bin/python -m rice count networks
  --profile golden --format json`; no no-argument network count is implied.
- `data/counts/ladenheim-148.json` is the deterministic structural 148-record
  golden catalogue. `tests/test_ladenheim.py` checks the expected
  `3, 6, 16, 38, 85` distribution, total 148, the eight `R=4`, `L+C=1` cases,
  record invariants, selected-source provenance, and exact committed-artifact
  regeneration. The documented drift check is `.venv/bin/python
  scripts/generate_ladenheim_148.py --check`; intentional updates use the
  corresponding `--write` command followed by review of the generated diff.

## Near-term next steps

1. Add golden comparison coverage for the later canonical 108 catalogue when
   its exclusions and historical mapping are implemented.
2. Keep future larger reduced-model golden artifacts regenerable from
   documented commands without manual post-processing.

# 07-tests / 02 — Golden-count tests

Status: `prog`

## Goal

Use stable generated counts to detect accidental changes.

## Initial golden targets

- Very small hand-checkable cases.
- Explicit subset: `R <= 2`, `L+C <= 3`.
- Bounded `R <= 3` slice (see `docs/plan/03-counting/05-ladenheim.md`):
  `R <= 3`, `L+C <= 2`, and `R+L+C <= 5`, including the `R=3`, `L+C=2`
  boundary. This is a well-defined slice of the current reduced-topology
  model in its own right; per `docs/ladenheim_benchmark.md` (2026-07-10), it
  is not itself the defining scope of the historical 148-network set, so its
  golden count is not to be described as a reproduction of 148, 108, or 62.

## Done means

- Golden counts are stored in machine-readable form.
- Tests fail when counts change unexpectedly.
- There is a documented process for intentionally updating golden counts.

## Progress notes

- Golden tests now exist for the phase-1 support-census table through
  `max_edges=8`, the phase-2 raw simple-bundle assignment table and
  `1,166,714` leaf total, and the phase-3 canonical bundle-labeling table with
  total `830,094`. The legacy multiset-bundle counter (both its `lc` and
  previously-removed `generic` modes) has been removed in full
  (`docs/plan/02-cleanup/02-legacy.md`, following
  `docs/plan/02-cleanup/03-generic-x.md`); its historical totals are recorded
  only as a labelled historical citation in `docs/results.md`, not as a live
  golden test.
- The reduced-model `R <= 2`, `L+C <= 3` golden output is now stored in `data/counts/small-r2-x3.json` and tested for exact equality against CLI JSON so the documented regeneration command can be diffed without post-processing. The no-argument `rice reduced` path defaults to this fast golden slice. Ladenheim golden outputs have not yet been generated.

## Near-term next steps

1. Add Ladenheim-slice golden counts only after the reduced distinctness contract
   is implemented enough to make those counts meaningful.
2. Keep any future reduced-model golden artifacts regenerable from documented
   commands without manual post-processing.

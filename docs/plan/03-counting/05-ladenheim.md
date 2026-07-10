# 03-counting / 05 — Define the Ladenheim comparison slices

Status: `todo`

## Goal

Define the enumeration slices used when comparing this project's counts
against the historical Ladenheim benchmark, and keep them clearly separate
from the historical construction itself.

## Revision note (2026-07-10)

This task previously stated that `R <= 3 / L + C <= 2 / R + L + C <= 5` was
"the correct comparison target" for the historical 148-network set. That was
wrong: the 148-network set's defining scope has no independent resistor
bound; the `R <= 3` bound belongs to the later 108-network canonical set, not
to 148. See `docs/ladenheim_benchmark.md` for the full reassessment,
including a verified reproduction of 140 under the old (incorrect) slice and
a diagnostic reproduction of 149 under the corrected 148 scope. Do not read
that 149 figure as a validated reproduction of 148; it is a diagnostic
finding, not a completed Stage B (see `docs/plan/04-ladenheim/01-148.md`).

## Two slices, not one

- **148-scope slice**: `L + C <= 2`, `R + L + C <= 5`, with no independent
  bound on `R`. This is the actual initial scope of the historical
  148-network set. The current CLI cannot express this directly as a single
  rectangular `--max-r`/`--max-reactive` region; it requires a loose
  rectangular superset (e.g. `--max-r 5 --max-reactive 2`) followed by a
  post-hoc filter on `r + (l + c) <= 5` using
  `iter_reduced_topology_signatures` and
  `reduced_signature_component_counts`, as demonstrated in
  `docs/ladenheim_benchmark.md`.
- **Bounded `R <= 3` slice**: `R <= 3`, `L + C <= 2`, `R + L + C <= 5`. This
  remains a useful, well-defined region in its own right — it matches the
  resistor range of the eventual 108-network canonical set and gives a
  smaller, fast slice for regression testing — but it must not be presented
  as the defining scope of the 148-network set. The verified count for this
  slice under the current reduced-topology model is 140 (see
  `docs/ladenheim_benchmark.md`); this is a fact about the current
  implementation's own model, not a claim of agreement or disagreement with
  148, 108, or 62.

## Tasks

- Keep both slices named and documented separately; do not let one stand in
  for the other.
- Add a small reporting helper (script or test, not new production
  enumeration code) that computes the 148-scope slice by composing existing
  exported API functions, if one does not already exist.
- Do not compare either slice's count against 148, 108, or 62 until the
  independent Ladenheim structural reproduction (`docs/plan/04-ladenheim/`,
  Stages A-D) exists. A rectangular RICE count matching or not matching a
  historical number is not by itself informative, because RICE's reduction
  and Ladenheim's 2-isomorphism are different (if related) relations — see
  `docs/ladenheim_benchmark.md`.

## Done means

- The 148-scope slice and the bounded `R <= 3` slice are both named,
  documented, and distinguished from each other and from the historical
  148/108/62 figures.
- The `3+2` boundary case (`R = 3`, `L + C = 2`, total `5`) is covered by the
  bounded slice's tests, where it already sits inside the full `R <= 3`,
  `L + C <= 5` scope but outside the smaller `R <= 2`, `L + C <= 3` subset.
- No documentation claims this task reproduces 148, 108, or 62; that
  reproduction is tracked separately under `docs/plan/04-ladenheim/`.

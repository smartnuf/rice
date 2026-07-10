# 08-docs / 02 — Document counting methodology

Status: `prog`

## Goal

Explain how counts are generated and what they mean.

## Required content

- Scope definition using `R` and `L+C` bounds.
- Definition of distinctness.
- Generation method.
- Rejection rules.
- Canonicalisation method.
- Descriptor conversion method.
- Output table interpretation.

## Done means

- A reader can reproduce the counts.
- The limits of the method are clear.

## Progress notes

- The repository now has normative model docs for the intended reduced model and
  support-census phase, plus docs that label the current multiset-bundle counter
  as legacy.
- `docs/results.md`, `docs/computation.md`, and the README record the
  legacy count results, the phase-1 support-census target table, and the phase-2
  raw simple primitive bundle-assignment target table.
- `docs/bundles_and_multiedges.md` documents the staged current status: legacy
  `count_networks` still uses multiset component-count bundles, `rice supports`
  implements phase 1, and `rice bundles` implements the phase-2 raw assignment
  census.
- Reduced counting methodology is documented for the first complete `R <= 2`, `L+C <= 3` golden slice in `docs/counts/small-r2-x3.md` and `docs/results.md`. Descriptor conversion, full standard-slice reporting, and Ladenheim comparison documentation remain pending.

## Near-term next steps

1. Add descriptor conversion methodology after implementation and tests exist.
2. Extend reduced-signature count-method documentation when the full standard slice is run.
3. Keep legacy, support-census, raw bundle-assignment, assigned-support orbit, and reduced-topology result tables clearly separated.

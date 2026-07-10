# 05-slices / 02 — Historical 148 scope and old RICE diagnostic slice

Status: `todo`

## Goal

Track the corrected historical Ladenheim scope separately from the old
repository RICE diagnostic slice.

## Historical 148 scope

```text
total elements <= 5
L + C <= 2
```

This scope does not impose `R <= 3`. Reproducing 148 also requires the
Ladenheim structural relation: graph 2-isomorphism-level identification of
deformation, separation, and series interchange, plus exclusion of trivially
simplifiable same-kind series or parallel connections.

## Old RICE diagnostic slice

```text
R <= 3
L + C <= 2
support edges <= 5
```

The current RICE reduced-signature implementation reports 140 signatures for
this diagnostic at commit `338ddec` using:

```bash
.venv/bin/python -m rice reduced --max-r 3 --max-reactive 2 --max-edges 5 --format json
```

This is not the historical 148 benchmark.

## Current capability gap

The CLI/API cannot express `total elements <= 5, L+C <= 2` exactly without an
independent resistor bound. `--max-r 5 --max-reactive 2 --max-edges 5` is not an
exact substitute because the current model can still admit reduced signatures
with `R+L+C > 5`.

## Done means

- The historical scope is implemented by the future Ladenheim structural
  enumerator, not by overloading the current RICE reduced mode.
- The old 140 RICE diagnostic remains documented as a separate current-model
  result.
- Counts, catalogue members, 2-isomorphism classes, RICE reduced signatures,
  and realizability-set equivalence classes are not conflated.

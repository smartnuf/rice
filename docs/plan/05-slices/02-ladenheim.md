# 05-slices / 02 — Ladenheim slices

Status: `todo`

## Revision note (2026-07-10)

This task previously stated a single set of "exact Ladenheim bounds":
`R <= 3 / L + C <= 2 / R + L + C <= 5`. That is not the defining scope of the
historical 148-network set; the `R <= 3` bound belongs to the later
108-network canonical set. See `docs/ladenheim_benchmark.md` for the full
reassessment and `docs/plan/03-counting/05-ladenheim.md` for the corrected
slice definitions.

## Goal

Use two distinct slices, per `docs/plan/03-counting/05-ladenheim.md`:

```text
148-scope slice:        L + C <= 2, R + L + C <= 5 (no independent R bound)
Bounded R <= 3 slice:   R <= 3, L + C <= 2, R + L + C <= 5
```

The 148-scope slice is the actual initial scope of the historical
148-network set. The bounded `R <= 3` slice is a separately useful,
well-defined region (matching the 108-network canonical set's resistor
range) but is not itself a reproduction of 148.

## Done means

- The task has a documented method and validation path for both slices.
- Counts, enumeration results, catalogues, equivalence classes, generator
  sets, and full immittance identity are not conflated.
- Neither slice's count is presented as a validated reproduction of 148,
  108, or 62; that reproduction is tracked under `docs/plan/04-ladenheim/`.

# 03-counting / 04 — Implement small explicit subset: `R <= 2`, `L+C <= 3`

Status: `todo`

## Goal

Create a deliberately smaller subset for early implementation, test speed, and regression coverage.

## Scope

```text
R <= 2
L + C <= 3
```

This subset should be treated as an explicit test point inside the larger `R <= 3`, `L+C <= 5` plan.

## Why this subset matters

- It should be small enough for fast local and CI tests.
- It exercises mixed R/L/C assignment without reaching the full search size.
- It provides early confidence in graph generation, colouring, canonicalisation, descriptor conversion, and count reporting.

## Done means

- The subset can be generated independently.
- It has stable count outputs.
- Its counts are used as golden regression tests.
- The subset is documented as a test slice, not the final catalogue target.

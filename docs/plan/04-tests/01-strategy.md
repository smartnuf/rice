# 04-tests / 01 — Test strategy for enumeration

Status: `todo`

## Goal

Build confidence while the enumeration machinery evolves.

## Test layers

1. Unit tests for graph validity checks.
2. Unit tests for edge colouring and R/L/C composition constraints.
3. Canonicalisation tests using hand-known isomorphic examples.
4. Descriptor conversion tests.
5. Golden-count tests for small scopes.
6. Regression tests for known catalogue slices.
7. Slow/full tests for the complete `R <= 3`, `L+C <= 5` scope.

## Done means

- Fast tests run by default.
- Slow enumeration tests are available but clearly marked.
- CI and local commands agree.

# 03-counting / 05 — Implement the Ladenheim comparison slice

Status: `todo`

## Goal

Create a comparison slice for the Ladenheim catalogue of distinct RLC networks
with no more than two reactances and three resistances. These networks are
relevant because they are realised by biquadratic functions.

## Correct comparison target

The comparison slice is the intersection of all three bounds:

```text
R <= 3
L + C <= 2
R + L + C <= 5
```

The explicit resistor bound matters: the other two bounds alone would admit
cases such as `R=4`, `L+C=1`, which are outside the catalogue's limit of three
resistances.

This includes the important `3+2` case:

```text
R = 3
L + C = 2
total = 5
```

This `3+2` point is inside the full `R <= 3`, `L+C <= 5` scope, but it is not inside the small `R <= 2`, `L+C <= 3` subset.

## Name and spelling

Use `Ladenheim catalogue` in repository docs unless a specific source being quoted uses another spelling.

## Tasks

- Encode the three Ladenheim-style bounds as a named count mode.
- Generate counts for the slice.
- Compare against known published counts only after our distinctness/reduction definition is aligned.
- Record differences if our definition deliberately differs.

## Done means

- The named slice enforces `R <= 3`, `L+C <= 2`, and total elements `<= 5`.
- `3+2` is explicitly generated and tested.
- The comparison slice is separate from the small smoke-test subset.
- Documentation states exactly why any count agrees or disagrees with the historical catalogue.

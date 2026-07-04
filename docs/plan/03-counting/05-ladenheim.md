# 03-counting / 05 — Implement Ladenheim comparison slice, including `3+2`

Status: `todo`

## Goal

Create a catalogue comparison slice that includes the historical `3+2` boundary case.

## Correct comparison target

The comparison slice should include networks with:

```text
total elements <= 5
reactive elements L+C <= 2
```

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

- Encode the Ladenheim-style slice as a named count mode.
- Generate counts for the slice.
- Compare against known published counts only after our distinctness/reduction definition is aligned.
- Record differences if our definition deliberately differs.

## Done means

- `3+2` is explicitly generated and tested.
- The comparison slice is separate from the small smoke-test subset.
- Documentation states exactly why any count agrees or disagrees with the historical catalogue.

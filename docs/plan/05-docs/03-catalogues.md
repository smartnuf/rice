# 05-docs / 03 — Document catalogue comparisons and references

Status: `todo`

## Goal

Keep historical comparisons precise and sourced.

## Notes

The relevant historical name appears to be the `Ladenheim catalogue`. It is commonly described as a catalogue of essentially distinct RLC two-terminal networks with at most five total elements, of which at most two are reactive.

Some sources report 108 networks in the catalogue. Pynntt should compare against this number only after matching the same distinctness and reduction assumptions.

## Planned comparison slices

- Ladenheim-style slice: `total elements <= 5`, `L+C <= 2`.
- Explicit boundary point: `R=3`, `L+C=2`, total `5`.
- Pynntt smoke-test slice: `R <= 2`, `L+C <= 3`.
- Pynntt full planned scope: `R <= 3`, `L+C <= 5`.

## Done means

- The repository cites the sources used.
- Agreement or disagreement with historical counts is explained.
- The spelling and scope of the catalogue are consistent throughout the docs.

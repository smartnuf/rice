# 08-docs / 03 — Document catalogue comparisons and references

Status: `todo`

## Goal

Keep historical comparisons precise and sourced.

## Revision note (2026-07-10)

This task previously described the Ladenheim catalogue as "a catalogue of
distinct RLC networks with no more than two reactances and three
resistances, subject also to a five-element total limit," and listed a
single "Ladenheim-style slice" of `R <= 3, L+C <= 2, R+L+C <= 5`. That
conflated two different historical sets. See `docs/ladenheim_benchmark.md`
for the full reassessment.

## Notes

There are three historical figures, not one, and they must stay distinct:

- **148 essentially distinct networks**: the initial set, scoped by
  `L + C <= 2` and `R + L + C <= 5`, with no independent resistor bound,
  after identifying networks related by 2-isomorphism and excluding networks
  trivially simplifiable by same-type series/parallel connections.
- **108-network canonical set** (the "Ladenheim catalogue" in Morelli &
  Smith's usual terminology): obtained from the 148 by removing 40 further
  networks via electrical-network transformations and realizability
  arguments; this is where the `R <= 3` bound applies.
- **62 realizability-set equivalence classes**: a classification of the 108
  canonical set by equality of realizability set, distinct from two other
  groupings of the same 108 networks (35 group-action orbits, 24
  subfamilies) that must not be conflated with the 62 classes.

These networks are relevant to this project because they are realised by
biquadratic immittances.

Source: A. Morelli and M. C. Smith, *Passive Network Synthesis: An Approach
to Classification*, SIAM, 2019 (Ch. 3 §3.1 p. 19; Ch. 5 pp. 41-43 §5.1;
Ch. 6; Thm. 7.4).

rice should compare against 148, 108, or 62 only after an independent
Ladenheim structural reproduction exists (`docs/plan/04-ladenheim/`,
Stages A-D), and only after Stage E has assessed how RICE's own
reduced-topology signature relates to Ladenheim's 2-isomorphism — a
rectangular RICE count matching or not matching one of these numbers is not
by itself informative.

## Planned comparison slices

- 148-scope slice: `L + C <= 2`, `R + L + C <= 5`, no independent `R` bound.
- Bounded `R <= 3` slice: `R <= 3`, `L + C <= 2`, `R + L + C <= 5` (matches
  the 108-network canonical set's resistor range; useful in its own right,
  but not itself a reproduction of 148).
- Explicit boundary point: `R = 3`, `L + C = 2`, total `5`.
- rice smoke-test slice: `R <= 2`, `L + C <= 3`.
- rice full planned scope: `R <= 3`, `L + C <= 5`.

## Done means

- The repository cites the sources used, with chapter/section/page
  references.
- 148, 108, and 62 are each defined precisely and kept distinct from each
  other and from the 35 orbits / 24 subfamilies groupings.
- Agreement or disagreement with historical counts is explained only after
  the independent Stage A-D reproduction exists.
- The spelling and scope of each figure is consistent throughout the docs.

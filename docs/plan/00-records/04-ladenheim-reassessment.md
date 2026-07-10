# 00-records / 04 — Ladenheim benchmark interpretation and revised validation plan

Status: `prog`

## Decision date

2026-07-10

## Source basis

This reassessment records the repository planning consequence of the source
findings from A. Morelli and M. C. Smith, *Passive Network Synthesis: An
Approach to Classification*, SIAM, 2019, especially Chapter 3, Section 3.1
(p. 19), Chapter 5 (pp. 41–43 and Section 5.1), the Chapter 6 classification
summary, and Theorem 7.4. The source is cited here bibliographically and
paraphrased; the repository does not copy the book or long copyrighted passages.

## Original working assumption now rejected

Earlier plan records treated the historical counts approximately as a sequence
of increasingly strong topology canonicalizers:

```text
broad candidates -> 148 -> 108 -> 62
```

They also treated the comparison slice

```text
R <= 3
L + C <= 2
R + L + C <= 5
```

as if it were the full initial scope needed to reproduce the historical 148.
That was too coarse and has been rejected.

## Corrected interpretation

The **148 essentially distinct networks** are already structural classes. They
are obtained by listing connected two-terminal basic graphs with at most five
branches, populating those branches with primitive `R`, `L`, or `C` elements
with at most two reactive elements, identifying deformation, separation, and
series interchange by graph 2-isomorphism, and excluding trivially simplifiable
same-kind series or parallel connections. Ordinary graph isomorphism alone is
therefore not the historical 148 relation.

The initial 148 scope is:

```text
total elements <= 5
L + C <= 2
```

It is not initially restricted to `R <= 3`. The 148 include eight networks with
four resistors and one reactive element. Those eight are later removed while
constructing the 108-network canonical set.

The **108-network canonical set**, usually referred to in this project as the
**Ladenheim catalogue**, is obtained from the 148 by forty additional removals:
eight four-resistor/one-reactive networks with bilinear impedances realizable by
simpler networks; four four-element Zobel reductions; twenty five-element
series-parallel Zobel reductions; and eight further O/O-dual, bridge,
Cauer-Foster, regularity, and Y-Delta-related cases. These operations are not
just another application of the same structural signature that produced 148.

The **62 realizability-set equivalence classes** classify the 108 catalogue
networks by equality of realizability sets as positive component values vary.
They are not merely the output of a stronger graph canonicalizer. The 108
catalogue members still exist as catalogue members. The 35 group-action orbits
and 24 subfamilies discussed by Morelli and Smith must also remain separate
from the 62 realizability-set equivalence classes.

## Current RICE reduction is a different implemented contract

The current implementation remains useful, but it is not the Ladenheim
2-isomorphism contract. It implements:

- connected unlabelled simple support graphs;
- unordered terminal pairs and terminal reversal;
- whole-graph rejection of terminal-irrelevant support edges;
- assignment of simple `R`/`L`/`C` primitive bundles to support edges;
- local parallel-factor merging;
- suppression of non-terminal degree-two vertices into series factors;
- flattening and commutative normalization of series and parallel expressions;
- merging repeated primitive singleton `R`, `L`, or `C` factors;
- ordinary graph isomorphism and internal-node relabelling.

It does not implement general graph 2-isomorphism, deformation, separation, and
series interchange as the historical 148 relation. It also collapses some local
same-kind simplifications into smaller reduced factors, whereas the historical
148 construction excludes trivially simplifiable candidates. These are related
ideas, not automatically the same counting procedure.

## Verified native RICE diagnostic

The previously provisional current-reduction count for the old planned slice is
now reproduced with the checked-out repository at commit `338ddec`:

```bash
.venv/bin/python -m rice reduced --max-r 3 --max-reactive 2 --max-edges 5 --format json
```

Interpretation: this is the **RICE reduced signature** count with `R <= 3`,
`L+C <= 2`, and support-edge count `<= 5`. Because `R <= 3` and `L+C <= 2`
imply `R+L+C <= 5` for generated and reduced signatures, the total-component
bound is enforced by these particular component budgets rather than by a
separate coupled `--max-components` option.

The verified exact table, where `X = L+C`, is:

| R \ X | 0 | 1 | 2 | Row total |
|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 2 | 4 |
| 1 | 1 | 4 | 12 | 17 |
| 2 | 0 | 4 | 34 | 38 |
| 3 | 0 | 4 | 77 | 81 |
| **Total** | **1** | **14** | **125** | **140** |

Diagnostics for the same command: 906 raw phase-2 assignments, 562 phase-3
assigned-support labeling orbits, and 140 final canonical reduced signatures.
This 140 is not a Ladenheim target and must not be presented as reproducing 148.

The corrected initial 148 scope, `total elements <= 5` and `L+C <= 2` without an
`R <= 3` bound, is not currently expressible exactly by the CLI/API. The closest
component budget would be `--max-r 5 --max-reactive 2 --max-edges 5`, but that
allows signatures with `R+L+C > 5` because the implementation has independent
`R` and `L+C` budgets plus an optional support-edge bound, not a coupled total
primitive-component bound. This is an identified capability gap for the future
Ladenheim structural enumeration.

## Revised validation sequence

### Stage A — Define the historical 148 contract

Before implementation, write a precise contract for primitive `R`/`L`/`C`
element edges, connected two-terminal networks, at most five total elements, at
most two reactive elements, terminal orientation, graph 2-isomorphism and its
relation to deformation/separation/series interchange, exclusion of same-kind
series and parallel simplifications, and the role of a distinguished port/source
edge if the chosen formulation needs one. Unsettled details must be listed as
open questions.

### Stage B — Reproduce 148

Implement and test a dedicated Ladenheim structural enumeration/signature whose
acceptance target is exactly 148. Keep it separate from the current RICE reduced
signature unless a later proof shows the contracts coincide. Require diagnostic
tables by element count and component composition.

### Stage C — Reproduce 108

Implement the forty removals as a separately documented stage with fixtures or
tests for the eight four-resistor/one-reactive nongeneric cases, four
four-element Zobel cases, twenty five-element Zobel cases, and eight
Cauer-Foster/regularity-related cases. The acceptance target is 108.

### Stage D — Reproduce the catalogue classification

Treat the 62 as realizability-set equivalence classes of the 108 catalogue
members. This likely requires algebraic network analysis and is not validated by
graph canonicalization alone. Keep 108 catalogue members, 35 group-action
orbits, 24 subfamilies, and 62 realizability-set equivalence classes separate.

### Stage E — Reconcile with native RICE reduction

Only after independently reproducing the historical stages should the project
compare them with the current RICE reduced signature. The comparison should ask
which Ladenheim networks coalesce under the RICE reduction, which RICE
signatures contain multiple 2-isomorphism classes, whether the current reduction
is stronger or weaker in different cases, and whether it remains a separate
user-facing enumeration mode.

## Consequences

- Do not mark reproduction of 148 as done.
- Do not use the 140 RICE diagnostic as a historical acceptance target.
- Do not describe 148 as raw candidates before canonical structural reduction.
- Do not describe 62 as merely another topology count.
- The implementation order changes from extending the current reduced signature
toward 148 to first specifying and implementing a separate Ladenheim structural
contract.

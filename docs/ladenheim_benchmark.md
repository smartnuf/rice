# Ladenheim benchmark interpretation and revised validation plan

Dated: 2026-07-10.

This is a decision/reassessment record. It documents a working assumption the
plan previously relied on, the evidence that invalidated it, the corrected
meanings of the historical counts, and the consequences for how this project
validates itself against the historical Ladenheim catalogue. It intentionally
preserves the old (incorrect) interpretation rather than silently rewriting
it, so a later contributor can see what changed and why.

## Source

A. Morelli and M. C. Smith, *Passive Network Synthesis: An Approach to
Classification*, SIAM, 2019. Specifically:

- Chapter 3, Section 3.1, p. 19 — the construction of the candidate network
  set from connected two-terminal basic graphs.
- Chapter 5, pp. 41-43, Section 5.1 — the reduction from the candidate set to
  the canonical catalogue by electrical-network transformations.
- Chapter 6 — the classification summary distinguishing the catalogue from
  further groupings (orbits, subfamilies, equivalence classes).
- Theorem 7.4.

This document paraphrases the source. It does not reproduce, copy, or closely
imitate copyrighted text or figures from it.

## The original working assumption (now known to be wrong)

Earlier planning documents (`docs/plan/03-counting/05-ladenheim.md`,
`docs/plan/05-slices/02-ladenheim.md`,
`docs/plan/00-records/02-literature-conclusions.md`,
`docs/plan/08-docs/03-catalogues.md`, and README.md's motivation section, prior
to this reassessment) treated the historical "148" as if it were the
*unabridged*, pre-reduction candidate set, and treated the comparison slice

```text
R <= 3
L + C <= 2
R + L + C <= 5
```

as *the* defining scope of that 148-network set. Both parts of that assumption
were wrong, in two different ways:

1. **148 is not raw/unabridged.** The 148-network set is already the result of
   identifying networks related by 2-isomorphism (deformation, separation, and
   series interchange) and excluding networks that are trivially simplifiable
   by same-type series/parallel connections. It is a set of *essentially
   distinct* networks, not the full space of labelled candidate graphs before
   any reduction.
2. **148 is not bounded by `R <= 3`.** The 148-network set's defining scope is
   networks with at most five elements in total and at most two reactive
   elements (`L + C <= 2`), with **no separate bound on the resistor count**.
   The set includes eight networks with four resistors and one reactive
   element (`R = 4`, `L + C = 1`), which the `R <= 3` bound would wrongly
   exclude. The `R <= 3` bound applies to the later 108-network catalogue, not
   to the initial 148-network set.

The old planning documents also implied that ordinary graph isomorphism (plus
terminal reversal and simple local series/parallel merging, as already
implemented by this repository) would suffice to reproduce 148. This is also
not correct: 2-isomorphism is a broader relation than graph isomorphism (see
"RICE reduction versus Ladenheim 2-isomorphism" below), and the exclusion of
trivially-simplifiable networks in the historical construction is a modelling
choice, not merely a consequence of a canonical signature.

## What invalidated it

Re-reading Morelli & Smith's construction (cited above) directly contradicts
both parts of the assumption: the text describes the 148-network set as
already essentially distinct under 2-isomorphism, built from basic graphs with
at most five branches populated by R/L/C subject only to `L + C <= 2`, with no
mention of a resistor-count bound at that stage. The `R <= 3` bound, and the
elimination of 40 further networks, are described as the *next* stage, which
produces the 108-network canonical set (the "Ladenheim catalogue" in Morelli &
Smith's usual terminology).

## Corrected meanings

- **148 essentially distinct networks**: connected two-terminal networks built
  on basic graphs with at most five branches, each branch a single primitive
  R, L, or C, with at most two reactive elements total (`L + C <= 2`) and no
  separate resistor bound, after identifying networks related by
  2-isomorphism (deformation, separation, series interchange) and excluding
  networks trivially simplifiable by same-type series/parallel connections.
- **108-network canonical set** (the Ladenheim catalogue): obtained from the
  148 essentially distinct networks by removing 40 further networks using
  electrical-network transformations and realizability arguments, not by
  applying a stronger topological canonicalization. The 40 removed break down
  as:
  - 8 networks with four resistors and one reactive element, realizable by a
    simpler (bilinear) network;
  - 4 four-element networks reducible to a three-element network by a Zobel
    transformation;
  - 20 five-element series-parallel networks reducible to a four-element (or
    smaller) network by a Zobel transformation;
  - 8 networks related by Cauer-Foster transformation, regularity, or
    Y-Delta relationships to an O-network, its dual, or a bridge network.
- **62 realizability-set equivalence classes**: a classification of the
  108-network canonical set into equivalence classes defined by equality of
  *realizability sets* — the set of positive-real driving-point immittances
  each network can realize as its component values vary — not by any further
  topological canonicalization. Morelli & Smith also describe two other
  groupings of the same 108-network set that must not be confused with the 62
  classes: 35 group-action orbits, and 24 subfamilies. All three groupings (62
  classes, 35 orbits, 24 subfamilies) partition or group the same 108-network
  set by different criteria and are not interchangeable numbers for "the
  equivalence classes."

## RICE reduction versus Ladenheim 2-isomorphism

The current implementation (`docs/model_decisions.md`) defines its own
reduced-topology model: connected unlabelled simple support graphs; two
unordered terminals; rejection of terminal-irrelevant edges; simple R/L/C
bundle assignment; local parallel-factor merging; suppression of non-terminal
degree-2 vertices into series factors; flattening and commutative
normalisation of series/parallel composition; merging of repeated primitive
singleton R/L/C factors within a series span; and quotienting by ordinary
graph isomorphism, internal-node relabelling, and terminal reversal.

This is a real and useful reduction — it defines a coherent, project-specific
reduced-network model, and its results (`docs/python_api.md`,
`docs/model_decisions.md`) are correct under that model's own stated contract.
It should not be described as wasted or incorrect work.

It is not, however, the same relation as Ladenheim's 2-isomorphism. In
particular:

- 2-isomorphism includes graph *deformation* and *separation* operations that
  can relate networks whose underlying graphs are not isomorphic in the
  ordinary sense (for example, some bridge/non-series-parallel structures).
  RICE's quotient is by ordinary graph isomorphism plus local series/parallel
  reduction; it does not implement general 2-isomorphism.
- The historical construction *excludes* networks that are trivially
  simplifiable by same-type series/parallel connections as a modelling choice
  made at candidate-generation time. RICE's reduction *merges* repeated
  primitive singleton factors within a series span (and merges same-type
  parallel primitives into a single bundle slot) as part of its own
  reduced-signature construction. These are different mechanisms that often,
  but do not provably always, produce the same practical effect on which
  networks collapse together.

Because of this, RICE's reduced-topology signature and Ladenheim's
essentially-distinct network are related but not proven identical relations.
Section "Consequences for implementation order" below explains why this
project should reproduce the Ladenheim construction independently before
assuming the two coincide.

## Verified counts under the old (incorrect) comparison slice

The old, `R <= 3 / L + C <= 2 / R + L + C <= 5` comparison slice is still a
well-defined region of the RICE reduced-topology model, even though it is not
the correct 148 scope. Running it against the current implementation is fully
reproducible:

```console
$ git rev-parse HEAD
338ddec5f0c577bb3b08204957fd7733f70dd0b0
$ .venv/bin/python -m rice reduced --max-r 3 --max-reactive 2 --format json
```

```json
{
  "definition": "canonical-reduced-topology-local-series-parallel-v1",
  "diagnostics": {
    "canonical_reduced_signatures_total": 140,
    "phase3_assigned_support_labeling_orbits_total": 562,
    "raw_phase2_assignments_total": 906
  },
  "equivalence": "internal node renaming, terminal reversal, local commutative series/parallel normalisation, and duplicate primitive singleton merging; not rational immittance equivalence",
  "exact_counts_by_r_x": [[0,2,2],[1,4,12],[0,4,34],[0,4,77]],
  "format_version": 1,
  "regeneration_command": ".venv/bin/python -m rice reduced --max-r 3 --max-reactive 2 --format json",
  "scope": {"max_edges": 5, "max_r": 3, "max_reactive": 2},
  "total": 140
}
```

By resistor count: `R=0` gives 4, `R=1` gives 17, `R=2` gives 38, `R=3` gives
81, for a grand total of 140. This is now a **verified** reproduction (not
merely provisional) of the previously-reported 140-count under the old,
incorrect comparison slice. It is **not** a reproduction of 148, 108, or 62,
which is exactly the point of this reassessment: the old slice's rectangular
bounds do not correspond to the historical construction's actual scope, so
matching or not matching 140 to any historical number would not have been
meaningful.

## Diagnostic finding under the corrected 148 scope

The corrected 148 scope is `total elements <= 5, L + C <= 2`, with no
independent bound on `R`. The current CLI cannot express this directly: `rice
reduced --max-r` and `--max-reactive` only express independent rectangular
bounds. `--max-r 5 --max-reactive 2` returns an unfiltered rectangle that
includes rows violating the joint total, e.g. `R=5, L+C=2` (total 7):

```console
$ .venv/bin/python -m rice reduced --max-r 5 --max-reactive 2 --format json
```

returns `"total": 1066`, which is the full `R <= 5, L + C <= 2` rectangle, not
the triangular `total <= 5` region.

The corrected scope *can* be computed today by composing already-exported API
functions (`iter_reduced_topology_signatures`,
`reduced_signature_component_counts`) with a post-hoc filter, without adding
any new production enumeration code:

```python
from rice import iter_reduced_topology_signatures, reduced_signature_component_counts
from collections import defaultdict

counts = defaultdict(lambda: defaultdict(int))
grand_total = 0
seen_signatures = set()
for signature in iter_reduced_topology_signatures(max_r=5, max_reactive=2):
    key = signature.stable_string()
    assert key not in seen_signatures, f"duplicate signature {key}"
    seen_signatures.add(key)
    r, l, c = reduced_signature_component_counts(signature)
    x = l + c
    assert r <= 5 and x <= 2, (r, x)
    if r + x <= 5:
        counts[r][x] += 1
        grand_total += 1
```

Run at the same commit (`338ddec5f0c577bb3b08204957fd7733f70dd0b0`), this
diagnostic gives:

```text
R=0: X=1:2, X=2:2   row total 4
R=1: X=0:1, X=1:4, X=2:12   row total 17
R=2: X=1:4, X=2:34   row total 38
R=3: X=1:4, X=2:77   row total 81
R=4: X=1:8   row total 8
R=5: X=0:1   row total 1
Grand total: 149
```

The `R <= 3, L + C <= 2` portion of this same data is 140, consistent with the
independently-verified result above.

**This diagnostic gives 149 RICE reduced signatures under the corrected 148
scope — one more than the historical 148.** Two details are worth recording:

- The `R=4, L+C=1` row gives exactly 8, consistent in count with the
  historical fact that the 148-network set includes eight networks with four
  resistors and one reactive element. This is a count-level consistency, not
  a proof that RICE's eight signatures are the same eight networks as
  Ladenheim's; establishing that requires the independent reproduction in
  Stage B below.
- The `R=5, L+C=0` row gives exactly 1. This is plausibly a genuinely
  non-series-parallel (bridge-like) five-resistor structure that RICE's
  local-only series/parallel reduction does not merge with anything else,
  since RICE does not implement general 2-isomorphism (see previous section).

This 149-vs-148 discrepancy is an expected and interesting finding given the
known gap between RICE's reduction and 2-isomorphism, not a bug in the current
implementation, and it must not be closed by tuning code to force a count of
140 or 148. Production enumeration behaviour is unchanged by this task.

## Why the plan is changing

The plan previously treated "reproduce 148/108/62" as a single comparison
slice to be validated by rectangular `--max-r`/`--max-reactive` counts against
the current reduced-topology model. That is not a valid comparison, because:

- the RICE reduced-topology signature and the Ladenheim essentially-distinct
  network are different (if related) relations, so numeric agreement or
  disagreement between a rectangular RICE count and a historical number is not
  by itself informative in either direction;
- 108 and 62 are not produced by any topological canonicalization at all —
  108 requires electrical-network transformation and realizability arguments,
  and 62 requires realizability-set comparison — neither of which the current
  implementation attempts.

## Consequences for implementation order

The former single "Ladenheim comparison slice" plan item is replaced by a
five-stage validation sequence, detailed in `docs/plan/04-ladenheim/`:

- **Stage A** (`01-148.md`): define the historical 148 contract precisely,
  without implementing it, and list unsettled details as open questions.
- **Stage B** (`01-148.md`): reproduce 148 via a dedicated, separate Ladenheim
  structural signature, distinct from the RICE reduced-factor signature
  unless later proven equivalent.
- **Stage C** (`02-108.md`): reproduce 108 via the 40 exclusions as a
  separately documented stage with fixtures per exclusion category, not
  hidden inside the 148 signature.
- **Stage D** (`03-62.md`): reproduce the 62-class realizability-set
  classification, keeping it explicitly distinct from the 35 orbits and 24
  subfamilies.
- **Stage E** (`05-numbering.md`): reconcile RICE's native reduction with the
  independently-reproduced Ladenheim stages only after B-D are complete,
  without pre-deciding that either model replaces the other.

None of stages A-E are implemented by this task. This task is documentation
and planning only; no production enumeration code changed.

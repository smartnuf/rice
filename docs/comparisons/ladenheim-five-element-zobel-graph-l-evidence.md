# Evidence for the graph-L five-element Zobel exclusions

## 1. Purpose and scope

This report investigates only the four five-element series-parallel networks
with Morelli and Smith basic graph `L` that Section 5.1 collectively says are
removed by Zobel transformation to canonical networks #20, #25, #28, and #32.
It transcribes the source diagrams, reproduces the complete RICE graph-`L`
candidate census under
`colour-preserving-port-augmented-cycle-matroid-v1`, and checks each proposed
candidate-to-target correspondence structurally and algebraically.

This report was originally prepared as evidence for later ledger review and did
not itself change production, assign a historical number to an excluded record,
or claim to reproduce the canonical 108-network catalogue. PR 63 applies the
four reviewed graph-`L` mappings through the version 3 subject-bound evidence
route. On that branch, the production ledger has 16 excluded, 132 unresolved,
and 0 retained records.

The publication states the four-member graph-family/target relationship only in
aggregate. It does not print RICE catalogue IDs or pair individual graph-`L`
assignments with target numbers. Consequently, `source-stated` below describes
only the aggregate publication claim; every individual mapping is instead
labelled according to its independently reproducible evidence.

## 2. Authoritative source statements

Morelli and Smith, Section 5.1, states that twenty five-element
series-parallel networks are reducible by Zobel transformation and, within that
group, that four having graph structure `L` reduce to networks #20, #25, #28,
and #32. This establishes the graph family, the count four, the transformation
class, and the target set collectively. It does not establish which RICE ID
maps to which target.

Appendix B gives the following facts in its graph-`L` row:

- there are four five-element assignments in total;
- zero are retained in the canonical total;
- two exclusions lie in the combined `3R-2L / 3R-2C` column; and
- two exclusions lie in the `3R-LC` column.

The parenthesized entries are exclusions, consistent with the table's zero
canonical total. The combined column does **not** separately source-state one
`3R-2L` and one `3R-2C` assignment. That split, and the distinction between the
two `3R-LC` assignments, comes from the independently reproduced RICE census
and colored topology checks in Sections 8-10.

Section 5.3.1 states the Zobel identity shown in Figure 5.2. For positive finite
coefficients, its right-hand network

```text
b' Z1 || (a' Z1 -- c' Z2)
```

is equivalent to its left-hand network

```text
a Z1 -- (b Z1 || c Z2)
```

when

```text
a = a'b'/(a'+b')
b = (b')^2/(a'+b')
c = c' (b'/(a'+b'))^2.
```

The source also explicitly notes that positive finite coefficients map to
positive finite coefficients in either direction.

## 3. Source locators

The authoritative source is A. Morelli and M. C. Smith, *Passive Network
Synthesis: An Approach to Classification* (2019). The inspected local copy was

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Precise locator | Inspection |
|---|---|---|
| Aggregate graph-`L` exclusion and target set | Section 5.1, printed p. 42, zero-based PDF index 48 | Extracted text and rendered page |
| Zobel topology, coefficient maps, and positivity statement | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Four-element target equivalence-class context | Figure 6.2, printed p. 50, PDF index 56 | Extracted text and rendered page |
| Graph `L`, its counts, and target basic graph `F` | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Diagrams for #20, #25, #28, and #32 | Appendix C, printed p. 130, PDF index 136 | Extracted text and rendered page |

The rendered pages were used for every graph and circuit transcription; no
topology was inferred from extracted text alone. No PDF, rendering, extracted
text, or OCR output is committed.

One previous-workspace lead was consulted. Repository `../network-theory` at
commit `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`, file
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/analysis-of-basic-graphs.md`,
suggested the edge list `AB;BC;CD;DE;EC`. That lead was independently confirmed
against the rendered Appendix B diagram and then against the complete RICE
census. Searches of clean `../pynntt` at
`f3db06032cbe23d583d77f6cb79d21ced90d7651` and clean `../pynntt_lab` at
`1ddd90034da4594bb6a3728b0700918883fd1172` supplied no candidate mapping used
as evidence. The PDF happens to reside in `pynntt_lab`; the publication itself,
not that workspace's analysis, is the authoritative source.

## 4. Transcription of graph L

The independently transcribed normalized two-terminal multigraph is:

```text
vertices:  A, B, C, D, E
terminals: {A, E}
edges:     AB, BC, CD, DE, CE
parallel edges: none
```

Equivalently, it is the four-edge terminal path
`A--B--C--D--E` plus chord `C--E`. As a series-parallel expression it is

```text
AB -- BC -- (CE || (CD -- DE)).
```

The source is the graph-`L` drawing in Appendix B, printed p. 126 / PDF index
132. The black vertices are terminals `A` and `E`; the three white vertices are
`B`, `C`, and `D`. The drawing contains five undirected edges and no parallel
edge. The normalized names are introduced here solely to make the transcription
reconstructible.

## 5. Transcription of targets #20, #25, #28, and #32

All four target diagrams have basic graph `F`: Appendix B's row `F` lists
exactly #20, #25, #28, and #32. A normalized graph-`F` fixture has vertices
`A,B,C,D`, terminals `{A,D}`, edges `AB`, `BC`, and two parallel copies of
`CD`. Appendix C supplies the following colors and labels:

| Target | Primitive edges in normalized order | Series/parallel topology | Composition |
|---:|---|---|---|
| #20 | `AB:R2`, `BC:C2`, `CD:R1`, `CD:C1` | `R2 -- C2 -- (R1 || C1)` | `2R-2C` |
| #25 | `AB:R2`, `BC:C1`, `CD:R1`, `CD:L1` | `R2 -- C1 -- (R1 || L1)` | `2R-LC` |
| #28 | `AB:R2`, `BC:L2`, `CD:R1`, `CD:L1` | `R2 -- L2 -- (R1 || L1)` | `2R-2L` |
| #32 | `AB:R2`, `BC:L1`, `CD:R1`, `CD:C1` | `R2 -- L1 -- (R1 || C1)` | `2R-LC` |

The circuit source for every row is Appendix C, printed p. 130 / PDF index 136.
The graph-`F` identification is Appendix B, printed p. 126 / PDF index 132.
Figure 6.2, printed p. 50 / PDF index 56, places these four targets in the
four-element Zobel-equivalence context; it is not used to infer the individual
five-element mappings.

## 6. Complete initial RICE candidate set

The committed structural catalogue contains 85 five-element records. Recoloring
each record's five real edges to one common color, while retaining the artificial
port edge and unordered terminal pair, gives exactly four matches to the
transcribed graph-`L` signature:

| RICE catalogue ID | Composition | Representative descriptor |
|---|---:|---|
| `lh148-f684b6a0ad3114c4` | `R3L0C2` | `0-2:C;0-3:R;1-4:C;2-3:R;3-4:R` |
| `lh148-2a3f20a9bcd73817` | `R3L1C1` | `0-2:C;0-3:R;1-4:L;2-3:R;3-4:R` |
| `lh148-a124f387d970b947` | `R3L1C1` | `0-2:C;1-3:L;1-4:R;2-4:R;3-4:R` |
| `lh148-5eb31698974d07f8` | `R3L2C0` | `0-2:L;0-3:R;1-4:L;2-3:R;3-4:R` |

This is the complete initial graph-`L` candidate set, not a subset selected by
composition. Its count four independently agrees with Appendix B's graph-`L`
total.

## 7. Structural matching method

The reproduction uses existing `rice.ladenheim` APIs only:
`PrimitiveNetwork`, `PrimitiveEdge`, `network_from_descriptor`, and
`canonical_structural_signature`.

For the broad census, every real edge is temporarily colored `R`. This removes
component assignment while preserving the artificial `P` port edge. Equality
is tested under the catalogue's exact relation,
`colour-preserving-port-augmented-cycle-matroid-v1`. This is a port-preserving
colored cycle-matroid comparison, so it includes the deformation, separation,
and series-interchange equivalences relevant to the structural catalogue; it is
not merely a drawing comparison.

For the final checks, the reproduction block constructs four independent
colored fixtures on the transcribed `L` edge set. In the expressions below,
the first reactive is on the leading two-edge series span and the second is in
the two-edge arm of the terminal parallel subnetwork:

```text
L(C,C): C -- R -- (R || (C -- R))
L(L,C): L -- R -- (R || (C -- R))
L(C,L): C -- R -- (R || (L -- R))
L(L,L): L -- R -- (R || (L -- R))
```

Each fixture is compared with its selected record using the unrecolored
canonical structural signature. Independently transcribed target fixtures are
checked the same way after the topology transformation. Component coefficients
do not enter this structural relation; their validity is checked separately in
Sections 10 and 11.

## 8. Candidate composition census

The reproduced census gives:

| Composition | Count | Structural distinction |
|---|---:|---|
| `3R-2C` | 1 | capacitor on each of the leading and parallel-arm series spans |
| `3R-LC` | 1 | leading inductor, capacitor in the parallel-arm series span |
| `3R-LC` | 1 | leading capacitor, inductor in the parallel-arm series span |
| `3R-2L` | 1 | inductor on each of the leading and parallel-arm series spans |

Thus Appendix B's combined-column count two resolves computationally to one
`3R-2L` and one `3R-2C` record. Its `3R-LC` count two resolves to two genuinely
different colored structural signatures. Neither conclusion is claimed as a
separate statement printed in Appendix B.

## 9. Candidate-to-target mappings

| RICE catalogue ID | Composition | Proposed target | Aggregate source support | Structural match | Zobel derivation | Overall status | Notes |
|---|---:|---:|---|---|---|---|---|
| `lh148-f684b6a0ad3114c4` | `3R-2C` | #20 | aggregate source-stated | exact colored signature | inverse Figure 5.2; exact | `independently-checked` | leading C; transformed arm C |
| `lh148-2a3f20a9bcd73817` | `3R-LC` | #32 | aggregate source-stated | exact colored signature | inverse Figure 5.2; exact | `independently-checked` | leading L; transformed arm C |
| `lh148-a124f387d970b947` | `3R-LC` | #25 | aggregate source-stated | exact colored signature | inverse Figure 5.2; exact | `independently-checked` | leading C; transformed arm L |
| `lh148-5eb31698974d07f8` | `3R-2L` | #28 | aggregate source-stated | exact colored signature | inverse Figure 5.2; exact | `independently-checked` | leading L; transformed arm L |

`source-stated` means only that Section 5.1 explicitly states the collective
graph-`L` count and target set. It does not automatically apply to any RICE-ID
correspondence. Here `independently-checked` means that both the colored
structural match and the Zobel derivation are reproducible. No mapping was
chosen from the order of the target list.

## 10. Zobel-reduction derivations

Let `Z1 = 1` denote the common resistor impedance basis, let `Z_Y` be the
reactive impedance in graph `L`'s two-edge parallel arm, and let `Z_X` be the
possibly different untouched leading reactive impedance. Every candidate has
the form

```text
d Z_X -- r Z1 -- [b' Z1 || (a' Z1 -- c' Z_Y)].
```

The bracketed subnetwork is the **right-hand side** of Figure 5.2. Apply the
published inverse coefficient map

```text
a = a'b'/(a'+b')
b = (b')^2/(a'+b')
c = c' (b'/(a'+b'))^2
```

to obtain

```text
d Z_X -- r Z1 -- a Z1 -- (b Z1 || c Z_Y).
```

The adjacent same-kind resistors merge trivially, producing

```text
d Z_X -- (r+a) Z1 -- (b Z1 || c Z_Y).
```

This is graph `F`. The untouched leading type `X` and transformed-arm type `Y`
select the target topology directly:

| Candidate fixture | Substitution in Figure 5.2 | Result after resistor merge | Target |
|---|---|---|---:|
| `L(C,C)` | `Z1=R`, `Z2=C` | `C -- R -- (R || C)` | #20 |
| `L(L,C)` | `Z1=R`, `Z2=C`; leading `L` untouched | `L -- R -- (R || C)` | #32 |
| `L(C,L)` | `Z1=R`, `Z2=L`; leading `C` untouched | `C -- R -- (R || L)` | #25 |
| `L(L,L)` | `Z1=R`, `Z2=L` | `L -- R -- (R || L)` | #28 |

Series interchange places the merged resistor before the leading reactive in
the Appendix C drawings, without changing the structural or impedance result.
For positive finite `a'`, `b'`, and `c'`, the denominator `a'+b'` is positive
and finite, so `a`, `b`, and `c` are positive and finite. Adding the positive
finite resistor coefficients `r+a` preserves those properties.

Each mapping uses one inverse Zobel step followed by one trivial same-kind
series resistor merge. None depends on frequency inversion, terminal reversal,
duality, a second Zobel step, or an unstated source assumption. Terminal
reversal and series interchange are permitted by the structural relation but
are not needed to choose the target.

## 11. Exact-arithmetic corroboration

With `Z1=1`, write parallel composition as `p(x,y)=xy/(x+y)`. For positive
rational `x=Z_Y`, the graph-`L` portion affected by the transformation has
impedance

```text
r + p(b', a' + c'x),
```

whereas the transformed and merged portion has

```text
(r+a) + p(b, cx).
```

The reproduction block uses a different generic positive integer tuple
`(r,a',b',c')` for each mapping, derives `a,b,c` as exact `Fraction` objects,
asserts every input and output coefficient positive, and verifies exact equality
at `x = 1, 2, 5, 11`. These multiple exact substitutions corroborate the
symbolic/topological derivation; they are not a floating-point proof and are not
the principal basis for the mapping.

## 12. Conclusions

The available evidence selects exactly four graph-`L` RICE records, with no
additional candidate under the committed relation. The census independently
reproduces Appendix B's total and composition-column counts. Exact colored
fixtures distinguish the two mixed-reactive placements, and one inverse Zobel
step plus a resistor merge assigns all four targets unambiguously:

```text
lh148-f684b6a0ad3114c4 -> #20
lh148-2a3f20a9bcd73817 -> #32
lh148-a124f387d970b947 -> #25
lh148-5eb31698974d07f8 -> #28
```

All four mappings are `independently-checked`, not individually
`source-stated`. This report originally supplied them for separate ledger
review; PR 63 now applies them through the version 3 subject-bound evidence
route. The target numbers remain reduction destinations rather than historical
identities of the excluded records.

## 13. Remaining uncertainties

No alternative graph-`L` candidate or target ambiguity remains under the
transcribed diagrams and the repository's named structural relation. The
publication still does not state the individual RICE-ID correspondences, so
those correspondences remain computational conclusions rather than direct
historical quotations.

This report does not investigate the other sixteen five-element Zobel
exclusions (`M`, `S`, `S`-dual, `M`-dual, or `L`-dual), the final eight
exclusions, or canonical-108 membership generally. Those are outside scope and
remain unresolved in the production ledger.

## 14. Reproduction commands

Run from the RICE repository root at commit
`d02e59a853d54cc8cacdb2ca4b4e6db46f81cc7c` or this report's descendant:

```bash
sha256sum \
  ../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf

.venv/bin/python - <<'PY'
import json
from collections import Counter
from fractions import Fraction

from rice.ladenheim import (
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    network_from_descriptor,
)


def make(edges):
    return PrimitiveNetwork(
        ("A", "E"),
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def uncoloured_signature(network):
    plain = PrimitiveNetwork(
        network.terminals,
        tuple(PrimitiveEdge(edge.u, edge.v, "R") for edge in network.edges),
    )
    return canonical_structural_signature(plain)


def parallel(left, right):
    return left * right / (left + right)


graph_l = make(
    [
        ("A", "B", "R"),
        ("B", "C", "R"),
        ("C", "D", "R"),
        ("D", "E", "R"),
        ("C", "E", "R"),
    ]
)

fixtures = {
    "lh148-f684b6a0ad3114c4": (
        "C",
        "C",
        20,
        make(
            [
                ("A", "B", "C"),
                ("B", "C", "R"),
                ("C", "D", "C"),
                ("D", "E", "R"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-2a3f20a9bcd73817": (
        "L",
        "C",
        32,
        make(
            [
                ("A", "B", "L"),
                ("B", "C", "R"),
                ("C", "D", "C"),
                ("D", "E", "R"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-a124f387d970b947": (
        "C",
        "L",
        25,
        make(
            [
                ("A", "B", "C"),
                ("B", "C", "R"),
                ("C", "D", "L"),
                ("D", "E", "R"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-5eb31698974d07f8": (
        "L",
        "L",
        28,
        make(
            [
                ("A", "B", "L"),
                ("B", "C", "R"),
                ("C", "D", "L"),
                ("D", "E", "R"),
                ("C", "E", "R"),
            ]
        ),
    ),
}

targets = {
    20: make(
        [
            ("A", "B", "R"),
            ("B", "C", "C"),
            ("C", "E", "R"),
            ("C", "E", "C"),
        ]
    ),
    25: make(
        [
            ("A", "B", "R"),
            ("B", "C", "C"),
            ("C", "E", "R"),
            ("C", "E", "L"),
        ]
    ),
    28: make(
        [
            ("A", "B", "R"),
            ("B", "C", "L"),
            ("C", "E", "R"),
            ("C", "E", "L"),
        ]
    ),
    32: make(
        [
            ("A", "B", "R"),
            ("B", "C", "L"),
            ("C", "E", "R"),
            ("C", "E", "C"),
        ]
    ),
}

with open("data/counts/ladenheim-148.json", encoding="utf-8") as stream:
    catalogue = json.load(stream)

five_element = [row for row in catalogue["records"] if row["rlc"] == 5]
assert len(five_element) == 85, len(five_element)

matches = []
for row in five_element:
    network = network_from_descriptor(row["representative_descriptor"])
    if uncoloured_signature(network) == uncoloured_signature(graph_l):
        matches.append(row)

assert len(matches) == 4, [row["catalogue_id"] for row in matches]
assert {row["catalogue_id"] for row in matches} == set(fixtures)

print("five-element records", len(five_element))
print("graph-L candidates", len(matches))
for row in matches:
    composition = f"R{row['r']}L{row['l']}C{row['c']}"
    print(
        row["catalogue_id"],
        composition,
        row["representative_descriptor"],
    )

assert Counter((row["r"], row["l"], row["c"]) for row in matches) == {
    (3, 0, 2): 1,
    (3, 1, 1): 2,
    (3, 2, 0): 1,
}

by_id = {row["catalogue_id"]: row for row in matches}
parameters = {
    "lh148-f684b6a0ad3114c4": (2, 3, 5, 7),
    "lh148-2a3f20a9bcd73817": (3, 4, 7, 5),
    "lh148-a124f387d970b947": (5, 2, 9, 4),
    "lh148-5eb31698974d07f8": (7, 6, 11, 3),
}

for catalogue_id, (leading, arm, target, fixture) in fixtures.items():
    row = by_id[catalogue_id]
    record = network_from_descriptor(row["representative_descriptor"])
    assert canonical_structural_signature(record) == (
        canonical_structural_signature(fixture)
    ), catalogue_id

    transformed = make(
        [
            ("A", "B", leading),
            ("B", "C", "R"),
            ("C", "E", "R"),
            ("C", "E", arm),
        ]
    )
    assert canonical_structural_signature(transformed) == (
        canonical_structural_signature(targets[target])
    ), (catalogue_id, target)

    r, a_prime, b_prime, c_prime = map(Fraction, parameters[catalogue_id])
    a = a_prime * b_prime / (a_prime + b_prime)
    b = b_prime**2 / (a_prime + b_prime)
    c = c_prime * (b_prime / (a_prime + b_prime)) ** 2
    coefficients = (r, a_prime, b_prime, c_prime, a, b, c, r + a)
    assert all(value > 0 and value.denominator > 0 for value in coefficients)

    for reactive_impedance in map(Fraction, (1, 2, 5, 11)):
        original = r + parallel(
            b_prime,
            a_prime + c_prime * reactive_impedance,
        )
        reduced = (r + a) + parallel(b, c * reactive_impedance)
        assert original == reduced, (
            catalogue_id,
            reactive_impedance,
            original,
            reduced,
        )

    print(
        f"{catalogue_id} -> #{target}: "
        "coloured structural and exact Zobel checks OK"
    )
PY
```

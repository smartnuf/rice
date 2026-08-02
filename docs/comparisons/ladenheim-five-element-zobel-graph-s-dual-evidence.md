# Evidence for the graph-S-dual five-element Zobel exclusions

## 1. Purpose and scope

This report investigates only the five five-element series-parallel networks
with Morelli and Smith basic graph `S^d` that Section 5.1 collectively says are
removed by Zobel transformation to canonical networks 37, 40, 45, 48, and 72.
It visually transcribes the source and target diagrams, reproduces the complete
graph-`S^d` RICE census under
`colour-preserving-port-augmented-cycle-matroid-v1`, and checks every proposed
candidate-to-target correspondence structurally and algebraically.

This is evidence-only work. It does not change production, assign a historical
number or basic graph to a RICE record, investigate the final eight exclusions,
or claim to reproduce the canonical 108-network catalogue. Production remains
27 excluded, 121 unresolved, and 0 retained records. All production graph
assignments remain null and all historical identifier lists remain empty.

The publication states the five-member graph-family/target relationship only
in aggregate. It does not print RICE catalogue IDs or pair individual
graph-`S^d` assignments with target numbers. Consequently, `aggregate
source-stated` below describes only the publication claim; each individual
mapping is an independently reproduced and checked conclusion.

## 2. Authoritative source statements

Section 5.1 states that five five-element networks with graph structure `S^d`
reduce by Zobel transformation to canonical networks 37, 40, 45, 48, and 72.
This establishes the graph family, count, transformation class, and collective
target set, but not the entry-specific allocation.

Appendix B reports 15 graph-`S^d` five-element assignments: two exclusions in
the combined `4R-L / 4R-C` column, two exclusions plus four canonical entries in
the combined `3R-2L / 3R-2C` column, and three exclusions plus four canonical
entries in the `3R-LC` column. Thus eight are canonical and seven are excluded
in total. Section 5.1 accounts for five of those exclusions as the Zobel group
studied here; the two four-resistor exclusions belong to the already applied
simpler-bilinear category.

Appendix B separately identifies graph `G^d` as the basic graph containing
canonical networks 37, 40, 45, and 48 and graph `H` as the one-member basic
graph containing canonical network 72. Appendix C supplies the entry-specific
circuit drawings transcribed below.

Section 5.3.1 states that Figure 5.2 applies for arbitrary impedances `Z1` and
`Z2`, gives both coefficient maps, and states that positive finite coefficients
map to positive finite coefficients in either direction.

## 3. Source locators and inspected copy

The inspected PDF was:

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Locator | Inspection |
|---|---|---|
| Aggregate graph-`S^d` exclusion and target set | Section 5.1, printed p. 42, PDF index 48 | Extracted text and rendered page |
| Zobel topology, maps, and positive domain | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Graphs `G^d`, `H`, and their canonical populations | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Graph `S^d` and five-element population | Appendix B, printed p. 127, PDF index 133 | Extracted text and rendered page |
| Canonical networks 37, 40, 45, and 48 | Appendix C, printed p. 131, PDF index 137 | Extracted text and rendered page |
| Canonical network 72 | Appendix C, printed p. 132, PDF index 138 | Extracted text and rendered page |

No PDF page, rendering, extracted text, or source image is committed.

## 4. Independent graph-S-dual transcription

Visual transcription of the Appendix B diagram gives:

```text
vertices:  A, B, C, E
terminals: A, E (unordered)
edges:     AB, BC, CE, BE, AE
parallel edges: none
```

Normalized topology:

```text
AE || (AB -- (BE || (BC -- CE)))
```

The upper chord is `BE`; the lower chord is `AE`. This is important: replacing
the upper chord by a second `AE` edge produces a different port-augmented cycle
matroid and no RICE match. A separately relabelled fixture with reversed
terminals has the same committed signature, confirming invariance to internal
labels and terminal reversal.

## 5. Target transcriptions

The rendered Appendix C diagrams give the following primitive coloured
topologies. Series and parallel branch order is immaterial, but every edge and
terminal placement below is retained.

| Target | Normalized topology | Composition | Appendix B graph |
|---:|---|---|---|
| 37 | `L2 || (R2 -- (R1 || L1))` | `2R-2L` | `G^d` |
| 40 | `L1 || (R2 -- (R1 || C1))` | `2R-LC` | `G^d` |
| 45 | `C2 || (R2 -- (R1 || C1))` | `2R-2C` | `G^d` |
| 48 | `C1 || (R2 -- (R1 || L1))` | `2R-LC` | `G^d` |
| 72 | `R2 || (R1 -- L1 -- C1)` | `2R-LC` | `H` |

Networks 37, 40, 45, and 48 are all on printed page 131 / PDF index 137.
Network 72 is on printed page 132 / PDF index 138. The independent fixtures in
the reproduction block encode these drawings directly rather than importing a
numbered descriptor from another workspace.

## 6. Complete initial RICE candidate set

The committed 148-record catalogue contains 85 records with `rlc == 5`.
Recolouring every real edge to `R`, retaining the artificial port edge, and
comparing the complete port-augmented cycle-matroid signature finds exactly 15
graph-`S^d` records:

| RICE ID | Composition | Representative descriptor |
|---|---|---|
| `lh148-0c94f62def7dc462` | `R3L0C2` | `0-1:R;0-2:C;0-3:C;1-2:R;2-3:R` |
| `lh148-4cf39db00710fb1c` | `R3L0C2` | `0-1:C;0-2:C;0-3:R;1-3:R;2-3:R` |
| `lh148-90a706c48f568ac5` | `R3L0C2` | `0-1:R;0-2:C;0-3:R;1-3:C;2-3:R` |
| `lh148-3bf13e1a1ad41cd5` | `R3L1C1` | `0-1:C;0-2:L;0-3:R;1-3:R;2-3:R` |
| `lh148-6456494eb91d8897` | `R3L1C1` | `0-1:R;0-2:C;0-3:R;1-3:L;2-3:R` |
| `lh148-81ffdfa53c07c484` | `R3L1C1` | `0-1:L;0-2:C;0-3:R;1-3:R;2-3:R` |
| `lh148-aefb4b8fe01749c6` | `R3L1C1` | `0-1:R;0-2:C;0-3:R;1-3:R;2-3:L` |
| `lh148-d640e5a51b7f9267` | `R3L1C1` | `0-1:R;0-2:C;1-2:R;1-3:L;2-3:R` |
| `lh148-d83685d4a7f0cd41` | `R3L1C1` | `0-1:R;0-2:C;0-3:L;1-2:R;2-3:R` |
| `lh148-e965ee7277ab24b2` | `R3L1C1` | `0-1:R;0-2:C;0-3:L;1-3:R;2-3:R` |
| `lh148-44baa015c7dbccf2` | `R3L2C0` | `0-1:R;0-2:L;0-3:R;1-3:L;2-3:R` |
| `lh148-84fedcab1cc7f77d` | `R3L2C0` | `0-1:L;0-2:L;0-3:R;1-3:R;2-3:R` |
| `lh148-ceda8e624931aa86` | `R3L2C0` | `0-1:R;0-2:L;0-3:L;1-2:R;2-3:R` |
| `lh148-42d941084ce5f049` | `R4L0C1` | `0-1:R;0-2:C;0-3:R;1-3:R;2-3:R` |
| `lh148-f0feabf623eadb0d` | `R4L1C0` | `0-1:R;0-2:L;0-3:R;1-3:R;2-3:R` |

All 15 have source support `support-512149e3cd66bcb4`, two generated source
candidates, and two distinct representative forms. Their composition census is
one `4R-L`, one `4R-C`, three `3R-2L`, three `3R-2C`, and seven `3R-LC`, exactly
matching Appendix B's combined-column totals when the eight canonical and seven
excluded entries are counted together.

The two `R4` records are the already applied simpler-bilinear exclusions. The
five coloured Zobel fixtures below select five of the remaining 13 records;
the other eight are precisely Appendix B's canonical graph-`S^d` population.

## 7. Structural matching method

Both census and coloured checks use the public `rice.ladenheim` objects
`PrimitiveEdge`, `PrimitiveNetwork`, `network_from_descriptor`, and
`canonical_structural_signature`. The relation returned by the API and asserted
by the reproduction is:

```text
colour-preserving-port-augmented-cycle-matroid-v1
```

For the broad census only, all five real edges are recoloured to a common
colour. Final matching retains R/L/C colours. The artificial port edge and
unordered terminal pair are never discarded. No descriptor-string comparison,
graph dualization, target-list order, or catalogue order participates in the
selection.

## 8. Coloured candidate fixtures

The five independently constructed source fixtures are:

| RICE ID | Coloured graph-`S^d` topology | Composition |
|---|---|---|
| `lh148-84fedcab1cc7f77d` | `L || (R -- (R || (R -- L)))` | `R3L2C0` |
| `lh148-81ffdfa53c07c484` | `L || (R -- (R || (R -- C)))` | `R3L1C1` |
| `lh148-4cf39db00710fb1c` | `C || (R -- (R || (R -- C)))` | `R3L0C2` |
| `lh148-3bf13e1a1ad41cd5` | `C || (R -- (R || (R -- L)))` | `R3L1C1` |
| `lh148-aefb4b8fe01749c6` | `R || (R -- (R || (L -- C)))` | `R3L1C1` |

Each candidate is the unique catalogue record with its full coloured
structural signature. The `L--C` order in the last fixture may be interchanged
within that series arm; the committed relation treats that as the same network.
The reproduction also proves that no sixth graph-`S^d` record matches one of
these five pathway signatures.

## 9. Candidate-to-target mappings

| RICE catalogue ID | Composition | Proposed target | Aggregate source support | Structural match | Zobel derivation | Overall status | Notes |
|---|---|---:|---|---|---|---|---|
| `lh148-84fedcab1cc7f77d` | `R3L2C0` | 37 | aggregate source-stated | exact coloured signature | inverse map plus series-R merge | `independently-checked` | direct L; transformed-arm L |
| `lh148-81ffdfa53c07c484` | `R3L1C1` | 40 | aggregate source-stated | exact coloured signature | inverse map plus series-R merge | `independently-checked` | direct L; transformed-arm C |
| `lh148-4cf39db00710fb1c` | `R3L0C2` | 45 | aggregate source-stated | exact coloured signature | inverse map plus series-R merge | `independently-checked` | direct C; transformed-arm C |
| `lh148-3bf13e1a1ad41cd5` | `R3L1C1` | 48 | aggregate source-stated | exact coloured signature | inverse map plus series-R merge | `independently-checked` | direct C; transformed-arm L |
| `lh148-aefb4b8fe01749c6` | `R3L1C1` | 72 | aggregate source-stated | exact coloured signature | forward map plus parallel-R merge | `independently-checked` | composite series L-C arm |

The first four targets are allocated by the independently transcribed direct
reactive and transformed-arm reactive colours, not by their order in Section
5.1. The fifth has a different source pathway and a separately transcribed
graph-`H` target. Canonical target numbers are reduction destinations, not
historical identities of the five-element RICE records.

## 10. Four inverse-map pathways to graph G-dual

Write each of the first four sources as

```text
X || (pR -- (b'R || (a'R -- c'Y)))
```

where `X` is the untouched direct reactive, `Y` is the transformed-arm
reactive, and every coefficient is positive and finite. The parenthesized
right-hand Figure 5.2 topology transforms inversely to

```text
aR -- (bR || cY)
```

with

```text
a = a'b'/(a'+b')
b = (b')^2/(a'+b')
c = c'(b'/(a'+b'))^2.
```

The full result is

```text
X || (pR -- aR -- (bR || cY)).
```

Series interchange places `pR` beside `aR`; the same-kind merge replaces them
by `(p+a)R`, giving

```text
X || (R -- (R || Y)),
```

the independently transcribed graph-`G^d` target topology. This yields:

```text
L/L -> network 37
L/C -> network 40
C/C -> network 45
C/L -> network 48.
```

The inverse map's converse is the published forward map

```text
a' = a(a+b)/b
b' = a+b
c' = c((a+b)/b)^2.
```

Direct substitution recovers the starting triple in both directions. All sums,
products, quotients, and squared ratios have strictly positive finite
denominators on the positive finite domain. Thus the map is a bijection on
that domain; there is no omitted positive exceptional case.

## 11. Forward-map pathway to graph H

The remaining source is

```text
qR || (aR -- (bR || cW)),   W = L -- C.
```

Here Figure 5.2 acts on `R` and the complete composite series one-port `W`.
The published forward map gives

```text
qR || (b'R || (a'R -- c'W)),

a' = a(a+b)/b,
b' = a+b,
c' = c((a+b)/b)^2.
```

The untouched `qR` and transformed `b'R` branches are parallel and merge to a
single positive resistor. Scaling the series one-port `W` scales both primitive
impedances while retaining one L and one C. The result is

```text
R || (R -- L -- C),
```

which has the exact coloured signature of the independently transcribed graph
`H` fixture and canonical network 72. The inverse equations displayed in the
previous section recover `a`, `b`, and `c` exactly, so this pathway also covers
the full positive finite domain in both directions.

The resistor merge is the element-count reduction. Series interchange inside
`W` is structural equivalence, not an additional synthesis transformation.

## 12. Exact structural and immittance corroboration

The reproduction block evaluates all identities with `fractions.Fraction`.
For the four inverse paths it checks, for multiple positive tuples and multiple
positive values of the arbitrary reactive impedance `Y` and untouched
impedance `X`,

```text
X || (p + (b' || (a' + c'Y)))
 =
X || ((p+a) + (b || cY)).
```

For the forward composite-arm path it checks

```text
q || (a + (b || cW))
 =
(q || b') || (a' + c'W)
```

for multiple positive values of the arbitrary composite impedance `W`. It also
checks both coefficient maps are mutual inverses and every coefficient and
merged resistor is positive. These exact substitutions corroborate the general
symbolic identities; a finite sample is not presented as the proof.

## 13. Provenance and sibling-workspace audit

The authoritative conclusions come only from the rendered and extracted
Morelli-Smith source. The RICE correspondence comes only from the committed
catalogue and public structural API. The exact algebra is independently
reproduced here.

A bounded read-only audit found the following sibling state:

| Repository | Commit | Item inspected | Result |
|---|---|---|---|
| `../network-theory` | `87b831831c154c5c3675853a99ff7e5a2b7dfb6d` | `016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/img/Sd.png` | visual cross-check agrees with the independently rendered Appendix B fixture; not used for authority or candidate selection |
| `../pynntt` | `f3db06032cbe23d583d77f6cb79d21ced90d7651` | bounded filename/text search | no graph-`S^d` mapping lead used |
| `../pynntt_lab` | `1ddd90034da4594bb6a3728b0700918883fd1172` | local authoritative PDF path only | supplied the PDF copy, not a workspace mapping |

All three repositories were clean and remained read-only. Electrical duality
with the graph-`S` results agrees as a late cross-check, but supplied neither a
subject ID nor a target allocation in this investigation.

## 14. Conclusions

The evidence independently establishes all five mappings listed in Section 9.
The result follows from the rendered graph-`S^d` fixture, the complete 85-record
census and 15-member family, five unique coloured structural signatures,
independently rendered targets, complete Figure 5.2 pathways, and exact
positive-domain immittance checks.

Morelli and Smith states the graph family, count five, transformation class,
and collective target set. It does not state any RICE ID. The individual
correspondences and target allocation are therefore independently checked, not
individually source-stated. Network numbers 37, 40, 45, 48, and 72 remain
reduction targets rather than historical identifiers.

## 15. Remaining uncertainties and production boundary

No ambiguity remains within this five-member evidence group under the committed
structural relation. The historical limitation that the publication does not
print RICE IDs remains explicit.

This report does not apply the mappings. Production remains 27 excluded, 121
unresolved, and 0 retained; graph assignments remain null and historical
identifier lists remain empty. A separate reviewed production application is
required. The final eight O/O-dual and bridge exclusions are outside this goal.

## 16. Reproduction commands

Run from the RICE repository root at evidence merge baseline
`22e51deeab83c374a834aee8935812400c4f4f4c` or a descendant that has not applied
the graph-`S^d` findings:

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


RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"


def make(edges, terminals=("A", "E")):
    return PrimitiveNetwork(
        terminals,
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def uncoloured_signature(network):
    plain = PrimitiveNetwork(
        network.terminals,
        tuple(PrimitiveEdge(edge.u, edge.v, "R") for edge in network.edges),
    )
    signature = canonical_structural_signature(plain)
    assert signature.relation == RELATION
    return signature


def parallel(*values):
    reciprocal = sum((Fraction(1, value) for value in values), Fraction())
    return Fraction(1, reciprocal)


graph_sd = make(
    [
        ("A", "B", "R"),
        ("B", "C", "R"),
        ("C", "E", "R"),
        ("B", "E", "R"),
        ("A", "E", "R"),
    ]
)
relabeled_sd = make(
    [
        ("E", "Q", "R"),
        ("Q", "P", "R"),
        ("P", "A", "R"),
        ("Q", "A", "R"),
        ("E", "A", "R"),
    ],
    terminals=("E", "A"),
)
assert uncoloured_signature(graph_sd) == uncoloured_signature(relabeled_sd)

fixtures = {
    "lh148-84fedcab1cc7f77d": (
        37,
        "L",
        "L",
        make(
            [
                ("A", "E", "L"),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "L"),
            ]
        ),
    ),
    "lh148-81ffdfa53c07c484": (
        40,
        "L",
        "C",
        make(
            [
                ("A", "E", "L"),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "C"),
            ]
        ),
    ),
    "lh148-4cf39db00710fb1c": (
        45,
        "C",
        "C",
        make(
            [
                ("A", "E", "C"),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "C"),
            ]
        ),
    ),
    "lh148-3bf13e1a1ad41cd5": (
        48,
        "C",
        "L",
        make(
            [
                ("A", "E", "C"),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "L"),
            ]
        ),
    ),
    "lh148-aefb4b8fe01749c6": (
        72,
        "R",
        "L--C",
        make(
            [
                ("A", "E", "R"),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "L"),
                ("C", "E", "C"),
            ]
        ),
    ),
}

targets = {
    37: make(
        [
            ("A", "E", "L"),
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "L"),
        ]
    ),
    40: make(
        [
            ("A", "E", "L"),
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "C"),
        ]
    ),
    45: make(
        [
            ("A", "E", "C"),
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "C"),
        ]
    ),
    48: make(
        [
            ("A", "E", "C"),
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "L"),
        ]
    ),
    72: make(
        [
            ("A", "E", "R"),
            ("A", "B", "R"),
            ("B", "C", "L"),
            ("C", "E", "C"),
        ]
    ),
}

target_by_types = {
    ("L", "L"): 37,
    ("L", "C"): 40,
    ("C", "C"): 45,
    ("C", "L"): 48,
}

with open("data/counts/ladenheim-148.json", encoding="utf-8") as stream:
    catalogue = json.load(stream)

five_element = [row for row in catalogue["records"] if row["rlc"] == 5]
assert len(five_element) == 85
matches = [
    row
    for row in five_element
    if uncoloured_signature(
        network_from_descriptor(row["representative_descriptor"])
    )
    == uncoloured_signature(graph_sd)
]
assert len(matches) == 15
assert {row["source_support_id"] for row in matches} == {
    "support-512149e3cd66bcb4"
}
assert all(row["generated_source_candidates"] == 2 for row in matches)
assert all(row["distinct_representative_forms"] == 2 for row in matches)
assert Counter((row["r"], row["l"], row["c"]) for row in matches) == {
    (4, 1, 0): 1,
    (4, 0, 1): 1,
    (3, 2, 0): 3,
    (3, 0, 2): 3,
    (3, 1, 1): 7,
}

print("five-element records", len(five_element))
print("graph-S-dual candidates", len(matches))
print("uncoloured signature", uncoloured_signature(graph_sd))
for row in matches:
    print(
        row["catalogue_id"],
        f"R{row['r']}L{row['l']}C{row['c']}",
        row["representative_descriptor"],
        row["source_support_id"],
        row["source_assignment_id"],
        row["generated_source_candidates"],
        row["distinct_representative_forms"],
    )

by_id = {row["catalogue_id"]: row for row in matches}
assert set(fixtures) < set(by_id)
assert len(fixtures) == 5
pathway_signatures = {
    canonical_structural_signature(fixture): target
    for target, _, _, fixture in fixtures.values()
}
assert len(pathway_signatures) == 5
zobel_matches = [
    row
    for row in matches
    if canonical_structural_signature(
        network_from_descriptor(row["representative_descriptor"])
    )
    in pathway_signatures
]
assert {row["catalogue_id"] for row in zobel_matches} == set(fixtures)
assert Counter(
    (by_id[catalogue_id]["r"], by_id[catalogue_id]["l"], by_id[catalogue_id]["c"])
    for catalogue_id in fixtures
) == {(3, 0, 2): 1, (3, 2, 0): 1, (3, 1, 1): 3}

for catalogue_id, (target, direct, arm, fixture) in fixtures.items():
    record = network_from_descriptor(by_id[catalogue_id]["representative_descriptor"])
    assert canonical_structural_signature(record) == canonical_structural_signature(
        fixture
    )
    if target == 72:
        reduced = make(
            [
                ("A", "E", "R"),
                ("A", "B", "R"),
                ("B", "C", "L"),
                ("C", "E", "C"),
            ]
        )
    else:
        assert target == target_by_types[(direct, arm)]
        reduced = make(
            [
                ("A", "E", direct),
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "E", arm),
            ]
        )
    assert canonical_structural_signature(reduced) == (
        canonical_structural_signature(targets[target])
    )
    print(
        catalogue_id,
        "-> canonical network",
        target,
        f"({direct}, {arm}): coloured source and target fixtures OK",
    )

# Four graph-G-dual paths use the inverse Figure 5.2 map on
# b'R || (a'R -- c'Y), followed by a pR -- aR merge.
inverse_parameters = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 3)),
    (Fraction(5, 2), Fraction(7, 3), Fraction(11, 4), Fraction(13, 6)),
    (Fraction(7, 4), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8)),
)
samples = (
    (Fraction(2, 3), Fraction(3, 5)),
    (Fraction(5, 4), Fraction(7, 6)),
    (Fraction(11, 7), Fraction(13, 8)),
    (Fraction(17, 9), Fraction(19, 10)),
)
for a_prime, b_prime, c_prime, leading_r in inverse_parameters:
    a = a_prime * b_prime / (a_prime + b_prime)
    b = b_prime**2 / (a_prime + b_prime)
    c = c_prime * (b_prime / (a_prime + b_prime)) ** 2
    merged_r = leading_r + a
    assert all(value > 0 for value in (
        a, b, c, a_prime, b_prime, c_prime, leading_r, merged_r
    ))
    assert a_prime == a * (a + b) / b
    assert b_prime == a + b
    assert c_prime == c * ((a + b) / b) ** 2
    for direct_value, arm_value in samples:
        source = parallel(
            direct_value,
            leading_r + parallel(
                b_prime,
                a_prime + c_prime * arm_value,
            ),
        )
        transformed = parallel(
            direct_value,
            merged_r + parallel(b, c * arm_value),
        )
        assert source == transformed

# The graph-H path uses the forward map on aR -- (bR || cW),
# followed by an untouched qR || b'R merge.
forward_parameters = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 3)),
    (Fraction(5, 2), Fraction(7, 3), Fraction(11, 4), Fraction(13, 6)),
    (Fraction(7, 4), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8)),
)
for a, b, c, untouched_r in forward_parameters:
    a_prime = a * (a + b) / b
    b_prime = a + b
    c_prime = c * ((a + b) / b) ** 2
    merged_r = parallel(untouched_r, b_prime)
    assert all(value > 0 for value in (
        a, b, c, a_prime, b_prime, c_prime, untouched_r, merged_r
    ))
    assert a == a_prime * b_prime / (a_prime + b_prime)
    assert b == b_prime**2 / (a_prime + b_prime)
    assert c == c_prime * (b_prime / (a_prime + b_prime)) ** 2
    for _, composite_value in samples:
        source = parallel(
            untouched_r,
            a + parallel(b, c * composite_value),
        )
        transformed = parallel(
            merged_r,
            a_prime + c_prime * composite_value,
        )
        assert source == transformed

with open(
    "data/comparisons/ladenheim-148-to-108.json",
    encoding="utf-8",
) as stream:
    production = json.load(stream)
assert production["format_version"] == 3
assert production["summary"]["by_proposed_disposition"] == {
    "exclude": 27,
    "unresolved": 121,
}
assert all(row["basic_graph_assignment"] is None for row in production["records"])
assert all(not row["historical_identifiers"] for row in production["records"])
assert all(
    next(
        row
        for row in production["records"]
        if row["catalogue_id"] == catalogue_id
    )["comparison_status"]
    == "unresolved"
    for catalogue_id in fixtures
)
print("exact Figure 5.2 and immittance checks: 5 pathways OK")
print("production unchanged: 27 excluded / 121 unresolved / 0 retained")
PY
```

Observed deterministic output includes 85 five-element records, all 15
graph-`S^d` candidates and their catalogue provenance, five successful coloured
source/target checks, five exact Figure 5.2 pathways, and unchanged production.
The concluding output is:

```text
lh148-84fedcab1cc7f77d -> canonical network 37 (L, L): coloured source and target fixtures OK
lh148-81ffdfa53c07c484 -> canonical network 40 (L, C): coloured source and target fixtures OK
lh148-4cf39db00710fb1c -> canonical network 45 (C, C): coloured source and target fixtures OK
lh148-3bf13e1a1ad41cd5 -> canonical network 48 (C, L): coloured source and target fixtures OK
lh148-aefb4b8fe01749c6 -> canonical network 72 (R, L--C): coloured source and target fixtures OK
exact Figure 5.2 and immittance checks: 5 pathways OK
production unchanged: 27 excluded / 121 unresolved / 0 retained
```

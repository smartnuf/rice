# Evidence for the graph-S five-element Zobel exclusions

## 1. Purpose and scope

This report investigates only the five five-element series-parallel networks
with Morelli and Smith basic graph `S` that Section 5.1 collectively says are
removed by Zobel transformation to canonical networks 22, 24, 30, 33, and 73.
It visually transcribes the source and target diagrams, reproduces the complete
graph-`S` RICE census under
`colour-preserving-port-augmented-cycle-matroid-v1`, and checks every proposed
candidate-to-target correspondence structurally and algebraically.

This is evidence-only work. It does not change production, assign a historical
number or basic graph to a RICE record, investigate graph `S^d`, or claim to
reproduce the canonical 108-network catalogue. Production remains 22 excluded,
126 unresolved, and 0 retained records.

The publication states the five-member graph-family/target relationship only
in aggregate. It does not print RICE catalogue IDs or pair individual graph-`S`
assignments with target numbers. Consequently, `aggregate source-stated` below
describes only the publication claim; each individual mapping is an
independently reproduced and checked conclusion.

## 2. Authoritative source statements

Section 5.1 states that five five-element networks with graph structure `S`
reduce by Zobel transformation to canonical networks 22, 24, 30, 33, and 73.
This establishes the graph family, count, transformation class, and collective
target set. It does not allocate a target to an individual RICE record.

Appendix B's graph-`S` row reports 15 assignments in all and eight canonical
assignments. Its columns contain:

- two excluded `4R-L / 4R-C` assignments;
- two excluded plus four canonical assignments in the combined
  `3R-2L / 3R-2C` column; and
- three excluded plus four canonical `3R-LC` assignments.

The two four-resistor assignments belong to Section 5.1's separately stated
simpler-bilinear category and are already represented in production. The
remaining five parenthesized assignments are precisely the graph-`S` Zobel
population: two from the combined two-reactive column and three from `3R-LC`.
The combined column does not separately source-state one inductive and one
capacitive case; that split is independently reproduced below.

Section 5.3.1 and Figure 5.2 state that, for impedances `Z1` and `Z2`,

```text
(b Z1 || c Z2) -- a Z1
    <->
b' Z1 || (a' Z1 -- c' Z2)
```

with forward map

```text
a' = a(a+b)/b
b' = a+b
c' = c((a+b)/b)^2
```

and inverse map

```text
a = a'b'/(a'+b')
b = (b')^2/(a'+b')
c = c'(b'/(a'+b'))^2.
```

The source explicitly states that finite strictly positive coefficients remain
finite and strictly positive in either direction.

## 3. Source locators

The authoritative source is A. Morelli and M. C. Smith, *Passive Network
Synthesis: An Approach to Classification* (2019). The inspected local copy was:

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Precise locator | Inspection |
|---|---|---|
| Aggregate graph-`S` exclusion and collective target set | Section 5.1, printed p. 42, zero-based PDF index 48 | Extracted text and rendered page |
| Zobel topology, coefficient maps, and positivity | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Graphs `G` and `H^d` and their canonical populations | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Graph `S`, its population, and its canonical assignments | Appendix B, printed p. 127, PDF index 133 | Extracted text and rendered page |
| Target diagrams for canonical networks 22, 24, 30, and 33 | Appendix C, printed p. 130, PDF index 136 | Extracted text and rendered page |
| Target diagram for canonical network 73 | Appendix C, printed p. 133, PDF index 139 | Extracted text and rendered page |

Every graph and circuit topology was transcribed from a rendered page, not
from extracted text alone. No PDF, render, extracted text, OCR, or copied image
is committed.

## 4. Transcription of graph S

The independently transcribed normalized two-terminal multigraph is:

```text
vertices:  A, B, C, E
terminals: {A, E}
edges:     AB, BE, BC, CE_1, CE_2
parallel multiplicity: two C-E edges
```

Equivalently,

```text
AB -- (BE || (BC -- (CE_1 || CE_2))).
```

Appendix B, printed p. 127 / PDF index 133, shows black terminal vertices at
`A` and `E`, white internal vertices `B` and `C`, the leading `A-B` edge, the
upper `B-E` chord, the `B-C` edge, and two visibly distinct `C-E` branches.
The two parallel branches remain distinct primitive edges.

The reproduction separately verifies invariance under internal relabelling and
terminal reversal. Neither that invariance nor presumed graph duality is used
to select any subject.

## 5. Transcription of target graphs and networks

Appendix B identifies canonical networks 22, 24, 30, and 33 as graph `G` and
canonical network 73 as graph `H^d`. Their normalized fixtures are:

```text
G:
vertices:  A, B, C, E
terminals: {A, E}
edges:     AB, BE, BC, CE
topology:  AB -- (BE || (BC -- CE))

H^d:
vertices:  A, B, E
terminals: {A, E}
edges:     AB, BE_1, BE_2, BE_3
topology:  AB -- (BE_1 || BE_2 || BE_3)
```

The rendered Appendix C diagrams give:

| Target | Primitive colours | Series/parallel topology | Composition |
|---:|---|---|---|
| 22 | `AB:C2`, `BE:R2`, `BC:R1`, `CE:C1` | `C -- (R || (R -- C))` | `2R-2C` |
| 24 | `AB:C1`, `BE:R2`, `BC:R1`, `CE:L1` | `C -- (R || (R -- L))` | `2R-LC` |
| 30 | `AB:L2`, `BE:R2`, `BC:R1`, `CE:L1` | `L -- (R || (R -- L))` | `2R-2L` |
| 33 | `AB:L1`, `BE:R2`, `BC:R1`, `CE:C1` | `L -- (R || (R -- C))` | `2R-LC` |
| 73 | `AB:R2`, `BE_1:R1`, `BE_2:L1`, `BE_3:C1` | `R -- (R || L || C)` | `2R-LC` |

These numbers are reduction destinations, not historical identities of the
five-element RICE subjects.

## 6. Complete initial RICE candidate census

The committed structural catalogue contains 85 five-element records.
Recolouring every real edge to `R`, while preserving the artificial port edge
and unordered terminal pair, yields exactly 15 graph-`S` matches:

| RICE catalogue ID | Composition | Representative descriptor | Assignment ID |
|---|---:|---|---|
| `lh148-0d78e9c38dc5b94e` | `R3L0C2` | `0-2:C;0-2:R;0-3:C;1-3:R;2-3:R` | `assignment-3e62ebb934217512` |
| `lh148-a99495648823d8f1` | `R3L0C2` | `0-2:C;0-2:R;0-3:R;1-3:R;2-3:C` | `assignment-8f82bb6313aea3b3` |
| `lh148-dffc6c65dc65c0ec` | `R3L0C2` | `0-2:C;0-2:R;0-3:R;1-3:C;2-3:R` | `assignment-aec44e8cb846a57c` |
| `lh148-45d19cefc5b496ce` | `R3L1C1` | `0-2:C;0-2:L;0-3:R;1-3:R;2-3:R` | `assignment-ebf352171250ee2c` |
| `lh148-53370c9917eea4d0` | `R3L1C1` | `0-2:C;0-2:R;0-3:R;1-3:L;2-3:R` | `assignment-ef41131197bc759e` |
| `lh148-5bdd1d37b2007a4c` | `R3L1C1` | `0-2:C;1-2:R;1-3:L;1-3:R;2-3:R` | `assignment-d27b9f0e9ee83813` |
| `lh148-6601ce95cb4866ea` | `R3L1C1` | `0-2:C;0-3:R;1-3:R;2-3:L;2-3:R` | `assignment-26cc34db131f88d3` |
| `lh148-66a0391fd4dc6879` | `R3L1C1` | `0-2:C;0-2:R;0-3:R;1-3:R;2-3:L` | `assignment-bb6b156a9833a063` |
| `lh148-75a667eae30e9bd2` | `R3L1C1` | `0-2:C;0-3:L;0-3:R;1-2:R;2-3:R` | `assignment-7437a18eb9351a1c` |
| `lh148-e5953a9cf3d9cfa6` | `R3L1C1` | `0-2:C;0-2:R;0-3:L;1-3:R;2-3:R` | `assignment-cec55dece40abf84` |
| `lh148-3a5b171b0d2af32a` | `R3L2C0` | `0-2:L;0-2:R;0-3:L;1-3:R;2-3:R` | `assignment-2dfe763babd18450` |
| `lh148-3a7ebfebce0db0a4` | `R3L2C0` | `0-2:L;0-2:R;0-3:R;1-3:L;2-3:R` | `assignment-323e8fc87e9d1e3d` |
| `lh148-3ae4767397da2b12` | `R3L2C0` | `0-2:L;0-2:R;0-3:R;1-3:R;2-3:L` | `assignment-17f669248efe1ff9` |
| `lh148-a134c33979433ce6` | `R4L0C1` | `0-2:C;0-2:R;0-3:R;1-3:R;2-3:R` | `assignment-e5dc77c443f85893` |
| `lh148-82299f914f077df2` | `R4L1C0` | `0-2:L;0-2:R;0-3:R;1-3:R;2-3:R` | `assignment-974bbe2233358ed3` |

Every match has source support `support-f5983f285b660184`, two generated source
candidates, and two representative forms. The common uncoloured signature is:

```text
relation=colour-preserving-port-augmented-cycle-matroid-v1
multiplicities=(5,0,0,1)
cycle_space=(0,3,13,14,52,55,57,58)
```

The reproduced composition census is `1 R4L1C0`, `1 R4L0C1`, `3 R3L2C0`,
`3 R3L0C2`, and `7 R3L1C1`, agreeing exactly with Appendix B's 15-member row.

## 7. Structural matching and narrowing method

The census uses only `PrimitiveNetwork`, `PrimitiveEdge`,
`network_from_descriptor`, and `canonical_structural_signature` from
`rice.ladenheim`. It compares complete port-augmented cycle-matroid signatures,
not descriptor strings.

The two `R4` records are already the source-stated graph-`S` members of the
simpler-bilinear category and are not reconsidered here. Among the thirteen
`R3` assignments, exact coloured signatures identify precisely four fixtures
of the form

```text
P -- (Q R || (a R -- (b R || c X)))
```

where `P` and `X` are reactive and `Q` is an untouched resistor. Exactly one
further fixture has the form

```text
p R -- (b' R || (a' R -- c' (L || C))).
```

These are the only five members satisfying the complete one-step Zobel and
same-kind-merge pathways below. Their component census is one `3R-2C`, one
`3R-2L`, and three `3R-LC`, exactly matching Appendix B's parenthesized Zobel
population. No expected target count is used to manufacture a match: the code
asserts the complete 15-member family first, constructs all five coloured
fixtures explicitly, and checks each discovered RICE signature.

## 8. Candidate-to-target results

| RICE catalogue ID | Composition | Proposed target | Aggregate source support | Structural match | Zobel derivation | Overall status | Notes |
|---|---:|---:|---|---|---|---|---|
| `lh148-dffc6c65dc65c0ec` | `R3L0C2` | 22 | aggregate source-stated | exact coloured signature | forward map and parallel-R merge | `independently-checked` | leading C; transformed-arm C |
| `lh148-5bdd1d37b2007a4c` | `R3L1C1` | 24 | aggregate source-stated | exact coloured signature | forward map and parallel-R merge | `independently-checked` | leading C; transformed-arm L |
| `lh148-3a7ebfebce0db0a4` | `R3L2C0` | 30 | aggregate source-stated | exact coloured signature | forward map and parallel-R merge | `independently-checked` | leading L; transformed-arm L |
| `lh148-53370c9917eea4d0` | `R3L1C1` | 33 | aggregate source-stated | exact coloured signature | forward map and parallel-R merge | `independently-checked` | leading L; transformed-arm C |
| `lh148-45d19cefc5b496ce` | `R3L1C1` | 73 | aggregate source-stated | exact coloured signature | inverse map, series interchange, series-R merge | `independently-checked` | composite transformed arm `L || C` |

`source-stated` applies only to the collective graph-family claim. None of the
individual RICE-ID or target allocations is printed by Morelli and Smith.

## 9. Four forward pathways to graph G

For targets 22, 24, 30, and 33, write the coloured source as

```text
P -- [Q R || {a R -- (b R || c X)}].
```

The braced network is the terminal-reversed left side of Figure 5.2; reversing
a two-terminal one-port does not change its immittance. The forward map gives

```text
P -- [Q R || {b' R || (a' R -- c' X)}].
```

The untouched `Q R` and new `b' R` are parallel. Their ordinary same-kind
merge has coefficient

```text
Q* = Q b'/(Q+b') > 0,
```

so the reduced topology is

```text
P -- [Q* R || (a' R -- c' X)],
```

the rendered graph-`G` fixture. The untouched leading reactive `P` and the
transformed-arm reactive `X` determine the target independently of list order:

| Subject | Source fixture | Figure direction | Merge | Result |
|---|---|---|---|---|
| `lh148-dffc6c65dc65c0ec` | `C -- [R || {R -- (R || C)}]` | forward | `R || R` | `C -- [R || (R -- C)]`, network 22 |
| `lh148-5bdd1d37b2007a4c` | `C -- [R || {R -- (R || L)}]` | forward | `R || R` | `C -- [R || (R -- L)]`, network 24 |
| `lh148-3a7ebfebce0db0a4` | `L -- [R || {R -- (R || L)}]` | forward | `R || R` | `L -- [R || (R -- L)]`, network 30 |
| `lh148-53370c9917eea4d0` | `L -- [R || {R -- (R || C)}]` | forward | `R || R` | `L -- [R || (R -- C)]`, network 33 |

For positive finite `a`, `b`, `c`, and `Q`, the published map makes `a'`,
`b'`, and `c'` positive and finite, and the displayed parallel merge makes
`Q*` positive and finite. Scaling `X` scales its single primitive reactive
impedance without changing its type.

## 10. Inverse pathway to graph H-dual

The fifth source is

```text
p R -- [b' R || (a' R -- c' W)],    W = L || C.
```

Apply the inverse Figure 5.2 map to the bracketed right-hand network:

```text
p R -- [(b R || c W) -- a R].
```

At the top-level series connection, series interchange places `p R` adjacent
to `a R`; this is the publication's ordinary series-interchange equivalence,
not a second synthesis transformation. Merging those resistors gives

```text
(p+a) R -- (b R || c L || c C),
```

which is graph `H^d` with topology `R -- (R || L || C)`. Its exact coloured
signature equals the independently transcribed canonical-network-73 fixture.
Scaling the composite one-port `W` by positive `c` scales both parallel
element impedances and preserves their `L` and `C` types.

The inverse coefficients are positive and finite for positive finite
`a'`, `b'`, and `c'`; `p+a` is likewise positive and finite. Substitution into
the forward formulas reproduces `a'`, `b'`, and `c'`, so no positive exceptional
case is omitted.

## 11. Exact immittance corroboration

The reproduction block uses `fractions.Fraction` for four nontrivial positive
coefficient tuples and four pairs of positive exact impedance samples on each
distinct pathway.

For the four forward paths it verifies exactly:

```text
P + Q || [a + (b || cX)]
  = P + (Q || b') || [a' + c'X].
```

For the inverse path it verifies exactly:

```text
p + [b' || (a' + c'W)]
  = (p+a) + [b || cW].
```

All coefficients and merged coefficients are asserted positive. These finite
substitutions corroborate the symbolic identity; they are not presented as a
standalone proof.

## 12. Provenance distinctions and sibling audit

The historical authority is the rendered and extracted Morelli–Smith
publication. The RICE catalogue and its committed public structural API supply
the independent subject census and coloured comparisons. The exact arithmetic
is a separately reproduced corroboration.

Only after those conclusions were established, a bounded read-only audit found:

- clean `../network-theory` at commit
  `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`, file
  `016--graph-generation/generated_graphs/ladenheim/graph_S`, agrees with the
  five-edge transcription; and
- clean `../pynntt` at commit
  `f3db06032cbe23d583d77f6cb79d21ced90d7651`, file
  `catalogues/2019--MS-network-descriptors.csv`, gives expressions for the
  relevant canonical targets and eight canonical graph-`S` assignments that
  agree with the independently transcribed diagrams.

Clean `../pynntt_lab` at commit
`1ddd90034da4594bb6a3728b0700918883fd1172` supplied the local PDF path but no
mapping authority. No sibling label, descriptor, number, or catalogue order
was used to select a RICE subject or allocate a target.

## 13. Conclusions

The evidence independently establishes exactly five graph-`S` RICE subjects
and allocates all five collective targets without using source-list order:

```text
lh148-dffc6c65dc65c0ec -> canonical network 22
lh148-5bdd1d37b2007a4c -> canonical network 24
lh148-3a7ebfebce0db0a4 -> canonical network 30
lh148-53370c9917eea4d0 -> canonical network 33
lh148-45d19cefc5b496ce -> canonical network 73
```

Each conclusion has an exact coloured source match, a named Figure 5.2
direction and coefficient map, an explicit same-kind merge (plus series
interchange for network 73), a separately constructed target fixture, and
exact immittance corroboration. The individual RICE correspondences remain
independently checked conclusions rather than individually source-stated facts.

## 14. Remaining uncertainties and production boundary

The publication does not print RICE IDs or entry-specific target allocations.
That historical limitation remains explicit even though the structural and
algebraic checks select the five mappings uniquely.

This report does not apply the mappings. Production remains 22 excluded, 126
unresolved, and 0 retained; all graph assignments remain null and all
historical identifier lists remain empty. A separate reviewed production PR is
required. The five graph-`S^d` Zobel exclusions and final eight exclusions are
outside this milestone.

## 15. Reproduction commands

Run from the RICE repository root at merge commit
`98be55f2918076848c7a2a836cbbc83aff35bc6c` or a descendant that has not yet
applied the graph-`S` findings:

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


graph_s = make(
    [
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("B", "C", "R"),
        ("C", "E", "R"),
        ("C", "E", "R"),
    ]
)
relabeled_s = make(
    [
        ("E", "Q", "R"),
        ("Q", "A", "R"),
        ("Q", "P", "R"),
        ("P", "A", "R"),
        ("P", "A", "R"),
    ],
    terminals=("E", "A"),
)
assert uncoloured_signature(graph_s) == uncoloured_signature(relabeled_s)

fixtures = {
    "lh148-dffc6c65dc65c0ec": (
        22,
        "C",
        "C",
        make(
            [
                ("A", "B", "C"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "C"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-5bdd1d37b2007a4c": (
        24,
        "C",
        "L",
        make(
            [
                ("A", "B", "C"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "L"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-3a7ebfebce0db0a4": (
        30,
        "L",
        "L",
        make(
            [
                ("A", "B", "L"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "L"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-53370c9917eea4d0": (
        33,
        "L",
        "C",
        make(
            [
                ("A", "B", "L"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "C"),
                ("C", "E", "R"),
            ]
        ),
    ),
    "lh148-45d19cefc5b496ce": (
        73,
        "R",
        "L||C",
        make(
            [
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", "L"),
                ("C", "E", "C"),
            ]
        ),
    ),
}

targets = {
    22: make(
        [
            ("A", "B", "C"),
            ("B", "E", "R"),
            ("B", "C", "R"),
            ("C", "E", "C"),
        ]
    ),
    24: make(
        [
            ("A", "B", "C"),
            ("B", "E", "R"),
            ("B", "C", "R"),
            ("C", "E", "L"),
        ]
    ),
    30: make(
        [
            ("A", "B", "L"),
            ("B", "E", "R"),
            ("B", "C", "R"),
            ("C", "E", "L"),
        ]
    ),
    33: make(
        [
            ("A", "B", "L"),
            ("B", "E", "R"),
            ("B", "C", "R"),
            ("C", "E", "C"),
        ]
    ),
    73: make(
        [
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "L"),
            ("B", "E", "C"),
        ]
    ),
}

target_by_types = {
    ("C", "C"): 22,
    ("C", "L"): 24,
    ("L", "L"): 30,
    ("L", "C"): 33,
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
    == uncoloured_signature(graph_s)
]
assert len(matches) == 15
assert {row["source_support_id"] for row in matches} == {
    "support-f5983f285b660184"
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
print("graph-S candidates", len(matches))
print("uncoloured signature", uncoloured_signature(graph_s))
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

for catalogue_id, (target, leading, arm, fixture) in fixtures.items():
    record = network_from_descriptor(by_id[catalogue_id]["representative_descriptor"])
    assert canonical_structural_signature(record) == canonical_structural_signature(
        fixture
    )
    if target == 73:
        assert (leading, arm) == ("R", "L||C")
        reduced = make(
            [
                ("A", "B", "R"),
                ("B", "E", "R"),
                ("B", "E", "L"),
                ("B", "E", "C"),
            ]
        )
    else:
        assert target == target_by_types[(leading, arm)]
        reduced = make(
            [
                ("A", "B", leading),
                ("B", "E", "R"),
                ("B", "C", "R"),
                ("C", "E", arm),
            ]
        )
    assert canonical_structural_signature(reduced) == (
        canonical_structural_signature(targets[target])
    )
    print(
        catalogue_id,
        "-> canonical network",
        target,
        f"({leading}, {arm}): coloured source and target fixtures OK",
    )

# Four graph-G paths use the forward Figure 5.2 map on
# aR -- (bR || cX), followed by an untouched-R || b'R merge.
forward_parameters = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 3), Fraction(13, 5)),
    (Fraction(5, 2), Fraction(7, 3), Fraction(11, 4), Fraction(13, 6), Fraction(17, 5)),
    (Fraction(7, 4), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8), Fraction(19, 9)),
)
samples = (
    (Fraction(2, 3), Fraction(3, 5)),
    (Fraction(5, 4), Fraction(7, 6)),
    (Fraction(11, 7), Fraction(13, 8)),
    (Fraction(17, 9), Fraction(19, 10)),
)
for a, b, c, untouched_r, leading_scale in forward_parameters:
    a_prime = a * (a + b) / b
    b_prime = a + b
    c_prime = c * ((a + b) / b) ** 2
    merged_r = parallel(untouched_r, b_prime)
    assert all(value > 0 for value in (a, b, c, a_prime, b_prime, c_prime, merged_r))
    for leading_value, arm_value in samples:
        source = (
            leading_scale * leading_value
            + parallel(
                untouched_r,
                a + parallel(b, c * arm_value),
            )
        )
        transformed = (
            leading_scale * leading_value
            + parallel(
                merged_r,
                a_prime + c_prime * arm_value,
            )
        )
        assert source == transformed

# The graph-H-dual path uses the inverse map on
# b'R || (a'R -- c'W), then interchanges and merges pR -- aR.
inverse_parameters = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 3)),
    (Fraction(5, 2), Fraction(7, 3), Fraction(11, 4), Fraction(13, 6)),
    (Fraction(7, 4), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8)),
)
for a_prime, b_prime, c_prime, leading_r in inverse_parameters:
    a = a_prime * b_prime / (a_prime + b_prime)
    b = b_prime**2 / (a_prime + b_prime)
    c = c_prime * (b_prime / (a_prime + b_prime)) ** 2
    merged_r = leading_r + a
    assert all(value > 0 for value in (a, b, c, a_prime, b_prime, c_prime, merged_r))
    assert a_prime == a * (a + b) / b
    assert b_prime == a + b
    assert c_prime == c * ((a + b) / b) ** 2
    for _, composite_value in samples:
        source = leading_r + parallel(
            b_prime,
            a_prime + c_prime * composite_value,
        )
        transformed = merged_r + parallel(b, c * composite_value)
        assert source == transformed

with open(
    "data/comparisons/ladenheim-148-to-108.json",
    encoding="utf-8",
) as stream:
    production = json.load(stream)
assert production["format_version"] == 3
assert production["summary"]["by_proposed_disposition"] == {
    "exclude": 22,
    "unresolved": 126,
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
print("production unchanged: 22 excluded / 126 unresolved / 0 retained")
PY
```

Observed deterministic output is recorded by the script itself: 85
five-element records, 15 graph-`S` candidates, the complete candidate rows,
five successful coloured source/target checks, five exact Figure 5.2 pathways,
and unchanged production at 22 excluded / 126 unresolved / 0 retained.

The observed summary was:

```text
five-element records 85
graph-S candidates 15
lh148-dffc6c65dc65c0ec -> canonical network 22 (C, C): coloured source and target fixtures OK
lh148-5bdd1d37b2007a4c -> canonical network 24 (C, L): coloured source and target fixtures OK
lh148-3a7ebfebce0db0a4 -> canonical network 30 (L, L): coloured source and target fixtures OK
lh148-53370c9917eea4d0 -> canonical network 33 (L, C): coloured source and target fixtures OK
lh148-45d19cefc5b496ce -> canonical network 73 (R, L||C): coloured source and target fixtures OK
exact Figure 5.2 and immittance checks: 5 pathways OK
production unchanged: 22 excluded / 126 unresolved / 0 retained
```

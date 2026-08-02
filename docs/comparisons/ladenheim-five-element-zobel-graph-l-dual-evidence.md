# Evidence for the graph-L-dual five-element Zobel exclusions

## 1. Purpose and scope

This report investigates only the four five-element series-parallel networks
with Morelli and Smith basic graph `L^d` that Section 5.1 collectively says are
removed by Zobel transformation to canonical networks #35, #39, #43, and #47.
It visually transcribes the source diagrams, reproduces the complete RICE
graph-`L^d` candidate census under
`colour-preserving-port-augmented-cycle-matroid-v1`, and checks every proposed
candidate-to-target correspondence structurally and algebraically.

This report was originally prepared as evidence only and did not itself change
production, assign a historical number or basic graph to an excluded record,
investigate another graph family, or claim to reproduce the canonical
108-network catalogue. The production update containing this revision applies
the four reviewed mappings through the version 3 subject-bound evidence route.
On this branch, the ledger has 22 excluded, 126 unresolved, and 0 retained
records.

The publication states the four-member graph-family/target relationship only
in aggregate. It does not print RICE catalogue IDs or pair individual
graph-`L^d` assignments with target numbers. Consequently, `source-stated`
below describes only the aggregate publication claim; every individual mapping
is labelled according to its independently reproducible evidence.

## 2. Authoritative source statements

Morelli and Smith, Section 5.1, states that twenty five-element
series-parallel networks are reducible by Zobel transformation and, within that
group, that four with graph structure `L^d` reduce to networks #35, #39, #43,
and #47. This establishes the graph family, count four, transformation class,
and target set collectively. It does not establish which RICE ID maps to which
target.

Appendix B gives the following facts in its graph-`L^d` row:

- there are four five-element assignments in total;
- zero are retained in the canonical total;
- two exclusions lie in the combined `3R-2L / 3R-2C` column; and
- two exclusions lie in the `3R-LC` column.

The parenthesized entries are exclusions, consistent with the row's zero
canonical total. The combined column does **not** separately source-state one
`3R-2L` and one `3R-2C` assignment. That split, and the distinction between the
two `3R-LC` placements, comes from the independently reproduced RICE census and
coloured topology checks below.

Section 5.3.1 states the Figure 5.2 Zobel identity. For any impedances `Z1` and
`Z2`, its left-hand network

```text
(b Z1 || c Z2) -- a Z1
```

is equivalent to its right-hand network

```text
b' Z1 || (a' Z1 -- c' Z2)
```

when

```text
a' = a(a+b)/b
b' = a+b
c' = c((a+b)/b)^2.
```

The inverse map printed with the identity is

```text
a = a'b'/(a'+b')
b = (b')^2/(a'+b')
c = c'(b'/(a'+b'))^2.
```

The source explicitly states that positive finite coefficients map to positive
finite coefficients in either direction.

## 3. Source locators

The authoritative source is A. Morelli and M. C. Smith, *Passive Network
Synthesis: An Approach to Classification* (2019). The inspected local copy was

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Precise locator | Inspection |
|---|---|---|
| Aggregate graph-`L^d` exclusion and target set | Section 5.1, printed p. 42, zero-based PDF index 48 | Extracted text and rendered page |
| Zobel topology, coefficient maps, and positivity | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Four-element Zobel-equivalence context | Figure 6.2, printed p. 50, PDF index 56 | Extracted text and rendered page |
| Target graph `F^d` and its four canonical assignments | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Graph `L^d` and its five-element counts | Appendix B, printed p. 127, PDF index 133 | Extracted text and rendered page |
| Diagram for #35 | Appendix C, printed p. 130, PDF index 136 | Extracted text and rendered page |
| Diagrams for #39, #43, and #47 | Appendix C, printed p. 131, PDF index 137 | Extracted text and rendered page |

The rendered pages were used for every graph and circuit transcription; no
topology was inferred from extracted text alone. No PDF, rendering, extracted
text, or OCR output is committed.

## 4. Transcription of graph L-dual

The independently transcribed normalized two-terminal multigraph is:

```text
vertices:  A, B, E
terminals: {A, E}
edges:     AB_1, AB_2, BE, AE_1, AE_2
parallel multiplicity: two A-B edges and two A-E edges
```

Equivalently,

```text
(AE_1 || AE_2) || ((AB_1 || AB_2) -- BE).
```

The source is the graph-`L^d` drawing in Appendix B, printed p. 127 / PDF index
133. The black vertices are terminals `A` and `E`; the single white vertex is
`B`. The two visibly distinct A-B arcs and two visibly distinct direct A-E arcs
are retained as four separate edges. Together with `BE`, they give five
undirected edges. The normalized names are introduced here only to make the
transcription reconstructible.

The fixture remains unchanged under internal relabelling and terminal reversal
in the committed port-augmented structural signature. Neither this observation
nor duality from graph `L` is used to select a catalogue record.

## 5. Transcription of graph F-dual and the four targets

Appendix B's graph-`F^d` row lists exactly canonical networks #35, #39, #43,
and #47. Its normalized two-terminal multigraph is:

```text
vertices:  A, B, E
terminals: {A, E}
edges:     AE_1, AE_2, AB, BE
parallel multiplicity: two direct A-E edges
topology:  AE_1 || AE_2 || (AB -- BE)
```

Appendix C supplies the following independently transcribed colours and
labels:

| Target | Primitive edges | Series/parallel topology | Composition |
|---:|---|---|---|
| #35 | `AE_1:R2`, `AE_2:L2`, `AB:R1`, `BE:L1` | `R2 || L2 || (R1 -- L1)` | `2R-2L` |
| #39 | `AE_1:R2`, `AE_2:L1`, `AB:R1`, `BE:C1` | `R2 || L1 || (R1 -- C1)` | `2R-LC` |
| #43 | `AE_1:R2`, `AE_2:C2`, `AB:R1`, `BE:C1` | `R2 || C2 || (R1 -- C1)` | `2R-2C` |
| #47 | `AE_1:R2`, `AE_2:C1`, `AB:R1`, `BE:L1` | `R2 || C1 || (R1 -- L1)` | `2R-LC` |

Network #35 is drawn in Appendix C, printed p. 130 / PDF index 136. Networks
#39, #43, and #47 are drawn on printed p. 131 / PDF index 137. The graph-`F^d`
identification comes independently from Appendix B, printed p. 126 / PDF index
132. Figure 6.2 supplies aggregate Zobel-equivalence context but is not used to
allocate individual five-element candidates.

## 6. Complete initial RICE candidate set

The committed structural catalogue contains 85 five-element records. Recolouring
each record's five real edges to one common colour while retaining the
artificial port edge and unordered terminal pair gives exactly four matches to
the transcribed graph-`L^d` signature:

| RICE catalogue ID | Composition | Representative descriptor | Source assignment |
|---|---:|---|---|
| `lh148-5d5fb848a810c9cb` | `R3L0C2` | `0-1:C;0-1:R;0-2:C;0-2:R;1-2:R` | `assignment-35f8245d83d39490` |
| `lh148-534a4f02579831e9` | `R3L1C1` | `0-1:C;0-1:R;0-2:L;0-2:R;1-2:R` | `assignment-42e40d250a1a7ddd` |
| `lh148-9e140322bfd33a22` | `R3L1C1` | `0-1:L;0-1:R;0-2:C;0-2:R;1-2:R` | `assignment-0899751a9aa9a891` |
| `lh148-a1e6c042c7d77e41` | `R3L2C0` | `0-1:L;0-1:R;0-2:L;0-2:R;1-2:R` | `assignment-61adb58aab8b8553` |

All four records use source support `support-9defcf048b659b39`, have two
generated source candidates, and have one distinct representative form. This is
the complete initial graph-`L^d` candidate set, not a subset selected by
composition. Its count four independently agrees with Appendix B's total.

The common uncoloured structural signature is

```text
colour-preserving-port-augmented-cycle-matroid-v1
multiplicities=(5,0,0,1)
cycle_space=(0,3,12,15,21,22,25,26,33,34,45,46,52,55,56,59)
```

## 7. Structural matching method

The reproduction uses existing `rice.ladenheim` APIs only:
`PrimitiveNetwork`, `PrimitiveEdge`, `network_from_descriptor`, and
`canonical_structural_signature`.

For the broad census, every real edge is temporarily coloured `R`. This removes
component assignment while preserving the artificial `P` port edge. Equality
is tested under the catalogue's exact relation,
`colour-preserving-port-augmented-cycle-matroid-v1`. The comparison preserves
the unordered driving-point terminals and parallel-edge multiplicities and is
not descriptor-text equality or presumed dual catalogue numbering.

For final checks, four independent coloured fixtures are constructed on the
transcribed `L^d` edge set. Write `X` for the untouched direct reactive and `Y`
for the reactive in the A-B parallel pair:

```text
L^d(X,Y) = (R || X) || ((R || Y) -- R).
```

Each fixture is compared with its selected record using the unrecoloured
canonical structural signature. Independently transcribed target fixtures are
checked the same way after transformation and resistor merging.

## 8. Candidate composition census

The reproduced census gives:

| Composition | Count | Direct reactive `X` | Transformed reactive `Y` |
|---|---:|---|---|
| `3R-2C` | 1 | C | C |
| `3R-LC` | 1 | C | L |
| `3R-LC` | 1 | L | C |
| `3R-2L` | 1 | L | L |

Thus Appendix B's combined-column count two resolves computationally to one
`3R-2L` and one `3R-2C` record. Its `3R-LC` count two resolves to two different
coloured structural signatures. Neither allocation is described as a separate
source statement.

## 9. Candidate-to-target mappings

| RICE catalogue ID | Composition | Proposed target | Aggregate source support | Structural match | Zobel derivation | Overall status | Notes |
|---|---:|---:|---|---|---|---|---|
| `lh148-5d5fb848a810c9cb` | `3R-2C` | #43 | aggregate source-stated | exact coloured signature | forward Figure 5.2; exact | `independently-checked` | direct C; transformed C |
| `lh148-534a4f02579831e9` | `3R-LC` | #47 | aggregate source-stated | exact coloured signature | forward Figure 5.2; exact | `independently-checked` | direct C; transformed L |
| `lh148-9e140322bfd33a22` | `3R-LC` | #39 | aggregate source-stated | exact coloured signature | forward Figure 5.2; exact | `independently-checked` | direct L; transformed C |
| `lh148-a1e6c042c7d77e41` | `3R-2L` | #35 | aggregate source-stated | exact coloured signature | forward Figure 5.2; exact | `independently-checked` | direct L; transformed L |

`source-stated` means only that Section 5.1 explicitly states the collective
graph-`L^d` count and target set. It does not apply automatically to a RICE-ID
correspondence. Here `independently-checked` means that both the coloured
structural match and the Zobel derivation are reproducible. No target was chosen
from the order of Section 5.1's list.

## 10. Zobel-reduction derivations

Let `Z1=1` denote the resistor impedance basis. Let `Z_Y` be the reactive
impedance in graph `L^d`'s A-B parallel pair and let `Z_X` be the possibly
different untouched direct reactive impedance. Every candidate can be written

```text
d Z_X || r Z1 || [(b Z1 || c Z_Y) -- a Z1].
```

The bracketed subnetwork is the **left-hand side** of Figure 5.2. Apply the
published forward coefficient map

```text
a' = a(a+b)/b
b' = a+b
c' = c((a+b)/b)^2
```

to obtain

```text
d Z_X || r Z1 || b' Z1 || (a' Z1 -- c' Z_Y).
```

The two same-kind direct resistors merge in parallel with coefficient

```text
m = rb'/(r+b'),
```

giving

```text
d Z_X || m Z1 || (a' Z1 -- c' Z_Y).
```

This is graph `F^d`. The untouched direct type `X` and transformed series-arm
type `Y` select the target topology directly:

| Candidate fixture | Figure 5.2 substitution | Result after resistor merge | Target |
|---|---|---|---:|
| `L^d(C,C)` | `Z1=R`, `Z2=C`; direct C untouched | `C || R || (R -- C)` | #43 |
| `L^d(C,L)` | `Z1=R`, `Z2=L`; direct C untouched | `C || R || (R -- L)` | #47 |
| `L^d(L,C)` | `Z1=R`, `Z2=C`; direct L untouched | `L || R || (R -- C)` | #39 |
| `L^d(L,L)` | `Z1=R`, `Z2=L`; direct L untouched | `L || R || (R -- L)` | #35 |

For positive finite `a`, `b`, and `c`, the denominator `b` is positive and
finite, so `a'`, `b'`, and `c'` are positive and finite. Positive finite `r`
and `b'` make `r+b'` positive and finite, hence `m` is positive and finite.
Conversely, substituting the printed inverse map recovers `a`, `b`, and `c`
exactly, and the source's same positivity argument applies. Parallel splitting
of a positive `m` into positive `r` and `b'` is not needed for the claimed
candidate-to-target direction; the Figure 5.2 transformation itself remains
bidirectional over all positive finite coefficients.

Each mapping uses one forward Zobel step followed by one trivial same-kind
parallel resistor merge. None depends on frequency inversion, terminal
reversal, presumed graph duality, a second Zobel step, or an unstated target
ordering. Internal relabelling and terminal reversal are accepted by the
structural relation but do not choose the mapping.

## 11. Exact-arithmetic corroboration

With `p(x,y)=xy/(x+y)`, the affected left-hand Figure 5.2 subnetwork has
impedance

```text
a + p(b, c Z_Y),
```

and the right-hand subnetwork has impedance

```text
p(b', a' + c' Z_Y).
```

The complete candidate and reduced network impedances are therefore

```text
p(d Z_X, r, a + p(b, c Z_Y))
p(d Z_X, m, a' + c' Z_Y),
```

where `p` with more than two arguments denotes parallel composition of all
arguments. The reproduction block uses a different positive rational
coefficient tuple for each mapping, checks the forward and inverse maps, checks
the parallel merge, and verifies both displayed equalities exactly for five
pairs of positive rational `Z_X` and `Z_Y` values. These substitutions
corroborate the symbolic identity; a finite sample is not presented as its
proof.

## 12. Conclusions

The evidence selects exactly four graph-`L^d` RICE records, with no additional
candidate under the committed relation. The census independently reproduces
Appendix B's total and composition-column counts. Exact coloured fixtures
distinguish the two mixed-reactive placements, and one forward Zobel step plus
a parallel resistor merge assigns all four targets unambiguously:

```text
lh148-5d5fb848a810c9cb -> #43
lh148-534a4f02579831e9 -> #47
lh148-9e140322bfd33a22 -> #39
lh148-a1e6c042c7d77e41 -> #35
```

All four mappings are `independently-checked`, not individually
`source-stated`. Canonical networks #35, #39, #43, and #47 are reduction
destinations rather than historical identities of the excluded five-element
records. This report originally supplied evidence for a separate ledger
review; the production update containing this revision now applies all four
mappings without changing their evidential conclusions. Production on this
branch has 22 excluded, 126 unresolved, and 0 retained records.

## 13. Remaining uncertainties

No alternative graph-`L^d` candidate or target ambiguity remains under the
rendered source diagrams and the repository's named structural relation. The
publication does not state individual RICE-ID correspondences, so those remain
independently reproduced computational conclusions rather than direct
historical statements.

Fourteen five-element Zobel exclusions were unapplied when this evidence-only
investigation was prepared. This production update applies the four graph-`L^d`
findings and leaves the ten graph-`S`/`S^d` exclusions unresolved. The final
eight O/O-dual and bridge exclusions remain outside this goal milestone.

## 14. Previous-workspace audit

The bounded read-only audit was performed only after the source transcription
and RICE mapping were independently established:

- `../network-theory` at commit
  `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`, file
  `016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/analysis-of-basic-graphs.md`,
  gives graph `Ld` edge list `AB;BC;CB;CA;AC` with terminals `A,C`. After
  renaming `C` to `E`, it agrees with the independently rendered fixture. It
  supplied no RICE-ID or target allocation and is not historical authority.
- `../pynntt` at commit
  `f3db06032cbe23d583d77f6cb79d21ced90d7651`, file
  `catalogues/2019--MS-network-descriptors.csv`, gives descriptors for targets
  35, 39, 43, and 47 that agree with the independently transcribed Appendix C
  topologies. They were not used to select the mappings.
- A bounded search of clean `../pynntt_lab` at commit
  `1ddd90034da4594bb6a3728b0700918883fd1172` supplied no candidate mapping used
  as evidence. The authoritative PDF happens to reside there, but authority
  comes from the publication rather than the workspace.

All three sibling worktrees were clean and remained unchanged.

## 15. Reproduction commands

Run from the RICE repository root at commit
`deefccfd8732b1d35fa5b978a4de38d92d33f1dd` or a descendant:

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
    total_reciprocal = sum((Fraction(1, value) for value in values), Fraction())
    return Fraction(1, total_reciprocal)


graph_ld = make(
    [
        ("A", "B", "R"),
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("A", "E", "R"),
        ("A", "E", "R"),
    ]
)

# Explicitly verify relabelling and unordered terminal reversal.
relabeled_ld = make(
    [
        ("E", "Q", "R"),
        ("E", "Q", "R"),
        ("Q", "A", "R"),
        ("E", "A", "R"),
        ("E", "A", "R"),
    ],
    terminals=("E", "A"),
)
assert uncoloured_signature(graph_ld) == uncoloured_signature(relabeled_ld)

fixtures = {
    "lh148-5d5fb848a810c9cb": (
        "C",
        "C",
        43,
        make(
            [
                ("A", "E", "R"),
                ("A", "E", "C"),
                ("A", "B", "R"),
                ("A", "B", "C"),
                ("B", "E", "R"),
            ]
        ),
    ),
    "lh148-534a4f02579831e9": (
        "C",
        "L",
        47,
        make(
            [
                ("A", "E", "R"),
                ("A", "E", "C"),
                ("A", "B", "R"),
                ("A", "B", "L"),
                ("B", "E", "R"),
            ]
        ),
    ),
    "lh148-9e140322bfd33a22": (
        "L",
        "C",
        39,
        make(
            [
                ("A", "E", "R"),
                ("A", "E", "L"),
                ("A", "B", "R"),
                ("A", "B", "C"),
                ("B", "E", "R"),
            ]
        ),
    ),
    "lh148-a1e6c042c7d77e41": (
        "L",
        "L",
        35,
        make(
            [
                ("A", "E", "R"),
                ("A", "E", "L"),
                ("A", "B", "R"),
                ("A", "B", "L"),
                ("B", "E", "R"),
            ]
        ),
    ),
}

targets = {
    35: make(
        [
            ("A", "E", "R"),
            ("A", "E", "L"),
            ("A", "B", "R"),
            ("B", "E", "L"),
        ]
    ),
    39: make(
        [
            ("A", "E", "R"),
            ("A", "E", "L"),
            ("A", "B", "R"),
            ("B", "E", "C"),
        ]
    ),
    43: make(
        [
            ("A", "E", "R"),
            ("A", "E", "C"),
            ("A", "B", "R"),
            ("B", "E", "C"),
        ]
    ),
    47: make(
        [
            ("A", "E", "R"),
            ("A", "E", "C"),
            ("A", "B", "R"),
            ("B", "E", "L"),
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
    if uncoloured_signature(network) == uncoloured_signature(graph_ld):
        matches.append(row)

assert len(matches) == 4, [row["catalogue_id"] for row in matches]
assert {row["catalogue_id"] for row in matches} == set(fixtures)
assert {row["source_support_id"] for row in matches} == {
    "support-9defcf048b659b39"
}
assert all(row["generated_source_candidates"] == 2 for row in matches)
assert all(row["distinct_representative_forms"] == 1 for row in matches)

print("five-element records", len(five_element))
print("graph-L-dual candidates", len(matches))
print("uncoloured signature", uncoloured_signature(graph_ld))
for row in matches:
    composition = f"R{row['r']}L{row['l']}C{row['c']}"
    print(
        row["catalogue_id"],
        composition,
        row["representative_descriptor"],
        row["source_support_id"],
        row["source_assignment_id"],
        row["generated_source_candidates"],
        row["distinct_representative_forms"],
    )

assert Counter((row["r"], row["l"], row["c"]) for row in matches) == {
    (3, 0, 2): 1,
    (3, 1, 1): 2,
    (3, 2, 0): 1,
}

by_id = {row["catalogue_id"]: row for row in matches}
parameters = {
    "lh148-5d5fb848a810c9cb": (2, 3, 5, 7, 11),
    "lh148-534a4f02579831e9": (3, 4, 7, 5, 13),
    "lh148-9e140322bfd33a22": (5, 2, 9, 4, 7),
    "lh148-a1e6c042c7d77e41": (7, 6, 11, 3, 5),
}
impedances = (
    (Fraction(1), Fraction(2)),
    (Fraction(2), Fraction(5)),
    (Fraction(5, 3), Fraction(7, 2)),
    (Fraction(11, 4), Fraction(13, 5)),
    (Fraction(17, 6), Fraction(19, 7)),
)

for catalogue_id, (direct, transformed_arm, target, fixture) in fixtures.items():
    row = by_id[catalogue_id]
    record = network_from_descriptor(row["representative_descriptor"])
    assert canonical_structural_signature(record) == (
        canonical_structural_signature(fixture)
    ), catalogue_id

    reduced = make(
        [
            ("A", "E", direct),
            ("A", "E", "R"),
            ("A", "B", "R"),
            ("B", "E", transformed_arm),
        ]
    )
    assert canonical_structural_signature(reduced) == (
        canonical_structural_signature(targets[target])
    ), (catalogue_id, target)

    d, r, a, b, c = map(Fraction, parameters[catalogue_id])
    a_prime = a * (a + b) / b
    b_prime = a + b
    c_prime = c * ((a + b) / b) ** 2
    merged = parallel(r, b_prime)

    # Verify the printed inverse coefficient map exactly.
    assert a_prime * b_prime / (a_prime + b_prime) == a
    assert b_prime**2 / (a_prime + b_prime) == b
    assert c_prime * (b_prime / (a_prime + b_prime)) ** 2 == c

    coefficients = (d, r, a, b, c, a_prime, b_prime, c_prime, merged)
    assert all(value > 0 and value.denominator > 0 for value in coefficients)

    for direct_z, arm_z in impedances:
        left_affected = a + parallel(b, c * arm_z)
        right_affected = parallel(b_prime, a_prime + c_prime * arm_z)
        assert left_affected == right_affected

        original = parallel(d * direct_z, r, left_affected)
        transformed = parallel(
            d * direct_z,
            r,
            b_prime,
            a_prime + c_prime * arm_z,
        )
        reduced_impedance = parallel(
            d * direct_z,
            merged,
            a_prime + c_prime * arm_z,
        )
        assert original == transformed == reduced_impedance

    print(
        f"{catalogue_id} -> canonical network {target}: "
        "coloured structural and exact Zobel checks OK"
    )

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
assert all(
    row["basic_graph_assignment"] is None for row in production["records"]
)
assert all(not row["historical_identifiers"] for row in production["records"])
assert all(
    (
        next(
        row for row in production["records"] if row["catalogue_id"] == cid
        )["comparison_status"],
        next(
            row
            for row in production["records"]
            if row["catalogue_id"] == cid
        )["proposed_disposition"],
    )
    == ("derived-structural-match", "exclude")
    for cid in fixtures
)
print("production: 22 excluded / 126 unresolved / 0 retained")
PY
```

Observed deterministic output (apart from the absolute PDF path printed by
`sha256sum`) was:

```text
29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8  ../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
five-element records 85
graph-L-dual candidates 4
uncoloured signature StructuralSignature(relation='colour-preserving-port-augmented-cycle-matroid-v1', multiplicities=(5, 0, 0, 1), cycle_space=(0, 3, 12, 15, 21, 22, 25, 26, 33, 34, 45, 46, 52, 55, 56, 59))
lh148-5d5fb848a810c9cb R3L0C2 0-1:C;0-1:R;0-2:C;0-2:R;1-2:R support-9defcf048b659b39 assignment-35f8245d83d39490 2 1
lh148-534a4f02579831e9 R3L1C1 0-1:C;0-1:R;0-2:L;0-2:R;1-2:R support-9defcf048b659b39 assignment-42e40d250a1a7ddd 2 1
lh148-9e140322bfd33a22 R3L1C1 0-1:L;0-1:R;0-2:C;0-2:R;1-2:R support-9defcf048b659b39 assignment-0899751a9aa9a891 2 1
lh148-a1e6c042c7d77e41 R3L2C0 0-1:L;0-1:R;0-2:L;0-2:R;1-2:R support-9defcf048b659b39 assignment-61adb58aab8b8553 2 1
lh148-5d5fb848a810c9cb -> canonical network 43: coloured structural and exact Zobel checks OK
lh148-534a4f02579831e9 -> canonical network 47: coloured structural and exact Zobel checks OK
lh148-9e140322bfd33a22 -> canonical network 39: coloured structural and exact Zobel checks OK
lh148-a1e6c042c7d77e41 -> canonical network 35: coloured structural and exact Zobel checks OK
production: 22 excluded / 126 unresolved / 0 retained
```

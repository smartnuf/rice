# Evidence for the graph-M five-element Zobel exclusion

## 1. Purpose and scope

This report investigates only the single five-element series-parallel network
with Morelli and Smith basic graph `M` that Section 5.1 says is removed by a
Zobel transformation to canonical network #72. It independently transcribes
the source and target diagrams, performs the complete RICE graph-`M` census
under `colour-preserving-port-augmented-cycle-matroid-v1`, checks the unique
coloured correspondence, and verifies the Zobel reduction symbolically and
with exact arithmetic.

This report was originally prepared as evidence-only and did not itself change
production, assign a graph or historical identity to the RICE record, or claim
to reproduce the canonical 108-network catalogue. The production update
containing this revision applies the graph-`M` mapping through the version 3
subject-bound evidence route. With that update, the ledger has 17 excluded, 131
unresolved, and 0 retained records.

The publication states the graph family, population one, transformation class,
and target. It does not print a RICE catalogue ID. The individual RICE-ID
correspondence below is therefore independently reproduced and checked rather
than individually source-stated.

## 2. Authoritative source statements

Morelli and Smith, Section 5.1, states within the twenty five-element
series-parallel Zobel exclusions that one network with graph structure `M`
reduces to network #72. This is an aggregate source-stated one-member graph
family claim; it establishes the family, count, exclusion mechanism, and target,
but not a RICE identifier.

Appendix B reports exactly one graph-`M` five-element assignment. It appears in
the `3R-LC` column in parentheses, the total is one, and the canonical total is
zero. Thus the source independently fixes the excluded assignment's component
composition as `3R-LC`.

On the same rendered Appendix B page, graph `H` has one four-element assignment,
in the `2R-LC` column, with canonical total one and sole network number #72.
Appendix C then draws network #72 as a resistor branch in parallel with a
three-element series branch containing a resistor, an inductor, and a
capacitor.

Section 5.3.1 states that the two Figure 5.2 networks are equivalent for any two
impedances `Z1` and `Z2` when the printed coefficient relations hold. It also
states that positive finite coefficients transform to positive finite
coefficients in either direction.

## 3. Source locators and inspected copy

The authoritative source is A. Morelli and M. C. Smith, *Passive Network
Synthesis: An Approach to Classification* (2019). The inspected local copy was:

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Precise locator | Inspection |
|---|---|---|
| One graph-`M` exclusion reducing to #72 | Section 5.1, printed p. 42, zero-based PDF index 48 | Extracted text and rendered page |
| Zobel topology, coefficient relations, and positivity | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Graph `M`, its five-element row, graph `H`, and its four-element row | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Circuit diagram for canonical network #72 | Appendix C, printed p. 132, PDF index 138 | Extracted text and rendered page |

Every graph and circuit topology in this report was transcribed from a rendered
page, not inferred from extracted text. No PDF, rendering, extracted text, OCR
output, or source image is committed.

## 4. Independent graph-M transcription

The rendered Appendix B graph-`M` diagram gives the following normalized
two-terminal graph:

```text
vertices:      A, B, C, D, E
terminals:     {A, E}
edges:         AB, BC, CD, DE, BE
parallel edges: none
```

Equivalently, it is the terminal path `A--B--C--D--E` plus the upper chord
`B--E`:

```text
AB -- (BE || (BC -- CD -- DE)).
```

The chord is `BE`, not `AE`. The normalized vertex names are introduced here
only to make the transcription reconstructible. The source is Appendix B,
printed p. 126 / PDF index 132.

## 5. Independent graph-H and canonical network 72 transcription

The rendered graph-`H` diagram on the same Appendix B page normalizes to:

```text
vertices:      A, B, C, D
terminals:     {A, D}
edges:         AD, AB, BC, CD
parallel edges: none
```

Its series-parallel expression is:

```text
AD || (AB -- BC -- CD).
```

Appendix B assigns the sole `2R-LC` graph-`H` network the number #72. The
rendered Appendix C drawing labels the direct upper branch `R2` and the lower
three-element series branch, from left to right, `R1`, `L1`, `C1`. Its faithful
normalized coloured fixture is therefore:

```text
R2 || (R1 -- L1 -- C1).
```

Series interchange permits an equivalent order along the lower branch, but the
fixture used below retains the source drawing's order. Canonical network #72 is
a reduction destination, not the historical identity of the excluded
five-element RICE record.

## 6. Complete 85-record initial candidate census

The committed `data/counts/ladenheim-148.json` catalogue contains exactly 85
records with `rlc == 5`. For every one, the reproduction temporarily recolours
all five real edges `R`, while the artificial port edge and unordered terminal
pair remain part of the signature. Comparison with the independently
transcribed graph-`M` fixture yields exactly one match:

| RICE catalogue ID | Composition | Representative descriptor | Support | Source assignment |
|---|---:|---|---|---|
| `lh148-045c192be4de396d` | `R3L1C1` | `0-2:C;0-3:R;1-3:R;2-4:L;3-4:R` | `support-054451b74652a492` | `assignment-9f4eeb66bbfb8290` |

The normalized uncoloured fixture signature is:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(5, 0, 0, 1),
  cycle_space=(0, 15, 49, 62)
)
```

The record itself commits the same relation and records six generated source
candidates and six distinct representative forms in this structural class. At
the time of the evidence-only reproduction, the production row was
`unresolved`; the production update containing this revision changes it to a
derived structural exclusion while retaining a null `basic_graph_assignment`
and an empty historical-identifier list.

## 7. Structural matching method

The reproduction uses the existing public APIs `PrimitiveNetwork`,
`PrimitiveEdge`, `network_from_descriptor`, and
`canonical_structural_signature`. It does not compare descriptor strings or
introduce another isomorphism implementation.

The broad census compares the complete port-augmented cycle-matroid signature
after temporary recolouring. The final checks retain the R/L/C colours. In both
cases the asserted relation is exactly:

```text
colour-preserving-port-augmented-cycle-matroid-v1
```

This relation preserves the artificial port colour and handles the deformation,
separation, and series-interchange equivalences used by the structural
catalogue.

## 8. Unique candidate and composition

The census result agrees with both source constraints without using them as a
filter: there is one graph-`M` structural match, and it is `R3L1C1`. The unique
record is:

```text
catalogue ID:              lh148-045c192be4de396d
representative descriptor: 0-2:C;0-3:R;1-3:R;2-4:L;3-4:R
component counts:          R3L1C1, rlc=5
source support ID:         support-054451b74652a492
source assignment ID:      assignment-9f4eeb66bbfb8290
committed coloured signature:
  colour-preserving-port-augmented-cycle-matroid-v1|R3L1C1P1|0,1b,25,3e
```

The catalogue ID and descriptor are independently reproduced RICE facts, not
identifiers printed by Morelli and Smith.

## 9. Coloured candidate fixture

A separately constructed coloured fixture on the transcribed graph-`M` edges
uses:

```text
AB:R
BE:R
BC:R
CD:L
DE:C
```

Its topology is:

```text
R -- (R || (R -- L -- C)).
```

The candidate and fixture have the identical unrecoloured signature:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(3, 1, 1, 1),
  cycle_space=(0, 27, 37, 62)
)
```

Series interchange makes the order of the `R`, `L`, and `C` edges within the
three-edge path immaterial under the committed relation. This match establishes
the actual unique coloured class before the Zobel algebra is applied; the
placement was not selected merely because it makes the reduction work.

## 10. Candidate-to-target conclusion

| RICE catalogue ID | Composition | Proposed target | Source support | Structural match | Zobel derivation | Overall status |
|---|---:|---:|---|---|---|---|
| `lh148-045c192be4de396d` | `3R-LC` | #72 | aggregate source-stated | exact coloured graph-`M` and graph-`H` signatures | exact Figure 5.2 substitution plus resistor merge | `independently-checked` |

Morelli and Smith directly state the one-member graph-`M` exclusion and target.
Appendix B independently fixes its composition column. The RICE-ID
correspondence is computed under the committed structural relation, and the
candidate-to-target mapping is independently checked below. It is not an
individual source-stated RICE mapping.

## 11. Full Zobel coefficient derivation

Let `Z1 = R` be a resistor impedance basis and let the complete composite
one-port

```text
W = rho R -- lambda L -- kappa C
```

denote the graph-`M` three-element series path. Here `rho`, `lambda`, and
`kappa` represent positive finite element parameters in impedance form. Write
the candidate in the left-hand Figure 5.2 form:

```text
a R -- (b R || c W),
```

where `a`, `b`, and `c` are positive and finite. The coefficient `c` can be
absorbed into the chosen `W`; retaining it makes the published map explicit.
Use `Z1=R` and `Z2=W` in Figure 5.2.

Solving from the unprimed coefficients gives:

```text
b' = a + b
a' = a(a + b)/b
c' = c((a + b)/b)^2.
```

Substitution into the reverse printed relations gives:

```text
a'b'/(a'+b')
  = [a(a+b)/b](a+b) / ([a(a+b)/b] + a+b)
  = a,

(b')^2/(a'+b')
  = (a+b)^2 / ([a(a+b)/b] + a+b)
  = b,

c'(b'/(a'+b'))^2
  = c((a+b)/b)^2 [b/(a+b)]^2
  = c.
```

Thus Figure 5.2 transforms the graph-`M` candidate exactly to:

```text
b' R || (a' R -- c' W).
```

This is one Zobel step acting on the resistor impedance `R` and the entire
composite one-port `W`; it is not three separate transformations on the
elements inside `W`.

## 12. Resistor merge and target structural match

Scaling `W` by `c'` scales all three series element impedances. The transformed
lower branch is therefore:

```text
a' R -- c' rho R -- c' lambda L -- c' kappa C.
```

Series interchange can place the two resistor impedances adjacently. Their
ordinary same-kind series merge gives:

```text
(a' + c' rho) R -- c' lambda L -- c' kappa C.
```

The complete transformed topology is consequently:

```text
b' R || ((a' + c' rho) R -- c' lambda L -- c' kappa C),
```

which is `R || (R -- L -- C)`. A separately constructed transformed fixture has
the exact same coloured structural signature as the faithfully transcribed
canonical network #72 fixture:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(2, 1, 1, 1),
  cycle_space=(0, 15, 17, 30)
)
```

Because `a`, `b`, and `c` are positive finite, `a+b` and `b` are positive
finite, so `a'`, `b'`, and `c'` are positive finite. The merged resistor
coefficient `a'+c'rho` and the scaled inductor coefficient `c'lambda` are also
positive finite. Scaling a capacitor impedance by `c'` corresponds to dividing
its positive finite capacitance by `c'`, so the resulting capacitor value is
likewise positive and finite.

The element-count reduction comes only from the same-kind resistor merge after
the Zobel step. Series interchange is structural equivalence, not an additional
network-synthesis claim. No frequency inversion, duality, terminal reversal,
second Zobel step, or unstated source assumption is needed.

## 13. Exact-arithmetic corroboration

For impedance values, define `p(x,y)=xy/(x+y)`. The two Figure 5.2 sides are:

```text
left  = a + p(b, c W)
right = p(b', a' + c' W).
```

The reproduction block uses four distinct positive rational `(a,b,c)` tuples.
For each tuple it computes the primed coefficients as `Fraction` objects,
checks both directions of the published coefficient map, asserts positivity,
and verifies exact impedance equality at four positive rational values of `W`.
All 16 substitutions pass exactly.

These finite substitutions corroborate the symbolic identity; they are not
presented as its proof. The symbolic substitution and topology argument in
Sections 11-12 remain the principal derivation.

## 14. Provenance distinctions

The evidence hierarchy used here is:

1. rendered diagrams and text in Morelli and Smith for the historical claims,
   graph definitions, and target circuit;
2. the committed RICE catalogue and public structural-signature APIs for the
   candidate census and coloured correspondence;
3. the independently reproduced symbolic and exact-arithmetic Zobel checks;
4. sibling-workspace material only as a non-authoritative cross-check.

A bounded sibling audit was performed only after the PDF and RICE results were
independently established. Clean repository `../network-theory` at commit
`87b831831c154c5c3675853a99ff7e5a2b7dfb6d` contains
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/analysis-of-basic-graphs.md`
and `016--graph-generation/generated_graphs/ladenheim/graph_M`; they describe
the same `AB,BC,CD,DE,BE` graph and therefore agree with the transcription.
That agreement supplied no historical authority or RICE mapping. Bounded
searches of clean `../pynntt` at
`f3db06032cbe23d583d77f6cb79d21ced90d7651` and clean `../pynntt_lab` at
`1ddd90034da4594bb6a3728b0700918883fd1172` supplied no candidate or target
mapping used as evidence. The PDF's location in `pynntt_lab` does not make that
repository's analysis authoritative.

## 15. Remaining uncertainties

No alternative graph-`M` candidate, coloured placement, or target ambiguity
remains under the transcribed diagrams and committed structural relation. The
publication still does not print the individual RICE-ID correspondence, so that
correspondence remains an independently checked computational conclusion rather
than a historical quotation.

This report does not investigate graph `M`-dual, graph `S`, graph `S`-dual, or
any other family. The production update containing this revision applies the
graph-`M` exclusion through the complete version 3 subject-bound route. The
ledger now has 17 excluded, 131 unresolved, and 0 retained; fifteen other
five-element Zobel exclusions and eight final exclusions remain unresolved.
Canonical network #72 remains a reduction target rather than a historical
identity of the excluded record.

## 16. Complete runnable reproduction commands

The block and observed output below are preserved from the original
evidence-only report. Run the complete block at evidence-report commit
`46f009b99001a75dea4147312ee299d5aa036395`; its final production-boundary
assertions intentionally record the then-unresolved row. On this production
update, the structural census, signature, and exact-arithmetic portions remain
unchanged, while the row is now the derived exclusion described above.

Run this paste-ready block from the RICE repository root at that commit:

```bash
sha256sum \
  ../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf

.venv/bin/python - <<'PY'
import json
from fractions import Fraction
from pathlib import Path

from rice.ladenheim import (
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    network_from_descriptor,
)

RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"
EXPECTED_ID = "lh148-045c192be4de396d"


def make(terminals, edges):
    return PrimitiveNetwork(
        terminals,
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def uncoloured(network):
    return PrimitiveNetwork(
        network.terminals,
        tuple(PrimitiveEdge(edge.u, edge.v, "R") for edge in network.edges),
    )


def signature(network):
    result = canonical_structural_signature(network)
    assert result.relation == RELATION
    return result


def parallel(left, right):
    return left * right / (left + right)


catalogue = json.loads(Path("data/counts/ladenheim-148.json").read_text())
ledger = json.loads(
    Path("data/comparisons/ladenheim-148-to-108.json").read_text()
)
five = [record for record in catalogue["records"] if record["rlc"] == 5]
assert len(five) == 85

graph_m = make(
    ("A", "E"),
    [
        ("A", "B", "R"),
        ("B", "C", "R"),
        ("C", "D", "R"),
        ("D", "E", "R"),
        ("B", "E", "R"),
    ],
)
graph_m_signature = signature(graph_m)
matches = []
for record in five:
    network = network_from_descriptor(record["representative_descriptor"])
    if signature(uncoloured(network)) == graph_m_signature:
        matches.append(record)

assert len(matches) == 1
candidate = matches[0]
assert candidate["catalogue_id"] == EXPECTED_ID
assert (
    candidate["r"],
    candidate["l"],
    candidate["c"],
    candidate["rlc"],
) == (3, 1, 1, 5)
assert candidate["relation"] == RELATION

row = next(
    record for record in ledger["records"]
    if record["catalogue_id"] == EXPECTED_ID
)
assert row["comparison_status"] == "unresolved"
assert row["proposed_disposition"] == "unresolved"
assert row["basic_graph_assignment"] is None
assert row["historical_identifiers"] == []

candidate_network = network_from_descriptor(candidate["representative_descriptor"])
coloured_graph_m = make(
    ("A", "E"),
    [
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("B", "C", "R"),
        ("C", "D", "L"),
        ("D", "E", "C"),
    ],
)
assert signature(candidate_network) == signature(coloured_graph_m)

target_72 = make(
    ("A", "D"),
    [
        ("A", "D", "R"),
        ("A", "B", "R"),
        ("B", "C", "L"),
        ("C", "D", "C"),
    ],
)
transformed_and_merged = make(
    ("s", "t"),
    [
        ("s", "t", "R"),
        ("s", "u", "C"),
        ("u", "v", "R"),
        ("v", "t", "L"),
    ],
)
assert signature(transformed_and_merged) == signature(target_72)

parameter_sets = [
    (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)),
    (Fraction(4, 3), Fraction(5, 7), Fraction(7, 4)),
    (Fraction(9, 5), Fraction(11, 6), Fraction(13, 8)),
    (Fraction(17, 9), Fraction(19, 10), Fraction(23, 11)),
]
w_values = [
    Fraction(1, 3),
    Fraction(2, 1),
    Fraction(7, 4),
    Fraction(11, 5),
]
for a, b, c in parameter_sets:
    a_prime = a * (a + b) / b
    b_prime = a + b
    c_prime = c * ((a + b) / b) ** 2
    assert all(
        value > 0
        for value in (a, b, c, a_prime, b_prime, c_prime)
    )
    assert a == a_prime * b_prime / (a_prime + b_prime)
    assert b == b_prime**2 / (a_prime + b_prime)
    assert c == c_prime * (b_prime / (a_prime + b_prime)) ** 2
    for w in w_values:
        left = a + parallel(b, c * w)
        right = parallel(b_prime, a_prime + c_prime * w)
        assert left == right

print("five-element records: 85")
print("graph-M candidates: 1")
print(
    "candidate:",
    candidate["catalogue_id"],
    f"R{candidate['r']}L{candidate['l']}C{candidate['c']}",
    candidate["representative_descriptor"],
)
print(
    "support:",
    candidate["source_support_id"],
    candidate["source_assignment_id"],
)
print("uncoloured signature:", graph_m_signature)
print("coloured graph-M signature: pass")
print("canonical network 72 target signature: pass")
print("exact Zobel checks: 4 parameter tuples x 4 W values pass")
print("production row remains unresolved with null graph and empty identifiers")
PY
```

Observed output (following the SHA-256 line) was:

```text
five-element records: 85
graph-M candidates: 1
candidate: lh148-045c192be4de396d R3L1C1 0-2:C;0-3:R;1-3:R;2-4:L;3-4:R
support: support-054451b74652a492 assignment-9f4eeb66bbfb8290
uncoloured signature: StructuralSignature(relation='colour-preserving-port-augmented-cycle-matroid-v1', multiplicities=(5, 0, 0, 1), cycle_space=(0, 15, 49, 62))
coloured graph-M signature: pass
canonical network 72 target signature: pass
exact Zobel checks: 4 parameter tuples x 4 W values pass
production row remains unresolved with null graph and empty identifiers
```

# Evidence for the graph-M-dual five-element Zobel exclusion

## 1. Purpose and strict scope

This report investigates only the single five-element network with Morelli and
Smith basic graph `M^d` (called graph M-dual here) that Section 5.1 says reduces
by a Zobel transformation to canonical network 73. It transcribes the rendered
source diagrams, searches all 85 five-element RICE records under the committed
structural relation, and checks the resulting coloured topology and reduction.

This report was originally prepared as evidence only and did not itself update
the production ledger, assign a basic graph or historical identity, reproduce
the canonical 108 catalogue, or make a claim about another family. The
production update containing this revision applies the reviewed mapping through
the complete version 3 subject-bound route. With that update, production has 18
excluded, 130 unresolved, and 0 retained.

## 2. Authoritative statements and production baseline

Morelli and Smith Section 5.1 states, as part of the twenty five-element
series-parallel Zobel exclusions, that one graph-`M^d` network reduces to
canonical network 73. Appendix B reports one graph-`M^d` five-element
assignment, in the `3R-LC` column, with canonical total zero. The source does
not print a RICE catalogue ID or descriptor.

Appendix B separately reports one graph-`H^d` four-element `2R-LC` assignment,
with canonical total one and network number 73. Appendix C draws that network.
Thus the publication establishes the graph family, population, composition,
exclusion mechanism, and target; the RICE correspondence remains an
independently reproduced conclusion.

The committed production ledger when this evidence investigation was prepared
had:

```text
excluded:   17
unresolved: 131
retained:    0
```

The production update containing this revision changes only this subject's
status and disposition. All production `basic_graph_assignment` values remain
null and all historical identifier lists remain empty.

## 3. Source identity, checksum, and locators

The authoritative source is A. Morelli and M. C. Smith, *Passive Network
Synthesis: An Approach to Classification* (2019). The actual inspected copy is:

```text
../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf
SHA-256 29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8
```

| Evidence | Precise locator | Inspection |
|---|---|---|
| One graph-`M^d` exclusion reducing to canonical network 73 | Section 5.1, printed p. 42, zero-based PDF index 48 | Extracted text and rendered page |
| Zobel topology, coefficient maps, and positivity | Section 5.3.1 and Figure 5.2, printed p. 46, PDF index 52 | Extracted text and rendered page |
| Graph `H^d`, its `2R-LC` row, and network number 73 | Appendix B, printed p. 126, PDF index 132 | Extracted text and rendered page |
| Graph `M^d` and its one-member `3R-LC` row | Appendix B, printed p. 127, PDF index 133 | Extracted text and rendered page |
| Circuit diagram for canonical network 73 | Appendix C, printed p. 133, PDF index 139 | Extracted text and rendered page |

Every topology below was transcribed from a rendered page. Extracted text was
used only for prose and table location. No PDF-derived artefact is committed.

## 4. Visual transcription of graph M-dual

The rendered graph-`M^d` row in Appendix B normalizes to:

```text
vertices:      A, B, E
terminals:     {A, E}
edges:         AE, AB, BE_1, BE_2, BE_3
parallel edges: BE_1, BE_2, BE_3
```

Equivalently:

```text
AE || (AB -- (BE_1 || BE_2 || BE_3)).
```

The three `B--E` branches are distinct edges and are never collapsed during
matching. The direct edge is between the terminals `A` and `E`.

## 5. Visual transcription of graph H-dual

The rendered graph-`H^d` row on printed page 126 normalizes to:

```text
vertices:      A, B, E
terminals:     {A, E}
edges:         AB, BE_1, BE_2, BE_3
parallel edges: BE_1, BE_2, BE_3
```

Its expression is:

```text
AB -- (BE_1 || BE_2 || BE_3).
```

Appendix B assigns its sole `2R-LC` canonical assignment network number 73.

## 6. Visual transcription of canonical network 73

The Appendix C drawing has a left series resistor `R2`, followed by three
branches `R1`, `L1`, and `C1` in parallel. Its faithful coloured topology is:

```text
R2 -- (R1 || L1 || C1).
```

This is the coloured graph-`H^d` fixture. Canonical network 73 is used only as a
reduction destination, not as a historical identity of the five-element RICE
record.

## 7. Complete 85-record census

The reproduction loads `data/counts/ladenheim-148.json` and selects every row
with `rlc == 5`, yielding 85 records. Each real edge is temporarily recoloured
`R`; the artificial port edge and unordered terminals remain in the signature.
The comparison uses exactly:

```text
colour-preserving-port-augmented-cycle-matroid-v1
```

The uncoloured graph-`M^d` fixture has signature:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(5, 0, 0, 1),
  cycle_space=(0, 3, 5, 6, 25, 26, 28, 31,
               40, 43, 45, 46, 49, 50, 52, 55)
)
```

Exactly one of the 85 records matches. Reconstructing the same multigraph with
new internal labels and reversing the terminal tuple leaves the signature
unchanged. The census therefore does not depend on descriptor order, vertex
names, terminal direction, a presumed dual catalogue ID, or a sibling label.

## 8. Discovered RICE candidate

| Field | Independently reproduced value |
|---|---|
| Catalogue ID | `lh148-635770ede187bca9` |
| Representative descriptor | `0-1:R;0-2:C;0-2:L;0-2:R;1-2:R` |
| Composition | `R3L1C1` (`3R-LC`) |
| Source support | `support-9defcf048b659b39` |
| Source assignment | `assignment-1934f83e66920323` |
| Generated source candidates | 2 |
| Distinct representative forms | 1 |
| Source support edges | 3 |

The committed coloured signature string is:

```text
colour-preserving-port-augmented-cycle-matroid-v1|R3L1C1P1|0,7,9,e,11,16,18,1f,22,25,2b,2c,33,34,3a,3d
```

The record was found by the complete uncoloured census. It was not obtained by
dualizing the graph-`M` catalogue ID or by comparing descriptor strings.

## 9. Uncoloured structural proof

`PrimitiveNetwork` preserves the three parallel `B--E` primitive edges.
`canonical_structural_signature` then compares the complete port-augmented
cycle matroid. The sole candidate and the independent graph fixture have the
same uncoloured signature printed in Section 7, while all other 84
five-element records differ. Separate assertions verify internal relabelling
and terminal reversal.

## 10. Coloured placement proof

Appendix B fixes the sole graph-`M^d` assignment as `3R-LC`. In the independently
constructed coloured fixture the edges are:

```text
AE:R
AB:R
BE_1:R
BE_2:L
BE_3:C
```

or, equivalently:

```text
R || (R -- (R || L || C)).
```

Interchanging the three parallel `B--E` branches does not change the network.
Putting two same-kind elements there would be a trivially reducible parallel
pair and would not have the required `3R-LC` population. More importantly, the
actual catalogue record is checked directly against this separately built
fixture with colours retained. Both have:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(3, 1, 1, 1),
  cycle_space=(0, 7, 9, 14, 17, 22, 24, 31,
               34, 37, 43, 44, 51, 52, 58, 61)
)
```

Thus the placement is established from the RICE record rather than selected to
make the later algebra work.

## 11. Target-fixture proof

A separate coloured graph-`H^d` fixture and a separate canonical-network-73
fixture both represent `R -- (R || L || C)`. Their exact signature is:

```text
StructuralSignature(
  relation='colour-preserving-port-augmented-cycle-matroid-v1',
  multiplicities=(2, 1, 1, 1),
  cycle_space=(0, 5, 9, 12, 19, 22, 26, 31)
)
```

This independently connects the Appendix C target drawing to the Appendix B
graph-`H^d` row and composition.

## 12. Derivation of the dual Zobel map

Figure 5.2 prints the series/parallel identity. For the required dual topology,
normalize the resistor basis to one and write the arbitrary impedance ratio as
`x = W/R`. The two candidate impedances are:

```text
Z_left/R  = a || (b + cx)
          = a(b + cx)/(a + b + cx),

Z_right/R = b' + (a' || c'x)
          = b' + a'c'x/(a' + c'x).
```

Equating coefficients of `1`, `x`, and `x^2` after cross multiplication gives
the forward map:

```text
a' = a^2/(a + b)
b' = ab/(a + b)
c' = c(a/(a + b))^2.
```

Indeed `a' + b' = a`. Solving the same equations for the unprimed coefficients
gives the inverse map:

```text
a = a' + b'
b = b'(a' + b')/a'
c = c'((a' + b')/a')^2.
```

Substitution gives `a' + b' = a`, recovers `b` from
`b' = ab/(a+b)`, and recovers `c` from
`c' = c(a/(a+b))^2`; substituting the inverse into the forward equations gives
the converse. Hence, for an arbitrary one-port `W`,

```text
aR || (bR -- cW)  ==  b'R -- (a'R || c'W).
```

This is a direct impedance derivation of the parallel/series dual, not an
unchecked copy of the graph-`M` coefficient map.

## 13. Forward and inverse positivity

If `a`, `b`, and `c` are positive and finite, then `a+b` is positive and finite,
so every numerator and denominator in the forward map is positive and finite.
Thus `a'`, `b'`, and `c'` are strictly positive and finite.

Conversely, if `a'`, `b'`, and `c'` are positive and finite, then `a'+b'` and
`a'` are positive and finite. Every inverse expression is therefore strictly
positive and finite. There is no exceptional positive case, zero denominator,
or one-way restriction in the claimed domain.

## 14. Resistor parallel merge and reduction

Instantiate the arbitrary one-port as the complete parallel subnetwork

```text
W = rho R || lambda L || kappa C,
```

with positive finite element impedances. The graph-`M^d` candidate is the left
side `aR || (bR -- cW)`. The dual Zobel map produces:

```text
b'R -- (a'R || c'(rho R || lambda L || kappa C)).
```

Scaling `W` scales each branch impedance and preserves its component type. The
`a'R` branch is parallel with the `c'rho R` branch, so the ordinary same-kind
parallel merge gives the positive finite resistor

```text
(a' c' rho)/(a' + c' rho) R.
```

The resulting four-element topology is:

```text
R -- (R || L || C),
```

whose coloured signature is exactly the graph-`H^d` and canonical-network-73
signature in Section 11. The Zobel equivalence and the later resistor merge are
separate steps.

## 15. Exact-arithmetic corroboration

The reproduction uses `fractions.Fraction` for four nontrivial positive
coefficient tuples and five positive rational values of `W/R`. It checks the
two rational impedances for exact equality, checks that the inverse recovers
every input exactly, repeats forward recovery from the primed side, and asserts
positivity throughout. These finite substitutions corroborate, but do not
replace, the coefficient comparison and symbolic identity above.

## 16. Sibling-workspace audit

The following clean, read-only sibling commits were inspected after the PDF and
RICE derivations were complete:

| Repository and commit | Path inspected | Result and limitation |
|---|---|---|
| `../network-theory` at `87b831831c154c5c3675853a99ff7e5a2b7dfb6d` | `016--graph-generation/generated_graphs/ladenheim/graph_Md` and `comparison.md`; generator relationship in `src/gen_ladenheim_graphs.py` | Its three-vertex multigraph agrees with the independent graph-`M^d` transcription. It supplied no RICE ID, target allocation, or historical authority. |
| `../pynntt` at `f3db06032cbe23d583d77f6cb79d21ced90d7651` | bounded text search | No relevant graph-`M^d` or network-73 lead was used. |
| `../pynntt_lab` at `1ddd90034da4594bb6a3728b0700918883fd1172` | the external PDF path above; bounded non-PDF text search | The repository merely hosts the inspected source copy; no workspace mapping or descriptor was used. |

All three siblings remained clean and were not modified. Agreement in
`network-theory` is only a cross-check; the rendered publication and independent
RICE computation establish the conclusions.

## 17. Evidential conclusions and limitations

The evidence independently establishes exactly one RICE structural subject for
the source-stated graph-`M^d` exclusion:

| RICE catalogue ID | Composition | Reduction target | Source support | Structural check | Zobel check | Status |
|---|---:|---:|---|---|---|---|
| `lh148-635770ede187bca9` | `3R-LC` | canonical network 73 | aggregate source-stated one-member family | exact uncoloured and coloured signatures | derived dual map, exact arithmetic, resistor merge | `independently-checked` |

The candidate topology is `R || (R -- (R || L || C))`; the checked dual Zobel
transformation and resistor merge produce `R -- (R || L || C)`, matching
canonical network 73. The publication does not print the RICE ID, so the
individual correspondence is independently reproduced rather than individually
source-stated. Duality informed the identity to derive but did not select or
prove the catalogue subject.

The production update containing this revision applies this mapping through the
complete version 3 route. The target number is not a historical identity, no
graph assignment is populated, and no conclusion is made about another family
or the eight final exclusions. Fourteen five-element Zobel exclusions remain
unapplied.

## 18. Complete reproduction commands and observed output

Run this paste-ready block from the RICE repository root on a revision
containing the graph-`M^d` production application. Its production checks are
intentionally subject-level, so later applications do not invalidate it:

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
EXPECTED_ID = "lh148-635770ede187bca9"
EXPECTED_DESCRIPTOR = "0-1:R;0-2:C;0-2:L;0-2:R;1-2:R"


def make(terminals, edges):
    return PrimitiveNetwork(
        terminals,
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def uncoloured(network):
    return make(
        network.terminals,
        [(edge.u, edge.v, "R") for edge in network.edges],
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

graph_md = make(
    ("A", "E"),
    [
        ("A", "E", "R"),
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("B", "E", "R"),
        ("B", "E", "R"),
    ],
)
graph_md_signature = signature(graph_md)
matches = []
for record in five:
    network = network_from_descriptor(record["representative_descriptor"])
    if signature(uncoloured(network)) == graph_md_signature:
        matches.append(record)

assert len(matches) == 1
candidate = matches[0]
assert candidate["catalogue_id"] == EXPECTED_ID
assert candidate["representative_descriptor"] == EXPECTED_DESCRIPTOR
assert (candidate["r"], candidate["l"], candidate["c"]) == (3, 1, 1)
assert candidate["relation"] == RELATION
assert candidate["generated_source_candidates"] == 2
assert candidate["distinct_representative_forms"] == 1

relabelled = make(
    ("q", "p"),
    [
        ("q", "p", "R"),
        ("q", "x", "R"),
        ("x", "p", "R"),
        ("x", "p", "R"),
        ("x", "p", "R"),
    ],
)
reversed_terminals = make(
    ("E", "A"),
    [(edge.u, edge.v, edge.colour) for edge in graph_md.edges],
)
assert signature(relabelled) == graph_md_signature
assert signature(reversed_terminals) == graph_md_signature

candidate_network = network_from_descriptor(EXPECTED_DESCRIPTOR)
coloured_graph_md = make(
    ("A", "E"),
    [
        ("A", "E", "R"),
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("B", "E", "L"),
        ("B", "E", "C"),
    ],
)
assert signature(candidate_network) == signature(coloured_graph_md)

graph_hd = make(
    ("A", "E"),
    [
        ("A", "B", "R"),
        ("B", "E", "R"),
        ("B", "E", "L"),
        ("B", "E", "C"),
    ],
)
target_73 = make(
    ("s", "t"),
    [
        ("s", "u", "R"),
        ("u", "t", "R"),
        ("u", "t", "L"),
        ("u", "t", "C"),
    ],
)
transformed_and_merged = make(
    ("left", "right"),
    [
        ("left", "middle", "R"),
        ("middle", "right", "R"),
        ("middle", "right", "L"),
        ("middle", "right", "C"),
    ],
)
assert signature(graph_hd) == signature(target_73)
assert signature(transformed_and_merged) == signature(target_73)

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
    Fraction(13, 7),
]
for a, b, c in parameter_sets:
    a_prime = a**2 / (a + b)
    b_prime = a * b / (a + b)
    c_prime = c * (a / (a + b)) ** 2
    assert all(
        value > 0
        for value in (a, b, c, a_prime, b_prime, c_prime)
    )

    recovered_a = a_prime + b_prime
    recovered_b = b_prime * (a_prime + b_prime) / a_prime
    recovered_c = c_prime * ((a_prime + b_prime) / a_prime) ** 2
    assert (recovered_a, recovered_b, recovered_c) == (a, b, c)
    assert recovered_a**2 / (recovered_a + recovered_b) == a_prime
    assert recovered_a * recovered_b / (recovered_a + recovered_b) == b_prime
    assert (
        recovered_c * (recovered_a / (recovered_a + recovered_b)) ** 2
        == c_prime
    )

    for w in w_values:
        left = parallel(a, b + c * w)
        right = b_prime + parallel(a_prime, c_prime * w)
        assert left == right

row = next(
    record for record in ledger["records"]
    if record["catalogue_id"] == EXPECTED_ID
)
assert row["comparison_status"] == "derived-structural-match"
assert row["proposed_disposition"] == "exclude"
assert row["exclusion_category"] == "zobel-five-element-series-parallel"
assert row["basic_graph_assignment"] is None
assert row["historical_identifiers"] == []
assert "rice-lh148-635770ede187bca9-target-73" in row["evidence_record_ids"]
assert row["computational_cross_check_ids"] == [
    "rice-five-element-zobel-graph-m-dual-report-reproduction"
]

print("five-element records examined: 85")
print("graph-M-dual candidates: 1")
print(
    "candidate:",
    candidate["catalogue_id"],
    f"R{candidate['r']}L{candidate['l']}C{candidate['c']}",
    candidate["representative_descriptor"],
)
print("support:", candidate["source_support_id"])
print("assignment:", candidate["source_assignment_id"])
print(
    "sources/forms:",
    candidate["generated_source_candidates"],
    candidate["distinct_representative_forms"],
)
print("uncoloured signature:", graph_md_signature)
print("relabel and terminal reversal: pass")
print("coloured graph-M-dual signature: pass")
print("graph-H-dual and canonical network 73 signatures: pass")
print("dual Zobel exact checks: 4 tuples x 5 W values pass")
print("forward/inverse positivity and recovery: pass")
print("graph-M-dual production subject: resolved exclusion with durable links")
print("subject graph assignment null; historical identifiers empty")
PY
```

Observed output after the checksum line:

```text
five-element records examined: 85
graph-M-dual candidates: 1
candidate: lh148-635770ede187bca9 R3L1C1 0-1:R;0-2:C;0-2:L;0-2:R;1-2:R
support: support-9defcf048b659b39
assignment: assignment-1934f83e66920323
sources/forms: 2 1
uncoloured signature: StructuralSignature(relation='colour-preserving-port-augmented-cycle-matroid-v1', multiplicities=(5, 0, 0, 1), cycle_space=(0, 3, 5, 6, 25, 26, 28, 31, 40, 43, 45, 46, 49, 50, 52, 55))
relabel and terminal reversal: pass
coloured graph-M-dual signature: pass
graph-H-dual and canonical network 73 signatures: pass
dual Zobel exact checks: 4 tuples x 5 W values pass
forward/inverse positivity and recovery: pass
graph-M-dual production subject: resolved exclusion with durable links
subject graph assignment null; historical identifiers empty
```

# Evidence for the four-element Zobel exclusions

## 1. Purpose and scope

This report isolates the four four-element networks that Morelli and Smith say
are removed from the 148-network starting catalogue because networks with basic
graph `G` or `G^d` reduce by Zobel transformation to canonical networks #15 and
#17. It records the publication evidence, independent diagram transcriptions,
the complete RICE candidate set, and the strength of each resulting
correspondence.

This is a research artefact, not a production-ledger update. It does not change
the current ledger totals of 8 excluded, 140 unresolved, and 0 retained; it does
not populate graph assignments or historical identifiers in that ledger.

The authoritative source used throughout is A. Morelli and M. C. Smith,
*Passive Network Synthesis: An Approach to Classification* (2019). The inspected
local copy was
`../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf`
at `pynntt_lab` commit `1ddd90034da4594bb6a3728b0700918883fd1172`,
with SHA-256
`29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8`.
The PDF itself and all rendered pages remained outside this repository.

The status labels in this report mean:

- `source-stated`: the publication explicitly makes the claim. This does not,
  by itself, establish a RICE-ID correspondence.
- `independently-checked`: the reported RICE correspondence or algebraic step
  was reproduced from the source diagrams and RICE's named relation.
- `candidate-only`: useful locating evidence exists but the correspondence is
  not independently established.
- `unresolved`: available evidence does not select a result.

## 2. Authoritative source statements

Section 5.1 says that enumeration first gives 148 essentially distinct RLC
networks having at most five elements and at most two reactive elements. It then
lists four exclusion groups. The group relevant here is stated as four
four-element networks, having graph structure `G` or `G^d`, reducible by a Zobel
transformation to three-element networks #15 and #17 (printed p. 42, PDF index
48).

Appendix B explains that a superscript `d` denotes the graph dual and that
parenthesized values are networks eliminated from the canonical total (printed
p. 125, PDF index 131). Its four-element table gives both `G` and `G^d` a total
of 11 assignments and a canonical total of 9. For each row, the parenthesized
`(2)` occupies the stacked `3R-L / 3R-C` composition column (printed p. 126,
PDF index 132). Read together with Section 5.1, this identifies one `3R-L` and
one `3R-C` exclusion on each of `G` and `G^d`; the remaining `G`/`G^d`
assignments are not members of this four-network exclusion group.

Section 5.3.1 defines the Zobel equivalence for any two impedances `Z1` and
`Z2`. In normalized topology notation, its Figure 5.2 states

```text
(b Z1 || c Z2) -- a Z1
    ==
b' Z1 || (a' Z1 -- c' Z2)
```

for positive finite coefficients related by

```text
a' = a(a+b)/b       b' = a+b       c' = c((a+b)/b)^2
a  = a'b'/(a'+b')  b  = b'^2/(a'+b')
c  = c'(b'/(a'+b'))^2.
```

The publication explicitly observes that positive finite coefficients on
either side give positive finite coefficients on the other (printed p. 46,
PDF index 52, Section 5.3.1 and Figure 5.2).

## 3. Source locators

| Evidence | Printed page | Zero-based PDF index | Locator |
|---|---:|---:|---|
| Aggregate four-network exclusion and targets #15/#17 | 42 | 48 | Section 5.1, second exclusion bullet |
| Zobel topology and coefficient relations | 46 | 52 | Section 5.3.1, Figure 5.2 |
| Zobel-equivalence context for #15-#18 and four-element families | 50 | 56 | Figures 6.1 and 6.2 and their captions |
| Meaning of graph dual superscript and parentheses | 125 | 131 | Appendix B opening paragraph |
| Drawings and counts for `G` and `G^d` | 126 | 132 | Appendix B, four-element table, rows `G` and `G^d` |
| Three-element graph `D` and its canonical numbers | 125 | 131 | Appendix B, three-element table, row `D` |
| Canonical network #15 diagram | 129 | 135 | Appendix C, `Network #15` |
| Canonical network #17 diagram | 130 | 136 | Appendix C, `Network #17` |

Pages 42 and 46 were checked by text extraction and rendered-page inspection.
The graph and circuit conclusions below come from rendered pages, not extracted
diagram labels alone. Figures 6.1 and 6.2 were used as equivalence context; they
do not label the four excluded candidates with RICE IDs.

## 4. Transcription of basic graphs G and G-dual

The following normalized labels are local to this report. `s` and `t` are the
unordered driving-point terminals; all edges are undirected and repeated edge
rows are intentional.

| Graph | Vertices | Terminals | Normalized edges | Source |
|---|---|---|---|---|
| `G` | `{s,t,u,v}` | `{s,t}` | `{s-u, u-v, v-t, u-t}` | Appendix B, printed p. 126 / PDF index 132, row `G` |
| `G^d` | `{s,t,u}` | `{s,t}` | `{s-u, u-t, u-t, s-t}` | Appendix B, printed p. 126 / PDF index 132, row `G^d` |

Thus `G` is a terminal edge feeding a triangle whose other terminal is a
triangle vertex. `G^d` has a direct terminal edge and a two-edge terminal path,
with the path edge incident to `t` doubled. Appendix B explicitly marks `G^d`
as the dual of `G`; this report does not substitute graph isomorphism for that
source-stated dual relationship. Terminal reversal gives equivalent normalized
descriptions.

As a locating aid only, the earlier `network-theory` workspace at commit
`87b831831c154c5c3675853a99ff7e5a2b7dfb6d` contains compatible edge-list leads
in
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/analysis-of-basic-graphs.md`.
Those leads were not treated as authority: both edge sets above were
independently transcribed from the rendered Appendix B page and checked by the
RICE comparison described in Section 7. No earlier workspace supplied an
individual RICE mapping or target mapping used here. The clean `pynntt`
workspace at commit `f3db06032cbe23d583d77f6cb79d21ced90d7651` supplied no
conclusion; `pynntt_lab` supplied only the authoritative PDF named above.

## 5. Transcription of canonical networks #15 and #17

Using vertices `{s,u,t}` and terminals `{s,t}`, Appendix C gives:

| Network | Primitive edges | Topology | Basic graph | Exact source |
|---:|---|---|---|---|
| #15 | `s-u:R2`, `u-t:R1`, `u-t:L1` | `R2 -- (R1 || L1)` | `D` | Appendix C, printed p. 129 / PDF index 135; graph number cross-check in Appendix B, printed p. 125 / PDF index 131, row `D` |
| #17 | `s-u:R2`, `u-t:R1`, `u-t:C1` | `R2 -- (R1 || C1)` | `D` | Appendix C, printed p. 130 / PDF index 136; graph number cross-check in Appendix B, printed p. 125 / PDF index 131, row `D` |

The assignments and connections were transcribed from rendered circuit
diagrams. Extracted text was used only to locate the diagrams. Frequency
inversion exchanges the `L` and `C` versions; this report keeps #15 and #17
distinct and does not use frequency inversion to identify them.

## 6. Complete initial RICE candidate set

The initial structural filter deliberately ignored element colours. Each
four-element RICE representative was recoloured to a common temporary colour,
then compared with independently transcribed `G` and `G^d` using
`colour-preserving-port-augmented-cycle-matroid-v1`. This produced 22 records:
11 for each graph, exactly matching the Appendix B totals.

The temporary uncoloured port-augmented signatures were:

```text
G   colour-preserving-port-augmented-cycle-matroid-v1|R4L0C0P1|0,7,19,1e
G^d colour-preserving-port-augmented-cycle-matroid-v1|R4L0C0P1|0,3,d,e,14,17,19,1a
```

All initial candidates, before applying the source's parenthesized composition
evidence, are listed here:

| Historical graph | RICE catalogue ID | Composition | Representative descriptor |
|---|---|---|---|
| G | `lh148-53e805bd81449a69` | R2L0C2 | `0-2:C;0-3:R;1-3:C;2-3:R` |
| G | `lh148-79cf9dd24646a1a1` | R2L0C2 | `0-2:C;0-3:C;1-2:R;2-3:R` |
| G | `lh148-0f581053d03369e2` | R2L1C1 | `0-2:C;1-2:R;1-3:L;2-3:R` |
| G | `lh148-47aef84ec8f4741c` | R2L1C1 | `0-2:C;0-3:L;1-3:R;2-3:R` |
| G | `lh148-4d6ac6885b8efb8e` | R2L1C1 | `0-2:C;0-3:R;1-3:L;2-3:R` |
| G | `lh148-4fef33c7e96b6566` | R2L1C1 | `0-2:C;0-3:R;1-3:R;2-3:L` |
| G | `lh148-68712beedefbc0fa` | R2L1C1 | `0-2:C;0-3:L;1-2:R;2-3:R` |
| G | `lh148-366759d751e644ba` | R2L2C0 | `0-2:L;0-3:R;1-3:L;2-3:R` |
| G | `lh148-867793e6aaaea530` | R2L2C0 | `0-2:L;0-3:L;1-2:R;2-3:R` |
| G | `lh148-92649d60cfda8308` | R3L0C1 | `0-2:C;0-3:R;1-3:R;2-3:R` |
| G | `lh148-d5533186cc51bbab` | R3L1C0 | `0-2:L;0-3:R;1-3:R;2-3:R` |
| G^d | `lh148-102b49d775bd5eb8` | R2L0C2 | `0-1:C;0-2:C;0-2:R;1-2:R` |
| G^d | `lh148-fad884ca638a4191` | R2L0C2 | `0-1:R;0-2:C;0-2:R;1-2:C` |
| G^d | `lh148-3419842c4cffff68` | R2L1C1 | `0-1:R;0-2:C;0-2:L;1-2:R` |
| G^d | `lh148-5a15c54aa65b57dc` | R2L1C1 | `0-1:C;0-2:L;0-2:R;1-2:R` |
| G^d | `lh148-8a1860e27fc40c7f` | R2L1C1 | `0-1:R;0-2:C;1-2:L;1-2:R` |
| G^d | `lh148-b9495748ed67c6d6` | R2L1C1 | `0-1:R;0-2:C;0-2:R;1-2:L` |
| G^d | `lh148-cdfcaba8001db4d0` | R2L1C1 | `0-1:L;0-2:C;0-2:R;1-2:R` |
| G^d | `lh148-af3808b69e5fc54f` | R2L2C0 | `0-1:R;0-2:L;0-2:R;1-2:L` |
| G^d | `lh148-e61bc7a989c01099` | R2L2C0 | `0-1:L;0-2:L;0-2:R;1-2:R` |
| G^d | `lh148-5c74dc46f966ac91` | R3L0C1 | `0-1:R;0-2:C;0-2:R;1-2:R` |
| G^d | `lh148-13547be0432aeee6` | R3L1C0 | `0-1:R;0-2:L;0-2:R;1-2:R` |

Counts at the filtering steps were: 38 four-element RICE records; 22 uncoloured
`G`/`G^d` structural matches; four matches after applying the Appendix B
parenthesized `3R-L / 3R-C` evidence; and four after full colour-preserving
checking. The final step introduces no further choice because RICE contains
exactly one record for each of `G`-L, `G`-C, `G^d`-L, and `G^d`-C.

## 7. Structural matching method

The comparison used existing APIs from `rice.ladenheim` only:
`PrimitiveNetwork`, `PrimitiveEdge`, `network_from_descriptor`, and
`canonical_structural_signature`. No graph matcher or evidence schema was
added.

For the broad graph-name filter, all four real edges on each source
transcription and catalogue representative were temporarily assigned `R`.
Equality of the resulting complete GF(2) cycle spaces, with the artificial
port edge fixed, checked the exact port-augmented cycle-matroid relation while
intentionally ignoring R/L/C assignment. For the narrowed records, the
committed `canonical_structural_signature` retains R, L, C, and port colours.
The representative descriptors also give a direct graph-level reconstruction
with terminals 0 and 1. This independently preserves:

- the unordered driving-point terminal pair through the unique port edge;
- each R/L/C colour in the final record;
- the distinct `G` and `G^d` port-augmented cycle matroids;
- the distinct inductive and capacitive (frequency-inverted) cases.

The source's dual designation was recorded independently of RICE signature
equality. `G` and `G^d` do not have the same temporary signature and were not
collapsed.

## 8. Candidate-by-candidate results

`source-stated` in the source-support column describes the publication's
aggregate graph/category claim; it does not automatically establish the RICE
ID. Each RICE structural match below is separately independently checked.

| RICE catalogue ID | Historical graph | Proposed target network | Source support | Structural match | Zobel check | Overall status | Notes |
|---|---|---:|---|---|---|---|---|
| `lh148-d5533186cc51bbab` | G | #15 | source-stated | independently-checked | independently-checked | independently-checked | Unique G / R3L1C0 record; direct one-Zobel reduction followed by series-R merge |
| `lh148-92649d60cfda8308` | G | #17 | source-stated | independently-checked | independently-checked | independently-checked | Unique G / R3L0C1 record; direct one-Zobel reduction followed by series-R merge |
| `lh148-13547be0432aeee6` | G^d | #15 | source-stated | independently-checked | independently-checked | independently-checked | Unique G^d / R3L1C0 record; two uses of the source identity with a parallel-R merge |
| `lh148-5c74dc46f966ac91` | G^d | #17 | source-stated | independently-checked | independently-checked | independently-checked | Unique G^d / R3L0C1 record; two uses of the source identity with a parallel-R merge |

The publication does not print these `lh148-*` identifiers. Their overall
status is therefore `independently-checked`, not `source-stated`.

## 9. Zobel-reduction evidence

Let `X` denote either an inductor impedance or a capacitor impedance, including
its positive scale. The following checks are topology-and-parameter checks;
they are not claims of general rational-impedance canonicalization in RICE.

For either narrowed `G` representative, terminal reversal and renaming put its
impedance in the form

```text
r0 + [b' || (a' + c' X)].
```

The inverse relations on printed p. 46 give positive `a`, `b`, and `c` and
replace the bracket by `a + (b || c X)`. The two series resistors `r0` and `a`
merge, leaving

```text
R -- (R || X).
```

This is exactly the Appendix C topology of #15 when `X=L` and #17 when `X=C`.
Thus the two `G` reductions are independently checked with one application of
Figure 5.2 plus a trivial same-kind series merge.

For either narrowed `G^d` representative, renaming puts its impedance in the
form

```text
d || [a + (b || c X)].
```

The forward relations replace the bracket by
`b' || (a' + c' X)`. Merging `d || b'` gives
`R || (R + X)`, the right-hand Zobel topology. A second application of the
inverse relations gives `R -- (R || X)`, again #15 for `L` and #17 for `C`.
All intermediate values remain positive and finite by the positivity statement
in Section 5.3.1.

This establishes the proposed target correspondence algebraically. It also
bounds an evidentiary nuance: for the transcribed `G^d` representative, this
report's explicit derivation uses the published Zobel identity twice, whereas
Section 5.1 describes the exclusion category collectively as reduction “by a
Zobel transformation.” The publication does not provide an entry-specific
parameter derivation on p. 42. The result is checked, but this report does not
claim that its two-step path is the authors' unstated intended single-step
construction.

No numerical component values were needed: the source formulas are bijective
on positive finite coefficients. No source page directly states which RICE ID
maps to which target; that part is independently established by the diagram,
composition, structural-signature, and algebra checks above.

## 10. Conclusions

The available evidence establishes exactly four RICE records for this exclusion
category with no unresolved alternative candidate:

- `G` with one inductor: `lh148-d5533186cc51bbab` -> #15;
- `G` with one capacitor: `lh148-92649d60cfda8308` -> #17;
- `G^d` with one inductor: `lh148-13547be0432aeee6` -> #15;
- `G^d` with one capacitor: `lh148-5c74dc46f966ac91` -> #17.

The publication states the four-network `G`/`G^d` exclusion and the two targets.
Appendix B supplies the decisive excluded compositions, and the rendered
Appendix B/C diagrams supply independently transcribed graphs and targets.
RICE's named port-augmented coloured cycle-matroid relation selects the four
IDs uniquely, and the Section 5.3.1 coefficient relations verify their target
topologies without assuming equality from an earlier workspace.

These conclusions belong only to this report pending separate human review and
a later ledger-update task.

## 11. Remaining uncertainties

- Section 5.1 gives an aggregate statement, not four itemized diagrams or
  parameter substitutions. The RICE-ID correspondences are independently
  checked rather than publication-stated.
- The explicit `G^d` derivation above composes two applications of Figure 5.2.
  The source's shorter aggregate wording does not reveal whether the authors
  intended an equivalent dual formulation or omitted intermediate trivial
  steps.
- Component numbers such as `R1` and `R2` in Appendix C label elements; this
  report does not infer fixed numerical values from those subscripts.
- No production-ledger annotation, historical identifier, or graph-assignment
  field has been populated. The ledger therefore intentionally continues to
  report these four rows as unresolved until a later reviewed change.

There are no remaining alternative RICE candidates under the stated Appendix B
composition reading and the committed structural relation.

## 12. Reproduction commands

Run from the RICE repository root at commit
`3da389a4420013b3fa8131ee777967b4da88cbd2` or this report's descendant:

```bash
sha256sum \
  ../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf

.venv/bin/python - <<'PY'
import json
from collections import Counter, defaultdict
from rice.ladenheim import (
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    network_from_descriptor,
)

def shape_signature(edges, terminals):
    network = PrimitiveNetwork(
        terminals,
        tuple(PrimitiveEdge(u, v, "R") for u, v in edges),
    )
    return canonical_structural_signature(network).stable_string()

source_shapes = {
    "G": shape_signature(
        [("s", "u"), ("u", "v"), ("v", "t"), ("u", "t")],
        ("s", "t"),
    ),
    "Gd": shape_signature(
        [("s", "u"), ("u", "t"), ("u", "t"), ("s", "t")],
        ("s", "t"),
    ),
}

catalogue = json.load(open("data/counts/ladenheim-148.json"))
matches = defaultdict(list)
four_element = [row for row in catalogue["records"] if row["rlc"] == 4]
for row in four_element:
    network = network_from_descriptor(row["representative_descriptor"])
    signature = shape_signature(
        [(edge.u, edge.v) for edge in network.edges], network.terminals
    )
    for graph_name, source_signature in source_shapes.items():
        if signature == source_signature:
            matches[graph_name].append(row)

print("four-element records", len(four_element))
for graph_name in ("G", "Gd"):
    rows = matches[graph_name]
    print(graph_name, len(rows), Counter((r["r"], r["l"], r["c"]) for r in rows))
    for row in rows:
        print(
            row["catalogue_id"], row["r"], row["l"], row["c"],
            row["representative_descriptor"],
        )
PY

make validate-changed
git diff --check
```

PDF text was extracted with `pypdf` and the cited pages were rendered and
visually inspected with PyMuPDF from the local `.venv`. Those research-only
packages and `/tmp` renders are not project dependencies or committed inputs.

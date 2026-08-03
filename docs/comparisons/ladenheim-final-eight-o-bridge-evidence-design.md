# Evidence and contract design for the final eight Ladenheim exclusions

## 1. Purpose and boundary

This report investigates only the eight five-element networks drawn in Morelli
and Smith Figure 5.1: four series-parallel networks with basic graphs `O` or
`O^d`, and four graph-`V` bridge networks connected to them by resistor
Y--delta transformations. It transcribes the authoritative diagrams, searches
all 148 committed RICE records, checks the eight coloured correspondences,
derives their coefficient-zero and simpler-realisation facts, and recommends a
minimum evidence-contract extension.

This is evidence and contract design only. It does not change the annotation
contract, production evidence, dispositions, graph assignments, historical
identifiers, or canonical numbering. Production remains 32 excluded, 116
unresolved, and 0 retained. Canonical networks 21, 29, 36, and 44 are simpler
realisation destinations, not historical identities of the eight subjects.
Nothing here establishes the complementary 108 rows as retained or reproduces
the canonical 108 catalogue.

## 2. Source identity and locators

The authoritative source inspected was A. Morelli and M. C. Smith, *Passive
Network Synthesis: An Approach to Classification* (SIAM, 2019), at the external
read-only path
`../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf`.
Its SHA-256 is
`29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8`.
The PDF was not copied into RICE.

The following pages were text-extracted and rendered for visual inspection:

| Material | Printed page | Zero-based PDF index | Use |
|---|---:|---:|---|
| Equation (5.1) | 41 | 47 | fixes `Z(s)=(As^2+Bs+C)/(Ds^2+Es+F)` |
| Section 5.1 | 42 | 48 | collective eight-member exclusion, graph families, Cauer--Foster destinations, coefficient-zero rationale |
| Figure 5.1 | 43 | 49 | eight coloured fixtures and four Y--delta pairings |
| Section 5.3.2, Figure 5.3 | 46 | 52 | bidirectional resistor Y--delta map |
| Section 7.1, Figures 7.1--7.2 | 67--68 | 73--74 | Cauer--Foster formulae and topology |
| Section 7.1 continuation | 69 | 75 | explicit warning that Cauer and Foster forms have different realizability sets |
| Theorem 7.4 | 71--72 | 77--78 | all eight Figure 5.1 networks are nongeneric because one of `A,C,D,F` is zero |
| Appendix B, graphs `O` and `V` | 126 | 132 | rendered basic graphs and populations |
| Appendix B, graph `O^d` | 127 | 133 | rendered dual graph and population |
| Appendix C, networks 21 and 29 | 130 | 136 | rendered target circuits |
| Appendix C, networks 36 and 44 | 130--131 | 136--137 | rendered target circuits |

Diagram transcriptions below come from the rendered pages, not extracted text.

## 3. What the publication establishes

Section 5.1 says collectively that the four graph-`O`/`O^d`
series-parallel networks in Figure 5.1, and thence the four paired bridge
networks, reduce to four-element networks 21, 29, 36, and 44 through a
Cauer--Foster transformation. The same paragraph immediately limits that
claim: this is not a true equivalence in the publication's realizability-set
sense. Instead, one of `A`, `C`, `D`, or `F` is zero for each network, so every
impedance it realizes is also realizable with fewer elements.

Figure 5.1 visually supplies four explicit Y--delta pairs. Section 5.3.2 gives
the positive resistor Y--delta formulas. Section 7.1 explains why the
Cauer/Foster relation is only a quasi-equivalence: the two forms differ on a
lower-dimensional subset and therefore do not have identical realizability
sets. Theorem 7.4 then uses the forced zero coefficient to bound each Figure
5.1 realizability set's dimension by five and classifies all eight networks as
nongeneric.

Appendix B independently gives:

- graph `O`: three assignments total, one canonical, and two exclusions in the
  combined `3R-2L / 3R-2C` column;
- graph `O^d`: the same `3`, `1`, and `2` counts;
- graph `V`: seventeen assignments total and nine canonical; four excluded
  `4R-L / 4R-C` assignments belong to the already applied simpler-bilinear
  group, while four further exclusions occur in the combined
  `3R-2L / 3R-2C` column.

Thus Appendix B supports exactly eight final exclusions in the relevant
compositions, but it does not print RICE IDs. The individual subject and target
allocation below is independently reproduced.

## 4. Normalized graph and coloured fixture transcription

All terminal pairs are unordered. Edge names distinguish primitive parallel
edges.

### 4.1 Basic graphs

| Graph | Vertices | Terminals | Undirected edge multiset | Prose form |
|---|---|---|---|---|
| `O` | `A,B,C,D,E` | `A,E` | `AB, BC, CE, BD, DE` | `AB -- ((BC--CE) || (BD--DE))` |
| `O^d` | `A,B,E` | `A,E` | `AE, AB_1, AB_2, BE_1, BE_2` | `AE || ((AB_1||AB_2) -- (BE_1||BE_2))` |
| `V` | `A,B,D,E` | `A,E` | `AB, BE, AD, DE, BD` | Wheatstone bridge with cross-edge `BD` |

The upper chord in graph `V` is not collapsed, and the parallel multiplicities
in `O^d` are retained as separate primitive edges.

### 4.2 The eight Figure 5.1 fixtures

| Fixture | Coloured primitive edges | Class | Figure pairing |
|---|---|---|---|
| `O-L` | `AB:R, BC:R, CE:L, BD:R, DE:L` | series-parallel | `V-terminal-L` |
| `O-C` | `AB:R, BC:R, CE:C, BD:R, DE:C` | series-parallel | `V-terminal-C` |
| `O^d-L` | `AE:R, AB_1:R, AB_2:L, BE_1:R, BE_2:L` | series-parallel | `V-path-L` |
| `O^d-C` | `AE:R, AB_1:R, AB_2:C, BE_1:R, BE_2:C` | series-parallel | `V-path-C` |
| `V-terminal-L` | `AB:L, AD:L, BE:R, DE:R, BD:R` | bridge | `O-L` |
| `V-terminal-C` | `AB:C, AD:C, BE:R, DE:R, BD:R` | bridge | `O-C` |
| `V-path-L` | `AB:L, BE:L, AD:R, DE:R, BD:R` | bridge | `O^d-L` |
| `V-path-C` | `AB:C, BE:C, AD:R, DE:R, BD:R` | bridge | `O^d-C` |

These are row-by-row visual pairings in Figure 5.1. No pairing was inferred
from target-list order or electrical duality.

## 5. Complete RICE census and exact subjects

The reproduction loads every record in `data/counts/ladenheim-148.json`,
temporarily recolours all five real edges to `R`, preserves the artificial port
edge and unordered terminals, and compares
`canonical_structural_signature` under
`colour-preserving-port-augmented-cycle-matroid-v1`.

The complete uncoloured populations are:

| Graph | RICE population | Composition census |
|---|---:|---|
| `O` | 3 | one each of `R3L0C2`, `R3L1C1`, `R3L2C0` |
| `O^d` | 3 | one each of `R3L0C2`, `R3L1C1`, `R3L2C0` |
| `V` | 17 | four `R3L0C2`, five `R3L1C1`, four `R3L2C0`, two `R4L0C1`, two `R4L1C0` |

Retaining colours and comparing every independently transcribed fixture selects
exactly one record apiece:

| Fixture | RICE catalogue ID | Representative descriptor | Support / assignment | Sources / forms |
|---|---|---|---|---:|
| `O-C` | `lh148-4a925dd55dc8da19` | `0-2:C;0-3:C;1-4:R;2-4:R;3-4:R` | `support-599e70e6844b1d00` / `assignment-6fbbc6adf021e135` | `4 / 3` |
| `O-L` | `lh148-68430bbb448b9991` | `0-2:L;0-3:L;1-4:R;2-4:R;3-4:R` | `support-599e70e6844b1d00` / `assignment-91d44c4db2d77b07` | `4 / 3` |
| `O^d-C` | `lh148-5278112fab778336` | `0-1:R;0-2:C;0-2:R;1-2:C;1-2:R` | `support-9defcf048b659b39` / `assignment-028c94f471f15ad5` | `1 / 1` |
| `O^d-L` | `lh148-debfbc02c5650a94` | `0-1:R;0-2:L;0-2:R;1-2:L;1-2:R` | `support-9defcf048b659b39` / `assignment-032df459586efeb6` | `1 / 1` |
| `V-path-C` | `lh148-f942f37eed38400a` | `0-2:C;0-3:R;1-2:C;1-3:R;2-3:R` | `support-bea50b5cd065e186` / `assignment-141fcecedc0f759b` | `2 / 1` |
| `V-terminal-C` | `lh148-47ee32380ab1b406` | `0-2:C;0-3:C;1-2:R;1-3:R;2-3:R` | `support-bea50b5cd065e186` / `assignment-a67aeacc7cab0a59` | `2 / 1` |
| `V-path-L` | `lh148-f40bfca59082ff8d` | `0-2:L;0-3:R;1-2:L;1-3:R;2-3:R` | `support-bea50b5cd065e186` / `assignment-21674c2b6141fccd` | `2 / 1` |
| `V-terminal-L` | `lh148-7e24311a6fea4531` | `0-2:L;0-3:L;1-2:R;1-3:R;2-3:R` | `support-bea50b5cd065e186` / `assignment-8caa7f44cb5e618d` | `2 / 1` |

All eight production rows remain unresolved in this evidence milestone.

The exact signature payloads, written as `(multiplicities, cycle_space)` after
the common relation name above, are:

| Fixtures | Exact coloured structural-signature payload |
|---|---|
| `O-C` | `((3,0,2,1), (0,27,45,54))` |
| `O-L` | `((3,2,0,1), (0,27,45,54))` |
| `O^d-C` | `((3,0,2,1), (0,7,9,14,18,21,27,28,35,36,42,45,49,54,56,63))` |
| `O^d-L` | `((3,2,0,1), (0,7,9,14,18,21,27,28,35,36,42,45,49,54,56,63))` |
| `V-path-C` | `((3,0,2,1), (0,11,21,30,38,45,51,56))` |
| `V-terminal-C` | `((3,0,2,1), (0,7,25,30,42,45,51,52))` |
| `V-path-L` | `((3,2,0,1), (0,11,21,30,38,45,51,56))` |
| `V-terminal-L` | `((3,2,0,1), (0,7,25,30,42,45,51,52))` |

## 6. Y--delta equivalence within each pair

For a resistor star with positive finite legs `x_A,x_B,x_E`, let

```text
P = x_A x_B + x_B x_E + x_A x_E
r_AB = P/x_E,  r_BE = P/x_A,  r_AE = P/x_B.
```

The inverse delta-to-star map is

```text
x_A = r_AB r_AE / S
x_B = r_AB r_BE / S
x_E = r_BE r_AE / S
S   = r_AB + r_BE + r_AE.
```

Direct substitution recovers every input in both directions. Every numerator
and denominator is strictly positive and finite when the inputs are, so this is
a positive-finite bijection over the required resistor domain.

For `V-path-X`, the resistor star is centred at `D` and has leaves `A,B,E`.
Replacing it by its delta leaves the two `X` edges on `AB` and `BE` in parallel
with delta resistors and creates the direct `AE` resistor: exactly `O^d-X`.
For `V-terminal-X`, the resistor delta is `BDE`. Replacing it by a star centred
at a new `X_0` leaves two arms consisting of a reactive edge followed by a
resistor and a third leading resistor to `E`: graph `O-X`, up to terminal
reversal and series interchange. Here `X` is independently `L` and `C`.

The symbolic star/delta identities prove the topology-local transformation.
The reproduction additionally checks exact driving-point equality for three
nontrivial rational parameter tuples and four rational frequency values per
pair; those finite substitutions are corroboration, not the general proof.

## 7. Forced coefficients and nongenericity

Write each impedance in the source's equation (5.1) form

```text
Z(s) = (A s^2 + B s + C) / (D s^2 + E s + F).
```

For graph `O`, write the leading resistance as `r_0`, the two arm resistances
as `r_1,r_2`, and the two inductances as `l_1,l_2`:

```text
Z_O,L = r_0 + (r_1+s l_1) || (r_2+s l_2).
```

Expansion gives

```text
A = l_1 l_2
B = r_0(l_1+l_2) + r_1 l_2 + r_2 l_1
C = r_0(r_1+r_2) + r_1 r_2
D = 0
E = l_1+l_2
F = r_1+r_2.
```

For `O-C`, put `q_i=1/c_i` and replace `s l_i` by `q_i/s`.
Multiplying numerator and denominator by `s^2` gives the same coefficient
pattern in reverse and forces `F=0`.

For `O^d-L`, direct expansion of

```text
Z_Od,L = r_0 || ((r_1 || s l_1) + (r_2 || s l_2))
```

gives

```text
A = r_0 l_1 l_2(r_1+r_2)
B = r_0 r_1 r_2(l_1+l_2)
C = 0
D = r_0 l_1 l_2 + l_1 l_2(r_1+r_2)
E = r_0(r_1 l_2+r_2 l_1) + r_1 r_2(l_1+l_2)
F = r_0 r_1 r_2.
```

Frequency inversion gives `O^d-C` and forces `A=0`. Exact Y--delta equality
means each paired bridge has the same driving-point immittance and therefore
the same forced zero:

| Pair | Identically zero coefficient |
|---|---|
| `O-C` / `V-terminal-C` | `F` |
| `O-L` / `V-terminal-L` | `D` |
| `O^d-C` / `V-path-C` | `A` |
| `O^d-L` / `V-path-L` | `C` |

Equation (5.1) has six homogeneous coefficients. Constraining one coordinate
to zero confines the realizability set to dimension at most five in the
`R^6_+` coefficient-space convention of Definitions 7.1--7.2 and Theorem 7.4,
which retains the common positive homogeneous scale. A projective convention
would subtract one from both the generic dimension six and the constrained
dimension five, leaving the same nongenericity conclusion. The bound used here
is the source's nonprojective bound; it is not inferred merely from the
existence of a visually simpler circuit.

## 8. Cauer--Foster extraction and individual target allocation

The four Appendix C targets were visually transcribed as:

| Target | Coloured topology | Basic graph | Forced coefficient |
|---:|---|---|---|
| 21 | `R -- (C || (R -- C))` | `G` | `F=0` |
| 29 | `R -- (L || (R -- L))` | `G` | `D=0` |
| 36 | `R || (L -- (R || L))` | `G^d` | `C=0` |
| 44 | `R || (C -- (R || C))` | `G^d` | `A=0` |

The allocation is therefore fixed by independently reproduced topology,
reactive type, and zero coefficient—not by the order `21,29,36,44` in Section
5.1.

For either the inductive variable `t=s` or the capacitive variable `t=1/s`, set

```text
Z = r_0 + (r_1+t x_1) || (r_2+t x_2).
F_0 = r_1+r_2, E_0 = x_1+x_2, A_0=x_1 x_2
C_0 = r_0 F_0+r_1 r_2
B_0 = r_0 E_0+r_1 x_2+r_2 x_1.
```

Extraction into `r'_0 + (t x'_0 || (r'_1+t x'_1))` is

```text
r'_0 = C_0/F_0
x'_0 = (B_0-r'_0 E_0)/F_0
delta = x'_0 E_0-A_0
      = (r_1 x_2-r_2 x_1)^2/F_0^2
k = (x'_0)^2/delta
r'_1 = k F_0
x'_1 = k E_0-x'_0.
```

When `delta>0`, every extracted element is positive and finite, and direct
coefficient substitution proves equality. When `delta=0`, the two original
series `R-X` arms have the same time constant and are proportional. Their
parallel combination is one series `R-X` branch; its resistor is then adjacent
to the leading resistor, so the two resistors merge. The result has two
primitive elements, one resistor and one reactive element. The corresponding
network dual is a two-element parallel `R-X` realisation. Thus every graph-`O`
or graph-`O^d` impedance has a realisation with fewer than five elements, but
the named four-element target is established only on the nondegenerate locus.
This does not prove that every source parameter lies in the positive-finite
realizability set of one named canonical target.

Indeed, if `r_2=lambda r_1` and `x_2=lambda x_1` for `lambda>0`, then

```text
(r_1+t x_1) || (r_2+t x_2)
  = lambda/(1+lambda) (r_1+t x_1).
```

The leading `r_0` therefore merges with the displayed resistor, leaving only
one resistor and one `X`. Series/parallel dualization gives the corresponding
two-element parallel formula for `O^d`. The reproduction checks both reactive
types and both topologies with exact rational arithmetic.

More explicitly,

```text
x'_0 = (r_1^2 x_2+r_2^2 x_1)/F_0^2 > 0,
r'_1 = (x'_0)^2 F_0/delta > 0,
x'_1 = x'_0 A_0/delta > 0.
```

Together with `r'_0=C_0/F_0>0`, these identities prove positivity and
finiteness throughout the nondegenerate positive-finite domain; they are not
inferences from the finite substitutions in the reproduction block.

The `O-L` and `O-C` extractions give targets 29 and 21 respectively. Applying
impedance inversion to the extracted network, with reciprocal branch
impedances and series/parallel interchange, gives the `O^d-L` and `O^d-C`
targets 36 and 44. The reproduction performs all four transformations with
four rational parameter tuples, checks positivity and finiteness on the
nondegenerate locus, evaluates exact immittances at four rational frequencies,
and compares every resulting coloured topology with its independently
transcribed Appendix C fixture. It separately constructs the two-element
series or parallel realisation on the degenerate locus and checks its
immittance exactly.

Consequently the independently checked subject allocation is:

| Series-parallel subject | Bridge partner | Simpler target | Status |
|---|---|---:|---|
| `lh148-4a925dd55dc8da19` (`O-C`) | `lh148-47ee32380ab1b406` | 21 | independently checked |
| `lh148-68430bbb448b9991` (`O-L`) | `lh148-7e24311a6fea4531` | 29 | independently checked |
| `lh148-debfbc02c5650a94` (`O^d-L`) | `lh148-f40bfca59082ff8d` | 36 | independently checked |
| `lh148-5278112fab778336` (`O^d-C`) | `lh148-f942f37eed38400a` | 44 | independently checked |

The Y--delta pair is a true positive-finite network equivalence. The arrow from
each pair to its named four-element destination records a positive-finite
Cauer--Foster realisation only when `delta>0`. When `delta=0`, the route instead
ends in the two-element series or parallel `R-X` realisation derived above. The
unconditional conclusion is nongenericity and the existence of a
fewer-element realisation, not membership of the complete source family in one
named target's positive-finite realizability set.

## 9. Evidence-contract assessment

Format version 3 cannot represent these conclusions honestly without a
contract change. Its `derived-structural-match` route requires a
`reduction-target-match` with
`rice-derived-network-equivalence-fact` provenance. Reusing that claim would
misstate the conditional Cauer--Foster simplification as true network
equivalence. The current
aggregate claim also assumes one graph label and as many unique targets as
subjects, whereas this group contains three graph labels and two subjects per
destination.

The minimum recommended version-4 addition is a new explicit-only status,
`derived-nongeneric-simplification-match`, with one evidence basis such as
`aggregate-historical-nongeneric-group-plus-subject-bound-rice-facts`. It must
remain invalid for rules and retention and must not be treated as
source-backed.

Add these narrowly typed claims:

1. `aggregate-nongeneric-exclusion-group`

   - exact fields: `claim_type`, `supported_subject_counts_by_graph`,
     `source_population`,
     `supported_disposition`, `supported_exclusion_category`,
     `supported_exclusion_mechanism`, `supported_zero_coefficient_set`, and
     `supported_simpler_realisation_targets`;
   - the authoritative values are selected-subject counts `O:2`, `O^d:2`,
     `V:4`, source population eight, the collective zero-coefficient set
     `{A,C,D,F}`, and collective target set `{21,29,36,44}`; these selected
     counts are not the independently reproduced complete graph populations
     `3`, `3`, and `17`;
   - requires authoritative-source provenance, source verification, and the
     precise Section 5.1/Figure 5.1 locator.

2. `y-delta-partner-match`

   - exact fields: `claim_type`, `subject_catalogue_ids` (exactly two),
     `subject_fixture_ids` (exactly two), `transformation_figure`,
     `positive_finite_forward`, and `positive_finite_inverse`;
   - requires one `O`/`O^d` subject and one `V` subject, distinct fixtures,
     cross-checked RICE transformation provenance, and the committed relation
     for each separate fixture match;
   - pair claims must partition all eight subjects into four disjoint pairs.

3. `forced-immittance-coefficient`

   - exact fields: `claim_type`, `subject_catalogue_ids`,
     `immittance_representation`, `coefficient`, `forced_value`,
     `nongeneric_dimension_bound`, and `supported_disposition`;
   - `coefficient` is controlled to `A,C,D,F`, `forced_value` is exactly zero,
     the representation is equation (5.1), the dimension bound is at most
     five, and the supported disposition is `exclude`;
   - every subject needs exactly one positive cross-checked claim, and paired
     subjects must name the same coefficient.

4. `conditional-simpler-realisation-route`

   - exact fields: `claim_type`, `subject_catalogue_ids` (exactly one),
     `condition_parameterization_fixture_id`, `condition_expression`,
     `nondegenerate_condition`, `nondegenerate_target_network_number`,
     `nondegenerate_target_fixture_id`, `degenerate_condition`,
     `degenerate_realisation_class`, `route_relation`, and optionally
     `y_delta_partner_match_evidence_id`;
   - `route_relation` is the controlled value
     `conditional-nondegenerate-target-plus-degenerate-fewer-element`, which
     asserts neither network equivalence nor an unconditional named-target
     result; `condition_expression` is the controlled normalized expression
     `(r1*x2-r2*x1)^2/(r1+r2)^2`, `nondegenerate_condition` is exactly
     `delta > 0`, while
     `degenerate_condition` is exactly `delta = 0` and the realisation class is
     the appropriate two-element series or parallel `R-X` class;
   - the nondegenerate target is constrained to `1..108` and must agree with
     any locator network number;
   - for an `O` or `O^d` subject, the parameterization fixture is that subject's
     reviewed fixture; for a graph-`V` bridge subject, the partner evidence ID
     is required and the parameterization fixture is the corresponding
     `O`/`O^d` fixture named by that `y-delta-partner-match`;
   - the condition expression is a controlled reviewed expression, not
     arbitrary prose, and its fixture must belong to the subject or its
     declared Y--delta partner;
   - `delta>0` and `delta=0` must be complementary over the positive-finite
     parameter domain (the normalized square cannot be negative);
   - both members of each Y--delta pair must reference the same parameterized
     condition and the same conditional four-element target.

The authoritative aggregate claim supplies the collective exclusion mechanism,
but does not allocate individual subjects to targets or assert that every
target has two subjects. Group validation derives target multiplicity two from
the eight subject-bound conditional routes after their independent checks. The
exclusion status itself is supported by the aggregate historical statement
together with each subject's forced-coefficient and nongenericity facts, not by
an unconditional named-target assertion.

The route should continue to reuse authoritative `basic-graph-definition` and
subject-bound `basic-graph-match` records for `O`, `O^d`, and `V`. A common
independently reproduced computation must be scoped to exactly the eight
subjects and target set. Its `verified_evidence_record_ids` must equal exactly
the eight subject-bound graph-match records, four Y--delta partner claims,
eight coefficient-zero claims, and eight conditional simpler-realisation
routes whose nondegenerate and degenerate branches it checks. Authoritative
source transcriptions remain provenance inputs and are not mislabelled as
computationally verified records.

Global completeness validation must require all eight explicit exclusions,
the exact supported `2+2+4` subject counts, four disjoint Y--delta pairs, one
coefficient-zero fact and one conditional route per subject, derived target
multiplicity two, and the exact collective target set. Every row must remain an
exclusion in `other-canonical-exclusion`, with a nonempty reason and
non-`none` confidence. The route must not require or create a historical
identifier or a production graph assignment. It must reject use of a
simpler-realisation destination as the excluded subject's identity, reject an
unconditional named-target claim, and reject any attempt to substitute a
`reduction-target-match` equivalence claim.

This is a recommendation only; no controlled value, claim type, schema, or
validator is changed in this milestone.

## 10. Previous-workspace audit

Only after completing the source transcription and RICE matching, a bounded
read-only audit inspected:

- `../network-theory` at
  `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`, paths
  `016--graph-generation/doc/ladenheim-catalogue/ladenheim-basic-graphs/analysis-of-basic-graphs.md`
  and `016--graph-generation/generated_graphs/ladenheim/graph_O`,
  `graph_Od`, and `graph_V`;
- `../pynntt` at `f3db06032cbe23d583d77f6cb79d21ced90d7651`;
- `../pynntt_lab` at `1ddd90034da4594bb6a3728b0700918883fd1172`.

The `network-theory` graph edge lists agree with the independently rendered
`O`, `O^d`, and `V` transcriptions after relabelling. No sibling supplied a
RICE ID or target allocation used in the argument. No relevant mapping was
found in the bounded `pynntt`/`pynntt_lab` search. All sibling worktrees were
clean and remained unchanged. This agreement is a cross-check, not historical
authority.

## 11. Conclusions and limitations

The evidence independently selects exactly eight RICE records and assigns four
Y--delta pairs to targets 21, 29, 36, and 44. Each coloured match is unique
under the committed relation. The Y--delta maps are bijective over positive
finite resistor parameters. Symbolic coefficient expansion fixes respectively
`F`, `D`, `A`, and `C` to zero, and exact Cauer--Foster extraction checks the
simpler target on its nondegenerate locus while identifying the still-simpler
degenerate locus.

What is established is:

```text
source pair --Y-delta equivalence--> same five-element immittance
source pair --coefficient-zero/nongeneric argument--> fewer-element realisation
```

It is not established, and this report does not claim, that a five-element
subject is truly equivalent to its four-element destination in the
publication's realizability-set sense. Applying the mappings requires the
reviewed contract extension described above and a separate production PR.

## 12. Reproduction commands

Run this paste-ready block from the RICE repository root on a revision
containing this report. It uses only existing RICE APIs and the Python standard
library.

```bash
.venv/bin/python - <<'PY'
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from rice.ladenheim import (
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    network_from_descriptor,
)


RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"
EXPECTED = {
    "O-C": ("lh148-4a925dd55dc8da19", 21, "F"),
    "O-L": ("lh148-68430bbb448b9991", 29, "D"),
    "Od-C": ("lh148-5278112fab778336", 44, "A"),
    "Od-L": ("lh148-debfbc02c5650a94", 36, "C"),
    "V-path-C": ("lh148-f942f37eed38400a", 44, "A"),
    "V-terminal-C": ("lh148-47ee32380ab1b406", 21, "F"),
    "V-path-L": ("lh148-f40bfca59082ff8d", 36, "C"),
    "V-terminal-L": ("lh148-7e24311a6fea4531", 29, "D"),
}


def make(edges, terminals=("A", "E")):
    return PrimitiveNetwork(
        terminals,
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def signature(network):
    result = canonical_structural_signature(network)
    assert result.relation == RELATION
    return result


def uncoloured(network):
    return PrimitiveNetwork(
        network.terminals,
        tuple(PrimitiveEdge(edge.u, edge.v, "R") for edge in network.edges),
    )


graph_fixtures = {
    "O": make(
        [
            ("A", "B", "R"),
            ("B", "C", "R"),
            ("C", "E", "R"),
            ("B", "D", "R"),
            ("D", "E", "R"),
        ]
    ),
    "Od": make(
        [
            ("A", "E", "R"),
            ("A", "B", "R"),
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("B", "E", "R"),
        ]
    ),
    "V": make(
        [
            ("A", "B", "R"),
            ("B", "E", "R"),
            ("A", "D", "R"),
            ("D", "E", "R"),
            ("B", "D", "R"),
        ]
    ),
}

fixtures = {
    "O-C": make(
        [
            ("A", "B", "R"),
            ("B", "C", "R"),
            ("C", "E", "C"),
            ("B", "D", "R"),
            ("D", "E", "C"),
        ]
    ),
    "O-L": make(
        [
            ("A", "B", "R"),
            ("B", "C", "R"),
            ("C", "E", "L"),
            ("B", "D", "R"),
            ("D", "E", "L"),
        ]
    ),
    "Od-C": make(
        [
            ("A", "E", "R"),
            ("A", "B", "R"),
            ("A", "B", "C"),
            ("B", "E", "R"),
            ("B", "E", "C"),
        ]
    ),
    "Od-L": make(
        [
            ("A", "E", "R"),
            ("A", "B", "R"),
            ("A", "B", "L"),
            ("B", "E", "R"),
            ("B", "E", "L"),
        ]
    ),
    "V-path-C": make(
        [
            ("A", "B", "C"),
            ("B", "E", "C"),
            ("A", "D", "R"),
            ("D", "E", "R"),
            ("B", "D", "R"),
        ]
    ),
    "V-terminal-C": make(
        [
            ("A", "B", "C"),
            ("B", "E", "R"),
            ("A", "D", "C"),
            ("D", "E", "R"),
            ("B", "D", "R"),
        ]
    ),
    "V-path-L": make(
        [
            ("A", "B", "L"),
            ("B", "E", "L"),
            ("A", "D", "R"),
            ("D", "E", "R"),
            ("B", "D", "R"),
        ]
    ),
    "V-terminal-L": make(
        [
            ("A", "B", "L"),
            ("B", "E", "R"),
            ("A", "D", "L"),
            ("D", "E", "R"),
            ("B", "D", "R"),
        ]
    ),
}

target_fixtures = {
    21: make(
        [
            ("A", "B", "R"),
            ("B", "E", "C"),
            ("B", "C", "R"),
            ("C", "E", "C"),
        ]
    ),
    29: make(
        [
            ("A", "B", "R"),
            ("B", "E", "L"),
            ("B", "C", "R"),
            ("C", "E", "L"),
        ]
    ),
    36: make(
        [
            ("A", "E", "R"),
            ("A", "B", "L"),
            ("B", "E", "R"),
            ("B", "E", "L"),
        ]
    ),
    44: make(
        [
            ("A", "E", "R"),
            ("A", "B", "C"),
            ("B", "E", "R"),
            ("B", "E", "C"),
        ]
    ),
}


catalogue = json.loads(Path("data/counts/ladenheim-148.json").read_text())
ledger = json.loads(
    Path("data/comparisons/ladenheim-148-to-108.json").read_text()
)
assert len(catalogue["records"]) == 148
assert ledger["format_version"] == 3
assert ledger["summary"]["by_proposed_disposition"] == {
    "exclude": 32,
    "unresolved": 116,
}

uncoloured_matches = {}
for graph_name, graph_fixture in graph_fixtures.items():
    graph_signature = signature(graph_fixture)
    matches = []
    for row in catalogue["records"]:
        network = network_from_descriptor(row["representative_descriptor"])
        if signature(uncoloured(network)) == graph_signature:
            matches.append(row)
    uncoloured_matches[graph_name] = matches

assert {name: len(rows) for name, rows in uncoloured_matches.items()} == {
    "O": 3,
    "Od": 3,
    "V": 17,
}
assert Counter(
    (row["r"], row["l"], row["c"])
    for row in uncoloured_matches["O"]
) == {(3, 0, 2): 1, (3, 1, 1): 1, (3, 2, 0): 1}
assert Counter(
    (row["r"], row["l"], row["c"])
    for row in uncoloured_matches["Od"]
) == {(3, 0, 2): 1, (3, 1, 1): 1, (3, 2, 0): 1}
assert Counter(
    (row["r"], row["l"], row["c"])
    for row in uncoloured_matches["V"]
) == {
    (3, 0, 2): 4,
    (3, 1, 1): 5,
    (3, 2, 0): 4,
    (4, 0, 1): 2,
    (4, 1, 0): 2,
}

by_signature = {}
for row in catalogue["records"]:
    network = network_from_descriptor(row["representative_descriptor"])
    by_signature.setdefault(signature(network), []).append(row)

selected = {}
for fixture_name, fixture in fixtures.items():
    rows = by_signature.get(signature(fixture), [])
    assert len(rows) == 1, (fixture_name, [row["catalogue_id"] for row in rows])
    row = rows[0]
    expected_id, target, coefficient = EXPECTED[fixture_name]
    assert row["catalogue_id"] == expected_id
    assert (row["r"], row["l"], row["c"]) in ((3, 2, 0), (3, 0, 2))
    selected[fixture_name] = row
    production_row = next(
        item
        for item in ledger["records"]
        if item["catalogue_id"] == expected_id
    )
    assert production_row["comparison_status"] == "unresolved"
    assert production_row["proposed_disposition"] == "unresolved"
    assert production_row["basic_graph_assignment"] is None
    assert production_row["historical_identifiers"] == []
    assert target in target_fixtures
    assert coefficient in {"A", "C", "D", "F"}

assert len({row["catalogue_id"] for row in selected.values()}) == 8


def solve(matrix, vector):
    size = len(vector)
    augmented = [list(matrix[i]) + [vector[i]] for i in range(size)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(size + 1)
                ]
    return [augmented[i][-1] for i in range(size)]


def edge_impedance(kind, value, s):
    if kind == "R":
        return value
    if kind == "L":
        return s * value
    if kind == "C":
        return Fraction(1, 1) / (s * value)
    raise AssertionError(kind)


def driving_point_impedance(edges, terminals, s):
    source, ground = terminals
    nodes = sorted({node for edge in edges for node in edge[:2]})
    unknown = [node for node in nodes if node != ground]
    index = {node: position for position, node in enumerate(unknown)}
    matrix = [[Fraction() for _ in unknown] for _ in unknown]
    for u, v, kind, value in edges:
        conductance = Fraction(1, 1) / edge_impedance(kind, value, s)
        if u != ground:
            matrix[index[u]][index[u]] += conductance
        if v != ground:
            matrix[index[v]][index[v]] += conductance
        if u != ground and v != ground:
            matrix[index[u]][index[v]] -= conductance
            matrix[index[v]][index[u]] -= conductance
    current = [Fraction() for _ in unknown]
    current[index[source]] = Fraction(1)
    voltage = solve(matrix, current)
    return voltage[index[source]]


def star_to_delta(x_a, x_b, x_e):
    product_sum = x_a * x_b + x_b * x_e + x_a * x_e
    return (
        product_sum / x_e,
        product_sum / x_a,
        product_sum / x_b,
    )


def delta_to_star(r_ab, r_be, r_ae):
    total = r_ab + r_be + r_ae
    return (
        r_ab * r_ae / total,
        r_ab * r_be / total,
        r_be * r_ae / total,
    )


s_values = (Fraction(1, 3), Fraction(2), Fraction(7, 4), Fraction(11, 5))
y_delta_parameter_sets = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 6), Fraction(13, 5)),
    (Fraction(5, 4), Fraction(7, 3), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8)),
)

for reactive_kind in ("L", "C"):
    for x_a, x_b, x_e, reactive_1, reactive_2 in y_delta_parameter_sets:
        r_ab, r_be, r_ae = star_to_delta(x_a, x_b, x_e)
        assert delta_to_star(r_ab, r_be, r_ae) == (x_a, x_b, x_e)
        assert all(value > 0 for value in (r_ab, r_be, r_ae))

        bridge_path = [
            ("A", "B", reactive_kind, reactive_1),
            ("B", "E", reactive_kind, reactive_2),
            ("A", "D", "R", x_a),
            ("B", "D", "R", x_b),
            ("D", "E", "R", x_e),
        ]
        sp_dual = [
            ("A", "B", reactive_kind, reactive_1),
            ("A", "B", "R", r_ab),
            ("B", "E", reactive_kind, reactive_2),
            ("B", "E", "R", r_be),
            ("A", "E", "R", r_ae),
        ]
        for s in s_values:
            assert driving_point_impedance(bridge_path, ("A", "E"), s) == (
                driving_point_impedance(sp_dual, ("A", "E"), s)
            )

        r_be, r_de, r_bd = x_a, x_b, x_e
        x_b_star, x_d_star, x_e_star = delta_to_star(r_bd, r_de, r_be)
        assert star_to_delta(x_b_star, x_d_star, x_e_star) == (
            r_bd,
            r_de,
            r_be,
        )
        assert all(value > 0 for value in (x_b_star, x_d_star, x_e_star))

        bridge_terminal = [
            ("A", "B", reactive_kind, reactive_1),
            ("A", "D", reactive_kind, reactive_2),
            ("B", "E", "R", r_be),
            ("D", "E", "R", r_de),
            ("B", "D", "R", r_bd),
        ]
        sp = [
            ("E", "X", "R", x_e_star),
            ("X", "B", "R", x_b_star),
            ("B", "A", reactive_kind, reactive_1),
            ("X", "D", "R", x_d_star),
            ("D", "A", reactive_kind, reactive_2),
        ]
        for s in s_values:
            assert driving_point_impedance(bridge_terminal, ("A", "E"), s) == (
                driving_point_impedance(sp, ("A", "E"), s)
            )


def parallel(left, right):
    return left * right / (left + right)


def o_coefficients(r0, r1, x1, r2, x2, reactive_kind):
    if reactive_kind == "L":
        return (
            x1 * x2,
            r0 * (x1 + x2) + r1 * x2 + r2 * x1,
            r0 * (r1 + r2) + r1 * r2,
            Fraction(),
            x1 + x2,
            r1 + r2,
        )
    return (
        r0 * (r1 + r2) + r1 * r2,
        r0 * (x1 + x2) + r1 * x2 + r2 * x1,
        x1 * x2,
        r1 + r2,
        x1 + x2,
        Fraction(),
    )


def od_coefficients(r0, r1, x1, r2, x2, reactive_kind):
    if reactive_kind == "L":
        return (
            r0 * x1 * x2 * (r1 + r2),
            r0 * r1 * r2 * (x1 + x2),
            Fraction(),
            r0 * x1 * x2 + x1 * x2 * (r1 + r2),
            r0 * (r1 * x2 + r2 * x1) + r1 * r2 * (x1 + x2),
            r0 * r1 * r2,
        )
    return (
        Fraction(),
        r0 * r1 * r2 * (x1 + x2),
        r0 * x1 * x2 * (r1 + r2),
        r0 * r1 * r2,
        r0 * (r1 * x2 + r2 * x1) + r1 * r2 * (x1 + x2),
        r0 * x1 * x2 + x1 * x2 * (r1 + r2),
    )


def evaluate_biquadratic(coefficients, s):
    a, b, c, d, e, f = coefficients
    return (a * s * s + b * s + c) / (d * s * s + e * s + f)


def reduce_o(r0, r1, x1, r2, x2):
    denominator_constant = r1 + r2
    denominator_linear = x1 + x2
    numerator_quadratic = x1 * x2
    numerator_linear = r0 * denominator_linear + r1 * x2 + r2 * x1
    numerator_constant = r0 * denominator_constant + r1 * r2
    target_r0 = numerator_constant / denominator_constant
    target_x0 = (
        numerator_linear - target_r0 * denominator_linear
    ) / denominator_constant
    determinant = target_x0 * denominator_linear - numerator_quadratic
    expected_determinant = (r1 * x2 - r2 * x1) ** 2 / denominator_constant**2
    assert determinant == expected_determinant
    assert determinant > 0
    scale = target_x0**2 / determinant
    target_r1 = scale * denominator_constant
    target_x1 = scale * denominator_linear - target_x0
    assert all(value > 0 for value in (target_r0, target_x0, target_r1, target_x1))
    return target_r0, target_x0, target_r1, target_x1


cf_parameter_sets = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)),
    (Fraction(3, 2), Fraction(5, 3), Fraction(7, 4), Fraction(11, 6), Fraction(13, 5)),
    (Fraction(5, 4), Fraction(7, 3), Fraction(11, 5), Fraction(13, 7), Fraction(17, 8)),
    (Fraction(7, 5), Fraction(11, 6), Fraction(13, 8), Fraction(17, 9), Fraction(19, 10)),
)

for r0, r1, x1, r2, x2 in cf_parameter_sets:
    assert r1 * x2 != r2 * x1
    target_r0, target_x0, target_r1, target_x1 = reduce_o(
        r0, r1, x1, r2, x2
    )
    for reactive_kind, target_number in (("L", 29), ("C", 21)):
        source_edges = [
            ("A", "B", "R", r0),
            ("B", "C", "R", r1),
            ("C", "E", reactive_kind, x1 if reactive_kind == "L" else 1 / x1),
            ("B", "D", "R", r2),
            ("D", "E", reactive_kind, x2 if reactive_kind == "L" else 1 / x2),
        ]
        target_edges = [
            ("A", "B", "R", target_r0),
            ("B", "E", reactive_kind, target_x0 if reactive_kind == "L" else 1 / target_x0),
            ("B", "C", "R", target_r1),
            ("C", "E", reactive_kind, target_x1 if reactive_kind == "L" else 1 / target_x1),
        ]
        target_structure = make([(u, v, kind) for u, v, kind, _ in target_edges])
        assert signature(target_structure) == signature(target_fixtures[target_number])
        coefficients = o_coefficients(r0, r1, x1, r2, x2, reactive_kind)
        zero_index = 3 if reactive_kind == "L" else 5
        assert coefficients[zero_index] == 0
        for s in s_values:
            source_z = driving_point_impedance(source_edges, ("A", "E"), s)
            target_z = driving_point_impedance(target_edges, ("A", "E"), s)
            assert source_z == target_z
            assert source_z == evaluate_biquadratic(coefficients, s)

    dual_r0, dual_r1, dual_x1, dual_r2, dual_x2 = (
        1 / r0,
        1 / r1,
        1 / x1,
        1 / r2,
        1 / x2,
    )
    d_target_r0, d_target_x0, d_target_r1, d_target_x1 = reduce_o(
        dual_r0, dual_r1, dual_x1, dual_r2, dual_x2
    )

    od_l_edges = [
        ("A", "E", "R", r0),
        ("A", "B", "R", r1),
        ("A", "B", "L", x1),
        ("B", "E", "R", r2),
        ("B", "E", "L", x2),
    ]
    target_36_edges = [
        ("A", "E", "R", 1 / d_target_r0),
        ("A", "B", "L", 1 / d_target_x0),
        ("B", "E", "R", 1 / d_target_r1),
        ("B", "E", "L", 1 / d_target_x1),
    ]
    assert signature(make([(u, v, k) for u, v, k, _ in target_36_edges])) == (
        signature(target_fixtures[36])
    )
    coefficients = od_coefficients(r0, r1, x1, r2, x2, "L")
    assert coefficients[2] == 0
    for s in s_values:
        source_z = driving_point_impedance(od_l_edges, ("A", "E"), s)
        target_z = driving_point_impedance(target_36_edges, ("A", "E"), s)
        assert source_z == target_z
        assert source_z == evaluate_biquadratic(coefficients, s)

    dual_r0, dual_r1, dual_x1, dual_r2, dual_x2 = (
        1 / r0,
        1 / r1,
        x1,
        1 / r2,
        x2,
    )
    d_target_r0, d_target_x0, d_target_r1, d_target_x1 = reduce_o(
        dual_r0, dual_r1, dual_x1, dual_r2, dual_x2
    )
    od_c_edges = [
        ("A", "E", "R", r0),
        ("A", "B", "R", r1),
        ("A", "B", "C", x1),
        ("B", "E", "R", r2),
        ("B", "E", "C", x2),
    ]
    target_44_edges = [
        ("A", "E", "R", 1 / d_target_r0),
        ("A", "B", "C", d_target_x0),
        ("B", "E", "R", 1 / d_target_r1),
        ("B", "E", "C", d_target_x1),
    ]
    assert signature(make([(u, v, k) for u, v, k, _ in target_44_edges])) == (
        signature(target_fixtures[44])
    )
    q1, q2 = 1 / x1, 1 / x2
    coefficients = od_coefficients(r0, r1, q1, r2, q2, "C")
    assert coefficients[0] == 0
    for s in s_values:
        source_z = driving_point_impedance(od_c_edges, ("A", "E"), s)
        target_z = driving_point_impedance(target_44_edges, ("A", "E"), s)
        assert source_z == target_z
        assert source_z == evaluate_biquadratic(coefficients, s)


degenerate_parameter_sets = (
    (Fraction(2), Fraction(3), Fraction(5), Fraction(2)),
    (Fraction(7, 3), Fraction(11, 4), Fraction(13, 5), Fraction(5, 2)),
    (Fraction(17, 6), Fraction(19, 7), Fraction(23, 8), Fraction(7, 3)),
)

for r0, r1, x1, scale in degenerate_parameter_sets:
    r2, x2 = scale * r1, scale * x1
    assert r1 * x2 == r2 * x1
    series_r = r0 + parallel(r1, r2)
    series_x = parallel(x1, x2)
    parallel_r = parallel(r0, r1 + r2)
    parallel_l = (x1 / r1) * (r1 + r2)
    parallel_c = (r1 / x1) / (r1 + r2)

    for reactive_kind in ("L", "C"):
        source_o = [
            ("A", "B", "R", r0),
            ("B", "C", "R", r1),
            ("C", "E", reactive_kind, x1 if reactive_kind == "L" else 1 / x1),
            ("B", "D", "R", r2),
            ("D", "E", reactive_kind, x2 if reactive_kind == "L" else 1 / x2),
        ]
        reduced_o = [
            ("A", "B", "R", series_r),
            (
                "B",
                "E",
                reactive_kind,
                series_x if reactive_kind == "L" else 1 / series_x,
            ),
        ]
        source_od = [
            ("A", "E", "R", r0),
            ("A", "B", "R", r1),
            ("A", "B", reactive_kind, x1 if reactive_kind == "L" else 1 / x1),
            ("B", "E", "R", r2),
            ("B", "E", reactive_kind, x2 if reactive_kind == "L" else 1 / x2),
        ]
        reduced_od = [
            ("A", "E", "R", parallel_r),
            (
                "A",
                "E",
                reactive_kind,
                parallel_l if reactive_kind == "L" else parallel_c,
            ),
        ]
        for s in s_values:
            assert driving_point_impedance(source_o, ("A", "E"), s) == (
                driving_point_impedance(reduced_o, ("A", "E"), s)
            )
            assert driving_point_impedance(source_od, ("A", "E"), s) == (
                driving_point_impedance(reduced_od, ("A", "E"), s)
            )


print("catalogue records examined: 148")
for graph_name in ("O", "Od", "V"):
    rows = uncoloured_matches[graph_name]
    print(
        f"graph {graph_name} uncoloured population: {len(rows)}",
        sorted(Counter((row["r"], row["l"], row["c"]) for row in rows).items()),
    )
for fixture_name in fixtures:
    row = selected[fixture_name]
    expected_id, target, coefficient = EXPECTED[fixture_name]
    print(
        fixture_name,
        expected_id,
        row["representative_descriptor"],
        "-> canonical network",
        target,
        f"({coefficient}=0): structural match unique",
    )
print("Y-delta: 4 fixture pairings, 3 parameter tuples x 4 s values pass")
print("Y-delta forward/inverse positive-finite recovery: pass")
print("Cauer-Foster extraction: 4 paths, 4 parameter tuples x 4 s values pass")
print("degenerate locus: 4 two-element paths, 3 parameter tuples x 4 s values pass")
print("coefficient-zero identities: O-C F, O-L D, Od-C A, Od-L C")
print("target structural signatures: canonical networks 21, 29, 36, 44 pass")
print("production unchanged: 32 excluded / 116 unresolved / 0 retained")

PY
```

The observed concluding output was:

```text
catalogue records examined: 148
graph O uncoloured population: 3 [((3, 0, 2), 1), ((3, 1, 1), 1), ((3, 2, 0), 1)]
graph Od uncoloured population: 3 [((3, 0, 2), 1), ((3, 1, 1), 1), ((3, 2, 0), 1)]
graph V uncoloured population: 17 [((3, 0, 2), 4), ((3, 1, 1), 5), ((3, 2, 0), 4), ((4, 0, 1), 2), ((4, 1, 0), 2)]
O-C lh148-4a925dd55dc8da19 0-2:C;0-3:C;1-4:R;2-4:R;3-4:R -> canonical network 21 (F=0): structural match unique
O-L lh148-68430bbb448b9991 0-2:L;0-3:L;1-4:R;2-4:R;3-4:R -> canonical network 29 (D=0): structural match unique
Od-C lh148-5278112fab778336 0-1:R;0-2:C;0-2:R;1-2:C;1-2:R -> canonical network 44 (A=0): structural match unique
Od-L lh148-debfbc02c5650a94 0-1:R;0-2:L;0-2:R;1-2:L;1-2:R -> canonical network 36 (C=0): structural match unique
V-path-C lh148-f942f37eed38400a 0-2:C;0-3:R;1-2:C;1-3:R;2-3:R -> canonical network 44 (A=0): structural match unique
V-terminal-C lh148-47ee32380ab1b406 0-2:C;0-3:C;1-2:R;1-3:R;2-3:R -> canonical network 21 (F=0): structural match unique
V-path-L lh148-f40bfca59082ff8d 0-2:L;0-3:R;1-2:L;1-3:R;2-3:R -> canonical network 36 (C=0): structural match unique
V-terminal-L lh148-7e24311a6fea4531 0-2:L;0-3:L;1-2:R;1-3:R;2-3:R -> canonical network 29 (D=0): structural match unique
Y-delta: 4 fixture pairings, 3 parameter tuples x 4 s values pass
Y-delta forward/inverse positive-finite recovery: pass
Cauer-Foster extraction: 4 paths, 4 parameter tuples x 4 s values pass
degenerate locus: 4 two-element paths, 3 parameter tuples x 4 s values pass
coefficient-zero identities: O-C F, O-L D, Od-C A, Od-L C
target structural signatures: canonical networks 21, 29, 36, 44 pass
production unchanged: 32 excluded / 116 unresolved / 0 retained
```

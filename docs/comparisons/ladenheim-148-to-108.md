# Ladenheim 148-to-108 evidence ledger

This is an evidence ledger for comparing RICE's reproduced structural
148-record catalogue with the reported canonical 108-network catalogue. It is
not a reproduction of the complete 108 catalogue. The committed evidence maps
all forty proposed exclusions and now positively identifies the complete
reviewed 25-member one-, two-, and three-element group together with the
complete reviewed 34-member four-element group. The remaining 49 survivors are
unresolved five-element networks.

## Two different catalogue layers

The structural starting catalogue contains 148 primitive RLC classes under
RICE's executable
`colour-preserving-port-augmented-cycle-matroid-v1` relation. Its stable IDs,
representatives, and source assignment/support provenance are in
`data/counts/ladenheim-148.json`.

The canonical 108 is reported as a subset after forty further exclusions. That
reduction is not one graph equivalence relation: the repository's literature
synthesis attributes the exclusions to simpler bilinear realizations, Zobel
transformations, Cauer-Foster relationships, regularity or realizability
arguments, and related Y-delta reasoning. A graph property or a RICE reduction
signature cannot silently stand in for one of those historical arguments.

The four aggregate comparison targets are:

| Reported exclusion group | Target | Mapped here | Still requiring individual mapping |
|---|---:|---:|---:|
| Simpler bilinear realization: four resistors and one reactive | 8 | 8 | 0 |
| Zobel-reducible four-element | 4 | 4 | 0 |
| Zobel-reducible five-element series-parallel | 20 | 20 | 0 |
| Other O/O-dual and bridge exclusions | 8 | 8 | 0 |
| **Total** | **40** | **40** | **0** |

The final O/O-dual and bridge subjects are applied through the reviewed
format-version-4 evidence group. Their conditional simpler-realisation targets
remain destinations rather than historical identities.

## Evidence material and provenance

The comparison now has access to the authoritative Morelli and Smith
publication outside the repository. The annotation file records only precise
citations and short paraphrases; it does not copy PDF pages or depend on that
local file at generation or test time. The checked locations used here are:

- Chapter 5 introduction, printed page 41 / zero-based PDF page index 47, for
  the reported 148-to-108 reduction;
- Chapter 5, Section 5.1, printed page 42 / PDF index 48, for the aggregate
  groups of eight four-resistor/one-reactive exclusions and four four-element
  G/G-dual Zobel exclusions, with targets #15 and #17 stated collectively;
- Appendix B, printed page 126 / PDF index 132, for two exclusions in the
  combined `3R-L / 3R-C` column for `G` and two in the same column for `G^d`;
  and
- Appendix B, printed pages 125--127 / PDF indices 131--133, for the tabulated
  catalogue structure and exclusion totals.

The reviewed repository report
`docs/comparisons/ladenheim-four-element-zobel-evidence.md` independently
reproduces the four RICE graph/composition correspondences and their algebraic
reductions. It is repository evidence, not the authoritative historical source.
The reviewed graph-`L` report at
`docs/comparisons/ladenheim-five-element-zobel-graph-l-evidence.md` likewise
reproduces the complete 85-record five-element census, the four graph-`L`
matches, their coloured signatures and target fixtures, and exact Zobel checks.
It documents independently checked correspondences rather than individual
historical source statements.
The reviewed graph-`M` report at
`docs/comparisons/ladenheim-five-element-zobel-graph-m-evidence.md` independently
reproduces the complete five-element census, the unique graph-`M` coloured
match, the target fixture, and the exact Zobel reduction to canonical network
canonical network 72. It likewise supplies repository evidence rather than an individual
source-stated RICE correspondence.
The reviewed graph-`M^d` report at
`docs/comparisons/ladenheim-five-element-zobel-graph-m-dual-evidence.md`
independently reproduces the complete 85-record census, unique coloured match,
graph-`H^d` target fixture, derived dual Zobel map, and exact reduction to
canonical network 73. It is repository evidence rather than an individual
source-stated RICE correspondence.
The reviewed graph-`L^d` report at
`docs/comparisons/ladenheim-five-element-zobel-graph-l-dual-evidence.md`
independently reproduces the complete 85-record census, four coloured source
fixtures, each ordered Figure 5.2 coefficient transformation, the
parallel-resistor merge, each resulting graph-`F^d` fixture, and exact target
matches to canonical networks 35, 39, 43, and 47. It likewise documents
independently checked correspondences rather than individual source-stated
RICE mappings.
The reviewed graph-`S^d` report at
`docs/comparisons/ladenheim-five-element-zobel-graph-s-dual-evidence.md`
independently reproduces the complete 85-record census and 15-member graph
population, five coloured source fixtures, four inverse Figure 5.2 pathways
with series-resistor merges to graph `G^d`, the forward composite-series-arm
pathway with a parallel-resistor merge to graph `H`, both-direction
positive-finite coverage, and exact target checks. It documents independently
checked correspondences rather than individual source-stated RICE mappings.

The reviewed low-order positive-identification pilot at
[`docs/comparisons/ladenheim-canonical-108-low-order-evidence.md`](ladenheim-canonical-108-low-order-evidence.md)
transcribes all 25 one-, two-, and three-element canonical diagrams, records
their nine source subfamilies and 21 source equivalence classes, and
independently obtains 25 distinct unique RICE structural matches. It keeps
network identity, orbit membership, and source realizability-set equivalence
separate. The reviewed format-version-5 route now uses this repository evidence
to populate exactly those 25 historical identifiers and retained dispositions;
it does not reproduce the complete canonical 108 or begin the 108-to-62
production classification.

The four-element evidence report at
[`docs/comparisons/ladenheim-canonical-108-four-element-evidence.md`](ladenheim-canonical-108-four-element-evidence.md)
visually transcribes all 34 four-element canonical diagrams across six source
subfamilies, 20 source equivalence classes, and ten source orbits. It
independently obtains 34 distinct unique RICE structural matches while keeping
identity, orbit, and realizability-set equivalence separate. The report is
preserved as the evidence basis for the now-applied complete 34-member group;
that application does not complete the canonical 108 or reproduce the 62
classes.

Previous research workspaces contain useful graph descriptions, images,
descriptor transcriptions, and computational results. Those artefacts can help
later transcription and cross-checking, but they are not authoritative
historical evidence. In particular, computational agreement can corroborate a
transcription without converting an uncited workspace assertion into a
source-backed mapping.

## Version 6 evidence contract

The manual file
`data/comparisons/ladenheim-108-annotations.json` uses `format_version: 6` and
contains reviewed assertions and structural matching rules without duplicating
all 148 structural records. The generated file
`data/comparisons/ladenheim-148-to-108.json` joins those assertions to the
structural catalogue and carries exactly one row per stable `lh148-*` ID.
Generation accepts only the exact
`colour-preserving-port-augmented-cycle-matroid-v1` source-catalogue relation;
the evidence rules cannot be applied to a catalogue using another distinctness
contract.

The provenance layers are deliberately separate:

| Layer | Meaning | Can establish historical source evidence? |
|---|---|---|
| `sources` | Publications, RICE artefacts or documentation, and previous-workspace repositories. A source describes an origin but does not itself support an assertion. | No |
| `evidence_records` | A specific assertion, structured locator, paraphrase, provenance level, verification state, and asserted fields. | Only an authoritative, source-verified record with a precise publication locator |
| `previous_workspace_records` | Repository-relative earlier transcriptions, generated artefacts, or visual cross-checks, with commit and limitations. | No |
| `computational_cross_checks` | A recorded implementation, input, operation, result, reproducibility state, and limitations. | No |

Computational provenance and the `independently_reproduced` flag must agree:
an independently reproduced computation is `true`, while a
previous-workspace-generated result is `false`.

Entries and rules reference these collections through separately validated
`evidence_record_ids`, `previous_workspace_record_ids`, and
`computational_cross_check_ids`. IDs cannot cross namespaces. Locators are
objects with controlled page, PDF index, chapter, section, figure, appendix,
table, network-number, repository-path, and commit fields; absolute machine
paths and timestamps are forbidden.
Conventional timestamp metadata keys such as `generated_at`, `createdAt`, and
`source_timestamp` are rejected recursively throughout the annotation tree.

Absolute paths are rejected even when embedded in prose. Printed-page and
historical-network locators are positive one-based integers; only the explicitly
zero-based PDF page index may be zero.

Each evidence record also has a structured `claim`. Claim types distinguish
the overall catalogue target, exclusion-category totals, an aggregate
exclusion category, a RICE selector/count result, an individual catalogue
record, a historical identifier, a historical basic-graph definition, and a
RICE-derived basic-graph match. Validation
matches evidence to the actual assertion: its subject record, disposition,
category, selector, expected population, identifier, or graph assignment must
agree as applicable. Provenance and verification state are necessary but not
sufficient. Thus evidence for the general 148-to-108 total cannot support an
individual exclusion, and evidence for one exclusion category cannot support a
different category.

Aggregate historical exclusion claims include their controlled component
predicate. For the simpler-bilinear group, the authoritative predicate, rule
selector, and mechanical RICE selector agree exactly on `r=4`, `lc=1`, with
population and expected match count both eight. For the four-element Zobel
group, they agree on `r=3`, `lc=1`, `rlc=4`, with population and expected match
count both four. Every claim carrying
`subject_catalogue_ids` is checked against the exact ID set in the committed
148 catalogue, including evidence not yet referenced by a row or rule.
Individual-record claim values are validated when evidence is loaded, so even
an unreferenced claim cannot carry an uncontrolled disposition, category, or
incoherent exclusion tuple.

The generated `target` is supplied by the annotation contract rather than
being an unevidenced generator constant. It references separate authoritative,
source-verified evidence for the `148 - 40 = 108` target and for the precise
`8 + 4 + 20 + 8` category populations. The generator validates those values
and carries their evidence-record IDs into the output.

Historical identifiers are structured by scheme, value, verification state,
and evidence-record IDs. A source-verified identifier requires precise
authoritative evidence. The nullable `basic_graph_assignment` contract can
later record a label, base label, dual designation, fixture, matching relation,
verification state, and evidence references. Every current identifier list is
empty and every basic-graph assignment is null.

A future source-verified basic-graph assignment must cite authoritative
evidence for the exact historical graph definition and fixture. It must also
cite an exact RICE-derived match naming the receiving `lh148-*` catalogue ID,
fixture, graph label, and structural relation. A historical definition alone
does not establish that a RICE row matches it. Unrelated, subject-mismatched, or
rejected evidence, and positive verification with either layer absent, are
invalid.

`comparison_status` has these meanings:

| Value | Meaning |
|---|---|
| `source-backed` | A source explicitly identifies this entry or its checked mapping. |
| `derived-unique-match` | An aggregate historical category has one logically unique set of RICE matches, with the inference recorded. |
| `working-hypothesis` | A researcher proposal not yet established by adequate source evidence. |
| `unresolved` | No adequate entry-level mapping is available. |

`proposed_disposition` is `exclude`, `retain`, or `unresolved`. Unresolved does
not mean retained. Retention requires a resolved status and evidence basis plus
authoritative, source-verified individual-record evidence for that exact
catalogue ID and retained disposition. It is never inferred merely because an
exclusion has not yet been found. An exclusion requires a controlled category,
a reason, an evidence basis, and source references. No entries are currently
marked `retain`.
Any future retained row and its supporting individual claim must use category
`none` and a null exclusion reason.
An unresolved comparison status must use the complete default unresolved
contract; it cannot carry either an exclusion or retention disposition.

`exclusion_category` is one of
`simpler-bilinear-realisation`, `zobel-four-element`,
`zobel-five-element-series-parallel`, `other-canonical-exclusion`, `none`, or
`unresolved`.

`evidence_basis` distinguishes an explicit historical entry statement, an
explicit table/figure mapping, an aggregate category plus a logically unique
RICE match, an aggregate historical graph group plus subject-bound RICE
matches, a mechanically derived RICE structural fact, a researcher hypothesis,
or no evidence yet. Mechanically derived facts establish only the stated RICE
property; they are not historical evidence by themselves.
`no-evidence-yet` is exclusive to unresolved assertions, and positive statuses
must use the basis values appropriate to their source-backed, unique-match, or
hypothesis contract.

Version 3 added `derived-structural-match` for explicit exclusion annotations
that cannot be selected by component counts. It joins an authoritative,
source-verified `aggregate-basic-graph-exclusion` claim to an authoritative
basic-graph definition, a subject-bound RICE `basic-graph-match`, a
cross-checked `reduction-target-match`, and an independently reproduced
computation. Every member of an aggregate group must cite the same single
authoritative graph-definition record and use its fixture under the committed
structural relation. The common computation must carry machine-readable scope
equal to the group's complete catalogue-subject and reduction-target sets, and
must verify exactly the graph-match and reduction-target evidence records
selected for those subjects. Every member must cite that computation; an
unscoped or unrelated computation cannot satisfy this route. Positive graph and
target evidence is exclusive to its subject row. If a member carries a graph
assignment, it must use the group's common definition, fixture, selected graph
match, and structural relation. Reduction-target evidence uses
`rice-derived-network-equivalence-fact` provenance; a target is a reduction
destination and does not become a historical identifier of the excluded row.
This route does not require `basic_graph_assignment` or a historical identifier.

Every aggregate graph-group claim used by this route is complete or invalid.
Exactly its stated population of explicit derived records must cite it; every
record must match the claimed graph and exactly one target; allocated targets
must be unique and equal the complete authoritative target set; and no rule or
row with another status may cite the claim as support. The status is invalid in
rules and cannot assert retention. Existing `source-backed`,
`derived-unique-match`, retention, historical-identifier, graph-assignment, and
component-selector contracts are unchanged.

Version 4 added the explicit-only
`derived-nongeneric-simplification-match` route and the
`aggregate-historical-nongeneric-group-plus-subject-bound-rice-facts` basis.
The final-eight structured evidence records the authoritative collective
nongeneric exclusion, subject-bound graph matches, four positive-finite
Y--delta pairs, one forced-zero immittance coefficient per subject, and one
conditional simpler-realisation route per subject. Each conditional route
distinguishes a positive-finite four-element Cauer--Foster realisation on
`delta > 0` from a two-element `R-X` realisation on `delta = 0`; it does not
assert network equivalence or unconditional realizability-set containment in
the named target. One exact-scope computation verifies the derived facts, not
the authoritative source transcriptions. The eight subjects now use the new
status and are applied as one complete group.

Confidence is controlled as `high`, `medium`, `low`, or `none`.

Version 5 adds the explicit-only `derived-canonical-identity-match` route and
the `authoritative-canonical-diagram-plus-subject-bound-rice-match` basis. The
complete low-order structured group joins 25 authoritative numbered diagram
definitions to 25 unique subject-bound RICE structural matches and one exact
computation from the reviewed low-order report. The production application
retains all 25 subjects together and assigns each exactly its matched
`morelli-smith-canonical-network` historical identifier. The publication's
orbit and equivalence-class labels remain contextual source facts, not alternate
proofs of identity.

Version 6 generalizes that route through a closed, code-controlled registry of
reviewed canonical-identity groups. The existing 25-member low-order group
remains fully applied and unchanged. A second group encodes 34 authoritative
four-element definitions, 34 unique subject-bound RICE matches, its exact
aggregate inventory, and its pinned computation from the reviewed
four-element report. Each group is independently all-or-nothing: the
four-element evidence is complete, and all 34 identities and retained
dispositions are now applied together.

## Version 6 validation boundary

The version 6 validator is closed-world for every annotation object. It checks
object shapes, controlled vocabularies, reference and catalogue-subject
resolution, provenance and verification coherence, status/disposition/category
tuples, numeric boundaries, target and count invariants, and deterministic-output
hygiene. It also rejects cross-group canonical evidence and partial application
of either controlled identity group. Unknown fields are rejected rather than
copied into the ledger.

Version 6 does not represent ambiguous candidate mappings. A later extension
must record the finite candidate set, evidence for each candidate, the comparison
relation, and why the evidence does not distinguish them. Also deferred are real
basic-graph assignments, the 49 five-element canonical identities, and transformation
proofs beyond the reviewed reports. Absence of those schema
objects establishes none of those claims.

## Current population

| Comparison status | Rows |
|---|---:|
| `derived-unique-match` | 12 |
| `derived-structural-match` | 20 |
| `derived-nongeneric-simplification-match` | 8 |
| `derived-canonical-identity-match` | 59 |
| `unresolved` | 49 |
| **Total** | **148** |

| Proposed disposition | Rows |
|---|---:|
| `exclude` | 40 |
| `retain` | 59 |
| `unresolved` | 49 |
| **Total** | **148** |

| Exclusion category | Rows |
|---|---:|
| `simpler-bilinear-realisation` | 8 |
| `zobel-four-element` | 4 |
| `zobel-five-element-series-parallel` | 20 |
| `other-canonical-exclusion` | 8 |
| `none` | 59 |
| `unresolved` | 49 |
| **Total** | **148** |

The structural catalogue contains exactly eight records with `R=4` and
`L+C=1`, and no other record satisfies that description. Morelli and Smith,
Chapter 5, Section 5.1, printed page 42 / PDF index 48, reports exactly eight
four-resistor/one-reactive exclusions whose bilinear impedances have simpler
realizations. The rule combines that aggregate authoritative statement with a
separate mechanically derived RICE component-count fact. It therefore remains
`derived-unique-match`, not `source-backed`: the source does not explicitly map
each of the eight individual RICE records to a historical figure or number.

The four Zobel four-element mappings are now applied through the aggregate
Section 5.1 statement, Appendix B's combined composition counts, and the
independently reproduced RICE evidence report. Exactly four catalogue records
satisfy the rule's `R=3`, `L+C=1`, four-element selector; the report separately
checks their G/G-dual coloured structural matches and reductions to #15 or #17.
The source does not state the individual RICE-ID correspondences, so these rows
remain `derived-unique-match`, not `source-backed`.

The four reviewed graph-`L` five-element mappings are applied through one
complete version 3 group: a collective authoritative exclusion and target-set
claim, one common authoritative graph definition, four exclusive subject-bound
graph and target matches, and one independently reproduced computation bound
to those eight selected evidence records. The targets are reduction
destinations only; they are not historical identities of the excluded rows.

The reviewed one-member graph-`M` group is also applied through version 3: one
authoritative aggregate claim and graph definition, one exclusive subject-bound
graph match, one reduction-target match to canonical network 72, and one
independently reproduced computation bound exactly to those two evidence
records. Network 72 is a reduction destination, not a historical identity.

The reviewed one-member graph-`M^d` group is applied through the same complete
version 3 route. Its subject-bound graph match and reduction-target match to
canonical network 73 are verified by the exact scoped computation from the
merged evidence report. Network 73 is a reduction destination, not a historical
identity.

The four reviewed graph-`L^d` mappings are now applied through one complete
version 3 group. Each subject cites the common aggregate claim and graph
definition, its exclusive coloured graph match, its full checked pathway from
source topology through the forward Figure 5.2 coefficient map and
parallel-resistor merge to graph `F^d`, its target match, and the common exact
computation bound to all eight selected evidence records. Canonical networks
35, 39, 43, and 47 remain reduction destinations rather than historical
identities.

The five reviewed graph-`S` mappings are applied through one complete version 3
group. Four subjects cite their forward Figure 5.2 transformations and
parallel-resistor merges to graph `G`; the fifth cites its inverse Figure 5.2
transformation on the composite parallel L-C arm, series interchange, and
series-resistor merge to graph `H^d`. Each pathway includes its coefficient
map, resulting target fixture, canonical target match, and the common exact
computation bound to all ten selected graph-match and target-match evidence
records. Canonical networks 22, 24, 30, 33, and 73 remain reduction
destinations rather than historical identities.

The five reviewed graph-`S^d` mappings complete the five-element Zobel category
through one complete version 3 group. Four subjects cite their inverse Figure
5.2 transformations and series-resistor merges to graph `G^d`; the fifth cites
its forward transformation on the composite series L-C arm and
parallel-resistor merge to graph `H`. Each pathway includes its coefficient
map, positive-finite domain argument in both directions, resulting target
fixture, canonical target match, and the common exact computation bound to all
ten selected graph-match and target-match evidence records. Canonical networks
37, 40, 45, 48, and 72 remain reduction destinations rather than historical
identities.

The eight O/O-dual and bridge mappings are applied through the complete
version 4 group. Each row cites the aggregate nongeneric exclusion, its reviewed
graph match and Y--delta pair, its forced-zero coefficient, its conditional
simpler-realisation route, and the common exact computation. On `delta > 0`
the route records a positive-finite four-element Cauer--Foster realisation; on
`delta = 0` it records a separate two-element `R-X` realisation. Neither route
asserts network equivalence or unconditional named-target containment.

The complete reviewed low-order group contributes 25 retained rows with exact
cross-checked canonical network identifiers. The complete reviewed
four-element group contributes another 34 retained rows with the same
authoritative-definition-plus-subject-match boundary. The remaining 49
survivors are unresolved five-element networks; this ledger therefore does not
positively identify the complete canonical catalogue.

The controlled four-element group contributes structured evidence for all 34
four-element identities: six subfamilies, 20 source equivalence classes, ten
source orbits, and one exact-scope computation. Its complete production
application now retains and numbers all 34 reviewed subjects. The remaining 49
five-element subjects remain uninvestigated and unresolved.

Production basic-graph assignments remain deferred: every
`basic_graph_assignment` is null. Exactly 25 historical identifier lists are
populated by the reviewed low-order application and another 34 by the reviewed
four-element application, for 59 total; the other 89 remain empty.

Mapped exclusion counts are consistency-checked against the evidence-linked
historical targets. The total may not exceed forty, and no controlled category
may exceed its declared `8`, `4`, `20`, or `8` target. Category counts must sum
to the mapped exclusion total. All four category targets are now met, for a
current mapped total of forty.

## Regeneration and validation

From the repository root:

```bash
.venv/bin/python scripts/generate_ladenheim_108_evidence.py --write
.venv/bin/python scripts/generate_ladenheim_108_evidence.py --check
.venv/bin/python -m pytest -q tests/test_ladenheim_evidence.py
```

The generator validates the source catalogue, controlled values, every record
namespace and cross-reference, structured claims and locators, historical
identifiers, claim-specific evidence suitability, the evidence-linked target,
the separation of authoritative and non-authoritative evidence, structural
assertions, row count, and ordering. Output has no timestamps, machine-absolute
paths, or unstable metadata. `--check` fails if the committed ledger differs.

## Next evidence work

1. Transcribe and validate the remaining 49 five-element canonical network
   numbers from the authoritative catalogue diagrams.
2. Add independently checked subject-bound matches without treating
   previous-workspace graph files as authoritative.
3. Only after all 108 survivors have positive identity evidence, assess whether
   the complete canonical catalogue has been reproduced.

# Ladenheim 148-to-108 evidence ledger

This is an evidence ledger for comparing RICE's reproduced structural
148-record catalogue with the reported canonical 108-network catalogue. It is
not a reproduction of the 108 catalogue. The committed evidence currently maps
seventeen proposed exclusions through reviewed unique and subject-bound
structural evidence and leaves the other 131 records unresolved.

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
| Zobel-reducible five-element series-parallel | 20 | 5 | 15 |
| Other O/O-dual and bridge exclusions | 8 | 0 | 8 |
| **Total** | **40** | **17** | **23** |

Fifteen five-element and all final O/O-dual or bridge rows remain aggregate
gaps rather than identifications of particular RICE records. Their 23
individual mappings remain unresolved.

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

Previous research workspaces contain useful graph descriptions, images,
descriptor transcriptions, and computational results. Those artefacts can help
later transcription and cross-checking, but they are not authoritative
historical evidence. In particular, computational agreement can corroborate a
transcription without converting an uncited workspace assertion into a
source-backed mapping.

## Version 3 evidence contract

The manual file
`data/comparisons/ladenheim-108-annotations.json` uses `format_version: 3` and
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

Version 3 adds `derived-structural-match` for explicit exclusion annotations
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

Confidence is controlled as `high`, `medium`, `low`, or `none`.

## Version 3 validation boundary

The version 3 validator is closed-world for every annotation object. It checks
object shapes, controlled vocabularies, reference and catalogue-subject
resolution, provenance and verification coherence, status/disposition/category
tuples, numeric boundaries, target and count invariants, and deterministic-output
hygiene. Unknown fields are rejected rather than copied into the ledger.

Version 3 does not represent ambiguous candidate mappings. A later extension
must record the finite candidate set, evidence for each candidate, the comparison
relation, and why the evidence does not distinguish them. Also deferred are real
basic-graph assignments, the remaining twenty-three exclusions,
retained canonical membership, canonical network numbering, and transformation
proofs beyond the reviewed Zobel reports. Absence of those schema
objects establishes none of those claims.

## Current population

| Comparison status | Rows |
|---|---:|
| `derived-unique-match` | 12 |
| `derived-structural-match` | 5 |
| `unresolved` | 131 |
| **Total** | **148** |

| Proposed disposition | Rows |
|---|---:|
| `exclude` | 17 |
| `retain` | 0 |
| `unresolved` | 131 |
| **Total** | **148** |

| Exclusion category | Rows |
|---|---:|
| `simpler-bilinear-realisation` | 8 |
| `zobel-four-element` | 4 |
| `zobel-five-element-series-parallel` | 5 |
| `other-canonical-exclusion` | 0 |
| `unresolved` | 131 |
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

Fifteen Zobel five-element series-parallel mappings and all eight other
O/O-dual or bridge mappings remain deliberately unassigned. The remaining
entries are not called retained merely because no exclusion has yet been found.

Production basic-graph assignments, all remaining exclusions, and canonical
network identities are intentionally deferred to later focused changes. Every
`basic_graph_assignment` remains null, every historical identifier list remains
empty, and no record is retained.

Mapped exclusion counts are consistency-checked against the evidence-linked
historical targets. The total may not exceed forty, and no controlled category
may exceed its declared `8`, `4`, `20`, or `8` target. Category counts must sum
to the mapped exclusion total. These are upper bounds while the ledger is
incomplete; equality is not required and the current mapping is seventeen.

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

1. Add independently checked basic-graph fixtures and map the 148 structural
   records without treating previous-workspace graph files as authoritative.
2. Establish the remaining fifteen individual five-element series-parallel
   Zobel mappings through complete reviewed evidence groups.
3. Identify the final eight O/O-dual and bridge cases and record each distinct
   Cauer-Foster, regularity, realizability, Y-delta, or other argument.
4. Transcribe and validate the surviving canonical network numbers from the
   authoritative catalogue diagrams.
5. Only after all forty exclusions are established, review whether evidence
   also warrants marking the complementary 108 records retained and claiming
   reproduction of the canonical catalogue.

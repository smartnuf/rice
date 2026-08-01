# Ladenheim 148-to-108 evidence ledger

This is an evidence ledger for comparing RICE's reproduced structural
148-record catalogue with the reported canonical 108-network catalogue. It is
not a reproduction of the 108 catalogue. The committed evidence currently maps
eight proposed exclusions by a logically unique component-count match and
leaves the other 140 records unresolved.

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
| Zobel-reducible four-element | 4 | 0 | 4 |
| Zobel-reducible five-element series-parallel | 20 | 0 | 20 |
| Other O/O-dual and bridge exclusions | 8 | 0 | 8 |
| **Total** | **40** | **8** | **32** |

The last three rows are aggregate gaps, not identifications of particular RICE
records. Their 32 individual mappings remain wholly unresolved.

## Evidence material and provenance

The comparison now has access to the authoritative Morelli and Smith
publication outside the repository. The annotation file records only precise
citations and short paraphrases; it does not copy PDF pages or depend on that
local file at generation or test time. The checked locations used here are:

- Chapter 5 introduction, printed page 41 / zero-based PDF page index 47, for
  the reported 148-to-108 reduction;
- Chapter 5, Section 5.1, printed page 42 / PDF index 48, for the aggregate
  group of eight four-resistor/one-reactive exclusions; and
- Appendix B, printed pages 125--127 / PDF indices 131--133, for the tabulated
  catalogue structure and exclusion totals.

Previous research workspaces contain useful graph descriptions, images,
descriptor transcriptions, and computational results. Those artefacts can help
later transcription and cross-checking, but they are not authoritative
historical evidence. In particular, computational agreement can corroborate a
transcription without converting an uncited workspace assertion into a
source-backed mapping.

## Version 2 evidence contract

The manual file
`data/comparisons/ladenheim-108-annotations.json` uses `format_version: 2` and
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
predicate. For the currently mapped group, the authoritative predicate, rule
selector, and mechanical RICE selector agree exactly on `r=4`, `lc=1`, with
population and expected match count both eight. Every claim carrying
`subject_catalogue_ids` is checked against the exact ID set in the committed
148 catalogue, including evidence not yet referenced by a row or rule.

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
| `ambiguous` | Evidence narrows the entry to multiple plausible mappings. |
| `unresolved` | No adequate entry-level mapping is available. |

`proposed_disposition` is `exclude`, `retain`, or `unresolved`. Unresolved does
not mean retained. Retention requires a resolved status and evidence basis plus
authoritative, source-verified individual-record evidence for that exact
catalogue ID and retained disposition. It is never inferred merely because an
exclusion has not yet been found. An exclusion requires a controlled category,
a reason, an evidence basis, and source references. No entries are currently
marked `retain`.

`exclusion_category` is one of
`simpler-bilinear-realisation`, `zobel-four-element`,
`zobel-five-element-series-parallel`, `other-canonical-exclusion`, `none`, or
`unresolved`.

`evidence_basis` distinguishes an explicit historical entry statement, an
explicit table/figure mapping, an aggregate category plus a logically unique
RICE match, a mechanically derived RICE structural fact, a researcher
hypothesis, or no evidence yet. Mechanically derived facts establish only the
stated RICE property; they are not historical evidence by themselves.
`no-evidence-yet` is exclusive to unresolved assertions, and positive statuses
must use the basis values appropriate to their source-backed, unique-match, or
hypothesis contract.

Confidence is controlled as `high`, `medium`, `low`, or `none`.

## Current population

| Comparison status | Rows |
|---|---:|
| `derived-unique-match` | 8 |
| `unresolved` | 140 |
| **Total** | **148** |

| Proposed disposition | Rows |
|---|---:|
| `exclude` | 8 |
| `unresolved` | 140 |
| **Total** | **148** |

| Exclusion category | Rows |
|---|---:|
| `simpler-bilinear-realisation` | 8 |
| `unresolved` | 140 |
| **Total** | **148** |

The structural catalogue contains exactly eight records with `R=4` and
`L+C=1`, and no other record satisfies that description. Morelli and Smith,
Chapter 5, Section 5.1, printed page 42 / PDF index 48, reports exactly eight
four-resistor/one-reactive exclusions whose bilinear impedances have simpler
realizations. The rule combines that aggregate authoritative statement with a
separate mechanically derived RICE component-count fact. It therefore remains
`derived-unique-match`, not `source-backed`: the source does not explicitly map
each of the eight individual RICE records to a historical figure or number.

All four Zobel four-element mappings, all twenty Zobel five-element
series-parallel mappings, and all eight other O/O-dual or bridge mappings are
deliberately unassigned. The remaining entries are not called retained merely
because no exclusion has yet been established.

Basic-graph fixtures and assignments, all remaining exclusions, and canonical
network numbers are intentionally deferred to later focused changes. No graph
letter or historical network number is asserted by this ledger, every
`basic_graph_assignment` remains null, and no record is retained.

Mapped exclusion counts are consistency-checked against the evidence-linked
historical targets. The total may not exceed forty, and no controlled category
may exceed its declared `8`, `4`, `20`, or `8` target. Category counts must sum
to the mapped exclusion total. These are upper bounds while the ledger is
incomplete; equality is not required and the current mapping remains eight.

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
2. Establish the four individual four-element Zobel mappings without inferring
   them from graph appearance.
3. Establish the twenty individual five-element series-parallel Zobel mappings
   with source-backed transformations.
4. Identify the final eight O/O-dual and bridge cases and record each distinct
   Cauer-Foster, regularity, realizability, Y-delta, or other argument.
5. Transcribe and validate the surviving canonical network numbers from the
   authoritative catalogue diagrams.
6. Only after all forty exclusions are established, review whether evidence
   also warrants marking the complementary 108 records retained and claiming
   reproduction of the canonical catalogue.

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

## Repository source inventory

The repository contains:

- the full generated 148 structural catalogue, representative descriptors,
  structural signatures, and assignment/support provenance;
- planning summaries citing A. Morelli and M. C. Smith, *Passive Network
  Synthesis: An Approach to Classification* (SIAM, 2019), with chapter/section
  context for the 148, 108, 62, and aggregate exclusion claims;
- the aggregate `8 + 4 + 20 + 8` exclusion grouping; and
- explicit warnings that historical numbering, transformations, and individual
  realizability mappings remain open.

The repository search found no book extract, scan, copied figure, checked-in
historical table, Morelli/Ladenheim number mapping, or individual record-level
statement for the Zobel, O/O-dual, Cauer-Foster, regularity, realizability, or
Y-delta exclusions. No page number or historical network number has therefore
been guessed. The ledger stores citations and short paraphrases only.

## Evidence contract

The manual file
`data/comparisons/ladenheim-108-annotations.json` contains reviewed assertions,
source definitions, and structural matching rules. It does not duplicate all
148 structural records. The generated file
`data/comparisons/ladenheim-148-to-108.json` joins those assertions to the
structural catalogue and carries exactly one row per stable `lh148-*` ID.

`comparison_status` has these meanings:

| Value | Meaning |
|---|---|
| `source-backed` | A source explicitly identifies this entry or its checked mapping. |
| `derived-unique-match` | An aggregate historical category has one logically unique set of RICE matches, with the inference recorded. |
| `working-hypothesis` | A researcher proposal not yet established by adequate source evidence. |
| `ambiguous` | Evidence narrows the entry to multiple plausible mappings. |
| `unresolved` | No adequate entry-level mapping is available. |

`proposed_disposition` is `exclude`, `retain`, or `unresolved`. Unresolved does
not mean retained. An exclusion requires a controlled category, a reason, an
evidence basis, and source references. No entries are currently marked
`retain`.

`exclusion_category` is one of
`simpler-bilinear-realisation`, `zobel-four-element`,
`zobel-five-element-series-parallel`, `other-canonical-exclusion`, `none`, or
`unresolved`.

`evidence_basis` distinguishes an explicit historical entry statement, an
explicit table/figure mapping, an aggregate category plus a logically unique
RICE match, a mechanically derived RICE structural fact, a researcher
hypothesis, or no evidence yet. Mechanically derived facts establish only the
stated RICE property; they are not historical evidence by themselves.

Source references resolve to structured source records with a citation,
locator, and project-authored summary. Historical identifiers are separate and
remain empty unless a checked source mapping supplies them. Confidence is
controlled as `high`, `medium`, `low`, or `none`.

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
`L+C=1`, and no other record satisfies that description. The repository's
cited literature synthesis reports exactly eight four-resistor/one-reactive
exclusions whose bilinear impedances have simpler realizations. The annotation
rule therefore proposes those eight records for exclusion with status
`derived-unique-match`. This is not an explicit historical figure or number
mapping, and the missing per-network primary-source locators are recorded as
open questions.

All four Zobel four-element mappings, all twenty Zobel five-element
series-parallel mappings, and all eight other O/O-dual or bridge mappings are
deliberately unassigned. The remaining entries are not called retained merely
because no exclusion has yet been established.

## Regeneration and validation

From the repository root:

```bash
.venv/bin/python scripts/generate_ladenheim_108_evidence.py --write
.venv/bin/python scripts/generate_ladenheim_108_evidence.py --check
.venv/bin/python -m pytest -q tests/test_ladenheim_evidence.py
```

The generator validates the source catalogue, controlled values, citations,
annotation IDs, structural assertions, evidence requirements, row count, and
ordering. Output has no timestamps, absolute machine paths, or unstable
metadata. `--check` fails if the committed ledger differs.

## Next evidence work

1. Consult the cited source and record exact page, figure, table, network
   number, or paragraph locators for each proposed mapping.
2. Establish the four individual four-element Zobel mappings without inferring
   them from graph appearance.
3. Establish the twenty individual five-element series-parallel Zobel mappings
   with source-backed transformations.
4. Identify the final eight O/O-dual and bridge cases and record each distinct
   Cauer-Foster, regularity, realizability, Y-delta, or other argument.
5. Only after all forty exclusions are established, review whether evidence
   also warrants marking the complementary 108 records retained and claiming
   reproduction of the canonical catalogue.

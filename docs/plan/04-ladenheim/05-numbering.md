# 04-ladenheim / 05 — Map descriptors to Morelli/Ladenheim numbering

Status: `prog`

## Goal

Map repository representatives and SP/bridge descriptors to historical numbering
once the cited sources and reduction definitions are aligned.

## Tasks

- Record the source and page or table provenance for each historical number.
- Link each known number to a repository representative and canonical
  descriptor.
- Mark unknown, ambiguous, or source-dependent mappings explicitly.

## Done means

- Historical numbering is searchable from repository fixtures.
- Descriptor, representative, and source references agree for every mapped item.

## Progress notes

- The version 2 evidence ledger reserves validated structured
  `historical_identifiers`, per-assertion publication locators, and a nullable
  basic-graph assignment for each record. A source-verified identifier must
  cite precise authoritative evidence. No graph letter or historical network
  number has been populated.
- The evidence-only report
  [`docs/comparisons/ladenheim-canonical-108-low-order-evidence.md`](../../comparisons/ladenheim-canonical-108-low-order-evidence.md)
  transcribes and independently matches 25 historical canonical network
  numbers covering every one-, two-, and three-element network. For each
  network it records precise authoritative locators, an explicit coloured
  topology, one unique RICE catalogue ID, and a representative descriptor.
  This begins the historical-numbering task at the evidence layer, but no
  production `historical_identifiers`, canonical-number field, or positive
  disposition has been applied. The remaining 83 canonical networks are not
  yet mapped, so this task remains `prog` rather than complete.
- Implemented the format-version-5 structured identity contract and complete
  25-definition/25-match evidence group from the same reviewed report. It
  validates the authoritative numbered diagrams, unique subject-bound RICE
  matches, and an all-or-nothing later application. The 25 historical
  identifiers and retained dispositions remain unapplied; all 108 survivors
  are still unresolved, so the numbering task remains `prog`.

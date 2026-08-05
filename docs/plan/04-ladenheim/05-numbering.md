# 04-ladenheim / 05 — Map descriptors to Morelli/Ladenheim numbering

Status: `done`

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
  matches, and an all-or-nothing later application. At that contract-only
  milestone the 25 historical identifiers and retained dispositions were
  unapplied and all 108 survivors were unresolved.
- Applied the reviewed low-order identity group. Exactly 25 production rows now
  carry searchable `morelli-smith-canonical-network` identifiers and retained
  dispositions, joined to their authoritative numbered definitions and exact
  subject-bound RICE matches. The remaining 83 canonical networks are still
  unmapped, and no graph assignments or 108-to-62 classification were added,
  so this task remains `prog`.
- The evidence-only report
  [`docs/comparisons/ladenheim-canonical-108-four-element-evidence.md`](../../comparisons/ladenheim-canonical-108-four-element-evidence.md)
  adds 34 independently reproduced four-element number-to-subject mappings.
  Production still contains only the 25 populated low-order canonical
  identifiers; the 34 four-element identifiers are not yet applied, and 49
  five-element networks remain unmapped. The numbering task therefore remains
  `prog`.
- Implemented the format-version-6 controlled group for those 34 reviewed
  four-element mappings. Their definitions, exact subject matches, aggregate,
  and pinned computation are now structured evidence, while production still
  contains only the 25 applied low-order canonical identifiers. The 34
  four-element identities remain unapplied and 49 five-element identities
  remain to be investigated, so this task remains `prog`.
- Applied the complete reviewed four-element group. Production now contains 59
  searchable `morelli-smith-canonical-network` identifiers: the unchanged 25
  low-order identifiers plus 34 four-element identifiers. The remaining 49
  five-element canonical numbers are unmapped, so this task remains `prog`.
- The evidence-only report
  [`docs/comparisons/ladenheim-canonical-108-five-element-evidence.md`](../../comparisons/ladenheim-canonical-108-five-element-evidence.md)
  now records exact number-to-subject mappings for all remaining 49
  five-element networks. Those mappings are not yet populated as production
  historical identifiers: production still contains 59 searchable canonical
  identifiers, and the five-element contract and application remain pending.
  The numbering task therefore remains `prog`.
- Encoded those 49 evidence-only mappings as the complete third controlled
  format-version-6 identity group. The contract now covers all 108 canonical
  numbers and subjects, but only the existing 59 identifiers are populated;
  the five-element group remains unapplied pending a separate all-or-nothing
  application. The numbering task therefore remains `prog`.
- Applied the complete five-element group. Canonical numbers 1 through 108 are
  now populated and searchable from each RICE subject and representative. Every
  mapping joins authoritative numbered-diagram provenance to its exact
  subject-bound RICE match, with no ambiguous or unmapped canonical number.
  Basic-graph letters remain a separate deferred field and do not prevent the
  canonical-numbering task from being `done`.

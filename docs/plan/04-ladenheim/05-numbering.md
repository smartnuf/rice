# 04-ladenheim / 05 — Stage E: reconcile RICE reduction with the Ladenheim stages

Status: `todo`

## Revision note (2026-07-10)

This task previously read "Map repository representatives to historical
numbering once cited sources and definitions are aligned," which is
consistent with the corrected plan but did not state how or when that
mapping should happen relative to the other stages. See
`docs/ladenheim_benchmark.md` for the full reassessment.

## Goal

Reconcile the repository's native RICE reduced-topology model
(`docs/model_decisions.md`) with the independently-reproduced Ladenheim
Stages A-D (`01-148.md`, `02-108.md`, `03-62.md`), and only after those
stages are complete. Do not pre-decide that either model must replace the
other; this stage's job is to characterise the relationship, not to pick a
winner in advance.

This stage depends on Stages B, C, and D being complete: there is nothing to
reconcile against until the independent Ladenheim reproductions exist.

## Tasks

- Identify which distinct Ladenheim networks (from Stage B's 148-network
  reproduction) coalesce under RICE's reduced-topology signature, and record
  concrete examples, not just a count difference.
- Identify which RICE reduced signatures span more than one Ladenheim
  2-isomorphism class, if any, and record concrete examples.
- Characterise, with examples, in which specific cases RICE's reduction is
  strictly finer (distinguishes more), strictly coarser (distinguishes
  less), or simply different from Ladenheim's 2-isomorphism, rather than
  asserting a single blanket direction.
- Map repository representatives to the historical Ladenheim/Morelli
  numbering for networks that do correspond one-to-one, once the
  correspondence in the previous tasks is established.
- Decide, based on the above findings rather than in advance, whether RICE's
  native reduced-topology mode should remain a separate user-facing mode
  alongside a Ladenheim-structural mode, be documented as a distinct but
  related model (the likely outcome given `docs/ladenheim_benchmark.md`'s
  finding that the two mechanisms differ), or something else.

## Done means

- The relationship between RICE's reduced-topology signature and Ladenheim's
  2-isomorphism is characterised with concrete examples in both directions
  (coalescing and splitting), not just a top-level count comparison.
- Historical numbering is mapped only for networks with an established
  correspondence.
- No premature decision to replace one model with the other is recorded
  before this stage's findings are in.
- Counts, enumeration results, catalogues, equivalence classes, generator
  sets, and full immittance identity are not conflated.

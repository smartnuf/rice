# rice plan index

Status key: `done`, `prog`, `todo`, `blocked`, `later`.

## Orientation

The numbered groups organize work by subject and dependency; they are not a
strict chronological queue. Status labels in this index and the individual task
records identify the state of each task.

## Current direction

The structural [148-network Ladenheim catalogue](04-ladenheim/01-148.md) has
been reproduced with traceable records and provenance. Comparison with the
[canonical 108-network catalogue](04-ladenheim/02-108.md) is also complete:
all forty exclusions have per-entry evidence, all 108 retained subjects have
exact canonical numbers, and the production ledger contains 40 excluded and
108 retained rows with no unresolved rows. Structural identity remains
distinct from Zobel transformations, star-delta or Y-delta relationships,
simpler bilinear realisations, nongeneric simplification, and
realizability-set equivalence.

The next distinct Ladenheim milestone is independent reproduction of the
[62 realizability-set classes](04-ladenheim/03-62.md). The source class labels
have been transcribed, but RICE has not yet independently reproduced that
behavioural classification. Other subsequent work includes
[generator sets](04-ladenheim/04-generators.md), integrated
[SP/bridge descriptors](04-ladenheim/06-descriptors.md), and comparison of the
[named structural and reduction contracts](04-ladenheim/07-compare-reductions.md).
Canonical numbering is complete; basic-graph letters and broader descriptor
vocabularies remain separate work.
Larger slices, including the
[full `R <= 3`, `L+C <= 5` census](05-slices/04-r3-x5.md), remain later work
subject to performance and output-size review. Those catalogue results will
feed the later
[biquadratic investigations](06-biquad/05-impedance-classes.md).

## 00 — Plan records and literature alignment

- `done` [Bring plan records up to date](00-records/01-update-plan-records.md)
- `prog` [Record literature conclusions from deep research](00-records/02-literature-conclusions.md)
- `done` [Update README motivation](00-records/03-readme-motivation.md)

## 01 — Development environment

- `done` [Fix Makefile syntax](01-dev-env/01-make.md)
- `done` [Make Codex use `.venv` explicitly](01-dev-env/02-codex-venv.md)
- `done` [Validate WSL2 Ubuntu path](01-dev-env/03-wsl.md)
- `done` [Run `make setup` and `make test`](01-dev-env/04-make-setup-test.md)
- `done` [Create Windows/Linux scripts under `scripts/`](01-dev-env/05-scripts.md)
- `done` [Keep Makefile, scripts, README, and AGENTS.md aligned](01-dev-env/06-contract.md)

## 02 — Cleanup and simplification

The cleanup family is complete. Executed in the order reviewed in
`02-cleanup/01-review.md` section 8 (which intentionally did not match the
files' numeric prefixes; the files were not renamed/renumbered to match):
`03-generic-x` → `02-legacy` → `04-public-api` → `07-tests/04-cleanup-tests`
(the last of these lives under the `07 —` group below, not this one).

- `done` [Review current implementation before deletion](02-cleanup/01-review.md)
- `done` [Remove legacy implementation](02-cleanup/02-legacy.md)
- `done` [Remove generic `X` implementation, tests, and docs](02-cleanup/03-generic-x.md)
- `done` [Update examples, imports, and public surface](02-cleanup/04-public-api.md)

## 03 — Catalogue model and distinctness

- `prog` [Define catalogue object model](03-counting/02-distinct.md)
- `prog` [Define enumeration scope](03-counting/03-scope.md)
- `done` [Define small explicit catalogue slice](03-counting/04-small-slice.md)
- `prog` [Define Ladenheim comparison contracts](03-counting/05-ladenheim.md)
- `todo` [Define full current project slice](03-counting/06-full-counts.md)
- `prog` [Define output catalogue format](03-counting/07-outputs.md)

## 04 — Ladenheim reproduction

- `done` [Reproduce structural 148-network Ladenheim set](04-ladenheim/01-148.md)
- `done` [Compare with canonical 108-network Ladenheim catalogue](04-ladenheim/02-108.md)
- `todo` [Reproduce 62 realizability-set classes](04-ladenheim/03-62.md)
- `todo` [Identify generator sets](04-ladenheim/04-generators.md)
- `done` [Map descriptors to Morelli/Ladenheim numbering](04-ladenheim/05-numbering.md)
- `todo` [Integrate SP/bridge descriptors](04-ladenheim/06-descriptors.md)
- `todo` [Compare local SP and 2-isomorphism reductions](04-ladenheim/07-compare-reductions.md)

## 05 — Enumeration slices and counts

- `done` [Small fast test slice: `R <= 2`, `L+C <= 3`](05-slices/01-r2-x3.md)
- `done` [Ladenheim slice: `R+L+C <= 5`, `L+C <= 2`](05-slices/02-ladenheim.md)
- `todo` [Morelli next-class slice: `R <= 4`, `L+C <= 3`](05-slices/03-r4-x3.md)
- `todo` [Full current project slice: `R <= 3`, `L+C <= 5`](05-slices/04-r3-x5.md)
- `todo` [Two-resistor high-reactive slice: `R <= 2`, `L+C <= 5`](05-slices/05-r2-x5.md)
- `todo` [Three-reactive high-resistor slice: `R <= 5`, `L+C <= 3`](05-slices/06-r5-x3.md)
- `todo` [Eight-element series-parallel slice](05-slices/07-sp8.md)

## 06 — Biquadratic realisability investigations

- `todo` [Investigate whether `R <= 2`, `L+C <= 5` suffices for all biquadratic immittances](06-biquad/01-r2-x5-sufficiency.md)
- `todo` [Investigate whether 8-element SP networks suffice for all biquadratic immittances](06-biquad/02-sp8-sufficiency.md)
- `todo` [Investigate whether `R <= 5`, `L+C <= 3` suffices for all biquadratic immittances](06-biquad/03-r5-x3-sufficiency.md)
- `todo` [Track known regular/non-regular/minimum-function cases](06-biquad/04-known-classes.md)
- `todo` [Relate catalogue slices to impedance classes](06-biquad/05-impedance-classes.md)

## 07 — Test coverage

- `prog` [Set up test strategy for catalogue enumeration](07-tests/01-strategy.md)
- `prog` [Add golden count tests](07-tests/02-golden-counts.md)
- `prog` [Add distinctness and reduction tests](07-tests/03-canon-tests.md)
- `done` [Add cleanup regression tests](07-tests/04-cleanup-tests.md)
- `prog` [Add CI-friendly validation commands](07-tests/05-ci.md)

## 08 — Documentation

- `todo` [Document developer workflow](08-docs/01-dev-workflow.md)
- `prog` [Document counting methodology](08-docs/02-count-method.md)
- `prog` [Document catalogue comparisons and references](08-docs/03-catalogues.md)
- `prog` [Document known limits and open questions](08-docs/04-open.md)

## 09 — Later named features

- `later` [Render schematics](09-later/01-schematics.md)
- `later` [Identify quartets](09-later/02-quartets.md)
- `later` [Identify bridge/core/non-SP structures](09-later/03-cores.md)
- `later` [Compute symbolic immittances](09-later/05-symbolic.md)
- `later` [Investigate Bott-Duffin redundancy](09-later/06-equivalence.md)
- `later` [Catalogue browser/search tools](09-later/07-browser.md)

## 10 — Object-oriented counting language

- `done` [PR1 — counting-language foundations and bundle-set census](10-count-language/01-foundations.md)
- `done` [PR2 — migrate assignments, assigned supports and reduced networks beneath `rice count`](10-count-language/02-count-migration.md)
- `done` [PR3 — enumeration and reduction mapping/analysis](10-count-language/03-enum-reductions.md)
- `done` [Interface consolidation](10-count-language/04-interface-consolidation.md)

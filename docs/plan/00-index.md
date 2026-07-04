# rlc-oneport-count plan index

Status key: `done`, `doing`, `todo`, `blocked`, `later`.

## 00 — Plan records and literature alignment

- `todo` [Bring plan records up to date](00-records/01-update-plan.md)
- `todo` [Record literature conclusions from deep research](00-records/02-literature-conclusions.md)
- `todo` [Update README motivation](00-records/03-readme-motivation.md)

## 01 — Development environment

- `done` [Fix Makefile syntax](01-dev-env/01-make.md)
- `done` [Make Codex use `.venv` explicitly](01-dev-env/02-codex-venv.md)
- `done` [Validate WSL2 Ubuntu path](01-dev-env/03-wsl.md)
- `done` [Use `make setup`, `make test`, and scripts contract](01-dev-env/04-setup-test.md)
- `done` [Create Windows/Linux scripts under `scripts/`](01-dev-env/05-scripts.md)
- `done` [Keep Makefile, scripts, README, and AGENTS.md aligned](01-dev-env/06-contract.md)

## 02 — Cleanup and simplification

- `todo` [Review current implementation before deletion](02-cleanup/01-review.md)
- `todo` [Remove legacy implementation](02-cleanup/02-legacy.md)
- `todo` [Remove generic `X` implementation, tests, and docs](02-cleanup/03-generic-x.md)
- `todo` [Update examples, imports, and public surface](02-cleanup/04-public-api.md)

## 03 — Catalogue model and distinctness

- `todo` [Define catalogue object model](03-catalogue/01-object-model.md)
- `todo` [Define distinctness layers](03-catalogue/02-distinctness.md)
- `todo` [Define reduced-topology rules](03-catalogue/03-reduced-topology.md)
- `todo` [Define genericity and non-generic rejection](03-catalogue/04-genericity.md)
- `todo` [Define output catalogue format](03-catalogue/05-output-format.md)

## 04 — Ladenheim reproduction

- `todo` [Reproduce unabridged 148-candidate Ladenheim set](04-ladenheim/01-148.md)
- `todo` [Reproduce canonical 108-network catalogue](04-ladenheim/02-108.md)
- `todo` [Reproduce 62 equivalence classes](04-ladenheim/03-62.md)
- `todo` [Identify generator sets](04-ladenheim/04-generators.md)
- `todo` [Compare with Morelli/Ladenheim numbering](04-ladenheim/05-numbering.md)

## 05 — Enumeration slices and counts

- `todo` [Small fast test slice: `R <= 2`, `L+C <= 3`](05-slices/01-r2-x3.md)
- `todo` [Ladenheim slice: `R <= 3`, `L+C <= 2`, `R+L+C <= 5`](05-slices/02-ladenheim.md)
- `todo` [Morelli next-class slice: `R <= 4`, `L+C <= 3`](05-slices/03-r4-x3.md)
- `todo` [Full current project slice: `R <= 3`, `L+C <= 5`](05-slices/04-r3-x5.md)
- `todo` [Two-resistor high-reactive slice: `R <= 2`, `L+C <= 5`](05-slices/05-r2-x5.md)
- `todo` [Three-reactive high-resistor slice: `R <= 5`, `L+C <= 3`](05-slices/06-r5-x3.md)
- `todo` [Eight-element series-parallel slice](05-slices/07-sp8.md)

## 06 — Biquadratic realisability investigations

- `todo` [Investigate whether `R <= 2`, `L+C <= 5` suffices for all biquadratic immittances](06-biquad/01-r2-x5-sufficiency.md)
- `todo` [Investigate whether 8-element SP networks suffice for all biquadratic immittances](06-biquad/02-sp8-sufficiency.md)
- `todo` [Track known regular/non-regular/minimum-function cases](06-biquad/03-known-classes.md)
- `todo` [Relate catalogue slices to impedance classes](06-biquad/04-impedance-classes.md)

## 07 — Test coverage

- `todo` [Set up test strategy for catalogue enumeration](07-tests/01-strategy.md)
- `todo` [Add golden support-graph tests](07-tests/02-support-golden.md)
- `todo` [Add Ladenheim 148/108/62 regression tests](07-tests/03-ladenheim-golden.md)
- `todo` [Add distinctness and reduction tests](07-tests/04-distinctness.md)
- `todo` [Add slice-count regression tests](07-tests/05-slice-counts.md)
- `todo` [Add CI-friendly validation commands](07-tests/06-ci.md)

## 08 — Documentation

- `todo` [Document developer workflow](08-docs/01-dev-workflow.md)
- `todo` [Document catalogue methodology](08-docs/02-catalogue-method.md)
- `todo` [Document literature references](08-docs/03-references.md)
- `todo` [Document known limits and open questions](08-docs/04-open.md)

## 09 — Later named features

- `later` [Render schematics](09-later/01-schematics.md)
- `later` [Identify quartets](09-later/02-quartets.md)
- `later` [Identify bridge/core/non-SP structures](09-later/03-cores.md)
- `later` [Export Pynntt descriptors](09-later/04-descriptors.md)
- `later` [Compute symbolic immittances](09-later/05-symbolic.md)
- `later` [Classify equivalence and generator sets](09-later/06-equivalence.md)
- `later` [Catalogue browser/search tools](09-later/07-browser.md)

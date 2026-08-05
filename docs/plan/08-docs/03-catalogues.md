# 08-docs / 03 — Document catalogue comparisons and references

Status: `prog`

## Goal

Keep historical comparisons precise and sourced.

## Notes

Detailed historical catalogue comparisons, bibliographic support, and
contract-by-contract explanations belong to this task rather than blocking the
general README motivation task.

The relevant historical name is the Ladenheim catalogue. Repository
Ladenheim documentation should distinguish:

- the 148 structural primitive RLC networks in the scope `R+L+C <= 5`,
  `L+C <= 2`, after colour-preserving graph 2-isomorphism and same-kind
  series/parallel rejection;
- the canonical 108-network catalogue, a subset of the 148 after forty further
  exclusions, whose members satisfy `R <= 3`, `L+C <= 2`, and `R+L+C <= 5`;
- the later 62 realizability-set equivalence classes, distinct from the reported
  35 group-action orbits and 24 subfamilies.

Bibliographic source: A. Morelli and M. C. Smith, *Passive Network Synthesis: An
Approach to Classification*, SIAM, 2019, including Chapter 3 Section 3.1,
Chapter 5, the Chapter 6 classification discussion, and Theorem 7.4.

## Planned comparison slices

- Historical Ladenheim structural scope: `R+L+C <= 5` and `L+C <= 2`.
- RICE local series/parallel comparison point: `R <= 3`, `L+C <= 2`,
  `max_edges = 5`, currently counting 140 reduced signatures. Historical 108
  members lie in this budget region, but that local-SP relation is distinct
  from the completed mapping of the canonical 108 identities against the
  structural 148 catalogue under the named port-augmented coloured structural
  contract. The two relations must not be silently equated.
- RICE smoke-test slice: `R <= 2`, `L+C <= 3`.
- RICE full planned scope: `R <= 3`, `L+C <= 5`.

## Done means

- The repository cites the sources used.
- Agreement or disagreement with historical counts is explained by named
  contracts rather than by informal distinctness language.
- The spelling and scope of each catalogue are consistent throughout the docs.

## Progress notes

- Added `docs/comparisons/ladenheim-148-to-108.md` with the evidence-status and
  disposition contract, complete 40 excluded / 0 unresolved / 108 retained
  population, source inventory, explicit research boundaries, and
  deterministic regeneration commands.
- Documented the version 2 separation between authoritative evidence,
  previous-workspace material, and computational cross-checks, including the
  precise Morelli and Smith page/PDF-index locators used by the later reviewed
  evidence contracts.
- All forty exclusions now have per-entry evidence, all 108 nonexcluded
  subjects are positively identified, and canonical numbers 1 through 108 are
  populated. Production is 40 excluded / 0 unresolved / 108 retained, so the
  central identity-comparison and numbering documentation is complete. The
  source's 62 class labels have been transcribed, but RICE has not independently
  reproduced the 62 realizability-set classes. Basic-graph assignments and
  broader descriptor integration remain open, so this wider documentation task
  remains in progress.

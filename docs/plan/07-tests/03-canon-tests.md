# 07-tests / 03 — Descriptor and canonicalisation tests

Status: `prog`

## Goal

Ensure duplicate rejection and descriptor production are trustworthy.

## Tasks

- Test canonicalisation under internal node renaming and terminal-pair reversal.
- Test simple primitive bundle-label preservation.
- Test series/parallel normalisation where applicable.
- Test bridge/non-series-parallel examples separately.
- Test that descriptor output is stable.

## Done means

- Equivalent networks collapse to the same canonical representative where intended.
- Non-equivalent networks do not collapse accidentally.
- Descriptor output is deterministic.


## Progress notes

- Added focused phase-3 assigned-support canonicalisation tests covering single-edge supports, terminal-path reversal, asymmetric terminal-labelled supports, exclusion of automorphisms that do not preserve the terminal set, explicit terminal-swapping automorphisms, budget accounting over edge cycles, and brute-force cross-checks for small supports.
- Local series/parallel normalisation and descriptor-output tests remain future work.

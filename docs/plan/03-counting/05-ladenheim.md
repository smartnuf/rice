# 03-counting / 05 — Define the Ladenheim comparison contracts

Status: `todo`

## Goal

Replace the old single "Ladenheim slice" idea with precise comparison
contracts for the historical stages and for the current RICE reduced diagnostic.

## Correct historical scope

The initial 148 stage uses:

```text
total elements <= 5
L + C <= 2
```

It is not initially restricted to `R <= 3`. The 148 are already **essentially
distinct networks** under graph 2-isomorphism-level structural distinctness
(deformation, separation, and series interchange), after excluding same-kind
series/parallel simplifications.

## Current RICE diagnostic slice

The old planned slice remains useful only as a RICE reduced-signature diagnostic:

```text
R <= 3
L + C <= 2
support edges <= 5
```

At commit `338ddec`, the repository-native command

```bash
.venv/bin/python -m rice reduced --max-r 3 --max-reactive 2 --max-edges 5 --format json
```

reports 140 final RICE reduced signatures. Because `R <= 3` and `L+C <= 2`
imply total primitive components `<= 5`, this command enforces the old coupled
total bound only indirectly for this particular diagnostic.

## Capability gap

The corrected initial 148 scope cannot currently be expressed exactly by the
CLI/API without imposing `R <= 3`. The implementation has independent `R` and
`L+C` budgets plus an optional support-edge bound; it does not have a coupled
`total elements <= 5` primitive-component budget. A future Ladenheim enumerator
needs that contract explicitly.

## Done means

- Stage A defines the historical 148 model contract before implementation.
- Stage B reproduces 148 with a dedicated Ladenheim structural signature.
- Stage C reproduces the 108-network canonical set as a separate removal stage.
- Stage D reproduces the 62 realizability-set equivalence classes as behavioral
  classification of the 108 members.
- Stage E compares those historical results with the native RICE reduced
  signature without pre-deciding that either model replaces the other.

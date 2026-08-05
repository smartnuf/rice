# Structural Ladenheim 148 catalogue

This catalogue contains 148 essentially distinct primitive RLC two-terminal
networks in the historical starting scope:

```text
R + L + C <= 5
L + C <= 2
```

The generator starts with RICE's terminal-relevant simple supports and simple
bundle assignments, then expands every bundle into individual R, L, and C
primitive edges. It does not call `canonical_reduced_signature` or apply the
RICE local series/parallel relation.

## Structural identity

Each candidate is augmented with one artificial edge of unique colour `P`
between its external terminals. The implemented relation,
`colour-preserving-port-augmented-cycle-matroid-v1`, compares the complete
binary cycle spaces of these augmented graphs. Edge positions may be permuted
within the R, L, C, and P colour blocks; the unique P edge is therefore fixed.
The lexicographically least permuted cycle-space encoding is an exact
colour-preserving augmented cycle-matroid signature for these small graphs and
is the executable two-terminal 2-isomorphism contract.

The separately named representative descriptor canonicalizes internal node
labels, terminal reversal, undirected edge orientation, and parallel-edge
ordering. It selects an auditable primitive graph; it is not the structural
identity signature.

Each catalogue record also names the exact selected `source_assignment_id`,
`source_support_id`, and source support-edge count. The representative is
chosen by descriptor first, then by those stable source identifiers. These
fields are audit provenance for the selected graph only; they do not define
structural identity and do not contribute to the catalogue ID.

## Preliminary exclusions

Before a structural class is accepted, the generator rejects a same-colour
two-edge circuit among primitive edges, a same-colour two-edge cocircuit in the
augmented graph, or a multi-element all-resistor network. A single resistor is
retained. These matroid conditions express trivial same-kind parallel and
series pairs invariantly, without topology-specific exceptions.

| Stage | Structural classes |
|---|---:|
| Before exclusions | 366 |
| After same-kind parallel exclusion | 366 |
| After same-kind series exclusion | 149 |
| After multi-element all-resistor exclusion | 148 |

The simple-bundle source model generates no same-kind primitive parallel pair.
The series exclusion removes 217 structural classes, and the final resistor-only
exclusion removes one bridge class.

| Primitive elements | Classes |
|---:|---:|
| 1 | 3 |
| 2 | 6 |
| 3 | 16 |
| 4 | 38 |
| 5 | 85 |
| **Total** | **148** |

Eight records have four resistors and one reactive element. This is not the
RICE local-SP count, rational immittance equality, or the canonical Ladenheim
108 catalogue. Subsequent comparison work has accounted for all forty
exclusions and positively identified and numbered the 108 nonexcluded subjects
as canonical networks 1 through 108, without changing this structural count.
See `docs/comparisons/ladenheim-148-to-108.md` for the evidence contract and
detailed mapping. Independent reproduction of the 62 realizability-set classes,
basic-graph letters, and broader descriptor integration remain separate work.

Machine-readable catalogue: `data/counts/ladenheim-148.json`.

Regenerate or verify it from the repository root:

```bash
.venv/bin/python scripts/generate_ladenheim_148.py --write
.venv/bin/python scripts/generate_ladenheim_148.py --check
```

# 03-counting / 02 — Define “distinct network” precisely

Status: `todo`

## Goal

Define exactly what is being counted before generating counts.

## Questions to settle

- Are networks compared as terminal-labelled graphs?
- Are R elements indistinguishable from one another?
- Are L elements indistinguishable from one another?
- Are C elements indistinguishable from one another?
- Is L/C type part of the graph colouring?
- Are series and parallel reductions applied before counting?
- Are same-kind series/parallel combinations excluded as non-generic or reducible?
- Are open circuits, shorts, disconnected graphs, and dangling subgraphs excluded?
- Are networks equivalent under impedance identity, graph isomorphism, known transformations, or some staged combination of these?

## Working approach

Start with a conservative staged definition:

1. Generate connected two-terminal multigraph candidates.
2. Colour edges as R, L, or C.
3. Canonicalise under terminal-preserving graph isomorphism with edge colours.
4. Apply explicit rejection rules for disconnected, dangling, shorted, or trivially reducible forms.
5. Separately record stronger equivalences discovered by impedance identity or known network transformations.

## Done means

- The definition is written down before counts are treated as meaningful.
- Count tables state which equivalence relation they use.
- Tests encode the definition.

# Computation notes

## Object counted

The counted object is an isomorphism class of connected undirected two-terminal multigraphs.  The terminal pair is unordered.  Internal nodes are unlabelled.  Self-loops are excluded.  Parallel branches are allowed and are represented as component-count bundles on edges of a simple support graph.

For the main run the component budget is:

- `R <= 3`
- `L + C <= 5`

Therefore the largest possible number of physical branches is eight, and the largest possible number of simple support edges is also eight.

## Support graph enumeration

The code enumerates connected unlabelled simple graphs level by level by support-edge count.  From a graph at level `m - 1`, candidates at level `m` are made by either:

1. adding a new leaf vertex joined to one existing vertex, or
2. adding a missing edge between two existing vertices.

This generates all connected simple graphs.  Duplicates are removed using NetworkX isomorphism checks in buckets keyed by cheap invariants such as node count, edge count, degree sequence, and triangle count.

## Terminal relevance test

For every unordered node pair `(s, t)`, the code enumerates all simple paths from `s` to `t` and records the support edges used by those paths.  The terminal pair is retained only if the path-edge cover equals the full support-edge set.

This deliberately excludes branches that occur only in a terminal-to-terminal walk that repeats a vertex.  Such branches are not on any simple path and should not be part of the driving-point one-port core.

## Quotienting terminal choices

For each simple support graph, valid terminal pairs are quotiented by the automorphism group of the unterminalled support graph.  This gives one representative for each distinct two-terminal support topology.

For `R <= 3, reactive <= 5`, there are 383 two-terminal support topologies:

| Support edges | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 1 | 1 | 2 | 4 | 10 | 27 | 80 | 258 | 383 |

## Bundle assignment and Burnside's lemma

Each support edge receives a non-empty bundle:

- in generic mode: `(r, x)`;
- in L/C mode: `(r, l, c)`.

The total budget is applied after summing all support-edge bundles.

For each two-terminal support graph, the relevant group is the automorphism group preserving the terminal set.  Terminal swapping is allowed.  The group induces permutations of the support edges.

Burnside's lemma is then used to count bundle assignments up to this group action.  For an edge permutation, assignments fixed by that permutation must be constant on each cycle of the permutation.  The implementation performs a small dynamic-programming count over the cycle lengths and component budgets.

## Reference result

For `R <= 3, L + C <= 5`, with L and C distinct:

- exactly `R = 3`: 1,268,282;
- at most `R = 3`: 1,408,796.

For `R <= 3, X <= 5`, with all reactive elements treated as a generic `X`:

- exactly `R = 3`: 51,736;
- at most `R = 3`: 57,945.

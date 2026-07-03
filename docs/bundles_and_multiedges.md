# Bundles and multi-edges

This project counts two-terminal RLC network topologies by splitting each network into two parts:

1. a **simple support graph**, which records which nodes are connected to which other nodes; and
2. a **bundle** on each support edge, which records how many physical component branches of each type are placed in parallel between the same two support nodes.

This is the main device that lets the code count parallel branches without directly enumerating arbitrary multigraphs.

## Support edges versus physical branches

A **support graph** is a simple undirected graph. It has no self-loops and no repeated edges. If two support nodes are connected, there is exactly one support edge between them.

A **physical branch** is one actual circuit element: one resistor, one inductor, or one capacitor.

A **bundle** is the collection of physical branches that are all connected between the same two support nodes.

For example, a resistor and an inductor in parallel between terminals `s` and `t` are represented as:

```text
support graph:  s ---- t
bundle on s-t:  (r=1, l=1, c=0)
```

The support graph has one edge, but the physical circuit has two branches.

Likewise, three capacitors in parallel between the same two nodes are:

```text
support graph:  s ---- t
bundle on s-t:  (r=0, l=0, c=3)
```

The three capacitors are not represented as three separate support edges. They are one support edge with a three-capacitor bundle.

## Bundle forms used by the code

The project has two counting modes.

In `lc` mode, inductors and capacitors are distinct branch types. A bundle is:

```text
(r, l, c)
```

where:

- `r` is the number of resistors in that bundle;
- `l` is the number of inductors in that bundle;
- `c` is the number of capacitors in that bundle.

In `generic` mode, all reactive elements are collapsed into one generic type `X`. A bundle is:

```text
(r, x)
```

where `x` is the number of generic reactive branches.

Every support edge must receive a **non-empty** bundle. So these are valid bundles in `lc` mode:

```text
(1, 0, 0)     one resistor
(0, 1, 0)     one inductor
(0, 0, 1)     one capacitor
(1, 1, 0)     one resistor in parallel with one inductor
(0, 2, 1)     two inductors in parallel with one capacitor
```

but this is not a valid bundle on an existing support edge:

```text
(0, 0, 0)     no branch at all
```

An absent connection is represented by the absence of a support edge, not by an empty bundle.

## What is counted as distinct inside one bundle?

The bundle records only the **counts** of the branch types. It does not record an ordering of branches.

Therefore, these drawings are the same topology:

```text
s == R == t       and       s == L == t
s == L == t                 s == R == t
```

Both are simply:

```text
(r=1, l=1, c=0)
```

Similarly, two parallel capacitors form one bundle:

```text
(r=0, l=0, c=2)
```

There is no distinction between “capacitor 1 above capacitor 2” and “capacitor 2 above capacitor 1”. Physical component identities, drawing order, lead order, and layout position are not part of the topology.

Component **values** are also not counted. A bundle with two capacitors is counted as one topological case, not as separate cases for different capacitance values.

## What is counted as distinct between bundles?

Different bundle contents are distinct if they are placed on support edges that cannot be mapped to one another by a symmetry of the two-terminal support graph.

For example, consider a three-edge chain:

```text
s ---- a ---- b ---- t
```

The end edges are symmetric under terminal reversal, but the middle edge is different. So placing a two-component parallel bundle on an end edge is not the same as placing it on the middle edge.

These are distinct:

```text
s ==RL== a ---- b ---- t
```

and:

```text
s ---- a ==RL== b ---- t
```

But these two are the same, because the terminal pair is unordered and the whole network may be reversed:

```text
s ==RL== a ---- b ---- t
```

and:

```text
s ---- a ---- b ==RL== t
```

The code handles this by computing support-graph automorphisms that preserve the terminal set. Terminal interchange is allowed.

## Parallel versus series is still distinct

A bundle means parallel components between the same two nodes. It does not mean a small internal circuit hidden inside a branch.

So a parallel `R` and `L` between the terminals is:

```text
s ==RL== t
```

which is one support edge with bundle:

```text
(1, 1, 0)
```

A series `R` followed by `L` is different:

```text
s ---- R ---- a ---- L ---- t
```

which is a two-edge support graph with bundles:

```text
s-a: (1, 0, 0)
a-t: (0, 1, 0)
```

Those two networks are counted separately.

## Examples of what is not counted separately

The following are not distinct topologies in the current model:

1. swapping two identical components in the same parallel bundle;
2. swapping the drawing order of different components in the same bundle;
3. renumbering internal nodes;
4. reversing the two terminal nodes;
5. moving bundles between support edges related by a terminal-preserving symmetry;
6. assigning different physical values to otherwise identical component-type branches;
7. changing a drawing layout without changing the graph.

For example, this single support-edge bundle:

```text
(r=1, l=2, c=1)
```

is counted once, not as the many possible visual orders:

```text
R, L, L, C
L, R, L, C
L, L, R, C
C, L, L, R
...
```

## Examples of what is counted separately

The following are distinct in `lc` mode:

```text
(r=0, l=2, c=0)     two inductors in parallel
(r=0, l=1, c=1)     one inductor and one capacitor in parallel
(r=0, l=0, c=2)     two capacitors in parallel
```

They all have two reactive elements, so they contribute to the same `L+C = 2` column in the published results table, but they are distinct internal cases.

By contrast, in `generic` mode all three collapse to:

```text
(r=0, x=2)
```

This is why the `lc` counts are much larger than the `generic` counts.

## Why count bundles on a simple support graph?

The alternative would be to enumerate multigraphs directly. That is more awkward because every pair of nodes might be connected by zero, one, two, three, or more parallel branches, and each branch has a component type.

The support-and-bundle representation factors the problem:

1. enumerate the simple support graph once;
2. put a non-empty branch bundle on each support edge;
3. quotient the resulting assignments by graph symmetries.

This keeps the topology model explicit:

```text
support edge present      <=> at least one physical branch exists
bundle size               <=> number of parallel branches between those nodes
bundle type counts         <=> R/L/C composition of those parallel branches
```

It also makes the component budgets straightforward. For `R <= 3, L+C <= 5`, the total contribution of all bundles must satisfy:

```text
sum_e r_e <= 3
sum_e (l_e + c_e) <= 5
```

The maximum number of physical branches is therefore eight. The maximum number of support edges is also eight, occurring only when every support edge has a one-component bundle.

## Why Burnside's lemma is used

After a support graph is chosen, the code still has to count bundle assignments on its support edges. Some assignments that look different edge-by-edge are actually the same network because the support graph has symmetries.

For example, the two-edge series chain:

```text
s ---- a ---- t
```

has a terminal-reversing symmetry that swaps the two support edges. Therefore the assignment:

```text
s-a: A
a-t: B
```

is the same as:

```text
s-a: B
a-t: A
```

where `A` and `B` are bundles.

Burnside's lemma gives a clean way to count these assignments without listing every assignment and then removing duplicates one by one.

For a finite symmetry group `G`, Burnside's lemma says:

```text
number of distinct assignments = average number of assignments fixed by a symmetry
```

or, more formally:

```text
number of orbits = (1 / |G|) * sum_{g in G} |Fix(g)|
```

Here:

- `G` is the automorphism group of the support graph that preserves the unordered terminal pair;
- an “assignment” means choosing one non-empty bundle for each support edge;
- `Fix(g)` is the set of bundle assignments unchanged by the symmetry `g`.

## Fixed assignments and edge cycles

Each graph symmetry induces a permutation of the support edges. For an assignment to be fixed by that symmetry, every edge in the same permutation cycle must receive the same bundle.

For example, suppose a symmetry swaps two support edges and leaves a third edge alone. Its edge cycles have lengths:

```text
2, 1
```

A fixed assignment must look like:

```text
edge 1: A
edge 2: A
edge 3: B
```

not:

```text
edge 1: A
edge 2: C
edge 3: B
```

because the swapped edges must match.

This is why the code reduces each edge permutation to its cycle lengths. If a cycle has length `k`, then choosing bundle `(r, l, c)` on that cycle consumes:

```text
(k*r, k*l, k*c)
```

from the total component budget.

The dynamic-programming routine `fixed_assignments_by_total` counts how many fixed assignments are possible for each total `(R, L+C)` budget and each list of edge-cycle lengths.

## Small Burnside example

Suppose there are only two support edges, and the graph symmetry group either:

1. does nothing, or
2. swaps the two edges.

Let there be `n` possible bundle choices under some small budget, ignoring the budget interaction for the moment.

The identity symmetry fixes all ordered choices:

```text
(A, B)
```

so it fixes `n^2` assignments.

The swap symmetry only fixes assignments where both edges have the same bundle:

```text
(A, A)
```

so it fixes `n` assignments.

Burnside gives:

```text
(n^2 + n) / 2
```

which is exactly the number of unordered pairs of bundles with repetition allowed.

The real project does the same thing, but with:

- arbitrary small support graphs;
- automorphism groups that may have several symmetries;
- edge permutations with several cycle lengths;
- component budgets `R <= max_r` and `L+C <= max_reactive`.

## Relationship to the published result table

In `lc` mode the code counts assignments using full `(r, l, c)` bundles. After counting, it aggregates the output table by:

```text
R = total number of resistors
X = L + C = total number of reactive elements
```

So a table entry such as:

```text
R = 1, L+C = 3
```

includes all distinct topologies and all distinct L/C splittings having one resistor and three total reactive elements.

That aggregation is only in the presentation of the result. Internally, the code still distinguishes inductors from capacitors when `mode="lc"`.

## Summary

A project “multi-edge” is not stored as several parallel support edges. It is stored as one support edge with a non-empty bundle of parallel physical branches.

The count distinguishes different support topology, different branch-type counts in a bundle, and non-equivalent placements of bundles on the support graph. It does not distinguish branch ordering, internal-node names, terminal reversal, physical component identity, or component values.

Burnside's lemma is used because graph symmetries can make two apparently different bundle placements represent the same two-terminal network.

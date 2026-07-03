# Connectivity, Simple-Path Coverage, and Edge Deletion

This note documents the graph-theoretic relevance test used by the RLC one-port topology counter. It explains why plain connectedness is too weak, why a simple edge-deletion test is not sufficient, and why the project uses terminal-to-terminal simple-path coverage as the intended core criterion.

The intended object counted by the project is not merely a connected graph with two terminals. It is a connected two-terminal network in which every branch belongs to the active one-port core: every branch must be capable of participating in at least one path by which current can pass from one terminal to the other.

Throughout this note, let the two terminal nodes be denoted by `s` and `t`.

## 1. Connectivity

A graph is **connected** if every node can be reached from every other node.

For example, the following graph is connected:

```text
s ---- a ---- t
       |
       x
```

Every node is reachable from every other node, so the graph passes a connectivity test. But the branch `a-x` is a dangling appendage. It cannot carry current in an ideal passive driving-point one-port, because it is not part of any route from `s` to `t`.

So connectedness is necessary, but not sufficient.

In the project, connectedness is only a coarse first filter. A stricter terminal-relevance test is then applied.

## 2. Simple terminal-to-terminal paths

A **simple path** from `s` to `t` is a path that starts at `s`, ends at `t`, and does not repeat vertices.

The project keeps a support graph only if:

> Every support edge lies on at least one simple path from `s` to `t`.

Equivalently, every branch in the network must be part of at least one non-self-intersecting terminal-to-terminal route.

This series network is valid:

```text
s ---- a ---- t
```

Both edges lie on the simple path:

```text
s, a, t
```

This parallel/cyclic network is also valid:

```text
      a
     / \
s ---   --- t
     \ /
      b
```

Every edge lies on one of the simple paths `s-a-t` or `s-b-t`.

By contrast, this graph is not valid:

```text
s ---- a ---- t
       |
       x
```

The edge `a-x` lies on no simple `s-t` path.

The test also excludes pendant cycles or pendant blobs. For example:

```text
s ---- a ---- t
       |\
       | \
       b--c
```

The triangle `a-b-c-a` is connected to the rest of the network, but only through the articulation vertex `a`. To traverse an edge in the triangle and still get from `s` to `t`, a walk would have to enter the triangle at `a` and later return to `a`, repeating `a`. That is a walk, but not a simple path.

Therefore the edges in the pendant triangle are not part of the terminal one-port core and the support graph is rejected.

## 3. Edge deletion

A tempting relevance test is:

> Delete edge `e`. If `s` and `t` become disconnected, then `e` matters.

This identifies terminal bridges. For example:

```text
s ---- a ---- t
```

Deleting either edge disconnects `s` from `t`, so each edge is clearly relevant.

However, this implication only works in one direction:

```text
edge deletion disconnects s and t  =>  edge is relevant
```

The converse is false.

For example, in this network:

```text
      a
     / \
s ---   --- t
     \ /
      b
```

Deleting the edge `s-a` does not disconnect the terminals, because `s-b-t` remains. But `s-a` is still a relevant branch, because it lies on the simple path `s-a-t`.

So:

```text
edge deletion does not disconnect s and t  =>  inconclusive
```

The edge might be a legitimate branch in a cycle, or it might be irrelevant material in a pendant cycle.

For example, in the pendant-triangle graph:

```text
s ---- a ---- t
       |\
       | \
       b--c
```

Deleting the edge `b-c` does not disconnect `s` from `t`, but `b-c` is not relevant to the one-port impedance.

A pure edge-deletion test is therefore too crude.

## 4. Criterion used by the project

The project applies simple terminal-path coverage:

```python
used_edges = union of edges appearing in all simple paths from s to t
valid = used_edges == all_edges
```

In words:

> Keep a two-terminal support graph only if every edge is used by at least one simple terminal-to-terminal path.

This accepts series edges and bridge edges, because they lie on the unique terminal path. It also accepts cyclic alternatives, because each edge can lie on at least one terminal path. It rejects dangling trees and pendant blobs, because their edges are not on any simple terminal path.

## 5. Biconnected-component equivalent

There is a useful equivalent graph-theoretic formulation.

1. Add a temporary artificial edge directly between the terminals `s` and `t`.
2. Find the biconnected component containing that artificial edge.
3. Remove the artificial edge.
4. Check whether all original edges lie in that same biconnected component.

If they do, then every original edge lies on at least one simple path between `s` and `t`.

For a series chain:

```text
s ---- a ---- b ---- t
```

adding the artificial terminal edge gives:

```text
s ---- a ---- b ---- t
|                   |
+-------------------+
```

All original edges now lie in the same biconnected component as the artificial edge, so the series chain is accepted.

For the pendant-triangle graph:

```text
s ---- a ---- t
       |\
       | \
       b--c
```

adding the artificial edge `s-t` puts the main terminal path edges in the terminal biconnected component, but the pendant triangle remains outside it. The support graph is therefore rejected.

This formulation is often more efficient and elegant than explicitly enumerating all simple paths, especially as the graph size grows.

## 6. Why this matters for circuit enumeration

A connected graph can contain electrically irrelevant material. A dangling resistor, inductor, capacitor, tree, or pendant subnetwork attached through a single articulation node does not affect the ideal driving-point impedance seen between the terminals.

Counting such material as a distinct topology would inflate the enumeration with graphs that are connected but not distinct one-port cores.

The intended counting object is therefore:

```text
connected two-terminal graph whose every branch is part of the terminal one-port core
```

Simple terminal-to-terminal path coverage is the rule used by this project to capture that object.

## 7. Relationship to support graphs and labelled branches

The test is applied to the **support graph** before assigning branch multiplicities and element labels.

A support edge may later represent one or more parallel branches, each with a type such as `R`, `L`, or `C`. The support graph test asks only whether the underlying connection between two nodes belongs to the terminal one-port core.

Once a support graph passes this relevance test, the counting code assigns branch compositions and quotients those assignments by the automorphism group of the support graph.


"""Count small two-terminal RLC one-port network topologies.

The counting model is graph-theoretic.  A network is represented by an
undirected connected multigraph between two terminal nodes, with branches
labelled by component type.  The implementation counts isomorphism classes by
first enumerating simple support graphs and then using Burnside's lemma to
count labelled parallel bundles on the support edges.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import DefaultDict, Iterable, Literal

import networkx as nx
from networkx.algorithms import isomorphism as iso

Mode = Literal["lc", "generic"]


@dataclass(frozen=True)
class CountResult:
    """Result returned by :func:`count_networks`.

    Attributes:
        max_r: Maximum total number of resistors.
        max_reactive: Maximum total number of reactive elements.
        mode: ``"lc"`` distinguishes inductors and capacitors. ``"generic"``
            treats all reactive elements as one type ``X``.
        table: A rectangular table indexed by ``table[r][x]``, where ``x`` is
            total reactive count.  For ``mode="lc"`` the count sums over all
            L/C splittings with ``l + c == x``.
        support_count: Number of distinct simple two-terminal support graphs.
        support_count_by_edges: Counts of support graphs by number of support
            edges.
    """

    max_r: int
    max_reactive: int
    mode: Mode
    table: tuple[tuple[int, ...], ...]
    support_count: int
    support_count_by_edges: dict[int, int]

    @property
    def total(self) -> int:
        return sum(sum(row) for row in self.table)

    def row_total(self, r: int) -> int:
        return sum(self.table[r])

    def exactly_r_total(self, r: int) -> int:
        return self.row_total(r)

    def as_markdown_table(self) -> str:
        headers = ["R \\ X"] + [str(x) for x in range(self.max_reactive + 1)] + ["Row total"]
        lines = ["| " + " | ".join(headers) + " |"]
        lines.append("|" + "---:|" * len(headers))
        for r, row in enumerate(self.table):
            values = [str(r)] + [str(v) for v in row] + [str(sum(row))]
            lines.append("| " + " | ".join(values) + " |")
        return "\n".join(lines)


def graph_invariant(graph: nx.Graph) -> tuple[object, ...]:
    """Cheap invariant used to bucket candidate simple graphs.

    Isomorphism testing is still used inside each bucket, so this does not need
    to be a complete canonical form.
    """

    degree_sequence = tuple(sorted(dict(graph.degree()).values()))
    triangle_count = sum(nx.triangles(graph).values()) // 3 if graph.number_of_nodes() > 2 else 0
    return (graph.number_of_nodes(), graph.number_of_edges(), degree_sequence, triangle_count)


def _add_unique(bucketed_graphs: DefaultDict[tuple[object, ...], list[nx.Graph]], graph: nx.Graph) -> bool:
    key = graph_invariant(graph)
    for existing in bucketed_graphs[key]:
        if nx.is_isomorphic(graph, existing):
            return False
    bucketed_graphs[key].append(graph.copy())
    return True


def generate_connected_unlabelled_simple_graphs(max_edges: int) -> list[list[nx.Graph]]:
    """Generate connected unlabelled simple graphs with up to ``max_edges``.

    ``levels[m]`` contains one representative for every connected unlabelled
    simple graph with exactly ``m`` edges.  The method uses canonical
    augmentation in a pragmatic form: every connected graph can be obtained by
    repeatedly adding either a missing edge between existing vertices or a new
    leaf edge, and duplicates are removed by graph isomorphism.
    """

    levels: list[list[nx.Graph]] = []
    initial = nx.Graph()
    initial.add_node(0)
    levels.append([initial])

    for edge_count in range(1, max_edges + 1):
        bucketed: DefaultDict[tuple[object, ...], list[nx.Graph]] = defaultdict(list)
        for graph in levels[edge_count - 1]:
            nodes = sorted(graph.nodes())
            new_node = max(nodes) + 1

            # Add a new vertex joined by one edge.  This is enough to grow any
            # connected graph alongside adding missing edges between old nodes.
            for node in nodes:
                candidate = graph.copy()
                candidate.add_node(new_node)
                candidate.add_edge(node, new_node)
                _add_unique(bucketed, candidate)

            # Add any missing simple edge between existing vertices.
            for i, u in enumerate(nodes):
                for v in nodes[i + 1 :]:
                    if not graph.has_edge(u, v):
                        candidate = graph.copy()
                        candidate.add_edge(u, v)
                        _add_unique(bucketed, candidate)

        levels.append([graph for graphs in bucketed.values() for graph in graphs])

    return levels


def automorphisms(graph: nx.Graph) -> list[dict[int, int]]:
    return list(iso.GraphMatcher(graph, graph).isomorphisms_iter())


def simple_path_edge_cover(graph: nx.Graph, source: int, target: int) -> set[tuple[int, int]]:
    """Return the support edges lying on at least one simple source-target path."""

    used: set[tuple[int, int]] = set()
    for path in nx.all_simple_paths(graph, source, target, cutoff=graph.number_of_nodes() - 1):
        for u, v in zip(path, path[1:]):
            used.add(tuple(sorted((u, v))))
    return used


def is_two_terminal_relevant(graph: nx.Graph, source: int, target: int) -> bool:
    """Check whether every support edge lies on a simple terminal-terminal path.

    This removes dangling appendages and other branches that are not part of the
    driving-point one-port core.  It is deliberately implemented by enumerating
    simple terminal paths, rather than by a merely connectedness-based bridge
    test, because connectedness alone incorrectly admits edges on non-simple
    walks.
    """

    all_edges = {tuple(sorted(edge)) for edge in graph.edges()}
    return simple_path_edge_cover(graph, source, target) == all_edges


def terminal_pair_orbit_representatives(
    graph: nx.Graph, graph_automorphisms: Iterable[dict[int, int]]
) -> list[tuple[int, int]]:
    """Return unordered terminal-pair representatives for a support graph."""

    autos = list(graph_automorphisms)
    valid_pairs: list[tuple[int, int]] = []
    for source, target in combinations(sorted(graph.nodes()), 2):
        if is_two_terminal_relevant(graph, source, target):
            valid_pairs.append((source, target))

    valid_set = set(valid_pairs)
    representatives: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()

    for pair in valid_pairs:
        if pair in seen:
            continue
        a, b = pair
        orbit = {
            tuple(sorted((mapping[a], mapping[b])))
            for mapping in autos
            if tuple(sorted((mapping[a], mapping[b]))) in valid_set
        }
        seen |= orbit
        representatives.append(min(orbit))

    return representatives


def edge_permutations_preserving_terminal_set(
    graph: nx.Graph,
    terminals: tuple[int, int],
    graph_automorphisms: Iterable[dict[int, int]],
) -> list[tuple[int, ...]]:
    """Return induced edge permutations for automorphisms preserving terminals setwise.

    Terminals are treated as an unordered pair.  Therefore an automorphism may
    either fix the terminal nodes individually or swap them.
    """

    source, target = terminals
    terminal_set = {source, target}
    edge_list = sorted(tuple(sorted(edge)) for edge in graph.edges())
    edge_index = {edge: i for i, edge in enumerate(edge_list)}

    permutations: list[tuple[int, ...]] = []
    seen: set[tuple[int, ...]] = set()

    for mapping in graph_automorphisms:
        if {mapping[source], mapping[target]} != terminal_set:
            continue
        permutation = []
        for u, v in edge_list:
            image_edge = tuple(sorted((mapping[u], mapping[v])))
            permutation.append(edge_index[image_edge])
        permutation_tuple = tuple(permutation)
        if permutation_tuple not in seen:
            seen.add(permutation_tuple)
            permutations.append(permutation_tuple)

    return permutations


def permutation_cycle_lengths(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(permutation)
    lengths: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        node = start
        length = 0
        while not seen[node]:
            seen[node] = True
            length += 1
            node = permutation[node]
        lengths.append(length)
    return tuple(sorted(lengths))


def fixed_assignments_by_total(
    cycle_lengths: tuple[int, ...],
    max_r: int,
    max_reactive: int,
    mode: Mode,
) -> dict[tuple[int, int], int]:
    """Count assignments fixed by an edge permutation with given cycle lengths.

    Burnside's lemma reduces the orbit count to fixed assignments under each
    automorphism.  An assignment fixed on a cycle of support edges must put the
    same non-empty branch bundle on every edge in that cycle.
    """

    if mode == "generic":
        dp: dict[tuple[int, int], int] = {(0, 0): 1}
        for cycle_length in cycle_lengths:
            next_dp: DefaultDict[tuple[int, int], int] = defaultdict(int)
            options = [
                (r, x)
                for r in range(max_r // cycle_length + 1)
                for x in range(max_reactive // cycle_length + 1)
                if r + x > 0
            ]
            for (old_r, old_x), count in dp.items():
                for r, x in options:
                    new_r = old_r + cycle_length * r
                    new_x = old_x + cycle_length * x
                    if new_r <= max_r and new_x <= max_reactive:
                        next_dp[(new_r, new_x)] += count
            dp = dict(next_dp)
        return dp

    if mode != "lc":
        raise ValueError(f"unknown mode {mode!r}; expected 'lc' or 'generic'")

    dp_lc: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    for cycle_length in cycle_lengths:
        next_dp_lc: DefaultDict[tuple[int, int, int], int] = defaultdict(int)
        options_lc = [
            (r, l, c)
            for r in range(max_r // cycle_length + 1)
            for l in range(max_reactive // cycle_length + 1)
            for c in range(max_reactive // cycle_length + 1)
            if r + l + c > 0 and cycle_length * (l + c) <= max_reactive
        ]
        for (old_r, old_l, old_c), count in dp_lc.items():
            for r, l, c in options_lc:
                new_r = old_r + cycle_length * r
                new_l = old_l + cycle_length * l
                new_c = old_c + cycle_length * c
                if new_r <= max_r and new_l + new_c <= max_reactive:
                    next_dp_lc[(new_r, new_l, new_c)] += count
        dp_lc = dict(next_dp_lc)

    aggregated: DefaultDict[tuple[int, int], int] = defaultdict(int)
    for (r, l, c), count in dp_lc.items():
        aggregated[(r, l + c)] += count
    return dict(aggregated)


def iter_two_terminal_supports(max_edges: int):
    """Yield ``(graph, terminal_pair, automorphisms)`` support representatives."""

    levels = generate_connected_unlabelled_simple_graphs(max_edges)
    for edge_count in range(1, max_edges + 1):
        for graph in levels[edge_count]:
            autos = automorphisms(graph)
            for terminals in terminal_pair_orbit_representatives(graph, autos):
                yield graph, terminals, autos


def count_networks(max_r: int = 3, max_reactive: int = 5, mode: Mode = "lc") -> CountResult:
    """Count two-terminal network topologies under the documented assumptions."""

    if max_r < 0 or max_reactive < 0:
        raise ValueError("component limits must be non-negative")
    if mode not in {"lc", "generic"}:
        raise ValueError("mode must be 'lc' or 'generic'")

    max_edges = max_r + max_reactive
    counts: DefaultDict[tuple[int, int], int] = defaultdict(int)
    support_count = 0
    support_count_by_edges: Counter[int] = Counter()
    fixed_count_cache: dict[tuple[tuple[int, ...], int, int, Mode], dict[tuple[int, int], int]] = {}

    for graph, terminals, autos in iter_two_terminal_supports(max_edges):
        support_count += 1
        support_count_by_edges[graph.number_of_edges()] += 1
        edge_permutations = edge_permutations_preserving_terminal_set(graph, terminals, autos)
        group_size = len(edge_permutations)
        burnside_sum: DefaultDict[tuple[int, int], int] = defaultdict(int)

        for permutation in edge_permutations:
            cycle_lengths = permutation_cycle_lengths(permutation)
            cache_key = (cycle_lengths, max_r, max_reactive, mode)
            fixed_counts = fixed_count_cache.get(cache_key)
            if fixed_counts is None:
                fixed_counts = fixed_assignments_by_total(cycle_lengths, max_r, max_reactive, mode)
                fixed_count_cache[cache_key] = fixed_counts
            for total_key, count in fixed_counts.items():
                burnside_sum[total_key] += count

        for total_key, count in burnside_sum.items():
            if count % group_size != 0:
                raise ArithmeticError(
                    f"Burnside sum {count} is not divisible by group size {group_size} for {total_key}"
                )
            counts[total_key] += count // group_size

    table = tuple(
        tuple(counts.get((r, x), 0) for x in range(max_reactive + 1)) for r in range(max_r + 1)
    )

    return CountResult(
        max_r=max_r,
        max_reactive=max_reactive,
        mode=mode,
        table=table,
        support_count=support_count,
        support_count_by_edges=dict(sorted(support_count_by_edges.items())),
    )

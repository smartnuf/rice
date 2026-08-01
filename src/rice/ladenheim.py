"""Structural primitive-network catalogue for the Ladenheim 148 starting set.

This module deliberately does not use RICE's local series/parallel reduced
signature.  Its named identity relation is the edge-coloured cycle matroid of
the primitive graph after adding one uniquely coloured edge across the port.
For the at-most-five-component scope an exhaustive cycle-space canonical form
is both exact and inspectable.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
import json
from typing import Iterable

import networkx as nx

from .core import (
    AssignmentRecord,
    CountQuery,
    SupportRecord,
    enum_assignments,
    enum_supports,
)


RELATION_NAME = "colour-preserving-port-augmented-cycle-matroid-v1"
FORMAT_VERSION = 1
COLOUR_ORDER = {"R": 0, "L": 1, "C": 2, "P": 3}


@dataclass(frozen=True, order=True)
class PrimitiveEdge:
    """One undirected, individually typed primitive component edge."""

    u: object
    v: object
    colour: str

    def __post_init__(self) -> None:
        if self.u == self.v:
            raise ValueError("primitive edges may not be loops")
        if self.colour not in {"R", "L", "C"}:
            raise ValueError("primitive edge colour must be R, L, or C")


@dataclass(frozen=True)
class PrimitiveNetwork:
    """Connected terminal-relevant primitive RLC multigraph."""

    terminals: tuple[object, object]
    edges: tuple[PrimitiveEdge, ...]

    def __post_init__(self) -> None:
        if self.terminals[0] == self.terminals[1]:
            raise ValueError("terminals must be distinct")
        graph = self.graph()
        if not nx.is_connected(graph):
            raise ValueError("primitive network must be connected")
        for index in range(len(self.edges)):
            if not _edge_lies_on_terminal_path(self, index):
                raise ValueError(
                    "every primitive edge must be terminal-relevant"
                )

    def graph(self) -> nx.MultiGraph:
        graph = nx.MultiGraph()
        graph.add_nodes_from(self.terminals)
        for index, edge in enumerate(self.edges):
            graph.add_edge(edge.u, edge.v, key=index, colour=edge.colour)
        return graph

    @property
    def counts(self) -> tuple[int, int, int]:
        counts = Counter(edge.colour for edge in self.edges)
        return counts["R"], counts["L"], counts["C"]


@dataclass(frozen=True)
class StructuralSignature:
    """Exact canonical form of a port-augmented coloured graphic matroid."""

    relation: str
    multiplicities: tuple[int, int, int, int]
    cycle_space: tuple[int, ...]

    def stable_string(self) -> str:
        resistors, inductors, capacitors, port_edges = self.multiplicities
        cycles = ",".join(format(value, "x") for value in self.cycle_space)
        counts = f"R{resistors}L{inductors}C{capacitors}P{port_edges}"
        return f"{self.relation}|{counts}|{cycles}"


def _edge_lies_on_terminal_path(
    network: PrimitiveNetwork, edge_index: int
) -> bool:
    edge = network.edges[edge_index]
    graph = nx.Graph(network.graph())
    s, t = network.terminals
    return any(
        any(
            {left, right} == {edge.u, edge.v}
            for left, right in zip(path, path[1:])
        )
        for path in nx.all_simple_paths(graph, s, t)
    )


def _edge_rows(
    network: PrimitiveNetwork,
) -> tuple[tuple[object, object, str], ...]:
    rows = [(edge.u, edge.v, edge.colour) for edge in network.edges]
    rows.append((network.terminals[0], network.terminals[1], "P"))
    return tuple(rows)


def _cycle_space(
    rows: tuple[tuple[object, object, str], ...],
) -> tuple[int, ...]:
    """Return all binary cycle-space vectors in the supplied edge order."""

    vertices = set()
    for u, v, _colour in rows:
        vertices.update((u, v))
    result = []
    for mask in range(1 << len(rows)):
        parity = {vertex: 0 for vertex in vertices}
        for index, (u, v, _colour) in enumerate(rows):
            if mask & (1 << index):
                parity[u] ^= 1
                parity[v] ^= 1
        if not any(parity.values()):
            result.append(mask)
    return tuple(result)


def canonical_structural_signature(
    network: PrimitiveNetwork,
) -> StructuralSignature:
    """Canonicalize colour-preserving port-augmented graphic 2-isomorphism.

    The complete GF(2) cycle space determines a binary matroid.  Edge positions
    may be permuted only within the R, L, C, and P colour blocks; P occurs once
    and therefore fixes the artificial port edge.  Equality of the returned
    value is the executable historical structural relation used here.
    """

    rows = _edge_rows(network)
    ordered_indices = tuple(
        sorted(range(len(rows)), key=lambda i: (COLOUR_ORDER[rows[i][2]], i))
    )
    ordered_rows = tuple(rows[i] for i in ordered_indices)
    base_space = _cycle_space(ordered_rows)
    blocks: list[tuple[int, ...]] = []
    for colour in ("R", "L", "C", "P"):
        blocks.append(
            tuple(i for i, row in enumerate(ordered_rows) if row[2] == colour)
        )

    best: tuple[int, ...] | None = None
    block_permutations = [tuple(permutations(block)) for block in blocks]
    for choices in product(*block_permutations):
        old_at_new = tuple(index for block in choices for index in block)
        encoded = []
        for vector in base_space:
            permuted = 0
            for new_index, old_index in enumerate(old_at_new):
                if vector & (1 << old_index):
                    permuted |= 1 << new_index
            encoded.append(permuted)
        candidate = tuple(sorted(encoded))
        if best is None or candidate < best:
            best = candidate
    counts = Counter(row[2] for row in ordered_rows)
    return StructuralSignature(
        RELATION_NAME,
        (counts["R"], counts["L"], counts["C"], counts["P"]),
        best or (0,),
    )


def representative_descriptor(network: PrimitiveNetwork) -> str:
    """Canonical primitive graph descriptor, separate from 2-isomorphism."""

    s, t = network.terminals
    internal = sorted(set(network.graph()) - {s, t}, key=repr)
    best: tuple[tuple[int, int, str], ...] | None = None
    for reverse in (False, True):
        terminal_map = {s: int(reverse), t: int(not reverse)}
        for internal_order in permutations(internal):
            mapping = dict(terminal_map)
            mapping.update(
                {node: index + 2 for index, node in enumerate(internal_order)}
            )
            rows = tuple(
                sorted(
                    (
                        min(mapping[e.u], mapping[e.v]),
                        max(mapping[e.u], mapping[e.v]),
                        e.colour,
                    )
                    for e in network.edges
                )
            )
            if best is None or rows < best:
                best = rows
    assert best is not None
    return ";".join(f"{u}-{v}:{colour}" for u, v, colour in best)


def network_from_descriptor(descriptor: str) -> PrimitiveNetwork:
    edges = []
    for item in descriptor.split(";"):
        endpoints, colour = item.split(":")
        u, v = (int(value) for value in endpoints.split("-"))
        edges.append(PrimitiveEdge(u, v, colour))
    return PrimitiveNetwork((0, 1), tuple(edges))


def has_same_kind_parallel_pair(network: PrimitiveNetwork) -> bool:
    seen: set[tuple[frozenset[object], str]] = set()
    for edge in network.edges:
        key = (frozenset((edge.u, edge.v)), edge.colour)
        if key in seen:
            return True
        seen.add(key)
    return False


def has_same_kind_series_pair(network: PrimitiveNetwork) -> bool:
    """Whether the augmented graphic matroid has a same-colour 2-cocircuit."""

    rows = _edge_rows(network)
    graph = nx.MultiGraph()
    for index, (u, v, colour) in enumerate(rows):
        graph.add_edge(u, v, key=index, colour=colour)
    base_components = nx.number_connected_components(graph)
    for left in range(len(network.edges)):
        for right in range(left + 1, len(network.edges)):
            if rows[left][2] != rows[right][2]:
                continue
            one = graph.copy()
            one.remove_edge(rows[left][0], rows[left][1], key=left)
            two = graph.copy()
            two.remove_edge(rows[right][0], rows[right][1], key=right)
            both = graph.copy()
            both.remove_edge(rows[left][0], rows[left][1], key=left)
            both.remove_edge(rows[right][0], rows[right][1], key=right)
            if (
                nx.number_connected_components(one) == base_components
                and nx.number_connected_components(two) == base_components
                and nx.number_connected_components(both) > base_components
            ):
                return True
    return False


def preliminary_rejection(network: PrimitiveNetwork) -> str | None:
    if has_same_kind_parallel_pair(network):
        return "same-kind-parallel-pair"
    if has_same_kind_series_pair(network):
        return "same-kind-series-pair"
    resistors, inductors, capacitors = network.counts
    if resistors > 1 and inductors + capacitors == 0:
        return "multi-element-all-resistor"
    return None


def _expand_assignment(
    edge_assignments: Iterable[tuple[tuple[int, int], str]],
) -> PrimitiveNetwork:
    edges = []
    for (u, v), label in edge_assignments:
        edges.extend(
            PrimitiveEdge(u, v, colour) for colour in label.split("||")
        )
    return PrimitiveNetwork((0, 1), tuple(edges))


def _primitive_network_from_source(
    assignment: AssignmentRecord, support: SupportRecord
) -> PrimitiveNetwork:
    """Expand one exact source assignment on its referenced support."""

    if assignment.support_id != support.support_id:
        raise ValueError("assignment and support identifiers do not match")
    expanded = _expand_assignment(assignment.edge_assignments)
    return PrimitiveNetwork(support.terminals, expanded.edges)


def generate_ladenheim_148_catalogue() -> dict[str, object]:
    """Generate the deterministic structural catalogue and provenance."""

    query = CountQuery(profile="ladenheim-structural-region")
    assignments = enum_assignments(query, max_records=2_000)
    supports = {record.support_id: record for record in enum_supports(query)}
    classes: dict[str, dict[str, object]] = {}
    generated_forms: set[tuple[str, str]] = set()
    rejected_candidates: Counter[str] = Counter()
    signatures_by_rejection: defaultdict[str, set[str]] = defaultdict(set)
    for assignment in assignments:
        support = supports[assignment.support_id]
        network = _primitive_network_from_source(assignment, support)
        signature = canonical_structural_signature(network).stable_string()
        descriptor = representative_descriptor(network)
        generated_forms.add((signature, descriptor))
        rejection = preliminary_rejection(network)
        if rejection is not None:
            rejected_candidates[rejection] += 1
            signatures_by_rejection[rejection].add(signature)
            continue
        bucket = classes.setdefault(
            signature, {"candidates": 0, "forms": set(), "representatives": []}
        )
        bucket["candidates"] = int(bucket["candidates"]) + 1
        bucket["forms"].add(descriptor)  # type: ignore[union-attr]
        bucket["representatives"].append(  # type: ignore[union-attr]
            (
                descriptor,
                assignment.assignment_id,
                assignment.support_id,
                assignment.source_support_edges,
            )
        )

    records = []
    for signature, bucket in classes.items():
        descriptor, assignment_id, support_id, support_edges = min(
            bucket["representatives"]  # type: ignore[arg-type]
        )
        network = network_from_descriptor(descriptor)
        resistors, inductors, capacitors = network.counts
        digest = sha256(signature.encode("ascii")).hexdigest()[:16]
        catalogue_id = "lh148-" + digest
        records.append(
            {
                "catalogue_id": catalogue_id,
                "relation": RELATION_NAME,
                "canonical_structural_signature": signature,
                "representative_descriptor": descriptor,
                "terminals": [0, 1],
                "primitive_edges": [
                    {"u": edge.u, "v": edge.v, "type": edge.colour}
                    for edge in network.edges
                ],
                "r": resistors,
                "l": inductors,
                "c": capacitors,
                "lc": inductors + capacitors,
                "rlc": resistors + inductors + capacitors,
                "source_assignment_id": assignment_id,
                "source_support_id": support_id,
                "source_support_edges": support_edges,
                "generated_source_candidates": bucket["candidates"],
                "distinct_representative_forms": len(bucket["forms"]),
            }
        )
    records.sort(
        key=lambda row: (
            row["rlc"],
            row["r"],
            row["l"],
            row["c"],
            row["catalogue_id"],
        )
    )
    totals_by_size = Counter(str(row["rlc"]) for row in records)
    totals_by_composition = Counter(
        f"R{row['r']}L{row['l']}C{row['c']}" for row in records
    )
    return {
        "format_version": FORMAT_VERSION,
        "object": "ladenheim-structural-148-catalogue",
        "source_scope": {
            "max_rlc": 5,
            "max_lc": 2,
            "profile": "ladenheim-structural-region",
        },
        "relation": {
            "name": RELATION_NAME,
            "definition": (
                "Equality of complete GF(2) cycle spaces of port-augmented "
                "primitive graphs under permutations within R, L, C, and "
                "uniquely fixed P colour blocks."
            ),
        },
        "preliminary_rejections": [
            "same-colour two-edge circuits among non-port edges",
            (
                "same-colour two-edge cocircuits among non-port edges in the "
                "port-augmented graph"
            ),
            "multi-element all-resistor networks",
        ],
        "generation": {
            "source_assignments": len(assignments),
            "distinct_structural_signatures_before_rejection": len(
                {sig for sig, _ in generated_forms}
            ),
            "distinct_graph_representative_forms_before_rejection": len(
                generated_forms
            ),
            "rejected_source_candidates": dict(
                sorted(rejected_candidates.items())
            ),
            "distinct_classes_by_exclusion_stage": {
                "before_exclusions": len({sig for sig, _ in generated_forms}),
                "after_same_kind_parallel": len(
                    {sig for sig, _ in generated_forms}
                )
                - len(signatures_by_rejection["same-kind-parallel-pair"]),
                "after_same_kind_series": len(classes)
                + len(signatures_by_rejection["multi-element-all-resistor"]),
                "after_multi_element_all_resistor": len(classes),
            },
            "rejected_structural_classes": {
                key: len(value)
                for key, value in sorted(signatures_by_rejection.items())
            },
        },
        "totals_by_primitive_elements": dict(
            sorted(totals_by_size.items(), key=lambda item: int(item[0]))
        ),
        "totals_by_composition": dict(sorted(totals_by_composition.items())),
        "total": len(records),
        "records": records,
    }


def catalogue_json() -> str:
    return (
        json.dumps(
            generate_ladenheim_148_catalogue(), indent=2, sort_keys=True
        )
        + "\n"
    )

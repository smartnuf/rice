import json
from pathlib import Path

import networkx as nx

from rice.ladenheim import (
    RELATION_NAME,
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    generate_ladenheim_148_catalogue,
    has_same_kind_parallel_pair,
    has_same_kind_series_pair,
    network_from_descriptor,
    preliminary_rejection,
    representative_descriptor,
)


def network(edges, terminals=(0, 1)):
    return PrimitiveNetwork(
        terminals, tuple(PrimitiveEdge(*edge) for edge in edges)
    )


def signature(value):
    return canonical_structural_signature(value).stable_string()


def test_signature_ignores_names_reversal_orientation_and_order():
    original = network([(0, 2, "R"), (2, 1, "L"), (0, 1, "C")])
    renamed = network(
        [("right", "left", "C"), ("x", "right", "L"), ("left", "x", "R")],
        ("right", "left"),
    )
    assert signature(original) == signature(renamed)
    assert representative_descriptor(original) == representative_descriptor(
        renamed
    )


def test_series_interchange_and_whitney_twist_share_structural_identity():
    first_series = network(
        [(0, 2, "R"), (2, 3, "L"), (3, 1, "C")]
    )
    second_series = network(
        [(0, 2, "C"), (2, 3, "R"), (3, 1, "L")]
    )
    assert signature(first_series) == signature(second_series)
    left = network([(0, 2, "C"), (0, 2, "R"), (1, 3, "C"), (2, 3, "R")])
    right = network([(0, 2, "C"), (1, 3, "R"), (2, 3, "C"), (2, 3, "R")])
    assert sorted(dict(left.graph().degree()).values()) != sorted(
        dict(right.graph().degree()).values()
    )
    assert signature(left) == signature(right)


def test_colours_and_port_choice_are_part_of_structural_identity():
    assert signature(network([(0, 2, "R"), (2, 1, "L")])) != signature(
        network([(0, 2, "R"), (2, 1, "C")])
    )
    cycle_edges = [(0, 1, "R"), (1, 2, "L"), (2, 3, "R"), (3, 0, "C")]
    assert signature(network(cycle_edges, (0, 2))) != signature(
        network(cycle_edges, (0, 1))
    )


def test_graph_shape_does_not_override_coloured_cycle_matroid():
    first = network([(0, 2, "R"), (2, 1, "L"), (0, 1, "C")])
    second = network([(0, 2, "R"), (2, 1, "C"), (0, 1, "L")])
    assert nx.is_isomorphic(first.graph(), second.graph())
    assert signature(first) != signature(second)


def test_preliminary_same_kind_and_all_resistor_rejections():
    same_parallel = network([(0, 1, "R"), (0, 1, "R")])
    mixed_parallel = network([(0, 1, "R"), (0, 1, "L")])
    same_series = network([(0, 2, "R"), (2, 1, "R")])
    mixed_series = network([(0, 2, "R"), (2, 1, "L")])
    resistor_bridge = network(
        [(0, 2, "R"), (2, 1, "R"), (0, 3, "R"), (3, 1, "R"), (2, 3, "R")]
    )
    one_resistor = network([(0, 1, "R")])
    assert has_same_kind_parallel_pair(same_parallel)
    assert preliminary_rejection(same_parallel) == "same-kind-parallel-pair"
    assert not has_same_kind_parallel_pair(mixed_parallel)
    assert preliminary_rejection(mixed_parallel) is None
    assert has_same_kind_series_pair(same_series)
    assert preliminary_rejection(same_series) == "same-kind-series-pair"
    assert not has_same_kind_series_pair(mixed_series)
    assert preliminary_rejection(mixed_series) is None
    assert (
        preliminary_rejection(resistor_bridge)
        == "multi-element-all-resistor"
    )
    assert preliminary_rejection(one_resistor) is None


def test_full_structural_catalogue_regression_and_record_contract():
    catalogue = generate_ladenheim_148_catalogue()
    assert catalogue["relation"]["name"] == RELATION_NAME
    expected_by_size = {
        "1": 3,
        "2": 6,
        "3": 16,
        "4": 38,
        "5": 85,
    }
    assert catalogue["totals_by_primitive_elements"] == expected_by_size
    assert catalogue["total"] == 148
    records = catalogue["records"]
    assert sum(row["r"] == 4 and row["lc"] == 1 for row in records) == 8
    assert all(row["rlc"] <= 5 and row["lc"] <= 2 for row in records)
    assert all(row["rlc"] == 1 or row["lc"] > 0 for row in records)
    assert all(
        {edge["type"] for edge in row["primitive_edges"]} <= {"R", "L", "C"}
        for row in records
    )
    representatives = [
        network_from_descriptor(row["representative_descriptor"])
        for row in records
    ]
    assert all(nx.is_connected(item.graph()) for item in representatives)
    assert all(preliminary_rejection(item) is None for item in representatives)
    assert [signature(item) for item in representatives] == [
        row["canonical_structural_signature"] for row in records
    ]
    assert len({row["catalogue_id"] for row in records}) == 148
    assert len({row["representative_descriptor"] for row in records}) == 148
    assert records == sorted(
        records,
        key=lambda row: (
            row["rlc"],
            row["r"],
            row["l"],
            row["c"],
            row["catalogue_id"],
        ),
    )


def test_committed_catalogue_is_exact_deterministic_generation():
    committed = json.loads(
        Path("data/counts/ladenheim-148.json").read_text(encoding="utf-8")
    )
    generated = generate_ladenheim_148_catalogue()
    assert committed == generated
    serialized = json.dumps(generated, sort_keys=True)
    assert "timestamp" not in serialized.lower()
    assert "/home/" not in serialized

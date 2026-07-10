"""Reproduces the counts recorded in docs/ladenheim_benchmark.md.

These are diagnostics about the *current* RICE reduced-topology model under
two different scopes, not a claim of agreement with the historical 148, 108,
or 62 Ladenheim figures. See docs/ladenheim_benchmark.md for the full
reassessment of what those historical figures actually mean and why they are
not directly comparable to a rectangular RICE count.
"""

from collections import defaultdict

from rice.core import (
    iter_reduced_topology_signatures,
    reduced_signature_component_counts,
    reduced_topology_census,
)


def test_bounded_r3_slice_matches_verified_140_table():
    """The old (incorrect-as-a-148-proxy) R<=3, L+C<=2 slice, verified."""
    result = reduced_topology_census(max_r=3, max_reactive=2)

    assert result.total == 140
    assert result.exact_table == (
        (0, 2, 2),
        (1, 4, 12),
        (0, 4, 34),
        (0, 4, 77),
    )


def _corrected_148_scope_counts():
    """total elements <= 5, L + C <= 2, no independent R bound."""
    counts = defaultdict(lambda: defaultdict(int))
    seen_signatures = set()
    grand_total = 0
    for signature in iter_reduced_topology_signatures(max_r=5, max_reactive=2):
        key = signature.stable_string()
        assert key not in seen_signatures, f"duplicate signature {key}"
        seen_signatures.add(key)
        r, l, c = reduced_signature_component_counts(signature)
        x = l + c
        assert r <= 5 and x <= 2, (r, x)
        if r + x <= 5:
            counts[r][x] += 1
            grand_total += 1
    return counts, grand_total


def test_corrected_148_scope_diagnostic_gives_149():
    counts, grand_total = _corrected_148_scope_counts()

    assert grand_total == 149
    assert dict(counts[0]) == {1: 2, 2: 2}
    assert dict(counts[1]) == {0: 1, 1: 4, 2: 12}
    assert dict(counts[2]) == {1: 4, 2: 34}
    assert dict(counts[3]) == {1: 4, 2: 77}
    assert dict(counts[4]) == {1: 8}
    assert dict(counts[5]) == {0: 1}


def test_corrected_148_scope_r3_subset_matches_bounded_slice():
    counts, _ = _corrected_148_scope_counts()

    r_le_3_total = sum(sum(x_counts.values()) for r, x_counts in counts.items() if r <= 3)
    assert r_le_3_total == 140

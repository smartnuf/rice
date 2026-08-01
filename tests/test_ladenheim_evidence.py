import json
from collections import Counter
from pathlib import Path

import pytest

from rice.ladenheim_evidence import _validate_exclusion_counts, generate_evidence_ledger


CATALOGUE_PATH = Path("data/counts/ladenheim-148.json")
ANNOTATION_PATH = Path("data/comparisons/ladenheim-108-annotations.json")
LEDGER_PATH = Path("data/comparisons/ladenheim-148-to-108.json")


@pytest.fixture
def catalogue():
    return json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))


@pytest.fixture
def annotations():
    return json.loads(ANNOTATION_PATH.read_text(encoding="utf-8"))


def _unresolved_annotation(catalogue_id):
    return {
        "catalogue_id": catalogue_id,
        "comparison_status": "unresolved",
        "proposed_disposition": "unresolved",
        "exclusion_category": "unresolved",
        "exclusion_reason": None,
        "evidence_basis": ["no-evidence-yet"],
        "evidence_record_ids": [],
        "previous_workspace_record_ids": [],
        "computational_cross_check_ids": [],
        "historical_identifiers": [],
        "basic_graph_assignment": None,
        "confidence": "none",
        "notes": ["Fixture annotation."],
        "open_questions": ["What evidence resolves this entry?"],
    }


def _workspace_source():
    return {
        "source_id": "workspace-source",
        "source_type": "previous-workspace-repository",
        "citation": "Previous workspace fixture.",
        "repository": "smartnuf/example",
        "commit_sha": "abc123",
        "notes": "Test fixture only.",
    }


def _workspace_record():
    return {
        "workspace_record_id": "workspace-record",
        "source_id": "workspace-source",
        "provenance_level": "previous-workspace-transcription",
        "repository_path": "catalogues/example.csv",
        "row": "1",
        "verification_state": "parsed",
        "limitations": "No authoritative citation.",
        "notes": "Test fixture only.",
    }


def _cross_check():
    return {
        "cross_check_id": "computation-record",
        "provenance_level": "independently-reproduced-computation",
        "implementation": "fixture evaluator",
        "commit_sha": "abc123",
        "input": "fixture descriptor",
        "operation": "compare fixture signatures",
        "result": "equal",
        "independently_reproduced": True,
        "limitations": "Does not establish historical identity.",
        "verification_state": "cross-checked",
    }


def test_format_version_two_is_required(catalogue, annotations):
    annotations["format_version"] = 1
    with pytest.raises(ValueError, match="format_version must be 2"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("collection", "id_field"),
    [
        ("sources", "source_id"),
        ("evidence_records", "evidence_id"),
        ("previous_workspace_records", "workspace_record_id"),
        ("computational_cross_checks", "cross_check_id"),
    ],
)
def test_duplicate_collection_ids_are_rejected(
    catalogue, annotations, collection, id_field
):
    if collection == "previous_workspace_records":
        annotations["sources"].append(_workspace_source())
        annotations[collection] = [_workspace_record()]
    elif collection == "computational_cross_checks":
        annotations[collection] = [_cross_check()]
    annotations[collection].append(dict(annotations[collection][0]))
    with pytest.raises(ValueError, match=f"duplicate {id_field}"):
        generate_evidence_ledger(catalogue, annotations)


def test_duplicate_rule_and_annotation_ids_are_rejected(catalogue, annotations):
    annotations["rules"].append(dict(annotations["rules"][0]))
    with pytest.raises(ValueError, match="duplicate rule_id"):
        generate_evidence_ledger(catalogue, annotations)
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    annotations["records"] = [row, dict(row)]
    with pytest.raises(ValueError, match="duplicate annotation ID"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "unknown"),
    [
        ("evidence_record_ids", "unknown-evidence"),
        ("previous_workspace_record_ids", "unknown-workspace"),
        ("computational_cross_check_ids", "unknown-computation"),
    ],
)
def test_unknown_cross_references_are_rejected(
    catalogue, annotations, field, unknown
):
    annotations["rules"][0][field] = [unknown]
    with pytest.raises(ValueError, match=f"unknown {field}"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "locator",
    [
        "printed page 42",
        {},
        {"printed_page": -1},
        {"repository_path": "/home/person/source.json"},
        {"unknown": "value"},
    ],
)
def test_structured_locators_are_validated(catalogue, annotations, locator):
    annotations["evidence_records"][0]["locator"] = locator
    with pytest.raises(ValueError, match="locator|absolute"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("boolean", [True, False])
@pytest.mark.parametrize(
    "location",
    ["locator", "target", "category", "selector", "expected_matches"],
)
def test_booleans_are_rejected_in_numeric_schema_fields(
    catalogue, annotations, location, boolean
):
    if location == "locator":
        annotations["evidence_records"][0]["locator"]["printed_page"] = boolean
    elif location == "target":
        annotations["target"]["reported_members"] = boolean
    elif location == "category":
        annotations["evidence_records"][3]["claim"]["supported_values"][
            "exclusion_category_targets"
        ]["zobel-four-element"] = boolean
    elif location == "selector":
        annotations["evidence_records"][2]["claim"]["supported_selector"]["r"] = boolean
    else:
        annotations["evidence_records"][2]["claim"]["expected_matches"] = boolean
    with pytest.raises(ValueError, match="integer|target|claim"):
        generate_evidence_ledger(catalogue, annotations)


def _source_backed_fixture(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row.update(
        comparison_status="source-backed",
        confidence="medium",
        evidence_basis=["explicit-historical-entry-statement"],
    )
    annotations["records"] = [row]
    return row


def test_source_backed_cannot_rely_on_previous_workspace(
    catalogue, annotations
):
    annotations["sources"].append(_workspace_source())
    annotations["previous_workspace_records"] = [_workspace_record()]
    row = _source_backed_fixture(catalogue, annotations)
    row["previous_workspace_record_ids"] = ["workspace-record"]
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


def test_source_backed_cannot_rely_on_computation(catalogue, annotations):
    annotations["computational_cross_checks"] = [_cross_check()]
    row = _source_backed_fixture(catalogue, annotations)
    row["computational_cross_check_ids"] = ["computation-record"]
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("reference_kind", ["workspace", "computation"])
def test_exclusion_cannot_rely_on_non_authoritative_records(
    catalogue, annotations, reference_kind
):
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        comparison_status="working-hypothesis",
        proposed_disposition="exclude",
        exclusion_category="other-canonical-exclusion",
        exclusion_reason="Fixture exclusion.",
        evidence_basis=["researcher-hypothesis"],
    )
    if reference_kind == "workspace":
        annotations["sources"].append(_workspace_source())
        annotations["previous_workspace_records"] = [_workspace_record()]
        row["previous_workspace_record_ids"] = ["workspace-record"]
    else:
        annotations["computational_cross_checks"] = [_cross_check()]
        row["computational_cross_check_ids"] = ["computation-record"]
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


def test_source_backed_rejects_general_catalogue_target_evidence(
    catalogue, annotations
):
    row = _source_backed_fixture(catalogue, annotations)
    row["evidence_record_ids"] = ["ms-2019-reported-148-to-108"]
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


def test_exclusion_rejects_authoritative_unrelated_category(
    catalogue, annotations
):
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        comparison_status="working-hypothesis",
        proposed_disposition="exclude",
        exclusion_category="zobel-four-element",
        exclusion_reason="Fixture claim.",
        evidence_basis=["researcher-hypothesis"],
        evidence_record_ids=["ms-2019-eight-four-resistor-one-reactive"],
    )
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("mismatch", ["selector", "category"])
def test_unique_match_rejects_mismatched_claim_metadata(
    catalogue, annotations, mismatch
):
    if mismatch == "selector":
        annotations["evidence_records"][2]["claim"]["supported_selector"] = {"r": 3}
        message = "matching mechanical RICE basis"
    else:
        annotations["evidence_records"][1]["claim"][
            "supported_exclusion_category"
        ] = "zobel-four-element"
        message = "matching aggregate authoritative evidence"
    with pytest.raises(ValueError, match=message):
        generate_evidence_ledger(catalogue, annotations)


def test_rejected_rice_evidence_cannot_satisfy_unique_match(catalogue, annotations):
    annotations["evidence_records"][2]["verification_state"] = "rejected"
    with pytest.raises(ValueError, match="matching mechanical RICE basis"):
        generate_evidence_ledger(catalogue, annotations)


def test_target_requires_aggregate_evidence(catalogue, annotations):
    annotations["target"]["evidence_record_ids"].remove(
        "ms-2019-reported-148-to-108"
    )
    with pytest.raises(ValueError, match="aggregate evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_target_requires_category_target_evidence(catalogue, annotations):
    annotations["target"]["evidence_record_ids"].remove(
        "ms-2019-four-exclusion-category-targets"
    )
    with pytest.raises(ValueError, match="category-target evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_generated_target_references_its_evidence(catalogue, annotations):
    target = generate_evidence_ledger(catalogue, annotations)["target"]
    assert target["evidence_record_ids"] == [
        "ms-2019-reported-148-to-108",
        "ms-2019-four-exclusion-category-targets",
    ]


def _retained_evidence(catalogue_id):
    return {
        "evidence_id": "fixture-retained-record",
        "source_id": "morelli-smith-2019",
        "provenance_level": "authoritative-source-transcription",
        "verification_state": "source-verified",
        "locator": {"appendix": "C", "printed_page": 129, "network_number": 1},
        "paraphrase": "Synthetic retained-record test fixture.",
        "claim": {
            "claim_type": "individual-catalogue-record",
            "subject_catalogue_ids": [catalogue_id],
            "supported_values": {"proposed_disposition": "retain"},
        },
    }


def test_unresolved_retain_without_evidence_is_rejected(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["proposed_disposition"] = "retain"
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="resolved evidence basis"):
        generate_evidence_ledger(catalogue, annotations)


def test_working_hypothesis_retain_without_evidence_is_rejected(
    catalogue, annotations
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row.update(
        comparison_status="working-hypothesis",
        proposed_disposition="retain",
        evidence_basis=["researcher-hypothesis"],
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="individual-record evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_retain_rejects_unrelated_authoritative_evidence(catalogue, annotations):
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        proposed_disposition="retain",
        evidence_record_ids=["ms-2019-reported-148-to-108"],
    )
    with pytest.raises(ValueError, match="claim-specific|individual-record"):
        generate_evidence_ledger(catalogue, annotations)


def test_valid_source_backed_retained_fixture_is_accepted(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].append(_retained_evidence(row_id))
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        proposed_disposition="retain",
        evidence_record_ids=["fixture-retained-record"],
    )
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["proposed_disposition"] == "retain"


def test_source_verified_identifier_requires_authoritative_evidence(
    catalogue, annotations
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": 70,
        "verification_state": "source-verified",
        "evidence_record_ids": ["rice-lh148-r4-lc1-count"],
    }]
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="requires appropriate authoritative evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_source_verified_identifier_requires_identifier_specific_evidence(
    catalogue, annotations
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": 70,
        "verification_state": "source-verified",
        "evidence_record_ids": ["ms-2019-reported-148-to-108"],
    }]
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="appropriate authoritative evidence"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "identifier",
    [
        "70",
        {"scheme": "unknown", "value": 70, "verification_state": "parsed", "evidence_record_ids": []},
        {"scheme": "morelli-smith-canonical-network", "value": None, "verification_state": "parsed", "evidence_record_ids": []},
        {"scheme": "morelli-smith-canonical-network", "value": 70, "verification_state": "unknown", "evidence_record_ids": []},
    ],
)
def test_malformed_historical_identifiers_are_rejected(
    catalogue, annotations, identifier
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["historical_identifiers"] = [identifier]
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="historical identifier"):
        generate_evidence_ledger(catalogue, annotations)


def _graph_assignment(evidence_ids):
    return {
        "graph_label": "Fixture-G",
        "base_label": "Fixture-G",
        "is_dual": False,
        "fixture_id": "fixture-g",
        "structural_relation": "fixture-port-relation",
        "verification_state": "source-verified",
        "evidence_record_ids": evidence_ids,
    }


def _graph_definition_evidence():
    return {
        "evidence_id": "fixture-graph-evidence",
        "source_id": "morelli-smith-2019",
        "provenance_level": "authoritative-source-transcription",
        "verification_state": "source-verified",
        "locator": {"printed_page": 125, "appendix": "B"},
        "paraphrase": "Synthetic graph-assignment test fixture.",
        "claim": {
            "claim_type": "basic-graph-definition",
            "definition": {
                "graph_label": "Fixture-G",
                "base_label": "Fixture-G",
                "is_dual": False,
                "fixture_id": "fixture-g",
            },
        },
    }


def _graph_match_evidence(catalogue_id):
    return {
        "evidence_id": "fixture-graph-match",
        "source_id": "rice-ladenheim-148-catalogue",
        "provenance_level": "rice-derived-structural-fact",
        "verification_state": "cross-checked",
        "locator": {"repository_path": "tests/fixtures/basic-graph.json"},
        "paraphrase": "Synthetic subject-bound graph-match test fixture.",
        "claim": {
            "claim_type": "basic-graph-match",
            "subject_catalogue_ids": [catalogue_id],
            "match": {
                "fixture_id": "fixture-g",
                "graph_label": "Fixture-G",
                "structural_relation": "fixture-port-relation",
                "matched": True,
            },
        },
    }


def test_source_verified_graph_assignment_requires_evidence(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["basic_graph_assignment"] = _graph_assignment([])
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="graph-definition evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_source_verified_graph_assignment_rejects_unrelated_evidence(
    catalogue, annotations
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["basic_graph_assignment"] = _graph_assignment(
        ["ms-2019-reported-148-to-108"]
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="graph-definition evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_graph_definition_alone_cannot_assign_rice_row(catalogue, annotations):
    annotations["rules"] = []
    annotations["evidence_records"].append(_graph_definition_evidence())
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["basic_graph_assignment"] = _graph_assignment(["fixture-graph-evidence"])
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="subject-bound RICE graph-match"):
        generate_evidence_ledger(catalogue, annotations)


def test_graph_match_for_another_catalogue_id_is_rejected(catalogue, annotations):
    annotations["rules"] = []
    row_id = catalogue["records"][0]["catalogue_id"]
    other_id = catalogue["records"][1]["catalogue_id"]
    annotations["evidence_records"].extend(
        [_graph_definition_evidence(), _graph_match_evidence(other_id)]
    )
    row = _unresolved_annotation(row_id)
    row["basic_graph_assignment"] = _graph_assignment(
        ["fixture-graph-evidence", "fixture-graph-match"]
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="subject-bound RICE graph-match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("field", ["graph_label", "fixture_id", "structural_relation", "is_dual"])
def test_graph_assignment_mismatches_are_rejected(catalogue, annotations, field):
    annotations["rules"] = []
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].extend(
        [_graph_definition_evidence(), _graph_match_evidence(row_id)]
    )
    row = _unresolved_annotation(row_id)
    row["basic_graph_assignment"] = _graph_assignment(
        ["fixture-graph-evidence", "fixture-graph-match"]
    )
    row["basic_graph_assignment"][field] = (
        True if field == "is_dual" else f"mismatched-{field}"
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="graph-definition|graph-match"):
        generate_evidence_ledger(catalogue, annotations)


def test_valid_two_layer_graph_assignment_fixture_is_accepted(
    catalogue, annotations
):
    annotations["rules"] = []
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].extend(
        [_graph_definition_evidence(), _graph_match_evidence(row_id)]
    )
    row = _unresolved_annotation(row_id)
    row["basic_graph_assignment"] = _graph_assignment(
        ["fixture-graph-evidence", "fixture-graph-match"]
    )
    annotations["records"] = [row]
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["basic_graph_assignment"] == row[
        "basic_graph_assignment"
    ]


@pytest.mark.parametrize(
    ("remove_id", "message"),
    [
        ("ms-2019-eight-four-resistor-one-reactive", "aggregate authoritative"),
        ("rice-lh148-r4-lc1-count", "mechanical RICE basis"),
    ],
)
def test_derived_unique_match_requires_historical_and_mechanical_evidence(
    catalogue, annotations, remove_id, message
):
    annotations["rules"][0]["evidence_record_ids"].remove(remove_id)
    with pytest.raises(ValueError, match=message):
        generate_evidence_ledger(catalogue, annotations)


def _populate_exclusions(catalogue, annotations, category_counts):
    annotations["rules"] = []
    annotations["records"] = []
    offset = 0
    for category, count in category_counts.items():
        for index in range(count):
            row_id = catalogue["records"][offset]["catalogue_id"]
            evidence_id = f"fixture-exclusion-{offset}"
            annotations["evidence_records"].append({
                "evidence_id": evidence_id,
                "source_id": "morelli-smith-2019",
                "provenance_level": "authoritative-source-transcription",
                "verification_state": "source-verified",
                "locator": {"printed_page": 42, "section": "5.1"},
                "paraphrase": "Synthetic exclusion-bound test fixture.",
                "claim": {
                    "claim_type": "individual-catalogue-record",
                    "subject_catalogue_ids": [row_id],
                    "supported_values": {
                        "proposed_disposition": "exclude",
                        "exclusion_category": category,
                    },
                },
            })
            row = _unresolved_annotation(row_id)
            row.update(
                comparison_status="source-backed",
                proposed_disposition="exclude",
                exclusion_category=category,
                exclusion_reason="Synthetic exclusion-bound fixture.",
                evidence_basis=["explicit-historical-entry-statement"],
                evidence_record_ids=[evidence_id],
                confidence="high",
            )
            annotations["records"].append(row)
            offset += 1


@pytest.mark.parametrize(
    ("category", "count"),
    [
        ("simpler-bilinear-realisation", 9),
        ("zobel-four-element", 5),
    ],
)
def test_mapped_exclusions_cannot_exceed_category_target(
    catalogue, annotations, category, count
):
    _populate_exclusions(catalogue, annotations, {category: count})
    with pytest.raises(ValueError, match="exceed category target"):
        generate_evidence_ledger(catalogue, annotations)


def test_mapped_exclusions_cannot_exceed_total_target(catalogue, annotations):
    _populate_exclusions(
        catalogue,
        annotations,
        {
            "simpler-bilinear-realisation": 8,
            "zobel-four-element": 4,
            "zobel-five-element-series-parallel": 20,
            "other-canonical-exclusion": 9,
        },
    )
    with pytest.raises(ValueError, match="exceed reported exclusion target"):
        generate_evidence_ledger(catalogue, annotations)


def test_category_counter_must_agree_with_total(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    with pytest.raises(ValueError, match="categories disagree"):
        _validate_exclusion_counts(
            ledger["records"],
            ledger["target"],
            8,
            Counter({"simpler-bilinear-realisation": 7}),
        )


def test_unresolved_entry_needs_no_fabricated_evidence(catalogue, annotations):
    annotations["rules"] = []
    annotations["records"] = [
        _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    ]
    row = generate_evidence_ledger(catalogue, annotations)["records"][0]
    assert row["comparison_status"] == "unresolved"
    assert row["evidence_record_ids"] == []
    assert row["previous_workspace_record_ids"] == []
    assert row["computational_cross_check_ids"] == []


def test_exact_eight_and_140_distribution(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["summary"]["by_comparison_status"] == {
        "derived-unique-match": 8,
        "unresolved": 140,
    }
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 8,
        "unresolved": 140,
    }
    assert all(row["proposed_disposition"] != "retain" for row in ledger["records"])
    mapped = [row for row in ledger["records"] if row["proposed_disposition"] == "exclude"]
    assert len(mapped) == 8
    assert all(row["r"] == 4 and row["lc"] == 1 for row in mapped)
    assert all(row["comparison_status"] == "derived-unique-match" for row in mapped)
    assert all(row["historical_identifiers"] == [] for row in ledger["records"])
    assert all(row["basic_graph_assignment"] is None for row in ledger["records"])


def test_ledger_has_every_source_id_once_in_source_order(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    source_ids = [row["catalogue_id"] for row in catalogue["records"]]
    ledger_ids = [row["catalogue_id"] for row in ledger["records"]]
    assert ledger_ids == source_ids
    assert len(ledger_ids) == len(set(ledger_ids)) == 148


def test_immutable_structural_fields_match_catalogue(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    fields = {
        "catalogue_id", "representative_descriptor", "r", "l", "c", "lc",
        "rlc", "source_assignment_id", "source_support_id", "source_support_edges",
    }
    assert [{field: row[field] for field in fields} for row in ledger["records"]] == [
        {field: row[field] for field in fields} for row in catalogue["records"]
    ]


def test_annotation_cannot_contradict_structural_catalogue(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["structural_assertions"] = {"r": 999}
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="contradicts immutable r"):
        generate_evidence_ledger(catalogue, annotations)


def test_committed_ledger_is_exact_and_has_no_unstable_metadata(catalogue, annotations):
    committed = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    generated = generate_evidence_ledger(catalogue, annotations)
    assert committed == generated
    serialized = json.dumps(generated, sort_keys=True).lower()
    assert "timestamp" not in serialized
    assert "/home/" not in serialized
    assert "\\users\\" not in serialized


def test_timestamps_are_rejected(catalogue, annotations):
    annotations["sources"][0]["timestamp"] = "2026-01-01"
    with pytest.raises(ValueError, match="timestamps"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "path",
    [
        "/tmp/example",
        "/mnt/data/example",
        "/var/example",
        "C:\\Users\\example",
        "C:/Users/example",
        "\\\\server\\share\\example",
    ],
)
def test_machine_absolute_paths_are_rejected(catalogue, annotations, path):
    annotations["sources"][0]["notes"] = path
    with pytest.raises(ValueError, match="absolute paths"):
        generate_evidence_ledger(catalogue, annotations)


def test_repository_relative_paths_and_slash_prose_are_accepted(
    catalogue, annotations
):
    annotations["sources"][0]["notes"] = "See chapter/section references."
    annotations["evidence_records"][2]["locator"]["repository_path"] = (
        "data/counts/ladenheim-148.json"
    )
    generate_evidence_ledger(catalogue, annotations)


def test_original_catalogue_ids_and_file_are_unchanged(catalogue):
    regenerated = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
    assert regenerated == catalogue
    assert [row["catalogue_id"] for row in regenerated["records"]] == [
        row["catalogue_id"] for row in catalogue["records"]
    ]

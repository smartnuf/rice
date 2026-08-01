import json
from pathlib import Path

import pytest

from rice.ladenheim_evidence import generate_evidence_ledger


CATALOGUE_PATH = Path("data/counts/ladenheim-148.json")
ANNOTATION_PATH = Path(
    "data/comparisons/ladenheim-108-annotations.json"
)
LEDGER_PATH = Path("data/comparisons/ladenheim-148-to-108.json")


@pytest.fixture
def catalogue():
    return json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))


@pytest.fixture
def annotations():
    return json.loads(ANNOTATION_PATH.read_text(encoding="utf-8"))


def test_ledger_has_every_source_id_once_in_source_order(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    source_ids = [row["catalogue_id"] for row in catalogue["records"]]
    ledger_ids = [row["catalogue_id"] for row in ledger["records"]]
    assert ledger_ids == source_ids
    assert len(ledger_ids) == len(set(ledger_ids)) == 148


def test_immutable_structural_fields_match_catalogue(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    fields = {
        "catalogue_id",
        "representative_descriptor",
        "r",
        "l",
        "c",
        "lc",
        "rlc",
        "source_assignment_id",
        "source_support_id",
        "source_support_edges",
    }
    assert [
        {field: row[field] for field in fields} for row in ledger["records"]
    ] == [
        {field: row[field] for field in fields}
        for row in catalogue["records"]
    ]


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda data: data["records"].append({"catalogue_id": "unknown"}), "unknown"),
        (
            lambda data: data["records"].extend(
                [
                    _unresolved_annotation("lh148-187ef8e981d523c3"),
                    _unresolved_annotation("lh148-187ef8e981d523c3"),
                ]
            ),
            "duplicate",
        ),
        (
            lambda data: data["rules"][0].update(
                comparison_status="not-a-status"
            ),
            "comparison_status",
        ),
    ],
)
def test_duplicate_unknown_and_vocabulary_errors_rejected(
    catalogue, annotations, mutation, message
):
    annotations["rules"] = [] if message in {"unknown", "duplicate"} else annotations["rules"]
    mutation(annotations)
    with pytest.raises(ValueError, match=message):
        generate_evidence_ledger(catalogue, annotations)


def _unresolved_annotation(catalogue_id):
    return {
        "catalogue_id": catalogue_id,
        "comparison_status": "unresolved",
        "proposed_disposition": "unresolved",
        "exclusion_category": "unresolved",
        "exclusion_reason": None,
        "evidence_basis": ["no-evidence-yet"],
        "source_references": [],
        "historical_identifiers": [],
        "confidence": "none",
        "notes": ["Fixture annotation."],
        "open_questions": ["What evidence resolves this entry?"],
    }


def test_incomplete_source_reference_is_rejected(catalogue, annotations):
    annotations["sources"][0].pop("locator")
    with pytest.raises(ValueError, match="locator"):
        generate_evidence_ledger(catalogue, annotations)


def test_asserted_exclusion_without_evidence_is_rejected(catalogue, annotations):
    annotations["rules"] = []
    assertion = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    assertion.update(
        proposed_disposition="exclude",
        exclusion_category="other-canonical-exclusion",
        exclusion_reason="Unsupported fixture claim.",
    )
    annotations["records"] = [assertion]
    with pytest.raises(ValueError, match="requires source evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_unresolved_entry_needs_no_fabricated_evidence(catalogue, annotations):
    annotations["rules"] = []
    annotations["records"] = [
        _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    ]
    ledger = generate_evidence_ledger(catalogue, annotations)
    row = ledger["records"][0]
    assert row["comparison_status"] == "unresolved"
    assert row["proposed_disposition"] == "unresolved"
    assert row["source_references"] == []


def test_unique_component_match_identifies_exactly_eight(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    mapped = [
        row
        for row in ledger["records"]
        if row["comparison_status"] == "derived-unique-match"
    ]
    assert len(mapped) == 8
    assert all(row["r"] == 4 and row["lc"] == 1 for row in mapped)
    assert {
        row["catalogue_id"] for row in mapped
    } == {
        row["catalogue_id"]
        for row in catalogue["records"]
        if row["r"] == 4 and row["lc"] == 1
    }


def test_committed_ledger_is_exact_and_has_no_unstable_metadata(
    catalogue, annotations
):
    committed = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    generated = generate_evidence_ledger(catalogue, annotations)
    assert committed == generated
    serialized = json.dumps(generated, sort_keys=True)
    assert "timestamp" not in serialized.lower()
    assert "/home/" not in serialized
    assert "\\users\\" not in serialized.lower()


def test_annotation_cannot_contradict_structural_catalogue(
    catalogue, annotations
):
    annotations["rules"] = []
    annotation = _unresolved_annotation(
        catalogue["records"][0]["catalogue_id"]
    )
    annotation["structural_assertions"] = {"r": 999}
    annotations["records"] = [annotation]
    with pytest.raises(ValueError, match="contradicts immutable r"):
        generate_evidence_ledger(catalogue, annotations)


def test_original_catalogue_ids_and_file_are_unchanged(catalogue):
    regenerated = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
    assert regenerated == catalogue
    assert [row["catalogue_id"] for row in regenerated["records"]] == [
        row["catalogue_id"] for row in catalogue["records"]
    ]

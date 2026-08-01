import json
from collections import Counter
from pathlib import Path

import pytest

from rice.ladenheim_evidence import (
    _is_unstable_time_key,
    _validate_disposition_partition,
    _validate_exclusion_counts,
    _validate_generated_ledger,
    generate_evidence_ledger,
)


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


def _previous_workspace_cross_check():
    record = _cross_check()
    record["provenance_level"] = "previous-workspace-generated"
    record["independently_reproduced"] = False
    return record


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


@pytest.mark.parametrize("field", ["printed_page", "network_number"])
def test_one_based_locator_fields_reject_zero(catalogue, annotations, field):
    annotations["evidence_records"][0]["locator"][field] = 0
    with pytest.raises(ValueError, match="positive integer"):
        generate_evidence_ledger(catalogue, annotations)


def test_pdf_page_index_accepts_zero(catalogue, annotations):
    annotations["evidence_records"][0]["locator"]["pdf_page_index"] = 0
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
        proposed_disposition="retain",
        exclusion_category="none",
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
    with pytest.raises(ValueError, match="working-hypothesis cannot"):
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
    with pytest.raises(ValueError, match="working-hypothesis cannot"):
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


def test_unique_match_cannot_replace_historical_component_predicate(
    catalogue, annotations
):
    annotations["rules"][0]["selector"] = {"r": 2, "l": 2}
    annotations["evidence_records"][2]["claim"]["supported_selector"] = {
        "r": 2,
        "l": 2,
    }
    with pytest.raises(ValueError, match="matching aggregate authoritative"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("mismatch", ["selector", "population", "category", "disposition"])
def test_unique_match_requires_exact_aggregate_claim(catalogue, annotations, mismatch):
    claim = annotations["evidence_records"][1]["claim"]
    if mismatch == "selector":
        claim["supported_selector"] = {"r": 3, "lc": 1}
    elif mismatch == "population":
        claim["source_population"] = 7
    elif mismatch == "category":
        claim["supported_exclusion_category"] = "zobel-four-element"
    else:
        claim["supported_disposition"] = "retain"
    with pytest.raises(ValueError, match="aggregate exclusion|aggregate authoritative"):
        generate_evidence_ledger(catalogue, annotations)


def test_unique_match_accepts_exact_historical_and_mechanical_predicate(
    catalogue, annotations
):
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert annotations["evidence_records"][1]["claim"]["supported_selector"] == {
        "r": 4,
        "lc": 1,
    }
    assert ledger["summary"]["mapped_exclusions"] == 8


def test_rejected_rice_evidence_cannot_satisfy_unique_match(catalogue, annotations):
    annotations["evidence_records"][2]["verification_state"] = "rejected"
    with pytest.raises(ValueError, match="matching mechanical RICE basis"):
        generate_evidence_ledger(catalogue, annotations)


def test_rice_derived_evidence_requires_rice_source(catalogue, annotations):
    annotations["evidence_records"][2]["source_id"] = "morelli-smith-2019"
    with pytest.raises(ValueError, match="requires a RICE source"):
        generate_evidence_ledger(catalogue, annotations)


def test_evidence_cannot_use_previous_workspace_source(catalogue, annotations):
    annotations["sources"].append(_workspace_source())
    annotations["evidence_records"][2]["source_id"] = "workspace-source"
    with pytest.raises(ValueError, match="previous-workspace source"):
        generate_evidence_ledger(catalogue, annotations)


def test_unreferenced_evidence_subject_must_exist(catalogue, annotations):
    evidence = _retained_evidence("lh148-does-not-exist")
    annotations["evidence_records"].append(evidence)
    with pytest.raises(ValueError, match="unknown catalogue subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_referenced_evidence_subject_must_exist(catalogue, annotations):
    evidence = _retained_evidence("lh148-does-not-exist")
    annotations["evidence_records"].append(evidence)
    row = _source_backed_fixture(catalogue, annotations)
    row["proposed_disposition"] = "retain"
    row["evidence_record_ids"] = [evidence["evidence_id"]]
    with pytest.raises(ValueError, match="unknown catalogue subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_duplicate_evidence_subjects_are_rejected(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _retained_evidence(row_id)
    evidence["claim"]["subject_catalogue_ids"] = [row_id, row_id]
    annotations["evidence_records"].append(evidence)
    with pytest.raises(ValueError, match="invalid catalogue subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_exact_existing_evidence_subject_is_accepted(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].append(_retained_evidence(row_id))
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("referenced", [False, True])
@pytest.mark.parametrize(
    "supported_values",
    [
        {"proposed_disposition": "banana"},
        {"exclusion_category": "unknown-category"},
        {"exclusion_reason": 123},
        {"exclusion_reason": True},
        {"exclusion_reason": ""},
        {"proposed_disposition": "exclude", "exclusion_reason": "Reason."},
        {
            "proposed_disposition": "exclude",
            "exclusion_category": "other-canonical-exclusion",
        },
        {"exclusion_category": "other-canonical-exclusion"},
        {
            "proposed_disposition": "retain",
            "exclusion_category": "other-canonical-exclusion",
        },
        {
            "proposed_disposition": "unresolved",
            "exclusion_category": "other-canonical-exclusion",
        },
        {"proposed_disposition": "unresolved", "exclusion_reason": "Reason."},
    ],
)
def test_invalid_individual_claim_values_are_rejected(
    catalogue, annotations, supported_values, referenced
):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _individual_evidence(row_id, supported_values)
    annotations["evidence_records"].append(evidence)
    if referenced:
        annotations["rules"] = []
        row = _unresolved_annotation(row_id)
        row["evidence_record_ids"] = [evidence["evidence_id"]]
        annotations["records"] = [row]
    with pytest.raises(ValueError, match="evidence fixture-individual"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "supported_values",
    [
        {
            "proposed_disposition": "exclude",
            "exclusion_category": "other-canonical-exclusion",
            "exclusion_reason": "Complete exclusion fixture.",
        },
        {
            "proposed_disposition": "retain",
            "exclusion_category": "none",
            "exclusion_reason": None,
        },
        {
            "proposed_disposition": "unresolved",
            "exclusion_category": "unresolved",
            "exclusion_reason": None,
        },
        {"exclusion_reason": None},
    ],
)
def test_valid_individual_claim_values_are_accepted(
    catalogue, annotations, supported_values
):
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].append(
        _individual_evidence(row_id, supported_values)
    )
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
            "supported_values": {
                "proposed_disposition": "retain",
                "exclusion_category": "none",
                "exclusion_reason": None,
            },
        },
    }


def _individual_evidence(catalogue_id, supported_values, evidence_id="fixture-individual"):
    evidence = _retained_evidence(catalogue_id)
    evidence["evidence_id"] = evidence_id
    evidence["claim"]["supported_values"] = supported_values
    return evidence


def test_unresolved_retain_without_evidence_is_rejected(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row["proposed_disposition"] = "retain"
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="default unresolved contract"):
        generate_evidence_ledger(catalogue, annotations)


def test_unresolved_individual_exclusion_is_rejected(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _individual_evidence(
        row_id,
        {
            "proposed_disposition": "exclude",
            "exclusion_category": "other-canonical-exclusion",
            "exclusion_reason": "Synthetic complete exclusion.",
        },
    )
    annotations["evidence_records"].append(evidence)
    annotations["rules"] = []
    row = _unresolved_annotation(row_id)
    row.update(
        proposed_disposition="exclude",
        exclusion_category="other-canonical-exclusion",
        exclusion_reason="Synthetic complete exclusion.",
        evidence_record_ids=[evidence["evidence_id"]],
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="default unresolved contract"):
        generate_evidence_ledger(catalogue, annotations)


def test_unresolved_aggregate_exclusion_is_rejected(catalogue, annotations):
    annotations["rules"][0]["comparison_status"] = "unresolved"
    with pytest.raises(ValueError, match="default unresolved contract"):
        generate_evidence_ledger(catalogue, annotations)


def test_exact_default_unresolved_contract_is_accepted(catalogue, annotations):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    annotations["records"] = [row]
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["comparison_status"] == "unresolved"


def test_valid_source_backed_individual_exclusion_is_accepted(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    reason = "Synthetic complete exclusion."
    evidence = _individual_evidence(
        row_id,
        {
            "proposed_disposition": "exclude",
            "exclusion_category": "other-canonical-exclusion",
            "exclusion_reason": reason,
        },
    )
    annotations["evidence_records"].append(evidence)
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        proposed_disposition="exclude",
        exclusion_category="other-canonical-exclusion",
        exclusion_reason=reason,
        evidence_record_ids=[evidence["evidence_id"]],
    )
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["proposed_disposition"] == "exclude"


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
    with pytest.raises(ValueError, match="working-hypothesis cannot"):
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
        exclusion_category="none",
        exclusion_reason=None,
        evidence_record_ids=["fixture-retained-record"],
    )
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["proposed_disposition"] == "retain"


@pytest.mark.parametrize(
    ("category", "reason"),
    [
        ("unresolved", None),
        ("other-canonical-exclusion", None),
        ("none", "Contradictory reason."),
    ],
)
def test_retained_row_requires_clear_exclusion_metadata(
    catalogue, annotations, category, reason
):
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].append(_retained_evidence(row_id))
    row = _source_backed_fixture(catalogue, annotations)
    row.update(
        exclusion_category=category,
        exclusion_reason=reason,
        evidence_record_ids=["fixture-retained-record"],
    )
    with pytest.raises(ValueError, match="retained disposition|claim-specific"):
        generate_evidence_ledger(catalogue, annotations)


def test_retention_rejects_incomplete_or_rejected_claim(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _retained_evidence(row_id)
    evidence["verification_state"] = "rejected"
    annotations["evidence_records"].append(evidence)
    row = _source_backed_fixture(catalogue, annotations)
    row["evidence_record_ids"] = [evidence["evidence_id"]]
    with pytest.raises(ValueError, match="claim-specific authoritative"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("basis", [["researcher-hypothesis"], []])
def test_ambiguous_status_is_unavailable_in_version_two(
    catalogue, annotations, basis
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row.update(
        comparison_status="ambiguous",
        evidence_basis=basis,
        notes=["Finite candidates are not represented in version 2."],
    )
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="comparison_status"):
        generate_evidence_ledger(catalogue, annotations)


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


def _historical_identifier_evidence(
    catalogue_id, *, scheme="morelli-smith-canonical-network", value=70
):
    locator = {"appendix": "C", "printed_page": 129, "network_number": 70}
    if (
        scheme == "morelli-smith-canonical-network"
        and isinstance(value, int)
        and not isinstance(value, bool)
        and 1 <= value <= 108
    ):
        locator["network_number"] = value
    return {
        "evidence_id": "fixture-historical-identifier",
        "source_id": "morelli-smith-2019",
        "provenance_level": "authoritative-source-transcription",
        "verification_state": "source-verified",
        "locator": locator,
        "paraphrase": "Synthetic historical-identifier test fixture.",
        "claim": {
            "claim_type": "historical-identifier",
            "subject_catalogue_ids": [catalogue_id],
            "scheme": scheme,
            "value": value,
        },
    }


def test_historical_identifier_evidence_is_bound_to_catalogue_row(
    catalogue, annotations
):
    annotations["rules"] = []
    first_id = catalogue["records"][0]["catalogue_id"]
    other_id = catalogue["records"][1]["catalogue_id"]
    annotations["evidence_records"].append(_historical_identifier_evidence(other_id))
    row = _unresolved_annotation(first_id)
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": 70,
        "verification_state": "source-verified",
        "evidence_record_ids": ["fixture-historical-identifier"],
    }]
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="appropriate authoritative evidence"):
        generate_evidence_ledger(catalogue, annotations)


def test_exact_subject_historical_identifier_fixture_is_accepted(
    catalogue, annotations
):
    annotations["rules"] = []
    row_id = catalogue["records"][0]["catalogue_id"]
    annotations["evidence_records"].append(_historical_identifier_evidence(row_id))
    row = _unresolved_annotation(row_id)
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": 70,
        "verification_state": "source-verified",
        "evidence_record_ids": ["fixture-historical-identifier"],
    }]
    annotations["records"] = [row]
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["records"][0]["historical_identifiers"] == row[
        "historical_identifiers"
    ]


def _parsed_historical_identifier(scheme, value):
    return {
        "scheme": scheme,
        "value": value,
        "verification_state": "parsed",
        "evidence_record_ids": [],
    }


def test_canonical_network_numbers_are_unique_across_rows(catalogue, annotations):
    annotations["rules"] = []
    rows = [
        _unresolved_annotation(record["catalogue_id"])
        for record in catalogue["records"][:2]
    ]
    for row in rows:
        row["historical_identifiers"] = [
            _parsed_historical_identifier("morelli-smith-canonical-network", 70)
        ]
    annotations["records"] = rows
    with pytest.raises(
        ValueError,
        match=r"morelli-smith-canonical-network 70.*lh148-.*lh148-",
    ):
        generate_evidence_ledger(catalogue, annotations)


def test_different_canonical_network_numbers_are_accepted(catalogue, annotations):
    annotations["rules"] = []
    rows = [
        _unresolved_annotation(record["catalogue_id"])
        for record in catalogue["records"][:2]
    ]
    for number, row in enumerate(rows, start=70):
        row["historical_identifiers"] = [
            _parsed_historical_identifier("morelli-smith-canonical-network", number)
        ]
    annotations["records"] = rows
    generate_evidence_ledger(catalogue, annotations)


def test_non_global_identifier_scheme_may_repeat_across_rows(catalogue, annotations):
    annotations["rules"] = []
    rows = [
        _unresolved_annotation(record["catalogue_id"])
        for record in catalogue["records"][:2]
    ]
    for row in rows:
        row["historical_identifiers"] = [
            _parsed_historical_identifier("ladenheim-original-identifier", "L-1")
        ]
    annotations["records"] = rows
    generate_evidence_ledger(catalogue, annotations)


def test_boolean_cannot_bypass_canonical_number_uniqueness(catalogue, annotations):
    annotations["rules"] = []
    rows = [
        _unresolved_annotation(record["catalogue_id"])
        for record in catalogue["records"][:2]
    ]
    rows[0]["historical_identifiers"] = [
        _parsed_historical_identifier("morelli-smith-canonical-network", True)
    ]
    rows[1]["historical_identifiers"] = [
        _parsed_historical_identifier("morelli-smith-canonical-network", 1)
    ]
    annotations["records"] = rows
    with pytest.raises(ValueError, match="canonical network must be an integer"):
        generate_evidence_ledger(catalogue, annotations)


def test_committed_ledger_has_no_historical_identifiers():
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    assert all(not row["historical_identifiers"] for row in ledger["records"])


def test_canonical_identifier_locator_must_match_claim(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(row_id, value=70)
    evidence["locator"]["network_number"] = 1
    annotations["evidence_records"].append(evidence)
    with pytest.raises(ValueError, match="network_number locator does not match"):
        generate_evidence_ledger(catalogue, annotations)


def test_canonical_identifier_matching_locator_is_accepted(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(row_id, value=70)
    annotations["evidence_records"].append(evidence)
    generate_evidence_ledger(catalogue, annotations)


def test_canonical_identifier_locator_may_omit_network_number(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(row_id, value=70)
    del evidence["locator"]["network_number"]
    annotations["evidence_records"].append(evidence)
    generate_evidence_ledger(catalogue, annotations)


def test_basic_graph_identifier_is_unaffected_by_network_locator(catalogue, annotations):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(
        row_id, scheme="morelli-smith-basic-graph", value="G"
    )
    annotations["evidence_records"].append(evidence)
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(("claim_value", "locator_value"), [(True, 1), (1, True)])
def test_canonical_identifier_and_locator_reject_booleans(
    catalogue, annotations, claim_value, locator_value
):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(row_id, value=claim_value)
    evidence["locator"]["network_number"] = locator_value
    annotations["evidence_records"].append(evidence)
    with pytest.raises(ValueError, match="locator|canonical network"):
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


@pytest.mark.parametrize(
    ("scheme", "value", "accepted"),
    [
        ("morelli-smith-canonical-network", 0, False),
        ("morelli-smith-canonical-network", -1, False),
        ("morelli-smith-canonical-network", True, False),
        ("morelli-smith-canonical-network", "1", False),
        ("morelli-smith-canonical-network", 1, True),
        ("morelli-smith-canonical-network", 108, True),
        ("morelli-smith-canonical-network", 109, False),
        ("morelli-smith-basic-graph", 1, False),
        ("morelli-smith-basic-graph", "", False),
        ("morelli-smith-basic-graph", "G'", True),
        ("ladenheim-original-identifier", 0, False),
        ("ladenheim-original-identifier", "L-1", True),
    ],
)
def test_historical_identifier_value_contract(
    catalogue, annotations, scheme, value, accepted
):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence = _historical_identifier_evidence(
        row_id, scheme=scheme, value=value
    )
    annotations["evidence_records"].append(evidence)
    row = _unresolved_annotation(row_id)
    row["historical_identifiers"] = [{
        "scheme": scheme,
        "value": value,
        "verification_state": "source-verified",
        "evidence_record_ids": [evidence["evidence_id"]],
    }]
    annotations["rules"] = []
    annotations["records"] = [row]
    if accepted:
        generate_evidence_ledger(catalogue, annotations)
    else:
        with pytest.raises(ValueError, match="identifier|canonical network|basic graph"):
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
                        "exclusion_reason": "Synthetic exclusion-bound fixture.",
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


def _populate_retentions(catalogue, annotations, count):
    annotations["rules"] = []
    annotations["records"] = []
    for index, source_row in enumerate(catalogue["records"][:count]):
        row_id = source_row["catalogue_id"]
        evidence = _retained_evidence(row_id)
        evidence["evidence_id"] = f"fixture-retained-{index}"
        evidence["locator"]["network_number"] = index % 108 + 1
        annotations["evidence_records"].append(evidence)
        row = _unresolved_annotation(row_id)
        row.update(
            comparison_status="source-backed",
            proposed_disposition="retain",
            exclusion_category="none",
            exclusion_reason=None,
            evidence_basis=["explicit-historical-entry-statement"],
            evidence_record_ids=[evidence["evidence_id"]],
            confidence="high",
        )
        annotations["records"].append(row)


def test_109_retained_rows_exceed_membership_target(catalogue, annotations):
    _populate_retentions(catalogue, annotations, 109)
    with pytest.raises(ValueError, match="retained rows exceed"):
        generate_evidence_ledger(catalogue, annotations)


def test_retained_count_respects_temporarily_reduced_target(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = ledger["records"][:2]
    rows[0] = {**rows[0], "proposed_disposition": "retain"}
    rows[1] = {**rows[1], "proposed_disposition": "retain"}
    with pytest.raises(ValueError, match="retained rows exceed"):
        _validate_disposition_partition(
            rows + ledger["records"][2:],
            {**ledger["target"], "reported_members": 1},
            Counter(row["proposed_disposition"] for row in rows + ledger["records"][2:]),
        )


def test_disposition_partition_rejects_inconsistent_counters(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    with pytest.raises(ValueError, match="counters disagree"):
        _validate_disposition_partition(
            ledger["records"], ledger["target"], Counter({"unresolved": 148})
        )


def test_disposition_partition_must_total_148(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = ledger["records"][:-1]
    with pytest.raises(ValueError, match="partition must total 148"):
        _validate_disposition_partition(
            rows,
            ledger["target"],
            Counter(row["proposed_disposition"] for row in rows),
        )


def test_generated_summary_must_match_records(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    ledger["summary"]["mapped_exclusions"] = 7
    with pytest.raises(ValueError, match="summary disagrees"):
        _validate_generated_ledger(ledger, catalogue["records"])


def test_incomplete_retention_below_target_is_accepted(catalogue, annotations):
    _populate_retentions(catalogue, annotations, 1)
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["summary"]["by_proposed_disposition"]["retain"] == 1


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
    assert all(row["comparison_status"] != "ambiguous" for row in ledger["records"])
    assert ledger["target"]["reproduction_claimed"] is False
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
    def keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from keys(item)

    assert not [key for key in keys(committed) if _is_unstable_time_key(key)]
    serialized = json.dumps(generated, sort_keys=True).lower()
    assert "/home/" not in serialized
    assert "\\users\\" not in serialized


def test_timestamps_are_rejected(catalogue, annotations):
    annotations["sources"][0]["timestamp"] = "2026-01-01"
    with pytest.raises(ValueError, match="timestamps"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "key",
    [
        "generated_at",
        "created_at",
        "updated_at",
        "modified-at",
        "recordedAt",
        "source_timestamp",
        "Timestamp",
        "checked_at",
        "processed_at",
        "exported_at",
        "written_at",
    ],
)
@pytest.mark.parametrize("nested", [False, True])
def test_conventional_timestamp_metadata_keys_are_rejected(
    catalogue, annotations, key, nested
):
    target = annotations["sources"][0]["publication"] if nested else annotations
    target[key] = "2026-08-01"
    with pytest.raises(ValueError, match="timestamps"):
        generate_evidence_ledger(catalogue, annotations)


def test_stable_publication_and_locator_metadata_are_accepted(catalogue, annotations):
    annotations["sources"][0]["publication"]["year"] = 2019
    annotations["sources"][0]["citation"] += " Published in 2019."
    locator = annotations["evidence_records"][0]["locator"]
    locator["printed_page"] = 41
    locator["pdf_page_index"] = 47
    annotations["sources"].append(_workspace_source())
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


@pytest.mark.parametrize(
    "text",
    [
        "chapter/section",
        "R/L/C",
        "ratio 1/2",
        "https://example.com/reference",
        "A. Morelli and M. C. Smith, 2019.",
    ],
)
def test_non_path_slash_prose_and_urls_are_accepted(catalogue, annotations, text):
    annotations["sources"][0]["notes"] = text
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "path",
    [
        "Local copy: /workspace/rice/private/source.pdf",
        "Local copy:/workspace/rice/private.pdf",
        "[/workspace/rice/private.pdf]",
        "path,/tmp/result.json",
        "(/var/tmp/result.json)",
        "[C:\\tmp\\result.json]",
        'source="C:/Users/example/file.pdf"',
        "location:\\\\server\\share\\file.json",
        "Output at C:\\Users\\example\\result.json",
        "Output at C:/Users/example/result.json",
        "Share: \\\\server\\share\\example",
    ],
)
def test_machine_absolute_paths_embedded_in_prose_are_rejected(
    catalogue, annotations, path
):
    annotations["sources"][0]["notes"] = path
    with pytest.raises(ValueError, match="absolute paths"):
        generate_evidence_ledger(catalogue, annotations)


def test_no_evidence_basis_cannot_describe_positive_assertion(catalogue, annotations):
    annotations["rules"][0]["evidence_basis"] = ["no-evidence-yet"]
    with pytest.raises(ValueError, match="exclusive to unresolved"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_unique_match_requires_both_matching_basis_values(
    catalogue, annotations
):
    annotations["rules"][0]["evidence_basis"] = [
        "aggregate-historical-category-plus-logically-unique-rice-match"
    ]
    with pytest.raises(ValueError, match="inconsistent with derived-unique-match"):
        generate_evidence_ledger(catalogue, annotations)


def test_independent_computation_requires_reproduced_flag(catalogue, annotations):
    record = _cross_check()
    record["independently_reproduced"] = False
    annotations["computational_cross_checks"] = [record]
    with pytest.raises(ValueError, match="provenance contradicts"):
        generate_evidence_ledger(catalogue, annotations)


def test_previous_workspace_computation_requires_unreproduced_flag(
    catalogue, annotations
):
    record = _previous_workspace_cross_check()
    record["independently_reproduced"] = True
    annotations["computational_cross_checks"] = [record]
    with pytest.raises(ValueError, match="provenance contradicts"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("record_factory", [_cross_check, _previous_workspace_cross_check])
def test_consistent_computational_provenance_is_accepted(
    catalogue, annotations, record_factory
):
    annotations["computational_cross_checks"] = [record_factory()]
    generate_evidence_ledger(catalogue, annotations)


def test_committed_structural_relation_is_required(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["source_catalogue_relation"] == (
        "colour-preserving-port-augmented-cycle-matroid-v1"
    )


@pytest.mark.parametrize(
    "relation",
    [
        {"name": "colour-preserving-port-augmented-cycle-matroid-v2"},
        {"name": "colour-preserving-port-augmented-cycle-matroid-v1 "},
        {},
        None,
    ],
)
def test_alternate_or_missing_structural_relation_is_rejected(
    catalogue, annotations, relation
):
    if relation is None:
        catalogue.pop("relation")
    else:
        catalogue["relation"] = relation
    with pytest.raises(ValueError, match="structural catalogue relation"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "object_type",
    [
        "annotations",
        "source",
        "publication",
        "evidence",
        "locator",
        "catalogue-target-claim",
        "category-target-claim",
        "aggregate-claim",
        "selector-claim",
        "individual-claim",
        "identifier-claim",
        "graph-definition-claim",
        "graph-definition",
        "graph-match-claim",
        "graph-match",
        "workspace-record",
        "computation",
        "target",
        "rule",
        "annotation-record",
        "historical-identifier",
        "basic-graph-assignment",
    ],
)
def test_version_two_closed_world_rejects_unknown_keys(
    catalogue, annotations, object_type
):
    row_id = catalogue["records"][0]["catalogue_id"]
    if object_type == "annotations":
        target = annotations
    elif object_type == "source":
        target = annotations["sources"][0]
    elif object_type == "publication":
        target = annotations["sources"][0]["publication"]
    elif object_type == "evidence":
        target = annotations["evidence_records"][0]
    elif object_type == "locator":
        target = annotations["evidence_records"][0]["locator"]
    elif object_type.endswith("-claim") and object_type in {
        "catalogue-target-claim", "category-target-claim", "aggregate-claim",
        "selector-claim",
    }:
        index = {
            "catalogue-target-claim": 0,
            "aggregate-claim": 1,
            "selector-claim": 2,
            "category-target-claim": 3,
        }[object_type]
        target = annotations["evidence_records"][index]["claim"]
    elif object_type == "individual-claim":
        evidence = _retained_evidence(row_id)
        annotations["evidence_records"].append(evidence)
        target = evidence["claim"]
    elif object_type == "identifier-claim":
        evidence = _historical_identifier_evidence(row_id)
        annotations["evidence_records"].append(evidence)
        target = evidence["claim"]
    elif object_type in {"graph-definition-claim", "graph-definition"}:
        evidence = _graph_definition_evidence()
        annotations["evidence_records"].append(evidence)
        target = evidence["claim"] if object_type.endswith("claim") else evidence["claim"]["definition"]
    elif object_type in {"graph-match-claim", "graph-match"}:
        evidence = _graph_match_evidence(row_id)
        annotations["evidence_records"].append(evidence)
        target = evidence["claim"] if object_type.endswith("claim") else evidence["claim"]["match"]
    elif object_type == "workspace-record":
        annotations["sources"].append(_workspace_source())
        record = _workspace_record()
        annotations["previous_workspace_records"] = [record]
        target = record
    elif object_type == "computation":
        record = _cross_check()
        annotations["computational_cross_checks"] = [record]
        target = record
    elif object_type == "target":
        target = annotations["target"]
    elif object_type == "rule":
        target = annotations["rules"][0]
    elif object_type == "annotation-record":
        annotations["rules"] = []
        record = _unresolved_annotation(row_id)
        annotations["records"] = [record]
        target = record
    elif object_type == "historical-identifier":
        annotations["rules"] = []
        record = _unresolved_annotation(row_id)
        identifier = {
            "scheme": "morelli-smith-basic-graph",
            "value": "G",
            "verification_state": "parsed",
            "evidence_record_ids": [],
        }
        record["historical_identifiers"] = [identifier]
        annotations["records"] = [record]
        target = identifier
    else:
        annotations["rules"] = []
        annotations["evidence_records"].extend(
            [_graph_definition_evidence(), _graph_match_evidence(row_id)]
        )
        record = _unresolved_annotation(row_id)
        record["basic_graph_assignment"] = _graph_assignment(
            ["fixture-graph-evidence", "fixture-graph-match"]
        )
        annotations["records"] = [record]
        target = record["basic_graph_assignment"]
    target["unexpected_contract_field"] = "rejected"
    with pytest.raises(ValueError, match="unknown fields|locator|invalid fields|invalid graph"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("claim_type", "required_field"),
    [
        ("catalogue-target", "supported_values"),
        ("exclusion-category-targets", "supported_values"),
        ("aggregate-exclusion-category", "supported_selector"),
        ("rice-selector-count", "expected_matches"),
        ("individual-catalogue-record", "supported_values"),
        ("historical-identifier", "value"),
        ("basic-graph-definition", "definition"),
        ("basic-graph-match", "match"),
    ],
)
def test_claim_subtype_matrix_rejects_missing_required_fields(
    catalogue, annotations, claim_type, required_field
):
    row_id = catalogue["records"][0]["catalogue_id"]
    evidence_by_type = {
        "catalogue-target": annotations["evidence_records"][0],
        "aggregate-exclusion-category": annotations["evidence_records"][1],
        "rice-selector-count": annotations["evidence_records"][2],
        "exclusion-category-targets": annotations["evidence_records"][3],
        "individual-catalogue-record": _retained_evidence(row_id),
        "historical-identifier": _historical_identifier_evidence(row_id),
        "basic-graph-definition": _graph_definition_evidence(),
        "basic-graph-match": _graph_match_evidence(row_id),
    }
    evidence = evidence_by_type[claim_type]
    if evidence not in annotations["evidence_records"]:
        annotations["evidence_records"].append(evidence)
    evidence["claim"].pop(required_field)
    with pytest.raises(ValueError, match="missing fields"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("case_id", "mutation"),
    [
        ("source-missing-citation", "source"),
        ("evidence-wrong-paraphrase-type", "evidence"),
        ("publication-bool-year", "publication"),
        ("target-duplicate-reference", "target-reference"),
        ("rule-invalid-kind", "rule-kind"),
        ("annotation-missing-notes", "annotation"),
        ("claim-wrong-controlled-type", "claim-type"),
    ],
)
def test_version_two_contract_mutation_matrix(
    catalogue, annotations, case_id, mutation
):
    if mutation == "source":
        annotations["sources"][0].pop("citation")
    elif mutation == "evidence":
        annotations["evidence_records"][0]["paraphrase"] = 1
    elif mutation == "publication":
        annotations["sources"][0]["publication"]["year"] = True
    elif mutation == "target-reference":
        ids = annotations["target"]["evidence_record_ids"]
        ids.append(ids[0])
    elif mutation == "rule-kind":
        annotations["rules"][0]["kind"] = "unknown-rule-kind"
    elif mutation == "annotation":
        annotations["rules"] = []
        row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
        row.pop("notes")
        annotations["records"] = [row]
    else:
        annotations["evidence_records"][0]["claim"]["claim_type"] = []
    with pytest.raises(ValueError, match="missing|requires|integer|duplicates|unsupported|valid"):
        generate_evidence_ledger(catalogue, annotations)


def test_original_catalogue_ids_and_file_are_unchanged(catalogue):
    regenerated = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
    assert regenerated == catalogue
    assert [row["catalogue_id"] for row in regenerated["records"]] == [
        row["catalogue_id"] for row in catalogue["records"]
    ]

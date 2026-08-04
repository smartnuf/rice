import json
from collections import Counter
from copy import deepcopy
from pathlib import Path

import pytest

from rice.ladenheim_evidence import (
    FOUR_ELEMENT_AGGREGATE_ID,
    FOUR_ELEMENT_COMPUTATION_ID,
    REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS,
    REVIEWED_LOW_ORDER_CANONICAL_NETWORKS,
    _is_unstable_time_key,
    _validate_disposition_partition,
    _validate_exclusion_counts,
    _validate_generated_ledger,
    generate_evidence_ledger,
)


CATALOGUE_PATH = Path("data/counts/ladenheim-148.json")
ANNOTATION_PATH = Path("data/comparisons/ladenheim-108-annotations.json")
LEDGER_PATH = Path("data/comparisons/ladenheim-148-to-108.json")
ZOBEL_FOUR_ELEMENT_IDS = {
    "lh148-d5533186cc51bbab",
    "lh148-92649d60cfda8308",
    "lh148-13547be0432aeee6",
    "lh148-5c74dc46f966ac91",
}
SIMPLER_BILINEAR_IDS = {
    "lh148-42d941084ce5f049",
    "lh148-8e314b1dc699f2f3",
    "lh148-a134c33979433ce6",
    "lh148-f0ea8600831b22d5",
    "lh148-82299f914f077df2",
    "lh148-932f408750ebae4c",
    "lh148-f0feabf623eadb0d",
    "lh148-f78bad46fde941ae",
}
ZOBEL_GRAPH_L_TARGETS = {
    "lh148-f684b6a0ad3114c4": 20,
    "lh148-2a3f20a9bcd73817": 32,
    "lh148-a124f387d970b947": 25,
    "lh148-5eb31698974d07f8": 28,
}
GRAPH_L_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-l-group"
GRAPH_L_DEFINITION_ID = "ms-2019-basic-graph-l-definition"
GRAPH_L_COMPUTATION_ID = "rice-five-element-zobel-graph-l-report-reproduction"
ZOBEL_GRAPH_M_ID = "lh148-045c192be4de396d"
GRAPH_M_TARGET = 72
GRAPH_M_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-m-group"
GRAPH_M_DEFINITION_ID = "ms-2019-basic-graph-m-definition"
GRAPH_M_GRAPH_MATCH_ID = "rice-lh148-045c192be4de396d-graph-m-match"
GRAPH_M_TARGET_MATCH_ID = "rice-lh148-045c192be4de396d-target-72"
GRAPH_M_COMPUTATION_ID = "rice-five-element-zobel-graph-m-report-reproduction"
ZOBEL_GRAPH_M_DUAL_ID = "lh148-635770ede187bca9"
GRAPH_M_DUAL_TARGET = 73
GRAPH_M_DUAL_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-m-dual-group"
GRAPH_M_DUAL_DEFINITION_ID = "ms-2019-basic-graph-m-dual-definition"
GRAPH_M_DUAL_GRAPH_MATCH_ID = (
    "rice-lh148-635770ede187bca9-graph-m-dual-match"
)
GRAPH_M_DUAL_TARGET_MATCH_ID = "rice-lh148-635770ede187bca9-target-73"
GRAPH_M_DUAL_COMPUTATION_ID = (
    "rice-five-element-zobel-graph-m-dual-report-reproduction"
)
ZOBEL_GRAPH_L_DUAL_TARGETS = {
    "lh148-5d5fb848a810c9cb": 43,
    "lh148-534a4f02579831e9": 47,
    "lh148-9e140322bfd33a22": 39,
    "lh148-a1e6c042c7d77e41": 35,
}
GRAPH_L_DUAL_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-l-dual-group"
GRAPH_L_DUAL_DEFINITION_ID = "ms-2019-basic-graph-l-dual-definition"
GRAPH_L_DUAL_COMPUTATION_ID = (
    "rice-five-element-zobel-graph-l-dual-report-reproduction"
)
ZOBEL_GRAPH_S_TARGETS = {
    "lh148-dffc6c65dc65c0ec": 22,
    "lh148-5bdd1d37b2007a4c": 24,
    "lh148-3a7ebfebce0db0a4": 30,
    "lh148-53370c9917eea4d0": 33,
    "lh148-45d19cefc5b496ce": 73,
}
GRAPH_S_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-s-group"
GRAPH_S_DEFINITION_ID = "ms-2019-basic-graph-s-definition"
GRAPH_S_COMPUTATION_ID = "rice-five-element-zobel-graph-s-report-reproduction"
ZOBEL_GRAPH_S_DUAL_TARGETS = {
    "lh148-84fedcab1cc7f77d": 37,
    "lh148-81ffdfa53c07c484": 40,
    "lh148-4cf39db00710fb1c": 45,
    "lh148-3bf13e1a1ad41cd5": 48,
    "lh148-aefb4b8fe01749c6": 72,
}
GRAPH_S_DUAL_AGGREGATE_ID = "ms-2019-five-element-zobel-graph-s-dual-group"
GRAPH_S_DUAL_DEFINITION_ID = "ms-2019-basic-graph-s-dual-definition"
GRAPH_S_DUAL_COMPUTATION_ID = (
    "rice-five-element-zobel-graph-s-dual-report-reproduction"
)


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


def _populate_derived_structural_group(catalogue, annotations):
    unresolved_ids = [
        row["catalogue_id"]
        for row in generate_evidence_ledger(catalogue, annotations)["records"]
        if row["comparison_status"] == "unresolved"
    ][:4]
    annotations["records"] = []
    targets = [20, 25, 28, 32]
    source_id = "fixture-graph-report"
    aggregate_id = "fixture-aggregate-graph-l"
    definition_id = "fixture-graph-l-definition"
    computation_id = "fixture-graph-l-computation"
    annotations["sources"].append({
        "source_id": source_id,
        "source_type": "rice-documentation",
        "citation": "Fixture reviewed graph-family evidence report.",
        "notes": "Test fixture only.",
    })
    annotations["evidence_records"].extend([
        {
            "evidence_id": aggregate_id,
            "source_id": "morelli-smith-2019",
            "provenance_level": "authoritative-source-transcription",
            "verification_state": "source-verified",
            "locator": {
                "section": "5.1",
                "printed_page": 42,
                "pdf_page_index": 48,
            },
            "paraphrase": "Four graph-L networks reduce to four targets.",
            "claim": {
                "claim_type": "aggregate-basic-graph-exclusion",
                "graph_label": "L",
                "source_population": 4,
                "supported_disposition": "exclude",
                "supported_exclusion_category": (
                    "zobel-five-element-series-parallel"
                ),
                "supported_reduction_targets": list(targets),
            },
        },
        {
            "evidence_id": definition_id,
            "source_id": "morelli-smith-2019",
            "provenance_level": "authoritative-source-transcription",
            "verification_state": "source-verified",
            "locator": {
                "appendix": "B",
                "printed_page": 126,
                "pdf_page_index": 132,
            },
            "paraphrase": "Appendix B defines graph L.",
            "claim": {
                "claim_type": "basic-graph-definition",
                "definition": {
                    "graph_label": "L",
                    "base_label": "L",
                    "is_dual": False,
                    "fixture_id": "fixture-L-five-edge",
                },
            },
        },
    ])
    computation = _cross_check()
    computation.update({
        "cross_check_id": computation_id,
        "implementation": "fixture graph-group reproduction",
        "operation": "match coloured fixtures and exact reductions",
        "result": "four unique subject and target matches",
        "subject_catalogue_ids": list(unresolved_ids),
        "reduction_target_network_numbers": list(targets),
        "verified_evidence_record_ids": [
            *(
                f"fixture-{catalogue_id}-graph-match"
                for catalogue_id in unresolved_ids
            ),
            *(
                f"fixture-{catalogue_id}-target-match"
                for catalogue_id in unresolved_ids
            ),
        ],
    })
    annotations["computational_cross_checks"].append(computation)
    for catalogue_id, target in zip(unresolved_ids, targets):
        graph_id = f"fixture-{catalogue_id}-graph-match"
        target_id = f"fixture-{catalogue_id}-target-match"
        annotations["evidence_records"].extend([
            {
                "evidence_id": graph_id,
                "source_id": source_id,
                "provenance_level": "rice-derived-structural-fact",
                "verification_state": "cross-checked",
                "locator": {"repository_path": "docs/fixture-report.md"},
                "paraphrase": "The subject matches the graph-L fixture.",
                "claim": {
                    "claim_type": "basic-graph-match",
                    "subject_catalogue_ids": [catalogue_id],
                    "match": {
                        "fixture_id": "fixture-L-five-edge",
                        "graph_label": "L",
                        "structural_relation": (
                            "colour-preserving-port-augmented-cycle-matroid-v1"
                        ),
                        "matched": True,
                    },
                },
            },
            {
                "evidence_id": target_id,
                "source_id": source_id,
                "provenance_level": (
                    "rice-derived-network-equivalence-fact"
                ),
                "verification_state": "cross-checked",
                "locator": {"repository_path": "docs/fixture-report.md"},
                "paraphrase": "The subject reduces to its allocated target.",
                "claim": {
                    "claim_type": "reduction-target-match",
                    "subject_catalogue_ids": [catalogue_id],
                    "target_network_number": target,
                },
            },
        ])
        annotations["records"].append({
            "catalogue_id": catalogue_id,
            "comparison_status": "derived-structural-match",
            "proposed_disposition": "exclude",
            "exclusion_category": "zobel-five-element-series-parallel",
            "exclusion_reason": (
                "Aggregate graph-family exclusion with independently checked "
                "subject and reduction-target matches."
            ),
            "evidence_basis": [
                (
                    "aggregate-historical-graph-group-plus-subject-bound-"
                    "rice-match"
                ),
                "mechanically-derived-rice-structural-fact",
            ],
            "evidence_record_ids": [
                aggregate_id,
                definition_id,
                graph_id,
                target_id,
            ],
            "previous_workspace_record_ids": [],
            "computational_cross_check_ids": [computation_id],
            "historical_identifiers": [],
            "basic_graph_assignment": None,
            "confidence": "high",
            "notes": ["Fixture explicit subject-bound mapping."],
            "open_questions": ["Test fixture only."],
        })
    return {
        "aggregate_id": aggregate_id,
        "computation_id": computation_id,
        "definition_id": definition_id,
        "subject_ids": unresolved_ids,
        "targets": targets,
    }


def _previous_workspace_cross_check():
    record = _cross_check()
    record["provenance_level"] = "previous-workspace-generated"
    record["independently_reproduced"] = False
    return record


def test_format_version_six_is_required(catalogue, annotations):
    annotations["format_version"] = 5
    with pytest.raises(ValueError, match="format_version must be 6"):
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
    assert ledger["summary"]["mapped_exclusions"] == 40


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
    with pytest.raises(ValueError, match="exactly the two reviewed aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_target_requires_category_target_evidence(catalogue, annotations):
    annotations["target"]["evidence_record_ids"].remove(
        "ms-2019-four-exclusion-category-targets"
    )
    with pytest.raises(ValueError, match="exactly the two reviewed aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_generated_target_references_its_evidence(catalogue, annotations):
    target = generate_evidence_ledger(catalogue, annotations)["target"]
    assert target["evidence_record_ids"] == [
        "ms-2019-reported-148-to-108",
        "ms-2019-four-exclusion-category-targets",
    ]


@pytest.mark.parametrize(
    "extra_kind", ["aggregate", "definition", "match", "unrelated"]
)
def test_target_rejects_every_additional_evidence_record(
    catalogue, annotations, extra_kind
):
    extra_id = {
        "aggregate": LOW_ORDER_AGGREGATE_ID,
        "definition": _low_order_definitions(annotations)[0]["evidence_id"],
        "match": _low_order_matches(annotations)[0]["evidence_id"],
        "unrelated": "ms-2019-eight-four-resistor-one-reactive",
    }[extra_kind]
    annotations["target"]["evidence_record_ids"].append(extra_id)
    with pytest.raises(ValueError, match="exactly the two reviewed aggregate"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "required_id",
    [
        "ms-2019-reported-148-to-108",
        "ms-2019-four-exclusion-category-targets",
    ],
)
def test_target_rejects_each_missing_required_evidence(
    catalogue, annotations, required_id
):
    annotations["target"]["evidence_record_ids"].remove(required_id)
    with pytest.raises(ValueError, match="exactly the two reviewed aggregate"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "required_id",
    [
        "ms-2019-reported-148-to-108",
        "ms-2019-four-exclusion-category-targets",
    ],
)
def test_target_rejects_replacement_evidence(catalogue, annotations, required_id):
    ids = annotations["target"]["evidence_record_ids"]
    ids[ids.index(required_id)] = "ms-2019-eight-four-resistor-one-reactive"
    with pytest.raises(ValueError, match="exactly the two reviewed aggregate"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("required_index", [0, 1])
def test_target_rejects_duplicate_required_evidence(
    catalogue, annotations, required_index
):
    ids = annotations["target"]["evidence_record_ids"]
    ids.append(ids[required_index])
    with pytest.raises(ValueError, match="duplicates"):
        generate_evidence_ledger(catalogue, annotations)


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
def test_ambiguous_status_is_unavailable_in_version_three(
    catalogue, annotations, basis
):
    annotations["rules"] = []
    row = _unresolved_annotation(catalogue["records"][0]["catalogue_id"])
    row.update(
        comparison_status="ambiguous",
        evidence_basis=basis,
        notes=["Finite candidates are not represented in version 3."],
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
    for number, row in enumerate(rows, start=100):
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


def test_committed_ledger_has_exact_low_order_historical_identifiers():
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    identifiers = [
        (row["catalogue_id"], identifier)
        for row in ledger["records"]
        for identifier in row["historical_identifiers"]
    ]
    assert len(identifiers) == 25
    assert {
        (row_id, identifier["value"])
        for row_id, identifier in identifiers
    } == {
        (payload[0], number)
        for number, payload in REVIEWED_LOW_ORDER_CANONICAL_NETWORKS.items()
    }
    assert all(
        identifier["scheme"] == "morelli-smith-canonical-network"
        and identifier["verification_state"] == "cross-checked"
        for _, identifier in identifiers
    )


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
        ("morelli-smith-canonical-network", 1.0, False),
        ("morelli-smith-canonical-network", "1", False),
        ("morelli-smith-canonical-network", 1, False),
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
            40,
            Counter(
                {
                    "simpler-bilinear-realisation": 8,
                    "zobel-four-element": 3,
                }
            ),
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


def test_exact_forty_83_and_25_distribution(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["summary"]["by_comparison_status"] == {
        "derived-nongeneric-simplification-match": 8,
        "derived-structural-match": 20,
        "derived-unique-match": 12,
        "derived-canonical-identity-match": 25,
        "unresolved": 83,
    }
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 25,
        "unresolved": 83,
    }
    assert ledger["summary"]["by_exclusion_category"] == {
        "other-canonical-exclusion": 8,
        "simpler-bilinear-realisation": 8,
        "none": 25,
        "unresolved": 83,
        "zobel-five-element-series-parallel": 20,
        "zobel-four-element": 4,
    }
    assert ledger["summary"]["mapped_exclusions"] == 40
    assert ledger["summary"]["unresolved_dispositions"] == 83
    assert sum(
        row["proposed_disposition"] == "retain" for row in ledger["records"]
    ) == 25
    mapped = [row for row in ledger["records"] if row["proposed_disposition"] == "exclude"]
    assert len(mapped) == 40
    assert all(row["comparison_status"] != "ambiguous" for row in ledger["records"])
    assert ledger["target"]["reproduction_claimed"] is False
    assert sum(bool(row["historical_identifiers"]) for row in ledger["records"]) == 25
    assert all(row["basic_graph_assignment"] is None for row in ledger["records"])


def _fixture_evidence(annotations, claim_type, subject_id=None):
    matches = [
        record
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"] == claim_type
        and (
            subject_id is not None
            or record["evidence_id"].startswith("fixture-")
        )
        and (
            subject_id is None
            or record["claim"].get("subject_catalogue_ids") == [subject_id]
        )
    ]
    assert len(matches) == 1
    return matches[0]


def _fixture_computation(annotations, computation_id):
    matches = [
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == computation_id
    ]
    assert len(matches) == 1
    return matches[0]


def _append_graph_definition(
    annotations, *, evidence_id, fixture_id, graph_label="L"
):
    definition = deepcopy(
        _fixture_evidence(annotations, "basic-graph-definition")
    )
    definition["evidence_id"] = evidence_id
    definition["claim"]["definition"]["graph_label"] = graph_label
    definition["claim"]["definition"]["fixture_id"] = fixture_id
    annotations["evidence_records"].append(definition)
    return definition


def _fixture_graph_assignment(annotations, fixture, member_index=0):
    catalogue_id = fixture["subject_ids"][member_index]
    graph = _fixture_evidence(annotations, "basic-graph-match", catalogue_id)
    definition = _fixture_evidence(annotations, "basic-graph-definition")
    return {
        **definition["claim"]["definition"],
        "structural_relation": graph["claim"]["match"]["structural_relation"],
        "verification_state": "cross-checked",
        "evidence_record_ids": [definition["evidence_id"], graph["evidence_id"]],
    }


def _set_separately_evidenced_graph_assignment(
    annotations,
    fixture,
    *,
    graph_label="L",
    base_label="L",
    is_dual=False,
    fixture_id="fixture-L-five-edge",
    structural_relation=(
        "colour-preserving-port-augmented-cycle-matroid-v1"
    ),
):
    catalogue_id = fixture["subject_ids"][0]
    definition = deepcopy(_fixture_evidence(annotations, "basic-graph-definition"))
    definition["evidence_id"] = "fixture-separate-graph-definition"
    definition["claim"]["definition"] = {
        "graph_label": graph_label,
        "base_label": base_label,
        "is_dual": is_dual,
        "fixture_id": fixture_id,
    }
    graph = deepcopy(
        _fixture_evidence(annotations, "basic-graph-match", catalogue_id)
    )
    graph["evidence_id"] = "fixture-separate-graph-match"
    graph["claim"]["match"] = {
        "fixture_id": fixture_id,
        "graph_label": graph_label,
        "structural_relation": structural_relation,
        "matched": True,
    }
    annotations["evidence_records"].extend([definition, graph])
    annotations["records"][0]["basic_graph_assignment"] = {
        **definition["claim"]["definition"],
        "structural_relation": structural_relation,
        "verification_state": "cross-checked",
        "evidence_record_ids": [definition["evidence_id"], graph["evidence_id"]],
    }


def test_complete_derived_structural_group_is_accepted(catalogue, annotations):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["comparison_status"] == "derived-structural-match"
    }
    assert set(rows) == set(fixture["subject_ids"])
    assert len(rows) == 4
    assert all(row["proposed_disposition"] == "exclude" for row in rows.values())
    assert all(row["basic_graph_assignment"] is None for row in rows.values())
    assert all(row["historical_identifiers"] == [] for row in rows.values())


def test_derived_structural_group_accepts_exact_graph_assignment(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    annotations["records"][0]["basic_graph_assignment"] = (
        _fixture_graph_assignment(annotations, fixture)
    )
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "changes",
    [
        {"graph_label": "G", "base_label": "G", "fixture_id": "fixture-G"},
        {"fixture_id": "fixture-L-other"},
        {"base_label": "L-other"},
        {"is_dual": True},
        {"structural_relation": "other-structural-relation"},
    ],
)
def test_derived_structural_group_rejects_inconsistent_graph_assignment(
    catalogue, annotations, changes
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    _set_separately_evidenced_graph_assignment(
        annotations, fixture, **changes
    )
    with pytest.raises(ValueError, match="graph assignment must use"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_duplicate_assignment_definition(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    assignment = _fixture_graph_assignment(annotations, fixture)
    duplicate = _append_graph_definition(
        annotations,
        evidence_id="fixture-duplicate-assignment-definition",
        fixture_id=assignment["fixture_id"],
    )
    assignment["evidence_record_ids"][0] = duplicate["evidence_id"]
    annotations["records"][0]["basic_graph_assignment"] = assignment
    with pytest.raises(ValueError, match="graph assignment must use"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_assignment_requires_selected_graph_match(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    assignment = _fixture_graph_assignment(annotations, fixture)
    graph = deepcopy(
        _fixture_evidence(
            annotations, "basic-graph-match", fixture["subject_ids"][0]
        )
    )
    graph["evidence_id"] = "fixture-duplicate-assignment-graph-match"
    annotations["evidence_records"].append(graph)
    assignment["evidence_record_ids"][1] = graph["evidence_id"]
    annotations["records"][0]["basic_graph_assignment"] = assignment
    with pytest.raises(ValueError, match="graph assignment must use"):
        generate_evidence_ledger(catalogue, annotations)


def test_aggregate_graph_claim_cannot_also_support_existing_rule(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    annotations["rules"][0]["evidence_record_ids"].append(fixture["aggregate_id"])
    with pytest.raises(ValueError, match="may support only explicit"):
        generate_evidence_ledger(catalogue, annotations)


def test_rule_only_aggregate_graph_claim_consumer_is_rejected(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    annotations["records"] = []
    annotations["rules"][1]["evidence_record_ids"].append(fixture["aggregate_id"])
    with pytest.raises(ValueError, match="may support only explicit"):
        generate_evidence_ledger(catalogue, annotations)


def test_unresolved_record_cannot_consume_aggregate_graph_claim(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    row = _unresolved_annotation(fixture["subject_ids"][0])
    row["evidence_record_ids"] = [fixture["aggregate_id"]]
    annotations["records"] = [row]
    with pytest.raises(ValueError, match="may support only explicit"):
        generate_evidence_ledger(catalogue, annotations)


def test_source_backed_record_cannot_consume_aggregate_graph_claim(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    retained = _retained_evidence(fixture["subject_ids"][0])
    annotations["evidence_records"].append(retained)
    row = _source_backed_fixture(catalogue, annotations)
    row["catalogue_id"] = fixture["subject_ids"][0]
    row["evidence_record_ids"] = [retained["evidence_id"], fixture["aggregate_id"]]
    with pytest.raises(ValueError, match="may support only explicit"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_incomplete_population(
    catalogue, annotations
):
    _populate_derived_structural_group(catalogue, annotations)
    annotations["records"].pop()
    with pytest.raises(ValueError, match="group population"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_excessive_population(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    extra_id = next(
        row["catalogue_id"]
        for row in catalogue["records"]
        if row["catalogue_id"] not in fixture["subject_ids"]
        and row["catalogue_id"] not in {
            item["catalogue_id"] for item in annotations["records"]
        }
    )
    template_id = fixture["subject_ids"][-1]
    extra = deepcopy(annotations["records"][-1])
    extra["catalogue_id"] = extra_id
    graph = deepcopy(_fixture_evidence(annotations, "basic-graph-match", template_id))
    graph["evidence_id"] = f"fixture-{extra_id}-graph-match"
    graph["claim"]["subject_catalogue_ids"] = [extra_id]
    target = deepcopy(
        _fixture_evidence(annotations, "reduction-target-match", template_id)
    )
    target["evidence_id"] = f"fixture-{extra_id}-target-match"
    target["claim"]["subject_catalogue_ids"] = [extra_id]
    annotations["evidence_records"].extend([graph, target])
    extra["evidence_record_ids"][-2:] = [graph["evidence_id"], target["evidence_id"]]
    annotations["records"].append(extra)
    with pytest.raises(ValueError, match="group population"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_duplicate_target(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    last = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][-1]
    )
    last["claim"]["target_network_number"] = fixture["targets"][0]
    with pytest.raises(ValueError, match="targets must be unique"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_target_outside_source_set(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][-1]
    )
    target["claim"]["target_network_number"] = 99
    with pytest.raises(ValueError, match="subject-bound reduction-target match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_missing_authoritative_target(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    aggregate = _fixture_evidence(
        annotations, "aggregate-basic-graph-exclusion"
    )
    aggregate["claim"]["supported_reduction_targets"][-1] = 31
    assert fixture["targets"][-1] not in aggregate["claim"][
        "supported_reduction_targets"
    ]
    with pytest.raises(ValueError, match="subject-bound reduction-target match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("field", ["graph_label", "fixture_id"])
def test_derived_structural_group_rejects_graph_or_fixture_mismatch(
    catalogue, annotations, field
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    match = _fixture_evidence(
        annotations, "basic-graph-match", fixture["subject_ids"][0]
    )
    match["claim"]["match"][field] = "wrong"
    with pytest.raises(ValueError, match="subject-bound graph match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_row_rejects_other_subject_graph_match(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    other = _fixture_evidence(
        annotations, "basic-graph-match", fixture["subject_ids"][1]
    )
    annotations["records"][0]["evidence_record_ids"].append(other["evidence_id"])
    with pytest.raises(ValueError, match="one exact subject-bound graph match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_row_rejects_two_positive_graph_matches(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    graph = deepcopy(
        _fixture_evidence(
            annotations, "basic-graph-match", fixture["subject_ids"][0]
        )
    )
    graph["evidence_id"] = "fixture-second-positive-graph-match"
    annotations["evidence_records"].append(graph)
    annotations["records"][0]["evidence_record_ids"].append(graph["evidence_id"])
    with pytest.raises(ValueError, match="one exact subject-bound graph match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_split_authoritative_fixtures(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    second = _append_graph_definition(
        annotations,
        evidence_id="fixture-graph-l-second-definition",
        fixture_id="fixture-L-alternate-five-edge",
    )
    for catalogue_id, row in zip(fixture["subject_ids"][2:], annotations["records"][2:]):
        row["evidence_record_ids"][1] = second["evidence_id"]
        match = _fixture_evidence(annotations, "basic-graph-match", catalogue_id)
        match["claim"]["match"]["fixture_id"] = "fixture-L-alternate-five-edge"
    with pytest.raises(ValueError, match="common authoritative graph-definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_different_definition_id(
    catalogue, annotations
):
    _populate_derived_structural_group(catalogue, annotations)
    second = _append_graph_definition(
        annotations,
        evidence_id="fixture-graph-l-duplicate-definition",
        fixture_id="fixture-L-five-edge",
    )
    annotations["records"][-1]["evidence_record_ids"][1] = second["evidence_id"]
    with pytest.raises(ValueError, match="common authoritative graph-definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_match_outside_common_fixture(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    match = _fixture_evidence(
        annotations, "basic-graph-match", fixture["subject_ids"][-1]
    )
    match["claim"]["match"]["fixture_id"] = "fixture-L-alternate-five-edge"
    with pytest.raises(ValueError, match="subject-bound graph match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_target_for_wrong_subject(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][0]
    )
    target["claim"]["subject_catalogue_ids"] = [fixture["subject_ids"][1]]
    with pytest.raises(ValueError, match="subject-bound reduction-target match"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_row_rejects_other_subject_target_match(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    other = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][1]
    )
    annotations["records"][0]["evidence_record_ids"].append(other["evidence_id"])
    with pytest.raises(ValueError, match="one exact subject-bound reduction-target"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_row_rejects_conflicting_positive_target_matches(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = deepcopy(
        _fixture_evidence(
            annotations, "reduction-target-match", fixture["subject_ids"][0]
        )
    )
    target["evidence_id"] = "fixture-conflicting-positive-target-match"
    target["claim"]["target_network_number"] = fixture["targets"][1]
    annotations["evidence_records"].append(target)
    annotations["records"][0]["evidence_record_ids"].append(target["evidence_id"])
    with pytest.raises(ValueError, match="one exact subject-bound reduction-target"):
        generate_evidence_ledger(catalogue, annotations)


def test_reduction_target_matching_network_locator_is_accepted(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][0]
    )
    target["locator"]["network_number"] = fixture["targets"][0]
    generate_evidence_ledger(catalogue, annotations)


def test_reduction_target_network_locator_mismatch_is_rejected(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][0]
    )
    target["locator"]["network_number"] = 99
    with pytest.raises(ValueError, match="reduction-target locator does not match"):
        generate_evidence_ledger(catalogue, annotations)


def test_reduction_target_locator_may_omit_network_number(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    target = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][0]
    )
    assert target["locator"] == {"repository_path": "docs/fixture-report.md"}
    generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_requires_reproduced_computation(
    catalogue, annotations
):
    _populate_derived_structural_group(catalogue, annotations)
    annotations["records"][0]["computational_cross_check_ids"] = []
    with pytest.raises(ValueError, match="independently reproduced"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_positive_unscoped_computation(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    del computation["subject_catalogue_ids"]
    del computation["reduction_target_network_numbers"]
    del computation["verified_evidence_record_ids"]
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_scope_without_verified_evidence(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    del computation["verified_evidence_record_ids"]
    with pytest.raises(ValueError, match="scope fields must be present together"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_missing_graph_evidence_binding(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    graph_id = _fixture_evidence(
        annotations, "basic-graph-match", fixture["subject_ids"][0]
    )["evidence_id"]
    computation["verified_evidence_record_ids"].remove(graph_id)
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_missing_target_evidence_binding(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    target_id = _fixture_evidence(
        annotations, "reduction-target-match", fixture["subject_ids"][0]
    )["evidence_id"]
    computation["verified_evidence_record_ids"].remove(target_id)
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_extra_evidence_binding(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    computation["verified_evidence_record_ids"].append(fixture["aggregate_id"])
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_other_subject_evidence_binding(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    other = next(
        record
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"] == "basic-graph-match"
        and record["claim"]["subject_catalogue_ids"][0]
        not in fixture["subject_ids"]
    )
    computation["verified_evidence_record_ids"][0] = other["evidence_id"]
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_wrong_computation_subjects(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    replacement = next(
        row["catalogue_id"]
        for row in catalogue["records"]
        if row["catalogue_id"] not in fixture["subject_ids"]
    )
    computation["subject_catalogue_ids"][-1] = replacement
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_wrong_computation_targets(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    computation["reduction_target_network_numbers"][-1] = 31
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_computation_missing_subject(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    computation["subject_catalogue_ids"].pop()
    computation["reduction_target_network_numbers"].pop()
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_computation_extra_subject(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(annotations, fixture["computation_id"])
    extra = next(
        row["catalogue_id"]
        for row in catalogue["records"]
        if row["catalogue_id"] not in fixture["subject_ids"]
    )
    computation["subject_catalogue_ids"].append(extra)
    computation["reduction_target_network_numbers"].append(31)
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_different_scoped_computations(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    second = deepcopy(
        _fixture_computation(annotations, fixture["computation_id"])
    )
    second["cross_check_id"] = "fixture-graph-l-second-computation"
    annotations["computational_cross_checks"].append(second)
    for row in annotations["records"][2:]:
        row["computational_cross_check_ids"] = [second["cross_check_id"]]
    with pytest.raises(ValueError, match="one common independently reproduced"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_rejects_unrelated_existing_computation(
    catalogue, annotations
):
    _populate_derived_structural_group(catalogue, annotations)
    for row in annotations["records"][-4:]:
        row["computational_cross_check_ids"] = [
            "rice-four-element-zobel-report-reproduction"
        ]
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_relabelled_four_element_computation_cannot_verify_fixture_group(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    computation = _fixture_computation(
        annotations, "rice-four-element-zobel-report-reproduction"
    )
    computation["subject_catalogue_ids"] = list(fixture["subject_ids"])
    computation["reduction_target_network_numbers"] = list(fixture["targets"])
    computation["verified_evidence_record_ids"] = [fixture["aggregate_id"]]
    for row in annotations["records"][-4:]:
        row["computational_cross_check_ids"] = [computation["cross_check_id"]]
    with pytest.raises(ValueError, match="scoped to its exact subjects"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_group_requires_authoritative_aggregate(
    catalogue, annotations
):
    _populate_derived_structural_group(catalogue, annotations)
    aggregate = _fixture_evidence(
        annotations, "aggregate-basic-graph-exclusion"
    )
    aggregate["verification_state"] = "cross-checked"
    with pytest.raises(ValueError, match="authoritative aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_match_is_invalid_in_rule(catalogue, annotations):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    template = deepcopy(annotations["records"][0])
    del template["catalogue_id"]
    annotations["records"] = []
    annotations["rules"] = []
    source = next(
        row for row in catalogue["records"] if row["catalogue_id"] in fixture["subject_ids"]
    )
    selector = {"r": source["r"], "l": source["l"], "c": source["c"]}
    count = sum(
        all(row[field] == value for field, value in selector.items())
        for row in catalogue["records"]
    )
    template.update({
        "rule_id": "invalid-derived-structural-rule",
        "kind": "unique-component-match",
        "selector": selector,
        "expected_matches": count,
    })
    annotations["rules"].append(template)
    with pytest.raises(ValueError, match="only for explicit annotation records"):
        generate_evidence_ledger(catalogue, annotations)


def test_derived_structural_match_cannot_retain(catalogue, annotations):
    _populate_derived_structural_group(catalogue, annotations)
    row = annotations["records"][0]
    row["proposed_disposition"] = "retain"
    row["exclusion_category"] = "none"
    row["exclusion_reason"] = None
    with pytest.raises(ValueError, match="cannot assert retention"):
        generate_evidence_ledger(catalogue, annotations)


def test_reduction_target_is_not_historical_identity_without_evidence(
    catalogue, annotations
):
    fixture = _populate_derived_structural_group(catalogue, annotations)
    row = annotations["records"][0]
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": fixture["targets"][0],
        "verification_state": "parsed",
        "evidence_record_ids": [],
    }]
    with pytest.raises(ValueError, match="historical identity"):
        generate_evidence_ledger(catalogue, annotations)


def test_exact_four_element_zobel_exclusions(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["exclusion_category"] == "zobel-four-element"
    }
    assert set(rows) == ZOBEL_FOUR_ELEMENT_IDS
    assert all(row["proposed_disposition"] == "exclude" for row in rows.values())
    assert all(row["comparison_status"] == "derived-unique-match" for row in rows.values())
    assert {
        (row["r"], row["l"], row["c"], row["rlc"])
        for row in rows.values()
    } == {(3, 1, 0, 4), (3, 0, 1, 4)}


def test_exact_graph_l_five_element_zobel_exclusions(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_L_TARGETS
    }
    assert set(rows) == set(ZOBEL_GRAPH_L_TARGETS)
    assert all(row["proposed_disposition"] == "exclude" for row in rows.values())
    assert all(
        row["exclusion_category"] == "zobel-five-element-series-parallel"
        for row in rows.values()
    )
    assert all(row["basic_graph_assignment"] is None for row in rows.values())
    assert all(row["historical_identifiers"] == [] for row in rows.values())

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    aggregate_references = {
        evidence_id
        for row in rows.values()
        for evidence_id in row["evidence_record_ids"]
        if evidence[evidence_id]["claim"]["claim_type"]
        == "aggregate-basic-graph-exclusion"
    }
    definition_references = {
        evidence_id
        for row in rows.values()
        for evidence_id in row["evidence_record_ids"]
        if evidence[evidence_id]["claim"]["claim_type"]
        == "basic-graph-definition"
    }
    assert aggregate_references == {GRAPH_L_AGGREGATE_ID}
    assert definition_references == {GRAPH_L_DEFINITION_ID}
    assert evidence[GRAPH_L_AGGREGATE_ID]["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "L",
        "source_population": 4,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [20, 25, 28, 32],
    }
    assert evidence[GRAPH_L_DEFINITION_ID]["claim"]["definition"] == {
        "base_label": "L",
        "fixture_id": "morelli-smith-L-five-edge",
        "graph_label": "L",
        "is_dual": False,
    }

    selected_evidence_ids = set()
    for catalogue_id, target in ZOBEL_GRAPH_L_TARGETS.items():
        row = rows[catalogue_id]
        graph_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"] == "basic-graph-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        target_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "reduction-target-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        assert len(graph_matches) == len(target_matches) == 1
        assert graph_matches[0]["claim"]["subject_catalogue_ids"] == [catalogue_id]
        assert graph_matches[0]["claim"]["match"] == {
            "fixture_id": "morelli-smith-L-five-edge",
            "graph_label": "L",
            "matched": True,
            "structural_relation": (
                "colour-preserving-port-augmented-cycle-matroid-v1"
            ),
        }
        assert target_matches[0]["claim"] == {
            "claim_type": "reduction-target-match",
            "subject_catalogue_ids": [catalogue_id],
            "target_network_number": target,
        }
        selected_evidence_ids.update(
            {graph_matches[0]["evidence_id"], target_matches[0]["evidence_id"]}
        )
        assert row["computational_cross_check_ids"] == [GRAPH_L_COMPUTATION_ID]

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_L_COMPUTATION_ID
    )
    assert set(computation["subject_catalogue_ids"]) == set(ZOBEL_GRAPH_L_TARGETS)
    assert set(computation["reduction_target_network_numbers"]) == set(
        ZOBEL_GRAPH_L_TARGETS.values()
    )
    assert set(computation["verified_evidence_record_ids"]) == selected_evidence_ids


def test_exact_graph_l_dual_five_element_zobel_exclusions(
    catalogue, annotations
):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_L_DUAL_TARGETS
    }
    assert set(rows) == set(ZOBEL_GRAPH_L_DUAL_TARGETS)
    assert all(
        row["comparison_status"] == "derived-structural-match"
        and row["proposed_disposition"] == "exclude"
        and row["exclusion_category"]
        == "zobel-five-element-series-parallel"
        for row in rows.values()
    )
    assert all(row["basic_graph_assignment"] is None for row in rows.values())
    assert all(row["historical_identifiers"] == [] for row in rows.values())

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    assert evidence[GRAPH_L_DUAL_AGGREGATE_ID]["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "L^d",
        "source_population": 4,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [35, 39, 43, 47],
    }
    assert evidence[GRAPH_L_DUAL_DEFINITION_ID]["claim"]["definition"] == {
        "base_label": "L",
        "fixture_id": "morelli-smith-Ld-five-edge",
        "graph_label": "L^d",
        "is_dual": True,
    }

    selected_evidence_ids = set()
    for catalogue_id, target in ZOBEL_GRAPH_L_DUAL_TARGETS.items():
        row = rows[catalogue_id]
        graph_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "basic-graph-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        target_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "reduction-target-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        assert len(graph_matches) == len(target_matches) == 1
        graph_match = graph_matches[0]
        target_match = target_matches[0]
        assert graph_match["claim"] == {
            "claim_type": "basic-graph-match",
            "match": {
                "fixture_id": "morelli-smith-Ld-five-edge",
                "graph_label": "L^d",
                "matched": True,
                "structural_relation": (
                    "colour-preserving-port-augmented-cycle-matroid-v1"
                ),
            },
            "subject_catalogue_ids": [catalogue_id],
        }
        assert target_match["claim"] == {
            "claim_type": "reduction-target-match",
            "subject_catalogue_ids": [catalogue_id],
            "target_network_number": target,
        }
        assert target_match["locator"]["network_number"] == target
        assert "forward Figure 5.2" in target_match["paraphrase"]
        assert "parallel resistors" in target_match["paraphrase"]
        assert "graph-F-dual" in target_match["paraphrase"]
        assert "Figure 5.2" in row["exclusion_reason"]
        assert "graph F-dual" in row["exclusion_reason"]
        assert set(row["evidence_record_ids"]) == {
            GRAPH_L_DUAL_AGGREGATE_ID,
            GRAPH_L_DUAL_DEFINITION_ID,
            graph_match["evidence_id"],
            target_match["evidence_id"],
        }
        assert row["computational_cross_check_ids"] == [
            GRAPH_L_DUAL_COMPUTATION_ID
        ]
        selected_evidence_ids.update(
            {graph_match["evidence_id"], target_match["evidence_id"]}
        )
        assert not any(
            identifier.get("value") == target
            for identifier in row["historical_identifiers"]
        )

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_L_DUAL_COMPUTATION_ID
    )
    assert set(computation["subject_catalogue_ids"]) == set(
        ZOBEL_GRAPH_L_DUAL_TARGETS
    )
    assert set(computation["reduction_target_network_numbers"]) == set(
        ZOBEL_GRAPH_L_DUAL_TARGETS.values()
    )
    assert set(computation["verified_evidence_record_ids"]) == (
        selected_evidence_ids
    )
    assert "forward Figure 5.2 coefficient map" in computation["operation"]
    assert "parallel resistors" in computation["operation"]
    assert "graph-F-dual" in computation["operation"]


def test_exact_graph_s_five_element_zobel_exclusions(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_S_TARGETS
    }
    assert set(rows) == set(ZOBEL_GRAPH_S_TARGETS)
    assert all(
        row["comparison_status"] == "derived-structural-match"
        and row["proposed_disposition"] == "exclude"
        and row["exclusion_category"]
        == "zobel-five-element-series-parallel"
        for row in rows.values()
    )

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    assert evidence[GRAPH_S_AGGREGATE_ID]["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "S",
        "source_population": 5,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [22, 24, 30, 33, 73],
    }
    assert evidence[GRAPH_S_DEFINITION_ID]["claim"]["definition"] == {
        "base_label": "S",
        "fixture_id": "morelli-smith-S-five-edge",
        "graph_label": "S",
        "is_dual": False,
    }

    selected_evidence_ids = set()
    for catalogue_id, target in ZOBEL_GRAPH_S_TARGETS.items():
        row = rows[catalogue_id]
        graph_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "basic-graph-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        target_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "reduction-target-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        assert len(graph_matches) == len(target_matches) == 1
        graph_match = graph_matches[0]
        target_match = target_matches[0]
        assert graph_match["claim"] == {
            "claim_type": "basic-graph-match",
            "match": {
                "fixture_id": "morelli-smith-S-five-edge",
                "graph_label": "S",
                "matched": True,
                "structural_relation": (
                    "colour-preserving-port-augmented-cycle-matroid-v1"
                ),
            },
            "subject_catalogue_ids": [catalogue_id],
        }
        assert target_match["claim"] == {
            "claim_type": "reduction-target-match",
            "subject_catalogue_ids": [catalogue_id],
            "target_network_number": target,
        }
        assert target_match["locator"]["network_number"] == target
        assert "coefficient map" in target_match["paraphrase"]
        if target == 73:
            for phrase in (
                "inverse Figure 5.2",
                "composite parallel L-C",
                "series interchange",
                "series resistors",
                "graph H-dual",
            ):
                assert phrase in target_match["paraphrase"]
        else:
            for phrase in (
                "forward Figure 5.2",
                "parallel resistors",
                "graph G",
            ):
                assert phrase in target_match["paraphrase"]
        assert set(row["evidence_record_ids"]) == {
            GRAPH_S_AGGREGATE_ID,
            GRAPH_S_DEFINITION_ID,
            graph_match["evidence_id"],
            target_match["evidence_id"],
        }
        assert row["computational_cross_check_ids"] == [GRAPH_S_COMPUTATION_ID]
        assert row["basic_graph_assignment"] is None
        assert row["historical_identifiers"] == []
        selected_evidence_ids.update(
            {graph_match["evidence_id"], target_match["evidence_id"]}
        )

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_S_COMPUTATION_ID
    )
    assert set(computation["subject_catalogue_ids"]) == set(ZOBEL_GRAPH_S_TARGETS)
    assert set(computation["reduction_target_network_numbers"]) == set(
        ZOBEL_GRAPH_S_TARGETS.values()
    )
    assert set(computation["verified_evidence_record_ids"]) == (
        selected_evidence_ids
    )
    for phrase in (
        "forward Figure 5.2",
        "merge parallel resistors",
        "graph G",
        "inverse map",
        "composite parallel L-C",
        "series interchange",
        "merge series resistors",
        "graph H-dual",
        "fractions.Fraction",
    ):
        assert phrase in computation["operation"]


def test_exact_graph_s_dual_five_element_zobel_exclusions(
    catalogue, annotations
):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_S_DUAL_TARGETS
    }
    assert set(rows) == set(ZOBEL_GRAPH_S_DUAL_TARGETS)
    assert all(
        row["comparison_status"] == "derived-structural-match"
        and row["proposed_disposition"] == "exclude"
        and row["exclusion_category"]
        == "zobel-five-element-series-parallel"
        and row["basic_graph_assignment"] is None
        and row["historical_identifiers"] == []
        for row in rows.values()
    )

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    assert evidence[GRAPH_S_DUAL_AGGREGATE_ID]["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "S^d",
        "source_population": 5,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [37, 40, 45, 48, 72],
    }
    assert evidence[GRAPH_S_DUAL_DEFINITION_ID]["claim"]["definition"] == {
        "base_label": "S",
        "fixture_id": "morelli-smith-Sd-five-edge",
        "graph_label": "S^d",
        "is_dual": True,
    }

    selected_evidence_ids = set()
    for catalogue_id, target in ZOBEL_GRAPH_S_DUAL_TARGETS.items():
        row = rows[catalogue_id]
        graph_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "basic-graph-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        target_matches = [
            evidence[evidence_id]
            for evidence_id in row["evidence_record_ids"]
            if evidence[evidence_id]["claim"]["claim_type"]
            == "reduction-target-match"
            and evidence[evidence_id]["verification_state"] == "cross-checked"
        ]
        assert len(graph_matches) == len(target_matches) == 1
        graph_match = graph_matches[0]
        target_match = target_matches[0]
        assert graph_match["claim"] == {
            "claim_type": "basic-graph-match",
            "match": {
                "fixture_id": "morelli-smith-Sd-five-edge",
                "graph_label": "S^d",
                "matched": True,
                "structural_relation": (
                    "colour-preserving-port-augmented-cycle-matroid-v1"
                ),
            },
            "subject_catalogue_ids": [catalogue_id],
        }
        assert target_match["claim"] == {
            "claim_type": "reduction-target-match",
            "subject_catalogue_ids": [catalogue_id],
            "target_network_number": target,
        }
        assert target_match["locator"]["network_number"] == target
        assert "coefficient map" in target_match["paraphrase"]
        assert "positive finite" in target_match["paraphrase"]
        assert "both directions" in target_match["paraphrase"]
        if target == 72:
            for phrase in (
                "forward Figure 5.2",
                "composite series L-C",
                "parallel resistors",
                "graph H",
            ):
                assert phrase in target_match["paraphrase"]
        else:
            for phrase in (
                "inverse Figure 5.2",
                "series resistors",
                "graph G-dual",
            ):
                assert phrase in target_match["paraphrase"]
        assert set(row["evidence_record_ids"]) == {
            GRAPH_S_DUAL_AGGREGATE_ID,
            GRAPH_S_DUAL_DEFINITION_ID,
            graph_match["evidence_id"],
            target_match["evidence_id"],
        }
        assert row["computational_cross_check_ids"] == [
            GRAPH_S_DUAL_COMPUTATION_ID
        ]
        selected_evidence_ids.update(
            {graph_match["evidence_id"], target_match["evidence_id"]}
        )
        assert not any(
            identifier.get("value") == target
            for identifier in row["historical_identifiers"]
        )

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_S_DUAL_COMPUTATION_ID
    )
    assert set(computation["subject_catalogue_ids"]) == set(
        ZOBEL_GRAPH_S_DUAL_TARGETS
    )
    assert set(computation["reduction_target_network_numbers"]) == set(
        ZOBEL_GRAPH_S_DUAL_TARGETS.values()
    )
    assert set(computation["verified_evidence_record_ids"]) == (
        selected_evidence_ids
    )
    for phrase in (
        "inverse Figure 5.2",
        "merge series resistors",
        "graph G-dual",
        "forward Figure 5.2",
        "composite series L-C",
        "merge parallel resistors",
        "graph H",
        "positive finite domain in both directions",
        "fractions.Fraction",
    ):
        assert phrase in computation["operation"]


def test_exact_graph_m_five_element_zobel_exclusion(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    row = next(
        record for record in ledger["records"]
        if record["catalogue_id"] == ZOBEL_GRAPH_M_ID
    )
    assert row["comparison_status"] == "derived-structural-match"
    assert row["proposed_disposition"] == "exclude"
    assert row["exclusion_category"] == "zobel-five-element-series-parallel"
    assert row["basic_graph_assignment"] is None
    assert row["historical_identifiers"] == []
    assert row["previous_workspace_record_ids"] == []
    assert row["computational_cross_check_ids"] == [GRAPH_M_COMPUTATION_ID]

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    aggregate = evidence[GRAPH_M_AGGREGATE_ID]
    definition = evidence[GRAPH_M_DEFINITION_ID]
    graph_match = evidence[GRAPH_M_GRAPH_MATCH_ID]
    target_match = evidence[GRAPH_M_TARGET_MATCH_ID]
    assert aggregate["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "M",
        "source_population": 1,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [GRAPH_M_TARGET],
    }
    assert definition["claim"]["definition"] == {
        "base_label": "M",
        "fixture_id": "morelli-smith-M-five-edge",
        "graph_label": "M",
        "is_dual": False,
    }
    assert graph_match["claim"] == {
        "claim_type": "basic-graph-match",
        "match": {
            "fixture_id": "morelli-smith-M-five-edge",
            "graph_label": "M",
            "matched": True,
            "structural_relation": (
                "colour-preserving-port-augmented-cycle-matroid-v1"
            ),
        },
        "subject_catalogue_ids": [ZOBEL_GRAPH_M_ID],
    }
    assert graph_match["verification_state"] == "cross-checked"
    assert target_match["claim"] == {
        "claim_type": "reduction-target-match",
        "subject_catalogue_ids": [ZOBEL_GRAPH_M_ID],
        "target_network_number": GRAPH_M_TARGET,
    }
    assert target_match["verification_state"] == "cross-checked"
    assert set(row["evidence_record_ids"]) == {
        GRAPH_M_AGGREGATE_ID,
        GRAPH_M_DEFINITION_ID,
        GRAPH_M_GRAPH_MATCH_ID,
        GRAPH_M_TARGET_MATCH_ID,
    }

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_M_COMPUTATION_ID
    )
    assert computation["subject_catalogue_ids"] == [ZOBEL_GRAPH_M_ID]
    assert set(computation["reduction_target_network_numbers"]) == {GRAPH_M_TARGET}
    assert set(computation["verified_evidence_record_ids"]) == {
        GRAPH_M_GRAPH_MATCH_ID,
        GRAPH_M_TARGET_MATCH_ID,
    }
    assert not any(
        identifier.get("value") == GRAPH_M_TARGET
        for identifier in row["historical_identifiers"]
    )


def test_exact_graph_m_dual_five_element_zobel_exclusion(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    row = next(
        record for record in ledger["records"]
        if record["catalogue_id"] == ZOBEL_GRAPH_M_DUAL_ID
    )
    assert row["comparison_status"] == "derived-structural-match"
    assert row["proposed_disposition"] == "exclude"
    assert row["exclusion_category"] == "zobel-five-element-series-parallel"
    assert row["basic_graph_assignment"] is None
    assert row["historical_identifiers"] == []
    assert row["previous_workspace_record_ids"] == []
    assert row["computational_cross_check_ids"] == [GRAPH_M_DUAL_COMPUTATION_ID]

    evidence = {
        record["evidence_id"]: record
        for record in annotations["evidence_records"]
    }
    aggregate = evidence[GRAPH_M_DUAL_AGGREGATE_ID]
    definition = evidence[GRAPH_M_DUAL_DEFINITION_ID]
    graph_match = evidence[GRAPH_M_DUAL_GRAPH_MATCH_ID]
    target_match = evidence[GRAPH_M_DUAL_TARGET_MATCH_ID]
    assert aggregate["claim"] == {
        "claim_type": "aggregate-basic-graph-exclusion",
        "graph_label": "M^d",
        "source_population": 1,
        "supported_disposition": "exclude",
        "supported_exclusion_category": "zobel-five-element-series-parallel",
        "supported_reduction_targets": [GRAPH_M_DUAL_TARGET],
    }
    assert definition["claim"]["definition"] == {
        "base_label": "M",
        "fixture_id": "morelli-smith-Md-five-edge",
        "graph_label": "M^d",
        "is_dual": True,
    }
    assert graph_match["claim"] == {
        "claim_type": "basic-graph-match",
        "match": {
            "fixture_id": "morelli-smith-Md-five-edge",
            "graph_label": "M^d",
            "matched": True,
            "structural_relation": (
                "colour-preserving-port-augmented-cycle-matroid-v1"
            ),
        },
        "subject_catalogue_ids": [ZOBEL_GRAPH_M_DUAL_ID],
    }
    assert graph_match["verification_state"] == "cross-checked"
    assert target_match["claim"] == {
        "claim_type": "reduction-target-match",
        "subject_catalogue_ids": [ZOBEL_GRAPH_M_DUAL_ID],
        "target_network_number": GRAPH_M_DUAL_TARGET,
    }
    assert target_match["locator"]["network_number"] == GRAPH_M_DUAL_TARGET
    assert target_match["verification_state"] == "cross-checked"
    assert set(row["evidence_record_ids"]) == {
        GRAPH_M_DUAL_AGGREGATE_ID,
        GRAPH_M_DUAL_DEFINITION_ID,
        GRAPH_M_DUAL_GRAPH_MATCH_ID,
        GRAPH_M_DUAL_TARGET_MATCH_ID,
    }

    computation = next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == GRAPH_M_DUAL_COMPUTATION_ID
    )
    assert computation["subject_catalogue_ids"] == [ZOBEL_GRAPH_M_DUAL_ID]
    assert computation["reduction_target_network_numbers"] == [
        GRAPH_M_DUAL_TARGET
    ]
    assert set(computation["verified_evidence_record_ids"]) == {
        GRAPH_M_DUAL_GRAPH_MATCH_ID,
        GRAPH_M_DUAL_TARGET_MATCH_ID,
    }
    assert not any(
        identifier.get("value") == GRAPH_M_DUAL_TARGET
        for identifier in row["historical_identifiers"]
    )


def test_only_reviewed_exclusions_are_resolved(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    expected = (
        SIMPLER_BILINEAR_IDS
        | ZOBEL_FOUR_ELEMENT_IDS
        | set(ZOBEL_GRAPH_L_TARGETS)
        | set(ZOBEL_GRAPH_L_DUAL_TARGETS)
        | set(ZOBEL_GRAPH_S_TARGETS)
        | set(ZOBEL_GRAPH_S_DUAL_TARGETS)
        | {ZOBEL_GRAPH_M_ID, ZOBEL_GRAPH_M_DUAL_ID}
        | FINAL_EIGHT_SUBJECTS
        | {
            payload[0]
            for payload in REVIEWED_LOW_ORDER_CANONICAL_NETWORKS.values()
        }
    )
    resolved = {
        row["catalogue_id"]
        for row in ledger["records"]
        if row["comparison_status"] != "unresolved"
    }
    assert resolved == expected
    assert all(
        row["comparison_status"] == "unresolved"
        and row["proposed_disposition"] == "unresolved"
        for row in ledger["records"]
        if row["catalogue_id"] not in expected
    )


def test_four_element_zobel_generation_is_deterministic(catalogue, annotations):
    first = generate_evidence_ledger(catalogue, annotations)
    second = generate_evidence_ledger(catalogue, annotations)
    assert first == second
    assert json.loads(LEDGER_PATH.read_text(encoding="utf-8")) == first


def test_existing_simpler_bilinear_exclusions_are_unchanged(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    rows = {
        row["catalogue_id"]: row
        for row in ledger["records"]
        if row["exclusion_category"] == "simpler-bilinear-realisation"
    }
    assert set(rows) == SIMPLER_BILINEAR_IDS
    assert all(row["r"] == 4 and row["lc"] == 1 for row in rows.values())
    assert all(row["proposed_disposition"] == "exclude" for row in rows.values())


def test_exclusion_category_population_and_identity_boundary(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    categories = Counter(row["exclusion_category"] for row in ledger["records"])
    assert categories["simpler-bilinear-realisation"] == 8
    assert categories["zobel-four-element"] == 4
    assert categories["zobel-five-element-series-parallel"] == 20
    assert categories["other-canonical-exclusion"] == 8
    assert categories["none"] == 25
    assert categories["unresolved"] == 83
    assert all(row["basic_graph_assignment"] is None for row in ledger["records"])
    assert sum(bool(row["historical_identifiers"]) for row in ledger["records"]) == 25
    assert all(
        not any(
            identifier.get("value") in {15, 17}
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_FOUR_ELEMENT_IDS
    )
    assert all(
        not any(
            identifier.get("value") in {20, 25, 28, 32}
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_L_TARGETS
    )
    assert all(
        not any(
            identifier.get("value") == GRAPH_M_TARGET
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] == ZOBEL_GRAPH_M_ID
    )
    assert all(
        not any(
            identifier.get("value") == GRAPH_M_DUAL_TARGET
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] == ZOBEL_GRAPH_M_DUAL_ID
    )
    assert all(
        not any(
            identifier.get("value") in set(ZOBEL_GRAPH_L_DUAL_TARGETS.values())
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_L_DUAL_TARGETS
    )
    assert all(
        not any(
            identifier.get("value") in set(ZOBEL_GRAPH_S_TARGETS.values())
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_S_TARGETS
    )
    assert all(
        not any(
            identifier.get("value") in set(ZOBEL_GRAPH_S_DUAL_TARGETS.values())
            for identifier in row["historical_identifiers"]
        )
        for row in ledger["records"]
        if row["catalogue_id"] in ZOBEL_GRAPH_S_DUAL_TARGETS
    )


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
    publication_source = deepcopy(annotations["sources"][0])
    publication_source["source_id"] = "fixture-stable-publication"
    publication_source["publication"]["year"] = 2019
    publication_source["citation"] += " Published in 2019."
    annotations["sources"].append(publication_source)
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
    "path",
    [
        "data/counts/ladenheim-148.json",
        "./data/counts/ladenheim-148.json",
        "../fixtures/graph.json",
    ],
)
def test_repository_relative_path_forms_are_accepted(catalogue, annotations, path):
    annotations["evidence_records"][2]["locator"]["repository_path"] = path
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "text",
    [
        "Local copy: ./data/counts/ladenheim-148.json",
        "Fixture path,../fixtures/graph.json",
    ],
)
def test_dot_relative_paths_embedded_in_prose_are_accepted(
    catalogue, annotations, text
):
    annotations["sources"][0]["notes"] = text
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


def test_category_target_claim_accepts_exact_supported_values_shape(
    catalogue, annotations
):
    generate_evidence_ledger(catalogue, annotations)


def test_category_target_claim_rejects_extra_supported_value(
    catalogue, annotations
):
    values = annotations["evidence_records"][3]["claim"]["supported_values"]
    values["bogus_claim"] = 123
    with pytest.raises(ValueError, match="invalid category-target claim"):
        generate_evidence_ledger(catalogue, annotations)


def test_category_target_claim_requires_target_map(catalogue, annotations):
    values = annotations["evidence_records"][3]["claim"]["supported_values"]
    values.pop("exclusion_category_targets")
    with pytest.raises(ValueError, match="invalid category-target claim"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("mutation", ["extra", "missing"])
def test_category_target_claim_requires_exact_categories(
    catalogue, annotations, mutation
):
    targets = annotations["evidence_records"][3]["claim"]["supported_values"][
        "exclusion_category_targets"
    ]
    if mutation == "extra":
        targets["none"] = 1
    else:
        targets.pop("other-canonical-exclusion")
    with pytest.raises(ValueError, match="invalid category-target claim"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("count", [True, False, 0, -1])
def test_category_target_claim_requires_positive_genuine_counts(
    catalogue, annotations, count
):
    targets = annotations["evidence_records"][3]["claim"]["supported_values"][
        "exclusion_category_targets"
    ]
    targets["zobel-four-element"] = count
    with pytest.raises(ValueError, match="invalid category-target claim"):
        generate_evidence_ledger(catalogue, annotations)


def test_catalogue_target_claim_accepts_consistent_arithmetic(catalogue, annotations):
    values = annotations["evidence_records"][0]["claim"]["supported_values"]
    assert values == {
        "source_population": 148,
        "reported_members": 108,
        "reported_exclusions": 40,
    }
    generate_evidence_ledger(catalogue, annotations)


def test_catalogue_target_claim_rejects_inconsistent_arithmetic(
    catalogue, annotations
):
    annotations["evidence_records"][0]["claim"]["supported_values"][
        "reported_exclusions"
    ] = 41
    with pytest.raises(ValueError, match="inconsistent catalogue-target arithmetic"):
        generate_evidence_ledger(catalogue, annotations)


def test_unreferenced_catalogue_target_claim_rejects_inconsistent_arithmetic(
    catalogue, annotations
):
    annotations["evidence_records"][4]["claim"]["supported_values"][
        "reported_exclusions"
    ] = 41
    with pytest.raises(ValueError, match="inconsistent catalogue-target arithmetic"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("field", [
    "source_population", "reported_members", "reported_exclusions"
])
@pytest.mark.parametrize("value", [True, False])
def test_catalogue_target_claim_rejects_boolean_values(
    catalogue, annotations, field, value
):
    annotations["evidence_records"][0]["claim"]["supported_values"][field] = value
    with pytest.raises(ValueError, match="invalid catalogue-target claim"):
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
    annotations["computational_cross_checks"].append(record_factory())
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "field",
    [
        "subject_catalogue_ids",
        "reduction_target_network_numbers",
        "verified_evidence_record_ids",
    ],
)
def test_computational_scope_fields_must_be_present_together(
    catalogue, annotations, field
):
    record = _cross_check()
    record[field] = (
        [catalogue["records"][0]["catalogue_id"]]
        if field == "subject_catalogue_ids"
        else [20]
        if field == "reduction_target_network_numbers"
        else ["ms-2019-reported-148-to-108"]
    )
    annotations["computational_cross_checks"].append(record)
    with pytest.raises(ValueError, match="scope fields must be present together"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "missing_field",
    [
        "subject_catalogue_ids",
        "reduction_target_network_numbers",
        "verified_evidence_record_ids",
    ],
)
def test_two_computational_scope_fields_are_rejected(
    catalogue, annotations, missing_field
):
    record = _cross_check()
    record.update({
        "subject_catalogue_ids": [catalogue["records"][0]["catalogue_id"]],
        "reduction_target_network_numbers": [20],
        "verified_evidence_record_ids": ["ms-2019-reported-148-to-108"],
    })
    del record[missing_field]
    annotations["computational_cross_checks"].append(record)
    with pytest.raises(ValueError, match="scope fields must be present together"):
        generate_evidence_ledger(catalogue, annotations)


def test_computational_scope_lists_must_have_equal_lengths(
    catalogue, annotations
):
    record = _cross_check()
    record["subject_catalogue_ids"] = [catalogue["records"][0]["catalogue_id"]]
    record["reduction_target_network_numbers"] = [20, 25]
    record["verified_evidence_record_ids"] = ["ms-2019-reported-148-to-108"]
    annotations["computational_cross_checks"].append(record)
    with pytest.raises(ValueError, match="scope lists must have equal lengths"):
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


FINAL_EIGHT_SUBJECTS = {
    "lh148-4a925dd55dc8da19",
    "lh148-47ee32380ab1b406",
    "lh148-68430bbb448b9991",
    "lh148-7e24311a6fea4531",
    "lh148-debfbc02c5650a94",
    "lh148-f40bfca59082ff8d",
    "lh148-5278112fab778336",
    "lh148-f942f37eed38400a",
}
FINAL_EIGHT_AGGREGATE_ID = "ms-2019-final-eight-nongeneric-exclusion-group"
FINAL_EIGHT_COMPUTATION_ID = "rice-final-eight-o-bridge-report-reproduction"


def _evidence_of_type(annotations, claim_type):
    return [
        record
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"] == claim_type
    ]


def _subject_evidence(annotations, claim_type, subject):
    return next(
        record
        for record in _evidence_of_type(annotations, claim_type)
        if record["claim"].get("subject_catalogue_ids") == [subject]
    )


def _final_eight_computation(annotations):
    return next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == FINAL_EIGHT_COMPUTATION_ID
    )


def _remove_final_eight_explicit_records(annotations):
    annotations["records"] = [
        row
        for row in annotations["records"]
        if row["catalogue_id"] not in FINAL_EIGHT_SUBJECTS
    ]


def _populate_final_eight_explicit_records(annotations):
    _remove_final_eight_explicit_records(annotations)
    pairs = _evidence_of_type(annotations, "y-delta-partner-match")
    for subject in sorted(FINAL_EIGHT_SUBJECTS):
        graph = _subject_evidence(annotations, "basic-graph-match", subject)
        coefficient = _subject_evidence(
            annotations, "forced-immittance-coefficient", subject
        )
        route = _subject_evidence(
            annotations, "conditional-simpler-realisation-route", subject
        )
        pair = next(
            record
            for record in pairs
            if subject in record["claim"]["subject_catalogue_ids"]
        )
        annotations["records"].append({
            "catalogue_id": subject,
            "comparison_status": "derived-nongeneric-simplification-match",
            "proposed_disposition": "exclude",
            "exclusion_category": "other-canonical-exclusion",
            "exclusion_reason": (
                "Fixture aggregate nongeneric exclusion with independently "
                "checked subject-bound facts."
            ),
            "evidence_basis": [
                "aggregate-historical-nongeneric-group-plus-subject-bound-rice-facts"
            ],
            "evidence_record_ids": [
                FINAL_EIGHT_AGGREGATE_ID,
                graph["evidence_id"],
                pair["evidence_id"],
                coefficient["evidence_id"],
                route["evidence_id"],
            ],
            "previous_workspace_record_ids": [],
            "computational_cross_check_ids": [FINAL_EIGHT_COMPUTATION_ID],
            "historical_identifiers": [],
            "basic_graph_assignment": None,
            "confidence": "high",
            "notes": ["Complete-group application fixture."],
            "open_questions": ["Test fixture only."],
        })


def test_final_eight_structured_evidence_is_complete_and_applied(
    catalogue, annotations
):
    ledger = generate_evidence_ledger(catalogue, annotations)
    records = {row["catalogue_id"]: row for row in ledger["records"]}
    assert ledger["format_version"] == 6
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 25,
        "unresolved": 83,
    }
    assert len(_evidence_of_type(annotations, "aggregate-nongeneric-exclusion-group")) == 1
    assert len(_evidence_of_type(annotations, "y-delta-partner-match")) == 4
    assert len(_evidence_of_type(annotations, "forced-immittance-coefficient")) == 8
    assert len(_evidence_of_type(annotations, "conditional-simpler-realisation-route")) == 8
    assert {
        row["claim"]["subject_catalogue_ids"][0]
        for row in _evidence_of_type(annotations, "forced-immittance-coefficient")
    } == FINAL_EIGHT_SUBJECTS
    pairs = _evidence_of_type(annotations, "y-delta-partner-match")
    for subject in FINAL_EIGHT_SUBJECTS:
        row = records[subject]
        graph = _subject_evidence(annotations, "basic-graph-match", subject)
        coefficient = _subject_evidence(
            annotations, "forced-immittance-coefficient", subject
        )
        route = _subject_evidence(
            annotations, "conditional-simpler-realisation-route", subject
        )
        pair = next(
            item for item in pairs if subject in item["claim"]["subject_catalogue_ids"]
        )
        assert row["comparison_status"] == "derived-nongeneric-simplification-match"
        assert row["proposed_disposition"] == "exclude"
        assert row["exclusion_category"] == "other-canonical-exclusion"
        assert set(row["evidence_record_ids"]) == {
            FINAL_EIGHT_AGGREGATE_ID,
            graph["evidence_id"],
            pair["evidence_id"],
            coefficient["evidence_id"],
            route["evidence_id"],
        }
        assert row["computational_cross_check_ids"] == [
            FINAL_EIGHT_COMPUTATION_ID
        ]
    assert all(row["basic_graph_assignment"] is None for row in records.values())
    assert all(
        not records[subject]["historical_identifiers"]
        for subject in FINAL_EIGHT_SUBJECTS
    )


def test_complete_final_eight_explicit_group_can_apply(catalogue, annotations):
    _populate_final_eight_explicit_records(annotations)
    ledger = generate_evidence_ledger(catalogue, annotations)
    records = {row["catalogue_id"]: row for row in ledger["records"]}
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 25,
        "unresolved": 83,
    }
    assert all(
        records[subject]["comparison_status"]
        == "derived-nongeneric-simplification-match"
        for subject in FINAL_EIGHT_SUBJECTS
    )


def test_partial_final_eight_explicit_group_is_rejected(catalogue, annotations):
    _populate_final_eight_explicit_records(annotations)
    annotations["records"].pop()
    with pytest.raises(ValueError, match="must include the complete group"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_common_computation_has_exact_derived_fact_scope(annotations):
    computation = _final_eight_computation(annotations)
    derived_ids = {
        record["evidence_id"]
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"]
        in {
            "basic-graph-match",
            "y-delta-partner-match",
            "forced-immittance-coefficient",
            "conditional-simpler-realisation-route",
        }
        and set(record["claim"].get("subject_catalogue_ids", []))
        <= FINAL_EIGHT_SUBJECTS
        and record["claim"].get("subject_catalogue_ids")
    }
    assert set(computation["subject_catalogue_ids"]) == FINAL_EIGHT_SUBJECTS
    assert set(computation["conditional_target_network_numbers"]) == {21, 29, 36, 44}
    assert set(computation["verified_evidence_record_ids"]) == derived_ids
    assert FINAL_EIGHT_AGGREGATE_ID not in computation["verified_evidence_record_ids"]


@pytest.mark.parametrize(
    ("claim_type", "provenance"),
    [
        ("y-delta-partner-match", "rice-derived-structural-fact"),
        ("forced-immittance-coefficient", "rice-derived-structural-fact"),
        ("conditional-simpler-realisation-route", "rice-derived-structural-fact"),
    ],
)
def test_final_eight_positive_claims_require_exact_cross_checked_provenance(
    catalogue, annotations, claim_type, provenance
):
    _evidence_of_type(annotations, claim_type)[0]["provenance_level"] = provenance
    with pytest.raises(ValueError, match="cross-checked RICE-derived provenance"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_aggregate_must_remain_authoritative(catalogue, annotations):
    aggregate = _evidence_of_type(annotations, "aggregate-nongeneric-exclusion-group")[0]
    aggregate["verification_state"] = "cross-checked"
    with pytest.raises(ValueError, match="must be authoritative and source-verified"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_aggregate_requires_reviewed_publication_source(
    catalogue, annotations
):
    source = deepcopy(
        next(
            item
            for item in annotations["sources"]
            if item["source_id"] == "morelli-smith-2019"
        )
    )
    source["source_id"] = "fixture-other-authoritative-publication"
    annotations["sources"].append(source)
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    aggregate["source_id"] = source["source_id"]
    with pytest.raises(ValueError, match="must be authoritative and source-verified"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("citation", "publisher", "year"),
    [
        ("Unrelated publication.", "SIAM", 2019),
        (
            "A. Morelli and M. C. Smith, Passive Network Synthesis: An Approach "
            "to Classification, SIAM, 2019.",
            "Other publisher",
            2019,
        ),
        (
            "A. Morelli and M. C. Smith, Passive Network Synthesis: An Approach "
            "to Classification, SIAM, 2019.",
            "SIAM",
            2020,
        ),
        ("Unrelated publication.", "Other publisher", 2020),
    ],
)
def test_final_eight_publication_source_requires_reviewed_identity(
    catalogue, annotations, citation, publisher, year
):
    source = next(
        item
        for item in annotations["sources"]
        if item["source_id"] == "morelli-smith-2019"
    )
    source["citation"] = citation
    source["publication"] = {"publisher": publisher, "year": year}
    with pytest.raises(ValueError, match="reviewed final-eight identity"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("citation", "RICE graph-S five-element Zobel exclusion evidence report."),
        ("source_type", "rice-generated-artefact"),
    ],
)
def test_final_eight_rice_source_requires_reviewed_identity(
    catalogue, annotations, field, value
):
    source = next(
        item
        for item in annotations["sources"]
        if item["source_id"] == "rice-final-eight-o-bridge-report"
    )
    source[field] = value
    with pytest.raises(ValueError, match="reviewed final-eight identity"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("section", "7.1"),
        ("figure", "5.2"),
        ("appendix", "B"),
    ],
)
def test_final_eight_aggregate_requires_exact_reviewed_locator(
    catalogue, annotations, field, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    aggregate["locator"][field] = value
    with pytest.raises(ValueError, match="must be authoritative and source-verified"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_population", 8.0),
        ("supported_subject_counts_by_graph", {"O": 2.0, "O^d": 2, "V": 4}),
    ],
)
def test_final_eight_aggregate_counts_require_integers(
    catalogue, annotations, field, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    aggregate["claim"][field] = value
    with pytest.raises(ValueError, match="invalid aggregate nongeneric exclusion"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "targets",
    [
        [21.0, 29, 36, 44],
        [True, 29, 36, 44],
    ],
)
def test_final_eight_aggregate_targets_require_integers(
    catalogue, annotations, targets
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    aggregate["claim"]["supported_simpler_realisation_targets"] = targets
    with pytest.raises(ValueError, match="invalid aggregate nongeneric exclusion"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "coefficients",
    [
        [["A"], "C", "D", "F"],
        [1, "C", "D", "F"],
    ],
)
def test_final_eight_aggregate_coefficients_require_controlled_strings(
    catalogue, annotations, coefficients
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    aggregate["claim"]["supported_zero_coefficient_set"] = coefficients
    with pytest.raises(ValueError, match="invalid aggregate nongeneric exclusion"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_specialized_fact_requires_reviewed_report_source(
    catalogue, annotations
):
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    pair["source_id"] = "rice-five-element-zobel-graph-s-report"
    with pytest.raises(ValueError, match="must cite the reviewed final-eight RICE report"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_selected_graph_match_requires_reviewed_report_source(
    catalogue, annotations
):
    graph_match = _subject_evidence(
        annotations, "basic-graph-match", "lh148-4a925dd55dc8da19"
    )
    graph_match["source_id"] = "rice-five-element-zobel-graph-s-report"
    with pytest.raises(ValueError, match="requires exactly eight report-backed records"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("claim_type", "locator_updates"),
    [
        ("y-delta-partner-match", {"repository_path": "README.md"}),
        ("y-delta-partner-match", {"figure": "9.9"}),
        ("basic-graph-match", {"repository_path": "README.md"}),
        ("forced-immittance-coefficient", {"repository_path": "README.md"}),
        (
            "conditional-simpler-realisation-route",
            {"repository_path": "README.md"},
        ),
        ("basic-graph-match", {"section": "5.1"}),
    ],
)
def test_final_eight_structured_facts_require_exact_report_locators(
    catalogue, annotations, claim_type, locator_updates
):
    record = next(
        item
        for item in _evidence_of_type(annotations, claim_type)
        if item["source_id"] == "rice-final-eight-o-bridge-report"
    )
    record["locator"].update(locator_updates)
    with pytest.raises(ValueError, match="must use the reviewed final-eight report locator"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_route_locator_requires_its_validated_target(
    catalogue, annotations
):
    route = next(
        item
        for item in _evidence_of_type(
            annotations, "conditional-simpler-realisation-route"
        )
        if item["source_id"] == "rice-final-eight-o-bridge-report"
    )
    route["locator"]["network_number"] = 99
    with pytest.raises(ValueError, match="conditional-route locator does not match"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_structured_fact_locator_shapes_are_accepted(
    catalogue, annotations
):
    path = "docs/comparisons/ladenheim-final-eight-o-bridge-evidence-design.md"
    expected = {
        "basic-graph-match": {"repository_path": path},
        "y-delta-partner-match": {"figure": "5.1", "repository_path": path},
        "forced-immittance-coefficient": {"repository_path": path},
    }
    for claim_type, locator in expected.items():
        records = [
            item
            for item in _evidence_of_type(annotations, claim_type)
            if item["source_id"] == "rice-final-eight-o-bridge-report"
        ]
        assert records and all(item["locator"] == locator for item in records)
    routes = [
        item
        for item in _evidence_of_type(
            annotations, "conditional-simpler-realisation-route"
        )
        if item["source_id"] == "rice-final-eight-o-bridge-report"
    ]
    assert routes and all(
        item["locator"] == {
            "network_number": item["claim"]["nondegenerate_target_network_number"],
            "repository_path": path,
        }
        for item in routes
    )
    generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("cross_check_id", "fixture-other-final-eight-computation"),
        ("implementation", "Reproduction commands in README.md"),
        ("commit_sha", "not-a-commit"),
        ("commit_sha", "0123456789abcdef0123456789abcdef01234567"),
    ],
)
def test_final_eight_computation_requires_reviewed_report_identity(
    catalogue, annotations, field, value
):
    _remove_final_eight_explicit_records(annotations)
    computation = _final_eight_computation(annotations)
    computation[field] = value
    with pytest.raises(ValueError, match="reviewed final-eight fixed reproduction payload"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "field",
    ["input", "operation", "result", "limitations"],
)
def test_final_eight_computation_requires_complete_fixed_payload(
    catalogue, annotations, field
):
    computation = _final_eight_computation(annotations)
    computation[field] = f"Altered {field}."
    with pytest.raises(ValueError, match="reviewed final-eight fixed reproduction payload"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_report_graph_matches_are_an_exact_inventory(
    catalogue, annotations
):
    graph_match = deepcopy(
        _subject_evidence(
            annotations, "basic-graph-match", "lh148-4a925dd55dc8da19"
        )
    )
    graph_match["evidence_id"] = "fixture-orphan-final-eight-graph-match"
    graph_match["claim"]["match"].update(
        {
            "fixture_id": "morelli-smith-V-five-edge",
            "graph_label": "V",
        }
    )
    annotations["evidence_records"].append(graph_match)
    with pytest.raises(ValueError, match="requires exactly eight report-backed records"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("verification_state", "source-verified"),
        ("provenance_level", "rice-derived-network-equivalence-fact"),
    ],
)
def test_final_eight_selected_graph_matches_require_exact_provenance(
    catalogue, annotations, field, value
):
    graph_match = _subject_evidence(
        annotations, "basic-graph-match", "lh148-4a925dd55dc8da19"
    )
    graph_match[field] = value
    with pytest.raises(
        ValueError, match="one positive committed-relation graph match per subject"
    ):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "updates",
    [
        {"base_label": "V"},
        {"is_dual": False},
        {"base_label": "V", "is_dual": False},
    ],
)
def test_final_eight_graph_definition_requires_complete_reviewed_metadata(
    catalogue, annotations, updates
):
    definition = next(
        record
        for record in _evidence_of_type(annotations, "basic-graph-definition")
        if record["claim"]["definition"]["graph_label"] == "O^d"
    )
    definition["claim"]["definition"].update(updates)
    with pytest.raises(ValueError, match="complete reviewed authoritative definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_graph_definition_requires_reviewed_publication_source(
    catalogue, annotations
):
    source = deepcopy(
        next(
            item
            for item in annotations["sources"]
            if item["source_id"] == "morelli-smith-2019"
        )
    )
    source["source_id"] = "fixture-unrelated-graph-authority"
    annotations["sources"].append(source)
    definition = next(
        record
        for record in _evidence_of_type(annotations, "basic-graph-definition")
        if record["claim"]["definition"]["graph_label"] == "O^d"
    )
    definition["source_id"] = source["source_id"]
    with pytest.raises(ValueError, match="complete reviewed authoritative definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("printed_page", 126),
        ("pdf_page_index", 132),
        ("section", "5.1"),
    ],
)
def test_final_eight_graph_definition_requires_exact_reviewed_locator(
    catalogue, annotations, field, value
):
    definition = next(
        record
        for record in _evidence_of_type(annotations, "basic-graph-definition")
        if record["claim"]["definition"]["graph_label"] == "O^d"
    )
    definition["locator"][field] = value
    with pytest.raises(ValueError, match="complete reviewed authoritative definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("route_relation", "realizability-set-containment", "invalid conditional"),
        ("condition_expression", "delta", "invalid conditional"),
        ("nondegenerate_condition", "delta >= 0", "invalid conditional"),
        ("degenerate_condition", "delta <= 0", "invalid conditional"),
    ],
)
def test_conditional_routes_reject_unreviewed_relations_or_conditions(
    catalogue, annotations, field, value, message
):
    route = _evidence_of_type(annotations, "conditional-simpler-realisation-route")[0]
    route["claim"][field] = value
    with pytest.raises(ValueError, match=message):
        generate_evidence_ledger(catalogue, annotations)


def test_projective_dimension_bound_cannot_replace_source_bound(catalogue, annotations):
    coefficient = _evidence_of_type(annotations, "forced-immittance-coefficient")[0]
    coefficient["claim"]["nongeneric_dimension_bound"] = 4
    with pytest.raises(ValueError, match="invalid forced coefficient claim"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("forced_value", False),
        ("nongeneric_dimension_bound", 5.0),
    ],
)
def test_forced_coefficient_numeric_fields_require_integers(
    catalogue, annotations, field, value
):
    coefficient = _evidence_of_type(annotations, "forced-immittance-coefficient")[0]
    coefficient["claim"][field] = value
    with pytest.raises(ValueError, match="invalid forced coefficient claim"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("coefficient", [["A"], 1])
def test_forced_coefficient_requires_controlled_string(
    catalogue, annotations, coefficient
):
    record = _evidence_of_type(annotations, "forced-immittance-coefficient")[0]
    record["claim"]["coefficient"] = coefficient
    with pytest.raises(ValueError, match="invalid forced coefficient claim"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "degenerate_class",
    [["two-element-series-R-X"], 1],
)
def test_conditional_route_requires_controlled_degenerate_class(
    catalogue, annotations, degenerate_class
):
    route = _evidence_of_type(
        annotations, "conditional-simpler-realisation-route"
    )[0]
    route["claim"]["degenerate_realisation_class"] = degenerate_class
    with pytest.raises(ValueError, match="invalid conditional simpler-realisation"):
        generate_evidence_ledger(catalogue, annotations)


def test_y_delta_pairs_must_be_complete_and_disjoint(catalogue, annotations):
    pairs = _evidence_of_type(annotations, "y-delta-partner-match")
    pairs[1]["claim"]["subject_catalogue_ids"] = list(
        pairs[0]["claim"]["subject_catalogue_ids"]
    )
    pairs[1]["claim"]["subject_fixture_ids"] = list(
        pairs[0]["claim"]["subject_fixture_ids"]
    )
    with pytest.raises(ValueError, match="pairs must be disjoint"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_specialized_facts_require_one_aggregate(catalogue, annotations):
    _remove_final_eight_explicit_records(annotations)
    aggregate = _evidence_of_type(
        annotations, "aggregate-nongeneric-exclusion-group"
    )[0]
    annotations["evidence_records"].remove(aggregate)
    with pytest.raises(ValueError, match="requires exactly one aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_format_version_four_requires_complete_final_eight_inventory(
    catalogue, annotations
):
    _remove_final_eight_explicit_records(annotations)
    final_eight_claim_types = {
        "aggregate-nongeneric-exclusion-group",
        "y-delta-partner-match",
        "forced-immittance-coefficient",
        "conditional-simpler-realisation-route",
    }
    annotations["evidence_records"] = [
        record
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"] not in final_eight_claim_types
    ]
    annotations["computational_cross_checks"] = [
        record
        for record in annotations["computational_cross_checks"]
        if "conditional_target_network_numbers" not in record
    ]
    with pytest.raises(ValueError, match="final-eight inventory requires exactly one aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_format_version_four_requires_exact_specialized_inventory(
    catalogue, annotations
):
    _remove_final_eight_explicit_records(annotations)
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    annotations["evidence_records"].remove(pair)
    _final_eight_computation(annotations)["verified_evidence_record_ids"].remove(
        pair["evidence_id"]
    )
    with pytest.raises(ValueError, match="inventory requires four Y-delta pairs"):
        generate_evidence_ledger(catalogue, annotations)


def test_format_version_four_accepts_complete_final_eight_inventory(
    catalogue, annotations
):
    generated = generate_evidence_ledger(catalogue, annotations)
    assert generated["format_version"] == 6


def test_final_eight_specialized_facts_cannot_escape_computation_scope(
    catalogue, annotations
):
    source = _evidence_of_type(annotations, "forced-immittance-coefficient")[0]
    orphan = deepcopy(source)
    orphan["evidence_id"] = "fixture-orphan-final-eight-coefficient"
    annotations["evidence_records"].append(orphan)
    with pytest.raises(ValueError, match="must belong to the aggregate computation"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_requires_one_conditional_computation(catalogue, annotations):
    duplicate = deepcopy(_final_eight_computation(annotations))
    duplicate["cross_check_id"] = "fixture-second-final-eight-computation"
    annotations["computational_cross_checks"].append(duplicate)
    with pytest.raises(ValueError, match="exactly one conditional computation"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_requires_one_aggregate(catalogue, annotations):
    duplicate = deepcopy(
        _evidence_of_type(annotations, "aggregate-nongeneric-exclusion-group")[0]
    )
    duplicate["evidence_id"] = "fixture-second-final-eight-aggregate"
    annotations["evidence_records"].append(duplicate)
    with pytest.raises(ValueError, match="requires exactly one aggregate"):
        generate_evidence_ledger(catalogue, annotations)


def test_y_delta_pair_fixture_order_is_bound_to_subject_order(catalogue, annotations):
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    pair["claim"]["subject_fixture_ids"].reverse()
    with pytest.raises(ValueError, match="invalid Y-delta partner claim"):
        generate_evidence_ledger(catalogue, annotations)


def test_reviewed_fixtures_reject_consistent_capacitive_inductive_subject_swap(
    catalogue, annotations
):
    _remove_final_eight_explicit_records(annotations)
    subject_swap = {
        "lh148-4a925dd55dc8da19": "lh148-68430bbb448b9991",
        "lh148-68430bbb448b9991": "lh148-4a925dd55dc8da19",
        "lh148-47ee32380ab1b406": "lh148-7e24311a6fea4531",
        "lh148-7e24311a6fea4531": "lh148-47ee32380ab1b406",
    }
    for record in annotations["evidence_records"]:
        claim = record["claim"]
        if claim["claim_type"] in {
            "basic-graph-match",
            "y-delta-partner-match",
            "forced-immittance-coefficient",
            "conditional-simpler-realisation-route",
        }:
            claim["subject_catalogue_ids"] = [
                subject_swap.get(subject, subject)
                for subject in claim.get("subject_catalogue_ids", [])
            ]
    computation = _final_eight_computation(annotations)
    computation["subject_catalogue_ids"] = [
        subject_swap.get(subject, subject)
        for subject in computation["subject_catalogue_ids"]
    ]
    with pytest.raises(ValueError, match="reviewed catalogue subject"):
        generate_evidence_ledger(catalogue, annotations)


def test_y_delta_pair_rejects_internally_consistent_arbitrary_fixtures(
    catalogue, annotations
):
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    arbitrary_nonbridge = "arbitrary-nonbridge-fixture"
    arbitrary_bridge = "arbitrary-bridge-fixture"
    pair["claim"]["subject_fixture_ids"] = [
        arbitrary_nonbridge,
        arbitrary_bridge,
    ]
    for subject in pair["claim"]["subject_catalogue_ids"]:
        route = _subject_evidence(
            annotations, "conditional-simpler-realisation-route", subject
        )
        route["claim"]["condition_parameterization_fixture_id"] = (
            arbitrary_nonbridge
        )
    with pytest.raises(ValueError, match="invalid Y-delta partner claim"):
        generate_evidence_ledger(catalogue, annotations)


def test_y_delta_pair_requires_the_reviewed_transformation_figure(
    catalogue, annotations
):
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    pair["claim"]["transformation_figure"] = "Figure 99.1"
    with pytest.raises(ValueError, match="invalid Y-delta partner claim"):
        generate_evidence_ledger(catalogue, annotations)


def test_missing_y_delta_pair_is_rejected(catalogue, annotations):
    _remove_final_eight_explicit_records(annotations)
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    annotations["evidence_records"].remove(pair)
    computation = _final_eight_computation(annotations)
    computation["verified_evidence_record_ids"].remove(pair["evidence_id"])
    with pytest.raises(ValueError, match="four Y-delta pairs"):
        generate_evidence_ledger(catalogue, annotations)


def test_y_delta_pair_members_require_the_same_forced_coefficient(
    catalogue, annotations
):
    pair = _evidence_of_type(annotations, "y-delta-partner-match")[0]
    subject = pair["claim"]["subject_catalogue_ids"][1]
    subject_claim = _subject_evidence(
        annotations, "forced-immittance-coefficient", subject
    )["claim"]
    other_claim = _subject_evidence(
        annotations,
        "forced-immittance-coefficient",
        "lh148-5278112fab778336",
    )["claim"]
    subject_claim["coefficient"], other_claim["coefficient"] = (
        other_claim["coefficient"],
        subject_claim["coefficient"],
    )
    with pytest.raises(ValueError, match="same forced coefficient"):
        generate_evidence_ledger(catalogue, annotations)


def test_bridge_route_requires_its_reviewed_partner(catalogue, annotations):
    bridge_subject = "lh148-47ee32380ab1b406"
    route = _subject_evidence(
        annotations, "conditional-simpler-realisation-route", bridge_subject
    )
    route["claim"].pop("y_delta_partner_match_evidence_id")
    with pytest.raises(ValueError, match="bridge conditional route requires"):
        generate_evidence_ledger(catalogue, annotations)


def test_pair_routes_require_the_same_condition_fixture(catalogue, annotations):
    bridge_subject = "lh148-47ee32380ab1b406"
    route = _subject_evidence(
        annotations, "conditional-simpler-realisation-route", bridge_subject
    )
    route["claim"]["condition_parameterization_fixture_id"] = "wrong-fixture"
    with pytest.raises(ValueError, match="one reviewed condition fixture"):
        generate_evidence_ledger(catalogue, annotations)


def test_conditional_targets_require_exact_derived_multiplicity(catalogue, annotations):
    route = _subject_evidence(
        annotations,
        "conditional-simpler-realisation-route",
        "lh148-47ee32380ab1b406",
    )
    route["claim"]["nondegenerate_target_network_number"] = 29
    route["claim"]["nondegenerate_target_fixture_id"] = (
        "morelli-smith-canonical-network-29"
    )
    route["locator"]["network_number"] = 29
    with pytest.raises(ValueError, match="one reviewed condition fixture and target"):
        generate_evidence_ledger(catalogue, annotations)


def test_conditional_target_number_requires_its_reviewed_fixture(
    catalogue, annotations
):
    route = _evidence_of_type(
        annotations, "conditional-simpler-realisation-route"
    )[0]
    route["claim"]["nondegenerate_target_fixture_id"] = (
        "morelli-smith-canonical-network-29"
    )
    with pytest.raises(ValueError, match="invalid conditional simpler-realisation"):
        generate_evidence_ledger(catalogue, annotations)


def test_common_computation_must_verify_every_derived_fact(catalogue, annotations):
    computation = _final_eight_computation(annotations)
    computation["verified_evidence_record_ids"].pop()
    with pytest.raises(ValueError, match="must belong to the aggregate computation"):
        generate_evidence_ledger(catalogue, annotations)


def test_nongeneric_aggregate_cannot_support_a_rule(catalogue, annotations):
    annotations["rules"][0]["evidence_record_ids"].append(FINAL_EIGHT_AGGREGATE_ID)
    with pytest.raises(ValueError, match="cannot support a rule"):
        generate_evidence_ledger(catalogue, annotations)


def test_nongeneric_aggregate_cannot_apply_through_another_status(
    catalogue, annotations
):
    _remove_final_eight_explicit_records(annotations)
    subject = next(iter(FINAL_EIGHT_SUBJECTS))
    row = _unresolved_annotation(subject)
    row["evidence_record_ids"] = [FINAL_EIGHT_AGGREGATE_ID]
    annotations["records"].append(row)
    with pytest.raises(ValueError, match="only the explicit nongeneric simplification status"):
        generate_evidence_ledger(catalogue, annotations)


def test_nongeneric_status_rejects_reduction_target_match(catalogue, annotations):
    _populate_final_eight_explicit_records(annotations)
    subject = sorted(FINAL_EIGHT_SUBJECTS)[0]
    route = _subject_evidence(
        annotations, "conditional-simpler-realisation-route", subject
    )["claim"]
    evidence_id = "fixture-invalid-reduction-target-match"
    annotations["evidence_records"].append({
        "evidence_id": evidence_id,
        "source_id": "rice-final-eight-o-bridge-report",
        "provenance_level": "rice-derived-network-equivalence-fact",
        "verification_state": "cross-checked",
        "locator": {
            "repository_path": (
                "docs/comparisons/"
                "ladenheim-final-eight-o-bridge-evidence-design.md"
            )
        },
        "paraphrase": "Invalidly treats a conditional destination as equivalence.",
        "claim": {
            "claim_type": "reduction-target-match",
            "subject_catalogue_ids": [subject],
            "target_network_number": route[
                "nondegenerate_target_network_number"
            ],
        },
    })
    row = next(item for item in annotations["records"] if item["catalogue_id"] == subject)
    row["evidence_record_ids"].append(evidence_id)
    with pytest.raises(ValueError, match="cannot use a reduction-target-match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("target", [29, 99])
def test_final_eight_subject_cannot_have_a_canonical_historical_identity(
    catalogue, annotations, target
):
    _populate_final_eight_explicit_records(annotations)
    subject = "lh148-4a925dd55dc8da19"
    identifier_evidence = _historical_identifier_evidence(subject, value=target)
    annotations["evidence_records"].append(identifier_evidence)
    row = next(item for item in annotations["records"] if item["catalogue_id"] == subject)
    row["historical_identifiers"] = [{
        "scheme": "morelli-smith-canonical-network",
        "value": target,
        "verification_state": "source-verified",
        "evidence_record_ids": [identifier_evidence["evidence_id"]],
    }]
    with pytest.raises(ValueError, match="cannot use a canonical network.*historical identity"):
        generate_evidence_ledger(catalogue, annotations)


def test_final_eight_status_requires_null_graph_assignment(catalogue, annotations):
    _populate_final_eight_explicit_records(annotations)
    subject = "lh148-4a925dd55dc8da19"
    graph_match = _subject_evidence(annotations, "basic-graph-match", subject)
    definition = next(
        record
        for record in _evidence_of_type(annotations, "basic-graph-definition")
        if record["claim"]["definition"]["graph_label"] == "O"
    )
    row = next(item for item in annotations["records"] if item["catalogue_id"] == subject)
    row["basic_graph_assignment"] = {
        **definition["claim"]["definition"],
        "structural_relation": (
            "colour-preserving-port-augmented-cycle-matroid-v1"
        ),
        "verification_state": "cross-checked",
        "evidence_record_ids": [
            definition["evidence_id"],
            graph_match["evidence_id"],
        ],
    }
    with pytest.raises(ValueError, match="requires no production basic graph assignment"):
        generate_evidence_ledger(catalogue, annotations)


def test_new_status_is_invalid_for_rules_and_retention(catalogue, annotations):
    _remove_final_eight_explicit_records(annotations)
    annotations["rules"][0]["comparison_status"] = (
        "derived-nongeneric-simplification-match"
    )
    annotations["rules"][0]["evidence_basis"] = [
        "aggregate-historical-nongeneric-group-plus-subject-bound-rice-facts"
    ]
    with pytest.raises(ValueError, match="valid only for explicit annotation records"):
        generate_evidence_ledger(catalogue, annotations)

    annotations["rules"][0]["comparison_status"] = "derived-unique-match"
    annotations["rules"][0]["evidence_basis"] = [
        "aggregate-historical-category-plus-logically-unique-rice-match"
    ]
    subject = next(iter(FINAL_EIGHT_SUBJECTS))
    row = _unresolved_annotation(subject)
    row.update({
        "comparison_status": "derived-nongeneric-simplification-match",
        "proposed_disposition": "retain",
        "exclusion_category": "other-canonical-exclusion",
        "exclusion_reason": "Invalid fixture retention.",
        "confidence": "high",
        "evidence_basis": [
            "aggregate-historical-nongeneric-group-plus-subject-bound-rice-facts"
        ],
    })
    annotations["records"].append(row)
    with pytest.raises(ValueError, match="cannot assert retention"):
        generate_evidence_ledger(catalogue, annotations)


LOW_ORDER_AGGREGATE_ID = "rice-low-order-canonical-network-group"
LOW_ORDER_COMPUTATION_ID = "rice-low-order-canonical-report-reproduction"


def _low_order_definitions(annotations):
    return [
        record
        for record in _evidence_of_type(annotations, "canonical-network-definition")
        if record["claim"]["canonical_network_number"]
        in REVIEWED_LOW_ORDER_CANONICAL_NETWORKS
    ]


def _low_order_matches(annotations):
    return [
        record
        for record in _evidence_of_type(annotations, "canonical-network-match")
        if record["claim"]["canonical_network_number"]
        in REVIEWED_LOW_ORDER_CANONICAL_NETWORKS
    ]


def _low_order_computation(annotations):
    return next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == LOW_ORDER_COMPUTATION_ID
    )


def _four_element_definitions(annotations):
    return [
        record
        for record in _evidence_of_type(annotations, "canonical-network-definition")
        if record["claim"]["canonical_network_number"]
        in REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS
    ]


def _four_element_matches(annotations):
    return [
        record
        for record in _evidence_of_type(annotations, "canonical-network-match")
        if record["claim"]["canonical_network_number"]
        in REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS
    ]


def _four_element_computation(annotations):
    return next(
        record
        for record in annotations["computational_cross_checks"]
        if record["cross_check_id"] == FOUR_ELEMENT_COMPUTATION_ID
    )


def _four_element_aggregate(annotations):
    return next(
        record
        for record in _evidence_of_type(
            annotations, "aggregate-canonical-network-group"
        )
        if record["evidence_id"] == FOUR_ELEMENT_AGGREGATE_ID
    )


def _populate_low_order_identity_records(annotations):
    aggregate = next(
        record
        for record in _evidence_of_type(
            annotations, "aggregate-canonical-network-group"
        )
        if record["evidence_id"] == LOW_ORDER_AGGREGATE_ID
    )
    definitions = {
        record["claim"]["canonical_network_number"]: record
        for record in _low_order_definitions(annotations)
    }
    matches = {
        record["claim"]["canonical_network_number"]: record
        for record in _low_order_matches(annotations)
    }
    expected_subjects = {
        record["claim"]["subject_catalogue_ids"][0] for record in matches.values()
    }
    existing_subjects = {
        record["catalogue_id"]
        for record in annotations["records"]
        if record["comparison_status"] == "derived-canonical-identity-match"
    }
    if existing_subjects == expected_subjects:
        return
    for number in aggregate["claim"]["canonical_network_numbers"]:
        definition = definitions[number]
        match = matches[number]
        subject = match["claim"]["subject_catalogue_ids"][0]
        annotations["records"].append(
            {
            "catalogue_id": subject,
            "comparison_status": "derived-canonical-identity-match",
            "proposed_disposition": "retain",
            "exclusion_category": "none",
            "exclusion_reason": None,
            "evidence_basis": [
                "authoritative-canonical-diagram-plus-subject-bound-rice-match"
            ],
            "evidence_record_ids": [
                LOW_ORDER_AGGREGATE_ID,
                definition["evidence_id"],
                match["evidence_id"],
            ],
            "previous_workspace_record_ids": [],
            "computational_cross_check_ids": [LOW_ORDER_COMPUTATION_ID],
                "historical_identifiers": [
                    {
                "scheme": "morelli-smith-canonical-network",
                "value": number,
                "verification_state": "cross-checked",
                "evidence_record_ids": [
                    definition["evidence_id"],
                    match["evidence_id"],
                ],
                    }
                ],
            "basic_graph_assignment": None,
            "confidence": "high",
            "notes": ["Complete low-order identity application fixture."],
            "open_questions": [],
            }
        )


def _populate_four_element_identity_records(annotations):
    definitions = {
        record["claim"]["canonical_network_number"]: record
        for record in _four_element_definitions(annotations)
    }
    matches = {
        record["claim"]["canonical_network_number"]: record
        for record in _four_element_matches(annotations)
    }
    for number in _four_element_aggregate(annotations)["claim"][
        "canonical_network_numbers"
    ]:
        definition = definitions[number]
        match = matches[number]
        subject = match["claim"]["subject_catalogue_ids"][0]
        row = {
            "catalogue_id": subject,
            "comparison_status": "derived-canonical-identity-match",
            "proposed_disposition": "retain",
            "exclusion_category": "none",
            "exclusion_reason": None,
            "evidence_basis": [
                "authoritative-canonical-diagram-plus-subject-bound-rice-match"
            ],
            "evidence_record_ids": [
                FOUR_ELEMENT_AGGREGATE_ID,
                definition["evidence_id"],
                match["evidence_id"],
            ],
            "previous_workspace_record_ids": [],
            "computational_cross_check_ids": [FOUR_ELEMENT_COMPUTATION_ID],
            "historical_identifiers": [
                {
                    "scheme": "morelli-smith-canonical-network",
                    "value": number,
                    "verification_state": "cross-checked",
                    "evidence_record_ids": [
                        definition["evidence_id"],
                        match["evidence_id"],
                    ],
                }
            ],
            "basic_graph_assignment": None,
            "confidence": "high",
            "notes": ["Complete four-element identity application fixture."],
            "open_questions": [],
        }
        annotations["records"].append(row)


def test_low_order_contract_group_is_complete_and_applied(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    definitions = _low_order_definitions(annotations)
    matches = _low_order_matches(annotations)
    assert len(definitions) == 25
    assert len(matches) == 25
    assert len({row["claim"]["canonical_network_number"] for row in definitions}) == 25
    assert len({row["claim"]["subject_catalogue_ids"][0] for row in matches}) == 25
    assert ledger["format_version"] == 6
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 25,
        "unresolved": 83,
    }
    assert all(row["basic_graph_assignment"] is None for row in ledger["records"])
    retained = [
        row for row in ledger["records"]
        if row["comparison_status"] == "derived-canonical-identity-match"
    ]
    assert len(retained) == 25
    assert {
        (row["catalogue_id"], row["historical_identifiers"][0]["value"])
        for row in retained
    } == {
        (payload[0], number)
        for number, payload in REVIEWED_LOW_ORDER_CANONICAL_NETWORKS.items()
    }


@pytest.mark.parametrize(
    "claim_type",
    [
    "canonical-network-definition",
    "canonical-network-match",
    ],
)
def test_low_order_group_rejects_a_missing_definition_or_match(
    catalogue, annotations, claim_type
):
    record = (
        _low_order_definitions(annotations)[-1]
        if claim_type == "canonical-network-definition"
        else _low_order_matches(annotations)[-1]
    )
    annotations["evidence_records"].remove(record)
    computation = _low_order_computation(annotations)
    scope_field = (
        "canonical_definition_evidence_record_ids"
        if claim_type == "canonical-network-definition"
        else "verified_evidence_record_ids"
    )
    computation[scope_field].remove(record["evidence_id"])
    with pytest.raises(
        ValueError,
        match="unknown evidence_record_ids|low-order canonical .* inventory is incomplete",
    ):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_group_rejects_duplicate_canonical_number(catalogue, annotations):
    definitions = _low_order_definitions(annotations)
    definitions[1]["claim"]["canonical_network_number"] = definitions[0]["claim"][
        "canonical_network_number"
    ]
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_group_rejects_duplicate_or_wrong_subject(catalogue, annotations):
    matches = _low_order_matches(annotations)
    matches[1]["claim"]["subject_catalogue_ids"] = matches[0]["claim"][
        "subject_catalogue_ids"
    ].copy()
    with pytest.raises(ValueError, match="invalid canonical-network match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("number", [[1], {"number": 1}, True])
def test_canonical_network_match_rejects_noninteger_numbers(
    catalogue, annotations, number
):
    _low_order_matches(annotations)[0]["claim"]["canonical_network_number"] = number
    with pytest.raises(ValueError, match="invalid canonical-network match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 1.0])
def test_canonical_definition_requires_integer_element_count(
    catalogue, annotations, value
):
    _low_order_definitions(annotations)[0]["claim"]["element_count"] = value
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("field", ["r", "l", "c"])
@pytest.mark.parametrize("replacement", [True, "equal-float"])
def test_canonical_definition_requires_integer_component_inventory(
    catalogue, annotations, field, replacement
):
    definition = _low_order_definitions(annotations)[0]["claim"]
    value = definition["component_inventory"][field]
    definition["component_inventory"][field] = (
        float(value) if replacement == "equal-float" else replacement
    )
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("locator", "field", "value"),
    [
        ("diagram_locator", "network_number", True),
        ("diagram_locator", "network_number", 1.0),
        ("figure_locator", "printed_page", 50.0),
        ("class_table_locator", "pdf_page_index", 64.0),
    ],
)
def test_canonical_definition_requires_integer_nested_locators(
    catalogue, annotations, locator, field, value
):
    definition = _low_order_definitions(annotations)[0]["claim"]
    definition[locator][field] = value
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 1.0])
def test_canonical_aggregate_requires_integer_number_scope(
    catalogue, annotations, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-canonical-network-group"
    )[0]["claim"]
    aggregate["canonical_network_numbers"][0] = value
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [("source_orbit_count", True), ("total_networks", 25.0)],
)
def test_canonical_aggregate_requires_integer_counts(
    catalogue, annotations, field, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-canonical-network-group"
    )[0]["claim"]
    aggregate[field] = value
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 3.0])
def test_canonical_aggregate_requires_integer_element_order_counts(
    catalogue, annotations, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-canonical-network-group"
    )[0]["claim"]
    aggregate["counts_by_element_order"]["1"] = value
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("locator", "field", "value"),
    [
        ("count_table_locator", "printed_page", 49.0),
        ("figure_locator", "pdf_page_index", 56.0),
    ],
)
def test_canonical_aggregate_requires_integer_locators(
    catalogue, annotations, locator, field, value
):
    aggregate = _evidence_of_type(
        annotations, "aggregate-canonical-network-group"
    )[0]["claim"]
    aggregate[locator][field] = value
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 1.0])
def test_canonical_computation_requires_integer_number_scope(
    catalogue, annotations, value
):
    _low_order_computation(annotations)["canonical_network_numbers"][0] = value
    with pytest.raises(ValueError, match="invalid canonical-number scope"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("mutation", ["diagram-locator", "report-path", "relation"])
def test_low_order_group_rejects_mutated_binding(catalogue, annotations, mutation):
    if mutation == "diagram-locator":
        _low_order_definitions(annotations)[0]["locator"]["printed_page"] = 999
        expected = "exact reviewed publication payload, provenance, and locators"
    elif mutation == "report-path":
        _low_order_matches(annotations)[0]["locator"]["repository_path"] = "README.md"
        expected = (
            "reviewed group, immutable catalogue row, definition, or report provenance"
        )
    else:
        _low_order_matches(annotations)[0]["claim"]["structural_relation"] = "wrong"
        expected = "invalid canonical-network match"
    with pytest.raises(ValueError, match=expected):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_group_rejects_component_inventory_disagreement(
    catalogue, annotations
):
    _low_order_definitions(annotations)[0]["claim"]["component_inventory"] = {
        "r": 1, "l": 0, "c": 0,
    }
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_group_rejects_an_excluded_subject(catalogue, annotations):
    excluded = next(
        row["catalogue_id"]
        for row in generate_evidence_ledger(catalogue, annotations)["records"]
        if row["proposed_disposition"] == "exclude"
    )
    _low_order_matches(annotations)[0]["claim"]["subject_catalogue_ids"] = [excluded]
    with pytest.raises(ValueError, match="invalid canonical-network match"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("scope_field", [
    "canonical_definition_evidence_record_ids",
    "verified_evidence_record_ids",
])
def test_low_order_computation_requires_complete_evidence_scope(
    catalogue, annotations, scope_field
):
    _low_order_computation(annotations)[scope_field].pop()
    with pytest.raises(ValueError, match="exact canonical definition and match scope"):
        generate_evidence_ledger(catalogue, annotations)


def test_complete_low_order_identity_application_can_pass(catalogue, annotations):
    _populate_low_order_identity_records(annotations)
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 25,
        "unresolved": 83,
    }


def test_low_order_computation_result_is_durable_and_pinned(annotations):
    computation = _low_order_computation(annotations)
    result = computation["result"].lower()
    assert all(
        word not in result for word in ("unresolved", "retained", "excluded")
    )
    assert computation["commit_sha"] == (
        "4411b1fa441241f47e3d2e39a4e96ef5447199e9"
    )


@pytest.mark.parametrize("reviewed_kind", ["aggregate", "definition", "match"])
def test_basic_graph_assignment_low_order_evidence_triggers_consumption(
    catalogue, annotations, reviewed_kind
):
    row = annotations["records"][0]
    evidence = {
        record["evidence_id"]: record for record in annotations["evidence_records"]
    }
    definition = next(
        evidence[evidence_id]
        for evidence_id in row["evidence_record_ids"]
        if evidence[evidence_id]["claim"]["claim_type"] == "basic-graph-definition"
    )
    graph_match = next(
        evidence[evidence_id]
        for evidence_id in row["evidence_record_ids"]
        if evidence[evidence_id]["claim"]["claim_type"] == "basic-graph-match"
    )
    reviewed_id = {
        "aggregate": LOW_ORDER_AGGREGATE_ID,
        "definition": _low_order_definitions(annotations)[0]["evidence_id"],
        "match": _low_order_matches(annotations)[0]["evidence_id"],
    }[reviewed_kind]
    row["basic_graph_assignment"] = {
        **definition["claim"]["definition"],
        "structural_relation": graph_match["claim"]["match"][
            "structural_relation"
        ],
        "verification_state": "cross-checked",
        "evidence_record_ids": [
            definition["evidence_id"],
            graph_match["evidence_id"],
            reviewed_id,
        ],
    }
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def _append_indirect_low_order_computation(annotations, evidence_id):
    computation = _cross_check()
    computation.update({
        "cross_check_id": "fixture-indirect-low-order-computation",
        "subject_catalogue_ids": [annotations["records"][0]["catalogue_id"]],
        "reduction_target_network_numbers": [1],
        "verified_evidence_record_ids": [evidence_id],
    })
    annotations["computational_cross_checks"].append(computation)
    return computation["cross_check_id"]


@pytest.mark.parametrize("reviewed_kind", ["aggregate", "definition", "match"])
def test_rule_computation_scope_low_order_evidence_triggers_consumption(
    catalogue, annotations, reviewed_kind
):
    reviewed_id = {
        "aggregate": LOW_ORDER_AGGREGATE_ID,
        "definition": _low_order_definitions(annotations)[0]["evidence_id"],
        "match": _low_order_matches(annotations)[0]["evidence_id"],
    }[reviewed_kind]
    computation_id = _append_indirect_low_order_computation(
        annotations, reviewed_id
    )
    annotations["rules"][0]["computational_cross_check_ids"].append(
        computation_id
    )
    with pytest.raises(ValueError, match="explicit-record only"):
        generate_evidence_ledger(catalogue, annotations)


def test_explicit_computation_scope_low_order_evidence_triggers_consumption(
    catalogue, annotations
):
    reviewed_id = _low_order_definitions(annotations)[0]["evidence_id"]
    computation_id = _append_indirect_low_order_computation(
        annotations, reviewed_id
    )
    annotations["records"][0]["computational_cross_check_ids"].append(
        computation_id
    )
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_unrelated_computation_scope_does_not_trigger_low_order_consumption(
    catalogue, annotations
):
    computation_id = _append_indirect_low_order_computation(
        annotations, "ms-2019-reported-148-to-108"
    )
    computation = next(
        item
        for item in annotations["computational_cross_checks"]
        if item["cross_check_id"] == computation_id
    )
    computation["result"] = (
        f"Editorial mention only: {LOW_ORDER_AGGREGATE_ID} is not evidence scope."
    )
    annotations["rules"][0]["computational_cross_check_ids"].append(
        computation_id
    )
    generate_evidence_ledger(catalogue, annotations)


def _add_low_order_bypass_record(
    annotations,
    *,
    status="unresolved",
    identifier_value=1,
    identifier_evidence=True,
    include_identifier=True,
    identifier_evidence_ids=None,
    direct_evidence_ids=(),
    identifier_scheme="morelli-smith-canonical-network",
    evidence_basis=None,
):
    match = next(
        record
        for record in _low_order_matches(annotations)
        if record["claim"]["canonical_network_number"] == 1
    )
    definition = next(
        record
        for record in _low_order_definitions(annotations)
        if record["claim"]["canonical_network_number"] == 1
    )
    if status == "working-hypothesis":
        basis = ["researcher-hypothesis"]
        confidence = "low"
    else:
        basis = ["no-evidence-yet"]
        confidence = "none"
    if evidence_basis is not None:
        basis = list(evidence_basis)
    identifiers = []
    if include_identifier:
        identifiers.append({
            "scheme": identifier_scheme,
            "value": identifier_value,
            "verification_state": "cross-checked",
            "evidence_record_ids": (
                list(identifier_evidence_ids)
                if identifier_evidence_ids is not None
                else (
                    [definition["evidence_id"], match["evidence_id"]]
                    if identifier_evidence
                    else []
                )
            ),
        })
    invalid_record = {
        "catalogue_id": match["claim"]["subject_catalogue_ids"][0],
        "comparison_status": status,
        "proposed_disposition": "unresolved",
        "exclusion_category": "unresolved",
        "exclusion_reason": None,
        "evidence_basis": basis,
        "evidence_record_ids": list(direct_evidence_ids),
        "previous_workspace_record_ids": [],
        "computational_cross_check_ids": [],
        "historical_identifiers": identifiers,
        "basic_graph_assignment": None,
        "confidence": confidence,
        "notes": ["Invalid partial low-order identity fixture."],
        "open_questions": [],
    }
    index = next(
        index
        for index, record in enumerate(annotations["records"])
        if record["catalogue_id"] == invalid_record["catalogue_id"]
    )
    annotations["records"][index] = invalid_record


@pytest.mark.parametrize("status", ["unresolved", "working-hypothesis"])
def test_low_order_identifier_requires_the_grouped_status(
    catalogue, annotations, status
):
    _add_low_order_bypass_record(annotations, status=status)
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_reviewed_low_order_number_cannot_omit_grouped_status(
    catalogue, annotations
):
    _add_low_order_bypass_record(annotations, identifier_evidence=False)
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_other_number_cannot_cite_low_order_identity_evidence(
    catalogue, annotations
):
    _add_low_order_bypass_record(annotations, identifier_value=108)
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_other_number_cannot_cite_low_order_aggregate_as_nested_evidence(
    catalogue, annotations
):
    _add_low_order_bypass_record(
        annotations,
        identifier_value=108,
        identifier_evidence_ids=[LOW_ORDER_AGGREGATE_ID],
    )
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("identifier_scheme", "identifier_value", "evidence_kind"),
    [
        ("morelli-smith-basic-graph", "G", "definition"),
        ("morelli-smith-basic-graph", "G", "match"),
        ("ladenheim-original-identifier", "L-1", "aggregate"),
    ],
)
def test_nested_low_order_evidence_triggers_consumption_for_every_identifier_scheme(
    catalogue, annotations, identifier_scheme, identifier_value, evidence_kind
):
    evidence_id = {
        "definition": _low_order_definitions(annotations)[0]["evidence_id"],
        "match": _low_order_matches(annotations)[0]["evidence_id"],
        "aggregate": LOW_ORDER_AGGREGATE_ID,
    }[evidence_kind]
    _add_low_order_bypass_record(
        annotations,
        identifier_scheme=identifier_scheme,
        identifier_value=identifier_value,
        identifier_evidence_ids=[evidence_id],
    )
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_direct_low_order_evidence_citation_requires_the_grouped_status(
    catalogue, annotations
):
    definition_id = _low_order_definitions(annotations)[0]["evidence_id"]
    _add_low_order_bypass_record(
        annotations,
        identifier_value=108,
        identifier_evidence=False,
        include_identifier=False,
        direct_evidence_ids=[definition_id],
    )
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_partial_low_order_identity_application_is_rejected(catalogue, annotations):
    _populate_low_order_identity_records(annotations)
    annotations["records"].pop()
    with pytest.raises(ValueError, match="complete 25-row group"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_retention_requires_its_identifier(catalogue, annotations):
    _populate_low_order_identity_records(annotations)
    annotations["records"][-1]["historical_identifiers"] = []
    with pytest.raises(ValueError, match="exact cross-checked canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_identifier_requires_its_own_number(catalogue, annotations):
    _populate_low_order_identity_records(annotations)
    annotations["records"][-1]["historical_identifiers"][0]["value"] = 1
    with pytest.raises(ValueError, match="exact cross-checked canonical"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("disposition", "category", "reason"),
    [("exclude", "other-canonical-exclusion", "wrong"),
     ("unresolved", "unresolved", None)],
)
def test_low_order_status_rejects_nonretention_dispositions(
    catalogue, annotations, disposition, category, reason
):
    _populate_low_order_identity_records(annotations)
    row = annotations["records"][-1]
    row["proposed_disposition"] = disposition
    row["exclusion_category"] = category
    row["exclusion_reason"] = reason
    with pytest.raises(ValueError, match="requires retention"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_status_is_invalid_for_a_rule(catalogue, annotations):
    rule = annotations["rules"][0]
    rule["comparison_status"] = "derived-canonical-identity-match"
    rule["proposed_disposition"] = "retain"
    rule["exclusion_category"] = "none"
    rule["exclusion_reason"] = None
    rule["evidence_basis"] = [
        "authoritative-canonical-diagram-plus-subject-bound-rice-match"
    ]
    with pytest.raises(ValueError, match="valid only for explicit records"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_identity_basis_is_invalid_for_a_rule(catalogue, annotations):
    annotations["rules"][0]["evidence_basis"].append(
        "authoritative-canonical-diagram-plus-subject-bound-rice-match"
    )
    with pytest.raises(ValueError, match="explicit-record only"):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_identity_basis_is_invalid_for_an_unresolved_record(
    catalogue, annotations
):
    _add_low_order_bypass_record(
        annotations,
        include_identifier=False,
        evidence_basis=[
            "authoritative-canonical-diagram-plus-subject-bound-rice-match"
        ],
    )
    with pytest.raises(ValueError):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_identity_basis_is_invalid_for_a_derived_unique_record(
    catalogue, annotations
):
    generated = generate_evidence_ledger(catalogue, annotations)
    row = next(
        record
        for record in generated["records"]
        if record["comparison_status"] == "derived-unique-match"
    )
    assertion_fields = {
        "catalogue_id",
        "comparison_status",
        "proposed_disposition",
        "exclusion_category",
        "exclusion_reason",
        "evidence_basis",
        "evidence_record_ids",
        "previous_workspace_record_ids",
        "computational_cross_check_ids",
        "historical_identifiers",
        "basic_graph_assignment",
        "confidence",
        "notes",
        "open_questions",
    }
    row = {field: deepcopy(row[field]) for field in assertion_fields}
    row["evidence_basis"].append(
        "authoritative-canonical-diagram-plus-subject-bound-rice-match"
    )
    annotations["records"].append(row)
    with pytest.raises(ValueError):
        generate_evidence_ledger(catalogue, annotations)


def test_low_order_identity_basis_is_invalid_for_a_working_hypothesis_record(
    catalogue, annotations
):
    _add_low_order_bypass_record(
        annotations,
        status="working-hypothesis",
        include_identifier=False,
        evidence_basis=[
            "researcher-hypothesis",
            "authoritative-canonical-diagram-plus-subject-bound-rice-match",
        ],
    )
    with pytest.raises(ValueError, match="identifiers require derived-canonical"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    "consumer_kind",
    ["definition", "match", "computation", "aggregate", "identifier", "nested"],
)
def test_all_low_order_identity_consumption_is_invalid_for_rules(
    catalogue, annotations, consumer_kind
):
    rule = annotations["rules"][0]
    if consumer_kind == "definition":
        rule["evidence_record_ids"].append(
            _low_order_definitions(annotations)[0]["evidence_id"]
        )
    elif consumer_kind == "match":
        rule["evidence_record_ids"].append(
            _low_order_matches(annotations)[0]["evidence_id"]
        )
    elif consumer_kind == "computation":
        rule["computational_cross_check_ids"].append(LOW_ORDER_COMPUTATION_ID)
    elif consumer_kind == "aggregate":
        rule["evidence_record_ids"].append(LOW_ORDER_AGGREGATE_ID)
    else:
        rule["historical_identifiers"].append({
            "scheme": "morelli-smith-canonical-network",
            "value": 1 if consumer_kind == "identifier" else 108,
            "verification_state": "cross-checked",
            "evidence_record_ids": (
                [] if consumer_kind == "identifier" else [LOW_ORDER_AGGREGATE_ID]
            ),
        })
    with pytest.raises(ValueError, match="explicit-record only"):
        generate_evidence_ledger(catalogue, annotations)
def test_four_element_canonical_group_is_complete_and_unapplied(catalogue, annotations):
    ledger = generate_evidence_ledger(catalogue, annotations)
    definitions = _four_element_definitions(annotations)
    matches = _four_element_matches(annotations)
    aggregate = _four_element_aggregate(annotations)["claim"]
    assert len(definitions) == len(matches) == 34
    assert {
        record["claim"]["canonical_network_number"] for record in definitions
    } == set(REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS)
    assert (
        len({record["claim"]["subject_catalogue_ids"][0] for record in matches}) == 34
    )
    assert aggregate["counts_by_element_order"] == {"4": 34}
    assert aggregate["subfamilies"] == ["IVA", "IVB", "IVC", "IVD", "IVE", "IVF"]
    assert aggregate["source_equivalence_class_count"] == 20
    assert aggregate["source_orbit_count"] == 10
    four_subjects = {
        reviewed[0] for reviewed in REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS.values()
    }
    assert all(
        row["comparison_status"] == "unresolved"
        for row in ledger["records"]
        if row["catalogue_id"] in four_subjects
    )


@pytest.mark.parametrize("claim_type", ["definition", "match"])
def test_four_element_group_rejects_missing_inventory(
    catalogue, annotations, claim_type
):
    records = (
        _four_element_definitions(annotations)
        if claim_type == "definition"
        else _four_element_matches(annotations)
    )
    record = records[-1]
    annotations["evidence_records"].remove(record)
    field = (
        "canonical_definition_evidence_record_ids"
        if claim_type == "definition"
        else "verified_evidence_record_ids"
    )
    _four_element_computation(annotations)[field].remove(record["evidence_id"])
    with pytest.raises(
        ValueError, match="four-element canonical .* inventory is incomplete"
    ):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("mutation", "expected"),
    [
        ("descriptor", "invalid canonical-network match"),
        ("diagram", "invalid canonical-network definition"),
        ("figure", "invalid canonical-network definition"),
        ("class-table", "invalid canonical-network definition"),
        ("orbit", "invalid canonical-network definition"),
        ("report-path", "report provenance"),
    ],
)
def test_four_element_group_rejects_mutated_reviewed_bindings(
    catalogue, annotations, mutation, expected
):
    definition = _four_element_definitions(annotations)[0]
    match = _four_element_matches(annotations)[0]
    if mutation == "descriptor":
        match["claim"]["representative_descriptor"] = "0-1:R"
    elif mutation == "diagram":
        definition["claim"]["diagram_locator"]["printed_page"] = 999
    elif mutation == "figure":
        definition["claim"]["figure_locator"]["figure"] = "6.1"
    elif mutation == "class-table":
        definition["claim"]["class_table_locator"]["pdf_page_index"] = 65
    elif mutation == "orbit":
        definition["claim"]["source_orbit"] = [20, 28]
    else:
        match["locator"]["repository_path"] = "README.md"
    with pytest.raises(ValueError, match=expected):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_orbit_count", 10.0),
        ("source_equivalence_class_count", True),
        ("total_networks", 34.0),
    ],
)
def test_four_element_aggregate_requires_strict_integer_counts(
    catalogue, annotations, field, value
):
    _four_element_aggregate(annotations)["claim"][field] = value
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 20.0, [20]])
def test_four_element_canonical_numbers_require_strict_integers(
    catalogue, annotations, value
):
    _four_element_definitions(annotations)[0]["claim"]["canonical_network_number"] = (
        value
    )
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


@pytest.mark.parametrize("value", [True, 20.0, [20]])
def test_four_element_orbit_members_require_strict_integers(
    catalogue, annotations, value
):
    _four_element_definitions(annotations)[0]["claim"]["source_orbit"][0] = value
    with pytest.raises(ValueError, match="invalid canonical-network definition"):
        generate_evidence_ledger(catalogue, annotations)


def test_four_element_computation_requires_exact_scope_and_revision(
    catalogue, annotations
):
    computation = _four_element_computation(annotations)
    computation["commit_sha"] = "0" * 40
    with pytest.raises(ValueError, match="four-element computation must use"):
        generate_evidence_ledger(catalogue, annotations)


def test_cross_group_definition_and_match_are_rejected(catalogue, annotations):
    low_match = _low_order_matches(annotations)[0]
    four_match = _four_element_matches(annotations)[0]
    low_match["claim"]["canonical_network_number"] = four_match["claim"][
        "canonical_network_number"
    ]
    with pytest.raises(ValueError, match="invalid canonical-network match"):
        generate_evidence_ledger(catalogue, annotations)


def test_cross_group_aggregate_scope_is_rejected(catalogue, annotations):
    aggregate = _four_element_aggregate(annotations)["claim"]
    aggregate["canonical_network_numbers"][0] = next(
        iter(REVIEWED_LOW_ORDER_CANONICAL_NETWORKS)
    )
    with pytest.raises(ValueError, match="invalid aggregate canonical-network"):
        generate_evidence_ledger(catalogue, annotations)


def test_complete_four_element_identity_application_can_pass(catalogue, annotations):
    _populate_four_element_identity_records(annotations)
    ledger = generate_evidence_ledger(catalogue, annotations)
    assert ledger["summary"]["by_proposed_disposition"] == {
        "exclude": 40,
        "retain": 59,
        "unresolved": 49,
    }


@pytest.mark.parametrize("consumer_count", [1, 33])
def test_partial_four_element_identity_application_is_rejected(
    catalogue, annotations, consumer_count
):
    _populate_four_element_identity_records(annotations)
    annotations["records"] = [
        record
        for record in annotations["records"]
        if record["catalogue_id"]
        not in {
            reviewed[0]
            for reviewed in list(REVIEWED_FOUR_ELEMENT_CANONICAL_NETWORKS.values())[
                consumer_count:
            ]
        }
    ]
    with pytest.raises(ValueError, match="complete 34-row group"):
        generate_evidence_ledger(catalogue, annotations)


def test_four_element_identifier_cannot_use_low_order_evidence(catalogue, annotations):
    _populate_four_element_identity_records(annotations)
    row = annotations["records"][-1]
    row["historical_identifiers"][0]["evidence_record_ids"][0] = _low_order_definitions(
        annotations
    )[0]["evidence_id"]
    with pytest.raises(ValueError, match="exact cross-checked canonical"):
        generate_evidence_ledger(catalogue, annotations)


def test_four_element_evidence_is_invalid_for_a_rule(catalogue, annotations):
    annotations["rules"][0]["evidence_record_ids"].append(
        _four_element_definitions(annotations)[0]["evidence_id"]
    )
    with pytest.raises(ValueError, match="explicit-record only"):
        generate_evidence_ledger(catalogue, annotations)


def test_indirect_four_element_evidence_is_invalid_for_a_rule(catalogue, annotations):
    computation_id = _append_indirect_low_order_computation(
        annotations, _four_element_matches(annotations)[0]["evidence_id"]
    )
    annotations["rules"][0]["computational_cross_check_ids"].append(computation_id)
    with pytest.raises(ValueError, match="explicit-record only"):
        generate_evidence_ledger(catalogue, annotations)


def test_prior_reduction_target_evidence_cannot_replace_canonical_identity_evidence(
    catalogue, annotations
):
    _populate_four_element_identity_records(annotations)
    row = annotations["records"][-1]
    reduction_target = next(
        record
        for record in annotations["evidence_records"]
        if record["claim"]["claim_type"] == "reduction-target-match"
    )
    row["evidence_record_ids"][1] = reduction_target["evidence_id"]
    with pytest.raises(ValueError, match="one definition, match, and aggregate"):
        generate_evidence_ledger(catalogue, annotations)

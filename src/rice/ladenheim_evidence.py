"""Evidence-ledger contract for the structural 148 to canonical 108 comparison."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path, PurePath
from typing import Any


FORMAT_VERSION = 2
COMPARISON_STATUSES = {
    "source-backed",
    "derived-unique-match",
    "working-hypothesis",
    "ambiguous",
    "unresolved",
}
DISPOSITIONS = {"exclude", "retain", "unresolved"}
EXCLUSION_CATEGORIES = {
    "simpler-bilinear-realisation",
    "zobel-four-element",
    "zobel-five-element-series-parallel",
    "other-canonical-exclusion",
    "none",
    "unresolved",
}
EVIDENCE_BASES = {
    "explicit-historical-entry-statement",
    "explicit-historical-table-or-figure-mapping",
    "aggregate-historical-category-plus-logically-unique-rice-match",
    "mechanically-derived-rice-structural-fact",
    "researcher-hypothesis",
    "no-evidence-yet",
}
CONFIDENCE_VALUES = {"high", "medium", "low", "none"}
SOURCE_TYPES = {
    "authoritative-publication",
    "rice-generated-artefact",
    "rice-documentation",
    "previous-workspace-repository",
}
EVIDENCE_PROVENANCE_LEVELS = {
    "authoritative-source-transcription",
    "rice-derived-structural-fact",
    "researcher-hypothesis",
}
WORKSPACE_PROVENANCE_LEVELS = {
    "previous-workspace-transcription",
    "previous-workspace-generated",
    "visual-cross-check",
}
COMPUTATION_PROVENANCE_LEVELS = {
    "independently-reproduced-computation",
    "previous-workspace-generated",
}
VERIFICATION_STATES = {
    "unreviewed",
    "parsed",
    "cross-checked",
    "source-verified",
    "conflicted",
    "rejected",
}
HISTORICAL_IDENTIFIER_SCHEMES = {
    "morelli-smith-basic-graph",
    "morelli-smith-canonical-network",
    "ladenheim-original-identifier",
}
LOCATOR_FIELDS = {
    "chapter",
    "section",
    "printed_page",
    "pdf_page_index",
    "figure",
    "appendix",
    "table",
    "network_number",
    "repository_path",
    "commit_sha",
}
PUBLICATION_LOCATOR_FIELDS = {
    "printed_page",
    "pdf_page_index",
    "figure",
    "appendix",
    "table",
    "network_number",
}
IMMUTABLE_FIELDS = (
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
)
ASSERTION_FIELDS = (
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
)


def _require_string_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise ValueError(f"{field} must be a list of non-empty strings")


def _validate_no_unstable_metadata(value: Any, field: str = "annotations") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if "timestamp" in key.lower():
                raise ValueError(f"timestamps are not allowed in {field}")
            _validate_no_unstable_metadata(item, f"{field}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _validate_no_unstable_metadata(item, f"{field}[{index}]")
    elif isinstance(value, str):
        lower = value.lower()
        if lower.startswith("/home/") or lower.startswith("/users/"):
            raise ValueError(f"absolute paths are not allowed in {field}")
        if len(value) >= 3 and value[1:3] in {":\\", ":/"}:
            raise ValueError(f"absolute paths are not allowed in {field}")


def _objects_by_id(
    values: Any, collection: str, id_field: str
) -> dict[str, dict[str, Any]]:
    if not isinstance(values, list):
        raise ValueError(f"{collection} must be a list")
    result: dict[str, dict[str, Any]] = {}
    for value in values:
        if not isinstance(value, dict):
            raise ValueError(f"each {collection} entry must be an object")
        record_id = value.get(id_field)
        if not isinstance(record_id, str) or not record_id:
            raise ValueError(f"each {collection} entry requires {id_field}")
        if record_id in result:
            raise ValueError(f"duplicate {id_field}: {record_id}")
        result[record_id] = value
    return result


def _validate_sources(values: Any) -> dict[str, dict[str, Any]]:
    sources = _objects_by_id(values, "sources", "source_id")
    for source_id, source in sources.items():
        if source.get("source_type") not in SOURCE_TYPES:
            raise ValueError(f"source {source_id} has invalid source_type")
        if not isinstance(source.get("citation"), str) or not source["citation"]:
            raise ValueError(f"source {source_id} requires non-empty citation")
        if not isinstance(source.get("notes"), str) or not source["notes"]:
            raise ValueError(f"source {source_id} requires non-empty notes")
        repository = source.get("repository")
        commit_sha = source.get("commit_sha")
        if source["source_type"] == "previous-workspace-repository":
            if not isinstance(repository, str) or not repository:
                raise ValueError(f"source {source_id} requires repository")
            if not isinstance(commit_sha, str) or not commit_sha:
                raise ValueError(f"source {source_id} requires commit_sha")
    return sources


def _validate_locator(locator: Any, record_id: str) -> None:
    if not isinstance(locator, dict) or not locator:
        raise ValueError(f"{record_id} requires a structured locator")
    unknown = set(locator) - LOCATOR_FIELDS
    if unknown:
        raise ValueError(f"{record_id} locator has unknown fields: {sorted(unknown)}")
    if not any(value is not None and value != "" for value in locator.values()):
        raise ValueError(f"{record_id} locator requires a meaningful field")
    for field in {"printed_page", "pdf_page_index", "network_number"}:
        value = locator.get(field)
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError(f"{record_id} locator {field} must be a non-negative integer")
    path = locator.get("repository_path")
    if path is not None:
        if not isinstance(path, str) or not path or PurePath(path).is_absolute():
            raise ValueError(f"{record_id} repository_path must be relative")
    for field, value in locator.items():
        if field not in {"printed_page", "pdf_page_index", "network_number"} and (
            value is not None and (not isinstance(value, str) or not value)
        ):
            raise ValueError(f"{record_id} locator {field} must be a non-empty string")


def _validate_evidence_records(
    values: Any, sources: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(values, "evidence_records", "evidence_id")
    for evidence_id, record in records.items():
        source_id = record.get("source_id")
        if source_id not in sources:
            raise ValueError(f"evidence {evidence_id} has unknown source_id")
        if record.get("provenance_level") not in EVIDENCE_PROVENANCE_LEVELS:
            raise ValueError(f"evidence {evidence_id} has invalid provenance_level")
        if record.get("verification_state") not in VERIFICATION_STATES:
            raise ValueError(f"evidence {evidence_id} has invalid verification_state")
        _validate_locator(record.get("locator"), evidence_id)
        if not isinstance(record.get("paraphrase"), str) or not record["paraphrase"]:
            raise ValueError(f"evidence {evidence_id} requires paraphrase")
        _require_string_list(record.get("asserted_fields"), f"{evidence_id}.asserted_fields")
        source = sources[source_id]
        if record["provenance_level"] == "authoritative-source-transcription":
            if source["source_type"] != "authoritative-publication":
                raise ValueError(f"evidence {evidence_id} is not from an authoritative source")
            if record["verification_state"] == "source-verified" and not any(
                record["locator"].get(field) is not None
                for field in PUBLICATION_LOCATOR_FIELDS
            ):
                raise ValueError(
                    f"source-verified evidence {evidence_id} requires a precise publication locator"
                )
    return records


def _validate_workspace_records(
    values: Any, sources: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(
        values, "previous_workspace_records", "workspace_record_id"
    )
    for record_id, record in records.items():
        source_id = record.get("source_id")
        if source_id not in sources or sources[source_id]["source_type"] != "previous-workspace-repository":
            raise ValueError(f"workspace record {record_id} requires a workspace source")
        if record.get("provenance_level") not in WORKSPACE_PROVENANCE_LEVELS:
            raise ValueError(f"workspace record {record_id} has invalid provenance_level")
        if record.get("verification_state") not in VERIFICATION_STATES:
            raise ValueError(f"workspace record {record_id} has invalid verification_state")
        for field in ("repository_path", "limitations"):
            if not isinstance(record.get(field), str) or not record[field]:
                raise ValueError(f"workspace record {record_id} requires {field}")
        if PurePath(record["repository_path"]).is_absolute():
            raise ValueError(f"workspace record {record_id} path must be relative")
    return records


def _validate_computational_cross_checks(
    values: Any,
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(
        values, "computational_cross_checks", "cross_check_id"
    )
    for record_id, record in records.items():
        if record.get("provenance_level") not in COMPUTATION_PROVENANCE_LEVELS:
            raise ValueError(f"cross-check {record_id} has invalid provenance_level")
        if record.get("verification_state") not in VERIFICATION_STATES:
            raise ValueError(f"cross-check {record_id} has invalid verification_state")
        for field in ("implementation", "commit_sha", "input", "operation", "result", "limitations"):
            if not isinstance(record.get(field), str) or not record[field]:
                raise ValueError(f"cross-check {record_id} requires {field}")
        if not isinstance(record.get("independently_reproduced"), bool):
            raise ValueError(f"cross-check {record_id} requires independently_reproduced")
    return records


def _require_references(value: Any, field: str, known: dict[str, Any]) -> None:
    _require_string_list(value, field)
    unknown = set(value) - known.keys()
    if unknown:
        raise ValueError(f"unknown {field}: {sorted(unknown)}")


def _authoritative_verified(
    evidence_ids: list[str], evidence: dict[str, dict[str, Any]]
) -> bool:
    return any(
        evidence[item]["provenance_level"] == "authoritative-source-transcription"
        and evidence[item]["verification_state"] == "source-verified"
        for item in evidence_ids
    )


def _rice_derived(evidence_ids: list[str], evidence: dict[str, dict[str, Any]]) -> bool:
    return any(
        evidence[item]["provenance_level"] == "rice-derived-structural-fact"
        for item in evidence_ids
    )


def _validate_historical_identifiers(
    values: Any, evidence: dict[str, dict[str, Any]]
) -> None:
    if not isinstance(values, list):
        raise ValueError("historical_identifiers must be a list")
    for identifier in values:
        if not isinstance(identifier, dict):
            raise ValueError("historical identifier must be an object")
        if identifier.get("scheme") not in HISTORICAL_IDENTIFIER_SCHEMES:
            raise ValueError("historical identifier has invalid scheme")
        if not isinstance(identifier.get("value"), (str, int)) or isinstance(
            identifier.get("value"), bool
        ) or identifier.get("value") == "":
            raise ValueError("historical identifier requires a string or integer value")
        if identifier.get("verification_state") not in VERIFICATION_STATES:
            raise ValueError("historical identifier has invalid verification_state")
        ids = identifier.get("evidence_record_ids")
        _require_references(ids, "historical identifier evidence_record_ids", evidence)
        if identifier["verification_state"] == "source-verified":
            suitable = [
                item
                for item in ids
                if "historical_identifiers" in evidence[item]["asserted_fields"]
                or identifier["scheme"] in evidence[item]["asserted_fields"]
            ]
            if not _authoritative_verified(suitable, evidence):
                raise ValueError(
                    "source-verified historical identifier requires appropriate "
                    "authoritative evidence"
                )


def _validate_basic_graph_assignment(
    value: Any, evidence: dict[str, dict[str, Any]]
) -> None:
    if value is None:
        return
    required = {
        "graph_label", "base_label", "is_dual", "fixture_id",
        "structural_relation", "verification_state", "evidence_record_ids",
    }
    if not isinstance(value, dict) or set(value) != required:
        raise ValueError("basic_graph_assignment has invalid fields")
    for field in ("graph_label", "base_label", "fixture_id", "structural_relation"):
        if not isinstance(value[field], str) or not value[field]:
            raise ValueError(f"basic_graph_assignment requires {field}")
    if not isinstance(value["is_dual"], bool):
        raise ValueError("basic_graph_assignment requires boolean is_dual")
    if value["verification_state"] not in VERIFICATION_STATES:
        raise ValueError("basic_graph_assignment has invalid verification_state")
    _require_references(value["evidence_record_ids"], "basic graph evidence_record_ids", evidence)


def _validate_assertion(
    assertion: dict[str, Any], evidence: dict[str, dict[str, Any]],
    workspace: dict[str, dict[str, Any]], computations: dict[str, dict[str, Any]],
) -> None:
    missing = set(ASSERTION_FIELDS) - assertion.keys()
    if missing:
        raise ValueError(f"assertion missing fields: {sorted(missing)}")
    if assertion["comparison_status"] not in COMPARISON_STATUSES:
        raise ValueError("invalid comparison_status")
    if assertion["proposed_disposition"] not in DISPOSITIONS:
        raise ValueError("invalid proposed_disposition")
    if assertion["exclusion_category"] not in EXCLUSION_CATEGORIES:
        raise ValueError("invalid exclusion_category")
    if assertion["confidence"] not in CONFIDENCE_VALUES:
        raise ValueError("invalid confidence")
    _require_string_list(assertion["evidence_basis"], "evidence_basis")
    if not set(assertion["evidence_basis"]) <= EVIDENCE_BASES:
        raise ValueError("invalid evidence_basis")
    _require_references(assertion["evidence_record_ids"], "evidence_record_ids", evidence)
    _require_references(assertion["previous_workspace_record_ids"], "previous_workspace_record_ids", workspace)
    _require_references(assertion["computational_cross_check_ids"], "computational_cross_check_ids", computations)
    _validate_historical_identifiers(assertion["historical_identifiers"], evidence)
    _validate_basic_graph_assignment(assertion["basic_graph_assignment"], evidence)
    _require_string_list(assertion["notes"], "notes")
    _require_string_list(assertion["open_questions"], "open_questions")

    status = assertion["comparison_status"]
    disposition = assertion["proposed_disposition"]
    category = assertion["exclusion_category"]
    reason = assertion["exclusion_reason"]
    evidence_ids = assertion["evidence_record_ids"]
    if status == "source-backed" and not _authoritative_verified(evidence_ids, evidence):
        raise ValueError("source-backed assertion requires authoritative source-verified evidence")
    if status == "derived-unique-match":
        if not _authoritative_verified(evidence_ids, evidence):
            raise ValueError("derived-unique-match requires aggregate authoritative evidence")
        if not _rice_derived(evidence_ids, evidence):
            raise ValueError("derived-unique-match requires a mechanical RICE basis")
    if disposition == "exclude":
        if category in {"none", "unresolved"} or not isinstance(reason, str) or not reason:
            raise ValueError("asserted exclusion requires category and reason")
        if not _authoritative_verified(evidence_ids, evidence):
            raise ValueError("asserted exclusion requires authoritative evidence")
    elif category not in {"none", "unresolved"}:
        raise ValueError("non-exclusion cannot assert an exclusion category")


def _default_assertion() -> dict[str, Any]:
    return {
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
        "notes": ["No individual canonical-catalogue mapping is established."],
        "open_questions": [
            "Which historical network or figure, if any, corresponds to this record?",
            "What entry-specific evidence establishes exclusion or retention?",
        ],
    }


def generate_evidence_ledger(
    catalogue: dict[str, Any], annotations: dict[str, Any]
) -> dict[str, Any]:
    """Validate annotations and join them to the committed 148 records."""

    _validate_no_unstable_metadata(annotations)
    if catalogue.get("object") != "ladenheim-structural-148-catalogue":
        raise ValueError("unexpected structural catalogue object")
    records = catalogue.get("records")
    if not isinstance(records, list) or len(records) != 148:
        raise ValueError("structural catalogue must contain exactly 148 records")
    ids = [row.get("catalogue_id") for row in records]
    if len(set(ids)) != 148 or not all(
        isinstance(value, str) and value.startswith("lh148-") for value in ids
    ):
        raise ValueError("structural catalogue IDs must be 148 unique lh148 IDs")
    if annotations.get("format_version") != FORMAT_VERSION:
        raise ValueError(f"annotation format_version must be {FORMAT_VERSION}")
    sources = _validate_sources(annotations.get("sources"))
    evidence = _validate_evidence_records(annotations.get("evidence_records"), sources)
    workspace = _validate_workspace_records(annotations.get("previous_workspace_records"), sources)
    computations = _validate_computational_cross_checks(annotations.get("computational_cross_checks"))
    namespaces = [set(sources), set(evidence), set(workspace), set(computations)]
    if sum(len(items) for items in namespaces) != len(set().union(*namespaces)):
        raise ValueError("record IDs must occupy separate namespaces")

    explicit: dict[str, dict[str, Any]] = {}
    annotation_records = annotations.get("records")
    if not isinstance(annotation_records, list):
        raise ValueError("annotation records must be a list")
    source_by_id = {row["catalogue_id"]: row for row in records}
    for annotation in annotation_records:
        if not isinstance(annotation, dict):
            raise ValueError("each annotation record must be an object")
        catalogue_id = annotation.get("catalogue_id")
        if catalogue_id in explicit:
            raise ValueError(f"duplicate annotation ID: {catalogue_id}")
        if catalogue_id not in source_by_id:
            raise ValueError(f"unknown annotation ID: {catalogue_id}")
        structural = annotation.get("structural_assertions", {})
        if not isinstance(structural, dict) or any(key not in IMMUTABLE_FIELDS for key in structural):
            raise ValueError("invalid structural_assertions")
        for field, value in structural.items():
            if source_by_id[catalogue_id][field] != value:
                raise ValueError(f"annotation contradicts immutable {field} for {catalogue_id}")
        assertion = {key: annotation.get(key) for key in ASSERTION_FIELDS}
        _validate_assertion(assertion, evidence, workspace, computations)
        explicit[catalogue_id] = assertion

    resolved = dict(explicit)
    rules = annotations.get("rules")
    if not isinstance(rules, list):
        raise ValueError("annotation rules must be a list")
    rule_ids: set[str] = set()
    for rule in rules:
        if not isinstance(rule, dict):
            raise ValueError("each annotation rule must be an object")
        rule_id = rule.get("rule_id")
        if not isinstance(rule_id, str) or not rule_id:
            raise ValueError("each annotation rule requires rule_id")
        if rule_id in rule_ids:
            raise ValueError(f"duplicate rule_id: {rule_id}")
        rule_ids.add(rule_id)
        if rule.get("kind") != "unique-component-match":
            raise ValueError("unsupported annotation rule")
        selector = rule.get("selector")
        if not isinstance(selector, dict) or not selector or any(
            field not in {"r", "l", "c", "lc", "rlc"} for field in selector
        ):
            raise ValueError("invalid unique-component-match selector")
        matches = [
            row for row in records
            if all(row[field] == value for field, value in selector.items())
        ]
        if len(matches) != rule.get("expected_matches"):
            raise ValueError("unique-component-match count differs from expectation")
        if any(row["catalogue_id"] in resolved for row in matches):
            raise ValueError("annotation rule overlaps another assertion")
        assertion = {key: rule.get(key) for key in ASSERTION_FIELDS}
        _validate_assertion(assertion, evidence, workspace, computations)
        if assertion["comparison_status"] != "derived-unique-match":
            raise ValueError("unique-component-match must be derived-unique-match")
        for row in matches:
            resolved[row["catalogue_id"]] = deepcopy(assertion)

    ledger_rows = []
    for source_row in records:
        row = {field: source_row[field] for field in IMMUTABLE_FIELDS}
        row.update(deepcopy(resolved.get(row["catalogue_id"], _default_assertion())))
        ledger_rows.append(row)

    statuses = Counter(row["comparison_status"] for row in ledger_rows)
    dispositions = Counter(row["proposed_disposition"] for row in ledger_rows)
    categories = Counter(row["exclusion_category"] for row in ledger_rows)
    return {
        "format_version": FORMAT_VERSION,
        "object": "ladenheim-148-to-108-evidence-ledger",
        "source_catalogue": "data/counts/ladenheim-148.json",
        "source_catalogue_relation": catalogue["relation"]["name"],
        "target": {
            "reported_members": 108,
            "reported_exclusions": 40,
            "exclusion_category_targets": {
                "simpler-bilinear-realisation": 8,
                "zobel-four-element": 4,
                "zobel-five-element-series-parallel": 20,
                "other-canonical-exclusion": 8,
            },
            "reproduction_claimed": False,
        },
        "sources": list(sources.values()),
        "evidence_records": list(evidence.values()),
        "previous_workspace_records": list(workspace.values()),
        "computational_cross_checks": list(computations.values()),
        "summary": {
            "total_rows": len(ledger_rows),
            "by_comparison_status": dict(sorted(statuses.items())),
            "by_proposed_disposition": dict(sorted(dispositions.items())),
            "by_exclusion_category": dict(sorted(categories.items())),
            "mapped_exclusions": dispositions["exclude"],
            "unresolved_dispositions": dispositions["unresolved"],
        },
        "records": ledger_rows,
    }


def load_and_generate(catalogue_path: Path, annotation_path: Path) -> dict[str, Any]:
    catalogue = json.loads(catalogue_path.read_text(encoding="utf-8"))
    annotations = json.loads(annotation_path.read_text(encoding="utf-8"))
    return generate_evidence_ledger(catalogue, annotations)


def ledger_json(catalogue_path: Path, annotation_path: Path) -> str:
    return json.dumps(
        load_and_generate(catalogue_path, annotation_path), indent=2, sort_keys=True
    ) + "\n"

"""Evidence-ledger contract for the structural 148 to canonical 108 comparison."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
from typing import Any


FORMAT_VERSION = 2
SOURCE_CATALOGUE_RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"
COMPARISON_STATUSES = {
    "source-backed",
    "derived-unique-match",
    "working-hypothesis",
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
GLOBALLY_UNIQUE_HISTORICAL_IDENTIFIER_SCHEMES = {
    "morelli-smith-canonical-network",
}
REUSABLE_HISTORICAL_IDENTIFIER_SCHEMES = {
    "morelli-smith-basic-graph",
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
CLAIM_TYPES = {
    "catalogue-target",
    "exclusion-category-targets",
    "aggregate-exclusion-category",
    "rice-selector-count",
    "individual-catalogue-record",
    "historical-identifier",
    "basic-graph-definition",
    "basic-graph-match",
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
ANNOTATION_FIELDS = {
    "format_version", "sources", "evidence_records", "previous_workspace_records",
    "computational_cross_checks", "target", "rules", "records",
}
SOURCE_REQUIRED_FIELDS = {"source_id", "source_type", "citation", "notes"}
SOURCE_OPTIONAL_FIELDS = {"publication", "repository", "commit_sha"}
PUBLICATION_FIELDS = {"publisher", "year"}
EVIDENCE_REQUIRED_FIELDS = {
    "evidence_id", "source_id", "provenance_level", "verification_state",
    "locator", "paraphrase", "claim",
}
EVIDENCE_OPTIONAL_FIELDS = {"notes"}
WORKSPACE_REQUIRED_FIELDS = {
    "workspace_record_id", "source_id", "provenance_level", "repository_path",
    "verification_state", "limitations", "notes",
}
WORKSPACE_OPTIONAL_FIELDS = {
    "row", "image", "descriptor", "graph_label", "network_number",
}
COMPUTATION_FIELDS = {
    "cross_check_id", "provenance_level", "implementation", "commit_sha", "input",
    "operation", "result", "independently_reproduced", "limitations",
    "verification_state",
}
TARGET_FIELDS = {
    "source_population", "reported_members", "reported_exclusions",
    "exclusion_category_targets", "evidence_record_ids",
}
RULE_FIELDS = set(ASSERTION_FIELDS) | {
    "rule_id", "kind", "selector", "expected_matches",
}
def _validate_object_shape(
    value: Any, name: str, required: set[str], optional: set[str] | None = None
) -> None:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    allowed = required | (optional or set())
    missing = required - value.keys()
    unknown = value.keys() - allowed
    if missing:
        raise ValueError(f"{name} missing fields: {sorted(missing)}")
    if unknown:
        raise ValueError(f"{name} has unknown fields: {sorted(unknown)}")


def _require_string_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise ValueError(f"{field} must be a list of non-empty strings")


def _require_unique_string_list(value: Any, field: str) -> None:
    _require_string_list(value, field)
    if len(set(value)) != len(value):
        raise ValueError(f"{field} must not contain duplicates")


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _is_controlled(value: Any, choices: set[str]) -> bool:
    return isinstance(value, str) and value in choices


def _is_machine_absolute_path(value: str) -> bool:
    """Recognize machine-absolute path tokens, including paths within prose."""

    without_urls = re.sub(r"\bhttps?://[^\s\]\[(){}<>\"']+", "", value)
    boundary = r"(?:^|[^A-Za-z0-9])"
    posix_boundary = r"(?:^|[^A-Za-z0-9.])"
    return any(
        re.search(pattern, without_urls) is not None
        for pattern in (
            posix_boundary + r"/(?!/)(?=[^\s])",
            boundary + r"//[^/\s]+/",
            boundary + r"\\\\[^\\\s]+\\",
            boundary + r"[A-Za-z]:[\\/]",
        )
    )


def _is_structural_selector(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and bool(value)
        and all(field in {"r", "l", "c", "lc", "rlc"} for field in value)
        and all(_is_int(item) and item >= 0 for item in value.values())
    )


def _validate_subjects(
    subjects: Any, evidence_id: str, catalogue_ids: set[str]
) -> None:
    if (
        not isinstance(subjects, list)
        or not subjects
        or not all(isinstance(item, str) for item in subjects)
        or len(set(subjects)) != len(subjects)
    ):
        raise ValueError(f"evidence {evidence_id} has invalid catalogue subjects")
    unknown = set(subjects) - catalogue_ids
    if unknown:
        raise ValueError(
            f"evidence {evidence_id} has unknown catalogue subjects: {sorted(unknown)}"
        )


def _validate_historical_identifier_value(
    scheme: Any, value: Any, field: str
) -> None:
    if not _is_controlled(scheme, HISTORICAL_IDENTIFIER_SCHEMES):
        raise ValueError(f"{field} has invalid historical identifier scheme")
    if scheme == "morelli-smith-canonical-network":
        if not _is_int(value) or not 1 <= value <= 108:
            raise ValueError(f"{field} canonical network must be an integer from 1 to 108")
    elif scheme == "morelli-smith-basic-graph":
        if not isinstance(value, str) or not value:
            raise ValueError(f"{field} basic graph must be a non-empty string")
    elif not (
        (isinstance(value, str) and bool(value))
        or (_is_int(value) and value > 0)
    ):
        raise ValueError(
            f"{field} Ladenheim identifier must be a non-empty string or positive integer"
        )


def _is_unstable_time_key(key: Any) -> bool:
    if not isinstance(key, str):
        return False
    normalized = re.sub(r"(?<!^)(?=[A-Z])", "_", key).replace("-", "_").lower()
    return normalized == "timestamp" or normalized.endswith("_timestamp") or normalized in {
        "generated_at",
        "created_at",
        "updated_at",
        "modified_at",
        "recorded_at",
        "checked_at",
        "processed_at",
        "exported_at",
        "written_at",
    }


def _validate_no_unstable_metadata(value: Any, field: str = "annotations") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if _is_unstable_time_key(key):
                raise ValueError(f"timestamps are not allowed in {field}")
            _validate_no_unstable_metadata(item, f"{field}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _validate_no_unstable_metadata(item, f"{field}[{index}]")
    elif isinstance(value, str):
        if _is_machine_absolute_path(value):
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
        _validate_object_shape(
            source, f"source {source_id}", SOURCE_REQUIRED_FIELDS, SOURCE_OPTIONAL_FIELDS
        )
        if not _is_controlled(source.get("source_type"), SOURCE_TYPES):
            raise ValueError(f"source {source_id} has invalid source_type")
        if not isinstance(source.get("citation"), str) or not source["citation"]:
            raise ValueError(f"source {source_id} requires non-empty citation")
        if not isinstance(source.get("notes"), str) or not source["notes"]:
            raise ValueError(f"source {source_id} requires non-empty notes")
        publication = source.get("publication")
        if publication is not None:
            _validate_object_shape(
                publication, f"source {source_id} publication", PUBLICATION_FIELDS
            )
            for field in set(publication) - {"year"}:
                if not isinstance(publication[field], str) or not publication[field]:
                    raise ValueError(
                        f"source {source_id} publication {field} must be non-empty"
                    )
            year = publication.get("year")
            if year is not None and (not _is_int(year) or year <= 0):
                raise ValueError(f"source {source_id} publication year must be a positive integer")
        repository = source.get("repository")
        commit_sha = source.get("commit_sha")
        if source["source_type"] == "previous-workspace-repository":
            if not isinstance(repository, str) or not repository:
                raise ValueError(f"source {source_id} requires repository")
            if not isinstance(commit_sha, str) or not commit_sha:
                raise ValueError(f"source {source_id} requires commit_sha")
        elif repository is not None or commit_sha is not None:
            raise ValueError(
                f"source {source_id} repository metadata requires workspace source type"
            )
        if source["source_type"] == "authoritative-publication" and publication is None:
            raise ValueError(f"source {source_id} requires publication metadata")
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
        minimum = 0 if field == "pdf_page_index" else 1
        if value is not None and (not _is_int(value) or value < minimum):
            qualifier = "non-negative" if minimum == 0 else "positive"
            raise ValueError(
                f"{record_id} locator {field} must be a {qualifier} integer"
            )
    path = locator.get("repository_path")
    if path is not None:
        if not isinstance(path, str) or not path or _is_machine_absolute_path(path):
            raise ValueError(f"{record_id} repository_path must be relative")
    for field, value in locator.items():
        if field not in {"printed_page", "pdf_page_index", "network_number"} and (
            value is not None and (not isinstance(value, str) or not value)
        ):
            raise ValueError(f"{record_id} locator {field} must be a non-empty string")


def _validate_claim(
    claim: Any, evidence_id: str, catalogue_ids: set[str]
) -> None:
    if not isinstance(claim, dict) or not _is_controlled(
        claim.get("claim_type"), CLAIM_TYPES
    ):
        raise ValueError(f"evidence {evidence_id} requires a valid structured claim")
    claim_type = claim["claim_type"]
    if claim_type == "catalogue-target":
        _validate_object_shape(
            claim, f"evidence {evidence_id} catalogue-target claim",
            {"claim_type", "supported_values"},
        )
        expected = {"source_population", "reported_members", "reported_exclusions"}
        values = claim.get("supported_values")
        if not isinstance(values, dict) or set(values) != expected or not all(
            _is_int(values[field]) and values[field] > 0 for field in expected
        ):
            raise ValueError(f"evidence {evidence_id} has invalid catalogue-target claim")
        if values["source_population"] != (
            values["reported_members"] + values["reported_exclusions"]
        ):
            raise ValueError(
                f"evidence {evidence_id} has inconsistent catalogue-target arithmetic"
            )
    elif claim_type == "exclusion-category-targets":
        _validate_object_shape(
            claim, f"evidence {evidence_id} category-target claim",
            {"claim_type", "supported_values"},
        )
        values = claim.get("supported_values")
        targets = (
            values.get("exclusion_category_targets")
            if isinstance(values, dict)
            and set(values) == {"exclusion_category_targets"}
            else None
        )
        expected = EXCLUSION_CATEGORIES - {"none", "unresolved"}
        if not isinstance(targets, dict) or set(targets) != expected or not all(
            _is_int(value) and value > 0 for value in targets.values()
        ):
            raise ValueError(f"evidence {evidence_id} has invalid category-target claim")
    elif claim_type == "aggregate-exclusion-category":
        _validate_object_shape(
            claim, f"evidence {evidence_id} aggregate exclusion claim",
            {"claim_type", "supported_exclusion_category", "supported_selector",
             "source_population", "supported_disposition"},
        )
        selector = claim.get("supported_selector")
        if (
            not _is_controlled(
                claim.get("supported_exclusion_category"),
                EXCLUSION_CATEGORIES - {"none", "unresolved"},
            )
            or not _is_structural_selector(selector)
            or not _is_int(claim.get("source_population"))
            or claim["source_population"] <= 0
            or claim.get("supported_disposition") != "exclude"
        ):
            raise ValueError(f"evidence {evidence_id} has invalid aggregate exclusion claim")
    elif claim_type == "rice-selector-count":
        _validate_object_shape(
            claim, f"evidence {evidence_id} selector/count claim",
            {"claim_type", "supported_selector", "expected_matches"},
        )
        selector = claim.get("supported_selector")
        if (
            not _is_structural_selector(selector)
            or not _is_int(claim.get("expected_matches"))
            or claim["expected_matches"] <= 0
        ):
            raise ValueError(f"evidence {evidence_id} has invalid selector/count claim")
    elif claim_type == "individual-catalogue-record":
        _validate_object_shape(
            claim, f"evidence {evidence_id} individual-record claim",
            {"claim_type", "subject_catalogue_ids", "supported_values"},
        )
        subjects = claim.get("subject_catalogue_ids")
        _validate_subjects(subjects, evidence_id, catalogue_ids)
        values = claim.get("supported_values")
        allowed = {"proposed_disposition", "exclusion_category", "exclusion_reason"}
        if (
            not isinstance(values, dict)
            or not values
            or not set(values) <= allowed
        ):
            raise ValueError(f"evidence {evidence_id} has invalid individual-record claim")
        disposition = values.get("proposed_disposition")
        category = values.get("exclusion_category")
        reason_present = "exclusion_reason" in values
        reason = values.get("exclusion_reason")
        if disposition is not None and not _is_controlled(disposition, DISPOSITIONS):
            raise ValueError(f"evidence {evidence_id} has invalid disposition")
        if category is not None and not _is_controlled(category, EXCLUSION_CATEGORIES):
            raise ValueError(f"evidence {evidence_id} has invalid exclusion category")
        if reason_present and reason is not None and (
            not isinstance(reason, str) or not reason
        ):
            raise ValueError(f"evidence {evidence_id} has invalid exclusion reason")
        concrete_category = category not in {None, "none", "unresolved"}
        if disposition == "exclude":
            if not concrete_category or not reason_present or not reason:
                raise ValueError(
                    f"evidence {evidence_id} exclusion claim requires disposition, category, and reason"
                )
        elif concrete_category:
            raise ValueError(
                f"evidence {evidence_id} concrete exclusion category requires exclude disposition"
            )
        if disposition in {"retain", "unresolved"} and reason_present and reason is not None:
            raise ValueError(
                f"evidence {evidence_id} non-exclusion claim cannot have exclusion reason"
            )
        if disposition == "retain" and values != {
            "proposed_disposition": "retain",
            "exclusion_category": "none",
            "exclusion_reason": None,
        }:
            raise ValueError(
                f"evidence {evidence_id} retained claim requires complete retention tuple"
            )
        if disposition == "unresolved" and category not in {None, "unresolved"}:
            raise ValueError(f"evidence {evidence_id} unresolved claim has invalid category")
        if disposition is None and reason_present and reason is not None:
            raise ValueError(
                f"evidence {evidence_id} exclusion reason requires exclude disposition"
            )
    elif claim_type == "historical-identifier":
        _validate_object_shape(
            claim, f"evidence {evidence_id} identifier claim",
            {"claim_type", "subject_catalogue_ids", "scheme", "value"},
        )
        subjects = claim.get("subject_catalogue_ids")
        _validate_subjects(subjects, evidence_id, catalogue_ids)
        _validate_historical_identifier_value(
            claim.get("scheme"), claim.get("value"), f"evidence {evidence_id}"
        )
    elif claim_type == "basic-graph-definition":
        _validate_object_shape(
            claim, f"evidence {evidence_id} graph-definition claim",
            {"claim_type", "definition"},
        )
        required = {
            "graph_label", "base_label", "is_dual", "fixture_id"
        }
        definition = claim.get("definition")
        if (
            not isinstance(definition, dict)
            or set(definition) != required
            or not all(
                isinstance(definition[field], str) and definition[field]
                for field in required - {"is_dual"}
            )
            or not isinstance(definition["is_dual"], bool)
        ):
            raise ValueError(f"evidence {evidence_id} has invalid graph-definition claim")
    elif claim_type == "basic-graph-match":
        _validate_object_shape(
            claim, f"evidence {evidence_id} graph-match claim",
            {"claim_type", "subject_catalogue_ids", "match"},
        )
        subjects = claim.get("subject_catalogue_ids")
        _validate_subjects(subjects, evidence_id, catalogue_ids)
        required = {"fixture_id", "graph_label", "structural_relation", "matched"}
        match = claim.get("match")
        if (
            not isinstance(match, dict)
            or set(match) != required
            or not all(
                isinstance(match[field], str) and match[field]
                for field in required - {"matched"}
            )
            or not isinstance(match["matched"], bool)
        ):
            raise ValueError(f"evidence {evidence_id} has invalid graph-match claim")


def _validate_evidence_records(
    values: Any, sources: dict[str, dict[str, Any]], catalogue_ids: set[str]
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(values, "evidence_records", "evidence_id")
    for evidence_id, record in records.items():
        _validate_object_shape(
            record, f"evidence {evidence_id}", EVIDENCE_REQUIRED_FIELDS,
            EVIDENCE_OPTIONAL_FIELDS,
        )
        source_id = record.get("source_id")
        if source_id not in sources:
            raise ValueError(f"evidence {evidence_id} has unknown source_id")
        if not _is_controlled(record.get("provenance_level"), EVIDENCE_PROVENANCE_LEVELS):
            raise ValueError(f"evidence {evidence_id} has invalid provenance_level")
        if not _is_controlled(record.get("verification_state"), VERIFICATION_STATES):
            raise ValueError(f"evidence {evidence_id} has invalid verification_state")
        _validate_locator(record.get("locator"), evidence_id)
        if not isinstance(record.get("paraphrase"), str) or not record["paraphrase"]:
            raise ValueError(f"evidence {evidence_id} requires paraphrase")
        if "notes" in record and (
            not isinstance(record["notes"], str) or not record["notes"]
        ):
            raise ValueError(f"evidence {evidence_id} notes must be non-empty")
        _validate_claim(record.get("claim"), evidence_id, catalogue_ids)
        claim = record["claim"]
        if (
            claim["claim_type"] == "historical-identifier"
            and claim["scheme"] == "morelli-smith-canonical-network"
            and "network_number" in record["locator"]
            and record["locator"]["network_number"] != claim["value"]
        ):
            raise ValueError(
                f"evidence {evidence_id} network_number locator does not match "
                "the claimed canonical network"
            )
        source = sources[source_id]
        if source["source_type"] == "previous-workspace-repository":
            raise ValueError(
                f"evidence {evidence_id} cannot use a previous-workspace source"
            )
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
        elif record["provenance_level"] == "rice-derived-structural-fact" and source[
            "source_type"
        ] not in {"rice-generated-artefact", "rice-documentation"}:
            raise ValueError(
                f"RICE-derived evidence {evidence_id} requires a RICE source"
            )
    return records


def _validate_workspace_records(
    values: Any, sources: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(
        values, "previous_workspace_records", "workspace_record_id"
    )
    for record_id, record in records.items():
        _validate_object_shape(
            record, f"workspace record {record_id}", WORKSPACE_REQUIRED_FIELDS,
            WORKSPACE_OPTIONAL_FIELDS,
        )
        source_id = record.get("source_id")
        if source_id not in sources or sources[source_id]["source_type"] != "previous-workspace-repository":
            raise ValueError(f"workspace record {record_id} requires a workspace source")
        if not _is_controlled(record.get("provenance_level"), WORKSPACE_PROVENANCE_LEVELS):
            raise ValueError(f"workspace record {record_id} has invalid provenance_level")
        if not _is_controlled(record.get("verification_state"), VERIFICATION_STATES):
            raise ValueError(f"workspace record {record_id} has invalid verification_state")
        for field in ("repository_path", "limitations", "notes"):
            if not isinstance(record.get(field), str) or not record[field]:
                raise ValueError(f"workspace record {record_id} requires {field}")
        if _is_machine_absolute_path(record["repository_path"]):
            raise ValueError(f"workspace record {record_id} path must be relative")
        for field in WORKSPACE_OPTIONAL_FIELDS - {"network_number"}:
            if field in record and (
                not isinstance(record[field], str) or not record[field]
            ):
                raise ValueError(f"workspace record {record_id} has invalid {field}")
        if "network_number" in record and (
            not _is_int(record["network_number"]) or record["network_number"] <= 0
        ):
            raise ValueError(f"workspace record {record_id} has invalid network_number")
    return records


def _validate_computational_cross_checks(
    values: Any,
) -> dict[str, dict[str, Any]]:
    records = _objects_by_id(
        values, "computational_cross_checks", "cross_check_id"
    )
    for record_id, record in records.items():
        _validate_object_shape(
            record, f"cross-check {record_id}", COMPUTATION_FIELDS
        )
        if not _is_controlled(record.get("provenance_level"), COMPUTATION_PROVENANCE_LEVELS):
            raise ValueError(f"cross-check {record_id} has invalid provenance_level")
        if not _is_controlled(record.get("verification_state"), VERIFICATION_STATES):
            raise ValueError(f"cross-check {record_id} has invalid verification_state")
        for field in ("implementation", "commit_sha", "input", "operation", "result", "limitations"):
            if not isinstance(record.get(field), str) or not record[field]:
                raise ValueError(f"cross-check {record_id} requires {field}")
        if not isinstance(record.get("independently_reproduced"), bool):
            raise ValueError(f"cross-check {record_id} requires independently_reproduced")
        expected_reproduced = (
            record["provenance_level"] == "independently-reproduced-computation"
        )
        if record["independently_reproduced"] is not expected_reproduced:
            raise ValueError(
                f"cross-check {record_id} provenance contradicts independently_reproduced"
            )
    return records


def _require_references(value: Any, field: str, known: dict[str, Any]) -> None:
    _require_unique_string_list(value, field)
    unknown = set(value) - known.keys()
    if unknown:
        raise ValueError(f"unknown {field}: {sorted(unknown)}")


def _is_authoritative(record: dict[str, Any]) -> bool:
    return (
        record["provenance_level"] == "authoritative-source-transcription"
        and record["verification_state"] == "source-verified"
    )


def _is_positive_rice_derived(record: dict[str, Any]) -> bool:
    return (
        record["provenance_level"] == "rice-derived-structural-fact"
        and record["verification_state"] in {"cross-checked", "source-verified"}
    )


def _matching_evidence(
    evidence_ids: list[str], evidence: dict[str, dict[str, Any]], claim_type: str
) -> list[dict[str, Any]]:
    return [
        evidence[item]
        for item in evidence_ids
        if evidence[item]["verification_state"] != "rejected"
        and evidence[item]["claim"]["claim_type"] == claim_type
    ]


def _validate_historical_identifiers(
    values: Any, evidence: dict[str, dict[str, Any]], catalogue_id: str | None
) -> None:
    if not isinstance(values, list):
        raise ValueError("historical_identifiers must be a list")
    seen: set[tuple[str, str]] = set()
    for identifier in values:
        _validate_object_shape(
            identifier, "historical identifier",
            {"scheme", "value", "verification_state", "evidence_record_ids"},
            {"notes"},
        )
        _validate_historical_identifier_value(
            identifier.get("scheme"), identifier.get("value"), "historical identifier"
        )
        identity = (identifier["scheme"], repr(identifier["value"]))
        if identity in seen:
            raise ValueError("historical_identifiers must not contain duplicates")
        seen.add(identity)
        if not _is_controlled(identifier.get("verification_state"), VERIFICATION_STATES):
            raise ValueError("historical identifier has invalid verification_state")
        if "notes" in identifier and (
            not isinstance(identifier["notes"], str) or not identifier["notes"]
        ):
            raise ValueError("historical identifier notes must be non-empty")
        ids = identifier.get("evidence_record_ids")
        _require_references(ids, "historical identifier evidence_record_ids", evidence)
        if identifier["verification_state"] == "source-verified":
            suitable = _matching_evidence(ids, evidence, "historical-identifier")
            if not any(
                _is_authoritative(record)
                and catalogue_id in record["claim"]["subject_catalogue_ids"]
                and record["claim"]["scheme"] == identifier["scheme"]
                and record["claim"]["value"] == identifier["value"]
                for record in suitable
            ):
                raise ValueError(
                    "source-verified historical identifier requires appropriate "
                    "authoritative evidence"
                )


def _validate_basic_graph_assignment(
    value: Any, evidence: dict[str, dict[str, Any]], catalogue_id: str | None
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
    if not _is_controlled(value["verification_state"], VERIFICATION_STATES):
        raise ValueError("basic_graph_assignment has invalid verification_state")
    _require_references(value["evidence_record_ids"], "basic graph evidence_record_ids", evidence)
    expected_definition = {key: value[key] for key in (
        "graph_label", "base_label", "is_dual", "fixture_id"
    )}
    definitions = _matching_evidence(
        value["evidence_record_ids"], evidence, "basic-graph-definition"
    )
    if not any(
        _is_authoritative(record)
        and record["claim"]["definition"] == expected_definition
        for record in definitions
    ):
        raise ValueError(
            "basic_graph_assignment requires exact authoritative graph-definition evidence"
        )
    expected_match = {
        "fixture_id": value["fixture_id"],
        "graph_label": value["graph_label"],
        "structural_relation": value["structural_relation"],
        "matched": True,
    }
    matches = _matching_evidence(
        value["evidence_record_ids"], evidence, "basic-graph-match"
    )
    if not any(
        _is_positive_rice_derived(record)
        and catalogue_id in record["claim"]["subject_catalogue_ids"]
        and record["claim"]["match"] == expected_match
        for record in matches
    ):
        raise ValueError(
            "basic_graph_assignment requires exact subject-bound RICE graph-match evidence"
        )


def _validate_assertion(
    assertion: dict[str, Any], evidence: dict[str, dict[str, Any]],
    workspace: dict[str, dict[str, Any]], computations: dict[str, dict[str, Any]],
    *, catalogue_id: str | None = None,
    rule_selector: dict[str, int] | None = None,
    expected_matches: int | None = None,
) -> None:
    missing = set(ASSERTION_FIELDS) - assertion.keys()
    if missing:
        raise ValueError(f"assertion missing fields: {sorted(missing)}")
    if not _is_controlled(assertion["comparison_status"], COMPARISON_STATUSES):
        raise ValueError("invalid comparison_status")
    if not _is_controlled(assertion["proposed_disposition"], DISPOSITIONS):
        raise ValueError("invalid proposed_disposition")
    if not _is_controlled(assertion["exclusion_category"], EXCLUSION_CATEGORIES):
        raise ValueError("invalid exclusion_category")
    if not _is_controlled(assertion["confidence"], CONFIDENCE_VALUES):
        raise ValueError("invalid confidence")
    _require_unique_string_list(assertion["evidence_basis"], "evidence_basis")
    if not set(assertion["evidence_basis"]) <= EVIDENCE_BASES:
        raise ValueError("invalid evidence_basis")
    basis = set(assertion["evidence_basis"])
    status = assertion["comparison_status"]
    if status == "unresolved" and (
        assertion["proposed_disposition"] != "unresolved"
        or assertion["exclusion_category"] != "unresolved"
        or assertion["exclusion_reason"] is not None
        or assertion["evidence_basis"] != ["no-evidence-yet"]
        or assertion["confidence"] != "none"
    ):
        raise ValueError("unresolved status requires the default unresolved contract")
    if "no-evidence-yet" in basis and (
        status != "unresolved" or basis != {"no-evidence-yet"}
    ):
        raise ValueError("no-evidence-yet is exclusive to unresolved assertions")
    historical_bases = {
        "explicit-historical-entry-statement",
        "explicit-historical-table-or-figure-mapping",
    }
    if status == "source-backed" and not basis & historical_bases:
        raise ValueError(f"evidence_basis is inconsistent with {status}")
    required_basis = {
        "derived-unique-match": {
            "aggregate-historical-category-plus-logically-unique-rice-match",
            "mechanically-derived-rice-structural-fact",
        },
        "working-hypothesis": {"researcher-hypothesis"},
    }
    if status in required_basis and not required_basis[status] <= basis:
        raise ValueError(f"evidence_basis is inconsistent with {status}")
    if status == "working-hypothesis" and assertion["proposed_disposition"] != "unresolved":
        raise ValueError("working-hypothesis cannot assert retention or exclusion")
    if status == "working-hypothesis" and (
        assertion["exclusion_category"] != "unresolved"
        or assertion["exclusion_reason"] is not None
    ):
        raise ValueError("working-hypothesis requires unresolved exclusion metadata")
    if status == "source-backed" and assertion["proposed_disposition"] not in {
        "exclude", "retain"
    }:
        raise ValueError("source-backed status requires a positive disposition")
    if status != "unresolved" and assertion["confidence"] == "none":
        raise ValueError("resolved comparison status requires non-none confidence")
    _require_references(assertion["evidence_record_ids"], "evidence_record_ids", evidence)
    _require_references(assertion["previous_workspace_record_ids"], "previous_workspace_record_ids", workspace)
    _require_references(assertion["computational_cross_check_ids"], "computational_cross_check_ids", computations)
    _validate_historical_identifiers(
        assertion["historical_identifiers"], evidence, catalogue_id
    )
    _validate_basic_graph_assignment(
        assertion["basic_graph_assignment"], evidence, catalogue_id
    )
    _require_string_list(assertion["notes"], "notes")
    _require_string_list(assertion["open_questions"], "open_questions")

    disposition = assertion["proposed_disposition"]
    category = assertion["exclusion_category"]
    reason = assertion["exclusion_reason"]
    evidence_ids = assertion["evidence_record_ids"]
    individual = _matching_evidence(
        evidence_ids, evidence, "individual-catalogue-record"
    )
    matching_individual = [
        record
        for record in individual
        if catalogue_id in record["claim"]["subject_catalogue_ids"]
        and all(
            assertion[field] == value
            for field, value in record["claim"]["supported_values"].items()
        )
    ]
    if status == "source-backed" and not any(
        _is_authoritative(record) for record in matching_individual
    ):
        raise ValueError(
            "source-backed assertion requires claim-specific authoritative evidence"
        )
    if status == "derived-unique-match":
        aggregate = _matching_evidence(
            evidence_ids, evidence, "aggregate-exclusion-category"
        )
        if not any(
            _is_authoritative(record)
            and record["claim"]["supported_exclusion_category"] == category
            and record["claim"]["supported_selector"] == rule_selector
            and record["claim"]["source_population"] == expected_matches
            and record["claim"]["supported_disposition"] == disposition
            for record in aggregate
        ):
            raise ValueError(
                "derived-unique-match requires matching aggregate authoritative evidence"
            )
        derived = _matching_evidence(evidence_ids, evidence, "rice-selector-count")
        if not any(
            _is_positive_rice_derived(record)
            and record["claim"]["supported_selector"] == rule_selector
            and record["claim"]["expected_matches"] == expected_matches
            for record in derived
        ):
            raise ValueError(
                "derived-unique-match requires a matching mechanical RICE basis"
            )
    if disposition == "exclude":
        if category in {"none", "unresolved"} or not isinstance(reason, str) or not reason:
            raise ValueError("asserted exclusion requires category and reason")
        aggregate_match = any(
            _is_authoritative(record)
            and record["claim"]["supported_exclusion_category"] == category
            and record["claim"]["supported_selector"] == rule_selector
            and record["claim"]["source_population"] == expected_matches
            and record["claim"]["supported_disposition"] == disposition
            for record in _matching_evidence(
                evidence_ids, evidence, "aggregate-exclusion-category"
            )
        )
        if not aggregate_match and not any(
            _is_authoritative(record)
            and record["claim"]["supported_values"].get("proposed_disposition")
            == disposition
            and record["claim"]["supported_values"].get("exclusion_category")
            == category
            for record in matching_individual
        ):
            raise ValueError(
                "asserted exclusion requires claim-specific authoritative evidence"
            )
    elif disposition == "retain":
        if (
            status == "unresolved"
            or assertion["evidence_basis"] == ["no-evidence-yet"]
            or category != "none"
            or reason is not None
        ):
            raise ValueError("retained disposition requires a resolved evidence basis")
        if not any(
            _is_authoritative(record)
            and record["claim"]["supported_values"] == {
                "proposed_disposition": "retain",
                "exclusion_category": "none",
                "exclusion_reason": None,
            }
            for record in matching_individual
        ):
            raise ValueError(
                "retained disposition requires exact authoritative individual-record evidence"
            )
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


def _validate_target(
    target: Any, evidence: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    expected_targets = {
        "simpler-bilinear-realisation": 8,
        "zobel-four-element": 4,
        "zobel-five-element-series-parallel": 20,
        "other-canonical-exclusion": 8,
    }
    _validate_object_shape(target, "annotation target", TARGET_FIELDS)
    expected = {
        "source_population": 148,
        "reported_members": 108,
        "reported_exclusions": 40,
        "exclusion_category_targets": expected_targets,
    }
    numeric_fields = {"source_population", "reported_members", "reported_exclusions"}
    if any(not _is_int(target.get(field)) or target[field] <= 0 for field in numeric_fields):
        raise ValueError("annotation target counts must be positive integers")
    category_targets = target.get("exclusion_category_targets")
    if not isinstance(category_targets, dict) or any(
        not _is_int(value) or value <= 0 for value in category_targets.values()
    ):
        raise ValueError("annotation category targets must be positive integers")
    if any(target.get(field) != value for field, value in expected.items()):
        raise ValueError("annotation target values differ from the comparison contract")
    ids = target.get("evidence_record_ids")
    _require_references(ids, "target evidence_record_ids", evidence)
    catalogue_claim = {
        "source_population": 148,
        "reported_members": 108,
        "reported_exclusions": 40,
    }
    if not any(
        _is_authoritative(record)
        and record["claim"]["supported_values"] == catalogue_claim
        for record in _matching_evidence(ids, evidence, "catalogue-target")
    ):
        raise ValueError("target requires matching authoritative aggregate evidence")
    if not any(
        _is_authoritative(record)
        and record["claim"]["supported_values"]["exclusion_category_targets"]
        == expected_targets
        for record in _matching_evidence(ids, evidence, "exclusion-category-targets")
    ):
        raise ValueError("target requires matching authoritative category-target evidence")
    return {**expected, "evidence_record_ids": list(ids), "reproduction_claimed": False}


def _validate_exclusion_counts(
    rows: list[dict[str, Any]],
    target: dict[str, Any],
    mapped_total: int,
    mapped_categories: Counter[str],
) -> None:
    exclusion_rows = [row for row in rows if row["proposed_disposition"] == "exclude"]
    if mapped_total != len(exclusion_rows):
        raise ValueError("mapped exclusion total disagrees with exclusion rows")
    if mapped_total > target["reported_exclusions"]:
        raise ValueError("mapped exclusions exceed reported exclusion target")
    if sum(mapped_categories.values()) != mapped_total:
        raise ValueError("mapped exclusion categories disagree with total exclusions")
    for row in rows:
        category = row["exclusion_category"]
        excluded = row["proposed_disposition"] == "exclude"
        if excluded and category in {"none", "unresolved"}:
            raise ValueError("excluded row lacks a mapped exclusion category")
        if not excluded and category not in {"none", "unresolved"}:
            raise ValueError("non-exclusion row contributes to a mapped category")
    for category, count in mapped_categories.items():
        category_target = target["exclusion_category_targets"].get(category)
        if category_target is None or count > category_target:
            raise ValueError(f"mapped {category} exclusions exceed category target")


def _validate_disposition_partition(
    rows: list[dict[str, Any]], target: dict[str, Any], dispositions: Counter[str]
) -> None:
    recomputed = Counter(row["proposed_disposition"] for row in rows)
    if dispositions != recomputed:
        raise ValueError("disposition counters disagree with generated rows")
    partition = sum(dispositions[value] for value in DISPOSITIONS)
    if partition != len(rows) or len(rows) != 148:
        raise ValueError("disposition partition must total 148 rows")
    if dispositions["retain"] > target["reported_members"]:
        raise ValueError("retained rows exceed reported membership target")


def _validate_generated_ledger(
    ledger: dict[str, Any], source_records: list[dict[str, Any]]
) -> None:
    rows = ledger["records"]
    if len(rows) != 148 or len({row["catalogue_id"] for row in rows}) != 148:
        raise ValueError("generated ledger must contain 148 unique catalogue IDs")
    for row, source in zip(rows, source_records, strict=True):
        if any(row[field] != source[field] for field in IMMUTABLE_FIELDS):
            raise ValueError("generated rows must preserve source order and immutable fields")
    globally_assigned: dict[tuple[str, Any], str] = {}
    for row in rows:
        for identifier in row["historical_identifiers"]:
            scheme = identifier["scheme"]
            if scheme in REUSABLE_HISTORICAL_IDENTIFIER_SCHEMES:
                continue
            if scheme not in GLOBALLY_UNIQUE_HISTORICAL_IDENTIFIER_SCHEMES:
                raise ValueError(
                    "historical identifier scheme lacks uniqueness policy: "
                    f"{scheme}"
                )
            identity = (scheme, identifier["value"])
            previous_catalogue_id = globally_assigned.get(identity)
            if previous_catalogue_id is not None:
                raise ValueError(
                    f"globally unique historical identifier {scheme} "
                    f"{identifier['value']!r} is assigned to both "
                    f"{previous_catalogue_id} and {row['catalogue_id']}"
                )
            globally_assigned[identity] = row["catalogue_id"]
    if ledger["source_catalogue_relation"] != SOURCE_CATALOGUE_RELATION:
        raise ValueError("generated ledger has unexpected structural relation")
    if ledger["target"]["reproduction_claimed"] and any(
        row["proposed_disposition"] == "unresolved" for row in rows
    ):
        raise ValueError("reproduction cannot be claimed while rows remain unresolved")
    statuses = Counter(row["comparison_status"] for row in rows)
    dispositions = Counter(row["proposed_disposition"] for row in rows)
    categories = Counter(row["exclusion_category"] for row in rows)
    expected_summary = {
        "total_rows": len(rows),
        "by_comparison_status": dict(sorted(statuses.items())),
        "by_proposed_disposition": dict(sorted(dispositions.items())),
        "by_exclusion_category": dict(sorted(categories.items())),
        "mapped_exclusions": dispositions["exclude"],
        "unresolved_dispositions": dispositions["unresolved"],
    }
    if ledger["summary"] != expected_summary:
        raise ValueError("generated summary disagrees with records")
    _validate_no_unstable_metadata(ledger, "generated ledger")


def generate_evidence_ledger(
    catalogue: dict[str, Any], annotations: dict[str, Any]
) -> dict[str, Any]:
    """Validate annotations and join them to the committed 148 records."""

    _validate_no_unstable_metadata(annotations)
    _validate_object_shape(annotations, "annotations", ANNOTATION_FIELDS)
    if catalogue.get("object") != "ladenheim-structural-148-catalogue":
        raise ValueError("unexpected structural catalogue object")
    relation = catalogue.get("relation")
    if (
        not isinstance(relation, dict)
        or relation.get("name") != SOURCE_CATALOGUE_RELATION
    ):
        raise ValueError(
            f"structural catalogue relation must be {SOURCE_CATALOGUE_RELATION}"
        )
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
    evidence = _validate_evidence_records(
        annotations.get("evidence_records"), sources, set(ids)
    )
    workspace = _validate_workspace_records(annotations.get("previous_workspace_records"), sources)
    computations = _validate_computational_cross_checks(annotations.get("computational_cross_checks"))
    namespaces = [set(sources), set(evidence), set(workspace), set(computations)]
    if sum(len(items) for items in namespaces) != len(set().union(*namespaces)):
        raise ValueError("record IDs must occupy separate namespaces")
    target = _validate_target(annotations.get("target"), evidence)

    explicit: dict[str, dict[str, Any]] = {}
    annotation_records = annotations.get("records")
    if not isinstance(annotation_records, list):
        raise ValueError("annotation records must be a list")
    source_by_id = {row["catalogue_id"]: row for row in records}
    for annotation in annotation_records:
        _validate_object_shape(
            annotation, "annotation record", set(ASSERTION_FIELDS) | {"catalogue_id"},
            {"structural_assertions"},
        )
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
        _validate_assertion(
            assertion, evidence, workspace, computations, catalogue_id=catalogue_id
        )
        explicit[catalogue_id] = assertion

    resolved = dict(explicit)
    rules = annotations.get("rules")
    if not isinstance(rules, list):
        raise ValueError("annotation rules must be a list")
    rule_ids: set[str] = set()
    for rule in rules:
        _validate_object_shape(rule, "annotation rule", RULE_FIELDS)
        rule_id = rule.get("rule_id")
        if not isinstance(rule_id, str) or not rule_id:
            raise ValueError("each annotation rule requires rule_id")
        if rule_id in rule_ids:
            raise ValueError(f"duplicate rule_id: {rule_id}")
        rule_ids.add(rule_id)
        if rule.get("kind") != "unique-component-match":
            raise ValueError("unsupported annotation rule")
        selector = rule.get("selector")
        if not _is_structural_selector(selector):
            raise ValueError("invalid unique-component-match selector")
        expected_match_count = rule.get("expected_matches")
        if not _is_int(expected_match_count) or expected_match_count <= 0:
            raise ValueError("invalid unique-component-match expected_matches")
        matches = [
            row for row in records
            if all(row[field] == value for field, value in selector.items())
        ]
        if len(matches) != expected_match_count:
            raise ValueError("unique-component-match count differs from expectation")
        if any(row["catalogue_id"] in resolved for row in matches):
            raise ValueError("annotation rule overlaps another assertion")
        assertion = {key: rule.get(key) for key in ASSERTION_FIELDS}
        _validate_assertion(
            assertion,
            evidence,
            workspace,
            computations,
            rule_selector=selector,
            expected_matches=expected_match_count,
        )
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
    mapped_categories = Counter(
        row["exclusion_category"]
        for row in ledger_rows
        if row["proposed_disposition"] == "exclude"
    )
    _validate_exclusion_counts(
        ledger_rows, target, dispositions["exclude"], mapped_categories
    )
    _validate_disposition_partition(ledger_rows, target, dispositions)
    ledger = {
        "format_version": FORMAT_VERSION,
        "object": "ladenheim-148-to-108-evidence-ledger",
        "source_catalogue": "data/counts/ladenheim-148.json",
        "source_catalogue_relation": SOURCE_CATALOGUE_RELATION,
        "target": target,
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
    _validate_generated_ledger(ledger, records)
    return ledger


def load_and_generate(catalogue_path: Path, annotation_path: Path) -> dict[str, Any]:
    catalogue = json.loads(catalogue_path.read_text(encoding="utf-8"))
    annotations = json.loads(annotation_path.read_text(encoding="utf-8"))
    return generate_evidence_ledger(catalogue, annotations)


def ledger_json(catalogue_path: Path, annotation_path: Path) -> str:
    return json.dumps(
        load_and_generate(catalogue_path, annotation_path), indent=2, sort_keys=True
    ) + "\n"

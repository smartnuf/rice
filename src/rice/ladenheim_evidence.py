"""Evidence-ledger contract for the structural 148 to canonical 108 comparison."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from typing import Any


FORMAT_VERSION = 1
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
    "source_references",
    "historical_identifiers",
    "confidence",
    "notes",
    "open_questions",
)


def _require_string_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise ValueError(f"{field} must be a list of non-empty strings")


def _validate_sources(sources: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(sources, list):
        raise ValueError("sources must be a list")
    result: dict[str, dict[str, Any]] = {}
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("each source must be an object")
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id:
            raise ValueError("each source requires source_id")
        if source_id in result:
            raise ValueError(f"duplicate source_id: {source_id}")
        for field in ("citation", "locator", "summary"):
            if not isinstance(source.get(field), str) or not source[field]:
                raise ValueError(f"source {source_id} requires non-empty {field}")
        result[source_id] = source
    return result


def _validate_assertion(
    assertion: dict[str, Any], sources: dict[str, dict[str, Any]]
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
    _require_string_list(assertion["source_references"], "source_references")
    unknown_sources = set(assertion["source_references"]) - sources.keys()
    if unknown_sources:
        raise ValueError(f"unknown source references: {sorted(unknown_sources)}")
    if not isinstance(assertion["historical_identifiers"], list):
        raise ValueError("historical_identifiers must be a list")
    _require_string_list(assertion["notes"], "notes")
    _require_string_list(assertion["open_questions"], "open_questions")

    status = assertion["comparison_status"]
    disposition = assertion["proposed_disposition"]
    category = assertion["exclusion_category"]
    reason = assertion["exclusion_reason"]
    if status in {"source-backed", "derived-unique-match"}:
        if not assertion["source_references"]:
            raise ValueError(f"{status} assertion requires source evidence")
        if assertion["evidence_basis"] == ["no-evidence-yet"]:
            raise ValueError(f"{status} assertion requires an evidence basis")
    if disposition == "exclude":
        if category in {"none", "unresolved"} or not isinstance(reason, str) or not reason:
            raise ValueError("asserted exclusion requires category and reason")
        if not assertion["source_references"]:
            raise ValueError("asserted exclusion requires source evidence")
    elif category not in {"none", "unresolved"}:
        raise ValueError("non-exclusion cannot assert an exclusion category")


def _default_assertion() -> dict[str, Any]:
    return {
        "comparison_status": "unresolved",
        "proposed_disposition": "unresolved",
        "exclusion_category": "unresolved",
        "exclusion_reason": None,
        "evidence_basis": ["no-evidence-yet"],
        "source_references": [],
        "historical_identifiers": [],
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
        raise ValueError("unsupported annotation format_version")
    sources = _validate_sources(annotations.get("sources"))

    explicit: dict[str, dict[str, Any]] = {}
    annotation_records = annotations.get("records")
    if not isinstance(annotation_records, list):
        raise ValueError("annotation records must be a list")
    for annotation in annotation_records:
        if not isinstance(annotation, dict):
            raise ValueError("each annotation record must be an object")
        catalogue_id = annotation.get("catalogue_id")
        if catalogue_id in explicit:
            raise ValueError(f"duplicate annotation ID: {catalogue_id}")
        if catalogue_id not in ids:
            raise ValueError(f"unknown annotation ID: {catalogue_id}")
        structural = annotation.get("structural_assertions", {})
        source_row = records[ids.index(catalogue_id)]
        if not isinstance(structural, dict) or any(
            key not in IMMUTABLE_FIELDS for key in structural
        ):
            raise ValueError("invalid structural_assertions")
        for field, value in structural.items():
            if source_row[field] != value:
                raise ValueError(
                    f"annotation contradicts immutable {field} for {catalogue_id}"
                )
        assertion = {key: annotation.get(key) for key in ASSERTION_FIELDS}
        _validate_assertion(assertion, sources)
        explicit[catalogue_id] = assertion

    resolved = dict(explicit)
    rules = annotations.get("rules")
    if not isinstance(rules, list):
        raise ValueError("annotation rules must be a list")
    for rule in rules:
        if not isinstance(rule, dict) or rule.get("kind") != "unique-component-match":
            raise ValueError("unsupported annotation rule")
        selector = rule.get("selector")
        if not isinstance(selector, dict) or not selector or any(
            field not in {"r", "l", "c", "lc", "rlc"} for field in selector
        ):
            raise ValueError("invalid unique-component-match selector")
        matches = [
            row
            for row in records
            if all(row[field] == value for field, value in selector.items())
        ]
        if len(matches) != rule.get("expected_matches"):
            raise ValueError("unique-component-match count differs from expectation")
        if any(row["catalogue_id"] in resolved for row in matches):
            raise ValueError("annotation rule overlaps another assertion")
        assertion = {key: rule.get(key) for key in ASSERTION_FIELDS}
        _validate_assertion(assertion, sources)
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

#!/usr/bin/env python3
"""Write or check the deterministic Ladenheim 148-to-108 evidence ledger."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from rice.ladenheim_evidence import ledger_json  # noqa: E402


CATALOGUE = REPOSITORY_ROOT / "data" / "counts" / "ladenheim-148.json"
ANNOTATIONS = (
    REPOSITORY_ROOT / "data" / "comparisons" / "ladenheim-108-annotations.json"
)
OUTPUT = (
    REPOSITORY_ROOT / "data" / "comparisons" / "ladenheim-148-to-108.json"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail on ledger drift")
    mode.add_argument("--write", action="store_true", help="write the ledger")
    args = parser.parse_args()
    try:
        content = ledger_json(CATALOGUE, ANNOTATIONS)
    except (OSError, ValueError, KeyError) as error:
        print(f"invalid evidence inputs: {error}", file=sys.stderr)
        return 1
    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"wrote {OUTPUT.relative_to(REPOSITORY_ROOT)}")
        return 0
    if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
        print(
            f"generated artefact is stale: {OUTPUT.relative_to(REPOSITORY_ROOT)}",
            file=sys.stderr,
        )
        return 1
    print(f"verified {OUTPUT.relative_to(REPOSITORY_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

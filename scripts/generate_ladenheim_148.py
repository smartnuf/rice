#!/usr/bin/env python3
"""Write or check the deterministic Ladenheim structural catalogue."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from rice.ladenheim import catalogue_json  # noqa: E402


OUTPUT = REPOSITORY_ROOT / "data" / "counts" / "ladenheim-148.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check",
        action="store_true",
        help="fail if the committed JSON differs",
    )
    mode.add_argument(
        "--write", action="store_true", help="write the deterministic JSON"
    )
    args = parser.parse_args()
    content = catalogue_json()
    if args.write:
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"wrote {OUTPUT.relative_to(REPOSITORY_ROOT)}")
        return 0
    if not OUTPUT.exists():
        print(
            "missing generated artefact: "
            f"{OUTPUT.relative_to(REPOSITORY_ROOT)}",
            file=sys.stderr,
        )
        return 1
    if OUTPUT.read_text(encoding="utf-8") != content:
        print(
            "generated artefact is stale: "
            f"{OUTPUT.relative_to(REPOSITORY_ROOT)}",
            file=sys.stderr,
        )
        return 1
    print(f"verified {OUTPUT.relative_to(REPOSITORY_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

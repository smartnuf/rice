#!/usr/bin/env python3
"""Fail if a change set touches protected evidence paths without a declaration.

Protected paths are the production evidence artefacts: the golden
catalogues under ``data/`` and the files that assert or publish the
production totals. A pull request that modifies any of them must carry an
explicit declaration, either:

  * the ``evidence-change`` label on the pull request, or
  * a line in the pull request body of the form ``Evidence-Change: <reason>``
    with a non-empty reason.

Usage (as run by .github/workflows/evidence-guard.yml):

  evidence_guard.py --base <sha> --head <sha> \
      [--pr-body-file <path>] [--labels <comma-separated>]

Exit status 0 when no protected path changed, or when a declaration is
present; exit status 1 otherwise, with a report listing the offending
paths.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

# Paths whose modification constitutes an evidence change. Glob patterns
# are matched against repository-relative paths with fnmatch semantics.
#
# Boundary: the guard protects the canonical evidence contract — the
# committed data artefacts, the tests comparing committed data against
# deterministic regeneration, the census tests asserting production
# totals, and the normative documents publishing golden values as
# static text. Test assertions that recompute values live in CI are
# deliberately excluded: weakening one changes no published value, and
# shifting a value fails other protected checks. Evidence publications
# belong under docs/counts/ or docs/comparisons/, which are protected
# as classes; a PR introducing a publisher document elsewhere must add
# it to this list in the same PR. Other extensions are an operator
# decision (see issue 76).
PROTECTED_PATTERNS: tuple[str, ...] = (
    "data/counts/*",
    "data/comparisons/*",
    "docs/results.md",
    "docs/computation.md",
    "docs/support_graph_enumeration.md",
    "docs/python_api.md",
    "docs/counts/*",
    "docs/comparisons/*",
    "README.md",
    "tests/test_bundle_census.py",
    "tests/test_bundle_labelings.py",
    "tests/test_count_language.py",
    "tests/test_reduced_census.py",
    "tests/test_ladenheim.py",
    "tests/test_ladenheim_evidence.py",
)

DECLARATION_LABEL = "evidence-change"
DECLARATION_RE = re.compile(
    r"^[ \t]*Evidence-Change:[ \t]*(\S.*)$", re.MULTILINE
)


def changed_paths(base: str, head: str) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--name-only", "--no-renames", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return [line.strip() for line in out.splitlines() if line.strip()]


def protected_hits(paths: list[str]) -> list[str]:
    hits = []
    for path in paths:
        if any(fnmatch.fnmatch(path, pat) for pat in PROTECTED_PATTERNS):
            hits.append(path)
    return hits


def declaration_reason(body: str) -> str | None:
    match = DECLARATION_RE.search(body)
    return match.group(1).strip() if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--pr-body-file", default=None)
    parser.add_argument("--labels", default="")
    args = parser.parse_args()

    hits = protected_hits(changed_paths(args.base, args.head))
    if not hits:
        print("evidence-guard: no protected evidence paths changed.")
        return 0

    labels = {l.strip() for l in args.labels.split(",") if l.strip()}
    body = ""
    if args.pr_body_file:
        body = Path(args.pr_body_file).read_text(encoding="utf-8")
    reason = declaration_reason(body)

    print("evidence-guard: protected evidence paths changed:")
    for path in hits:
        print(f"  - {path}")

    if DECLARATION_LABEL in labels:
        print(
            "evidence-guard: declared via "
            f"'{DECLARATION_LABEL}' label; passing."
        )
        return 0
    if reason:
        print(
            f"evidence-guard: declared in PR body: {reason!r}; passing."
        )
        return 0

    print(
        "\nevidence-guard: FAIL. This change alters production"
        " evidence totals\n"
        "or golden catalogues without a declaration. To proceed, either add\n"
        f"the '{DECLARATION_LABEL}' label to the pull request, or add a line\n"
        "to the pull request description:\n\n"
        "    Evidence-Change: <one-line reason>\n",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

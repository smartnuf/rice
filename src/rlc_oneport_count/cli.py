"""Command line interface for rlc-oneport-count."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .core import count_networks, support_census


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rlc-oneport-count",
        description="Count small two-terminal RLC one-port network topology classes.",
    )
    subparsers = parser.add_subparsers(dest="command")

    count_parser = subparsers.add_parser("count", help="run the legacy component-bundle count")
    _add_count_arguments(count_parser)

    supports_parser = subparsers.add_parser("supports", help="run the phase-1 support graph census")
    supports_parser.add_argument("--max-edges", type=int, default=8, help="maximum support-edge count, default: 8")
    supports_parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="output format, default: markdown",
    )

    # Preserve the original no-subcommand interface for the legacy count.
    _add_count_arguments(parser)
    return parser


def _add_count_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--max-r", type=int, default=3, help="maximum number of resistors, default: 3")
    parser.add_argument(
        "--max-reactive",
        type=int,
        default=5,
        help="maximum total number of reactive elements, default: 5",
    )
    parser.add_argument(
        "--mode",
        choices=("lc", "generic"),
        default="lc",
        help="'lc' distinguishes L and C; 'generic' treats reactive elements as X",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="output format, default: markdown",
    )


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "supports":
        result = support_census(max_edges=args.max_edges)
        if args.format == "json":
            print(json.dumps(asdict(result), indent=2, sort_keys=True))
        else:
            print(f"Support census: max_edges <= {result.max_edges}")
            print("| Support edges | Basic connected unlabelled graphs | Unordered two-terminal labelings | Terminal-relevant two-terminal graphs |")
            print("|---:|---:|---:|---:|")
            for edge_count in range(1, result.max_edges + 1):
                print(
                    f"| {edge_count} | {result.basic_by_edges[edge_count]} | "
                    f"{result.terminal_labelings_by_edges[edge_count]} | "
                    f"{result.relevant_by_edges[edge_count]} |"
                )
            print(
                f"| Total | {result.basic_total} | {result.terminal_labelings_total} | "
                f"{result.relevant_total} |"
            )
        return 0

    result = count_networks(max_r=args.max_r, max_reactive=args.max_reactive, mode=args.mode)

    if args.format == "json":
        print(json.dumps(asdict(result), indent=2, sort_keys=True))
    else:
        reactive_label = "L+C" if args.mode == "lc" else "X"
        print(f"Mode: {args.mode}  (reactive column is {reactive_label})")
        print(f"Limits: R <= {args.max_r}, reactive <= {args.max_reactive}")
        print(f"Terminal-relevant two-terminal support graphs: {result.support_count}")
        print(f"Terminal-relevant support graphs by support-edge count: {result.support_count_by_edges}")
        print()
        print(result.as_markdown_table())
        print()
        print(f"Total: {result.total}")
        if args.max_r >= 3:
            print(f"Exactly R=3, reactive <= {args.max_reactive}: {result.exactly_r_total(3)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

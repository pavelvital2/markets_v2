"""Command-line skeleton for market-parser-v2.

Commands are offline and never invoke live marketplace collection.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from market_parser_v2.api import route_manifest
from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.contracts import synthetic_contract_row, validate_contract_rows
from market_parser_v2.core.export import create_export_skeleton
from market_parser_v2.core.registry import get_provider, resolve_marketplace
from market_parser_v2.core.run import new_run_id


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="market-parser-v2")
    subcommands = parser.add_subparsers(dest="command", required=True)

    subcommands.add_parser("providers", help="List registered provider ids.")
    subcommands.add_parser("api-routes", help="Print read-only API route skeleton.")

    plan = subcommands.add_parser("plan", help="Print an offline provider plan.")
    plan.add_argument("--marketplace", choices=["wb", "ozon", "all"], required=True)

    validate = subcommands.add_parser(
        "validate-synthetic",
        help="Validate one synthetic sanitized contract row.",
    )
    validate.add_argument("--marketplace", choices=["wb", "ozon"], required=True)

    export = subcommands.add_parser(
        "create-export-skeleton",
        help="Create analytics export layout with placeholder files.",
    )
    export.add_argument("--marketplace", choices=["wb", "ozon"], required=True)
    export.add_argument("--run-id", default=None)
    export.add_argument("--output-dir", type=Path, required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "providers":
        print(json.dumps({"providers": resolve_marketplace("all")}, sort_keys=True))
        return 0

    if args.command == "api-routes":
        print(json.dumps(route_manifest(), sort_keys=True))
        return 0

    if args.command == "plan":
        plans = [get_provider(provider_id).build_plan() for provider_id in resolve_marketplace(args.marketplace)]
        print(json.dumps({"plans": [plan.to_dict() for plan in plans]}, sort_keys=True))
        return 0

    if args.command == "validate-synthetic":
        row = synthetic_contract_row(source_system=args.marketplace, run_id=new_run_id())
        result = validate_contract_rows([row], source_system=args.marketplace)
        print(json.dumps(result.to_dict(), sort_keys=True))
        return 0 if result.ok else 1

    if args.command == "create-export-skeleton":
        config = ParserConfig.with_export_root(args.output_dir)
        export_result = create_export_skeleton(
            config=config,
            marketplace=args.marketplace,
            run_id=args.run_id or new_run_id(),
        )
        print(json.dumps(export_result.to_dict(), sort_keys=True))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())

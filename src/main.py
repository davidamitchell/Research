"""CLI entry point for research tooling."""

from __future__ import annotations

import argparse
import sys

from src.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="research",
        description="Research tracking and tooling",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command")

    # Placeholder: research sub-commands will be added in Epic 1
    subparsers.add_parser("research", help="Manage research items")

    # Placeholder: fetch sub-commands will be added in Epic 2
    subparsers.add_parser("fetch", help="Fetch content from sources")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    logger.info("command=%s", args.command)


if __name__ == "__main__":
    main()

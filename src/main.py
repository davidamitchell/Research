"""CLI entry point for research tooling."""

from __future__ import annotations

import argparse
import os
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

    # Epic 1 — research item management
    import src.research.cli as research_cli

    research_cli.register_subparser(subparsers)

    # Epic 2 — fetch sub-commands
    _register_fetch_subparser(subparsers)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    logger.info("command=%s", args.command)

    if args.command == "research":
        research_cli.dispatch(args)
    elif args.command == "fetch":
        _dispatch_fetch(args)


def _register_fetch_subparser(subparsers: argparse.Action) -> None:  # type: ignore[type-arg]
    """Register the `fetch` sub-command and its children."""
    fetch_parser: argparse.ArgumentParser = subparsers.add_parser(
        "fetch", help="Fetch content from sources"
    )
    fetch_sub = fetch_parser.add_subparsers(dest="fetch_command")

    yt = fetch_sub.add_parser("youtube", help="Fetch YouTube transcripts")
    group = yt.add_mutually_exclusive_group()
    group.add_argument("--channel", metavar="CHANNEL_ID", help="Fetch from a channel")
    group.add_argument("--video", metavar="VIDEO_URL", help="Fetch a single video")
    yt.add_argument(
        "--max-videos",
        type=int,
        default=5,
        metavar="N",
        help="Max videos to fetch per channel (default: 5)",
    )


def _dispatch_fetch(args: argparse.Namespace) -> None:
    """Dispatch parsed fetch args."""
    cmd = getattr(args, "fetch_command", None)
    if cmd == "youtube":
        _fetch_youtube(args)
    else:
        print("Usage: research fetch <youtube>", file=sys.stderr)
        sys.exit(1)


def _fetch_youtube(args: argparse.Namespace) -> None:
    """Run the YouTube fetcher and print results to stdout."""
    from src.fetchers.youtube import YouTubeFetcher
    from src.state import StateStore

    channel_id = getattr(args, "channel", None)
    video_url = getattr(args, "video", None)
    max_videos = getattr(args, "max_videos", 5)

    if not channel_id and not video_url:
        print("Provide --channel CHANNEL_ID or --video VIDEO_URL", file=sys.stderr)
        sys.exit(1)

    store = StateStore()

    fetcher = YouTubeFetcher(
        channel_id=channel_id,
        max_videos=max_videos,
        video_urls=[video_url] if video_url else [],
        api_key=os.environ.get("YOUTUBE_DATA_API"),
    )
    items = fetcher.fetch()
    if not items:
        print("No items fetched.", file=sys.stderr)
        sys.exit(1)

    new_count = 0
    for item in items:
        if store.is_processed(item.url):
            logger.info("Skipping already-processed: %s", item.url)
            print(f"[skip] {item.title} — already processed")
            continue
        store.record(item)
        new_count += 1
        print(f"=== {item.title} ===")
        print(f"URL: {item.url}")
        print()
        print(item.content)
        print()

    if new_count == 0:
        print("All items already processed — nothing new.", file=sys.stderr)


if __name__ == "__main__":
    main()

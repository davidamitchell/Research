#!/usr/bin/env python3
"""Migrate source display names in completed research items to canonical form.

Applies ``normalize_source_display_name`` from ``build_site`` to every
``[display](url)`` entry in the ``## Sources`` section of each completed item.

Usage::

    # Preview changes (default — no files modified)
    python scripts/migrate_source_display_names.py

    # Apply changes in-place
    python scripts/migrate_source_display_names.py --apply

    # Specify a different completed directory
    python scripts/migrate_source_display_names.py --completed-dir Research/completed

The script is idempotent: running it twice on already-canonical files produces
no changes on the second run.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup — allow running from repo root or scripts/ directly.
# ---------------------------------------------------------------------------

_SCRIPTS_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPTS_DIR.parent
sys.path.insert(0, str(_REPO_ROOT))

from scripts.build_site import normalize_source_display_name  # noqa: E402
from src.logger import get_logger  # noqa: E402

logger = get_logger(__name__)

# Matches a Markdown link: [display name](url)
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _migrate_file(path: Path, *, dry_run: bool) -> int:
    """Normalise source display names in *path*.

    Returns the number of lines changed.
    """
    text = path.read_text(encoding="utf-8")

    # Only process lines inside the ## Sources section.
    lines = text.splitlines(keepends=True)
    changed = 0
    in_sources = False
    result: list[str] = []

    for line in lines:
        stripped = line.strip()

        # Detect section boundaries.
        if stripped.startswith("## "):
            in_sources = stripped == "## Sources"
            result.append(line)
            continue

        if not in_sources:
            result.append(line)
            continue

        # Replace display names inside Markdown links on this line.
        def _repl(m: re.Match[str]) -> str:
            display, url = m.group(1), m.group(2)
            normalised = normalize_source_display_name(display)
            return f"[{normalised}]({url})"

        new_line, n = _LINK_RE.subn(_repl, line)
        # Count as changed only when the normalisation actually modified something.
        if new_line != line:
            changed += n
        result.append(new_line)

    if changed and not dry_run:
        path.write_text("".join(result), encoding="utf-8")

    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files. Without this flag the script runs in dry-run mode.",
    )
    parser.add_argument(
        "--completed-dir",
        default=str(_REPO_ROOT / "Research" / "completed"),
        help="Path to the completed research items directory.",
    )
    args = parser.parse_args()

    dry_run = not args.apply
    completed_dir = Path(args.completed_dir)

    if not completed_dir.is_dir():
        logger.error("completed-dir not found: %s", completed_dir)
        sys.exit(1)

    md_files = sorted(completed_dir.glob("*.md"))
    if not md_files:
        logger.info("No .md files found in %s", completed_dir)
        return

    mode_label = "DRY RUN" if dry_run else "APPLY"
    logger.info("[%s] Scanning %d files in %s", mode_label, len(md_files), completed_dir)

    total_files_changed = 0
    total_lines_changed = 0

    for path in md_files:
        if path.name == ".gitkeep":
            continue
        n = _migrate_file(path, dry_run=dry_run)
        if n:
            total_files_changed += 1
            total_lines_changed += n
            logger.info("%s  %d link(s) updated", path.name, n)

    if dry_run:
        logger.info(
            "[DRY RUN] Would update %d link(s) across %d file(s). "
            "Re-run with --apply to write changes.",
            total_lines_changed,
            total_files_changed,
        )
    else:
        logger.info(
            "[APPLY] Updated %d link(s) across %d file(s).",
            total_lines_changed,
            total_files_changed,
        )


if __name__ == "__main__":
    main()

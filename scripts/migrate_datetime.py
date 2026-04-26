"""Migrate research item front-matter dates to full ISO 8601 datetime strings.

For each research item that has a date-only value (``YYYY-MM-DD``) in the
``added``, ``started``, or ``completed`` fields, this script uses ``git log``
to find the commit that introduced or last changed that value, then replaces
the bare date with the commit's ISO 8601 datetime (UTC, with offset).

Usage::

    python scripts/migrate_datetime.py [--dry-run] [--verbose]

Options:
    --dry-run   Report what would change without writing any files.
    --verbose   Print per-file detail even for unchanged items.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
_RESEARCH_ROOT = _REPO_ROOT / "Research"

# YAML front-matter fields that should carry a full datetime.
_DATE_FIELDS = ("added", "started", "completed")

# Matches a date-only value: YYYY-MM-DD (not already a datetime).
_DATE_ONLY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------


def _git_log_for_file(rel_path: str) -> list[tuple[str, str]]:
    """Return ``[(commit_hash, iso_datetime), ...]`` for *rel_path*, oldest first.

    Uses ``--follow`` so renames across directories (backlog → in-progress →
    completed) are tracked.
    """
    result = subprocess.run(
        ["git", "log", "--follow", "--format=%H %ai", "--", rel_path],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    entries: list[tuple[str, str]] = []
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(" ", 1)
        if len(parts) == 2:
            entries.append((parts[0], parts[1].strip()))
    entries.reverse()  # chronological order (oldest first)
    return entries


def _git_file_at_commit(rel_path: str, commit_hash: str) -> str | None:
    """Return the file content at *commit_hash*, or ``None`` if absent."""
    result = subprocess.run(
        ["git", "show", f"{commit_hash}:{rel_path}"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
    )
    return result.stdout if result.returncode == 0 else None


def _parse_git_datetime(git_time: str) -> str:
    """Convert ``git log --format=%ai`` output to ISO 8601 with offset.

    ``%ai`` produces ``YYYY-MM-DD HH:MM:SS +HHMM``.  We normalise the offset
    to ``+HH:MM`` format expected by ISO 8601.
    """
    # e.g. "2026-04-26 08:03:43 +0000"
    parts = git_time.rsplit(" ", 1)  # split off offset
    dt_part = parts[0]  # "2026-04-26 08:03:43"
    offset_raw = parts[1] if len(parts) == 2 else "+0000"  # "+0000" or "-1200"
    # Normalise "+0000" → "+00:00"
    sign = offset_raw[0]
    hours = offset_raw[1:3]
    minutes = offset_raw[3:5]
    offset = f"{sign}{hours}:{minutes}"
    # Build ISO string: replace space with T
    return f"{dt_part.replace(' ', 'T')}{offset}"


# ---------------------------------------------------------------------------
# Front-matter helpers
# ---------------------------------------------------------------------------


def _get_field(text: str, key: str) -> str | None:
    """Return the raw string value of a YAML front-matter field."""
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    if match is None:
        return None
    val = match.group(1).strip()
    return val if val not in ("~", "null", "") else None


def _find_commit_when_field_set(
    rel_path: str, key: str, commit_log: list[tuple[str, str]]
) -> str | None:
    """Return the git timestamp of the first commit where *key* was non-null.

    Iterates over commits in chronological order (oldest first) and returns
    the timestamp of the earliest commit where the field held a non-null,
    non-tilde value.  Falls back to the oldest commit overall.
    """
    for commit_hash, commit_time in commit_log:
        content = _git_file_at_commit(rel_path, commit_hash)
        if content is None:
            continue
        val = _get_field(content, key)
        if val and _DATE_ONLY_RE.match(val):
            return commit_time
        if val and not _DATE_ONLY_RE.match(val) and val not in ("~", "null"):
            # Already a datetime in git history — return its time.
            return commit_time
    return commit_log[0][1] if commit_log else None


# ---------------------------------------------------------------------------
# Per-file migration
# ---------------------------------------------------------------------------


def _migrate_file(filepath: Path, *, dry_run: bool, verbose: bool) -> bool:
    """Migrate a single file.  Returns ``True`` if the file was (or would be) changed."""
    rel_path = str(filepath.relative_to(_REPO_ROOT))
    text = filepath.read_text(encoding="utf-8")

    # Collect fields that need updating
    needs_update: dict[str, str] = {}
    for key in _DATE_FIELDS:
        val = _get_field(text, key)
        if val and _DATE_ONLY_RE.match(val):
            needs_update[key] = val

    if not needs_update:
        if verbose:
            print(f"  skip  {rel_path}  (no date-only fields)")
        return False

    # Get commit log (may be slow for files with many commits)
    commit_log = _git_log_for_file(rel_path)
    if not commit_log:
        print(f"  WARN  {rel_path}  (no git history — skipping)", file=sys.stderr)
        return False

    updated_text = text
    changes: list[str] = []

    for key, current_date in needs_update.items():
        commit_time = _find_commit_when_field_set(rel_path, key, commit_log)
        if commit_time is None:
            commit_time = commit_log[-1][1]  # newest commit as fallback

        new_value = _parse_git_datetime(commit_time)
        # Replace the date-only value in the frontmatter line for this key.
        pattern = re.compile(rf"^({re.escape(key)}:\s*){re.escape(current_date)}$", re.MULTILINE)
        new_text = pattern.sub(rf"\g<1>{new_value}", updated_text, count=1)
        if new_text != updated_text:
            changes.append(f"{key}: {current_date!r} → {new_value!r}")
            updated_text = new_text

    if not changes:
        if verbose:
            print(f"  skip  {rel_path}  (regex replacement produced no change)")
        return False

    change_summary = ", ".join(changes)
    if dry_run:
        print(f"  [dry-run]  {rel_path}  {change_summary}")
    else:
        filepath.write_text(updated_text, encoding="utf-8")
        print(f"  updated  {rel_path}  {change_summary}")

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detail for skipped files too.",
    )
    args = parser.parse_args(argv)

    subdirs = ("backlog", "in-progress", "completed")
    files = [
        p
        for subdir in subdirs
        for p in sorted((_RESEARCH_ROOT / subdir).glob("*.md"))
        if p.name not in (".gitkeep", "README.md")
    ]

    updated = 0
    for filepath in files:
        if _migrate_file(filepath, dry_run=args.dry_run, verbose=args.verbose):
            updated += 1

    noun = "file" if updated == 1 else "files"
    action = "would update" if args.dry_run else "updated"
    print(f"\n{action} {updated} {noun} out of {len(files)} total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

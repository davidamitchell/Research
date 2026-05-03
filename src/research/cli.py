"""Research item CLI commands: add, list, start, draft, complete, pick."""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from src.logger import get_logger
from src.research.item import ResearchItem

logger = get_logger(__name__)

_RESEARCH_ROOT = Path(__file__).parent.parent.parent / "Research"

_TEMPLATE = """\
---
title: "{title}"
added: {added}
status: backlog
priority: medium
blocks: []
tags: []
started: ~
completed: ~
output: []
---

# {title}

## Research Question

State the specific, answerable question this research addresses.

## Scope

**In scope:**
-

**Out of scope:**
-

**Constraints:**

## Context

Why is this question worth answering now?

## Approach

1.
2.

## Sources

- [ ] Source 1

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type:
- Description:
- Links:
"""


def _git_add(repo_root: Path, *paths: Path) -> None:
    """Stage git changes for the given paths (additions and deletions).

    Calling ``git add`` on a deleted tracked file stages the deletion; calling
    it on a new untracked file stages the addition.  Both are needed when a
    file is moved between directories (old path deleted, new path written).

    Silently does nothing if git is unavailable or the directory is not a git
    repository -- the commands that call this function work correctly without
    git staging, just as they did before this helper existed.
    """
    if not paths:
        return
    try:
        rel_paths = [str(p.relative_to(repo_root)) for p in paths]
        subprocess.run(
            ["git", "add", "--", *rel_paths],
            cwd=str(repo_root),
            capture_output=True,
            check=False,
        )
    except (FileNotFoundError, OSError, ValueError):
        pass


def _slug(title: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]  # cap length


def _research_root(override: Path | None = None) -> Path:
    return override if override is not None else _RESEARCH_ROOT


def _now_iso() -> str:
    """Return the current UTC datetime as an ISO 8601 string with seconds precision."""
    return datetime.now(UTC).isoformat(timespec="seconds")


def cmd_add(title: str, research_root: Path | None = None) -> Path:
    """Create a new research item in backlog and return its path."""
    root = _research_root(research_root)
    now = _now_iso()
    date_prefix = now[:10]  # YYYY-MM-DD for filename
    filename = f"{date_prefix}-{_slug(title)}.md"
    dest = root / "backlog" / filename

    if dest.exists():
        logger.warning("File already exists: %s", dest)
        print(f"Already exists: {dest}", file=sys.stderr)
        return dest

    content = _TEMPLATE.format(title=title, added=now)
    dest.write_text(content, encoding="utf-8")
    logger.info("Created research item: %s", dest)
    print(f"Created: {dest}")
    return dest


def cmd_list(research_root: Path | None = None) -> list[ResearchItem]:
    """List all backlog and in-progress research items."""
    root = _research_root(research_root)
    items: list[ResearchItem] = []
    for subdir in ("backlog", "in-progress"):
        for path in sorted((root / subdir).glob("*.md")):
            try:
                items.append(ResearchItem.from_file(path))
            except (ValueError, OSError) as exc:
                logger.warning("Skipping %s: %s", path.name, exc)

    for item in items:
        print(f"[{item.status}] {item.title}  ({item.path.name})")

    return items


def cmd_start(filename: str, research_root: Path | None = None) -> Path:
    """Move a backlog item to in-progress and update its status."""
    root = _research_root(research_root)
    src = root / "backlog" / filename
    if not src.exists():
        print(f"Not found in backlog: {filename}", file=sys.stderr)
        sys.exit(1)

    dest = root / "in-progress" / filename
    text = src.read_text(encoding="utf-8")
    text = _set_frontmatter_field(text, "status", "in-progress")
    text = _set_frontmatter_field(text, "started", _now_iso())
    dest.write_text(text, encoding="utf-8")
    src.unlink()
    _git_add(root.parent, src, dest)
    logger.info("Started: %s -> %s", src, dest)
    print(f"Started: {dest}")
    return dest


def cmd_draft(filename: str, research_root: Path | None = None) -> Path:
    """Mark an in-progress item as reviewing (status update only, no file move)."""
    root = _research_root(research_root)
    path = root / "in-progress" / filename
    if not path.exists():
        print(f"Not found in in-progress: {filename}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    text = _set_frontmatter_field(text, "status", "reviewing")
    path.write_text(text, encoding="utf-8")
    logger.info("Draft (reviewing): %s", path)
    print(f"Reviewing: {path}")
    return path


def cmd_complete(filename: str, research_root: Path | None = None) -> Path:
    """Move an in-progress item to completed and update its status."""
    root = _research_root(research_root)
    src = root / "in-progress" / filename
    if not src.exists():
        print(f"Not found in in-progress: {filename}", file=sys.stderr)
        sys.exit(1)

    text = src.read_text(encoding="utf-8")
    current_status = _get_frontmatter_field(text, "status")
    if current_status != "reviewing":
        msg = (
            f"Warning: completing item with status '{current_status}' "
            "(expected 'reviewing'). Proceeding anyway."
        )
        print(msg, file=sys.stderr)
        logger.warning(msg)

    dest = root / "completed" / filename
    text = _set_frontmatter_field(text, "status", "completed")
    text = _set_frontmatter_field(text, "completed", _now_iso())
    dest.write_text(text, encoding="utf-8")
    src.unlink()
    _git_add(root.parent, src, dest)
    logger.info("Completed: %s -> %s", src, dest)
    print(f"Completed: {dest}")
    return dest


def cmd_pick(research_root: Path | None = None) -> None:
    """Select the next research item and print its JSON context to stdout.

    Applies the same priority rules as the research prompt:
      1. In-progress items take priority over backlog (oldest first).
      2. Backlog: high > medium > low priority.
      3. Tie-break: non-empty ``blocks`` list first.
      4. Final tie-break: oldest filename (earliest date).

    Outputs a JSON object with keys:
      filename      -- basename of the selected file
      path          -- repo-relative path the agent should use (always the
                       in-progress location, even for backlog items, because
                       the workflow calls ``research start`` before the session)
      status        -- current status from frontmatter
      review_count  -- integer review_count from frontmatter (0 if absent)
      context_block -- formatted markdown for {{ITEM_CONTEXT}} substitution

    Prints ``{}`` and exits 0 if no work is available.
    """
    import json as _json

    root = _research_root(research_root)

    # In-progress items always take priority -- resume oldest first.
    in_prog_files = sorted(p for p in (root / "in-progress").glob("*.md") if p.name != "README.md")
    if in_prog_files:
        path = in_prog_files[0]
        item = ResearchItem.from_file(path)
        print(_json.dumps(_pick_context(item, path, root)))
        return

    # Select highest-priority backlog item.
    backlog: list[ResearchItem] = []
    for p in sorted((root / "backlog").glob("*.md")):
        if p.name == "README.md":
            continue
        try:
            backlog.append(ResearchItem.from_file(p))
        except (ValueError, OSError) as exc:
            logger.warning("Skipping %s: %s", p.name, exc)

    if not backlog:
        print(_json.dumps({}))
        return

    # Build set of completed slugs for dependency gating.
    completed_slugs: set[str] = {
        p.stem for p in (root / "completed").glob("*.md") if p.name != "README.md"
    }

    eligible = [item for item in backlog if all(dep in completed_slugs for dep in item.depends_on)]

    if not eligible:
        logger.warning("All backlog items have unsatisfied depends_on dependencies.")
        print(_json.dumps({}))
        return

    _prio = {"high": 0, "medium": 1, "low": 2}
    eligible.sort(
        key=lambda i: (
            _prio.get(i.priority, 1),
            0 if i.blocks else 1,  # non-empty blocks list comes first
            i.path.name,  # oldest filename (YYYY-MM-DD prefix) first
        )
    )
    item = eligible[0]
    print(_json.dumps(_pick_context(item, item.path, root)))


def _pick_context(item: ResearchItem, path: Path, root: Path) -> dict:  # type: ignore[type-arg]
    """Build the JSON context dict for the selected item.

    ``root`` is the Research directory (e.g. ``<repo>/Research``).
    The repo root is ``root.parent``.
    """
    text = path.read_text(encoding="utf-8")
    rc_val = _get_frontmatter_field(text, "review_count")
    review_count = int(rc_val) if rc_val and rc_val.isdigit() else 0

    status = item.status

    # For backlog items the workflow calls `research start` before the Copilot
    # session, which moves the file to in-progress.  Show the post-start path
    # so the agent uses the right location from the outset.
    if status == "backlog":
        display_path = f"Research/in-progress/{path.name}"
    else:
        try:
            display_path = str(path.relative_to(root.parent))
        except ValueError:
            display_path = str(path)

    # Determine where the agent should resume (references the new prompt step
    # numbers: Step 1 = Read, Step 2 = Research, Step 7 = Draft+Review,
    # Step 8 = Handle review, Step 9 = Complete).
    if status == "backlog":
        action = (
            "Begin at **Step 1** — the item has been moved to `in-progress`. "
            "Read it in full, then start research from \u00a7\u00a70 in Step 2."
        )
    elif status == "in-progress":
        action = (
            "Begin at **Step 1** — read the item in full. It is already "
            "`in-progress`; check the \u00a7\u00a70\u2013\u00a7\u00a77 sections for "
            "existing work and resume from where it left off in Step 2, "
            "or restart from \u00a7\u00a70 if they are empty."
        )
    elif status == "reviewing":
        if review_count == 0:
            action = (
                "Begin at **Step 7** — status is `reviewing` but `review_count` "
                "is 0. The review workflow was not triggered. Trigger it now."
            )
        elif review_count == 1:
            action = (
                "Begin at **Step 8** — one review pass has run. Check the latest "
                "review workflow log for `OVERALL` result. If `PASS`, proceed to "
                "Step 9. If `FAIL`, fix violations and re-trigger."
            )
        else:
            action = (
                f"Begin at **Step 9** — `review_count` is {review_count} (≥ 2), "
                f"auto-passes. Run `python -m src.main research complete "
                f"{path.name}` and proceed with Steps 10\u201312."
            )
    else:
        action = (
            "Begin at **Step 1** — unrecognised status, treat as in-progress. "
            "Read the item, then resume or restart research in Step 2."
        )

    context_block = (
        f"**Item:** `{display_path}`  \n"
        f"**Status:** `{status}`  \n"
        f"**Review count:** {review_count}  \n"
        f"**Action:** {action}"
    )

    return {
        "filename": path.name,
        "path": display_path,
        "status": status,
        "review_count": review_count,
        "context_block": context_block,
    }


def _set_frontmatter_field(text: str, key: str, value: str) -> str:
    """Update a single YAML front-matter field value in-place."""
    pattern = re.compile(rf"^({re.escape(key)}:\s*)(.*)$", re.MULTILINE)
    replacement = rf"\g<1>{value}"
    updated, n = pattern.subn(replacement, text, count=1)
    if n == 0:
        logger.warning("Field '%s' not found in front matter", key)
    return updated


def _get_frontmatter_field(text: str, key: str) -> str | None:
    """Return the value of a single YAML front-matter field, or None if absent."""
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*)$", re.MULTILINE)
    match = pattern.search(text)
    if match is None:
        return None
    value = match.group(1).strip()
    return value if value else None


def register_subparser(subparsers: object) -> None:  # type: ignore[type-arg]
    """Attach the `research` sub-command and its children to *subparsers*."""
    import argparse

    parser: argparse.ArgumentParser = subparsers.add_parser(
        "research", help="Manage research items"
    )
    sub = parser.add_subparsers(dest="research_command")

    # add
    add_p = sub.add_parser("add", help="Create a new research item in backlog")
    add_p.add_argument("title", help="Title of the new research item")

    # list
    sub.add_parser("list", help="List backlog and in-progress research items")

    # start
    start_p = sub.add_parser("start", help="Move a backlog item to in-progress")
    start_p.add_argument("filename", help="Filename of the research item to start")

    # draft
    draft_p = sub.add_parser("draft", help="Mark an in-progress item as ready for review")
    draft_p.add_argument("filename", help="Filename of the research item to mark for review")

    # complete
    complete_p = sub.add_parser("complete", help="Move an in-progress item to completed")
    complete_p.add_argument("filename", help="Filename of the research item to complete")

    # pick
    sub.add_parser(
        "pick",
        help=(
            "Select the next item to work on and print JSON context for prompt "
            "injection. Prints {} if no work is available."
        ),
    )


def dispatch(args: object) -> None:  # type: ignore[type-arg]
    """Dispatch parsed args to the appropriate research command."""
    import argparse

    a: argparse.Namespace = args  # type: ignore[assignment]
    cmd = getattr(a, "research_command", None)
    if cmd == "add":
        cmd_add(a.title)
    elif cmd == "list":
        cmd_list()
    elif cmd == "start":
        cmd_start(a.filename)
    elif cmd == "draft":
        cmd_draft(a.filename)
    elif cmd == "complete":
        cmd_complete(a.filename)
    elif cmd == "pick":
        cmd_pick()
    else:
        print("Usage: research research <add|list|start|draft|complete|pick>", file=sys.stderr)
        sys.exit(1)

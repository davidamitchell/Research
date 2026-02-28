"""Research item CLI commands: add, list, start, complete."""

from __future__ import annotations

import re
import sys
from datetime import date
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


def _slug(title: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]  # cap length


def _research_root(override: Path | None = None) -> Path:
    return override if override is not None else _RESEARCH_ROOT


def cmd_add(title: str, research_root: Path | None = None) -> Path:
    """Create a new research item in backlog and return its path."""
    root = _research_root(research_root)
    today = date.today().isoformat()
    filename = f"{today}-{_slug(title)}.md"
    dest = root / "backlog" / filename

    if dest.exists():
        logger.warning("File already exists: %s", dest)
        print(f"Already exists: {dest}", file=sys.stderr)
        return dest

    content = _TEMPLATE.format(title=title, added=today)
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
    text = _set_frontmatter_field(text, "started", date.today().isoformat())
    dest.write_text(text, encoding="utf-8")
    src.unlink()
    logger.info("Started: %s -> %s", src, dest)
    print(f"Started: {dest}")
    return dest


def cmd_complete(filename: str, research_root: Path | None = None) -> Path:
    """Move an in-progress item to completed and update its status."""
    root = _research_root(research_root)
    src = root / "in-progress" / filename
    if not src.exists():
        print(f"Not found in in-progress: {filename}", file=sys.stderr)
        sys.exit(1)

    dest = root / "completed" / filename
    text = src.read_text(encoding="utf-8")
    text = _set_frontmatter_field(text, "status", "completed")
    text = _set_frontmatter_field(text, "completed", date.today().isoformat())
    dest.write_text(text, encoding="utf-8")
    src.unlink()
    logger.info("Completed: %s -> %s", src, dest)
    print(f"Completed: {dest}")
    return dest


def _set_frontmatter_field(text: str, key: str, value: str) -> str:
    """Update a single YAML front-matter field value in-place."""
    pattern = re.compile(rf"^({re.escape(key)}:\s*)(.*)$", re.MULTILINE)
    replacement = rf"\g<1>{value}"
    updated, n = pattern.subn(replacement, text, count=1)
    if n == 0:
        logger.warning("Field '%s' not found in front matter", key)
    return updated


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

    # complete
    complete_p = sub.add_parser("complete", help="Move an in-progress item to completed")
    complete_p.add_argument("filename", help="Filename of the research item to complete")


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
    elif cmd == "complete":
        cmd_complete(a.filename)
    else:
        print("Usage: research research <add|list|start|complete>", file=sys.stderr)
        sys.exit(1)

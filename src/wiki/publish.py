"""Publish completed research items to the GitHub wiki.

Usage (run from repository root):
    python -m src.wiki.publish <completed_dir> <wiki_dir>

Arguments:
    completed_dir  Path to Research/completed/ directory.
    wiki_dir       Path to a checked-out wiki repository directory.

The script performs a full rebuild:
  - Reads every *.md file in completed_dir (excluding README.md).
  - Strips YAML front-matter and writes a wiki page per item.
  - Generates Home.md (date-sorted index table).
  - Generates _Sidebar.md (tag-grouped navigation).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

# ---------------------------------------------------------------------------
# Front-matter helpers
# ---------------------------------------------------------------------------


def load_frontmatter(text: str) -> dict[str, Any]:
    """Extract and parse YAML front-matter from Markdown text.

    Returns an empty dict if no front-matter block is found.
    """
    match = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        result = yaml.safe_load(match.group(1))
        return result if isinstance(result, dict) else {}
    except yaml.YAMLError:
        return {}


def strip_frontmatter(text: str) -> str:
    """Remove the YAML front-matter block from the beginning of text.

    Returns the text unchanged if no front-matter block is found.
    """
    match = re.match(r"^---\n.+?\n---\n*", text, re.DOTALL)
    if match:
        return text[match.end() :]
    return text


# ---------------------------------------------------------------------------
# Page name
# ---------------------------------------------------------------------------


def page_name(filename: str) -> str:
    """Derive the wiki page name from a research item filename.

    Strips the .md extension; keeps the date-prefixed slug as-is since
    all characters are URL-safe for the GitHub wiki.
    """
    return Path(filename).stem


# ---------------------------------------------------------------------------
# Wiki link helpers
# ---------------------------------------------------------------------------


def wiki_link(page: str, title: str, *, in_table: bool = False) -> str:
    """Format a GitHub wiki internal link.

    GitHub wiki links use ``[[Page-Name|Display Text]]`` syntax.  When the
    link appears inside a Markdown table cell the pipe must be written as
    ``\\|`` so that it is not treated as a column delimiter.

    Args:
        page:     Wiki page name (filename without .md).
        title:    Display text shown to the reader.
        in_table: Pass True when the link is inside a Markdown table cell.
    """
    sep = "\\|" if in_table else "|"
    return f"[[{page}{sep}{title}]]"


# ---------------------------------------------------------------------------
# Index and sidebar generators
# ---------------------------------------------------------------------------


def generate_home(items: list[dict[str, Any]]) -> str:
    """Generate Home.md — date-sorted index of all completed items."""
    sorted_items = sorted(items, key=lambda x: str(x.get("added", "")), reverse=True)
    lines = [
        "# Research Index",
        "",
        "Completed research items, most recent first.",
        "",
        "| Date | Title | Tags |",
        "|------|-------|------|",
    ]
    for item in sorted_items:
        date = item.get("added", "")
        title = item.get("title", item["page_name"])
        pname = item["page_name"]
        tags = ", ".join(item.get("tags") or [])
        link = wiki_link(pname, title, in_table=True)
        lines.append(f"| {date} | {link} | {tags} |")
    lines.append("")
    return "\n".join(lines)


def generate_sidebar(items: list[dict[str, Any]]) -> str:
    """Generate _Sidebar.md — tag-grouped navigation."""
    # Build tag → items map
    tag_map: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        for tag in item.get("tags") or []:
            tag_map.setdefault(tag, []).append(item)

    lines = [
        "**Navigation**",
        "",
        "[[Home]]",
        "",
        "**By Tag**",
        "",
    ]
    for tag in sorted(tag_map.keys()):
        lines.append(f"**{tag}**")
        tag_items = sorted(tag_map[tag], key=lambda x: str(x.get("added", "")), reverse=True)
        for item in tag_items:
            pname = item["page_name"]
            title = item.get("title", pname)
            lines.append(f"- {wiki_link(pname, title)}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main publish function
# ---------------------------------------------------------------------------


def publish(completed_dir: Path, wiki_dir: Path) -> list[str]:
    """Publish all completed research items to wiki_dir.

    Returns a list of wiki page filenames that were written.
    """
    wiki_dir.mkdir(parents=True, exist_ok=True)

    # Remove existing .md files from the wiki (full rebuild)
    for existing in wiki_dir.glob("*.md"):
        existing.unlink()

    items: list[dict[str, Any]] = []
    written: list[str] = []

    for md_file in sorted(completed_dir.glob("*.md")):
        if md_file.name == "README.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta = load_frontmatter(text)
        body = strip_frontmatter(text)
        pname = page_name(md_file.name)

        items.append(
            {
                "page_name": pname,
                "title": meta.get("title", pname),
                "added": str(meta.get("added", "")),
                "tags": meta.get("tags") or [],
            }
        )

        wiki_page = wiki_dir / f"{pname}.md"
        wiki_page.write_text(body, encoding="utf-8")
        written.append(wiki_page.name)

    # Write index and sidebar
    home = wiki_dir / "Home.md"
    home.write_text(generate_home(items), encoding="utf-8")
    written.append("Home.md")

    sidebar = wiki_dir / "_Sidebar.md"
    sidebar.write_text(generate_sidebar(items), encoding="utf-8")
    written.append("_Sidebar.md")

    return written


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    """Entry point: python -m src.wiki.publish <completed_dir> <wiki_dir>."""
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 2:
        print("Usage: python -m src.wiki.publish <completed_dir> <wiki_dir>", file=sys.stderr)
        return 1

    completed_dir = Path(args[0])
    wiki_dir = Path(args[1])

    if not completed_dir.is_dir():
        print(f"Error: {completed_dir} is not a directory", file=sys.stderr)
        return 1

    written = publish(completed_dir, wiki_dir)
    for name in written:
        print(f"  wrote: {name}")
    print(f"Published {len(written) - 2} research items + Home.md + _Sidebar.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

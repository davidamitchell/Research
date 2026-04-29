"""Canonicalise tags across all research items.

Reads the canonical tag vocabulary from docs/tag-vocabulary.md and rewrites
the ``tags:`` frontmatter field in every research item under:

    Research/completed/
    Research/backlog/
    Research/in-progress/

Any tag that matches an alias in the vocabulary is replaced with its canonical
form. Canonical tags already in their canonical form are unchanged. Unknown
tags (not in the vocabulary as either a canonical or alias) are preserved as-is.

Duplicate tags introduced by canonicalisation (e.g. both ``ai`` and
``agentic-ai`` were present) are deduplicated while preserving order.

Usage:
    python scripts/canonicalise_tags.py [--root /path/to/repo] [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Vocabulary loading
# ---------------------------------------------------------------------------

_YAML_BLOCK_RE = re.compile(r"```yaml\n(.*?)```", re.DOTALL)

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "tag-vocabulary.md"


def load_vocabulary(vocab_path: Path = VOCAB_PATH) -> dict[str, str]:
    """Return a reverse map: alias -> canonical by parsing docs/tag-vocabulary.md.

    The vocabulary markdown file must contain exactly one fenced ``yaml`` code
    block.  The YAML inside that block maps each canonical tag to a list of
    aliases::

        canonical-tag:
          - alias1
          - alias2

    Returns a dict where every alias (and the canonical tag itself) maps to
    the canonical tag string.
    """
    text = vocab_path.read_text(encoding="utf-8")
    match = _YAML_BLOCK_RE.search(text)
    if not match:
        raise ValueError(f"No yaml code block found in {vocab_path}")

    yaml_text = match.group(1)
    alias_map: dict[str, str] = {}

    current_canonical: str | None = None
    for line in yaml_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # Top-level key: "canonical-tag:"
        if not line.startswith(" ") and not line.startswith("-") and stripped.endswith(":"):
            current_canonical = stripped[:-1]
            alias_map[current_canonical] = current_canonical
        # List item: "  - alias"
        elif stripped.startswith("- ") and current_canonical is not None:
            alias = stripped[2:].strip()
            if alias:
                alias_map[alias] = current_canonical

    return alias_map


# ---------------------------------------------------------------------------
# Frontmatter rewriting
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Matches inline-list tags line:   tags: [a, b, c]
_INLINE_TAGS_RE = re.compile(r"^(tags\s*:)\s*(\[.*?\])\s*$", re.MULTILINE)

# Matches block-list tags line: the "tags:" header followed by "  - item" lines
_BLOCK_TAGS_RE = re.compile(
    r"^(tags\s*:)\s*\n((?:[ \t]+-[ \t]+\S.*\n)+)",
    re.MULTILINE,
)


def _canonicalise_list(tags: list[str], alias_map: dict[str, str]) -> list[str]:
    """Return tags with aliases replaced by canonical forms, duplicates removed."""
    seen: set[str] = set()
    result: list[str] = []
    for tag in tags:
        canonical = alias_map.get(tag, tag)
        if canonical not in seen:
            seen.add(canonical)
            result.append(canonical)
    return result


def _parse_inline_list(raw: str) -> list[str]:
    """Parse an inline YAML list string ``[a, b, c]`` into a Python list."""
    inner = raw.strip()[1:-1]
    if not inner.strip():
        return []
    return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]


def _format_inline_list(tags: list[str]) -> str:
    """Format a list of tags as an inline YAML list string ``[a, b, c]``."""
    if not tags:
        return "[]"
    return "[" + ", ".join(tags) + "]"


def _parse_block_list(block: str) -> list[str]:
    """Parse a YAML block list (``  - item`` lines) into a Python list."""
    tags = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            tag = stripped[2:].strip().strip("\"'")
            if tag:
                tags.append(tag)
    return tags


def _format_block_list(tags: list[str]) -> str:
    """Format a list of tags as a YAML block list string (newline-terminated)."""
    if not tags:
        return "\n"
    return "\n" + "".join(f"  - {t}\n" for t in tags)


def canonicalise_file(path: Path, alias_map: dict[str, str], *, dry_run: bool = False) -> bool:
    """Rewrite ``tags:`` frontmatter in *path* using *alias_map*.

    Returns ``True`` if the file was (or would be) changed.
    """
    text = path.read_text(encoding="utf-8")
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return False

    new_text = text
    changed = False

    # Try inline format first: tags: [a, b, c]
    inline_match = _INLINE_TAGS_RE.search(new_text)
    if inline_match:
        key_part = inline_match.group(1)
        raw_list = inline_match.group(2)
        old_tags = _parse_inline_list(raw_list)
        new_tags = _canonicalise_list(old_tags, alias_map)
        if new_tags != old_tags:
            new_raw = f"{key_part} {_format_inline_list(new_tags)}"
            new_text = new_text[: inline_match.start()] + new_raw + new_text[inline_match.end() :]
            changed = True
    else:
        # Try block format: tags:\n  - a\n  - b
        block_match = _BLOCK_TAGS_RE.search(new_text)
        if block_match:
            key_part = block_match.group(1)
            raw_block = block_match.group(2)
            old_tags = _parse_block_list(raw_block)
            new_tags = _canonicalise_list(old_tags, alias_map)
            if new_tags != old_tags:
                new_block = f"{key_part}{_format_block_list(new_tags)}"
                new_text = (
                    new_text[: block_match.start()] + new_block + new_text[block_match.end() :]
                )
                changed = True

    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return changed


# ---------------------------------------------------------------------------
# Directory scan
# ---------------------------------------------------------------------------


def canonicalise_directory(
    root: Path, alias_map: dict[str, str], *, dry_run: bool = False
) -> list[Path]:
    """Canonicalise tags in all research items under *root*.

    Scans ``Research/completed/``, ``Research/backlog/``, and
    ``Research/in-progress/``.  Returns the list of files that were changed
    (or would be changed in dry-run mode).
    """
    dirs = [
        root / "Research" / "completed",
        root / "Research" / "backlog",
        root / "Research" / "in-progress",
    ]
    changed_files: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name.lower() in {".gitkeep", "readme.md"}:
                continue
            if canonicalise_file(path, alias_map, dry_run=dry_run):
                changed_files.append(path)
    return changed_files


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root (default: parent of scripts/)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would change without writing them",
    )
    p.add_argument(
        "--vocab",
        type=Path,
        default=None,
        help="Path to tag-vocabulary.md (default: docs/tag-vocabulary.md)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    vocab_path = args.vocab or (args.root / "docs" / "tag-vocabulary.md")

    try:
        alias_map = load_vocabulary(vocab_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    changed = canonicalise_directory(args.root, alias_map, dry_run=args.dry_run)

    if not changed:
        print("No tag changes needed.")
        return 0

    mode = "Would change" if args.dry_run else "Changed"
    for p in changed:
        print(f"{mode}: {p}")
    print(f"\n{mode} {len(changed)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

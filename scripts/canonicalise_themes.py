"""Migrate research items from legacy ``tags:`` / ``ai_themes:`` to ``themes:``.

Reads the canonical themes vocabulary from docs/themes-vocabulary.md and rewrites
every research item under:

    Research/completed/
    Research/backlog/
    Research/in-progress/

Migration rules:
  1. ``ai_themes:`` values are mapped through the synonym map; already-canonical
     slugs pass through unchanged.
  2. ``tags:`` values that match a canonical slug or alias in the themes vocabulary
     are mapped to their canonical form; unknown ``tags:`` values are **dropped**
     (they do not belong in the themes controlled vocabulary).
  3. The merged, deduplicated list is written to ``themes:``.
  4. The ``tags:`` and ``ai_themes:`` fields are removed from frontmatter.
  5. Items that already have ``themes:`` and no legacy fields are unchanged
     (idempotent).

A migration summary is written to ``state/themes-migration.md``.

Usage:
    python scripts/canonicalise_themes.py [--root /path/to/repo] [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Vocabulary loading
# ---------------------------------------------------------------------------

_YAML_BLOCK_RE = re.compile(r"```yaml\n(.*?)```", re.DOTALL)

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "themes-vocabulary.md"


def load_themes_vocabulary(vocab_path: Path = VOCAB_PATH) -> dict[str, str]:
    """Return a reverse map: alias/canonical -> canonical.

    The vocabulary markdown file must contain exactly one fenced ``yaml`` code
    block mapping each canonical slug to a list of aliases::

        canonical-slug:
          - alias1
          - alias2

    Returns a dict where every alias (and each canonical slug) maps to
    the canonical slug string.
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
        if not line.startswith(" ") and not line.startswith("-") and stripped.endswith(":"):
            current_canonical = stripped[:-1]
            alias_map[current_canonical] = current_canonical
        elif stripped.startswith("- ") and current_canonical is not None:
            alias = stripped[2:].strip()
            if alias:
                alias_map[alias] = current_canonical

    return alias_map


# ---------------------------------------------------------------------------
# Frontmatter parsing helpers
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Inline list: themes: [a, b]  or  tags: [a, b]  or  ai_themes: [a, b]
_INLINE_LIST_RE = re.compile(r"^({field}\s*:)\s*(\[.*?\])\s*$", re.MULTILINE)

# Block list: themes:\n  - a\n  - b
_BLOCK_LIST_RE = re.compile(r"^({field}\s*:)\s*\n((?:[ \t]+-[ \t]+\S.*\n)*)", re.MULTILINE)

# Empty list or null: themes: []\n  or  themes: ~
_EMPTY_FIELD_RE = re.compile(r"^{field}\s*:\s*(?:\[\]|~|-)\s*$", re.MULTILINE)


def _inline_re(field: str) -> re.Pattern[str]:
    return re.compile(rf"^({re.escape(field)}\s*:)\s*(\[.*?\])\s*$", re.MULTILINE)


def _block_re(field: str) -> re.Pattern[str]:
    return re.compile(
        rf"^({re.escape(field)}\s*:)\s*\n((?:[ \t]+-[ \t]+\S.*\n)+)",
        re.MULTILINE,
    )


def _field_line_re(field: str) -> re.Pattern[str]:
    """Match any line that starts the given field (inline, block, empty)."""
    return re.compile(rf"^{re.escape(field)}\s*:.*$", re.MULTILINE)


def _parse_inline(raw: str) -> list[str]:
    inner = raw.strip()[1:-1]
    if not inner.strip():
        return []
    return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]


def _parse_block(block: str) -> list[str]:
    result = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            val = stripped[2:].strip().strip("\"'")
            if val:
                result.append(val)
    return result


def _format_inline(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(values) + "]"


def _extract_field(text: str, field: str) -> list[str]:
    """Extract values from a frontmatter field (inline or block list)."""
    inline_match = _inline_re(field).search(text)
    if inline_match:
        return _parse_inline(inline_match.group(2))
    block_match = _block_re(field).search(text)
    if block_match:
        return _parse_block(block_match.group(2))
    return []


def _remove_field(text: str, field: str) -> str:
    """Remove a frontmatter field (inline or block) from text."""
    # Block list (multi-line) — must match first to avoid partial removal
    block_match = _block_re(field).search(text)
    if block_match:
        return text[: block_match.start()] + text[block_match.end() :]
    # Inline or empty single-line
    line_match = _field_line_re(field).search(text)
    if line_match:
        start = line_match.start()
        end = line_match.end()
        # Remove the trailing newline too
        if end < len(text) and text[end] == "\n":
            end += 1
        return text[:start] + text[end:]
    return text


def _has_field(text: str, field: str) -> bool:
    """Return True if the field appears in frontmatter."""
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return False
    fm = fm_match.group(1)
    return bool(_field_line_re(field).search(fm)) or bool(_block_re(field).search(fm))


def _insert_themes_field(text: str, themes: list[str]) -> str:
    """Insert themes: [values] after the output: field in frontmatter.

    Falls back to inserting before the first blank line or before the closing ---.
    """
    themes_line = f"themes: {_format_inline(themes)}"

    # Prefer inserting after the output: line
    output_match = _field_line_re("output").search(text)
    if output_match:
        insert_pos = output_match.end()
        if insert_pos < len(text) and text[insert_pos] == "\n":
            insert_pos += 1
        return text[:insert_pos] + themes_line + "\n" + text[insert_pos:]

    # Fallback: insert before the closing ---
    close_match = re.search(r"^---$", text, re.MULTILINE)
    if close_match:
        return text[: close_match.start()] + themes_line + "\n" + text[close_match.start() :]

    return text + themes_line + "\n"


def _merge_themes(
    ai_themes: list[str],
    tags: list[str],
    vocab: dict[str, str],
) -> list[str]:
    """Merge ai_themes: and tags: into a deduplicated canonical themes list.

    - ai_themes: values: pass through vocabulary map (all are expected to be
      canonical or near-canonical).
    - tags: values: only include values that resolve to a known canonical slug;
      unrecognised tags are dropped.
    """
    seen: set[str] = set()
    result: list[str] = []

    def _add(slug: str) -> None:
        canonical = vocab.get(slug)
        if canonical is not None and canonical not in seen:
            seen.add(canonical)
            result.append(canonical)

    for slug in ai_themes:
        _add(slug)
    for slug in tags:
        _add(slug)

    return result


# ---------------------------------------------------------------------------
# File migration
# ---------------------------------------------------------------------------


def canonicalise_file(path: Path, vocab: dict[str, str], *, dry_run: bool = False) -> bool:
    """Migrate legacy fields to ``themes:`` in *path*.

    Returns ``True`` if the file was (or would be) changed.
    """
    text = path.read_text(encoding="utf-8")

    has_tags = _has_field(text, "tags")
    has_ai_themes = _has_field(text, "ai_themes")
    has_themes = _has_field(text, "themes")

    # Idempotent: nothing to do
    if not has_tags and not has_ai_themes:
        return False

    ai_themes = _extract_field(text, "ai_themes")
    tags = _extract_field(text, "tags")

    merged = _merge_themes(ai_themes, tags, vocab)

    # Determine new themes: merge with any existing themes: values
    existing_themes: list[str] = []
    if has_themes:
        existing_themes = _extract_field(text, "themes")

    # Combine: existing themes take priority (already canonical), then merged
    combined_set: set[str] = set()
    combined: list[str] = []
    for slug in existing_themes + merged:
        if slug not in combined_set:
            combined_set.add(slug)
            combined.append(slug)

    # Build new text
    new_text = text

    # Remove legacy fields
    new_text = _remove_field(new_text, "ai_themes")
    new_text = _remove_field(new_text, "tags")

    # Update or insert themes:
    if has_themes:
        # Replace existing themes field value
        inline_match = _inline_re("themes").search(new_text)
        if inline_match:
            replacement = f"{inline_match.group(1)} {_format_inline(combined)}"
            new_text = (
                new_text[: inline_match.start()] + replacement + new_text[inline_match.end() :]
            )
        else:
            block_match = _block_re("themes").search(new_text)
            if block_match:
                replacement = f"{block_match.group(1)} {_format_inline(combined)}\n"
                new_text = (
                    new_text[: block_match.start()] + replacement + new_text[block_match.end() :]
                )
    else:
        new_text = _insert_themes_field(new_text, combined)

    if new_text == text:
        return False

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return True


# ---------------------------------------------------------------------------
# Directory scan
# ---------------------------------------------------------------------------


def canonicalise_directory(
    root: Path, vocab: dict[str, str], *, dry_run: bool = False
) -> list[Path]:
    """Migrate all research items under *root*.

    Scans ``Research/completed/``, ``Research/backlog/``, and
    ``Research/in-progress/``.  Returns the list of files that were (or would be)
    changed.
    """
    dirs = [
        root / "Research" / "completed",
        root / "Research" / "backlog",
        root / "Research" / "in-progress",
    ]
    changed: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name.lower() in {".gitkeep", "readme.md"}:
                continue
            if canonicalise_file(path, vocab, dry_run=dry_run):
                changed.append(path)
    return changed


# ---------------------------------------------------------------------------
# Migration summary
# ---------------------------------------------------------------------------


def write_migration_summary(root: Path, changed: list[Path]) -> None:
    """Write a migration summary to ``state/themes-migration.md``."""
    state_dir = root / "state"
    state_dir.mkdir(exist_ok=True)
    summary_path = state_dir / "themes-migration.md"

    today = date.today().isoformat()
    lines = [
        f"# Themes migration summary — {today}",
        "",
        f"Migrated {len(changed)} file(s) from `tags:` / `ai_themes:` to `themes:`.",
        "",
    ]
    if changed:
        lines.append("## Migrated files")
        lines.append("")
        for path in changed:
            lines.append(f"- {path}")
        lines.append("")

    summary_path.write_text("\n".join(lines), encoding="utf-8")


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
        help="Path to themes-vocabulary.md (default: docs/themes-vocabulary.md)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    vocab_path = args.vocab or (args.root / "docs" / "themes-vocabulary.md")

    try:
        vocab = load_themes_vocabulary(vocab_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    changed = canonicalise_directory(args.root, vocab, dry_run=args.dry_run)

    if not args.dry_run:
        write_migration_summary(args.root, changed)

    if not changed:
        print("No theme migration needed.")
        return 0

    mode = "Would change" if args.dry_run else "Migrated"
    for p in changed:
        print(f"{mode}: {p}")
    print(f"\n{mode} {len(changed)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

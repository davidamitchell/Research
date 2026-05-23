"""Validate that no research items contain legacy ``tags:`` or ``ai_themes:`` fields.

After running ``scripts/canonicalise_themes.py``, this script confirms that the
migration is complete across all items in:

    Research/completed/
    Research/backlog/
    Research/in-progress/

Exits with code 0 if no violations are found, code 1 otherwise.

Usage:
    python scripts/validate_themes.py [--root /path/to/repo]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_TAGS_RE = re.compile(r"^tags\s*:", re.MULTILINE)
_AI_THEMES_RE = re.compile(r"^ai_themes\s*:", re.MULTILINE)


def _has_legacy_fields(text: str) -> tuple[bool, bool]:
    """Return (has_tags, has_ai_themes) for the given item text."""
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return False, False
    fm = fm_match.group(1)
    return bool(_TAGS_RE.search(fm)), bool(_AI_THEMES_RE.search(fm))


def validate_directory(root: Path) -> list[str]:
    """Scan all research items under *root* for residual legacy fields.

    Returns a list of violation messages (empty if all items are clean).
    """
    dirs = [
        root / "Research" / "completed",
        root / "Research" / "backlog",
        root / "Research" / "in-progress",
    ]
    violations: list[str] = []
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name.lower() in {".gitkeep", "readme.md"}:
                continue
            text = path.read_text(encoding="utf-8")
            has_tags, has_ai_themes = _has_legacy_fields(text)
            if has_tags:
                violations.append(f"{path}: still contains tags: field")
            if has_ai_themes:
                violations.append(f"{path}: still contains ai_themes: field")
    return violations


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root (default: parent of scripts/)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    violations = validate_directory(args.root)

    if not violations:
        print("OK: No legacy tags: or ai_themes: fields found.")
        return 0

    print(f"FAIL: {len(violations)} violation(s) found:\n", file=sys.stderr)
    for v in violations:
        print(f"  {v}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

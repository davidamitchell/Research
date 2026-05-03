"""Gap registry aggregator.

Scans all research items in Research/completed/, extracts the ``gaps:``
YAML list from each item's frontmatter, and writes a consolidated registry to
``state/gap_registry.json``.

Each unique gap string (after normalisation) is mapped to:
- ``count``   — number of completed items that raised it
- ``items``   — list of item slugs (filename without ``.md``) that raised it
- ``promote`` — ``true`` when count >= 3 (threshold for automatic backlog
  promotion)

Near-duplicate detection: gaps that differ only in case or surrounding
whitespace are treated as the same gap. The canonical form stored in the
output is the first occurrence (lowest lexicographic order after
normalisation).

Usage::

    python scripts/aggregate_gaps.py [--completed-dir <dir>] [--output <file>]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

# Make src/ importable when running the script directly from the repo root.
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.logger import get_logger

logger = get_logger(__name__)

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_GAPS_BLOCK_RE = re.compile(r"^gaps\s*:(.*)$", re.MULTILINE)

PROMOTE_THRESHOLD = 3


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


def _extract_frontmatter(text: str) -> str | None:
    """Return the raw YAML frontmatter string, or None if absent."""
    m = _FM_RE.match(text)
    return m.group(1) if m else None


def _parse_gaps(frontmatter: str) -> list[str]:
    """Return the list of gap strings from a YAML frontmatter block.

    Supports both inline list syntax ``gaps: [a, b]`` and block list syntax::

        gaps:
          - a
          - b

    Returns an empty list if the field is absent or empty.
    """
    m = _GAPS_BLOCK_RE.search(frontmatter)
    if not m:
        return []

    # Everything after "gaps:" on the same line
    rest_of_line = m.group(1).strip()

    # Inline list: gaps: [a, b, c]
    if rest_of_line.startswith("[") and rest_of_line.endswith("]"):
        inner = rest_of_line[1:-1]
        if not inner.strip():
            return []
        return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]

    # Block list: entries are on subsequent lines starting with "  - "
    # We grab everything from the match position to the next top-level key.
    fm_lines = frontmatter.splitlines()
    gaps_start = None
    for i, line in enumerate(fm_lines):
        if _GAPS_BLOCK_RE.match(line):
            gaps_start = i
            break

    if gaps_start is None:
        return []

    result: list[str] = []
    for line in fm_lines[gaps_start + 1 :]:
        stripped = line.strip()
        if not stripped:
            continue
        # A new top-level key ends the block
        if re.match(r"^[a-zA-Z_-][a-zA-Z0-9_-]*\s*:", stripped) and not stripped.startswith("-"):
            break
        if stripped.startswith("- "):
            value = stripped[2:].strip().strip("\"'")
            if value:
                result.append(value)
        elif stripped.startswith("-"):
            value = stripped[1:].strip().strip("\"'")
            if value:
                result.append(value)

    return result


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------


def _normalise(gap: str) -> str:
    """Return a normalised form of a gap string for deduplication.

    Strips surrounding whitespace and lowercases. This is intentionally
    lightweight — heavy NLP is not used.
    """
    return gap.strip().lower()


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def aggregate_gaps(completed_dir: Path) -> dict[str, dict]:
    """Scan completed items and return a mapping of gap → {count, items, promote}.

    The keys are canonical gap strings (first-seen, original case).
    """
    # norm_key → canonical string (first-seen)
    canonical: dict[str, str] = {}
    # norm_key → list of item slugs
    slug_map: dict[str, list[str]] = defaultdict(list)

    for path in sorted(completed_dir.glob("*.md")):
        if path.name == ".gitkeep":
            continue
        text = path.read_text(encoding="utf-8")
        fm = _extract_frontmatter(text)
        if fm is None:
            logger.info("No frontmatter found in %s — skipping", path.name)
            continue

        gaps = _parse_gaps(fm)
        slug = path.stem
        logger.info("Processing %s — found %d gap(s)", path.name, len(gaps))

        for gap in gaps:
            norm = _normalise(gap)
            if norm not in canonical:
                canonical[norm] = gap  # preserve original casing
            slug_map[norm].append(slug)

    result: dict[str, dict] = {}
    for norm, slugs in slug_map.items():
        count = len(slugs)
        result[canonical[norm]] = {
            "count": count,
            "items": slugs,
            "promote": count >= PROMOTE_THRESHOLD,
        }

    return result


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate gaps from completed research items.")
    parser.add_argument(
        "--completed-dir",
        type=Path,
        default=Path(__file__).parent.parent / "Research" / "completed",
        help="Path to Research/completed/ directory (default: auto-detected from script location)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent / "state" / "gap_registry.json",
        help="Output JSON path (default: state/gap_registry.json)",
    )
    args = parser.parse_args()

    completed_dir: Path = args.completed_dir.resolve()
    output_path: Path = args.output.resolve()

    if not completed_dir.exists():
        logger.error("Completed directory not found: %s", completed_dir)
        sys.exit(1)

    gaps = aggregate_gaps(completed_dir)

    if not gaps:
        logger.info("No gaps found across completed items.")

    promote_count = sum(1 for v in gaps.values() if v["promote"])
    logger.info(
        "Aggregated %d unique gap(s); %d flagged for promotion (count >= %d)",
        len(gaps),
        promote_count,
        PROMOTE_THRESHOLD,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "gaps": gaps,
        "generated_at": datetime.now(tz=UTC).isoformat(),
    }
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Written: %s", output_path)


if __name__ == "__main__":
    main()

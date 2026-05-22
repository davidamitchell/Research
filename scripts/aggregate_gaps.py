"""Gap registry aggregator.

Scans all completed research items in ``Research/completed/``, extracts the
``gaps:`` YAML frontmatter field from each, counts how often identical (after
normalisation) gap strings appear across the corpus, and writes the results to
``state/gap_registry.json``.

A gap that appears in three or more completed items is flagged with
``"promote": true``, signalling that it should be converted into a new research
backlog item.

Usage::

    python scripts/aggregate_gaps.py [--root /path/to/repo] [--threshold 3]

Outputs:

    state/gap_registry.json  — machine-readable gap registry
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import UTC, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Frontmatter extraction
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def extract_gaps(path: Path) -> list[str]:
    """Return the list of gaps from a research item's YAML frontmatter.

    Returns an empty list if the file has no frontmatter, no ``gaps:`` field,
    or the field is an empty list.
    """
    if path.name.lower() in (".gitkeep", "_template.md"):
        return []

    text = path.read_text(encoding="utf-8")
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return []

    import yaml  # type: ignore[import-untyped]

    try:
        meta = yaml.safe_load(fm_match.group(1))
    except yaml.YAMLError:
        return []

    if not isinstance(meta, dict):
        return []

    gaps = meta.get("gaps")
    if not gaps:
        return []
    if isinstance(gaps, list):
        return [str(g).strip() for g in gaps if g]
    # Scalar (uncommon but handle gracefully)
    return [str(gaps).strip()] if str(gaps).strip() else []


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------


def normalize_gap(gap: str) -> str:
    """Return a normalised form of a gap string for counting purposes.

    Normalisation: strip surrounding whitespace, convert to lowercase.
    """
    return gap.strip().lower()


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def aggregate_gaps(completed_dir: Path, threshold: int = 3) -> dict:
    """Scan completed items and return a gap registry dict.

    Args:
        completed_dir: Path to ``Research/completed/``.
        threshold: Minimum count for a gap to be flagged ``promote: true``.

    Returns:
        A dict matching the ``gap_registry.json`` schema:
        ``{generated, total_gaps, promoted_count, gaps: [{text, count, items, promote}]}``.
    """
    # gap_normalized -> {original_text, [slugs]}
    gap_map: dict[str, dict] = {}

    for path in sorted(completed_dir.glob("*.md")):
        if path.name.lower() in (".gitkeep", "_template.md"):
            continue
        slug = path.stem
        for gap in extract_gaps(path):
            norm = normalize_gap(gap)
            if not norm:
                continue
            if norm not in gap_map:
                gap_map[norm] = {"text": norm, "items": []}
            if slug not in gap_map[norm]["items"]:
                gap_map[norm]["items"].append(slug)

    gaps_list = []
    for norm, data in gap_map.items():
        count = len(data["items"])
        gaps_list.append(
            {
                "text": norm,
                "count": count,
                "items": sorted(data["items"]),
                "promote": count >= threshold,
            }
        )

    # Sort by count descending, then text ascending for determinism
    gaps_list.sort(key=lambda g: (-g["count"], g["text"]))

    promoted = sum(1 for g in gaps_list if g["promote"])

    return {
        "generated": datetime.now(UTC).strftime("%Y-%m-%d"),
        "total_gaps": len(gaps_list),
        "promoted_count": promoted,
        "gaps": gaps_list,
    }


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def write_registry(registry: dict, output_path: Path) -> None:
    """Write the gap registry to a JSON file, creating parent directories."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Aggregate research item gaps into state/gap_registry.json."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Minimum count to flag a gap as promote=true (default: 3)",
    )
    args = parser.parse_args()

    completed_dir = args.root / "Research" / "completed"
    output_path = args.root / "state" / "gap_registry.json"

    registry = aggregate_gaps(completed_dir, threshold=args.threshold)
    write_registry(registry, output_path)

    print(f"Gap registry written to {output_path}")
    print(f"  Total unique gaps : {registry['total_gaps']}")
    print(f"  Promoted (>={args.threshold} items): {registry['promoted_count']}")


if __name__ == "__main__":
    main()

"""Tag co-occurrence report generator.

Scans all research items in Research/completed/ and Research/backlog/, then
produces two output files:

    state/tag_report.json  — machine-readable data
    state/tag_report.md    — human-readable summary for review

Outputs computed:
- Tag frequency (how many items each tag appears in)
- Singleton tags (appear in exactly one item)
- Co-occurrence matrix (how many items share each tag pair)
- Strong co-occurrence pairs (appear together in >80% of each other's
  occurrences — strong synonymy signal)
- Near-duplicate candidates (Levenshtein distance ≤ 2 or prefix/suffix
  overlap ≥ 0.8 between any two tags that each appear in ≥ 2 items)

Usage:
    python scripts/tag_report.py [--root /path/to/repo]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

# ---------------------------------------------------------------------------
# Levenshtein distance (pure stdlib, no external dependency)
# ---------------------------------------------------------------------------


def levenshtein(a: str, b: str) -> int:
    """Return the Levenshtein edit distance between two strings."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = curr
    return prev[-1]


# ---------------------------------------------------------------------------
# Near-duplicate heuristics
# ---------------------------------------------------------------------------


def _prefix_suffix_overlap(a: str, b: str) -> float:
    """Return the best prefix/suffix overlap ratio between two tag strings.

    Computed as max(len(shared_prefix), len(shared_suffix)) / max(len(a), len(b)).
    A value ≥ 0.8 signals strong morphological similarity (e.g. plurals,
    compound variants).
    """
    if not a or not b:
        return 0.0
    # Shared prefix length
    prefix_len = 0
    for ca, cb in zip(a, b, strict=False):
        if ca == cb:
            prefix_len += 1
        else:
            break
    # Shared suffix length
    suffix_len = 0
    for ca, cb in zip(reversed(a), reversed(b), strict=False):
        if ca == cb:
            suffix_len += 1
        else:
            break
    denom = max(len(a), len(b))
    return max(prefix_len, suffix_len) / denom


def is_near_duplicate(a: str, b: str) -> bool:
    """Return True if two tags are near-duplicates.

    Criteria (either is sufficient):
    - Levenshtein distance ≤ 2
    - Prefix/suffix overlap ≥ 0.8
    """
    if levenshtein(a, b) <= 2:  # noqa: SIM103
        return True
    return _prefix_suffix_overlap(a, b) >= 0.8


# ---------------------------------------------------------------------------
# Frontmatter tag extraction
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_TAGS_RE = re.compile(r"^tags\s*:\s*(.+)$", re.MULTILINE)


def _extract_tags(path: Path) -> list[str]:
    """Return the list of tags from a research item's YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return []
    fm = fm_match.group(1)
    tags_match = _TAGS_RE.search(fm)
    if not tags_match:
        return []
    raw = tags_match.group(1).strip()
    # Inline list: [tag1, tag2, ...]
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1]
        if not inner.strip():
            return []
        return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]
    # Scalar (single tag not in a list — rare but valid)
    return [raw.strip().strip("\"'")]


# ---------------------------------------------------------------------------
# Core analysis
# ---------------------------------------------------------------------------


def collect_tags(root: Path) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return (slug_to_tags, tag_to_slugs) by scanning completed + backlog items."""
    slug_to_tags: dict[str, list[str]] = {}
    tag_to_slugs: dict[str, list[str]] = defaultdict(list)

    dirs = [root / "Research" / "completed", root / "Research" / "backlog"]
    for d in dirs:
        for path in sorted(d.glob("*.md")):
            if path.name.lower() == ".gitkeep":
                continue
            slug = path.stem
            tags = _extract_tags(path)
            if tags:
                slug_to_tags[slug] = tags
                for t in tags:
                    tag_to_slugs[t].append(slug)

    return slug_to_tags, dict(tag_to_slugs)


def compute_cooccurrence(slug_to_tags: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    """Return a co-occurrence count dict: co[tag_a][tag_b] = item count."""
    co: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for tags in slug_to_tags.values():
        tag_set = sorted(set(tags))
        for a, b in combinations(tag_set, 2):
            co[a][b] += 1
            co[b][a] += 1
    return {k: dict(v) for k, v in co.items()}


def find_strong_pairs(
    tag_to_slugs: dict[str, list[str]],
    cooccurrence: dict[str, dict[str, int]],
    threshold: float = 0.8,
    min_cooccurrence: int = 2,
) -> list[dict]:
    """Return pairs where tags co-occur in > threshold of each other's occurrences.

    Only considers pairs with at least min_cooccurrence shared items to avoid
    trivial 100%-ratio matches from tags that each appear in exactly one item.
    """
    results = []
    tags = sorted(tag_to_slugs.keys())
    for a, b in combinations(tags, 2):
        count_a = len(tag_to_slugs[a])
        count_b = len(tag_to_slugs[b])
        co = cooccurrence.get(a, {}).get(b, 0)
        if co < min_cooccurrence:
            continue
        ratio_a = co / count_a
        ratio_b = co / count_b
        if ratio_a > threshold and ratio_b > threshold:
            results.append(
                {
                    "tag_a": a,
                    "tag_b": b,
                    "cooccurrence": co,
                    "count_a": count_a,
                    "count_b": count_b,
                    "ratio_a": round(ratio_a, 3),
                    "ratio_b": round(ratio_b, 3),
                }
            )
    return sorted(results, key=lambda x: -(x["cooccurrence"]))


def find_near_duplicates(tag_to_slugs: dict[str, list[str]]) -> list[dict]:
    """Return near-duplicate tag pairs from tags that appear in ≥ 2 items."""
    # Only consider tags appearing in ≥ 2 items to reduce noise
    candidate_tags = [t for t, slugs in tag_to_slugs.items() if len(slugs) >= 2]
    results = []
    for a, b in combinations(sorted(candidate_tags), 2):
        if is_near_duplicate(a, b):
            results.append(
                {
                    "tag_a": a,
                    "tag_b": b,
                    "count_a": len(tag_to_slugs[a]),
                    "count_b": len(tag_to_slugs[b]),
                    "distance": levenshtein(a, b),
                    "overlap": round(_prefix_suffix_overlap(a, b), 3),
                }
            )
    return sorted(results, key=lambda x: (x["distance"], -max(x["count_a"], x["count_b"])))


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------


def build_report(root: Path) -> dict:
    """Build the full tag report data structure."""
    slug_to_tags, tag_to_slugs = collect_tags(root)

    frequency = {tag: len(slugs) for tag, slugs in sorted(tag_to_slugs.items())}
    singletons = sorted(t for t, slugs in tag_to_slugs.items() if len(slugs) == 1)
    cooccurrence = compute_cooccurrence(slug_to_tags)
    strong_pairs = find_strong_pairs(tag_to_slugs, cooccurrence)
    near_dupes = find_near_duplicates(tag_to_slugs)

    return {
        "summary": {
            "total_tags": len(frequency),
            "total_items_scanned": len(slug_to_tags),
            "singleton_count": len(singletons),
            "strong_pair_count": len(strong_pairs),
            "near_duplicate_count": len(near_dupes),
        },
        "frequency": frequency,
        "singletons": singletons,
        "strong_pairs": strong_pairs,
        "near_duplicates": near_dupes,
    }


def render_markdown(data: dict) -> str:
    """Render the report as a human-readable Markdown document."""
    s = data["summary"]
    lines = [
        "# Tag Report",
        "",
        f"**Total tags:** {s['total_tags']}  ",
        f"**Items scanned:** {s['total_items_scanned']}  ",
        f"**Singleton tags:** {s['singleton_count']}  ",
        f"**Strong synonym pairs:** {s['strong_pair_count']}  ",
        f"**Near-duplicate candidates:** {s['near_duplicate_count']}",
        "",
        "---",
        "",
        "## Strong synonym pairs",
        "",
        "> Tags that appear together in >80% of each other's occurrences.",
        "> These are the highest-priority candidates for consolidation.",
        "",
    ]
    if data["strong_pairs"]:
        lines += [
            "| Tag A | Tag B | Co-occ | Ratio A | Ratio B |",
            "|---|---|---|---|---|",
        ]
        for p in data["strong_pairs"]:
            lines.append(
                f"| `{p['tag_a']}` | `{p['tag_b']}` "
                f"| {p['cooccurrence']} | {p['ratio_a']} | {p['ratio_b']} |"
            )
    else:
        lines.append("_None found._")

    lines += [
        "",
        "---",
        "",
        "## Near-duplicate candidates",
        "",
        "> Tags with Levenshtein distance ≤ 2 or prefix/suffix overlap ≥ 0.8.",
        "> Only tags appearing in ≥ 2 items are included.",
        "",
    ]
    if data["near_duplicates"]:
        lines += [
            "| Tag A | Count A | Tag B | Count B | Distance | Overlap |",
            "|---|---|---|---|---|---|",
        ]
        for d in data["near_duplicates"]:
            lines.append(
                f"| `{d['tag_a']}` | {d['count_a']} | `{d['tag_b']}` | {d['count_b']} "
                f"| {d['distance']} | {d['overlap']} |"
            )
    else:
        lines.append("_None found._")

    lines += [
        "",
        "---",
        "",
        "## Singleton tags",
        "",
        "> Tags that appear in exactly one item. Consider whether each is",
        "> specific enough to warrant a dedicated tag or should be merged",
        "> into a broader canonical form.",
        "",
    ]
    if data["singletons"]:
        lines.append(", ".join(f"`{t}`" for t in data["singletons"]))
    else:
        lines.append("_None found._")

    lines += [
        "",
        "---",
        "",
        "## Tag frequency",
        "",
        "| Tag | Item count |",
        "|---|---|",
    ]
    for tag, count in sorted(data["frequency"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| `{tag}` | {count} |")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate tag co-occurrence report.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root directory (default: parent of scripts/)",
    )
    args = parser.parse_args()

    root: Path = args.root.resolve()
    state_dir = root / "state"
    state_dir.mkdir(exist_ok=True)

    print("Scanning research items…")
    data = build_report(root)
    s = data["summary"]
    print(f"  {s['total_items_scanned']} items scanned")
    print(f"  {s['total_tags']} unique tags")
    print(f"  {s['singleton_count']} singletons")
    print(f"  {s['strong_pair_count']} strong synonym pairs")
    print(f"  {s['near_duplicate_count']} near-duplicate candidates")

    json_path = state_dir / "tag_report.json"
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Written: {json_path}")

    md_path = state_dir / "tag_report.md"
    md_path.write_text(render_markdown(data), encoding="utf-8")
    print(f"Written: {md_path}")


if __name__ == "__main__":
    main()

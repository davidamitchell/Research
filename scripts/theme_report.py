"""Theme usage audit report generator.

Scans research items in ``Research/completed/`` and produces:

    state/theme_report.json  — machine-readable audit data
    state/theme_report.md    — human-readable summary

Usage:
    python scripts/theme_report.py [--root /path/to/repo]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import TypedDict

from tag_report import _prefix_suffix_overlap, levenshtein

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


class ExtractedThemes(TypedDict):
    """Theme values and field-presence flags extracted from frontmatter."""

    themes: list[str]
    ai_themes: list[str]
    has_themes_field: bool
    has_ai_themes_field: bool


def _parse_yaml_list(raw: str) -> list[str]:
    """Parse a scalar or inline YAML list value into a list of strings."""
    value = raw.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip("\"'") for part in inner.split(",") if part.strip()]
    return [value.strip().strip("\"'")]


def _extract_field_values(frontmatter: str, field: str) -> tuple[list[str], bool]:
    """Extract values for a single frontmatter field from YAML text."""
    pattern = re.compile(rf"^{re.escape(field)}[ \t]*:[ \t]*(.*)$", re.MULTILINE)
    match = pattern.search(frontmatter)
    if not match:
        return [], False

    inline_value = match.group(1)
    if inline_value.strip():
        return _parse_yaml_list(inline_value), True

    values: list[str] = []
    rest = frontmatter[match.end() :]
    for line in rest.splitlines():
        bullet = re.match(r"^\s*-\s*(.+)$", line)
        if bullet:
            values.append(bullet.group(1).strip().strip("\"'"))
            continue
        if line.strip() == "":
            continue
        if line.startswith((" ", "\t")):
            continue
        break
    return values, True


def _extract_themes(path: Path) -> ExtractedThemes:
    """Extract ``themes`` and ``ai_themes`` values from a markdown file."""
    text = path.read_text(encoding="utf-8")
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return {
            "themes": [],
            "ai_themes": [],
            "has_themes_field": False,
            "has_ai_themes_field": False,
        }

    frontmatter = fm_match.group(1)
    themes, has_themes = _extract_field_values(frontmatter, "themes")
    ai_themes, has_ai_themes = _extract_field_values(frontmatter, "ai_themes")
    return {
        "themes": themes,
        "ai_themes": ai_themes,
        "has_themes_field": has_themes,
        "has_ai_themes_field": has_ai_themes,
    }


def collect_themes(root: Path) -> dict:
    """Collect per-item and per-term theme usage across completed research items."""
    completed_dir = root / "Research" / "completed"

    term_to_slugs: dict[str, set[str]] = defaultdict(set)
    provenance: dict[str, dict[str, int]] = defaultdict(lambda: {"themes": 0, "ai_themes": 0})

    items_scanned = 0
    items_with_themes_field = 0
    items_with_ai_themes_field = 0
    items_with_neither: list[str] = []

    for path in sorted(completed_dir.glob("*.md")):
        if path.name in {"README.md", ".gitkeep"}:
            continue

        items_scanned += 1
        slug = path.stem
        extracted = _extract_themes(path)

        if extracted["has_themes_field"]:
            items_with_themes_field += 1
        if extracted["has_ai_themes_field"]:
            items_with_ai_themes_field += 1
        if not extracted["has_themes_field"] and not extracted["has_ai_themes_field"]:
            items_with_neither.append(slug)

        themes_terms = sorted(set(extracted["themes"]))
        ai_themes_terms = sorted(set(extracted["ai_themes"]))

        for term in themes_terms:
            provenance[term]["themes"] += 1
        for term in ai_themes_terms:
            provenance[term]["ai_themes"] += 1

        for term in set(themes_terms) | set(ai_themes_terms):
            term_to_slugs[term].add(slug)

    return {
        "items_scanned": items_scanned,
        "items_with_themes_field": items_with_themes_field,
        "items_with_ai_themes_field": items_with_ai_themes_field,
        "items_with_neither": sorted(items_with_neither),
        "term_to_slugs": term_to_slugs,
        "provenance": dict(provenance),
    }


def _is_hyphenated_overlap_candidate(a: str, b: str) -> bool:
    """Return True when hyphenated terms have strong lexical overlap."""
    if "-" not in a or "-" not in b:
        return False
    if a in b or b in a:
        return True
    tokens_a = set(a.split("-"))
    tokens_b = set(b.split("-"))
    return bool(tokens_a & tokens_b)


def find_near_duplicates(term_to_slugs: dict[str, set[str]]) -> list[dict]:
    """Find near-duplicate theme terms using lexical overlap heuristics."""
    candidate_terms = [term for term, slugs in term_to_slugs.items() if len(slugs) >= 2]

    results = []
    for term_a, term_b in combinations(sorted(candidate_terms), 2):
        distance = levenshtein(term_a, term_b)
        overlap = _prefix_suffix_overlap(term_a, term_b)

        if distance <= 2 or overlap >= 0.8 or _is_hyphenated_overlap_candidate(term_a, term_b):
            results.append(
                {
                    "term_a": term_a,
                    "term_b": term_b,
                    "count_a": len(term_to_slugs[term_a]),
                    "count_b": len(term_to_slugs[term_b]),
                    "distance": distance,
                    "overlap": round(overlap, 3),
                }
            )

    return sorted(results, key=lambda row: (row["distance"], -max(row["count_a"], row["count_b"])))


def build_report(root: Path) -> dict:
    """Build the machine-readable theme report payload."""
    collected = collect_themes(root)
    term_to_slugs: dict[str, set[str]] = collected["term_to_slugs"]
    provenance: dict[str, dict[str, int]] = collected["provenance"]

    frequency = {
        term: len(slugs)
        for term, slugs in sorted(term_to_slugs.items(), key=lambda item: (-len(item[1]), item[0]))
    }
    near_duplicates = find_near_duplicates(term_to_slugs)

    return {
        "summary": {
            "total_terms": len(frequency),
            "items_scanned": collected["items_scanned"],
            "items_with_themes_field": collected["items_with_themes_field"],
            "items_with_ai_themes_field": collected["items_with_ai_themes_field"],
            "items_with_neither": len(collected["items_with_neither"]),
            "near_duplicate_count": len(near_duplicates),
        },
        "frequency": frequency,
        "provenance": {
            term: {
                "themes": provenance.get(term, {}).get("themes", 0),
                "ai_themes": provenance.get(term, {}).get("ai_themes", 0),
            }
            for term in frequency
        },
        "items_with_neither": collected["items_with_neither"],
        "near_duplicates": near_duplicates,
    }


def render_markdown(data: dict) -> str:
    """Render the theme report as Markdown for manual review."""
    summary = data["summary"]
    lines = [
        "# Theme Report",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Total terms | {summary['total_terms']} |",
        f"| Items scanned | {summary['items_scanned']} |",
        f"| Items with `themes:` | {summary['items_with_themes_field']} |",
        f"| Items with `ai_themes:` | {summary['items_with_ai_themes_field']} |",
        f"| Items with neither | {summary['items_with_neither']} |",
        f"| Near-duplicate candidates | {summary['near_duplicate_count']} |",
        "",
        "## Near-duplicate candidates",
        "",
    ]

    if data["near_duplicates"]:
        lines += [
            "| Term A | Count A | Term B | Count B | Distance | Overlap |",
            "|---|---|---|---|---|---|",
        ]
        for row in data["near_duplicates"]:
            lines.append(
                f"| `{row['term_a']}` | {row['count_a']} | `{row['term_b']}` | {row['count_b']} "
                f"| {row['distance']} | {row['overlap']} |"
            )
    else:
        lines.append("_None found._")

    lines += [
        "",
        "## Frequency",
        "",
        "| Term | Count | From `themes:` | From `ai_themes:` |",
        "|---|---|---|---|",
    ]

    for term, count in data["frequency"].items():
        provenance = data["provenance"].get(term, {"themes": 0, "ai_themes": 0})
        lines.append(f"| `{term}` | {count} | {provenance['themes']} | {provenance['ai_themes']} |")

    lines += [
        "",
        "## Items with neither field",
        "",
    ]

    if data["items_with_neither"]:
        lines.extend([f"- `{slug}`" for slug in data["items_with_neither"]])
    else:
        lines.append("_None._")

    lines += [
        "",
        "## Review actions needed",
        "",
        "Terms appearing only in `ai_themes:` (never in `themes:`):",
        "",
    ]

    ai_only_terms = [
        term
        for term, provenance in data["provenance"].items()
        if provenance["themes"] == 0 and provenance["ai_themes"] > 0
    ]
    if ai_only_terms:
        lines.extend([f"- `{term}`" for term in sorted(ai_only_terms)])
    else:
        lines.append("_None._")

    return "\n".join(lines) + "\n"


def main() -> None:
    """CLI entry point for generating theme audit reports."""
    parser = argparse.ArgumentParser(description="Generate theme usage audit report.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root directory (default: parent of scripts/)",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    state_dir = root / "state"
    state_dir.mkdir(exist_ok=True)

    data = build_report(root)

    json_path = state_dir / "theme_report.json"
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    md_path = state_dir / "theme_report.md"
    md_path.write_text(render_markdown(data), encoding="utf-8")

    summary = data["summary"]
    print(f"Items scanned: {summary['items_scanned']}")
    print(f"Total terms: {summary['total_terms']}")
    print(f"Near-duplicate candidates: {summary['near_duplicate_count']}")
    print(f"Written: {json_path}")
    print(f"Written: {md_path}")


if __name__ == "__main__":
    main()

"""Theme governance report generator.

Scans all research items in Research/completed/ and Research/backlog/, then
produces two output files:

    state/theme_report.json  — machine-readable data
    state/theme_report.md    — human-readable summary for review

Outputs computed:
- Theme frequency (how many items each canonical theme appears in)
- Uncovered items (no themes: field set)
- Near-duplicate candidates among the canonical vocabulary using
  Levenshtein distance ≤ 2 combined with token Jaccard similarity ≥ 0.6
  (per W-0076 findings)
- Theme distribution statistics

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

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_THEMES_RE = re.compile(r"^themes\s*:\s*(.+)$", re.MULTILINE)
_BLOCK_LIST_RE = re.compile(r"^themes\s*:\s*\n((?:[ \t]+-[ \t]+\S.*\n)+)", re.MULTILINE)
_YAML_BLOCK_RE = re.compile(r"```yaml\n(.*?)```", re.DOTALL)

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "themes-vocabulary.md"


# ---------------------------------------------------------------------------
# Vocabulary loading
# ---------------------------------------------------------------------------


def _load_canonical_slugs(vocab_path: Path) -> list[str]:
    """Return the list of canonical theme slugs from the vocabulary file."""
    text = vocab_path.read_text(encoding="utf-8")
    match = _YAML_BLOCK_RE.search(text)
    if not match:
        raise ValueError(f"No yaml code block found in {vocab_path}")
    yaml_text = match.group(1)
    slugs: list[str] = []
    for line in yaml_text.splitlines():
        stripped = line.strip()
        if (
            stripped
            and not stripped.startswith("#")
            and not line.startswith(" ")
            and not line.startswith("-")
            and stripped.endswith(":")
        ):
            slugs.append(stripped[:-1])
    return slugs


# ---------------------------------------------------------------------------
# Near-duplicate detection (Levenshtein + token Jaccard)
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


def token_jaccard(a: str, b: str) -> float:
    """Return token Jaccard similarity between two hyphenated slugs.

    Tokens are the hyphen-separated components of each slug.
    Jaccard = |A ∩ B| / |A ∪ B|.
    """
    tokens_a = set(a.split("-"))
    tokens_b = set(b.split("-"))
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    return len(intersection) / len(union)


def find_theme_near_duplicates(slugs: list[str]) -> list[dict]:
    """Return near-duplicate slug pairs using Levenshtein ≤ 2 OR token Jaccard ≥ 0.6.

    Based on the W-0076 research findings on similarity thresholds for controlled
    vocabulary management.
    """
    results: list[dict] = []
    for a, b in combinations(sorted(slugs), 2):
        dist = levenshtein(a, b)
        jaccard = token_jaccard(a, b)
        if dist <= 2 or jaccard >= 0.6:
            results.append(
                {
                    "a": a,
                    "b": b,
                    "levenshtein": dist,
                    "jaccard": round(jaccard, 3),
                }
            )
    return sorted(results, key=lambda x: (x["levenshtein"], -x["jaccard"]))


# ---------------------------------------------------------------------------
# Frontmatter theme extraction
# ---------------------------------------------------------------------------


def _extract_themes_from_text(text: str) -> list[str]:
    """Return themes from YAML frontmatter (inline or block list)."""
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return []
    fm = fm_match.group(1)

    # Block list: themes:\n  - a\n  - b
    block_match = _BLOCK_LIST_RE.search(fm)
    if block_match:
        themes: list[str] = []
        for line in block_match.group(1).splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                val = stripped[2:].strip().strip("\"'")
                if val:
                    themes.append(val)
        return themes

    # Inline list: themes: [a, b, c]
    inline_match = _THEMES_RE.search(fm)
    if inline_match:
        raw = inline_match.group(1).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1]
            if not inner.strip():
                return []
            return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]

    return []


# ---------------------------------------------------------------------------
# Core collection
# ---------------------------------------------------------------------------


def collect_themes(root: Path) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return (slug_to_themes, theme_to_slugs) by scanning completed + backlog items."""
    slug_to_themes: dict[str, list[str]] = {}
    theme_to_slugs: dict[str, list[str]] = defaultdict(list)

    dirs = [root / "Research" / "completed", root / "Research" / "backlog"]
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name.lower() in {".gitkeep", "readme.md"}:
                continue
            text = path.read_text(encoding="utf-8")
            themes = _extract_themes_from_text(text)
            if themes:
                slug = path.stem
                slug_to_themes[slug] = themes
                for t in themes:
                    theme_to_slugs[t].append(slug)

    return slug_to_themes, dict(theme_to_slugs)


def find_uncovered_items(root: Path) -> list[str]:
    """Return slugs of items that have no themes: field."""
    dirs = [root / "Research" / "completed", root / "Research" / "backlog"]
    uncovered: list[str] = []
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name.lower() in {".gitkeep", "readme.md"}:
                continue
            text = path.read_text(encoding="utf-8")
            if not _extract_themes_from_text(text) and _FM_RE.match(text):
                uncovered.append(path.stem)
    return sorted(uncovered)


# ---------------------------------------------------------------------------
# Report assembly
# ---------------------------------------------------------------------------


def build_theme_report(root: Path, vocab_path: Path = VOCAB_PATH) -> dict:
    """Build the full theme governance report data structure."""
    slug_to_themes, theme_to_slugs = collect_themes(root)
    uncovered = find_uncovered_items(root)
    canonical_slugs = _load_canonical_slugs(vocab_path)
    near_dupes = find_theme_near_duplicates(canonical_slugs)

    frequency = {t: len(slugs) for t, slugs in sorted(theme_to_slugs.items())}

    # Themes in corpus that are NOT in the canonical vocabulary (stray slugs)
    stray = sorted(t for t in theme_to_slugs if t not in set(canonical_slugs))

    # Canonical themes with zero corpus items
    unused = sorted(t for t in canonical_slugs if t not in theme_to_slugs)

    return {
        "summary": {
            "total_canonical_themes": len(canonical_slugs),
            "total_items_scanned": len(slug_to_themes) + len(uncovered),
            "items_with_themes": len(slug_to_themes),
            "uncovered_count": len(uncovered),
            "near_duplicate_count": len(near_dupes),
            "stray_theme_count": len(stray),
            "unused_canonical_count": len(unused),
        },
        "frequency": frequency,
        "coverage": {
            "uncovered_count": len(uncovered),
            "uncovered_slugs": uncovered,
        },
        "near_duplicates": near_dupes,
        "stray_themes": stray,
        "unused_canonicals": unused,
    }


def render_theme_report_markdown(data: dict) -> str:
    """Render the report as a human-readable Markdown document."""
    s = data["summary"]
    lines = [
        "# Theme Report",
        "",
        f"**Canonical themes in vocabulary:** {s['total_canonical_themes']}  ",
        f"**Items scanned:** {s['total_items_scanned']}  ",
        f"**Items with themes:** {s['items_with_themes']}  ",
        f"**Uncovered items (no themes:):** {s['uncovered_count']}  ",
        f"**Near-duplicate vocabulary candidates:** {s['near_duplicate_count']}  ",
        f"**Stray (non-vocabulary) themes in corpus:** {s['stray_theme_count']}  ",
        f"**Unused canonical themes:** {s['unused_canonical_count']}",
        "",
        "---",
        "",
        "## Coverage — uncovered items",
        "",
        "> Items without a `themes:` field. These should be enriched via `enrich-items.yml`.",
        "> If count is 0, coverage is complete.",
        "",
    ]
    if data["coverage"]["uncovered_slugs"]:
        for slug in data["coverage"]["uncovered_slugs"]:
            lines.append(f"- `{slug}`")
    else:
        lines.append("✅ All items have `themes:` — coverage is complete.")

    lines += [
        "",
        "---",
        "",
        "## Near-duplicate vocabulary candidates",
        "",
        "> Canonical slugs with Levenshtein distance ≤ 2 or token Jaccard ≥ 0.6.",
        "> Candidates for future vocabulary consolidation (requires ≥3-item policy check).",
        "",
    ]
    if data["near_duplicates"]:
        lines += ["| Slug A | Slug B | Levenshtein | Jaccard |", "|---|---|---|---|"]
        for d in data["near_duplicates"]:
            lines.append(f"| `{d['a']}` | `{d['b']}` | {d['levenshtein']} | {d['jaccard']} |")
    else:
        lines.append("_None found._")

    lines += [
        "",
        "---",
        "",
        "## Stray themes (not in canonical vocabulary)",
        "",
        "> Theme slugs found in corpus items that are not in `docs/themes-vocabulary.md`.",
        "> These may be pre-migration artefacts or new candidate themes.",
        "",
    ]
    if data["stray_themes"]:
        lines.append(", ".join(f"`{t}`" for t in data["stray_themes"]))
    else:
        lines.append("_None found — all corpus themes are in the vocabulary._")

    lines += [
        "",
        "---",
        "",
        "## Unused canonical themes",
        "",
        "> Canonical slugs with zero corpus items. Consider whether they are",
        "> still needed or should be removed from the vocabulary.",
        "",
    ]
    if data["unused_canonicals"]:
        lines.append(", ".join(f"`{t}`" for t in data["unused_canonicals"]))
    else:
        lines.append("_All canonical themes are in use._")

    lines += [
        "",
        "---",
        "",
        "## Theme frequency",
        "",
        "| Theme | Item count |",
        "|---|---|",
    ]
    for theme, count in sorted(data["frequency"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| `{theme}` | {count} |")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate theme governance report.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root directory (default: parent of scripts/)",
    )
    parser.add_argument(
        "--vocab",
        type=Path,
        default=None,
        help="Path to themes-vocabulary.md (default: docs/themes-vocabulary.md)",
    )
    args = parser.parse_args()

    root: Path = args.root.resolve()
    vocab_path = args.vocab or (root / "docs" / "themes-vocabulary.md")
    state_dir = root / "state"
    state_dir.mkdir(exist_ok=True)

    print("Scanning research items…")
    data = build_theme_report(root, vocab_path)
    s = data["summary"]
    print(f"  {s['total_items_scanned']} items scanned")
    print(f"  {s['items_with_themes']} items with themes")
    print(f"  {s['uncovered_count']} items uncovered")
    print(f"  {s['near_duplicate_count']} near-duplicate vocabulary candidates")
    print(f"  {s['stray_theme_count']} stray themes")
    print(f"  {s['unused_canonical_count']} unused canonical themes")

    json_path = state_dir / "theme_report.json"
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Written: {json_path}")

    md_path = state_dir / "theme_report.md"
    md_path.write_text(render_theme_report_markdown(data), encoding="utf-8")
    print(f"Written: {md_path}")


if __name__ == "__main__":
    main()

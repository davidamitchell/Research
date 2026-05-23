"""Tests for scripts/theme_report.py — theme governance report."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from theme_report import (  # noqa: E402
    build_theme_report,
    collect_themes,
    find_theme_near_duplicates,
    find_uncovered_items,
    render_theme_report_markdown,
)

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "themes-vocabulary.md"
REPO_ROOT = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _item(tmp_path: Path, name: str, frontmatter: str) -> Path:
    path = tmp_path / name
    fm = textwrap.dedent(frontmatter).strip()
    path.write_text(f"---\n{fm}\n---\n\n# Test\n", encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# collect_themes
# ---------------------------------------------------------------------------


def test_collect_themes_reads_themes_field(tmp_path: Path) -> None:
    """collect_themes extracts themes: values from items."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "Test"
        status: completed
        themes: [agentic-ai, governance-policy]
        """,
    )
    slug_to_themes, theme_to_slugs = collect_themes(tmp_path)
    assert "item" in slug_to_themes
    assert "agentic-ai" in slug_to_themes["item"]
    assert "governance-policy" in slug_to_themes["item"]
    assert "item" in theme_to_slugs["agentic-ai"]


def test_collect_themes_skips_items_without_themes(tmp_path: Path) -> None:
    """Items without themes: field are tracked separately as uncovered."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "Test"
        status: completed
        """,
    )
    slug_to_themes, theme_to_slugs = collect_themes(tmp_path)
    assert "item" not in slug_to_themes


# ---------------------------------------------------------------------------
# find_uncovered_items
# ---------------------------------------------------------------------------


def test_find_uncovered_items_returns_items_without_themes(tmp_path: Path) -> None:
    """find_uncovered_items returns slugs of items missing themes: field."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "with-themes.md", "title: A\nstatus: completed\nthemes: [agentic-ai]")
    _item(d, "without-themes.md", "title: B\nstatus: completed")
    uncovered = find_uncovered_items(tmp_path)
    assert "without-themes" in uncovered
    assert "with-themes" not in uncovered


def test_find_uncovered_items_includes_backlog(tmp_path: Path) -> None:
    """find_uncovered_items also scans backlog/ items."""
    d = tmp_path / "Research" / "backlog"
    d.mkdir(parents=True)
    _item(d, "backlog-item.md", "title: Backlog\nstatus: backlog")
    uncovered = find_uncovered_items(tmp_path)
    assert "backlog-item" in uncovered


# ---------------------------------------------------------------------------
# find_theme_near_duplicates — uses Levenshtein + token Jaccard
# ---------------------------------------------------------------------------


def test_find_near_duplicates_detects_close_slugs() -> None:
    """Slugs differing by ≤ 2 edits are near-duplicate candidates."""
    # "security-risk" vs "security-risks" — Levenshtein distance 1
    result = find_theme_near_duplicates(["security-risk", "security-risks", "governance-policy"])
    pairs = [(r["a"], r["b"]) for r in result]
    assert ("security-risk", "security-risks") in pairs or (
        "security-risks",
        "security-risk",
    ) in pairs


def test_find_near_duplicates_detects_high_jaccard() -> None:
    """Slugs with token Jaccard ≥ 0.6 are near-duplicate candidates."""
    # "ai-risk" vs "ai-risk-management": tokens {ai,risk} vs {ai,risk,management}
    # Jaccard = 2/3 ≈ 0.67 ≥ 0.6
    result = find_theme_near_duplicates(["ai-risk", "ai-risk-management"])
    assert len(result) >= 1


def test_find_near_duplicates_excludes_dissimilar_slugs() -> None:
    """Clearly different slugs must not be flagged as near-duplicates."""
    result = find_theme_near_duplicates(["agentic-ai", "knowledge-graphs", "governance-policy"])
    assert result == []


# ---------------------------------------------------------------------------
# build_theme_report
# ---------------------------------------------------------------------------


def test_build_theme_report_includes_coverage(tmp_path: Path) -> None:
    """build_theme_report includes a coverage section with missing-themes items."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "has-themes.md", "title: A\nstatus: completed\nthemes: [agentic-ai]")
    _item(d, "no-themes.md", "title: B\nstatus: completed")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    assert data["coverage"]["uncovered_count"] == 1
    assert "no-themes" in data["coverage"]["uncovered_slugs"]


def test_build_theme_report_summary_has_total_themes(tmp_path: Path) -> None:
    """build_theme_report summary includes total_canonical_themes from vocabulary."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed\nthemes: [agentic-ai]")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    assert data["summary"]["total_canonical_themes"] >= 16


def test_build_theme_report_frequency_populated(tmp_path: Path) -> None:
    """build_theme_report includes theme frequency counts."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed\nthemes: [agentic-ai, governance-policy]")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    assert data["frequency"].get("agentic-ai", 0) >= 1


# ---------------------------------------------------------------------------
# render_theme_report_markdown
# ---------------------------------------------------------------------------


def test_render_theme_report_markdown_returns_string(tmp_path: Path) -> None:
    """render_theme_report_markdown must return a non-empty markdown string."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed\nthemes: [agentic-ai]")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    md = render_theme_report_markdown(data)
    assert isinstance(md, str)
    assert len(md) > 100
    assert "# Theme Report" in md


def test_render_theme_report_includes_coverage_section(tmp_path: Path) -> None:
    """Rendered markdown must have a coverage section."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    md = render_theme_report_markdown(data)
    assert "coverage" in md.lower() or "uncovered" in md.lower()


# ---------------------------------------------------------------------------
# Integration: runs against actual repo corpus
# ---------------------------------------------------------------------------


def test_build_theme_report_runs_on_corpus() -> None:
    """build_theme_report must run to completion on the real corpus without errors."""
    data = build_theme_report(REPO_ROOT, VOCAB_PATH)
    assert "summary" in data
    assert "frequency" in data
    assert "coverage" in data
    assert "near_duplicates" in data
    # After W-0078 migration, items with empty themes: [] are still reported as
    # uncovered; those need the enrich-items.yml workflow. Allow up to 10.
    assert data["coverage"]["uncovered_count"] <= 10, (
        f"Too many uncovered items ({data['coverage']['uncovered_count']}): "
        f"{data['coverage']['uncovered_slugs']}"
    )

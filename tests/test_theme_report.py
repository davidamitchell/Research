"""Tests for scripts/theme_report.py — theme governance report."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from theme_report import (  # noqa: E402
    build_theme_report,
    classify_stray_themes,
    collect_themes,
    find_theme_near_duplicates,
    find_uncovered_items,
    load_themes_vocabulary,
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
# Vocabulary loading and stray-theme classification
# ---------------------------------------------------------------------------


def test_load_themes_vocabulary_maps_aliases_to_canonical() -> None:
    """load_themes_vocabulary must return a reverse alias → canonical map."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    assert vocab["agentic-ai"] == "agentic-ai"
    assert vocab["prompt-engineering"] == "llm-reasoning"
    assert vocab["workflow-automation"] == "tools-infrastructure"


def test_classify_stray_themes_maps_known_aliases() -> None:
    """A stray slug that is a known alias maps with high confidence."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonical_slugs = [s for s, c in vocab.items() if s == c]
    mappable, gaps = classify_stray_themes(["workflow-automation"], vocab, canonical_slugs)
    assert len(mappable) == 1
    assert mappable[0]["stray"] == "workflow-automation"
    assert mappable[0]["canonical"] == "tools-infrastructure"
    assert mappable[0]["confidence"] == "high"
    assert "alias" in mappable[0]["basis"]
    assert gaps == []


def test_classify_stray_themes_uses_token_jaccard_fallback() -> None:
    """A stray slug with no exact alias match falls back to token Jaccard."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonical_slugs = [s for s, c in vocab.items() if s == c]
    # "ai-governance" is a known alias, so use a synthetic token-overlapping slug
    # that is not in the vocabulary to force the heuristic path.
    mappable, gaps = classify_stray_themes(["policy-governance-ai"], vocab, canonical_slugs)
    assert len(mappable) == 1
    assert mappable[0]["canonical"] == "governance-policy"
    assert "Jaccard" in mappable[0]["basis"]


def test_classify_stray_themes_leaves_unmatched_as_gaps() -> None:
    """Stray slugs that cannot be matched are returned as genuine gaps."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonical_slugs = [s for s, c in vocab.items() if s == c]
    mappable, gaps = classify_stray_themes(["xyzzy-nonsense-theme"], vocab, canonical_slugs)
    assert mappable == []
    assert gaps == ["xyzzy-nonsense-theme"]


def test_build_theme_report_includes_mappable_strays(tmp_path: Path) -> None:
    """build_theme_report includes mappable_strays and candidate_aliases."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed\nthemes: [workflow-automation]")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    assert data["summary"]["mappable_stray_count"] == 1
    assert data["summary"]["genuine_gap_count"] == 0
    assert len(data["mappable_strays"]) == 1
    assert data["mappable_strays"][0]["stray"] == "workflow-automation"
    # workflow-automation is already a known alias, so no candidate_aliases entry
    assert data["candidate_aliases"] == {}


def test_render_theme_report_includes_mappable_section(tmp_path: Path) -> None:
    """Rendered markdown includes the mappable stray themes table."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(d, "item.md", "title: A\nstatus: completed\nthemes: [workflow-automation]")
    data = build_theme_report(tmp_path, VOCAB_PATH)
    md = render_theme_report_markdown(data)
    assert "## Mappable stray themes" in md
    assert "workflow-automation" in md
    assert "tools-infrastructure" in md


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
    assert "mappable_strays" in data
    assert "candidate_aliases" in data
    # After W-0078 migration, items with empty themes: [] are still reported as
    # uncovered; those need the enrich-items.yml workflow. Allow up to 10.
    assert data["coverage"]["uncovered_count"] <= 10, (
        f"Too many uncovered items ({data['coverage']['uncovered_count']}): "
        f"{data['coverage']['uncovered_slugs']}"
    )
    # Most current stray themes should be mappable via the expanded alias map.
    assert data["summary"]["genuine_gap_count"] <= 5, (
        f"Too many genuine gap themes ({data['summary']['genuine_gap_count']}): "
        f"{data['stray_themes']}"
    )

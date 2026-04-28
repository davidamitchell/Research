"""Tests for scripts/tag_report.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# Make the scripts/ directory importable in tests
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from tag_report import (  # noqa: E402
    _extract_tags,
    _prefix_suffix_overlap,
    build_report,
    compute_cooccurrence,
    find_near_duplicates,
    find_strong_pairs,
    is_near_duplicate,
    levenshtein,
    render_markdown,
)

# ---------------------------------------------------------------------------
# Levenshtein distance
# ---------------------------------------------------------------------------


def test_levenshtein_identical() -> None:
    assert levenshtein("ai", "ai") == 0


def test_levenshtein_empty_strings() -> None:
    assert levenshtein("", "") == 0
    assert levenshtein("abc", "") == 3
    assert levenshtein("", "abc") == 3


def test_levenshtein_single_edit() -> None:
    assert levenshtein("ai", "ci") == 1
    assert levenshtein("workflow", "workflows") == 1
    assert levenshtein("memory-system", "memory-systems") == 1


def test_levenshtein_distance_two() -> None:
    assert levenshtein("ab", "cd") == 2


# ---------------------------------------------------------------------------
# Prefix/suffix overlap
# ---------------------------------------------------------------------------


def test_prefix_suffix_overlap_identical() -> None:
    assert _prefix_suffix_overlap("ai", "ai") == 1.0


def test_prefix_suffix_overlap_suffix_match() -> None:
    # "workflow" and "workflows" share prefix 8/9 = 0.889
    ratio = _prefix_suffix_overlap("workflow", "workflows")
    assert ratio == pytest.approx(8 / 9)


def test_prefix_suffix_overlap_empty() -> None:
    assert _prefix_suffix_overlap("", "ai") == 0.0
    assert _prefix_suffix_overlap("ai", "") == 0.0


# ---------------------------------------------------------------------------
# is_near_duplicate
# ---------------------------------------------------------------------------


def test_is_near_duplicate_by_levenshtein() -> None:
    assert is_near_duplicate("ai", "ci")  # distance 1
    assert is_near_duplicate("workflow", "workflows")  # distance 1


def test_is_near_duplicate_by_overlap() -> None:
    assert is_near_duplicate("memory-system", "memory-systems")  # overlap ≥ 0.8


def test_is_near_duplicate_false_for_unrelated() -> None:
    assert not is_near_duplicate("governance", "python")


# ---------------------------------------------------------------------------
# Tag extraction from frontmatter
# ---------------------------------------------------------------------------


def test_extract_tags_inline_list(tmp_path: Path) -> None:
    md = "---\ntitle: Test\ntags: [ai, governance, python]\n---\n# Body\n"
    path = tmp_path / "item.md"
    path.write_text(md)
    assert _extract_tags(path) == ["ai", "governance", "python"]


def test_extract_tags_empty_list(tmp_path: Path) -> None:
    md = "---\ntitle: Test\ntags: []\n---\n# Body\n"
    path = tmp_path / "item.md"
    path.write_text(md)
    assert _extract_tags(path) == []


def test_extract_tags_no_frontmatter(tmp_path: Path) -> None:
    md = "# No frontmatter here\n"
    path = tmp_path / "item.md"
    path.write_text(md)
    assert _extract_tags(path) == []


def test_extract_tags_no_tags_field(tmp_path: Path) -> None:
    md = "---\ntitle: Test\nstatus: completed\n---\n# Body\n"
    path = tmp_path / "item.md"
    path.write_text(md)
    assert _extract_tags(path) == []


# ---------------------------------------------------------------------------
# Co-occurrence matrix
# ---------------------------------------------------------------------------


def test_compute_cooccurrence_basic() -> None:
    slug_to_tags = {
        "item-a": ["ai", "governance"],
        "item-b": ["ai", "python"],
        "item-c": ["governance", "python"],
    }
    co = compute_cooccurrence(slug_to_tags)
    assert co["ai"]["governance"] == 1
    assert co["ai"]["python"] == 1
    assert co["governance"]["python"] == 1


def test_compute_cooccurrence_multiple_shared_items() -> None:
    slug_to_tags = {
        "item-a": ["ai", "governance"],
        "item-b": ["ai", "governance"],
        "item-c": ["ai"],
    }
    co = compute_cooccurrence(slug_to_tags)
    assert co["ai"]["governance"] == 2
    assert co["governance"]["ai"] == 2


def test_compute_cooccurrence_single_tag_items() -> None:
    slug_to_tags = {"item-a": ["ai"], "item-b": ["governance"]}
    co = compute_cooccurrence(slug_to_tags)
    # No pairs possible with single-tag items
    assert co.get("ai", {}).get("governance", 0) == 0


# ---------------------------------------------------------------------------
# Strong synonym pairs
# ---------------------------------------------------------------------------


def test_find_strong_pairs_detects_synonyms() -> None:
    # Two tags that always appear together in 3+ items
    tag_to_slugs = {
        "coase": ["a", "b", "c"],
        "institutional-economics": ["a", "b", "c"],
        "python": ["a", "b", "c", "d"],
    }
    co = {
        "coase": {"institutional-economics": 3, "python": 3},
        "institutional-economics": {"coase": 3, "python": 3},
        "python": {"coase": 3, "institutional-economics": 3},
    }
    pairs = find_strong_pairs(tag_to_slugs, co, threshold=0.8, min_cooccurrence=2)
    pair_tags = {(p["tag_a"], p["tag_b"]) for p in pairs}
    assert ("coase", "institutional-economics") in pair_tags


def test_find_strong_pairs_excludes_below_threshold() -> None:
    # python appears in 4 items but only co-occurs with governance in 1
    tag_to_slugs = {
        "ai": ["a", "b"],
        "python": ["a", "b", "c", "d"],
    }
    co = {"ai": {"python": 2}, "python": {"ai": 2}}
    pairs = find_strong_pairs(tag_to_slugs, co, threshold=0.8, min_cooccurrence=2)
    # ai: 2/2=1.0, python: 2/4=0.5 < 0.8 → not a strong pair
    assert len(pairs) == 0


def test_find_strong_pairs_requires_min_cooccurrence() -> None:
    tag_to_slugs = {"a": ["x"], "b": ["x"]}
    co = {"a": {"b": 1}, "b": {"a": 1}}
    # min_cooccurrence=2 means co=1 pairs are excluded
    pairs = find_strong_pairs(tag_to_slugs, co, threshold=0.8, min_cooccurrence=2)
    assert len(pairs) == 0


# ---------------------------------------------------------------------------
# Near duplicates
# ---------------------------------------------------------------------------


def test_find_near_duplicates_detects_plural_forms() -> None:
    tag_to_slugs = {
        "workflow": ["a", "b", "c", "d", "e", "f", "g", "h"],
        "workflows": ["a", "b"],
    }
    dupes = find_near_duplicates(tag_to_slugs)
    pairs = [(d["tag_a"], d["tag_b"]) for d in dupes]
    assert ("workflow", "workflows") in pairs


def test_find_near_duplicates_excludes_singletons() -> None:
    # Tags appearing in only 1 item should not appear in near-duplicates
    tag_to_slugs = {
        "governance": ["a"],
        "governanc": ["b"],
    }
    dupes = find_near_duplicates(tag_to_slugs)
    assert len(dupes) == 0


def test_find_near_duplicates_unrelated_tags() -> None:
    tag_to_slugs = {
        "governance": ["a", "b"],
        "python": ["a", "b"],
    }
    dupes = find_near_duplicates(tag_to_slugs)
    assert len(dupes) == 0


# ---------------------------------------------------------------------------
# Full report and Markdown output
# ---------------------------------------------------------------------------


def test_build_report_structure(tmp_path: Path) -> None:
    """build_report returns a dict with the expected top-level keys."""
    # Create minimal fixture file structure
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    backlog = tmp_path / "Research" / "backlog"
    backlog.mkdir(parents=True)

    (completed / "item-a.md").write_text("---\ntitle: A\ntags: [ai, governance]\n---\n# A\n")
    (completed / "item-b.md").write_text("---\ntitle: B\ntags: [ai, python]\n---\n# B\n")
    (backlog / "item-c.md").write_text("---\ntitle: C\ntags: [governance, python]\n---\n# C\n")

    data = build_report(tmp_path)
    assert "summary" in data
    assert "frequency" in data
    assert "singletons" in data
    assert "strong_pairs" in data
    assert "near_duplicates" in data
    assert data["summary"]["total_items_scanned"] == 3
    assert data["summary"]["total_tags"] == 3
    assert data["frequency"]["ai"] == 2
    assert data["frequency"]["governance"] == 2
    assert data["frequency"]["python"] == 2
    assert data["singletons"] == []  # all tags appear ≥ 2 times


def test_build_report_singletons(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    (tmp_path / "Research" / "backlog").mkdir(parents=True)
    (completed / "item-a.md").write_text("---\ntitle: A\ntags: [ai, rare-tag]\n---\n# A\n")
    (completed / "item-b.md").write_text("---\ntitle: B\ntags: [ai, another-rare]\n---\n# B\n")
    data = build_report(tmp_path)
    assert "rare-tag" in data["singletons"]
    assert "another-rare" in data["singletons"]
    assert "ai" not in data["singletons"]


def test_render_markdown_sections(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    (tmp_path / "Research" / "backlog").mkdir(parents=True)
    (completed / "item-a.md").write_text("---\ntitle: A\ntags: [ai, governance]\n---\n# A\n")
    data = build_report(tmp_path)
    md = render_markdown(data)
    assert "# Tag Report" in md
    assert "## Strong synonym pairs" in md
    assert "## Near-duplicate candidates" in md
    assert "## Singleton tags" in md
    assert "## Tag frequency" in md


def test_main_writes_output_files(tmp_path: Path) -> None:
    """main() writes both output files to state/."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    (tmp_path / "Research" / "backlog").mkdir(parents=True)
    (completed / "item-a.md").write_text("---\ntitle: A\ntags: [ai]\n---\n# A\n")

    from tag_report import main

    sys.argv = ["tag_report.py", "--root", str(tmp_path)]
    main()

    json_path = tmp_path / "state" / "tag_report.json"
    md_path = tmp_path / "state" / "tag_report.md"
    assert json_path.exists()
    assert md_path.exists()

    data = json.loads(json_path.read_text())
    assert data["summary"]["total_items_scanned"] == 1
    assert data["summary"]["total_tags"] == 1

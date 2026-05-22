"""Tests for scripts/aggregate_gaps.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Make scripts/ importable in tests (mirrors test_tag_report.py pattern)
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from aggregate_gaps import (  # noqa: E402
    aggregate_gaps,
    extract_gaps,
    normalize_gap,
    write_registry,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_ITEM_WITH_GAPS = """\
---
title: "Test Item"
added: 2026-01-01
status: completed
gaps:
  - How does X scale beyond 1000 items?
  - What happens when two agents conflict?
  - Is there a lower-cost alternative?
---

# Test Item

## Findings

placeholder
"""

_ITEM_WITH_INLINE_GAPS = """\
---
title: "Inline Gaps Item"
added: 2026-01-02
status: completed
gaps: ["How does X scale beyond 1000 items?", "Why is Y expensive?"]
---

# Inline Gaps Item
"""

_ITEM_WITHOUT_GAPS = """\
---
title: "No Gaps Item"
added: 2026-01-03
status: completed
tags: [agentic-ai]
---

# No Gaps Item
"""

_ITEM_EMPTY_GAPS = """\
---
title: "Empty Gaps Item"
added: 2026-01-04
status: completed
gaps: []
---

# Empty Gaps Item
"""


# ---------------------------------------------------------------------------
# extract_gaps
# ---------------------------------------------------------------------------


def test_extract_gaps_returns_list_from_block_yaml(tmp_path: Path) -> None:
    p = tmp_path / "item.md"
    p.write_text(_ITEM_WITH_GAPS, encoding="utf-8")
    result = extract_gaps(p)
    assert result == [
        "How does X scale beyond 1000 items?",
        "What happens when two agents conflict?",
        "Is there a lower-cost alternative?",
    ]


def test_extract_gaps_returns_list_from_inline_yaml(tmp_path: Path) -> None:
    p = tmp_path / "item.md"
    p.write_text(_ITEM_WITH_INLINE_GAPS, encoding="utf-8")
    result = extract_gaps(p)
    assert "How does X scale beyond 1000 items?" in result
    assert "Why is Y expensive?" in result
    assert len(result) == 2


def test_extract_gaps_returns_empty_list_when_field_absent(tmp_path: Path) -> None:
    p = tmp_path / "item.md"
    p.write_text(_ITEM_WITHOUT_GAPS, encoding="utf-8")
    assert extract_gaps(p) == []


def test_extract_gaps_returns_empty_list_for_empty_field(tmp_path: Path) -> None:
    p = tmp_path / "item.md"
    p.write_text(_ITEM_EMPTY_GAPS, encoding="utf-8")
    assert extract_gaps(p) == []


def test_extract_gaps_returns_empty_list_when_no_frontmatter(tmp_path: Path) -> None:
    p = tmp_path / "item.md"
    p.write_text("# No frontmatter\n\nBody text.\n", encoding="utf-8")
    assert extract_gaps(p) == []


def test_extract_gaps_skips_gitkeep(tmp_path: Path) -> None:
    p = tmp_path / ".gitkeep"
    p.write_text("", encoding="utf-8")
    assert extract_gaps(p) == []


# ---------------------------------------------------------------------------
# normalize_gap
# ---------------------------------------------------------------------------


def test_normalize_gap_strips_whitespace() -> None:
    assert normalize_gap("  How does X scale?  ") == "how does x scale?"


def test_normalize_gap_lowercases() -> None:
    assert normalize_gap("How Does X Scale?") == "how does x scale?"


def test_normalize_gap_already_normalized() -> None:
    assert normalize_gap("how does x scale?") == "how does x scale?"


def test_normalize_gap_empty_string() -> None:
    assert normalize_gap("") == ""


# ---------------------------------------------------------------------------
# aggregate_gaps
# ---------------------------------------------------------------------------


def _write_item(path: Path, slug: str, gaps: list[str]) -> None:
    """Write a minimal completed item with the given gaps."""
    gaps_yaml = "\n".join(f"  - {g}" for g in gaps) if gaps else "  []"
    gaps_block = f"gaps:\n{gaps_yaml}" if gaps else "gaps: []"
    path.write_text(
        f"---\ntitle: '{slug}'\nadded: 2026-01-01\nstatus: completed\n{gaps_block}\n---\n\n# {slug}\n",
        encoding="utf-8",
    )


def test_aggregate_gaps_empty_directory(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    (completed / ".gitkeep").write_text("", encoding="utf-8")
    result = aggregate_gaps(completed)
    assert result["total_gaps"] == 0
    assert result["promoted_count"] == 0
    assert result["gaps"] == []


def test_aggregate_gaps_single_item_no_promote(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    _write_item(completed / "item-a.md", "item-a", ["How does X scale?"])
    result = aggregate_gaps(completed)
    assert result["total_gaps"] == 1
    assert result["promoted_count"] == 0
    assert result["gaps"][0]["promote"] is False
    assert result["gaps"][0]["count"] == 1


def test_aggregate_gaps_counts_matching_gaps(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    gap = "How does X scale beyond 1000 items?"
    _write_item(completed / "item-a.md", "item-a", [gap])
    _write_item(completed / "item-b.md", "item-b", [gap])
    _write_item(completed / "item-c.md", "item-c", [gap])
    result = aggregate_gaps(completed)
    matching = [g for g in result["gaps"] if g["count"] == 3]
    assert len(matching) == 1
    assert set(matching[0]["items"]) == {"item-a", "item-b", "item-c"}


def test_aggregate_gaps_promotes_at_threshold(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    gap = "What is the minimum viable config?"
    for i in range(3):
        _write_item(completed / f"item-{i}.md", f"item-{i}", [gap])
    result = aggregate_gaps(completed)
    assert result["promoted_count"] == 1
    assert result["gaps"][0]["promote"] is True


def test_aggregate_gaps_no_promote_below_threshold(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    gap = "Rare gap question?"
    _write_item(completed / "item-a.md", "item-a", [gap])
    _write_item(completed / "item-b.md", "item-b", [gap])
    result = aggregate_gaps(completed)
    assert result["gaps"][0]["promote"] is False
    assert result["promoted_count"] == 0


def test_aggregate_gaps_normalizes_before_counting(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    # Same gap with different capitalisation — should be counted as one
    _write_item(completed / "item-a.md", "item-a", ["How does X scale?"])
    _write_item(completed / "item-b.md", "item-b", ["how does x scale?"])
    _write_item(completed / "item-c.md", "item-c", ["HOW DOES X SCALE?"])
    result = aggregate_gaps(completed)
    assert len(result["gaps"]) == 1
    assert result["gaps"][0]["count"] == 3


def test_aggregate_gaps_sorted_by_count_descending(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    rare_gap = "Rare gap only once?"
    common_gap = "Common gap in many items?"
    _write_item(completed / "item-a.md", "item-a", [rare_gap, common_gap])
    _write_item(completed / "item-b.md", "item-b", [common_gap])
    _write_item(completed / "item-c.md", "item-c", [common_gap])
    result = aggregate_gaps(completed)
    counts = [g["count"] for g in result["gaps"]]
    assert counts == sorted(counts, reverse=True)


def test_aggregate_gaps_custom_threshold(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    gap = "Gap that appears twice?"
    _write_item(completed / "item-a.md", "item-a", [gap])
    _write_item(completed / "item-b.md", "item-b", [gap])
    # With default threshold=3: not promoted
    result_default = aggregate_gaps(completed, threshold=3)
    assert result_default["gaps"][0]["promote"] is False
    # With threshold=2: promoted
    result_low = aggregate_gaps(completed, threshold=2)
    assert result_low["gaps"][0]["promote"] is True


def test_aggregate_gaps_output_schema(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    _write_item(completed / "item-a.md", "item-a", ["A gap?"])
    result = aggregate_gaps(completed)
    assert "generated" in result
    assert "total_gaps" in result
    assert "promoted_count" in result
    assert "gaps" in result
    g = result["gaps"][0]
    assert "text" in g
    assert "count" in g
    assert "items" in g
    assert "promote" in g


# ---------------------------------------------------------------------------
# write_registry
# ---------------------------------------------------------------------------


def test_write_registry_creates_json_file(tmp_path: Path) -> None:
    registry = {
        "generated": "2026-05-22",
        "total_gaps": 1,
        "promoted_count": 0,
        "gaps": [{"text": "A gap?", "count": 1, "items": ["item-a"], "promote": False}],
    }
    out = tmp_path / "gap_registry.json"
    write_registry(registry, out)
    assert out.exists()
    loaded = json.loads(out.read_text(encoding="utf-8"))
    assert loaded["total_gaps"] == 1


def test_write_registry_creates_parent_directory(tmp_path: Path) -> None:
    registry = {"generated": "2026-05-22", "total_gaps": 0, "promoted_count": 0, "gaps": []}
    out = tmp_path / "state" / "gap_registry.json"
    write_registry(registry, out)
    assert out.exists()

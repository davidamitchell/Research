"""Tests for scripts/aggregate_gaps.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Make scripts/ importable in tests
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from aggregate_gaps import (  # noqa: E402
    PROMOTE_THRESHOLD,
    _extract_frontmatter,
    _normalise,
    _parse_gaps,
    aggregate_gaps,
    main,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

TEMPLATE_PATH = Path(__file__).parent.parent / "Research" / "_template.md"


def _make_item(tmp_path: Path, slug: str, gaps: list[str]) -> Path:
    """Write a minimal research item with the given gap strings to tmp_path."""
    gaps_yaml = "gaps:\n" + "".join(f'  - "{g}"\n' for g in gaps) if gaps else "gaps: []\n"
    content = f"---\ntitle: {slug}\nstatus: completed\n{gaps_yaml}---\n\n# Body\n"
    path = tmp_path / f"{slug}.md"
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Template field presence
# ---------------------------------------------------------------------------


def test_template_has_gaps_field() -> None:
    """Research/_template.md must contain a `gaps:` field in the frontmatter."""
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    fm = _extract_frontmatter(text)
    assert fm is not None, "Template has no YAML frontmatter"
    assert "gaps:" in fm, "Template frontmatter must contain a 'gaps:' field"


# ---------------------------------------------------------------------------
# Frontmatter / gap parsing
# ---------------------------------------------------------------------------


def test_parse_gaps_block_list(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "item-a", ["Why does X happen?", "What is the scale of Y?"])
    text = path.read_text()
    fm = _extract_frontmatter(text)
    assert fm is not None
    gaps = _parse_gaps(fm)
    assert gaps == ["Why does X happen?", "What is the scale of Y?"]


def test_parse_gaps_inline_list(tmp_path: Path) -> None:
    content = "---\ntitle: T\ngaps: [gap one, gap two]\n---\n# B\n"
    path = tmp_path / "item.md"
    path.write_text(content)
    fm = _extract_frontmatter(path.read_text())
    assert fm is not None
    assert _parse_gaps(fm) == ["gap one", "gap two"]


def test_parse_gaps_empty() -> None:
    fm = "title: T\nstatus: completed\ngaps: []\n"
    assert _parse_gaps(fm) == []


def test_parse_gaps_missing_field() -> None:
    fm = "title: T\nstatus: completed\n"
    assert _parse_gaps(fm) == []


def test_extract_frontmatter_absent() -> None:
    assert _extract_frontmatter("# No frontmatter\n") is None


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------


def test_normalise_strips_and_lowercases() -> None:
    assert _normalise("  Hello World  ") == "hello world"
    assert _normalise("UPPER CASE GAP") == "upper case gap"


# ---------------------------------------------------------------------------
# aggregate_gaps output schema
# ---------------------------------------------------------------------------


def test_aggregate_gaps_output_schema(tmp_path: Path) -> None:
    """aggregate_gaps returns a dict where each entry has count, items, promote."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", ["What is the long-term cost?"])
    _make_item(completed, "item-b", ["What is the long-term cost?"])

    result = aggregate_gaps(completed)

    assert len(result) == 1
    key = next(iter(result))
    entry = result[key]
    assert "count" in entry
    assert "items" in entry
    assert "promote" in entry
    assert isinstance(entry["count"], int)
    assert isinstance(entry["items"], list)
    assert isinstance(entry["promote"], bool)


def test_aggregate_gaps_empty_directory(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    result = aggregate_gaps(completed)
    assert result == {}


def test_aggregate_gaps_no_gaps_in_items(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", [])
    _make_item(completed, "item-b", [])
    result = aggregate_gaps(completed)
    assert result == {}


# ---------------------------------------------------------------------------
# Promotion threshold logic
# ---------------------------------------------------------------------------


def test_promote_threshold_true(tmp_path: Path) -> None:
    """A gap appearing in PROMOTE_THRESHOLD (3) or more items gets promote: true."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    gap = "How does adoption scale affect regulation?"
    for i in range(PROMOTE_THRESHOLD):
        _make_item(completed, f"item-{i}", [gap])

    result = aggregate_gaps(completed)
    assert len(result) == 1
    entry = next(iter(result.values()))
    assert entry["count"] == PROMOTE_THRESHOLD
    assert entry["promote"] is True


def test_promote_threshold_false(tmp_path: Path) -> None:
    """A gap appearing in fewer than PROMOTE_THRESHOLD items gets promote: false."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    gap = "What is the regulatory baseline?"
    for i in range(PROMOTE_THRESHOLD - 1):
        _make_item(completed, f"item-{i}", [gap])

    result = aggregate_gaps(completed)
    assert len(result) == 1
    entry = next(iter(result.values()))
    assert entry["count"] == PROMOTE_THRESHOLD - 1
    assert entry["promote"] is False


def test_promote_threshold_above(tmp_path: Path) -> None:
    """A gap appearing in more than PROMOTE_THRESHOLD items is also promoted."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    gap = "Which jurisdictions have comparable frameworks?"
    for i in range(5):
        _make_item(completed, f"item-{i}", [gap])

    result = aggregate_gaps(completed)
    entry = next(iter(result.values()))
    assert entry["count"] == 5
    assert entry["promote"] is True


# ---------------------------------------------------------------------------
# Near-duplicate normalisation
# ---------------------------------------------------------------------------


def test_near_duplicate_normalization_casing(tmp_path: Path) -> None:
    """Same gap string with different casing should be counted once."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", ["What is the long-term cost?"])
    _make_item(completed, "item-b", ["WHAT IS THE LONG-TERM COST?"])
    _make_item(completed, "item-c", ["What Is The Long-Term Cost?"])

    result = aggregate_gaps(completed)
    assert len(result) == 1
    entry = next(iter(result.values()))
    assert entry["count"] == 3
    assert entry["promote"] is True


def test_near_duplicate_normalization_whitespace(tmp_path: Path) -> None:
    """Same gap string with leading/trailing whitespace should be counted once."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", ["  What is the scope? "])
    _make_item(completed, "item-b", ["What is the scope?"])

    result = aggregate_gaps(completed)
    assert len(result) == 1
    entry = next(iter(result.values()))
    assert entry["count"] == 2


def test_distinct_gaps_counted_separately(tmp_path: Path) -> None:
    """Different gap strings must remain as separate entries."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", ["Gap about cost?"])
    _make_item(completed, "item-b", ["Gap about timeline?"])

    result = aggregate_gaps(completed)
    assert len(result) == 2


# ---------------------------------------------------------------------------
# main() writes gap_registry.json
# ---------------------------------------------------------------------------


def test_main_writes_output_json(tmp_path: Path) -> None:
    """main() produces a valid gap_registry.json with the expected top-level keys."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", ["Will cost decrease over time?"])

    output_path = tmp_path / "state" / "gap_registry.json"

    sys.argv = [
        "aggregate_gaps.py",
        "--completed-dir",
        str(completed),
        "--output",
        str(output_path),
    ]
    main()

    assert output_path.exists()
    data = json.loads(output_path.read_text())
    assert "gaps" in data
    assert "generated_at" in data
    assert isinstance(data["gaps"], dict)


def test_main_exits_cleanly_with_no_gaps(tmp_path: Path) -> None:
    """main() exits cleanly when no gaps are found."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "item-a", [])

    output_path = tmp_path / "state" / "gap_registry.json"
    sys.argv = [
        "aggregate_gaps.py",
        "--completed-dir",
        str(completed),
        "--output",
        str(output_path),
    ]
    main()  # should not raise

    data = json.loads(output_path.read_text())
    assert data["gaps"] == {}

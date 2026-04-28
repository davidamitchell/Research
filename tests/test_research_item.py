"""Tests for the ResearchItem data model."""

from __future__ import annotations

from datetime import UTC, date, datetime
from pathlib import Path

import pytest

from src.research.item import ResearchItem

SAMPLE_ITEM = """\
---
title: "Test research item"
added: 2026-02-27
status: backlog
priority: high
tags: [testing, example]
started: ~
completed: ~
output: [knowledge]
---

# Test research item

## Question / Hypothesis

A test question.
"""

SAMPLE_ITEM_WITH_DATETIME = """\
---
title: "Test research item with datetime"
added: 2026-02-27T09:30:00+00:00
status: backlog
priority: high
tags: [testing]
started: ~
completed: ~
output: [knowledge]
---

# Test research item with datetime
"""

SAMPLE_ITEM_WITH_NEW_FIELDS = """\
---
title: "Test item with new fields"
added: 2026-04-28
status: completed
priority: high
tags: [testing]
started: 2026-04-28
completed: 2026-04-28
output: [knowledge]
cites: [2026-02-27-some-prior-item]
related: [2026-03-01-related-item]
superseded_by: ~
supersedes: 2026-01-01-older-item
item_type: synthesis
confidence: high
versions:
  - version: "1.0"
    sha: "abc1234"
    changed: 2026-04-28
    progress: "progress/2026-04-28-test.md"
    summary: "Initial completion"
---

# Test item with new fields
"""


def test_from_file_loads_title(tmp_path: Path) -> None:
    """ResearchItem.from_file reads the title from front matter."""
    f = tmp_path / "2026-02-27-test.md"
    f.write_text(SAMPLE_ITEM)
    item = ResearchItem.from_file(f)
    assert item.title == "Test research item"


def test_from_file_loads_status(tmp_path: Path) -> None:
    """ResearchItem.from_file reads the status from front matter."""
    f = tmp_path / "2026-02-27-test.md"
    f.write_text(SAMPLE_ITEM)
    item = ResearchItem.from_file(f)
    assert item.status == "backlog"


def test_from_file_loads_tags(tmp_path: Path) -> None:
    """ResearchItem.from_file reads tags from front matter."""
    f = tmp_path / "2026-02-27-test.md"
    f.write_text(SAMPLE_ITEM)
    item = ResearchItem.from_file(f)
    assert item.tags == ["testing", "example"]


def test_from_file_loads_added_date(tmp_path: Path) -> None:
    """ResearchItem.from_file parses the added date."""
    f = tmp_path / "2026-02-27-test.md"
    f.write_text(SAMPLE_ITEM)
    item = ResearchItem.from_file(f)
    assert item.added == date(2026, 2, 27)


def test_from_file_loads_added_datetime(tmp_path: Path) -> None:
    """ResearchItem.from_file parses a full ISO 8601 datetime in the added field."""
    f = tmp_path / "2026-02-27-test-dt.md"
    f.write_text(SAMPLE_ITEM_WITH_DATETIME)
    item = ResearchItem.from_file(f)
    expected = datetime(2026, 2, 27, 9, 30, 0, tzinfo=UTC)
    assert item.added == expected


def test_from_file_raises_on_missing_frontmatter(tmp_path: Path) -> None:
    """ResearchItem.from_file raises ValueError if no front matter is present."""
    f = tmp_path / "2026-02-27-no-frontmatter.md"
    f.write_text("# No front matter here\n")
    with pytest.raises(ValueError, match="No YAML front matter"):
        ResearchItem.from_file(f)


def test_state_dir_name_backlog() -> None:
    """state_dir_name returns 'backlog' for backlog status."""
    item = ResearchItem(
        path=Path("dummy.md"),
        title="t",
        added=date.today(),
        status="backlog",
        priority="medium",
    )
    assert item.state_dir_name() == "backlog"


def test_state_dir_name_in_progress() -> None:
    """state_dir_name returns 'in-progress' for in-progress status."""
    item = ResearchItem(
        path=Path("dummy.md"),
        title="t",
        added=date.today(),
        status="in-progress",
        priority="medium",
    )
    assert item.state_dir_name() == "in-progress"


def test_state_dir_name_completed() -> None:
    """state_dir_name returns 'completed' for completed status."""
    item = ResearchItem(
        path=Path("dummy.md"),
        title="t",
        added=date.today(),
        status="completed",
        priority="medium",
    )
    assert item.state_dir_name() == "completed"


def test_state_dir_name_reviewing_maps_to_in_progress() -> None:
    """state_dir_name returns 'in-progress' for reviewing status (file stays in place)."""
    item = ResearchItem(
        path=Path("dummy.md"),
        title="t",
        added=date.today(),
        status="reviewing",
        priority="medium",
    )
    assert item.state_dir_name() == "in-progress"


# ---------------------------------------------------------------------------
# New frontmatter field tests
# ---------------------------------------------------------------------------


def test_from_file_defaults_new_fields_when_absent(tmp_path: Path) -> None:
    """ResearchItem.from_file defaults new fields to empty/None when absent from frontmatter."""
    f = tmp_path / "2026-02-27-test.md"
    f.write_text(SAMPLE_ITEM)
    item = ResearchItem.from_file(f)
    assert item.cites == []
    assert item.related == []
    assert item.superseded_by is None
    assert item.supersedes is None
    assert item.item_type == "primary"
    assert item.confidence == "medium"
    assert item.versions == []


def test_from_file_parses_cites_and_related(tmp_path: Path) -> None:
    """ResearchItem.from_file reads cites and related slug lists from frontmatter."""
    f = tmp_path / "2026-04-28-test-new.md"
    f.write_text(SAMPLE_ITEM_WITH_NEW_FIELDS)
    item = ResearchItem.from_file(f)
    assert item.cites == ["2026-02-27-some-prior-item"]
    assert item.related == ["2026-03-01-related-item"]


def test_from_file_parses_supersedes(tmp_path: Path) -> None:
    """ResearchItem.from_file reads supersedes from frontmatter."""
    f = tmp_path / "2026-04-28-test-new.md"
    f.write_text(SAMPLE_ITEM_WITH_NEW_FIELDS)
    item = ResearchItem.from_file(f)
    assert item.supersedes == "2026-01-01-older-item"
    assert item.superseded_by is None


def test_from_file_parses_item_type_synthesis(tmp_path: Path) -> None:
    """ResearchItem.from_file reads item_type: synthesis from frontmatter."""
    f = tmp_path / "2026-04-28-test-new.md"
    f.write_text(SAMPLE_ITEM_WITH_NEW_FIELDS)
    item = ResearchItem.from_file(f)
    assert item.item_type == "synthesis"


def test_from_file_parses_confidence_high(tmp_path: Path) -> None:
    """ResearchItem.from_file reads confidence: high from frontmatter."""
    f = tmp_path / "2026-04-28-test-new.md"
    f.write_text(SAMPLE_ITEM_WITH_NEW_FIELDS)
    item = ResearchItem.from_file(f)
    assert item.confidence == "high"


def test_from_file_parses_versions(tmp_path: Path) -> None:
    """ResearchItem.from_file reads versions list from frontmatter."""
    f = tmp_path / "2026-04-28-test-new.md"
    f.write_text(SAMPLE_ITEM_WITH_NEW_FIELDS)
    item = ResearchItem.from_file(f)
    assert len(item.versions) == 1
    assert item.versions[0]["version"] == "1.0"
    assert item.versions[0]["sha"] == "abc1234"
    assert item.versions[0]["summary"] == "Initial completion"

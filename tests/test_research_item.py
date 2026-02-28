"""Tests for the ResearchItem data model."""

from __future__ import annotations

from datetime import date
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

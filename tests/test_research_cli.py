"""Tests for the research item CLI commands (add, list, start, complete)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from src.research.cli import (
    _set_frontmatter_field,
    _slug,
    cmd_add,
    cmd_complete,
    cmd_list,
    cmd_start,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SAMPLE_FRONTMATTER = """\
---
title: "Sample item"
added: 2026-02-28
status: backlog
priority: medium
tags: []
started: ~
completed: ~
output: []
---

# Sample item
"""


def _make_item(research_dir: Path, subdir: str, filename: str, content: str) -> Path:
    path = research_dir / subdir / filename
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# _slug
# ---------------------------------------------------------------------------


def test_slug_converts_spaces() -> None:
    assert _slug("Hello World") == "hello-world"


def test_slug_strips_special_chars() -> None:
    assert _slug("Foo: bar & baz!") == "foo-bar-baz"


def test_slug_caps_at_80() -> None:
    long_title = "a" * 100
    assert len(_slug(long_title)) <= 80


# ---------------------------------------------------------------------------
# _set_frontmatter_field
# ---------------------------------------------------------------------------


def test_set_frontmatter_field_updates_status() -> None:
    updated = _set_frontmatter_field(SAMPLE_FRONTMATTER, "status", "in-progress")
    assert "status: in-progress" in updated


def test_set_frontmatter_field_updates_tilde_value() -> None:
    updated = _set_frontmatter_field(SAMPLE_FRONTMATTER, "started", "2026-02-28")
    assert "started: 2026-02-28" in updated


# ---------------------------------------------------------------------------
# cmd_add
# ---------------------------------------------------------------------------


def test_cmd_add_creates_file(research_dir: Path) -> None:
    path = cmd_add("My new item", research_root=research_dir)
    assert path.exists()
    assert path.parent.name == "backlog"


def test_cmd_add_filename_contains_today(research_dir: Path) -> None:
    path = cmd_add("My new item", research_root=research_dir)
    today = date.today().isoformat()
    assert path.name.startswith(today)


def test_cmd_add_file_contains_title(research_dir: Path) -> None:
    path = cmd_add("Great research title", research_root=research_dir)
    content = path.read_text()
    assert "Great research title" in content


def test_cmd_add_file_has_frontmatter_status_backlog(research_dir: Path) -> None:
    path = cmd_add("Status check", research_root=research_dir)
    content = path.read_text()
    assert "status: backlog" in content


def test_cmd_add_does_not_overwrite_existing(
    research_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = cmd_add("Duplicate item", research_root=research_dir)
    original_mtime = path.stat().st_mtime
    cmd_add("Duplicate item", research_root=research_dir)
    assert path.stat().st_mtime == original_mtime


# ---------------------------------------------------------------------------
# cmd_list
# ---------------------------------------------------------------------------


def test_cmd_list_returns_backlog_items(research_dir: Path) -> None:
    _make_item(research_dir, "backlog", "2026-02-28-test.md", SAMPLE_FRONTMATTER)
    items = cmd_list(research_root=research_dir)
    assert len(items) == 1
    assert items[0].title == "Sample item"


def test_cmd_list_returns_in_progress_items(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    items = cmd_list(research_root=research_dir)
    assert any(i.status == "in-progress" for i in items)


def test_cmd_list_skips_completed(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: completed")
    _make_item(research_dir, "completed", "2026-02-28-test.md", content)
    items = cmd_list(research_root=research_dir)
    assert len(items) == 0


def test_cmd_list_prints_item(research_dir: Path, capsys: pytest.CaptureFixture[str]) -> None:
    _make_item(research_dir, "backlog", "2026-02-28-test.md", SAMPLE_FRONTMATTER)
    cmd_list(research_root=research_dir)
    out = capsys.readouterr().out
    assert "Sample item" in out
    assert "backlog" in out


# ---------------------------------------------------------------------------
# cmd_start
# ---------------------------------------------------------------------------


def test_cmd_start_moves_file(research_dir: Path) -> None:
    _make_item(research_dir, "backlog", "2026-02-28-test.md", SAMPLE_FRONTMATTER)
    dest = cmd_start("2026-02-28-test.md", research_root=research_dir)
    assert dest.exists()
    assert dest.parent.name == "in-progress"
    assert not (research_dir / "backlog" / "2026-02-28-test.md").exists()


def test_cmd_start_updates_status(research_dir: Path) -> None:
    _make_item(research_dir, "backlog", "2026-02-28-test.md", SAMPLE_FRONTMATTER)
    dest = cmd_start("2026-02-28-test.md", research_root=research_dir)
    content = dest.read_text()
    assert "status: in-progress" in content


def test_cmd_start_sets_started_date(research_dir: Path) -> None:
    _make_item(research_dir, "backlog", "2026-02-28-test.md", SAMPLE_FRONTMATTER)
    dest = cmd_start("2026-02-28-test.md", research_root=research_dir)
    content = dest.read_text()
    today = date.today().isoformat()
    assert f"started: {today}" in content


def test_cmd_start_exits_on_missing(research_dir: Path) -> None:
    with pytest.raises(SystemExit):
        cmd_start("nonexistent.md", research_root=research_dir)


# ---------------------------------------------------------------------------
# cmd_complete
# ---------------------------------------------------------------------------


def test_cmd_complete_moves_file(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    dest = cmd_complete("2026-02-28-test.md", research_root=research_dir)
    assert dest.exists()
    assert dest.parent.name == "completed"
    assert not (research_dir / "in-progress" / "2026-02-28-test.md").exists()


def test_cmd_complete_updates_status(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    dest = cmd_complete("2026-02-28-test.md", research_root=research_dir)
    updated_content = dest.read_text()
    assert "status: completed" in updated_content


def test_cmd_complete_sets_completed_date(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    dest = cmd_complete("2026-02-28-test.md", research_root=research_dir)
    updated_content = dest.read_text()
    today = date.today().isoformat()
    assert f"completed: {today}" in updated_content


def test_cmd_complete_exits_on_missing(research_dir: Path) -> None:
    with pytest.raises(SystemExit):
        cmd_complete("nonexistent.md", research_root=research_dir)

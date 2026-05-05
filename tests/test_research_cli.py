"""Tests for the research item CLI commands (add, list, start, draft, complete)."""

from __future__ import annotations

import re
import subprocess
from datetime import date
from pathlib import Path

import pytest

from src.research.cli import (
    _get_frontmatter_field,
    _set_frontmatter_field,
    _slug,
    cmd_add,
    cmd_complete,
    cmd_draft,
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


_ISO_DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$")


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
    # started: should be a full ISO 8601 datetime (not a bare date)
    match = re.search(r"^started:\s*(.+)$", content, re.MULTILINE)
    assert match is not None
    assert _ISO_DATETIME_RE.match(match.group(1).strip()), (
        f"started: expected ISO datetime, got {match.group(1).strip()!r}"
    )


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
    # completed: should be a full ISO 8601 datetime (not a bare date)
    match = re.search(r"^completed:\s*(.+)$", updated_content, re.MULTILINE)
    assert match is not None
    assert _ISO_DATETIME_RE.match(match.group(1).strip()), (
        f"completed: expected ISO datetime, got {match.group(1).strip()!r}"
    )


def test_cmd_complete_exits_on_missing(research_dir: Path) -> None:
    with pytest.raises(SystemExit):
        cmd_complete("nonexistent.md", research_root=research_dir)


# ---------------------------------------------------------------------------
# _get_frontmatter_field
# ---------------------------------------------------------------------------


def test_get_frontmatter_field_returns_value() -> None:
    assert _get_frontmatter_field(SAMPLE_FRONTMATTER, "status") == "backlog"


def test_get_frontmatter_field_returns_none_for_missing_key() -> None:
    assert _get_frontmatter_field(SAMPLE_FRONTMATTER, "nonexistent") is None


def test_get_frontmatter_field_returns_tilde_as_string() -> None:
    assert _get_frontmatter_field(SAMPLE_FRONTMATTER, "started") == "~"


# ---------------------------------------------------------------------------
# cmd_draft
# ---------------------------------------------------------------------------


def test_cmd_draft_updates_status_to_reviewing(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    path = cmd_draft("2026-02-28-test.md", research_root=research_dir)
    assert "status: reviewing" in path.read_text()


def test_cmd_draft_does_not_move_file(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    path = cmd_draft("2026-02-28-test.md", research_root=research_dir)
    assert path.parent.name == "in-progress"


def test_cmd_draft_file_remains_in_in_progress(research_dir: Path) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    cmd_draft("2026-02-28-test.md", research_root=research_dir)
    assert (research_dir / "in-progress" / "2026-02-28-test.md").exists()
    assert not (research_dir / "completed" / "2026-02-28-test.md").exists()
    assert not (research_dir / "backlog" / "2026-02-28-test.md").exists()


def test_cmd_draft_exits_on_missing(research_dir: Path) -> None:
    with pytest.raises(SystemExit):
        cmd_draft("nonexistent.md", research_root=research_dir)


# ---------------------------------------------------------------------------
# cmd_complete — soft guard for reviewing status
# ---------------------------------------------------------------------------


def test_cmd_complete_warns_if_status_not_reviewing(
    research_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    cmd_complete("2026-02-28-test.md", research_root=research_dir)
    err = capsys.readouterr().err
    assert "Warning" in err
    assert "reviewing" in err


def test_cmd_complete_still_completes_despite_warning(
    research_dir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: in-progress")
    _make_item(research_dir, "in-progress", "2026-02-28-test.md", content)
    dest = cmd_complete("2026-02-28-test.md", research_root=research_dir)
    assert dest.parent.name == "completed"
    assert "status: completed" in dest.read_text()


# ---------------------------------------------------------------------------
# Git staging — cmd_start and cmd_complete must leave no unstaged changes.
#
# Root cause of the research-loop "unstaged changes" bug: both commands used
# Python file I/O (Path.unlink / Path.write_text) to move files but never
# updated the git index.  The Copilot agent's subsequent ``git add <new-file>
# && git commit`` therefore missed the old-file deletion, leaving an unstaged
# deletion in the working tree.  The next iteration's ``git pull --rebase``
# then failed with "You have unstaged changes."
# ---------------------------------------------------------------------------


@pytest.fixture
def git_research_dir(tmp_path: Path) -> Path:
    """A Research dir structure inside a real git repository."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)

    research_dir = tmp_path / "Research"
    for subdir in ("backlog", "in-progress", "completed"):
        (research_dir / subdir).mkdir(parents=True)
        (research_dir / subdir / ".gitkeep").write_text("", encoding="utf-8")

    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "initial structure"], cwd=tmp_path, check=True)

    return research_dir


def _git_dirty_files(repo_root: Path) -> str:
    """Return the ``git diff --stat`` output for the working tree vs index."""
    result = subprocess.run(
        ["git", "diff", "--stat"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def test_cmd_start_leaves_no_unstaged_changes(git_research_dir: Path) -> None:
    """cmd_start must stage the backlog→in-progress move; no unstaged deletions."""
    item_path = git_research_dir / "backlog" / "2026-03-01-test.md"
    item_path.write_text(SAMPLE_FRONTMATTER, encoding="utf-8")

    repo_root = git_research_dir.parent
    subprocess.run(
        ["git", "add", str(item_path.relative_to(repo_root))],
        cwd=str(repo_root),
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-q", "-m", "add backlog item"], cwd=str(repo_root), check=True
    )

    cmd_start("2026-03-01-test.md", research_root=git_research_dir)

    dirty = _git_dirty_files(repo_root)
    assert dirty == "", (
        f"Working tree must be clean after cmd_start, but git diff --stat shows:\n{dirty}"
    )


def test_cmd_complete_leaves_no_unstaged_changes(git_research_dir: Path) -> None:
    """cmd_complete must stage the in-progress→completed move; no unstaged deletions."""
    content = SAMPLE_FRONTMATTER.replace("status: backlog", "status: reviewing")
    item_path = git_research_dir / "in-progress" / "2026-03-01-test.md"
    item_path.write_text(content, encoding="utf-8")

    repo_root = git_research_dir.parent
    subprocess.run(
        ["git", "add", str(item_path.relative_to(repo_root))],
        cwd=str(repo_root),
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-q", "-m", "add in-progress item"], cwd=str(repo_root), check=True
    )

    cmd_complete("2026-03-01-test.md", research_root=git_research_dir)

    dirty = _git_dirty_files(repo_root)
    assert dirty == "", (
        f"Working tree must be clean after cmd_complete, but git diff --stat shows:\n{dirty}"
    )

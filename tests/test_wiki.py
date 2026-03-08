"""Tests for the wiki publishing module (src/wiki/publish.py)."""

from __future__ import annotations

from pathlib import Path

from src.wiki.publish import (
    generate_home,
    generate_sidebar,
    load_frontmatter,
    page_name,
    publish,
    strip_frontmatter,
    wiki_link,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_ITEM = """\
---
title: "AI Strategy Research"
added: 2026-02-28
status: completed
priority: high
tags: [ai, strategy]
started: 2026-02-28
completed: 2026-02-28
output: [knowledge]
---

# AI Strategy Research

## Research Question

What does an effective AI strategy look like?
"""

ITEM_NO_FRONTMATTER = """\
# Just a plain page

No front-matter here.
"""


def _write_item(directory: Path, filename: str, content: str) -> Path:
    path = directory / filename
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# wiki_link
# ---------------------------------------------------------------------------


def test_wiki_link_plain() -> None:
    assert wiki_link("my-page", "My Page") == "[[My Page|my-page]]"


def test_wiki_link_in_table_escapes_pipe() -> None:
    # Pipe must be escaped as \| inside a Markdown table cell.
    assert wiki_link("my-page", "My Page", in_table=True) == "[[My Page\\|my-page]]"


# ---------------------------------------------------------------------------
# load_frontmatter
# ---------------------------------------------------------------------------


def test_load_frontmatter_parses_yaml() -> None:
    meta = load_frontmatter(SAMPLE_ITEM)
    assert meta["title"] == "AI Strategy Research"
    assert str(meta["added"]) == "2026-02-28"
    assert meta["tags"] == ["ai", "strategy"]


def test_load_frontmatter_returns_empty_dict_when_no_frontmatter() -> None:
    assert load_frontmatter(ITEM_NO_FRONTMATTER) == {}


def test_load_frontmatter_returns_empty_dict_on_invalid_yaml() -> None:
    bad = "---\n: bad: yaml: [\n---\n# body"
    assert load_frontmatter(bad) == {}


# ---------------------------------------------------------------------------
# strip_frontmatter
# ---------------------------------------------------------------------------


def test_strip_frontmatter_removes_yaml_block() -> None:
    body = strip_frontmatter(SAMPLE_ITEM)
    assert body.startswith("# AI Strategy Research")
    assert "---" not in body.split("\n")[0]


def test_strip_frontmatter_leaves_plain_text_unchanged() -> None:
    body = strip_frontmatter(ITEM_NO_FRONTMATTER)
    assert body == ITEM_NO_FRONTMATTER


def test_strip_frontmatter_preserves_body_content() -> None:
    body = strip_frontmatter(SAMPLE_ITEM)
    assert "What does an effective AI strategy look like?" in body


# ---------------------------------------------------------------------------
# page_name
# ---------------------------------------------------------------------------


def test_page_name_strips_extension() -> None:
    assert page_name("2026-02-28-ai-strategy.md") == "2026-02-28-ai-strategy"


def test_page_name_preserves_date_prefix() -> None:
    name = page_name("2026-03-01-github-wiki-research-content.md")
    assert name == "2026-03-01-github-wiki-research-content"


# ---------------------------------------------------------------------------
# generate_home
# ---------------------------------------------------------------------------


def test_generate_home_contains_header() -> None:
    home = generate_home([])
    assert "# Research Index" in home


def test_generate_home_contains_item_link() -> None:
    items = [
        {
            "page_name": "2026-02-28-ai-strategy",
            "title": "AI Strategy Research",
            "added": "2026-02-28",
            "tags": ["ai", "strategy"],
        }
    ]
    home = generate_home(items)
    # Link should use title as display text and page slug as the URL target.
    assert "[[AI Strategy Research" in home
    assert "2026-02-28-ai-strategy" in home


def test_generate_home_sorted_most_recent_first() -> None:
    items = [
        {"page_name": "older", "title": "Older", "added": "2026-01-01", "tags": []},
        {"page_name": "newer", "title": "Newer", "added": "2026-03-01", "tags": []},
    ]
    home = generate_home(items)
    assert home.index("newer") < home.index("older")


def test_generate_home_includes_tags() -> None:
    items = [
        {
            "page_name": "2026-02-28-ai-strategy",
            "title": "AI Strategy",
            "added": "2026-02-28",
            "tags": ["ai", "strategy"],
        }
    ]
    home = generate_home(items)
    assert "ai, strategy" in home


# ---------------------------------------------------------------------------
# generate_sidebar
# ---------------------------------------------------------------------------


def test_generate_sidebar_contains_home_link() -> None:
    sidebar = generate_sidebar([])
    assert "[[Home]]" in sidebar


def test_generate_sidebar_groups_by_tag() -> None:
    items = [
        {"page_name": "page-a", "title": "Page A", "added": "2026-02-28", "tags": ["ai"]},
        {"page_name": "page-b", "title": "Page B", "added": "2026-02-28", "tags": ["ai"]},
    ]
    sidebar = generate_sidebar(items)
    assert "**ai**" in sidebar
    assert "page-a" in sidebar
    assert "page-b" in sidebar


def test_generate_sidebar_tags_sorted_alphabetically() -> None:
    items = [
        {"page_name": "p1", "title": "P1", "added": "2026-02-28", "tags": ["zebra"]},
        {"page_name": "p2", "title": "P2", "added": "2026-02-28", "tags": ["alpha"]},
    ]
    sidebar = generate_sidebar(items)
    assert sidebar.index("alpha") < sidebar.index("zebra")


# ---------------------------------------------------------------------------
# publish (integration)
# ---------------------------------------------------------------------------


def test_publish_creates_wiki_dir(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    publish(completed, wiki)

    assert wiki.is_dir()


def test_publish_writes_page_per_item(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    publish(completed, wiki)

    assert (wiki / "2026-02-28-ai-strategy.md").exists()


def test_publish_writes_home_and_sidebar(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    publish(completed, wiki)

    assert (wiki / "Home.md").exists()
    assert (wiki / "_Sidebar.md").exists()


def test_publish_strips_frontmatter_from_wiki_page(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    publish(completed, wiki)

    content = (wiki / "2026-02-28-ai-strategy.md").read_text()
    assert content.startswith("# AI Strategy Research")
    assert "status: completed" not in content


def test_publish_skips_readme(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "README.md", "# README\n")
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    written = publish(completed, wiki)

    assert "README.md" not in written
    assert not (wiki / "README.md").exists()


def test_publish_returns_written_filenames(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    written = publish(completed, wiki)

    assert "2026-02-28-ai-strategy.md" in written
    assert "Home.md" in written
    assert "_Sidebar.md" in written


def test_publish_full_rebuild_removes_old_pages(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"
    wiki.mkdir()

    # Pre-existing stale page
    stale = wiki / "stale-old-page.md"
    stale.write_text("stale", encoding="utf-8")

    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)

    publish(completed, wiki)

    assert not stale.exists()


def test_publish_empty_completed_dir(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"

    written = publish(completed, wiki)

    assert "Home.md" in written
    assert "_Sidebar.md" in written
    assert (wiki / "Home.md").read_text().count("|") > 0  # table header still present


def test_publish_multiple_items(tmp_path: Path) -> None:
    completed = tmp_path / "completed"
    completed.mkdir()
    wiki = tmp_path / "wiki"

    item2 = SAMPLE_ITEM.replace("AI Strategy Research", "Jevons Paradox").replace(
        "2026-02-28", "2026-02-27"
    )
    _write_item(completed, "2026-02-28-ai-strategy.md", SAMPLE_ITEM)
    _write_item(completed, "2026-02-27-jevons-paradox.md", item2)

    written = publish(completed, wiki)

    assert "2026-02-28-ai-strategy.md" in written
    assert "2026-02-27-jevons-paradox.md" in written
    home = (wiki / "Home.md").read_text()
    assert "2026-02-28-ai-strategy" in home
    assert "2026-02-27-jevons-paradox" in home

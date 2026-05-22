"""Tests for scripts/theme_report.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Make scripts/ importable in tests.
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from theme_report import (  # noqa: E402
    _extract_themes,
    build_report,
    collect_themes,
    find_near_duplicates,
    render_markdown,
)


def _write_item(base_dir: Path, slug: str, frontmatter: str) -> Path:
    path = base_dir / f"{slug}.md"
    path.write_text(f"---\n{frontmatter}\n---\n\n# {slug}\n", encoding="utf-8")
    return path


def test_extract_themes_inline_list(tmp_path: Path) -> None:
    path = tmp_path / "item.md"
    path.write_text("---\nthemes: [agentic-ai, governance-policy]\n---\n", encoding="utf-8")

    extracted = _extract_themes(path)

    assert extracted["themes"] == ["agentic-ai", "governance-policy"]
    assert extracted["ai_themes"] == []
    assert extracted["has_themes_field"] is True
    assert extracted["has_ai_themes_field"] is False


def test_extract_themes_block_list(tmp_path: Path) -> None:
    path = tmp_path / "item.md"
    path.write_text("---\nthemes:\n  - agentic-ai\n  - governance-policy\n---\n", encoding="utf-8")

    extracted = _extract_themes(path)

    assert extracted["themes"] == ["agentic-ai", "governance-policy"]
    assert extracted["has_themes_field"] is True


def test_extract_themes_missing_fields(tmp_path: Path) -> None:
    path = tmp_path / "item.md"
    path.write_text("---\ntitle: No themes\n---\n", encoding="utf-8")

    extracted = _extract_themes(path)

    assert extracted["themes"] == []
    assert extracted["ai_themes"] == []
    assert extracted["has_themes_field"] is False
    assert extracted["has_ai_themes_field"] is False


def test_extract_themes_both_fields_present(tmp_path: Path) -> None:
    path = tmp_path / "item.md"
    path.write_text(
        "---\nthemes: [agentic-ai]\nai_themes:\n  - national-ai-strategy\n---\n",
        encoding="utf-8",
    )

    extracted = _extract_themes(path)

    assert extracted["themes"] == ["agentic-ai"]
    assert extracted["ai_themes"] == ["national-ai-strategy"]
    assert extracted["has_themes_field"] is True
    assert extracted["has_ai_themes_field"] is True


def test_collect_themes_counts_per_field(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)

    _write_item(completed, "item-a", "themes: [agentic-ai, governance-policy]")
    _write_item(completed, "item-b", "ai_themes: [agentic-ai, national-ai-strategy]")
    _write_item(
        completed,
        "item-c",
        "themes:\n  - governance-policy\nai_themes:\n  - national-ai-strategy",
    )

    collected = collect_themes(tmp_path)

    assert collected["items_scanned"] == 3
    assert collected["items_with_themes_field"] == 2
    assert collected["items_with_ai_themes_field"] == 2
    assert collected["items_with_neither"] == []
    assert collected["provenance"]["agentic-ai"] == {"themes": 1, "ai_themes": 1}
    assert collected["provenance"]["governance-policy"] == {"themes": 2, "ai_themes": 0}
    assert collected["provenance"]["national-ai-strategy"] == {"themes": 0, "ai_themes": 2}


def test_find_near_duplicates_signals() -> None:
    term_to_slugs = {
        "workflow": {"a", "b"},
        "workflows": {"c", "d"},
        "agentic-ai": {"a", "c"},
        "strategic-agentic-ai": {"b", "d"},
        "python": {"a", "b"},
        "governance": {"c", "d"},
    }

    near = find_near_duplicates(term_to_slugs)
    pairs = {(row["term_a"], row["term_b"]) for row in near}

    assert ("workflow", "workflows") in pairs
    assert ("agentic-ai", "strategic-agentic-ai") in pairs
    assert ("governance", "python") not in pairs


def test_collect_themes_items_with_neither(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)

    _write_item(completed, "item-a", "title: Has none")
    _write_item(completed, "item-b", "themes: [agentic-ai]")

    collected = collect_themes(tmp_path)

    assert collected["items_with_neither"] == ["item-a"]


def test_build_report_schema(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)

    _write_item(completed, "item-a", "themes: [agentic-ai, governance-policy]")
    _write_item(completed, "item-b", "ai_themes: [agentic-ai, national-ai-strategy]")
    _write_item(completed, "item-c", "title: Neither")

    data = build_report(tmp_path)

    assert set(data.keys()) == {
        "summary",
        "frequency",
        "provenance",
        "items_with_neither",
        "near_duplicates",
    }
    assert data["summary"]["items_scanned"] == 3
    assert data["summary"]["items_with_themes_field"] == 1
    assert data["summary"]["items_with_ai_themes_field"] == 1
    assert data["summary"]["items_with_neither"] == 1
    assert data["frequency"]["agentic-ai"] == 2
    assert data["provenance"]["national-ai-strategy"] == {"themes": 0, "ai_themes": 1}
    assert data["items_with_neither"] == ["item-c"]


def test_render_markdown_contains_sections(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)

    _write_item(completed, "item-a", "themes: [agentic-ai]")
    data = build_report(tmp_path)

    markdown = render_markdown(data)

    assert "# Theme Report" in markdown
    assert "## Summary" in markdown
    assert "## Near-duplicate candidates" in markdown
    assert "## Frequency" in markdown
    assert "## Items with neither field" in markdown
    assert "## Review actions needed" in markdown


def test_main_writes_output_files(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)

    _write_item(completed, "item-a", "themes: [agentic-ai]")

    from theme_report import main

    sys.argv = ["theme_report.py", "--root", str(tmp_path)]
    main()

    json_path = tmp_path / "state" / "theme_report.json"
    md_path = tmp_path / "state" / "theme_report.md"

    assert json_path.exists()
    assert md_path.exists()

    payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert payload["summary"]["items_scanned"] == 1
    assert payload["summary"]["total_terms"] == 1

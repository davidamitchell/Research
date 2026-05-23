"""Tests for scripts/canonicalise_themes.py and scripts/validate_themes.py."""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from canonicalise_themes import (  # noqa: E402
    canonicalise_directory,
    canonicalise_file,
    load_themes_vocabulary,
    write_migration_summary,
)
from validate_themes import validate_directory  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "themes-vocabulary.md"


def _item(tmp_path: Path, name: str, frontmatter: str, body: str = "# Test") -> Path:
    """Write a minimal research item file and return its Path."""
    path = tmp_path / name
    fm = textwrap.dedent(frontmatter).strip()
    path.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# load_themes_vocabulary — reverse map (alias → canonical)
# ---------------------------------------------------------------------------


def test_load_vocabulary_returns_identity_for_canonicals() -> None:
    """Every canonical slug must map to itself in the reverse map."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    text = VOCAB_PATH.read_text()
    match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
    assert match
    parsed = yaml.safe_load(match.group(1))
    for canonical in parsed:
        assert vocab.get(canonical) == canonical, f"{canonical!r} should map to itself"


def test_load_vocabulary_maps_aliases_to_canonical() -> None:
    """Alias slugs must map to their canonical form."""
    vocab = load_themes_vocabulary(VOCAB_PATH)
    # prompt-engineering is an alias for llm-reasoning per the vocabulary
    assert vocab.get("prompt-engineering") == "llm-reasoning"
    # ai-governance is an alias for governance-policy
    assert vocab.get("ai-governance") == "governance-policy"
    # organisation is an alias for organisational-design
    assert vocab.get("organisation") == "organisational-design"


# ---------------------------------------------------------------------------
# canonicalise_file — ai_themes migration
# ---------------------------------------------------------------------------


def test_ai_themes_migrated_to_themes(tmp_path: Path) -> None:
    """ai_themes: values are mapped to canonical themes: and the field is removed."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        ai_themes: [agentic-ai, governance-policy]
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_file(path, vocab)

    assert changed
    content = path.read_text()
    assert "themes: [agentic-ai, governance-policy]" in content
    assert "ai_themes:" not in content


def test_themes_inserted_inside_frontmatter_when_no_output_field(tmp_path: Path) -> None:
    """themes: must land inside the frontmatter block, not before the opening ---.

    Regression guard for the bug where ``re.search(r"^---$", text, re.MULTILINE)``
    in ``_insert_themes_field`` matched the *opening* delimiter (first occurrence),
    causing ``themes:`` to be prepended before the frontmatter rather than inside it.
    """
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        ai_themes: [agentic-ai]
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonicalise_file(path, vocab)

    content = path.read_text()
    assert content.startswith("---\n"), "File must start with the opening frontmatter ---"
    opening_pos = content.index("---\n")
    themes_pos = content.index("themes:")
    assert themes_pos > opening_pos, "themes: must be inside frontmatter, not before it"


def test_tags_known_aliases_migrated_to_themes(tmp_path: Path) -> None:
    """tags: values that are known aliases are resolved to canonical themes:."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        tags: [agentic-ai, prompt-engineering]
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_file(path, vocab)

    assert changed
    content = path.read_text()
    # prompt-engineering → llm-reasoning
    assert "llm-reasoning" in content
    assert "agentic-ai" in content
    assert "tags:" not in content


def test_unknown_tags_dropped_during_migration(tmp_path: Path) -> None:
    """tags: values not in the themes vocabulary are dropped (not preserved)."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        tags: [agentic-ai, some-unknown-singleton-tag]
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonicalise_file(path, vocab)

    content = path.read_text()
    assert "some-unknown-singleton-tag" not in content
    assert "agentic-ai" in content


def test_both_fields_merged_and_deduplicated(tmp_path: Path) -> None:
    """When both tags: and ai_themes: are present, they are merged and deduplicated."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        tags: [agentic-ai, ai-governance]
        ai_themes: [agentic-ai, governance-policy]
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    canonicalise_file(path, vocab)

    content = path.read_text()
    # ai-governance (alias) and governance-policy (canonical) resolve to the same slug
    # agentic-ai appears in both — must appear exactly once in themes:
    assert content.count("agentic-ai") == 1
    assert content.count("governance-policy") == 1
    assert "tags:" not in content
    assert "ai_themes:" not in content


def test_idempotent_when_themes_already_set(tmp_path: Path) -> None:
    """Files with themes: and no legacy fields are not modified."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        themes: [agentic-ai, governance-policy]
        """,
    )
    original = path.read_text()
    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_file(path, vocab)

    assert not changed
    assert path.read_text() == original


def test_file_without_theme_fields_not_modified(tmp_path: Path) -> None:
    """Files that have no tags:, ai_themes:, or themes: are left unchanged."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: backlog
        """,
    )
    original = path.read_text()
    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_file(path, vocab)

    assert not changed
    assert path.read_text() == original


def test_block_list_ai_themes_migrated(tmp_path: Path) -> None:
    """Block-list format for ai_themes is migrated correctly."""
    path = _item(
        tmp_path,
        "item.md",
        """\
        title: "Test"
        status: completed
        ai_themes:
          - agentic-ai
          - knowledge-management
        """,
    )
    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_file(path, vocab)

    assert changed
    content = path.read_text()
    assert "agentic-ai" in content
    assert "knowledge-management" in content
    assert "ai_themes:" not in content
    assert "themes:" in content


# ---------------------------------------------------------------------------
# canonicalise_directory
# ---------------------------------------------------------------------------


def test_directory_scan_processes_all_subdirs(tmp_path: Path) -> None:
    """canonicalise_directory processes completed/, backlog/, and in-progress/."""
    for subdir in ("completed", "backlog", "in-progress"):
        d = tmp_path / "Research" / subdir
        d.mkdir(parents=True)
        _item(
            d,
            "item.md",
            """\
            title: "Test"
            status: completed
            ai_themes: [agentic-ai]
            """,
        )

    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_directory(tmp_path, vocab)

    assert len(changed) == 3


def test_directory_scan_skips_gitkeep_and_readme(tmp_path: Path) -> None:
    """canonicalise_directory skips .gitkeep and README.md files."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    (d / ".gitkeep").write_text("", encoding="utf-8")
    (d / "README.md").write_text("# Readme\n", encoding="utf-8")

    vocab = load_themes_vocabulary(VOCAB_PATH)
    changed = canonicalise_directory(tmp_path, vocab)

    assert not changed


# ---------------------------------------------------------------------------
# write_migration_summary
# ---------------------------------------------------------------------------


def test_migration_summary_written_to_state(tmp_path: Path) -> None:
    """write_migration_summary creates state/themes-migration.md."""
    changed_paths = [tmp_path / "Research" / "completed" / "item-a.md"]
    write_migration_summary(tmp_path, changed_paths)

    summary_path = tmp_path / "state" / "themes-migration.md"
    assert summary_path.exists()
    content = summary_path.read_text()
    assert "item-a.md" in content


def test_migration_summary_includes_count(tmp_path: Path) -> None:
    """Migration summary must include the count of migrated files."""
    changed_paths = [
        tmp_path / "Research" / "completed" / "item-a.md",
        tmp_path / "Research" / "completed" / "item-b.md",
    ]
    write_migration_summary(tmp_path, changed_paths)

    content = (tmp_path / "state" / "themes-migration.md").read_text()
    assert "2" in content


# ---------------------------------------------------------------------------
# validate_directory
# ---------------------------------------------------------------------------


def test_validate_passes_when_no_legacy_fields(tmp_path: Path) -> None:
    """validate_directory returns no violations when items have only themes:."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "Test"
        status: completed
        themes: [agentic-ai]
        """,
    )
    violations = validate_directory(tmp_path)
    assert violations == []


def test_validate_detects_residual_tags_field(tmp_path: Path) -> None:
    """validate_directory flags items that still have a tags: field."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "Test"
        status: completed
        tags: [agentic-ai]
        """,
    )
    violations = validate_directory(tmp_path)
    assert len(violations) == 1
    assert "tags:" in violations[0]


def test_validate_detects_residual_ai_themes_field(tmp_path: Path) -> None:
    """validate_directory flags items that still have an ai_themes: field."""
    d = tmp_path / "Research" / "completed"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "Test"
        status: completed
        ai_themes: [agentic-ai]
        """,
    )
    violations = validate_directory(tmp_path)
    assert len(violations) == 1
    assert "ai_themes:" in violations[0]


def test_validate_items_without_any_theme_field_pass(tmp_path: Path) -> None:
    """Items with neither tags:, ai_themes:, nor themes: are valid (backlog items)."""
    d = tmp_path / "Research" / "backlog"
    d.mkdir(parents=True)
    _item(
        d,
        "item.md",
        """\
        title: "New backlog item"
        status: backlog
        """,
    )
    violations = validate_directory(tmp_path)
    assert violations == []

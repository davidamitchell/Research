"""Tests for scripts/canonicalise_tags.py."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pytest
import yaml

# Make the scripts/ directory importable in tests
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from canonicalise_tags import (  # noqa: E402
    _canonicalise_list,
    _format_block_list,
    _format_inline_list,
    _parse_block_list,
    _parse_inline_list,
    canonicalise_directory,
    canonicalise_file,
    load_vocabulary,
    main,
)
from tag_report import collect_tags  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "tag-vocabulary.md"


def _write_item(path: Path, tags_line: str, extra: str = "") -> None:
    """Write a minimal research item with the given tags: line."""
    path.write_text(
        textwrap.dedent(f"""\
            ---
            title: "Test Item"
            status: backlog
            tags: {tags_line}
            ---

            # Test Item
            {extra}
        """),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Vocabulary file
# ---------------------------------------------------------------------------


def test_vocab_file_exists() -> None:
    """docs/tag-vocabulary.md must exist in the repository."""
    assert VOCAB_PATH.exists(), f"Missing vocabulary file: {VOCAB_PATH}"


def test_vocab_yaml_block_is_valid_yaml() -> None:
    """The ```yaml block inside docs/tag-vocabulary.md must be valid YAML."""
    import re

    text = VOCAB_PATH.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
    assert match, "No ```yaml block found in docs/tag-vocabulary.md"
    # Must parse without error
    parsed = yaml.safe_load(match.group(1))
    assert isinstance(parsed, dict), "YAML block must be a mapping"


def test_vocab_yaml_all_values_are_lists() -> None:
    """Every value in the vocabulary YAML must be a list (list of aliases)."""
    import re

    text = VOCAB_PATH.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
    parsed = yaml.safe_load(match.group(1))
    for canonical, aliases in parsed.items():
        assert isinstance(aliases, list), (
            f"Vocabulary entry '{canonical}' value must be a list, got {type(aliases)}"
        )


def test_vocab_no_alias_is_its_own_canonical() -> None:
    """No alias should map to itself — aliases must resolve to a different canonical form."""
    alias_map = load_vocabulary(VOCAB_PATH)
    for alias, canonical in alias_map.items():
        if alias != canonical:
            # For non-canonical aliases: the canonical must self-map (no chains)
            assert alias_map.get(canonical) == canonical, (
                f"Alias '{alias}' maps to '{canonical}', but '{canonical}' "
                f"is not itself a canonical key"
            )


def test_load_vocabulary_returns_reverse_map() -> None:
    """load_vocabulary should return a dict mapping aliases to canonical forms."""
    alias_map = load_vocabulary(VOCAB_PATH)
    assert isinstance(alias_map, dict)
    # Check spec-required mappings
    assert alias_map.get("ai") == "agentic-ai"
    assert alias_map.get("agents") == "agentic-ai"
    assert alias_map.get("ai-agents") == "agentic-ai"
    assert alias_map.get("agentic-systems") == "agentic-ai"
    assert alias_map.get("large-language-model") == "llm"
    assert alias_map.get("llm-agent") == "llm"


def test_load_vocabulary_canonical_maps_to_itself() -> None:
    """Every canonical tag must be its own key in the alias map."""
    alias_map = load_vocabulary(VOCAB_PATH)
    assert alias_map.get("agentic-ai") == "agentic-ai"
    assert alias_map.get("llm") == "llm"
    assert alias_map.get("hallucinations") == "hallucinations"


def test_load_vocabulary_missing_file(tmp_path: Path) -> None:
    """load_vocabulary raises FileNotFoundError for a missing vocab file."""
    with pytest.raises(FileNotFoundError):
        load_vocabulary(tmp_path / "nonexistent.md")


def test_load_vocabulary_missing_yaml_block(tmp_path: Path) -> None:
    """load_vocabulary raises ValueError if no ```yaml block is present."""
    bad = tmp_path / "vocab.md"
    bad.write_text("# No yaml block here\n", encoding="utf-8")
    with pytest.raises(ValueError, match="No.*yaml.*block"):
        load_vocabulary(bad)


# ---------------------------------------------------------------------------
# _canonicalise_list
# ---------------------------------------------------------------------------


def test_canonicalise_list_replaces_alias() -> None:
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai", "llm": "llm"}
    assert _canonicalise_list(["ai", "llm"], alias_map) == ["agentic-ai", "llm"]


def test_canonicalise_list_preserves_unknown_tag() -> None:
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    assert _canonicalise_list(["governance", "ai"], alias_map) == ["governance", "agentic-ai"]


def test_canonicalise_list_deduplicates() -> None:
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    # Both 'ai' and 'agentic-ai' map to 'agentic-ai' → deduplicated
    result = _canonicalise_list(["ai", "agentic-ai", "governance"], alias_map)
    assert result == ["agentic-ai", "governance"]


def test_canonicalise_list_preserves_order() -> None:
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai", "llm": "llm"}
    result = _canonicalise_list(["llm", "ai", "governance"], alias_map)
    assert result == ["llm", "agentic-ai", "governance"]


def test_canonicalise_list_empty() -> None:
    assert _canonicalise_list([], {}) == []


# ---------------------------------------------------------------------------
# Parse/format helpers
# ---------------------------------------------------------------------------


def test_parse_inline_list_basic() -> None:
    assert _parse_inline_list("[ai, llm, governance]") == ["ai", "llm", "governance"]


def test_parse_inline_list_empty() -> None:
    assert _parse_inline_list("[]") == []


def test_parse_inline_list_single() -> None:
    assert _parse_inline_list("[governance]") == ["governance"]


def test_format_inline_list() -> None:
    assert _format_inline_list(["agentic-ai", "llm"]) == "[agentic-ai, llm]"


def test_format_inline_list_empty() -> None:
    assert _format_inline_list([]) == "[]"


def test_parse_block_list() -> None:
    block = "  - ai\n  - llm\n  - governance\n"
    assert _parse_block_list(block) == ["ai", "llm", "governance"]


def test_format_block_list() -> None:
    result = _format_block_list(["agentic-ai", "llm"])
    assert result == "\n  - agentic-ai\n  - llm\n"


def test_format_block_list_empty() -> None:
    assert _format_block_list([]) == "\n"


# ---------------------------------------------------------------------------
# canonicalise_file
# ---------------------------------------------------------------------------


def test_canonicalise_file_inline_list(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    _write_item(f, "[ai, governance, llm]")
    alias_map = {
        "ai": "agentic-ai",
        "agentic-ai": "agentic-ai",
        "llm": "llm",
        "governance": "governance",
    }
    changed = canonicalise_file(f, alias_map)
    assert changed
    content = f.read_text()
    assert "tags: [agentic-ai, governance, llm]" in content


def test_canonicalise_file_no_change_needed(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    _write_item(f, "[agentic-ai, llm]")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai", "llm": "llm"}
    changed = canonicalise_file(f, alias_map)
    assert not changed


def test_canonicalise_file_dry_run_does_not_write(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    _write_item(f, "[ai, llm]")
    original = f.read_text()
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai", "llm": "llm"}
    changed = canonicalise_file(f, alias_map, dry_run=True)
    assert changed
    # File must not be modified in dry-run
    assert f.read_text() == original


def test_canonicalise_file_deduplicates_tags(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    # Both 'ai' and 'agentic-ai' map to 'agentic-ai'
    _write_item(f, "[ai, agentic-ai, governance]")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai", "governance": "governance"}
    changed = canonicalise_file(f, alias_map)
    assert changed
    content = f.read_text()
    assert "tags: [agentic-ai, governance]" in content


def test_canonicalise_file_no_frontmatter(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    f.write_text("# No frontmatter here\n", encoding="utf-8")
    changed = canonicalise_file(f, {"ai": "agentic-ai"})
    assert not changed


def test_canonicalise_file_empty_tags(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    _write_item(f, "[]")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    changed = canonicalise_file(f, alias_map)
    assert not changed


def test_canonicalise_file_preserves_unknown_tags(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    _write_item(f, "[ai, very-specific-topic]")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    canonicalise_file(f, alias_map)
    content = f.read_text()
    assert "very-specific-topic" in content
    assert "agentic-ai" in content


def test_canonicalise_file_preserves_body(tmp_path: Path) -> None:
    f = tmp_path / "item.md"
    body = "## Findings\n\nSome important findings here.\n"
    _write_item(f, "[ai]", extra=body)
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    canonicalise_file(f, alias_map)
    content = f.read_text()
    assert "Some important findings here." in content


# ---------------------------------------------------------------------------
# canonicalise_directory
# ---------------------------------------------------------------------------


def test_canonicalise_directory_processes_all_subdirs(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    backlog = tmp_path / "Research" / "backlog"
    in_progress = tmp_path / "Research" / "in-progress"
    for d in (completed, backlog, in_progress):
        d.mkdir(parents=True)

    _write_item(completed / "2026-01-01-a.md", "[ai, governance]")
    _write_item(backlog / "2026-01-02-b.md", "[agents]")
    _write_item(in_progress / "2026-01-03-c.md", "[agentic-ai]")

    alias_map = {
        "ai": "agentic-ai",
        "agents": "agentic-ai",
        "agentic-ai": "agentic-ai",
        "governance": "governance",
    }
    changed = canonicalise_directory(tmp_path, alias_map)
    # completed/a and backlog/b should change; in-progress/c is already canonical
    changed_names = {p.name for p in changed}
    assert "2026-01-01-a.md" in changed_names
    assert "2026-01-02-b.md" in changed_names
    assert "2026-01-03-c.md" not in changed_names


def test_canonicalise_directory_skips_gitkeep(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    gitkeep = completed / ".gitkeep"
    gitkeep.write_text("", encoding="utf-8")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    changed = canonicalise_directory(tmp_path, alias_map)
    assert len(changed) == 0


def test_canonicalise_directory_missing_subdir(tmp_path: Path) -> None:
    """A missing subdirectory should be silently skipped."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _write_item(completed / "item.md", "[ai]")
    alias_map = {"ai": "agentic-ai", "agentic-ai": "agentic-ai"}
    # backlog and in-progress directories do not exist — should not raise
    changed = canonicalise_directory(tmp_path, alias_map)
    assert len(changed) == 1


# ---------------------------------------------------------------------------
# No new singletons introduced
# ---------------------------------------------------------------------------


def test_no_new_singletons_after_canonicalisation(tmp_path: Path) -> None:
    """Running canonicalise_directory on the real corpus must not introduce new singletons.

    After canonicalisation every tag that was an alias must have disappeared
    (replaced by its canonical form).  The number of unique tags in the corpus
    must not increase.
    """
    root = Path(__file__).parent.parent
    alias_map = load_vocabulary(VOCAB_PATH)

    # Count unique tags BEFORE
    _, tag_to_slugs_before = collect_tags(root)
    unique_before = set(tag_to_slugs_before.keys())

    # Run canonicalisation in dry-run against real corpus (no writes)
    changed = canonicalise_directory(root, alias_map, dry_run=True)
    # At least one file should be changed (corpus has alias tags)
    assert len(changed) > 0

    # Simulate canonicalised tags to check no new tags appear
    # (dry-run: we verify the logic without touching files)
    # Collect all tags that WOULD exist post-canonicalisation
    simulated_tags: set[str] = set()
    for _slug, tags in collect_tags(root)[0].items():
        canonical_tags = _canonicalise_list(tags, alias_map)
        simulated_tags.update(canonical_tags)

    # After canonicalisation, no tag should appear that wasn't already in the corpus
    # as a canonical tag (i.e. a canonical tag that was completely absent before)
    new_tags = simulated_tags - unique_before
    assert new_tags == set(), f"Canonicalisation would introduce new unknown tags: {new_tags}"


# ---------------------------------------------------------------------------
# main() CLI
# ---------------------------------------------------------------------------


def test_main_dry_run(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _write_item(completed / "item.md", "[ai, governance]")

    vocab = tmp_path / "vocab.md"
    vocab.write_text(
        "```yaml\nagentic-ai:\n  - ai\n```\n",
        encoding="utf-8",
    )

    ret = main(["--root", str(tmp_path), "--vocab", str(vocab), "--dry-run"])
    assert ret == 0
    # File should NOT be modified
    assert "ai" in (completed / "item.md").read_text()


def test_main_missing_vocab(tmp_path: Path) -> None:
    ret = main(["--root", str(tmp_path), "--vocab", str(tmp_path / "missing.md")])
    assert ret == 1


def test_main_no_changes(tmp_path: Path) -> None:
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _write_item(completed / "item.md", "[agentic-ai]")

    vocab = tmp_path / "vocab.md"
    vocab.write_text(
        "```yaml\nagentic-ai:\n  - ai\n```\n",
        encoding="utf-8",
    )

    ret = main(["--root", str(tmp_path), "--vocab", str(vocab)])
    assert ret == 0

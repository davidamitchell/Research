"""Tests for docs/themes-vocabulary.md — vocabulary file structure and integrity."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

VOCAB_PATH = Path(__file__).parent.parent / "docs" / "themes-vocabulary.md"
SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))


# ---------------------------------------------------------------------------
# File existence and basic YAML validity
# ---------------------------------------------------------------------------


def test_themes_vocabulary_file_exists() -> None:
    """docs/themes-vocabulary.md must exist in the repository."""
    assert VOCAB_PATH.exists(), f"Missing vocabulary file: {VOCAB_PATH}"


def _load_yaml_block(path: Path) -> dict:
    """Extract and parse the YAML block from the vocabulary markdown file."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
    assert match, f"No ```yaml block found in {path}"
    parsed = yaml.safe_load(match.group(1))
    assert isinstance(parsed, dict), "YAML block must be a mapping"
    return parsed


def test_themes_yaml_block_is_valid_yaml() -> None:
    """The ```yaml block inside docs/themes-vocabulary.md must be valid YAML."""
    parsed = _load_yaml_block(VOCAB_PATH)
    assert len(parsed) >= 1


def test_themes_yaml_all_values_are_lists() -> None:
    """Every value in the themes YAML block must be a list (list of aliases, may be empty)."""
    parsed = _load_yaml_block(VOCAB_PATH)
    for canonical, aliases in parsed.items():
        assert isinstance(aliases, list), (
            f"Vocabulary entry '{canonical}' value must be a list, got {type(aliases)}"
        )


# ---------------------------------------------------------------------------
# Canonical slug format
# ---------------------------------------------------------------------------


_SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")


def test_all_canonical_slugs_are_lowercase_hyphenated() -> None:
    """Every canonical key must be a lowercase-hyphenated slug (e.g. agentic-ai)."""
    parsed = _load_yaml_block(VOCAB_PATH)
    bad = [k for k in parsed if not _SLUG_RE.match(k)]
    assert not bad, f"Canonical slugs with invalid format: {bad}"


def test_all_alias_slugs_are_lowercase_hyphenated() -> None:
    """Every alias in the synonym lists must be a lowercase-hyphenated slug."""
    parsed = _load_yaml_block(VOCAB_PATH)
    bad: list[str] = []
    for canonical, aliases in parsed.items():
        for alias in aliases:
            if not _SLUG_RE.match(str(alias)):
                bad.append(f"{alias!r} (alias of {canonical!r})")
    assert not bad, f"Alias slugs with invalid format: {bad}"


# ---------------------------------------------------------------------------
# No duplicate canonical slugs
# ---------------------------------------------------------------------------


def test_no_duplicate_canonical_slugs() -> None:
    """The YAML block must not contain duplicate canonical keys."""
    text = VOCAB_PATH.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
    assert match
    yaml_text = match.group(1)
    # Count top-level keys by counting unindented lines that look like YAML keys
    keys = re.findall(r"^([a-z][a-z0-9-]+):", yaml_text, re.MULTILINE)
    duplicates = [k for k in keys if keys.count(k) > 1]
    assert not duplicates, f"Duplicate canonical slugs in YAML block: {set(duplicates)}"


# ---------------------------------------------------------------------------
# Synonym map integrity — aliases resolve to known canonicals
# ---------------------------------------------------------------------------


def test_no_alias_equals_its_canonical() -> None:
    """An alias must not be identical to its canonical slug."""
    parsed = _load_yaml_block(VOCAB_PATH)
    violations: list[str] = []
    for canonical, aliases in parsed.items():
        for alias in aliases:
            if alias == canonical:
                violations.append(f"{alias!r} is an alias of itself")
    assert not violations, f"Self-aliasing entries: {violations}"


def test_no_alias_is_also_a_canonical() -> None:
    """No alias may also appear as a top-level canonical slug."""
    parsed = _load_yaml_block(VOCAB_PATH)
    canonicals = set(parsed.keys())
    violations: list[str] = []
    for canonical, aliases in parsed.items():
        for alias in aliases:
            if alias in canonicals:
                violations.append(
                    f"{alias!r} is both a canonical slug and an alias of {canonical!r}"
                )
    assert not violations, f"Aliases that are also canonicals: {violations}"


def test_no_alias_appears_in_multiple_canonical_lists() -> None:
    """Each alias must map to exactly one canonical slug."""
    parsed = _load_yaml_block(VOCAB_PATH)
    alias_to_canonical: dict[str, list[str]] = {}
    for canonical, aliases in parsed.items():
        for alias in aliases:
            alias_to_canonical.setdefault(alias, []).append(canonical)
    duplicates = {a: cs for a, cs in alias_to_canonical.items() if len(cs) > 1}
    assert not duplicates, f"Aliases mapping to multiple canonicals: {duplicates}"


# ---------------------------------------------------------------------------
# Vocabulary size (operational constraint)
# ---------------------------------------------------------------------------


def test_vocabulary_has_at_least_16_canonical_themes() -> None:
    """Vocabulary must contain at least 16 themes (the minimum from the ai_themes baseline)."""
    parsed = _load_yaml_block(VOCAB_PATH)
    assert len(parsed) >= 16, (
        f"Vocabulary only has {len(parsed)} canonical themes; expected at least 16"
    )


def test_vocabulary_has_at_most_40_canonical_themes() -> None:
    """Vocabulary must not exceed 40 canonical themes at launch (growth-policy ceiling)."""
    parsed = _load_yaml_block(VOCAB_PATH)
    assert len(parsed) <= 40, f"Vocabulary has {len(parsed)} canonical themes; ceiling is 40"


# ---------------------------------------------------------------------------
# Prose table consistency — every canonical in YAML block has a prose row
# ---------------------------------------------------------------------------


def test_all_yaml_canonicals_appear_in_prose_table() -> None:
    """Every canonical slug in the YAML block must also appear in the Markdown table."""
    text = VOCAB_PATH.read_text(encoding="utf-8")
    parsed = _load_yaml_block(VOCAB_PATH)
    missing = [slug for slug in parsed if f"`{slug}`" not in text]
    assert not missing, f"Canonical slugs in YAML block but absent from prose table: {missing}"

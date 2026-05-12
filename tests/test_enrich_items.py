"""Tests for scripts/enrich_items.py — frontmatter helpers and theme parsing."""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Import helpers from enrich_items (via sys.path insert in the module itself).
# ---------------------------------------------------------------------------
import sys
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.enrich_items import (
    _build_prompt,
    _extract_summary,
    _has_ai_themes,
    _insert_ai_themes,
    _parse_themes,
    _reconstruct,
    _split_frontmatter,
)

# ---------------------------------------------------------------------------
# _split_frontmatter
# ---------------------------------------------------------------------------


class TestSplitFrontmatter:
    def test_valid_frontmatter(self) -> None:
        text = "---\ntitle: Test\n---\n\nBody text."
        fence, yaml_block, body = _split_frontmatter(text)
        assert fence == "---"
        assert "title: Test" in yaml_block
        assert body == "Body text."

    def test_no_frontmatter(self) -> None:
        text = "Just body text."
        fence, yaml_block, body = _split_frontmatter(text)
        assert fence == ""
        assert yaml_block == ""
        assert body == "Just body text."

    def test_unclosed_frontmatter(self) -> None:
        text = "---\ntitle: Test\n"
        fence, yaml_block, body = _split_frontmatter(text)
        assert fence == ""  # not closed → treat as no frontmatter

    def test_crlf_line_endings(self) -> None:
        text = "---\r\ntitle: CRLF\r\n---\r\n\r\nBody."
        fence, yaml_block, body = _split_frontmatter(text)
        assert fence == "---"
        assert "title: CRLF" in yaml_block
        assert body == "Body."

    def test_embedded_dash_fence_in_yaml_value(self) -> None:
        # A YAML value containing "---" must not be mistaken for the closing fence.
        text = '---\ntitle: foo\ndescription: "a --- b"\n---\n\nBody.'
        fence, yaml_block, body = _split_frontmatter(text)
        assert fence == "---"
        assert "description" in yaml_block
        assert body == "Body."


# ---------------------------------------------------------------------------
# _has_ai_themes
# ---------------------------------------------------------------------------


class TestHasAiThemes:
    def test_detects_ai_themes_field(self) -> None:
        yaml_block = "title: Foo\nai_themes: [agentic-ai]\ntags: [ai]"
        assert _has_ai_themes(yaml_block) is True

    def test_no_ai_themes_field(self) -> None:
        yaml_block = "title: Foo\ntags: [ai]"
        assert _has_ai_themes(yaml_block) is False

    def test_ai_themes_with_spaces(self) -> None:
        yaml_block = "title: Foo\nai_themes : []\n"
        assert _has_ai_themes(yaml_block) is True


# ---------------------------------------------------------------------------
# _insert_ai_themes
# ---------------------------------------------------------------------------


class TestInsertAiThemes:
    def test_inserts_after_tags(self) -> None:
        yaml_block = "title: Foo\ntags: [ai, llm]\nstatus: completed"
        result = _insert_ai_themes(yaml_block, ["agentic-ai", "llm-reasoning"])
        lines = result.splitlines()
        tags_idx = next(i for i, line in enumerate(lines) if line.startswith("tags:"))
        themes_idx = next(i for i, line in enumerate(lines) if line.startswith("ai_themes:"))
        assert themes_idx == tags_idx + 1

    def test_appends_when_no_tags(self) -> None:
        yaml_block = "title: Foo\nstatus: completed"
        result = _insert_ai_themes(yaml_block, ["agentic-ai"])
        assert result.endswith("ai_themes: [agentic-ai]")

    def test_themes_formatted_correctly(self) -> None:
        result = _insert_ai_themes("title: Foo\ntags: [x]", ["a", "b"])
        assert "ai_themes: [a, b]" in result


# ---------------------------------------------------------------------------
# _reconstruct
# ---------------------------------------------------------------------------


class TestReconstruct:
    def test_round_trip(self) -> None:
        yaml_block = "title: Test\ntags: [x]"
        body = "## Section\n\nContent."
        result = _reconstruct(yaml_block, body)
        assert result.startswith("---\n")
        assert "title: Test" in result
        assert "## Section" in result


# ---------------------------------------------------------------------------
# _parse_themes
# ---------------------------------------------------------------------------


class TestParseThemes:
    def test_plain_json_array(self) -> None:
        assert _parse_themes('["agentic-ai", "memory-context"]') == ["agentic-ai", "memory-context"]

    def test_json_in_code_fence(self) -> None:
        raw = '```json\n["agentic-ai"]\n```'
        assert _parse_themes(raw) == ["agentic-ai"]

    def test_embedded_array_in_prose(self) -> None:
        raw = 'The themes are: ["agentic-ai", "llm-reasoning"] based on the content.'
        result = _parse_themes(raw)
        assert result is not None
        assert "agentic-ai" in result

    def test_empty_response(self) -> None:
        assert _parse_themes("") is None

    def test_unparseable(self) -> None:
        assert _parse_themes("I cannot classify this item.") is None

    def test_lowercases_themes(self) -> None:
        assert _parse_themes('["Agentic-AI", "LLM-Reasoning"]') == ["agentic-ai", "llm-reasoning"]


# ---------------------------------------------------------------------------
# _extract_summary
# ---------------------------------------------------------------------------


class TestExtractSummary:
    def test_extracts_findings_section(self) -> None:
        body = textwrap.dedent("""\
            ## Findings

            Key finding here about AI systems.

            ## Sources
        """)
        summary = _extract_summary(body, max_chars=100)
        assert "Key finding" in summary
        assert "## Sources" not in summary

    def test_falls_back_to_body_when_no_findings(self) -> None:
        body = "Some content without a Findings section."
        summary = _extract_summary(body, max_chars=50)
        assert "Some content" in summary

    def test_respects_max_chars(self) -> None:
        body = "A" * 500
        summary = _extract_summary(body, max_chars=100)
        assert len(summary) <= 100


# ---------------------------------------------------------------------------
# _build_prompt
# ---------------------------------------------------------------------------


class TestBuildPrompt:
    def test_includes_title_and_tags(self) -> None:
        prompt = _build_prompt("Test Title", "ai, llm", "Summary text.")
        assert "Test Title" in prompt
        assert "ai, llm" in prompt
        assert "Summary text." in prompt

    def test_includes_theme_list(self) -> None:
        from scripts.enrich_items import _AI_THEMES

        prompt = _build_prompt("T", "t", "s")
        for theme in _AI_THEMES:
            assert theme in prompt


# ---------------------------------------------------------------------------
# enrich_item — integration-level (mocks Gemini call)
# ---------------------------------------------------------------------------


class TestEnrichItem:
    def _make_item(self, tmp_path: Path, has_ai_themes: bool = False) -> Path:
        if has_ai_themes:
            content = textwrap.dedent("""\
                ---
                title: "Test Item"
                tags: [ai]
                ai_themes: [agentic-ai]
                status: completed
                ---

                ## Findings

                Some findings here.
            """)
        else:
            content = textwrap.dedent("""\
                ---
                title: "Test Item"
                tags: [ai]
                status: completed
                ---

                ## Findings

                Some findings here.
            """)
        p = tmp_path / "2026-01-01-test.md"
        p.write_text(content, encoding="utf-8")
        return p

    def _make_cascade(self) -> MagicMock:
        cascade = MagicMock()
        cascade.model = "gemini-3-flash"
        cascade.all_exhausted = False
        cascade.check_daily_quota_header.return_value = False
        return cascade

    def test_skips_already_enriched(self, tmp_path: Path) -> None:
        from scripts.enrich_items import enrich_item

        path = self._make_item(tmp_path, has_ai_themes=True)
        cascade = self._make_cascade()
        client = MagicMock()

        result = enrich_item(path, client, cascade, dry_run=True)
        assert result is False
        cascade.wait.assert_not_called()

    def test_skips_when_cascade_exhausted(self, tmp_path: Path) -> None:
        from scripts.enrich_items import enrich_item

        path = self._make_item(tmp_path)
        cascade = self._make_cascade()
        cascade.all_exhausted = True
        client = MagicMock()

        result = enrich_item(path, client, cascade, dry_run=True)
        assert result is False

    def test_enriches_item_dry_run(self, tmp_path: Path) -> None:
        from scripts.enrich_items import enrich_item

        path = self._make_item(tmp_path)
        cascade = self._make_cascade()
        client = MagicMock()

        mock_response = MagicMock()
        mock_response.text = '["agentic-ai", "llm-reasoning"]'
        client.models.generate_content.return_value = mock_response

        with patch(
            "scripts.enrich_items._generate_themes", return_value=(["agentic-ai"], "gemini-3-flash")
        ):
            result = enrich_item(path, client, cascade, dry_run=True)

        assert result is True
        # File should be unchanged in dry_run mode.
        assert "ai_themes" not in path.read_text(encoding="utf-8")

    def test_enriches_item_writes_file(self, tmp_path: Path) -> None:
        from scripts.enrich_items import enrich_item

        path = self._make_item(tmp_path)
        cascade = self._make_cascade()
        client = MagicMock()

        with patch(
            "scripts.enrich_items._generate_themes",
            return_value=(["agentic-ai", "llm-reasoning"], "gemini-3-flash"),
        ):
            result = enrich_item(path, client, cascade, dry_run=False)

        assert result is True
        written = path.read_text(encoding="utf-8")
        assert "ai_themes: [agentic-ai, llm-reasoning]" in written


class TestGenerateThemes:
    """Unit tests for _generate_themes — cascade advance on errors."""

    # Patch sys.modules so `from google.genai import types` succeeds in the
    # broken test environment where _cffi_backend is missing.
    _GENAI_MODULES = {
        "google.genai": MagicMock(),
        "google.genai.types": MagicMock(),
        "google.genai.errors": MagicMock(),
    }

    def _make_cascade(self, model: str = "gemini-3-flash") -> MagicMock:
        cascade = MagicMock()
        cascade.model = model
        cascade.all_exhausted = False
        cascade.check_daily_quota_header.return_value = False
        return cascade

    def test_returns_failed_model_name_on_exception(self) -> None:
        """Returns (None, <failed model>) — the model that errored, not the next one.

        Before the fix, cascade.model was read AFTER advance(), returning the new model.
        """
        from scripts.enrich_items import _generate_themes

        cascade = self._make_cascade("gemini-3-flash")

        # Simulate advance changing the model name (as the real cascade would).
        def _advance() -> bool:
            cascade.model = "gemini-3.1-flash-lite"
            return True

        cascade.advance.side_effect = _advance
        client = MagicMock()
        client.models.generate_content.side_effect = RuntimeError("network error")

        with (
            patch.dict("sys.modules", self._GENAI_MODULES),
            patch("scripts.enrich_items._THINKING_MODELS", frozenset()),
        ):
            themes, model_used = _generate_themes(client, cascade, "prompt")

        assert themes is None
        assert model_used == "gemini-3-flash"  # failing model, not the next one

    def test_cascade_advance_called_on_exception(self) -> None:
        """cascade.advance() is called exactly once whenever the API call raises."""
        from scripts.enrich_items import _generate_themes

        cascade = self._make_cascade("gemini-3-flash")
        client = MagicMock()
        client.models.generate_content.side_effect = RuntimeError("unexpected")

        with (
            patch.dict("sys.modules", self._GENAI_MODULES),
            patch("scripts.enrich_items._THINKING_MODELS", frozenset()),
        ):
            themes, _ = _generate_themes(client, cascade, "prompt")

        assert themes is None
        cascade.advance.assert_called_once()

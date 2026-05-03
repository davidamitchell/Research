"""Tests for scripts/eval_harness.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# Make scripts/ importable in tests.
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from eval_harness import (  # noqa: E402
    PROCESSES,
    build_process_prompt,
    evaluate_item,
    extract_approach,
    extract_frontmatter,
    extract_frontmatter_tags,
    extract_key_findings,
    extract_question,
    extract_title_from_frontmatter,
    format_markdown_report,
    generate_eval_report,
    main,
    sample_items,
    score_coverage_overlap,
    score_perspective_slots,
    score_structural_completeness,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_SAMPLE_ITEM = """\
---
title: "How do agents retain context across sessions?"
added: 2026-03-01
status: completed
priority: medium
tags: [agentic-ai, memory-system, context-engineering]
---

# How do agents retain context across sessions?

## Research Question

How do artificial intelligence agents retain context and knowledge across
multiple independent sessions without relying on a persistent in-process
state?

## Approach

1. Survey memory architectures used in production agent systems.
2. Assess the trade-offs between in-context memory and external storage.
3. Identify failure modes when cross-session context is lost or corrupted.

## Sources

- https://example.com/memory-agents

## Findings

### Executive Summary

Agents typically use external stores such as vector databases, knowledge
graphs, or structured summaries to persist context across sessions.

### Key Findings

1. **External memory stores are the dominant cross-session retention pattern.**
   ([fact]; high confidence; source: https://example.com/memory-agents)
2. **In-context retrieval is bounded by the context window.**
   ([inference]; medium confidence; source: https://example.com/context-limits)
"""

_MINIMAL_ITEM = """\
---
title: Minimal
added: 2026-01-01
status: completed
priority: low
tags: [llm]
---

# Minimal
"""

# A well-formed perspective-discovery response containing all four STORM lens
# labels and all required structural patterns.  Used across multiple tests that
# need a response which satisfies structural_completeness == 1.0.
_FAKE_PERSPECTIVE_RESPONSE = (
    "Perspective: basic facts\n"
    "Distinct coverage added: covers background definitions.\n"
    "Seed question: What is cross-session memory?\n"
    "Evidence to seek: academic surveys\n\n"
    "Perspective: mechanism\n"
    "Distinct coverage added: covers implementation.\n"
    "Seed question: How do vector databases store embeddings?\n"
    "Evidence to seek: technical documentation\n\n"
    "Perspective: stakeholder\n"
    "Distinct coverage added: covers decision impact.\n"
    "Seed question: Who bears the cost of memory failure?\n"
    "Evidence to seek: user research\n\n"
    "Perspective: failure\n"
    "Distinct coverage added: covers failure modes.\n"
    "Seed question: When does context corruption occur?\n"
    "Evidence to seek: incident reports"
)

# Minimal response that satisfies structural_completeness checks for
# perspective-discovery but is not semantically complete (only one slot).
_MINIMAL_PERSPECTIVE_RESPONSE = (
    "Perspective: basic facts\n"
    "Seed question: What is X?\n"
    "Distinct coverage added: D\n"
    "Evidence to seek: papers"
)


def _make_item(tmp_path: Path, slug: str, content: str) -> Path:
    path = tmp_path / f"{slug}.md"
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# PROCESSES registry
# ---------------------------------------------------------------------------


def test_all_required_process_keys() -> None:
    """Each process entry must have all required keys."""
    required_keys = {"description", "prompt_template", "required_patterns", "compare_against"}
    for name, cfg in PROCESSES.items():
        assert required_keys.issubset(set(cfg.keys())), (
            f"Process '{name}' is missing keys: {required_keys - set(cfg.keys())}"
        )


def test_process_names() -> None:
    """The expected process names are present."""
    assert "perspective-discovery" in PROCESSES
    assert "question-decomposition" in PROCESSES
    assert "adversarial-challenge" in PROCESSES


def test_perspective_discovery_required_patterns() -> None:
    """Perspective-discovery required patterns include the four mandatory output fields."""
    patterns = PROCESSES["perspective-discovery"]["required_patterns"]
    assert any("Perspective:" in p for p in patterns)
    assert any("Seed question:" in p for p in patterns)


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------


def test_extract_frontmatter_present() -> None:
    fm = extract_frontmatter(_SAMPLE_ITEM)
    assert fm is not None
    assert "title" in fm


def test_extract_frontmatter_absent() -> None:
    assert extract_frontmatter("# No frontmatter\n") is None


def test_extract_frontmatter_tags_inline(tmp_path: Path) -> None:
    content = "---\ntitle: T\ntags: [agentic-ai, llm, workflow]\n---\n# Body\n"
    tags = extract_frontmatter_tags(content)
    assert tags == ["agentic-ai", "llm", "workflow"]


def test_extract_frontmatter_tags_block(tmp_path: Path) -> None:
    content = "---\ntitle: T\ntags:\n  - agentic-ai\n  - llm\n---\n# Body\n"
    tags = extract_frontmatter_tags(content)
    assert tags == ["agentic-ai", "llm"]


def test_extract_frontmatter_tags_empty() -> None:
    content = "---\ntitle: T\ntags: []\n---\n# Body\n"
    assert extract_frontmatter_tags(content) == []


def test_extract_question() -> None:
    q = extract_question(_SAMPLE_ITEM)
    assert "artificial intelligence agents" in q
    assert "## Approach" not in q


def test_extract_question_not_found() -> None:
    assert extract_question(_MINIMAL_ITEM) == ""


def test_extract_approach() -> None:
    a = extract_approach(_SAMPLE_ITEM)
    assert "memory architectures" in a
    assert "Key Findings" not in a


def test_extract_approach_not_found() -> None:
    assert extract_approach(_MINIMAL_ITEM) == ""


def test_extract_key_findings() -> None:
    kf = extract_key_findings(_SAMPLE_ITEM)
    assert "External memory stores" in kf
    assert "Evidence Map" not in kf


def test_extract_key_findings_not_found() -> None:
    assert extract_key_findings(_MINIMAL_ITEM) == ""


def test_extract_title_from_frontmatter() -> None:
    t = extract_title_from_frontmatter(_SAMPLE_ITEM)
    assert "agents retain context" in t


def test_extract_title_missing() -> None:
    assert extract_title_from_frontmatter("# No FM\n") == ""


def test_section_stops_at_next_same_level() -> None:
    """Approach section must not bleed into Sources or Findings."""
    a = extract_approach(_SAMPLE_ITEM)
    assert "## Sources" not in a
    assert "## Findings" not in a


# ---------------------------------------------------------------------------
# Sampling
# ---------------------------------------------------------------------------


def test_sample_items_returns_n(tmp_path: Path) -> None:
    for i in range(8):
        _make_item(tmp_path, f"item-{i}", _SAMPLE_ITEM)
    result = sample_items(tmp_path, n=5, seed=1)
    assert len(result) == 5
    assert all(isinstance(p, Path) for p in result)


def test_sample_items_clamps_to_available(tmp_path: Path) -> None:
    for i in range(3):
        _make_item(tmp_path, f"item-{i}", _SAMPLE_ITEM)
    result = sample_items(tmp_path, n=10, seed=1)
    assert len(result) == 3


def test_sample_items_empty_dir(tmp_path: Path) -> None:
    result = sample_items(tmp_path, n=5)
    assert result == []


def test_sample_items_seed_reproducible(tmp_path: Path) -> None:
    for i in range(10):
        _make_item(tmp_path, f"item-{i}", _SAMPLE_ITEM)
    r1 = [p.stem for p in sample_items(tmp_path, n=4, seed=99)]
    r2 = [p.stem for p in sample_items(tmp_path, n=4, seed=99)]
    assert r1 == r2


def test_sample_items_different_seeds_usually_differ(tmp_path: Path) -> None:
    for i in range(20):
        _make_item(tmp_path, f"item-{i:02d}", _SAMPLE_ITEM)
    r1 = [p.stem for p in sample_items(tmp_path, n=10, seed=1)]
    r2 = [p.stem for p in sample_items(tmp_path, n=10, seed=2)]
    # With 20 items and seed 1 vs 2, at least one element should differ.
    assert r1 != r2


def test_sample_items_ignores_gitkeep(tmp_path: Path) -> None:
    _make_item(tmp_path, "item-1", _SAMPLE_ITEM)
    (tmp_path / ".gitkeep").write_text("")
    result = sample_items(tmp_path, n=10)
    assert all(p.name != ".gitkeep" for p in result)


# ---------------------------------------------------------------------------
# Prompt building
# ---------------------------------------------------------------------------


def test_build_process_prompt_perspective_discovery() -> None:
    context = {
        "question": "What is the impact of X on Y?",
        "approach": "1. Sub-Q1\n2. Sub-Q2",
        "key_findings": "",
        "tags_list": ["agentic-ai", "llm"],
    }
    prompt = build_process_prompt("perspective-discovery", context)
    assert "What is the impact of X on Y?" in prompt
    assert "Perspective:" in prompt
    assert "Seed question:" in prompt


def test_build_process_prompt_question_decomposition() -> None:
    context = {
        "question": "How does memory affect performance?",
        "approach": "1. Survey approaches\n2. Compare benchmarks",
        "key_findings": "",
        "tags_list": ["memory-system"],
    }
    prompt = build_process_prompt("question-decomposition", context)
    assert "How does memory affect performance?" in prompt
    assert "Survey approaches" in prompt


def test_build_process_prompt_adversarial_challenge() -> None:
    context = {
        "question": "Does approach A work?",
        "approach": "",
        "key_findings": "Finding 1: A works well.",
        "tags_list": [],
    }
    prompt = build_process_prompt("adversarial-challenge", context)
    assert "Finding 1: A works well." in prompt
    assert "[unresolved objection]" in prompt


def test_build_process_prompt_unknown_process() -> None:
    with pytest.raises(KeyError):
        build_process_prompt("nonexistent-process", {"question": "Q"})


def test_build_process_prompt_tags_formatted() -> None:
    context = {
        "question": "Q",
        "approach": "",
        "key_findings": "",
        "tags_list": ["tag-a", "tag-b", "tag-c"],
    }
    prompt = build_process_prompt("perspective-discovery", context)
    assert "tag-a, tag-b, tag-c" in prompt


def test_build_process_prompt_empty_tags() -> None:
    context = {
        "question": "Q",
        "approach": "",
        "key_findings": "",
        "tags_list": [],
    }
    prompt = build_process_prompt("perspective-discovery", context)
    assert "(none)" in prompt


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def test_score_structural_completeness_all_found() -> None:
    patterns = ["Perspective:", "Seed question:"]
    text = "Perspective: basic facts\nSeed question: What is X?"
    assert score_structural_completeness(text, patterns) == 1.0


def test_score_structural_completeness_none_found() -> None:
    patterns = ["Perspective:", "Seed question:"]
    assert score_structural_completeness("Some unrelated text", patterns) == 0.0


def test_score_structural_completeness_partial() -> None:
    patterns = ["Perspective:", "Seed question:", "Evidence to seek:"]
    text = "Perspective: basic facts\nSeed question: What is X?"
    score = score_structural_completeness(text, patterns)
    assert abs(score - 2 / 3) < 0.01


def test_score_structural_completeness_case_insensitive() -> None:
    patterns = ["Perspective:"]
    assert score_structural_completeness("perspective: basic facts", patterns) == 1.0


def test_score_structural_completeness_empty_patterns() -> None:
    assert score_structural_completeness("anything", []) == 1.0


def test_score_coverage_overlap_identical() -> None:
    text = "memory agents context session persistent"
    assert score_coverage_overlap(text, text) == 1.0


def test_score_coverage_overlap_disjoint() -> None:
    assert score_coverage_overlap("alpha beta gamma", "delta epsilon zeta") == 0.0


def test_score_coverage_overlap_partial() -> None:
    generated = "memory agents context novel"
    reference = "memory agents session persistent"
    score = score_coverage_overlap(generated, reference)
    assert 0 < score < 1


def test_score_coverage_overlap_empty_both() -> None:
    assert score_coverage_overlap("", "") == 0.0


def test_score_coverage_overlap_short_words_excluded() -> None:
    # Words ≤ 3 chars should not contribute
    assert score_coverage_overlap("a to of", "a to of") == 0.0


def test_score_perspective_slots_all_four() -> None:
    text = "basic facts mechanism stakeholder failure-mode"
    assert score_perspective_slots(text) == 1.0


def test_score_perspective_slots_two_found() -> None:
    text = "basic facts and mechanism present"
    assert score_perspective_slots(text) == 0.5


def test_score_perspective_slots_none() -> None:
    assert score_perspective_slots("unrelated text here") == 0.0


# ---------------------------------------------------------------------------
# evaluate_item
# ---------------------------------------------------------------------------


def test_evaluate_item_no_response(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "test-item", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery", response_text=None)
    assert result["slug"] == "test-item"
    assert result["response"] is None
    assert result["scores"] is None
    assert "Perspective:" in result["prompt"]


def test_evaluate_item_with_response(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "test-item", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery", response_text=_FAKE_PERSPECTIVE_RESPONSE)
    assert result["scores"] is not None
    assert "structural_completeness" in result["scores"]
    assert "coverage_overlap" in result["scores"]
    assert "perspective_slots" in result["scores"]
    assert result["scores"]["structural_completeness"] == 1.0


def test_evaluate_item_scores_populated(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "scored-item", _SAMPLE_ITEM)
    result = evaluate_item(
        path, "perspective-discovery", response_text=_MINIMAL_PERSPECTIVE_RESPONSE
    )
    assert result["scores"]["structural_completeness"] > 0
    assert 0.0 <= result["scores"]["coverage_overlap"] <= 1.0


def test_evaluate_item_extracts_question(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "q-item", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery")
    assert "artificial intelligence agents" in result["question"]


# ---------------------------------------------------------------------------
# generate_eval_report
# ---------------------------------------------------------------------------


def test_generate_eval_report_schema(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "rpt-item", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery")
    report = generate_eval_report([result], "perspective-discovery", n=1, seed=42)
    assert "meta" in report
    assert "results" in report
    assert report["meta"]["process"] == "perspective-discovery"
    assert report["meta"]["n_requested"] == 1
    assert report["meta"]["seed"] == 42
    assert isinstance(report["results"], list)


def test_generate_eval_report_summary_when_scored(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "scored-rpt", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery", response_text=_FAKE_PERSPECTIVE_RESPONSE)
    report = generate_eval_report([result], "perspective-discovery", n=1, seed=1)
    assert report["meta"]["scored"] is True
    assert "summary" in report["meta"]
    assert "mean_structural_completeness" in report["meta"]["summary"]
    assert "mean_perspective_slots" in report["meta"]["summary"]


def test_generate_eval_report_no_summary_when_unscored(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "unscored-rpt", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery", response_text=None)
    report = generate_eval_report([result], "perspective-discovery", n=1, seed=None)
    assert report["meta"]["scored"] is False
    assert "summary" not in report["meta"]


def test_generate_eval_report_multiple_items(tmp_path: Path) -> None:
    paths = [_make_item(tmp_path, f"multi-{i}", _SAMPLE_ITEM) for i in range(3)]
    results = [evaluate_item(p, "question-decomposition") for p in paths]
    report = generate_eval_report(results, "question-decomposition", n=3, seed=7)
    assert len(report["results"]) == 3
    assert report["meta"]["n_sampled"] == 3


# ---------------------------------------------------------------------------
# format_markdown_report
# ---------------------------------------------------------------------------


def test_format_markdown_report_contains_process_name(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "md-item", _SAMPLE_ITEM)
    result = evaluate_item(path, "perspective-discovery")
    report = generate_eval_report([result], "perspective-discovery", n=1, seed=0)
    md = format_markdown_report(report)
    assert "perspective-discovery" in md
    assert "md-item" in md
    assert "Process Prompt" in md


def test_format_markdown_report_includes_scores_when_present(tmp_path: Path) -> None:
    path = _make_item(tmp_path, "scored-md", _SAMPLE_ITEM)
    result = evaluate_item(
        path, "perspective-discovery", response_text=_MINIMAL_PERSPECTIVE_RESPONSE
    )
    report = generate_eval_report([result], "perspective-discovery", n=1, seed=0)
    md = format_markdown_report(report)
    assert "Scores" in md or "structural_completeness" in md


# ---------------------------------------------------------------------------
# main() — CLI integration
# ---------------------------------------------------------------------------


def test_main_writes_json_and_markdown(tmp_path: Path) -> None:
    """main() produces a valid JSON report and a Markdown report."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    for i in range(3):
        _make_item(completed, f"cli-item-{i}", _SAMPLE_ITEM)

    output_dir = tmp_path / "state" / "eval_reports"

    sys.argv = [
        "eval_harness.py",
        "--process",
        "perspective-discovery",
        "--n",
        "2",
        "--seed",
        "1",
        "--completed-dir",
        str(completed),
        "--output-dir",
        str(output_dir),
    ]
    main()

    json_files = list(output_dir.glob("*.json"))
    md_files = list(output_dir.glob("*.md"))
    assert len(json_files) == 1
    assert len(md_files) == 1

    data = json.loads(json_files[0].read_text())
    assert "meta" in data
    assert "results" in data
    assert data["meta"]["process"] == "perspective-discovery"
    assert data["meta"]["n_sampled"] == 2


def test_main_with_responses_dir_scores_items(tmp_path: Path) -> None:
    """When --responses-dir is provided with response files, items are scored."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    _make_item(completed, "resp-item", _SAMPLE_ITEM)

    responses_dir = tmp_path / "responses"
    responses_dir.mkdir()
    (responses_dir / "resp-item.txt").write_text(
        _FAKE_PERSPECTIVE_RESPONSE,
        encoding="utf-8",
    )

    output_dir = tmp_path / "state" / "eval_reports"

    sys.argv = [
        "eval_harness.py",
        "--process",
        "perspective-discovery",
        "--n",
        "1",
        "--seed",
        "42",
        "--completed-dir",
        str(completed),
        "--responses-dir",
        str(responses_dir),
        "--output-dir",
        str(output_dir),
    ]
    main()

    json_files = list(output_dir.glob("*.json"))
    data = json.loads(json_files[0].read_text())
    assert data["meta"]["scored"] is True
    assert data["results"][0]["scores"] is not None


def test_main_list_processes(capsys) -> None:
    """--list-processes prints process names and exits cleanly."""
    sys.argv = ["eval_harness.py", "--list-processes"]
    main()
    out = capsys.readouterr().out
    assert "perspective-discovery" in out
    assert "question-decomposition" in out
    assert "adversarial-challenge" in out


def test_main_empty_completed_dir(tmp_path: Path) -> None:
    """main() exits with code 0 when no completed items are found."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    output_dir = tmp_path / "out"

    sys.argv = [
        "eval_harness.py",
        "--process",
        "perspective-discovery",
        "--n",
        "3",
        "--completed-dir",
        str(completed),
        "--output-dir",
        str(output_dir),
    ]
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 0


def test_main_report_stem_contains_process_and_n(tmp_path: Path) -> None:
    """The output filename encodes the process name and sample size."""
    completed = tmp_path / "Research" / "completed"
    completed.mkdir(parents=True)
    for i in range(2):
        _make_item(completed, f"fn-item-{i}", _SAMPLE_ITEM)

    output_dir = tmp_path / "state" / "eval_reports"

    sys.argv = [
        "eval_harness.py",
        "--process",
        "adversarial-challenge",
        "--n",
        "2",
        "--seed",
        "7",
        "--completed-dir",
        str(completed),
        "--output-dir",
        str(output_dir),
    ]
    main()

    json_files = list(output_dir.glob("*.json"))
    assert len(json_files) == 1
    assert "adversarial-challenge" in json_files[0].stem
    assert "n2" in json_files[0].stem
    assert "seed7" in json_files[0].stem

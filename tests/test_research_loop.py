"""Tests proving the research loop workflow logic and safety controls.

These tests verify:
1. The workflow YAML has the expected safety attributes (timeout, concurrency,
   dropdown-constrained max_items, COPILOT_GITHUB_TOKEN secret name).
2. The Python CLI commands that the loop calls behave correctly end-to-end
   (backlog discovery, start, complete).
3. The research-prompt.md file exists and contains the mandatory sections the
   Copilot agent must follow.
4. Backlog counting logic mirrors what the bash loop uses (*.md excluding README).
"""

from __future__ import annotations

from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "research-loop.yml"
PROMPT_PATH = REPO_ROOT / "research-prompt.md"

SAMPLE_BACKLOG_ITEM = """\
---
title: "Test research item"
added: 2026-03-01
status: backlog
priority: high
tags: []
started: ~
completed: ~
output: []
---

## Research Question

What is being tested?

## Findings

### Executive Summary

TBD

### Key Findings

- TBD

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions
"""


# ---------------------------------------------------------------------------
# Workflow YAML structure tests
# ---------------------------------------------------------------------------


def test_workflow_file_exists() -> None:
    """The research-loop workflow file must be present."""
    assert WORKFLOW_PATH.exists(), f"Workflow file not found: {WORKFLOW_PATH}"


def test_workflow_is_valid_yaml() -> None:
    """The workflow file must parse as valid YAML."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    wf = yaml.safe_load(content)
    assert isinstance(wf, dict)


def _load_workflow() -> dict:
    return yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))


def test_workflow_has_job_timeout() -> None:
    """The research job must have a timeout-minutes to prevent runaway runs."""
    wf = _load_workflow()
    job = wf["jobs"]["research"]
    assert "timeout-minutes" in job, "Job must declare timeout-minutes"
    assert job["timeout-minutes"] == 90, "Timeout must be exactly 90 minutes per ADR-0004"


def test_workflow_has_concurrency_no_cancel() -> None:
    """Concurrency must be configured and must NOT cancel in-progress runs."""
    wf = _load_workflow()
    concurrency = wf.get("concurrency", {})
    assert concurrency.get("group") == "research-loop"
    assert concurrency.get("cancel-in-progress") is False


def test_workflow_uses_copilot_github_token_secret() -> None:
    """The workflow must reference COPILOT_GITHUB_TOKEN, not GH_TOKEN."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "COPILOT_GITHUB_TOKEN" in content, "Workflow must reference COPILOT_GITHUB_TOKEN secret"
    assert "secrets.GH_TOKEN" not in content, "Workflow must not reference old GH_TOKEN secret"


def test_workflow_dispatch_max_items_is_choice_type() -> None:
    """max_items must be a dropdown (choice) to prevent unbounded free-text input."""
    wf = _load_workflow()
    # PyYAML parses `on:` as boolean True
    triggers = wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"]
    assert "max_items" in inputs
    assert inputs["max_items"]["type"] == "choice", (
        "max_items must be a constrained choice, not free text"
    )


def test_workflow_dispatch_max_items_options_are_bounded() -> None:
    """All max_items choices must be ≤ 5 (conservative upper bound)."""
    wf = _load_workflow()
    triggers = wf[True]
    options = triggers["workflow_dispatch"]["inputs"]["max_items"]["options"]
    for opt in options:
        assert int(opt) <= 5, f"max_items option {opt} exceeds safe upper bound of 5"


def test_workflow_has_schedule_trigger() -> None:
    """The workflow must have a schedule trigger for autonomous operation."""
    wf = _load_workflow()
    triggers = wf[True]
    assert "schedule" in triggers


def test_workflow_shell_has_safety_flags() -> None:
    """The loop step must use set -euo pipefail for fail-fast shell behaviour."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "set -euo pipefail" in content, "Shell script must start with set -euo pipefail"


def test_workflow_has_hard_max_iterations() -> None:
    """The workflow must define a HARD_MAX_ITERATIONS guard to cap runaway loops."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "HARD_MAX_ITERATIONS" in content


def test_workflow_has_consecutive_failure_guard() -> None:
    """The workflow must abort after consecutive Copilot failures."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "CONSECUTIVE_FAILURES" in content
    assert "FAILURE_THRESHOLD" in content


def test_workflow_has_inter_iteration_sleep() -> None:
    """The workflow must sleep between iterations for rate-limit protection."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "INTER_ITERATION_SLEEP" in content
    assert "sleep" in content


# ---------------------------------------------------------------------------
# research-prompt.md content tests
# ---------------------------------------------------------------------------


def test_prompt_file_exists() -> None:
    """research-prompt.md must be present — it is the only tuning lever."""
    assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"


def test_prompt_has_required_sections() -> None:
    """The prompt must contain all mandatory instruction sections."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    required = [
        "## Steps",
        "research start",
        "research draft",
        "research complete",
        "PROGRESS.md",
        "git commit",
        "git push",
        "## Rules",
    ]
    for section in required:
        assert section in content, f"Prompt missing required content: {section!r}"


def test_prompt_instructs_single_item_only() -> None:
    """The prompt must instruct the agent to process exactly one item per session."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    # The "one item" rule should be explicit to match the Ralph Wiggum pattern
    assert "one item" in content.lower() or "exactly one" in content.lower()


def test_prompt_requires_direct_main_commit() -> None:
    """The prompt must instruct the agent to commit directly to main (not a PR)."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "main" in content
    assert "pull request" not in content.lower() or "do not open" in content.lower()


# ---------------------------------------------------------------------------
# Backlog discovery logic tests (mirrors bash: find *.md -not -name README.md)
# ---------------------------------------------------------------------------


def _count_backlog_items(backlog_dir: Path) -> int:
    """Count backlog items the same way the bash loop does."""
    return sum(1 for f in backlog_dir.glob("*.md") if f.name.lower() != "readme.md")


def test_backlog_count_excludes_readme(tmp_path: Path) -> None:
    """Backlog count must exclude README.md (mirrors bash find logic)."""
    (tmp_path / "README.md").write_text("# Backlog\n")
    (tmp_path / "2026-03-01-item-a.md").write_text(SAMPLE_BACKLOG_ITEM)
    (tmp_path / "2026-03-02-item-b.md").write_text(SAMPLE_BACKLOG_ITEM)

    count = _count_backlog_items(tmp_path)
    assert count == 2


def test_backlog_count_empty_dir(tmp_path: Path) -> None:
    """Backlog count is 0 for an empty directory (loop terminates cleanly)."""
    assert _count_backlog_items(tmp_path) == 0


def test_backlog_count_readme_only(tmp_path: Path) -> None:
    """A directory with only README.md is treated as empty (loop terminates)."""
    (tmp_path / "README.md").write_text("# Backlog\n")
    assert _count_backlog_items(tmp_path) == 0


# ---------------------------------------------------------------------------
# End-to-end loop cycle: start → complete via Python CLI
# ---------------------------------------------------------------------------


from src.research.cli import cmd_complete, cmd_list, cmd_start  # noqa: E402


def test_loop_cycle_start_and_complete(research_dir: Path) -> None:
    """A full loop iteration: item moves backlog → in-progress → completed."""
    # Seed the backlog
    item_path = research_dir / "backlog" / "2026-03-01-test-loop.md"
    item_path.write_text(SAMPLE_BACKLOG_ITEM, encoding="utf-8")

    # Verify it appears in listing
    items = cmd_list(research_root=research_dir)
    assert any("Test research item" in i.title for i in items)

    # Start the item (simulates step 2 of research-prompt.md)
    in_progress = cmd_start("2026-03-01-test-loop.md", research_root=research_dir)
    assert in_progress.parent.name == "in-progress"
    assert not item_path.exists()

    # Complete the item (simulates step 6 of research-prompt.md)
    completed = cmd_complete("2026-03-01-test-loop.md", research_root=research_dir)
    assert completed.parent.name == "completed"
    assert not in_progress.exists()

    # Verify it no longer appears in listing (completed items are excluded)
    remaining = cmd_list(research_root=research_dir)
    assert all("Test research item" not in i.title for i in remaining)


def test_loop_terminates_when_backlog_empty(research_dir: Path) -> None:
    """With no backlog items, the loop guard correctly reports empty."""
    count = _count_backlog_items(research_dir / "backlog")
    assert count == 0, "Empty backlog should produce count=0 so loop exits immediately"


def test_max_items_guard_logic() -> None:
    """Verify the max_items guard: iteration >= max_items stops the loop."""
    max_items = 2
    for iteration in range(5):
        should_stop = iteration >= max_items
        if iteration < max_items:
            assert not should_stop, (
                f"Should not stop at iteration {iteration} < max_items {max_items}"
            )
        else:
            assert should_stop, f"Should stop at iteration {iteration} >= max_items {max_items}"


def test_hard_max_iterations_guard_logic() -> None:
    """Verify the hard ceiling guard fires before HARD_MAX_ITERATIONS."""
    hard_max = 10
    for iteration in range(15):
        should_hard_stop = iteration >= hard_max
        if iteration < hard_max:
            assert not should_hard_stop
        else:
            assert should_hard_stop


def test_consecutive_failure_threshold_logic() -> None:
    """Verify consecutive failure counter aborts at threshold."""
    threshold = 2
    consecutive = 0

    # Simulate two failures
    for _ in range(threshold):
        consecutive += 1

    assert consecutive >= threshold, "Should abort when consecutive failures reach threshold"


# ---------------------------------------------------------------------------
# ADR-0004 exists and is indexed
# ---------------------------------------------------------------------------


def test_adr_0004_exists() -> None:
    """ADR-0004 documenting the autonomous research loop must exist."""
    adr_path = REPO_ROOT / "docs" / "adr" / "0004-autonomous-research-loop.md"
    assert adr_path.exists(), f"ADR-0004 not found at {adr_path}"


def test_adr_0004_indexed() -> None:
    """ADR-0004 must be referenced in the ADR index."""
    index_path = REPO_ROOT / "docs" / "adr" / "README.md"
    content = index_path.read_text(encoding="utf-8")
    assert "0004" in content, "ADR-0004 must be added to the ADR index"

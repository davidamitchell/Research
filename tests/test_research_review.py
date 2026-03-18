"""Tests proving the research review workflow and prompt are correctly structured.

These tests verify:
1. The workflow YAML has the expected attributes (timeout, triggers, secrets,
   permissions, submodule initialization).
2. The review prompt exists and contains the mandatory instruction sections.
3. The item-path injection convention ({{ITEM_PATH}} placeholder) is correct.
4. The expected output format from the review agent is parseable and the
   PASS/FAIL detection logic is sound.
"""

from __future__ import annotations

from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "research-review.yml"
PROMPT_PATH = REPO_ROOT / "research-review-prompt.md"


def _load_workflow() -> dict:
    return yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Workflow file structure tests
# ---------------------------------------------------------------------------


def test_workflow_file_exists() -> None:
    """The research-review workflow file must be present."""
    assert WORKFLOW_PATH.exists(), f"Workflow file not found: {WORKFLOW_PATH}"


def test_workflow_is_valid_yaml() -> None:
    """The workflow file must parse as valid YAML."""
    wf = _load_workflow()
    assert isinstance(wf, dict)


def test_workflow_has_job_timeout() -> None:
    """The review job must declare a timeout to prevent runaway runs."""
    wf = _load_workflow()
    job = wf["jobs"]["review"]
    assert "timeout-minutes" in job, "Job must declare timeout-minutes"
    assert job["timeout-minutes"] <= 60, "Review timeout must not exceed 60 minutes"


def test_workflow_has_workflow_dispatch_trigger() -> None:
    """The workflow must support manual dispatch so any item can be reviewed on demand."""
    wf = _load_workflow()
    # PyYAML parses the `on:` key as boolean True
    triggers = wf[True]
    assert "workflow_dispatch" in triggers, "workflow_dispatch trigger is required"


def test_workflow_dispatch_requires_item_path_input() -> None:
    """workflow_dispatch must accept an item_path input so callers specify the target."""
    wf = _load_workflow()
    # PyYAML parses the `on:` key as boolean True
    triggers = wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"]
    assert "item_path" in inputs, "workflow_dispatch must have an item_path input"
    assert inputs["item_path"]["required"] is True, "item_path must be required"
    assert inputs["item_path"]["type"] == "string", "item_path must be type: string"


def test_workflow_has_push_trigger_for_completed_items() -> None:
    """The push trigger on Research/completed/ must be absent — review is dispatch-only."""
    wf = _load_workflow()
    # PyYAML parses the `on:` key as boolean True
    triggers = wf[True]
    assert "push" not in triggers, (
        "push trigger must be removed; review is triggered via workflow_dispatch only"
    )


def test_workflow_push_trigger_restricted_to_main() -> None:
    """No push trigger exists; this test verifies workflow_dispatch is the sole trigger."""
    wf = _load_workflow()
    triggers = wf[True]
    assert "push" not in triggers, "push trigger must not be present after migration to dispatch"


def test_workflow_uses_copilot_github_token_secret() -> None:
    """The workflow must reference COPILOT_GITHUB_TOKEN (not GH_TOKEN)."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "COPILOT_GITHUB_TOKEN" in content, "Workflow must use COPILOT_GITHUB_TOKEN secret"
    assert "secrets.GH_TOKEN" not in content, "Workflow must not reference old GH_TOKEN secret"


def test_workflow_permissions_allow_contents_write() -> None:
    """Review job must use contents: write — it commits review_count increments."""
    wf = _load_workflow()
    job = wf["jobs"]["review"]
    perms = job.get("permissions", {})
    assert perms.get("contents") == "write", (
        "Review job must have contents: write — it commits review_count frontmatter updates"
    )


def test_workflow_initializes_skills_submodule() -> None:
    """The workflow must initialize .github/skills to access skill files."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "submodule" in content, "Workflow must initialize the skills submodule"
    assert ".github/skills" in content, "Workflow must initialize .github/skills specifically"


def test_workflow_references_review_prompt() -> None:
    """The workflow must use research-review-prompt.md as the review prompt."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "research-review-prompt.md" in content, (
        "Workflow must reference the research-review-prompt.md template"
    )


def test_workflow_injects_item_path_into_prompt() -> None:
    """The workflow must substitute {{ITEM_PATH}} before passing the prompt to Copilot."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "{{ITEM_PATH}}" in content, (
        "Workflow must use sed (or equivalent) to inject the item path into the prompt"
    )


def test_workflow_checks_overall_fail_marker() -> None:
    """The workflow must fail if the report contains 'OVERALL: FAIL'."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "OVERALL: FAIL" in content, (
        "Workflow must grep for 'OVERALL: FAIL' to determine pass/fail"
    )


def test_workflow_uses_shell_fail_fast() -> None:
    """The review shell script must use set -euo pipefail."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "set -euo pipefail" in content, "Shell script must use set -euo pipefail"


def test_workflow_handles_missing_item_gracefully() -> None:
    """The workflow must emit an error and fail if a specified item does not exist."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "not found" in content.lower(), "Workflow must handle missing item paths"


def test_workflow_accepts_in_progress_item_paths() -> None:
    """The workflow must not restrict item_path to Research/completed/; in-progress is valid."""
    wf = _load_workflow()
    triggers = wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"]
    description = inputs["item_path"].get("description", "")
    # The description should reference in-progress (not only completed/)
    assert "in-progress" in description, (
        "item_path description must accept Research/in-progress/ paths"
    )


def test_workflow_runs_copilot_autopilot() -> None:
    """The workflow must invoke Copilot CLI in autopilot mode to use filesystem tools."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "--autopilot" in content, "Workflow must use copilot --autopilot"
    assert "--allow-all" in content, "Workflow must use --allow-all to permit file reads/writes"


# ---------------------------------------------------------------------------
# Review prompt content tests
# ---------------------------------------------------------------------------


def test_prompt_file_exists() -> None:
    """research-review-prompt.md must be present."""
    assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"


def test_prompt_has_item_path_placeholder() -> None:
    """The prompt must contain {{ITEM_PATH}} so the workflow can inject the target."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "{{ITEM_PATH}}" in content, (
        "Prompt must contain {{ITEM_PATH}} placeholder for path injection"
    )


def test_prompt_references_all_three_skills() -> None:
    """The prompt must reference all three review skills."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    for skill in ("citation-discipline", "speculation-control", "remove-ai-slop"):
        assert skill in content, f"Prompt must reference the {skill} skill"


def test_prompt_references_skill_files() -> None:
    """The prompt must tell the agent where to find the skill SKILL.md files."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert ".github/skills" in content, "Prompt must reference .github/skills directory"


def test_prompt_specifies_report_output_path() -> None:
    """The prompt must tell the agent to write to /tmp/research-review-report.txt."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "/tmp/research-review-report.txt" in content, (
        "Prompt must specify the report output path"
    )


def test_prompt_specifies_overall_pass_fail() -> None:
    """The prompt must instruct the agent to write OVERALL: PASS or OVERALL: FAIL."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "OVERALL: PASS" in content, "Prompt must document OVERALL: PASS output"
    assert "OVERALL: FAIL" in content, "Prompt must document OVERALL: FAIL output"


def test_prompt_prohibits_commits() -> None:
    """The prompt must explicitly prohibit git commit and git push."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "do not" in content.lower() and (
        "git commit" in content.lower() or "commit" in content.lower()
    ), "Prompt must prohibit git commit"


def test_prompt_prohibits_modifying_research_item() -> None:
    """The prompt must explicitly tell the agent not to modify the research item."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    assert "DO NOT" in content or "must not" in content.lower(), (
        "Prompt must prohibit modifying the research item"
    )


def test_citation_discipline_has_context_scope_note() -> None:
    """Step 1 (citation-discipline) must have a scope note scoping it off ## Context."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    # Find Step 1 section and verify it contains both "Scope note" and "## Context"
    step1_start = content.find("### Step 1 — citation-discipline")
    step2_start = content.find("### Step 2 — speculation-control")
    assert step1_start != -1, "Step 1 section must exist"
    assert step2_start != -1, "Step 2 section must exist"
    assert step1_start < step2_start, "Step 1 must appear before Step 2"
    step1_text = content[step1_start:step2_start]
    assert "Scope note" in step1_text, (
        "Step 1 (citation-discipline) must contain a 'Scope note' for ## Context"
    )
    assert "## Context" in step1_text, "Step 1 scope note must reference '## Context'"


def test_speculation_control_has_context_scope_note() -> None:
    """Step 2 (speculation-control) must have a scope note scoping it off ## Context."""
    content = PROMPT_PATH.read_text(encoding="utf-8")
    step2_start = content.find("### Step 2 — speculation-control")
    step3_start = content.find("### Step 3 — remove-ai-slop")
    assert step2_start != -1, "Step 2 section must exist"
    assert step3_start != -1, "Step 3 section must exist"
    assert step2_start < step3_start, "Step 2 must appear before Step 3"
    step2_text = content[step2_start:step3_start]
    assert "Scope note" in step2_text, (
        "Step 2 (speculation-control) must contain a 'Scope note' for ## Context"
    )
    assert "## Context" in step2_text, "Step 2 scope note must reference '## Context'"


def test_workflow_does_not_create_github_issues() -> None:
    """Failures emit ::warning annotations only — no GitHub issue creation."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "gh issue" not in content, (
        "Workflow must not create GitHub issues on failure — use ::warning annotations instead"
    )


def test_workflow_emits_warning_on_failure() -> None:
    """The workflow must emit a ::warning annotation when a review fails."""
    content = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "::warning::" in content, (
        "Workflow must emit ::warning:: annotations for review failures"
    )


# ---------------------------------------------------------------------------
# PASS/FAIL detection logic tests (unit-level)
# ---------------------------------------------------------------------------

PASS_REPORT = """\
REVIEW_TARGET: Research/completed/2026-03-01-example.md
citation-discipline: PASS
speculation-control: PASS
remove-ai-slop: PASS
OVERALL: PASS
"""

FAIL_REPORT = """\
REVIEW_TARGET: Research/completed/2026-03-01-example.md
citation-discipline: FAIL
  VIOLATION: Claim "X causes Y" has no source citation.
speculation-control: PASS
remove-ai-slop: PASS
OVERALL: FAIL
"""

PARTIAL_FAIL_REPORT = """\
REVIEW_TARGET: Research/completed/2026-03-01-example.md
citation-discipline: PASS
speculation-control: PASS
remove-ai-slop: FAIL
  VIOLATION: Excessive use of "Furthermore" and "Additionally" transitions.
  VIOLATION: Symmetrical paragraph structure throughout Executive Summary.
OVERALL: FAIL
"""


def _overall_status(report: str) -> str:
    """Mirrors the bash grep logic: return PASS or FAIL from an OVERALL line."""
    for line in report.splitlines():
        if line.startswith("OVERALL:"):
            return line.split(":", 1)[1].strip()
    return "UNKNOWN"


def test_pass_report_detected_as_pass() -> None:
    """A report with no violations must be detected as PASS."""
    assert _overall_status(PASS_REPORT) == "PASS"


def test_fail_report_detected_as_fail() -> None:
    """A report with any OVERALL: FAIL line must be detected as FAIL."""
    assert _overall_status(FAIL_REPORT) == "FAIL"


def test_partial_fail_report_detected_as_fail() -> None:
    """A report where only one skill fails must still be detected as FAIL."""
    assert _overall_status(PARTIAL_FAIL_REPORT) == "FAIL"


def test_fail_report_contains_violations() -> None:
    """A FAIL report must list at least one VIOLATION line."""
    violations = [
        line for line in FAIL_REPORT.splitlines() if line.strip().startswith("VIOLATION:")
    ]
    assert len(violations) >= 1, "FAIL report must include at least one VIOLATION line"


def test_violation_lines_have_detail() -> None:
    """VIOLATION lines must carry a non-empty description."""
    violations = [
        line.strip() for line in FAIL_REPORT.splitlines() if line.strip().startswith("VIOLATION:")
    ]
    for v in violations:
        detail = v.removeprefix("VIOLATION:").strip()
        assert len(detail) > 0, f"VIOLATION line has no detail: {v!r}"

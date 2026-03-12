# 2026-03-12 - Evaluate instructions and feedback for continuous improvement

## Task

Evaluate the repository instructions against recent commits, PRs, and owner feedback. Suggest
and implement improvements specifically related to continuous self-improvement.

Owner feedback after initial evaluation: "do a proper full evaluation looking for correctness,
factualness and better improvements. Don't just take a punt do some searching and see what you
can find out."

---

## Research conducted (second pass)

Searched for and read:
- Anthropic "Building Effective Agents" (anthropic.com/research/building-effective-agents):
  keep instruction files short; start simple; only add complexity when justified.
- GitHub Copilot instruction file best practices (dev.to, georg.dev, docs.github.com):
  files exceeding a few thousand tokens cause "lost in the middle" effect -- instructions in
  the middle of the file are systematically de-prioritized. Recommendation: keep under a few
  hundred lines; use targeted prompt files for specific workflows.
- Agent instruction anti-patterns (elements.cloud, datagrid.com):
  "over-specification" and "config file prompts" cause degraded instruction-following.
  Verbosity and redundancy confuse the model; conflicting rules produce inconsistent output.
- Agent evaluation best practices (Anthropic, AWS, Microsoft):
  quality gates must be BLOCKING (not async/advisory) to prevent non-compliant outputs from
  propagating downstream. Evaluation-driven development shifts gates left.
- Open GitHub issues #77-107: confirmed 19+ research review failures, all items in
  Research/completed/, all for the same three violation classes. Proves items are completing
  before reviews pass.

---

## Findings

### What is working

1. Non-Negotiable Constraints: explicit, named, enforced. Submodule read-only constraint added
   proactively after second violation.
2. Session logs: created consistently.
3. CHANGELOG.md: being maintained; ADR triggers are clear.
4. learnings.md: substantive cross-cutting synthesis with six evidence-backed threads.
5. Safety controls in research-loop.yml: timeout, item cap, failure threshold, sleep -- well-designed.

### What is broken: specific findings with evidence

#### Finding 1 (factual): Research/_template.md missing reviewing status

`status: backlog  # backlog | in-progress | completed` -- reviewing was added as a valid status
in PR #104 but the template comment was never updated. Agents creating a new item from the
template see an incomplete/incorrect status list.

Fix: Added `reviewing` to the status comment on line 4 of _template.md.

#### Finding 2 (factual): Draft commit message uses filename not slug

research-prompt.md Step 8 had `git commit -m "research: draft - <filename>"` while Step 13
uses `<slug>` (the date-and-slug portion, e.g. ai-strategy-swe-focus). The commit message
convention was inconsistent across the same file.

Fix: Updated Step 8 to derive SLUG via `basename <filename> .md` and use `${SLUG}` in the
commit message, matching the Step 13 convention.

#### Finding 3 (factual): Stale section reference in copilot-instructions.md

Line 176 referenced "research-prompt.md section 4" using the prefix character from SKILL.md
section numbering. research-prompt.md uses numbered steps (1-13), not numbered sections.
The reference was factually wrong.

Fix: Updated to "Steps 3-7 of research-prompt.md".

#### Finding 4 (architectural): Review is fire-and-forget, not a blocking gate

Evidence: All 19+ items with open review failures (#81-106) are in Research/completed/ -- they
were completed BEFORE their reviews passed. This is observable in the repository state.

Root cause: research-prompt.md Step 8 fired `gh workflow run research-review.yml` (async) with
no wait mechanism. The agent could not wait for the external workflow to finish within its own
session, so it proceeded directly to Step 10 (complete). The review workflow ran after the
session ended and created issues that no one was watching.

Fix: Added three commands to Step 8: `sleep 20` (wait for run to register), `gh run list` (get
the run ID), `gh run watch "$RUN_ID"` (wait for completion). Step 9 now uses `gh issue list`
to check for a failure issue programmatically, rather than asking the agent to "check GitHub"
manually. The review is now a genuine blocking gate.

#### Finding 5 (process): Review issues never closed

When an item passes review (first attempt or after fixing violations), the previously opened
research-review GitHub issue is never closed. 19+ issues have accumulated. The owner has no
clear picture of what still needs attention vs. what is resolved.

Fix: Added `gh issue close` to Step 9 (PASS path) and to the "Completing Research" section in
copilot-instructions.md.

#### Finding 6 (factual): Research loop description is inaccurate

copilot-instructions.md line 392 said "Copilot... commits the completed item". The actual
design (as documented in research-prompt.md) is: draft -> wait for review -> complete. The
description implied no review gate existed, which was misleading.

Fix: Updated the description to "marks it as a draft, triggers the quality review workflow
(and waits for it), then completes the item."

#### Finding 7 (structural): copilot-instructions.md at ~6,600 tokens triggers lost-in-the-middle

The file is 575 lines / ~6,600 tokens. Published research on GitHub Copilot instruction files
confirms that files of this size cause the "lost in the middle" effect: the model de-prioritizes
instructions in the middle of the file. The Continuous Improvement section (lines 465-590,
containing the Mini-Retro requirement and the acronym expansion rule) sits exactly in the
middle/end of the file -- the most vulnerable position.

This explains the persistent acronym failures and missing mini-retros despite both rules being
explicitly documented.

Fix: Added a 5-item "Quick Reference" block at the very TOP of copilot-instructions.md (before
Project Overview). Even if the agent reads only the first screen, it now sees the Mini-Retro
requirement, the acronym rule, and the submodule constraint.

---

## All changes made

### Commit 1 (initial pass)

- research-prompt.md Step 6: inline acronym expansion audit (13-entry table, self-contained,
  no submodule dependency)
- research-prompt.md Step 11 (new): update learnings.md after completing an item
- research-prompt.md Step 12 (was 11): mini-retro format added to session log template
- research-prompt.md Step 13 (was 12): renumbered commit step
- copilot-instructions.md Completing Research: learnings.md update as step 5
- copilot-instructions.md Known Recurring Failure Patterns: new table under Improvement Comes
  in Classes

### Commit 2 (full evaluation)

- Research/_template.md: add reviewing to status comment (factual fix)
- research-prompt.md Step 8: fix commit message format + add review polling commands
  (factual fix + architectural fix)
- research-prompt.md Step 9: command-based outcome check + gh issue close (process fix)
- copilot-instructions.md: Quick Reference block at top (structural fix)
- copilot-instructions.md: fix stale section reference (factual fix)
- copilot-instructions.md: fix research loop description (factual fix)
- copilot-instructions.md: add close-review-issue to Completing Research (process fix)
- progress/2026-03-12-evaluate-instructions-feedback.md: this file, expanded with full findings

---

## Mini-Retro

1. Did the process work? Yes. The second pass -- searching for published best practices, then
   using them to audit specific claims in the instructions against the actual file contents and
   observable repository state (open issues, completed items) -- found issues the first pass
   missed entirely. The standard for "proper evaluation" is: external reference + internal audit
   + evidence from running system.

2. What slowed down or went wrong? The first evaluation was self-referential: it assessed the
   system by inspecting itself rather than comparing it to external standards. "Check if the
   retro is being written" is not the same as "ask whether the retro mechanism is correctly
   designed." The owner's feedback was correct to push for more.

3. What single change would prevent this next time? The evaluation protocol should be
   codified in the instructions: when evaluating the system, always (1) search for published
   best practices on the relevant topic, (2) audit factual claims in the instructions against
   actual file contents and workflow behavior, (3) use open issues and repository state as
   evidence of what is not working.

4. Is this a pattern? Yes -- "surface evaluation vs. deep evaluation." This is a new recurring
   pattern worth adding to the Known Recurring Patterns table: when asked to evaluate or review
   the system, the agent defaults to self-inspection rather than external benchmarking. The fix
   is the evaluation protocol above.

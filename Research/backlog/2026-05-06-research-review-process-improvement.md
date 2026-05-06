---
title: "What specific, actionable changes to `research-review-prompt.md` and the automated review workflow would most improve reliability, consistency, and catch rate?"
added: 2026-05-06T09:03:23+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [research-quality, evaluation, llm, governance, fact-checking]
started: ~
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-openfactcheck-automated-fact-verification, 2026-05-06-factscore-atomic-claim-precision-scoring, 2026-05-06-loki-fact-checking-journalists-ai-content, 2026-05-06-open-weight-policy-enforcement-research-review, 2026-05-06-barnum-statements-ai-response-detection-removal]
related: [2026-05-02-adversarial-review-methods-ai-research-quality, 2026-03-02-research-quality-assurance-methodology]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: synthesis # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What specific, actionable changes to `research-review-prompt.md` and the automated review workflow would most improve reliability, consistency, and catch rate?

## Research Question

The automated research review pipeline (`research-review-prompt.md`) applies four checks to completed research items using a general-purpose LLM (Large Language Model) judge operating zero-shot. Known limitations include: non-deterministic verdicts, no live evidence retrieval, a binary PASS/FAIL output that obscures partial compliance, and a `remove-ai-slop` check that does not explicitly target Barnum statements. Drawing on the five companion items (OpenFactCheck, FActScore, Loki, gpt-oss-safeguard, and Barnum statements), what is the minimum set of concrete, implementable changes to `research-review-prompt.md` that would deliver the highest-impact improvement in review reliability and catch rate?

## Scope

**In scope:**
- Synthesising the improvement candidates surfaced by the five companion backlog items into a prioritised, implementable change list
- The four existing check dimensions in `research-review-prompt.md` (citation-discipline, speculation-control, remove-AI-slop, peer-reviewer) and their known failure modes
- Candidate improvements: quantitative scoring (FActScore), live evidence retrieval (OpenFactCheck, Loki), policy-conditioned reasoning (gpt-oss-safeguard), Barnum statement criteria (Barnum item)
- Trade-off analysis: automation depth vs. inference cost vs. GitHub Actions feasibility
- A recommended minimal viable change set: what can be done to `research-review-prompt.md` today without new infrastructure, and what requires tooling investment

**Out of scope:**
- Conducting the underlying tool research (delegated to the five cites items above)
- Changing the research item template format (separate concern)
- Review process changes outside `research-review-prompt.md` (e.g. research-loop workflow scheduling)

**Constraints:**
- Findings must be synthesised from the completed cites items, not independently researched
- Recommended changes must be testable: each change should have a falsifiable success criterion
- Self-hosting feasibility must be assessed against GitHub Actions runner specifications (16 GB RAM baseline)
- This item should not start until all five cites items are completed

## Context

The research review pipeline is the primary quality gate for research items published from this repository. It currently runs as a GitHub Actions workflow, invoking a general-purpose LLM with `research-review-prompt.md` as a zero-shot instruction. The five preceding backlog items investigate specific tooling and conceptual advances (atomic claim scoring, evidence retrieval, policy enforcement, Barnum statement detection) that each address a known weakness of the current approach. This synthesis item converts those findings into a ranked improvement roadmap: what to change now, what to prototype, and what to defer.

## Approach

1. **Failure mode audit:** Enumerate the known failure modes of the current `research-review-prompt.md` pipeline. For each: how often does it occur, what is the impact, and which cites item addresses it?

2. **Improvement candidate inventory:** For each of the five cites items, extract the single highest-impact change that could be applied to `research-review-prompt.md` or the review workflow.

3. **Feasibility ranking:** Score each candidate on three axes: (a) implementation effort (hours), (b) self-hosting feasibility within GitHub Actions limits, (c) estimated improvement in catch rate. Produce a priority-ordered list.

4. **Minimal viable change set:** Identify the subset of changes that can be applied to `research-review-prompt.md` as prompt edits (no new tooling required) versus those that require additional infrastructure.

5. **Prototype specification:** For the top-ranked infrastructure-requiring change, write a concrete specification: what the new workflow step does, what tool it calls, how it integrates with the existing PASS/FAIL report format, and how success would be measured.

6. **Recommended next actions:** Produce a ranked backlog of concrete tasks, each linked to a success criterion, for improving the review pipeline.

## Sources

- [ ] `research-review-prompt.md` — the current review prompt; source of truth for existing checks and failure modes
- [ ] `2026-05-06-openfactcheck-automated-fact-verification.md` (completed) — OpenFactCheck gap analysis and integration feasibility
- [ ] `2026-05-06-factscore-atomic-claim-precision-scoring.md` (completed) — FActScore alignment with citation-discipline and scoring thresholds
- [ ] `2026-05-06-loki-fact-checking-journalists-ai-content.md` (completed) — Loki explainability and evidence traceability findings
- [ ] `2026-05-06-open-weight-policy-enforcement-research-review.md` (completed) — gpt-oss-safeguard policy mapping and self-hosting feasibility
- [ ] `2026-05-06-barnum-statements-ai-response-detection-removal.md` (completed) — Barnum detection criteria for `remove-ai-slop`

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description: A prioritised, implementable change list for `research-review-prompt.md`
- Links:

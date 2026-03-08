---
title: "Inbox folder pattern: frictionless capture without forced structure"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [capture, ux, memory-system, triage, agent-automation]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Inbox folder pattern: frictionless capture without forced structure

## Research Question

Does removing the folder-selection decision from the capture path meaningfully reduce friction? Design and evaluate an `inbox/` folder pattern where: (a) any capture tool writes unstructured notes to `inbox/` with no required metadata, (b) a periodic agent task reads the inbox and classifies each item into `meetings/`, `journal/`, or `projects/` with proper front-matter. What is the minimum viable agent prompt for triage? Can the existing `research-loop.yml` pattern be adapted?

## Scope

**In scope:**
- Inbox pattern design: what metadata (if any) is required at capture time vs triage time
- Front-matter requirements for inbox files vs classified files
- Agent triage prompt design: classification rules, folder mapping, front-matter generation
- GitHub Actions workflow for automated triage (adapting `research-loop.yml` pattern from this repo)
- Failure modes: misclassification, ambiguous items, items that don't fit existing folders
- UX comparison: current `add_memory` with required `folder` parameter vs inbox-first capture

**Out of scope:**
- The capture tool itself (separate items: `2026-03-08-ios-shortcuts-github-api-memory-capture.md`, `2026-03-08-telegram-bot-memory-capture-retrieval.md`, CLI)
- Retrieval from the inbox before triage (acceptable latency: triage runs periodically)
- Changing the folder structure of the Memory-System (that is an ADR for the Memory-System repo)

**Constraints:** The triage workflow must be fully autonomous — no human review step required. Misclassifications must be recoverable (files can be manually moved; git history preserved).

## Context

The current `add_memory` MCP tool requires a `folder` parameter. Forcing a decision at capture time is friction — especially on mobile where context-switching is costly and the "right folder" may not be obvious when capturing a fleeting thought. The inbox pattern is well-established in PKM (Getting Things Done, Andy Matuschak's Evergreen Notes): capture everything first, classify later.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` cites Matuschak's Evergreen Notes as a reference architecture for memory systems and notes that capture friction is a primary reason memory systems fail in practice. The `research-loop.yml` workflow in this repo provides an existing autonomous agent loop pattern (GitHub Actions + Copilot CLI + commit to main) that could be adapted directly for inbox triage without building new infrastructure.

## Related

**Memory-System backlog:** [W-0012 — Inbox folder pattern: frictionless capture without forced structure](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Review the Getting Things Done inbox pattern and Andy Matuschak's capture-then-link approach — map to the Memory-System context
2. Define the minimum front-matter for inbox files: timestamp + raw content is sufficient; no folder required
3. Design the agent triage prompt: given an inbox file, classify into `meetings/`, `journal/`, or `projects/`, generate front-matter, output the move operation
4. Review `research-loop.yml` in this repo: identify which steps can be reused for inbox triage (checkout, agent invocation, commit, push)
5. Prototype a GitHub Actions workflow for triage: schedule (e.g. every 6 hours), process all files in `inbox/`, commit classified files, delete processed inbox entries
6. Define failure modes and recovery: misclassified files (git history + manual move), empty inbox (no-op), ambiguous items (leave in inbox with a `?-` prefix)
7. Evaluate: does removing the folder decision at capture time measurably reduce the friction of mobile capture?

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — capture friction as a primary memory system failure mode; Evergreen Notes reference architecture
- [ ] `Research/completed/2026-03-02-integrative-framework-agent-decision-making.md` — procedural memory as encoded judgement from past experience (relevant to triage agent design)
- [ ] Andy Matuschak's Evergreen Notes: https://notes.andymatuschak.org/Evergreen_notes
- [ ] Getting Things Done (GTD) inbox processing: https://gettingthingsdone.com/
- [ ] `.github/workflows/research-loop.yml` in this repo — autonomous agent loop pattern to adapt for triage
- [ ] GitHub Actions schedule trigger docs: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule
- [ ] `2026-03-08-ios-shortcuts-github-api-memory-capture.md` — capture tool that would write to inbox
- [ ] `2026-03-08-telegram-bot-memory-capture-retrieval.md` — capture tool that would write to inbox
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0012 — the corresponding discovery item that this research informs

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

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

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

- Type: knowledge, backlog-item
- Description:
- Links:

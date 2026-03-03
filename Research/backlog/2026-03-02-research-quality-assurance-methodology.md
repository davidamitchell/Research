---
title: "Research Quality Assurance and Knowledge Integration Methodology"
added: 2026-03-02
status: backlog
priority: medium
tags: [research-methodology, quality-assurance, peer-review, knowledge-integration, information-to-wisdom, ci, skills]
started: ~
completed: ~
output: [skill, knowledge, backlog-item]
---

# Research Quality Assurance and Knowledge Integration Methodology

## Research Question

What review methodology is required to reliably move from information gathering through to applied knowledge and wisdom — and which of those steps can be automated in a CI pipeline versus requiring human or peer-level judgement?

## Scope

**In scope:**
- Current skills inventory and gap analysis: citation-discipline, speculation-control, remove-ai-slop — what each checks, what each misses
- Peer review as a distinct quality dimension: what a peer reviewer catches that automated checks cannot (logical coherence, missing context, alternative interpretations, applicability)
- Integration skill: synthesising findings from multiple completed research items into a coherent body of knowledge rather than treating each item in isolation
- The information → knowledge → wisdom pipeline: how raw sourced information becomes internalised knowledge, and how knowledge becomes applicable wisdom (decision-relevant, context-adapted, actionable)
- Applicability testing: how to verify that a research finding is usable in a specific context, not just true in the abstract
- Which review steps are automatable via a CI pipeline (static analysis of structure, citation presence, speculation markers, slop patterns) versus which require agent-level reasoning or human review
- Ordering and composition of review steps: can automated checks gate the pipeline before expensive reasoning-based checks?

**Out of scope:**
- Research item filing mechanics (covered by existing CLI tooling)
- Content of any specific research item (this is methodology, not object-level research)
- General epistemology or philosophy of science beyond what is directly applicable to a practical review pipeline

**Constraints:** Focus on what is implementable using GitHub Actions, existing agent skills, and MCP tools already available in this repo. Do not propose infrastructure that requires new credentials or services without flagging as a follow-up.

## Context

This repo uses a set of agent skills to review research quality: `citation-discipline` (are claims sourced?), `speculation-control` (are uncertain claims flagged?), and `remove-ai-slop` (is the writing direct and precise?). These cover factual hygiene and writing quality.

What they do not cover:
- **Peer review**: whether the reasoning holds, whether alternative explanations were considered, whether the conclusions follow from the evidence
- **Integration**: whether findings from this item connect to, extend, or contradict findings from related completed items
- **Applicability**: whether the knowledge can actually be applied in the specific contexts relevant to this repo's owner (NZ financial services, SWE, agentic AI)
- **Wisdom**: whether the accumulated body of completed research items is forming coherent, decision-relevant understanding — or just accumulating facts

There is a related repo improvement item (BACKLOG.md W-0031) to implement a research review CI step. That item is blocked until this research is complete: the CI design depends on knowing which checks are automatable and in what order.

## Approach

1. **Skills gap analysis** — Document precisely what each existing skill checks, what format/structure it expects, and what quality dimensions it leaves uncovered. Identify the specific failure modes that citation-discipline, speculation-control, and remove-ai-slop do not catch.
2. **Peer review patterns** — Survey how peer review is structured in academic, open-source, and knowledge-management contexts. Identify which peer review behaviours are replicable by an LLM agent with access to the completed item and its sources, and which require a second independent expert.
3. **Integration methodology** — How do knowledge management systems (Zettelkasten, Roam, Obsidian workflows, Notion AI) handle cross-item synthesis? Which techniques transfer to a file-based Markdown research corpus?
4. **Information → knowledge → wisdom frameworks** — Review Ackoff's DIKW hierarchy, Nonaka's SECI model, and pragmatic alternatives. Assess which frameworks translate into testable, checkable steps rather than vague aspirational stages.
5. **Applicability testing** — What does it mean to test whether a finding is applicable? Survey methods: scenario-based testing, counterfactual checking, decision-forcing cases. Which are automatable?
6. **CI pipeline design** — Map each review dimension to: (a) fully automatable (rule/structure-based), (b) agent-automatable (requires LLM reasoning), (c) human-only. Sequence them by cost and gate logic. This is the direct input to BACKLOG.md W-0031.
7. **New skills needed** — Identify whether a `peer-review` skill and/or an `integration` skill should be added to `davidamitchell/Skills`, and draft their scope.

## Sources

- [ ] Ackoff (1989) — "From Data to Wisdom": https://doi.org/10.1111/j.1467-9310.1989.tb00072.x — foundational DIKW hierarchy
- [ ] Nonaka & Takeuchi (1995) — *The Knowledge-Creating Company* — SECI model (socialisation, externalisation, combination, internalisation)
- [ ] Bloom's Taxonomy (1956, revised 2001) — cognitive levels as a framework for knowledge depth vs applicability
- [ ] Zettelkasten method — https://zettelkasten.de/introduction/ — atomic notes, linking, emergence of insight through connection
- [ ] Ahrens (2017) — *How to Take Smart Notes* — practical Zettelkasten for researchers; integration as a first-class practice
- [ ] GitHub Actions documentation — composite actions, reusable workflows — for CI pipeline design
- [ ] Existing skills: `.github/skills/citation-discipline/SKILL.md`, `.github/skills/speculation-control/SKILL.md`, `.github/skills/remove-ai-slop/SKILL.md` — gap analysis starting point
- [ ] Academic peer review process documentation (e.g. Nature's peer review guidelines) — what reviewers are asked to check
- [ ] "Wisdom engineering" or "applied epistemology" — search arXiv and Google Scholar for operational definitions of wisdom in AI/knowledge systems
- [ ] McKinsey / HBR literature on "insight to action" gaps in knowledge management

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: skill, knowledge, backlog-item
- Description:
- Links:

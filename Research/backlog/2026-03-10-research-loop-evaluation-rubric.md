---
title: "Research loop evaluation rubric: LLM-as-judge specification for this repository's research loop agent"
added: 2026-03-10
status: backlog
priority: high
blocks: []
tags: [agents, evaluation, rubric, research-loop, llm-as-judge, regression, quality-gate, ci]
started: ~
completed: ~
output: [knowledge, artefact]
---

# Research loop evaluation rubric: LLM-as-judge specification for this repository's research loop agent

## Research Question

What structured rubric should be used to evaluate the outputs of this repository's research loop agent — and what does a minimal viable implementation of a CI-integrated eval gate for that rubric look like? The rubric must be specific enough to produce reproducible LLM-as-judge scores, version-controlled alongside the agent prompt, and executable in CI without prohibitive cost.

## Scope

**In scope:**
- Specification of evaluation dimensions for a completed research item (§2 evidence quality, §6 synthesis completeness, claim sourcing, executive summary quality, Key Finding structure, Evidence Map coverage)
- Rubric formalisation: each dimension as a scored criterion with explicit scoring guidance (not open-ended prompts)
- Trajectory evaluation: did the agent follow the research protocol (consult required sources, apply taxonomy vocabulary, write all §0–§7 sections)?
- Gold dataset design: what constitutes a known-good research item for regression baseline?
- CI integration: how to run the rubric evaluation on every commit to main that modifies Research/completed/? What cost threshold is acceptable?
- Tooling selection: which of DeepEval, Pydantic Evals, agentevals, or custom implementation best fits this repository's constraints?

**Out of scope:**
- Building a full automated cross-repo analysis pipeline
- Evaluating non-research-loop agent implementations
- Safety evaluation (OWASP LLM Top 10 integration) — this is a separate concern

**Constraints:** Must run in GitHub Actions using available credentials (GITHUB_TOKEN, COPILOT_GITHUB_TOKEN). No new external services without owner approval. Evaluation must complete within 5 minutes per research item to be practical in CI.

## Context

The agent evaluation framework research (`2026-03-10-agent-evaluation-cross-repo-analysis.md`) established that a minimal viable evaluation framework requires five components: a versioned scenario registry, a two-layer metric stack (code-based + LLM-as-judge), trace capture, a CI regression gate, and a gold dataset refresh protocol. This item specifies what those components look like for the specific case of this repository's research loop agent.

The research loop agent currently has no automated quality gate. There is no way to know from a CI signal whether the agent's output meets the expected standard. This item closes that gap by producing a rubric and a CI workflow design.

## Approach

1. **Define evaluation dimensions**: Map the research item format (§0–§7, Findings, Evidence Map) to a set of measurable quality criteria
2. **Write rubric for each dimension**: For each criterion, define 1–5 scoring levels with explicit, unambiguous descriptions
3. **Specify gold dataset requirements**: What properties must a "known-good" research item have to serve as a regression baseline?
4. **Design CI workflow**: Trigger, model selection, cost estimate, threshold configuration, pass/fail reporting
5. **Select tooling**: Evaluate Pydantic Evals vs DeepEval vs custom for this use case; recommend one
6. **Produce artefacts**: (a) rubric document as a versioned file in this repo; (b) CI workflow YAML specification (not implementation — a separate task)

## Sources

- [ ] `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` — the framework that motivates this item
- [ ] Pydantic Evals documentation: https://ai.pydantic.dev/evals/
- [ ] DeepEval agent evaluation guide: https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide
- [ ] Hamel Husain evals guide: https://hamel.dev/blog/posts/evals/
- [ ] langchain-ai/agentevals: https://github.com/langchain-ai/agentevals
- [ ] Anthropic "Writing effective tools for AI agents": https://www.anthropic.com/engineering/writing-tools-for-agents

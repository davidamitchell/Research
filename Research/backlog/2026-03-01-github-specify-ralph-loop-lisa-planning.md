---
title: "GitHub Specify, Ralph Loops, and Lisa Planning: Proof-Driven Development with AI Agents"
added: 2026-03-01
status: backlog
priority: high
tags: [proof-driven-development, ai-agents, ralph-loop, lisa-planning, specify, autonomous-development, github-copilot, software-engineering]
started: ~
completed: ~
output: [knowledge]
---

# GitHub Specify, Ralph Loops, and Lisa Planning: Proof-Driven Development with AI Agents

## Research Question

What is "Specify" in the context of GitHub-integrated AI development workflows, how does the Ralph loop implement proof-driven development in practice, and what role does Lisa planning play in the specification-to-implementation pipeline?

## Scope

**In scope:**
- GitHub's "Specify" concept — what it means, how it is expressed (Markdown specs, acceptance criteria, formal requirements), and what tooling supports it
- The Ralph Wiggum Technique — the autonomous AI coding loop, its phases, termination conditions, and GitHub integration
- Lisa planning — the planning subagent pattern, what a Lisa planning pass produces, and how it differs from a Ralph implementation pass
- Proof-driven development as applied in this context — what constitutes a "proof" (tests, formal assertions, acceptance criteria, behavioural specs) and how it guides the loop
- Concrete implementations and repos: ghuntley/how-to-ralph-wiggum, ClaytonFarr/ralph-playbook, frankbria/ralph-claude-code
- Comparison of Ralph/Lisa to other structured AI coding workflows (e.g. TDD-first agents, spec-first Copilot)

**Out of scope:**
- Formal verification / theorem provers (Coq, Lean, Isabelle) unless directly referenced in the Ralph/Lisa context
- General CI/CD automation not tied to the specification-loop pattern
- Unrelated products named "Specify" (e.g. design-token tooling)

**Constraints:** Focus on documented, practitioner-tested workflows. Prioritise primary sources (repos, blog posts, talks by originators) over secondary summaries.

## Context

The Ralph Wiggum Technique has emerged as an approach to autonomous AI-assisted software development that explicitly couples specification writing to implementation. The pattern has three phases: (1) a **Specify** phase — precise, testable requirements written upfront as the "proof" the agent must satisfy; (2) a **Lisa** planning pass — a planning agent decomposes the spec into an ordered implementation plan; and (3) a **Ralph** implementation loop — an agent iterates through the plan, commits working code, and halts only when all proof criteria are met.

This mirrors proof-driven development: code is correct by construction when it demonstrably satisfies the spec. The loop cannot proceed indefinitely because the termination condition is proof completion, not elapsed time or iteration count.

Understanding how Specify, Ralph, and Lisa map to GitHub tooling (Copilot Agent mode, issues, PRs, Actions) matters for designing repeatable, auditable AI development workflows in this repository and for evaluating whether the approach can be applied to the research tooling in `src/`.

The proof-driven development connection also links to active inference and free energy minimisation (see `2026-02-28-free-energy-entropy-and-life.md`): an agent that minimises surprise by satisfying a prior specification is structurally similar to an agent minimising free energy against a generative model. This cross-domain connection is worth exploring.

## Approach

1. **Characterise Specify** — what format does a Specify document take? What level of granularity is required? How does it differ from a user story, an issue, or a test case? Find examples from the primary repos.
2. **Map the Ralph loop** — trace a complete Ralph cycle: spec in → plan → implement → verify → commit. Identify where GitHub tooling (Actions, PRs, Copilot Agent) is used at each step and what the exit condition looks like in practice.
3. **Understand Lisa planning** — what does a Lisa planning agent produce? How is the output structured? Is Lisa a separate model/agent or a mode of the same agent? Find documented examples.
4. **Locate the proof-driven development framing** — how do originators define "proof" in this context? Is it automated tests, static assertions, human review, or a combination? What counts as proof completion?
5. **Cross-reference with GitHub Copilot Agent mode** — does GitHub's official Agent mode documentation reference or align with this pattern? Is there a formal GitHub-endorsed "Specify" workflow?
6. **Assess applicability** — can this workflow be applied to the `src/` tooling in this repository? What would a Specify document look like for a new fetcher or a CLI command?

## Sources

- [ ] https://github.com/ghuntley/how-to-ralph-wiggum — Geoffrey Huntley's original Ralph Wiggum Technique repository and documentation
- [ ] https://github.com/ClaytonFarr/ralph-playbook — community-curated comprehensive Ralph playbook
- [ ] https://github.com/frankbria/ralph-claude-code — Claude Code implementation of the Ralph autonomous development loop
- [ ] Geoffrey Huntley blog posts and talks on proof-driven development and the Ralph methodology
- [ ] GitHub Copilot Agent mode documentation — official GitHub docs on autonomous agent workflows
- [ ] GitHub blog posts on Copilot Workspace and specification-first development (2024–2025)
- [ ] Any primary sources on Lisa as a planning agent pattern (search Geoffrey Huntley's writing and the ralph-playbook for "Lisa" references)

---

## Findings

*(Fill in when completing.)*

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

- Type: knowledge
- Description:
- Links:

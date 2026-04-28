---
title: "GitHub Specify, Ralph Loops, and Lisa Planning: Proof-Driven Development with AI Agents"
added: 2026-03-02T05:09:06+00:00
status: completed
priority: high
tags: [proof-driven-development, agentic-ai, ralph-loop, lisa-planning, specify, autonomous-development, github-copilot, software-engineering]
started: 2026-03-02T05:09:06+00:00
completed: 2026-03-02T05:09:06+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

### Executive Summary

The Ralph Wiggum Technique is a proof-driven autonomous coding loop coined by Geoffrey Huntley (ghuntley.com/ralph/), published July 2025 and going viral December 2025. At its simplest it is a bash `while` loop that repeatedly feeds a prompt and project context to an LLM agent until a proof criterion (tests passing) is met. The workflow has three phases — **Specify** (write scoped requirements into `specs/*.md`), **Plan** (gap-analysis agent produces `IMPLEMENTATION_PLAN.md`), and **Build** (implementation agent executes one task per loop iteration, runs backpressure, commits, repeats). "Lisa" is the planning archetype: methodical, memory-keeping, orchestrating — contrasted with Ralph's brute persistence. GitHub Copilot Agent mode maps onto this pattern through issues, AGENTS.md, and Agent Skills. This repository already follows Ralph-compatible conventions; a thin layer of `specs/` files and `IMPLEMENTATION_PLAN.md` would complete the setup.

### Key Findings

1. **The Ralph loop is three phases, two prompts, one outer loop.** Phase 1 (human + LLM conversation) defines Jobs to Be Done (JTBD) and writes one spec file per Topic of Concern (`specs/FILENAME.md`). Phase 2 (PLANNING mode) does gap analysis against the code and writes a prioritised `IMPLEMENTATION_PLAN.md` — no implementation. Phase 3 (BUILDING mode) picks the most important task, implements it, runs backpressure (tests/lint), commits, updates the plan, and exits — the outer bash loop immediately restarts with a fresh context.

2. **"Specify" is Phase 1 — not a product feature.** GitHub has no product called "Specify." In the Ralph/Lisa context, "Specify" is the requirement-writing phase that produces `specs/*.md`. In GitHub Copilot Agent mode, the equivalent is a well-written issue with detailed body, custom `.instructions.md` files, and AGENTS.md — Copilot assigns the issue, generates a plan, opens a draft PR, and iterates without human intervention between cycles.

3. **Spec format: one Markdown file per Topic of Concern.** A topic is something describable in one sentence without "and." Specs contain what-not-how. Example topics for a new research fetcher: "YouTube transcript retrieval," "transcript deduplication," "config schema validation." Each spec → multiple tasks in the plan.

4. **Context management is the core engineering discipline.** Usable context is ~176K of the advertised 200K tokens; Ralph targets 40–60% utilisation ("smart zone"). One task per loop keeps context tight. The main agent acts as a scheduler; subagents handle expensive work (file reads, test runs). Each iteration deterministically loads the same three artefacts: `PROMPT.md` + `AGENTS.md` + `specs/*`.

5. **Back-pressure (tests) is what makes the loop proof-driven.** The loop cannot advance until tests, lint, and typechecks pass. Without a stable binary fitness signal the loop degenerates. Frank Bria's implementation requires both "completion indicators" AND an explicit EXIT_SIGNAL — preventing premature exit. Ian Reppel characterises Ralph as a (1,1) evolutionary strategy: single parent, LLM-generated mutation, test suite as fitness function.

6. **Lisa = persistent memory + planning orchestration, Ralph = brute execution.** Lisa Simpson (analytical, memory-keeping) contrasts with Ralph Wiggum (persistent, naive). In practice: the PLANNING mode prompt *is* Lisa. In more sophisticated implementations, Lisa is a separate agent layer with a knowledge graph (Graphiti + Neo4j via MCP) that survives session restarts — solving the "Groundhog Day Problem" where stateless Ralph loops forget everything overnight. Lisa uses Claude Code hooks (session-start, session-stop, user-prompt-submit) to extract and store timestamped facts, decisions, and relationships about the codebase.

7. **GitHub Copilot Agent mode is spec-first by design.** Copilot's coding agent (2025): assign an issue → agent reads codebase + AGENTS.md + Agent Skills → plans → implements → opens draft PR. Agent Skills (`.github/skills/` Markdown files, announced December 2025) are invokable patterns that Copilot applies automatically. This repo's `AGENTS.md` + `.github/skills/` setup is already Copilot Agent-compatible.

8. **Active inference connection is structural, not merely analogical.** A Ralph loop minimises prediction error against a spec-as-prior: the agent's generative model predicts "tests pass"; the fitness signal is the actual test result; iteration continues until prediction error reaches zero (all tests green). This is formally identical to active inference minimising free energy — each loop iteration is a perception–action cycle where the "perception" is test output and the "action" is code edit. Proof completion = surprise minimisation to zero.

9. **Security boundary is mandatory.** `--dangerously-skip-permissions` (or equivalent) is required for headless operation. Without a sandbox (Docker, Fly Sprites, E2B), a runaway Ralph loop has access to credentials, SSH keys, and browser cookies. Escape hatches: Ctrl+C, `git reset --hard`, plan regeneration.

10. **This repo can adopt the Ralph pattern with minimal changes.** Existing foundations: `AGENTS.md` (operational guide already loaded), `src/` (code), `tests/` (backpressure), `pyproject.toml` (validation commands). Gaps: no `specs/` folder, no `IMPLEMENTATION_PLAN.md`, no `loop.sh`. The BACKLOG.md items are structurally equivalent to implementation plan tasks; the Research backlog items serve as specs. The main blocker for a full Ralph loop is headless Claude Code CLI access from CI.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Ralph = bash while loop feeding PROMPT.md to claude | ghuntley.com/ralph/ | high | Primary source; original technique description |
| Three phases: Specify → Plan → Build | ClaytonFarr/ralph-playbook, aibit.im tutorial | high | Two independent descriptions match exactly |
| One task per loop; 40-60% context = smart zone | ClaytonFarr/ralph-playbook | high | Quoted figure; matches ghuntley.com architecture diagram |
| "Specify" is not a GitHub product name | Web search, GitHub docs | high | No GitHub product by that name found |
| GitHub Copilot Agent assigns issues, plans, opens PRs | github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent | high | Official announcement |
| Agent Skills launched December 2025 | github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/ | high | Official changelog |
| Lisa = planning + persistent memory layer | dev.to/tonycasey/why-ralph-wiggum-needs-lisa-23nm, web search | medium | Lisa as product is community-built; role definition from multiple sources |
| Lisa solves Groundhog Day Problem via knowledge graph | dev.to/tonycasey/why-ralph-wiggum-needs-lisa-23nm | medium | Single primary source; architecture is credible but one team's implementation |
| Ralph is (1,1) evolutionary strategy | ianreppel.org/ralph-wiggum-as-a-degenerate-evolutionary-search/ | high | Formal analysis; the mapping is precise |
| Active inference structural equivalence | Derived from ghuntley.com/ralph/ + Friston FEP literature | low | Author's inference, not asserted in primary sources |
| frankbria/ralph-claude-code: dual-condition exit gate | github.com/frankbria/ralph-claude-code README | high | Documented feature; v0.9.9 changelog entry |

### Assumptions

- **Assumption:** Geoffrey Huntley coined the Ralph Wiggum Technique. **Justification:** ghuntley.com/ralph/ is cited by all downstream sources as the originating post; Huntley is credited as the inventor in every secondary source found.
- **Assumption:** "Specify" in the research question refers to Phase 1 of the Ralph workflow, not a GitHub product. **Justification:** Web search found no GitHub product called "Specify"; the ralph-playbook and ghuntley.com use "Specify" as a phase name. The Copilot "issue assignment" workflow is the closest product analogue.
- **Assumption:** Lisa as a persistent planning agent is community-built, not an official Huntley deliverable. **Justification:** ghuntley.com does not document Lisa; Lisa implementations (kenziecreative/lisa-simpson-claudecode, dev.to/tonycasey) are community responses to a real gap Huntley identifies (session statefulness).

### Analysis

**The workflow is a funnel, not a loop.** The outer structure is: conversation (human-guided) → PLANNING pass (bounded, usually 1–2 iterations) → BUILDING loop (unbounded, terminates on proof). Only the BUILDING phase is truly indefinite. This distinction matters for tooling: PLANNING can be triggered once per feature; BUILDING runs until done.

**Specs are the bottleneck, not the loop.** Ralph cannot converge without precise, binary-testable specs. Vague or open-ended requirements produce loops that never reach proof completion. The rate-limiting investment is spec quality, not loop configuration. This applies directly to this repo: the research backlog items describe *what to investigate* but not *what constitutes done*. A fetcher spec would need to include: protocol contract, error behaviour, test coverage targets, config schema constraints.

**Lisa's Groundhog Day solution is MCP-native.** Lisa uses Claude Code hooks + MCP (Graphiti server) to extract and persist a knowledge graph across sessions. This is architecturally compatible with the MCP server stack this repo already configures. The `memory` MCP server configured in `.mcp.json` provides similar (lighter) cross-session memory via a knowledge graph without the full Graphiti/Neo4j infrastructure.

**Evolutionary framing clarifies failure modes.** A (1,1) strategy with no fitness signal degenerates. The practical corollary: deploy no Ralph loop without a test suite. For this repo, `make check` + `pytest` are the existing fitness signals. Any new feature worked on via Ralph-style autonomous loops requires those passing before commit.

**GitHub Copilot Agent vs Claude Code Ralph: same pattern, different execution.** GitHub Copilot Agent runs in GitHub's hosted environment (no local shell, no `--dangerously-skip-permissions`). Claude Code Ralph runs locally or in a sandboxed CI-like environment. For this repo's owner (GitHub-only, no local IDE), Copilot Agent mode is the practical entry point — assign a detailed issue with clear acceptance criteria and let the agent open a PR.

### Risks, Gaps, and Uncertainties

- **Lisa product maturity is low.** Multiple community implementations exist; none appear production-stable. The Graphiti/Neo4j dependency is heavy for a knowledge graph that could be approximated with simpler solutions.
- **"--dangerously-skip-permissions" is a hard requirement for headless Claude Code.** GitHub Copilot Agent mode does not expose this flag — it runs with its own permission model. A true Claude Code Ralph loop requires a sandboxed environment this repo does not currently configure.
- **Spec quality is the unconstrained variable.** No tooling prevents writing vague specs. The "one sentence without and" test is a heuristic, not a guarantee. Observed failure mode: specs that describe the implementation rather than the behaviour.
- **Active inference connection is speculative.** The structural similarity is real but no primary source in this domain has drawn the connection formally. It remains an author's framing.

### Open Questions

- Is there a community-accepted minimal Lisa implementation (hooks + lightweight memory) that works with Claude Code without Neo4j?
- Can the Ralph building loop be triggered from a GitHub Actions workflow using `gh copilot` CLI or the Copilot API, making it accessible from the GitHub website?
- What does a practical `specs/` file look like for a new research item fetcher in this repo? Is one spec per fetcher protocol enough, or does the state/deduplication layer warrant its own spec?

---

## Output

- Type: knowledge
- Description: Structured findings on the Ralph Wiggum Technique, Lisa planning, proof-driven development, and GitHub Copilot Agent mode — including applicability assessment for this repository.
- Links:
  - https://ghuntley.com/ralph/ — primary source
  - https://github.com/ClaytonFarr/ralph-playbook — community playbook
  - https://github.com/frankbria/ralph-claude-code — Claude Code implementation
  - https://dev.to/tonycasey/why-ralph-wiggum-needs-lisa-23nm — Lisa motivation and architecture
  - https://ianreppel.org/ralph-wiggum-as-a-degenerate-evolutionary-search/ — evolutionary framing
  - https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/ — Agent Skills announcement
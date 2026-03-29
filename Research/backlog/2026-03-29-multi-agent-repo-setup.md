---
title: "Multi-agent repo setup: best practices for configuring a repository to be worked on by Claude (iOS and GitHub Issues) and Copilot (Spaces and GitHub Issues)"
added: 2026-03-29
status: backlog
priority: high
blocks: []
tags: [copilot, claude, ios, github-issues, multi-agent, copilot-spaces, repo-setup, instructions, agents-md]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Multi-agent repo setup: best practices for configuring a repository to be worked on by Claude (iOS and GitHub Issues) and Copilot (Spaces and GitHub Issues)

## Research Question

What are the best practices for setting up a GitHub repository so that it can be worked on effectively by multiple Artificial Intelligence (AI) agents — specifically: (1) Claude via the iOS Claude app, (2) Claude via GitHub Issues assigned to Claude, (3) Copilot via Copilot Spaces, and (4) Copilot via GitHub Issues assigned to the Copilot coding agent — with consistent instruction loading, environment setup, and quality outcomes across all four surfaces?

## Scope

**In scope:**
- Repository configuration files that each agent reads on startup (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `copilot-setup-steps.yml`, `devcontainer.json`)
- How GitHub Issues work with each agent surface (Copilot coding agent and Claude GitHub integration)
- How Copilot Spaces work and what repository configuration they respect
- How the Claude iOS `code` feature accesses and configures itself from the repository
- Minimal diff from this repo's current state to support all four surfaces

**Out of scope:**
- Local IDE setups (no Codespaces, no `git clone` terminal use)
- Third-party agent tools (Cursor, Aider, Codex) beyond what the research reveals incidentally
- Agent capability comparison (what each agent can *do*) — focus is configuration and instruction loading

**Constraints:** Must be achievable without adding credentials beyond those already in the repo. No local IDE access; the owner operates exclusively via the GitHub website and iOS apps.

## Context

The repository is actively used by two agents across four distinct surfaces. Each surface may load different instruction files, run in a different environment, and have different access to the skills submodule at `.github/skills/`. At present, the repo holds instructions only in `.github/copilot-instructions.md` (Architecture Decision Record (ADR)-0006 deleted `AGENTS.md` and `.claude/CLAUDE.md` on 2026-03-07). Whether this file is loaded by all four surfaces is unverified.

Three related backlog items were added on 2026-03-28 that address sub-questions directly relevant here:
- `2026-03-28-agent-instruction-loading-and-skills-access` — what each agent loads and whether it reads `.github/skills/`
- `2026-03-28-agents-md-role-and-cross-agent-instructions` — the role of `AGENTS.md` in a repo using `copilot-instructions.md`
- `2026-03-28-environment-setup-consistency` — environment setup (dependencies, submodule) for each agent surface

This item is the parent strategy question: given findings from those three items, what is the complete, minimal repo configuration that makes all four surfaces work well together?

## Approach

1. **Q1 — GitHub Issues → Copilot coding agent:** What repo configuration does the Copilot coding agent need to receive instructions, initialise the environment, and access the skills submodule when it picks up an assigned GitHub issue? What is the role of `.github/copilot-setup-steps.yml`? What files does it read before planning?

2. **Q2 — Copilot Spaces:** What is Copilot Spaces? How does it interact with a repository? What configuration does it respect — does it read `.github/copilot-instructions.md`, `AGENTS.md`, or a Spaces-specific file? Is it in scope for this repository?

3. **Q3 — GitHub Issues → Claude:** Is there a GitHub integration for assigning issues to Claude directly (analogous to the Copilot coding agent)? If so, what repo configuration does it require — `CLAUDE.md`, `AGENTS.md`, a GitHub App? What is the setup process?

4. **Q4 — Claude iOS app (`code` feature):** What files does the Claude iOS `code` feature load when a repository is opened? Does it clone the repo locally, or operate via the GitHub Application Programming Interface (API)? What is the path to making the iOS surface read the same instructions as the other surfaces?

5. **Q5 — Convergence and minimum viable configuration:** Given answers to Q1–Q4, what is the smallest set of files that reliably serves all four agent surfaces? Is a thin `AGENTS.md` pointer the right pattern, or does each surface need a dedicated file? Map current state to recommended target state.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [GitHub Copilot coding agent documentation](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-as-an-agent) — entry point for coding agent behaviour and configuration
- [ ] [GitHub Copilot custom instructions (.github/copilot-instructions.md)](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) — what the file covers and which surfaces load it
- [ ] [copilot-setup-steps documentation](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) — schema and when it runs
- [ ] [Copilot Spaces documentation](https://docs.github.com/en/copilot/github-copilot-spaces/about-github-copilot-spaces) — what Spaces are and how they use repo config
- [ ] [AGENTS.md specification / agentprotocol.ai](https://agentprotocol.ai) — cross-vendor standard for agent instruction files
- [ ] [Anthropic Claude iOS app `code` feature](https://support.anthropic.com/en/articles/10166833-using-claude-for-coding) — how Claude iOS interacts with repositories
- [ ] [Claude GitHub integration / Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview) — how GitHub Issues can be assigned to Claude
- [ ] `docs-adr/0006-standardise-agent-instructions.md` — local ADR documenting the decision to delete `AGENTS.md`
- [ ] `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — prior research on `AGENTS.md` as cross-vendor standard
- [ ] `Research/completed/2026-03-22-using-awesome-copilot-across-repos.md` — prior research noting `AGENTS.md` is read by GitHub web

---

## Research Skill Output

*(Research agent to complete)*

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
- Description: Confirmed minimum viable repo configuration for all four agent surfaces; actionable recommendations for what files to add, remove, or modify; new backlog items for any implementation work identified.
- Links:

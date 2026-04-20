---
title: "Harness-level selection and use of tools, agents, skills, prompts, and instruction files"
added: 2026-04-20
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agent-harnesses, copilot, claude-code, codex, opencode, prompts, instructions, skills, tools, best-practices]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Harness-level selection and use of tools, agents, skills, prompts, and instruction files

## Research Question

When should teams choose tools, agent definition files, skills, prompts, instruction files, and AGENTS.md, and what verifiable best practices align with how major harnesses actually select and apply each artifact?

## Scope

**In scope:**
- Define common concepts and boundaries: tool, agent definition file, skill, prompt, instruction file, and AGENTS.md
- Compare selection and utilisation behavior across GitHub Copilot (issue assignment flow, Copilot Spaces, Visual Studio Code (VS Code) extension, command line interface (CLI)), Claude Code, OpenCode CLI, Codex, and closely related harnesses with public documentation
- Identify currently common files, common selection mechanisms, and precedence rules where documented
- Distinguish implementation-defined behavior (documented, testable, or source-backed) from opinion-based guidance
- Capture current trends and emerging patterns in harness design

**Out of scope:**
- Building or changing any harness implementation
- Vendor marketing claims that cannot be tied to documented behavior or code
- Proprietary internal harnesses without public, verifiable documentation

**Constraints:** (time, source types, access)
Use publicly verifiable sources only (official documentation, source repositories, standards/specifications, and reproducible behavior notes). Prioritise primary sources and clearly flag unknowns where no authoritative evidence exists.

## Context

The issue requests a non-opinionated, evidence-backed guide for deciding between multiple markdown-based control artifacts whose behavior differs by harness, so this research should produce decision-quality clarity on file roles, selection methods, and practical adoption patterns.

## Approach

1. Build a terminology map for each artifact type, including equivalent names used by each harness.
2. For each target harness, document the loading and precedence model for tools, agents, skills, prompts, instructions, and AGENTS.md-like files.
3. Verify each behavior against primary documentation and, where possible, implementation sources or reproducible examples.
4. Produce a cross-harness comparison matrix showing common files, selection methods, and divergence points.
5. Synthesize evidence-backed best practices for both general use and harness-specific use.
6. Extract trend signals and emerging conventions, then list open gaps that need ongoing tracking.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [GitHub Docs: Configure custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) — baseline instruction-file behavior in GitHub Copilot
- [ ] [GitHub Docs: About Copilot Spaces](https://docs.github.com/en/copilot/concepts/copilot-spaces/about-copilot-spaces) — product-level context model and reusable instruction spaces
- [ ] [GitHub Docs: Customize the Copilot coding agent development environment](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/customizing-the-development-environment-for-copilot-coding-agent) — agent-oriented repository controls and workflow integration
- [ ] [Visual Studio Code Docs: GitHub Copilot customization](https://code.visualstudio.com/docs/copilot/copilot-customization) — Visual Studio Code (VS Code) harness behavior and configuration surfaces
- [ ] [Anthropic Docs: Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview) — Claude Code artifact model and execution context
- [ ] [Anthropic Docs: Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/memory) — repository and user instruction persistence behavior
- [ ] [OpenCode Docs](https://opencode.ai/docs) — OpenCode CLI configuration and instruction model
- [ ] [OpenAI Docs: Codex](https://developers.openai.com/codex/overview) — Codex harness concepts and task execution model
- [ ] [AGENTS.md specification](https://agents.md/) — emerging cross-tool convention for repository-level agent instructions

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:

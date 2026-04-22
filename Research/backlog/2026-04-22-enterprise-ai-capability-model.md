---
title: "Enterprise AI capability model for use-case maturity decisions"
added: 2026-04-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai, enterprise, capability-model, maturity-framework, software-delivery]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Enterprise AI capability model for use-case maturity decisions

## Research Question

What enterprise-wide Artificial Intelligence (AI) capability model best supports deciding whether a candidate AI use case requires net-new foundational capabilities or can reuse capabilities already built across the enterprise?

## Scope

**In scope:**
- Synthesize capability models and maturity frameworks relevant to enterprise AI adoption and scale
- Compare software-delivery-focused evidence (for example, Development and Operations (DevOps) research) with broader enterprise and investment ecosystem perspectives
- Derive a reusable capability map for use-case triage: foundational capability needed vs reusable capability available
- Define practical decision criteria, observable signals, and governance checkpoints for use-case assessment

**Out of scope:**
- Building or selecting a specific vendor platform
- Detailed implementation playbooks for one company or one business unit
- Financial business case modelling at project level

**Constraints:** (time, source types, access)
- Prioritise high-signal, current sources (2024-2026 where available)
- Start from reports listed in the issue and add complementary maturity frameworks
- Use public sources only

## Context

The issue asks for an AI ecosystem capability model that helps enterprise leaders judge which use cases should invest in foundational capabilities first versus which can safely reuse capabilities already established. This directly informs sequencing, governance, and delivery strategy for enterprise-wide AI maturity.

## Approach

1. Extract and normalise capability dimensions from DORA, GitClear, and other software-engineering-focused reports.
2. Extract enterprise-scale capability dimensions from ecosystem reports (Stanford AI Index, State of AI, McKinsey, and similar).
3. Add benchmark maturity frameworks (for example, National Institute of Standards and Technology (NIST) AI Risk Management Framework and International Organization for Standardization (ISO)/International Electrotechnical Commission (IEC) 42001) to cover governance and risk capability baselines.
4. Build a consolidated capability taxonomy grouped into foundational, enabling, and differentiating capabilities.
5. Define a use-case triage rubric mapping each use case to required capabilities, readiness indicators, and build-vs-reuse guidance.
6. Validate the model against representative use-case archetypes and identify likely failure modes when foundational capabilities are missing.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [DORA Research Program](https://dora.dev/research/) — primary source for the 2024 and 2025 Development and Operations (DevOps) reports and associated AI capability guidance
- [ ] [Google Cloud DORA overview](https://cloud.google.com/devops) — contextual landing page for DORA report publication and capability framing
- [ ] [GitClear AI code quality research](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) — telemetry-based counterpoint on code churn and cloning
- [ ] [State of AI Report](https://www.stateof.ai/) — annual ecosystem synthesis across research, market, and policy signals
- [ ] [Stanford Human-Centered Artificial Intelligence (HAI) AI Index](https://hai.stanford.edu/ai-index) — data-heavy annual benchmark across investment, policy, education, and model progress
- [ ] [a16z Big Ideas in Tech](https://a16z.com/big-ideas-in-tech/) — venture and product-strategy perspective with substantial AI sections
- [ ] [McKinsey State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — enterprise survey evidence on adoption and scaling bottlenecks
- [ ] [McKinsey Superagency in the Workplace](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential) — workforce and operating-model capability gaps
- [ ] [GitHub Octoverse](https://octoverse.github.com/) — software ecosystem and developer workflow trend context
- [ ] [GitHub Research and impact posts](https://github.blog/news-insights/research/) — publicly shared findings on Copilot productivity and developer outcomes
- [ ] [Faros AI Productivity Paradox](https://faros.ai/blog/the-ai-productivity-paradox) — telemetry analysis of individual versus organisational productivity effects
- [ ] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — governance and risk capability baseline for enterprise maturity
- [ ] [ISO/IEC 42001 standard overview](https://www.iso.org/standard/81230.html) — AI management system standard relevant to organisational capability design

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

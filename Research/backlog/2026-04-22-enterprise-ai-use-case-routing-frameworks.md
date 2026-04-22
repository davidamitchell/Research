---
title: "Enterprise AI use-case routing frameworks"
added: 2026-04-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [artificial-intelligence, platform-governance, risk-tiering, operating-model]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Enterprise AI use-case routing frameworks

## Research Question

What decision frameworks do enterprises use to route Artificial Intelligence (AI) use cases to the appropriate platform, implementation pattern, and risk tier—distinguishing low-code business-led, pro-code custom, and developer productivity use cases—and what criteria, routing signals, and governance checkpoints does each routing decision require?

## Scope

**In scope:**
- Enterprise decision frameworks that classify AI use cases into low-code business-led, pro-code custom, and developer productivity routes.
- Gating criteria used at intake (data sensitivity, model criticality, autonomy level, integration depth, change impact, and regulatory exposure).
- Governance checkpoints per route (architecture review, security/privacy review, legal/compliance review, human oversight, and post-deployment monitoring).
- Practical operating models (central platform team, federated domain teams, and hybrid models) that determine who can build what, where, and under what controls.

**Out of scope:**
- Vendor-specific implementation tutorials for a single tool.
- Detailed model-training techniques unrelated to routing and governance decisions.
- Small-business or consumer-only contexts that do not map to enterprise governance constraints.

**Constraints:** (time, source types, access)
- Prioritise public, citable sources from standards bodies, regulators, cloud/platform architecture guidance, and enterprise governance publications.
- Focus on frameworks and checkpoints that can be translated into an actionable triage rubric for backlog intake.
- Identify where evidence is prescriptive guidance versus observed enterprise practice.

## Context

Enterprises need a repeatable intake decision process that sends each AI use case to the right delivery path (business-led low-code, pro-code custom engineering, or developer productivity enablement) while applying proportional risk controls. Without a clear routing framework, teams either over-govern low-risk work or under-govern high-risk deployments, slowing delivery and increasing operational and compliance risk.

## Approach

Decompose the question into sub-questions and describe how each will be investigated (literature review, experiment, prototype, expert interview, etc.).

1. Identify the most-cited enterprise AI governance and risk management frameworks, then extract how they classify use-case risk and required controls.
2. Compare enterprise platform strategy guidance to map route-selection criteria for low-code business-led, pro-code custom, and developer productivity use cases.
3. Synthesize common intake signals into a draft routing matrix (criteria, thresholds, route assignment, and checkpoint sequence).
4. Validate governance checkpoints per route (security, privacy, legal, model risk, and operational readiness) and note minimum evidence artifacts required to pass each gate.
5. Highlight failure modes (misrouting, control gaps, and review bottlenecks) and mitigation patterns used in mature enterprise operating models.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — baseline risk framing and governance functions for AI systems.
- [ ] [International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) 42001 Artificial intelligence management system](https://www.iso.org/standard/81230.html) — management-system structure for enterprise AI governance.
- [ ] [European Union (EU) AI Act overview](https://artificialintelligenceact.eu/) — regulatory risk-tier context and obligations relevant to routing decisions.
- [ ] [Cloud Adoption Framework for Azure: AI governance](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern) — enterprise operating model and governance checkpoints.
- [ ] [Google Cloud Architecture Framework: AI and machine learning governance](https://cloud.google.com/architecture/framework) — control and architecture decision guidance for AI workloads.
- [ ] [Amazon Web Services (AWS) Well-Architected Framework: Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/welcome.html) — route-specific architecture and risk considerations.

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

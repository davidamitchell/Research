---
title: "Runtime placement criteria for software-engineering agents in regulated organisations"
added: 2026-10-17T07:34:52+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, governance-policy, security-risk, tools-infrastructure, regulatory-compliance]
started: ~
completed: ~
output: []
cites: [2026-08-12-ai-coding-agent-runtime-security-evolution, 2026-04-26-ai-agent-identity-access-management-enterprise]
related: [2026-03-08-ai-coding-harnesses-agent-philosophy]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Runtime placement criteria for software-engineering agents in regulated organisations

## Research Question

For software-engineering agent workloads in a regulated organisation, what evidence-based conditions justify placing a workload in local execution on a developer workstation, a vendor-hosted coding-agent runtime, or an organisation-owned managed agent runtime? How do scaffolding maturity, identity and attribution, raw versus sanctioned reach, model choice, triggering, egress controls, risk, parallelism, and volume affect that placement, and what measurable criteria support moving forward, skipping a stage, or moving back?

## Scope

**In scope:**
- Placement decisions across local workstation, vendor-hosted, and organisation-owned managed runtimes.
- Whether agent input scaffolding and output validation maturity support unattended execution, and evidence that distinguishes their effect from model capability.
- Agent identity, delegation, credential scope and revocation, attribution, and audit records.
- Raw versus sanctioned access, local controls, vendor-hosted egress and tool enforcement, and organisation-owned cloud runners as an intermediate option.
- Model choice, workload triggers, and measurable placement thresholds for risk, scaffolding maturity, parallelism, and volume.

**Out of scope:**
- Isolation mechanics already covered by the cited runtime item, including microVM versus container choices and session persistence.
- Model economics and harness feature comparisons.

**Constraints:**
- Use primary vendor documentation and changelogs for factual claims; identify undocumented behavior rather than infer it.
- Keep the framing vendor-neutral, using named products only as worked examples.

## Context

The cited runtime research established the three execution stages and their security mechanics, while the identity research addressed agent identity; this item asks what makes moving a particular workload between those stages safe and worthwhile, with the working hypothesis that unattended trust depends more on scaffolding and validation than on supervision alone.

## Approach

1. Compare scaffolding and validation maturity across the three stages; assess evidence about unattended reliability and whether it tracks those controls independently of model capability.
2. For widely adopted vendor-hosted coding agents, establish from primary documentation which principal acts, how commits, pull requests, and audit events are attributed, what credentials and scopes are granted, when they are revoked, and what remains undocumented.
3. Compare raw and sanctioned reach across stages, identify controls that limit local access without changing stages, and determine whether vendor-hosted egress, tool access, and secrets are enforceable at organisation or repository level; assess organisation-cloud runners as an intermediate option.
4. Compare model-selection options and the available work triggers at each stage, including human, issue, event, and scheduled starts.
5. Build an evidence-backed placement matrix using measurable criteria for scaffolding maturity, risk classification, parallelism, and volume; distinguish evidence-supported thresholds from proposed decision rules and identify when to skip or move back a stage.

## Sources

- [Secure Runtime Evolution for AI Coding Agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md) — cited work establishing the runtime stages and security mechanics.
- [Enterprise Agent Identity and Access Management](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md) — cited work on agent identity, access, and attribution.
- [AI Coding Harnesses: Execution Model, Memory, and Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md) — related work on coding-agent execution models.

## Related

- [Secure Runtime Evolution for AI Coding Agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md)
- [Enterprise Agent Identity and Access Management](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md)
- [AI Coding Harnesses: Execution Model, Memory, and Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:

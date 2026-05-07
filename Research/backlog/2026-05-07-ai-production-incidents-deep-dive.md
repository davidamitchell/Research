---
title: "Production incidents linked to Artificial Intelligence systems"
added: 2026-05-07T12:05:05+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, governance, ai-platform, evaluation]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Production incidents linked to Artificial Intelligence systems

## Research Question

What documented production incidents over the last five years were caused or materially contributed to by Artificial Intelligence (AI) systems, and what recurring failure modes and mitigations were identified?

## Scope

**In scope:**
- Publicly documented production incidents involving deployed AI systems (consumer, enterprise, or public-sector)
- Incident characteristics: trigger conditions, impact, and time-to-detection/remediation where available
- Evidence-based classification of failure modes (for example model behaviour, orchestration, data pipeline, governance, monitoring, or human-in-the-loop breakdown)
- Mitigation patterns that were applied or recommended after the incidents

**Out of scope:**
- Laboratory-only failures with no production deployment impact
- Speculative or anecdotal claims lacking verifiable sources
- General AI risk commentary that is not tied to specific incidents

**Constraints:** (time, source types, access)
- Focus on incidents from 2021 onward unless an earlier incident is repeatedly cited as foundational context
- Prioritise primary incident reports, regulator disclosures, postmortems, and reputable incident databases
- Every extracted incident claim must map to at least one URL in `## Sources`

## Context

This question informs operational and governance decisions about how to safely deploy AI systems in production by identifying real-world failure patterns rather than hypothetical risks.

## Approach

1. Build a candidate list of production AI incidents from incident databases, regulator notices, and vendor/public postmortems.
2. Validate each candidate against source quality criteria and remove items without sufficient evidence.
3. For validated incidents, extract structured fields (system type, trigger, impact, detection mode, remediation, and residual risk).
4. Group incidents into recurring failure-mode categories and identify cross-incident mitigation patterns.
5. Synthesize practical controls and monitoring recommendations tied to the observed incident patterns.

## Sources

- [AI Incident Database](https://incidentdatabase.ai/) — seed catalogue of publicly reported AI incidents
- [Organisation for Economic Co-operation and Development (OECD) AI Incidents Monitor](https://oecd.ai/en/incidents) — supplementary incident repository
- [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — mitigation and governance framing for categorizing controls
https://www.pointguardai.com/ai-security-incident-tracker
https://www.osohq.com/developers/ai-agents-gone-rogue
https://github.com/webpro255/awesome-ai-agent-attacks
https://www.gravitee.io/blog/88-of-companies-have-already-seen-ai-agent-security-failures

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

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:

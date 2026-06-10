---
title: "AI productivity, quality, and governance open questions"
added: 2026-06-10T09:29:28+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
themes: [benchmarks-eval, software-engineering, enterprise-adoption, governance-policy, agentic-ai]  # 3–5 canonical slugs from docs/themes-vocabulary.md — e.g. [agentic-ai, governance-policy, tools-infrastructure]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator, 2026-05-31-itil-capacity-baseline-assertion-vs-telemetry, 2026-04-30-tdd-feedback-loops-ai-augmented-dev]        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# AI productivity, quality, and governance open questions

## Research Question

What empirical evidence can distinguish sustainable Artificial Intelligence (AI)-enabled software delivery gains from short-lived throughput effects and hidden quality or governance costs in production engineering organizations over a 12-to-24-month horizon?

## Scope

**In scope:**
- Empirical productivity and throughput metrics (per-developer repository creation, approval latency, capacity constraints, fast-path versus exception-path flow)
- Longitudinal quality and maintainability indicators (architectural coherence, cognitive debt proxies, maintenance effort ratios, mutation-score trends)
- Organizational readiness and operating-model controls (Platform Engineering maturity, junior onboarding redesign, runtime controls, rollback and reversal design)
- Comparison of suggestion-based assistants versus autonomous multi-step code agents in regulated and high-control environments

**Out of scope:**
- Vendor marketing claims without field evidence or reproducible methods
- Consumer use cases outside professional software delivery organizations
- Prescriptive tooling selection for a single company without transferable evidence

**Constraints:** (time, source types, access)
- Prioritize studies and field reports from 2019–2026 to capture pre-assistant and post-adoption periods
- Use public sources only (peer-reviewed papers, standards, benchmark reports, engineering field studies, regulator publications)
- Separate directly observed facts from model-based inferences where causal evidence is incomplete

## Context

This question informs strategic decisions about where to adopt agentic delivery tooling, where to hold stricter controls, and which measurement system can detect whether observed acceleration is producing durable value or deferred operational risk.

## Approach

Decompose the investigation into independent evidence threads that can be synthesized into one decision-ready model.

1. Throughput and bottleneck dynamics
   1a. Measure whether repository and change-volume growth remains significant after normalizing for developer-count growth.
   1b. Test whether bottlenecks shift from approval latency to execution capacity as governance and approvals are streamlined.
   1c. Estimate whether the observed stability drop during adoption behaves as a temporary transition effect or a persistent steady-state penalty.
   1d. Quantify fast-path versus exception-path flow changes as throughput increases.
2. Codebase quality and maintenance externalities
   2a. Evaluate 12-to-24-month architectural coherence outcomes in teams with high assistant usage.
   2b. Identify validated instruments for measuring cognitive debt accumulation in AI-assisted codebases.
   2c. Estimate maintenance ratios for workaround-heavy agent outputs (review, operations, and incident recovery effort).
   2d. Compare mutation-score trajectories across representative repositories between 2019 and 2025.
3. Organizational readiness and governance calibration
   3a. Identify the minimum Platform Engineering maturity conditions associated with net-positive outcomes.
   3b. Evaluate onboarding and career-path redesign options for junior engineers when entry-level automation tasks are displaced.
   3c. Compare runtime controls and approval patterns that reduce do-mode incidents while preserving economic return.
   3d. Evaluate the option value of time-boxed recurring-agent pilots for target-state architecture discovery.
4. Agentic versus suggestion-based tool comparison
   4a. Compare productivity and quality outcomes for autonomous code agents versus suggestion-based copilots.
   4b. Estimate incident-type asymmetry between explicit hard failures and silent semantic degradations.
   4c. Identify new high-control field evidence from heavily regulated engineering environments.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below — they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` — for papers with named authors
- `[Organisation Title](https://url)` — for documentation, standards, or pages without a named author

- [ ] [GitHub Issue #621: Many new research questions to answer outstanding questions](https://github.com/davidamitchell/Research/issues/621) — seed set of open questions spanning productivity, quality, governance, and agentic adoption.

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

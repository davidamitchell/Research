---
title: "State mutation decision framework: mapping delivery delay, ownership, and change costs"
added: 2026-10-23T21:41:54+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
themes: [software-engineering, cost-performance, benchmarks-eval]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-ai-code-entropy-quality-metrics, 2026-05-21-monolith-vs-cohesive-portfolio-tco, 2026-05-29-commit-trends-repo-velocity-rework-abandonment, 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# State mutation decision framework: mapping delivery delay, ownership, and change costs

## Research Question

Which published empirical software-engineering metrics can operationalise Cost of Delay (CoD),
Future Cost of Ownership (FCO), and Future Cost of Change (FCC), and what evidence shows whether
shortcut-related quality degradation compounds over time or affects ownership and change costs
differently across software architecture styles?

## Scope

**In scope:**
- Map established software quality, delivery, and cost measures to CoD, FCO, and FCC; test whether
  each measure is a direct outcome, a proxy, or an indicator of more than one construct.
- Assess candidate FCO indicators such as defect density, mean time to resolution (MTTR), incident
  frequency, and patch overhead, and candidate FCC indicators such as code churn, change
  propagation, cyclomatic complexity, and modification blast radius.
- Assess candidate CoD indicators such as change lead time, release latency, and service-level
  agreement (SLA) non-compliance costs, distinguishing elapsed delivery time from monetised delay.
- Review evidence linking technical shortcuts or technical debt to later maintenance burden and
  change friction, separating longitudinal or causal findings from cross-sectional correlations.
- Compare evidence across architecture styles, including monolithic, modular-monolith, and
  microservice systems, without assuming that operating cost and change friction move together.
- Consider relevant measurement frameworks and cost models, including the International
  Organization for Standardization and International Electrotechnical Commission (ISO/IEC) 25010
  quality model, Consortium for Information & Software Quality (CISQ) automated measures, and
  Constructive Cost Model II (COCOMO II) drivers.

**Out of scope:**
- Prescribing a universally superior architecture or a single metric score for all organisations.
- Vendor-specific tooling, pricing, or recommendations for a particular enterprise.
- Treating shortcut exposure as a comparable numeric variable unless a study defines and measures
  it explicitly.

**Constraints:**
- Search the Association for Computing Machinery (ACM) Digital Library, Institute of Electrical
  and Electronics Engineers (IEEE) Xplore, Google Scholar, and Software Engineering Institute
  (SEI) technical reports; record search strings, dates, screening criteria, and exclusions.
- Prefer peer-reviewed empirical studies, repository-mining datasets, official standards, and
  primary technical reports; use secondary sources for discovery and context.
- Report effect sizes and study limitations where available; do not infer a universal compounding
  rate from heterogeneous measures or observational associations.
- Treat CoD, FCO, and FCC as constructs to operationalise and validate, not as interchangeable
  labels for existing metrics.

## Context

The existing corpus asks which quality-metric bundle best predicts remediation cost
([code entropy and quality metrics](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md)),
leaves open when modular monoliths capture change benefits without service-governance costs
([architecture portfolio total cost of ownership](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md)),
tracks repository velocity and rework while leaving longitudinal outcomes unresolved
([repository commit trends](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md)),
and asks which measures distinguish unmet demand and debt accumulation
([throughput and debt accumulation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md)).
This review connects those strands to determine whether their metrics measure distinct cost
constructs or overlapping proxies, informing decisions about where short-term delivery choices
create later operating or modification costs.

## Approach

1. Define CoD, FCO, and FCC as decision constructs and identify how published studies operationalise
   delivery delay, recurring ownership cost, and change effort.
   1a. Map candidate measures to the construct and outcome they directly observe.
   1b. Check construct validity, overlap, measurement windows, and whether measures capture cost
   rather than only technical condition or elapsed time.
2. Review repository-mining and software-economics evidence on shortcuts and technical debt.
   2a. Extract longitudinal and causal estimates separately from cross-sectional associations.
   2b. Record how studies define shortcuts, debt, maintenance overhead, and change friction; identify
   whether any measured exposure supports a compounding claim.
3. Compare operational ownership costs and change-friction outcomes across architecture styles.
   3a. Separate recurring run-state outcomes from the effort and risk of making modifications.
   3b. Identify architecture, system size, team, and governance factors that may confound or moderate
   the comparison.
4. Synthesize a decision-oriented metric map, stating which measures are supported, ambiguous, or
   unsupported for each construct, and identify evidence gaps that prevent causal or general claims.

## Sources

Starting points from the completed research corpus and references already catalogued there:

- [ ] [McCabe (1976) A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837) — cyclomatic complexity measure used in the quality-metrics review.
- [ ] [Chidamber and Kemerer (1994) A Metrics Suite for Object Oriented Design](https://ieeexplore.ieee.org/document/295895/) — object-oriented design metrics cited in the architecture cost review.
- [ ] [DevOps Research and Assessment (DORA) 2024 State of DevOps Report](https://dora.dev/research/2024/dora-report/) — delivery-performance and stability outcomes.
- [ ] [GitClear (2025) AI Copilot Code Quality: 2025 Look Back at 12 Months of Data](https://www.gitclear.com/ai_assistant_code_quality_2025_research) — repository-mining indicators of churn and rework.
- [ ] [Mitchell (2026) Artificial Intelligence code entropy and complexity](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md) — prior work on code-quality indicators and remediation-cost metric gaps.
- [ ] [Mitchell (2026) Long-term total cost of ownership trade-offs](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md) — prior architecture comparison and open questions on modular-monolith and governance costs.
- [ ] [Mitchell (2026) Software-development commit trends](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md) — repository velocity, rework, and open longitudinal questions.
- [ ] [Mitchell (2026) Information Technology throughput and debt accumulation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md) — prior work on delivery constraints and the need for debt-accumulation indicators.

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

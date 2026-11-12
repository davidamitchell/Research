---
title: "A practical product quality measurement rubric for internal platforms"
added: 2026-11-12T08:07:53+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
themes: [benchmarks-eval, software-engineering, tools-infrastructure, regulatory-compliance, organisational-design]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related:
  - 2026-10-02-ideal-internal-platform-product-standard
  - 2026-10-01-thinnest-viable-internal-platform-standard
  - 2026-08-13-llm-consumption-maturity-ladder
  - 2026-05-31-sre-slo-threshold-justification
  - 2026-03-02-research-quality-assurance-methodology
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# A practical product quality measurement rubric for internal platforms

## Research Question

What is the most practical way to adapt and operationalise the International Organization for Standardization and International Electrotechnical Commission (ISO/IEC) 25010 Product Quality Model as a reusable, evidence-backed measurement and five-level maturity rubric for assessing and improving internal platforms and enterprise systems in knowledge-work and regulated settings?

## Scope

**In scope:**
- Actionable measurements for each of the eight requested product-quality characteristics and key sub-characteristics, using ISO/IEC 25023 formulas where applicable and identifying observable indicators, tools and data sources.
- Characteristic-level scoring criteria, evidence requirements and maturity mapping, including mappings to National Institute of Standards and Technology (NIST) and Center for Internet Security (CIS) controls and verification methods.
- Links to continuous integration and continuous delivery (CI/CD) gates, application performance monitoring (APM), telemetry, DevOps Research and Assessment (DORA) metrics, chaos and disaster recovery (DR) drills, static application security testing (SAST), dynamic application security testing (DAST), accessibility audits and architecture fitness functions.
- How scores and maturity levels inform prioritisation, investment, service level objectives (SLOs), error budgets and continuous improvement.

**Out of scope:**
- Formal certification against the ISO/IEC 25000 series and the quality-in-use model.
- Domain-specific safety-critical certification beyond the product-quality lens and green-field consumer products outside enterprise or internal-platform contexts.

**Constraints:**
- Prefer existing telemetry, delivery and operational data over a new heavy measurement programme; account for federated multi-team ownership, regulatory expectations and auditable evidence trails.
- Draw on standards, published practice and prior local research. The issue refers to a supplied summary but does not include it; recover it if available or explicitly note the gap.
- Verify the applicable editions and characteristic counts before adopting the requested eight-characteristic framing; distinguish an adapted Capability Maturity Model Integration (CMMI)-style rubric from formal appraisal. Standards may require paid access, so distinguish verified formulas from adaptations if the text is unavailable.

## Context

Platform, architecture and quality teams need a concrete way to collect evidence, score product quality and choose improvements, extending prior work on assessable internal-platform standards.

## Approach

Investigate the following through standards and published-practice review, cross-checking the prior local research:

1. Which editions, characteristics and sub-characteristics are relevant, and how should differences from the requested eight-characteristic summary be handled?
2. For each characteristic, which ISO/IEC 25023 measurement functions apply, and what practical indicators, formulas, data sources and tools can supply equivalent evidence where access or telemetry is limited?
3. What five-level criteria and evidence requirements make each characteristic's score repeatable across teams, and how should missing data, ownership and audit trails be handled?
4. How can the measurements map to NIST and CIS controls and to existing tests, delivery gates, monitoring, accessibility audits and resilience drills without implying control compliance?
5. How should teams use the resulting scores, risks and maturity gaps to prioritise investment, set SLOs and error budgets, and track improvement? This depends on the measurement and scoring design in questions 2–3.

Readiness: READY — the question is specific, answerable in principle, scoped, motivated and decomposable; access to standards and the missing summary are constraints to resolve during research.

## Sources

- [ ] [Ideal internal platforms as products: an assessable operating standard](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md)
- [ ] [Satisfiable internal platforms: a practical standard for platform teams](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-01-thinnest-viable-internal-platform-standard.md)
- [ ] [Enterprise artificial intelligence maturity frameworks and the language model consumption ladder](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md)
- [ ] [Establishing service level objectives as contractual capability boundaries](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md)
- [ ] [Research quality assurance methodology](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-research-quality-assurance-methodology.md)

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

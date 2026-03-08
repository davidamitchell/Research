---
title: "Better Business Cases: Five Case Model authoring and application"
added: 2026-03-08
status: backlog
priority: medium
blocks: []
tags: [business-case, bbc, five-case-model, public-sector, strategy, economics, procurement]
started: ~
completed: ~
output: [knowledge, skill]
---

# Better Business Cases: Five Case Model authoring and application

## Research Question

What is the Better Business Cases (BBC) Five Case Model framework, what are the requirements and standards for each of the five cases, and how should an AI agent apply this framework to author, review, and critique business cases proportionately?

## Scope

**In scope:**
- HM Treasury BBC Five Case Model: Strategic, Economic, Commercial, Financial, and Management cases
- Proportionality guidance: Strategic Outline Case (SOC), Outline Business Case (OBC), Full Business Case (FBC)
- Options framework: long-list generation, short-listing criteria, do-nothing baseline
- Economic appraisal methods: Net Present Value (NPV), Benefit-Cost Ratio (BCR), optimism bias, sensitivity analysis
- Common failure modes and quality tests for each case
- Relationship to HM Treasury Green Book and Infrastructure and Projects Authority (IPA) assurance

**Out of scope:**
- Organisation-specific business case templates (NHS, MOD, etc.) beyond referencing their derivations from BBC
- Detailed financial modelling or spreadsheet design
- Procurement law and contract law details beyond what is needed to structure the Commercial Case

**Constraints:** Primary sources are HM Treasury guidance documents and the BBC framework itself; secondary sources are worked examples and IPA guidance.

## Context

The Better Business Cases framework is the UK public sector standard for investment proposals and spending approvals. Any AI-assisted work in a government or public-sector context that involves recommending investment, structuring a business case, or reviewing an approval submission will encounter this framework. Understanding the Five Case Model well enough to author compliant, proportionate business cases — and to identify gaps in submitted ones — is a directly applicable skill. The `strategy-author` skill handles strategy documents; the BBC framework handles the wider investment case including economic appraisal, commercial structuring, financial affordability, and management arrangements. These are distinct skill sets.

## Approach

1. Obtain and review HM Treasury BBC guidance: "Better Business Cases: Guide to Developing the Project Business Case" and the Green Book
2. Map the five cases: required content, quality tests, and common failure modes for each
3. Review the proportionality framework: SOC vs OBC vs FBC requirements and decision criteria
4. Analyse the options framework: how long-list and short-list appraisal should be structured
5. Review economic appraisal requirements: Green Book discount rates, NPV/BCR methods, optimism bias tables, sensitivity analysis
6. Identify common failure modes across BBC submissions (from IPA guidance and audit reports)
7. Synthesise into a skill specification: input contract, structured authoring process, quality tests, behavioural constraints

## Sources

- [ ] HM Treasury – Better Business Cases: Guide to Developing the Project Business Case (latest edition): https://www.gov.uk/government/publications/better-business-cases-for-better-outcomes
- [ ] HM Treasury – The Green Book: Central Government Guidance on Appraisal and Evaluation: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government
- [ ] Infrastructure and Projects Authority – Assurance Review Toolkit: https://www.gov.uk/government/collections/infrastructure-and-projects-authority-ipa-assurance-toolkit
- [ ] HM Treasury – Guide to Developing the Project Business Case (supplementary guidance)
- [ ] National Audit Office – reports on business case quality in major government programmes (for failure mode evidence)

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

- Type: knowledge, skill
- Description: BBC Five Case Model framework knowledge and a `bbc-author` skill for authoring, reviewing, and critiquing Better Business Cases
- Links:
  - `.github/skills/bbc-author/SKILL.md` — initial draft skill created alongside this backlog item

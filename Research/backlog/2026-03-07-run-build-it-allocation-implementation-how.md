---
title: "How organisations practically implement IT RUN vs BUILD cost allocation"
added: 2026-03-07
status: backlog
priority: medium
blocks: []
tags: [it-finance, run-build, cost-allocation, application-portfolio, change-management, organisational-design, tbm]
started: ~
completed: ~
output: [knowledge]
---

# How organisations practically implement IT RUN vs BUILD cost allocation

## Research Question

How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: how did they agree on what counts as an "application", how did they get consistent work-item tagging across teams, how did they establish a shared team taxonomy, who drove the change, and how did they make the business case for the investment required?

## Scope

**In scope:**
- How organisations define "application" in practice — the governance process, who decides, how edge cases (shared platforms, vendor bundles, middleware) are resolved, and how the definition is maintained over time
- How teams are defined and kept consistent — the challenge of a shared team taxonomy when org structures change, when work cuts across teams, and when contracts don't align with internal team boundaries
- How work-item (ticket) tagging is enforced or incentivised — tooling choices, training, gamification, automation, and what happens when tagging breaks down
- How contracts and vendor agreements are mapped to applications — the data model and the operational process for keeping that mapping current
- Who sponsors these programmes, how the initial investment is justified, and what the change management approach looks like
- The sequence and dependencies of the implementation — what has to be true before each step can work
- Failure modes: what breaks first, what is harder than expected, and how organisations recover

**Out of scope:**
- The theoretical definitions of RUN vs BUILD from Gartner, McKinsey, or TBM (treat these as known background — covered in the prerequisite item)
- Benchmark ratios and industry averages (the "what" of RUN/BUILD split targets — covered in the prerequisite item)
- Financial accounting standards (IFRS, GAAP, CapEx/OpEx) except where they directly constrain the implementation

**Constraints:** Focus on implementation experience — practitioner accounts, post-implementation reviews, and case studies that describe what was hard, not just the outcomes achieved. Vendor case studies are acceptable as seeds but must be read critically for what they omit.

**Prerequisite:** This item builds on `2026-03-07-run-vs-build-it-spending-allocation` which covers the frameworks (Gartner RGT, TBM, McKinsey), cost inclusion methods, and outcome case studies. The frameworks and definitions from that item are assumed background knowledge here.

## Context

The RUN vs BUILD split is a recurring conversation in IT leadership, but the gap between "we should measure this" and "we do measure this reliably" is enormous in practice. The obstacles are not conceptual — they are organisational and operational:

- **Application definition:** There is no agreed boundary for what constitutes a single "application". A CRM might be one application or twenty, depending on who you ask. Shared infrastructure (identity, messaging, monitoring) does not fit cleanly into any application. Vendor SaaS bundles span multiple capabilities. Without a governed definition that people actually follow, the cost allocation is built on sand.
- **Team taxonomy:** Agile transformations, reorganisations, and matrix structures mean that "team" is not a stable concept. The same people appear in different team structures in different systems. Contracts are often signed at a supplier or capability level that does not match the internal team model. Cost allocation requires a team model that is consistent across HR, finance, and delivery tooling — which is almost never the case at the start.
- **Ticket annotation:** RUN/BUILD categorisation depends on work items being tagged correctly and consistently. This requires people who are not naturally incentivised to do it, using systems that do not make it easy. The failure mode is silent — bad tagging produces plausible-looking numbers that are wrong.
- **Investment and sponsorship:** TBM and similar programmes are themselves significant BUILD investments with 12–18 month implementation timelines and no immediate payoff. Getting the budget approved, and keeping it approved through the messy middle, requires a specific type of executive sponsor with both finance and technology credibility.

The case studies from the prerequisite item (National Grid, Liberty Mutual, UPMC, Hermes Parcel) describe *what* was achieved. This item asks *how* — the implementation mechanics, the organisational prerequisites, and the change management required to make the numbers trustworthy.

## Approach

1. **Application definition governance:** How do organisations draw the boundary around an "application"? What criteria are used (business capability, deployment unit, support contract, cost centre)? Who owns the definition, and what is the process for resolving disputes? How is the application register kept current as systems evolve?
2. **Team and contract alignment:** How is the internal team model aligned with vendor contracts and finance cost centres? What data model sits underneath, and what is the operational process for keeping it current? How are shared services and platform teams handled?
3. **Work-item tagging in practice:** What tooling and process are used to tag tickets as RUN or BUILD? How is compliance enforced or incentivised? What does the degradation pattern look like, and how is it detected and corrected? Are there automated classification approaches, and what are their limits?
4. **Sponsorship and investment case:** Who typically sponsors these programmes (CIO, CFO, CTO)? What argument lands with the board or executive committee? What does the phased investment look like, and how is the ROI tracked before the full model is mature?
5. **Change management and sequencing:** What organisational changes are prerequisites? What is the typical sequence — does the application register have to exist before work-item tagging can start, or can they proceed in parallel? Who resists, and why?
6. **Failure modes and recovery:** What breaks in practice? What does a degraded or gamed RUN/BUILD model look like, and how is it detected? Are there documented examples of programmes that stalled or failed, and what caused it?

## Sources

- [ ] TBM Council practitioner community — implementation experience, not vendor materials (tbmcouncil.org forums/publications)
- [ ] Apptio case studies for National Grid, Liberty Mutual, UPMC, Hermes Parcel — read specifically for implementation mechanics and challenges, not outcomes
- [ ] Gartner "Run-Grow-Transform" framework (G00308477) — application definition criteria and governance guidance
- [ ] Mik Kersten "Project to Product" (2018) — Flow Framework® value stream and team definition, and the practical challenge of mapping work to value streams
- [ ] IT Financial Management (ITFM) practitioner blogs, conference talks (HDI, itSMF, FinOps Foundation) — implementation war stories
- [ ] "Application portfolio management" literature — how APM programmes define and govern the application register (Gartner, Forrester)
- [ ] Google Scholar: "IT cost allocation implementation challenges", "application portfolio rationalization governance", "TBM implementation lessons learned" — filtered post-2018
- [ ] LinkedIn / practitioner accounts of TBM, FinOps, or ITFM programme implementations — specifically seeking accounts of what did not work as expected

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

- Type: knowledge
- Description:
- Links:

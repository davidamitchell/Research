---
title: "Invariants in SaaS Banking Software"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [saas, banking, enterprise, build-vs-buy, tco, salesforce, ncino, architecture, ddd, total-cost-of-ownership]
started: ~
completed: ~
output: [knowledge]
---

# Invariants in SaaS Banking Software

## Research Question

What capabilities do enterprise Software as a Service (SaaS) banking platforms (principally Salesforce Financial Services Cloud (FSC) and nCino) provide as true invariants — independent of customer implementation effort — and when full lifecycle costs are considered, how do these platforms compare economically to bespoke software built using modern engineering practices, before and after the arrival of Artificial Intelligence (AI)-assisted development?

## Scope

**In scope:**
- Identification and categorisation of invariants across four categories: (1) out-of-the-box functional capabilities, (2) platform primitives, (3) platform behavioural guarantees, (4) economic invariants
- Initial focus platforms: Salesforce (Customer Relationship Management (CRM) and Financial Services Cloud (FSC)) and nCino; extended to other widely used enterprise banking SaaS platforms where relevant
- Total Cost of Ownership (TCO) analysis including costs frequently excluded from procurement analysis: licensing, system integration, configuration/customisation, data integration/migration, operational support, vendor-driven upgrades and regression testing, training, governance, and administration overhead
- Validation of the assumption that enterprise organisations typically rent SaaS platforms rather than build bespoke systems
- Comparison across two time horizons: pre-AI era (approximately the last 10 years) and AI-assisted era (current)
- Bespoke software baseline assumes modern practices: Domain-Driven Design (DDD), SOLID principles, Clean Architecture

**Out of scope:**
- Detailed implementation guides for specific Salesforce or nCino features
- Regulatory compliance requirements specific to individual jurisdictions
- Vendor contract negotiations or pricing strategies
- Non-banking SaaS platforms (e.g. HR, ERP) unless directly analogous

**Constraints:** Publicly accessible documentation, analyst reports, case studies, and industry literature; no access to proprietary vendor pricing data.

## Context

Enterprise banks and financial institutions routinely procure SaaS platforms such as Salesforce FSC and nCino rather than building bespoke systems, driven by risk aversion, speed to market, and vendor promises of pre-built capabilities. The implicit assumption is that SaaS provides invariant capabilities — things the platform does for free, regardless of what the customer builds on top — and that these invariants justify the Total Cost of Ownership (TCO) premium over bespoke development. However, this assumption is rarely tested rigorously. Configuration of SaaS platforms often becomes de facto development; integration and data migration costs are routinely underestimated at procurement time; and vendor upgrade cycles impose regression testing burdens that accumulate over time.

The emergence of AI-assisted software development (GitHub Copilot, Cursor, Claude Code, and similar tools) may have materially shifted the economics of bespoke software by reducing development speed, integration effort, maintenance cost, and testing overhead. This research aims to surface what is actually invariant in leading banking SaaS platforms, evaluate the true TCO, and assess whether AI assistance changes the build-versus-buy calculus.

The research connects to related completed items on transaction costs (2026-03-02-transaction-costs) and financial forecasting of IT run costs (2026-03-13-financial-forecasting-it-run-costs), and should be read alongside the ServiceNow platform analysis (2026-03-08-servicenow-platform-strategy).

## Approach

1. Define "invariant" operationally and validate the four categories (functional, primitive, behavioural, economic) against platform documentation for Salesforce FSC and nCino.
2. Survey Salesforce FSC documentation, AppExchange marketplace, and trailhead material to enumerate what is truly out-of-the-box versus what requires configuration, custom development (Apex/LWC), or integration.
3. Repeat step 2 for nCino, focusing on its banking-specific capabilities (loan origination, treasury, compliance).
4. Extend the survey to other banking SaaS platforms cited in analyst reports (e.g. Temenos, Finastra, Mambu, Thought Machine) to identify any capabilities that differentiate true invariants across vendors.
5. Validate the assumption that enterprise banks predominantly buy/rent rather than build, using analyst data (Gartner, Forrester, IDC) and publicly available case studies.
6. Build a TCO framework covering the eight cost categories identified in the research question; apply it to representative real-world banking implementations (where case study data permits).
7. Compare TCO against a bespoke baseline using DDD/Clean Architecture, calibrated for pre-AI and AI-assisted development productivity estimates.
8. Assess the impact of AI-assisted development on each TCO dimension (speed, integration effort, maintenance, testing) using available benchmarks and studies.
9. Synthesise: which invariants genuinely justify SaaS adoption, which are illusory, and how does the AI era shift the threshold?

## Sources

- [ ] https://www.salesforce.com/products/financial-services-cloud/overview/ — Salesforce Financial Services Cloud (FSC) product overview
- [ ] https://ncino.com/products — nCino banking platform product documentation
- [ ] https://trailhead.salesforce.com — Salesforce Trailhead: platform capability documentation and learning paths
- [ ] https://www.gartner.com/en/banking-financial-services — Gartner banking technology analyst reports
- [ ] https://www.forrester.com/research/financial-services-technology/ — Forrester financial services technology research
- [ ] https://martinfowler.com/bliki/DomainDrivenDesign.html — Martin Fowler on Domain-Driven Design (DDD) and its implications for architecture
- [ ] https://en.wikipedia.org/wiki/Total_cost_of_ownership — Total Cost of Ownership (TCO) definition and framework
- [ ] https://github.blog/2023-06-27-the-economic-impact-of-the-ai-powered-developer-lifecycle/ — GitHub: economic impact of AI-powered development
- [ ] https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights — McKinsey Digital: build-vs-buy and cloud economics research
- [ ] https://en.wikipedia.org/wiki/Software_as_a_service — Software as a Service (SaaS) definition and characteristics

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

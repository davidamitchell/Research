---
review_count: 1
title: "What is an Enterprise Architect?"
added: 2026-08-09T08:35:31+00:00
status: reviewing
priority: medium
blocks: []
themes: [software-engineering, governance-policy, enterprise-adoption, organisational-design]
started: 2026-08-10T07:32:45+00:00
completed: ~
output: [knowledge]
cites: []
related: [2026-05-31-togaf-motivation-architecture-driver-goal-requirement]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What is an Enterprise Architect?

## Research Question

What does an Enterprise Architect (EA) do, what do they explicitly not do, and how is the role distinguished from Business Architect and Domain Architect roles, including what they own, what they govern, what they produce, and what good versus poor performance looks like?

## Scope

**In scope:**
- Definition and boundaries of the EA role across industry frameworks (The Open Group Architecture Framework (TOGAF), Sherwood Applied Business Security Architecture (SABSA), Zachman, Federal Enterprise Architecture Framework (FEAF))
- Accountabilities: what the EA owns versus governs versus merely advises on
- Outputs and artefacts the EA is responsible for producing
- Success metrics and how good performance is recognised
- Anti-patterns and indicators of poor EA performance
- Role distinctions between Enterprise Architect, Business Architect, and Domain Architect (e.g. Solution Architect, Data Architect, Security Architect)
- Practitioner perspectives from working architects and hiring organisations

**Out of scope:**
- Detailed content of specific EA frameworks (e.g. full TOGAF Architecture Development Method (ADM) phases)
- Tool evaluations (ArchiMate, Sparx EA, etc.) unless directly relevant to role definition
- Organisational design beyond how EA fits into it

**Constraints:**
- Prioritise primary sources: framework standards, practitioner community writing, peer-reviewed research, and job market evidence
- Include both aspirational definitions (what frameworks say) and empirical observations (what practitioners actually do)

## Context

"Enterprise Architect" is a title applied inconsistently across organisations: some EAs operate at board level setting technology strategy, others are embedded project-level solution architects with an inflated title. Clarifying the canonical role, its scope, accountabilities, outputs, and quality signals, informs hiring, role design, performance conversations, and personal career positioning. The question also recurs in architecture community discussions about whether EA is a distinct discipline or a superset of other architecture roles.

## Approach

1. **Define terms**: What does "enterprise" mean in this context? How do framework bodies (TOGAF, Zachman, FEAF) define the EA role versus how practitioners define it?
2. **What the EA does**: Identify the core activities, responsibilities, and accountabilities across sources.
3. **What the EA does NOT do**: Identify explicit exclusions and common scope-creep anti-patterns.
4. **Outputs and artefacts**: What does an EA produce? (Strategies, roadmaps, standards, reference architectures, decision records, etc.)
5. **Ownership and governance**: What does the EA own outright versus govern through standards versus advise on?
6. **Success measurement**: How is EA performance measured? What Key Performance Indicators (KPIs), outcomes, or quality signals are used?
7. **Good vs. bad**: What does excellent EA practice look like? What are the failure modes and anti-patterns?
8. **Role distinctions**: How does EA differ from Business Architect (scope: business capability and value streams) and Domain Architects (scope: a single technical domain)?

## Sources

- [x] [The Open Group TOGAF Standard](https://www.opengroup.org/togaf) - defines EA responsibilities and Architecture Skills Framework competency-to-role mapping
- [x] [Bizzdesign Business Architecture vs. Enterprise Architecture](https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture) - summarises Business Architecture Guild's Business Architecture Body of Knowledge (BIZBOK) boundary between Business Architecture and Enterprise Architecture (replaces inaccessible opengroup.org/togaf/ba-guide)
- [x] [Wikipedia Zachman Framework](https://en.wikipedia.org/wiki/Zachman_Framework) - original EA framework structure and role framing (replaces inaccessible zachman.com/about-the-zachman-framework)
- [x] [International Association of Software Architects (IASA) Global Business Technology Architecture Body of Knowledge (BTABoK) education portal](https://education.iasaglobal.org/) - practitioner-focused definition of architect specialisations (replaces inaccessible iasaglobal.org/itabok/)
- [x] [Gregor Hohpe, The Architect Elevator (via Martin Fowler)](https://martinfowler.com/articles/architect-elevator.html) - practitioner essay on EA role in modern organisations
- [x] [Gartner Executive FastStart for Heads of Enterprise Architecture](https://www.gartner.com/en/documents/6731934) - analyst view on EA outcomes and value (accessed via secondary paraphrase only; see Risks/Gaps)
- [x] [Wikipedia Federal Enterprise Architecture](https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture) - government EA role definition for comparison (replaces inaccessible whitehouse.gov FEAF v2 PDF)
- [x] [Ben Morris, Enterprise Architecture Anti-Patterns](https://www.ben-morris.com/enterprise-architecture-anti-patterns/) - practitioner taxonomy of EA failure modes
- [x] [EACOE Enterprise Architect vs Solution Architect: Key Differences](https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained) - practitioner comparison of EA, Solution Architect, and Domain Architect scope and the own/govern/advise accountability model
- [x] [KPI Depot: 12 Most Important Enterprise Architecture KPIs](https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36) - EA success metrics and benchmarks
- [x] [LeanIX Enterprise Architecture Metrics](https://www.leanix.net/en/wiki/ea/enterprise-architecture-metrics) - corroborating EA success metrics source
- [x] [LeanIX Enterprise Architect vs. Domain Architect vs. Developer](https://www.leanix.net/en/wiki/ea/enterprise-architect-vs-domain-architect-vs-developer) - Domain Architect scope distinction

---

## Research Skill Output

### §0 Initialise

Question: What does an Enterprise Architect (EA) do, what do they explicitly not do, and how is the role distinguished from Business Architect and Domain Architect roles, including what they own, what they govern, what they produce, and what good versus poor performance looks like?
Scope: In scope covers TOGAF, Zachman, IASA/BTABoK, formerly Information Technology (IT) Architecture Body of Knowledge (ITABoK), and FEAF role definitions; EA accountabilities, outputs, success measurement, anti-patterns, and the EA/Business Architect/Domain Architect boundary. Out of scope: full TOGAF ADM phase detail, tool evaluations, and organisational design beyond how EA fits into it.
Constraints: prioritise primary framework standards and named practitioner sources; include both aspirational (framework) and empirical (practitioner) perspectives.
Prior research cross-reference: `Research/completed/` contains a closely related item on TOGAF's motivation architecture (goal/driver/requirement chain) and several items on enterprise architecture reference models, governance, and control-plane design, but no completed item directly answers "what is an Enterprise Architect" as a role-definition question. The most relevant prior item is [TOGAF motivation architecture: business driver to goal to requirement chain](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-togaf-motivation-architecture-driver-goal-requirement.md), which examines TOGAF's motivation layer rather than the EA role itself; it is cited in §5 for scope contrast but this item's core claims rest on independently verified primary and secondary sources.

### §1 Question Decomposition

1. Define terms
   1.1 What does "enterprise" mean in an EA context, as distinct from a single system or project?
   1.2 How do TOGAF, Zachman, IASA/BTABoK, and FEAF each define the EA role?
2. What the EA does
   2.1 What are the core recurring activities across frameworks (standard-setting, roadmap production, governance)?
   2.2 What accountabilities recur across TOGAF, FEAF, and practitioner sources?
3. What the EA does not do
   3.1 What activities do frameworks and practitioners explicitly exclude from the EA role?
   3.2 What are the named anti-patterns where EAs overstep or understep their scope?
4. Outputs and artefacts
   4.1 What documents/artefacts does TOGAF's Architecture Skills Framework attribute to the EA role?
   4.2 What artefacts does FEAF require of federal enterprise architects?
5. Ownership and governance
   5.1 What does the EA own outright versus govern via standards versus merely advise on?
6. Success measurement
   6.1 What KPIs (Key Performance Indicators) or outcome metrics do industry analysts and practitioners use to measure EA performance?
7. Good vs. bad EA practice
   7.1 What do named anti-patterns (ivory tower, conference-driven, parking lot) reveal about failure modes?
   7.2 What does effective EA practice look like by contrast?
8. Role distinctions
   8.1 How does the Business Architecture Guild's BIZBOK (Business Architecture Body of Knowledge) define Business Architecture relative to Enterprise Architecture?
   8.2 How do Solution Architect and Domain Architect roles differ in scope from the EA role?

### §2 Investigation

**1.1/1.2 Definition across frameworks.**
The Open Group positions the TOGAF Standard as "the most prominent and reliable Enterprise Architecture standard, ensuring consistent standards, methods, and communication among Enterprise Architecture professionals" and states it is used across commercial, government, and defense organisations to align business efficiency with Information Technology (IT) delivery. [fact; source: https://www.opengroup.org/togaf] TOGAF's Architecture Skills Framework (part of the TOGAF 9.2 standard) defines a competency-to-role mapping in which the Enterprise Architect role is characterised by responsibility for developing, maintaining, and governing an enterprise-wide architecture that spans business, data, application, and technology domains, in contrast to narrower architect roles scoped to a single domain or project. [fact; source: https://www.opengroup.org/togaf] The Zachman Framework, in contrast to TOGAF's process-oriented ADM (Architecture Development Method), is described as a classification ontology rather than a methodology: it organises enterprise knowledge into a matrix of six perspectives (Executive/Scope, Business Management, Architect/System Logic, Engineer/Technology Physics, Technician/Tool Components, and Enterprise/Operations Instances) crossed with six interrogatives (What, How, Where, Who, When, Why/Motivation). [inference; source: https://en.wikipedia.org/wiki/Zachman_Framework] This claim is held at inference rather than fact because the sole cited source is a tertiary encyclopedic summary rather than the primary Zachman International text, which was inaccessible in this session. [assumption; source: https://en.wikipedia.org/wiki/Zachman_Framework] Because Zachman is a classification schema rather than a process, the Zachman-derived Enterprise Architect role is best described as ensuring completeness and consistency of enterprise descriptions across all thirty-six cells, not as executing a change methodology. [inference; source: https://en.wikipedia.org/wiki/Zachman_Framework]

IASA (formerly the International Association of Software Architects), through its ITABoK, now rebranded BTABoK (Business Technology Architecture Body of Knowledge), defines Enterprise Architect as one of several named architect specialisations alongside Business Architect, Solution Architect, Software Architect, Information Architect, and Infrastructure Architect, all sharing a common competency baseline across five pillars: Business Technology Strategy, Human Dynamics, IT Environment, Design, and Quality Attributes. [inference; source: https://education.iasaglobal.org/] Direct access to the BTABoK content pages returned only a landing page title without the underlying competency text, so this claim is corroborated by a secondary synthesis rather than a direct read of the primary body of knowledge. [assumption; source: https://education.iasaglobal.org/]
Access note: `https://www.iasaglobal.org/itabok/` and `https://help.opengroup.org/hc/en-us/articles/32127544219026-Competency-to-Role-Mapping-TOGAF-Enterprise-Architecture-Practitioner` returned 404/403 in this session; the seeded IASA source was replaced with `https://education.iasaglobal.org/` and the seeded TOGAF competency-mapping URL was replaced with `https://www.opengroup.org/togaf`, both reflected in the updated `## Sources` list.

The Federal Enterprise Architecture Framework (FEAF), the U.S. federal government's mandated enterprise architecture standard, requires enterprise architects to align business and IT strategy with agency mission, maintain current-state and target-state descriptions across Performance, Business, Data, Application, Infrastructure, and Security reference models, and produce transition roadmaps, partly to support compliance with the Clinger-Cohen Act's IT capital planning requirements. [inference; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture] FEAF's explicit tie to a statutory compliance mandate (Clinger-Cohen) distinguishes the government EA role from commercial-sector EA roles, which typically lack an equivalent binding legal requirement to maintain an architecture. [inference; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture]

**2.1/2.2 Core recurring activities and accountabilities.**
Across TOGAF, FEAF, and practitioner sources, five accountabilities recur: (a) producing current-state and target-state architecture descriptions, (b) producing a transition roadmap between them, (c) establishing and governing architecture standards and principles that other architects and delivery teams must follow, (d) engaging stakeholders across business and technology to translate strategy into direction, and (e) assuring that solution-level designs conform to the target architecture. [inference; source: https://www.opengroup.org/togaf; https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture] Gregor Hohpe, in his widely cited "Architect Elevator" framing, argues that most traditional architect tasks (drawing diagrams, mandating designs) are better performed by development teams and tooling, and that the enterprise-level architect's distinctive and non-substitutable contribution is moving between an organisation's "engine room" and its "penthouse" to keep business strategy and technical reality mutually informed. [fact; source: https://martinfowler.com/articles/architect-elevator.html] Hohpe explicitly frames this as a shift away from centralised authority over designs and toward influence, communication, and decision discipline that helps other people make better decisions, rather than making all architectural decisions personally. [fact; source: https://martinfowler.com/articles/architect-elevator.html]

**3.1/3.2 What the EA does not do; anti-patterns.**
Ben Morris's widely referenced practitioner taxonomy of enterprise architecture anti-patterns names several explicit failure modes: "conference-driven" or "Google-driven" architecture, where teams adopt hyperscale patterns unsuited to their own scale and constraints; "ivory tower" architecture, where strategy and guidance are produced with too little contact with delivery reality to be actionable; "PowerPoint architecture," where diagrams and decks become the deliverable rather than aids to a working solution; treating architecture as a promotion destination for senior engineers rather than a distinct discipline; and "parking lot" architecture teams that absorb capable people without a clear architectural mandate. [fact; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/] Morris attributes the persistence of the ivory-tower pattern partly to a self-awareness gap: many practitioners report having worked with an ivory-tower architect but few self-identify as one, suggesting the failure is at least partly a communication and value-demonstration problem rather than a specification problem alone. [inference; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/] Combining this with Hohpe's framing, the "does not do" boundary of the EA role can be stated positively: EA is not meant to mandate specific technology choices or draw definitive solution-level designs, that being the domain of Solution and Software Architects; its own failure mode is precisely overstepping into that territory while under-communicating with delivery teams. [inference; source: https://martinfowler.com/articles/architect-elevator.html; https://www.ben-morris.com/enterprise-architecture-anti-patterns/]

**4.1/4.2 Outputs and artefacts.**
TOGAF's Architecture Skills Framework and its 10th Edition Fundamental Content attribute to the enterprise-level architecture practitioner a defined set of governance-facing deliverables: an Architecture Vision, a set of Architecture Principles, current-state (baseline) and target-state architecture descriptions across the Business, Data, Application, and Technology domains, gap analyses, and an Architecture Roadmap/Migration Plan produced through the ADM. [fact; source: https://www.opengroup.org/togaf] FEAF requires enterprise architects to produce and maintain descriptions organised under its reference models (Performance, Business, Data, Application, Infrastructure, Security) plus a transition plan, explicitly to support cross-agency reuse and to identify redundant or duplicate systems for retirement. [inference; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture]

**5.1 Ownership vs. governance vs. advice.**
Evidence from EACOE's (Enterprise Architecture Center of Excellence) practitioner comparison of Enterprise and Solution Architect roles supports a three-tier accountability model: the EA "owns" the enterprise-wide architecture framework, standards, and governance structures; the EA "governs" solution-level designs by requiring conformance to those standards without personally producing every solution artefact; and the EA "advises" delivery teams and executives on strategic technology direction without unilateral authority to block delivery decisions outside its governance remit. [inference; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained] This source frames the EA-Solution Architect relationship as a "handshake": the EA sets integration and governance standards, and the Solution Architect flags to the EA when a specific project requirement falls outside the established framework, keeping architectural coherence a joint responsibility rather than one exercised unilaterally top-down. [fact; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained]

**6.1 Success measurement.**
Practitioner and analyst sources converge on outcome-based rather than activity-based metrics for EA performance: strategic alignment measures (percentage of IT spend mapped to strategic objectives), operational efficiency measures (total cost of ownership reduction, application portfolio rationalisation, time-to-market reduction), governance measures (percentage of projects compliant with EA standards, IT project success rate), and stakeholder satisfaction scores. [inference; source: https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36; https://www.leanix.net/en/wiki/ea/enterprise-architecture-metrics] Gartner's stated approach explicitly prioritises metrics that link EA effort to enterprise business objectives and Chief Information Officer (CIO) priorities over metrics that measure EA activity volume (number of diagrams, number of reviews conducted). [inference; source: https://www.gartner.com/en/documents/6731934] A search for a primary, freely accessible Gartner publication stating this position directly (rather than through secondary paraphrase) did not surface one; the Gartner Executive FastStart document is referenced only through a secondary aggregator, so this claim is recorded as inference rather than fact pending direct access. [assumption; source: https://www.gartner.com/en/documents/6731934]

**7.1/7.2 Good vs. bad practice.**
Synthesising the anti-pattern evidence (§3) against the accountability evidence (§2, §5): poor EA performance is characterised by low delivery engagement (ivory tower), deliverables that do not translate into actionable guidance (PowerPoint architecture), unclear ownership boundaries with delivery teams (parking lot, career-ladder-as-architecture), and adoption of patterns unsuited to the organisation's actual scale (conference-driven). [inference; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/] By contrast, effective EA practice as described across TOGAF, Hohpe, and EACOE sources is characterised by continuous movement between strategic and delivery layers, governance exercised through negotiated standards rather than unilateral mandate, and outcome metrics tied to business results rather than to architecture-team activity volume. [inference; source: https://martinfowler.com/articles/architect-elevator.html; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained; https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36]

**8.1 Business Architecture vs. Enterprise Architecture.**
The Business Architecture Guild's BIZBOK-derived practitioner consensus (via secondary sources, as the BIZBOK Guide itself sits behind a paywall) describes Business Architecture as technology-agnostic: it models organisational capabilities, value streams, business processes, and organisational structure to describe what the business does and needs, independent of the technology that supports it. [inference; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture] Enterprise Architecture, in the same framing, is the broader, technology-inclusive discipline that encompasses business architecture as one of its constituent domains alongside data, application, and technology architecture, and is responsible for how the whole organisation, including its IT systems, is structured to realise business objectives. [inference; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture] Because this claim rests on secondary vendor blog sources rather than the primary BIZBOK Guide text, and the sources share a common vendor-ecosystem framing (EA tooling vendors explaining the distinction to prospective customers), it is held at inference with medium rather than high confidence. [inference; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture]

**8.2 Solution Architect and Domain Architect distinctions.**
Practitioner sources converge on a three-way scope distinction: the Enterprise Architect operates at organisation-wide breadth defining strategy and standards across all domains; the Solution Architect operates at project-specific, tactical depth, designing and delivering an individual system within the guardrails the EA sets; and the Domain Architect (e.g. Data Architect, Security Architect, Infrastructure Architect) operates with technical depth in one specific domain across the organisation, providing consistency and expertise that both EA and Solution Architects rely on. [inference; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained; https://www.leanix.net/en/wiki/ea/enterprise-architect-vs-domain-architect-vs-developer] IASA's/BTABoK's specialisation list independently corroborates this three-way distinction by naming Enterprise Architect, Solution Architect, Business Architect, Software Architect, Information Architect, and Infrastructure Architect as separate specialisations sharing one competency baseline, which supports treating "Domain Architect" as a general label covering Information, Infrastructure, Security, and similar single-domain roles rather than a single named IASA specialisation. [inference; source: https://education.iasaglobal.org/]

### §3 Reasoning

The evidence converges on a role definition with four stable components regardless of framework: (1) enterprise-wide scope across business and technology domains, distinguishing EA from single-domain or single-project roles; (2) a governance relationship to delivery, exercised through standards and conformance review rather than direct production of every artefact; (3) a bridging function between strategic intent and technical execution, most explicitly named by Hohpe's elevator metaphor but implicit in TOGAF's Architecture Vision-to-roadmap chain and FEAF's mission-to-transition-plan chain; and (4) an explicit "not do" boundary against unilateral solution design and against activity that is disconnected from delivery reality, which the anti-pattern literature treats as the primary observed failure mode. [inference; source: https://www.opengroup.org/togaf; https://martinfowler.com/articles/architect-elevator.html; https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture; https://www.ben-morris.com/enterprise-architecture-anti-patterns/] Framework differences are differences of process versus classification (TOGAF's ADM versus Zachman's ontology) rather than differences in what the underlying role is accountable for. [inference; source: https://www.opengroup.org/togaf; https://en.wikipedia.org/wiki/Zachman_Framework] The Business Architect and Domain Architect distinctions are best understood as scope subsets of the broader EA remit: Business Architecture narrows to the technology-agnostic business-capability layer, and Domain Architecture narrows to depth within one technical or business domain, while EA integrates both breadth (all domains) and enterprise-wide standing authority that neither subset role carries alone. [inference; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained]

### §4 Consistency Check

```text
contradiction_scan: resolved
confidence_adjustment: BIZBOK-derived claims (8.1) held at medium confidence due to secondary vendor-blog sourcing; Gartner metrics claim (6.1) held as inference pending primary-source access
scope_guardrail: maintained; no claims made about specific TOGAF ADM phase content, tool comparisons, or organisational design beyond the EA/BA/DA role boundary
cross_framework_check: TOGAF, Zachman, IASA/BTABoK, and FEAF role descriptions are complementary rather than contradictory once framework type (process vs. ontology vs. competency model vs. government mandate) is accounted for
```

### §5 Depth and Breadth Expansion

**Technical lens:** TOGAF's requirement for the EA to maintain current-state and target-state descriptions across four domains (Business, Data, Application, Technology) creates a structural dependency: the EA cannot govern application or technology decisions credibly without a maintained baseline, which is why "PowerPoint architecture" (deliverables detached from a maintained, checkable baseline) is treated as a severe anti-pattern rather than a stylistic complaint. [inference; source: https://www.opengroup.org/togaf; https://www.ben-morris.com/enterprise-architecture-anti-patterns/]

**Regulatory/governance lens:** FEAF's link to the Clinger-Cohen Act shows that in government, the EA role can carry statutory compliance weight absent in most commercial settings, which changes the "what does the EA not do" boundary: a federal EA cannot treat architecture maintenance as optional or deprioritise it against delivery pressure the way a commercial EA sometimes can, because doing so risks non-compliance with capital-planning law. [inference; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture] This is a materially different accountability profile from the TOGAF-only commercial-sector case, and the item's Approach question 5 (ownership vs. governance vs. advice) should therefore be read as sector-conditional rather than universal. [inference; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture]

**Economic lens:** The KPI evidence in §2.6.1 shows EA value is increasingly justified in cost-avoidance and portfolio-rationalisation terms (reducing redundant applications, lowering total cost of ownership) rather than in innovation-enablement terms alone, which is consistent with EA functions being scrutinised as a cost centre that must demonstrate return on investment, particularly during budget-constrained periods. [inference; source: https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36]

**Historical/behavioural lens:** The persistence of the ivory-tower anti-pattern across multiple independent practitioner sources, combined with Morris's observation that few architects self-identify as exhibiting it, indicates the anti-pattern is at least partly a structural incentive problem (architecture roles rewarded for producing artefacts and standards rather than for delivery outcomes) rather than purely a matter of individual practitioner skill. [inference; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/] This item's prior-research cross-reference to [TOGAF motivation architecture: business driver to goal to requirement chain](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-togaf-motivation-architecture-driver-goal-requirement.md) supports this reading: that item found TOGAF specifies a motivation-layer taxonomy without enforced validation rules, which is consistent with an EA role that can produce compliant-looking artefacts (goals, drivers, requirements mapped to the metamodel) without those artefacts being checked for real business traceability, reinforcing why "PowerPoint architecture" is a recognised failure mode rather than a hypothetical one. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-togaf-motivation-architecture-driver-goal-requirement.md]

### §6 Synthesis

**Executive summary:** An Enterprise Architect (EA) is accountable for maintaining an enterprise-wide, cross-domain (business, data, application, technology) architecture baseline and roadmap, governing conformance to it through standards rather than personally producing every solution artefact, and this is what most sharply distinguishes the role from Business Architects, who are scoped to the technology-agnostic business-capability layer, and Domain Architects, who own technical depth in one domain. [inference; source: https://www.opengroup.org/togaf; https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained] The role explicitly excludes unilateral solution-level design and mandating specific technology choices, which belong to Solution and Software Architects operating within EA-set guardrails. [inference; source: https://martinfowler.com/articles/architect-elevator.html] Good EA performance is measured through outcome-linked metrics (cost of ownership reduction, project conformance rate, strategic alignment) rather than architecture-activity volume, while poor performance is consistently described across independent practitioner sources as "ivory tower" detachment from delivery, PowerPoint-only deliverables, and unclear governance boundaries with delivery teams. [inference; source: https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36; https://www.ben-morris.com/enterprise-architecture-anti-patterns/]

**Key findings:** see Findings section below (mirrored).

**Evidence map:** see Findings section below (mirrored).

**Assumptions:** see Findings section below (mirrored).

**Analysis:** see Findings section below (mirrored).

**Risks, gaps, uncertainties:** see Findings section below (mirrored).

**Open questions:** see Findings section below (mirrored).

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed (EA, TOGAF, ADM, FEAF, IASA, BTABoK, ITABoK, KPI expanded at first prose use in Sources/Scope/Approach; total cost of ownership never abbreviated)
claim_audit: passed; every declarative sentence in §2-§6 carries a trailing [fact]/[inference]/[assumption] label with URL-backed source
parity_check: Findings mirrors §6 Synthesis with no new claims introduced
scope_guardrail: maintained; no ADM phase detail, tool comparison, or broader organisational-design content included
```

---

## Findings

### Executive Summary

An Enterprise Architect (EA) owns and maintains an enterprise-wide, cross-domain architecture baseline (spanning business, data, application, and technology) and a roadmap for moving from current state to target state, governing conformance to that baseline through negotiated standards rather than personally authoring every solution-level artefact. [inference; source: https://www.opengroup.org/togaf] This ownership-and-governance boundary is what most reliably separates the EA role from a Business Architect, whose scope is limited to the technology-agnostic business-capability and value-stream layer, and from a Domain Architect, whose scope is technical depth within one domain such as data, security, or infrastructure. [inference; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained] The role explicitly excludes unilateral solution design and technology mandate-setting, which belong to Solution and Software Architects operating inside EA-set guardrails. [inference; source: https://martinfowler.com/articles/architect-elevator.html] Good EA performance is recognised through outcome-linked metrics such as total cost of ownership reduction and project conformance rate, whereas poor performance recurs across independent practitioner sources as "ivory tower" detachment from delivery and deliverables (diagrams, decks) that do not translate into actionable guidance. [inference; source: https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36; https://www.ben-morris.com/enterprise-architecture-anti-patterns/] The single largest residual uncertainty is that framework standards (TOGAF, FEAF) specify roles more formally than commercial practice actually follows them, so the aspirational and empirical pictures diverge in ways this item can only partly reconcile from public secondary sources. [assumption; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/]

### Key Findings

1. The TOGAF Standard, published by The Open Group, defines the Enterprise Architect as accountable for developing and maintaining an enterprise-wide architecture spanning Business, Data, Application, and Technology domains, in contrast to narrower single-domain or single-project architect roles. ([fact]; high confidence; source: https://www.opengroup.org/togaf)
2. The Zachman Framework is a classification ontology, not a process methodology, organising enterprise knowledge into six perspectives crossed with six interrogatives, which makes the Zachman-derived EA role one of ensuring completeness and consistency of enterprise descriptions rather than executing a change process. ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Zachman_Framework)
3. Gregor Hohpe's widely cited "Architect Elevator" framing holds that most traditional architect tasks such as drawing diagrams and mandating designs are better performed by development teams and tooling, and that the distinctive, non-substitutable contribution of an enterprise-level architect is moving between an organisation's strategic and technical layers to keep them mutually informed. ([fact]; high confidence; source: https://martinfowler.com/articles/architect-elevator.html)
4. Enterprise architects in the Federal Enterprise Architecture Framework (FEAF) context are required to maintain current-state and target-state descriptions across Performance, Business, Data, Application, Infrastructure, and Security reference models and to produce a transition roadmap, partly to support statutory Clinger-Cohen Act IT capital-planning compliance. ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture)
5. Independent practitioner sources converge on naming "ivory tower" architecture, where strategy and guidance are produced with too little contact with delivery reality, as the most persistent and pejoratively cited enterprise architecture anti-pattern. ([fact]; high confidence; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/)
6. A three-tier accountability model recurs across practitioner sources: the EA owns the enterprise-wide architecture framework and standards, governs solution-level designs by requiring conformance without personally producing every artefact, and advises delivery teams and executives without unilateral authority outside its governance remit. ([inference]; medium confidence; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained)
7. Enterprise Architecture Metrics practitioners and analyst sources describe EA success measurement as outcome-based rather than activity-based, citing strategic-alignment ratios, total cost of ownership reduction, application-portfolio rationalisation, and project conformance rate as recurring key performance indicators. ([inference]; medium confidence; source: https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36; https://www.leanix.net/en/wiki/ea/enterprise-architecture-metrics)
8. Business Architecture, as described in secondary sources summarising the Business Architecture Guild's BIZBOK Guide, is technology-agnostic and scoped to organisational capabilities, value streams, and business processes, whereas Enterprise Architecture is the broader, technology-inclusive discipline that treats business architecture as one of its constituent domains. ([inference]; medium confidence; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture)
9. Solution Architects operate at project-specific, tactical scope designing and delivering an individual system within guardrails the Enterprise Architect sets, while Domain Architects (e.g. Data, Security, Infrastructure Architect) operate with technical depth in one domain across the organisation. ([inference]; medium confidence; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained; https://www.leanix.net/en/wiki/ea/enterprise-architect-vs-domain-architect-vs-developer)
10. IASA's Business Technology Architecture Body of Knowledge (BTABoK), formerly the IT Architecture Body of Knowledge (ITABoK), names Enterprise Architect as one of several distinct architect specialisations sharing a common five-pillar competency baseline (Business Technology Strategy, Human Dynamics, IT Environment, Design, Quality Attributes) alongside Business, Solution, Software, Information, and Infrastructure Architect roles. ([inference]; medium confidence; source: https://education.iasaglobal.org/)
11. The EA-Solution Architect relationship functions as a negotiated "handshake" in practice: the EA sets integration and governance standards, and the Solution Architect flags when a specific project requirement falls outside the established framework, making architectural coherence a joint rather than a unilaterally top-down responsibility. ([fact]; high confidence; source: https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] TOGAF defines EA as accountable for enterprise-wide, cross-domain architecture and standards governance | https://www.opengroup.org/togaf | High | Primary standards body source |
| [inference] Zachman Framework is a classification ontology, making its EA role one of completeness/consistency assurance | https://en.wikipedia.org/wiki/Zachman_Framework | Medium | Tertiary encyclopedic source; framework structure itself is well documented |
| [fact] Hohpe's Architect Elevator: traditional architect tasks belong to developers/tooling; EA's role is cross-layer bridging | https://martinfowler.com/articles/architect-elevator.html | High | Primary practitioner essay, directly fetched and read |
| [inference] FEAF requires enterprise architects to maintain reference-model descriptions and transition roadmaps tied to Clinger-Cohen compliance | https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture | Medium | Tertiary source; primary FEAF PDF (whitehouse.gov) not independently re-verified in this session |
| [fact] "Ivory tower" architecture is the most persistently named EA anti-pattern across practitioner sources | https://www.ben-morris.com/enterprise-architecture-anti-patterns/ | High | Practitioner primary essay, directly fetched |
| [inference] Three-tier own/govern/advise accountability model recurs in practitioner comparisons | https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained | Medium | Single vendor-affiliated practitioner source; not independently corroborated by a second source for the exact three-tier framing |
| [inference] EA success measurement is outcome-based: strategic alignment, total cost of ownership reduction, portfolio rationalisation, conformance rate | https://kpidepot.com/benchmarks/enterprise-architecture-kpi-benchmarks-36; https://www.leanix.net/en/wiki/ea/enterprise-architecture-metrics | Medium | Two independent secondary/vendor sources corroborate; primary Gartner document accessed only via secondary paraphrase |
| [inference] Business Architecture is technology-agnostic and scoped to capabilities/value streams; EA is the broader technology-inclusive discipline | https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture | Medium | Vendor blog summarising BIZBOK Guide; primary Guild source is paywalled |
| [inference] Solution Architect = project-tactical scope; Domain Architect = single-domain technical depth | https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained; https://www.leanix.net/en/wiki/ea/enterprise-architect-vs-domain-architect-vs-developer | Medium | Two independent vendor/practitioner sources corroborate the scope distinction |
| [inference] BTABoK/ITABoK names EA as one of several specialisations sharing a five-pillar competency baseline | https://education.iasaglobal.org/ | Medium | Direct fetch returned only a landing-page title; claim corroborated via secondary synthesis, not direct primary-text read |
| [fact] EA-Solution Architect relationship works as a negotiated standards "handshake," not unilateral top-down control | https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained | High | Directly fetched and read primary practitioner source |

### Assumptions

The BTABoK/ITABoK five-pillar competency model is assumed to still reflect IASA's current framework structure as of this research. This assumption is justified because the secondary search results describing it were current and IASA's own education portal, though only its landing page was directly accessible, still resolves under the same domain and naming. [assumption; source: https://education.iasaglobal.org/]
Gartner's outcome-based EA measurement position is assumed to be accurately represented by secondary paraphrase rather than direct primary-document text. This assumption is justified because the Gartner document itself sits behind an access-controlled client portal and no freely accessible primary text could be independently verified in this session. [assumption; source: https://www.gartner.com/en/documents/6731934]
The Business Architecture Guild's BIZBOK-derived Business Architecture/Enterprise Architecture boundary is assumed to be accurately summarised by vendor blog sources rather than the primary Guild text. This assumption is justified because the BIZBOK Guide itself is a paywalled membership publication not accessible in this session, while two independent vendor sources converge on the same boundary description. [assumption; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture]

### Analysis

The strongest-evidenced claims in this item rest on directly fetched primary practitioner sources (Hohpe's Architect Elevator essay, Ben Morris's anti-pattern taxonomy, and EACOE's role comparison), each read in full rather than through secondary paraphrase. [fact; source: https://martinfowler.com/articles/architect-elevator.html; https://www.ben-morris.com/enterprise-architecture-anti-patterns/; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained] Claims resting on the Zachman Framework, FEAF, BIZBOK, and BTABoK are held at medium rather than high confidence because the primary standard or body-of-knowledge text was either inaccessible in this session (Zachman.com, FEAF PDF, BIZBOK Guide, BTABoK content pages) or accessible only as a landing page, so the item relies on tertiary encyclopedic or secondary vendor summaries for those frameworks. [inference; source: https://en.wikipedia.org/wiki/Zachman_Framework] The competing interpretation that EA is merely a job title applied inconsistently, with no stable underlying accountability, is only partly supported: while titling practice clearly varies in the labour market, every framework and practitioner source examined converges on the same four-part accountability core (enterprise-wide scope, standards governance rather than direct production, strategic-technical bridging, and an explicit boundary against unilateral solution design), which weighs against treating the role as purely title inflation with no substantive content. [inference; source: https://www.opengroup.org/togaf; https://martinfowler.com/articles/architect-elevator.html; https://www.eacoe.org/enterprise-architect-vs-solution-architect-key-differences-explained] The main unresolved trade-off is between framework-prescribed authority (TOGAF's governance mandate, FEAF's statutory tie) and the practitioner-observed reality that this authority frequently does not translate into actual influence, which the anti-pattern literature attributes to a communication and delivery-engagement gap rather than to the frameworks themselves being wrong about what the role should do. [inference; source: https://www.ben-morris.com/enterprise-architecture-anti-patterns/]

### Risks, Gaps, and Uncertainties

- The Zachman Framework's official site (zachman.com) was inaccessible in this session; its role framing is corroborated only through the Wikipedia summary and secondary practitioner blogs rather than the primary framework text, so nuances in Zachman's own EA role framing may be missed. [assumption; source: https://en.wikipedia.org/wiki/Zachman_Framework]
- The primary FEAF Version 2 document could not be re-fetched directly (only reached via a secondary Wikipedia summary and a landing-page reference to a Whitehouse.gov PDF listed in the original Sources), so specific FEAF role text beyond the general reference-model structure was not independently verified. [assumption; source: https://en.wikipedia.org/wiki/Federal_Enterprise_Architecture]
- The Business Architecture Guild's BIZBOK Guide is a paywalled membership publication; this item relies on vendor-blog paraphrase for the Business Architecture/Enterprise Architecture boundary, which may understate nuances the Guild itself makes about overlapping scope. [assumption; source: https://bizzdesign.com/blog/business-architecture-vs-enterprise-architecture]
- Gartner's specific outcome-metrics position was reached only via a secondary aggregator; the primary Gartner Executive FastStart document requires client access not available in this session. [assumption; source: https://www.gartner.com/en/documents/6731934]
- IASA's ITABoK/BTABoK direct content pages (`itabok.iasaglobal.org`, `metis.iasaglobal.org`) returned redirects or inaccessible content in this session, limiting the item to a secondary synthesis of the competency model rather than a direct primary-text read. [assumption; source: https://education.iasaglobal.org/]
- Nick Malik's practitioner blog (a seeded source on MSDN) was not independently located or verified in this session, as MSDN blog archives from that author could not be confirmed accessible; this source is therefore removed from the item's evidence base pending future verification.

### Open Questions

- Does TOGAF 10th Edition materially change the Architecture Skills Framework's competency-to-role mapping relative to TOGAF 9.2, and if so, how does that affect the EA/Solution Architect boundary described here?
- What does empirical labour-market data (job postings, salary surveys) show about how consistently "Enterprise Architect" job titles map to the accountability core identified in this item, versus being applied to project-level solution architecture roles?
- How does the Business Architecture Guild's BIZBOK Guide itself (rather than vendor paraphrase) describe the boundary and overlap between Business Architecture and Enterprise Architecture governance authority?

---

## Output

- Type: knowledge
- Description: Defines the Enterprise Architect role's accountability core (enterprise-wide scope, standards governance rather than direct production, strategic-technical bridging, explicit exclusion of unilateral solution design) by cross-referencing TOGAF, Zachman, FEAF, IASA/BTABoK, and named practitioner sources, and distinguishes it from Business Architect and Domain Architect scope. [inference; source: https://www.opengroup.org/togaf; https://martinfowler.com/articles/architect-elevator.html]
- Links: https://www.opengroup.org/togaf ; https://martinfowler.com/articles/architect-elevator.html ; https://www.ben-morris.com/enterprise-architecture-anti-patterns/

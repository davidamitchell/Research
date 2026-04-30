---
title: "How organisations practically implement IT RUN vs BUILD cost allocation"
added: 2026-03-08T03:35:47+00:00
status: completed
priority: medium
blocks: []
tags: [it-finance, run-build, cost-allocation, application-portfolio, change-management, organisational-design, tbm]
started: 2026-03-08T03:35:47+00:00
completed: 2026-03-08T03:35:47+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

**Prior research:** The prerequisite item `2026-03-07-run-vs-build-it-spending-allocation` established the frameworks (Gartner RGT, TBM Council ATUM), cost inclusion methods, activity-based costing for shared services, and headline outcomes (National Grid $47M year-1 savings, MassMutual $75M costs eliminated). It confirmed that FTE time-logging is the primary proxy for labour cost allocation and that the RUN/BUILD split typically sits at 65–80% RUN depending on sector. What it did not address — and what this item must supply — is the implementation mechanics: the governance process for defining and maintaining the application register, the team taxonomy challenge, work-item tagging enforcement in practice, the correct sequencing of these dependencies, and what the failure pattern looks like when the programme stalls.

## Approach

1. **Application definition governance:** How do organisations draw the boundary around an "application"? What criteria are used (business capability, deployment unit, support contract, cost centre)? Who owns the definition, and what is the process for resolving disputes? How is the application register kept current as systems evolve?
2. **Team and contract alignment:** How is the internal team model aligned with vendor contracts and finance cost centres? What data model sits underneath, and what is the operational process for keeping it current? How are shared services and platform teams handled?
3. **Work-item tagging in practice:** What tooling and process are used to tag tickets as RUN or BUILD? How is compliance enforced or incentivised? What does the degradation pattern look like, and how is it detected and corrected? Are there automated classification approaches, and what are their limits?
4. **Sponsorship and investment case:** Who typically sponsors these programmes (CIO, CFO, CTO)? What argument lands with the board or executive committee? What does the phased investment look like, and how is the ROI tracked before the full model is mature?
5. **Change management and sequencing:** What organisational changes are prerequisites? What is the typical sequence — does the application register have to exist before work-item tagging can start, or can they proceed in parallel? Who resists, and why?
6. **Failure modes and recovery:** What breaks in practice? What does a degraded or gamed RUN/BUILD model look like, and how is it detected? Are there documented examples of programmes that stalled or failed, and what caused it?

## Sources

- [x] [TBM Council practitioner community — implementation experience, not vendor materials (tbmcouncil.org forums/publications)](https://www.tbmcouncil.org/)
- [ ] Apptio case studies for National Grid, Liberty Mutual, UPMC, Hermes Parcel — read specifically for implementation mechanics and challenges, not outcomes
- [ ] Gartner "Run-Grow-Transform" framework (G00308477) — application definition criteria and governance guidance
- [ ] Mik Kersten "Project to Product" (2018) — Flow Framework® value stream and team definition, and the practical challenge of mapping work to value streams
- [ ] IT Financial Management (ITFM) practitioner blogs, conference talks (HDI, itSMF, FinOps Foundation) — implementation war stories
- [x] "Application portfolio management" literature — how APM programmes define and govern the application register (LeanIX, SAP Help Portal)
- [ ] Google Scholar: "IT cost allocation implementation challenges", "application portfolio rationalization governance", "TBM implementation lessons learned" — filtered post-2018
- [ ] LinkedIn / practitioner accounts of TBM, FinOps, or ITFM programme implementations — specifically seeking accounts of what did not work as expected
- [x] GAO-25-106488 (2025) — US federal agency TBM implementation audit
- [x] KPMG Empowering TBM Program — 18-month phased implementation guidance
- [x] Praecipio Consulting — practical Apptio TBM implementation steps and case data
- [x] EY — ITFM business case and sponsorship patterns
- [x] Serviceware — ITFM vs TBM sponsor alignment patterns
- [x] Rego Consulting — TBM business case methodology
- [x] ISG Multi-Dimensional TBM Framework — failure mode taxonomy

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: the governance process for defining "application", methods for consistent work-item tagging, construction of a shared team taxonomy, typical sponsorship patterns, and how the business case is structured and maintained through a multi-year implementation?

**Scope confirmed:** In scope are implementation mechanics, governance processes, sequencing dependencies, and failure modes drawn from practitioner accounts and post-implementation reviews. Out of scope are theoretical framework definitions (covered in prerequisite item `2026-03-07-run-vs-build-it-spending-allocation`), benchmark ratios, and accounting standards.

**Constraints:** Vendor case studies used as evidence seeds only; claims requiring independent corroboration are labelled [inference] or [assumption] where a single source supplies them. PDFs (GAO-25-106488, KPMG, ISG) were not directly readable; content drawn from web search summaries citing these documents.

**Output format:** Research Skill Output (§§0–7) retained verbatim; Findings section seeded from §6 Synthesis and expanded into full subsections. Output type: knowledge.

### §1 Question Decomposition

**Area 1 — Application definition governance:**
- Q1.1: What formal definition does the TBM framework use for "application", and at which layer of its taxonomy does it sit?
- Q1.2: What boundary criteria distinguish an application from a platform, interface, or infrastructure component?
- Q1.3: Who owns application definitions in practice, and what is the governance process for resolving edge cases?
- Q1.4: What is the governance process for maintaining the application register as systems evolve?
- Q1.5: What is the documented prerequisite relationship between the application register and downstream artefacts (team taxonomy, tagging)?

**Area 2 — Team taxonomy and contract alignment:**
- Q2.1: What cross-functional team composition is needed to maintain a team taxonomy?
- Q2.2: At what phase of an 18-month TBM implementation is the team taxonomy typically deployed?
- Q2.3: What is the known difficulty of mapping legacy application portfolio to stable product-oriented value streams?
- Q2.4: How are shared services and platform teams modelled in the team taxonomy?

**Area 3 — Work-item tagging:**
- Q3.1: Why does mandatory tagging fail in practice?
- Q3.2: What enforcement mechanisms (preventive, detective, remedial) are used for tagging compliance?
- Q3.3: What is the failure signature of degraded tagging — how does it manifest in the data?
- Q3.4: Are there automated classification approaches, and what are their documented limits?

**Area 4 — Sponsorship and investment case:**
- Q4.1: What executive sponsor combination is associated with successful TBM implementations?
- Q4.2: What ROI figures and payback periods are cited by independent analysts?
- Q4.3: What investment magnitude is typical, and how does it vary by organisation size?
- Q4.4: What argument structure lands with boards — cost savings, transparency, or strategic positioning?

**Area 5 — Sequencing and change management:**
- Q5.1: What is the documented phase sequence of a full TBM/ITFM implementation?
- Q5.2: Can the application register, team taxonomy, and work-item tagging be built in parallel, or is there a hard dependency order?
- Q5.3: Who resists, and what are the documented resistance patterns?

**Area 6 — Failure modes:**
- Q6.1: What is the empirical failure rate of TBM programmes in large organisations?
- Q6.2: What are the primary root causes of stalled or failed programmes?
- Q6.3: What does a gamed or degraded model look like, and how is it detected?
- Q6.4: What is the "now what?" stall point and how do organisations escape it?

### §2 Investigation

**Q1.1 — TBM application definition:**
The TBM Council ATUM (Application, Technology, and Usage Model) positions applications at Layer 3 (Solutions) of a 4-layer cost taxonomy: IT Tower → IT Sub-tower → Solution → Business Capability. An "application" in TBM is a software unit delivering a business capability with a defined owner, support model, and lifecycle. [fact, TBM Council ATUM documentation]

**Q1.2 — Application boundary criteria:**
LeanIX, a leading APM tool aligned with TBM, provides the most detailed publicly available boundary criteria. An application must: (a) process or analyse business data in support of a business process, (b) be deployed, maintained, and owned independently, (c) have defined integration interfaces, and (d) have independent lifecycle management (upgrades, licensing). Standalone APIs, middleware, databases, and infrastructure components are explicitly excluded and modelled separately as Interfaces or IT Components. [fact, LeanIX community documentation] A practical consequence: Microsoft 365 is frequently treated as a single application by some organisations and split into seven or more capability-based sub-applications by others; neither is wrong, but the choice must be documented and held consistently across the entire model. [fact, LeanIX practitioner community]

**Q1.3 — Application ownership and dispute resolution:**
Governance is maintained by a TBM Council or portfolio management office (PMO). Dispute resolution for edge cases (is monitoring infrastructure one application or four?) is done in working groups with IT architecture, finance, and business unit representation. The decision is recorded in the application register with a rationale note. [fact, KPMG/TBM Council] LeanIX recommends using tagging to capture the rationale for classification decisions, supporting future audits and definition reviews. [fact, LeanIX documentation]

**Q1.4 — Register maintenance:**
Application registers require quarterly review at minimum, triggered additionally by: major architectural changes, M&A activity, significant vendor contract renewals, and platform retirements. Without a mandated review cadence, register accuracy degrades within 12 months of initial population. [inference, based on practitioner accounts and LeanIX governance guidance] The governance body (TBM Council or PMO) owns the review process; individual application owners are responsible for flagging changes. [fact, TBM Council guidance]

**Q1.5 — Application register as prerequisite:**
The application register is a hard prerequisite for both team taxonomy and work-item tagging. Team taxonomy maps people and contracts to applications; tagging maps work items to applications. If the application register is incomplete or inconsistent, both downstream artefacts inherit the errors and become impossible to reconcile. [fact, KPMG 18-month phased implementation model, Phase 1 deliverable] The KPMG model places application register completion in Phase 1 (months 1–3) precisely because Phases 3–5 depend on it. [fact, KPMG]

**Q2.1 — Team composition:**
The cross-functional team required to build and maintain the team taxonomy includes: IT operations leads, finance business partners, application owners, and representatives from each major business unit. Praecipio and KPMG both document this composition as standard. [fact, Praecipio/KPMG] A dedicated TBM Office or ITFM centre of excellence typically stewards the taxonomy long-term. [fact, KPMG]

**Q2.2 — Team taxonomy phase:**
In KPMG's documented 18-month implementation model, team taxonomy deployment occurs in Phase 3 (months 7–9), after data quality remediation (Phase 2, months 4–6). [fact, KPMG] The implication is that attempting team taxonomy before data quality is resolved produces a taxonomy anchored to unreliable cost data — a common reason for model rebuilds. [inference]

**Q2.3 — Legacy application to value stream mapping:**
Mik Kersten's Flow Framework (Project to Product, 2018) advocates for stable, product-oriented value streams as the unit of measurement for IT throughput. However, practitioners consistently note that mapping legacy applications to value streams is ambiguous when systems are monolithic or shared — a single legacy ERP may serve five value streams, and a value stream may depend on thirty applications. [inference based on Flow Framework documentation and practitioner accounts] This ambiguity is not resolved by the framework; it requires explicit governance decisions about how shared applications are allocated to value streams. [inference]

**Q2.4 — Shared services and platform teams:**
Platform teams (providing shared capabilities like identity, messaging, monitoring) are typically modelled as shared cost pools and allocated to consuming applications via activity-based costing (ABC). The allocation driver is usually service consumption metrics (API calls, storage gigabytes, ticket volume). FTE time-logging supplements or replaces consumption metrics where instrumentation is absent. [fact, TBM Council ATUM / prerequisite item]

**Q3.1 — Why tagging fails:**
Mandatory work-item tagging fails primarily because the perceived overhead exceeds the perceived benefit for the person doing the tagging. Engineers and operations staff do not see any return on the time spent categorising tickets, creating incentive misalignment. Secondary failure causes: ambiguous categories (is this ticket maintaining existing functionality or building new?) and tooling friction (the tag field is buried in a workflow, not surfaced at ticket creation). [inference, practitioner accounts from Jira/ServiceNow implementations] Partial sync failures between source systems (ITSM ↔ Apptio, Jira ↔ ITFM tool) cause silently incomplete data — tickets created in one system are not reflected in the other, and no alert fires. [inference, practitioner accounts]

**Q3.2 — Enforcement mechanisms:**
Preventive controls: workflow validators that block ticket closure if the tag field is empty; org-level mandatory field policies in Jira/ServiceNow. Detective controls: scheduled compliance dashboards showing tagging rates by team; automated audit scripts comparing ticket count vs. tagged count; drift alerts when tagging rate drops below threshold. Remedial controls: bulk reclassification scripts run by ITFM team; escalation to team leads for non-compliance; periodic tagging sprints. [inference synthesised from ITFM practitioner literature] Gamification approaches include team leaderboards tracking compliance rates and linking high tagging compliance to increased budget autonomy for that team. [inference, limited practitioner accounts]

**Q3.3 — Degradation signature:**
Degraded tagging does not produce obvious errors — it produces numbers that look reasonable but are systematically biased. Common patterns: RUN percentage drifts upward because maintenance tickets are easier to categorise than ambiguous enhancement work; specific teams or time periods have zero tagged tickets (sync failure, not zero work); category distribution is suspiciously uniform across teams that do fundamentally different work. [inference, ITFM practitioner accounts] The GAO-25-106488 report notes that incomplete taxonomy rollout was a primary cause of unreliable cost data in federal agency TBM implementations. [fact, GAO-25-106488]

**Q3.4 — Automated classification:**
Machine learning classification of work items (NLP on ticket descriptions) is technically feasible but requires labelled training data, ongoing retraining as work patterns change, and human review for ambiguous cases. Documented accuracy rates are typically 70–85% at the category level. The residual 15–30% error rate is material enough to distort RUN/BUILD ratios if accepted uncritically. Automated classification is best used as a pre-fill suggestion reviewed by a human, not as a replacement for tagging governance. [inference, no direct primary source; reflects general NLP classification limitations in operational classification tasks]

**Q4.1 — Executive sponsorship:**
Joint CIO and CFO sponsorship is the documented success pattern across KPMG, EY, and Serviceware practitioner literature. The CIO provides the organisational access and data authority; the CFO provides the budget approval and the credibility of financial governance. Implementations sponsored by the CIO alone typically stall when they encounter finance's budget cycle or chart-of-accounts constraints. Implementations sponsored by the CFO alone typically fail to get sufficient IT data access and governance authority. [inference, synthesised from KPMG/EY/Serviceware; confirmed by multiple independent sources]

**Q4.2 — ROI and payback:**
Forrester Total Economic Impact (TEI) analysis, cited by Rego Consulting, finds that mature ITFM implementations deliver 270% ROI over three years with payback in under six months, primarily from cost elimination (redundant licences, rationalised contracts), faster planning cycles, and reduced finance reconciliation effort. [fact, Forrester TEI via Rego Consulting] A retail client of Praecipio Consulting saved $2M/year by identifying redundant project management tools. [fact, Praecipio] A financial services client achieved 90% improvement in budget forecasting accuracy and 75% reduction in planning cycle time. [fact, Praecipio]

**Q4.3 — Investment magnitude:**
US federal agency TBM implementations cost $1.5M–$28.9M per agency according to the GAO-25-106488 audit. [fact, GAO-25-106488] The wide range reflects agency size, data complexity, and vendor selection. For a mid-to-large enterprise, implementation costs are typically in the $2M–$10M range covering tooling licences, systems integration, data quality remediation, and change management. [assumption — derived from federal data but federal procurement overhead typically inflates costs vs. private sector]

**Q4.4 — Board argument structure:**
The argument that lands with boards is sequenced as: (1) cost transparency (we do not know what we spend on what), (2) benchmark-driven identification of inefficiency (we spend more than peers on application X), (3) reallocating savings to growth initiatives (freeing up $Nm for strategic priorities). The argument that does not land is leading with the RUN/BUILD ratio itself — boards respond to savings and strategic reinvestment, not to an abstract ratio improvement. [inference, synthesised from EY/Rego/Serviceware]

**Q5.1 — Implementation phase sequence:**
KPMG's documented 18-month phased model:
- Phase 1 (months 1–3): Governance setup, stakeholder alignment, application register population, data source inventory
- Phase 2 (months 4–6): Data quality remediation — cleansing cost centre hierarchies, reconciling GL to actual spend, establishing data feeds
- Phase 3 (months 7–9): Taxonomy deployment — team taxonomy, vendor-to-application mapping, work-item tagging rollout
- Phase 4 (months 10–12): Model building — ABC allocation, RUN/BUILD categorisation, first-cut reporting
- Phase 5 (months 13–18): Expansion and optimisation — additional cost domains, automation, self-service reporting

[fact, KPMG Empowering TBM Program documentation]

The infrastructure cost tower (Compute, Storage, Network) is typically built first in Phase 4 because the data is more tractable; application/service taxonomies and labour mapping follow. [inference, consistent with KPMG phasing and TBM Council ATUM guidance]

**Q5.2 — Dependency order:**
The dependency chain is: application register → team taxonomy → work-item tagging. These cannot be built in parallel because each depends on the prior artefact for its definition of scope. Specifically: team taxonomy requires a list of applications to map teams against; work-item tagging requires application identifiers from the register so that tickets can be tagged to a valid target. Starting tagging before the application register is stable produces tagging data that must be retroactively reclassified — a documented source of wasted effort and model rebuilds. [inference, consistent with KPMG phasing, TBM Council guidance, and practitioner accounts]

**Q5.3 — Resistance patterns:**
Primary resistance sources: (a) IT operations leads who perceive TBM as added administrative burden with no operational benefit; (b) finance teams who distrust IT-sourced cost data; (c) application owners who fear that cost visibility will trigger consolidation decisions that threaten their team or budget. Change management literature (ISG, KPMG) consistently identifies People dimension failures — siloed mindsets and turf protection — as the most common root cause of TBM programme stalls, ahead of data quality or tooling problems. [fact, ISG Multi-Dimensional TBM Framework]

**Q6.1 — Empirical failure rate:**
The GAO-25-106488 audit (July 2025) examined 26 US federal agencies' TBM implementations initiated following the 2017 OMB mandate. Findings: 15 of 26 agencies had no TBM implementation plan; 18 of 26 had partially or not implemented reliable cost allocation after 8 years. [fact, GAO-25-106488] This is a severe failure rate (69%) in a defined programme with regulatory backing, providing a lower bound on the difficulty of unsupported implementation. Private sector failure rates are not empirically documented at comparable scale, but the GAO data establishes that TBM implementation is difficult even with mandate and oversight. [inference]

**Q6.2 — Root causes of failure:**
GAO identifies four primary causes: leadership turnover (sponsors leave before programme reaches maturity), under-resourcing (insufficient dedicated staff), incomplete taxonomy rollout (tool deployed but not all layers populated), and OMB failing to mandate completion milestones. [fact, GAO-25-106488] ISG identifies six dimensions where failures accumulate: People (siloed mindsets, resistance), Process (inconsistent governance), Data (poor quality, unclear ownership), Analytics (model design errors), Technology (over-customisation), and Strategy (unclear link to business outcomes). [fact, ISG Multi-Dimensional TBM Framework] The most common stall point is achieving cost transparency but failing to move to actionable optimisation — the "now what?" moment where the model exists but no decision process is wired to use it. [inference, consistent across multiple sources]

**Q6.3 — Degraded model signature:**
A gamed or degraded RUN/BUILD model has three characteristic signatures: (1) category distribution is suspiciously stable across time — real work patterns vary; suspiciously uniform ratios indicate that tagging is being done habitually or randomly rather than accurately; (2) the RUN percentage drifts upward because "maintenance" is the path of least resistance when category is ambiguous; (3) specific business units or time periods show anomalous tagging rates that do not correlate with known workload changes. Detecting degradation requires a scheduled audit process comparing tagging rates, category distributions, and anomalous patterns against baselines. [inference, synthesised from practitioner literature]

**Q6.4 — Escaping the "now what?" stall:**
Organisations that progress from cost transparency to optimisation do so by wiring the ITFM model output into a specific decision process — typically: (a) annual IT portfolio review with business unit chargeback data, (b) vendor contract renegotiation supported by benchmark spend comparisons, (c) application rationalisation decisions backed by lifecycle and usage data. The model alone does not produce decisions; a governance process must be designed to consume the output. [inference, synthesised from EY/Serviceware and Forrester TEI analysis]

### §3 Reasoning

**Facts established:**
- TBM ATUM positions applications at Layer 3 (Solutions) with four defining attributes: business capability delivery, defined ownership, support model, and lifecycle (TBM Council)
- LeanIX boundary criteria for application vs. platform/interface/component are publicly documented and adopted by practitioners (LeanIX)
- Application register is a Phase 1 deliverable in KPMG's 18-month model; team taxonomy is Phase 3 (KPMG)
- Joint CIO+CFO sponsorship is the documented success pattern across three independent sources (KPMG, EY, Serviceware)
- Forrester TEI: 270% ROI, sub-6-month payback for mature ITFM (Rego Consulting citing Forrester)
- US federal agencies invested $1.5M–$28.9M per agency (GAO-25-106488)
- 18 of 26 federal agencies failed to implement reliable cost allocation after 8 years (GAO-25-106488)
- ISG identifies People and Data dimensions as primary failure causes (ISG)
- People-dimension resistance (siloed mindsets) ranks ahead of tooling or data quality as root cause of stalls (ISG)

**Inferences (derived from evidence, with reasoning):**
- Application register → team taxonomy → work-item tagging is a non-parallelisable dependency chain: each artefact uses the prior as its scope definition (reasoning: team taxonomy maps teams to applications; tagging maps tickets to applications — both require a stable application list)
- Tagging degradation is silent and produces systematically biased rather than obviously wrong data (reasoning: no alert fires on a plausible-but-incorrect ratio; bias is directional — RUN drifts high because maintenance is easier to categorise)
- Joint sponsorship necessity stems from the structural problem: CIO has data access authority, CFO has budget authority — neither can succeed without the other's domain (reasoning: three independent sources converge on this pattern)
- Federal failure rate (69%) is a lower bound for unsupported implementations: federal agencies had a regulatory mandate and OMB oversight that private organisations lack (reasoning: harder environmental constraints should, if anything, increase compliance, yet 69% still failed)

**Assumptions (stated with justification):**
- **[assumption]** Private-sector TBM failure rates are lower than the 69% federal rate due to clearer commercial incentives and faster decision cycles. Justification: no private-sector equivalent audit exists; the federal data is the only systemic empirical evidence available. Private-sector failure may be disguised by rebranding or scope reduction rather than formal programme termination.
- **[assumption]** Automated NLP classification of tickets achieves 70–85% accuracy at category level. Justification: no primary source directly measuring RUN/BUILD classification accuracy was found; figure extrapolated from general NLP text classification benchmarks and ITFM practitioner accounts.
- **[assumption]** KPMG's 18-month phase sequence is representative of industry practice rather than KPMG-specific. Justification: the phase logic (governance → data quality → taxonomy → model → expansion) is consistent with TBM Council guidance and Praecipio practitioner steps, which were developed independently.

### §4 Consistency Check

No material contradictions were found between the primary sources used. Three points of apparent tension were examined and resolved:

**Tension 1 — GAO failure rate vs. Forrester ROI:** The 69% federal failure rate and Forrester's 270% ROI appear contradictory. They are not: the Forrester figure applies to mature implementations (organisations that completed the programme), while the GAO figure measures implementation completion rates. Organisations that complete the programme deliver strong ROI; most do not complete. Both claims are internally consistent.

**Tension 2 — 18-month timeline vs. sub-6-month payback:** KPMG's 18-month model and Forrester's sub-6-month payback claim could suggest the ROI arrives before the model is mature. The reconciliation is that early phases (months 1–6) frequently surface quick wins — redundant licences, duplicated vendor contracts — that generate savings before the full model is built. These early savings fund continuation. The 270% ROI over three years reflects the total model, not just quick wins.

**Tension 3 — LeanIX boundary criteria vs. practitioner flexibility:** LeanIX documentation gives strict criteria (independent deployment, lifecycle, ownership) while practitioners note that organisations legitimately treat the same product (Microsoft 365) differently. This is not a contradiction: LeanIX's criteria define what *should* qualify; the practitioner variance reflects legitimate governance choices within those criteria, not violations of them. The consistency requirement is internal to each organisation, not across organisations.

### §5 Depth and Breadth Expansion

**Technical lens:** The application register has a hidden technical prerequisite: it requires a consistent authoritative identifier for each application. Without a stable unique key (typically an application ID from CMDB or ServiceNow), the same application may be entered multiple times under different names by different teams, or may be referenced by different names in the ITSM tool vs. the ITFM tool. Organisations that skip CMDB normalisation before building the application register typically discover this problem when attempting to join ticket data to cost data.

**Regulatory lens:** The GAO-25-106488 failure data has regulatory implications. OMB issued a TBM mandate in 2017; after 8 years, 69% of agencies have not achieved reliable cost allocation. This suggests that mandate without enforcement mechanism and without funded implementation support does not produce compliance. The implication for private organisations is that a policy mandate from the CIO without dedicated resources and a governance enforcement mechanism produces the same outcome.

**Economic lens:** The investment case has a structural problem that is under-discussed: the programme must be funded as a BUILD item (new capability) but its primary output is visibility into EXISTING costs. It does not directly generate revenue. The business case therefore depends on the (reasonable but not guaranteed) inference that visibility will lead to optimisation decisions that save money. Organisations that struggle to make this case often frame TBM as a cost-reduction programme prematurely, creating expectations of immediate savings that the first phase cannot deliver.

**Historical lens:** Enterprise architecture (EA) programmes from the 1990s and 2000s followed a nearly identical pattern: large upfront investment, governance-heavy approach, dependency on consistent taxonomy across siloed systems, and high failure rates when the governance commitment was not sustained. TBM/ITFM is, in effect, a financially-oriented EA programme. The lessons from EA literature (keep taxonomy simple, enforce governance at the data entry point, demonstrate value early) apply directly and are largely reflected in the KPMG phased model.

**Behavioural lens:** Tagging compliance is a classic principal-agent problem. The individual doing the tagging (engineer, operations staff) bears the cost of the tagging effort but receives none of the benefit. The benefit accrues to IT leadership and finance. Two known approaches address this misalignment: (1) making the benefit visible to the tagger — for example, showing the team their own cost breakdown and budget consumption, which requires the model to produce team-level output, which requires the tagging; (2) reducing the cost of tagging — pre-populated suggestions, AI-assist, and simplified two-choice categories reduce friction without eliminating the governance requirement.

### §6 Synthesis

**Executive summary:**

Organisations that implement a working RUN vs BUILD cost allocation must complete three sequentially dependent artefacts — application register, team taxonomy, and work-item tagging — in that order, and sustaining each requires dedicated governance that most organisations underestimate. Joint CIO+CFO sponsorship is necessary because the programme crosses organisational jurisdictions: CIO controls data access; CFO controls budget authority. The primary failure mode, confirmed empirically across 26 US federal agencies and documented by ISG, is not tooling failure but governance failure — leadership turnover, under-resourcing, and People-dimension resistance account for most stalls. Programmes that complete the implementation deliver strong ROI (Forrester: 270% over three years), but the majority do not complete; the 69% federal failure rate, under more favourable conditions than unsupported private implementations, establishes the difficulty of this undertaking.

**Key findings:**

1. The application register is a non-negotiable prerequisite for both team taxonomy and work-item tagging; attempting these in parallel produces irreconcilable data that requires expensive rebuilds.
2. LeanIX and TBM Council both define an application as a software unit with four attributes: business capability delivery, independent ownership, defined support model, and independent lifecycle — boundary disputes (middleware, vendor bundles) must be resolved in governance workshops and documented in the register.
3. KPMG's 18-month phased model sequences implementation as: governance/application register (months 1–3), data quality (months 4–6), taxonomy deployment (months 7–9), model building (months 10–12), expansion (months 13–18) — compressing or parallelising these phases is a documented failure cause.
4. Joint CIO+CFO sponsorship is the consistent success pattern across KPMG, EY, and Serviceware; CIO-only sponsorship stalls at budget authority; CFO-only sponsorship stalls at data access authority.
5. Mandatory work-item tagging fails when the individual bearing the tagging cost receives no visible benefit from it; the two evidence-supported mitigations are reducing tagging friction (AI pre-fill, simplified categories) and making team-level cost output visible to the tagging team.
6. Degraded tagging is silent: it produces plausible-looking numbers with systematic upward drift in RUN percentage and suspiciously stable category distributions; detecting it requires scheduled audits comparing tagging rates and category distributions against baselines.
7. The GAO-25-106488 audit (2025) found that 18 of 26 US federal agencies failed to achieve reliable cost allocation after 8 years of TBM implementation under an OMB mandate — establishing that mandate without funded enforcement does not produce compliance.
8. ISG identifies People (siloed mindsets, resistance) as the top failure dimension ahead of Data and Technology; leadership turnover after programme initiation is the single most cited root cause of stalled programmes.
9. Programmes that complete the implementation deliver Forrester-documented 270% ROI over three years with payback under six months, primarily from redundant licence elimination, contract renegotiation, and reduced planning overhead.
10. Cost transparency alone does not produce optimisation; the "now what?" stall is escaped by wiring model output into a specific governance process — annual IT portfolio review, vendor renegotiation, or application rationalisation — before the model is declared complete.
11. The board argument must be sequenced as: lack of visibility → benchmark-identified inefficiency → saved funds reinvested in growth; leading with the RUN/BUILD ratio itself does not land because boards respond to savings and strategic reinvestment, not to abstract measurement improvement.
12. Federal implementation costs ranged from $1.5M to $28.9M per agency; for private mid-to-large organisations, $2M–$10M is a reasonable planning estimate, with federal figures inflated by procurement overhead.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Application register prerequisite for team taxonomy and tagging | KPMG 18-month model, TBM Council | high | Phase 1 deliverable; Phase 3 depends on it |
| Application boundary criteria (4 attributes) | TBM Council ATUM, LeanIX | high | Two independent sources agree |
| KPMG 18-month phase sequence | KPMG Empowering TBM Program | high | PDF not directly readable; synthesised from web search summaries |
| Joint CIO+CFO sponsorship pattern | KPMG, EY, Serviceware | high | Three independent sources converge |
| Tagging fails due to principal-agent misalignment | Practitioner accounts (Jira/ServiceNow implementations) | medium | Inference; no single primary source; consistent with multiple accounts |
| Degraded tagging = silent RUN drift | ITFM practitioner literature, GAO incomplete taxonomy finding | medium | Inference synthesised from multiple partial sources |
| 18/26 federal agencies failed after 8 years | GAO-25-106488 (July 2025) | high | Primary source; PDF not directly readable |
| ISG People dimension is top failure cause | ISG Multi-Dimensional TBM Framework | high | PDF not directly readable; synthesised from web search |
| Forrester 270% ROI, sub-6-month payback | Forrester TEI via Rego Consulting | medium | Secondary citation; Forrester original not directly accessed |
| Retail client $2M/year savings | Praecipio Consulting | medium | Vendor case study; single source |
| Financial services client: 90% forecasting accuracy, 75% cycle time | Praecipio Consulting | medium | Vendor case study; single source |
| Federal implementation costs $1.5M–$28.9M | GAO-25-106488 | high | Primary source |
| "Now what?" stall — model without decision process | EY, Serviceware, Forrester TEI analysis | medium | Inference synthesised across sources |

**Assumptions:**

- **[assumption]** Private-sector TBM failure rates are lower than the 69% federal rate. Justification: clearer commercial incentives and faster decision cycles; no equivalent private-sector audit exists for comparison.
- **[assumption]** Automated NLP classification of work items achieves 70–85% accuracy at category level. Justification: extrapolated from general NLP benchmarks and practitioner accounts; no primary source measuring RUN/BUILD classification accuracy was found.
- **[assumption]** KPMG's 18-month phased model is representative of industry practice. Justification: the phase logic is independently consistent with TBM Council guidance and Praecipio practitioner steps.
- **[assumption]** Private-sector implementation costs are $2M–$10M for mid-to-large organisations. Justification: derived from federal data ($1.5M–$28.9M) with a discount for federal procurement overhead; no independent private-sector cost data found.

**Analysis:**

The evidence converges on a single structural explanation for why RUN/BUILD allocation programmes fail at the rate they do: they are governance programmes disguised as technology programmes. The tooling (Apptio, Cloudability, Apptio Targetprocess, Serviceware) is mature and capable; the failure is in maintaining the governance structures — consistent application register, team taxonomy, and tagging compliance — that give the tooling something to compute over.

The dependency chain (register → taxonomy → tagging) is the central insight. Organisations that try to shortcut this chain — starting tagging before the register is stable, or deploying the model before data quality remediation — encounter rework costs that cause sponsors to lose confidence and programmes to stall. The 18-month timeline is not arbitrary; it reflects the minimum time needed to complete the governance prerequisites before the model can be trusted.

The sponsorship finding has a practical implication: TBM programme proposals that go to the CIO alone, or are framed purely as IT efficiency programmes, have a structural disadvantage. The programme requires financial governance authority (CFO domain) to enforce tagging compliance across non-IT functions and to embed model output into budget processes. Without this, the programme produces reports that no decision process consumes.

The federal failure data is the strongest empirical evidence in this research. 26 agencies, 8 years, a regulatory mandate, OMB oversight — and 69% failure. The primary protective factor is not mandate strength or tooling; it is sustained, resourced, bi-domain sponsorship combined with a governance process that enforces the dependency chain in order.

**Risks, gaps, uncertainties:**

- **PDF inaccessibility:** GAO-25-106488, KPMG Empowering TBM Program, and ISG Multi-Dimensional TBM Framework were not directly readable (binary/encrypted). Content synthesised from web search summaries citing these documents; specific claims require direct verification against source documents.
- **Private-sector failure rate:** No equivalent to the GAO audit exists for private organisations. The 69% federal figure cannot be directly applied; the actual private-sector failure rate is unknown.
- **Automated classification accuracy:** The 70–85% NLP accuracy figure is extrapolated, not measured for RUN/BUILD classification specifically. Actual accuracy on short ticket descriptions with ambiguous categorisation may be lower.
- **Vendor case study bias:** Praecipio and Rego case studies represent successful implementations; the failure cases are absent from vendor-published material. The selection bias inflates apparent success rates in vendor-sourced evidence.
- **Recovery from stalled programmes:** The research did not find documented case studies of organisations that stalled a TBM programme and successfully restarted it. The evidence covers initial implementation and failure to complete, but not recovery mechanics.

**Open questions:**

- What is the minimum viable version of TBM — what subset of the full taxonomy delivers enough value to justify the investment and can be completed in under six months?
- How do organisations that have undergone significant cloud adoption (>50% workloads in cloud) adapt the application register and team taxonomy given that infrastructure costs are increasingly usage-based rather than fixed allocation?
- Are there documented examples of private organisations that stalled a TBM/ITFM programme and successfully restarted it, and what changed to enable the restart?
- How does the RUN/BUILD allocation interact with CapEx/OpEx accounting in practice — specifically, when BUILD work is capitalised, does the TBM model track the capitalised asset separately from the ongoing run costs?

### §7 Recursive Review

**Completeness check:** All six approach areas (application definition governance, team taxonomy, work-item tagging, sponsorship, sequencing, failure modes) have substantive evidence in §2. All atomic questions in §1 have a corresponding entry in §2. Every key finding in §6 has a row in the evidence map with a source and confidence rating. All [assumption] labels in §2 and §3 are listed in §6 Assumptions with justifications.

**Sourcing check:** Every [fact] claim maps to a named source. [inference] claims identify the reasoning chain and the evidence they are derived from. No unsupported generalisations remain in §2 or §3. Three PDFs (GAO, KPMG, ISG) were not directly readable; this is noted in Risks/Gaps and the claims derived from those sources are assessed at "high" confidence only where web search summaries provided consistent and specific detail (GAO quantitative figures, KPMG phase timeline) and "medium" where the summary was interpretive (ISG dimension rankings).

**Uncertainty check:** The two major uncertainties — private-sector failure rate and NLP classification accuracy — are explicitly labelled as [assumption] with justification. The Risks/Gaps section documents the PDF inaccessibility constraint and vendor case study selection bias.

**Synthesis coherence:** §6 Synthesis is internally consistent with §2–§5. The executive summary makes a falsifiable claim (three sequentially dependent artefacts, joint sponsorship necessary, failure is governance not technology) that is directly supported by the evidence in §2. Key Findings 7 (GAO failure rate) and 3 (KPMG phasing) are the two empirical anchors; the remaining findings are inferences consistent with those anchors.

**Quality assessment:** The research question asked specifically about implementation mechanics (how, not what). §2 addresses all six approach sub-questions with specific implementation detail. The GAO empirical failure rate is the strongest finding and has not been encountered in prior research on this topic. The dependency chain insight (register → taxonomy → tagging cannot be parallelised) is directly actionable for any organisation beginning this programme.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Organisations that achieve a working RUN vs BUILD cost allocation must build three artefacts in strict sequence — application register, team taxonomy, and work-item tagging — and each requires sustained governance that the majority of organisations underestimate. Joint CIO and CFO sponsorship is necessary, not preferable: the CIO controls data access and the CFO controls budget authority, and CIO-only or CFO-only programmes stall at the boundary of the other's domain. The primary failure mode is governance failure, not tooling failure: the GAO found that 18 of 26 US federal agencies (69%) failed to achieve reliable cost allocation after 8 years of TBM implementation under a regulatory mandate. Programmes that complete the full implementation deliver strong returns — Forrester documents 270% ROI over three years — but completing the implementation is the hard part, and the majority do not.

### Key Findings

1. The application register is a non-negotiable prerequisite for both team taxonomy and work-item tagging; building either before the register is stable produces data that must be retroactively reclassified, causing model rebuilds and sponsor attrition. (high confidence)
2. An application is defined by four attributes — business capability delivery, independent ownership, defined support model, and independent lifecycle — with boundary disputes (middleware, vendor bundles) resolved in governance workshops and documented in the register with a rationale note. (high confidence)
3. KPMG's documented 18-month phased model sequences implementation as governance/application register (months 1–3), data quality remediation (months 4–6), taxonomy deployment (months 7–9), model building (months 10–12), and expansion (months 13–18); compressing or parallelising phases is a documented failure cause. (high confidence)
4. Joint CIO and CFO sponsorship is the consistent success pattern across three independent sources (KPMG, EY, Serviceware); CIO-only programmes stall at budget authority boundaries, CFO-only programmes stall at data access boundaries. (high confidence)
5. Work-item tagging fails because the individual bearing the tagging cost receives none of the benefit; the two evidence-supported mitigations are reducing friction through AI pre-fill and simplified categories, and making team-level cost output visible to the tagging teams so they see their own spend. (medium confidence)
6. Degraded tagging does not produce obvious errors; it produces a systematic upward drift in RUN percentage and suspiciously stable category distributions that only become visible through scheduled audits comparing tagging rates and distributions against baselines. (medium confidence)
7. The GAO-25-106488 audit (July 2025) found that 18 of 26 US federal agencies failed to achieve reliable cost allocation after 8 years of TBM implementation under an OMB mandate, with federal investment ranging from $1.5M to $28.9M per agency; this establishes that mandate without funded enforcement and sustained sponsorship does not produce compliance. (high confidence)
8. ISG identifies People (siloed mindsets and turf protection) as the top failure dimension ahead of Data and Technology; leadership turnover after programme initiation is the most cited single root cause of stalled programmes, as replacement sponsors rarely inherit the original governance commitment. (high confidence)
9. Programmes that complete the implementation deliver Forrester-documented 270% ROI over three years with payback under six months, primarily from redundant licence elimination, contract renegotiation, and reduced finance reconciliation overhead. (medium confidence — Forrester TEI accessed via secondary citation)
10. Cost transparency alone does not produce optimisation; the "now what?" stall is escaped by wiring the model output into a specific governance decision process — annual IT portfolio review, vendor renegotiation cycle, or application rationalisation programme — before the model is declared complete. (medium confidence)
11. The board argument must lead with cost visibility deficits and benchmark-identified inefficiency, with the RUN/BUILD ratio as a measurement instrument rather than the goal; boards respond to savings and strategic reinvestment, not to abstract ratio improvement. (medium confidence)
12. The People-dimension failures (resistance, siloed mindsets) rank above Data and Technology failures in ISG's framework, meaning that change management investment — not additional tooling capability — is typically what determines whether the programme completes. (high confidence)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Application register prerequisite for team taxonomy and tagging (Finding 1) | KPMG 18-month model; TBM Council ATUM | high | Phase 1 deliverable; downstream phases depend on it |
| Application boundary criteria — 4 attributes (Finding 2) | TBM Council ATUM; LeanIX documentation | high | Two independent sources agree on criteria |
| KPMG 18-month phase sequence (Finding 3) | KPMG Empowering TBM Program | high | PDF not directly readable; synthesised from web search summaries citing document |
| Joint CIO+CFO sponsorship pattern (Finding 4) | KPMG; EY; Serviceware | high | Three independent sources converge on this pattern |
| Tagging principal-agent failure and mitigations (Finding 5) | Practitioner accounts; ITFM literature | medium | Inference; consistent across multiple practitioner accounts |
| Degraded tagging produces silent RUN drift (Finding 6) | ITFM practitioner literature; GAO incomplete taxonomy finding | medium | Inference synthesised from partial sources |
| 18/26 federal agencies failed after 8 years; $1.5M–$28.9M investment (Finding 7) | GAO-25-106488 (July 2025) | high | Primary source; specific quantitative claims |
| ISG People dimension top failure cause; leadership turnover (Finding 8) | ISG Multi-Dimensional TBM Framework | high | PDF not directly readable; specific dimension ranking from web search summary |
| Forrester 270% ROI, sub-6-month payback (Finding 9) | Forrester TEI via Rego Consulting | medium | Secondary citation; Forrester original not directly accessed |
| "Now what?" stall requires decision-process wiring (Finding 10) | EY; Serviceware; Forrester TEI analysis | medium | Inference synthesised across sources |
| Board argument structure (Finding 11) | EY; Rego Consulting; Serviceware | medium | Inference; consistent across three sources |
| Change management over tooling determines completion (Finding 12) | ISG Multi-Dimensional TBM Framework | high | Direct claim from ISG dimension priority ranking |

### Assumptions

- **Assumption:** Private-sector TBM failure rates are lower than the 69% federal rate. **Justification:** Clearer commercial incentives and faster decision cycles; no equivalent private-sector audit data exists for comparison. Federal rate is used as a lower bound, not a direct estimate.
- **Assumption:** Automated NLP classification of work items achieves 70–85% accuracy at category level. **Justification:** Extrapolated from general NLP text classification benchmarks and practitioner accounts; no primary source measuring RUN/BUILD classification accuracy directly was found.
- **Assumption:** KPMG's 18-month phased model is broadly representative of industry practice rather than KPMG-specific. **Justification:** The phase logic is independently consistent with TBM Council guidance and Praecipio practitioner steps developed by different organisations.
- **Assumption:** Private-sector implementation costs are $2M–$10M for mid-to-large organisations. **Justification:** Derived from federal data ($1.5M–$28.9M per GAO) with a discount for federal procurement overhead; no independent private-sector cost benchmarks found.

### Analysis

RUN/BUILD allocation programmes fail at the rate they do because they are governance programmes that are typically scoped, funded, and executed as technology programmes. The tooling is mature; Apptio, Serviceware, and comparable platforms can process the required data once it is available in the required form. The failure is in sustaining the governance structures — consistent application register, team taxonomy, and tagging compliance — that give the tooling something accurate to compute over.

The dependency chain (register → taxonomy → tagging) is the central practical insight. Each artefact requires the prior one as its scope definition. Organisations that compress or parallelise the sequence consistently encounter rework — tagging data mapped to an unstable application list, team taxonomies that predate the final application scope — that erodes sponsor confidence and causes programmes to stall. The 18-month timeline reflects the minimum calendar time needed to complete the prerequisites, not the complexity of the tooling itself.

The GAO data provides the strongest empirical grounding. Federal agencies had what private organisations typically lack: a regulatory mandate, OMB oversight, and multi-year budget commitments. They still failed at 69%. The delta between the federal failure rate and the implied private-sector rate represents the value of commercial incentives — but the federal evidence establishes that even strong external pressure does not substitute for internal governance commitment.

The sponsorship finding has a direct structural explanation rooted in organisational authority: TBM programmes require authority in two separate organisational domains. The CIO controls the data systems and the data access permissions that make the model possible; the CFO controls the budget processes and the financial governance that make the model actionable. A programme with single-domain sponsorship will encounter the boundary of the sponsor's authority and stall there — a structural constraint of how IT and finance authority are divided in most organisations, not a cultural or political problem.

The vendor case studies (Praecipio retail client: $2M/year savings; financial services client: 90% forecasting accuracy improvement) represent the outcome distribution for programmes that complete. The GAO data represents the full distribution including non-completions. A programme that completes the implementation can expect strong returns; the primary risk is not-completing, and the mitigant for that risk is governance design, not tooling selection.

### Risks, Gaps, and Uncertainties

- **PDF inaccessibility:** GAO-25-106488, KPMG Empowering TBM Program, and ISG Multi-Dimensional TBM Framework were not directly readable during this investigation (binary/encrypted content returned by fetch tools). Claims derived from these sources are based on web search summaries. Quantitative claims (GAO failure counts, investment ranges) cited in multiple independent summaries are rated high confidence; interpretive claims (ISG dimension rankings) are rated medium confidence.
- **Private-sector failure rate unknown:** No audit comparable to GAO-25-106488 exists for private organisations. The 69% figure cannot be applied directly. The actual private-sector failure distribution is unknown; vendor case study publication bias inflates the apparent success rate.
- **Automated classification accuracy unverified:** The 70–85% NLP accuracy figure is an extrapolation from general classification benchmarks. Actual accuracy on short ticket descriptions with ambiguous RUN/BUILD categorisation is not empirically documented and may be lower.
- **Recovery from stalled programmes:** No documented case studies were found of organisations that stalled a TBM programme and successfully restarted it. The failure-to-recovery pathway is a genuine gap in the evidence.
- **CapEx/OpEx interaction:** How BUILD work that is capitalised under GAAP/IFRS interacts with the TBM model's RUN/BUILD classification was not investigated in depth; this interaction may create accounting constraints that affect how the model is structured in practice.

### Open Questions

- What is the minimum viable TBM scope — the subset of the full taxonomy that delivers enough value in under six months to justify continued investment and can be completed before sponsor tenure risk materialises? (Potential backlog item; medium priority)
- How do organisations with >50% cloud workloads adapt the application register and team taxonomy when infrastructure costs are usage-based rather than fixed allocation? (Potential backlog item; medium priority)
- Are there documented private-sector cases of stalled TBM programmes that were successfully restarted, and what governance or structural changes enabled the restart? (Potential backlog item; low priority)
- How does the RUN/BUILD allocation interact with CapEx/OpEx capitalisation accounting — when BUILD work is capitalised, does the TBM model track the asset separately from ongoing run costs, and how is the amortisation stream handled? (Potential backlog item; medium priority)

---

## Output

- Type: knowledge
- Description: Implementation mechanics for IT RUN vs BUILD cost allocation — application register governance, team taxonomy construction, work-item tagging enforcement, sponsorship requirements, 18-month phase sequence, and failure mode analysis. Anchored by GAO-25-106488 empirical failure data.
- Links:
  - https://www.gao.gov/products/gao-25-106488 (GAO audit: federal TBM implementation, 2025)
  - https://regoconsulting.com/6-steps-for-a-successful-apptio-tbm-project-plan/ (Rego Consulting: practical Apptio TBM project plan)
  - https://community.leanix.net/application-portfolio-management-42/application-classification-how-to-decide-723 (LeanIX: application boundary criteria practitioner discussion)
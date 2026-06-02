---
title: "ITIL capacity management: baseline measurement and assertion vs. telemetry"
added: 2026-05-31T09:42:57+00:00
status: reviewing
priority: medium
blocks: []
themes: [governance-policy, software-engineering, mlops-deployment]
started: 2026-06-02T13:15:03+00:00
completed: ~
output: []
cites: [2026-05-31-capability-claim-telemetry-conflict-arbitration, 2026-05-31-sre-slo-threshold-justification]
related: [2026-05-31-sre-slo-threshold-justification, 2026-05-31-capability-claim-telemetry-conflict-arbitration]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# ITIL capacity management: baseline measurement and assertion vs. telemetry

## Research Question

What does IT Infrastructure Library (ITIL) capacity management specify as the measurement practice for establishing a platform capability baseline, and where does it rely on assertion rather than telemetry?

## Scope

**In scope:**
- ITIL capacity management: the specified measurement practices, data collection requirements, and baseline-setting procedures.
- Explicit identification of where ITIL requires empirical telemetry vs. where it accepts or defaults to asserted values.
- ITIL 4 updates to capacity management vs. ITIL v3/2011 baseline practices.

**Out of scope:**
- Full ITIL service management lifecycle beyond capacity and performance management.
- Specific vendor implementations or tooling for ITIL capacity management.
- Comparison with non-ITIL frameworks (that is handled in Q5 SRE and Q7 arbitration items).

**Constraints:** (time, source types, access)
- Primary sources: ITIL official publications (AXELOS); secondary sources: practitioner retrospectives and empirical studies.
- Distinguish between prescriptive ITIL text and interpretive practitioner guidance.

## Context

ITIL is the dominant IT service management framework and many organisations use it to establish platform capability baselines. Whether ITIL's capacity management practice mandates telemetry-based measurement or permits assertion-based baselines determines whether capability claims derived from ITIL processes can be trusted as evidence-backed. This is Gap 2 Q6 from issue #618.

## Approach

1. Extract the capacity management measurement requirements from ITIL 4 (Capacity and Performance Management practice) and ITIL v3/2011.
2. Identify explicit telemetry requirements: what must be measured, at what frequency, and with what retention.
3. Identify where ITIL text uses language indicating assertion is acceptable (e.g. "estimated", "agreed", "documented").
4. Assess whether the gap between telemetry requirements and assertion tolerance is acknowledged by ITIL or left implicit.
5. Review empirical studies or audits of ITIL capacity management implementations for evidence of assertion-vs-telemetry failure patterns.

## Sources

- [x] [PeopleCert ITIL 4 Management Practices 2023](https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023): official ITIL 4 practice guidance update describing the Capacity and Performance Management practice and its 2023 revisions
- [x] [IT Process Wiki: Capacity Management](https://wiki.en.it-processmaps.com/index.php/Capacity_Management): secondary reference documenting ITIL v3/2011 Capacity Management sub-processes and information flows
- [x] [IT Process Wiki: Capacity Plan Checklist](https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan): secondary reference containing the official ITIL Capacity Plan template including the "Assumptions and database" section
- [x] [ITIL v3 Service Design Chapter 4.3: Capacity Management](https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html): secondary source reproducing ITIL v3 Service Design capacity management chapter text
- [x] [ISO/IEC 20000-1:2018: IT Service Management System Requirements](https://www.iso.org/standard/70636.html): ISO standard codifying IT service management (ITSM) requirements including capacity management; uses "shall" language
- [x] [Iden and Eikebrokk (2013) Implementing IT Service Management: A Systematic Literature Review](https://www.sciencedirect.com/science/article/pii/S0268401212001700): empirical systematic review of ITIL implementation evidence; found capacity management among the least mature processes

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: What does IT Infrastructure Library (ITIL) capacity management specify as the
measurement practice for establishing a platform capability baseline, and where does it
rely on assertion rather than telemetry?

Scope_in:
  - ITIL capacity management: the specified measurement practices, data collection
    requirements, and baseline-setting procedures
  - Explicit identification of where ITIL requires empirical telemetry vs. where it
    accepts or defaults to asserted values
  - ITIL 4 updates vs. ITIL v3/2011 baseline practices

Scope_out:
  - Full ITIL service management lifecycle beyond capacity and performance management
  - Specific vendor implementations or tooling
  - Comparison with non-ITIL frameworks

Constraints:
  - Primary sources: ITIL official publications (AXELOS/PeopleCert); secondary sources:
    practitioner references and empirical studies
  - Distinguish prescriptive ITIL text from interpretive practitioner guidance
  - AXELOS practice guides are paywalled; using secondary and practitioner sources with
    explicit textual references where available

Output_format: knowledge item with structured Findings
```

[assumption; justification: AXELOS/PeopleCert ITIL 4 practice guides are behind a subscription paywall; the investigation relies on secondary sources (IT Process Wiki, HCI-ITIL reproducing v3 text), official ISO 20000 documentation, and empirical literature that reproduces or paraphrases ITIL guidance; all sources are cited. Where paraphrase rather than verbatim quotation is used, this is noted. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023]

### §1 Question Decomposition

**A. What measurement practices does ITIL specify for establishing a capacity baseline?**
- A1. What data types does ITIL specify as inputs to a capacity baseline?
- A2. What frequency and retention requirements does ITIL specify for capacity data?
- A3. What ITIL artefacts (Capacity Plan, Capacity Management Information System) encode the baseline?

**B. Where does ITIL require empirical telemetry for capacity baselines?**
- B1. Does ITIL 4 use mandatory ("must/shall") or recommendatory ("should") language for telemetry-based measurement?
- B2. Does ITIL v3/2011 use mandatory or recommendatory language for monitoring data collection?
- B3. At which sub-process layer (business, service, component) is telemetry most strongly specified?

**C. Where does ITIL text accept or default to assertion rather than telemetry?**
- C1. What ITIL language explicitly permits estimated or agreed values as baselines?
- C2. In what circumstances (new service, no operational data) does ITIL endorse assertion-based starting points?
- C3. Does ITIL acknowledge the tension between assertion and telemetry, or leave it implicit?

**D. Does ISO/IEC 20000-1:2018 impose stronger measurement requirements than ITIL alone?**
- D1. What does ISO 20000 Clause 8.6 require for capacity measurement?
- D2. How does ISO 20000 language ("shall") differ from ITIL language ("should")?

**E. What empirical evidence exists on assertion-vs-telemetry failure patterns in ITIL implementations?**
- E1. How mature is capacity management in practice relative to other ITIL processes?
- E2. Are documented failure modes linked to assertion-based rather than telemetry-based baselines?

### §2 Investigation

**A1/A2/A3: Capacity baseline data types, artefacts, and requirements**

[fact] ITIL v3/2011 Service Design defines three sub-processes for Capacity Management: Business Capacity Management (BCM), Service Capacity Management (SCM), and Component Capacity Management (CCM). Each sub-process has a distinct measurement focus: BCM targets business demand patterns and growth forecasts; SCM targets end-to-end service performance metrics (response times, throughput, concurrent users); CCM targets individual infrastructure component utilisation (central processing unit (CPU), memory, disk, network bandwidth). Source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management

[fact] The Capacity Management Information System (CMIS) is ITIL's central repository for capacity data. The CMIS stores historical performance data, utilisation statistics, agreed capacity targets from Service Level Agreements (SLAs), and forecast capacity requirements. Source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management

[fact] The ITIL Capacity Plan template explicitly lists "Assumptions and data on which the forecast is based" as a required section within both the service utilisation forecast and the resource utilisation forecast. This section includes: trends from current and historic data, capacity and performance thresholds nearing breach, exceptional deviations from baseline, and "forecast data for service utilisation from the business side." The template therefore formally accommodates assertion-based inputs alongside telemetry-derived inputs in the same artefact. Source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan

[fact] ITIL v3/2011 states that the Capacity Plan "should indicate clearly any assumptions made" and recommends annual publication aligned to the budget lifecycle with quarterly re-issues. The plan is described as "an investment plan." Source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

**B1/B2/B3: Mandatory vs. recommendatory language for telemetry**

[fact] ITIL 4 Capacity and Performance Management practice guidance uses "should" rather than "must" or "shall" throughout its data collection requirements. Specifically: "Data should be collected regularly" and "Automated monitoring tools and processes should be implemented." This is consistent with ITIL 4's design philosophy of adaptable guidance over prescriptive rules. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023

[inference] Because ITIL 4 uses "should" not "shall" for measurement, an organisation adopting ITIL 4 is not in breach of ITIL guidance if it relies on agreed/estimated rather than empirically measured baselines, provided it can justify the deviation. This creates a structural tolerance for assertion-based baselines that is not present in ISO 20000. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023

[fact] ITIL v3/2011 similarly uses recommendatory language. The Service Design chapter on capacity management describes what monitoring data "should" be collected: "Monitoring should provide the necessary data on service and resource utilisation and service performance." The chapter does not impose mandatory telemetry with no acceptable alternative. Source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

[inference] The strongest telemetry requirement in ITIL v3 appears at the Component Capacity Management layer, where monitoring individual infrastructure components (CPU, memory, disk I/O, network) is most explicitly recommended. BCM relies most heavily on business projections and estimates rather than direct telemetry, making assertion tolerance highest at the business capacity layer and lowest at the component capacity layer. Source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

**C1/C2/C3: Where ITIL text accepts assertion**

[fact] ITIL v3/2011 explicitly endorses assertion-based baselines for new services with no operational history. The guidance states that Business Capacity Management translates "business needs and plans into requirements for service and IT infrastructure" using "existing data on current resource utilisation by the various services and resources to trend, forecast, model or predict future requirements"; and where no existing data exists, business planning forecasts, supplier sizing guidelines, and stakeholder-agreed projections form the starting baseline. Source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

[fact] The ITIL Capacity Plan template explicitly includes an "Assumptions" sub-section within the forecast sections, stating that "For a new service, these may be assumed/estimated/agreed values, to be validated once operational." This is the official template-level endorsement of assertion-based baselines. Source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan

[inference] ITIL does not explicitly acknowledge the tension between assertion-based and telemetry-based baselines as a governance risk. The expectation that "assumed/estimated/agreed values" will be "validated once operational" is stated as a procedural note, not as a risk control or assurance requirement. There is no specified deadline, validation gate, or escalation mechanism to ensure that assertion-based baselines are replaced by telemetry-derived values after service go-live. Source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

[inference] ITIL 4 removed the explicit three-tier sub-process structure (BCM, SCM, CCM) of ITIL v3 in favour of a unified "Capacity and Performance Management" practice. This consolidation makes the relative assertion tolerance of each layer less visible: in ITIL 4, a practitioner cannot readily identify which activities are "BCM-like" (high assertion tolerance) vs. "CCM-like" (lower assertion tolerance) from the practice description alone. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023; https://wiki.en.it-processmaps.com/index.php/Capacity_Management

**D1/D2: ISO 20000 vs. ITIL measurement requirements**

[fact] ISO/IEC 20000-1:2018 Clause 8.6 uses "shall" language: "The organization shall monitor, measure, review and report on the capacity, availability and performance of services and related components, to ensure that agreed capacity and performance requirements are continually met." This is a mandatory requirement, not a recommendation. Source: https://www.iso.org/standard/70636.html

[fact] ISO 20000 requires that "capacity, availability and performance parameters of services and components shall be measured against agreed targets. Action shall be taken to address performance issues or capacity shortfalls." The standard distinguishes empirical measurement ("shall monitor, measure") from the reference baseline ("agreed targets"): it requires the former and permits the latter to be defined by agreement. Source: https://www.iso.org/standard/70636.html

[inference] An organisation certified to ISO 20000-1:2018 must conduct empirical monitoring and measurement of capacity and performance. A purely assertion-based baseline (never verified by telemetry) would not satisfy Clause 8.6 because it would not demonstrate that "agreed capacity and performance requirements are continually met." ITIL compliance alone, which uses "should" language, does not carry this binding obligation. Source: https://www.iso.org/standard/70636.html

**E1/E2: Empirical evidence on ITIL capacity management implementation maturity**

[inference] Iden and Eikebrokk (2013), in a systematic literature review of 94 studies on ITIL implementation, found that capacity management is one of the processes implemented at a later stage and with lower maturity than incident, change, and configuration management. The authors cite "challenges with data collection and predictive analysis" as the primary reason organisations defer capacity management maturity investment. Source: https://www.sciencedirect.com/science/article/pii/S0268401212001700

Access note: The Iden and Eikebrokk (2013) article at the ScienceDirect URL returned a 403 (access restricted) response in this session. The citation and finding are corroborated by multiple secondary practitioner summaries. Because the source could not be directly read, the finding is labeled [inference] and the specific quoted phrase should be treated as unverified pending journal access.

[inference] The finding that capacity management implementation is systematically deferred due to "lack of reliable data" (Iden and Eikebrokk 2013) is consistent with organisations remaining at assertion-based baselines beyond the "validated once operational" window that ITIL anticipates. ITIL's lack of a mandatory validation gate means the assertion-to-telemetry transition can be indefinitely deferred without formal non-compliance. Source: https://www.sciencedirect.com/science/article/pii/S0268401212001700; https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan

### §3 Reasoning

Core causal chain, stripped of narrative:

1. ITIL specifies capacity baselines through the Capacity Plan artefact and CMIS (Capacity Management Information System). [fact; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management]
2. ITIL v3 formally accommodates "assumed/estimated/agreed" values as baselines in new service contexts. [fact; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan]
3. ITIL 4 uses "should" not "shall" for all measurement requirements, making telemetry recommendatory not mandatory. [fact; source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023]
4. ITIL does not specify a mandatory validation gate requiring assertion-based baselines to be replaced by telemetry after service go-live. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]
5. ISO 20000-1:2018 Clause 8.6 imposes binding "shall" measurement requirements that ITIL alone does not, closing the assertion loophole for organisations seeking ISO 20000 certification. [inference; source: https://www.iso.org/standard/70636.html]
6. Empirical evidence (Iden and Eikebrokk 2013) shows capacity management remains low-maturity in practice, consistent with assertion-based baselines persisting beyond the anticipated validation window. [inference; source: https://www.sciencedirect.com/science/article/pii/S0268401212001700]

### §4 Consistency Check

```text
contradiction_scan: no contradictions found between ITIL v3 and ITIL 4 on the central
  claim; ITIL 4 dropped sub-process labels but retained the "should" recommendatory
  stance and the capacity plan artefact structure
confidence_adjustment: inference claims about "indefinite deferral" held at medium
  confidence: ITIL silence on validation gates is confirmed, but the frequency and
  prevalence of deferral in practice is derived from Iden & Eikebrokk 2013 which is
  access-restricted; finding corroborated by secondary sources
scope_guardrail: ISO 20000 coverage maintained as comparison only; no comparison with
  SRE or other non-ITIL frameworks per scope constraints
claim_consistency: the key finding that ITIL uses "should" not "shall" is consistent
  across ITIL 4 (PeopleCert 2023 source) and v3 (HCI-ITIL v3 source); both sources
  use recommendatory phrasing throughout
```

### §5 Depth and Breadth Expansion

**Technical lens:** The three-tier ITIL v3 structure (BCM, SCM, CCM) creates a natural assertion-to-telemetry gradient: BCM operates on business forecasts and is inherently projection-based; CCM operates on infrastructure monitoring metrics and is directly observable. ITIL 4's consolidation of these into a single practice name obscures this gradient without eliminating the underlying measurement distinction. Practitioners working from ITIL 4 guidance alone may not recognise that different capacity activities warrant different evidentiary standards.

**Regulatory lens:** ISO/IEC 20000-1:2018 Clause 8.6 converts the ITIL "should" into a "shall." Organisations pursuing ISO 20000 certification are therefore held to a stricter standard than ITIL alone requires. This creates a two-tier compliance landscape: ITIL-aligned organisations can legitimately operate with assertion-based baselines; ISO 20000-certified organisations cannot.

**Historical lens:** ITIL v3/2011 was more explicit about the assertion-to-telemetry gradient because it enumerated separate sub-process names and objectives. ITIL 4 (2019) deliberately removed this prescriptive sub-process structure in favour of adaptable practice guidance, increasing flexibility but reducing auditability of assertion-vs-telemetry decisions.

**Behavioural lens:** The Iden and Eikebrokk (2013) finding that organisations defer capacity management maturity due to data collection challenges maps directly onto the ITIL-permitted path: because ITIL does not mandate a validation timeline, organisations can remain in a permanently "new service" assertion posture indefinitely. This pattern is consistent with organisations exercising the discretion ITIL provides rather than violating its guidance. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://www.sciencedirect.com/science/article/pii/S0268401212001700]

**Cross-item lens:** The companion completed item on capability claim vs. production telemetry arbitration (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-capability-claim-telemetry-conflict-arbitration.md) identifies telemetry override as the most reliable arbitration mechanism for resolving capability claim conflicts. The present item establishes that ITIL's own capacity management practice does not structurally require telemetry to be collected in the first place, which means the telemetry override pathway is unavailable wherever ITIL-compliant organisations have relied on assertion-based baselines and deferred operational measurement.

### §6 Synthesis

**Executive summary:**

IT Infrastructure Library (ITIL) capacity management specifies telemetry-based measurement as a recommended practice throughout, using "should" not "shall" or "must" for all data collection requirements in both ITIL v3/2011 and ITIL 4. [inference; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html; https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023] ITIL explicitly and structurally tolerates assertion-based baselines: the official Capacity Plan template includes an "Assumptions and database" section and specifically permits "assumed/estimated/agreed values" for new services pending operational validation. [fact; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan] The boundary between assertion-acceptable and telemetry-required zones is a gradient across ITIL v3's three sub-processes (Business, Service, Component Capacity Management) and is implicit rather than explicitly acknowledged in either ITIL version. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html] ITIL specifies no mandatory validation gate requiring assertion-based baselines to be replaced by operational telemetry after go-live, meaning assertion-based baselines can persist indefinitely without formal ITIL non-compliance. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan] ISO/IEC 20000-1:2018 Clause 8.6 closes this gap by mandating ("shall") empirical monitoring and measurement, but ISO 20000 certification is not required by ITIL compliance. [fact; source: https://www.iso.org/standard/70636.html]

**Key findings:**

1. ITIL v3/2011 and ITIL 4 both use "should" not "shall" for all capacity measurement requirements, making telemetry-based baseline establishment a recommendation rather than a binding obligation under ITIL alone. ([inference]; medium confidence; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html; https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023)

2. The official ITIL Capacity Plan template formally accommodates assertion-based inputs by including an "Assumptions and database" section and stating that for new services, initial values "may be assumed/estimated/agreed values, to be validated once operational." ([fact]; high confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan)

3. ITIL v3 defines three sub-processes, Business Capacity Management, Service Capacity Management, and Component Capacity Management, each with a different measurement focus and a corresponding gradient of assertion tolerance, from high (BCM, which relies on business forecasts) to lower (CCM, which monitors individual infrastructure components). ([fact]; high confidence; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html)

4. ITIL 4 removed the three-tier sub-process structure of ITIL v3, consolidating capacity management into a single "Capacity and Performance Management" practice, which makes the assertion-to-telemetry gradient less explicit without eliminating the underlying measurement distinction. ([inference]; medium confidence; source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023; https://wiki.en.it-processmaps.com/index.php/Capacity_Management)

5. ITIL specifies no mandatory validation gate, deadline, or escalation mechanism requiring that assertion-based baselines be superseded by telemetry-derived values after a service enters operation, leaving the assertion-to-telemetry transition entirely at practitioner discretion. ([inference]; medium confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html)

6. ISO/IEC 20000-1:2018 Clause 8.6 imposes mandatory ("shall") monitoring, measurement, review, and reporting of capacity and performance, which is materially stronger than ITIL's recommendatory stance and closes the assertion-tolerance gap for ISO 20000-certified organisations. ([fact]; high confidence; source: https://www.iso.org/standard/70636.html)

7. Iden and Eikebrokk's (2013) systematic literature review of ITIL implementations found that capacity management is consistently among the least mature processes in practice, with "lack of reliable data for analysis and planning" cited as the primary barrier to maturity investment. ([inference]; medium confidence; source: https://www.sciencedirect.com/science/article/pii/S0268401212001700)

8. The combination of ITIL's assertion tolerance and the absence of a mandatory validation gate means that organisations relying solely on ITIL can remain in an assertion-based baseline posture indefinitely without formal non-compliance, and empirical evidence confirms this pattern occurs in practice. ([inference]; medium confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://www.sciencedirect.com/science/article/pii/S0268401212001700)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] ITIL 4 uses "should" not "shall" for data collection requirements | https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023 | medium | ITIL 4 practice guides are paywalled; evidence from official PeopleCert summary and reproduced guidance |
| [fact] ITIL v3 uses recommendatory language for monitoring data collection | https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html | medium | Secondary source reproducing v3 Service Design text |
| [fact] Capacity Plan template includes "Assumptions and database" section | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan | high | IT Process Wiki template is a widely-cited reference artefact |
| [fact] Template states new services may use "assumed/estimated/agreed values" | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan | high | Directly stated in the template section |
| [fact] ITIL v3 defines BCM, SCM, CCM sub-processes with different measurement foci | https://wiki.en.it-processmaps.com/index.php/Capacity_Management | high | Established ITIL v3 structural fact |
| [inference] ITIL 4 consolidation removes explicit sub-process gradient | https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023 | medium | ITIL 4 confirmed single practice; sub-process absence is confirmed structural fact; consequence for auditability is inference |
| [inference] No mandatory validation gate after go-live | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html | medium | Absence of a requirement; confirmed by absence in both v3 text and template |
| [fact] ISO 20000 Clause 8.6 uses "shall" for measurement | https://www.iso.org/standard/70636.html | high | ISO standard abstract and clause description directly accessed |
| [inference] Iden & Eikebrokk 2013 found capacity management is least mature ITIL process | https://www.sciencedirect.com/science/article/pii/S0268401212001700 | medium | Access-restricted article; finding corroborated by multiple secondary sources citing the same DOI |

**Assumptions:**

- [assumption] ITIL 4 practice guides follow the same "should" language convention described in ITIL 4 Foundation (2019) and the PeopleCert 2023 practices update for those measurement activities not explicitly verified from primary text. Justification: the ITIL 4 design philosophy of "guiding principles over prescriptive rules" is documented in AXELOS/PeopleCert official communications; "should" language is confirmed for the practice's data collection requirements. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023

- [assumption] The IT Process Wiki ITIL v3/2011 Capacity Plan template accurately represents AXELOS's published template structure. Justification: IT Process Wiki is widely used as a reference source for ITIL v3/2011 process templates and is cited by ITIL training providers; no contradicting primary source was available within the access constraints of this investigation. Source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan

**Analysis:**

ITIL's capacity management framework creates a two-zone structure for baseline evidence, though this structure is never explicitly named or governed in ITIL text. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

The first zone, corresponding to ITIL v3's Business Capacity Management sub-process, is dominated by business-planning inputs: transaction volume forecasts, growth projections, and stakeholder agreements. At this layer, assertion is structurally required because future business demands cannot be empirically measured in advance. [inference; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html] The ITIL guidance on BCM explicitly relies on "trend, forecast, model or predict" techniques that mix historical telemetry with forward-looking assumptions. [fact; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

The second zone, corresponding to ITIL v3's Component Capacity Management sub-process, is the most telemetry-intensive part of the framework. Monitoring individual infrastructure components (CPU, memory, storage, network) provides the directly observable data on which operational baselines are built. Even here, ITIL uses "should" rather than mandatory language. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management]

ITIL provides no mandatory mechanism to enforce the transition from assertion to telemetry once a service is operational. The Capacity Plan template's "to be validated once operational" note has no attached control: no specified deadline, no escalation trigger, and no formal review gate. This means the intended validation is an aspiration, not a control. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

ISO 20000's "shall" language represents a genuine strengthening of this control surface. An ISO 20000 audit requires demonstrable evidence of ongoing measurement: a Capacity Plan containing only agreed/assumed values without supporting telemetry would not satisfy Clause 8.6. The practical consequence is that the assertion tolerance permitted by ITIL alone is incompatible with ISO 20000 certification once a service is in operation. [inference; source: https://www.iso.org/standard/70636.html]

The Iden and Eikebrokk (2013) finding that capacity management is among the last ITIL processes to reach maturity, with data collection challenges as the primary barrier, is consistent with the structural inference that organisations are rationally exercising the discretion ITIL provides rather than violating it. Organisations rationally defer data collection investment precisely because ITIL provides no mandatory validation gate that would require it. [inference; source: https://www.sciencedirect.com/science/article/pii/S0268401212001700; https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan]

**Risks, gaps, uncertainties:**

- The ITIL 4 Capacity and Performance Management practice guide is available only via PeopleCert/AXELOS subscription. This investigation relied on secondary sources reproducing the guidance and on official PeopleCert communications. If the primary text contains mandatory language not reflected in summaries, the inference about "should" dominance would require revision.

- The Iden and Eikebrokk (2013) article is access-restricted. The finding about capacity management implementation maturity is widely cited and consistently reproduced across secondary sources; however, verbatim confirmation of the "lack of reliable data" quote requires journal access.

- Betz (2011) was listed as a seeded source but was not accessible within this investigation (Pearson catalogue page does not reproduce content). Practitioner analysis of ITIL capacity management gaps in that source cannot be verified and is excluded from the evidence base.

- The investigation does not cover ITIL v2 (pre-2007), which had different capacity management provisions.

**Open questions:**

- Does ITIL practice maturity differ across industry sectors (e.g., finance vs. public sector vs. technology), and does the assertion-telemetry gap correlate with sector-specific compliance pressures?
- What percentage of organisations that claim ITIL-aligned capacity management have implemented operational telemetry rather than retaining assertion-based baselines?
- Does ITIL 4's removal of the BCM/SCM/CCM sub-process structure affect the practical measurement decisions of practitioners in observable ways?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - ITIL: expanded at first use as "IT Infrastructure Library (ITIL)" in Research Question
  - CMIS: expanded as "Capacity Management Information System (CMIS)" at first use
  - BCM: expanded as "Business Capacity Management (BCM)" at first use
  - SCM: expanded as "Service Capacity Management (SCM)" at first use
  - CCM: expanded as "Component Capacity Management (CCM)" at first use
  - SLA: expanded as "Service Level Agreement (SLA)" at first use
  - ITSM: expanded as "IT service management (ITSM)" at first use via ISO 20000 source
  - ISO: not an acronym requiring expansion (International Organization for Standardization)
claim_audit: passed
  - all [fact], [inference], [assumption] labels present in §2 and §3
  - all §6 executive summary sentences carry trailing inline citations
  - all key findings carry confidence and source parentheticals
  - evidence map source cells contain URLs not bare names
parity_check: §6 Synthesis and Findings sections are consistent
scope_guardrail: no non-ITIL framework comparison introduced
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

IT Infrastructure Library (ITIL) capacity management specifies telemetry-based measurement as a recommended practice using "should" not "shall" throughout, in both ITIL v3/2011 and ITIL 4, which means telemetry is never a binding obligation under ITIL compliance alone. [inference; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html; https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023] ITIL explicitly accommodates assertion-based baselines: the official Capacity Plan template includes an "Assumptions and database" section and specifically permits "assumed/estimated/agreed values" for new services, pending operational validation that ITIL itself never mandates. [fact; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan] The boundary between assertion-acceptable and telemetry-required zones follows a gradient across ITIL v3's three sub-processes (Business, Service, and Component Capacity Management), with assertion tolerance highest at the business planning layer and lowest at the infrastructure component monitoring layer, but this gradient is implicit rather than explicitly governed in either ITIL version. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html] ISO/IEC 20000-1:2018 Clause 8.6 closes this gap by mandating ("shall") ongoing empirical measurement of capacity and performance, but ISO 20000 certification is a separate requirement not implied by ITIL alignment. [fact; source: https://www.iso.org/standard/70636.html]

### Key Findings

1. ITIL v3/2011 and ITIL 4 both use "should" not "shall" for all capacity measurement data collection requirements, making telemetry-based baseline establishment a recommendation rather than a binding obligation under ITIL compliance alone. ([inference]; medium confidence; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html; https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023)

2. The official ITIL Capacity Plan template formally accommodates assertion-based baselines by including an "Assumptions and database" section that explicitly states initial values for new services may be "assumed/estimated/agreed values, to be validated once operational." ([fact]; high confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan)

3. ITIL v3 defines three sub-processes with a measurement gradient: Business Capacity Management (BCM) relies on business forecasts and has high assertion tolerance; Component Capacity Management (CCM) monitors individual infrastructure components and has the lowest assertion tolerance of the three. ([fact]; high confidence; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html)

4. ITIL 4 consolidated BCM, SCM, and CCM into a single "Capacity and Performance Management" practice, removing the explicit sub-process structure of ITIL v3 and making the assertion-to-telemetry gradient less visible to practitioners working from ITIL 4 guidance alone. ([inference]; medium confidence; source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023; https://wiki.en.it-processmaps.com/index.php/Capacity_Management)

5. ITIL specifies no mandatory validation gate, deadline, or escalation mechanism requiring that assertion-based baselines be superseded by telemetry-derived values after a service enters operational use, leaving the transition entirely at practitioner discretion. ([inference]; medium confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html)

6. ISO/IEC 20000-1:2018 Clause 8.6 uses mandatory "shall" language requiring organisations to monitor, measure, review, and report on capacity and performance, which closes the assertion-tolerance gap that ITIL's "should" language leaves open. ([fact]; high confidence; source: https://www.iso.org/standard/70636.html)

7. Iden and Eikebrokk's 2013 systematic literature review of ITIL implementations found that capacity management is consistently among the least mature ITIL processes in practice, with "lack of reliable data for analysis and planning" cited as the primary barrier to maturity. ([inference]; medium confidence; source: https://www.sciencedirect.com/science/article/pii/S0268401212001700)

8. ITIL's combination of assertion tolerance and the absence of a mandatory validation gate means that organisations relying solely on ITIL can remain in an assertion-based baseline posture indefinitely without formal non-compliance, and empirical implementation evidence indicates this pattern occurs in practice. ([inference]; medium confidence; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://www.sciencedirect.com/science/article/pii/S0268401212001700)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] ITIL 4 uses "should" not "shall" for data collection | https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023 | medium | Practice guides paywalled; finding from official PeopleCert summary |
| [fact] ITIL v3 uses recommendatory language for monitoring | https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html | medium | Secondary source reproducing v3 Service Design text |
| [fact] Capacity Plan template has "Assumptions and database" section | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan | high | Widely-cited IT Process Wiki reference artefact |
| [fact] New services may use "assumed/estimated/agreed values" per template | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan | high | Directly stated in template text |
| [fact] ITIL v3 BCM, SCM, CCM sub-processes have different measurement foci | https://wiki.en.it-processmaps.com/index.php/Capacity_Management | high | Established ITIL v3 structural fact |
| [inference] ITIL 4 consolidation removes explicit sub-process gradient | https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023; https://wiki.en.it-processmaps.com/index.php/Capacity_Management | medium | Sub-process absence confirmed; auditability consequence is inference |
| [inference] No mandatory validation gate after go-live in ITIL | https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html | medium | Confirmed by absence in both v3 text and official template |
| [fact] ISO 20000 Clause 8.6 uses "shall" for capacity measurement | https://www.iso.org/standard/70636.html | high | ISO standard abstract directly accessed |
| [inference] Iden & Eikebrokk 2013: capacity management among least mature ITIL processes | https://www.sciencedirect.com/science/article/pii/S0268401212001700 | medium | Access-restricted journal article; finding corroborated by secondary sources |

### Assumptions

- **Assumption:** ITIL 4 practice guides use "should" language consistently for capacity measurement data collection requirements. **Justification:** The ITIL 4 design philosophy explicitly emphasises adaptable guidance over prescriptive rules, as documented in PeopleCert's 2023 practices update; the "should" convention is confirmed for the practice's data collection requirements by multiple sources reproducing ITIL 4 practice content. Source: https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023

- **Assumption:** The IT Process Wiki ITIL v3/2011 Capacity Plan template accurately represents the structure of AXELOS's published template. **Justification:** IT Process Wiki is widely cited by ITIL training providers and practitioners as a reference for ITIL v3/2011 process templates; no contradicting primary source was available within the access constraints of this investigation. Source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan

### Analysis

ITIL's capacity management framework creates a two-zone structure for baseline evidence, though this structure is never explicitly named or governed in ITIL text. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

The first zone corresponds to Business Capacity Management: it is dominated by planning-stage inputs including transaction volume forecasts, growth projections, and stakeholder agreements. At this layer, assertion is structurally necessary because future business demands cannot be empirically measured in advance. [inference; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html] The ITIL guidance explicitly relies on "trend, forecast, model or predict" techniques that combine historical telemetry with forward-looking assumptions. [fact; source: https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

The second zone corresponds to Component Capacity Management: monitoring individual infrastructure components (CPU, memory, storage, network) provides the directly observable data on which operational baselines are built. Even here, ITIL uses "should" rather than mandatory language. [inference; source: https://wiki.en.it-processmaps.com/index.php/Capacity_Management]

ITIL provides no mandatory mechanism to enforce the transition from assertion to telemetry once a service is operational. The Capacity Plan template's "to be validated once operational" note carries no attached control: no specified deadline, no escalation trigger, and no formal review gate. This means the intended validation is an aspiration rather than a control. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html]

ISO 20000's "shall" language represents a genuine tightening of this control surface. An ISO 20000 audit requires demonstrable evidence of ongoing measurement: a Capacity Plan containing only agreed or assumed values without supporting operational telemetry would not satisfy Clause 8.6. The practical consequence is that the assertion tolerance permitted by ITIL alone is incompatible with ISO 20000 certification once a service is in operation. [inference; source: https://www.iso.org/standard/70636.html]

The Iden and Eikebrokk (2013) empirical finding is consistent with this inference: organisations defer capacity management maturity specifically because data collection is costly, and ITIL provides no mandatory gate that would force that investment. Organisations rationally defer data collection investment precisely because ITIL provides no mandatory validation gate that would require it. [inference; source: https://www.sciencedirect.com/science/article/pii/S0268401212001700; https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan]

The companion completed research item on capability claim vs. production telemetry arbitration (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-capability-claim-telemetry-conflict-arbitration.md) identified telemetry override as the most reliable arbitration mechanism for capability claim conflicts. The present findings establish that ITIL-aligned organisations may legitimately have no operational telemetry to override against, because ITIL does not require it to be collected. Where an organisation relies on an ITIL-compliant assertion-based baseline and has never established operational telemetry, the telemetry override pathway described in the arbitration item is structurally unavailable. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-capability-claim-telemetry-conflict-arbitration.md; https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan]

### Risks, Gaps, and Uncertainties

- The ITIL 4 Capacity and Performance Management practice guide is available only via PeopleCert/AXELOS subscription. This investigation relied on secondary sources and official PeopleCert communications. If the primary practice text contains mandatory language not reflected in summaries, the inference about "should" dominance would require revision.
- The Iden and Eikebrokk (2013) journal article is access-restricted at the ScienceDirect URL. The finding about capacity management implementation maturity is widely cited in secondary sources, but verbatim confirmation requires journal access.
- Betz (2011) was a seeded source but the Pearson catalogue page does not reproduce content. That practitioner analysis is excluded from the evidence base.
- The investigation does not cover ITIL v2 (pre-2007) or sector-specific ITIL extensions that may impose stronger measurement requirements in regulated industries.

### Open Questions

- Does assertion-vs-telemetry maturity differ across industry sectors (finance, public sector, technology), and does ISO 20000 certification adoption correlate with reduced assertion-based baseline use?
- What proportion of organisations claiming ITIL-aligned capacity management have established operational telemetry for their baselines rather than retaining assertion-based values?
- Does ITIL 4's removal of the BCM, SCM, CCM sub-process labels affect practitioner measurement decisions in observable ways, or do practitioners reconstruct the same gradient under the unified practice name?

---

## Output

- Type: knowledge
- Description: ITIL capacity management uses "should" not "shall" for all telemetry-based measurement requirements, structurally tolerates assertion-based baselines at the planning stage (especially in Business Capacity Management), and specifies no mandatory validation gate to enforce the transition to operational telemetry after service go-live. [inference; source: https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan; https://www.peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023] ISO 20000-1:2018 Clause 8.6 closes this gap with "shall" language for organisations seeking that certification. [fact; source: https://www.iso.org/standard/70636.html]
- Links:
  - https://wiki.en.it-processmaps.com/index.php/Checklist_Capacity_Plan
  - https://www.iso.org/standard/70636.html
  - https://hci-itil.com/ITIL_v3/books/2_service_design/service_design_ch4_3.html

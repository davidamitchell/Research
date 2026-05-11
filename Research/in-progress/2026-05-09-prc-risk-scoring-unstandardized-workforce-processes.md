---
review_count: 2
title: "Process-Risk-Control (PRC) scoring impacts from unstandardized workforce processes"
added: 2026-05-09T22:56:47+00:00
status: reviewing
priority: high
blocks: []
tags: [organisation, workflow, organisational-design]
started: 2026-05-11T11:45:15+00:00
completed: ~
output: []
cites: [2026-05-09-basel-iso-nist-shadow-workforce-risk-classification, 2026-05-09-cobit-cmmi-defined-process-risk-mitigation]
related: [2026-05-09-key-person-dependency-basel-risk-linkage]
superseded_by: ~
supersedes: 2026-05-09-enterprise-risk-workforce-shadow-systems
item_type: primary
confidence: medium
versions: []
---

# Process-Risk-Control (PRC) scoring impacts from unstandardized workforce processes

## Research Question

How should inherent risk, meaning exposure before relying on controls, and control effectiveness, meaning the demonstrated reliability of the mitigating control, scores in a PRC library change when workforce and skills processes are undocumented, unstandardized, or partially manual?

## Scope

**In scope:**
- PRC scoring logic implications of process immaturity
- Evidence thresholds for score adjustments
- Workforce process examples where scoring distortions occur

**Out of scope:**
- Building a full quantitative model
- Enterprise-specific risk appetite setting

**Constraints:** Use auditable scoring rationale and align with public risk/control framework language.

## Context

Risk libraries can understate exposure when they assume process standardization that does not exist in practice, especially when workforce data or approvals depend on local spreadsheets, undocumented handoffs, or team-specific tacit knowledge. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d515.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html]

## Approach

1. Define scoring assumptions that fail under process immaturity.
2. Develop adjustment criteria for inherent risk and control effectiveness.
3. Propose documentation minimums required to justify lower risk scores.

## Sources

- [x] [Basel Committee on Banking Supervision (2013) Principles for effective risk data aggregation and risk reporting](https://www.bis.org/publ/bcbs239.htm) - automation, spreadsheet, and control-consistency expectations
- [x] [Basel Committee on Banking Supervision (2021) Revisions to the Principles for the Sound Management of Operational Risk](https://www.bis.org/bcbs/publ/d515.htm) - operational-risk definition and inherent-risk identification expectations
- [x] [Basel Committee on Banking Supervision (2021) Principles for operational resilience](https://www.bis.org/bcbs/publ/d516.htm) - critical-operations dependency and continuity-trigger language
- [x] [International Organization for Standardization (2018) ISO 31000 Risk management](https://www.iso.org/iso-31000-risk-management.html) - risk principles, monitoring, and continual-improvement framing
- [x] [National Institute of Standards and Technology (2018) Risk Management Framework for Information Systems and Organizations](https://doi.org/10.6028/NIST.SP.800-37r2) - structured categorise-select-implement-assess-authorise-monitor cycle
- [x] [National Institute of Standards and Technology (2024) The NIST Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) - repeatable-policy threshold, governance, and training expectations
- [x] [Public Company Accounting Oversight Board (2024) Auditing Standard (AS) 2201 An Audit of Internal Control Over Financial Reporting That Is Integrated with An Audit of Financial Statements](https://pcaobus.org/standards/auditing-standards/details/AS2201) - evidence sufficiency, risk-based control testing, and process-complexity assessment
- [x] [Capability Maturity Model Integration Institute Levels of Capability and Performance](https://cmmiinstitute.com/learning/appraisals/levels) - managed versus defined process thresholds
- [x] [Souza Neto et al. (2019) Defining target capability levels in Control Objectives for Information and Related Technologies (COBIT) 2019: a proposal for refinement](https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement) - public COBIT capability-level characteristics
- [x] [Mitchell (2026) Basel Committee on Banking Supervision (BCBS), International Organization for Standardization (ISO), and National Institute of Standards and Technology (NIST): classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html) - prior completed item on shadow workforce-system classification
- [x] [Mitchell (2026) Control Objectives for Information and Related Technologies (COBIT) and Capability Maturity Model Integration (CMMI): process-definition requirements for risk mitigation](https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html) - prior completed item on defined-process minimums
- [x] [Mitchell (2026) Key-person dependency and Basel execution, delivery, and process-management risk linkage](https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html) - prior completed item on single-person workforce dependency as Basel-classified exposure

## Related

- [Mitchell (2026) Basel Committee on Banking Supervision (BCBS), International Organization for Standardization (ISO), and National Institute of Standards and Technology (NIST): classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)
- [Mitchell (2026) Control Objectives for Information and Related Technologies (COBIT) and Capability Maturity Model Integration (CMMI): process-definition requirements for risk mitigation](https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html)
- [Mitchell (2026) Key-person dependency and Basel execution, delivery, and process-management risk linkage](https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How should inherent-risk and control-effectiveness scores in a Process-Risk-Control (PRC) library change when workforce and skills processes are undocumented, unstandardized, or partially manual?
- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://pcaobus.org/standards/auditing-standards/details/AS2201; https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] Working definitions for this item: inherent risk means the exposure present before relying on the mitigating control, control effectiveness means how reliably the control can be shown to reduce that exposure, and defined-process threshold means the point at which execution uses organizational standards and assets rather than only local practice.
- Scope: Translate public framework language into auditable PRC scoring logic for process immaturity, evidence thresholds, and minimum documentation conditions, without building a quantitative model or setting enterprise-specific risk appetite.
- Constraints: Primary and official framework sources first, completed-item cross-reference required, Uniform Resource Locator (URL)-backed citations only, and every abbreviation expanded on first use in the document.
- Output: knowledge item with mirrored synthesis and Findings sections, explicit scoring rules, an Evidence Map, and documentation minimums for lower scores.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] Prior completed-item sweep found adjacent repository work that already classifies shadow workforce tooling as operational risk, defines the managed-to-defined process threshold, and maps single-person dependency into Basel execution and resilience surfaces, but none of those items turns the evidence into PRC score-adjustment rules.

### §1 Question Decomposition

- **Root question:** How should a PRC library score workforce-process risk when the process is undocumented, unstandardized, or partially manual?
- **A. Inherent-risk baseline**
  - A1. Which assumptions behind a low or moderate inherent-risk score fail when a workforce process is undocumented?
  - A2. Which assumptions fail when the process is only locally standardized rather than organization-standardized?
  - A3. Which assumptions fail when execution depends on spreadsheets, desktop databases, or other manual steps?
- **B. Control-effectiveness baseline**
  - B1. What minimum evidence is needed before a control over the workforce process can be called repeatable rather than ad hoc?
  - B2. What higher threshold is needed before the control can be called durable or strong rather than merely present?
  - B3. How should manual but documented controls be differentiated from undocumented manual work?
- **C. Documentation minimums**
  - C1. Which documents or artifacts prove scope, ownership, and standard steps?
  - C2. Which artifacts prove trained execution, monitoring, and evidence retention?
  - C3. Which artifacts justify lowering a score instead of only avoiding a worst-case score?
- **D. PRC synthesis**
  - D1. What inherent-risk floor is supportable for undocumented, unstandardized, and partially manual material workforce processes?
  - D2. What cap on control effectiveness is supportable at each maturity state?
  - D3. Which workforce-process characteristics require a further upward adjustment because they affect critical operations, access, staffing, or reporting?

### §2 Investigation

- [fact; source: https://www.iso.org/iso-31000-risk-management.html] International Organization for Standardization (ISO) publishes enough public summary material to support principles-level claims about ISO 31000, but the full standard text is paywalled, so ISO claims in this item stay at the principles and framework level rather than clause-by-clause interpretation.
- [fact; source: https://www.bis.org/bcbs/publ/d515.htm] Basel Committee on Banking Supervision (BCBS) defines operational risk as the risk of loss resulting from inadequate or failed internal processes, people and systems or from external events.
- [fact; source: https://www.bis.org/bcbs/publ/d515.htm] Basel Committee on Banking Supervision (BCBS) Principle 6 requires comprehensive identification and assessment of operational risk inherent in all material products, activities, processes, and systems so that inherent risks are understood before relying on them.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision (BCBS) 239 says risk data should be aggregated on a largely automated basis so as to minimize the probability of errors.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision (BCBS) 239 states that where a bank relies on manual processes and desktop applications such as spreadsheets and databases, it should have effective mitigants in place and other effective controls consistently applied across the bank's processes.
- [fact; source: https://www.bis.org/bcbs/publ/d516.htm] Basel Committee on Banking Supervision (BCBS) operational-resilience guidance defines tolerance for disruption and says business-continuity plans should address disruption that impacts key personnel and define triggers for invoking the bank's business-continuity plan.
- [fact; source: https://www.iso.org/iso-31000-risk-management.html] International Organization for Standardization (ISO) 31000 describes risk management as a comprehensive approach to identifying, analysing, evaluating, treating, monitoring, and communicating risks across an organization.
- [fact; source: https://doi.org/10.6028/NIST.SP.800-37r2] National Institute of Standards and Technology (NIST) Special Publication 800-37 describes the Risk Management Framework as a disciplined, structured, and flexible process that includes information security categorization, control selection, implementation, assessment, authorization, and continuous monitoring.
- [fact; source: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] National Institute of Standards and Technology (NIST) Cybersecurity Framework 2.0 describes Tier 3, Repeatable, as a state where risk-management practices are formally approved and expressed as policy, defined, implemented as intended, reviewed, and regularly updated.
- [fact; source: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] National Institute of Standards and Technology (NIST) Cybersecurity Framework 2.0 also states that personnel need awareness, knowledge, skills, and training to perform their risk-management tasks effectively.
- [fact; source: https://cmmiinstitute.com/learning/appraisals/levels] Capability Maturity Model Integration (CMMI) level 2, Managed, requires a simple but complete set of practices that address the full intent of the practice area and identify and monitor progress toward performance objectives.
- [fact; source: https://cmmiinstitute.com/learning/appraisals/levels] Capability Maturity Model Integration (CMMI) level 3, Defined, builds on level 2 by using organizational standards and tailoring, requiring projects to use and contribute to organizational assets and to focus on both project and organizational objectives.
- [fact; source: https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] Public Control Objectives for Information and Related Technologies (COBIT) 2019 guidance says level 2 is a basic yet complete set of activities, while level 3 uses organizational assets and typically well-defined processes.
- [fact; source: https://pcaobus.org/standards/auditing-standards/details/AS2201] Public Company Accounting Oversight Board (PCAOB) Auditing Standard (AS) 2201 says risk assessment underlies the entire control audit, that more audit attention should be devoted to higher-risk areas, and that the type and extent of available evidence related to control effectiveness affects the necessary procedures.

#### Prior completed-item sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] The nearest completed items establish that unmanaged workforce tooling is already an operational-risk problem, that sustainable mitigation begins only once the process is organization-standardized and evidenced, and that single-person execution concentration is a Basel-classified exposure rather than a mere staffing inconvenience.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html] The remaining gap is therefore a scoring question: how to convert those classifications and maturity thresholds into inherent-risk floors and control-effectiveness caps inside a PRC library.

#### A. Inherent-risk assumptions that fail under process immaturity

- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html] A low inherent-risk score assumes that the process path is known, stable, and governable enough for uncertainty to stay bounded; undocumented execution breaks that assumption because the process is no longer fully identifiable, assessable, or monitorable as a defined internal process.
- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] A moderate inherent-risk score often assumes at least a complete and consistently performed process, but local or manager-specific standardization falls short of that assumption when the organization lacks shared assets, standard tailoring rules, and defined evidence of execution.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] A partially manual process adds extra error, delay, opacity, and continuity exposure when material decisions depend on spreadsheet logic, desktop databases, or one person's tacit workflow, so a manual workforce process usually deserves a higher inherent-risk score than an otherwise equivalent automated one.

#### B. Control-effectiveness assumptions that fail under process immaturity

- [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] A control cannot credibly be scored as strong merely because someone performs it today; level 2 evidence supports that the process is complete and monitored, while level 3 evidence supports that the process is defined beyond one team and backed by organizational assets.
- [inference; source: https://pcaobus.org/standards/auditing-standards/details/AS2201; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] Where available evidence is thin, informal, or team-specific, the control-effectiveness score should fall because evidence sufficiency, policy approval, review, and trained execution are part of what makes a control reliable rather than merely described.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://pcaobus.org/standards/auditing-standards/details/AS2201] Manual controls can justify a moderate score when they are documented, independently reviewable, and consistently evidenced, but they should not receive a strong score for a material workforce process if execution still depends on local spreadsheets or desktop applications without consistently applied mitigants.

#### C. Documentation minimums for lower scores

- [fact; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] The first durable threshold in both Capability Maturity Model Integration (CMMI) and Control Objectives for Information and Related Technologies (COBIT) is a defined process that uses organizational standards and assets rather than only a complete local practice.
- [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://pcaobus.org/standards/auditing-standards/details/AS2201; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] The minimum evidence set to justify lowering scores therefore includes documented scope and purpose, a named owner, standard steps and inputs or outputs, approved local tailoring rules, retained execution evidence, trained participants, review cadence, and a method for updating the common process when exceptions or failures occur.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] If the workforce process feeds critical operations, access decisions, staffing allocation, regulatory attestations, or risk reporting, the evidence threshold should be stricter because continuity and data-integrity failures propagate beyond one team's workflow.

#### D. PRC scoring synthesis

- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html] For a material workforce process, undocumented or purely intuitive execution should move inherent risk upward from the score used for a documented, organization-standard process, because the process itself is inadequately understood and therefore not yet fully assessable.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] A further upward adjustment is justified when the process remains partially manual, relies on spreadsheets or desktop databases, or depends on one person's tacit knowledge, especially when the process supports critical operations or risk reporting.
- [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html] Control effectiveness should be capped at weak until the process is at least complete, monitored, and evidenced, and capped at moderate until it reaches the defined-process threshold with organizational standards, trained execution, and shared assets.
- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] This item assumes the workforce process is material to operational delivery, access, staffing, reporting, or continuity; if the process is trivial and local only, the same maturity logic still applies but the inherent-risk uplift may be smaller.

### §3 Reasoning

- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html] The framework evidence points in the same direction: risk rises when the organization cannot clearly identify, evaluate, monitor, and communicate how a material process actually operates.
- [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] The maturity evidence also points in the same direction: a complete local practice and a defined organizational process are different states, with the durable threshold beginning only at the defined state.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://pcaobus.org/standards/auditing-standards/details/AS2201; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] PRC scoring should therefore separate three cases rather than two: undocumented or intuitive processes, documented but still manual or local processes, and organization-defined processes with evidence, policy, review, and training.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm; https://cmmiinstitute.com/learning/appraisals/levels] Because manuality, spreadsheet dependence, and key-person concentration add distinct failure modes beyond mere lack of documentation, they justify an extra inherent-risk uplift even after a process becomes documented.

### §4 Consistency Check

- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm; https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement] The sources do not conflict on the main conclusion: undocumented and locally improvised workforce processes increase inherent exposure, while stronger control scores require evidence of complete execution first and organization-defined execution after that.
- [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] The main ambiguity is not whether immaturity matters, but how much numeric uplift or downgrade any one enterprise should choose, because public frameworks define conditions and thresholds but not a universal PRC score scale.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://pcaobus.org/standards/auditing-standards/details/AS2201] The proposed band adjustments are therefore inferential scoring rules grounded in framework logic and evidence sufficiency, not quoted regulatory numbers.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] Operational lens: workforce processes that affect staffing, approvals, access, or capability reporting are not just administrative routines when they feed critical operations or risk reporting, because failure in those processes can become a continuity and data-integrity issue.
- [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] Governance lens: the strongest signal that a score may be lowered is not the age of the process but the presence of policy-backed standards, trained participants, review, and shared organizational assets.
- [inference; source: https://pcaobus.org/standards/auditing-standards/details/AS2201; https://www.bis.org/publ/bcbs239.htm] Assurance lens: a control without preserved evidence may still be happening, but it is difficult to defend as effective in an audit or review context, so PRC scoring should treat missing evidence as a control-strength problem rather than as a documentation inconvenience.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html] Cross-item lens: this item extends earlier repository findings by showing that shadow systems and key-person dependency do not only change classification language, they also require explicit PRC score penalties unless the process has crossed the defined-process threshold.

### §6 Synthesis

**Executive summary:**

Material workforce processes that are undocumented, unstandardized, or partly manual should be scored as higher inherent risk and lower control effectiveness than an equivalent organization-defined process, because the evidence base shows that process opacity, manual handling, and local variation increase uncertainty, error probability, and continuity dependence. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.iso.org/iso-31000-risk-management.html] For a material process, undocumented or purely intuitive execution should move inherent risk upward from the standardized baseline, and spreadsheet-dependent, desktop-database-dependent, or single-person-dependent execution should usually justify a further upward adjustment when the process affects reporting, access, staffing, or critical operations. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] Control effectiveness should be capped at weak until the process is complete, monitored, and evidenced, and capped at moderate until it reaches the defined-process threshold with organizational standards, trained participants, review, and shared assets. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://pcaobus.org/standards/auditing-standards/details/AS2201] The first defensible basis for lower PRC scores is therefore documented, organization-backed repeatability rather than manager reassurance or long habit. [inference; source: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html]

**Key findings:**

1. **A material workforce process that is undocumented or mainly intuitive should not retain the same inherent-risk score as a documented, organization-defined process, because Basel Committee on Banking Supervision and International Organization for Standardization sources treat poorly understood internal processes as higher uncertainty and higher operational-risk exposure.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html)
2. **A material workforce process that still depends on spreadsheets, desktop databases, or other manual handling should receive an additional inherent-risk uplift beyond the documentation penalty, because Basel Committee on Banking Supervision 239 links manual desktop workflows to higher error risk and requires consistently applied mitigants.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.htm)
3. **Control effectiveness should be capped at weak when the workforce process lacks complete documented steps, named ownership, retained execution evidence, and monitoring against explicit objectives, because Capability Maturity Model Integration level 2 and Public Company Accounting Oversight Board evidence rules make those conditions the first credible baseline for repeatable control operation.** ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://pcaobus.org/standards/auditing-standards/details/AS2201)
4. **Control effectiveness should be capped at moderate rather than strong until the workforce process reaches the defined-process threshold that uses organizational standards, approved tailoring, shared assets, trained participants, and regular review, because both public Control Objectives for Information and Related Technologies guidance and Capability Maturity Model Integration distinguish durable defined execution from merely complete local execution.** ([inference]; medium confidence; source: https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html)
5. **Documentation minimums that justify lowering PRC scores include a stated purpose and scope, named owner, standard steps with inputs and outputs, approved exception or tailoring rules, retained evidence, trained participants, review cadence, and a mechanism for updating the common process after failures or exceptions.** ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://pcaobus.org/standards/auditing-standards/details/AS2201)
6. **Workforce processes that affect critical operations, access control decisions, staffing allocation, regulatory attestations, or risk reporting merit stricter score penalties for immaturity than low-materiality administrative routines, because Basel operational-resilience and risk-data guidance treats those dependencies as wider continuity and data-integrity exposures.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Undocumented material workforce processes require a higher inherent-risk floor than documented organization-defined processes. | https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html | Medium | Process-identification failure |
| [inference] Manual spreadsheet or desktop-database dependence adds a further inherent-risk uplift beyond documentation weakness. | https://www.bis.org/publ/bcbs239.htm | Medium | Error and consistency exposure |
| [inference] Weak control-effectiveness is the maximum defensible score before the process is complete, monitored, and evidenced. | https://cmmiinstitute.com/learning/appraisals/levels; https://pcaobus.org/standards/auditing-standards/details/AS2201 | Medium | First repeatable baseline |
| [inference] Moderate, not strong, is the ceiling until the process uses organization-defined standards and shared assets. | https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html | Medium | Defined-process threshold |
| [inference] Lower PRC scores require a documented evidence set covering owner, steps, evidence, training, review, and update logic. | https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://pcaobus.org/standards/auditing-standards/details/AS2201 | Medium | Score-reduction prerequisites |
| [inference] Critical-operation, access, staffing, and reporting dependencies justify stricter immaturity penalties than low-materiality routines. | https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html | Medium | Wider blast radius |

**Assumptions:**

- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] The PRC library uses ordered qualitative bands such as low, medium, and high for inherent risk and weak, moderate, and strong for control effectiveness, so "one-band uplift" and "score cap" are practical translation rules rather than claims about a universal numeric scale.
- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/bcbs/publ/d516.htm] The workforce processes in view are material to staffing, approvals, access, reporting, or continuity; low-materiality local routines would still follow the same maturity logic but may warrant smaller score movement.

**Analysis:**

The evidence weighs more heavily toward conditions and thresholds than toward numeric scoring formulas, so the scoring rules in this item are inferential translations from public framework language into PRC-library practice rather than quoted supervisory numbers. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] Basel Committee on Banking Supervision sources carry the strongest weight on inherent-risk uplift because they directly address failed internal processes, manual data handling, and continuity exposure. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] Capability Maturity Model Integration, Control Objectives for Information and Related Technologies, and Public Company Accounting Oversight Board sources carry the strongest weight on control-effectiveness caps because they distinguish complete execution from defined organization-backed execution and tie reliability to preserved evidence and review. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://pcaobus.org/standards/auditing-standards/details/AS2201] A plausible rival remedy would be to leave the score unchanged and rely on manager judgement or informal compensating checks, but the cited maturity and evidence sources do not support treating local habit as equivalent to a defined process. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final]

**Risks, gaps, uncertainties:**

- Public framework sources support threshold logic and evidence expectations, but they do not specify a universal numeric PRC score scale, so any exact band size remains an inferential local design choice. [fact; source: https://www.iso.org/iso-31000-risk-management.html; https://www.bis.org/bcbs/publ/d515.htm; https://cmmiinstitute.com/learning/appraisals/levels]
- International Organization for Standardization (ISO) 31000 public access is limited to summary material, so clause-level ISO mapping is weaker than the Basel Committee on Banking Supervision and Capability Maturity Model Integration evidence in this item. [fact; source: https://www.iso.org/iso-31000-risk-management.html]
- The strongest manual-versus-automated control language in this item comes from Basel Committee on Banking Supervision 239 rather than from a workforce-specific standard, so the application to workforce process scoring is a cross-domain inference. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html]

**Open questions:**

- Which concrete ordinal or numeric PRC scale best preserves comparability when one-band and two-band uplifts are translated into enterprise scoring practice?
- Which workforce-process attributes, such as approval authority, access rights, regulatory attestation, or staffing for critical operations, should trigger automatic high-materiality classification in the PRC library?
- What evidence-retention pattern best distinguishes a moderate manual control from a weak manual control for workforce workflows that cannot yet be automated?

### §7 Recursive Review

- Opinion: pass
- Checks: acronym expansion; claim labels and source binding; Findings and §6 parity; uncertainty placement

---

## Findings

### Executive Summary

Material workforce processes that are undocumented, unstandardized, or partly manual should be scored as higher inherent risk and lower control effectiveness than an equivalent organization-defined process, because the evidence base shows that process opacity, manual handling, and local variation increase uncertainty, error probability, and continuity dependence. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.iso.org/iso-31000-risk-management.html] For a material process, undocumented or purely intuitive execution should raise inherent risk above the standardized baseline, and spreadsheet-dependent, desktop-database-dependent, or single-person-dependent execution should usually justify a further upward adjustment when the process affects reporting, access, staffing, or critical operations. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] Control effectiveness should be capped at weak until the process is complete, monitored, and evidenced, and capped at moderate until it reaches the defined-process threshold with organizational standards, trained participants, review, and shared assets. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://pcaobus.org/standards/auditing-standards/details/AS2201] The first defensible basis for lower PRC scores is therefore documented, organization-backed repeatability rather than manager reassurance or long habit. [inference; source: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html]

### Key Findings

1. **A material workforce process that is undocumented or mainly intuitive should not retain the same inherent-risk score as a documented, organization-defined process, because Basel Committee on Banking Supervision and International Organization for Standardization sources treat poorly understood internal processes as higher uncertainty and higher operational-risk exposure.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html)
2. **A material workforce process that still depends on spreadsheets, desktop databases, or other manual handling should receive an additional inherent-risk uplift beyond the documentation penalty, because Basel Committee on Banking Supervision 239 links manual desktop workflows to higher error risk and requires consistently applied mitigants.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.htm)
3. **Control effectiveness should be capped at weak when the workforce process lacks complete documented steps, named ownership, retained execution evidence, and monitoring against explicit objectives, because Capability Maturity Model Integration level 2 and Public Company Accounting Oversight Board evidence rules make those conditions the first credible baseline for repeatable control operation.** ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://pcaobus.org/standards/auditing-standards/details/AS2201)
4. **Control effectiveness should be capped at moderate rather than strong until the workforce process reaches the defined-process threshold that uses organizational standards, approved tailoring, shared assets, trained participants, and regular review, because both public Control Objectives for Information and Related Technologies guidance and Capability Maturity Model Integration distinguish durable defined execution from merely complete local execution.** ([inference]; medium confidence; source: https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html)
5. **Documentation minimums that justify lowering PRC scores include a stated purpose and scope, named owner, standard steps with inputs and outputs, approved exception or tailoring rules, retained evidence, trained participants, review cadence, and a mechanism for updating the common process after failures or exceptions.** ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://pcaobus.org/standards/auditing-standards/details/AS2201)
6. **Workforce processes that affect critical operations, access control decisions, staffing allocation, regulatory attestations, or risk reporting merit stricter score penalties for immaturity than low-materiality administrative routines, because Basel operational-resilience and risk-data guidance treats those dependencies as wider continuity and data-integrity exposures.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Undocumented material workforce processes require a higher inherent-risk floor than documented organization-defined processes. | https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html | Medium | Process-identification failure |
| [inference] Manual spreadsheet or desktop-database dependence adds a further inherent-risk uplift beyond documentation weakness. | https://www.bis.org/publ/bcbs239.htm | Medium | Error and consistency exposure |
| [inference] Weak control-effectiveness is the maximum defensible score before the process is complete, monitored, and evidenced. | https://cmmiinstitute.com/learning/appraisals/levels; https://pcaobus.org/standards/auditing-standards/details/AS2201 | Medium | First repeatable baseline |
| [inference] Moderate, not strong, is the ceiling until the process uses organization-defined standards and shared assets. | https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html | Medium | Defined-process threshold |
| [inference] Lower PRC scores require a documented evidence set covering owner, steps, evidence, training, review, and update logic. | https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final; https://pcaobus.org/standards/auditing-standards/details/AS2201 | Medium | Score-reduction prerequisites |
| [inference] Critical-operation, access, staffing, and reporting dependencies justify stricter immaturity penalties than low-materiality routines. | https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html | Medium | Wider blast radius |

### Assumptions

- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] The PRC library uses ordered qualitative bands such as low, medium, and high for inherent risk and weak, moderate, and strong for control effectiveness, so "upward adjustment" and "score cap" are practical translation rules rather than claims about a universal numeric scale.
- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/bcbs/publ/d516.htm] The workforce processes in view are material to staffing, approvals, access, reporting, or continuity; low-materiality local routines would still follow the same maturity logic but may warrant smaller score movement.

### Analysis

The evidence weighs more heavily toward conditions and thresholds than toward numeric scoring formulas, so the scoring rules in this item are inferential translations from public framework language into PRC-library practice rather than quoted supervisory numbers. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final] Basel Committee on Banking Supervision sources carry the strongest weight on inherent-risk uplift because they directly address failed internal processes, manual data handling, and continuity exposure. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d516.htm] Capability Maturity Model Integration, Control Objectives for Information and Related Technologies, and Public Company Accounting Oversight Board sources carry the strongest weight on control-effectiveness caps because they distinguish complete execution from defined organization-backed execution and tie reliability to preserved evidence and review. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement; https://pcaobus.org/standards/auditing-standards/details/AS2201] A plausible rival remedy would be to leave the score unchanged and rely on manager judgement or informal compensating checks, but the cited maturity and evidence sources do not support treating local habit as equivalent to a defined process. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final]

### Risks, Gaps, and Uncertainties

- Public framework sources support threshold logic and evidence expectations, but they do not specify a universal numeric PRC score scale, so any exact band size remains an inferential local design choice. [fact; source: https://www.iso.org/iso-31000-risk-management.html; https://www.bis.org/bcbs/publ/d515.htm; https://cmmiinstitute.com/learning/appraisals/levels]
- International Organization for Standardization (ISO) 31000 public access is limited to summary material, so clause-level ISO mapping is weaker than the Basel Committee on Banking Supervision and Capability Maturity Model Integration evidence in this item. [fact; source: https://www.iso.org/iso-31000-risk-management.html]
- The strongest manual-versus-automated control language in this item comes from Basel Committee on Banking Supervision 239 rather than from a workforce-specific standard, so the application to workforce process scoring is a cross-domain inference. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html]

### Open Questions

- Which concrete ordinal or numeric PRC scale best preserves comparability when upward adjustments are translated into enterprise scoring practice?
- Which workforce-process attributes, such as approval authority, access rights, regulatory attestation, or staffing for critical operations, should trigger automatic high-materiality classification in the PRC library?
- What evidence-retention pattern best distinguishes a moderate manual control from a weak manual control for workforce workflows that cannot yet be automated?

---

## Output

- Type: knowledge
- Description: PRC scoring guidance for raising inherent-risk floors and capping control-effectiveness ratings when workforce processes are undocumented, team-local, or partly manual. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://cmmiinstitute.com/learning/appraisals/levels; https://pcaobus.org/standards/auditing-standards/details/AS2201]
- Links:
  - https://www.bis.org/publ/bcbs239.htm
  - https://cmmiinstitute.com/learning/appraisals/levels
  - https://pcaobus.org/standards/auditing-standards/details/AS2201

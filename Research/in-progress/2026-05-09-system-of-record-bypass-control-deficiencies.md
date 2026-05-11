---
review_count: 1
title: "Control deficiencies from bypassing designated workforce record platforms"
added: 2026-05-09T22:56:47+00:00
status: reviewing
priority: high
blocks: []
tags: [organisation, workflow]
started: 2026-05-11T12:31:24+00:00
completed: ~
output: []
cites: [2026-05-09-basel-iso-nist-shadow-workforce-risk-classification, 2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts]
related: [2026-05-09-prc-risk-scoring-unstandardized-workforce-processes, 2026-05-09-key-person-dependency-basel-risk-linkage, 2026-04-22-knowledge-curation-governance-for-regulated-ai]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Control deficiencies from bypassing designated workforce record platforms

## Research Question

What control deficiencies are most common when designated workforce record platforms are bypassed by spreadsheet, presentation, and list-based shadow workflows?

## Scope

**In scope:**
- Control design and operating-effectiveness gaps caused by bypass behaviour
- Workforce and skill-tracking process contexts
- Preventive and detective control patterns documented in public frameworks

**Out of scope:**
- Vendor selection decisions
- Enterprise-specific implementation playbooks

**Constraints:** Prioritise framework-backed deficiency patterns and include evidence for prevalence and severity signals.

## Context

Control teams need a concrete deficiency catalog to prioritize remediation and assign ownership. [inference; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.bis.org/publ/bcbs239.htm]

## Approach

1. Identify recurring bypass patterns and associated control failures.
2. Map failures to control objectives across common governance frameworks.
3. Rank deficiencies by impact on integrity, auditability, and operational resilience.

## Sources

- [x] [Bank for International Settlements (2013) Principles for effective risk data aggregation and risk reporting](https://www.bis.org/publ/bcbs239.htm) - primary Basel Committee on Banking Supervision (BCBS) framework for governance, accuracy, completeness, timeliness, and adaptability
- [x] [Bank for International Settlements (2021) Principles for the sound management of operational risk](https://www.bis.org/bcbs/publ/d515.htm) - primary operational-risk framing for failed processes, people, and systems
- [x] [European Central Bank (2024) Guide on effective risk data aggregation and risk reporting](https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en) - supervisory evidence on persistent manual-adjustment, reconciliation, and data-quality weaknesses
- [x] [National Institute of Standards and Technology (2020) Security and Privacy Controls for Information Systems and Organizations](https://doi.org/10.6028/NIST.SP.800-53r5) - primary control catalog for Audit and Accountability, Configuration Management, System and Information Integrity, and Continuous Assessment mappings
- [x] [National Institute of Standards and Technology (2018) Risk Management Framework for Information Systems and Organizations](https://doi.org/10.6028/NIST.SP.800-37r2) - governance and accountability linkage between system controls and mission or business use
- [x] [National Institute of Standards and Technology Glossary provenance](https://csrc.nist.gov/glossary/term/Provenance) - authoritative provenance definition
- [x] [National Institute of Standards and Technology Glossary system of records](https://csrc.nist.gov/glossary/term/System_of_Records) - governance definition for identifier-linked record collections
- [x] [Control Objectives for Information and Related Technologies resources](https://www.isaca.org/resources/cobit) - official Control Objectives for Information and Related Technologies (COBIT) framework landing page
- [x] [Intrenion Control Objectives for Information and Related Technologies 2019 processes](https://www.intrenion.com/framework-isaca-cobit-2019-processes/) - accessible process list for Managed Data, Managed Information Technology Changes, Managed Business Process Controls, and Managed Compliance With External Requirements
- [x] [Microsoft Support Export to Excel from SharePoint or Lists](https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9) - one-way export behaviour and downstream disconnect from the source list
- [x] [Microsoft Support View previous versions of Office files](https://support.microsoft.com/en-us/office/view-previous-versions-of-office-files-5c1e076f-a9c9-41b8-8ace-f77b9642e2c2) - version-history scope for Excel and PowerPoint
- [x] [Microsoft Support Get help with Show Changes in Excel](https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5) - unsupported edits, clearing conditions, and previous-value limits in Excel change history
- [x] [Microsoft Support Work together on PowerPoint presentations](https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d) - collaboration, revision-highlighting limits, and storage conditions for PowerPoint revision data
- [x] [Deloitte Australia Analytics, automation and spreadsheets: Who's in control?](https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html) - control and governance signals for business-user tools outside the central technology framework
- [x] [Deloitte United Kingdom Spreadsheet controls: are your spreadsheets exposing your organisation to unmitigated risks?](https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html) - recurring spreadsheet-control deficiency patterns, including accountability, testing, lifecycle, and knowledge concentration
- [x] [European Spreadsheet Risks Interest Group (EuSpRIG) Research and Best Practice](https://eusprig.org/research-info/research-and-best-practice/) - research summary on spreadsheet error prevalence and common spreadsheet-risk categories
- [x] [Mitchell (2026) Basel Committee on Banking Supervision, International Organization for Standardization, and National Institute of Standards and Technology: classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html) - adjacent completed item that classifies shadow workforce systems as a cross-framework control surface
- [x] [Mitchell (2026) National Institute of Standards and Technology Special Publication 800-53: provenance gaps in workforce shadow artifacts](https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html) - adjacent completed item on provenance and change-history gaps in Microsoft Lists, Excel, and PowerPoint

## Related

- [Mitchell (2026) Basel Committee on Banking Supervision, International Organization for Standardization, and National Institute of Standards and Technology: classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)
- [Mitchell (2026) National Institute of Standards and Technology Special Publication 800-53: provenance gaps in workforce shadow artifacts](https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html)
- [Mitchell (2026) Risk scoring for unstandardized workforce processes](https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What control deficiencies are most common when designated workforce record platforms are bypassed by spreadsheet, presentation, and list-based shadow workflows?
- Scope: Workforce and skill-tracking shadow workflows, framework-backed control deficiencies, and severity ranking by integrity, auditability, and operational resilience; not vendor selection or tenant-specific implementation design.
- Constraints: Primary framework sources first, URL-backed citations only, full-document acronym expansion on first use, and no unsupported frequency ranking claims.
- Output: knowledge item with mirrored section 6 synthesis and Findings sections, ranked Key Findings, Evidence Map, and explicit cross-framework control mapping.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] Prior completed-item sweep found two directly relevant completed items: one classifies shadow workforce workflows as a Basel Committee on Banking Supervision, International Organization for Standardization, and National Institute of Standards and Technology control surface, and one isolates provenance and change-history weaknesses in Microsoft Lists, Excel, and PowerPoint.
- [assumption; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.bis.org/publ/bcbs239.htm] "Most common" is interpreted in this item as the deficiency patterns that recur across the three shadow artifact types and across the cited framework and end-user-computing sources, not as a statistically complete enterprise census of all workforce shadow workflows.

### §1 Question Decomposition

- **Root question:** Which deficiencies recur most often when designated workforce record platforms are bypassed by spreadsheet, presentation, and list-based shadow workflows, and how should they be ranked?
- **A. Framework baseline**
  - A1. Which control objectives do the Basel Committee on Banking Supervision, European Central Bank, National Institute of Standards and Technology, and Control Objectives for Information and Related Technologies frameworks emphasize for authoritative data, change control, accountability, and business-process control?
  - A2. What supervisory or practitioner evidence shows that manual workarounds and shadow tools remain a live governance problem?
- **B. Artifact behaviour**
  - B1. What lineage and source-of-truth breaks occur when Microsoft Lists data is exported or copied into downstream artifacts?
  - B2. What audit and change-history blind spots remain in Excel even when version history exists?
  - B3. What revision and attribution blind spots remain in PowerPoint even when collaborative storage exists?
- **C. Deficiency clustering**
  - C1. Which gaps collapse into the same control-deficiency class across lists, spreadsheets, and presentations?
  - C2. Which classes map most directly to authoritative-source, auditability, change-control, access-and-ownership, data-quality, and resilience objectives?
- **D. Ranking**
  - D1. Which classes have the strongest integrity impact?
  - D2. Which classes most directly impair auditability and non-repudiation?
  - D3. Which classes most directly weaken operational resilience and continuity?

### §2 Investigation

#### A. Framework baseline

- [fact; source: https://www.bis.org/publ/bcbs239.htm] The Basel Committee on Banking Supervision (BCBS) says the 2007 financial crisis showed that many banks could not aggregate risk exposures fully, quickly, and accurately, which materially impaired timely risk decisions.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision Principle 3 requires accurate and reliable risk data aggregated on a largely automated basis so as to minimize the probability of errors.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision Principle 3 also says that where a bank relies on manual processes and desktop applications such as spreadsheets and databases, it should have effective mitigants and consistently applied controls.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision Principle 3 requires reconciliation to source systems and says a bank should strive toward a single authoritative source for each type of risk data.
- [fact; source: https://www.bis.org/publ/bcbs239.htm] Basel Committee on Banking Supervision Principle 4 requires capture and aggregation of all material data, Principle 5 requires timely up-to-date data, and Principle 6 requires adaptable on-demand reporting for stress, internal change, and supervisory requests.
- [fact; source: https://www.bis.org/bcbs/publ/d515.htm] Basel Committee on Banking Supervision operational-risk guidance frames operational risk as the risk of loss from inadequate or failed internal processes, people, and systems.
- [fact; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] The European Central Bank says effective aggregation of risk-related data is an essential precondition for sound decision-making and strong risk governance across strategic, operational, risk, financial, and supervisory reporting uses.
- [fact; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] The European Central Bank says difficulties in data accuracy, integrity, completeness, timeliness, and adaptability are still widely encountered.
- [fact; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] The European Central Bank reports large-scale miscalculations of key risk ratios and limits caused by reconciliation errors, extensive manual adjustments, inconsistent or incomplete underlying data, and weak data-quality controls.
- [fact; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/glossary/term/non_repudiation] National Institute of Standards and Technology (NIST) Special Publication 800-53 requires audit records with event content, generated audit records, documented change control, accurate component inventory, integrity protection, ongoing assessment, and non-repudiation, which the National Institute of Standards and Technology glossary defines as protection against an individual falsely denying having performed an action.
- [fact; source: https://doi.org/10.6028/NIST.SP.800-37r2] National Institute of Standards and Technology Special Publication 800-37 links those controls to organization-level accountability and continuous monitoring.
- [inference; source: https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://www.isaca.org/resources/cobit] Accessible Control Objectives for Information and Related Technologies (COBIT) 2019 materials indicate relevant objectives for Managed Data, Managed Information Technology Changes, Managed Business Process Controls, Managed System of Internal Control, and Managed Compliance With External Requirements.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://doi.org/10.6028/NIST.SP.800-53r5; https://www.intrenion.com/framework-isaca-cobit-2019-processes/] Across the frameworks, bypassing an authoritative workforce record with local artifacts is best treated as a control-design deficiency in authoritative-source control, auditability, change control, data quality, and business-process governance.

#### B. Artifact behaviour

- [fact; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9] Exporting Microsoft Lists data to Excel creates a one-way data connection, and changes made in the Excel table are not sent back to the source list.
- [fact; source: https://support.microsoft.com/en-us/office/view-previous-versions-of-office-files-5c1e076f-a9c9-41b8-8ace-f77b9642e2c2] Version history for Excel and PowerPoint depends on storage in OneDrive or SharePoint.
- [fact; source: https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5] Excel Show Changes does not show chart, shape, or other object edits, PivotTable operations, formatting changes, hidden-cell changes, or filtering changes.
- [fact; source: https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5] Excel change history can be cleared by older clients, unsupported features, uploaded replacement copies, or explicit reset actions, and previous values can be missing for edits made through code or add-ins.
- [fact; source: https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] PowerPoint revision highlighting works only in specific storage and client conditions, and not all revisions are indicated on the slide.
- [fact; source: https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] PowerPoint revision highlighting does not indicate all revision types, including notes-pane changes, deletion of shapes, comment additions, and animation changes.
- [inference; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] Lists, Excel, and PowerPoint each preserve some local history, but each leaves conditions under which edits, copies, or downstream derivatives escape the full authoritative trail.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9] The most important break happens at the derivative boundary, because once a list export or copied deck becomes the working record, the upstream artifact's version history no longer proves the downstream decision path.

#### C. Secondary prevalence and severity signals

- [fact; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html] Deloitte says many business-user tools remain outside the central technology framework, can proliferate as quick tactical fixes, and can increase operational-risk exposure because they are integral to critical processes and decision making.
- [fact; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html] Deloitte identifies recurring spreadsheet-control weaknesses in purpose definition, build quality, testing, accountability, knowledge concentration, and assumption management.
- [fact; source: https://eusprig.org/research-info/research-and-best-practice/] The European Spreadsheet Risks Interest Group (EuSpRIG) summarizes the spreadsheet-risk literature as showing that most spreadsheets contain errors, about half of operational models in large businesses have material defects, and recurring risk categories include human error, fraud opportunity, overconfidence, interpretation error, and poor archiving.
- [inference; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://eusprig.org/research-info/research-and-best-practice/; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] Practitioner and supervisory sources converge on the same pattern: local artifacts become high-risk when they carry consequential decisions without inventory, controlled change, independent review, and durable evidence.

#### D. Deficiency clustering and control mapping

- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] The first recurring deficiency class is authoritative-source and lineage failure: exports, copied workbooks, and copied presentation content sever the link between the designated source record and the downstream working artifact.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] The second recurring deficiency class is incomplete auditability and non-repudiation: shadow artifacts often cannot prove every materially relevant change, previous value, actor, or retained review outcome.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html] The third recurring deficiency class is weak change control, because manual workarounds, local edits, and undocumented assumptions undermine approved change decisions, validation, and retained change records.
- [inference; source: https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://doi.org/10.6028/NIST.SP.800-53r5] The fourth recurring deficiency class is incomplete inventory, ownership, and access governance, because business-user tools outside the central framework are harder to inventory, assign, monitor, and constrain.
- [inference; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9] The fifth recurring deficiency class is data-quality degradation through manual reconciliation, manual adjustment, inconsistent underlying data, and incomplete downstream refresh paths.
- [inference; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://www.bis.org/publ/bcbs239.htm; https://www.bis.org/bcbs/publ/d515.htm] The sixth recurring deficiency class is operational-resilience weakness, because key-person knowledge, manual compilation, and opaque assumptions make the process slower to recover, harder to challenge, and less reliable under stress.

#### E. Ranking by impact

- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] The highest-impact class is authoritative-source and lineage failure because it destabilizes integrity, completeness, auditability, and reconciliation at once.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] The next most direct audit failure is incomplete auditability and non-repudiation because missing or partial change evidence prevents a reviewer from reconstructing who changed what and why.
- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] Data-quality degradation ranks alongside audit failure because reconciliation errors, manual adjustments, and incomplete underlying data can directly create wrong decisions or wrong supervisory indicators.
- [inference; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://www.bis.org/bcbs/publ/d515.htm] Resilience weakness becomes especially severe when the shadow artifact influences access, staffing, attestations, or critical reporting, because process failure then affects continuity at enterprise level.

### §3 Reasoning

- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://www.intrenion.com/framework-isaca-cobit-2019-processes/] The ranking in this item follows cumulative control-surface impact, so deficiency classes that simultaneously break source authority, change evidence, and reconciliation were ranked above classes that mainly weaken ownership or continuity.
- [inference; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] The artifact evidence supports treating these gaps as recurring, because all three shadow artifact types retain only partial local history and each allows materially relevant activity to occur outside a fully authoritative trail.
- [inference; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html] Supervisory and practitioner sources point to the same operating model failure, which strengthens the conclusion that these are common control deficiencies.

### §4 Consistency Check

- [fact; source: https://www.bis.org/publ/bcbs239.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] Cross-source consistency confirmed: Basel Committee on Banking Supervision and European Central Bank sources both treat manual adjustments, incomplete data, and poor aggregation capability as material governance weaknesses.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://www.intrenion.com/framework-isaca-cobit-2019-processes/] Framework mapping confirmed: National Institute of Standards and Technology and accessible Control Objectives for Information and Related Technologies materials both provide change, data, internal-control, and compliance surfaces that match the clustered deficiencies.
- [inference; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d] No internal contradiction remains between the product-behaviour evidence and the ranked deficiency classes; the product details explain why the same classes recur across lists, spreadsheets, and presentations.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.bis.org/publ/bcbs239.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en] From a regulatory lens, system-of-record bypass is serious because it can make risk and workforce data insufficiently accurate, complete, timely, or adaptable for management and supervisory decisions.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/glossary/term/System_of_Records] From an accountability lens, identifier-linked workforce records raise the stakes because incomplete audit trails and uncontrolled copies weaken both governance and privacy duties.
- [inference; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html] From an economic and operating-model lens, shadow workflows persist because they are quick tactical fixes and because their downstream reconciliation, review, testing, and remediation costs are often not priced into the local decision.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] From an adjacent completed-item lens, the same bypass pattern also explains why undocumented workforce processes and single-person spreadsheet ownership deserve risk uplifts even when no incident has yet occurred.

### §6 Synthesis

**Executive summary:**

Bypassing designated workforce record platforms most commonly produces six recurring control deficiencies: broken authoritative-source and lineage control, incomplete audit evidence and non-repudiation, weak change control, incomplete inventory and ownership governance, data-quality drift from manual reconciliation, and resilience weakness from manual and key-person dependence. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html]

These deficiencies are common in this item's sense because they recur across the three shadow artifact types and across both framework and practitioner sources. This item does not claim that one public survey provides a single universal ranking for workforce shadow workflows. [assumption; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/]

The highest-impact deficiency is the loss of a single authoritative record, because once copied artifacts become working records, integrity, completeness, reconciliation, and reviewability degrade together. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

Severity rises further when the shadow workflow informs access, staffing, attestations, or risk reporting, because the same local bypass then affects enterprise governance and operational resilience. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records]

**Key findings:**

1. **The most recurrent deficiency when designated workforce record platforms are bypassed is authoritative-source and lineage failure, because exports, copied workbooks, and copied presentation content detach the working artifact from the source record that should remain authoritative.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html)
2. **Incomplete auditability and non-repudiation are the next most common deficiencies, because materially relevant edits in Excel and PowerPoint can occur outside a complete retained trail of actor, prior value, revision type, and review outcome.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d)
3. **Weak change control is a common downstream deficiency, because shadow artifacts allow undocumented assumptions, manual workarounds, and local edits to bypass approved change decisions, validation expectations, and retained change records.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html)
4. **Inventory, ownership, and access governance deficiencies recur because business-user tools outside the central technology framework are harder to discover, classify, assign, permission, and monitor as controlled process components.** ([inference]; medium confidence; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://doi.org/10.6028/NIST.SP.800-53r5)
5. **Data-quality degradation is a common and often severe deficiency, because manual reconciliation, manual adjustments, one-way refresh paths, and inconsistent underlying data can directly distort reports and decisions and can also slow them.** ([inference]; medium confidence; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9)
6. **Operational-resilience weakness is also common, because spreadsheet and presentation bypasses concentrate process knowledge, prolong manual compilation, and make control execution more fragile during staff turnover, stress events, or urgent management requests.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html)
7. **The same six deficiency classes align strongly across Basel Committee on Banking Supervision, National Institute of Standards and Technology, and European Central Bank control surfaces, and accessible Control Objectives for Information and Related Technologies materials place them in compatible data, change, business-control, and compliance categories.** ([inference]; low confidence; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.intrenion.com/framework-isaca-cobit-2019-processes/)
8. **Severity rises when the bypassed artifact informs access, staffing, attestations, or risk reporting, because the same local workaround then affects privacy, accountability, governance, and operational-resilience outcomes beyond the immediate team.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Authoritative-source and lineage failure is the most recurrent deficiency class. | https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html | medium | Source-of-truth break across derivative artifacts |
| [inference] Incomplete auditability and non-repudiation are the next most common deficiencies. | https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d | medium | Missing change evidence across edit types and clients |
| [inference] Weak change control is a recurring downstream deficiency. | https://doi.org/10.6028/NIST.SP.800-53r5; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html | medium | Approval and validation bypass |
| [inference] Inventory, ownership, and access governance deficiencies recur in business-user tools outside the central technology framework. | https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://doi.org/10.6028/NIST.SP.800-53r5 | medium | Discovery and accountability weakness |
| [inference] Data-quality degradation is common and often severe because manual adjustments and incomplete refresh paths distort outputs. | https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9 | medium | Manual reconciliation and inconsistent inputs |
| [inference] Operational-resilience weakness is a recurring deficiency when bypassed artifacts become critical process components. | https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html | medium | Key-person and manual-dependency exposure |
| [inference] The six deficiency classes align strongly across Basel Committee on Banking Supervision, National Institute of Standards and Technology, and European Central Bank control surfaces, with compatible Control Objectives for Information and Related Technologies categories. | https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.intrenion.com/framework-isaca-cobit-2019-processes/ | low | Cross-framework convergence with secondary COBIT support |
| [inference] Severity rises when the bypassed artifact informs access, staffing, attestations, or risk reporting. | https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records | medium | Broader governance and resilience blast radius |

**Assumptions:**

- [assumption; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/] Public sources are sufficient to rank recurring deficiency classes even though they do not provide a single workforce-specific census with one universal numeric ranking.
- [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://csrc.nist.gov/glossary/term/System_of_Records] The workforce artifacts in view influence consequential decisions such as access, staffing, attestation, or reporting; otherwise the same deficiencies would still exist but some severity judgments would weaken.

**Analysis:**

The evidence was weighted toward primary framework language for control classification and toward Microsoft product documentation for mechanism detail. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9]

The ranking gives first place to authoritative-source and lineage failure because it simultaneously destabilizes source authority, reconciliation, completeness, and downstream reviewability, which then drives the other deficiencies. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

Incomplete auditability and data-quality degradation were ranked next because National Institute of Standards and Technology controls and European Central Bank supervisory findings both show that weak evidence and weak data quality directly impair consequential decisions. [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en]

Weak change control, incomplete inventory and ownership governance, and resilience weakness were treated as tightly coupled but slightly downstream classes, because they are frequently the conditions that allow the authoritative-source, audit, and data-quality failures to persist unchallenged. [inference; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://www.bis.org/bcbs/publ/d515.htm]

The strongest rival interpretation is that the main problem is only spreadsheet error frequency. The cross-framework evidence supports a broader conclusion: bypassed artifacts weaken source authority, evidence retention, governed change, and recoverability at process level. [inference; source: https://eusprig.org/research-info/research-and-best-practice/; https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5]

**Risks, gaps, uncertainties:**

- Public sources do not provide a single workforce-specific prevalence dataset that numerically ranks these six classes across all enterprises, so the ranking in this item is a synthesis built from multiple framework, product, and practitioner sources. [fact; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/]
- Control Objectives for Information and Related Technologies public access is summary-level, so the COBIT contribution here stays at objective-level categorization and does not reach clause-level process-practice quotation. [inference; source: https://www.isaca.org/resources/cobit; https://www.intrenion.com/framework-isaca-cobit-2019-processes/]
- Microsoft documentation explains product behaviour but does not itself quantify how often firms misuse the features in workforce governance settings, so recurrence judgments rely partly on practitioner and supervisory synthesis. [inference; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en]

**Open questions:**

- Which public control frameworks best define quantitative escalation thresholds for when a workforce shadow artifact must be re-platformed back into the designated source system?
- Which detective controls most reliably identify when a copied spreadsheet or presentation has become the real working record?
- How should the ranking change when the bypassed workforce artifact is read-only reference material instead of a write-capable decision artifact?

### §7 Recursive Review

- Review result: pass
- Acronym audit: completed
- Claim-label audit: completed
- Findings and section 6 parity: confirmed
- Cross-reference sweep: repeated against related completed items and incorporated

---

## Findings

### Executive Summary

Bypassing designated workforce record platforms most commonly produces six recurring control deficiencies: broken authoritative-source and lineage control, incomplete audit evidence and non-repudiation, weak change control, incomplete inventory and ownership governance, data-quality drift from manual reconciliation, and resilience weakness from manual and key-person dependence. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html]

These deficiencies are common in this item's sense because they recur across the three shadow artifact types and across both framework and practitioner sources. This item does not claim that one public survey provides a single universal ranking for workforce shadow workflows. [assumption; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/]

The highest-impact deficiency is the loss of a single authoritative record, because once copied artifacts become working records, integrity, completeness, reconciliation, and reviewability degrade together. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

Severity rises further when the shadow workflow informs access, staffing, attestations, or risk reporting, because the same local bypass then affects enterprise governance and operational resilience. [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records]

### Key Findings

1. **The most recurrent deficiency when designated workforce record platforms are bypassed is authoritative-source and lineage failure, because exports, copied workbooks, and copied presentation content detach the working artifact from the source record that should remain authoritative.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html)
2. **Incomplete auditability and non-repudiation are the next most common deficiencies, because materially relevant edits in Excel and PowerPoint can occur outside a complete retained trail of actor, prior value, revision type, and review outcome.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d)
3. **Weak change control is a common downstream deficiency, because shadow artifacts allow undocumented assumptions, manual workarounds, and local edits to bypass approved change decisions, validation expectations, and retained change records.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html)
4. **Inventory, ownership, and access governance deficiencies recur because business-user tools outside the central technology framework are harder to discover, classify, assign, permission, and monitor as controlled process components.** ([inference]; medium confidence; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://doi.org/10.6028/NIST.SP.800-53r5)
5. **Data-quality degradation is a common and often severe deficiency, because manual reconciliation, manual adjustments, one-way refresh paths, and inconsistent underlying data can directly distort reports and decisions and can also slow them.** ([inference]; medium confidence; source: https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9)
6. **Operational-resilience weakness is also common, because spreadsheet and presentation bypasses concentrate process knowledge, prolong manual compilation, and make control execution more fragile during staff turnover, stress events, or urgent management requests.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html)
7. **The same six deficiency classes align strongly across Basel Committee on Banking Supervision, National Institute of Standards and Technology, and European Central Bank control surfaces, and accessible Control Objectives for Information and Related Technologies materials place them in compatible data, change, business-control, and compliance categories.** ([inference]; low confidence; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.intrenion.com/framework-isaca-cobit-2019-processes/)
8. **Severity rises when the bypassed artifact informs access, staffing, attestations, or risk reporting, because the same local workaround then affects privacy, accountability, governance, and operational-resilience outcomes beyond the immediate team.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Authoritative-source and lineage failure is the most recurrent deficiency class. | https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html | medium | Source-of-truth break across derivative artifacts |
| [inference] Incomplete auditability and non-repudiation are the next most common deficiencies. | https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/get-help-with-show-changes-in-excel-a1493bf9-25c3-470a-b970-60eceb0136e5; https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d | medium | Missing change evidence across edit types and clients |
| [inference] Weak change control is a recurring downstream deficiency. | https://doi.org/10.6028/NIST.SP.800-53r5; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html | medium | Approval and validation bypass |
| [inference] Inventory, ownership, and access governance deficiencies recur in business-user tools outside the central technology framework. | https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://doi.org/10.6028/NIST.SP.800-53r5 | medium | Discovery and accountability weakness |
| [inference] Data-quality degradation is common and often severe because manual adjustments and incomplete refresh paths distort outputs. | https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.bis.org/publ/bcbs239.htm; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9 | medium | Manual reconciliation and inconsistent inputs |
| [inference] Operational-resilience weakness is a recurring deficiency when bypassed artifacts become critical process components. | https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/publ/bcbs239.htm; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html | medium | Key-person and manual-dependency exposure |
| [inference] The six deficiency classes align strongly across Basel Committee on Banking Supervision, National Institute of Standards and Technology, and European Central Bank control surfaces, with compatible Control Objectives for Information and Related Technologies categories. | https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://www.intrenion.com/framework-isaca-cobit-2019-processes/ | low | Cross-framework convergence with secondary COBIT support |
| [inference] Severity rises when the bypassed artifact informs access, staffing, attestations, or risk reporting. | https://www.bis.org/bcbs/publ/d515.htm; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en; https://csrc.nist.gov/glossary/term/System_of_Records | medium | Broader governance and resilience blast radius |

### Assumptions

- Public sources are sufficient to rank recurring deficiency classes even though they do not provide a single workforce-specific census with one universal numeric ranking. [assumption; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/]
- The workforce artifacts in view influence consequential decisions such as access, staffing, attestation, or reporting; otherwise the same deficiencies would still exist but some severity judgments would weaken. [assumption; source: https://www.bis.org/bcbs/publ/d515.htm; https://csrc.nist.gov/glossary/term/System_of_Records]

### Analysis

The evidence was weighted toward primary framework language for control classification and toward Microsoft product documentation for mechanism detail. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9]

The ranking gives first place to authoritative-source and lineage failure because it simultaneously destabilizes source authority, reconciliation, completeness, and downstream reviewability, which then drives the other deficiencies. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

Incomplete auditability and data-quality degradation were ranked next because National Institute of Standards and Technology controls and European Central Bank supervisory findings both show that weak evidence and weak data quality directly impair consequential decisions. [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en]

Weak change control, incomplete inventory and ownership governance, and resilience weakness were treated as tightly coupled but slightly downstream classes, because they are frequently the conditions that allow the authoritative-source, audit, and data-quality failures to persist unchallenged. [inference; source: https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://www.intrenion.com/framework-isaca-cobit-2019-processes/; https://www.bis.org/bcbs/publ/d515.htm]

The strongest rival interpretation is that the main problem is only spreadsheet error frequency. The cross-framework evidence supports a broader conclusion: bypassed artifacts weaken source authority, evidence retention, governed change, and recoverability at process level. [inference; source: https://eusprig.org/research-info/research-and-best-practice/; https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5]

### Risks, Gaps, and Uncertainties

- Public sources do not provide a single workforce-specific prevalence dataset that numerically ranks these six classes across all enterprises, so the ranking in this item is a synthesis built from multiple framework, product, and practitioner sources. [fact; source: https://www.deloitte.com/au/en/Industries/financial-services/blogs/analytics-automation-spreadsheets-who-control.html; https://eusprig.org/research-info/research-and-best-practice/]
- Control Objectives for Information and Related Technologies public access is summary-level, so the COBIT contribution here stays at objective-level categorization and does not reach clause-level process-practice quotation. [inference; source: https://www.isaca.org/resources/cobit; https://www.intrenion.com/framework-isaca-cobit-2019-processes/]
- Microsoft documentation explains product behaviour but does not itself quantify how often firms misuse the features in workforce governance settings, so recurrence judgments rely partly on practitioner and supervisory synthesis. [inference; source: https://support.microsoft.com/en-us/office/export-to-excel-from-sharepoint-or-lists-bfb2ea48-6118-4fa9-abb6-cced9424e5d9; https://www.deloitte.com/uk/en/services/consulting-risk/blogs/2023/spreadsheet-controls-are-your-spreadsheets-exposing-your-organisation-to-unmitigated-risks.html; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en]

### Open Questions

- Which public control frameworks best define quantitative escalation thresholds for when a workforce shadow artifact must be re-platformed back into the designated source system?
- Which detective controls most reliably identify when a copied spreadsheet or presentation has become the real working record?
- How should the ranking change when the bypassed workforce artifact is read-only reference material instead of a write-capable decision artifact?

---

## Output

- Type: knowledge
- Description: Produced a framework-backed deficiency catalog for workforce system-of-record bypass, ranked by impact on integrity, auditability, and operational resilience. [inference; source: https://www.bis.org/publ/bcbs239.htm; https://doi.org/10.6028/NIST.SP.800-53r5; https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en]
- Links:
  - https://www.bis.org/publ/bcbs239.htm
  - https://doi.org/10.6028/NIST.SP.800-53r5
  - https://op.europa.eu/en/publication-detail/-/publication/637209da-0c36-11ef-a251-01aa75ed71a1/language-en

---
review_count: 2
title: "At what threshold does Human-in-the-Loop (HITL) oversight in bank compliance operations stop being a meaningful challenge function and become routine acceptance of automated outputs?"
added: 2026-05-20T08:35:44+00:00
status: completed
priority: high
blocks: []
started: 2026-05-20T11:04:10+00:00
completed: 2026-05-20T11:30:57+00:00
output: [knowledge]
themes: [agentic-ai, organisational-design, tools-infrastructure]
cites:
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
  - 2026-04-26-ai-lowcode-governance-enforcement-architecture
related:
  - 2026-04-26-ai-governance-cost-performance-delivery-impact
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 1c8847202ca270c064a2ad838fe889c16fae3925
    changed: 2026-05-20
    progress: progress/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.md
    summary: "Initial completion"
---

# At what threshold does Human-in-the-Loop (HITL) oversight in bank compliance operations stop being a meaningful challenge function and become routine acceptance of automated outputs?

## Research Question

What measurable workload, alert-volume, and staffing thresholds indicate that Human-in-the-Loop (HITL) compliance review is no longer a meaningful challenge function, meaning reviewers mostly accept automated triage without substantive verification, and which operational controls sustain reviewer vigilance when Artificial Intelligence (AI) systems perform most first-pass filtering?

## Scope

**In scope:**
- Quantitative and behavioural indicators of oversight degradation in high-volume review queues.
- Capacity, rest-cycle, and deliberately planted-error testing mechanisms that preserve reviewer challenge capability.
- Auditability of challenge and veto capacity under model-risk governance expectations.
- Mapping to Federal Reserve model-risk expectations and similar supervisory guidance.

**Out of scope:**
- Fully autonomous decisioning with no human review requirement.
- Workforce policy outside operational oversight design.

**Constraints:** Seek evidence that supports threshold-setting and testable governance controls, not only qualitative commentary.

## Context

Bank compliance teams increasingly inherit queues created by sanctions-screening and transaction-monitoring systems. [fact; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf]
Public sanctions-screening studies report false-positive rates above 90 percent, so nominal human presence is not enough unless reviewers retain protected time, authority, and evidence to challenge machine outputs. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

## Approach

1. Identify empirical research on alert overload, over-reliance on automated recommendations (automation bias), and reviewer throughput limits.
2. Define metrics for meaningful challenge capacity, including review depth, overturn rates, time-on-task, and escalation quality.
3. Assess intervention designs such as rest cycles, random challenge sampling, and simulated failure injections that deliberately plant errors.
4. Derive an audit-ready framework for testing and evidencing effective human challenge capacity.

## Sources

- [x] [Office of the Comptroller of the Currency (2026) Model Risk Management: Revised Guidance](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf) - interagency banking guidance on effective challenge, expertise, independence, and ongoing monitoring.
- [x] [European Commission AI Act Service Desk Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) - official human-oversight duties, automation-bias warning, and override or stop rights.
- [x] [Information Commissioner's Office Human Review Toolkit](https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/) - meaningful human review requirements, manageable caseloads, sampling, tolerances, and override logs.
- [x] [General Data Protection Regulation (GDPR) Article 22](https://gdpr-info.eu/art-22-gdpr/) - accessible text of human intervention and contest rights for solely automated decisions.
- [x] [International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) (2023) ISO/IEC 42001](https://www.iso.org/standard/81230.html) - official overview of the Artificial Intelligence Management System (AIMS) standard.
- [x] [Hong Kong Monetary Authority (2023) Transaction Monitoring, Screening and Suspicious Transaction Reporting](https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf) - transaction-monitoring thresholds, backlogs, internal timelines, and sanctions-screening tuning expectations.
- [x] [Goddard et al. (2012) Automation bias: a systematic review of frequency, effect mediators, and mitigators](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) - systematic review of automation-bias mechanisms and mitigations.
- [x] [Kupfer et al. (2023) Check the box! How to deal with automation bias in AI-based personnel selection](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full) - experiment on verification intensity, error briefings, and evidence aggregation.
- [x] [Hemmerich et al. (2025) Understanding vigilance and its decrement](https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full) - review of time-on-task vigilance degradation, including Mackworth's 30-minute drop.
- [x] [Allen and Hatfield (2025) Can Large Language Models (LLMs) Improve Sanctions Screening in the Financial System?](https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf) - Federal Reserve sanctions-screening benchmark with false-positive and manual-review implications.
- [x] [Leeuwenburgh and de Vries (2024) Accuracy improvement in financial sanction screening: is Natural Language Processing (NLP) the solution?](https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/) - open-access study reporting false-positive rates above 90 percent in sanctions screening.
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF) Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - governance, monitoring, testing, and accountability outcomes.
- [x] [When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html) - prior repository item on meaningful human oversight, trigger design, and passive-approval risk.
- [x] [How should human-in-the-loop (HITL) design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html) - prior repository item on queue overload, nominal review indicators, and scaled oversight patterns.
- [x] [What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) - prior repository item on override logging, attributable telemetry, and audit reconstruction.
- [x] [Where should governance enforcement points be implemented within enterprise architecture, and how should controls be applied consistently for AI and low-code systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html) - prior repository item on real stop and override surfaces.
- [x] [What is the cost, performance, and delivery impact of governance controls on AI and low-code development?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html) - prior repository item on review queues, delivery drag, and governance-friction economics.

## Related

- [When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
- [How should human-in-the-loop (HITL) design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
- [What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
- [Where should governance enforcement points be implemented within enterprise architecture, and how should controls be applied consistently for AI and low-code systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html)
- [What is the cost, performance, and delivery impact of governance controls on AI and low-code development?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html)

---

## Research Skill Output

### §0 Initialise

- question: identify the measurable point at which Human-in-the-Loop (HITL) bank-compliance review stops acting as an effective challenge function and becomes routine acceptance of automated triage, then specify controls that keep challenge capacity real.
- in_scope: alert-volume, workload, staffing, time-on-task, challenge-rate, escalation, override, auditability, and supervisory expectations for model-risk and human-oversight design.
- out_of_scope: fully autonomous decisioning, general labour policy, and vendor-by-vendor tool comparison.
- constraints: use full-mode research, prioritise primary supervisory sources, and translate human-factors evidence into bounded operational thresholds rather than treating it as direct banking law.
- output: knowledge
- prior_completed_items: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html, https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html, https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html, https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html, https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html
- source_correction: seeded SR 11-7 link -> OCC Bulletin 2026-13a
- failed_primary_search: direct fetches of the 2011 SR 11-7 landing pages and query `site:federalreserve.gov sr1107 pdf`

### §1 Question Decomposition

- **Root question:** What threshold tells a bank that nominal Human-in-the-Loop (HITL) review has degraded into superficial acceptance of automated triage?
- **A. Supervisory baseline**
  - A1. What do banking and Artificial Intelligence (AI) oversight sources require for review to count as meaningful challenge?
  - A2. Which reviewer attributes matter: authority, competence, independence, time, or logging?
  - A3. Do the sources define explicit thresholds or only operating conditions?
- **B. Queue mechanics**
  - B1. What queue conditions indicate that review capacity has failed?
  - B2. How severe is the false-positive problem in bank screening queues?
  - B3. Which monitoring parameters and internal timelines do supervisors expect firms to tune and test?
- **C. Human-performance mechanics**
  - C1. How do workload, time pressure, and repetitive alerts change reviewer vigilance?
  - C2. Which interface and workflow interventions reduce automation bias?
  - C3. What does time-on-task evidence suggest about uninterrupted review blocks?
- **D. Threshold synthesis**
  - D1. Which indicators can be made auditable in production?
  - D2. Which indicators are universal breach signals, and which must be locally calibrated?
  - D3. Which tests prove that humans still challenge machine output under load?

### §2 Investigation

#### Access and search notes

- source_replacement: OCC Bulletin 2026-13a
- source_access: local Portable Document Format (PDF) extraction

#### A. Supervisory baseline

- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Meaningful human oversight requires reviewers who can understand system limitations, detect anomalies, disregard or reverse outputs, and interrupt processing, and the Information Commissioner's Office (ICO) adds that these reviewers must have knowledge, authority, independence, and a manageable caseload.
- [fact; source: https://gdpr-info.eu/art-22-gdpr/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Human intervention for solely automated decisions must be substantive enough to let a person obtain review and contest the decision, so passive approval does not satisfy the safeguard requirement.
- [fact; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf] Updated interagency banking guidance defines effective challenge as critical analysis by objective experts with appropriate expertise, sufficient independence, and organisational standing to effect change across the model lifecycle.
- [fact; source: https://www.iso.org/standard/81230.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Governance standards outside banking converge on the same operating pattern: named roles, documented monitoring, periodic review, testing, and clear accountability for risk decisions.

#### B. Queue mechanics in bank compliance

- [fact; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf] The Hong Kong Monetary Authority (HKMA) requires banks to tune and test transaction-monitoring rules, scenarios, parameters, and thresholds, and to document clear internal timelines for alert review and escalation.
- [fact; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf] The HKMA states that significant and prolonged alert backlogs may indicate ineffective monitoring systems, resourcing concerns, poor rule or threshold design, or inappropriate customer segmentation, and that senior management or the relevant risk committee should be involved when such backlogs arise.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf] Published banking research reports sanctions-screening false-positive rates above 90 percent, and the Federal Reserve's 2025 benchmark paper treats false positives as a direct source of compliance burden, transaction delay, and manual-review cost, which together make bank screening queues structurally vulnerable to superficial review.
- [fact; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf] The Federal Reserve benchmark finds that Large Language Models (LLMs) reduced sanctions-screening false positives by 92 percent relative to the best fuzzy-matching baseline in the study.
- [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf] That reduction implies that upstream model quality can materially change downstream human-review load.

#### C. Human-performance mechanics

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] Goddard et al. define automation bias as over-reliance on automated advice and identify workload, task complexity, time pressure, trust, and confidence as mediators, while also listing training, explicit awareness of possible system error, confidence information, and showing information rather than recommendations as mitigations.
- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full] Kupfer et al. found that informing decision makers about possible system errors and presenting less aggregated data increased verification intensity and objective decision quality, while a responsibility reminder alone did not produce the same effect.
- [fact; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full] Hemmerich et al. review the vigilance literature and report Mackworth's classic finding that rare-signal detection falls sharply in the first 30 minutes of a 2-hour watch before continuing to decline more gradually.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4307024/] Reliance on automation changes with the distribution of misses and false alarms over time, which means that nominal average model accuracy does not tell a bank whether reviewers will stay attentive in the face of the specific error pattern its queue produces.

#### D. Threshold synthesis

- [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf] No reviewed supervisory source publishes a universal daily alert-count ceiling, so oversight collapse must be detected through the loss of challenge preconditions: manageable caseloads, timely review, effective challenge staffing, and the power to change outcomes.
- [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full] A defensible threshold can therefore be expressed as a capacity ratio, `required challenge minutes / available staffed challenge minutes`, where available minutes exclude breaks, reviewer calibration, second-review sampling, escalation work, and other non-queue tasks needed for substantive review.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full] Reviewer vigilance is more likely to hold when work is organised into shorter review blocks, reviewers are reminded that the system can be wrong, and case evidence is shown in a less aggregated form that forces verification rather than passive acceptance.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html] Banks need synthetic fault injection, planted-error sampling, or structured second review because a zero-override queue can reflect either highly reliable automation or collapsed human challenge, and only tested detection under load separates those cases.

### §3 Reasoning

- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf] The strongest cross-source agreement concerns threshold conditions for meaningful challenge, not a single numeric alert ceiling: reviewer authority, competence, independence, logging, and timely escalation all appear directly in the regulatory texts.
- [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Because supervisors describe backlog, missed timelines, and unmanaged caseload as control failures, the threshold question is better answered as an operating-capacity problem than as a headcount or staffing-ratio rule by itself.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full] Human-factors evidence explains why this is so: repetitive high-volume review reduces vigilance, aggregated dashboards encourage heuristic acceptance, and uninterrupted monitoring erodes detection performance quickly.
- [assumption; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Public sources do not disclose bank-by-bank case-handling times, so each institution must estimate local challenge minutes by alert family from internal operations data before applying the capacity-ratio threshold operationally.

### §4 Consistency Check

- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://gdpr-info.eu/art-22-gdpr/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] The reviewed human-oversight sources are internally consistent in rejecting passive approval as meaningful review.
- [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf] The reviewed banking sources are internally consistent in treating weak challenge staffing, poor threshold tuning, and significant backlog as governance problems rather than unavoidable operational noise.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] The queue-literature and human-performance literature align rather than conflict: very high false-positive environments raise the repetitive monitoring burden that the automation-bias literature identifies as a pathway to superficial review.
- [inference; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full] The 30-minute vigilance signal should be used as a design input for review blocks and staffing assumptions, not as a universal legal limit, because the underlying studies are generic sustained-attention tasks rather than bank-specific production queues.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/] **Technical lens:** Better screening models and better threshold tuning reduce false-positive burden and therefore reduce the risk that human review turns into queue-clearing rather than challenge.
- [fact; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] **Regulatory lens:** Review authority, independence, and the ability to change outcomes remain mandatory even when upstream model quality improves.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html; https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf] **Economic lens:** Prolonged backlog is not only a control failure but also a cost signal, because queues created by poor tuning consume scarce reviewer time that should be reserved for higher-value challenge work.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full] **Behavioural lens:** Training and interface design matter, but they work only when the queue still leaves enough protected time for verification behaviour to occur.

### §6 Synthesis

#### Executive Summary

Human-in-the-Loop (HITL) oversight in bank compliance stops being an effective safeguard once sustained review demand exceeds protected human challenge capacity, producing significant backlog, near-zero verified challenge activity, or uninterrupted monitoring blocks that push reviewers into passive acceptance of automated triage. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]
The evidence does not support a universal daily alert-count ceiling across banks, because supervisory sources specify operating conditions for effective challenge rather than a fixed case quota. [inference; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]
The strongest defensible threshold is therefore a locally calibrated capacity ratio supported by universal breach indicators such as prolonged backlog, missed review timelines, absent override or escalation evidence, and lack of tested second-review or fault-injection controls. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
Banks sustain reviewer vigilance when they reduce false-positive load upstream, preserve shorter review blocks, expose less aggregated case evidence, brief reviewers that the model can be wrong, and log challenge behaviour in a way that can be audited later. [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

#### Key Findings

1. Meaningful bank-compliance oversight requires reviewers who can understand system limits, detect anomalies, disregard or reverse outputs, and interrupt processing, because the reviewed supervisory sources treat authority, competence, independence, and real intervention power as the minimum standard for human challenge. ([fact]; high confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf)
2. No reviewed banking supervisor publishes a universal daily alert-count ceiling, but the Hong Kong Monetary Authority (HKMA) and interagency model-risk guidance treat significant backlog, missed timelines, and ineffective challenge staffing as observable signs that the review control has already failed. ([inference]; high confidence; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/)
3. Sanctions screening gives this failure mode real operational force because published banking research reports false-positive alert rates above 90 percent, and the Federal Reserve's 2025 benchmark paper treats manual review burden and transaction delay as direct consequences of those false positives. ([inference]; medium confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf)
4. Reviewers should not be left in uninterrupted queue-clearing sessions longer than roughly 30 minutes, because vigilance research traces a steep initial drop in rare-signal detection within the first half hour of sustained monitoring before further decline sets in. ([inference]; low confidence; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full)
5. Evidence-rich case presentation matters because informing reviewers that the system can be wrong and showing less aggregated case data increases verification intensity and decision quality more reliably than generic reminders of responsibility. ([fact]; medium confidence; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/)
6. An audit-ready threshold should compare required challenge minutes with available staffed challenge minutes after subtracting breaks, calibration, second-review sampling, and escalation work, because nominal headcount overstates the time available for substantive review. ([inference]; medium confidence; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html)
7. Near-zero override or escalation rates are not proof of safe automation, because the same pattern can arise from reviewer deference, so banks need logged second-review samples or planted-error tests to show that humans still detect machine mistakes under load. ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html)
8. Better screening models and threshold tuning materially reduce the risk of Human-in-the-Loop (HITL) collapse, but they do not remove the need for meaningful human challenge because banking and Artificial Intelligence (AI) oversight rules still require documented competence, accountability, and authority to intervene. ([inference]; medium confidence; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Meaningful oversight requires authority, competence, independence, and real power to override or stop outputs. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf | high | Direct supervisory requirement, not a synthesis-only claim. |
| [inference] Collapse is not defined by a universal alert count but by backlog, missed timelines, and ineffective challenge staffing. | https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/ | high | The sources specify breach indicators rather than a numeric quota. |
| [inference] False-positive alert rates above 90 percent make bank screening queues structurally vulnerable to superficial review. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf | medium | Supported by direct burden evidence plus synthesis about queue effects. |
| [inference] Uninterrupted review blocks longer than roughly 30 minutes raise the risk that challenge behaviour degrades into passive monitoring. | https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full | low | Transfer from vigilance research to bank review design, not a banking regulation. |
| [fact] Error briefings and less aggregated evidence improve verification intensity more than responsibility reminders alone. | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ | medium | Strong behavioural signal from non-banking decision-support studies. |
| [inference] The best operational threshold is a local capacity ratio based on required challenge minutes versus available staffed challenge minutes. | https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html | medium | Derived because public sources define control conditions but not universal staffing formulas. |
| [inference] Zero override rates are ambiguous unless banks run second-review samples or planted-error tests under load. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | Testing and telemetry close an otherwise unobservable governance gap. |
| [inference] Upstream model tuning reduces review burden but cannot substitute for meaningful human challenge controls. | https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf | medium | Technical improvement changes load, not the oversight obligation. |

#### Assumptions

- [assumption; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Each institution can estimate average challenge minutes by alert family from internal case-handling data even though no public cross-bank benchmark set exposes comparable staffing and handling-time distributions.
- [assumption; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] The vigilance-decrement and automation-bias findings are transferable enough to bank compliance review to justify shorter review blocks and verification-oriented interface design, while exact local timings should still be validated in production.

#### Analysis

Banking and Artificial Intelligence (AI) oversight sources are strongest on the conditions for effective human challenge, not on universal numeric queue quotas, so the most defensible answer is a hybrid threshold model rather than a single cases-per-reviewer benchmark. [inference; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]
The human-factors sources explain why these control conditions matter: high-volume repetitive review and time pressure shift people toward heuristic acceptance, while explicit error awareness and less aggregated evidence increase verification behaviour. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full]
That combination supports a threshold policy built from four linked indicators: capacity ratio, backlog and timeline compliance, observed challenge activity such as overrides or escalations, and periodic tested detection through second review or planted errors. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
Alternative remedies such as adding staff, improving the screening model, or redesigning the interface are complements rather than substitutes: more staff helps only if capacity is protected for challenge rather than queue clearing, better models reduce volume but do not remove the oversight obligation, and better interfaces improve verification only when reviewers still have authority and time to use them. [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf]

#### Risks, Gaps, and Uncertainties

- Public sources do not provide a universal bank-by-bank benchmark for alerts per reviewer, challenge minutes per alert family, or acceptable override-rate bands, so the final numeric threshold still requires local calibration. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf]
- Most controlled automation-bias and vigilance studies come from non-banking settings, so the exact size of the degradation effect inside compliance teams remains inferential even though the mechanism is strongly supported. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full]
- Accessible supervisory texts emphasise process quality, evidence, and governance accountability more than they specify any single mandatory testing frequency for planted-error exercises. [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

#### Open Questions

- Which compliance case families, such as sanctions, Anti-Money Laundering (AML), fraud, or conduct alerts, require different local challenge-minute assumptions?
- What minimum frequency of planted-error or synthetic-fault tests best balances realism with reviewer gaming risk?
- When should dual control or mandatory second review be reserved for only the highest-risk alerts instead of applied more broadly?

### §7 Recursive Review

- review_result: pass
- acronym_audit: passed
- domain_term_audit: passed
- claim_label_audit: passed
- source_url_audit: passed
- synthesis_findings_parity: aligned
- confidence_assessment: medium
- remaining_gaps: no universal bank-wide alert-count ceiling was found, so the final threshold remains capacity-ratio based and locally calibrated.

---

## Findings

### Executive Summary

Human-in-the-Loop (HITL) oversight in bank compliance stops being an effective safeguard once sustained review demand exceeds protected human challenge capacity, producing significant backlog, near-zero verified challenge activity, or uninterrupted monitoring blocks that push reviewers into passive acceptance of automated triage. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]
The reviewed evidence does not support a universal daily alert-count ceiling across banks, because supervisory sources specify operating conditions for effective challenge rather than a fixed case quota. [inference; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]
The strongest defensible threshold is therefore a locally calibrated capacity ratio supported by universal breach indicators such as prolonged backlog, missed review timelines, absent override or escalation evidence, and lack of tested second-review or fault-injection controls. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
Banks sustain reviewer vigilance when they reduce false-positive load upstream, preserve shorter review blocks, expose less aggregated case evidence, brief reviewers that the model can be wrong, and log challenge behaviour in a way that can be audited later. [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

### Key Findings

1. **Meaningful bank-compliance oversight requires reviewers who can understand system limits, detect anomalies, disregard or reverse outputs, and interrupt processing, because the reviewed supervisory sources treat authority, competence, independence, and real intervention power as the minimum standard for human challenge.** ([fact]; high confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf)
2. **No reviewed banking supervisor publishes a universal daily alert-count ceiling, but the Hong Kong Monetary Authority (HKMA) and interagency model-risk guidance treat significant backlog, missed timelines, and ineffective challenge staffing as observable signs that the review control has already failed.** ([inference]; high confidence; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/)
3. **Sanctions screening gives this failure mode real operational force because published banking research reports false-positive alert rates above 90 percent, and the Federal Reserve's 2025 benchmark paper treats manual review burden and transaction delay as direct consequences of those false positives.** ([inference]; medium confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf)
4. **Reviewers should not be left in uninterrupted queue-clearing sessions longer than roughly 30 minutes, because vigilance research traces a steep initial drop in rare-signal detection within the first half hour of sustained monitoring before further decline sets in.** ([inference]; low confidence; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full)
5. **Evidence-rich case presentation matters because informing reviewers that the system can be wrong and showing less aggregated case data increases verification intensity and decision quality more reliably than generic reminders of responsibility.** ([fact]; medium confidence; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/)
6. **An audit-ready threshold should compare required challenge minutes with available staffed challenge minutes after subtracting breaks, calibration, second-review sampling, and escalation work, because nominal headcount overstates the time available for substantive review.** ([inference]; medium confidence; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html)
7. **Near-zero override or escalation rates are not proof of safe automation, because the same pattern can arise from reviewer deference, so banks need logged second-review samples or planted-error tests to show that humans still detect machine mistakes under load.** ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html)
8. **Better screening models and threshold tuning materially reduce the risk of Human-in-the-Loop (HITL) collapse, but they do not remove the need for meaningful human challenge because banking and Artificial Intelligence (AI) oversight rules still require documented competence, accountability, and authority to intervene.** ([inference]; medium confidence; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Meaningful oversight requires authority, competence, independence, and real power to override or stop outputs. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf | high | Direct supervisory requirement, not a synthesis-only claim. |
| [inference] Collapse is not defined by a universal alert count but by backlog, missed timelines, and ineffective challenge staffing. | https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/ | high | The sources specify breach indicators rather than a numeric quota. |
| [inference] False-positive alert rates above 90 percent make bank screening queues structurally vulnerable to superficial review. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf | medium | Supported by direct burden evidence plus synthesis about queue effects. |
| [inference] Uninterrupted review blocks longer than roughly 30 minutes raise the risk that challenge behaviour degrades into passive monitoring. | https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full | low | Transfer from vigilance research to bank review design, not a banking regulation. |
| [fact] Error briefings and less aggregated evidence improve verification intensity more than responsibility reminders alone. | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ | medium | Strong behavioural signal from non-banking decision-support studies. |
| [inference] The best operational threshold is a local capacity ratio based on required challenge minutes versus available staffed challenge minutes. | https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html | medium | Derived because public sources define control conditions but not universal staffing formulas. |
| [inference] Zero override rates are ambiguous unless banks run second-review samples or planted-error tests under load. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | Testing and telemetry close an otherwise unobservable governance gap. |
| [inference] Upstream model tuning reduces review burden but cannot substitute for meaningful human challenge controls. | https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC11621073/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf | medium | Technical improvement changes load, not the oversight obligation. |

### Assumptions

- [assumption; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Each institution can estimate average challenge minutes by alert family from internal case-handling data even though no public cross-bank benchmark set exposes comparable staffing and handling-time distributions.
- [assumption; source: https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] The vigilance-decrement and automation-bias findings are transferable enough to bank compliance review to justify shorter review blocks and verification-oriented interface design, while exact local timings should still be validated in production.

### Analysis

Banking and Artificial Intelligence (AI) oversight sources are strongest on the conditions for effective human challenge, not on universal numeric queue quotas, so the most defensible answer is a hybrid threshold model rather than a single cases-per-reviewer benchmark. [inference; source: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]
The human-factors sources explain why these control conditions matter: high-volume repetitive review and time pressure shift people toward heuristic acceptance, while explicit error awareness and less aggregated evidence increase verification behaviour. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full]
That combination supports a threshold policy built from four linked indicators: capacity ratio, backlog and timeline compliance, observed challenge activity such as overrides or escalations, and periodic tested detection through second review or planted errors. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
Alternative remedies such as adding staff, improving the screening model, or redesigning the interface are complements rather than substitutes: more staff helps only if capacity is protected for challenge rather than queue clearing, better models reduce volume but do not remove the oversight obligation, and better interfaces improve verification only when reviewers still have authority and time to use them. [inference; source: https://www.federalreserve.gov/econres/feds/files/2025092pap.pdf; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf]

### Risks, Gaps, and Uncertainties

- Public sources do not provide a universal bank-by-bank benchmark for alerts per reviewer, challenge minutes per alert family, or acceptable override-rate bands, so the final numeric threshold still requires local calibration. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf]
- Most controlled automation-bias and vigilance studies come from non-banking settings, so the exact size of the degradation effect inside compliance teams remains inferential even though the mechanism is strongly supported. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://www.frontiersin.org/journals/cognition/articles/10.3389/fcogn.2025.1617561/full]
- Accessible supervisory texts emphasise process quality, evidence, and governance accountability more than they specify any single mandatory testing frequency for planted-error exercises. [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

### Open Questions

- Which compliance case families, such as sanctions, Anti-Money Laundering (AML), fraud, or conduct alerts, require different local challenge-minute assumptions?
- What minimum frequency of planted-error or synthetic-fault tests best balances realism with reviewer gaming risk?
- When should dual control or mandatory second review be reserved for only the highest-risk alerts instead of applied more broadly?

## Output

- Type: knowledge
- Description: This item provides a threshold framework for bank-compliance Human-in-the-Loop (HITL) review that treats meaningful challenge as a capacity-and-behaviour control rather than a headcount label, and it specifies the observable indicators needed to prove that reviewers still challenge automated triage under production load. [inference; source: https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html]
- Links:
  - https://www.hkma.gov.hk/media/eng/doc/key-information/guidelines-and-circular/2023/20230209e2a2.pdf
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/

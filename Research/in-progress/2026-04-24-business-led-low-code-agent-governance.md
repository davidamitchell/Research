---
review_count: 2
title: "Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments"
added: 2026-04-24
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [artificial-intelligence, governance, low-code, citizen-development, regulated-environments, operating-model, platform-governance]
started: 2026-04-24
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
---

# Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments

## Research Question

Under what conditions does business-led low-code Artificial Intelligence (AI) agent creation produce durable organisational value versus technical debt and governance fragmentation, and what foundational capabilities must exist before business-led agent creation is safe to scale in a regulated environment?

## Scope

**In scope:**
- Structural failure modes of ungoverned citizen development drawn from Robotic Process Automation (RPA) literature (2018-2022) as the closest direct analogue.
- DevOps Research and Assessment (DORA) 2025 AI Capabilities Model findings on platform quality as a prerequisite for sustainable AI delivery at scale.
- National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) Map function: how it classifies use-case risk and what that implies for low-code agent scenarios.
- Microsoft Power Platform Centre of Excellence (CoE) toolkit: the governance model Microsoft actually prescribes for Copilot Studio at scale (not marketing material).
- Conditions distinguishing organisations where citizen development delivers durable value from those where it produces fragmentation, loss of determinism, and weakened controls.
- Minimum foundational capabilities: governance, platform readiness, data controls, and operating model required before scaling business-led agent creation in a regulated environment.

**Out of scope:**
- In-depth vendor tutorial content or Copilot Studio feature documentation.
- AI model training and fine-tuning techniques unrelated to governance or operating-model decisions.
- Consumer-facing or small-business contexts that do not map to regulated-enterprise constraints.
- Comparison of specific low-code platforms beyond those directly referenced in governance literature.

**Constraints:**
- Prioritise public, citable primary sources: standards bodies (NIST, International Organization for Standardization (ISO)), regulator guidance, peer-reviewed literature, and vendor architecture guidance.
- Distinguish prescribed standards from observed practice where evidence permits.
- All sources must include URLs.

## Context

[fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] Microsoft positions Copilot Studio as a governed Power Platform service with tenant administration, data policies, environment controls, audit logging, and maker guidance, not as an unconstrained maker sandbox.
[inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The practical decision is whether an organisation already has the governance and platform quality needed to let business users create low-code agents safely, because RPA citizen development and DORA both indicate that scale amplifies existing control weaknesses rather than repairing them.

## Approach

1. Survey the RPA citizen-development failure literature (2018-2022) to identify the structural failure modes: loss of determinism, weak controls, process fragmentation, and maintenance debt, then map their direct analogues in business-led AI agent creation.
2. Analyse the DORA 2025 AI Capabilities Model to extract what platform-quality prerequisites it identifies as necessary for sustainable AI delivery, and whether citizen-development scenarios are addressed.
3. Review the NIST AI RMF Map function to understand how use-case risk classification is intended to operate, and how it can be applied to low-code agent scenarios at intake.
4. Examine the Microsoft Power Platform CoE toolkit and Copilot Studio governance guidance to understand what controls Microsoft actually recommends, including data loss prevention policies, environment strategy, managed environments, and connector governance, versus what marketing material presents.
5. Synthesise conditions under which business-led agent creation produces durable value versus fragmentation, producing a conditions-and-prerequisites framework with clear governance checkpoints.
6. Identify minimum viable foundational capabilities: governance policy, platform safety nets, data classification, and operating model oversight that must be demonstrably in place before scaling is safe in a regulated environment.

## Sources

Starting points - papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [x] [DORA 2025 report overview](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) - primary overview of the AI-as-amplifier finding and platform-quality prerequisite.
- [x] [DORA AI capabilities model report landing page](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) - seven foundational capabilities, 90% platform adoption, and 76% dedicated platform teams.
- [x] [Faros AI: Engineering Excellence Under AI Acceleration (2026)](https://faros.ai/blog/ai-acceleration-whiplash) - returned 404 in this environment and was not used for downstream claims.
- [x] [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) 1.0](https://doi.org/10.6028/NIST.AI.100-1) - primary framework source for govern-map-measure-manage structure.
- [x] [NIST AI RMF overview](https://www.nist.gov/itl/ai-risk-management-framework) - current NIST landing page linking the framework and playbook.
- [x] [NIST AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook) - replacement for the seeded `airc.nist.gov/Docs/2` URL, which returned 404 in this environment.
- [x] [NIST AI RMF Playbook landing page](https://airc.nist.gov/airmf-resources/playbook/) - confirms the playbook is voluntary, contextual, and organised by Govern, Map, Measure, and Manage.
- [x] [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - authoritative Map subcategories for context establishment, categorisation, and impact documentation.
- [x] [NIST AI RMF Playbook Map page](https://airc.nist.gov/airmf-resources/playbook/map/) - practitioner references aligned to Map activities.
- [x] [Microsoft Power Platform Centre of Excellence (CoE) Starter Kit overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) - Microsoft's reference implementation for governance, monitoring, and adoption.
- [x] [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) - current replacement for the seeded `admin-overview` URL, which returned 404 in this environment.
- [x] [Microsoft Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) - concrete controls over authentication, knowledge sources, channels, skills, triggers, and endpoints.
- [x] [Power Platform data policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) - design-time and runtime enforcement model for connectors and chatbots.
- [x] [Power Platform Managed Environments](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) - Microsoft's at-scale environment management capability.
- [x] [Digital.gov: 5 tips for implementing citizen development in your RPA program](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/) - government guidance on governance, repositories, separate environments, and leadership support.
- [x] [A framework for implementing robotic process automation projects](https://link.springer.com/article/10.1007/s10257-022-00553-8) - peer-reviewed synthesis on RPA implementation failure and the need for structured, socio-technical governance.
- [x] [UiPath: Successful citizen developer programs](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more) - vendor evidence that scaled programs define the governance model first and provide support structures.
- [x] [Deloitte intelligent automation survey results (2022)](https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html) - definition and adoption signal for citizen-led development in low-code automation.
- [x] [Gartner citizen developer glossary](https://www.gartner.com/en/information-technology/glossary/citizen-developer) - returned 403 in this environment and was not used for downstream claims.
- [x] [Forrester RPA research hub](https://www.forrester.com/research/rpa/) - returned 404 in this environment and was not used for downstream claims.
- [x] [IEEE Xplore seed search](https://ieeexplore.ieee.org/Xplore/home.jsp) - checked via search query `site:ieeexplore.ieee.org "RPA" "citizen development" governance`; no accessible pinpoint paper from the seeded search was used, so the RPA evidence base relies on the accessible Springer, Digital.gov, UiPath, and Deloitte sources above.

## Related

- [Enterprise AI platform operating models: organisational structure and ownership](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md)
- [AI governance assurance: change control, verification, and review loops](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md)
- [Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-knowledge-curation-governance-for-regulated-ai.md)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] Research question restated: when does business-led low-code agent creation create durable value instead of technical debt and governance fragmentation, and which governance, platform, data, and operating-model capabilities must already exist before scale is safe in a regulated environment?
- [fact; source: https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Scope confirmed: the investigation covers RPA citizen-development analogues, DORA platform prerequisites, NIST Map-based use-case classification, Microsoft's prescribed governance controls, and a conditions-and-prerequisites framework for regulated low-code agent deployment.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] Constraints confirmed: public sources were prioritised, broken seed URLs were replaced where possible with current primary pages, and inaccessible analyst pages were recorded but not used as direct evidence.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-knowledge-curation-governance-for-regulated-ai.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] Prior completed repository work already established that enterprise AI value depends on platform operating models, explicit change-control loops, authoritative knowledge governance, and explicit use-case routing, so this item extends that work into the specific problem of business-led low-code agent creation.
- Output format: knowledge.

### §1 Question Decomposition

- **Root question:** Under what conditions does business-led low-code agent creation produce durable organisational value rather than fragmentation in regulated environments?
- **A. RPA analogue**
  - A1. What governance and operating-model problems repeatedly appeared in RPA citizen development?
  - A2. Which of those problems plausibly transfer to low-code AI agent creation?
- **B. Platform prerequisite**
  - B1. What does DORA say about platform quality, workflows, safety nets, and team capability as prerequisites for AI value?
  - B2. What does that imply for business-led low-code agent programs?
- **C. Risk intake**
  - C1. What does NIST Map require teams to document before deploying an AI use case?
  - C2. How should those Map elements be translated into a low-code agent intake process?
- **D. Vendor-prescribed controls**
  - D1. What governance structure does Microsoft prescribe through the Power Platform CoE, data policies, managed environments, and Copilot Studio controls?
  - D2. Which controls are central-admin responsibilities rather than maker responsibilities?
- **E. Conditions for durable value**
  - E1. Which conditions distinguish safe, durable business-led agent creation from fragmentation?
  - E2. Which minimum foundational capabilities must exist before scale is allowed in regulated environments?

### §2 Investigation

#### Source access and replacement notes

- [fact; source: https://faros.ai/blog/ai-acceleration-whiplash; https://www.gartner.com/en/information-technology/glossary/citizen-developer; https://www.forrester.com/research/rpa/] Three seeded sources were inaccessible in this runtime: the Faros AI page returned 404, the Gartner glossary returned 403, and the Forrester hub returned 404, so none of them were used to support downstream claims.
- [fact; source: https://airc.nist.gov/Docs/2; https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook; https://airc.nist.gov/airmf-resources/playbook/] The seeded NIST Playbook URL returned 404, so the investigation used NIST's current Playbook entry page and the current AI Resource Center (AIRC) playbook pages instead.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] The seeded Microsoft Copilot Studio `admin-overview` URL returned 404, so the investigation used the current `security-and-governance` page and the detailed data-loss-prevention page instead.
- [fact; source: https://ieeexplore.ieee.org/Xplore/home.jsp] Failed primary-source search record: the seeded IEEE source was only a generic portal, and the query `site:ieeexplore.ieee.org "RPA" "citizen development" governance` did not yield an accessible pinpoint paper in this environment, so no IEEE source was used for factual support.
- [assumption; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] RPA citizen development is treated as the closest operational analogue to low-code agent creation. **Justification:** both move automation authoring toward business users on centrally administered low-code platforms, so the organisational failure modes and required guardrails are comparable even though generative agents introduce additional model risk.

#### A. What the RPA citizen-development analogue shows

- [fact; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] Digital.gov states that citizen RPA should be governed through standardised protocols, extensive code review, a central repository, Role-based access controls (RBAC), separate development, test, and production environments, collaboration with chief information officer and Information Technology (IT) teams, and leadership support.
- [fact; source: https://link.springer.com/article/10.1007/s10257-022-00553-8] The 2022 Springer article says reliable and scalable RPA still requires expert knowledge, that up to 50% of initial RPA implementations are estimated to fail, and that organisations need more systematic socio-technical implementation support than ad hoc local projects provide.
- [fact; source: https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] UiPath's scaled citizen-development examples report that successful programs defined the governance model first, clarified expectations for developers, business functions, digital teams, and executives, and then backed makers with reusable components, idea-intake processes, and professional-developer support.
- [fact; source: https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html] Deloitte defines citizen-led development as the use of IT-sanctioned low-code or no-code platforms by non-IT employees for low-complexity attended automations, which means the operating model assumes explicit sanctioning and bounded complexity rather than unlimited autonomy.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more; https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html] The RPA analogue shows a repeatable pattern: value appears when citizen development is tightly bounded, centrally governed, and productionised through shared engineering controls, while fragmentation appears when local makers are expected to solve governance, promotion, and maintenance themselves.

#### B. What DORA says about AI value at scale

- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA says Artificial Intelligence (AI) does not fix a team and instead amplifies what is already there, so weak workflows and weak control systems become more visible under AI-assisted acceleration.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA also says instability remains negatively related to AI adoption unless organisations have robust control systems such as automated testing, mature version control, and fast feedback loops.
- [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA's 2025 material says the greatest returns come from foundational systems, identifies internal platforms as crucial for scaling success, reports that 90% of organisations have adopted at least one platform, and reports that 76% now have dedicated platform teams.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] Low-code agent creation therefore cannot be treated as a shortcut around platform quality, because broader access to agent-building tools will magnify the quality of the underlying platform, workflow, safety-net, and policy system rather than substitute for it.

#### C. What NIST Map implies for low-code agent intake

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST describes Govern as a cross-cutting function and Map as the function that establishes the context needed to frame AI risks before measurement and management.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST Map 1.1 requires intended purposes, beneficial uses, context-specific laws and norms, deployment settings, likely users, positive and negative impacts, assumptions, and limitations to be understood and documented.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST Map 1.4 through Map 1.6 require business value, organisational risk tolerance, and system requirements with socio-technical implications to be clearly defined and documented.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST Map 2 and Map 5 require the task type, method, knowledge limits, human oversight, third-party software and data risks, and the likelihood and magnitude of positive and harmful impacts to be documented.
- [fact; source: https://airc.nist.gov/airmf-resources/playbook/; https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook] NIST states that the Playbook is voluntary, contextual, and not a checklist, which means organisations must tailor control depth to the use case instead of applying one universal approval flow.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://airc.nist.gov/airmf-resources/playbook/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] For low-code agent programs, a pre-build intake should classify purpose, users, data domains, deployment channels, autonomy level, external actions, human-review requirements, and third-party dependencies before a maker is allowed to publish, because NIST treats those facts as the basis for any go or no-go decision and the prior routing-framework item shows those signals are what determine the correct delivery lane.

#### D. What Microsoft actually prescribes for scale

- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Microsoft says the Power Platform CoE Starter Kit is only a reference implementation and not the CoE itself, because an actual CoE also requires people, communication, defined requirements, and processes.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Microsoft describes the CoE as a strategic organisational capability that balances innovation and control, scales citizen development, and uses monitoring, analytics, and automation to support governance.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] Microsoft's prescribed administrative surface includes environment and environment-security management, data policy management, tenant analytics, and Managed Environments for at-scale administration.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] Copilot Studio governance controls include data-policy controls over knowledge sources, actions, connectors, skills, Hypertext Transfer Protocol (HTTP) requests, publication channels, triggers, and telemetry; maker audit logs in Microsoft Purview; alerts in Microsoft Sentinel; environment routing; maker security warnings; sensitivity labels for SharePoint knowledge; and the option to disable agent publishing.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] Copilot Studio data-policy enforcement supports blocking unauthenticated chat, public-website knowledge, document knowledge, SharePoint knowledge, HTTP requests, skills, publication channels, and event triggers, and it supports endpoint filtering for selected knowledge and HTTP surfaces.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] Power Platform data policies apply at design time and runtime, can suspend or quarantine apps, flows, and chatbots that violate policy, can disable blocked connections, and can take up to 24 hours to fully propagate in extreme cases.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] Microsoft's scale pattern is therefore centrally administered guardrails plus maker enablement inside controlled environments, not unrestricted business-unit autonomy.

#### E. Conditions and prerequisites synthesis

- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] Durable value is most plausible when business-led agents are limited to low-risk, process-suitable, bounded workflows with authenticated users, approved knowledge sources, approved connectors, central logging, separate environments, and a defined escalation path into professional engineering or governance teams.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] Fragmentation is most plausible when makers can publish directly to live channels without risk classification, repository discipline, environment separation, connector restrictions, ownership clarity, auditability, or suitable process selection, because those gaps create hidden maintenance, inconsistent controls, and unstable operations.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] The minimum safe foundation is a central governance function, a risk-based intake process, controlled environments, enforceable data policies, monitoring and audit logs, maker training and support, and a shared team that owns exceptions, higher-risk use cases, and lifecycle governance from intake through retirement.

### §3 Reasoning

- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Direct primary-source agreement exists that scaled AI value depends on pre-existing governance and platform quality rather than on access to tools alone.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] The RPA literature does not prove low-code agent outcomes mechanically, but it does provide a strong organisational analogue because the same questions of repository discipline, environment promotion, ownership, and support recur before the addition of model-specific risk.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] The most important transfer is not "RPA failed" but "business-led automation only scales after intake, bounded scope, and central guardrails exist," which is exactly how NIST Map, Microsoft's control model, and the prior routing-framework item frame the problem.

### §4 Consistency Check

- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] No direct contradiction appeared across DORA, Microsoft, and Digital.gov on the core question of whether governance should precede scale; all three sources treat enablement as dependent on an operating model and shared controls.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] A tension exists between contextual tailoring and standardised controls, but it is resolved by combining NIST's risk-based tailoring with Microsoft's tenant-level guardrails and exception routing.
- [fact; source: https://faros.ai/blog/ai-acceleration-whiplash; https://www.gartner.com/en/information-technology/glossary/citizen-developer; https://www.forrester.com/research/rpa/] Inaccessible analyst pages were excluded from evidentiary weight, so no conclusion depends on a source that could not be checked in this session.

### §5 Depth and Breadth Expansion

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] **Technical lens:** the decisive technical controls are not model-tuning features but the ability to constrain knowledge sources, connectors, channels, HTTP access, authentication, and triggers before publication.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.nist.gov/itl/ai-risk-management-framework] **Regulatory lens:** regulated environments need documented risk tolerance, documented human oversight, and documented third-party dependency treatment, which makes informal maker-side judgment insufficient for medium-risk and high-risk agents.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] **Economic lens:** business-led agents can create real local productivity gains, but those gains do not become durable enterprise value unless a shared platform converts local wins into repeatable, supportable, and reviewable assets.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] **Behavioural lens:** durable programs treat makers as trained contributors inside a governed system, while failed programs implicitly treat enthusiasm as a substitute for support, review, and accountability.

### §6 Synthesis

**Executive summary:**

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] Business-led low-code agent creation produces durable value only when it is layered on top of a centrally governed platform with risk-based intake, enforceable data and channel controls, environment separation, shared lifecycle ownership, and suitable low-risk use-case selection; without that foundation it predictably produces local wins alongside enterprise fragmentation.
[inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] The closest operational analogue, RPA citizen development, shows that business-user automation succeeds when governance is defined first and fails when repository discipline, role clarity, review, and promotion controls are left to local teams.
[fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA strengthens that conclusion by showing that AI amplifies the quality of the surrounding platform and workflow system and that internal platforms are now the main scaling mechanism for enterprise AI value.
[fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] In a regulated environment, the minimum safe foundation is a central governance function, a NIST-style risk-classification intake, controlled environments, enforceable data policies, and central oversight for higher-risk or cross-boundary agents.

**Key findings:**

1. [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Business-led low-code agent creation creates durable value only when citizen builders operate inside a defined governance model and are limited to process-suitable, bounded tasks with central repositories, review paths, support structures, and separate promotion environments rather than publishing directly from local teams.
2. [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] **Medium confidence:** DORA's 2025 evidence shows that AI amplifies existing organisational conditions, so platform quality, workflow clarity, safety nets, and dedicated platform ownership are prerequisites for scaled value rather than optional improvements after rollout.
3. [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] **Medium confidence:** NIST Map requires organisations to document intended purpose, users, laws and norms, business value, risk tolerance, knowledge limits, human oversight, third-party dependencies, and likely impacts before they can make a credible go or no-go decision on an AI use case.
4. [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] **Medium confidence:** Microsoft's own at-scale model for Power Platform and Copilot Studio is a Centre of Excellence with managed environments, analytics, and admin controls, which means Microsoft prescribes central governance capability before broad maker enablement.
5. [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] **Medium confidence:** Copilot Studio can centrally restrict authentication modes, knowledge sources, connectors, publication channels, Hypertext Transfer Protocol (HTTP) access, skills, and triggers, and Power Platform policies can suspend or quarantine violating assets at runtime as well as design time.
6. [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Safe business-led agent programs should initially permit only bounded, low-risk, process-suitable use cases with authenticated users, approved knowledge domains, approved connectors, and explicit human escalation, while routing higher-risk, external-action, or cross-boundary agents into central review.
7. [inference; source: https://link.springer.com/article/10.1007/s10257-022-00553-8; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Fragmentation emerges when local makers can create or publish agents without ownership clarity, environment strategy, suitable process selection, or connector and channel guardrails, because the resulting estate becomes hard to review, support, and stabilise.
8. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** The minimum viable foundation before scaling is a central governance team, a risk-based intake workflow, controlled environments, enforceable data and channel policies, auditability, maker training, and a professional team that owns exceptions and lifecycle governance.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Durable value requires a governed operating model, not direct local publishing. | [Digital.gov citizen development guidance](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/); [Springer RPA implementation framework](https://link.springer.com/article/10.1007/s10257-022-00553-8); [UiPath citizen developer programs](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more) | high | Multi-source |
| [fact] AI value depends on foundational platform and workflow quality. | [DORA report overview](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [DORA AI capabilities model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | medium | Single-organisation primary evidence |
| [fact] NIST Map defines the intake facts required for an AI use-case decision. | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | medium | Single primary framework |
| [fact] Microsoft prescribes a CoE and managed environments before broad maker enablement. | [Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview); [Managed Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) | medium | Single-organisation primary evidence |
| [fact] Copilot Studio exposes central controls over auth, knowledge, channels, tools, and triggers. | [Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance); [Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention); [Power Platform data policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) | medium | Single-organisation primary evidence |
| [inference] Safe business-led rollout should start with bounded low-risk use cases and escalation paths. | [Digital.gov citizen development guidance](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/); [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/); [Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |
| [inference] Fragmentation follows from missing ownership, environment strategy, suitable process selection, and policy guardrails. | [Springer RPA implementation framework](https://link.springer.com/article/10.1007/s10257-022-00553-8); [DORA report overview](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [Power Platform data policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |
| [inference] The minimum viable foundation is governance, intake, environments, policies, audit, training, and exception handling. | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/); [Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview); [Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |

**Assumptions:**

- [assumption; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] The organisational lessons from RPA citizen development transfer materially to low-code AI agents. **Justification:** both patterns decentralise automation authoring to business users while relying on central platform controls for safe promotion and support.

**Analysis:**

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] The strongest evidence suggests that scaled AI value depends on platform quality, explicit governance, and documented use-case context.
[inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] The RPA analogue adds operating-model texture rather than direct proof, but it is persuasive because its recurring prescriptions, central repositories, environment separation, role clarity, and support, match the exact controls Microsoft now exposes for low-code agents.
[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] Governance is therefore necessary but not sufficient: durable value also depends on selecting process-suitable use cases and keeping autonomy within the bounds that the platform and operating model can actually support.

**Risks, gaps, uncertainties:**

- [fact; source: https://faros.ai/blog/ai-acceleration-whiplash; https://www.gartner.com/en/information-technology/glossary/citizen-developer; https://www.forrester.com/research/rpa/] Several seeded analyst sources were inaccessible, so this item relies on public standards, public-sector guidance, vendor documentation, and accessible peer-reviewed literature instead of analyst synthesis.
- [fact; source: https://ieeexplore.ieee.org/Xplore/home.jsp] The seeded IEEE search did not yield an accessible pinpoint paper in this runtime, so the academic RPA evidence base is narrower than ideal.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] The analogue from RPA to generative agents is strong on governance shape but weaker on model-specific failure modes such as hallucination, which would need a follow-on item if the question shifted toward model assurance rather than operating-model design.

**Open questions:**

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] What concrete risk tiers should a regulated enterprise use to separate low-risk business-led agents from centrally engineered medium-risk and high-risk agents?
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Which specific telemetry, approval, and recertification controls produce the best ongoing assurance for agents that remain business-owned after first publication?
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] How should platform-team capacity be sized so that escalation paths for higher-risk agents do not become the next delivery bottleneck?

### §7 Recursive Review

- Review outcome: claim labels and source bindings were re-checked after the first review pass.
- Review outcome: inaccessible or non-pinpoint seed sources remain recorded and excluded from factual support.
- Review outcome: the final conclusion treats governance as necessary but not sufficient, with use-case suitability and autonomy bounds now made explicit.

---

## Findings

*(Populated from section 6 Synthesis above.)*

### Executive Summary

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] Business-led low-code agent creation produces durable value only when it is layered on top of a centrally governed platform with risk-based intake, enforceable data and channel controls, environment separation, shared lifecycle ownership, and suitable low-risk use-case selection; without that foundation it predictably produces local wins alongside enterprise fragmentation.
[inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] The RPA citizen-development analogue shows that decentralised automation works when governance is defined first and fails when repository discipline, role clarity, review, and production promotion are left to local teams.
[fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA strengthens that conclusion by showing that AI amplifies the quality of the surrounding platform and workflow system and that internal platforms are now the main scaling mechanism for enterprise AI value.
[fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] In a regulated environment, the minimum safe foundation is a central governance function, a NIST-style risk-classification intake, controlled environments, enforceable data policies, and central oversight for higher-risk or cross-boundary agents.

### Key Findings

1. [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Business-led low-code agent creation creates durable value only when citizen builders operate inside a defined governance model and are limited to process-suitable, bounded tasks with central repositories, review paths, support structures, and separate promotion environments rather than publishing directly from local teams.
2. [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] **Medium confidence:** DORA's 2025 evidence shows that AI amplifies existing organisational conditions, so platform quality, workflow clarity, safety nets, and dedicated platform ownership are prerequisites for scaled value rather than optional improvements after rollout.
3. [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] **Medium confidence:** NIST Map requires organisations to document intended purpose, users, laws and norms, business value, risk tolerance, knowledge limits, human oversight, third-party dependencies, and likely impacts before they can make a credible go or no-go decision on an AI use case.
4. [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] **Medium confidence:** Microsoft's own at-scale model for Power Platform and Copilot Studio is a Centre of Excellence with managed environments, analytics, and admin controls, which means Microsoft prescribes central governance capability before broad maker enablement.
5. [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] **Medium confidence:** Copilot Studio can centrally restrict authentication modes, knowledge sources, connectors, publication channels, Hypertext Transfer Protocol (HTTP) access, skills, and triggers, and Power Platform policies can suspend or quarantine violating assets at runtime as well as design time.
6. [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Safe business-led agent programs should initially permit only bounded, low-risk, process-suitable use cases with authenticated users, approved knowledge domains, approved connectors, and explicit human escalation, while routing higher-risk, external-action, or cross-boundary agents into central review.
7. [inference; source: https://link.springer.com/article/10.1007/s10257-022-00553-8; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** Fragmentation emerges when local makers can create or publish agents without ownership clarity, environment strategy, suitable process selection, or connector and channel guardrails, because the resulting estate becomes hard to review, support, and stabilise.
8. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md] **High confidence:** The minimum viable foundation before scaling is a central governance team, a risk-based intake workflow, controlled environments, enforceable data and channel policies, auditability, maker training, and a professional team that owns exceptions and lifecycle governance.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Durable value requires a governed operating model, not direct local publishing. | [Digital.gov citizen development guidance](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/); [Springer RPA implementation framework](https://link.springer.com/article/10.1007/s10257-022-00553-8); [UiPath citizen developer programs](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more) | high | Multi-source |
| [fact] AI value depends on foundational platform and workflow quality. | [DORA report overview](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [DORA AI capabilities model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | medium | Single-organisation primary evidence |
| [fact] NIST Map defines the intake facts required for an AI use-case decision. | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | medium | Single primary framework |
| [fact] Microsoft prescribes a CoE and managed environments before broad maker enablement. | [Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview); [Managed Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) | medium | Single-organisation primary evidence |
| [fact] Copilot Studio exposes central controls over auth, knowledge, channels, tools, and triggers. | [Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance); [Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention); [Power Platform data policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) | medium | Single-organisation primary evidence |
| [inference] Safe business-led rollout should start with bounded low-risk use cases and escalation paths. | [Digital.gov citizen development guidance](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/); [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/); [Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |
| [inference] Fragmentation follows from missing ownership, environment strategy, suitable process selection, and policy guardrails. | [Springer RPA implementation framework](https://link.springer.com/article/10.1007/s10257-022-00553-8); [DORA report overview](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [Power Platform data policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |
| [inference] The minimum viable foundation is governance, intake, environments, policies, audit, training, and exception handling. | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/); [Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview); [Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance); [Enterprise AI use-case routing frameworks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-use-case-routing-frameworks.md) | high | Multi-source |

### Assumptions

- [assumption; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] **Assumption:** The organisational lessons from RPA citizen development transfer materially to low-code AI agents. **Justification:** Both patterns decentralise automation authoring to business users while relying on central platform controls for safe promotion and support.

### Analysis

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] The strongest evidence suggests that scaled AI value depends on platform quality, explicit governance, and documented use-case context.
[inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more] The RPA analogue adds operating-model texture rather than direct proof, but it is persuasive because its recurring prescriptions, central repositories, environment separation, role clarity, and support, match the exact controls Microsoft now exposes for low-code agents.
[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] Governance is therefore necessary but not sufficient: durable value also depends on selecting process-suitable use cases and keeping autonomy within the bounds that the platform and operating model can actually support.

### Risks, Gaps, and Uncertainties

- [fact; source: https://faros.ai/blog/ai-acceleration-whiplash; https://www.gartner.com/en/information-technology/glossary/citizen-developer; https://www.forrester.com/research/rpa/] Several seeded analyst sources were inaccessible, so this item relies on public standards, public-sector guidance, vendor documentation, and accessible peer-reviewed literature instead of analyst synthesis.
- [fact; source: https://ieeexplore.ieee.org/Xplore/home.jsp] The seeded IEEE search did not yield an accessible pinpoint paper in this runtime, so the academic RPA evidence base is narrower than ideal.
- [inference; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] The analogue from RPA to generative agents is strong on governance shape but weaker on model-specific failure modes such as hallucination, which would need a follow-on item if the question shifted toward model assurance rather than operating-model design.

### Open Questions

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] What concrete risk tiers should a regulated enterprise use to separate low-risk business-led agents from centrally engineered medium-risk and high-risk agents?
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Which specific telemetry, approval, and recertification controls produce the best ongoing assurance for agents that remain business-owned after first publication?
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] How should platform-team capacity be sized so that escalation paths for higher-risk agents do not become the next delivery bottleneck?

---

## Output

*(Fill in when completing - what was produced as a result of this research?)*

- Type: knowledge
- Description: Conditions-and-prerequisites guidance for deciding when business-led low-code agent creation is safe to scale in regulated environments.
- Links:
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report

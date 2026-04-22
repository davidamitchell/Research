---
review_count: 2
title: "Enterprise AI use-case routing frameworks"
added: 2026-04-22
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [artificial-intelligence, platform-governance, risk-tiering, operating-model]
started: 2026-04-22
completed: 2026-04-22
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
---

# Enterprise AI use-case routing frameworks

## Research Question

What decision frameworks do enterprises use to route Artificial Intelligence (AI) use cases to the appropriate platform, implementation pattern, and risk tier, distinguishing low-code business-led, pro-code custom, and developer productivity use cases, and what criteria, routing signals, and governance checkpoints does each routing decision require?

## Scope

**In scope:**
- Enterprise decision frameworks that classify AI use cases into low-code business-led, pro-code custom, and developer productivity routes.
- Gating criteria used at intake (data sensitivity, model criticality, autonomy level, integration depth, change impact, and regulatory exposure).
- Governance checkpoints per route (architecture review, security/privacy review, legal/compliance review, human oversight, and post-deployment monitoring).
- Practical operating models (central platform team, federated domain teams, and hybrid models) that determine who can build what, where, and under what controls.

**Out of scope:**
- Vendor-specific implementation tutorials for a single tool.
- Detailed model-training techniques unrelated to routing and governance decisions.
- Small-business or consumer-only contexts that do not map to enterprise governance constraints.

**Constraints:** (time, source types, access)
- Prioritise public, citable sources from standards bodies, regulators, cloud/platform architecture guidance, and enterprise governance publications.
- Focus on frameworks and checkpoints that can be translated into an actionable triage rubric for backlog intake.
- Identify where evidence is prescriptive guidance versus observed enterprise practice.

## Context

[fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Enterprises now govern at least three distinct AI delivery surfaces at once: business-user low-code platforms, custom AI engineering, and developer-assistance tools, each with different control points and failure modes.
[inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] A useful intake framework therefore needs to choose both a delivery lane and a proportional control set, so that low-risk internal use is not slowed by heavyweight review while high-impact or regulated systems do not bypass needed oversight.

## Approach

Decompose the question into sub-questions and describe how each will be investigated (literature review, experiment, prototype, expert interview, etc.).

1. Identify the most-cited enterprise AI governance and risk management frameworks, then extract how they classify use-case risk and required controls.
2. Compare enterprise platform strategy guidance to map route-selection criteria for low-code business-led, pro-code custom, and developer productivity use cases.
3. Synthesize common intake signals into a draft routing matrix (criteria, thresholds, route assignment, and checkpoint sequence).
4. Validate governance checkpoints per route (security, privacy, legal, model risk, and operational readiness) and note minimum evidence artifacts required to pass each gate.
5. Highlight failure modes (misrouting, control gaps, and review bottlenecks) and mitigation patterns used in mature enterprise operating models.

## Sources

Starting points - papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [x] [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - primary governance framework for Govern, Map, Measure, and Manage functions.
- [x] [NIST Artificial Intelligence Risk Management Framework (AI RMF) 1.0 Digital Object Identifier (DOI) record](https://doi.org/10.6028/NIST.AI.100-1) - authoritative citation for core functions and trustworthy AI characteristics.
- [x] [International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC) 42001:2023](https://www.iso.org/standard/81230.html) - Artificial Intelligence Management System (AIMS) requirements and continual-improvement framing.
- [x] [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) - official risk-tier summary, high-risk obligations, and application timeline.
- [x] [Cloud Adoption Framework for Azure: AI governance](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern) - intake risks, policy categories, enforcement, monitoring, and independent review guidance.
- [x] [Microsoft AI risk assessment for Machine Learning (ML) engineers](https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment) - severity signals for sensitive data, business criticality, and production use.
- [x] [Power Platform Center of Excellence (CoE) Starter Kit overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) - low-code governance model, maker enablement, and compliant-app controls.
- [x] [Power Platform data loss prevention overview](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) - connector guardrails, design-time and runtime enforcement, and quarantine behavior.
- [x] [Managed Environments for Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) - supported tenant-scale controls for low-code environments.
- [x] [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) - base control pillars for security, reliability, cost, operations, and performance.
- [x] [Google Cloud Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml?hl=en) - AI-specific operating guidance.
- [x] [Google Cloud AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en) - problem definition, versioning, observability, Continuous Integration and Continuous Delivery (CI/CD), and controlled release guidance.
- [x] [Amazon Web Services (AWS) Well-Architected Framework: Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) - lifecycle and route-specific machine learning design guidance.
- [x] [GitHub Copilot policies overview](https://docs.github.com/en/copilot/concepts/policies) - enterprise, organization, feature, model, and privacy policy controls.
- [x] [Managing policies and features for GitHub Copilot in your enterprise](https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise) - enterprise control surface for feature availability and enforcement.
- [x] [Responsible use of GitHub Copilot inline suggestions](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion) - human review, secure coding, and limitation guidance for developer productivity use cases.
- [x] [Enterprise AI platform operating models: organisational structure and ownership](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md) - prior completed repository work on central platform ownership and federated delivery.
- [x] [Enterprise AI capability model for use-case maturity decisions](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md) - prior completed repository work on shared capability reuse versus net-new capability building.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md] Prior completed repository work already established two adjacent points that matter here: enterprises benefit from a shared AI governance layer, and use-case intake should distinguish reusable enterprise capabilities from genuinely net-new capability needs.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The research question is to determine which enterprise routing framework best assigns AI use cases to one of three lanes, low-code business-led, pro-code custom, or developer productivity, and to identify the criteria, routing signals, and governance checkpoints that each lane requires.
- [fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Scope confirmed: in scope are intake criteria, operating-model implications, and governance checkpoints for the three lanes; out of scope are vendor tutorials, model-training methods unrelated to intake, and small-business contexts.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Constraint confirmed: the evidence base is public and citable, favors primary standards, regulators, and platform architecture guidance, and distinguishes prescriptive frameworks from observed operating practice.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The most decision-useful output format is a three-lane routing rubric with a single intake checklist, a centrally owned governance layer, and route-specific checkpoints rather than three disconnected governance processes.

### §1 Question Decomposition

- **Branch A - baseline classification**
  - A1. Which cross-framework signals determine whether an AI use case is low, medium, or high risk?
  - A2. Which signals are strong enough to force escalation regardless of platform preference?
- **Branch B - business-led low-code lane**
  - B1. Which use cases can remain on an approved low-code platform under business ownership?
  - B2. Which controls allow a central team to enable citizen development without losing governance?
- **Branch C - pro-code custom lane**
  - C1. Which signals require custom engineering rather than low-code configuration?
  - C2. Which checkpoints are repeatedly required for sensitive, externally impactful, or deeply integrated systems?
- **Branch D - developer productivity lane**
  - D1. Which AI tools are best treated as internal engineering assistance rather than business automation?
  - D2. Which enterprise controls are specific to developer productivity tools?
- **Branch E - operating model**
  - E1. Which decisions belong in the central platform or governance team?
  - E2. Which decisions can remain with domain teams after route assignment?
- **Branch F - failure modes**
  - F1. What kinds of misrouting produce control gaps?
  - F2. What kinds of over-governance create delivery bottlenecks without reducing material risk?

### §2 Investigation

#### Source audit and accessibility notes

- [fact; source: https://artificialintelligenceact.eu/; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The seeded European Union (EU) AI Act overview page was accessible, but the investigation used the European Commission page as the stronger primary source for official risk categories and obligations.
- [fact; source: https://cloud.google.com/architecture/framework; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml?hl=en; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en] The seeded Google Cloud Architecture Framework page was accessible but high level, so the investigation used the AI and ML perspective pages for AI-specific operational guidance.
- [fact; source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/welcome.html; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] The seeded AWS landing page redirected in this environment, so the investigation used the current Machine Learning Lens page.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/adoption/governance-considerations; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] A targeted search for a Microsoft Power Platform governance considerations page returned 404, so the investigation used the current Center of Excellence and data loss prevention guidance instead.

#### A. Cross-framework signals that should drive routing

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://doi.org/10.6028/NIST.AI.100-1] NIST AI RMF 1.0 defines four core functions, Govern, Map, Measure, and Manage, and frames AI risk management as an organizational process that spans design, development, deployment, use, and evaluation.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS) within organizations.
- [fact; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The European Commission summarizes the AI Act as a four-tier regime of unacceptable risk, high-risk, transparency risk, and minimal or no risk, and says high-risk systems require risk management, high-quality data, logging, documentation, deployer information, human oversight, robustness, cybersecurity, and accuracy.
- [fact; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] Microsoft's AI risk assessment guidance says severity should increase when a model uses sensitive personal or regulated data, is part of a business-critical system, affects physical safety, or supports critical infrastructure.
- [fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Azure Cloud Adoption Framework guidance says intake should examine workload purpose, data sources, intended outcomes, external dependencies, integration risks, misuse scenarios, and regional legal requirements before deployment.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] The shared routing signals across standards and platform guidance are data sensitivity, impact criticality, autonomy level, external user or customer effect, integration depth, third-party dependency exposure, and regulatory classification.
- [inference; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Any use case that affects employment, credit, safety, regulated decisions, or other fundamental-rights-sensitive outcomes should bypass lightweight routing and enter the pro-code custom lane with formal review, even if a low-code platform could technically implement it.

#### B. What belongs in the business-led low-code lane

- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Microsoft describes a Power Platform Center of Excellence as a strategic organizational capability that balances innovation and control, scales citizen development, and connects low-code initiatives to governance and measurable outcomes.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] The CoE guidance says administrators should define requirements for a compliant app or maker, decide what information is needed per app or maker, determine what happens to noncompliant apps and makers, and support makers with templates, training, and best practices.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] Managed Environments are Microsoft-supported tenant-scale controls that let administrators manage Power Platform adoption with more control, less effort, and more insights.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] Power Platform data policies act as connector guardrails, can block actions at design time and runtime, and can suspend or quarantine apps, flows, or chatbots that violate policy.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] Power Platform governance is especially focused on connector use, custom connectors, saved credentials, and the risk that makers unintentionally expose organizational data.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] The business-led low-code lane is appropriate when the use case stays inside an approved platform boundary, uses sanctioned connectors and managed environments, has reversible workflow consequences, and does not require bespoke model or infrastructure engineering.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] The minimum checkpoints for this lane are maker onboarding, environment approval, connector and data policy review, ownership registration, usage monitoring, and a documented escalation rule for anything that touches sensitive data, external users, or business-critical actions.

#### C. What belongs in the pro-code custom lane

- [fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Azure guidance recommends formal policies for model selection and onboarding, third-party tools and data, data sensitivity, data quality, monitoring and retraining, regional compliance, misuse controls, integration, and transition from legacy processes.
- [fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Azure guidance also recommends systematic monitoring, standardized reporting, and independent review, with quarterly risk assessments for high-risk workloads and annual assessments for lower-risk systems.
- [fact; source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en] Google Cloud's AI and ML operational excellence guidance calls for explicit problem definition, measurable outcomes, version control for code, models, and data, observability, CI/CD, controlled releases, and model monitoring.
- [fact; source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] AWS says the Machine Learning Lens applies to custom-built models and pre-trained solutions across the full machine learning lifecycle and emphasizes responsible implementation and continuous monitoring as data and model behavior change over time.
- [fact; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] Microsoft's AI risk assessment organizes controls around machine learning security policies, data collection, data processing, model training, model deployment, system monitoring, incident management, and business continuity and disaster recovery.
- [inference; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] The pro-code custom lane should be selected when a use case depends on custom code, custom model behavior, sensitive or regulated data, deep integration into operational systems, external user impact, or ongoing reliability and security engineering that low-code guardrails cannot provide.
- [inference; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] The minimum checkpoints for this lane are architecture review, security and privacy review, legal and compliance review where relevant, model onboarding and validation, human oversight design, controlled release, incident response readiness, and post-deployment monitoring.

#### D. What belongs in the developer productivity lane

- [fact; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise] GitHub Copilot exposes enterprise and organization policies for feature availability, privacy-sensitive actions, and model access, and enterprise owners can centrally enable, disable, or delegate those controls.
- [fact; source: https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise] GitHub's enterprise policy surface includes separate controls for Copilot, AI agents, and Model Context Protocol (MCP) servers where that support is generally available.
- [fact; source: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] GitHub's responsible-use guidance says Copilot suggestions are only added if the user accepts them and that users remain responsible for reviewing, validating, and securely testing generated code.
- [fact; source: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] GitHub also says Copilot should be used as a tool rather than a replacement, and highlights risks around insecure code, public-code matches, inaccurate output, and legal or regulatory obligations.
- [inference; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The developer productivity lane is appropriate when the AI system assists engineers with coding, review, or documentation inside existing human-governed software delivery processes and does not directly execute regulated or customer-facing business decisions.
- [inference; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The minimum checkpoints for this lane are enterprise policy configuration, privacy and data-retention decisions, feature and model scoping, secure coding standards, and mandatory human acceptance before generated output reaches production.

#### E. Operating model, route ownership, and likely failure modes

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] Prior completed work and Microsoft's CoE guidance both support a central team that owns shared governance, standards, and enablement while downstream teams retain delivery ownership inside approved boundaries.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] Prior completed work on capability reuse and Azure governance both imply that intake should ask whether a use case can reuse approved models, platforms, and controls before allowing net-new tooling or architecture.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies] The central platform team should own the shared enterprise governance layer: approved platforms and models, identity and access patterns, logging standards, evaluation requirements, connector and tool policies, and the escalation rubric that moves work between lanes.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The most common misrouting failures are allowing low-code automation to reach sensitive or high-impact actions without escalation, treating custom production systems as if platform defaults were sufficient controls, and treating developer tools as if code-generation speed removed the need for review.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] A split by vendor stack is usually a weak primary routing choice because the strongest intake signals are risk and control requirements rather than whether the implementation happens to land on one platform or another.

### §3 Reasoning

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] Baseline governance frameworks agree that AI routing should be risk-proportional, documented, and continuously monitored.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] Low-code platform guidance supports a business-led lane only when a central team can constrain environments, connectors, and compliance posture.
- [fact; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] Cloud AI architecture guidance supports a pro-code lane for workloads that need custom engineering, lifecycle controls, and operational monitoring.
- [fact; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] Developer productivity guidance supports a separate internal-tooling lane with policy controls and mandatory human review rather than model-risk-style approval for every use.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.github.com/en/copilot/concepts/policies] The logical synthesis is a single intake rubric with three routes, because the governing question is not "which vendor?" but "which control surface can safely host this use case?"
- [inference; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The strongest escalation triggers are sensitive data, high-impact outcomes, autonomous action, regulated domains, deep integration, and the possibility that generated output changes production systems or rights-bearing decisions.

### §4 Consistency Check

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] No material contradiction remained between standards, regulators, and cloud governance guidance on the need for proportional controls, documentation, human oversight, and monitoring.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] The apparent tension between business-led low-code enablement and centrally governed developer tooling is resolved by treating them as separate lanes with different central policy levers.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The evidence supports one common intake form but not one common review depth, because route-specific controls differ materially even when the same enterprise platform team owns the underlying guardrails.

### §5 Depth and Breadth Expansion

- [fact; source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] Technical lens: pro-code systems create larger lifecycle and observability demands because code, models, data pipelines, and release mechanisms all change together.
- [fact; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html] Regulatory lens: risk classification and accountability obligations become stricter as a use case approaches rights-bearing, safety-sensitive, or externally deployed decisions.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] Economic lens: low-code creates value when central policies and reusable templates reduce the marginal cost of business automation without forcing every workflow into a full engineering queue.
- [fact; source: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion; https://docs.github.com/en/copilot/concepts/policies] Behavioural lens: developer productivity tools create local speed gains quickly, so organizations need explicit policy and review norms to stop convenience from becoming unsupervised production change.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] The mature operating pattern is a hybrid model: one central team owns common policies and the shared enterprise governance layer, while route-specific builders stay close to the business users or engineers they serve.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Enterprises should use a three-lane routing framework with one shared intake rubric: route low-criticality, approved-platform business automation to a low-code lane, route sensitive or deeply integrated systems to a pro-code custom lane, and route internal engineering assistance to a developer productivity lane.
- [inference; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The decisive routing signals are data sensitivity, outcome criticality, autonomy, integration depth, third-party dependency exposure, and regulatory classification rather than vendor preference.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies] A central platform team should own the shared enterprise governance layer, approved tools, and escalation rubric, and routing should follow risk signals rather than vendor-stack silos because the same platform family can host both low-risk assistance and higher-control workflows.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] Misrouting causes predictable failures: low-code controls can be too weak for high-impact systems, pro-code review can be unnecessarily heavy for internal assistance, and developer tools can bypass policy if treated as harmless by default.

**Key findings:**

1. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] **High confidence:** Enterprises need one intake rubric that scores data sensitivity, impact criticality, autonomy, integration depth, and regulatory exposure before deciding which AI delivery lane a use case should enter.
2. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] **Medium confidence:** The business-led low-code lane is most defensible for approved-platform workflows where central administrators can enforce managed environments, connector guardrails, maker accountability, and rapid escalation of noncompliant apps.
3. [inference; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] **High confidence:** The pro-code custom lane should be selected when a use case depends on custom engineering, sensitive or regulated data, deep system integration, or operational controls that must span the full model and software lifecycle.
4. [inference; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] **Medium confidence:** Developer productivity AI is best treated as an internal tooling lane with enterprise policy controls, privacy decisions, and mandatory human review rather than as unattended business automation.
5. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] **Medium confidence:** The central platform team should own the shared enterprise governance layer and approved capabilities, while business or engineering teams should own route-specific implementation after the intake decision is made.
6. [inference; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] **Medium confidence:** The most reliable escalation triggers are trusted-boundary breaks, unsupervised action, production-system change, and rights-bearing decisions, because these signals consistently increase security, compliance, and operational risk across frameworks.
7. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/concepts/policies] **Medium confidence:** The main failure modes are misrouting low-code automation into high-impact domains, forcing low-risk internal assistance through heavyweight committees, and allowing AI tools or connectors to bypass central policy settings.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] One intake rubric should score shared risk signals before any platform choice. | https://www.nist.gov/itl/ai-risk-management-framework<br>https://www.iso.org/standard/81230.html<br>https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai<br>https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern | high | Cross-framework convergence on proportional governance. |
| [inference] The business-led low-code lane is most defensible when managed environments, connector guardrails, and maker accountability are in place. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview<br>https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview<br>https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention | medium | Evidence comes from Microsoft low-code governance guidance. |
| [inference] The pro-code custom lane should be selected when lifecycle controls must span design, deployment, monitoring, and incident response. | https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern<br>https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en<br>https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html<br>https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment | high | Evidence spans Microsoft, Google Cloud, and AWS guidance. |
| [inference] Developer productivity tools are best treated as an internal tooling lane with enterprise policy controls and human review requirements. | https://docs.github.com/en/copilot/concepts/policies<br>https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise<br>https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion | medium | Evidence comes from GitHub governance and responsible-use guidance. |
| [inference] The central platform team should own the shared enterprise governance layer and approved capabilities. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md<br>https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md<br>https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview | medium | Prior repository work and CoE guidance point to central ownership plus federated delivery. |
| [inference] Boundary breaks, unsupervised action, production change, and rights-bearing outcomes are the strongest escalation triggers. | https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment<br>https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern<br>https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention<br>https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion | medium | These signals recur across all three routes. |
| [inference] Misrouting and policy bypasses create the dominant governance failures. | https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention<br>https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment<br>https://docs.github.com/en/copilot/concepts/policies | medium | Failure pattern emerges from route-specific control gaps. |

**Assumptions:**

- None.

**Analysis:**

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The strongest evidence came from standards and regulatory sources, which agree on proportional governance but do not prescribe enterprise intake lanes by name.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] Product-specific governance documentation was then used to map those generic control expectations onto concrete lanes: low-code, pro-code, and developer productivity.
- [inference; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] The pro-code lane has the deepest evidence because cloud architecture guidance describes model lifecycle, observability, and release practices in detail.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies] A vendor-stack-based routing alternative is weaker than risk-signal routing, because the same platform family can host both lightly governed assistance and higher-control workflows, so platform brand alone does not determine review depth.

**Risks, gaps, uncertainties:**

- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Public platform documentation describes available governance levers, but it rarely publishes numeric scoring thresholds for route assignment, so specific cutoff values remain an implementation choice for each enterprise.
- [inference; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The European Commission's AI Act identifies prohibited, high-risk, transparency, and minimal-or-no-risk categories, but enterprise intake still needs internal judgment for cases that are not explicitly named as prohibited or high risk.
- [inference; source: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] Developer productivity tooling can drift into higher-risk territory if an organization adds autonomous code execution or direct production actions, so the route boundary must be reviewed as tooling capabilities change.

**Open questions:**

- What scoring rubric and threshold bands are most usable for a real backlog intake form across these three lanes?
- How should enterprises route AI agents that both assist developers and can execute production actions, such as deployment or support automation?
- Which evidence artifacts should be mandatory at each checkpoint for regulated sectors such as banking or healthcare?

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] The synthesis is supported by a consistent evidence chain from baseline governance frameworks to route-specific platform controls.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] All material uncertainties are explicit and center on threshold design and future route drift rather than on disagreement about the core lane structure.
- Acronym expansion audit completed.
- Claim-label audit completed.
- Em-dash audit completed.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

[inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Enterprises should use a three-lane routing framework with one shared intake rubric: route low-criticality, approved-platform business automation to a low-code lane, route sensitive or deeply integrated systems to a pro-code custom lane, and route internal engineering assistance to a developer productivity lane.
[inference; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The routing decision should be driven by data sensitivity, outcome criticality, autonomy, integration depth, third-party dependency exposure, and regulatory classification rather than by vendor preference or team habit.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies] A central platform team should own the shared enterprise governance layer, approved tools, and escalation rubric, and routing should follow risk signals rather than vendor-stack silos because the same platform family can host both low-risk assistance and higher-control workflows.
[inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] The main operational risk is misrouting, because lightweight platform controls are insufficient for high-impact systems and heavyweight review is wasteful for low-risk internal assistance.

### Key Findings

1. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern] **High confidence:** Enterprises need one intake rubric that scores data sensitivity, impact criticality, autonomy, integration depth, and regulatory exposure before deciding which AI delivery lane a use case should enter.
2. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention] **Medium confidence:** The business-led low-code lane is most defensible for approved-platform workflows where central administrators can enforce managed environments, connector guardrails, maker accountability, and rapid escalation of noncompliant apps.
3. [inference; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] **High confidence:** The pro-code custom lane should be selected when a use case depends on custom engineering, sensitive or regulated data, deep system integration, or operational controls that must span the full model and software lifecycle.
4. [inference; source: https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] **Medium confidence:** Developer productivity AI is best treated as an internal tooling lane with enterprise policy controls, privacy decisions, and mandatory human review rather than as unattended business automation.
5. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview] **Medium confidence:** The central platform team should own the shared enterprise governance layer and approved capabilities, while business or engineering teams should own route-specific implementation after the intake decision is made.
6. [inference; source: https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] **Medium confidence:** The most reliable escalation triggers are trusted-boundary breaks, unsupervised action, production-system change, and rights-bearing decisions, because these signals consistently increase security, compliance, and operational risk across frameworks.
7. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment; https://docs.github.com/en/copilot/concepts/policies] **Medium confidence:** The main failure modes are misrouting low-code automation into high-impact domains, forcing low-risk internal assistance through heavyweight committees, and allowing AI tools or connectors to bypass central policy settings.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] One intake rubric should score shared risk signals before any platform choice. | https://www.nist.gov/itl/ai-risk-management-framework<br>https://www.iso.org/standard/81230.html<br>https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai<br>https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern | high | Cross-framework convergence on proportional governance. |
| [inference] The business-led low-code lane is most defensible when managed environments, connector guardrails, and maker accountability are in place. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview<br>https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview<br>https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention | medium | Evidence comes from Microsoft low-code governance guidance. |
| [inference] The pro-code custom lane should be selected when lifecycle controls must span design, deployment, monitoring, and incident response. | https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern<br>https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en<br>https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html<br>https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment | high | Evidence spans Microsoft, Google Cloud, and AWS guidance. |
| [inference] Developer productivity tools are best treated as an internal tooling lane with enterprise policy controls and human review requirements. | https://docs.github.com/en/copilot/concepts/policies<br>https://docs.github.com/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise<br>https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion | medium | Evidence comes from GitHub governance and responsible-use guidance. |
| [inference] The central platform team should own the shared enterprise governance layer and approved capabilities. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md<br>https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md<br>https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview | medium | Prior repository work and CoE guidance point to central ownership plus federated delivery. |
| [inference] Boundary breaks, unsupervised action, production change, and rights-bearing outcomes are the strongest escalation triggers. | https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment<br>https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern<br>https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention<br>https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion | medium | These signals recur across all three routes. |
| [inference] Misrouting and policy bypasses create the dominant governance failures. | https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention<br>https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment<br>https://docs.github.com/en/copilot/concepts/policies | medium | Failure pattern emerges from route-specific control gaps. |

### Assumptions

- None.

### Analysis

[inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The standards and regulatory sources were weighted most heavily because they define the control objectives that any routing framework must satisfy, even though they do not name the three lanes directly.
[inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies; https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion] Route-specific platform guidance was then used to map those generic objectives onto concrete control surfaces, which is why the low-code and developer productivity lanes are justified as distinct patterns rather than as mere subcases of general AI governance.
[inference; source: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern; https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence?hl=en; https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html] The pro-code custom lane has the most detailed checkpoint evidence because cloud architecture frameworks describe model lifecycle, observability, CI/CD, controlled release, and post-deployment monitoring in operational detail.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md; https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention; https://docs.github.com/en/copilot/concepts/policies] A vendor-stack-based routing alternative is weaker than risk-signal routing, because the same platform family can host both lightly governed assistance and higher-control workflows, so platform brand alone does not determine review depth.

### Risks, Gaps, and Uncertainties

[fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview; https://docs.github.com/en/copilot/concepts/policies] Public platform documentation describes available governance levers, but it rarely publishes numeric scoring thresholds for route assignment, so each enterprise still needs to calibrate its own cutoff values.
[inference; source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai] The AI Act identifies prohibited, high-risk, transparency, and minimal-or-no-risk categories, but enterprise intake still needs internal judgment for cases that are not explicitly named as prohibited or high risk.
[inference; source: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-completion; https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment] The route boundary for developer productivity tools could shift if organizations allow those tools to execute production changes autonomously, because that would move them closer to operational automation than to supervised assistance.

### Open Questions

- What scoring rubric and threshold bands are most usable for a real backlog intake form across these three lanes?
- How should enterprises route AI agents that both assist developers and can execute production actions, such as deployment or support automation?
- Which evidence artifacts should be mandatory at each checkpoint for regulated sectors such as banking or healthcare?

### Output

- Type: knowledge
- Description: Three-lane enterprise routing framework for AI use-case intake, including route-selection signals and governance checkpoints for low-code, pro-code, and developer productivity work.
- Links:
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern
  - https://docs.github.com/en/copilot/concepts/policies

---

## Output

*(Filled in on completion.)*

- Type: knowledge
- Description: Research note defining an enterprise AI intake and routing framework across low-code business-led, pro-code custom, and developer productivity lanes.
- Links:
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern
  - https://docs.github.com/en/copilot/concepts/policies

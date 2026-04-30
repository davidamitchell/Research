---
review_count: 2
title: "How should AI and low-code governance integrate with existing software development and platform engineering practices?"
added: 2026-04-26T10:11:11+00:00
status: completed
priority: high
blocks: [2026-04-26-ai-governance-cost-performance-delivery-impact, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
tags: [sdlc, platform-engineering, ci-cd, devops, ai-governance, low-code, testing, release-management, infrastructure-as-code, enterprise-engineering]
started: 2026-04-26T22:30:44+00:00
completed: 2026-04-26T22:48:30+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How should AI and low-code governance integrate with existing software development and platform engineering practices?

## Research Question

How should Artificial Intelligence (AI) and low-code governance integrate with existing software development and platform engineering practices, specifically, how should governance controls be integrated with Continuous Integration/Continuous Delivery (CI/CD) pipelines, infrastructure as code (IaC), testing frameworks, release management, and platform engineering standards to avoid fragmentation between traditional and AI or low-code delivery models?

## Scope

**In scope:**
- Integration of AI and low-code governance checks into CI/CD pipelines, including automated governance gates such as security scanning, compliance checks, license validation, model performance tests, and low-code dependency checks.
- IaC for AI and low-code governance, including governance policy, environment configuration, deployment constraints, and platform resource configuration expressed as code rather than manual setup.
- Testing frameworks for AI and low-code artifacts, including unit testing for low-code logic, integration testing for AI plus human workflows, and evaluation frameworks for Large Language Model (LLM) and Retrieval-Augmented Generation (RAG) systems.
- Release management for AI and low-code artifacts that share dependencies, data, environments, or user interfaces with traditional software.
- Platform engineering standards, especially internal developer platform (IDP) paved roads that embed governance by default.
- Prevention of fragmented operating models in which AI or low-code delivery uses different approval, evidence, or release mechanics from the rest of the estate.

**Out of scope:**
- Lifecycle management of AI artifacts, because that is covered by Q7.
- Detailed enforcement-layer architecture at deployment time, because that is covered by Q3.
- Vendor-specific capability ceilings across every low-code or AI platform, because that is covered by Q11.

**Constraints:**
- The answer must address both the developer-facing workflow and the governance-facing assurance model.
- The answer must cover non-deterministic testing for AI systems and avoid pretending that classic binary test outcomes are always sufficient.
- The answer should remain usable in a multi-platform enterprise that already runs conventional software engineering, platform engineering, and release-management practices.

## Context

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html] Enterprises create governance seams when AI and low-code delivery uses a separate release path from conventional software, because release gates, evidence objects, and rollback controls then stop lining up across the same production estate.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] Existing secure-development and platform-engineering literature already assumes that delivery quality comes from integrating controls into normal engineering flow rather than from a parallel audit process after development finishes.
- [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Current delivery platforms already expose promotion gates, approvals, and protected environments, so the practical problem is how to extend those mechanisms to AI and low-code artifacts rather than how to invent a completely separate governance track.

Cross-references:
- Q3: `2026-04-26-ai-lowcode-governance-enforcement-architecture`
- Q7: `2026-04-26-ai-lowcode-lifecycle-management`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **CI/CD governance gate design:** review which conventional software gates already transfer to AI and low-code delivery, and which additional gates are needed for prompts, models, connectors, evaluations, and low-code artifacts.
2. **Infrastructure as code for AI governance:** assess how IaC can define AI platform resources, identities, network boundaries, environment defaults, and deployment settings as reviewable code.
3. **AI testing frameworks:** review official documentation for AI evaluation frameworks and assess how they fit into standard test runners and pipeline stages.
4. **Platform engineering patterns:** assess how IDP templates, catalogs, and plugins can encode AI and low-code governance by default.
5. **Fragmentation risk assessment:** identify how separate delivery models create audit, rollback, evidence, and control inconsistencies.
6. **Synthesis:** produce practical integration patterns for pipelines, IaC, testing, release management, and IDP scaffolding.

## Sources

- [x] [DevOps Research and Assessment (DORA) Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) — - platform engineering, delivery stability, testing, and continuous-improvement evidence.
- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-218, Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) — - secure-development practices intended to integrate into each Software Development Life Cycle (SDLC) implementation.
- [x] [GitHub Actions deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — - protected environments, required reviewers, branch restrictions, and third-party deployment gates.
- [x] [GitHub custom deployment protection rules](https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules) — - external change, observability, and quality systems as release gates.
- [x] [Azure DevOps approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) — - resource-owned approvals and checks outside pipeline code.
- [x] [Backstage overview](https://backstage.io/docs/overview/what-is-backstage) — - developer portal, software catalog, templates, docs, and plugin model.
- [x] [Backstage software templates](https://backstage.io/docs/features/software-templates/) — - scaffolding steps, input review, task execution, and standardization mechanisms.
- [x] [Backstage plugins](https://backstage.io/plugins/) — - evidence that Backstage exposes an extensible plugin ecosystem rather than a fixed portal surface.
- [x] [DeepEval documentation](https://docs.confident-ai.com/) — - pytest-native AI evaluations that run in CI/CD and expose research-backed metrics.
- [x] [Ragas documentation](https://docs.ragas.io/en/latest/) — - experiments-first evaluation loops for RAG and other LLM applications.
- [x] [Terraform documentation](https://developer.hashicorp.com/terraform/docs) — - reusable modules, Command Line Interface (CLI) workflows, and team governance.
- [x] [Use Terraform to create Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform) — - official Microsoft source showing AI Foundry resources, projects, deployments, connections, and capability hosts managed with Terraform providers.
- [x] [Terraform resource for Amazon Bedrock agents](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent) — - official registry evidence that Amazon Bedrock agent resources are represented as Terraform-managed objects.
- [x] [Open Policy Agent (OPA) integration](https://openpolicyagent.org/docs/integration) — - policy decision decoupling, management interfaces, status, health, and decision logs.
- [x] [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) — - native low-code pipeline governance, deployment validation, delegated deployments, and extensibility.
- [x] [Block unmanaged customizations](https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations) — - production lock-down and explicit statement that Copilot Studio publishing fails when unmanaged customizations are blocked.
- [x] [Managed Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) — - environment-level governance features for Power Platform.
- [x] [Publish and deploy your agent in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels) — - direct publish behavior across connected channels and the need for publish-time testing.
- [x] [Deploy a prompt flow for real-time inference](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy) — - direct deployment flow for prompt-based AI endpoints and current retirement notice for Prompt Flow.
- [x] [What lifecycle management model is required for AI models, prompts, and low-code applications?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html) — - related repository work on versioning, rollback, and promoted artifact state.
- [x] [Where should governance enforcement points be implemented within enterprise architecture?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html) — - related repository work on layered enforcement.
- [x] [Deployment pipeline as the only enforceable control gate for citizen-developed agents](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html) — - related repository work on low-code release governance.
- [x] [What control-plane architecture is required to manage AI agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — - related repository work on policy distribution and feedback loops.

## Related

- [What lifecycle management model is required for AI models, prompts, and low-code applications?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html)
- [Where should governance enforcement points be implemented within enterprise architecture?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html)
- [Deployment pipeline as the only enforceable control gate for citizen-developed agents](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html)
- [What control-plane architecture is required to manage AI agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] **Research question restated:** this item asks how AI and low-code governance should be folded into the same engineering delivery system that already governs conventional software, specifically across pipelines, IaC, testing, release management, and platform-engineering paved roads.
- [fact; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] **Scope confirmed:** the investigation covers build-time checks, promotion-time gates, infrastructure codification, AI-specific evaluation tooling, low-code deployment controls, and IDP scaffolding.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] **Prior work cross-reference:** adjacent completed items already established that governance controls must attach to concrete enforcement layers, artifacts need lifecycle state, low-code publication needs a governed release gate, and a central policy distribution model matters, so this item narrows the question to day-to-day engineering integration.
- [fact; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy] **Constraint confirmed:** non-deterministic systems require evaluation loops and regression thresholds rather than only classic binary test assertions, and vendor publish paths can otherwise bypass enterprise release discipline.
- **Output format:** knowledge, specifically an integration model and operating guidance for platform teams, delivery teams, and governance functions.

### §1 Question Decomposition

- **Root question:** What delivery model lets AI and low-code systems inherit the strengths of mainstream software engineering without creating a parallel and weaker governance path?
- **A. CI/CD integration**
  - A1. Which conventional secure-development gates already transfer directly to AI and low-code artifacts?
  - A2. Which new AI or low-code specific checks must be added to the same pipeline?
  - A3. Which promotion controls must live outside pipeline-authored code to remain authoritative?
- **B. IaC integration**
  - B1. Which AI and low-code control surfaces can be represented as managed infrastructure objects?
  - B2. Which environment defaults and deployment constraints should be reviewable in code?
- **C. Testing integration**
  - C1. How should AI evaluation frameworks fit beside unit, integration, and end-to-end tests?
  - C2. What can deterministic test frameworks still cover for low-code and orchestration logic?
  - C3. What evidence is required when outputs are non-deterministic?
- **D. Platform engineering integration**
  - D1. How can IDP templates and catalogs make governance the default path?
  - D2. What plugin and documentation surfaces help teams see ownership, controls, and evidence?
- **E. Release management integration**
  - E1. Which artifacts need to move together through the release graph?
  - E2. How should approval, rollback, and environment protection work when code and AI or low-code assets change together?
- **F. Fragmentation risk**
  - F1. What failures appear when AI and low-code delivery uses a separate process?
  - F2. What integration patterns close those failure modes?

### §2 Investigation

- #### A. Conventional secure-development and delivery controls already provide the baseline
  - [fact; source: https://csrc.nist.gov/pubs/sp/800/218/final] NIST SP 800-218 says secure software development practices should be integrated into each SDLC implementation rather than treated as a separate lifecycle.
  - [fact; source: https://csrc.nist.gov/pubs/sp/800/218/final] The SSDF explicitly aims to reduce released vulnerabilities, mitigate the impact of undetected flaws, and address root causes, which makes it a transferable baseline for AI and low-code artifacts that still ship into the same production estate.
  - [fact; source: https://dora.dev/research/2024/dora-report/] The 2024 DORA report says Artificial Intelligence increases individual productivity but can reduce software-delivery stability and throughput, and it separately says platform engineering improves productivity while requiring careful implementation focused on developer independence.
  - [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] The baseline implication is that AI and low-code delivery should inherit the ordinary secure-delivery system and then add safeguards, because treating AI as a parallel process would discard the same fundamentals that DORA says still matter.

- #### B. Modern pipeline platforms already support governance gates that can host AI and low-code checks
  - [fact; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments] GitHub Actions environments support required reviewers, wait timers, deployment branch restrictions, and custom deployment protection rules that can call third-party change, observability, or quality systems before a protected job runs.
  - [fact; source: https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules] GitHub custom deployment protection rules run automatically whenever a workflow job targets a protected environment and can wait for up to 30 days for an approve or reject decision from an external system.
  - [fact; source: https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops] Azure DevOps approvals and checks are configured on resources through the web interface rather than in pipeline Yet Another Markup Language (YAML), which prevents pipeline authors from weakening the production gate in the same pull request (PR) that introduces a risky change.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Power Platform pipelines centrally govern citizen-led and pro-developer projects, prevalidate deployments against target environments, validate connections and environment variables, support delegated deployments, and can be extended and integrated with other CI/CD tools.
  - [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] The practical pattern is to keep build logic in repository-controlled pipelines but place promotion authority on protected environments or external resource checks so that release control remains harder to bypass than repository code review.

- #### C. AI and low-code delivery need extra test categories, not a separate test universe
  - [fact; source: https://docs.confident-ai.com/] DeepEval describes itself as pytest-native, states that evaluations run in CI/CD or as Python scripts, and exposes research-backed metrics such as hallucination, faithfulness, answer relevancy, toxicity, bias, and conversational metrics.
  - [fact; source: https://docs.ragas.io/en/latest/] Ragas says it is built around experiments, metrics, and datasets for LLM applications and positions itself as a systematic evaluation loop rather than an informal vibe check.
  - [fact; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] Both tools frame AI quality as repeated measurement over scenarios and datasets instead of a single deterministic assertion per change.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Power Platform pipelines still perform conventional deployment validation, such as dependency checks and environment-variable validation, which means low-code artifacts continue to benefit from ordinary deterministic checks.
  - [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://csrc.nist.gov/pubs/sp/800/218/final] The testing pyramid therefore expands rather than resets: deterministic unit or dependency tests still cover logic, schemas, and connectors, while AI evaluations add scenario suites, threshold checks, and regression budgets for non-deterministic behavior.

- #### D. IaC can codify a large part of the AI and low-code control surface
  - [fact; source: https://developer.hashicorp.com/terraform/docs] Terraform documentation positions modules as reusable configurations and HashiCorp Cloud Platform (HCP) Terraform as team-oriented infrastructure management with version control, state sharing, and governance.
  - [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform] Microsoft documents AI Foundry creation with Terraform and states that the AzAPI provider can manage Foundry control-plane configurations, including preview features, while the AzureRM provider covers core capabilities such as resources, projects, and deployments.
  - [fact; source: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent] The official HashiCorp Terraform Registry exposes Amazon Bedrock agent resources as declarative objects, which means agent configuration itself can sit inside the same change-review and promotion path as other infrastructure.
  - [fact; source: https://openpolicyagent.org/docs/integration] OPA separates policy evaluation from management, distributes policies centrally, and exposes status, health, and decision logs as management-plane interfaces.
  - [inference; source: https://developer.hashicorp.com/terraform/docs; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent; https://openpolicyagent.org/docs/integration] The useful IaC boundary is therefore broader than network and compute: enterprises can version AI platform resources, deployments, policy bundles, environment defaults, and portions of agent configuration as reviewable code, then pair that with runtime policy engines for decisions that must remain dynamic.

- #### E. Platform engineering should make the governed path the easiest path
  - [fact; source: https://backstage.io/docs/overview/what-is-backstage] Backstage defines itself as an open source framework for developer portals built around a software catalog, software templates, TechDocs, and a plugin ecosystem.
  - [fact; source: https://backstage.io/docs/features/software-templates/] Backstage software templates collect inputs, review them before execution, run multi-step template tasks, and can publish templated repositories to systems such as GitHub or GitLab.
  - [fact; source: https://backstage.io/plugins/] Backstage maintains a large plugin ecosystem rather than a closed fixed portal, which creates room for organization-specific governance views and integrations.
  - [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://backstage.io/docs/features/software-templates/; https://backstage.io/plugins/] An IDP can therefore encode AI and low-code governance by scaffolding the approved repository shape, default test harnesses, policy files, environment metadata, ownership records, and evidence links before a team writes any business logic.

- #### F. Low-code governance only becomes authoritative when direct publish paths are narrowed
  - [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels] Copilot Studio lets a maker publish from within the product, and publishing updates all connected channels for the agent.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] Microsoft states that blocking unmanaged customizations ensures changes in an environment come only from approved Application Lifecycle Management (ALM) processes and explicitly states that Copilot Studio publishing does not work when the setting is enabled.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Managed Environments and Power Platform pipelines give administrators a governed environment surface, while pipelines add validation, delegated deployments, analytics, and extension points.
  - [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Low-code estates cannot rely on pipeline governance alone if creators still retain an easier direct publish route, so environment restrictions and managed artifact rules are part of SDLC integration rather than an optional side control.

- #### G. Release management must treat AI and low-code artifacts as first-class release objects
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html] The related lifecycle item concludes that models, prompts, and low-code applications need explicit versioning, rollback-ready prior versions, and a common artifact ledger.
  - [fact; source: https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy] Microsoft documents a direct deployment path for prompt flows to online endpoints and also notes that Prompt Flow development has ended and the feature will retire, which illustrates that AI delivery tooling can change materially even when application intent does not.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Power Platform pipelines treat solutions and configuration as deployable units and validate target-environment compatibility before deployment starts.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html; https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Release management should therefore promote code, prompt or model configuration, low-code solution packages, policy bundles, and environment metadata as one dependency-aware release set whenever they jointly determine runtime behavior.

- #### H. The main fragmentation failures are duplicated standards, missing evidence, and bypassable controls
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Adjacent completed items in this repository show that governance fails when the release gate is bypassable, when controls are not attached to concrete enforcement layers, and when policy distribution and evidence remain split across tool surfaces.
  - [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/; https://backstage.io/docs/overview/what-is-backstage; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] Fragmentation between conventional software delivery and AI or low-code delivery mainly recreates four avoidable defects: duplicated control catalogs, weak release authority, incompatible evidence objects, and missing shared platform ownership.

### §3 Reasoning

- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] The strongest pattern in the sources is continuity rather than exception, because both secure-development guidance and delivery-performance research treat good outcomes as a product of integrated engineering systems, not of separate governance processes.
- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] AI and low-code add artifact classes and evaluation methods, but they do not remove the need for deterministic validation, protected promotion, and explicit environment ownership.
- [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://openpolicyagent.org/docs/integration; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] The integration problem is therefore architectural: the governed path has to be pre-scaffolded, policy-backed, and environment-protected so that it becomes simpler than bypass.

### §4 Consistency Check

- [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] The source set is internally consistent that promotion controls should sit on protected resources or environments, not only inside mutable repository-defined pipeline logic.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] The source set is also internally consistent that low-code direct publication is a real bypass path unless administrators narrow it with environment-level restrictions.
- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] No reviewed source claims that non-deterministic AI quality can be reduced to a single definitive pass or fail assertion, so the synthesis keeps evaluation as thresholded regression evidence rather than as a perfect binary oracle.

### §5 Depth and Breadth Expansion

- [inference; source: https://dora.dev/research/2024/dora-report; https://backstage.io/docs/overview/what-is-backstage] **Technical lens:** platform engineering helps only if it preserves developer independence, so AI governance integration should arrive as paved roads and templates rather than as manual ticket handoffs.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://openpolicyagent.org/docs/integration] **Control lens:** policy-as-code only works durably when policy distribution, health, and decision logging are treated as managed interfaces, not as ad hoc scripts embedded in one repository.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy; https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels] **Vendor-change lens:** AI delivery tooling changes quickly enough that release management has to track deployable artifacts and platform dependencies together, because a vendor retirement or a changed publish surface can alter production behavior without a classic code rewrite.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/alm/pipelines; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] **Behavioral lens:** citizen and low-code builders will follow the shortest route to a working outcome, so the enterprise must make the approved route the shortest route and actively disable easier bypasses in production-capable environments.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] AI and low-code governance should be integrated into the same platform-engineering delivery system as conventional software, with any additional specialized assurance lane for higher-risk AI or low-code changes implemented as an extension of shared CI/CD, release, and environment controls rather than as a separate parallel process.
- [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] Build pipelines can own repository-defined checks, but production promotion authority should stay on protected environments, resource-owned approvals, and low-code environment restrictions so that the release gate remains harder to bypass than a code change.
- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] AI testing belongs inside the ordinary test stack as scenario suites, regression thresholds, and experiment runs placed beside deterministic unit, dependency, and integration tests, because non-deterministic outputs need evidence loops rather than a separate quality discipline.
- [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://backstage.io/docs/features/software-templates/; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform] Platform teams should encode the governed path as templates, catalogs, modules, policy bundles, and deployment defaults so that teams start from a compliant scaffold instead of bolting governance on after delivery.

**Key findings:**

1. [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] **High:** AI and low-code delivery should extend the existing SDLC rather than run a separate one, and when higher-risk changes need specialized assurance that lane should remain inside the shared delivery system because the SSDF is designed to integrate into each lifecycle implementation and DORA still ties software outcomes to testing, stability, and platform-engineering fundamentals.
2. [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops] **High:** The strongest pipeline split is repository-owned build logic plus resource-owned promotion authority, because protected environments, custom deployment gates, and approvals or checks outside YAML keep production release control independent from the change being proposed.
3. [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] **High:** AI-specific quality assurance should be inserted into the normal test stack, or into a higher-risk assurance lane that still uses the same release system, as evaluation suites and regression thresholds while low-code artifacts still undergo deterministic validation for dependencies, environment variables, and connector wiring.
4. [inference; source: https://developer.hashicorp.com/terraform/docs; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent; https://openpolicyagent.org/docs/integration] **High:** IaC should cover AI platform resources, deployments, identities, environment defaults, and policy distribution wherever possible, because official Microsoft, Amazon, Terraform, and OPA sources all expose these surfaces as managed and reviewable configuration objects.
5. [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] **Medium:** Low-code governance is materially weaker when direct publication stays easier than governed promotion, because Copilot Studio supports in-product publishing and Microsoft separately documents environment controls that can force production changes back through approved ALM paths.
6. [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://backstage.io/docs/features/software-templates/; https://backstage.io/plugins/] **Medium:** IDPs should be the main platform-engineering vehicle for AI and low-code governance because templates, catalogs, docs, and plugins let teams inherit compliant repository structure, ownership metadata, and evidence hooks before development starts.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html; https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] **Medium:** Release management should promote code, prompt or model configuration, low-code packages, policy bundles, and environment metadata as one dependency-aware release set because each of those objects can materially change runtime behavior or rollback feasibility.
8. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://dora.dev/research/2024/dora-report/] **Medium:** The main organizational cost of fragmentation is not only duplicated process but weaker control authority, poorer evidence coherence, and lower change stability, because adjacent governance work and DORA both point to system design, not isolated checks, as the determinant of durable delivery quality.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AI and low-code delivery should extend the existing SDLC, with any higher-risk assurance lane kept inside the shared delivery system. | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final); [DORA 2024](https://dora.dev/research/2024/dora-report/) | high | SSDF is lifecycle-integrated; DORA says AI does not remove the need for testing and stable delivery fundamentals. |
| [inference] Production promotion authority should sit on protected environments or resource-owned checks, not only in repository pipeline code. | [GitHub environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments); [GitHub custom deployment protection rules](https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules); [Azure DevOps approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) | high | Each platform exposes non-repository-controlled approval or gating surfaces. |
| [inference] AI quality assurance belongs beside conventional tests, or in a higher-risk assurance lane that still uses the same release system, as evaluation suites and regression thresholds. | [DeepEval docs](https://docs.confident-ai.com/); [Ragas docs](https://docs.ragas.io/en/latest/); [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) | high | DeepEval and Ragas describe evaluation loops; Power Platform still performs deterministic deployment validation. |
| [inference] IaC should cover AI platform resources, deployments, identities, defaults, and policy distribution wherever the platform exposes them as managed objects. | [Terraform docs](https://developer.hashicorp.com/terraform/docs); [Microsoft Foundry Terraform](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform); [Terraform Bedrock agent resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent); [OPA integration](https://openpolicyagent.org/docs/integration) | high | Evidence spans generic IaC, Microsoft Foundry, Amazon Bedrock, and centralized policy management. |
| [inference] Low-code governance is materially weaker when direct publication stays easier than governed promotion. | [Copilot Studio publish](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels); [Block unmanaged customizations](https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations); [Managed Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) | medium | The evidence is strong for Microsoft tooling, but cross-vendor generalization remains a synthesis step. |
| [inference] IDPs should act as the main platform-engineering vehicle for AI and low-code governance defaults. | [Backstage overview](https://backstage.io/docs/overview/what-is-backstage); [Backstage software templates](https://backstage.io/docs/features/software-templates/); [Backstage plugins](https://backstage.io/plugins/) | medium | Official sources show the template, catalog, docs, and plugin mechanics; governance-specific implementation is a synthesis step. |
| [inference] Release management should promote code, prompt or model configuration, low-code packages, policy bundles, and environment metadata as one dependency-aware release set. | [Lifecycle management item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html); [Prompt Flow deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy); [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) | medium | Runtime behavior depends on more than source code, but the exact release-object recommendation remains a synthesis over adjacent evidence. |
| [inference] Fragmentation weakens control authority, evidence coherence, and change stability rather than merely adding administrative overhead. | [Enforcement architecture item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html); [Deployment pipeline item](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html); [Control-plane architecture item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html); [DORA 2024](https://dora.dev/research/2024/dora-report/) | medium | The conclusion is a cross-source synthesis over several governance surfaces rather than one direct quote. |

**Assumptions:**

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] This item does not rely on a separate unresolved assumption beyond the interpretive steps already marked as inference.

**Analysis:**

- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops] The strongest evidence supported reusing the existing engineering operating model because secure-development guidance and delivery platforms already separate mutable build logic from protected promotion authority.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/; https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] A plausible competing model is a shared SDLC baseline plus a specialized assurance lane for higher-risk AI or low-code changes, and the evidence supports that variation only when the additional lane remains an overlay inside the same delivery and release system rather than becoming a separate end-to-end process.
- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] AI evaluation tooling was treated as an extension to testing rather than as a replacement because both reviewed frameworks emphasize iterative experiments, metrics, and repeated runs instead of definitive one-shot judgments.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] Low-code evidence was weighted heavily because the reviewed Microsoft documentation shows both sides of the governance problem directly, namely the native bypass path and the native administrative control that blocks it.
- [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://openpolicyagent.org/docs/integration] The platform-engineering synthesis favored templates, modules, and policy distribution over checklist governance because those are the mechanisms that can scale across teams without depending on perfect manual compliance.

**Risks, gaps, uncertainties:**

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] The reviewed AI evaluation sources clearly support CI integration, but they do not by themselves define sector-wide accepted pass thresholds for every enterprise use case.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy] Microsoft is retiring Prompt Flow, so any release design built around that exact artifact needs migration planning and should not be treated as a durable long-term control surface.
- [inference; source: https://backstage.io/plugins/] Backstage's plugin ecosystem proves extensibility, but the evidence reviewed here does not show one standardized off-the-shelf plugin that already solves enterprise AI governance end to end.

**Open questions:**

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] Which evaluation-threshold patterns are reliable enough for regulated production promotion of customer-facing AI systems across repeated model upgrades?
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent] Which portions of AI platform governance remain stubbornly outside declarative IaC and therefore require compensating runtime controls or post-deploy verification?
- [inference; source: https://backstage.io/docs/features/software-templates/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] How should an enterprise connect low-code pipeline metadata, AI evaluation results, and repository catalogs into one evidence object that auditors and release managers can read without tool hopping?

### §7 Recursive Review

- Review outcome: claim labels, confidence levels, and source links were rechecked after the final edits.
- Review outcome: adjacent completed items were rescanned to confirm lifecycle, enforcement, release-gate, and control-plane alignment.
- Review outcome: the synthesis now distinguishes between a shared SDLC baseline and a specialized assurance lane for higher-risk AI or low-code changes.

---

## Findings

### Executive Summary

[inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] AI and low-code governance should be integrated into the same platform-engineering delivery system as conventional software, with any additional specialized assurance lane for higher-risk AI or low-code changes implemented as an extension of shared CI/CD, release, and environment controls rather than as a separate parallel process.

[inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] Build pipelines can own repository-defined checks, but production promotion authority should stay on protected environments, resource-owned approvals, and low-code environment restrictions so that the release gate remains harder to bypass than a code change.

[inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] AI testing belongs inside the ordinary test stack as scenario suites, regression thresholds, and experiment runs placed beside deterministic unit, dependency, and integration tests, because non-deterministic outputs need evidence loops rather than a separate quality discipline.

[inference; source: https://backstage.io/docs/overview/what-is-backstage; https://backstage.io/docs/features/software-templates/; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform] Platform teams should encode the governed path as templates, catalogs, modules, policy bundles, and deployment defaults so that teams start from a compliant scaffold instead of bolting governance on after delivery.

### Key Findings

1. [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/] **High:** AI and low-code delivery should extend the existing SDLC rather than run a separate one, and when higher-risk changes need specialized assurance that lane should remain inside the shared delivery system because the SSDF is designed to integrate into each lifecycle implementation and DORA still ties software outcomes to testing, stability, and platform-engineering fundamentals.
2. [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops] **High:** The strongest pipeline split is repository-owned build logic plus resource-owned promotion authority, because protected environments, custom deployment gates, and approvals or checks outside YAML keep production release control independent from the change being proposed.
3. [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] **High:** AI-specific quality assurance should be inserted into the normal test stack, or into a higher-risk assurance lane that still uses the same release system, as evaluation suites and regression thresholds while low-code artifacts still undergo deterministic validation for dependencies, environment variables, and connector wiring.
4. [inference; source: https://developer.hashicorp.com/terraform/docs; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent; https://openpolicyagent.org/docs/integration] **High:** IaC should cover AI platform resources, deployments, identities, environment defaults, and policy distribution wherever possible, because official Microsoft, Amazon, Terraform, and OPA sources all expose these surfaces as managed and reviewable configuration objects.
5. [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations; https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview] **Medium:** Low-code governance is materially weaker when direct publication stays easier than governed promotion, because Copilot Studio supports in-product publishing and Microsoft separately documents environment controls that can force production changes back through approved ALM paths.
6. [inference; source: https://backstage.io/docs/overview/what-is-backstage; https://backstage.io/docs/features/software-templates/; https://backstage.io/plugins/] **Medium:** IDPs should be the main platform-engineering vehicle for AI and low-code governance because templates, catalogs, docs, and plugins let teams inherit compliant repository structure, ownership metadata, and evidence hooks before development starts.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html; https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] **Medium:** Release management should promote code, prompt or model configuration, low-code packages, policy bundles, and environment metadata as one dependency-aware release set because each of those objects can materially change runtime behavior or rollback feasibility.
8. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://dora.dev/research/2024/dora-report/] **Medium:** The main organizational cost of fragmentation is not only duplicated process but weaker control authority, poorer evidence coherence, and lower change stability, because adjacent governance work and DORA both point to system design, not isolated checks, as the determinant of durable delivery quality.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AI and low-code delivery should extend the existing SDLC, with any higher-risk assurance lane kept inside the shared delivery system. | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final); [DORA 2024](https://dora.dev/research/2024/dora-report/) | high | SSDF is lifecycle-integrated; DORA says AI does not remove the need for testing and stable delivery fundamentals. |
| [inference] Production promotion authority should sit on protected environments or resource-owned checks, not only in repository pipeline code. | [GitHub environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments); [GitHub custom deployment protection rules](https://docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules); [Azure DevOps approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) | high | Each platform exposes non-repository-controlled approval or gating surfaces. |
| [inference] AI quality assurance belongs beside conventional tests, or in a higher-risk assurance lane that still uses the same release system, as evaluation suites and regression thresholds. | [DeepEval docs](https://docs.confident-ai.com/); [Ragas docs](https://docs.ragas.io/en/latest/); [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) | high | DeepEval and Ragas describe evaluation loops; Power Platform still performs deterministic deployment validation. |
| [inference] IaC should cover AI platform resources, deployments, identities, defaults, and policy distribution wherever the platform exposes them as managed objects. | [Terraform docs](https://developer.hashicorp.com/terraform/docs); [Microsoft Foundry Terraform](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform); [Terraform Bedrock agent resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent); [OPA integration](https://openpolicyagent.org/docs/integration) | high | Evidence spans generic IaC, Microsoft Foundry, Amazon Bedrock, and centralized policy management. |
| [inference] Low-code governance is materially weaker when direct publication stays easier than governed promotion. | [Copilot Studio publish](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels); [Block unmanaged customizations](https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations); [Managed Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) | medium | The evidence is strong for Microsoft tooling, but cross-vendor generalization remains a synthesis step. |
| [inference] IDPs should act as the main platform-engineering vehicle for AI and low-code governance defaults. | [Backstage overview](https://backstage.io/docs/overview/what-is-backstage); [Backstage software templates](https://backstage.io/docs/features/software-templates/); [Backstage plugins](https://backstage.io/plugins/) | medium | Official sources show the template, catalog, docs, and plugin mechanics; governance-specific implementation is a synthesis step. |
| [inference] Release management should promote code, prompt or model configuration, low-code packages, policy bundles, and environment metadata as one dependency-aware release set. | [Lifecycle management item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html); [Prompt Flow deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy); [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) | medium | Runtime behavior depends on more than source code, but the exact release-object recommendation remains a synthesis over adjacent evidence. |
| [inference] Fragmentation weakens control authority, evidence coherence, and change stability rather than merely adding administrative overhead. | [Enforcement architecture item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html); [Deployment pipeline item](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html); [Control-plane architecture item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html); [DORA 2024](https://dora.dev/research/2024/dora-report/) | medium | The conclusion is a cross-source synthesis over several governance surfaces rather than one direct quote. |

### Assumptions

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] This item does not rely on a separate unresolved assumption beyond the interpretive steps already marked as inference.

### Analysis

[inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops] The strongest evidence supported reusing the existing engineering operating model because secure-development guidance and delivery platforms already separate mutable build logic from protected promotion authority.

[inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://dora.dev/research/2024/dora-report/; https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] A plausible competing model is a shared SDLC baseline plus a specialized assurance lane for higher-risk AI or low-code changes, and the evidence supports that variation only when the additional lane remains an overlay inside the same delivery and release system rather than becoming a separate end-to-end process.

[inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] AI evaluation tooling was treated as an extension to testing rather than as a replacement because both reviewed frameworks emphasize iterative experiments, metrics, and repeated runs instead of definitive one-shot judgments.

[inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels; https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations] Low-code evidence was weighted heavily because the reviewed Microsoft documentation shows both sides of the governance problem directly, namely the native bypass path and the native administrative control that blocks it.

[inference; source: https://backstage.io/docs/overview/what-is-backstage; https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://openpolicyagent.org/docs/integration] The platform-engineering synthesis favored templates, modules, and policy distribution over checklist governance because those are the mechanisms that can scale across teams without depending on perfect manual compliance.

### Risks, Gaps, and Uncertainties

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] The reviewed AI evaluation sources clearly support CI integration, but they do not by themselves define sector-wide accepted pass thresholds for every enterprise use case.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy] Microsoft is retiring Prompt Flow, so any release design built around that exact artifact needs migration planning and should not be treated as a durable long-term control surface.
- [inference; source: https://backstage.io/plugins/] Backstage's plugin ecosystem proves extensibility, but the evidence reviewed here does not show one standardized off-the-shelf plugin that already solves enterprise AI governance end to end.

### Open Questions

- [inference; source: https://docs.confident-ai.com/; https://docs.ragas.io/en/latest/] Which evaluation-threshold patterns are reliable enough for regulated production promotion of customer-facing AI systems across repeated model upgrades?
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/create-resource-terraform; https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrockagent_agent] Which portions of AI platform governance remain stubbornly outside declarative IaC and therefore require compensating runtime controls or post-deploy verification?
- [inference; source: https://backstage.io/docs/features/software-templates/; https://learn.microsoft.com/en-us/power-platform/alm/pipelines] How should an enterprise connect low-code pipeline metadata, AI evaluation results, and repository catalogs into one evidence object that auditors and release managers can read without tool hopping?

---

## Output

- Type: knowledge
- Description: A research synthesis describing how AI and low-code governance should be integrated into existing software delivery and platform-engineering practice through shared pipelines, protected promotion gates, IaC, expanded testing, and IDP paved roads.
- Links:
  - https://csrc.nist.gov/pubs/sp/800/218/final
  - https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
  - https://learn.microsoft.com/en-us/power-platform/alm/pipelines

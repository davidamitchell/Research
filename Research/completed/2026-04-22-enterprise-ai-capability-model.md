---
review_count: 2
title: "Enterprise AI capability model for use-case maturity decisions"
added: 2026-04-22T08:05:55+00:00
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai, enterprise, capability-model, maturity-framework, software-delivery]
started: 2026-04-22T08:05:55+00:00
completed: 2026-04-22T08:05:55+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Enterprise AI capability model for use-case maturity decisions

## Research Question

What enterprise-wide Artificial Intelligence (AI) capability model best supports deciding whether a candidate AI use case requires net-new foundational capabilities or can reuse capabilities already built across the enterprise?

## Scope

**In scope:**
- Synthesize capability models and maturity frameworks relevant to enterprise AI adoption and scale
- Compare software-delivery-focused evidence (for example, Development and Operations (DevOps) research) with broader enterprise and investment ecosystem perspectives
- Derive a reusable capability map for use-case triage: foundational capability needed vs reusable capability available
- Define practical decision criteria, observable signals, and governance checkpoints for use-case assessment

**Out of scope:**
- Building or selecting a specific vendor platform
- Detailed implementation playbooks for one company or one business unit
- Financial business case modelling at project level

**Constraints:** (time, source types, access)
- Prioritise high-signal, current sources (2024-2026 where available)
- Start from reports listed in the issue and add complementary maturity frameworks
- Use public sources only

## Context

[fact; source: this item's Research Question and Scope] This item asks for an enterprise AI capability model that helps leaders decide whether a candidate use case can reuse shared enterprise capabilities or first requires new foundational investment.
[inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html] The useful output is therefore a dependency model that ties use-case ambition to governance, data, platform, evaluation, and operating-model readiness, while treating a five-level maturity model as a separate portfolio overlay rather than the primary intake tool.

## Approach

1. Extract and normalise capability dimensions from DevOps Research and Assessment (DORA), GitClear, and other software-engineering-focused reports.
2. Extract enterprise-scale capability dimensions from ecosystem reports (Stanford AI Index, State of AI, McKinsey, and similar).
3. Add benchmark maturity frameworks (for example, National Institute of Standards and Technology (NIST) AI Risk Management Framework and International Organization for Standardization (ISO)/International Electrotechnical Commission (IEC) 42001) to cover governance and risk capability baselines.
4. Build a consolidated capability taxonomy grouped into foundational, enabling, and differentiating capabilities.
5. Define a use-case triage rubric mapping each use case to required capabilities, readiness indicators, and build-vs-reuse guidance.
6. Validate the model against representative use-case archetypes and identify likely failure modes when foundational capabilities are missing.

## Sources

Starting points - papers, articles, videos, repos, docs.
**Every source must include a Uniform Resource Locator (URL).** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [x] [DevOps Research and Assessment (DORA) Research Program](https://dora.dev/research/) - primary source for the 2024 and 2025 DORA reports and associated AI capability guidance
- [x] [Google Cloud DORA overview](https://cloud.google.com/devops) - contextual landing page for DORA report publication and capability framing
- [x] [GitClear AI code quality research](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) - telemetry-based counterpoint on code churn and cloning
- [x] [State of AI Report](https://www.stateof.ai/) - annual ecosystem synthesis across research, market, and policy signals
- [x] [Stanford Human-Centered Artificial Intelligence (HAI) AI Index](https://hai.stanford.edu/ai-index) - data-heavy annual benchmark across investment, policy, education, and model progress
- [x] [a16z Big Ideas in Tech](https://a16z.com/big-ideas-in-tech/) - listed URL returned a 404 page in this environment, so it was checked for context but not used for core evidence
- [x] [McKinsey State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) - enterprise survey evidence on adoption and scaling bottlenecks
- [x] [McKinsey Superagency in the Workplace](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential) - listed page failed to fetch directly in this environment; supporting claims use the associated [McKinsey Portable Document Format (PDF) file](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/superagency%20in%20the%20workplace%20empowering%20people%20to%20unlock%20ais%20full%20potential%20at%20work/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-v4.pdf) when noted
- [x] [GitHub Octoverse](https://octoverse.github.com/) - software ecosystem and developer workflow trend context
- [x] [GitHub Research and impact posts](https://github.blog/news-insights/research/) - publicly shared findings on Copilot productivity and developer outcomes
- [x] [Faros AI Productivity Paradox](https://faros.ai/blog/the-ai-productivity-paradox) - listed URL resolved to a page-missing page in this environment; supporting claims use [Faros follow-on analysis](https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes) and the linked [Faros report PDF](https://cdn.prod.website-files.com/66f2fa250759eeb1f2b1199a/68d6e93f3060b3c8a32e72bf_AI_Engineering_Impact_Report_July_2025_Faros_AI.pdf)
- [x] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - governance and risk capability baseline for enterprise maturity
- [x] [ISO/IEC 42001 standard overview](https://www.iso.org/standard/81230.html) - AI management system standard relevant to organisational capability design
- [x] [Microsoft agentic AI adoption maturity model overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview) - concrete five-level maturity model used here as the comparison point for why maturity models are useful overlays but weaker primary intake tools

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: this item's Research Question] The research question is: what enterprise-wide AI capability model best supports deciding whether a candidate AI use case requires net-new foundational capabilities or can reuse capabilities already built across the enterprise?
- [fact; source: this item's Scope and Constraints] In scope are enterprise AI capability models, maturity frameworks, software-delivery evidence, governance frameworks, practical decision criteria, and use-case assessment signals; out of scope are vendor selection, detailed single-company implementation playbooks, and project-level financial modelling.
- [fact; source: this item's Constraints] The investigation is constrained to public sources, with preference for 2024-2026 material and for primary sources over commentary.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-volume-vs-correctness-ai-era.md] Prior completed work already established three adjacent findings that matter here: durable enterprise capability maps separate taxonomy from assessment overlays; enterprise Large Language Model (LLM) systems are economically strongest as layered stacks rather than standalone bespoke models; and AI output acceleration does not create organisational value when downstream verification and workflow controls are weak.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.nist.gov/itl/ai-risk-management-framework] The most decision-useful output format is therefore a dependency map: a stable capability taxonomy plus a triage rubric that decides reuse versus net-new investment at use-case intake.

### §1 Question Decomposition

- **Branch A - software-delivery evidence**
  - A1. What capabilities do DORA, GitHub, GitClear, and Faros imply are prerequisites for organisation-level AI value?
  - A2. Which failure modes appear when AI accelerates local work but shared delivery controls stay weak?
- **Branch B - enterprise adoption evidence**
  - B1. What do AI Index, State of AI, McKinsey, and Octoverse show about adoption, investment, and scaling pressure?
  - B2. What do those sources imply about which capabilities are scarce versus commoditising?
- **Branch C - governance baselines**
  - C1. Which reusable organisational capabilities are explicitly required by the National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF)?
  - C2. Which reusable organisational capabilities are explicitly required by International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC) 42001?
- **Branch D - capability model synthesis**
  - D1. Which capabilities should be treated as foundational, enabling, and differentiating?
  - D2. Which parts of the model should be stable enterprise rails and which should remain use-case overlays?
- **Branch E - decision rubric**
  - E1. What observable signals indicate "reuse shared capability"?
  - E2. What signals indicate "build foundational capability first"?
  - E3. What signals indicate "add a new enabling or differentiating capability on top of shared foundations"?
- **Branch F - validation**
  - F1. Does the model classify representative use-case archetypes plausibly?
  - F2. What failure modes appear when organisations skip foundational capability building?

### §2 Investigation

#### Source audit and accessibility notes

- [fact; source: https://a16z.com/big-ideas-in-tech/] The listed a16z Big Ideas in Tech URL returned a 404 page in this environment, so it was checked for context only and is not used for downstream factual support.
- [fact; source: https://faros.ai/blog/the-ai-productivity-paradox; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://cdn.prod.website-files.com/66f2fa250759eeb1f2b1199a/68d6e93f3060b3c8a32e72bf_AI_Engineering_Impact_Report_July_2025_Faros_AI.pdf] The listed Faros URL resolved to a page-missing page in this environment; supporting Faros claims come from a later Faros post that references the report and from the linked report PDF.
- [fact; source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential; https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/superagency%20in%20the%20workplace%20empowering%20people%20to%20unlock%20ais%20full%20potential%20at%20work/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-v4.pdf] The listed McKinsey Superagency page failed direct fetches in this environment; the associated McKinsey PDF was discoverable publicly and is used only where noted.
- [fact; source: https://octoverse.github.com/; https://github.blog/news-insights/research/] GitHub Octoverse and the GitHub research landing page were accessible and used as contextual software-ecosystem signals, but the strongest measurable GitHub evidence comes from individual research posts rather than the landing pages themselves.

#### A. What software-delivery evidence says about prerequisite capability

- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] The 2025 DORA report draws on nearly 5,000 technology professionals and more than 100 hours of qualitative research, and its central claim is that AI does not fix a team, it amplifies what is already there.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA reports that 90% of survey respondents use AI at work, more than 80% believe it increased productivity, and 30% report little or no trust in AI-generated code.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA also reports that AI adoption now correlates positively with throughput and product performance but still negatively with software-delivery stability, which the authors tie to weak automated testing, weak version-control practice, and slow feedback loops downstream.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA says user-centricity is a prerequisite for AI success, and that 90% of organisations have adopted at least one platform, with high-quality internal platforms directly correlated with an organisation's ability to unlock AI value.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] DORA's published capability guidance is explicit: socialize AI policies, connect AI to internal context, prioritize foundational practices, fortify safety nets, invest in the internal platform, and focus on end users.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] In GitHub's controlled experiment, developers using GitHub Copilot completed the task 55% faster than developers without Copilot, with a 78% completion rate versus 70% for the non-Copilot group.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] GitHub's survey research also found that 73% of users said Copilot helped them stay in flow and 87% said it preserved mental effort during repetitive tasks.
- [fact; source: https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] GitClear analysed approximately 153 million changed lines of code from 2020 to 2023 and reported that churn code was projected to double in 2024 relative to its 2021 pre-AI baseline, alongside declining code reuse and increasing copy-paste patterns.
- [fact; source: https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://cdn.prod.website-files.com/66f2fa250759eeb1f2b1199a/68d6e93f3060b3c8a32e72bf_AI_Engineering_Impact_Report_July_2025_Faros_AI.pdf] Faros reports that developers using AI completed 98% more code changes and 21% more tasks, but those gains disappeared at company level because review queues, brittle test suites, and slow release pipelines remained the bottleneck.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] Software-delivery evidence converges on four shared prerequisites for enterprise AI reuse: clear policy, trusted internal context, strong delivery platform and workflow controls, and evaluation or safety nets that can absorb faster output without collapsing quality.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] The most common error is to treat faster local generation as if it were a reusable enterprise capability, when the reusable capability is actually the sociotechnical system that makes higher output safe, reviewable, and measurable.

#### B. What enterprise-scale evidence says about adoption pressure and scarce capability

- [fact; source: https://hai.stanford.edu/ai-index/2025-ai-index-report; https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf] The 2025 AI Index reports that U.S. private AI investment reached $109.1 billion in 2024, global corporate AI investment reached $252.3 billion, generative AI private investment reached $33.9 billion, and organisational AI use rose to 78% from 55% the previous year.
- [fact; source: https://hai.stanford.edu/ai-index/2025-ai-index-report; https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf] The same report says AI-related incidents are rising sharply, standardised responsible-AI evaluations remain rare among major model developers, and a gap persists between recognising AI risks and taking meaningful action.
- [fact; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf] AI Index 2025 also reports that U.S. federal agencies introduced 59 AI-related regulations in 2024, more than double the prior year.
- [fact; source: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] McKinsey's 2025 State of AI page states that reported AI use continues to tick upward, that use of AI agents is concentrated in Information Technology (IT) and knowledge-management functions, and that for most organisations AI use remains in pilot phases.
- [fact; source: https://www.stateof.ai/] The State of AI Report 2025 positions itself as an annual synthesis across research, industry, politics, safety, and practitioner survey signals, which makes it useful as ecosystem context but weaker than DORA, NIST, ISO, or AI Index for direct capability-model design.
- [fact; source: https://octoverse.github.com/] Octoverse 2025 frames AI, agents, and typed languages as a major shift in software development, with the headline that a new developer joins GitHub every second as AI leads TypeScript to number one.
- [inference; source: https://hai.stanford.edu/ai-index/2025-ai-index-report; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai; https://octoverse.github.com/] The adoption pressure is no longer the scarce factor; the scarce factor is the enterprise operating system that turns widespread model access into safe, repeatable, organisation-level outcomes.

#### C. What governance baselines say reusable enterprise capability must include

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST describes the AI RMF as a voluntary framework intended to improve the ability to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems.
- [fact; source: https://doi.org/10.6028/NIST.AI.100-1] AI RMF 1.0 defines four core functions: Govern, Map, Measure, and Manage.
- [fact; source: https://doi.org/10.6028/NIST.AI.100-1] AI RMF 1.0 also defines trustworthy AI characteristics that include valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 states that it specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS) within organisations.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 says the standard provides a structured way to manage AI-related risks and opportunities, and explicitly highlights responsible AI, traceability, transparency, reliability, and the use of policies and procedures for sound AI governance.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The governance baseline is therefore a reusable enterprise rail, not a use-case-specific embellishment: intake governance, context mapping, evaluation discipline, and lifecycle management have to exist before a portfolio can safely reuse capabilities across multiple AI use cases.

#### C2. What a concrete maturity-ladder alternative contributes, and where it falls short

- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview] Microsoft's agentic AI adoption maturity model is organized into five capability pillars and five progressive maturity levels, from initial experimentation to efficient enterprise-scale operation.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview] Microsoft states that this model is based on the Capability Maturity Model and is intended to help organisations assess current state, identify gaps, and plan what to do next as they scale AI agents.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md] That makes a five-level maturity model a credible overlay for portfolio assessment, but a weaker primary intake tool for this item's decision problem, because a single organisation can sit at one broad maturity stage while still having very different dependency gaps across individual use cases.

#### D. Consolidated enterprise AI capability model

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md] Prior repository work on technology capability models found that durable enterprise maps separate a stable capability taxonomy from traceability and maturity overlays rather than forcing all concerns into one model.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md; https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html] The strongest enterprise AI answer follows the same pattern: keep the capability taxonomy stable, use a five-level maturity model as a portfolio overlay, and treat use-case triage as a separate assessment overlay that decides whether a use case can ride shared enterprise rails.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] The **foundational** capability layer should contain five shared enterprise capabilities: (1) governance and portfolio intake, (2) authoritative context and data access, (3) platform and workflow safety nets, (4) evaluation and measurement, and (5) workforce adoption and operating-model change.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.nist.gov/itl/ai-risk-management-framework; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] The **enabling** capability layer should contain reusable retrieval and context assembly, access and policy enforcement, orchestration and routing, human approval steps, and experimentation infrastructure for adapters or prompt strategies.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1] The **differentiating** capability layer should contain domain ontologies and explicit domain-knowledge structures, task-specific adapters or fine-tunes, specialised review and checking components, and AI-native workflow redesign in places where the business deliberately wants advantage rather than mere parity.

#### E. Reuse-versus-build triage rubric

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] A candidate use case should be classified as **reuse shared capability** only when all five foundational capabilities are already present and evidenced: a named accountable owner, approved policy and risk class, authoritative data with access controls, delivery safety nets and rollback, measurable evaluation criteria, and an operating team willing to redesign workflow and training around the use case.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] A candidate use case should be classified as **build foundational capability first** when any core dependency is missing, because the likely result is the same pattern shown in software delivery: faster local output, weaker quality control, and no durable organisation-level gain.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] A candidate use case should be classified as **add a new enabling or differentiating capability** only after the foundational layer is already in place and the use case clearly needs one of three extras: internalised domain heuristics that retrieval alone does not handle well, specialised orchestration or routing, or higher-assurance verification than the shared baseline provides.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The minimum governance checkpoints are: intake and risk classification before build, authoritative-source and access review before pilot, evaluation exit criteria before scale, and post-launch drift and incident review during operation.

#### F. Validation against representative archetypes

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] An internal knowledge assistant for policies, procedures, or research should usually be a **reuse shared capability** case if enterprise retrieval, access controls, authoritative-source curation, and answer evaluation already exist; if those do not exist, the missing investment is foundational context and governance, not a new model.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] An engineering copilot or partially autonomous code-change agent is a **build foundational capability first** case when automated testing, version control discipline, review workflows, and rollback are weak, because software-delivery evidence says AI amplifies those weaknesses directly.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] A regulated decision-support use case, such as legal review, medical summarisation, or policy compliance support, is typically an **add new enabling or differentiating capability** case on top of shared foundations because it often needs domain-specific benchmarks, tighter approval workflows, and specialised critic or verifier layers.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://hai.stanford.edu/ai-index/2025-ai-index-report; https://www.iso.org/standard/81230.html] The recurring failure modes when foundational capabilities are missing are pilot sprawl, weak provenance, unmanaged risk, quality regressions, and local enthusiasm without portfolio learning.

### §3 Reasoning

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] I weighted DORA, NIST, ISO, and AI Index most heavily because they are the clearest primary sources on enterprise preconditions, governance requirements, and macro adoption pressure.
- [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] I used GitHub, GitClear, and Faros to reason about software-delivery dynamics because they explain why local productivity signals are not sufficient evidence of reusable enterprise capability.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] I treated prior repository work as structural prior art, not as external proof, because it helps decide model shape but does not replace current-source validation.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://doi.org/10.6028/NIST.AI.100-1] A five-level maturity model such as Microsoft's is useful for asking "how mature are we overall and what should improve next?", but this item's intake decision is different: it needs a dependency map that asks which shared prerequisites must already exist before a specific use case can safely reuse them.

### §4 Consistency Check

- [fact; source: https://hai.stanford.edu/ai-index/2025-ai-index-report; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] There is an apparent tension between very high adoption pressure and the claim that foundational capability is still the real bottleneck, because AI Index reports 78% organisational use while McKinsey says most organisations remain in pilot phases.
- [inference; source: https://hai.stanford.edu/ai-index/2025-ai-index-report; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] The tension resolves once adoption and reuse are separated: access to models has become common, but portfolio-level reuse still depends on governance, platform, and evaluation capability that many firms have not standardised.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] There is a second apparent tension between GitHub's 55% faster task-completion result and Faros's claim that organisational outcomes stay flat.
- [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] That second tension resolves when local assistance is distinguished from system performance: individual speed can improve at the same time that the overall delivery system remains constrained by review, testing, and release bottlenecks.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.iso.org/standard/81230.html] There is no material contradiction between NIST AI RMF and ISO/IEC 42001; one is a risk-management framework and the other is a management-system standard, and both require reusable organisational governance rather than ad hoc project-by-project control.

### §5 Depth and Breadth Expansion

**Technical lens**

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] Technically, the reusable enterprise asset is not one model but a layered stack: authoritative context, orchestration, testing, rollback, and optional specialised model layers.

**Regulatory lens**

- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html; https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf] Regulation raises the cost of getting governance wrong, which makes reusable intake, mapping, measurement, and lifecycle controls more valuable as shared enterprise capabilities.

**Economic lens**

- [inference; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Economically, model access is commoditising faster than enterprise control systems are improving, so the scarce asset is the capability layer around the model rather than the model itself.

**Historical lens**

- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md; https://octoverse.github.com/] The pattern mirrors earlier enterprise architecture history: once a technology becomes widely available, advantage shifts from possession of the tool to the organisation's ability to standardise, govern, and reuse it across multiple contexts.

**Behavioural lens**

- [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] Behaviourally, local user enthusiasm is a weak proxy for reusable enterprise readiness because the people who feel immediate value are often upstream of the bottlenecks that determine whether the portfolio sees value.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The best enterprise AI capability model for reuse-versus-build decisions is a dependency map with three layers: foundational shared capabilities, enabling reusable capabilities, and differentiating use-case-specific capabilities, while a five-level maturity model remains useful as a separate portfolio overlay.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] The decisive lesson from software-delivery evidence is that model access and local productivity are not themselves reusable enterprise capabilities; governance, context, platform safety nets, evaluation, and workflow redesign are.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html; https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf] A candidate use case should trigger foundational investment whenever one of those shared rails is missing, and should trigger a new enabling or differentiating investment only after the foundational layer is already proved.

**Key findings:**

1. [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** The strongest enterprise AI capability model for use-case intake is a dependency map, not a five-level maturity model used on its own, because the core question is whether a specific use case can safely reuse existing shared rails rather than where the enterprise sits on a single five-level journey.
2. [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] **Medium confidence:** DORA's public evidence says AI amplifies existing system quality, which means policy, internal context, platform quality, and safety nets are prerequisites for reuse rather than optional optimisation work.
3. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] **High confidence:** Individual developer productivity gains are not sufficient evidence of organisational readiness, because the combined GitHub, Faros, and GitClear evidence shows that faster generation can coexist with higher churn, larger queues, and flat company-level outcomes.
4. [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** Governance capability should sit in the foundational layer because both NIST AI RMF and ISO/IEC 42001 define organisation-wide intake, mapping, measurement, management, and lifecycle control structures that are reused across multiple AI use cases.
5. [inference; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] **Medium confidence:** External pressure to deploy AI is already high, but the stronger constraint now appears to be operating-model and governance maturity rather than simple access to models or pilot opportunities.
6. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** The foundational layer should contain governance and intake, authoritative context and access, platform and workflow safety nets, evaluation and measurement, and workforce adoption and change management.
7. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Medium confidence:** New enabling or differentiating capability should be added only when the foundations already exist and the use case clearly needs specialised routing, internalised domain heuristics, or higher-assurance verification.
8. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] **High confidence:** The default enterprise failure mode is to scale generation before scaling control, which creates pilot sprawl and local enthusiasm without reusable organisational learning.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The right intake model is a dependency map, while a five-level maturity model is better treated as a portfolio overlay. | https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | Microsoft provides the concrete maturity-model comparison point; DORA, NIST, and ISO explain why use-case dependencies still need their own map. |
| [fact] DORA shows that AI value depends on internal policy, context, platforms, and safety nets. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | medium | The blog states the amplifier thesis and the named capability guidance directly, but this row rests on one source. |
| [inference] Local productivity gains do not by themselves prove organisational readiness. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality | high | GitHub shows local gains; Faros and GitClear show the downstream limit and quality risk. |
| [inference] Governance capability belongs in the foundational layer of this model. | https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | Both frameworks define organisation-wide governance and lifecycle controls; the layer placement is the model's synthesis. |
| [inference] Adoption pressure is high while operating-model and governance maturity remain the stronger constraint. | https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | medium | AI Index gives the macro pressure signal, and McKinsey describes the pilot-heavy operating reality; the constraint judgement is interpretive. |
| [inference] The foundational layer should contain five enterprise capabilities. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | This is the direct synthesis of DORA's capability guidance with NIST and ISO baselines. |
| [inference] New enabling or differentiating capability belongs above, not below, shared foundations. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1 | medium | The repository item supplies the architecture pattern; NIST supplies the control requirement. |
| [inference] Scaling generation before scaling control is the default enterprise failure mode. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality | high | Independent delivery sources align on the same bottleneck story. |

**Assumptions:**

- [assumption; source: https://www.stateof.ai/] The State of AI Report is used as ecosystem context rather than primary capability evidence. **Justification:** it is useful for framing market and policy direction, but it is less direct than DORA, NIST, ISO, AI Index, GitHub, or GitClear for enterprise capability design.
- [assumption; source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential; https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/superagency%20in%20the%20workplace%20empowering%20people%20to%20unlock%20ais%20full%20potential%20at%20work/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-v4.pdf] The McKinsey Superagency source is treated as a secondary reinforcement for workforce and operating-model concerns rather than as a primary pillar of the model. **Justification:** the listed page was not directly fetchable in this environment.

**Analysis:**

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] The dominant trade-off is speed versus control. AI makes generation cheap quickly, but enterprises only get reusable value when policy, review, testing, and rollback scale with it.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The governance baseline is stronger than most maturity models because it is expressed as lifecycle capability, not as aspirational posture. That is why it belongs in the foundational layer.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md] Separating stable taxonomy from use-case assessment is important because enterprise portfolios need one enduring map of shared AI rails, while a five-level maturity model such as Microsoft's is better suited to overall progression scoring than to per-use-case dependency checks.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] The layered view also resolves the common false choice between "reuse everything" and "build something custom": foundations are reused broadly, enabling layers are reused selectively, and differentiating layers are built only where the enterprise wants advantage.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Foundational - governance and intake:** reuse is plausible only when a use case has a named owner, risk class, approved policy, and escalation path; if any of those are missing, the right decision is foundational investment first.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1] **Foundational - authoritative context and access:** reuse is plausible only when trusted sources, permissions, provenance, and refresh rules already exist as shared capability; if they do not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] **Foundational - platform and workflow safety nets:** reuse is plausible only when logging, testing, review, rollback, and fast feedback loops already exist as shared delivery controls; if they do not, the gap is foundational.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Foundational - evaluation and measurement:** reuse is plausible only when benchmark sets, error thresholds, incident metrics, and drift checks already exist as shared capability; if they do not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] **Foundational - workforce adoption and change:** reuse is plausible only when training, workflow redesign, support, and user accountability are already planned as operating capability; if they are not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] **Enabling - reusable retrieval and orchestration:** shared context stacks, routing, policy enforcement, and human approvals should be reused once the foundational layer is already in place.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Differentiating - domain-specific optimisation:** ontologies, adapters, specialised review components, and specialised benchmarks should be added only after foundations are proven and a specific use case clearly needs them.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Gate 1:** If the use case lacks an owner, risk class, or lifecycle control path, classify it as foundational investment first.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] **Gate 2:** If the use case lacks authoritative context, internal data access, platform safety nets, or measurable evaluation, classify it as foundational investment first.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] **Gate 3:** If all foundations exist and the use case mainly needs configuration on shared retrieval, policy, and evaluation rails, classify it as reuse shared capability.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Gate 4:** If all foundations exist but the use case needs specialised routing, internalised domain heuristics, or higher-assurance verification, classify it as add new enabling or differentiating capability.

**Risks, gaps, uncertainties:**

- [fact; source: https://a16z.com/big-ideas-in-tech/] The listed a16z source was inaccessible as a live page in this environment, so venture-style strategy framing is underweighted in the final synthesis.
- [fact; source: https://faros.ai/blog/the-ai-productivity-paradox] The listed Faros source URL was inaccessible as a live page in this environment, so Faros support relies on a follow-on Faros article and linked PDF rather than the original destination.
- [fact; source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential] The listed McKinsey Superagency page was not directly fetchable, so operating-model and training claims from that source are weaker than the DORA, NIST, ISO, AI Index, GitHub, GitClear, and Faros evidence.
- [inference; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] The evidence is very strong on adoption pressure and governance gaps, but it is still weak on the exact cost threshold at which an enterprise should move from shared foundations to expensive differentiating capability such as task-specific adapters or specialised checking components.

**Open questions:**

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] What measurable threshold should tell an enterprise that its shared retrieval, policy, and evaluation rails are mature enough to support a higher-autonomy use case?
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] Which governance controls can stay fully shared across the portfolio, and which must always remain specialised by domain or risk class?
- [inference; source: https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] What is the best enterprise metric for detecting when generation capacity is outrunning verification capacity before quality visibly degrades?

### §7 Recursive Review

- [fact; source: this item] Coverage check: the investigation addressed software-delivery evidence, enterprise adoption evidence, governance frameworks, a consolidated capability taxonomy, a triage rubric, and validation against representative archetypes.
- [fact; source: this item] Claim-labelling check: all factual and inferential statements in Research Skill Output are marked as `[fact]`, `[inference]`, or `[assumption]`.
- [fact; source: this item] Source-access check: inaccessible seed URLs are explicitly recorded in section 2 and Risks, Gaps, and Uncertainties.
- [inference; source: this item] Final judgement: the evidence strongly supports a layered capability model in which reuse decisions are gated by shared foundational rails, not by enthusiasm for a new use case.

---

## Findings

*(Seeded from section 6 synthesis above.)*

### Executive Summary

[inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The best enterprise AI capability model for use-case maturity decisions is a three-layer dependency map in which shared foundational capabilities are assessed before any use case is allowed to claim reuse, while a five-level maturity model remains a separate portfolio overlay.
[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] Software-delivery evidence shows why: model access and local productivity gains are easy to obtain, but organisation-level reuse only works when governance, internal context, platform safety nets, evaluation, and workflow redesign already exist as shared enterprise rails.
[inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview] A five-level maturity model remains useful as a separate portfolio view because it helps leaders assess broad organisational progression from experimentation to enterprise-scale operation, but it does not replace the dependency checks needed at use-case intake.
[inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] A candidate use case should trigger foundational investment whenever one of those rails is missing, because governance and lifecycle control are not project-specific add-ons but reusable enterprise capabilities.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Net-new enabling or differentiating capability is justified only after the foundations are already proved and the use case clearly needs specialised routing, internalised domain heuristics, or higher-assurance verification.

### Key Findings

1. [inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** The most useful enterprise AI capability model for use-case intake is a dependency map that separates foundational shared rails from enabling and differentiating layers, because the decision problem is whether a specific use case can safely ride existing enterprise capability rather than where the enterprise sits on a single five-level maturity model.
2. [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] **Medium confidence:** DORA's 2025 research shows that AI amplifies existing system quality, so clear AI policies, internal context, high-quality internal platforms, user-centric workflow design, and safety nets are prerequisites for reliable reuse across a portfolio of use cases.
3. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] **High confidence:** Individual AI productivity gains cannot be treated as sufficient evidence of enterprise readiness, because faster task completion can coexist with higher churn, larger review queues, and flat company-level outcomes when downstream controls remain weak.
4. [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** Governance capability belongs in the foundational layer because both NIST AI RMF and ISO/IEC 42001 require organisation-wide intake, mapping, measurement, management, and lifecycle controls that are reusable across multiple AI use cases.
5. [inference; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] **Medium confidence:** Enterprise pressure to deploy AI is already intense, but scaling maturity remains uneven, which implies that operating-model and governance capability are now a stronger constraint than simple access to models or pilot opportunities.
6. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **High confidence:** The foundational layer should contain governance and intake, authoritative context and access, platform and workflow safety nets, evaluation and measurement, and workforce adoption and change management, because each of these capabilities is repeatedly required before safe reuse becomes plausible.
7. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Medium confidence:** Net-new enabling or differentiating capability should only be added after the foundations are already in place and the use case clearly needs specialised routing, internalised domain heuristics, domain ontologies, or stronger review and checking layers than the shared baseline provides.
8. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] **High confidence:** The default enterprise failure mode is to scale generation before scaling control, which produces pilot sprawl, weak provenance, quality regressions, and local enthusiasm that never becomes reusable organisational learning.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The right enterprise AI model for intake is a dependency map, while a five-level maturity model is better treated as a portfolio overlay. | https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | Microsoft provides the concrete maturity-model comparison point, while DORA, NIST, and ISO show why dependency checks remain necessary per use case. |
| [fact] DORA says reusable AI value depends on policy, internal context, platforms, user-centricity, and safety nets. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | medium | This is stated directly in DORA's published guidance, but the table row rests on one source. |
| [inference] Local productivity gains do not by themselves prove organisational readiness. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality | high | GitHub shows local gains; Faros and GitClear show system-level bottlenecks and quality drag. |
| [inference] Governance capability belongs in the foundational layer of this model. | https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | Both frameworks define organisation-wide lifecycle control requirements, and the foundational-layer placement is the model synthesis. |
| [inference] Deployment pressure is high while operating-model and governance maturity remain the stronger constraint. | https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | medium | AI Index supplies macro pressure numbers, McKinsey describes pilot-heavy reality, and the constraint ranking is interpretive. |
| [inference] Five foundational capabilities are required before safe reuse becomes plausible. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html | high | This is the main synthesis output of the item. |
| [inference] Enabling and differentiating capabilities should be added only above proven foundations. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1 | medium | The pattern is structurally strong, but enterprise crossover thresholds remain under-specified in public evidence. |
| [inference] Scaling generation before scaling control is the most common enterprise failure mode. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality | high | Three independent software-delivery sources align on the same mechanism. |

### Assumptions

- [assumption; source: https://www.stateof.ai/] **Assumption:** The State of AI Report is useful as ecosystem context but not as direct capability-design evidence. **Justification:** the report is broad and signal-rich, but less direct than DORA, NIST, ISO, AI Index, GitHub, GitClear, and Faros for this decision problem.
- [assumption; source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential; https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/superagency%20in%20the%20workplace%20empowering%20people%20to%20unlock%20ais%20full%20potential%20at%20work/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-v4.pdf] **Assumption:** McKinsey Superagency is a useful secondary reinforcement for workforce and operating-model capability, not a primary pillar of the final model. **Justification:** the listed page was not directly fetchable in this environment.

### Analysis

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] I weighted software-delivery evidence heavily because it shows the exact enterprise failure mode that a reuse-versus-build model needs to prevent: faster local generation arriving before shared control systems are ready.
[inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] I weighted NIST AI RMF and ISO/IEC 42001 heavily because they turn vague maturity language into explicit organisational capabilities that can be reused across use cases and checked at intake.
[inference; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-technology-capability-models.md] I resolved the model-shape question by comparing a concrete five-level maturity model, Microsoft's, with the prior repository conclusion that durable enterprise maps separate stable taxonomy from assessment overlays, because that keeps the AI capability map stable while still allowing portfolio-level progression scoring.
[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] The resulting model is intentionally conservative: if a use case exposes a gap in governance, context, platform safety nets, evaluation, or operating-model readiness, the right answer is foundational investment first rather than custom capability on top of weak ground.

#### Consolidated capability model

- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Foundational - governance and intake:** reuse is plausible only when a use case has a named owner, risk class, approved policy, and escalation path; if any of those are missing, the right decision is foundational investment first.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://doi.org/10.6028/NIST.AI.100-1] **Foundational - authoritative context and access:** reuse is plausible only when trusted sources, permissions, provenance, and refresh rules already exist as shared capability; if they do not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes] **Foundational - platform and workflow safety nets:** reuse is plausible only when logging, testing, review, rollback, and fast feedback loops already exist as shared delivery controls; if they do not, the gap is foundational.
- [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Foundational - evaluation and measurement:** reuse is plausible only when benchmark sets, error thresholds, incident metrics, and drift checks already exist as shared capability; if they do not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] **Foundational - workforce adoption and change:** reuse is plausible only when training, workflow redesign, support, and user accountability are already planned as operating capability; if they are not, the gap is foundational.
- [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] **Enabling - reusable retrieval and orchestration:** shared context stacks, routing, policy enforcement, and human approvals should be reused once the foundational layer is already in place.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Differentiating - domain-specific optimisation:** ontologies, adapters, specialised review components, and specialised benchmarks should be added only after foundations are proven and a specific use case clearly needs them.

#### Triage rubric

1. [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] **Gate 1:** If the use case lacks an owner, risk class, or lifecycle control path, classify it as foundational investment first.
2. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] **Gate 2:** If the use case lacks authoritative context, internal data access, platform safety nets, or measurable evaluation, classify it as foundational investment first.
3. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md] **Gate 3:** If all foundations exist and the use case mainly needs configuration on shared retrieval, policy, and evaluation rails, classify it as reuse shared capability.
4. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-19-layered-org-llm-architecture.md; https://doi.org/10.6028/NIST.AI.100-1] **Gate 4:** If all foundations exist but the use case needs specialised routing, internalised domain heuristics, or higher-assurance verification, classify it as add new enabling or differentiating capability.

### Risks, Gaps, and Uncertainties

[fact; source: https://a16z.com/big-ideas-in-tech/] The listed a16z source was inaccessible as a live page in this environment, so venture-style strategy framing is underweighted in the final synthesis.
[fact; source: https://faros.ai/blog/the-ai-productivity-paradox] The listed Faros source URL was inaccessible as a live page, so Faros support relies on a later Faros analysis page and linked PDF rather than the original destination.
[fact; source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential] The listed McKinsey Superagency page did not fetch directly, so workforce and training claims from that seed source carry less weight than the DORA, NIST, ISO, AI Index, GitHub, GitClear, and Faros evidence.
[inference; source: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf; https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai] The evidence is very strong on adoption pressure and governance gaps, but it is still weak on the exact cost threshold at which an enterprise should graduate from shared foundations to expensive differentiating layers such as adapters, ontologies, or specialised checking components.

### Open Questions

[inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] What benchmark should tell an enterprise that its shared retrieval, policy, and evaluation rails are mature enough for higher-autonomy use cases?
[inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://www.iso.org/standard/81230.html] Which governance controls can remain fully shared across the enterprise, and which must always remain specialised by domain or risk class?
[inference; source: https://www.faros.ai/blog/translating-ai-powered-developer-velocity-into-business-outcomes; https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality] What is the best early-warning metric for the point where generation capacity begins to outrun verification capacity in enterprise delivery systems?

---

## Output

- Type: knowledge
- Description: A layered enterprise AI capability model and triage rubric for deciding when a candidate use case can reuse shared enterprise capabilities, when it exposes a missing foundation, and when it justifies a new enabling or differentiating layer.
- Links:
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - https://doi.org/10.6028/NIST.AI.100-1
  - https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf

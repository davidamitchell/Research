---
title: "How should banks govern department-level agent sprawl and bottleneck shifts across divisions?"
added: 2026-05-20T08:35:44+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, governance, organisation, workflow]
started: 2026-05-20T09:27:07+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
  - 2026-04-26-data-governance-ai-lowcode-enterprise-enforcement
  - 2026-04-26-ai-agent-identity-access-management-enterprise
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
related:
  - 2026-04-26-ai-lowcode-sdlc-platform-engineering-integration
  - 2026-04-26-ai-lowcode-failure-modes-governance-mitigation
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How should banks govern department-level agent sprawl and bottleneck shifts across divisions?

## Research Question

How does uncoordinated growth of department-level software agents change systemic risk and reporting integrity in banks, and which governance architecture can maintain consistency across agents, lineage, and operational resilience as bottlenecks shift from data entry to compliance decision queues?

## Scope

**In scope:**
- Cross-division inconsistencies created by local agent deployment in retail, commercial, treasury, operations, and risk functions.
- Governance requirements for agent and model lineage, version control, contradiction detection, and shared evidence.
- Operational bottleneck migration once local automation increases technical throughput but human approval, validation, and incident handling remain constrained.
- Mapping to the Digital Operational Resilience Act (DORA), Federal Reserve model risk guidance, and International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) 42001 management-system controls.

**Out of scope:**
- Vendor-by-vendor product comparisons except where a source is needed to clarify a control pattern.
- Detailed legal advice for a specific jurisdiction or institution.
- Non-financial sectors.

**Constraints:** Emphasise measurable governance mechanisms that can be stress-tested, audited, and operated inside a regulated banking environment.

## Context

- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] As banks let individual divisions deploy software agents, the dominant risk shifts from isolated tool quality toward coordination failures across shared data, policies, third-party services, and reporting chains.
- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.bis.org/bcbs/publ/d516.htm] Faster local automation does not remove control work, because validation, exception handling, monitoring, and incident response still have to happen somewhere, so the practical bottleneck moves into review and compliance queues unless those queues are governed as critical services.

## Approach

1. Characterise organisational failure modes created by distributed agent adoption and local optimisation.
2. Identify how prudential and resilience frameworks reframe those failures as inventory, validation, interdependency, and queue-governance problems.
3. Evaluate governance frameworks for lineage, control-plane coordination, contradiction management, and operational resilience.
4. Produce an implementation-oriented governance blueprint for regulated banking environments.

## Sources

- [x] [Central Bank of Ireland (2026) Digital Operational Resilience Act (DORA)](https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora) - official regulator summary of DORA control domains.
- [x] [European Banking Authority (2026) Interactive Single Rulebook - DORA](https://eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716) - official chapter structure for DORA.
- [x] [Autorite des Marches Financiers (2026) The European Regulation on Digital operational resilience in the financial sector (DORA)](https://www.amf-france.org/en/news-publications/depth/dora) - official supervisory summary with incident-reporting and testing detail.
- [x] [Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency (2011) Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf) - primary 2011 Federal Reserve and Office of the Comptroller of the Currency model-risk guidance.
- [x] [Federal Deposit Insurance Corporation (2026) Agencies Issue Revised Model Risk Guidance](https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance) - official notice that revised interagency guidance is current and risk-based.
- [x] [International Organization for Standardization and International Electrotechnical Commission (2023) ISO/IEC 42001:2023 - Artificial Intelligence (AI) management systems](https://www.iso.org/standard/81230.html) - official standard overview for governance, traceability, and continual improvement.
- [x] [National Cyber Security Centre (2023) Guidelines for secure Artificial Intelligence (AI) system development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) - official secure-design, deployment, and operation guidance.
- [x] [Bank for International Settlements Financial Stability Institute (2024) Regulating Artificial Intelligence (AI) in the financial sector: recent developments and main challenges](https://www.bis.org/fsi/publ/insights63.htm) - official summary of governance, expertise, model-risk, data-governance, and third-party issues in finance.
- [x] [Basel Committee on Banking Supervision (2021) Principles for Operational Resilience](https://www.bis.org/bcbs/publ/d516.htm) - official resilience framework for governance, interdependencies, incident management, and information and communication technology controls.
- [x] [Bank of England (2022) Artificial Intelligence (AI) and Machine Learning discussion paper](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence) - official discussion paper on how existing financial regulation applies to artificial intelligence.
- [x] [Mitchell (2026) What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior repository synthesis on central policy distribution and enforcement layers.
- [x] [Mitchell (2026) How can enterprise data governance frameworks be consistently enforced within Artificial Intelligence (AI) and visual, minimal-code application environments?](https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html) - prior repository synthesis on runtime data controls and lineage.
- [x] [Mitchell (2026) What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior repository synthesis on machine identity and delegation.
- [x] [Mitchell (2026) What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) - prior repository synthesis on traceability and evidence collection.

## Related

- [How should Artificial Intelligence (AI) and low-code governance integrate with existing software development and platform engineering practices?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html)
- [What are the primary failure modes in enterprise Artificial Intelligence (AI) and low-code deployments, and how can governance systems be designed to mitigate them?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html)

---

## Research Skill Output

### §0 Initialise

- Question: how should banks keep department-level software agents from fragmenting governance, breaking reporting integrity, and merely relocating bottlenecks into compliance and resilience queues?
- Mode: full.
- Scope: cross-division agent governance, lineage, contradiction management, review-queue migration, and banking resilience controls.
- Constraints: auditable controls, banking relevance, measurable governance mechanisms, and direct mapping to prudential or resilience sources.
- Output format: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Prior completed items already establish reusable control surfaces for policy distribution, runtime data governance, machine identity, and observability, so this item concentrates on how a bank should compose those surfaces into one resilient operating model.

### §1 Question Decomposition

- Root question: what governance model keeps a growing bank agent estate coherent when local productivity improvements outpace central review capacity?
- A. Risk reclassification
  - A1. What kinds of systemic risk increase when divisions deploy agents independently?
  - A2. How does reporting-integrity risk arise from inconsistent local agent behaviour?
- B. Bottleneck migration
  - B1. Which human control tasks remain after routine data-entry work is automated?
  - B2. Why do those residual tasks become the new bottlenecks?
- C. Regulatory control requirements
  - C1. What does DORA require around resilience, incidents, testing, and third-party risk?
  - C2. What does Federal Reserve model risk guidance require around validation, inventory, and effective challenge?
  - C3. What do ISO/IEC 42001 and National Cyber Security Centre guidance require around lifecycle governance?
- D. Architecture
  - D1. Which central services have to be shared across divisions?
  - D2. Which controls should stay local to the business domain?
- E. Lineage and contradiction management
  - E1. What metadata must every consequential agent carry?
  - E2. What evidence is needed to detect inconsistent decisions across agents?
- F. Resilience operations
  - F1. How should banks govern approval and exception queues once they become critical dependencies?
  - F2. Which tests demonstrate resilience when agent throughput rises?

### §2 Investigation

- [assumption; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716; https://www.amf-france.org/en/news-publications/depth/dora] DORA control mapping in this item uses official regulator summaries and the European Banking Authority chapter index as the accessible operational reference set. Justification: those official sources expose the control families needed for governance design even though this item does not quote article text line by line.

#### A. Department-level agent growth changes the class of banking risk

- [fact; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] The 2011 Federal Reserve and Office of the Comptroller of the Currency guidance says banks use models across underwriting, valuation, risk measurement, client-asset safeguarding, capital, and many other activities, and it frames model risk as the possibility of adverse consequences from incorrect or misused model outputs.
- [fact; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence] Banking authorities describe artificial-intelligence adoption as amplifying familiar governance, model-risk, data, consumer-protection, and third-party-dependency problems rather than replacing the existing control problem with a wholly different one.
- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] Once divisions deploy many local software agents, the main enterprise risk is no longer any single model or workflow but the interaction of many locally optimised systems with shared policies, data products, third-party services, and reporting obligations.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.amf-france.org/en/news-publications/depth/dora; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Reporting-integrity risk rises when divisions can produce or act on inconsistent states faster than central controls can reconcile them, because resilience frameworks treat interdependencies and shared control services as systemic amplifiers.

#### B. Automation shifts the bottleneck into human control work

- [fact; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] Secure artificial-intelligence operation still requires monitoring, documentation, update management, validation, outcomes analysis, and governance over model use after deployment.
- [fact; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] The 2011 Federal Reserve and Office of the Comptroller of the Currency guidance says effective model risk management depends on effective challenge, ongoing monitoring, outcomes analysis, board and senior-management oversight, policies and procedures, and an inventory of models in use.
- [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm] If agents remove manual data-entry steps but the retained control tasks remain human validation, exception review, incident triage, and policy approval, the operational bottleneck reappears in those decision queues rather than disappearing altogether.
- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] The more a bank automates front-end work, the more important expertise, escalation capacity, and queue governance become, because prudential sources repeatedly shift attention toward governance, skills, model oversight, and resilience under disruption.

#### C. Banking governance frameworks converge on lifecycle control, not local autonomy

- [fact; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716; https://www.amf-france.org/en/news-publications/depth/dora] DORA groups required controls into information and communication technology risk management, incident management and reporting, digital operational resilience testing, management of information and communication technology third-party risk, and information sharing.
- [fact; source: https://www.amf-france.org/en/news-publications/depth/dora] The Autorite des Marches Financiers summary says DORA requires a governance and internal-control framework, business continuity and recovery procedures, post-incident review, and structured initial, interim, and final reporting for major incidents.
- [fact; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] Federal Reserve model risk guidance and the 2026 revised interagency notice both require governance over model development and use, validation and monitoring, governance and controls, vendor products, and tailoring to the institution's size, complexity, and model-risk profile.
- [fact; source: https://www.iso.org/standard/81230.html; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development] ISO/IEC 42001 defines an artificial-intelligence management system around policies, objectives, processes, traceability, transparency, and continual improvement, while National Cyber Security Centre guidance spans secure design, development, deployment, and operation.
- [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.iso.org/standard/81230.html; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development] These frameworks all assume one accountable governance system that preserves inventory, testing, monitoring, and review evidence across the lifecycle, which is incompatible with unmanaged department-by-department agent sprawl.

#### D. The architecture must centralise control services while leaving execution federated

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Prior repository work already separates four essential control surfaces: central policy distribution, machine identity, runtime data governance, and shared observability.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora] The best banking fit is a federated hub-and-spoke model, with one central governance core for policy, inventory, lineage, and evidence, and multiple domain teams that run agents locally inside centrally bounded rules.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] Every consequential agent should therefore have a registry record containing owner, business purpose, machine identity, approved data domains, model or workflow version, validation status, risk tier, and emergency disable path.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://www.amf-france.org/en/news-publications/depth/dora] Contradiction management requires a shared reconciliation layer and shared evidence model, because local logs by themselves cannot show when two divisions used different policies, stale thresholds, or inconsistent customer or exposure states.

#### E. Queue governance becomes part of operational resilience

- [fact; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.amf-france.org/en/news-publications/depth/dora] Operational resilience guidance emphasises governance, business continuity, interdependency mapping, incident management, and third-party dependency management rather than only front-end uptime.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.amf-france.org/en/news-publications/depth/dora; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development] Once approval, exception, and incident queues become the main control chokepoints, banks should treat them as critical services with explicit service levels, staffing triggers, escalation paths, and fallback modes.
- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] Review intensity should be risk-tiered: low-impact agents can rely on automated policy checks plus sampling, while material agents need independent validation, effective challenge, and tighter release governance.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.amf-france.org/en/news-publications/depth/dora; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Resilience testing for an agent estate should include contradiction drills, review-backlog surges, third-party outages, stale-policy rollback, and evidence-reconstruction exercises, because those scenarios expose the real dependencies that local throughput metrics hide.

### §3 Reasoning

- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/fsi/publ/insights63.htm] The reviewed evidence does not support treating department-level agents as a wholly new prudential category; it supports treating them as a faster, more distributed execution layer for existing model, governance, data, and third-party risks.
- [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm] The bottleneck-shift claim is inferential rather than directly benchmarked, because the public sources clearly specify the retained human control tasks but do not publish queue telemetry across banks.
- [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.iso.org/standard/81230.html] The architecture recommendation therefore focuses on making control services explicit, measurable, and resilient instead of assuming local agent productivity automatically improves enterprise resilience.

### §4 Consistency Check

- [fact; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.iso.org/standard/81230.html; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.bis.org/bcbs/publ/d516.htm] All major source families in this item require lifecycle governance, monitoring, testing, and accountability, and none treats unmanaged local deployment as a sufficient control model.
- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] The 2011 guidance and the 2026 revised interagency notice are consistent rather than contradictory for this question, because the older document supplies the detailed mechanics of challenge, inventory, and validation while the newer notice confirms proportional, risk-based application.
- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] The weakest claim remains the magnitude of queue migration, so all statements about bottleneck relocation stay inferential and never claim a universal numeric effect.

### §5 Depth and Breadth Expansion

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Technical lens: cross-agent consistency depends on shared identity, shared data attributes, versioned policy artifacts, and shared traceability fields rather than on prose governance documents alone.
- [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.iso.org/standard/81230.html] Regulatory lens: supervisors need evidence objects that can be inspected without reconstructing every domain's local tooling path, which pushes design toward central registries and standardized evidence.
- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] Economic lens: local agent deployment looks cheap when measured against local labour savings, but the shared costs accumulate in validation, reconciliation, incident management, and specialist-review capacity.
- [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.bis.org/fsi/publ/insights63.htm] Behavioural lens: staff are more likely to over-trust fast local agents when ownership, override duty, and escalation duty are ambiguous, so explicit accountability design matters as much as technical policy.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.amf-france.org/en/news-publications/depth/dora] Historical lens: resilience frameworks already treat interdependencies and third parties as systemic amplifiers, so banks should govern agent sprawl as another dependency-multiplying layer rather than as a standalone productivity tool.

### §6 Synthesis

**Executive summary**

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora] Banks should govern department-level agent sprawl with a federated hub-and-spoke model that keeps inventory, policy, lineage, and resilience evidence centralized while leaving execution distributed inside domain-specific rails.
- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] Uncoordinated local agent growth raises systemic risk mainly by multiplying cross-division inconsistencies, shared-data dependencies, third-party concentration, and unreconciled overrides rather than by creating an entirely new risk category.
- [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm] As automation removes manual data-entry work, the operational bottleneck shifts into validation, exception handling, incident triage, and compliance decision queues, so those queues need explicit resilience, staffing, and fallback controls.
- [inference; source: https://www.iso.org/standard/81230.html; https://www.amf-france.org/en/news-publications/depth/dora; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] The required control stack is central inventory plus machine identity, versioned policy distribution, runtime data and action controls, shared telemetry, contradiction detection, and risk-tiered review intensity.

**Key findings**

1. [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] **High confidence:** Uncoordinated department-level agent growth shifts bank risk from single-model error toward cross-division coordination failure, because banking and resilience sources all emphasise firmwide governance of shared models, dependencies, and reporting controls rather than isolated local tooling.
2. [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm] **Medium confidence:** Automation does not remove human control work inside banks; it relocates the bottleneck into validation, exception handling, incident triage, and compliance decision queues that become new choke points when agent throughput rises.
3. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] **High confidence:** The governance architecture that best matches banking obligations is a federated hub-and-spoke control plane with central inventory, policy, lineage, and evidence services plus domain-owned agents that execute inside centrally bounded rails.
4. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf] **High confidence:** Every consequential agent needs an auditable registry entry containing ownership, business purpose, machine identity, approved data domains, model or workflow version, validation status, and emergency disable path if lineage is to remain reviewable.
5. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.amf-france.org/en/news-publications/depth/dora] **High confidence:** Consistency across agents cannot be maintained by local logs alone, because banks need shared telemetry and reconciliation events that can expose contradictory outputs, stale policies, and unresolved overrides across divisions and third-party services.
6. [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.amf-france.org/en/news-publications/depth/dora] **High confidence:** Operational resilience for an agent estate should test queue surges, third-party outages, stale-policy rollback, and contradiction drills in addition to ordinary model tests, because those dependent control services become part of the critical path.
7. [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance; https://www.iso.org/standard/81230.html] **High confidence:** Risk-tiered review intensity is necessary in practice, with automated checks and sampling for low-impact agents and independent validation plus effective challenge for material agents, because bank model governance is expected to be proportional to size, complexity, and risk profile.

**Evidence map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Department-level agent growth turns bank risk into a coordination problem across shared dependencies and reporting controls. | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.bis.org/fsi/publ/insights63.htm<br>https://www.bis.org/bcbs/publ/d516.htm | high | Banking and resilience sources converge on firmwide governance and dependency risk. |
| [inference] The main bottleneck moves into validation, exception, incident, and compliance queues after data-entry work is automated. | https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.bis.org/bcbs/publ/d516.htm | medium | The retained control tasks are explicit, but public queue-magnitude data are limited. |
| [inference] A federated hub-and-spoke control plane is the best banking governance fit. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | high | Central control services plus distributed execution align with both prior architecture work and banking obligations. |
| [inference] Every consequential agent needs registry, identity, lineage, validation, and shutdown metadata. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html<br>https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | high | The combined evidence supports auditable ownership, entitlements, and lifecycle records. |
| [inference] Shared telemetry and reconciliation are required to detect stale policy, contradiction, and unresolved override states across divisions. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html<br>https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://www.amf-france.org/en/news-publications/depth/dora | high | DORA reporting and prior observability work both point to central evidence collection. |
| [inference] Queue surges, third-party outages, stale-policy rollback, and contradiction drills belong inside resilience testing. | https://www.bis.org/bcbs/publ/d516.htm<br>https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora<br>https://www.amf-france.org/en/news-publications/depth/dora | high | Resilience sources emphasise interdependencies, incident handling, and structured testing. |
| [inference] Review intensity should vary by risk tier, with stronger challenge for material agents. | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance<br>https://www.iso.org/standard/81230.html | high | Proportionality and lifecycle governance are explicit in the cited sources. |

**Assumptions**

- [assumption; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] This item treats consequential software agents as falling within the spirit of bank model-risk governance even when a specific institution may classify some of them as workflow or decision-support systems rather than as formal models. Justification: the supervisory concern is adverse decisions from incorrect or misused outputs, which remains relevant to these systems.
- [assumption; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.amf-france.org/en/news-publications/depth/dora] This item uses DORA as a strong benchmark for bank operational resilience even where a given bank or division is not directly supervised under European Union law. Justification: the mapped control families are useful as design tests for resilience and auditability.
- [assumption; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.bis.org/bcbs/publ/d516.htm] Banks will continue to retain human approval for material exceptions, incidents, and policy changes. Justification: the reviewed resilience and security sources assume ongoing human responsibility for the most consequential decisions.

**Analysis**

- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] The evidence was weighted toward prudential regulators and standards bodies because the research question asks for auditable governance architecture, not for comparative vendor capability marketing.
- [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance] The 2011 guidance and the 2026 revised guidance were read together, because the older document supplies the operational mechanics of inventory, effective challenge, and validation while the newer notice confirms that those mechanics still need to be applied proportionately.
- [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.iso.org/standard/81230.html; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development] DORA, ISO/IEC 42001, and National Cyber Security Centre guidance were treated as complementary control families rather than competing regimes: DORA concentrates on resilience operations, ISO on management-system discipline, and National Cyber Security Centre guidance on secure lifecycle practice.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/fsi/publ/insights63.htm; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The architecture recommendation therefore prioritises central control services and explicit queue governance over per-division optimisation, because the systemic failure mode emerges from dependencies and unreconciled states, not from a lack of local automation.

**Risks, gaps, uncertainties**

- [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm] The public banking evidence base is strong on governance obligations and weak on published queue telemetry, so the bottleneck-shift claim is well-motivated but still inferential rather than directly quantified.
- [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716; https://www.amf-france.org/en/news-publications/depth/dora] The DORA mapping in this item relies on official regulator summaries and chapter structure rather than direct article-by-article parsing, so narrower legal nuances could adjust implementation detail without changing the overall control architecture.
- [inference; source: https://www.iso.org/standard/81230.html] The accessible ISO/IEC 42001 evidence is an official standard summary rather than the full clause text, so this item uses the standard for management-system direction and not for clause-by-clause certification interpretation.

**Open questions**

- Which bank metrics are most decision-useful for queue governance: backlog age, decision latency, exception recirculation rate, or override aging?
- How should banks distinguish agents that deserve full model-risk treatment from workflow agents that can stay under lighter controls without creating blind spots?
- Which contradiction patterns should trigger automatic rollback, and which should route into supervised human reconciliation?

### §7 Recursive Review

review_result: pass
acronym_audit: passed
claim_audit: all visible claims in Research Skill Output are labeled as fact, inference, or assumption
prior_work_check: repeated and incorporated for control plane, identity, data governance, and observability surfaces
main_remaining_uncertainty: queue-migration magnitude remains inferential rather than directly benchmarked

---

## Findings

### Executive Summary

Banks should govern department-level agent sprawl with a federated hub-and-spoke model, meaning one central governance core controls inventory, policy, lineage, and resilience evidence while domain teams run agents locally inside those shared rails. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora]
Uncoordinated local agent growth raises systemic risk mainly by multiplying cross-division inconsistencies, shared-data dependencies, third-party concentration, and unreconciled overrides rather than by creating a wholly new prudential risk class. [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
As automation removes manual data-entry work, the main operational bottlenecks move into validation, exception handling, incident triage, and compliance decision queues, so those queues need explicit resilience, staffing, and fallback controls. [inference; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm]
The strongest evidence supports central inventory, machine identity, versioned policy distribution, runtime data and action controls, shared telemetry, contradiction detection, and risk-tiered review intensity; the precise size of queue migration remains less directly measured in public banking sources and is therefore a medium-confidence inference. [inference; source: https://www.iso.org/standard/81230.html; https://www.amf-france.org/en/news-publications/depth/dora; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://www.bis.org/fsi/publ/insights63.htm]

### Key Findings

1. **Uncoordinated department-level agent growth shifts bank risk from single-model error toward cross-division coordination failure, because banking and resilience sources all emphasise firmwide governance of shared models, dependencies, and reporting controls rather than isolated local tooling.** ([inference]; high confidence; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm)
2. **Automation does not remove human control work inside banks; it relocates the bottleneck into validation, exception handling, incident triage, and compliance decision queues that become new choke points when agent throughput rises.** ([inference]; medium confidence; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bis.org/bcbs/publ/d516.htm)
3. **The governance architecture that best matches banking obligations is a federated hub-and-spoke control plane with central inventory, policy, lineage, and evidence services plus domain-owned agents that execute inside centrally bounded rails.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf)
4. **Every consequential agent needs an auditable registry entry containing ownership, business purpose, machine identity, approved data domains, model or workflow version, validation status, and emergency disable path if lineage is to remain reviewable.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf)
5. **Consistency across agents cannot be maintained by local logs alone, because banks need shared telemetry and reconciliation events that can expose contradictory outputs, stale policies, and unresolved overrides across divisions and third-party services.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.amf-france.org/en/news-publications/depth/dora)
6. **Operational resilience for an agent estate should test queue surges, third-party outages, stale-policy rollback, and contradiction drills in addition to ordinary model tests, because those dependent control services become part of the critical path.** ([inference]; high confidence; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.amf-france.org/en/news-publications/depth/dora)
7. **Risk-tiered review intensity is necessary in practice, with automated checks and sampling for low-impact agents and independent validation plus effective challenge for material agents, because bank model governance is expected to be proportional to size, complexity, and risk profile.** ([inference]; high confidence; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance; https://www.iso.org/standard/81230.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Department-level agent growth turns bank risk into a coordination problem across shared dependencies and reporting controls. | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.bis.org/fsi/publ/insights63.htm<br>https://www.bis.org/bcbs/publ/d516.htm | high | Banking and resilience sources converge on firmwide governance and dependency risk. |
| [inference] The main bottleneck moves into validation, exception, incident, and compliance queues after data-entry work is automated. | https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.bis.org/bcbs/publ/d516.htm | medium | The retained control tasks are explicit, but public queue-magnitude data are limited. |
| [inference] A federated hub-and-spoke control plane is the best banking governance fit. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | high | Central control services plus distributed execution align with both prior architecture work and banking obligations. |
| [inference] Every consequential agent needs registry, identity, lineage, validation, and shutdown metadata. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html<br>https://davidamitchell.github.io/Research/research/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.html<br>https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | high | The combined evidence supports auditable ownership, entitlements, and lifecycle records. |
| [inference] Shared telemetry and reconciliation are required to detect stale policy, contradiction, and unresolved override states across divisions. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html<br>https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://www.amf-france.org/en/news-publications/depth/dora | high | DORA reporting and prior observability work both point to central evidence collection. |
| [inference] Queue surges, third-party outages, stale-policy rollback, and contradiction drills belong inside resilience testing. | https://www.bis.org/bcbs/publ/d516.htm<br>https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora<br>https://www.amf-france.org/en/news-publications/depth/dora | high | Resilience sources emphasise interdependencies, incident handling, and structured testing. |
| [inference] Review intensity should vary by risk tier, with stronger challenge for material agents. | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf<br>https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance<br>https://www.iso.org/standard/81230.html | high | Proportionality and lifecycle governance are explicit in the cited sources. |

### Assumptions

- **Assumption:** Consequential software agents should be governed with bank model-risk discipline even when a local tool owner would classify them as workflow systems rather than as formal models. **Justification:** the supervisory concern is adverse decisions from incorrect or misused outputs, which remains relevant here. [assumption; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance]
- **Assumption:** DORA is used here as a strong banking-resilience benchmark even where a specific bank or division is not directly supervised under European Union law. **Justification:** the mapped control families are still useful as design tests for resilience and auditability. [assumption; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.amf-france.org/en/news-publications/depth/dora]
- **Assumption:** Banks will continue to retain human approval for material exceptions, incidents, and policy changes. **Justification:** the reviewed resilience and security sources assume ongoing human responsibility for the most consequential decisions. [assumption; source: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development; https://www.bis.org/bcbs/publ/d516.htm]

### Analysis

The evidence was weighted toward prudential regulators and standards bodies because the research question asks for auditable governance architecture, not for comparative vendor capability marketing. [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance]
The 2011 guidance and the 2026 revised guidance were read together, because the older document supplies the operational mechanics of inventory, effective challenge, and validation while the newer notice confirms that those mechanics still need to be applied proportionately. [inference; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance]
DORA, ISO/IEC 42001, and National Cyber Security Centre guidance were treated as complementary control families rather than competing regimes: DORA concentrates on resilience operations, ISO/IEC 42001 on management-system discipline, and National Cyber Security Centre guidance on secure lifecycle practice. [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://www.iso.org/standard/81230.html; https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development]
The architecture recommendation therefore prioritises central control services and explicit queue governance over per-division optimisation, because the systemic failure mode emerges from dependencies and unreconciled states, not from a lack of local automation. [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/fsi/publ/insights63.htm; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

### Risks, Gaps, and Uncertainties

- Public banking sources define the retained human control tasks clearly, but they do not publish enough queue telemetry to turn bottleneck migration into a quantified universal rule. [inference; source: https://www.bis.org/fsi/publ/insights63.htm; https://www.bis.org/bcbs/publ/d516.htm]
- The DORA mapping in this item relies on official regulator summaries and chapter structure rather than direct article-by-article parsing, so narrower legal nuances could adjust implementation detail without changing the overall control architecture. [inference; source: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora; https://eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716; https://www.amf-france.org/en/news-publications/depth/dora]
- The accessible ISO/IEC 42001 evidence is an official standard summary rather than the full clause text, so this item uses the standard for management-system direction and not for clause-by-clause certification interpretation. [inference; source: https://www.iso.org/standard/81230.html]

### Open Questions

- Which bank metrics are most decision-useful for queue governance: backlog age, decision latency, exception recirculation rate, or override aging?
- How should banks distinguish agents that deserve full model-risk treatment from workflow agents that can stay under lighter controls without creating blind spots?
- Which contradiction patterns should trigger automatic rollback, and which should route into supervised human reconciliation?

### Output

- Type: knowledge
- Description: A banking governance blueprint for department-level agent estates that centralises inventory, policy, lineage, and resilience evidence while treating review and compliance queues as first-class operational dependencies. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://www.bis.org/bcbs/publ/d516.htm; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
- Links:
  - https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
  - https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora
  - https://www.bis.org/bcbs/publ/d516.htm

---
review_count: 1
title: "What capability and control design is needed to mitigate incentive misalignment, shadow Artificial Intelligence (AI), rail bypass, and skill decay at enterprise scale?"
added: 2026-05-02T06:00:57+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, ai-governance, shadow-it, incentives, governance-behaviour, human-factors, skill-decay, enterprise, regulated-enterprise, culture]
started: 2026-05-02T10:16:41+00:00
completed: ~
output: [knowledge]
cites: [2026-04-26-ai-governance-culture-incentives-behaviour, 2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal, 2026-04-26-ai-lowcode-failure-modes-governance-mitigation, 2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-22-enterprise-ai-capability-model, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp]
related: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis, 2026-04-24-business-led-low-code-agent-governance, 2026-04-26-ai-lowcode-governance-maturity-model]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What capability and control design is needed to mitigate incentive misalignment, shadow Artificial Intelligence (AI), rail bypass, and skill decay at enterprise scale?

## Research Question

What capability and control design is needed, at enterprise scale, to mitigate incentive misalignment (where individuals are rewarded for bypassing governance), shadow Artificial Intelligence (AI) (AI tooling adopted outside sanctioned channels), rail bypass (deliberate circumvention of agent guardrails), and human skill decay (loss of practitioner capability through over-reliance on AI automation), and how should each failure mode be detected, deterred, and remediated within an enterprise AI governance framework?

## Scope

**In scope:**
- Definition and taxonomy of each of the four failure modes: incentive misalignment, shadow AI, rail bypass, and skill decay, including their interactions and compounding effects
- Empirical evidence or theoretical frameworks on each failure mode in enterprise AI or analogous technology deployments (cloud, robotic process automation (RPA), low-code)
- Detection mechanisms: telemetry, anomaly detection, shadow-AI discovery tooling, and competency audit methods
- Deterrence mechanisms: governance design, policy architecture, compensation structures, cultural interventions, and technical controls
- Remediation mechanisms: re-skilling programmes, sanctions, incident response, and rail strengthening
- How each mechanism maps to an existing or extended enterprise AI capability model domain

**Out of scope:**
- Model alignment in the machine learning (ML) safety sense, such as reinforcement learning from human feedback (RLHF) misalignment or reward hacking in training
- Consumer-tier AI products not deployed in regulated enterprise contexts
- Full Human Resources (HR) policy design or legal compliance frameworks per jurisdiction

**Constraints:**
- Ground all capability recommendations in observable enterprise patterns and flag inferences clearly
- Expand all acronyms on first use
- Prioritise primary sources, with secondary analysis acceptable where primary evidence is unavailable
- Prior research in the corpus provides foundational context, and this item must extend rather than duplicate it

## Context

Prior completed repository work already shows that governance circumvention is often driven by organisational incentives, weak sanctioned delivery paths, and human review designs that fail under scale. [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

The remaining gap is a single control design that treats incentive misalignment, shadow AI, rail bypass, and skill decay as interacting enterprise failure modes rather than as isolated policy or security problems. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html]

## Approach

1. **Failure mode taxonomy**: Define each of the four failure modes precisely, identify their causal conditions, and document how they interact.
2. **Empirical survey**: Search for documented enterprise cases of shadow Information Technology (IT), rail bypass analogues, and skill atrophy driven by automation dependence, then map findings to AI deployment contexts.
3. **Detection capabilities**: Identify what telemetry, tooling, and audit mechanisms can surface each failure mode, and assess what is commercially available versus requiring custom build.
4. **Control design**: For each failure mode, identify governance design choices, including policy, technical control, and cultural intervention, that deter or contain it, and assess evidence quality for each.
5. **Capability model mapping**: Map the resulting controls to an extended enterprise AI capability model, identifying new domains or sub-domains required.
6. **Scale considerations**: Assess how control effectiveness changes as AI deployment scales, and whether controls that work at small scale break down under volume.

## Sources

- [x] [Mitchell (2026) How do organisational incentives, culture, and behaviour influence adherence to governance in AI and low-code environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html)
- [x] [Mitchell (2026) Implicit rate-limiting controls and agentic AI risk](https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html)
- [x] [Mitchell (2026) AI low-code failure modes and governance mitigation](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html)
- [x] [Mitchell (2026) When and how should human intervention be incorporated into AI-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
- [x] [Mitchell (2026) Enterprise AI capability model for use-case maturity decisions](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html)
- [x] [Mitchell (2026) How should human-in-the-loop design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
- [x] [IBM (2025) Is rising AI adoption creating shadow AI risks?](https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks)
- [x] [IBM and Ponemon Institute (2025) Cost of a Data Breach Report, The AI oversight gap](https://www.ibm.com/reports/data-breach)
- [x] [Cyberhaven (2024) Shadow AI: How employees are leading the charge in AI adoption and putting company data at risk](https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk)
- [x] [SN Computer Science (2025) Shadow AI: Cyber Security Implications, Opportunities and Challenges in the Unseen Frontier](https://link.springer.com/article/10.1007/s42979-025-03962-x)
- [x] [Siponen and Vance (2010) Neutralization: New Insights into the Problem of Employee Systems Security Policy Violations](https://aisel.aisnet.org/misq/vol34/iss3/7/)
- [x] [National Institute of Standards and Technology (NIST) (2023) AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [x] [Google Cloud DORA (2025) Announcing the 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- [x] [MIT Sloan Management Review and Boston Consulting Group (2025) Agentic AI at Scale: Redefining Management for a Superhuman Workforce](https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/)
- [x] [Microsoft (2025) Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)
- [x] [Microsoft (2025) Configure data loss prevention for Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)
- [x] [Microsoft Security Response Center (2025) How Microsoft defends against indirect prompt injection attacks](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks)
- [x] [Open Worldwide Application Security Project (OWASP) (2025) LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [x] [Unit 42 (2025) Indirect prompt injection poisons AI long-term memory](https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/)
- [x] [Macnamara et al. (2024) Does using artificial intelligence assistance accelerate skill decay and hinder skill development without performers' awareness?](https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8)
- [x] [Crowston and Bolici (2025) Deskilling and upskilling with AI systems](https://publicera.kb.se/ir/article/view/47143)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What enterprise capability and control design keeps sanctioned AI use more attractive than workaround behavior while also containing shadow AI, guardrail bypass, and skill decay?
- Scope: Enterprise and regulated-enterprise governance design for four interacting failure modes, not consumer AI, model-training alignment, or full legal-framework design.
- Constraints: Observable enterprise patterns first, primary sources where available, explicit labels for inference and assumption, and acronym expansion on first use.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Prior completed items already established that organisational incentives shape governance adherence, agentic systems remove implicit human pacing controls, low-code and AI share core governance failure modes, human review requires explicit trigger design, capability maturity determines what can scale safely, and synchronous human review degrades into bottlenecks or rubber-stamping under volume.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/] This item therefore needs to integrate behavioural, platform, runtime, and workforce-capability controls into one operating design rather than treat each failure mode as a separate policy checklist.

### §1 Question Decomposition

- **Root question:** What operating model detects, deters, and remediates incentive misalignment, shadow AI, rail bypass, and skill decay before AI scale turns them into systemic governance failure?
- **A. Failure mode taxonomy**
  - A1. What specifically is incentive misalignment in enterprise AI governance?
  - A2. What specifically is shadow AI, and how does it differ from earlier shadow Information Technology (IT)?
  - A3. What specifically counts as rail bypass in agentic systems?
  - A4. What specifically counts as skill decay in AI-assisted work?
  - A5. How do the four failure modes reinforce one another?
- **B. Evidence of causes and prevalence**
  - B1. What evidence shows employees bypass controls when sanctioned paths are slower or less useful?
  - B2. What evidence shows unsanctioned AI adoption is widespread and data-bearing?
  - B3. What evidence shows guardrail bypass remains technically plausible despite policy rules?
  - B4. What evidence shows AI assistance can erode human skill or hide deterioration?
- **C. Detection**
  - C1. Which telemetry surfaces reveal shadow AI?
  - C2. Which process signals reveal incentive misalignment?
  - C3. Which runtime signals reveal rail bypass or prompt injection?
  - C4. Which workforce signals reveal skill decay?
- **D. Deterrence and containment**
  - D1. Which governance designs reduce the motive to bypass sanctioned channels?
  - D2. Which platform controls constrain exfiltration, unsafe actions, and covert publication?
  - D3. Which review patterns remain meaningful when activity runs at machine speed?
  - D4. Which learning and staffing patterns preserve human capability?
- **E. Remediation and capability mapping**
  - E1. What should incident response look like once each failure mode is detected?
  - E2. Which capability domains must exist in the enterprise model for these controls to hold at scale?

### §2 Investigation

- Prior completed-item sweep:
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The nearest corpus items already connect governance circumvention to incentives, show that agentic systems remove human pacing limits, document shared low-code and AI failure classes, and show that high-volume review collapses without risk-tiered oversight.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] The gap left by prior corpus work is a joined-up control design that maps behavioural failures to detection, deterrence, remediation, and capability ownership.

- **A. Failure mode taxonomy and interaction**
  - [fact; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Incentive misalignment is the condition in which employees are rewarded for local speed, delivery, or convenience while the cost of policy breach is diffuse, delayed, or easy to rationalize, which makes circumvention behavior easier to justify.
  - [fact; source: https://link.springer.com/article/10.1007/s42979-025-03962-x; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk] Shadow AI is the organisational use of AI tools or systems without explicit endorsement, supervision, or management by the enterprise information-security or Information Technology control structure, often through personal or otherwise unmanaged accounts that sit outside normal audit and policy controls.
  - [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks] Rail bypass in agentic systems includes direct or indirect prompt injection, jailbreak-style input manipulation, unsafe tool exposure, or workflow circumvention that causes a Large Language Model (LLM) system to ignore intended boundaries and perform unintended actions or data access.
  - [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Skill decay in AI-assisted work is the erosion of human judgment, problem solving, and verification capability when repeated delegation to AI reduces practice intensity, hides mistakes, or shifts the worker role from performer to passive accepter.
  - [inference; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html] These four modes reinforce each other: delivery pressure pushes workers toward shadow AI, shadow AI removes managed rails, unmanaged rails make bypass easier, and repeated delegation inside both managed and unmanaged systems weakens the human capability needed to notice failure early.

- **B. Evidence on causes and prevalence**
  - [fact; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Security-policy-violation research shows that employees do not breach policy only because sanctions are weak; they also rationalize violations through neutralization, which means governance design must account for self-justifying workarounds, not just formal rules.
  - [fact; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach] IBM reports that 80% of surveyed United States office workers use AI for work, only 22% use employer-provided tools exclusively, 97% of organisations reporting an AI-related incident lacked proper AI access controls, and 63% lacked AI governance policies to manage AI or prevent shadow AI.
  - [fact; source: https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk] Cyberhaven reports that the amount of corporate data workers put into AI tools increased 485% between March 2023 and March 2024, that 73.8% of workplace ChatGPT accounts were non-corporate, and that 27.4% of corporate data sent to AI tools in March 2024 was sensitive.
  - [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/] DevOps Research and Assessment (DORA) and MIT Sloan both argue that AI amplifies existing organisational weaknesses, and MIT Sloan adds that human-era management models break when autonomous systems operate with superhuman speed and scale unless explicit rules, thresholds, tracing, and intervention paths are defined.
  - [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/] OWASP, Microsoft, and Unit 42 all describe prompt injection as a current attack class capable of causing sensitive-data disclosure, unintended actions, or persistent manipulation, including long-term memory poisoning in agentic systems.
  - [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] The reviewed skill-decay literature does not yet provide large enterprise field measurements, but it consistently warns that AI assistance can accelerate expert skill decay, hinder learner development, and shift workers toward prompting and editing rather than direct problem solving.

- **C. Detection capabilities**
  - [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention] Microsoft documents concrete detection and governance surfaces for enterprise agents, including maker audit logs, Microsoft Sentinel integration, data policy enforcement in real time, environment routing, blocked connectors, blocked Hypertext Transfer Protocol (HTTP) requests, blocked event triggers, and restricted publishing channels.
  - [fact; source: https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://www.ibm.com/reports/data-breach] Shadow-AI discovery requires visibility into both sanctioned and personal-account traffic, sensitive-data uploads, and account type, because unmanaged adoption frequently occurs outside approved tenants and is strongly associated with governance gaps.
  - [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Incentive misalignment is best detected indirectly through friction and behavior signals, such as long approval latency, rising exception requests, low sanctioned-platform adoption, queue growth, override rarity, and evidence that teams are using unofficial paths to preserve throughput.
  - [fact; source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] Rail bypass detection needs runtime prompt-attack monitoring, tool-call logging, output validation, segregation of untrusted content, and alerting on attempted exfiltration or use of privileged functions outside approved workflows.
  - [inference; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] Skill decay detection requires competency and review-quality signals rather than security telemetry alone, including periodic unaided task assessment, rotation through non-automated work, verification intensity, override quality, and training completion on failure modes.

- **D. Deterrence and containment controls**
  - [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks] Organisations reduce the incentive to bypass governance when they make the sanctioned path useful, because workers adopt shadow tools when official tools are weaker, slower, or resisted by leadership.
  - [inference; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Deterrence therefore needs both policy and operating-model change: low-friction approved tools, clear permissioned use cases, training on sanctioned alternatives, named accountability for exceptions, and compensation structures that do not reward unofficial acceleration more than governed delivery.
  - [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance] Platform deterrence for shadow AI and rail bypass can be implemented through connector classification, authentication requirements, endpoint filtering, blocked public-website knowledge sources, restricted publication channels, blocked event triggers, and maker-facing security warnings before publication.
  - [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks] Rail-bypass containment requires defense in depth: constrained model roles, validated output formats, input and output filtering, least-privilege tool access, segregation of external content, adversarial testing, user-consent workflows, and deterministic blocking for known exfiltration paths.
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/] At scale, deterrence cannot rely on per-item human approval alone, because machine-speed operations outrun human review capacity, so organisations need exception-based oversight, recurring technical audits, and well-defined stop or rollback paths instead of universal synchronous approval.
  - [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Skill-decay deterrence requires deliberate practice and work design, including unaided exercises, rotation into manual or analytic tasks, evaluation of human reasoning rather than tool output alone, and training that treats prompting, editing, and verification as separate skills rather than proof that core expertise remains intact.

- **E. Remediation and capability mapping**
  - [inference; source: https://www.ibm.com/reports/data-breach; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks] Remediation for shadow AI and rail bypass must look like incident response rather than awareness-only coaching: identify affected accounts and data, disable or quarantine risky connectors and agents, rotate secrets or tokens, inspect logs, notify accountable owners, and update rules or prompts only after the broader control failure is understood.
  - [inference; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Remediation for skill decay must combine retraining with changed task allocation, because training alone does not restore judgment if the operating model continues to remove all opportunities for meaningful human practice.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] The capability model needs five explicit control domains to handle these risks at scale: incentive alignment and governance legitimacy, sanctioned AI platform and access management, runtime safety and rail enforcement, governance observability and incident response, and human capability preservation.
  - [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html] These domains map naturally onto the existing enterprise model by extending governance, platform, and operating-model capabilities rather than creating a wholly separate AI-behaviour programme.

- **F. Assumptions and evidence limits**
  - [assumption; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] The skill-decay findings are transferable from medicine and broader knowledge-work analysis to enterprise AI governance because the shared mechanism is repeated delegation of cognitive work to automation under performance pressure.
  - [assumption; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk] Vendor survey and telemetry evidence on shadow AI is directionally reliable for enterprise control design even though the strongest public prevalence data comes from vendors with product interests in detection and governance.

### §3 Reasoning

- [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] The evidence supports treating incentive misalignment as the upstream condition because workers bypass controls when sanctioned options impose local cost and unofficial options preserve speed, productivity, or convenience.
- [inference; source: https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.ibm.com/reports/data-breach] Shadow AI is not only a policy-compliance issue; it is a discovery and platform-governance problem because use often occurs beyond approved tenants and because unmanaged traffic carries sensitive data.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/] Rail bypass remains a live runtime risk even in governed deployments, so control design must assume prompt-level or tool-level failure and include deterministic containment where possible.
- [inference; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Skill decay cannot be handled as a secondary training issue because degraded human judgment weakens review quality, incident detection, and the organisation's ability to recover when automation fails.

### §4 Consistency Check

- [fact; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk] External evidence is consistent that unsanctioned AI use is widespread, data-bearing, and associated with governance gaps, although the precise prevalence figures vary by survey population and telemetry method.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/] External evidence is also consistent that prompt injection and related guardrail bypass remain active risks, and no reviewed source claims that prompting discipline alone fully eliminates them.
- [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Skill-decay evidence is directionally consistent but less mature than the shadow-AI and prompt-injection evidence base, which is why the item's overall confidence remains medium rather than high.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] No contradiction appeared between the proposed new control domains and the existing capability model, because the new domains operate as governance and operating-model extensions rather than a competing structure.

### §5 Depth and Breadth Expansion

- **Technical lens**
  - [fact; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks] The strongest technical pattern is pre-configured constriction of what an agent can read, call, publish, and trigger, followed by monitoring and deterministic blocking of known exfiltration or unsafe-action paths.
- **Behavioural lens**
  - [fact; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks] Behavioural evidence shows that people do not reliably interpret policy as binding when unofficial tools are easier and when leadership resistance or slow governance makes sanctioned use feel misaligned with performance expectations.
- **Economic lens**
  - [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/reports/data-breach] The economic case favors platform investment over ad hoc review labour because AI amplifies weak systems, while security incidents tied to poor AI governance are materially costly.
- **Operational-scale lens**
  - [fact; source: https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The scale problem is not only larger queue volume; it is the mismatch between machine-speed action and human-speed intervention, which pushes control design toward exception handling, continuous monitoring, and kill-switch readiness.
- **Workforce lens**
  - [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Workforce capability must be governed as a control surface, because organisations that automate judgment without preserving practice eventually lose the human competence needed for validation, escalation, and recovery.

### §6 Synthesis

**Executive summary:**

Enterprise-scale mitigation of incentive misalignment, shadow AI, rail bypass, and skill decay requires a dual design: make the sanctioned path faster and more useful than the workaround, then back it with runtime controls, telemetry, and deliberate skill-preservation routines that do not assume humans can review machine-speed activity line by line. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

The evidence shows that the four failure modes are coupled, because delivery pressure and legitimacy gaps push work into shadow channels, unmanaged channels weaken safety rails, runtime bypass remains technically possible, and repeated over-delegation erodes the human judgment needed to detect or correct failure. [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

The appropriate enterprise response is an operating model with five capability domains: incentive alignment, sanctioned AI platform management, runtime safety enforcement, governance observability and incident response, and human capability preservation. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html]

Confidence is medium because shadow-AI prevalence and prompt-injection risk are well supported by current public evidence, while skill-decay evidence remains more transfer-based and less measured in enterprise field settings. [inference; source: https://www.ibm.com/reports/data-breach; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

**Key findings:**

1. **Enterprise governance fails when local incentives reward speed and convenience more clearly than they reward governed use, because employees can rationalize policy violations when sanctioned tools or approvals slow delivery.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html)
2. **Public survey and telemetry evidence indicate that shadow AI is already a material enterprise control problem, because non-corporate AI account usage and sensitive-data flows outside sanctioned channels are common enough to undermine auditability and policy enforcement.** ([inference]; medium confidence; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://link.springer.com/article/10.1007/s42979-025-03962-x)
3. **Rail bypass remains a live control-design problem, because prompt injection and related attack paths can still induce data exfiltration, unintended actions, or persistent memory poisoning unless tool access, content boundaries, and exfiltration paths are constrained.** ([inference]; medium confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html)
4. **Skill decay is a governance problem, not only a learning-and-development problem, because organisations that repeatedly delegate judgment to AI can lose the human expertise required to verify outputs, challenge unsafe behavior, and recover from automation failure.** ([inference]; medium confidence; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
5. **Detection of these four failure modes requires combined telemetry across governance, platform, runtime, and workforce surfaces, because shadow adoption, prompt attacks, queue distortion, and human deskilling do not appear in one audit stream.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
6. **Governed fast lanes, preconfigured low-risk patterns, and clear exception ownership reduce the incentive to move into unofficial channels because they lower the local cost of sanctioned use without removing enterprise controls.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)
7. **Per-item human review does not scale as the primary control once AI systems operate at machine speed, so mature enterprises need exception-based oversight, recurring technical audits, and tested stop or rollback mechanisms instead of universal synchronous approval.** ([inference]; medium confidence; source: https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
8. **An enterprise AI capability model needs explicit ownership for incentive alignment, sanctioned platform design, runtime rail enforcement, governance observability, and human capability preservation if it is to contain behavioural and control failure at scale.** ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Incentive misalignment drives bypass when sanctioned paths impose local cost and unofficial paths preserve throughput. | https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html | medium | behavioural mechanism |
| [inference] Shadow AI is already a material enterprise control problem because unmanaged account usage and sensitive-data flows are common enough to weaken auditability and policy enforcement. | https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://link.springer.com/article/10.1007/s42979-025-03962-x | medium | survey plus telemetry |
| [inference] Prompt injection and related bypass paths remain a live control-design problem because they can trigger disclosure, unsafe tool use, and persistent manipulation. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html | medium | runtime safety |
| [inference] Skill decay reduces the human capacity needed for verification, escalation, and recovery. | https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | medium | transfer from reviewed domains |
| [inference] Detection must span traffic, agent configuration, runtime prompts, approvals, overrides, and competency signals. | https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | cross-surface telemetry |
| [inference] Governed fast lanes, preconfigured low-risk patterns, and clear exception ownership reduce the incentive to move into unofficial channels by lowering the local cost of sanctioned use. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention | medium | enablement plus controls |
| [inference] Machine-speed systems force oversight toward exception review, audits, and stop mechanisms. | https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | scale effect |
| [inference] Five explicit capability domains are needed to contain behavioural and runtime governance failure. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html | medium | model extension |

**Assumptions:**

- [assumption; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143] Skill-decay evidence from medicine and knowledge-work settings transfers sufficiently to enterprise AI governance because the shared mechanism is repeated delegation of cognitive work to AI under time pressure.
- [assumption; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk] Public vendor data on shadow AI is sufficiently directionally reliable for control design even though it is not an industry-neutral census.

**Analysis:**

This item has direct public measurements for shadow-AI prevalence and direct official guidance for rail-bypass risk, while the skill-decay case relies more on transfer from adjacent domains. [inference; source: https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

The incentive-misalignment case is slightly more inferential, but the neutralization literature, IBM worker survey, DORA findings, and prior corpus work point in the same direction: workers route around governance when official paths are misaligned with delivery pressure. [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]

The skill-decay case is the least directly measured in enterprise field studies, so the recommendation is to treat skill preservation as a prudential control: monitor it now rather than wait for a larger incident dataset after expertise has already degraded. [inference; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]

One plausible rival remedy is to preserve strict per-item review by adding more reviewers, but the reviewed scale evidence suggests this only delays the bottleneck unless the operating model also shifts toward bounded autonomy, exception handling, and stronger platform controls. [inference; source: https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

**Risks, gaps, uncertainties:**

- Enterprise-grade public field data on skill decay remains thinner than the public data on shadow AI and prompt injection. [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]
- Public prevalence data for shadow AI comes mainly from vendors and vendor-sponsored studies, which means exact percentages should be treated as directional rather than universal. [fact; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk]
- The reviewed sources support the need for explicit skill-preservation routines, but they do not yet define a single validated enterprise metric set for measuring capability loss across different job families. [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]

**Open questions:**

- Which workforce metrics best distinguish healthy AI augmentation from hidden deskilling in software, operations, and customer-service roles?
- How should compensation and performance frameworks be redesigned so teams are rewarded for governed throughput rather than unofficial acceleration?
- Which runtime safety controls for agent memory, tools, and publishing channels are most cost-effective across different platform stacks?

**Output:**

- Type: knowledge
- Description: Capability and control design for enterprise AI governance should treat incentive alignment, sanctioned platform design, runtime rail enforcement, observability, and skill preservation as one coupled control system rather than as separate policy topics. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html]
- Links:
  - https://www.ibm.com/reports/data-breach
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8

### §7 Recursive Review

- Claim-label audit: complete
- Findings inline-source audit: complete
- Acronym audit: AI, RPA, ML, RLHF, HR, IT, LLM, HTTP, NIST
- Synthesis and Findings parity: aligned
- Confidence: medium

---

## Findings

### Executive Summary

Enterprise-scale mitigation of incentive misalignment, shadow AI, rail bypass, and skill decay requires a dual design: make the sanctioned path faster and more useful than the workaround, then back it with runtime controls, telemetry, and deliberate skill-preservation routines that do not assume humans can review machine-speed activity line by line. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

The four failure modes are coupled, because delivery pressure and legitimacy gaps push work into shadow channels, unmanaged channels weaken safety rails, runtime bypass remains technically possible, and repeated over-delegation erodes the human judgment needed to detect or correct failure. [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

The appropriate enterprise response is an operating model with five capability domains: incentive alignment, sanctioned AI platform management, runtime safety enforcement, governance observability and incident response, and human capability preservation. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html]

Confidence is medium because shadow-AI prevalence and prompt-injection risk are well supported by current public evidence, while skill-decay evidence remains more transfer-based and less measured in enterprise field settings. [inference; source: https://www.ibm.com/reports/data-breach; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

### Key Findings

1. **Enterprise governance fails when local incentives reward speed and convenience more clearly than they reward governed use, because employees can rationalize policy violations when sanctioned tools or approvals slow delivery.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html)
2. **Public survey and telemetry evidence indicate that shadow AI is already a material enterprise control problem, because non-corporate AI account usage and sensitive-data flows outside sanctioned channels are common enough to undermine auditability and policy enforcement.** ([inference]; medium confidence; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://link.springer.com/article/10.1007/s42979-025-03962-x)
3. **Rail bypass remains a live control-design problem, because prompt injection and related attack paths can still induce data exfiltration, unintended actions, or persistent memory poisoning unless tool access, content boundaries, and exfiltration paths are constrained.** ([inference]; medium confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html)
4. **Skill decay is a governance problem, not only a learning-and-development problem, because organisations that repeatedly delegate judgment to AI can lose the human expertise required to verify outputs, challenge unsafe behavior, and recover from automation failure.** ([inference]; medium confidence; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
5. **Detection of these four failure modes requires combined telemetry across governance, platform, runtime, and workforce surfaces, because shadow adoption, prompt attacks, queue distortion, and human deskilling do not appear in one audit stream.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
6. **Governed fast lanes, preconfigured low-risk patterns, and clear exception ownership reduce the incentive to move into unofficial channels because they lower the local cost of sanctioned use without removing enterprise controls.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)
7. **Per-item human review does not scale as the primary control once AI systems operate at machine speed, so mature enterprises need exception-based oversight, recurring technical audits, and tested stop or rollback mechanisms instead of universal synchronous approval.** ([inference]; medium confidence; source: https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
8. **An enterprise AI capability model needs explicit ownership for incentive alignment, sanctioned platform design, runtime rail enforcement, governance observability, and human capability preservation if it is to contain behavioural and control failure at scale.** ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Incentive misalignment drives bypass when sanctioned paths impose local cost and unofficial paths preserve throughput. | https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html | medium | behavioural mechanism |
| [inference] Shadow AI is already a material enterprise control problem because unmanaged account usage and sensitive-data flows are common enough to weaken auditability and policy enforcement. | https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://link.springer.com/article/10.1007/s42979-025-03962-x | medium | survey plus telemetry |
| [inference] Prompt injection and related bypass paths remain a live control-design problem because they can trigger disclosure, unsafe tool use, and persistent manipulation. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html | medium | runtime safety |
| [inference] Skill decay reduces the human capacity needed for verification, escalation, and recovery. | https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | medium | transfer from reviewed domains |
| [inference] Detection must span traffic, agent configuration, runtime prompts, approvals, overrides, and competency signals. | https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | cross-surface telemetry |
| [inference] Governed fast lanes, preconfigured low-risk patterns, and clear exception ownership reduce the incentive to move into unofficial channels by lowering the local cost of sanctioned use. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention | medium | enablement plus controls |
| [inference] Machine-speed systems force oversight toward exception review, audits, and stop mechanisms. | https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | scale effect |
| [inference] Five explicit capability domains are needed to contain behavioural and runtime governance failure. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html | medium | model extension |

### Assumptions

- Skill-decay evidence from medicine and knowledge-work settings transfers sufficiently to enterprise AI governance because the shared mechanism is repeated delegation of cognitive work to AI under time pressure. [assumption; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]
- Public vendor data on shadow AI is sufficiently directionally reliable for control design even though it is not an industry-neutral census. [assumption; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk]

### Analysis

This item has direct public measurements for shadow-AI prevalence and direct official guidance for rail-bypass risk, while the skill-decay case relies more on transfer from adjacent domains. [inference; source: https://www.ibm.com/reports/data-breach; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8]

The incentive-misalignment case is slightly more inferential, but the neutralization literature, IBM worker survey, DORA findings, and prior corpus work point in the same direction: workers route around governance when official paths are misaligned with delivery pressure. [inference; source: https://aisel.aisnet.org/misq/vol34/iss3/7/; https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]

The skill-decay case is the least directly measured in enterprise field studies, so the recommendation is to treat skill preservation as a prudential control: monitor it now rather than wait for a larger incident dataset after expertise has already degraded. [inference; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]

One plausible rival remedy is to preserve strict per-item review by adding more reviewers, but the reviewed scale evidence suggests this only delays the bottleneck unless the operating model also shifts toward bounded autonomy, exception handling, and stronger platform controls. [inference; source: https://sloanreview.mit.edu/article/agentic-ai-at-scale-redefining-management-for-a-superhuman-workforce/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

### Risks, Gaps, and Uncertainties

- Enterprise-grade public field data on skill decay remains thinner than the public data on shadow AI and prompt injection. [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]
- Public prevalence data for shadow AI comes mainly from vendors and vendor-sponsored studies, which means exact percentages should be treated as directional rather than universal. [fact; source: https://www.ibm.com/think/insights/rising-ai-adoption-creating-shadow-risks; https://www.cyberhaven.com/blog/shadow-ai-how-employees-are-leading-the-charge-in-ai-adoption-and-putting-company-data-at-risk]
- The reviewed sources support the need for explicit skill-preservation routines, but they do not yet define a single validated enterprise metric set for measuring capability loss across different job families. [fact; source: https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8; https://publicera.kb.se/ir/article/view/47143]

### Open Questions

- Which workforce metrics best distinguish healthy AI augmentation from hidden deskilling in software, operations, and customer-service roles?
- How should compensation and performance frameworks be redesigned so teams are rewarded for governed throughput rather than unofficial acceleration?
- Which runtime safety controls for agent memory, tools, and publishing channels are most cost-effective across different platform stacks?

---

## Output

- Type: knowledge
- Description: Capability and control design for enterprise AI governance should treat incentive alignment, sanctioned platform design, runtime rail enforcement, observability, and skill preservation as one coupled control system rather than as separate policy topics. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html]
- Links:
  - https://www.ibm.com/reports/data-breach
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00572-8

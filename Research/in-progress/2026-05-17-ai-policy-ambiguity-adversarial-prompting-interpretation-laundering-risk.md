---
title: "Adversarial prompting risks in policy assistants: coercing restrictive policy into permissive interpretations"
added: 2026-05-17T20:33:05+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, llm, organisation, evaluation]
started: 2026-05-17T21:12:28+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-03-15-prompt-injection-threat-landscape
  - 2026-04-26-access-control-amplification-agentic-operations
  - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
related:
  - 2026-05-09-data-governance-frameworks-llm-nondeterminism-extension
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-05-10-m365-copilot-sensitive-data-security-governance-risks
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Adversarial prompting risks in policy assistants: coercing restrictive policy into permissive interpretations

## Research Question

How vulnerable are corporate compliance Large Language Models (LLMs) to adversarial prompting that reframes restrictive policy as permissive guidance, and which controls detect or contain deliberate manipulation?

## Scope

**In scope:**
- Evaluate prompt patterns that coerce permissive interpretations from restrictive policy language.
- Measure model and workflow susceptibility to prompt-induced policy reversal across representative compliance scenarios.
- Identify detection, containment, and deterrence controls for intentional manipulation attempts.

**Out of scope:**
- Implementing production policy-assistant software.
- Entity-specific legal advice.
- Exhaustive jurisdiction-by-jurisdiction legal analysis.

**Constraints:** Use publicly available sources, distinguish demonstrated evidence from inference, and prioritise sources with explicit governance or empirical grounding.

## Context

[fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] Prior completed repository research established that prompt injection becomes materially more dangerous when a model can use tools, private context, or external content rather than only answer a chat question.

[fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Related repository items also established that permission scope and review quality, not model quality alone, determine enterprise blast radius.

[assumption; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application] In this item, "interpretation laundering" is used as a plain-language shorthand for adversarial prompting that causes an assistant to restate a restrictive policy as if it permits the user's desired action. Justification: the exact phrase is not a formal standard term in the reviewed sources, but the mechanism is consistent with prompt injection and prompt-induced policy reversal described in the cited guidance.

## Approach

1. Evaluate prompt patterns that coerce permissive interpretations from restrictive policy language.
2. Measure model and workflow susceptibility to prompt-induced policy reversal across representative compliance scenarios.
3. Identify detection, containment, and deterrence controls for intentional manipulation attempts.

## Sources

- [x] [Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - threat taxonomy for prompt injection, excessive agency, and overreliance risks
- [x] [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework) - baseline governance and risk-management framing
- [x] [Willison (2023) Prompt Injection Primer](https://simonwillison.net/2023/May/2/prompt-injection-explained/) - practical adversarial prompting patterns and why prompt-only defenses fail
- [x] [Greshake et al. (2023) Not What You've Signed Up For: Compromising Real-World Large Language Model (LLM)-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) - foundational indirect prompt injection paper
- [x] [Mukkamala et al. (2024) Prompt Injection Attacks on Large Language Models and LLM-Integrated Applications: State of the Art, Open Problems and Future Directions](https://arxiv.org/abs/2402.00898) - attack categorization and implications review
- [x] [Autio et al. (2024) Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) - official generative Artificial Intelligence risk categories including human and Artificial Intelligence (AI) configuration and information security
- [x] [Microsoft Learn (2025) Security planning for Large Language Model-based applications](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application) - enterprise threat map and mitigations for prompt injection
- [x] [Microsoft Learn (2025) Defend against indirect prompt injection attacks](https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection) - defense-in-depth pattern for indirect prompt injection
- [x] [Microsoft Learn (2025) Prompt Shields in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields) - direct and document-attack detection controls
- [x] [Microsoft Learn (2025) Protecting against prompt injection attacks in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks) - concrete encoding and trust-boundary mitigation pattern
- [x] [Anthropic (2025) Mitigating the risk of prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses) - production defense progress and remaining residual risk
- [x] [Sharma et al. (2025) Constitutional Classifiers: Defending against universal jailbreaks](https://arxiv.org/abs/2501.18837) - measured safeguard performance and deployment trade-offs
- [x] [Zhan et al. (2025) Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061) - adaptive-attack benchmark against eight defenses
- [x] [Jia et al. (2025) A Critical Evaluation of Defenses against Prompt Injection Attacks](https://arxiv.org/abs/2505.18333) - evaluation methodology critique for prompt-injection defenses
- [x] [Shi et al. (2025) Lessons from Defending Gemini Against Indirect Prompt Injections](https://arxiv.org/abs/2505.14534) - continuous adaptive evaluation of a production model family
- [x] [NIST Center for AI Standards and Innovation (CAISI) (2025) Technical Blog: Strengthening AI Agent Hijacking Evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations) - official agent-hijacking evaluation lessons
- [x] [NIST Center for AI Standards and Innovation (CAISI) (2026) Request for Information on securing Artificial Intelligence agents](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems) - official indication that constraining and monitoring agent access remains an open deployment problem
- [x] [OWASP (2025) LLM06 Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html) - permission, autonomy, and user-approval controls
- [x] [OWASP (2024) LLM09 Overreliance](https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/) - oversight and validation controls for authoritative but wrong outputs
- [x] [Mitchell (2026) Prompt injection threat landscape](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html) - prior repository synthesis on attack classes and defense limits
- [x] [Mitchell (2026) Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) - prior repository synthesis on permission blast radius
- [x] [Mitchell (2026) Scaled human-in-the-loop oversight quality measurement](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html) - prior repository synthesis on review quality degradation
- [x] [Mitchell (2026) Extending traditional data governance frameworks to address Large Language Model non-determinism](https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.html) - prior repository synthesis on deterministic governance layers

## Related

- [Mitchell (2026) Prompt injection threat landscape](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html)
- [Mitchell (2026) Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
- [Mitchell (2026) Scaled human-in-the-loop oversight quality measurement](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: how vulnerable are corporate compliance Large Language Models (LLMs) to adversarial prompting that reframes restrictive policy as permissive guidance, and which controls detect or contain deliberate manipulation?
- Scope: prompt patterns, workflow susceptibility, and controls for policy assistants used in compliance or governance contexts; no jurisdiction-specific legal advice and no production implementation design.
- Constraints: publicly available sources only; direct evidence separated from inference; compliance-specific conclusions must be narrower than the underlying general prompt-injection evidence where domain benchmarks are absent.
- Output: knowledge.
- Constraint mode: full.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.html] Prior completed items already establish that prompt injection is structurally hard to eliminate, that agent permissions amplify blast radius, that oversight quality degrades under volume pressure, and that deterministic governance layers remain necessary around stochastic models.
- [assumption; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application] Working definition: a policy assistant includes any Large Language Model-based system that interprets policy text, retrieved guidance, or procedural rules for a user and may also trigger workflow steps based on that interpretation. Justification: the reviewed sources describe the relevant technical mechanisms, but they do not provide a single standard term for this exact enterprise product slice.

### §1 Question Decomposition

- **Root question:** When a user or external document tries to obtain a more permissive policy answer than the underlying rule supports, what evidence shows that a policy assistant can be manipulated, and what control stack actually reduces the risk?
- **A. Prompt-pattern branch**
  - A1. What attack classes can restate restrictive policy as permissive guidance?
  - A2. Which of those classes require direct user control, and which can arrive through retrieved or third-party content?
  - A3. What concrete software patterns let untrusted content change higher-priority instructions?
- **B. Susceptibility branch**
  - B1. What public evidence shows that tool-using or retrieval-using assistants remain vulnerable despite current defenses?
  - B2. How much do adaptive attacks degrade reported defense performance?
  - B3. What can be said directly about compliance assistants, and what must be inferred from adjacent agent evidence?
- **C. Control branch**
  - C1. Which controls are deterministic, meaning enforced outside the model, and which are probabilistic, meaning they only reduce attack likelihood?
  - C2. Which controls detect manipulation attempts before answer delivery or downstream action?
  - C3. Which controls contain damage if manipulation succeeds?
- **D. Governance branch**
  - D1. How do excessive permissions and overreliance change the harm from a permissive but wrong policy answer?
  - D2. What human-review and monitoring design keeps a policy assistant from becoming an unsupervised compliance authority?

### §2 Investigation

#### A. Attack patterns that can turn restrictive policy into permissive guidance

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP defines prompt injection as unintended model-behavior change caused by crafted inputs and distinguishes direct prompt injection from indirect prompt injection, where malicious instructions arrive through external content such as websites, files, or emails.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP also states that retrieval-augmented generation and fine-tuning do not fully mitigate prompt injection vulnerabilities, which means policy retrieval alone does not remove the risk that a model will privilege malicious framing over the intended policy task.
- [fact; source: https://arxiv.org/abs/2302.12173] Greshake et al. show that Large Language Model-integrated applications blur the boundary between data and instructions, allowing attackers to place malicious instructions in retrieved content that later manipulates model behavior, Application Programming Interface (API) calls, or data handling.
- [fact; source: https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks] Microsoft documents a concrete message-tag injection path in which untrusted variables or function-call returns can insert a new system message unless that content is encoded or explicitly trusted.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks] A policy assistant is therefore vulnerable whenever restrictive policy text, user justification, retrieved examples, and execution instructions share one model context without a deterministic boundary that distinguishes authoritative policy from untrusted argument.
- [inference; source: https://simonwillison.net/2023/May/2/prompt-injection-explained/; https://simonwillison.net/2023/Dec/20/mitigate-prompt-injection/] In a compliance setting, the adversarial prompt does not need to ask for obviously disallowed behavior. It can instead ask the assistant to reinterpret exceptions, weigh business urgency more heavily than the written rule, or produce a more executive-friendly summary that silently removes restrictive clauses.

#### B. Public evidence on susceptibility and defense limits

- [fact; source: https://arxiv.org/abs/2402.00898] Mukkamala et al. describe prompt injection as a continuing cat-and-mouse problem in which users probe restrictions while developers block discovered attacks, and they document both direct and indirect forms as established threat classes.
- [fact; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations] NIST Center for AI Standards and Innovation (CAISI) describes agent hijacking as a form of indirect prompt injection and reports that, for one evaluated model, attack success rose from 11% for the strongest baseline attack to 81% for the strongest newly developed adaptive attack.
- [fact; source: https://arxiv.org/abs/2503.00061] Zhan et al. evaluate eight indirect prompt injection defenses and report that adaptive attacks bypassed all of them with attack success rates above 50%, showing that defenses that look strong under non-adaptive tests can fail after disclosure.
- [fact; source: https://arxiv.org/abs/2505.18333] Jia et al. argue that prompt-injection defenses must be evaluated on both attack resistance and utility retention, and they conclude that several previously reported defense successes do not survive a more principled evaluation methodology.
- [fact; source: https://www.anthropic.com/research/prompt-injection-defenses] Anthropic reports that improved model training, classifiers, and human red teaming reduced prompt-injection risk in browser use, but it explicitly states that no browser agent is immune and that even a 1% attack success rate remains meaningful risk.
- [fact; source: https://arxiv.org/abs/2505.14534] Google DeepMind reports that Gemini tool-use scenarios remain exposed because some tools require access to untrusted data, and it responds with continuous adaptive adversarial evaluation rather than claiming a one-time fix.
- [inference; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534] The current empirical record supports a partial-containment view of prompt injection, not an elimination view: defenses can lower attack frequency and raise attacker cost, but motivated attackers still find policy-bypass paths when adaptive testing is applied.

#### C. Why compliance and policy assistants are a distinct harm surface

- [fact; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application] Microsoft's Large Language Model security planning guidance says prompt injection can modify system-level restrictions, exploit backend systems, and should be mitigated through least privilege, segregation of external content, prompt and output monitoring, adversarial testing, and human approval for high-risk actions.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP states that successful prompt injection can manipulate critical decision-making processes, not only content generation.
- [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html] OWASP Excessive Agency identifies excessive functionality, excessive permissions, and excessive autonomy as root causes that let manipulated model outputs produce damaging downstream actions.
- [fact; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/] OWASP Overreliance warns that authoritative but wrong model outputs create security, legal, and reputational harm when users or systems trust them without verification.
- [fact; source: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] NIST Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile names human and Artificial Intelligence (AI) configuration as a risk category that includes automation bias and overreliance, and names prompt injection under information security risks unique to or exacerbated by generative Artificial Intelligence.
- [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/] Compliance assistants are especially exposed because the harmful output can be a plausible permissioning answer rather than an obviously malicious command. A user who wants approval can use adversarial framing to obtain a permissive summary, and the organisation may then operationalize that answer through workflow tooling or human acceptance.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.html] The danger is therefore two-layered: first, the assistant can misstate the policy; second, enterprise permissions, workflow automation, and overloaded reviewers can let the misstated interpretation propagate into action.

#### D. Controls that detect or contain deliberate manipulation

- [fact; source: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields] Microsoft recommends defense in depth: prompt shields, content isolation, plan-drift detection, critic agents, tool-chain analysis, information-flow control, least privilege, short-lived privileges, and manual verification of risky actions.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields] Microsoft Prompt Shields separately detect user-prompt attacks and document attacks, which matters for policy assistants because both direct user persuasion and poisoned reference material can produce a permissive answer.
- [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html] OWASP recommends minimizing extensions, minimizing extension permissions, executing downstream actions in the user's context, requiring user approval for high-impact actions, and enforcing authorization in downstream systems rather than trusting the model to decide what is allowed.
- [fact; source: https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems] NIST's 2026 request for information specifically asks for deployment interventions that constrain and monitor the extent of agent access, which indicates that access scoping and runtime monitoring remain open security priorities for real deployments.
- [fact; source: https://simonwillison.net/2023/Dec/20/mitigate-prompt-injection/] Simon Willison argues that systems should be designed on the assumption that prompt injection will succeed sometimes, and that security work should therefore focus on limiting blast radius rather than expecting perfect instruction obedience.
- [inference; source: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://simonwillison.net/2023/Dec/20/mitigate-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.html] For policy assistants, the minimum credible control stack is: deterministic policy checks or rule validation outside the model; isolation of retrieved policy text from free-form user persuasion; least-privilege connectors; high-risk action approval; logging of prompts, retrieved sources, and overrides; and periodic review of permissive-answer patterns.

#### E. Explicit limitations and evidence gaps

- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2402.00898; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534] The strongest direct evidence concerns general prompt injection, indirect prompt injection, and tool-using agents, not a public benchmark named specifically for compliance-policy interpretation reversal.
- [inference; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application] The compliance-specific conclusion is still actionable because the reviewed governance sources already treat authoritative but wrong model outputs, prompt-induced control bypass, and overreliance as enterprise control problems even before a separate compliance-only benchmark exists.

### §3 Reasoning

- [fact; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2402.00898; https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061] Direct evidence is strongest for the existence of prompt injection, indirect prompt injection, and adaptive bypass of current defenses in tool-using or retrieval-using systems.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] Direct evidence is also strong that governance risk depends on more than model behavior alone, because authority, permissions, and human over-trust change the consequence of a wrong answer.
- [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] The compliance-specific claim is inferential because the reviewed primary sources describe enterprise copilots, agents, and governance systems in general rather than publishing a dedicated benchmark for policy-interpretation manipulation.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields] The key mechanism is still specific and falsifiable: if untrusted language can enter the same reasoning context as authoritative policy and the model's answer is treated as authoritative, the system can be manipulated into producing a permissive interpretation that the underlying rule does not support.
- [assumption; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://learn.microsoft.com/en-us/security/security-for-ai/protect] This item assumes that at least some corporate policy assistants are connected to enterprise retrieval or workflow surfaces rather than being isolated text generators. Justification: the reviewed enterprise guidance and protection tooling are explicitly written for that connected-assistant deployment pattern.

### §4 Consistency Check

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application] The core mechanism is internally consistent across standards, academic papers, and enterprise platform guidance: mixed trusted and untrusted text can alter model behavior in unintended ways.
- [fact; source: https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333; https://arxiv.org/abs/2505.14534] The sources are also consistent that current defenses can improve robustness but do not justify a claim of solved security.
- [inference; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] There is no contradiction between "human review is necessary" and "human review can fail": the consistent position is that review must be risk-tiered, instrumented, and protected against overreliance, not merely present on paper.
- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2503.00061; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html] The resulting confidence for the top-level conclusion is medium rather than high because the mechanism evidence is strong while the compliance-specific measurement evidence is still indirect.

### §5 Depth and Breadth Expansion

- [fact; source: https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields] Technical lens: the attack surface includes user prompts, retrieved documents, tool responses, and prompt-template assembly logic, so detection or escaping only at the final answer layer is incomplete.
- [fact; source: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems] Regulatory and governance lens: NIST treats prompt injection, overreliance, and human and AI configuration risks, plus agent-access constraints, as governance and security problems spanning deployment and operations, not only model training.
- [inference; source: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-ai-prompt-injection-protection] Economic and operational lens: layered defenses add cost, latency, and false-positive handling, but those trade-offs are smaller than the cost of treating a policy assistant as a low-friction authority that can quietly authorize forbidden actions or unsafe exceptions.
- [inference; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Behavioural lens: the enterprise failure mode is not only hostile prompting but also persuasive prompting that exploits reviewer trust, productivity pressure, or a user's desire for approval, making permissive wording itself a control surface.
- [inference; source: https://simonwillison.net/2023/May/2/prompt-injection-explained/; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.14534] Historical lens: the field has moved from explaining the problem in 2023 to measuring adaptive attack pressure in 2025, but the directional story is continuity of risk rather than imminent closure.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://arxiv.org/abs/2302.12173] Corporate compliance assistants are materially vulnerable to adversarial prompting whenever they mix authoritative policy text with untrusted user or retrieved content and then let the model produce authoritative guidance without deterministic policy checks.
- [fact; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534] Current defenses improve robustness but do not eliminate risk: public evidence shows adaptive attacks still bypass many defenses, while vendors that have made measurable progress still describe prompt injection as unresolved.
- [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Permissive policy reversal can also arise from ordinary policy ambiguity, retrieval error, or non-adversarial model misinterpretation, but adversarial prompting is still a material risk because it intentionally exploits the same weak separation between trusted policy and untrusted argument. The decisive controls are therefore architectural and procedural as much as model-centric: isolate untrusted content, enforce least privilege and downstream authorization, require review for high-impact actions, and measure whether humans are actually challenging permissive answers.

**Key findings:**

- [inference] **Policy assistants become vulnerable to prompt-induced policy reversal when restrictive policy text, user persuasion, and retrieved examples share a single reasoning context without deterministic separation of trusted rules from untrusted argument.** (medium confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks)
- [fact] **The empirical defense record does not support treating current prompt-injection mitigations as complete protection, because adaptive evaluations from NIST Center for AI Standards and Innovation, academic papers, Anthropic, and Google DeepMind all report meaningful residual attack success or the need for continuous retesting.** (high confidence; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534)
- [inference] **For compliance use cases, the same permissive answer can arise from adversarial prompting, ordinary policy ambiguity, retrieval error, or non-adversarial model misinterpretation, but deliberate manipulation remains material because it intentionally steers the assistant toward an apparently authorized exception path.** (medium confidence; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [fact] **Once a policy assistant is connected to workflow tools, the same attack class can escalate from bad advice to unauthorized action, because excessive permissions, excessive autonomy, and insufficient downstream authorization turn manipulated outputs into execution authority.** (high confidence; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
- [fact] **The most credible control pattern is layered rather than singular: user-prompt and document-attack detection, isolation of untrusted content, least-privilege connectors, complete mediation in downstream systems, and approval or override gates for high-impact actions.** (high confidence; source: https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)
- [inference] **Human review remains necessary but is not self-securing, because overreliance, automation bias, and throughput pressure can convert a nominal reviewer into a rubber-stamp layer unless review quality is measured and risky answers are routed for deeper scrutiny.** (medium confidence; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Shared model context lets untrusted argument pressure policy interpretation unless trusted rules are separated outside the model. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks | Medium | Mechanism direct, policy mapping inferential |
| [fact] Adaptive evaluation results show current prompt-injection defenses remain bypassable or incomplete. | https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations ; https://arxiv.org/abs/2503.00061 ; https://www.anthropic.com/research/prompt-injection-defenses ; https://arxiv.org/abs/2505.14534 | High | Multi-source direct evidence |
| [inference] A permissive compliance answer can be harmful before tool use, whether it comes from adversarial prompting or non-adversarial ambiguity, because users may still treat it as authorized guidance. | https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application ; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/ ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | Medium | Harm pathway partly behavioural |
| [fact] Tool-connected assistants amplify the same manipulation into unauthorized action when permissions and autonomy are too broad. | https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html ; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html | High | Direct control-surface evidence |
| [fact] Layered controls, not prompt wording alone, form the strongest current defense pattern. | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields ; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection ; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html | High | Strong practice alignment |
| [inference] Human review must be instrumented and risk-tiered because overreliance can convert review into formal but ineffective control. | https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/ ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence ; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html | Medium | Governance synthesis |

**Assumptions:**

- [assumption; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://learn.microsoft.com/en-us/security/security-for-ai/protect] The corporate policy assistants of interest are connected to enterprise retrieval, collaboration, or workflow surfaces rather than being isolated text generators. This assumption is needed because connected deployment is what turns a permissive answer into an operational risk surface.
- [assumption; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] Users and reviewers may treat a fluent policy explanation as more authoritative than its evidence warrants. This assumption is reasonable because both sources describe overreliance and automation bias as persistent human and AI interaction risks.

**Analysis:**

- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333] The highest-weight evidence in this item comes from papers that directly test indirect prompt injection and defense failure under adaptive attack.
- [inference; source: https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534] Vendor reports were weighted as primary operational evidence when they disclosed concrete evaluation setup, residual risk language, or continuous-testing methods rather than only marketing claims.
- [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/] A permissive answer does not by itself prove adversarial prompting, because hallucination, reasoning error, ambiguous policy text, or retrieval failure can produce the same symptom.
- [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html] The compliance-specific conclusion is a bounded synthesis from three linked facts: prompt injection changes model behavior, permissive but wrong outputs create governance harm, and broad permissions or weak review turn that harm into action.
- [inference; source: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://simonwillison.net/2023/Dec/20/mitigate-prompt-injection/] Rival remedies based only on better prompts or only on detector models were rejected because the stronger sources repeatedly recommend layered containment and blast-radius reduction instead of single-control reliance.

**Risks, gaps, uncertainties:**

- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2402.00898; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333] Public evidence does not yet provide a dedicated benchmark for compliance-policy interpretation manipulation, so the item depends on adjacent agent-hijacking and prompt-injection evidence.
- [inference; source: https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534] Vendor defense reports are useful primary sources, but they are still partly product-context-specific and do not automatically transfer to every enterprise policy-assistant design.
- [inference; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] The behavioural harm path, where a user acts on a permissive answer without any automated tool use, is plausible and well supported conceptually, but it is less directly benchmarked than action-execution hijacking.

**Open questions:**

- Which public benchmark design best measures policy-interpretation manipulation without encouraging disclosure of sensitive compliance edge cases?
- How often do real enterprise reviewers detect policy-reversal answers when productivity pressure is high?
- Which deterministic policy-check patterns are practical for natural-language policy text that contains exceptions and judgment terms?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Artificial Intelligence (AI), Large Language Model (LLM), Application Programming Interface (API), Open Worldwide Application Security Project (OWASP), National Institute of Standards and Technology (NIST), Artificial Intelligence Risk Management Framework (AI RMF), and NIST Center for AI Standards and Innovation (CAISI) expanded on first use
- Domain-term audit: "interpretation laundering" defined in `## Context` as a working term rather than treated as a settled standard label
- Claim audit: all visible claims in `## Research Skill Output` labeled as fact, inference, or assumption
- Synthesis parity check: `§6 Synthesis` is aligned with `## Findings`
- Confidence result: medium, because mechanism evidence is strong and direct, while compliance-specific benchmarking remains indirect

---

## Findings

*(Expanded from §6 Synthesis above without adding new claims.)*

### Executive Summary

Corporate compliance assistants are materially vulnerable to adversarial prompting whenever they mix authoritative policy text with untrusted user or retrieved content and then let the model produce authoritative guidance without deterministic policy checks. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://arxiv.org/abs/2302.12173]

Current defenses improve robustness but do not eliminate risk, because public evidence from official evaluations, academic papers, and vendor disclosures shows meaningful residual attack success and continued dependence on adaptive retesting. [fact; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534]

The core enterprise danger is not only data exfiltration or tool misuse, but also persuasive policy reversal: a model can present a restrictive rule as a reasonable exception path and have that answer accepted as if it were an authorised interpretation. That permissive answer can also come from ordinary ambiguity, retrieval failure, or non-adversarial model error, so adversarial prompting should be treated as a material route to failure rather than the sole explanation for every bad answer. [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence]

The strongest current response is layered containment, meaning prompt-attack detection, untrusted-content isolation, least-privilege workflow design, downstream authorization outside the model, and human review that is instrumented well enough to detect when reviewers stop challenging permissive answers. [inference; source: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

### Key Findings

1. **Policy assistants become vulnerable to prompt-induced policy reversal when restrictive policy text, user persuasion, and retrieved examples share a single reasoning context without deterministic separation of trusted rules from untrusted argument.** ([inference]; medium confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks)
2. **The empirical defense record does not support treating current prompt-injection mitigations as complete protection, because adaptive evaluations from NIST Center for AI Standards and Innovation, academic papers, Anthropic, and Google DeepMind all report meaningful residual attack success or the need for continuous retesting.** ([fact]; high confidence; source: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations; https://arxiv.org/abs/2503.00061; https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534)
3. **For compliance use cases, the same permissive answer can arise from adversarial prompting, ordinary policy ambiguity, retrieval error, or non-adversarial model misinterpretation, but deliberate manipulation remains material because it intentionally steers the assistant toward an apparently authorized exception path.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
4. **Once a policy assistant is connected to workflow tools, the same attack class can escalate from bad advice to unauthorized action, because excessive permissions, excessive autonomy, and insufficient downstream authorization turn manipulated outputs into execution authority.** ([fact]; high confidence; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
5. **The most credible control pattern is layered rather than singular: user-prompt and document-attack detection, isolation of untrusted content, least-privilege connectors, complete mediation in downstream systems, and approval or override gates for high-impact actions.** ([fact]; high confidence; source: https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)
6. **Human review remains necessary but is not self-securing, because overreliance, automation bias, and throughput pressure can convert a nominal reviewer into a rubber-stamp layer unless review quality is measured and risky answers are routed for deeper scrutiny.** ([inference]; medium confidence; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Shared model context lets untrusted argument pressure policy interpretation unless trusted rules are separated outside the model. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-injection-attacks | Medium | Mechanism direct, policy mapping inferential |
| [fact] Adaptive evaluation results show current prompt-injection defenses remain bypassable or incomplete. | https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations ; https://arxiv.org/abs/2503.00061 ; https://www.anthropic.com/research/prompt-injection-defenses ; https://arxiv.org/abs/2505.14534 | High | Multi-source direct evidence |
| [inference] A permissive compliance answer can be harmful before tool use, whether it comes from adversarial prompting or non-adversarial ambiguity, because users may still treat it as authorized guidance. | https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application ; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/ ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | Medium | Harm pathway partly behavioural |
| [fact] Tool-connected assistants amplify the same manipulation into unauthorized action when permissions and autonomy are too broad. | https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html ; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html | High | Direct control-surface evidence |
| [fact] Layered controls, not prompt wording alone, form the strongest current defense pattern. | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields ; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection ; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html | High | Strong practice alignment |
| [inference] Human review must be instrumented and risk-tiered because overreliance can convert review into formal but ineffective control. | https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/ ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence ; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html | Medium | Governance synthesis |

### Assumptions

- [assumption; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://learn.microsoft.com/en-us/security/security-for-ai/protect] The corporate policy assistants of interest are connected to enterprise retrieval, collaboration, or workflow surfaces rather than being isolated text generators, because connected deployment is what turns a permissive answer into a governance and execution risk.
- [assumption; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] Users and reviewers may treat a fluent policy explanation as more authoritative than its evidence warrants, because both sources describe overreliance and automation bias as persistent human and AI interaction risks.

### Analysis

The highest-weight evidence comes from papers and official evaluations that directly test indirect prompt injection and adaptive defense failure rather than from general opinion pieces. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333; https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations]

Vendor reports were treated as primary operational evidence only where they disclosed concrete evaluation setup, residual-risk language, or continuous-testing methods rather than only advertising product capabilities. [inference; source: https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields]

The compliance-specific conclusion is a bounded synthesis from three linked facts: prompt injection changes model behavior, authoritative but wrong answers create governance harm, and broad permissions or weak review let that harm propagate into action. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html]

Alternative remedies that rely only on stronger prompt wording or only on detector models were rejected as sufficient because the stronger sources repeatedly recommend layered containment and blast-radius reduction instead of single-control reliance. [inference; source: https://simonwillison.net/2023/Dec/20/mitigate-prompt-injection/; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection; https://arxiv.org/abs/2503.00061]

Prior repository items sharpen the conclusion by showing that permission scoping, deterministic governance, and measurable review quality are the enterprise control surfaces most likely to fail after a permissive answer is produced. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.html]

A permissive answer does not by itself prove adversarial prompting, because hallucination, reasoning error, ambiguous policy text, or retrieval failure can produce the same symptom. [inference; source: https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llm-application; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/]

### Risks, Gaps, and Uncertainties

Public evidence does not yet provide a dedicated benchmark for compliance-policy interpretation manipulation, so this item depends on adjacent agent-hijacking and prompt-injection evidence rather than a direct public compliance test suite. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2402.00898; https://arxiv.org/abs/2503.00061; https://arxiv.org/abs/2505.18333]

Vendor defense reports are useful primary sources, but they are still product-context-specific and do not automatically transfer to every enterprise policy-assistant design. [inference; source: https://www.anthropic.com/research/prompt-injection-defenses; https://arxiv.org/abs/2505.14534; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields]

The behavioural harm path, where a user acts on a permissive answer without any automated tool use, is conceptually well supported but less directly benchmarked than action-execution hijacking. [inference; source: https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence]

### Open Questions

- Which public benchmark design best measures policy-interpretation manipulation without encouraging disclosure of sensitive compliance edge cases?
- How often do real enterprise reviewers detect policy-reversal answers when productivity pressure is high?
- Which deterministic policy-check patterns are practical for natural-language policy text that contains exceptions and judgment terms?
- Which logging schema best captures prompt, retrieval, policy source, and override data for later forensic review?

---

## Output

- Type: knowledge
- Description: Evidence-backed synthesis of how prompt injection, overreliance, and excessive agency combine to let policy assistants restate restrictive policy as permissive guidance, plus the control stack most likely to detect or contain that failure mode. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/; https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html; https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection]
- Links:
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://arxiv.org/abs/2302.12173
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

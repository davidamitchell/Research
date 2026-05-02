---
review_count: 2
title: "What security capabilities are required in an enterprise Artificial Intelligence (AI) system to address prompt injection, Retrieval-Augmented Generation (RAG)-based attacks, model supply chain compromise, and data exfiltration beyond basic Application Programming Interface (API) access controls and audit logging?"
added: 2026-05-02T06:00:57+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [security, prompt-injection, rag, agentic-ai, llm, ai-governance, enterprise, access-control, supply-chain, runtime-monitoring]
started: 2026-05-02T09:08:55+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-15-prompt-injection-threat-landscape, 2026-04-22-enterprise-ai-capability-model, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-04-26-access-control-amplification-agentic-operations, 2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring]
related: [2026-04-26-deployment-pipeline-citizen-development-governed-gate, 2026-04-26-systems-capability-debt-citizen-development-empirical-evidence, 2026-04-28-uelgf-tooling-reference-architecture]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What security capabilities are required in an enterprise Artificial Intelligence (AI) system to address prompt injection, Retrieval-Augmented Generation (RAG)-based attacks, model supply chain compromise, and data exfiltration beyond basic Application Programming Interface (API) access controls and audit logging?

## Research Question

What security capabilities are required in an enterprise Artificial Intelligence (AI) system, beyond basic Application Programming Interface (API) access controls and audit logging, to address prompt injection (direct and indirect), Retrieval-Augmented Generation (RAG)-based attacks (data poisoning, context manipulation, indirect injection via retrieved documents), model supply chain compromise (malicious fine-tuned weights, compromised model registries, trojan base models), and data exfiltration (sensitive data leakage through model outputs or tool calls), and how should these capabilities be incorporated into a complete enterprise AI security threat model?

## Scope

**In scope:**
- Threat model construction: a structured model of the four named attack classes covering attacker goals, attack vectors, assets at risk, and observable indicators
- Prompt injection: direct injection (user-controlled inputs), indirect injection (content retrieved from external sources that contains adversarial instructions), and compositional injection (chained tool calls that escalate privileges)
- RAG-based attacks: document poisoning in the knowledge base, context window manipulation through retrieved content, and cross-tenant data leakage in shared RAG deployments
- Model supply chain: risks from third-party fine-tuned models, model registries without provenance controls, base model backdoors, and quantised or Open Neural Network Exchange (ONNX) variant substitution
- Data exfiltration: sensitive data extraction through crafted prompts, tool call payloads as exfiltration channels, and output sanitisation bypass
- Countermeasures for each attack class: detection, prevention, and containment capabilities with evidence of effectiveness
- Gap analysis: which of these countermeasures are currently absent from a "basic API access + audit" baseline and must be added

**Out of scope:**
- Traditional web application vulnerabilities (SQL injection, cross-site scripting) not specific to AI systems
- Physical security, insider threat, or non-AI supply chain compromise
- Consumer AI or non-enterprise deployments
- Full penetration testing methodology

**Constraints:**
- Expand all acronyms on first use
- Distinguish between theoretically demonstrated attacks and those with known real-world incidents; label claims accordingly
- Reference the Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model (LLM) Applications and the MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS) as authoritative threat taxonomies
- Prior corpus research on prompt injection provides foundational coverage; this item must extend to RAG attacks, supply chain, and exfiltration specifically

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] Prior completed corpus work already established that prompt injection is a structural security problem for tool-using agents and that blast-radius reduction matters more than prompt wording alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html] The enterprise capability-model item treated security as a necessary enterprise domain, but it did not yet break that domain into the control families required for prompt, retrieval, model, and tool-path threats.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The unresolved design gap is therefore not whether enterprise AI needs security, but which additional capabilities must sit between the model and the enterprise environment so that retrieved content, third-party model artifacts, and action-capable tools cannot silently bypass ordinary access control and logging.

## Approach

1. **Threat model construction**: Apply a structured threat-modelling methodology, such as STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) or PASTA (Process for Attack Simulation and Threat Analysis), to the four named attack classes; produce a structured threat model with attacker profiles, assets, vectors, and mitigations.
2. **Prompt injection extension**: Review the prior corpus item and current research to identify what has changed since the foundational survey; focus on indirect injection and compositional attacks in agentic pipelines.
3. **RAG-based attack survey**: Search for documented RAG-specific attacks, defences, and empirical studies; assess which are theoretical versus demonstrated in practice.
4. **Model supply chain threat analysis**: Survey model registry provenance controls, known incidents or research demonstrations of supply chain compromise, and current best-practice countermeasures.
5. **Data exfiltration via AI**: Review research on output-channel exfiltration, prompt-induced data leakage, and tool-call-as-covert-channel attacks; document known mitigations.
6. **Capability gap analysis**: Compare the resulting threat model against the "basic API access + audit" baseline to produce a structured list of additional security capabilities required.
7. **Capability model integration**: Map each required capability to a domain in the enterprise AI capability model or propose a new security threat model domain.

## Sources

- [x] [Mitchell (2026) Prompt injection threat landscape](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html) - foundational corpus item on prompt injection attacks and defences
- [x] [Mitchell (2026) Permission-safe Retrieval-Augmented Generation (RAG) enterprise information architecture](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html) - prior corpus item on retrieval boundary correctness, access representation, and retrieval-store leakage
- [x] [Mitchell (2026) AI agent identity and access management enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior corpus item on machine identity, delegation, and attribution
- [x] [Mitchell (2026) AI agent control-plane architecture enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior corpus item on external policy enforcement and observability planes
- [x] [Mitchell (2026) Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) - prior corpus item on machine-speed privilege amplification
- [x] [Mitchell (2026) UELGF agentic AI specific risks and runtime monitoring](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html) - prior corpus item on runtime precursor monitoring and circuit breakers
- [x] [OWASP GenAI LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) - authoritative taxonomy for prompt injection, agency-sensitive impact, and baseline mitigations
- [x] [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - canonical list showing prompt injection, supply chain, sensitive information disclosure, and excessive agency as distinct risks
- [x] [MITRE ATLAS](https://atlas.mitre.org/) - authoritative AI-adversary taxonomy baseline
- [x] [NIST AI Risk Management Framework (AI RMF) Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - lifecycle risk-management and third-party governance expectations
- [x] [Greshake et al. (2023) Not what you've signed up for](https://arxiv.org/abs/2302.12173) - foundational indirect prompt injection paper for real-world Large Language Model-integrated applications
- [x] [Debenedetti et al. (2025) Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) - capability-based defence showing explicit control/data-flow separation
- [x] [Palo Alto Networks Unit 42 (2026) AI agent prompt injection telemetry](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) - in-the-wild observations of indirect prompt injection payloads and attacker intents
- [x] [Microsoft Azure AI Content Safety Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - user-prompt and document-attack detection controls
- [x] [Morris et al. (2023) Text Embeddings Reveal (Almost) As Much As Text](https://arxiv.org/abs/2310.06816) - embedding inversion evidence
- [x] [Anderson et al. (2024) Is My Data in Your Retrieval Database? Membership Inference Attacks Against Retrieval Augmented Generation](https://arxiv.org/abs/2405.20446) - retrieval-database membership leakage evidence
- [x] [PyTorch (2022) Compromised nightly dependency](https://pytorch.org/blog/compromised-nightly-dependency/) - official real-world machine-learning supply-chain compromise case
- [x] [Hugging Face Docs Pickle security](https://huggingface.co/docs/hub/security-pickle) - official documentation on unsafe model serialization, signed commits, and trust boundaries
- [x] [Hugging Face (2023) Safetensors security audit](https://huggingface.co/blog/safetensors-security-audit) - external audit result for safer tensor serialization
- [x] [AWS Security Blog (2026) Four security principles for agentic AI systems](https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/) - explicit guidance on machine-speed privilege amplification and deterministic external controls

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] **Research question restated:** what additional enterprise security capabilities are required once an AI system can ingest untrusted content, retrieve internal knowledge, load third-party model artifacts, and invoke tools, and how should those capabilities be expressed as a threat model rather than as a loose list of controls?
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle] **Scope confirmed:** the investigation covers four attack classes, prompt injection, RAG attack paths, model supply chain compromise, and data exfiltration, plus the control families needed before and during execution; it does not cover generic web-security defects or physical or insider compromise.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] **Prior work cross-reference:** completed repository work already established prompt injection as structural, permission-safe retrieval as an information-architecture problem, and agent governance as a control-plane problem, so this item extends the corpus by integrating those strands with model provenance and exfiltration controls.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] **Output format confirmed:** knowledge, specifically a threat model and capability map suitable for enterprise architecture and governance use.

### §1 Question Decomposition

- **Root question:** which enterprise controls are missing if an organization protects AI only with API access controls and audit logs?
- **A. Prompt and instruction integrity**
  - A1. What do OWASP and current research say prompt injection can do in tool-using systems?
  - A2. Which prompt-injection risks are theoretical, and which now have real-world telemetry?
  - A3. Which mitigations reduce impact without assuming perfect model obedience?
- **B. Retrieval and knowledge-path integrity**
  - B1. How does RAG expand the prompt-injection surface through documents and retrieved context?
  - B2. What extra retrieval risks exist beyond prompt injection, such as poisoning, stale permissions, embedding inversion, and retrieval-database leakage?
  - B3. Which architectural capabilities make retrieval boundaries enforceable?
- **C. Model supply chain integrity**
  - C1. What does real-world evidence show about compromised machine-learning dependencies and unsafe model-loading paths?
  - C2. Which provenance and artifact controls are required before a model or adapter is allowed into production?
- **D. Data exfiltration and action-path control**
  - D1. Through which channels can sensitive data leave the system: model output, retrieved context, tool arguments, outbound connectors, or autonomous triggers?
  - D2. Which controls must sit outside the model to stop unauthorized disclosure or action?
- **E. Capability gap and threat-model synthesis**
  - E1. Which required controls are absent from a baseline of API access control plus audit logging?
  - E2. How should the enterprise threat model define assets, attacker goals, indicators, and capabilities across the four attack classes?
  - E3. How should the resulting controls map back into the enterprise AI capability model?

### §2 Investigation

#### 2.1 Threat taxonomies and why the baseline changed

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP defines prompt injection as unintended model-behavior change caused by crafted input and explicitly says that the impact depends on the business context and the degree of agentic capability attached to the model.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP's current material distinguishes direct prompt injection, indirect prompt injection, multimodal prompt injection, excessive agency, supply chain vulnerabilities, and sensitive information disclosure as separate but interacting risk classes.
- [fact; source: https://arxiv.org/abs/2302.12173] Greshake et al. show that Large Language Model-integrated applications blur the boundary between instructions and data, enabling indirect prompt injection through retrieved external content and demonstrating manipulated Application Programming Interface calls, data theft, and information-ecosystem contamination.
- [fact; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/] Unit 42 reports real-world telemetry for web-based indirect prompt injection and says previously theoretical attack patterns are now being actively weaponized, with observed intents that include unauthorized transactions, data destruction, sensitive information leakage, and system-prompt leakage.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] The baseline changed because the same model weakness that once produced policy bypass in chat now sits inside action loops that can read untrusted content, invoke tools, and act at machine speed before a human can intervene.

#### 2.2 Retrieval-Augmented Generation (RAG) attack surface

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173] OWASP and Greshake both treat retrieved external content as a prompt-delivery path, which means any document, webpage, email, or tool response can become an indirect instruction channel once retrieved into context.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446] The completed permission-safe RAG item, supported by embedding-inversion and Membership Inference Attack evidence, shows that retrieval risk is not limited to poisoned instructions; the retrieval corpus itself can leak sensitive information or membership when permissions are represented poorly or when embeddings and retrieval outputs are exposed carelessly.
- [fact; source: https://arxiv.org/abs/2310.06816] Morris et al. report that dense text embeddings can reveal source text with high fidelity, including exact recovery of 92% of 32-token inputs in their setting and recovery of sensitive personal information from clinical-note data.
- [fact; source: https://arxiv.org/abs/2405.20446] Anderson et al. show that a Retrieval-Augmented Generation system can leak whether a passage is present in the retrieval database through black-box or gray-box prompting, establishing that the retrieval database is itself a sensitive asset.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] A complete threat model therefore has to separate retrieval integrity from prompt integrity: one control family governs what content enters context, another governs whether the corpus and its permission state are themselves safe to query.

#### 2.3 Model supply chain compromise

- [fact; source: https://pytorch.org/blog/compromised-nightly-dependency/] The 2022 PyTorch nightly compromise is a real machine-learning supply-chain incident in which a malicious `torchtriton` dependency uploaded to the Python Package Index executed a binary that collected system data, read sensitive local files, and exfiltrated them through encrypted Domain Name System queries.
- [fact; source: https://huggingface.co/docs/hub/security-pickle] Hugging Face documents that pickle-based model files can execute arbitrary code when deserialized, advises users to rely on trusted users and organizations, recommends signed commits for origin assurance, and presents `safetensors` as a safer serialization path.
- [fact; source: https://huggingface.co/blog/safetensors-security-audit] Hugging Face's external audit of `safetensors` found no critical arbitrary-code-execution flaw and positioned the format as the default safer model-storage path precisely because model weights are part of the software supply chain.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The NIST AI Risk Management Framework (AI RMF) Core says organizations should address AI risks arising from third-party software, data, and other supply-chain issues, which places model registries, adapters, dependencies, and serialization formats inside governance scope rather than outside it.
- [inference; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit] Model supply chain compromise is therefore not a speculative "future AI risk"; it is a present software-supply-chain problem with AI-specific surfaces, because model artifacts can be executable, opaque, frequently downloaded from public hubs, and hard to validate by inspection alone.

#### 2.4 Data exfiltration and action-path abuse

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP lists disclosure of sensitive information, unauthorized access to functions, arbitrary commands in connected systems, and manipulation of critical decision-making as direct consequences of successful prompt injection when agency exists.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection] Microsoft Prompt Shields distinguishes user-prompt attacks from document attacks and explicitly lists unauthorized data exfiltration, code execution, and blocking of system capabilities as document-attack outcomes.
- [fact; source: https://arxiv.org/abs/2503.18813] CaMeL argues that robust defense requires explicit control-flow and data-flow extraction plus capability enforcement at tool-call time so that untrusted data cannot decide program flow or exfiltrate private data over unauthorized channels.
- [fact; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] AWS states that agents operate at machine speed, that excessive privileges therefore carry more potential for unintended consequences, and that deterministic external controls, not the model's internal reasoning, should govern which tools, operations, and data are reachable.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Completed repository work shows that separate machine identities, accountable delegation, central policy enforcement, and observability are the architectural prerequisites for constraining tool access and attributing downstream actions.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Data exfiltration in enterprise AI is mainly an execution-control problem rather than a logging problem, because the decisive control point is whether the agent can read, transform, and send sensitive data through an allowed path before an audit record is ever reviewed.

#### 2.5 Capability gap versus the "API access + audit logging" baseline

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] The NIST AI RMF and OWASP both imply governance obligations that are broader than access control and logs, including third-party risk, input and output safeguards, ongoing monitoring, and controls for excessive agency.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html] The runtime-monitoring item in this corpus concludes that deployed agents need precursor-signal monitoring, such as drift, anomalous tool sequences, or unsafe coordination, before harm materializes, not only retrospective audit evidence after the action.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] The access-amplification item, reinforced by AWS guidance, shows why ordinary user permissions become riskier under automation: the same scope can be exercised continuously and at scale, so least privilege has to be re-scoped for the agent rather than copied from the invoking user.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://pytorch.org/blog/compromised-nightly-dependency/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html] A baseline of API access control plus audit logging therefore misses at least six control families: prompt and retrieval boundary defenses, permission-safe knowledge architecture, model provenance and artifact safety, agent-specific execution control, runtime anomaly detection, and deployment-time promotion gates for models, prompts, tools, and connectors.

### §3 Reasoning

- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2503.18813; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] The strongest pattern across prompt injection sources is that no source claims perfect prevention through prompts or filters alone; the defensible pattern is to assume the model can be manipulated and to enforce deterministic constraints outside the model.
- [inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] Retrieval threats divide cleanly into instruction integrity and data-boundary integrity, so a threat model that treats RAG as "just more prompt injection" is incomplete.
- [inference; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit] Model supply chain evidence is operationally stronger than generic "backdoored base model" discussion because it shows real compromise paths, unsafe defaults, and concrete mitigations that enterprises can require immediately.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Exfiltration risk resolves to identity, scope, and egress control: once the agent can read sensitive data and invoke an outbound tool, retrospective logging is too late to be the primary safeguard.

### §4 Consistency Check

- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2503.18813] There is no contradiction between OWASP saying foolproof prevention is unclear and CaMeL reporting provable security on a benchmark subset, because CaMeL narrows the problem by moving enforcement into a protective external layer rather than claiming that prompt obedience alone becomes reliable.
- [inference; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446; https://pytorch.org/blog/compromised-nightly-dependency/] The evidence strength differs by attack class: indirect prompt injection and machine-learning dependency compromise have real-world incident evidence, while some retrieval-leakage mechanisms remain strongest as published research demonstrations rather than widely reported production incidents.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://pytorch.org/blog/compromised-nightly-dependency/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] That asymmetry does not weaken the capability case, because the required mitigations, least privilege, provenance, deterministic controls, approval gates, and monitoring, are low-regret controls across both demonstrated and emerging mechanisms.

### §5 Depth and Breadth Expansion

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] **Governance lens:** the security program cannot treat prompts, retrieval corpora, model artifacts, and tool connectors as separate local engineering concerns; they are shared governance objects that need central standards and reviewable promotion paths.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] **Capability-model lens:** the enterprise capability model should treat AI security as at least four subdomains, identity-scoped execution, prompt and retrieval boundary defense, model and connector supply-chain assurance, and runtime assurance, because each subdomain depends on different assets, indicators, and operating processes.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] **Operational-risk lens:** the machine-speed amplification problem means that controls which were "good enough" for human users can be materially inadequate once an agent can execute broad permissions continuously.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://pytorch.org/blog/compromised-nightly-dependency/] **Delivery lens:** promotion gates matter for AI security because the thing being promoted is not just code; it is also model artifacts, prompt templates, retrieval connectors, and autonomous actions whose blast radius depends on environment-specific policy and provenance checks.

### §6 Synthesis

**Executive summary:**

Enterprise AI systems need a security stack that goes beyond access control and audit logs by adding controls for prompt and retrieval boundary integrity, model and connector provenance, identity-scoped execution, deterministic egress control, and runtime circuit breakers. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]

Prompt injection and Retrieval-Augmented Generation attacks are structural because trusted instructions and untrusted content share model context, so the enterprise has to constrain what the model can do even after content is retrieved or interpreted. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

Model supply chain compromise and unsafe model-loading paths are already operational risks, not hypothetical edge cases, because public machine-learning ecosystems have documented malicious dependency compromise and still rely heavily on formats that can execute code at load time. [fact; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit]

The resulting enterprise threat model should treat the prompt plane, retrieval corpus, model artifact pipeline, tool-execution surface, and runtime governance plane as separate assets with distinct indicators and control families, then map those families back into the enterprise capability model as explicit security subdomains. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html]

**Key findings:**

1. **A baseline of Application Programming Interface access controls plus audit logging is insufficient for enterprise AI, because it does not verify prompt integrity, retrieval-boundary correctness, model provenance, deterministic tool mediation, or pre-action containment once a model can ingest untrusted content and invoke connected systems.** ([inference]; high confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/)
2. **Prompt injection remains a structural risk rather than a filter-tuning problem, because authoritative sources and current research converge on the point that indirect content can still steer model behavior unless control flow, tool access, and approval boundaries are enforced outside the model itself.** ([inference]; high confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2503.18813)
3. **Retrieval-Augmented Generation introduces a second security boundary beyond prompt injection, because poisoned documents, stale access-control metadata, embedding inversion, and retrieval-database membership leakage can all expose or reshape sensitive knowledge even when ordinary authentication is present.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
4. **Model supply chain security must be treated as a first-class enterprise capability, because compromised machine-learning dependencies and unsafe serialization formats have already created code-execution and exfiltration paths that ordinary access controls do not detect before model loading occurs.** ([inference]; medium confidence; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit)
5. **Data exfiltration control for enterprise AI has to be enforced at the agent-execution layer, because the decisive risk is whether the system can read sensitive data and send it through tools, triggers, or outbound connectors before a human or audit process reviews the event.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **The minimum additional control stack is separate machine identities, least-privilege delegation, prompt and document attack detection, permission-safe retrieval architecture, model-artifact provenance and scanning, deterministic egress controls, human approval for high-consequence actions, and runtime anomaly detection with halt or quarantine paths.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://huggingface.co/docs/hub/security-pickle; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)
7. **The evidence base is strongest for indirect prompt injection telemetry, retrieval-leakage research, and machine-learning dependency compromise, while public evidence for large-scale nation-state use of these exact AI-native techniques remains materially thinner than the evidence for researchers, red teams, and opportunistic attackers.** ([inference]; medium confidence; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; https://arxiv.org/abs/2405.20446; https://pytorch.org/blog/compromised-nightly-dependency/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html)
8. **In the enterprise AI capability model, security should no longer be a single generic domain, because the evidence supports at least four distinct security subdomains, prompt and retrieval boundary defense, identity-scoped execution control, model and connector supply-chain assurance, and runtime assurance.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] API access control plus audit logging leaves prompt, retrieval, provenance, and runtime gaps. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ | high | Convergent governance and control-stack evidence. |
| [inference] Prompt injection is structural and needs external controls, not prompt wording alone. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2503.18813 | high | OWASP and both papers agree on the core mechanism. |
| [inference] Retrieval threats include corpus poisoning, embedding inversion, and Membership Inference Attack leakage. | https://arxiv.org/abs/2310.06816 ; https://arxiv.org/abs/2405.20446 ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html | medium | External research plus prior repository synthesis. |
| [inference] Machine-learning supply-chain compromise is operationally real and unsafe model loading is a concrete risk. | https://pytorch.org/blog/compromised-nightly-dependency/ ; https://huggingface.co/docs/hub/security-pickle ; https://huggingface.co/blog/safetensors-security-audit | medium | Real incident plus official mitigation guidance. |
| [inference] Exfiltration control belongs at the execution and egress layer. | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Document-attack outcomes and machine-identity control patterns align. |
| [inference] The minimum safe stack includes machine identity, retrieval architecture, provenance, egress control, and runtime monitoring. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html ; https://huggingface.co/docs/hub/security-pickle ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html | medium | Cross-source synthesis now covers identity, retrieval, provenance, egress, and runtime controls. |
| [inference] Public evidence is stronger for research, red-team, and opportunistic attack activity than for separately measured nation-state campaigns. | https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ ; https://pytorch.org/blog/compromised-nightly-dependency/ ; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html | medium | Evidence shows exploitation, but prevalence attribution remains incomplete. |
| [inference] Enterprise capability models should split AI security into multiple subdomains. | https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html | medium | Repository synthesis with clear architectural separation. |

**Assumptions:**

- [assumption; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection] The target enterprise wants AI systems that can call tools or process third-party documents rather than a strictly isolated chat interface. **Justification:** the control gap only becomes material once the model can read untrusted content or cause side effects.
- [assumption; source: https://huggingface.co/docs/hub/security-pickle; https://pytorch.org/blog/compromised-nightly-dependency/] The enterprise either consumes public model artifacts directly or inherits upstream components built from public machine-learning ecosystems. **Justification:** otherwise model-supply-chain risk can be reduced substantially through full internal curation and signing.

**Analysis:**

The complete enterprise threat model separates five assets: the prompt and instruction plane, the retrieval corpus and permission state, the model artifact and dependency pipeline, the tool-execution surface, and the runtime governance plane. Prompt injection primarily targets instruction integrity and tool authority; Retrieval-Augmented Generation attacks target retrieval integrity, permission correctness, and corpus confidentiality; supply-chain attacks target model provenance and loader safety; exfiltration attacks target secrets in context, outputs, and tool arguments; and runtime-governance failures target the organization's ability to detect unsafe precursor signals before action. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://pytorch.org/blog/compromised-nightly-dependency/; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html]

The control trade-off is between adaptability and determinism. Enterprises want agents to reason flexibly over new content and workflows, but the evidence shows security cannot be delegated to that same flexible reasoning loop. The durable pattern is therefore layered: scoped identity and policy outside the model, bounded retrieval inside explicit knowledge architectures, safe model promotion through provenance checks, and runtime monitoring that can halt execution when behavior moves outside the permitted envelope. [inference; source: https://arxiv.org/abs/2503.18813; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

Relative to the "API access + audit" baseline, the decisive additions are not more logs but more chokepoints. The enterprise needs promotion-time checks before models, prompts, and tools reach production; execution-time checks before tools or outbound channels are used; and runtime checks that stop suspicious sequences before they accumulate into machine-speed harm. Audit logs remain necessary, but in this evidence set they are forensic evidence, not the main preventive control. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html]

**Risks, gaps, uncertainties:**

- [fact; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/] The prompt-injection evidence base now includes in-the-wild telemetry, but the public record still exposes only part of actual attacker prevalence and does not yet support a precise ranking of threat-actor classes.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446] Retrieval-leakage evidence is strong in research settings, but the exact exploitability of every managed enterprise vector service will still depend on its exposure model, permission architecture, and outbound interface surface.
- [fact; source: https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit] Safer serialization and trust signals reduce model-loading risk, but they do not by themselves prove that a model is behaviorally safe, policy-compliant, or free of targeted backdoors.

**Open questions:**

1. What is the minimum practical evidence package for promoting a third-party model, adapter, or connector into a regulated enterprise environment?
2. Which runtime precursor signals are most predictive of exfiltration attempts before any data leaves the boundary?
3. How should enterprises quantify acceptable stale-permission windows for copied retrieval corpora?
4. Which evaluation suite best tests combined prompt, retrieval, and tool-path abuse in the same agent workflow?

### §7 Recursive Review

- Metadata: Prior-work sweep completed across prompt injection, identity, control-plane, Retrieval-Augmented Generation, access-amplification, runtime-monitoring, deployment-pipeline, and systems-capability-debt items.
- Metadata: All visible claims in §§0-6 are labeled or written as pure metadata fragments.
- Metadata: Acronym first-use audit checked for AI, API, RAG, LLM, ONNX, OWASP, and AI RMF.
- Metadata: Remaining uncertainty item recorded on enterprise-specific retrieval and connector-surface exploitability.
- Metadata: Verdict: PASS.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Enterprise AI systems need a security stack that goes beyond access control and audit logs by adding controls for prompt and retrieval boundary integrity, model and connector provenance, identity-scoped execution, deterministic egress control, and runtime circuit breakers. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]

Prompt injection and Retrieval-Augmented Generation (RAG) attacks are structural because trusted instructions and untrusted content share model context, so the enterprise has to constrain what the model can do even after content is retrieved or interpreted. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

Model supply chain compromise and unsafe model-loading paths are already operational risks, not hypothetical edge cases, because public machine-learning ecosystems have documented malicious dependency compromise and still rely heavily on formats that can execute code at load time. [fact; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit]

The resulting enterprise threat model should treat the prompt plane, retrieval corpus, model artifact pipeline, tool-execution surface, and runtime governance plane as separate assets with distinct indicators and control families, then map those families back into the enterprise capability model as explicit security subdomains. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html]

### Key Findings

1. **A baseline of Application Programming Interface access controls plus audit logging is insufficient for enterprise AI, because it does not verify prompt integrity, retrieval-boundary correctness, model provenance, deterministic tool mediation, or pre-action containment once a model can ingest untrusted content and invoke connected systems.** ([inference]; high confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/)
2. **Prompt injection remains a structural risk rather than a filter-tuning problem, because authoritative sources and current research converge on the point that indirect content can still steer model behavior unless control flow, tool access, and approval boundaries are enforced outside the model itself.** ([inference]; high confidence; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2503.18813)
3. **Retrieval-Augmented Generation introduces a second security boundary beyond prompt injection, because poisoned documents, stale access-control metadata, embedding inversion, and retrieval-database membership leakage can all expose or reshape sensitive knowledge even when ordinary authentication is present.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
4. **Model supply chain security must be treated as a first-class enterprise capability, because compromised machine-learning dependencies and unsafe serialization formats have already created code-execution and exfiltration paths that ordinary access controls do not detect before model loading occurs.** ([inference]; medium confidence; source: https://pytorch.org/blog/compromised-nightly-dependency/; https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit)
5. **Data exfiltration control for enterprise AI has to be enforced at the agent-execution layer, because the decisive risk is whether the system can read sensitive data and send it through tools, triggers, or outbound connectors before a human or audit process reviews the event.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **The minimum additional control stack is separate machine identities, least-privilege delegation, prompt and document attack detection, permission-safe retrieval architecture, model-artifact provenance and scanning, deterministic egress controls, human approval for high-consequence actions, and runtime anomaly detection with halt or quarantine paths.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://huggingface.co/docs/hub/security-pickle; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)
7. **The evidence base is strongest for indirect prompt injection telemetry, retrieval-leakage research, and machine-learning dependency compromise, while public evidence for large-scale nation-state use of these exact AI-native techniques remains materially thinner than the evidence for researchers, red teams, and opportunistic attackers.** ([inference]; medium confidence; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; https://arxiv.org/abs/2405.20446; https://pytorch.org/blog/compromised-nightly-dependency/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html)
8. **In the enterprise AI capability model, security should no longer be a single generic domain, because the evidence supports at least four distinct security subdomains, prompt and retrieval boundary defense, identity-scoped execution control, model and connector supply-chain assurance, and runtime assurance.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] API access control plus audit logging leaves prompt, retrieval, provenance, and runtime gaps. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ | high | Convergent governance and control-stack evidence. |
| [inference] Prompt injection is structural and needs external controls, not prompt wording alone. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2503.18813 | high | OWASP and both papers agree on the core mechanism. |
| [inference] Retrieval threats include corpus poisoning, embedding inversion, and Membership Inference Attack leakage. | https://arxiv.org/abs/2310.06816 ; https://arxiv.org/abs/2405.20446 ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html | medium | External research plus prior repository synthesis. |
| [inference] Machine-learning supply-chain compromise is operationally real and unsafe model loading is a concrete risk. | https://pytorch.org/blog/compromised-nightly-dependency/ ; https://huggingface.co/docs/hub/security-pickle ; https://huggingface.co/blog/safetensors-security-audit | medium | Real incident plus official mitigation guidance. |
| [inference] Exfiltration control belongs at the execution and egress layer. | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Document-attack outcomes and machine-identity control patterns align. |
| [inference] The minimum safe stack includes machine identity, retrieval architecture, provenance, egress control, and runtime monitoring. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html ; https://huggingface.co/docs/hub/security-pickle ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html | medium | Cross-source synthesis now covers identity, retrieval, provenance, egress, and runtime controls. |
| [inference] Public evidence is stronger for research, red-team, and opportunistic attack activity than for separately measured nation-state campaigns. | https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ ; https://pytorch.org/blog/compromised-nightly-dependency/ ; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html | medium | Evidence shows exploitation, but prevalence attribution remains incomplete. |
| [inference] Enterprise capability models should split AI security into multiple subdomains. | https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html | medium | Repository synthesis with clear architectural separation. |

### Assumptions

- [assumption; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection] The target enterprise wants AI systems that can call tools or process third-party documents rather than a strictly isolated chat interface. **Justification:** the control gap only becomes material once the model can read untrusted content or cause side effects.
- [assumption; source: https://huggingface.co/docs/hub/security-pickle; https://pytorch.org/blog/compromised-nightly-dependency/] The enterprise either consumes public model artifacts directly or inherits upstream components built from public machine-learning ecosystems. **Justification:** otherwise model-supply-chain risk can be reduced substantially through full internal curation and signing.

### Analysis

The complete enterprise threat model separates five assets: the prompt and instruction plane, the retrieval corpus and permission state, the model artifact and dependency pipeline, the tool-execution surface, and the runtime governance plane. Prompt injection primarily targets instruction integrity and tool authority; Retrieval-Augmented Generation attacks target retrieval integrity, permission correctness, and corpus confidentiality; supply-chain attacks target model provenance and loader safety; exfiltration attacks target secrets in context, outputs, and tool arguments; and runtime-governance failures target the organization's ability to detect unsafe precursor signals before action. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://pytorch.org/blog/compromised-nightly-dependency/; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html]

The control trade-off is between adaptability and determinism. Enterprises want agents to reason flexibly over new content and workflows, but the evidence shows security cannot be delegated to that same flexible reasoning loop. The durable pattern is therefore layered: scoped identity and policy outside the model, bounded retrieval inside explicit knowledge architectures, safe model promotion through provenance checks, and runtime monitoring that can halt execution when behavior moves outside the permitted envelope. [inference; source: https://arxiv.org/abs/2503.18813; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

Relative to the "API access + audit" baseline, the decisive additions are not more logs but more chokepoints. The enterprise needs promotion-time checks before models, prompts, and tools reach production; execution-time checks before tools or outbound channels are used; and runtime checks that stop suspicious sequences before they accumulate into machine-speed harm. Audit logs remain necessary, but in this evidence set they are forensic evidence, not the main preventive control. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html]

### Risks, Gaps, and Uncertainties

- [fact; source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/] The prompt-injection evidence base now includes in-the-wild telemetry, but the public record still exposes only part of actual attacker prevalence and does not yet support a precise ranking of threat-actor classes.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446] Retrieval-leakage evidence is strong in research settings, but the exact exploitability of every managed enterprise vector service will still depend on its exposure model, permission architecture, and outbound interface surface.
- [fact; source: https://huggingface.co/docs/hub/security-pickle; https://huggingface.co/blog/safetensors-security-audit] Safer serialization and trust signals reduce model-loading risk, but they do not by themselves prove that a model is behaviorally safe, policy-compliant, or free of targeted backdoors.

### Open Questions

1. What is the minimum practical evidence package for promoting a third-party model, adapter, or connector into a regulated enterprise environment?
2. Which runtime precursor signals are most predictive of exfiltration attempts before any data leaves the boundary?
3. How should enterprises quantify acceptable stale-permission windows for copied retrieval corpora?
4. Which evaluation suite best tests combined prompt, retrieval, and tool-path abuse in the same agent workflow?

---

## Output

- Type: knowledge
- Description: This item produces a security capability map and threat-model structure showing that enterprise AI needs explicit controls for prompt and retrieval boundaries, model provenance, identity-scoped execution, deterministic egress, and runtime containment before action-capable deployment is defensible. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://pytorch.org/blog/compromised-nightly-dependency/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]
- Links:
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://pytorch.org/blog/compromised-nightly-dependency/
  - https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/

---
title: "What security capabilities are required in an enterprise AI system to address prompt injection, Retrieval-Augmented Generation (RAG)-based attacks, model supply chain compromise, and data exfiltration beyond basic API access controls and audit logging?"
added: 2026-05-02T06:00:57+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [security, prompt-injection, agentic-ai, llm, ai-governance, enterprise, regulated-enterprise, adversarial, owasp, supply-chain]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-15-prompt-injection-threat-landscape, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring, 2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-04-22-enterprise-ai-capability-model]
related: [2026-03-15-prompt-injection-threat-landscape, 2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-04-28-uelgf-tooling-reference-architecture]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What security capabilities are required in an enterprise AI system to address prompt injection, Retrieval-Augmented Generation (RAG)-based attacks, model supply chain compromise, and data exfiltration beyond basic API access controls and audit logging?

## Research Question

What security capabilities are required in an enterprise Artificial Intelligence (AI) system, beyond basic Application Programming Interface (API) access controls and audit logging, to address prompt injection (direct and indirect), Retrieval-Augmented Generation (RAG)-based attacks (data poisoning, context manipulation, indirect injection via retrieved documents), model supply chain compromise (malicious fine-tuned weights, compromised model registries, trojan base models), and data exfiltration (sensitive data leakage through model outputs or tool calls), and how should these capabilities be incorporated into a complete enterprise AI security threat model?

## Scope

**In scope:**
- Threat model construction: a structured model of the four named attack classes covering attacker goals, attack vectors, assets at risk, and observable indicators
- Prompt injection: direct injection (user-controlled inputs), indirect injection (content retrieved from external sources that contains adversarial instructions), and compositional injection (chained tool calls that escalate privileges)
- RAG-based attacks: document poisoning in the knowledge base, context window manipulation through retrieved content, and cross-tenant data leakage in shared RAG deployments
- Model supply chain: risks from third-party fine-tuned models, model registries without provenance controls, base model backdoors, and quantised or ONNX (Open Neural Network Exchange) variant substitution
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
- Reference the Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model (LLM) Applications and MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) as authoritative threat taxonomies
- Prior corpus research on prompt injection provides foundational coverage; this item must extend to RAG attacks, supply chain, and exfiltration specifically

## Context

Prior research comprehensively covered the prompt injection threat landscape. The enterprise AI capability model work included security as a domain but scoped it narrowly to API access controls and audit logging. As enterprise AI deployments mature and incorporate RAG pipelines, fine-tuned models from external registries, and agentic tool use, the attack surface expands significantly beyond what basic access controls address. This item produces the security threat model required to extend the capability model to cover the full attack surface.

## Approach

1. **Threat model construction**: Apply a structured threat modelling methodology (STRIDE — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — or PASTA — Process for Attack Simulation and Threat Analysis) to the four named attack classes; produce a structured threat model with attacker profiles, assets, vectors, and mitigations.
2. **Prompt injection extension**: Review the prior corpus item and current research to identify what has changed since the foundational survey; focus on indirect injection and compositional attacks in agentic pipelines.
3. **RAG-based attack survey**: Search for documented RAG-specific attacks, defences, and empirical studies; assess which are theoretical vs demonstrated in practice.
4. **Model supply chain threat analysis**: Survey model registry provenance controls, known incidents or research demonstrations of supply chain compromise, and current best-practice countermeasures.
5. **Data exfiltration via AI**: Review research on output-channel exfiltration, prompt-induced data leakage, and tool-call-as-covert-channel attacks; document known mitigations.
6. **Capability gap analysis**: Compare the resulting threat model against the "basic API access + audit" baseline to produce a structured list of additional security capabilities required.
7. **Capability model integration**: Map each required capability to a domain in the enterprise AI capability model or propose a new security threat model domain.

## Sources

- [ ] [Mitchell (2026) Prompt injection threat landscape](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html) — foundational corpus item on prompt injection attacks and defences
- [ ] [Mitchell (2026) Permission-safe RAG enterprise information architecture](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html) — RAG access control and cross-tenant data protection
- [ ] [Mitchell (2026) UELGF agentic AI specific risks and runtime monitoring](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html) — agentic risk categories in the governance framework
- [ ] [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — authoritative LLM vulnerability taxonomy including prompt injection and data exfiltration
- [ ] [MITRE ATLAS — Adversarial Threat Landscape for Artificial-Intelligence Systems](https://atlas.mitre.org/) — structured AI threat taxonomy covering supply chain and evasion attacks
- [ ] [NIST AI Risk Management Framework (AI RMF)](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — security control categories for AI systems

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:

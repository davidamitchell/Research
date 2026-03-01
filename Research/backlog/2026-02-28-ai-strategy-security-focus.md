---
title: "AI Strategy Examples: Security Focus"
added: 2026-02-28
status: backlog
priority: high
tags: [ai-strategy, security, cybersecurity, threat-detection, adversarial-ai, ai-governance]
started: ~
completed: ~
output: [knowledge]
---

# AI Strategy Examples: Security Focus

## Research Question

Which organisations have developed coherent AI strategies with security as the primary objective — either using AI to enhance security posture or governing the security risks that AI systems themselves introduce — and what frameworks, architectures, and governance structures characterise effective approaches?

## Scope

**In scope:**
- AI used offensively for security (threat detection, anomaly detection, attack surface analysis, vulnerability identification)
- AI used defensively in security operations (SOC automation, incident response, patch prioritisation)
- Security governance for AI systems themselves: adversarial attacks on AI models, data poisoning, model inversion, prompt injection in LLM-based systems
- Regulatory and standards frameworks for AI in security contexts: NIST CSF 2.0 AI considerations, ISO/IEC 27001 AI intersections, NZ NCSC guidance
- NZ-specific context: National Cyber Security Centre (NCSC), Government Communications Security Bureau (GCSB), CERT NZ

**Out of scope:**
- Physical security AI (surveillance, access control) — narrow scope
- AI regulation as a security issue (addressed in AI Act / NIST RMF item)
- Cryptography and post-quantum issues unrelated to AI

**Constraints:** Distinguish between AI applied to security (AI as a tool) and security applied to AI (AI as a threat surface). Both are in scope but must be kept analytically separate.

## Context

The AI strategy research item (completed 2026-02-28) identified security as a material gap in NZ's current strategy document — "Investing with Confidence" focuses on adoption and economic benefit with limited explicit security architecture guidance. The EU AI Act, DORA, and Singapore's Model AI Governance Framework all treat security as a first-order governance concern for AI systems.

Two distinct risks require separate treatment:
1. **AI-enhanced threats**: adversaries using AI to accelerate and scale attacks (phishing, social engineering, vulnerability exploitation)
2. **AI system vulnerabilities**: the AI systems themselves as attack surfaces (model poisoning, adversarial examples, prompt injection, supply chain attacks on model weights)

NZ organisations deploying Type 2, 3, and 4 AI (from the four-type typology) face both risks. The governance architecture for each is different.

## Approach

1. **Map the threat landscape** — what does the current evidence say about AI-enhanced cyberattacks? Quantify where possible (frequency change, cost change).
2. **Survey AI security strategy cases** — identify 6–8 organisations (government agencies, financial institutions, critical infrastructure operators) that have disclosed AI security strategy design and outcomes.
3. **AI system security governance** — document known attack vectors against AI systems (MITRE ATLAS, OWASP ML Top 10, NIST AI RMF adversarial threat categories) and how organisations are governing against them.
4. **NZ regulatory mapping** — what do NCSC, GCSB, and CERT NZ say specifically about AI in security contexts? Are there advisories or frameworks?
5. **Synthesis** — what does an AI security strategy look like for a NZ financial institution or government agency? What are the minimum viable governance controls?

## Sources

- [ ] MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- [ ] OWASP LLM Top 10 (2023 / 2024 update)
- [ ] NIST AI RMF: adversarial machine learning profile (NIST AI 100-2e2023)
- [ ] GCSB / NCSC NZ: annual cyber threat reports and any AI-specific advisories
- [ ] CERT NZ: threat intelligence reports referencing AI
- [ ] Microsoft Security Intelligence: AI-enhanced threat reports (2023–2025)
- [ ] Google Project Zero / DeepMind AI security research
- [ ] CISA (US): AI security guidance documents
- [ ] Singapore IMDA: security dimension of Model AI Governance Framework (2024)
- [ ] NZ financial sector: any RBNZ or FMA guidance on AI-related security obligations

---

## Findings

*(Fill in when completing.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:

---
title: "Prompt injection threat landscape: exploits, defences, and active research in agentic AI systems"
added: 2026-03-15
status: backlog
priority: high
blocks: []
tags: [prompt-injection, security, llm, agents, adversarial, owasp, mitre-atlas, red-team, ai-governance]
started: ~
completed: ~
output: [knowledge]
---

# Prompt injection threat landscape: exploits, defences, and active research in agentic AI systems

## Research Question

What is the current state of the prompt injection threat in agentic AI systems: who is exploiting it, who is defending against it, and what does the research community consider unsolved?

Supporting questions:
- What attack types exist (direct, indirect, compositional) and which are most dangerous for agents that can take real-world actions?
- Which threat actors are conducting prompt injection attacks, and what real-world incidents have been disclosed?
- Which organisations and researchers are building defences, and how effective are those defences?
- What are the 5–10 most significant papers or findings from 2024–2025, and what open problems remain?

## Scope

**In scope:**
- Taxonomy of prompt injection attack types: direct (user-controlled input), indirect (environment-sourced: web pages, documents, tool outputs), and multi-turn/compositional attacks
- Who is conducting attacks: threat actors, research groups, red teams, and known real-world incidents involving prompt injection in deployed systems
- Who is building defences: researchers, platform vendors (OpenAI, Anthropic, Google DeepMind, Microsoft), standards bodies (OWASP, NIST, MITRE), and enterprise security teams
- The attack surface specific to agentic systems: agents that browse the web, execute code, send emails, call APIs, or have filesystem access — and why indirect injection is qualitatively more dangerous in these contexts
- Current published research (2023–2025): academic papers, red-team disclosures, CVEs, and practitioner blog posts
- Mitigation approaches and their effectiveness: prompt hardening, instruction hierarchy, sandboxing, input/output filtering, privilege separation, human-in-the-loop gates
- Industry standards and frameworks: OWASP LLM Top 10 (LLM01 Prompt Injection), MITRE ATLAS, NIST AI 100-2 (Adversarial Machine Learning)

**Out of scope:**
- Adversarial attacks on non-LLM ML models (adversarial examples, model inversion) — covered in `ai-strategy-security-focus`
- Data poisoning of training data (separate threat model)
- General AI governance and AI strategy — covered in `ai-strategy-security-focus` and related items
- Post-quantum cryptography and unrelated cybersecurity domains

**Constraints:** Prioritise evidence from production deployments, red-team disclosures, and peer-reviewed research over theoretical attack descriptions. Focus on 2023–2025 to capture the agentic AI era.

## Context

Prompt injection was identified in `2026-02-28-ai-strategy-security-focus.md` as a key vulnerability in the "AI system as attack surface" category, alongside model poisoning and supply chain attacks on model weights. That item treated prompt injection as one item in a broader security taxonomy. The present research item is dedicated to prompt injection alone because:

1. **Severity has escalated with agency.** In 2022–2023 prompt injection was primarily a nuisance (jailbreaks, data exfiltration via the LLM's own output). In 2024–2025, agentic systems that browse, write code, call APIs, and send messages mean a successful injection can result in account takeover, data destruction, or lateral movement in the attacker's supply chain. The threat model has fundamentally changed.
2. **The adversarial agent pattern is now operationally relevant.** The research in `2026-03-10-adversarial-agents-shared-goals-multi-perspective.md` examined adversarial collaboration as a design pattern for multi-agent quality assurance. Prompt injection inverts this: it is a mechanism by which an attacker injects a hostile "agent" (a crafted instruction in the environment) that subverts a legitimate agent's goal. Understanding the injection threat landscape directly informs how to design and audit adversarial-collaboration pipelines against external manipulation.
3. **Standards work is in flight.** OWASP LLM Top 10 version 2 (2025), MITRE ATLAS updates for agentic systems, and NIST AI 100-2 all published or updated in 2024–2025. The landscape is moving fast enough that a dedicated, current-state research item is warranted.

## Approach

1. **Attack taxonomy** — synthesise the current academic and practitioner classification of prompt injection types (direct, indirect, compositional, multi-agent). Use OWASP LLM01, MITRE ATLAS, and Simon Willison's taxonomy as primary framings. What makes agentic indirect injection categorically more dangerous than chatbot-era injection?
2. **Who is attacking** — identify threat actors and attack patterns: known real-world incidents, red-team disclosures (from security researchers, AI companies' own red teams), and CVEs or published exploits. What is the evidence that this is being actively exploited in the wild vs. remaining primarily a research-stage attack?
3. **Who is defending** — survey the defence landscape: platform-level mitigations from major AI vendors (OpenAI, Anthropic, Google, Microsoft Copilot), research defences (instruction hierarchy, spotlighting, prompt shields, constitutional AI), and enterprise tooling (Lakera Guard, Rebuff, etc.). What is the empirical effectiveness of each?
4. **Active research front** — identify the 5–10 most cited or influential papers from 2024–2025 on prompt injection. What are the open problems the research community has not yet solved? What is the current consensus on what "solved" would even look like?
5. **Agentic system design implications** — synthesise findings into concrete design recommendations for agentic systems: what architectural choices reduce the injection attack surface, what operational controls are required, and what governance gates (human-in-the-loop) are non-negotiable for high-privilege agents?

## Sources

- [ ] OWASP LLM Top 10 v2 (2025) — https://owasp.org/www-project-top-10-for-large-language-model-applications/ — LLM01: Prompt Injection
- [ ] MITRE ATLAS — https://atlas.mitre.org/ — adversarial threat matrix for AI systems; agentic system entries
- [ ] NIST AI 100-2 "Adversarial Machine Learning: A Taxonomy and Terminology" — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf
- [ ] Simon Willison's prompt injection writing — https://simonwillison.net/series/prompt-injection/ — authoritative practitioner taxonomy and incident catalogue
- [ ] "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (Greshake et al., 2023) — foundational indirect injection paper
- [ ] Anthropic's "Many-shot jailbreaking" (2024) and Constitutional AI documentation — defence-side research
- [ ] Microsoft Prompt Shields documentation and Copilot red-team disclosures — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- [ ] Google DeepMind "CyberSecEval" and agent security research (2024–2025)
- [ ] Lakera AI "PINT Benchmark" and Gandalf red-team data — practitioner dataset of real injection attempts
- [ ] arXiv search: "prompt injection agent" 2024–2025 — top-cited papers on agentic injection

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:

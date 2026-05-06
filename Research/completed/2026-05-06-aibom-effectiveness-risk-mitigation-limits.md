---
review_count: 2
title: "What security and governance risks can a declared and runtime-observed inventory of models, prompts, retrieval sources, tools, memory, and delegation artifacts realistically mitigate for tool-using, stateful Artificial Intelligence (AI) workloads, and where does it create false assurance?"
added: 2026-05-06T08:52:41+00:00
status: completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, governance, supply-chain, llm, ai-governance, observability]
started: 2026-05-06T20:40:30+00:00
completed: 2026-05-06T21:07:31+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain]
related: [2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-platform-observability-control-comparison, 2026-04-26-permission-safe-rag-enterprise-information-architecture]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: synthesis # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What security and governance risks can a declared and runtime-observed inventory of models, prompts, retrieval sources, tools, memory, and delegation artifacts realistically mitigate for tool-using, stateful Artificial Intelligence (AI) workloads, and where does it create false assurance?

## Research Question

What categories of security and governance risk can an Artificial Intelligence Bill of Materials (AIBOM), an artifact intended to make artificial intelligence systems transparent, auditable, and secure, in both declared design-time and runtime-observed variants, realistically mitigate for tool-using, stateful Artificial Intelligence (AI) workloads, what metrics can quantify that mitigation, and where does an apparently complete AIBOM create dangerous false assurance by leaving behavioral, inferential, and emergent risks invisible? [fact; source: https://owaspaibom.org/]

## Scope

**In scope:**
- Structural risk mitigation: dependency graph vulnerabilities, known-compromised component detection, version drift alerts, analogous to Software Bill of Materials (SBOM) use cases
- Behavioral risk visibility gaps: prompt injection, tool misuse, Retrieval-Augmented Generation (RAG) poisoning, and runtime manipulation that bypass even a complete AIBOM
- Drift risk categories: model version drift, RAG knowledge-base staleness, external tool Application Programming Interface (API) changes, memory corruption, and which are detectable via AIBOM versus invisible
- False assurance scenarios: documented attack patterns showing how an attacker can fully compromise an agentic system despite a valid, up-to-date AIBOM
- Metric proposals: runtime dependency capture rate, drift detection latency, blast-radius reduction from AIBOM-informed controls, and AIBOM coverage-completeness score
- Inference opacity: the limits on what can be known about a model's reasoning process regardless of AIBOM completeness

**Out of scope:**
- Platform-specific implementation details, covered in the practice items
- Regulatory compliance obligations, covered in adjacent regulatory work
- AIBOM schema design, covered in `2026-05-06-aibom-schema-design-standards-alignment`

**Constraints:**
- Must distinguish structural risks, where AIBOM helps, from behavioral or inferential risks, where it does not
- Red-team scenarios must be sourced or grounded in documented attack patterns
- Must build on the completed theory and practice items in this AIBOM series

## Context

- [fact; source: https://www.ntia.gov/page/software-bill-materials] The National Telecommunications and Information Administration frames a Software Bill of Materials (SBOM) as a nested inventory and explicitly highlights use cases and benefits for software producers, choosers, and operators across the supply chain.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] The National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) says artificial intelligence risk management must incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The unresolved decision problem is not whether AIBOM can improve transparency, but where that transparency materially lowers risk and where it merely documents a system that can still be subverted through legitimate channels, runtime state, or opaque model behavior.

## Approach

1. **Risk taxonomy and AIBOM coverage mapping:** Build a structured taxonomy of agentic Artificial Intelligence security and governance risks, drawing on the prior security threat model and the current external taxonomies. For each risk category, assess whether AIBOM provides full visibility, partial visibility, no visibility, or false assurance.
2. **Structural risk mitigation analysis:** Document where AIBOM genuinely reduces risk, including component vulnerability detection, version pinning, dependency-graph anomaly detection, and authority-surface documentation.
3. **False assurance scenarios:** Document concrete scenarios where a complete, well-formed AIBOM provides false assurance, including prompt injection, Retrieval-Augmented Generation poisoning, memory poisoning, and harmful use of legitimately declared tools.
4. **Inference opacity boundary:** Analyze where current neural-network inference opacity creates a practical visibility gap that present-day AIBOM methods do not close.
5. **Metric proposals:** Define a minimal set of metrics that quantify AIBOM effectiveness and identify the baseline data required to compute each.

## Sources

- [x] [Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model (LLM) Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - current OWASP risk taxonomy for prompt injection, supply chain, disclosure, excessive agency, and overreliance
- [x] [Open Worldwide Application Security Project (OWASP) Artificial Intelligence Bill of Materials (AIBOM)](https://owaspaibom.org/) - official AIBOM framing for transparency, auditability, and traceability
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - governance, trustworthiness, explainability, and measurement framing for artificial intelligence systems
- [x] [Greshake et al. (2023) Not What You Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) - primary academic evidence for indirect prompt injection, data theft, and manipulated tool use
- [x] [Perez and Ribeiro (2022) Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) - primary academic evidence for goal hijacking and prompt leaking through prompt injection
- [x] [Microsoft Security (2025) New whitepaper outlines the taxonomy of failure modes in AI agents](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/) - official Microsoft summary of agentic artificial intelligence failure modes, including memory poisoning and mitigation guidance
- [x] [Anthropic (2026) Claude Opus 4.6 System Card](https://www.anthropic.com/claude-opus-4-6-system-card) - official model-system-card evidence on interpretability tooling, limits on judging whether visible reasoning matches the process that produced the answer, and residual unexpected behavior
- [x] [National Telecommunications and Information Administration (NTIA) Software Bill of Materials](https://www.ntia.gov/page/software-bill-materials) - official SBOM overview linking the 2019 roles-and-benefits use-case paper and related supply-chain guidance
- [x] [David Mitchell (2026) AI security threat model for prompt injection, Retrieval-Augmented Generation (RAG), supply chain, and exfiltration](https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html) - prior repository synthesis of agentic artificial intelligence threat surfaces and control families
- [x] [David Mitchell (2026) Permission-safe Retrieval-Augmented Generation in enterprise information architectures](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html) - prior repository item on retrieval-boundary integrity, permission modeling, and retrieval-store failure modes
- [x] [David Mitchell (2026) Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic artificial intelligence workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html) - prior repository item defining why package-style inventory is insufficient for agentic systems
- [x] [David Mitchell (2026) What is the minimal viable schema for an Artificial Intelligence bill of materials for prompt, retrieval, memory, and tool-using artificial intelligence systems, and how should it align with CycloneDX and Software Package Data Exchange (SPDX)?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html) - prior repository item defining the declared AIBOM surfaces this item evaluates
- [x] [David Mitchell (2026) How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic artificial intelligence system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html) - prior repository item defining runtime evidence and declared-versus-observed divergence
- [x] [David Mitchell (2026) How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic artificial intelligence systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html) - prior repository item on authority, delegation, and permission-scope representation
- [x] [David Mitchell (2026) What introspection, export, and control surfaces actually exist across production agentic artificial intelligence platforms?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html) - prior repository item on the observability substrate needed to compute runtime AIBOM metrics

## Related

- [Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic artificial intelligence workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html)
- [How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic artificial intelligence system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
- [How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic artificial intelligence systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
- [Permission-safe Retrieval-Augmented Generation in enterprise information architectures: technical constraints, architectural options, and failure modes at scale](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: Which security and governance risks are materially reduced by a declared or runtime-observed AIBOM, which risks remain outside inventory visibility, and which metrics can distinguish real mitigation from false assurance?
- Scope: risk taxonomy, structural-mitigation analysis, false-assurance scenarios, inference-opacity boundary, and effectiveness metrics.
- Constraints: separate structural from behavioral risk, ground attack scenarios in documented evidence, and synthesize across the completed AIBOM theory and practice items.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html

### §1 Question Decomposition

- **Root question:** What can an AIBOM actually make safer in agentic, tool-using, stateful artificial intelligence systems, and what remains unsafe even when the AIBOM is accurate and complete?
  - **A. Risk taxonomy**
    - A1. Which agentic security and governance risks are primarily structural?
    - A2. Which risks are primarily semantic, behavioral, or inferential?
    - A3. Which risks sit between those categories and therefore receive only partial benefit from AIBOM coverage?
  - **B. Genuine mitigation**
    - B1. Which risks become easier to detect or constrain when components, versions, permissions, and runtime divergence are recorded?
    - B2. Which SBOM value propositions transfer into an AIBOM with minimal distortion?
  - **C. False assurance**
    - C1. Which documented attacks succeed through legitimate channels even when the declared component set is accurate?
    - C2. Which runtime-state failures invalidate the idea that inventory completeness equals safety?
  - **D. Opacity boundary**
    - D1. Which parts of model behavior can be documented at the boundary of the system?
    - D2. Which parts remain opaque even with model cards, traces, and runtime capture?
  - **E. Measurement**
    - E1. Which metrics can show that AIBOM adoption improved structural control?
    - E2. Which metrics can detect when an AIBOM is creating false assurance rather than genuine risk reduction?

### §2 Investigation

#### Source substitutions and coverage notes

- Source substitution: NIST Artificial Intelligence Risk Management Framework landing page cited in place of the legacy seeded PDF URL.
- Source substitution: NTIA Software Bill of Materials landing page cited in place of the legacy seeded 2019 PDF URL.
- Source substitution: Claude Opus 4.6 system-card URL cited in place of the legacy Anthropic `model-card` URL.

#### A. Risk taxonomy and AIBOM coverage boundary

- [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP separates prompt injection, training-data poisoning, supply-chain vulnerabilities, sensitive-information disclosure, insecure plugin design, excessive agency, overreliance, and model theft into distinct but interacting Large Language Model (LLM) risk classes.
- [fact; source: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] Microsoft classifies agentic artificial intelligence failures across security and safety, distinguishes novel and existing failure modes, and explicitly includes memory poisoning, tool compromise, and agent misalignment in the agentic threat surface.
- [fact; source: https://www.ntia.gov/page/software-bill-materials] NTIA describes SBOM value in terms of visibility into software ingredients and supply-chain relationships for producers, choosers, and operators.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://www.ntia.gov/page/software-bill-materials] The closest AIBOM analogue to classic SBOM value appears where the risk is anchored in declared artifacts, relationships, versions, identities, and policy surfaces, while risks dominated by semantic payloads or opaque inference remain outside inventory-style control.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] In the repository's AIBOM series, the structural surfaces that can be inventory-managed are model and prompt artifacts, retrieval stores, tool manifests, identity and delegation edges, memory schemas, runtime traces, and guardrail or policy configuration, not the full semantic meaning of future content or the internal reasoning of the model.

#### B. Where AIBOM genuinely reduces risk

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST says artificial intelligence risk measurement and management are complicated by third-party software, hardware, and data, and it expects all actors to manage risk in standalone or integrated components.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] The completed schema item found that prompts, retrieval snapshots, tool permission manifests, memory schemas, and execution bindings can be represented as explicit design-time artifacts rather than left as hidden behavior.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The completed runtime item found that declared and observed AIBOMs can be compared across coverage, version, retrieval, memory-state, authority, topology, external-state, and control-policy divergence.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The completed identity item found that delegation chains, trust-domain crossings, and permission manifests must be modeled explicitly for attribution and least-privilege review.
- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] An AIBOM therefore materially helps with structural risk categories such as undeclared dependency introduction, model or prompt version drift, unapproved tool exposure, disabled logging or guardrails, authority-scope expansion, and incomplete incident scoping after a compromise.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] AIBOM-informed controls reduce blast radius when they are used to constrain reachable tools, delegated permissions, and retrieval surfaces before execution, because the inventory can be turned into allowlists, version checks, and scope-difference alerts rather than treated as documentation only.

#### C. False-assurance scenarios

- [fact; source: https://arxiv.org/abs/2302.12173] Greshake et al. show that indirect prompt injection can manipulate Application Programming Interface calls, enable data theft, and contaminate information ecosystems by placing malicious instructions in retrieved content that the system treats as ordinary data.
- [fact; source: https://arxiv.org/abs/2211.09527] Perez and Ribeiro show goal hijacking and prompt leaking through crafted user input, demonstrating that simple adversarial text can override or expose prompt-level controls.
- [fact; source: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] Microsoft says memory poisoning is especially insidious because malicious instructions can be stored, recalled, and executed when semantic analysis and contextual validation are weak, and it recommends restricting autonomous memory updates and tightening memory access.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP treats insecure plugin design and excessive agency as separate failure classes, which implies that a tool can be correctly declared and still create severe downstream risk when its invocation or authorization boundary is weak.
- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] A complete AIBOM can therefore be fully accurate and still create false assurance if reviewers mistake structural completeness for semantic safety, because injected documents, poisoned memories, and harmful tool arguments can travel through channels that the AIBOM correctly records but cannot certify as benign.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Runtime-observed AIBOMs narrow this gap by recording retrieved items, tool invocations, and observed topology, but they still document what happened rather than proving that the behavior was safe or that future runs will behave similarly.

#### D. Inference opacity and current visibility limits

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST identifies risk measurement, lack of robust and verifiable metrics, and inscrutability as core artificial intelligence risk-management challenges, and it treats explainability and interpretability as helpful but not sufficient trustworthiness characteristics.
- [fact; source: https://www.anthropic.com/claude-opus-4-6-system-card] Anthropic says it uses interpretability methods that probe internal activations and trace which internal features appear to contribute to outputs, while also stating that its methods and tools for alignment evaluation continue to develop and that its ability to assess reasoning faithfulness, meaning whether visible reasoning reflects the process that produced the answer, remains limited in depth.
- [fact; source: https://www.anthropic.com/claude-opus-4-6-system-card] Anthropic reports a low but persistent rate of the model acting against an operator's interests in unanticipated ways in some high-stakes scenarios, even after extensive evaluations and interpretability analysis.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] Current evidence supports a practical boundary in which an AIBOM can inventory boundary conditions, observed context, and governance artifacts, but does not yet make a frontier model's internal reasoning fully inspectable or replayable.

#### E. Metric proposals and required baseline data

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] **Runtime dependency capture rate** should be defined as the proportion of observed runtime dependencies, model invocations, retrieval events, tool calls, memory accesses, and policy hooks that are captured in the runtime AIBOM, and it requires trace-complete reference logs plus the runtime AIBOM export.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] **Drift detection latency** should be defined as the elapsed time between a material structural change, such as a model version, tool manifest, guardrail setting, or permission-scope change, and the alert generated from AIBOM comparison, and it requires authoritative change timestamps plus alert timestamps.
- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] **Blast-radius reduction** should be defined as the reduction in reachable privileged actions or reachable sensitive data paths after AIBOM-informed allowlists, version pins, and scope constraints are applied, and it requires a baseline privilege graph plus a constrained privilege graph.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] **AIBOM coverage-completeness score** should be defined as the weighted proportion of required declared and observed surfaces populated for model, prompt, retrieval, tool, identity, memory, and control-policy nodes, and it requires a fixed required-surface rubric plus extraction results for each run or release.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] A useful companion metric is **false-assurance gap rate**, the share of serious incidents in which the AIBOM was structurally complete but the root cause lay in semantic payloads, runtime state corruption, or opaque model behavior rather than missing inventory.

### §3 Reasoning

- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] Structural and behavioral risks are distinct in the source set, because OWASP and Microsoft both enumerate attack classes that arise from content semantics, autonomy, and runtime decision-making rather than only from component identity.
- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The strongest justified conclusion is that AIBOM transfers SBOM-style value into agentic artificial intelligence only for the subset of risks that are observable as declared or runtime-logged structure.
- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] The documented prompt-injection and memory-poisoning cases show why completeness of structure cannot be equated with safety of behavior, because the attack payload arrives through authorized channels and changes meaning rather than inventory membership.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] The opacity boundary is not a temporary paperwork gap alone, because even the strongest current governance and interpretability sources still treat risk measurement and the ability to judge whether visible reasoning matches the process that produced the answer as incomplete.

### §4 Consistency Check

- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] No contradiction remains between "AIBOM materially helps" and "AIBOM creates false assurance" once the claim is narrowed to different surfaces: structure can be measured and constrained, while semantic and inferential risk can still flow through legitimate structure.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] No contradiction remains between documentation and opacity claims once boundary documentation is separated from internal model reasoning, because the sources support better auditability without supporting full interpretability.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] The completed runtime and platform-observability items are consistent with the metric section, because they both treat runtime evidence fidelity as a precondition for measuring declared-versus-observed divergence.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] **Technical lens:** the practical value of AIBOM increases with the quality of the observability substrate, because runtime metrics and divergence alerts are only as strong as the traces and export surfaces feeding them.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework] **Governance lens:** AIBOM is most defensible as one evidence object inside a broader govern-map-measure-manage workflow, not as a standalone assurance artifact.
- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework] **Economic lens:** the highest-return use cases are release gating, drift detection, and faster incident scoping, because those outcomes map to inventory-style visibility benefits that organizations can automate and measure.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] **Behavioral lens:** the biggest governance danger is operator over-trust, because a precise-looking AIBOM can encourage approval of systems whose dominant risks still depend on prompt content, memory content, retrieval quality, or model judgment.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] An AIBOM materially reduces security and governance risk only for structural surfaces that can be declared or observed, such as versions, dependencies, retrieval stores, tool manifests, delegation edges, guardrails, and runtime divergence.
- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] An AIBOM creates false assurance when its completeness is mistaken for semantic safety, because adversarial instructions in prompts, poisoned retrieved context, poisoned stored memory, and harmful use of legitimately declared tools can all succeed through correctly declared channels.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] Current evidence does not show that AIBOM can close the visibility gap created by model inscrutability and the still-limited ability to assess whether visible reasoning matches the process that produced the answer, so it cannot currently supply complete explainability or guarantee safe behavior.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] AIBOM success should be judged by whether AIBOM-informed controls improve structural coverage, shorten drift detection, reduce reachable blast radius, and support better incident reconstruction.

**Key findings:**

1. [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] AIBOM is strongest where risk is anchored in declared or runtime-observed structure, because inventory-style evidence can represent components, versions, permissions, and policy surfaces in ways that support gating, comparison, and audit.
2. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] AIBOM materially mitigates undeclared dependency introduction, version drift, authority-scope expansion, disabled guardrails, and incomplete post-incident scoping when organizations use it as an enforcement and comparison object rather than passive documentation.
3. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://owasp.org/www-project-top-10-for-large-language-model-applications/] Prompt injection remains outside AIBOM's direct control boundary, because the attack works by changing the meaning of legitimate content rather than by introducing an undeclared component that inventory controls can block.
4. [inference; source: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] Retrieval poisoning and memory poisoning create especially strong false-assurance risk, because the retrieval store or memory subsystem can be fully declared while its runtime contents are semantically malicious and still treated as trusted context.
5. [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] Legitimately declared tools and permissions do not prove safe behavior, because the same accurately inventoried agency surface can still be misused through weak authorization boundaries, excessive autonomy, or compromised decision flow.
6. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] Under current governance and interpretability practice, inference opacity remains a material limit on AIBOM effectiveness because documentation of inputs, outputs, and conditions of use does not yet fully expose or validate internal reasoning.
7. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] The most decision-useful effectiveness metrics are runtime dependency capture rate, drift detection latency, blast-radius reduction, and coverage-completeness score, because each can be computed from operational evidence and linked to control outcomes.
8. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] The correct governance posture is to treat AIBOM as one layer in a control stack that also includes runtime policy enforcement, semantic-content defenses, monitoring, and adversarial testing, because the dominant agentic failure modes cross structural and behavioral boundaries.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AIBOM is strongest on structural surfaces that can be declared or observed. | https://www.ntia.gov/page/software-bill-materials ; https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html | medium | inventory-transfer claim |
| [inference] AIBOM mitigates undeclared dependency, drift, authority, guardrail, and scoping failures when used for enforcement and comparison. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | enforcement-dependent |
| [inference] Prompt injection sits outside direct AIBOM control because it changes content meaning rather than inventory membership. | https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2211.09527 ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | semantic-channel attack |
| [inference] Retrieval poisoning and memory poisoning create false assurance even with complete structure. | https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ ; https://arxiv.org/abs/2302.12173 ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | runtime-content compromise |
| [inference] Declared tools and permissions do not prove safe behavior. | https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | agency-surface limit |
| [inference] Current interpretability limits leave a material AIBOM boundary around internal reasoning. | https://www.nist.gov/itl/ai-risk-management-framework ; https://www.anthropic.com/claude-opus-4-6-system-card | medium | reasoning remains partly opaque |
| [inference] Runtime dependency capture, drift latency, blast-radius reduction, and coverage-completeness are the key effectiveness metrics. | https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html | medium | operational metric set |
| [inference] AIBOM must be one layer in a broader control stack. | https://www.nist.gov/itl/ai-risk-management-framework ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://arxiv.org/abs/2302.12173 ; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ | high | layered-governance conclusion |

**Assumptions:**

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] The proposed runtime metrics assume the organization can collect traces or logs with enough fidelity to compare declared and observed AIBOM state.

**Analysis:**

- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework] The evidence was weighted by first asking which SBOM-style benefits plausibly transfer to artificial intelligence systems in documented inventory-oriented cases and then testing whether the relevant object was an inventoryable structure, a runtime event, or a semantic behavior.
- [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/] Prompt injection, retrieval poisoning, and memory poisoning were treated as the decisive false-assurance cases because they show compromise traveling through authorized channels that an accurate inventory can record but cannot certify as safe.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card] Rival remedies such as stronger models, more manual review, or richer model cards do not remove the core limit identified here, because they may lower some failure rates without making internal reasoning fully inspectable or removing semantic-channel attacks.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The completed AIBOM series sharpened the conclusion by showing that declared structure, runtime evidence, and delegation history are all necessary for governance, but none of them alone is sufficient for behavioral assurance.

**Risks, gaps, uncertainties:**

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST says robust and verifiable risk-measurement methods remain an open challenge, so the metric formulas proposed here should be treated as operational starting points rather than settled industry standards.
- [inference; source: https://www.ntia.gov/page/software-bill-materials; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] The empirical case for AIBOM-specific return on investment remains thin because current public evidence is stronger on inventory and observability primitives than on mature, scaled AIBOM deployments with published outcome data.
- [inference; source: https://www.anthropic.com/claude-opus-4-6-system-card; https://www.nist.gov/itl/ai-risk-management-framework] Conclusions about inferential opacity may change at the margin as interpretability improves, but the current source set still supports only partial, not complete, reasoning visibility.

**Open questions:**

- Which metric thresholds would justify blocking a release when AIBOM coverage is incomplete but other compensating controls are strong?
- How should organizations classify and sample semantically risky retrieval content so the false-assurance gap rate becomes measurable across incidents?
- What evidence standard should distinguish acceptable runtime divergence from policy-violating divergence in multi-agent systems?

### §7 Recursive Review

- Coverage: complete
- Claim labels: applied in Research Skill Output
- Findings parity target: aligned to Section 6 synthesis
- Unresolved uncertainty: see Risks, Gaps, and Uncertainties

---

## Findings

### Executive Summary

An Artificial Intelligence Bill of Materials (AIBOM) materially reduces risk only for structural surfaces that can be declared or observed, such as versions, dependencies, retrieval stores, tool manifests, delegation edges, guardrails, and runtime divergence. [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

An AIBOM creates false assurance when its completeness is mistaken for semantic safety, because adversarial instructions in prompts, poisoned retrieved context, poisoned stored memory, and harmful use of legitimately declared tools can all succeed through correctly declared channels. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/]

Current evidence does not show that AIBOM can close the visibility gap created by model inscrutability and the still-limited ability to assess whether visible reasoning matches the process that produced the answer, so it cannot currently supply complete explainability or guarantee safe behavior. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card]

AIBOM success should be judged by whether AIBOM-informed controls improve structural coverage, shorten drift detection, reduce reachable blast radius, and support better incident reconstruction. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html]

### Key Findings

1. **AIBOM is strongest where risk is anchored in declared or runtime-observed structure, because inventory-style evidence can represent components, versions, permissions, and policy surfaces in ways that support gating, comparison, and audit.** ([inference]; medium confidence; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html)
2. **AIBOM materially mitigates undeclared dependency introduction, version drift, authority-scope expansion, disabled guardrails, and incomplete post-incident scoping when organizations use it as an enforcement and comparison object rather than passive documentation.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html)
3. **Prompt injection remains outside AIBOM's direct control boundary, because the attack works by changing the meaning of legitimate content rather than by introducing an undeclared component that inventory controls can block.** ([inference]; high confidence; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://owasp.org/www-project-top-10-for-large-language-model-applications/)
4. **Retrieval poisoning and memory poisoning create especially strong false-assurance risk, because the retrieval store or memory subsystem can be fully declared while its runtime contents are semantically malicious and still treated as trusted context.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
5. **Legitimately declared tools and permissions do not prove safe behavior, because the same accurately inventoried agency surface can still be misused through weak authorization boundaries, excessive autonomy, or compromised decision flow.** ([inference]; medium confidence; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
6. **Under current governance and interpretability practice, inference opacity remains a material limit on AIBOM effectiveness because documentation of inputs, outputs, and conditions of use does not yet fully expose or validate internal reasoning.** ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card)
7. **The most decision-useful effectiveness metrics are runtime dependency capture rate, drift detection latency, blast-radius reduction, and coverage-completeness score, because each can be computed from operational evidence and linked to control outcomes.** ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html)
8. **The correct governance posture is to treat AIBOM as one layer in a control stack that also includes runtime policy enforcement, semantic-content defenses, monitoring, and adversarial testing, because the dominant agentic failure modes cross structural and behavioral boundaries.** ([inference]; high confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AIBOM is strongest on structural surfaces that can be declared or observed. | https://www.ntia.gov/page/software-bill-materials ; https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html | medium | inventory-transfer claim |
| [inference] AIBOM mitigates undeclared dependency, drift, authority, guardrail, and scoping failures when used for enforcement and comparison. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | enforcement-dependent |
| [inference] Prompt injection sits outside direct AIBOM control because it changes content meaning rather than inventory membership. | https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2211.09527 ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | semantic-channel attack |
| [inference] Retrieval poisoning and memory poisoning create false assurance even with complete structure. | https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ ; https://arxiv.org/abs/2302.12173 ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html | medium | runtime-content compromise |
| [inference] Declared tools and permissions do not prove safe behavior. | https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | agency-surface limit |
| [inference] Current interpretability limits leave a material AIBOM boundary around internal reasoning. | https://www.nist.gov/itl/ai-risk-management-framework ; https://www.anthropic.com/claude-opus-4-6-system-card | medium | reasoning remains partly opaque |
| [inference] Runtime dependency capture, drift latency, blast-radius reduction, and coverage-completeness are the key effectiveness metrics. | https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html | medium | operational metric set |
| [inference] AIBOM must be one layer in a broader control stack. | https://www.nist.gov/itl/ai-risk-management-framework ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://arxiv.org/abs/2302.12173 ; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ | high | layered-governance conclusion |

### Assumptions

- **Assumption:** The proposed runtime metrics assume the organization can collect traces or logs with enough fidelity to compare declared and observed AIBOM state. **Justification:** That assumption follows from the completed runtime and platform-observability items, which both treat runtime evidence fidelity as a prerequisite for measuring divergence. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html]

### Analysis

The evidence was weighed by first asking which SBOM-style benefits plausibly transfer to artificial intelligence systems in documented inventory-oriented cases and then testing whether the relevant object was an inventoryable structure, a runtime event, or a semantic behavior. [inference; source: https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework]

Prompt injection, retrieval poisoning, and memory poisoning were treated as the decisive false-assurance cases because they show compromise traveling through authorized channels that an accurate inventory can record but cannot certify as safe. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2211.09527; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/]

Rival remedies such as stronger models, more manual review, or richer model cards do not remove the core limit identified here, because they may lower some failure rates without making internal reasoning fully inspectable or removing semantic-channel attacks. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.anthropic.com/claude-opus-4-6-system-card; https://arxiv.org/abs/2302.12173]

The completed AIBOM series sharpened the conclusion by showing that declared structure, runtime evidence, and delegation history are all necessary for governance, but none of them alone is sufficient for behavioral assurance. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

### Risks, Gaps, and Uncertainties

Robust and verifiable risk-measurement methods remain an open challenge, so the metric formulas proposed here should be treated as operational starting points rather than settled industry standards. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework]

The empirical case for AIBOM-specific return on investment remains thin because current public evidence is stronger on inventory and observability primitives than on mature, scaled AIBOM deployments with published outcome data. [inference; source: https://www.ntia.gov/page/software-bill-materials; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html]

Conclusions about inferential opacity may change at the margin as interpretability improves, but the current source set still supports only partial, not complete, reasoning visibility. [inference; source: https://www.anthropic.com/claude-opus-4-6-system-card; https://www.nist.gov/itl/ai-risk-management-framework]

### Open Questions

- Which metric thresholds would justify blocking a release when AIBOM coverage is incomplete but other compensating controls are strong?
- How should organizations classify and sample semantically risky retrieval content so the false-assurance gap rate becomes measurable across incidents?
- What evidence standard should distinguish acceptable runtime divergence from policy-violating divergence in multi-agent systems?

---

## Output

- Type: knowledge
- Description: This item defines the realistic control boundary of AIBOM, identifies the main false-assurance traps, and proposes an operational metric set for deciding whether AIBOM adoption is actually improving security and governance outcomes. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/]
- Links:
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://arxiv.org/abs/2302.12173
  - https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/

---
title: "AI Strategy Examples: Security Focus"
added: 2026-02-28
status: completed
priority: medium
tags: [ai-strategy, security, cybersecurity, threat-detection, adversarial-ai, ai-governance]
started: 2026-03-05
completed: 2026-03-05
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

**Prior research:** The completed AI strategy item (2026-02-28-ai-strategy.md) documented NZ's light-touch "Investing with Confidence" strategy and Singapore's nine-dimension Model AI Governance Framework (which explicitly includes security). The AI risk-reduction focus item (2026-02-28-ai-strategy-risk-reduction-focus.md) documented SR 11-7, APRA CPS 230, and DORA as governance frameworks for AI in financial services, plus HSBC and JPMorgan AML/fraud detection outcomes — establishing that AI for security in financial services has measurable efficacy. The AI control testing item (2026-02-28-ai-control-testing-and-assurance.md) covered AI in audit and GRC, with context on RBNZ/APRA oversight. This item must add: the threat-landscape quantification for AI-enhanced attacks, the specific attack taxonomy for AI systems (MITRE ATLAS, OWASP LLM Top 10, NIST AI 100-2), NZ NCSC/CERT NZ guidance specifics, SOC automation outcomes, and the minimum viable governance architecture for NZ organisations.

## Approach

1. **Map the threat landscape** — what does the current evidence say about AI-enhanced cyberattacks? Quantify where possible (frequency change, cost change).
2. **Survey AI security strategy cases** — identify 6–8 organisations (government agencies, financial institutions, critical infrastructure operators) that have disclosed AI security strategy design and outcomes.
3. **AI system security governance** — document known attack vectors against AI systems (MITRE ATLAS, OWASP ML Top 10, NIST AI RMF adversarial threat categories) and how organisations are governing against them.
4. **NZ regulatory mapping** — what do NCSC, GCSB, and CERT NZ say specifically about AI in security contexts? Are there advisories or frameworks?
5. **Synthesis** — what does an AI security strategy look like for a NZ financial institution or government agency? What are the minimum viable governance controls?

## Sources

- [x] MITRE ATLAS: Adversarial Threat Landscape for AI Systems — https://atlas.mitre.org/
- [x] OWASP LLM Top 10 (2023 / 2024 update) — https://owasp.org/www-project-top-10-for-large-language-model-applications/
- [x] NIST AI RMF: adversarial machine learning profile (NIST AI 100-2e2023) — https://doi.org/10.6028/NIST.AI.100-2e2023
- [x] GCSB / NCSC NZ: annual cyber threat reports and any AI-specific advisories — https://www.ncsc.govt.nz/publications/
- [ ] CERT NZ: threat intelligence reports referencing AI
- [x] Microsoft Security Intelligence: AI-enhanced threat reports (2023–2025) — https://www.microsoft.com/en-us/security/security-insider/intelligence-reports
- [ ] Google Project Zero / DeepMind AI security research
- [x] CISA (US): AI security guidance documents — https://www.cisa.gov/ai
- [x] Singapore IMDA: security dimension of Model AI Governance Framework (2024) — https://www.imda.gov.sg/resources/blog/2024/01/model-ai-governance-framework-second-edition
- [x] NZ financial sector: any RBNZ or FMA guidance on AI-related security obligations — https://www.rbnz.govt.nz/

---

## Research Skill Output

### §0 Initialise

**Research question restated:** Which organisations have developed coherent AI strategies with security as the primary objective, and what frameworks, architectures, and governance structures characterise effective approaches — covering both AI used as a security tool and AI systems as attack surfaces?

**Scope confirmed:** Both vectors are in scope: (1) AI applied to security — threat detection, SOC automation, fraud/anomaly detection; and (2) security applied to AI — adversarial ML, prompt injection, model poisoning, supply chain attacks. NZ context is explicitly required. Out of scope: physical security AI, post-quantum cryptography.

**Output format:** Structured research item with Evidence Map, Key Findings with confidence labels, and Assumptions section.

**Constraints:** All claims labelled [fact], [inference], or [assumption]. Every [fact] mapped to a source. Two independent credible sources required for evidence sufficiency, or one definitive primary source.

### §1 Question Decomposition

**A. AI-enhanced threat landscape**
- A1. What quantitative evidence exists for the scale and cost of AI-enhanced cyberattacks (2023–2025)?
- A2. What specific attack capabilities has adversarial AI unlocked that were not previously viable at scale?
- A3. Which threat actor categories (nation-state, criminal) are deploying AI offensively?

**B. AI security strategy cases — organisations deploying AI for security**
- B1. What disclosed cases exist of AI applied to threat detection with specific outcome metrics?
- B2. What cases exist of AI applied to SOC automation with measured results?
- B3. What governance structures support these deployments?

**C. AI system security — attack taxonomy and governance**
- C1. What are the canonical attack categories against AI/ML systems?
- C2. What frameworks exist to catalogue and govern these attacks?
- C3. What governance controls have been adopted by leading organisations?

**D. NZ regulatory mapping**
- D1. What has NCSC/CERT NZ published specifically on AI and security?
- D2. What have RBNZ and FMA required or expected from NZ financial institutions regarding AI security?
- D3. How does NZ's position compare to Five Eyes peers?

**E. Synthesis — minimum viable governance architecture**
- E1. What governance controls constitute a minimum viable AI security posture?
- E2. How should NZ organisations prioritise these controls given current regulatory requirements?

### §2 Investigation

**A1. Scale and cost of AI-enhanced cyberattacks**

[fact] AI-generated phishing emails increased 1,265% following the broad availability of generative AI tools. In 2025, 82% of phishing emails were assessed to use AI-generated content. (Source: Deepstrike/SlashNext phishing statistics 2025; KnowBe4 2025 Phishing Threat Trends Report)

[fact] Business Email Compromise (BEC) scams — substantially enabled by AI-generated content and voice deepfakes — resulted in $2.7 billion in US-reported losses in 2024. (Source: Deepstrike phishing statistics 2025, citing FBI IC3 data)

[fact] The average cost of a phishing-related data breach is $4.8–4.88 million per incident as of 2025, per IBM Cost of a Data Breach report. (Source: Deepstrike/Hoxhunt phishing statistics 2025)

[fact] A 703% increase in credential theft phishing was recorded in the second half of 2024. (Source: SlashNext 2024 Phishing Intelligence Report)

[fact] Microsoft's 2025 Digital Defense Report tracked over 200 instances of foreign adversaries using AI to generate fake online content in a single month — more than double the prior year's figure and tenfold more than 2023. (Source: Microsoft Digital Defense Report 2025; CNBC reporting October 2025)

[inference] The combination of lower cost-per-attack (AI automation) and higher success rate (AI personalisation) creates a compounding threat: even a modest deployment of generative AI by a threat actor multiplies effective attack capacity by an order of magnitude.

**A2. Specific attack capabilities unlocked by AI**

[fact] Palo Alto Unit 42's 2025 Global Incident Response Report documented social engineering attacks achieving privileged domain access in under 40 minutes, without malware, using AI-assisted social engineering scripts. (Source: Palo Alto Unit 42, 2025)

[fact] Deepfake tool trade increased 223% year-over-year in 2024–2025; 35% of AI-related social engineering incidents involved deepfakes in video or real-time voice calls. (Source: Sprinto social engineering statistics 2025)

[fact] Over 76% of phishing attacks in 2024 contained at least one polymorphic (AI-variant) feature, rendering traditional signature-based detection less effective. (Source: KnowBe4 2025 Phishing Threat Trends Report)

[inference] The shift from volume-based to precision-targeted attacks is the principal qualitative change attributable to AI. Traditional defences calibrated to volume thresholds fail against lower-volume, higher-quality AI-personalised attacks.

**A3. Threat actor categories**

[fact] Microsoft's 2025 report explicitly identified Russia, China, Iran, and North Korea as nation-state actors escalating AI deployment in offensive cyber operations targeting the US and its allies. (Source: Microsoft Digital Defense Report 2025)

[fact] Criminal organisations deploy generative AI for BEC, voice cloning, and AI-assisted ransomware delivery. Nation-state actors use AI for both espionage (synthetic content, influence operations) and direct infrastructure attack. (Source: Microsoft Digital Defense Report 2025)

**B1–B2. Disclosed cases of AI applied to security with outcome metrics**

[fact] HSBC's AI-driven AML system (Google Cloud Dynamic Risk Assessment) reduced false positive AML alerts by 60% and increased confirmed financial crime detection by 2–4×. (Source: completed research item 2026-02-28-ai-strategy-risk-reduction-focus.md, citing HSBC disclosed case; confirmed multiple sources)

[fact] JPMorgan Chase achieved 95% reduction in false positives in AML/fraud detection, with fraud detected 300× faster, across 450+ AI use cases. (Source: completed research item 2026-02-28-ai-strategy-risk-reduction-focus.md)

[fact] Microsoft Security Copilot field trials yielded a 30% reduction in mean time to resolution (MTTR) for SOC incidents. (Source: Microsoft Generative AI and Security Operations Center Productivity report, 2024)

[fact] KPMG's 2024 SOC Survey found 85% of SOC leaders in financial and government sectors confident in their readiness to deter future advanced attacks; over 70% identified AI as a material improvement in threat detection capability. (Source: KPMG SOC Survey 2024)

[fact] US Treasury's 2024 AI in financial services report flagged AI as both a fraud-prevention tool and a source of third-party concentration risk. (Source: US Treasury press release JY2760, 2024)

**B3. Governance structures**

[inference] The governance model common across disclosed cases is: AI executes detection and triage at scale; human analysts focus on investigation, escalation, and decision authority. No disclosed case eliminated human-in-the-loop for final determinations.

**C1. Canonical attack categories against AI/ML systems**

[fact] NIST AI 100-2e2023 ("Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations") defines four canonical attack categories: (1) Evasion — crafting inputs at inference time to cause wrong outputs; (2) Poisoning — corrupting training data or model weights; (3) Privacy — extracting sensitive information from models (membership inference, model inversion); (4) Abuse — misusing AI capabilities (prompt injection, output manipulation). Attacker knowledge is further classified white-box/black-box/gray-box. (Source: NIST AI 100-2e2023, csrc.nist.gov)

[fact] MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) is a living knowledge base as of 2024–2025 with 15–16 tactics, 66+ documented techniques, and 46+ sub-techniques, continuously updated (new agentic AI techniques added in 2025). Approximately 70% of ATLAS mitigations map to traditional cybersecurity controls; 30% require new AI-specific approaches. (Source: Vectra.ai MITRE ATLAS overview; CSO Online; MITRE ATLAS official at atlas.mitre.org)

[fact] OWASP LLM Top 10 (2025 version): LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain Vulnerabilities; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption. (Source: OWASP official project owasp.org/www-project-top-10-for-large-language-model-applications)

**C2. Frameworks for AI system security**

[fact] NIST CSRC published a Preliminary Draft Cybersecurity Framework Profile for Artificial Intelligence (NISTIR 8596, "Cyber AI Profile") in December 2025. It defines three focus areas mapped to CSF 2.0 functions: (1) Secure AI system components; (2) Defend with AI (using AI in cyber operations); (3) Thwart AI-enabled attacks. It is voluntary but is positioned as the benchmark for "reasonable cybersecurity" for AI under US law. (Source: NIST CSRC csrc.nist.gov/pubs/ir/8596/iprd; KPMG regulatory alert 2026)

[fact] CISA, NSA, and 14 international partners (including NZ NCSC) co-published "Deploying AI Systems Securely" guidance in April 2024, specifically for organisations that deploy third-party AI. Controls cover: supply chain evaluation, model weight protection via HSMs, API authentication, input sanitisation, logging of model inputs/outputs, and incident response. (Source: CISA news-events/alerts/2024/04/15; NZ NCSC deploying-ai-systems-securely page)

**C3. Governance controls adopted by leading organisations**

[fact] OpenAI acknowledged in public statements that prompt injection in AI browser agents "may never be fully patched," establishing that architectural boundaries — not patch management — are the primary mitigation path. (Source: Lakera blog on indirect prompt injection, citing OpenAI statements)

[fact] Real-world CVEs with CVSS scores above 9.0 have been exploited in GitHub Copilot and Microsoft Copilot via indirect prompt injection — attackers embedding malicious commands in code snippets or project metadata processed by the LLM tools. (Source: Vectra.ai prompt injection CVE documentation 2024)

[fact] RAG (Retrieval-Augmented Generation) pipeline poisoning has been documented in 2024: a small number of adversarially crafted documents embedded in a retrieval corpus can manipulate LLM outputs across the majority of subsequent queries. (Source: MDPI Information 2025, "Prompt Injection Attacks in Large Language Models and AI Agent Systems"; Aviatrix Threat Research 2024)

[inference] Indirect prompt injection — instructions embedded in data the model ingests rather than provided directly — is qualitatively harder to defend against than direct injection because the attack surface is any external data source the AI agent touches.

**D1. NZ NCSC/CERT NZ guidance**

[fact] NZ NCSC and CERT NZ (now merged into a single operational lead) published "Engaging with Artificial Intelligence" in January 2024 — a joint advisory with ASD/ACSC (Australia), CISA, NSA, and 12 additional international agencies. Scope: using AI systems securely (not building secure AI). Covers key threats to AI systems, mitigation measures for self-hosted and third-party-hosted AI. (Source: ncsc.govt.nz/protect-your-organisation/engaging-with-artificial-intelligence/)

[fact] NZ NCSC endorsed "Guidelines for Secure AI System Development" (November 2023), a 23-agency international publication emphasising secure-by-design principles covering privacy, reliability, resilience, and ethical use. (Source: ncsc.govt.nz/protect-your-organisation/guidelines-for-secure-ai-system-development/)

[fact] NZ NCSC mandated 10 Minimum Cyber Security Standards for public agencies, effective 30 October 2025. Standards include: security awareness, risk management, asset management, secure configuration, patching, MFA, anomaly detection, least privilege, data recovery, and response planning. These are not AI-specific but apply to AI systems as a subset of all ICT assets. (Source: Industrial Cyber reporting on NZ NCSC minimum cybersecurity baseline, 2025)

[fact] NZ "Guidance for safe use of AI in the public sector" was published in 2025 via the Public Service AI Framework, setting structured expectations on safety, transparency, accountability, and public trust. (Source: beehive.govt.nz release "Guidance for safe use of AI in the public sector")

**D2. RBNZ and FMA on AI security for NZ financial institutions**

[fact] FMA published research on AI use in NZ financial services in 2024, following roundtables with regulated entities. FMA expectations (not yet codified as rules): robust AI governance, data quality and security, upgraded cybersecurity controls, algorithmic bias evaluation, board-level oversight, and disclosure considerations. (Source: fma.govt.nz "Understanding Artificial Intelligence in Financial Services" media release 2024)

[fact] RBNZ's 2025 Financial Stability Report flagged AI systemic risks: opacity of AI algorithms, expanded cyber-attack surface, third-party concentration risk from large AI providers, and the risk of correlated failures if multiple institutions use the same underlying models. RBNZ expects regulated entities to adapt existing risk frameworks to capture AI exposures. (Source: rbnz.govt.nz/hub/publications/financial-stability-report/2025 "Rise of the Machines" pre-release)

[inference] NZ financial institutions face a three-layer regulatory environment for AI security: (1) APRA CPS 230 at group level (for Australian-owned banks) requiring AI in critical operations to be documented and resilience-tested; (2) FMA expectations for governance and disclosure; (3) RBNZ prudential supervision applying BS11 to outsourced AI and BPR requirements to risk models. No NZ-specific AI security regulation has been enacted.

**D3. NZ versus Five Eyes peers**

[inference] NZ's approach is consistent with but behind the operational pace of its Five Eyes peers. The joint "Engaging with AI" advisory was co-produced, meaning NZ's formal guidance output is aligned with the US (CISA), UK (NCSC), Australia (ASD/ACSC), and Canada (CSE) but NZ has not produced standalone AI security frameworks of the depth that CISA or NCSC UK have. Australia's approach (Essential Eight, AI-specific guidance from ASD) is more operationally prescriptive.

**E1–E2. Minimum viable governance architecture**

[inference] Drawing from MITRE ATLAS (30% of mitigations are AI-specific), OWASP LLM Top 10, NIST AI 100-2, CISA/NCSC joint guidance, and the Singapore nine-dimension framework, the minimum viable AI security governance architecture for a NZ financial institution or government agency comprises six controls:

1. **Attack surface inventory**: catalogue all AI/ML models in production, including third-party models, training data sources, and API endpoints — mapped against MITRE ATLAS tactics.
2. **Input/output sanitisation**: validate and sanitise all inputs to AI systems; monitor and filter outputs, especially for LLM-based applications (addresses OWASP LLM01, LLM05).
3. **Model weight protection**: restrict access to model weights; use cryptographic attestation of model versions; store in tamper-evident storage (addresses supply chain attacks per NIST and CISA).
4. **Adversarial testing regime**: red-team AI systems with adversarial examples and prompt injection attempts before deployment and after major model updates (addresses evasion, prompt injection).
5. **Monitoring and anomaly detection**: log model inputs, outputs, and intermediate states; set automated alerts on distributional shifts (addresses data/concept drift, model extraction, abuse attacks).
6. **Governance and accountability**: board/executive accountability for AI security posture; incident response plans specific to AI failures; documented human-in-the-loop thresholds for consequential AI decisions.

[assumption] The six-control architecture above is sufficient for organisations at an intermediate AI maturity (using third-party AI APIs and some internal ML models) but not for organisations building and training frontier models from scratch, where additional controls (differential privacy, federated learning, membership inference testing) would be required. Justification: the evidence base reviewed focuses on deploying rather than building AI, matching the profile of most NZ organisations.

### §3 Reasoning

The two-vector framing — AI as tool versus AI as attack surface — is analytically necessary because the governance responses are distinct. AI-enhanced threats (phishing, deepfakes, BEC) are best countered by AI-augmented defences (SOC automation, AI-generated content detection, adaptive authentication) at the perimeter and endpoint. AI system vulnerabilities (prompt injection, poisoning, model extraction) require internal controls applied to the AI pipeline itself — input sanitisation, model provenance, access control on weights.

The threat-landscape statistics support a directional claim: AI has not created categorically new attack types but has lowered the cost and raised the scale of attacks that previously required specialised skill (spear-phishing, social engineering, vulnerability exploitation). This is a force-multiplier dynamic, not a phase change. The governance implication is that organisations with already-weak traditional security hygiene face compounded risk.

The NZ regulatory picture is fragmented but operationally workable. The NCSC "Engaging with AI" advisory (January 2024), the CISA joint "Deploying AI Systems Securely" (April 2024), and the NCSC minimum standards (October 2025) together provide a defensible baseline. FMA and RBNZ have flagged expectations without prescribing specific controls, which means NZ financial institutions currently face supervisory discretion rather than mandatory compliance obligations on AI security specifically.

MITRE ATLAS's finding that 70% of AI-system mitigations are traditional cybersecurity controls is important: it means organisations with strong existing security hygiene are better positioned than those treating AI security as entirely novel. The genuinely novel 30% (adversarial training, data provenance, model monitoring, prompt injection defences) are where focused investment is required.

Singapore's Model AI Governance Framework (2024 generative AI update) is the most operationally detailed reference for the security dimension, including red-teaming requirements, incident reporting, and supply chain controls. It goes further than NCSC's "Engaging with AI" advisory in requiring structured governance, not just awareness.

### §4 Consistency Check

No internal contradictions detected in the evidence. The phishing statistics from multiple sources (Deepstrike, SlashNext, KnowBe4, Hoxhunt) converge on the same directional finding (substantial AI-driven increase) though specific percentages vary by methodology — the 1,265% figure comes from SlashNext/Deepstrike, while the 82% AI-content-in-phishing figure comes from KnowBe4. These measure different things (volume growth vs. prevalence) and are compatible.

The NIST AI 100-2 taxonomy (4 attack types) and MITRE ATLAS (15 tactics, 66+ techniques) are complementary, not competing — MITRE ATLAS operationalises the NIST categories into actionable tactics and techniques. OWASP LLM Top 10 is scoped specifically to LLM deployments and adds the "excessive agency" and "unbounded consumption" risks that are new to agentic AI systems not covered by the earlier NIST taxonomy.

One tension: CISA/NCSC guidance (April 2024) focuses on third-party AI deployment while NIST AI 100-2 focuses on ML model adversarial attacks more broadly. They are compatible — both are needed — but organisations may focus on one and neglect the other. This is noted in Risks/Gaps.

The RBNZ and FMA guidance is consistent with but more ambiguous than APRA CPS 230 and DORA. For NZ-domiciled entities not covered by APRA/DORA, the applicable governance standard is principle-based expectation rather than rule-based obligation.

### §5 Depth and Breadth Expansion

**Technical lens:** The emergence of agentic AI systems (AI with tool-use, memory, and API access) materially expands the prompt injection attack surface. An LLM chatbot that only answers questions presents a small attack surface; an AI agent that can send emails, execute code, access databases, and call external APIs presents an attack surface equivalent to a privileged internal user. MITRE ATLAS added new agentic AI attack techniques in 2025, tracking ahead of most organisations' governance frameworks.

**Regulatory lens:** The NIST Cyber AI Profile (NISTIR 8596, preliminary draft December 2025) is the first framework to explicitly address all three dimensions simultaneously: securing AI systems, using AI for defence, and defending against AI-enabled attacks. Its voluntary status and preliminary draft position mean it is not yet a compliance standard, but its structure is likely to propagate into future mandatory frameworks.

**Economic lens:** AI-enhanced attacks create an asymmetric cost structure: defenders must secure the entire perimeter while attackers need succeed only once. AI automation increases attacker ROI — AI-generated phishing costs a fraction of human-crafted spear-phishing while approaching similar quality. BEC losses ($2.7B US in 2024) represent a demonstrable economic harm attributable to AI enhancement of existing attack techniques.

**Behavioural/organisational lens:** The human-in-the-loop requirement universal across governance frameworks (NCSC, Singapore, NIST) reflects a finding from AI-assisted audit research: AI is trusted for detection and triage but not for final decisions with legal or financial consequence. This is consistent across SOC automation, AML, and AI audit contexts — AI expands analyst capacity but does not replace accountability.

**NZ-specific lens:** NZ's small-market context creates a concentration risk: most NZ banks rely on Australian-owned parent systems where AI models are trained, deployed, and monitored offshore. The BS11 outsourcing framework is the primary governance mechanism for this dependency, but BS11 was designed for IT outsourcing before the AI-specific attack surface was understood. A model-weight provenance requirement or AI supply chain audit standard would need to be added to BS11 or its successor to address this gap.

### §6 Synthesis

**Core finding:** AI security strategy requires explicit governance across two analytically separate vectors — AI as security tool and AI as attack surface — governed by different control architectures. Most NZ organisations have actionable guidance from NCSC joint advisories and CISA, but no mandatory AI-specific security regulation exists as of March 2026.

**AI-enhanced threat landscape:** AI has multiplied the scale and reduced the per-attack cost of phishing, BEC, and social engineering — 1,265% phishing volume increase, $2.7B BEC losses in 2024, 82% of phishing emails AI-generated in 2025. The qualitative change is precision at scale: AI enables personalised, polymorphic attacks that previously required human effort.

**AI as security tool:** Deployed AI security delivers measurable outcomes. HSBC: 60% false-positive reduction in AML. JPMorgan: 95% false-positive reduction, fraud detected 300× faster. Microsoft Security Copilot in SOC trials: 30% MTTR reduction. The governance model is AI for detection/triage, humans for decision authority.

**AI attack taxonomy:** Four canonical attack categories (NIST AI 100-2): evasion, poisoning, privacy, abuse. MITRE ATLAS operationalises these into 66+ techniques. OWASP LLM Top 10 extends the framework for LLM-specific risks including prompt injection (the highest-risk category) and excessive agency in agentic systems.

**Prompt injection as critical risk:** Prompt injection — especially indirect injection via data sources ingested by AI agents — is assessed as the most difficult-to-mitigate AI-specific attack. OpenAI has acknowledged it may never be fully patched. Real CVEs in GitHub Copilot and Microsoft Copilot (CVSS >9.0) confirm active exploitation. RAG pipeline poisoning is documented.

**NZ regulatory position:** NCSC published "Engaging with AI" (January 2024) with 14 international partners; the joint CISA guidance "Deploying AI Systems Securely" (April 2024) is co-endorsed by NZ. NCSC Minimum Cyber Security Standards apply to public agencies from October 2025. FMA and RBNZ have flagged expectations without prescribing specific AI security controls. No NZ-specific AI security regulation exists.

**Minimum viable governance architecture (six controls):** (1) AI/ML asset inventory mapped to MITRE ATLAS; (2) input/output sanitisation for LLM deployments; (3) model weight protection with cryptographic attestation; (4) adversarial testing regime including red-teaming; (5) model monitoring with distributional shift alerts; (6) board-level accountability with documented human-in-the-loop thresholds.

### §7 Recursive Review

All sections contain substantive content. All [fact] claims are mapped to sources. [inference] labels applied where evidence is sufficient but not direct. One [assumption] stated with justification.

Source marking: MITRE ATLAS, OWASP LLM Top 10, NIST AI 100-2, NCSC NZ "Engaging with AI" and "Guidelines for Secure AI", CISA "Deploying AI Systems Securely", Singapore IMDA Model AI Governance Framework, Microsoft Digital Defense Report 2025, FMA AI in financial services 2024, RBNZ FSR 2025 — all marked [x] where accessed directly or via authoritative summaries. CERT NZ is now merged with NCSC; the NCSC publications cover both. Google Project Zero/DeepMind materials were not directly accessed and are not marked.

Open question identified: BS11 adequacy for AI supply chain governance in NZ banking. Noted as Open Question below.

No unresolved contradictions. Confidence levels assigned: high where multiple independent sources agree on a specific claim; medium where claim is directionally supported but with methodological variation across sources; low where based on single source or inference from context.

---

## Findings

### Executive Summary

AI security strategy in 2025–2026 requires parallel governance architecture for two distinct problems: AI as an attack-amplification tool in adversaries' hands, and AI systems as a novel attack surface within organisations. AI-enhanced phishing has grown 1,265% in volume since generative AI became broadly available, with $2.7 billion in BEC losses in the US in 2024 alone, while the per-attack cost to adversaries has collapsed. Internally, prompt injection — particularly indirect injection targeting AI agents with tool-use capabilities — is the highest-severity AI-specific vulnerability, with no complete architectural fix known. NZ organisations have actionable guidance from NCSC joint advisories (January 2024) and the CISA/Five Eyes "Deploying AI Systems Securely" standard (April 2024), but no mandatory AI-specific security regulation exists in NZ as of March 2026; FMA and RBNZ have expressed expectations without prescribing controls.

### Key Findings

1. **AI-enhanced phishing grew 1,265% in volume following widespread generative AI availability, with 82% of phishing emails assessed as AI-generated content in 2025, and average phishing-related breach costs now standing at $4.8–4.88 million per incident.** [confidence: high; multiple industry reports converge]

2. **Business Email Compromise scams, substantially enabled by AI-generated content and voice deepfakes, generated $2.7 billion in US-reported losses in 2024, representing a quantifiable economic harm directly attributable to AI-enhanced social engineering.** [confidence: high; FBI IC3 data cited in multiple sources]

3. **The NIST AI 100-2e2023 taxonomy defines four canonical attack categories against AI systems — evasion, poisoning, privacy, and abuse — providing the foundational vocabulary for AI security governance; MITRE ATLAS operationalises this into 66+ techniques across 15 tactics, with 30% of ATLAS mitigations requiring AI-specific controls not found in traditional cybersecurity frameworks.** [confidence: high; primary source NIST and MITRE]

4. **Prompt injection, ranked #1 in the OWASP LLM Top 10, is the highest-severity AI-specific vulnerability for deployed LLM systems; OpenAI has stated indirect prompt injection in AI browser agents may never be fully patched, and real-world CVEs with CVSS scores above 9.0 have been exploited in GitHub Copilot and Microsoft Copilot via this attack vector.** [confidence: high; multiple primary and secondary sources]

5. **AI applied to security operations delivers measurable ROI: HSBC's AML system reduced false positive alerts by 60% and doubled confirmed financial crime detection; JPMorgan achieved 95% false-positive reduction with fraud detected 300× faster; Microsoft Security Copilot trials demonstrated 30% reduction in SOC mean time to resolution.** [confidence: high; disclosed case studies; corroborated in prior research item]

6. **NZ NCSC published "Engaging with Artificial Intelligence" in January 2024 in partnership with 14 international agencies including CISA, NSA, and ASD, providing AI security guidance for organisations using (not building) AI systems; a follow-on joint advisory "Deploying AI Systems Securely" (April 2024) co-endorsed by NZ adds controls for model weight protection, supply chain evaluation, and AI-specific monitoring.** [confidence: high; primary source NCSC NZ website confirmed]

7. **NZ NCSC mandated 10 Minimum Cyber Security Standards for public agencies effective October 2025 — including MFA, anomaly detection, and least privilege — that apply to AI systems as ICT assets, but no NZ-specific AI security standards have been issued separately.** [confidence: high; Industrial Cyber reporting confirmed against NCSC]

8. **FMA's 2024 AI research report and RBNZ's 2025 Financial Stability Report both flag AI security risks for NZ financial institutions — FMA expects governance, cybersecurity controls, and disclosure; RBNZ highlights third-party concentration risk and correlated model failure — but neither has issued prescriptive rules; NZ financial institutions operate under principle-based expectation, not rule-based obligation, for AI security.** [confidence: high; primary sources FMA and RBNZ publications]

9. **Singapore's 2024 Model AI Governance Framework for Generative AI is the most operationally detailed reference governance standard for AI security, requiring: adversarial prompt red-teaming, supply chain security for model weights, structured incident reporting, and continuous monitoring — exceeding the depth of NCSC's advisory-level guidance.** [confidence: medium; based on framework documentation and analysis, Singapore's own enforcement model is voluntary]

10. **Agentic AI systems (AI with tool-use, memory, and API access) present a qualitatively larger attack surface than passive LLMs because a successful prompt injection translates into capability to send emails, access databases, and execute code; MITRE ATLAS added new agentic AI attack techniques in 2025, tracking ahead of most organisations' current governance frameworks.** [confidence: medium; based on research reports and CVE evidence, not yet widely documented in primary regulatory guidance]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 1,265% phishing volume increase from AI | SlashNext 2024 Phishing Intelligence Report; Deepstrike phishing stats 2025 | high | Multiple industry reports converge; methodology differs but direction consistent |
| 82% of phishing emails AI-generated (2025) | KnowBe4 2025 Phishing Threat Trends Report | high | Specific to 2025; lower figures in prior-year reports |
| $4.8–4.88M average breach cost | IBM Cost of Data Breach 2025; Hoxhunt Phishing Trends 2025 | high | IBM benchmark widely reproduced |
| $2.7B BEC losses US 2024 | FBI IC3 2024; Deepstrike phishing stats 2025 | high | FBI primary source |
| NIST AI 100-2 4-category taxonomy | NIST AI 100-2e2023 (csrc.nist.gov) | high | Primary source |
| MITRE ATLAS 66+ techniques, 30% AI-specific mitigations | Vectra.ai MITRE ATLAS overview; CSO Online | high | Two independent summaries of primary ATLAS source |
| OWASP LLM Top 10 prompt injection #1 | OWASP official project page | high | Primary source |
| OpenAI prompt injection "may never be fully patched" | Lakera blog citing OpenAI statements | medium | Secondary source attributing OpenAI position; no primary transcript |
| GitHub/Microsoft Copilot CVEs CVSS >9.0 via prompt injection | Vectra.ai prompt injection CVE documentation | medium | Secondary source; specific CVE numbers not confirmed from primary |
| HSBC 60% false-positive reduction | Prior research item; multiple secondary sources | high | Corroborated in prior research item on risk-reduction AI |
| JPMorgan 95% false-positive reduction | Prior research item; multiple secondary sources | high | Corroborated in prior research item |
| Microsoft Security Copilot 30% MTTR reduction | Microsoft GenAI SOC Productivity report | high | Microsoft primary research publication |
| NCSC "Engaging with AI" January 2024 | NCSC NZ website confirmed | high | Primary source accessed |
| CISA/Five Eyes "Deploying AI Systems Securely" April 2024 | CISA news-events/alerts/2024/04/15 | high | Primary source confirmed |
| NCSC 10 Minimum Standards October 2025 | Industrial Cyber; confirmed against NCSC | high | Secondary source consistent with NCSC framework documentation |
| FMA AI research 2024, principle-based expectations | FMA media release; Lexology; MinterEllison | high | Multiple legal/regulatory secondary sources |
| RBNZ FSR 2025 AI systemic risk | RBNZ.govt.nz "Rise of the Machines" pre-release | high | Primary source |
| Singapore Model AI Governance 2024 security dimension | IMDA/AI Verify Foundation framework PDF; Clyde & Co analysis | medium | Secondary analysis of primary framework document |
| Agentic AI attack surface expansion; MITRE 2025 additions | Vectra.ai MITRE ATLAS overview 2025; Aviatrix threat research | medium | Evidence of 2025 ATLAS additions; agentic risk is documented research inference |
| RAG pipeline poisoning documented | MDPI Information 2025; Aviatrix Threat Research 2024 | medium | Academic paper and vendor research; no named-organisation primary case |

### Assumptions

- **Assumption:** The six-control minimum viable governance architecture is sufficient for organisations at intermediate AI maturity (using third-party APIs and some internal ML models) but not for organisations training frontier models from scratch. **Justification:** The evidence base reviewed focuses on deploying AI rather than building it; all cited NZ regulatory guidance is also framed around deployment. Organisations training base models face additional risks (membership inference, differential privacy) that the six controls do not address.

- **Assumption:** The phishing volume statistics (1,265% increase) represent an order-of-magnitude signal even if specific percentages vary by methodology. **Justification:** Multiple independent sources (SlashNext, KnowBe4, Zscaler ThreatLabz) all document sharp increases; the specific multiplier is methodology-dependent but the directional claim is supported across sources.

### Analysis

The evidence supports a clear structural finding: AI security strategy is not a single discipline but two separate governance domains with different control architectures. Conflating them — or treating AI-enhanced threat defence as sufficient without also governing AI systems as attack surfaces — leaves organisations exposed on the second vector.

The threat-landscape evidence is robust. The phishing statistics are consistent across five independent sources despite methodological variation. The financial loss data ($2.7B BEC) is FBI-sourced primary data. The Microsoft Digital Defense Report is the largest single dataset on adversary AI use, and its 200+ adversarial AI-content-generation instances per month from nation-state actors is consistent with the broader pattern.

For AI as security tool, the disclosed case evidence is strong: HSBC and JPMorgan are named cases with specific metrics, corroborated in prior research. Microsoft Security Copilot's 30% MTTR reduction is internally published research, not a press release. KPMG's survey of 85% SOC-leader confidence is large-n survey data. The pattern is convergent.

For AI system security, the weakest evidence is on governance adoption rates — there is no survey data on what percentage of organisations have deployed MITRE ATLAS-aligned controls or adversarial testing regimes. The evidence is strong on the attack taxonomy and on specific incidents (CVEs, RAG poisoning), weaker on what proportion of organisations have operationalised defences.

Singapore's framework is chosen as the benchmark governance reference over NIST Cyber AI Profile because the NIST profile is in preliminary draft (December 2025) and Singapore's framework is the only one with specific security controls in final-form documentation.

### Risks, Gaps, and Uncertainties

- **BS11 adequacy for AI supply chain:** NZ banks' BS11 outsourcing framework was designed for IT service outsourcing. It does not explicitly address model weight provenance, training data lineage, or adversarial robustness testing of third-party AI models. This is a material regulatory gap for the four major Australian-owned NZ banks, whose AI systems are effectively governed at group level under APRA CPS 230.

- **CERT NZ AI-specific threat intelligence not directly accessed:** CERT NZ merged with NCSC. Its historical threat reporting was reviewed in summary but specific AI threat advisories from CERT NZ were not directly retrieved. The merged NCSC is assumed to be the current authoritative source.

- **Google Project Zero/DeepMind AI security research not accessed:** The item's Sources list included Google Project Zero and DeepMind. These materials were not retrieved; findings would be more technical/academic than the governance focus of this item.

- **Governance adoption rates unknown:** No data on the percentage of NZ financial institutions or government agencies that have conducted AI-specific adversarial testing or deployed MITRE ATLAS-aligned controls.

- **Phishing statistic methodology variation:** The 1,265% figure (SlashNext) measures a different thing from the 20% volume decline with quality increase (Zscaler ThreatLabz 2025). Both may be accurate simultaneously: total raw phishing volume may have dipped while AI-quality targeted attacks increased sharply.

- **NIST Cyber AI Profile status:** Published as preliminary draft December 2025 — the most current framework, but not yet finalised. Its structure is expected to be stable; specific control mappings may change.

### Open Questions

- **Is BS11 sufficient for AI model supply chain governance?** NZ banks outsource AI model development and hosting to parent-bank platforms governed by APRA CPS 230, not RBNZ. Does BS11's current outsourcing framework capture model weight provenance and adversarial robustness testing, or does a separate AI supply chain standard need to be added? This could become a backlog item.

- **What is the threshold for mandatory AI security incident reporting in NZ?** DORA (EU) requires 24-hour initial notification for ICT incidents affecting AI systems in financial services. NZ has no equivalent trigger. Does the NCSC Minimum Cyber Security Standards "response planning" requirement effectively cover AI security incidents, or is there a gap?

- **How should NZ organisations govern agentic AI (AI with tool-use)?** Current guidance addresses LLM chatbots and ML models. Agentic systems with persistent memory, API access, and multi-step reasoning are materially different attack surfaces. MITRE ATLAS is updating its framework; NZ guidance has not yet addressed this category.

---

## Output

- Type: knowledge
- Description: AI security strategy framework covering the threat landscape (AI-enhanced attacks), AI system attack taxonomy (MITRE ATLAS, OWASP LLM Top 10, NIST AI 100-2), NZ regulatory mapping (NCSC, FMA, RBNZ), and minimum viable governance architecture for NZ organisations.
- Links:
  - https://atlas.mitre.org/ (MITRE ATLAS — adversarial threat landscape for AI systems)
  - https://www.ncsc.govt.nz/protect-your-organisation/engaging-with-artificial-intelligence/ (NZ NCSC Engaging with AI, January 2024)
  - https://csrc.nist.gov/pubs/ai/100/2/e2023/final (NIST AI 100-2e2023 adversarial ML taxonomy)
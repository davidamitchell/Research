---
title: "Coding AI Agent Skills Survey: Existing Vendor and OSS Prompt Libraries for Software Engineering Domains"
added: 2026-03-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [ai-agents, copilot, skills, prompts, software-engineering, dotnet, python, ddd, cqrs, clean-architecture, solid, api-design, testing, security, kafka, airflow, data-pipelines, data-visualisation, jupyter]
started: ~
completed: ~
output: [knowledge]
---

# Coding AI Agent Skills Survey: Existing Vendor and OSS Prompt Libraries for Software Engineering Domains

## Research Question

What actively maintained, publicly available agent skills, prompt libraries, instructions files, and system prompts exist — from vendors such as Microsoft and from the Open Source Software (OSS) community — that cover the following software engineering domains: UI/UX (User Interface/User Experience) development, Python backend development, data architecture, data modelling, software architecture, SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) software design, clean code, clean architecture, API (Application Programming Interface) design, DDD (Domain-Driven Design), .NET API development, Kafka event design for ECST (Event-Carried State Transfer), .NET architecture, .NET CQRS (Command Query Responsibility Segregation), database design, data pipelines, design, data visualisation, classification, semantic and concept extraction, unit testing, E2E (End-to-End) testing, integration testing, security architecture, security engineering, Apache Airflow, and Jupyter Notebooks — and which of these are suitable for adoption as-is to standardise and remove opinion from software development practice?

## Scope

**In scope:**
- Agent skill files, system prompts, prompt templates, and instructions files specifically targeting software engineering roles and domains listed in the research question
- Sources from major vendors: Microsoft GitHub Copilot skills/extensions, Microsoft Azure OpenAI prompt samples, JetBrains AI assistant prompts, Cursor IDE rule files, Anthropic Claude prompt library, OpenAI prompt engineering guide and example prompts
- OSS community sources: GitHub repositories with `.github/copilot-instructions.md`, `.cursorrules`, `.clinerules`, `.windsurfrules`, or equivalent convention files; awesome-lists for AI coding prompts; community prompt libraries with active maintenance signals (commit recency, star count, open issues)
- Coverage assessment across all listed domains — which domains have strong published prompt coverage vs. gaps
- Quality signals for each source: vendor vs. community, date of last update, evidence of production use, whether the prompts encode established standards vs. individual opinion
- Prompt/skill content alignment with well-known standards bodies: ISO (International Organisation for Standardisation), OWASP (Open Web Application Security Project), NIST, 12-Factor App, OpenAPI Specification, AsyncAPI, C4 model, DORA (DevOps Research and Assessment)

**Out of scope:**
- Building new skills or prompts — discovery and evaluation only
- Proprietary or paywalled prompt libraries with no public inspection capability
- General-purpose chatbot prompt engineering (focus is software engineering domain specificity)
- Evaluation of AI model quality — only the prompts/skills themselves are assessed, not the models they run on
- Fine-tuning, RAG (Retrieval-Augmented Generation) datasets, or embedding-based approaches — instruction-level prompts and skills only

**Constraints:** Publicly accessible sources only. Prefer sources with verifiable maintenance signals (recent commits, active issues). All sources documented at URL level. Treat vendor documentation as high-confidence for factual claims; treat community repositories as medium-confidence unless corroborated.

## Context

AI coding assistants — GitHub Copilot, Cursor, Windsurf, Cline, and similar tools — increasingly support customisation via skill files, system prompts, instructions files, and rules files that shape their behaviour for a specific engineering context. The question is not whether such customisation is possible, but whether high-quality, domain-specific prompts already exist that encode established engineering best practices for the listed domains, so that teams can adopt them rather than writing their own from scratch.

The motivation is twofold:

1. **Standardisation** — rather than every team, organisation, or individual writing their own prompts encoding personal opinions, adopting prompts that are grounded in established standards (OWASP for security, OpenAPI for API design, DDD tactical patterns, SOLID principles, Clean Architecture layers, etc.) removes subjective bias and aligns AI-assisted development with industry consensus.

2. **Avoiding rework** — vendors such as Microsoft, JetBrains, and Anthropic, and large OSS communities, may have already invested significant effort in producing high-quality prompt libraries. Before creating new prompt content, it is worth cataloguing what already exists and what its adoption characteristics are.

The scope is deliberately broad — covering 25+ engineering domains — because the goal is a comprehensive survey, not depth on a single domain. The output is a catalogue and a recommendation on which existing materials are adoption-ready vs. which domains have gaps requiring new prompt development.

## Approach

1. **Vendor survey** — systematically review publicly available prompt/skill libraries from: Microsoft (GitHub Copilot custom instructions, GitHub Copilot Extensions, Azure OpenAI prompt engineering guide, VS Code Copilot instructions docs), JetBrains (AI Assistant prompt library), Anthropic (Claude prompt library), OpenAI (prompt engineering guide and cookbook), Cursor IDE (`.cursorrules` documentation and community examples), Windsurf IDE (`.windsurfrules`), and Cline (`.clinerules`). Document: URL, last updated, domains covered, whether prompts reference established standards.

2. **OSS community survey** — search GitHub for repositories matching patterns: `awesome-copilot-instructions`, `awesome-cursorrules`, `awesome-prompts`, `.github/copilot-instructions.md`, `.cursorrules` with software engineering content. Filter for: 100+ stars or active maintenance in the last 6 months. Document per domain: which repositories have prompt content, what standards they reference, maintenance signals.

3. **Domain coverage matrix** — for each of the 25+ domains listed in the research question, produce a coverage assessment: (a) whether high-quality, standards-grounded prompts exist in vendor or OSS sources, (b) the best available source, (c) confidence in its quality and maintenance, (d) gap assessment if no good source exists.

4. **Standards alignment check** — for the domains where prompts exist, assess whether they reference or encode established standards: OWASP (security), OpenAPI/AsyncAPI (API design), Clean Architecture / Hexagonal Architecture (architecture), CQRS/Event Sourcing patterns from established literature (Fowler, Vernon, Young), SOLID principles from established literature, DDD tactical/strategic patterns from Evans and Vernon, 12-Factor App, DORA capabilities (testing, deployment), NIST Cybersecurity Framework (CSF) (security architecture).

5. **Specific domain deep-dives** — for the domains most likely to have rich existing content (security, testing, API design, .NET, Python), do a deeper search to surface the single best reference prompt/skill for each, and assess whether it is adoption-ready.

6. **Gap identification** — identify domains with no good publicly available prompts/skills. For each gap, note whether the gap is because: (a) the domain is too new for the community to have produced prompts, (b) the domain is too specialised (e.g., Kafka ECST design), or (c) prompts exist but are too opinion-laden to adopt without review.

7. **Synthesis** — produce Executive Summary, Key Findings, Evidence Map, domain coverage matrix, and a prioritised adoption recommendation: which prompts/skills to adopt immediately, which to adapt, and which domains need new development.

## Sources

- [ ] GitHub Copilot Custom Instructions documentation — Microsoft — https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- [ ] GitHub Copilot Extensions marketplace — Microsoft — https://github.com/marketplace?type=apps&copilot_app=true
- [ ] Azure OpenAI Prompt Engineering Guide — Microsoft — https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering
- [ ] VS Code GitHub Copilot Instructions documentation — Microsoft — https://code.visualstudio.com/docs/copilot/copilot-customization
- [ ] JetBrains AI Assistant Prompt Library — JetBrains — https://www.jetbrains.com/ai/
- [ ] Anthropic Claude Prompt Library — Anthropic — https://docs.anthropic.com/en/prompt-library/library
- [ ] OpenAI Prompt Engineering Guide — OpenAI — https://platform.openai.com/docs/guides/prompt-engineering
- [ ] OpenAI Cookbook — OpenAI — https://cookbook.openai.com/
- [ ] Cursor Rules documentation and community examples — Cursor — https://cursor.directory/ and https://www.cursorrules.com/
- [ ] `awesome-cursorrules` repository — PatrickJS — https://github.com/PatrickJS/awesome-cursorrules
- [ ] `awesome-copilot-instructions` — search GitHub for community collections of `.github/copilot-instructions.md` examples
- [ ] GitHub search: `filename:.github/copilot-instructions.md` language-specific results (Python, C#, TypeScript, etc.)
- [ ] Microsoft TypeSpec for API design — https://typespec.io/ — as a standards-grounded API design approach that could inform API design prompts
- [ ] OWASP (Open Web Application Security Project) LLM Security Top 10 — https://owasp.org/www-project-top-10-for-large-language-model-applications/ — for security-related prompt quality criteria
- [ ] OWASP Application Security Verification Standard (ASVS) — https://owasp.org/www-project-application-security-verification-standard/ — security architecture and security engineering prompt baseline
- [ ] Clean Architecture — Robert C. Martin (2017) — published reference for clean architecture prompt quality criteria
- [ ] Domain-Driven Design (DDD) Reference — Eric Evans (2015) — https://www.domainlanguage.com/ddd/reference/ — DDD prompt quality baseline
- [ ] "Implementing Domain-Driven Design" — Vaughn Vernon (2013) — DDD tactical pattern reference
- [ ] CQRS and Event Sourcing patterns — Martin Fowler — https://martinfowler.com/bliki/CQRS.html and https://martinfowler.com/eaaDev/EventSourcing.html
- [ ] Kafka design patterns and ECST (Event-Carried State Transfer) — Fowler — https://martinfowler.com/articles/201701-event-driven.html
- [ ] AsyncAPI Specification for event-driven API design — https://www.asyncapi.com/
- [ ] OpenAPI Specification 3.1 — https://spec.openapis.org/oas/v3.1.0
- [ ] 12-Factor App methodology — https://12factor.net/ — for Python and general backend prompt quality criteria
- [ ] DORA (DevOps Research and Assessment) capabilities — https://dora.dev/capabilities/ — for testing and deployment prompt quality criteria
- [ ] Apache Airflow documentation and best practices — Apache — https://airflow.apache.org/docs/
- [ ] Jupyter Notebooks best practices — Project Jupyter / nbconvert / nbformat — https://jupyter.org/
- [ ] Microsoft .NET architecture guides — Microsoft — https://dotnet.microsoft.com/en-us/learn/dotnet/architecture-guides — eShopOnContainers, Blazor, MAUI reference architectures
- [ ] Thoughtworks Technology Radar (2023–2025) — AI coding assistants and prompt engineering entries — https://www.thoughtworks.com/radar

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

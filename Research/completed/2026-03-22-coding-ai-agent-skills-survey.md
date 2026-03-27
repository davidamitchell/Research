---
review_count: 2
title: "Coding AI Agent Skills Survey: Existing Vendor and OSS Prompt Libraries for Software Engineering Domains"
added: 2026-03-22
status: completed
priority: high  # low | medium | high
blocks: []
tags: [ai-agents, copilot, skills, prompts, software-engineering, dotnet, python, ddd, cqrs, clean-architecture, solid, api-design, testing, security, kafka, airflow, data-pipelines, data-visualisation, jupyter]
started: 2026-03-22
completed: 2026-03-22
output: [knowledge]
---

# Coding AI Agent Skills Survey: Existing Vendor and OSS Prompt Libraries for Software Engineering Domains

## Research Question

What actively maintained, publicly available agent skills, prompt libraries, instructions files, and system prompts exist — from vendors such as Microsoft and from the Open Source Software (OSS) community — that cover the following software engineering domains: UI/UX (User Interface/User Experience) development, Python backend development, data architecture, data modelling, software architecture, SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) software design, clean code, clean architecture, API (Application Programming Interface) design, DDD (Domain-Driven Design), .NET API development, Kafka event design for ECST (Event-Carried State Transfer), .NET architecture, .NET CQRS (Command Query Responsibility Segregation), database design, data pipelines, design, data visualisation, classification, semantic and concept extraction, unit testing, E2E (End-to-End) testing, integration testing, security architecture, security engineering, Apache Airflow, and Jupyter Notebooks — and which of these are suitable for adoption as-is to standardise and remove opinion from software development practice?

## Scope

**In scope:**
- Agent skill files, system prompts, prompt templates, and instructions files specifically targeting software engineering roles and domains listed in the research question
- Sources from major vendors: Microsoft GitHub Copilot skills/extensions, Microsoft Azure OpenAI prompt samples, JetBrains AI Assistant prompts, Cursor IDE rule files, Anthropic Claude prompt library, OpenAI prompt engineering guide and example prompts
- OSS community sources: GitHub repositories with `.github/copilot-instructions.md`, `.cursorrules`, `.clinerules`, `.windsurfrules`, or equivalent convention files; awesome-lists for AI coding prompts; community prompt libraries with active maintenance signals (commit recency, star count, open issues)
- Coverage assessment across all listed domains — which domains have strong published prompt coverage vs. gaps
- Quality signals for each source: vendor vs. community, date of last update, evidence of production use, whether the prompts encode established standards vs. individual opinion
- Prompt/skill content alignment with well-known standards bodies: ISO (International Organisation for Standardisation), OWASP (Open Web Application Security Project), NIST (National Institute of Standards and Technology), 12-Factor App, OpenAPI Specification, AsyncAPI, C4 model, DORA (DevOps Research and Assessment)

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

- [x] GitHub Copilot Custom Instructions documentation — Microsoft — https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- [ ] GitHub Copilot Extensions marketplace — Microsoft — https://github.com/marketplace?type=apps&copilot_app=true
- [x] Azure OpenAI Prompt Engineering Guide — Microsoft — https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering
- [x] VS Code GitHub Copilot customization documentation — Microsoft — https://code.visualstudio.com/docs/copilot/copilot-customization
- [x] GitHub `awesome-copilot` repository — GitHub / Microsoft — https://github.com/github/awesome-copilot
- [x] `awesome-copilot` instructions index — GitHub / Microsoft — https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md
- [x] Microsoft blog on Awesome GitHub Copilot website, learning hub, and plugins — https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [x] JetBrains AI Assistant prompt library documentation — https://www.jetbrains.com/help/ai-assistant/prompt-library.html
- [x] JetBrains AI Assistant project rules documentation — https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html
- [x] JetBrains AI Assistant rules settings reference — https://www.jetbrains.com/help/ai-assistant/settings-reference-rules.html
- [x] Anthropic Claude prompt library — https://docs.anthropic.com/en/prompt-library/library
- [x] Anthropic `skills` repository — https://github.com/anthropics/skills and https://raw.githubusercontent.com/anthropics/skills/main/README.md
- [ ] OpenAI Prompt Engineering Guide — OpenAI — https://platform.openai.com/docs/guides/prompt-engineering — inaccessible (HTTP 403)
- [x] OpenAI Cookbook — OpenAI — https://cookbook.openai.com/
- [x] OpenAI `Skills in API` cookbook page — https://cookbook.openai.com/examples/skills_in_api
- [x] OpenAI Skills guide — https://developers.openai.com/api/docs/guides/tools-skills
- [x] Cursor rules documentation — https://cursor.com/docs/rules
- [ ] Cursor directory — https://cursor.directory/ — inaccessible during investigation (HTTP 429)
- [x] `awesome-cursorrules` repository — PatrickJS — https://github.com/PatrickJS/awesome-cursorrules and https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md
- [x] `awesome-agent-skills` repository — VoltAgent — https://github.com/VoltAgent/awesome-agent-skills and https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [x] `system-prompts-and-models-of-ai-tools` repository — x1xhlol — https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools and https://raw.githubusercontent.com/x1xhlol/system-prompts-and-models-of-ai-tools/main/README.md
- [x] Cline documentation — https://docs.cline.bot/
- [x] Windsurf Memories / Rules documentation — https://docs.windsurf.com/windsurf/cascade/memories
- [x] Windsurf Skills documentation — https://docs.windsurf.com/windsurf/cascade/skills
- [x] AGENTS.md standard site — https://agents.md/
- [x] OWASP Application Security Verification Standard (ASVS) — https://owasp.org/www-project-application-security-verification-standard/
- [x] OpenAPI Specification 3.1 — https://spec.openapis.org/oas/v3.1.0
- [x] AsyncAPI home page — https://www.asyncapi.com/
- [x] 12-Factor App methodology — https://12factor.net/
- [x] Apache Airflow documentation index — https://airflow.apache.org/docs/
- [x] Jupyter home page — https://jupyter.org/
- [x] Martin Fowler — CQRS — https://martinfowler.com/bliki/CQRS.html
- [x] Martin Fowler — Event Sourcing — https://martinfowler.com/eaaDev/EventSourcing.html
- [x] Martin Fowler — Event-Driven article with Event-Carried State Transfer (ECST) — https://martinfowler.com/articles/201701-event-driven.html
- [x] Prior completed research: `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`
- [x] Prior completed research: `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`
- [x] Prior completed research: `Research/completed/2026-03-16-intent-driven-development.md`

---

## Research Skill Output

### §0 Initialise

- [fact] **Research question restated:** Which actively maintained public prompt libraries, rules collections, skills repositories, and instruction-file conventions exist for software engineering work across the listed domains, and which of them are strong enough to adopt with minimal local rewriting?
- [fact] **Scope confirmed:** This investigation is limited to public vendor documentation, public GitHub repositories, and public standards pages. Proprietary internal prompt packs, non-public enterprise templates, and paywalled materials are excluded.
- [fact] **Constraint mode:** URL-level citations only for external claims. Vendor documentation is treated as primary evidence for product capabilities; public repository metadata and READMEs are treated as primary evidence for maintenance signals and catalog structure.
- [fact] **Output format:** Full §§0–7 completion, followed by Findings with Executive Summary, Key Findings, Evidence Map, Domain Coverage Matrix, Assumptions, Analysis, Risks/Gaps, Open Questions, and Output.
- [fact] **Prior work cross-reference:** `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` established that persistent context files and phase-specific prompt patterns matter, but it did not inventory current public libraries. `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` mapped tool architectures across Copilot, Cursor, Cline, and others, but it did not answer which reusable public artifacts are adoption-ready. `Research/completed/2026-03-16-intent-driven-development.md` showed that prompts become more reliable when grounded in durable artifacts rather than one-off chat phrasing. This item therefore focuses on the library and standards layer rather than re-arguing prompt theory.

### §1 Question Decomposition

- [fact] **A. Vendor surface area**
  - A1. Which surveyed vendors publish first-party mechanisms for repository instructions, project rules, skills, or prompt libraries?
  - A2. Which surveyed vendors publish first-party reusable software-engineering content rather than only “how to write prompts” guidance?
  - A3. Which vendor assets are installable or directly reusable without rewriting their structure?
- [fact] **B. Open standards and portability**
  - B1. Is there a cross-vendor instruction-file convention that reduces lock-in?
  - B2. Is there a cross-vendor skill packaging convention that reduces lock-in?
- [fact] **C. Community catalogs**
  - C1. Which OSS collections have the strongest maintenance signals and the broadest domain coverage?
  - C2. Which OSS collections are curated for adoption, and which are primarily archives or reverse-engineered prompt dumps?
- [fact] **D. Domain coverage**
  - D1. Which of the requested domains have strong public coverage from first-party or curated OSS sources?
  - D2. Which requested domains have only weak or highly opinionated public coverage?
  - D3. Which domains appear to lack good public prompt/skill artifacts even though the underlying engineering standards are mature?
- [fact] **E. Adoption readiness**
  - E1. Which public artifacts are strong enough to adopt largely as-is?
  - E2. Which artifacts should be used only as scaffolding, then aligned to authoritative standards such as OWASP ASVS, OpenAPI, AsyncAPI, or 12-Factor App?
  - E3. Which domains still require net-new internal development because public material is sparse or too context-dependent?

### §2 Investigation

**Consulted sources**
- [x] https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- [x] https://code.visualstudio.com/docs/copilot/copilot-customization
- [x] https://github.com/github/awesome-copilot
- [x] https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md
- [x] https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [x] https://www.jetbrains.com/help/ai-assistant/prompt-library.html
- [x] https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html
- [x] https://www.jetbrains.com/help/ai-assistant/settings-reference-rules.html
- [x] https://docs.anthropic.com/en/prompt-library/library
- [x] https://github.com/anthropics/skills
- [x] https://raw.githubusercontent.com/anthropics/skills/main/README.md
- [x] https://cookbook.openai.com/
- [x] https://cookbook.openai.com/examples/skills_in_api
- [x] https://developers.openai.com/api/docs/guides/tools-skills
- [x] https://cursor.com/docs/rules
- [x] https://github.com/PatrickJS/awesome-cursorrules
- [x] https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md
- [x] https://github.com/VoltAgent/awesome-agent-skills
- [x] https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [x] https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- [x] https://raw.githubusercontent.com/x1xhlol/system-prompts-and-models-of-ai-tools/main/README.md
- [x] https://docs.cline.bot/
- [x] https://docs.windsurf.com/windsurf/cascade/memories
- [x] https://docs.windsurf.com/windsurf/cascade/skills
- [x] https://agents.md/
- [x] https://owasp.org/www-project-application-security-verification-standard/
- [x] https://spec.openapis.org/oas/v3.1.0
- [x] https://www.asyncapi.com/
- [x] https://12factor.net/
- [x] https://airflow.apache.org/docs/
- [x] https://jupyter.org/
- [x] https://martinfowler.com/bliki/CQRS.html
- [x] https://martinfowler.com/eaaDev/EventSourcing.html
- [x] https://martinfowler.com/articles/201701-event-driven.html
- [x] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`
- [x] `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`
- [x] `Research/completed/2026-03-16-intent-driven-development.md`

**A1–A3 — Vendor mechanisms and first-party reusable content**

- [fact] GitHub Copilot on GitHub supports three repository customization types: repository-wide `copilot-instructions.md`, path-specific `*.instructions.md`, and agent instructions via an `AGENTS.md` agent-instructions file, `CLAUDE.md`, or `GEMINI.md`. Source: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- [fact] Visual Studio Code now exposes a broader customization system for GitHub Copilot, including custom instructions, prompt files, agent skills, custom agents, agent plugins, MCP (Model Context Protocol) servers, and hooks. Source: https://code.visualstudio.com/docs/copilot/copilot-customization
- [fact] The `github/awesome-copilot` repository describes itself as “a community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins” and offers direct plugin installation paths for the GitHub Copilot Command Line Interface (CLI) and Visual Studio Code. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/README.md
- [fact] Microsoft’s 2026-03-16 blog post states that `awesome-copilot` had **175+ agents**, **208+ skills**, **176+ instructions**, **48+ plugins**, **7 agentic workflows**, and **3 hooks** at that time. Source: https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [fact] The `awesome-copilot` instructions index includes directly installable examples for domains such as .NET Framework development, .NET upgrades, .NET MAUI, accessibility, agent safety and governance, prompt engineering safety, Ansible, Apex, and ASP.NET REST API development. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md
- [inference] Among the vendor-backed public assets inspected here, `github/awesome-copilot` is the clearest example of a large, directly reusable software-engineering customization catalog rather than just documentation about how to author prompts. Sources: https://github.com/github/awesome-copilot ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md

**B1–B2 — Anthropic and OpenAI skill systems**

- [fact] Anthropic’s prompt-library page is a general guide to prompt engineering, output control, tool use, and agentic systems. It is a reference manual for shaping model behavior, not a domain-indexed software-engineering prompt catalog. Source: https://docs.anthropic.com/en/prompt-library/library
- [fact] Anthropic’s `skills` repository defines skills as folders of instructions, scripts, and resources loaded dynamically for specialized tasks. The repository includes technical examples such as `frontend-design`, `mcp-builder`, and `webapp-testing`, plus document-oriented skills such as `docx`, `pptx`, `xlsx`, and `pdf`. Sources: https://github.com/anthropics/skills ; https://raw.githubusercontent.com/anthropics/skills/main/README.md
- [fact] Anthropic’s skill-creation documentation requires a `Skill.md` file with YAML frontmatter (`name`, `description`) and optional bundled resources or scripts, and explicitly recommends alignment to the open Agent Skills specification. Source: https://support.claude.com/en/articles/12512198-creating-custom-skills
- [fact] Anthropic’s “Using Skills in Claude” documentation states that Claude can automatically identify and load relevant built-in or custom skills, and that skills can also be provisioned organization-wide. Source: https://support.claude.com/en/articles/12512180-using-skills-in-claude
- [fact] OpenAI’s Skills guide defines skills as versioned bundles of files plus a `SKILL.md` skill-manifest file for hosted or local shell environments, and the guide explicitly says skills are compatible with the open Agent Skills standard. Source: https://developers.openai.com/api/docs/guides/tools-skills
- [fact] OpenAI’s cookbook page “Skills in API” positions skills as reusable bundles for procedures, scripts, templates, and stable workflows, and recommends them when teams need reusable, independently versionable behaviors. Source: https://cookbook.openai.com/examples/skills_in_api
- [fact] OpenAI’s Skills guide notes that OpenAI maintains first-party skills that can be referenced by id, such as `openai-spreadsheets`. Source: https://developers.openai.com/api/docs/guides/tools-skills
- [inference] Anthropic and OpenAI both publish mature skill packaging patterns and examples, but neither exposed a public first-party software-engineering catalog with the breadth of `awesome-copilot` or `awesome-cursorrules` during this investigation. Sources: https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cookbook.openai.com/examples/skills_in_api

**C1–C4 — Cursor, Windsurf, Cline, and JetBrains customization surfaces**

- [fact] Cursor’s official rules documentation page describes “persistent instructions with Project, Team, and User Rules, plus AGENTS.md,” which confirms that Cursor supports durable repository or team guidance rather than only ad hoc prompting. Source: https://cursor.com/docs/rules
- [fact] Windsurf differentiates **Rules**, **AGENTS.md**, **Workflows**, **Skills**, and **Memories**, and its rules engine supports always-on, model-decision, glob, and manual activation modes. Source: https://docs.windsurf.com/windsurf/cascade/memories
- [fact] Windsurf’s skills documentation requires `.windsurf/skills/<skill-name>/SKILL.md`, uses progressive disclosure, and gives software-engineering examples including deployment workflow, code review guidelines, and testing procedures. Source: https://docs.windsurf.com/windsurf/cascade/skills
- [fact] Cline’s documentation exposes customization via rules, skills, workflows, hooks, `.clineignore`, Memory Bank, and Jupyter support, while emphasising that every action requires explicit user approval. Source: https://docs.cline.bot/
- [fact] JetBrains AI Assistant lets users create custom prompts, modify built-in prompts, and create project rules stored in `.aiassistant/rules`, with rule modes such as Always, Manually, By model decision, and By file patterns. Sources: https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html ; https://www.jetbrains.com/help/ai-assistant/settings-reference-rules.html
- [inference] The first-party materials for Cursor, Windsurf, Cline, and JetBrains focus primarily on giving users extensibility mechanisms, not on shipping large, official, domain-indexed engineering prompt libraries. Sources: https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/skills ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html

**D1–D3 — Open standards and cross-tool portability**

- [fact] The AGENTS.md site describes AGENTS.md as “a simple, open format for guiding coding agents,” claims usage by over **60k open-source projects**, and positions AGENTS.md as a cross-agent “README for agents.” Source: https://agents.md/
- [fact] AGENTS.md is presented as compatible across a growing ecosystem, with nested AGENTS files allowing subproject overrides, and explicit guidance for Aider and Gemini Command Line Interface (CLI) configuration. Source: https://agents.md/
- [fact] Anthropic’s custom-skill documentation, OpenAI’s Skills guide, and Windsurf’s skills documentation all explicitly point to the open Agent Skills specification at `agentskills.io`. Sources: https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://developers.openai.com/api/docs/guides/tools-skills ; https://docs.windsurf.com/windsurf/cascade/skills
- [inference] `AGENTS.md` plus `SKILL.md` has become the lowest-friction portability layer across modern coding assistants, making investment in those formats safer than investment in older single-tool rule files alone. Sources: https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills

**E1–E4 — Community catalogs and maintenance signals**

- [fact] Public GitHub repository metadata retrieved on 2026-03-22 showed the following maintenance signals: `github/awesome-copilot` 26,402 stars and pushed 2026-03-21; `anthropics/skills` 99,462 stars and pushed 2026-03-06; `PatrickJS/awesome-cursorrules` 38,614 stars and pushed 2025-10-24; `VoltAgent/awesome-agent-skills` 12,268 stars and pushed 2026-03-20; `cline/cline` 59,220 stars and pushed 2026-03-22; `Aider-AI/aider` 42,222 stars and pushed 2026-03-17; `agentsmd/agents.md` 19,238 stars and pushed 2026-03-12. Sources: https://github.com/github/awesome-copilot ; https://github.com/anthropics/skills ; https://github.com/PatrickJS/awesome-cursorrules ; https://github.com/VoltAgent/awesome-agent-skills ; https://github.com/cline/cline ; https://github.com/Aider-AI/aider ; https://github.com/agentsmd/agents.md
- [fact] `awesome-cursorrules` is a large community catalog organized into categories such as frontend frameworks, backend and full-stack, database and API, testing, hosting and deployments, language-specific, documentation, and utilities. Source: https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md
- [fact] The public `awesome-cursorrules` repository tree on 2026-03-22 exposed domain-specific files for Python FastAPI, ASP.NET ABP, Cypress API/E2E/integration testing, Scala Kafka, pandas + scikit-learn + Jupyter, SOLID-oriented rules, database guidance, and data visualisation guidance. Source: https://github.com/PatrickJS/awesome-cursorrules
- [fact] `awesome-agent-skills` describes itself as a curated collection of **630+** agent skills from official teams and the community, including Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Microsoft, and OpenAI. Source: https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [fact] `system-prompts-and-models-of-ai-tools` is a large repository of public or reverse-engineered system prompts and tool configurations, but its own framing centers on prompt leakage and security exposure rather than on curated adoption of engineering standards. Source: https://raw.githubusercontent.com/x1xhlol/system-prompts-and-models-of-ai-tools/main/README.md
- [inference] Curated catalogs such as `awesome-copilot`, `awesome-cursorrules`, and `awesome-agent-skills` are much more adoption-relevant than leakage-oriented prompt archives, because curation, install paths, and human-readable descriptions matter more for engineering standardisation than raw prompt volume. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/README.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://raw.githubusercontent.com/x1xhlol/system-prompts-and-models-of-ai-tools/main/README.md

**F1–F5 — Standards grounding and domain implications**

- [fact] OWASP ASVS defines itself as a basis for testing web-application technical security controls and for giving developers a list of requirements for secure development. Source: https://owasp.org/www-project-application-security-verification-standard/
- [fact] OpenAPI 3.1 is a formal specification that defines required document structure, metadata, paths, components, and reusable security schemes for APIs. Source: https://spec.openapis.org/oas/v3.1.0
- [fact] 12-Factor App defines a portable software-as-a-service methodology, including explicit dependency isolation, environment-based configuration, strict build/release/run separation, stateless processes, and development/production parity. Source: https://12factor.net/
- [inference] Apache Airflow publishes extensive official documentation for core components, a Task Software Development Kit (SDK), a Python Application Programming Interface (API) client, and many providers, which indicates that the underlying domain is rich in authoritative source material even if the prompt-catalog layer is comparatively thin. Source: https://airflow.apache.org/docs/
- [fact] Jupyter presents itself as an open, notebook-centric interactive development environment and open standard for interactive computing, with notebook document format and interactive computing protocol documentation. Source: https://jupyter.org/
- [fact] Martin Fowler’s CQRS article warns that CQRS adds risky complexity for most systems and should be used cautiously; his Event-Driven article separates Event Notification, Event-Carried State Transfer, and Event Sourcing as distinct patterns rather than interchangeable jargon. Sources: https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://martinfowler.com/eaaDev/EventSourcing.html
- [inference] The requested domains that already have mature public engineering standards are not always the domains with mature public prompt libraries. Standards maturity and prompt-library maturity are related, but they are not the same variable. Sources: https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://12factor.net/ ; https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html

**G1–G4 — Coverage synthesis by domain family**

- [inference] GitHub’s `awesome-copilot` repository tree, public instructions index, and Microsoft blog together indicate that the densest vendor-backed public coverage in this survey sits around .NET, Python, API, security, testing, and database-oriented work. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [inference] `awesome-cursorrules` indicates that community coverage is comparatively strongest for frontend/UI work, Python backend, FastAPI, testing, Jupyter notebooks, and general engineering heuristics such as SOLID and clean-code style. Sources: https://github.com/PatrickJS/awesome-cursorrules ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md
- [inference] Public coverage is strongest where the engineering work is repetitive, framework-specific, and easy to express as conventions or checklists — for example frontend stacks, framework APIs, test generation, secure coding practices, and database interactions. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [inference] Public coverage is weakest where the engineering work is organisation-specific, architecture-heavy, or semantically loaded — for example DDD, CQRS architecture decisions, Kafka ECST design, data architecture, data modelling, classification, and semantic/concept extraction. Sources: https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules
- [assumption] Some niche domains may have isolated public prompt files outside the top collections inspected here, but no high-trust, widely maintained public catalog emerged for those domains during this investigation. **Justification:** the strongest first-party and community catalogs inspected here repeatedly surfaced the same strengths (.NET, Python, API, testing, security, frontend) while niche architecture-heavy domains remained sparse.

### §3 Reasoning

- [fact] First-party documentation from GitHub Copilot, Visual Studio Code, Anthropic, OpenAI, Cursor, Windsurf, Cline, and JetBrains all expose some durable customization mechanism, so mechanism existence is directly observed rather than inferred. Sources: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot ; https://code.visualstudio.com/docs/copilot/copilot-customization ; https://docs.anthropic.com/en/prompt-library/library ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/memories ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html
- [fact] Repository READMEs and published indexes for `awesome-copilot`, `awesome-cursorrules`, and `awesome-agent-skills` expose category structure, installation paths, and public breadth signals such as curated counts and domain lists. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [inference] **Adoption readiness** is not equivalent to repository popularity, because the most reusable artifacts in this survey combine inspectability, installation guidance, maintenance signals, and stable formats such as `AGENTS.md` or `SKILL.md`. Sources: https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://github.com/github/awesome-copilot
- [inference] **Standardisation potential** rises when artifacts can be paired with authoritative engineering standards, because public prompt collections vary in rigor while ASVS, OpenAPI, AsyncAPI, and 12-Factor provide an external benchmark for reusable engineering practice. Sources: https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/
- [assumption] **Absence evidence is bounded.** If a vendor’s official docs expose mechanisms but no large first-party domain library, I treat that as “no public library surfaced in the consulted primary materials,” not as proof that no internal or private library exists. **Justification:** this survey is explicitly limited to public documentation and repositories. Sources: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cursor.com/docs/rules

### §4 Consistency Check

- [fact] The OpenAI prompt engineering guide URL listed in the item was inaccessible with HTTP 403 in this environment during investigation, so OpenAI factual claims in this item were anchored to the public cookbook and Skills guide instead. Sources: https://platform.openai.com/docs/guides/prompt-engineering ; https://cookbook.openai.com/ ; https://developers.openai.com/api/docs/guides/tools-skills
- [fact] `cursor.directory` returned HTTP 429 during investigation, so Cursor-specific claims were anchored to the official `cursor.com/docs/rules` page and the public `awesome-cursorrules` repository rather than to the directory site. Sources: https://cursor.directory/ ; https://cursor.com/docs/rules ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md
- [fact] The JetBrains marketing page at `https://www.jetbrains.com/ai/` was too JavaScript-heavy to extract reliable structured evidence in this environment, so JetBrains-specific claims were anchored to official Help pages instead. Sources: https://www.jetbrains.com/ai/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html
- [inference] These access issues do not materially change the core conclusion, because the main comparative judgments in this item rest on accessible first-party mechanism documentation and on inspectable public repository catalogs that remained available throughout the investigation. Sources: https://code.visualstudio.com/docs/copilot/copilot-customization ; https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [inference] The final domain-coverage judgment remains consistent with the cited sources: the strongest catalogs repeatedly surface .NET, Python, API, testing, security, and frontend artifacts, while the cited CQRS, ECST, Airflow, and Jupyter sources describe domain standards or tooling rather than robust prompt catalogs. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://airflow.apache.org/docs/ ; https://jupyter.org/

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** The ecosystem is converging on progressive-disclosure packaging (`SKILL.md` plus bundled files), because Anthropic, OpenAI, and Windsurf all document skill bundles that load rich instructions and resources only when relevant rather than pinning everything into one monolithic prompt. Sources: https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills ; https://docs.windsurf.com/windsurf/cascade/skills
- [inference] **Governance lens:** `AGENTS.md` and packaged skills are more governable than free-form chat prompts, because they are durable files that can live in version control and can be reviewed against standards such as ASVS or OpenAPI before teams adopt them broadly. Sources: https://agents.md/ ; https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://developers.openai.com/api/docs/guides/tools-skills
- [inference] **Economic lens:** Teams get the largest return from adopting public artifacts in repetitive, framework-bound domains, because those are the domains that recur across the strongest inspected catalogs with explicit install paths and multiple maintained examples. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins
- [inference] **Behavioural lens:** Teams are most likely to over-trust public prompts in architecture-heavy domains, because the public evidence for those domains is thinner and more indirect than the evidence for framework-bound domains, leaving more room for hidden local assumptions. Sources: https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules
- [inference] **Historical lens:** The ecosystem is moving away from single-tool rules files toward portable instruction conventions such as `AGENTS.md` and packaged skill bundles such as `SKILL.md`, which improves reuse across tools and reduces configuration lock-in. Sources: https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://docs.windsurf.com/windsurf/cascade/skills

### §6 Synthesis

**Executive summary:**

- [inference] Public software-engineering customization ecosystems now exist across all major coding-assistant vendors, but most first-party vendor material still publishes **mechanisms** for rules and skills rather than large canonical domain libraries; the strongest vendor-backed reusable catalog found here is GitHub / Microsoft’s `awesome-copilot`, while Anthropic and OpenAI publish mature skill systems and examples rather than exhaustive engineering domain packs (https://github.com/github/awesome-copilot ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins ; https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills).
- [inference] The most portable adoption path is to standardize on open instruction and skill formats — especially `AGENTS.md` and `SKILL.md` — then selectively import vendor or curated community assets for concrete domains such as .NET, Python backend, API design, testing, security, and database work (https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md).
- [inference] Curated community catalogs currently provide more domain breadth than most first-party vendor libraries, but they vary significantly in trustworthiness: contributor-reviewed collections such as `awesome-cursorrules`, `awesome-agent-skills`, and `awesome-copilot` are materially safer adoption starting points than reverse-engineered prompt dumps (https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://raw.githubusercontent.com/x1xhlol/system-prompts-and-models-of-ai-tools/main/README.md).
- [inference] The domains most suitable for near-term adoption-as-is are repetitive, framework-heavy, standards-friendly domains; the domains least suitable are high-context architecture and semantic-design domains such as DDD, CQRS, Kafka ECST, data architecture, and classification, where public artifacts remain sparse or too opinionated to standardize without local judgment (https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules).

**Key findings:**

1. [inference] **[high confidence]** GitHub and Microsoft appear to host the broadest public vendor-backed software-engineering customization catalog in this survey, because `github/awesome-copilot` publicly packages hundreds of installable agents, skills, instructions, plugins, and workflows, and Microsoft reported 175+ agents, 208+ skills, 176+ instructions, and 48+ plugins in March 2026 (https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins).
2. [fact] **[high confidence]** Anthropic and OpenAI have both converged on `SKILL.md`-based packaged skills with progressive disclosure, bundled files, and reuse across sessions, but the public first-party materials reviewed here function mainly as mechanism guides and exemplar bundles rather than as exhaustive software-engineering domain libraries (https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cookbook.openai.com/examples/skills_in_api).
3. [inference] **[high confidence]** Cursor, Windsurf, Cline, and JetBrains all expose mature persistent customization surfaces — rules, skills, workflows, project rules, and prompt libraries — yet the first-party documentation inspected for those tools does not present a comparably large official cross-domain engineering catalog that teams can simply install wholesale (https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/memories ; https://docs.windsurf.com/windsurf/cascade/skills ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html).
4. [inference] **[high confidence]** Curated community collections currently provide the widest public domain breadth in this survey, because `awesome-cursorrules` spans frontend, backend, API, testing, database, and Jupyter-related rules, while `awesome-agent-skills` curates 630+ skills from many official engineering teams and `awesome-copilot` packages community-contributed artifacts behind a vendor-backed distribution surface (https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://github.com/github/awesome-copilot).
5. [inference] **[high confidence]** The most adoption-ready public artifacts are the ones built on portable formats such as `AGENTS.md` and `SKILL.md`, because those formats are explicitly cross-tool, version-control friendly, and now referenced by multiple vendors rather than being trapped inside one assistant’s legacy configuration file format (https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://docs.windsurf.com/windsurf/cascade/skills).
6. [inference] **[high confidence]** Public prompt and skill coverage is strongest for UI/UX, Python backend, .NET, API design, testing, security, and database work, because those domains recur across the strongest inspected catalogs with explicit installation paths, repeated file categories, and multiple maintained artifacts rather than one-off examples (https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins).
7. [inference] **[medium confidence]** Public coverage remains weak for DDD, CQRS, Kafka ECST, data architecture, data modelling, classification, semantic/concept extraction, and Apache Airflow-specific engineering guidance, because the best public evidence found for those areas is usually an underlying standard or architecture article rather than a broadly trusted prompt/skill pack (https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://airflow.apache.org/docs/ ; https://jupyter.org/ ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules).
8. [inference] **[high confidence]** Teams that want to “remove opinion” should adopt public artifacts only as scaffolding and then bind them to authoritative standards such as OWASP ASVS, OpenAPI, AsyncAPI, and 12-Factor App, because public prompt collections vary in rigor while those standards define stable security, interface, and operational expectations (https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/).

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] GitHub / Microsoft appear to host the broadest public vendor-backed catalog via `awesome-copilot`. | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins | high | Primary repo plus first-party Microsoft announcement with counts support the comparison. |
| [fact] Anthropic and OpenAI both use `SKILL.md`-based packaged skills. | https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cookbook.openai.com/examples/skills_in_api | high | Independent first-party docs converge on the same packaging pattern. |
| [fact] Cursor, Windsurf, Cline, and JetBrains all expose mature persistent customization surfaces. | https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/memories ; https://docs.windsurf.com/windsurf/cascade/skills ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html | high | Mechanism existence is directly stated in product docs. |
| [inference] Curated community collections provide the widest public breadth in this survey. | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://github.com/github/awesome-copilot | high | Repo READMEs and structures expose breadth and maintenance across more domains than any single non-GitHub vendor catalog inspected. |
| [inference] Portable open formats are the safest adoption substrate. | https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://docs.windsurf.com/windsurf/cascade/skills | high | Multiple vendors point to the same conventions and standards. |
| [inference] Strongest public coverage is in framework-heavy, repetitive engineering domains. | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins | high | Catalog categories and installation indexes cluster in these domains. |
| [inference] Weakest public coverage is in architecture-heavy and semantically loaded domains. | https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://airflow.apache.org/docs/ ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | medium | Standards exist, but robust prompt catalogs do not strongly surface. |
| [inference] Standards such as ASVS, OpenAPI, AsyncAPI, and 12-Factor are necessary companions to public prompt adoption. | https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/ | high | These standards supply the normative layer that prompt catalogs often lack. |

**Domain coverage matrix:**

| Domain | Label | Best public source(s) | Coverage | Adoption view |
|---|---|---|---|---|
| UI/UX development | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/anthropics/skills/main/README.md | high | Strong public examples exist; adopt selectively with local design-system constraints. |
| Python backend development | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | high | One of the strongest public domains; adoption is viable after project-specific testing and security alignment. |
| Data architecture | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | Standards and tools exist, but public prompt/skill packs remain thin; build internally. |
| Data modelling | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Some database-related rules exist, but robust data-modelling prompt libraries did not strongly surface. |
| Software architecture | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium | Good reviewer and blueprint artifacts exist, but wholesale adoption still needs local architecture principles. |
| SOLID software design | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium | Community rules exist; adopt only after aligning terminology and examples to house style. |
| Clean code | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html | medium | Easy to standardize, but many artifacts are opinionated and need local review. |
| Clean architecture | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low-medium | Public examples exist, but not a dominant, standards-grounded catalog. |
| API design | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ | high | Strong public support exists; adopt with OpenAPI / AsyncAPI as the normative layer. |
| DDD | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Public DDD prompt libraries did not strongly surface; do not standardize from public prompts alone. |
| .NET API development | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://github.com/github/awesome-copilot | high | Strong public guidance exists in vendor-backed Copilot assets. |
| Kafka event design for ECST | [inference] | https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/PatrickJS/awesome-cursorrules | low | Conceptual standards exist, but prompt catalogs are sparse and not adoption-ready. |
| .NET architecture | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium-high | Good public material exists, but enterprise architecture still needs local adaptation. |
| .NET CQRS | [inference] | https://martinfowler.com/bliki/CQRS.html ; https://github.com/github/awesome-copilot | low | Public CQRS prompts are far weaker than the underlying architectural literature. |
| Database design | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium-high | Good practical artifacts exist, but schema and operational decisions remain context-dependent. |
| Data pipelines | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | medium | Supporting public material exists, but domain-specific prompt packs are not yet dominant. |
| Design | [inference] | https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium | Plenty of creative/design artifacts exist, but engineering-standard alignment is uneven. |
| Data visualisation | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://jupyter.org/ | medium | Good notebook- and plotting-oriented examples exist; adopt with local charting conventions. |
| Classification | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Public catalogs did not surface strong, high-trust classification prompt packs. |
| Semantic and concept extraction | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | A few adjacent semantics-oriented artifacts exist, but coverage is shallow and fragmented. |
| Unit testing | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | high | One of the most mature public prompt domains; adoption is viable after aligning to test framework choices. |
| E2E testing | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://github.com/github/awesome-copilot | medium-high | Strong Cypress / Playwright examples exist, though they still need environment-specific adaptation. |
| Integration testing | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://github.com/github/awesome-copilot | medium-high | Good public artifacts exist, especially around web stacks and migrations. |
| Security architecture | [inference] | https://owasp.org/www-project-application-security-verification-standard/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium | Public prompts help, but the authoritative baseline is the security standard, not the prompt file. |
| Security engineering | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://owasp.org/www-project-application-security-verification-standard/ | high | Security-oriented prompts exist, and they can be anchored to ASVS for stronger standardization. |
| Apache Airflow | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | Official domain docs are rich, but prompt libraries are not yet strong enough for broad as-is adoption. |
| Jupyter Notebooks | [inference] | https://jupyter.org/ ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://docs.cline.bot/ | medium | Public notebook-oriented rules exist, but they are mostly community examples rather than vendor-backed standards. |

**Assumptions:**

- [assumption] Public absence in first-party docs is treated as absence of a **publicly inspectable** official library on 2026-03-22, not as proof that no private or enterprise-only library exists. **Justification:** this item is explicitly constrained to public sources.
- [assumption] GitHub repository metadata and file-category structure are used as proxies for maintenance and breadth, not as direct evidence of prompt quality. **Justification:** quality still requires human review and standards alignment.
- [assumption] Domains marked “low” coverage may still have isolated niche examples on the web. **Justification:** the strongest catalogs inspected here were broad enough that repeated absence across them is meaningful, but not mathematically exhaustive.

**Analysis:**

- [fact] The evidence separates cleanly into three layers: **mechanisms** (vendors teaching users how to customize assistants), **catalogs** (public collections of reusable artifacts), and **standards** (normative engineering references such as ASVS and OpenAPI).
- [inference] The strongest adoption candidates live where all three layers overlap: a reusable artifact exists, the artifact is easy to install or inspect, and an external standard exists to test whether the artifact is encoding durable engineering practice rather than one maintainer’s taste.
- [inference] GitHub / Microsoft currently lead the public vendor-backed catalog layer because `awesome-copilot` combines breadth, discoverability, and installation UX. Anthropic and OpenAI currently lead the public **skill-system design** layer because they document packaging, versioning, and invocation models clearly.
- [inference] Community collections are strategically useful because they surface domain-specific artifacts faster than vendor docs do, but they should be adopted as scaffolding rather than as final governance. The correct review question is not “is this prompt popular?” but “is this prompt inspectable, maintained, and anchored to a standard we already trust?”
- [inference] The recommendation that falls out of the evidence is a three-tier policy: **adopt as-is** for low-disagreement, repetitive domains with strong catalogs; **adapt** for high-volume but opinion-sensitive domains; **build internally** for architecture-heavy or semantically loaded domains where public catalogs remain weak.

**Risks, gaps, uncertainties:**

- [fact] Some listed source URLs were inaccessible during investigation, notably the OpenAI prompt-engineering guide (HTTP 403) and `cursor.directory` (HTTP 429), so claims relying on those pages were avoided.
- [inference] Public catalogs can change quickly; counts and breadth judgments here are accurate to the inspected dates but may drift within weeks.
- [inference] Community curation quality is uneven. Even a strong catalog can include outdated or opinionated artifacts that are unsuitable for organizational standardization without review.
- [inference] This survey measured public inspectability and apparent breadth, not execution quality under a controlled benchmark. A team may still need trial installs before committing to wide adoption.

**Open questions:**

- Which subset of `awesome-copilot` or `awesome-agent-skills` aligns best with a rigorous enterprise review process for security, architecture, and testing?
- Should internal standardisation effort center on `AGENTS.md` plus portable skills, or on tool-native collections such as Copilot plugins and Cursor rules?
- Is there enough public demand to justify building a new curated catalog specifically for DDD, CQRS, Kafka ECST, and data-architecture prompts?
- Can standards-oriented prompt linting be automated so that a prompt file can be validated against ASVS, OpenAPI, AsyncAPI, or 12-Factor requirements before adoption?

### §7 Recursive Review

- [fact] The recursive review pass re-checked the main comparative judgments against first-party mechanism documentation, curated catalog indexes, and engineering standards pages to confirm that the synthesis still rests on cited external evidence. Sources: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0
- [inference] The most material remaining uncertainty is still coverage absence rather than mechanism existence: public sources clearly confirm customization surfaces across vendors, while thin architecture-domain coverage may still reflect under-publication of reusable prompts rather than true non-existence. Sources: https://code.visualstudio.com/docs/copilot/copilot-customization ; https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/skills ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules ; https://martinfowler.com/bliki/CQRS.html
- [fact] The access limitations encountered during investigation were confined to a small set of URLs and were mitigated with accessible first-party replacements, so the final synthesis does not rely on inaccessible pages for its core claims. Sources: https://platform.openai.com/docs/guides/prompt-engineering ; https://cookbook.openai.com/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cursor.directory/ ; https://cursor.com/docs/rules ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html

---

## Findings

### Executive Summary

- [inference] The most adoptable public answer today is a portable stack rather than a single canonical library: teams should standardize on `AGENTS.md` or `SKILL.md`-style packaging, then source domain-specific artifacts mainly from `awesome-copilot` and the strongest curated community catalogs for repetitive domains such as .NET, Python backend, API design, testing, security, and database work (https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md).
- [inference] The survey found that all major coding-assistant vendors now expose persistent customization mechanisms, but only GitHub / Microsoft surfaced a large public vendor-backed engineering catalog at the scale seen in `awesome-copilot`, while Anthropic and OpenAI primarily surfaced the skill mechanism and exemplar bundles rather than a broad domain library (https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot ; https://code.visualstudio.com/docs/copilot/copilot-customization ; https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills).
- [inference] Standardization is realistic now for framework-bound domains with repeated public examples, but not yet for DDD, CQRS, Kafka ECST, data modelling, data architecture, and semantic extraction, where public artifacts remain sparse or depend heavily on local architectural judgment (https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://airflow.apache.org/docs/).
- [inference] Teams that want to remove opinion should therefore treat public prompts and skills as governed starting points, then bind them to external standards such as OWASP ASVS, OpenAPI, AsyncAPI, and 12-Factor before broad adoption (https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/).

### Key Findings

1. [inference] **[high confidence]** The public market is split between packaging mechanisms and domain catalogs, with GitHub / Microsoft leading the catalog side through `awesome-copilot` while Anthropic and OpenAI more clearly lead the published skill-packaging pattern through reusable `SKILL.md` bundles (https://github.com/github/awesome-copilot ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins ; https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills).
2. [inference] **[high confidence]** Anthropic and OpenAI independently document `SKILL.md`-based bundles with progressive disclosure, bundled resources, and reusable workflows, which indicates that packaged skills are now a first-party product pattern rather than a purely community convention (https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cookbook.openai.com/examples/skills_in_api).
3. [inference] **[high confidence]** Cursor, Windsurf, Cline, and JetBrains confirm that persistent customization is now mainstream across coding assistants, but their published first-party materials currently emphasize configuration surfaces more than a single installable cross-domain engineering library (https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/memories ; https://docs.windsurf.com/windsurf/cascade/skills ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html).
4. [inference] **[high confidence]** Curated community catalogs are where the widest public experimentation is visible today, because they aggregate many narrow artifacts across frontend, backend, API, testing, database, and notebook use cases that no single non-GitHub vendor catalog exposed at comparable breadth in this survey (https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://github.com/github/awesome-copilot).
5. [inference] **[high confidence]** `AGENTS.md` and `SKILL.md` are the safest medium-term formats to standardize around, because multiple vendors now acknowledge them and because they fit naturally into version control, code review, and repository governance workflows (https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://docs.windsurf.com/windsurf/cascade/skills).
6. [inference] **[high confidence]** Public material is strongest where engineering work is repetitive and framework-bound, which is why .NET, Python backend, API design, testing, security, and database work surfaced repeatedly across the most credible public catalogs inspected here (https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins).
7. [inference] **[medium confidence]** Public material is weakest where design quality depends on organisation-specific semantics or deep architectural trade-offs, which is why DDD, CQRS, Kafka ECST, data architecture, data modelling, classification, and semantic extraction remained thin across the strongest public catalogs (https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules ; https://airflow.apache.org/docs/).
8. [inference] **[high confidence]** A responsible adoption policy is therefore triage-based: adopt faster in low-disagreement domains, adapt with local review in medium-context domains, and build internally for architecture-heavy domains where public catalogs remain sparse or overly opinionated (https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/ ; https://martinfowler.com/bliki/CQRS.html).

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] GitHub / Microsoft lead the public catalog layer in this survey, while Anthropic and OpenAI lead the published skill-packaging pattern. | https://github.com/github/awesome-copilot ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins ; https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://developers.openai.com/api/docs/guides/tools-skills | high | This is a comparative synthesis across the strongest first-party public sources inspected. |
| [fact] Anthropic and OpenAI both document reusable `SKILL.md` bundles with bundled resources and workflows. | https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cookbook.openai.com/examples/skills_in_api | high | Independent first-party docs converge on the same packaging pattern. |
| [inference] Persistent customization is mainstream across major coding assistants, even where public first-party domain catalogs remain limited. | https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/memories ; https://docs.windsurf.com/windsurf/cascade/skills ; https://docs.cline.bot/ ; https://www.jetbrains.com/help/ai-assistant/prompt-library.html ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html | high | Product docs establish the mechanism surface; the absence of large official catalogs is a synthesis judgment. |
| [inference] Curated community catalogs expose broader public experimentation than most non-GitHub first-party libraries. | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://github.com/github/awesome-copilot | high | Breadth is visible in domain lists, counts, and repository structure. |
| [inference] Portable formats such as `AGENTS.md` and `SKILL.md` are the safest standardization substrate. | https://agents.md/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://support.claude.com/en/articles/12512198-creating-custom-skills ; https://docs.windsurf.com/windsurf/cascade/skills | high | Multiple vendors and communities point to the same portability pattern. |
| [inference] Public coverage clusters in repetitive, framework-bound engineering domains. | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://developer.microsoft.com/blog/awesome-github-copilot-just-got-a-website-and-a-learning-hub-and-plugins | high | The strongest catalogs repeatedly surface these categories with installable artifacts. |
| [inference] Public coverage thins out in architecture-heavy and semantically loaded domains. | https://martinfowler.com/bliki/CQRS.html ; https://martinfowler.com/articles/201701-event-driven.html ; https://airflow.apache.org/docs/ ; https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | medium | Standards and tooling docs exist, but trusted prompt catalogs remain sparse. |
| [inference] External engineering standards are required to govern prompt adoption responsibly. | https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/ | high | These standards provide the normative layer that prompt libraries alone do not guarantee. |

### Domain Coverage Matrix

| Domain | Label | Best public source(s) | Coverage | Adoption view |
|---|---|---|---|---|
| UI/UX development | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/anthropics/skills/main/README.md | high | Strong public examples exist; adopt selectively with local design-system constraints. |
| Python backend development | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | high | One of the strongest public domains; adoption is viable after project-specific testing and security alignment. |
| Data architecture | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | Standards and tools exist, but public prompt/skill packs remain thin; build internally. |
| Data modelling | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Some database-related rules exist, but robust data-modelling prompt libraries did not strongly surface. |
| Software architecture | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium | Good reviewer and blueprint artifacts exist, but wholesale adoption still needs local architecture principles. |
| SOLID software design | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium | Community rules exist; adopt only after aligning terminology and examples to house style. |
| Clean code | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html | medium | Easy to standardize, but many artifacts are opinionated and need local review. |
| Clean architecture | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low-medium | Public examples exist, but not a dominant, standards-grounded catalog. |
| API design | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ | high | Strong public support exists; adopt with OpenAPI / AsyncAPI as the normative layer. |
| DDD | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Public DDD prompt libraries did not strongly surface; do not standardize from public prompts alone. |
| .NET API development | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://github.com/github/awesome-copilot | high | Strong public guidance exists in vendor-backed Copilot assets. |
| Kafka event design for ECST | [inference] | https://martinfowler.com/articles/201701-event-driven.html ; https://github.com/PatrickJS/awesome-cursorrules | low | Conceptual standards exist, but prompt catalogs are sparse and not adoption-ready. |
| .NET architecture | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium-high | Good public material exists, but enterprise architecture still needs local adaptation. |
| .NET CQRS | [inference] | https://martinfowler.com/bliki/CQRS.html ; https://github.com/github/awesome-copilot | low | Public CQRS prompts are far weaker than the underlying architectural literature. |
| Database design | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium-high | Good practical artifacts exist, but schema and operational decisions remain context-dependent. |
| Data pipelines | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | medium | Supporting public material exists, but domain-specific prompt packs are not yet dominant. |
| Design | [inference] | https://raw.githubusercontent.com/anthropics/skills/main/README.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | medium | Plenty of creative/design artifacts exist, but engineering-standard alignment is uneven. |
| Data visualisation | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://jupyter.org/ | medium | Good notebook- and plotting-oriented examples exist; adopt with local charting conventions. |
| Classification | [inference] | https://github.com/github/awesome-copilot ; https://github.com/PatrickJS/awesome-cursorrules | low | Public catalogs did not surface strong, high-trust classification prompt packs. |
| Semantic and concept extraction | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | A few adjacent semantics-oriented artifacts exist, but coverage is shallow and fragmented. |
| Unit testing | [inference] | https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md | high | One of the most mature public prompt domains; adoption is viable after aligning to test framework choices. |
| E2E testing | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://github.com/github/awesome-copilot | medium-high | Strong Cypress / Playwright examples exist, though they still need environment-specific adaptation. |
| Integration testing | [inference] | https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://github.com/github/awesome-copilot | medium-high | Good public artifacts exist, especially around web stacks and migrations. |
| Security architecture | [inference] | https://owasp.org/www-project-application-security-verification-standard/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md | medium | Public prompts help, but the authoritative baseline is the security standard, not the prompt file. |
| Security engineering | [inference] | https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://owasp.org/www-project-application-security-verification-standard/ | high | Security-oriented prompts exist, and they can be anchored to ASVS for stronger standardization. |
| Apache Airflow | [inference] | https://airflow.apache.org/docs/ ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md | low | Official domain docs are rich, but prompt libraries are not yet strong enough for broad as-is adoption. |
| Jupyter Notebooks | [inference] | https://jupyter.org/ ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://docs.cline.bot/ | medium | Public notebook-oriented rules exist, but they are mostly community examples rather than vendor-backed standards. |

### Assumptions

- [assumption] Public absence in first-party docs is treated as absence of a **publicly inspectable** official library on 2026-03-22, not as proof that no private or enterprise-only library exists. **Justification:** this item is explicitly constrained to public sources.
- [assumption] GitHub repository metadata and file-category structure are used as proxies for maintenance and breadth, not as direct evidence of prompt quality. **Justification:** quality still requires human review and standards alignment.
- [assumption] Domains marked “low” coverage may still have isolated niche examples on the web. **Justification:** the strongest catalogs inspected here were broad enough that repeated absence across them is meaningful, but not mathematically exhaustive.

### Analysis

- [fact] I weighted first-party product documentation highest for mechanism existence, because vendors are the authoritative source for whether a tool supports repository instructions, prompt files, rules, skills, or agent guidance. Sources: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot ; https://code.visualstudio.com/docs/copilot/copilot-customization ; https://cursor.com/docs/rules ; https://docs.windsurf.com/windsurf/cascade/skills ; https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html
- [fact] I weighted catalog repositories and published indexes highest for breadth and maintenance signals, because those artifacts expose installation paths, category structures, curated counts, and domain coverage directly. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [inference] Comparative judgments such as “strongest public coverage” were treated as synthesis across multiple catalogs rather than as claims made by any one source, which is why those findings are labeled as inferences instead of facts. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [inference] The final adoption recommendation separates **adopt**, **adapt**, and **build internally** based on two dimensions: whether a reusable public artifact exists and whether an external engineering standard exists to constrain local variation after adoption. Sources: https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0 ; https://www.asyncapi.com/ ; https://12factor.net/ ; https://martinfowler.com/bliki/CQRS.html

### Risks, Gaps, and Uncertainties

- [fact] Some listed source URLs were inaccessible during investigation, notably the OpenAI prompt-engineering guide (HTTP 403) and `cursor.directory` (HTTP 429), so claims relying on those pages were avoided. Sources: https://platform.openai.com/docs/guides/prompt-engineering ; https://cursor.directory/ ; https://cookbook.openai.com/ ; https://developers.openai.com/api/docs/guides/tools-skills ; https://cursor.com/docs/rules
- [inference] Public catalogs can change quickly; counts and breadth judgments here are accurate to the inspected dates but may drift within weeks as repositories add, remove, or reorganize artifacts. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md
- [inference] Community curation quality is uneven, so even a strong catalog can include outdated or opinionated artifacts that are unsuitable for organizational standardization without review against external engineering standards. Sources: https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/README.md ; https://raw.githubusercontent.com/VoltAgent/awesome-agent-skills/main/README.md ; https://owasp.org/www-project-application-security-verification-standard/ ; https://spec.openapis.org/oas/v3.1.0
- [inference] This survey measured public inspectability and apparent breadth rather than execution quality under a controlled benchmark, so teams should still perform trial installs before committing to wide adoption. Sources: https://github.com/github/awesome-copilot ; https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md ; https://raw.githubusercontent.com/anthropics/skills/main/README.md

### Open Questions

- Which subset of `awesome-copilot` or `awesome-agent-skills` aligns best with a rigorous enterprise review process for security, architecture, and testing?
- Should internal standardisation effort center on `AGENTS.md` plus portable skills, or on tool-native collections such as Copilot plugins and Cursor rules?
- Is there enough public demand to justify building a new curated catalog specifically for DDD, CQRS, Kafka ECST, and data-architecture prompts?
- Can standards-oriented prompt linting be automated so that a prompt file can be validated against ASVS, OpenAPI, AsyncAPI, or 12-Factor requirements before adoption?

## Output

- Type: knowledge
- Description: Survey of public vendor and OSS prompt/skill ecosystems for software-engineering work, including adoption-readiness guidance and a full domain coverage matrix across the requested domains.
- Links:
  - https://github.com/github/awesome-copilot
  - https://raw.githubusercontent.com/anthropics/skills/main/README.md
  - https://agents.md/
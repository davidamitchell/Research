# Session: New Research Item — Coding AI Agent Skills Survey

**Date:** 2026-03-22
**Slug:** coding-ai-agent-skills-backlog
**Issue:** Coding AI - agent skills - new research

---

## What Was Done

Created a new research backlog item:
`Research/backlog/2026-03-22-coding-ai-agent-skills-survey.md`

The item addresses the issue's request to survey what already exists in terms of vendor and OSS community agent skills, prompt libraries, instructions files, and system prompts for 25+ software engineering domains, including: UI/UX (User Interface/User Experience) development, Python backend development, DDD (Domain-Driven Design), CQRS (Command Query Responsibility Segregation), SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) design, clean architecture, API (Application Programming Interface) design, .NET architecture, Kafka ECST (Event-Carried State Transfer), database design, data pipelines, testing (unit, integration, E2E (End-to-End)), security architecture, security engineering, Apache Airflow, Jupyter Notebooks, and others.

## Conventions Followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present: `status: backlog`, `started: ~`, `completed: ~`
- Priority set to `high` — this item directly unblocks any prompt/skill development work and has clear downstream impact on standardising AI-assisted development
- Research Skill Output and Findings sections left blank for the research agent to fill
- Acronyms expanded on first use throughout: UI/UX, OSS, API, DDD, CQRS, SOLID, ECST, E2E, RAG, OWASP, ASVS, NIST, CSF, DORA

## Decisions Made

- **Priority: high** — because the outcome directly unblocks tooling and skills development across multiple engineering domains; without this survey, any prompt/skill authoring risks duplicating existing vendor or community work.
- **Output type: knowledge** — the primary output is a curated catalogue and adoption recommendation, not a new tool or skill file (though those may be produced as downstream backlog items).
- **Scope deliberately broad** — the issue lists 25+ domains; the research question encompasses all of them to produce a coverage matrix, rather than artificially narrowing to a subset.

## Mini-Retro

1. **Did the process work?** Yes — the issue was well-specified with a clear list of domains and a clear goal (find what exists, don't reinvent the wheel), which translated cleanly into the template structure.
2. **What slowed down or went wrong?** Nothing significant. The main decision was how to phrase the research question to cover all listed domains without being unwieldy — resolved by leading with the specific question and listing all domains inline, with all acronyms expanded.
3. **What single change would prevent friction next time?** Nothing to change — the template and conventions handled this well.
4. **Is this a pattern?** No — a survey-type research item with a broad domain list is a slightly unusual pattern, but the template accommodates it cleanly via the domain coverage matrix in the Approach section.

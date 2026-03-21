# Session: New Research Item — Dependency Mapping Across .NET, Terraform, Dynatrace, Confluence, Log Aggregation, and CSDM

Date: 2026-03-21
Issue: Dependancy mapping

## Work Done

- Created `Research/backlog/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md` from `Research/_template.md`
- Research question scoped to practical tooling and methodology for multi-surface dependency mapping, incorporating the issue's explicit constraints (imperfect sources, locally-running agents)

## Conventions Followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`
- Research Skill Output and Findings sections left blank for the research agent to fill
- Acronyms expanded on first use:
  - Application Performance Management (APM)
  - Configuration and Service Data Model (CSDM)
  - Infrastructure as Code (IaC)
  - Configuration Management Database (CMDB)
  - Large Language Model (LLM)

## Decisions

- **CSDM expansion**: The issue refers to "csdms" — expanded as Configuration and Service Data Model (CSDM), the ServiceNow framework for modelling application and infrastructure relationships. This is the most common enterprise usage of the acronym and aligns with Dynatrace/Terraform/Confluence context.
- **Scope**: Kept tight to the five surfaces named in the issue plus CSDM and log aggregation. Deliberately excluded microservice mesh tools and security-specific dependency scanning to avoid scope creep.
- **Priority: high** — the question is operationally urgent (existing-state architecture understanding) and involves multiple active enterprise tooling surfaces.
- **Sources**: Seeded with specific tooling documentation URLs and search strategies. Practitioner accounts (InfoQ, Thoughtworks Radar, community forums) included alongside vendor docs, as this is a practical rather than academic question.

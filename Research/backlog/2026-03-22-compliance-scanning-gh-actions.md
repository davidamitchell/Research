---
title: "Compliance Scanning via GitHub Actions — Broad Policy as Code Across a Heterogeneous Stack"
added: 2026-03-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [github-actions, policy-as-code, compliance, codeql, ghas, dotnet, kubernetes, eventing, rest-api, graph-api, python, react, airflow, dbt, snowflake, rds, golang, terraform, ansible]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Compliance Scanning via GitHub Actions — Broad Policy as Code Across a Heterogeneous Stack

## Research Question

How can GitHub Actions (with GitHub Advanced Security (GHAS) and CodeQL already enabled) be extended to enforce a broad, organisation-wide compliance policy — covering naming conventions, architectural patterns, directory layout, API specifications, event schemas, and technology-stack-specific usage rules — across a heterogeneous estate of .NET, Kubernetes (k8s), Python, React, Go, Airflow, DBT, Snowflake, Relational Database Service (RDS), Terraform, Ansible, REST APIs, Graph APIs, and event-driven systems, where policies are defined once and shared across multiple enforcement points?

## Scope

**In scope:**
- GitHub Actions workflows as a compliance enforcement layer
- GitHub Advanced Security (GHAS) and CodeQL as the baseline scanning foundation
- Policy as Code (PaC) patterns that go beyond language-level static analysis: directory layout, naming conventions, usage patterns, Architectural Decision Records (ADRs), API specification conformance (OpenAPI / AsyncAPI), event schema validation, Infrastructure as Code (IaC) policy
- Policy definition and sharing mechanisms: centralised policy repositories, reusable GitHub Actions, composite actions, custom CodeQL packs/queries, and external policy engines (Open Policy Agent (OPA), Spectral, Semgrep, etc.)
- Technology stacks explicitly called out in the issue: .NET, Kubernetes (k8s), Python, React, Go (Golang), Apache Airflow, DBT (Data Build Tool), Snowflake, Relational Database Service (RDS), Terraform, Ansible, REST APIs (OpenAPI), Graph APIs (GraphQL), eventing (AsyncAPI / CloudEvents)
- Practical, runnable workflow patterns — not theoretical overviews
- How to scale one policy set across many repositories (inner-source model, GitHub rulesets, required workflows)

**Out of scope:**
- Runtime compliance monitoring (this is pre-merge / Continuous Integration (CI) only)
- Identity and Access Management (IAM) / authorisation policy (covered separately in adaptive-policy-authorization-compliance)
- Detailed setup of GHAS or CodeQL from scratch (assumed already operational per issue)
- Commercial third-party tools without a GitHub Actions integration path

**Constraints:** Publicly accessible documentation, open-source tooling, and GitHub Actions marketplace — no proprietary internal tooling assumed.

## Context

The organisation already has GHAS and CodeQL running. The next evolution is extending that baseline into a comprehensive compliance scanning layer that enforces standards beyond what CodeQL provides natively — directory structure, naming conventions, API/event specification conformance, architecture alignment, and stack-specific usage rules (e.g., no raw SQL in Airflow tasks, all Terraform modules must declare required providers, all REST APIs must have an OpenAPI 3.x spec, all Go services must follow a defined module layout). The ambition is "Policy as Code" where policy is defined once (likely in a shared repository or GitHub organisation-level configuration) and consumed at each enforcement point — the pull request (PR) check, the release gate, the scheduled audit — across a heterogeneous estate of at least 13 technology stacks. A related completed item on adaptive policy authorisation compliance (2026-03-16-adaptive-policy-authorization-compliance) covers the authorisation side; this item focuses on the development-pipeline scanning side.

## Approach

1. Survey what GHAS and CodeQL natively cover for each named stack, and identify the coverage gaps that require additional tooling.
2. Identify the leading open-source / GitHub-integrated PaC tools that fill each gap category (naming/layout, API specs, event schemas, IaC, stack-specific lint): Semgrep, OPA/Conftest, Spectral, Checkov, Trivy, Kube-score, SQLFluff, dbt-project-evaluator, golangci-lint, ESLint, Ruff, etc.
3. Investigate policy sharing patterns across repositories: GitHub Required Workflows, GitHub Reusable Workflows, composite actions, shared CodeQL packs published to GitHub Packages, OPA bundle servers, and Spectral rulesets hosted in a shared repo.
4. Map each named technology stack to the specific compliance dimensions (naming, layout, API spec, event spec, usage, architecture) and the recommended enforcement tool/mechanism for each.
5. Prototype or locate reference implementations of a "centralised policy → distributed enforcement" pattern in GitHub Actions — specifically how one policy definition triggers checks across multiple repos without copy-paste duplication.
6. Assess trade-offs: maintenance overhead, false positive rates, developer experience friction, and incremental adoption paths from "GHAS only" to "full broad PaC".
7. Identify any open questions or follow-on backlog items surfaced by the research.

## Sources

- [ ] GitHub Docs — Required workflows (org-level): https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [ ] GitHub Docs — Reusable workflows: https://docs.github.com/en/actions/sharing-automations/reusing-workflows
- [ ] GitHub Docs — CodeQL custom queries and packs: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs
- [ ] Open Policy Agent (OPA) — Conftest for CI: https://www.conftest.dev/
- [ ] Spectral (API linting for OpenAPI / AsyncAPI): https://docs.stoplight.io/docs/spectral/
- [ ] Semgrep — custom rules for language/pattern enforcement: https://semgrep.dev/docs/writing-rules/overview
- [ ] Checkov — IaC scanning (Terraform, Ansible, k8s): https://www.checkov.io/
- [ ] dbt-project-evaluator — DBT project structure linting: https://github.com/dbt-labs/dbt-project-evaluator
- [ ] SQLFluff — SQL linting (Snowflake, RDS): https://sqlfluff.com/
- [ ] golangci-lint — Go static analysis composite: https://golangci-lint.run/
- [ ] kube-score — Kubernetes manifest scoring: https://kube-score.com/
- [ ] AsyncAPI / CloudEvents schema validation tooling: https://www.asyncapi.com/tools/cli
- [ ] Search for published examples of "centralised GitHub Actions compliance" or "policy as code monorepo GitHub" patterns

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

- Type: knowledge, backlog-item
- Description:
- Links:

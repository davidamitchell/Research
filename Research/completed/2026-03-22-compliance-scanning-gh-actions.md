---
review_count: 2
title: "Compliance Scanning via GitHub Actions — Broad Policy as Code Across a Heterogeneous Stack"
added: 2026-03-22
status: completed
priority: high  # low | medium | high
blocks: []
tags: [github-actions, policy-as-code, compliance, codeql, ghas, dotnet, kubernetes, eventing, rest-api, graph-api, python, react, airflow, dbt, snowflake, rds, golang, terraform, ansible]
started: 2026-03-22
completed: 2026-03-22
output: [knowledge, backlog-item]
---

# Compliance Scanning via GitHub Actions — Broad Policy as Code Across a Heterogeneous Stack

## Research Question

How can GitHub Actions (with GitHub Advanced Security (GHAS) and CodeQL already enabled) be extended to enforce a broad, organisation-wide compliance policy — covering naming conventions, architectural patterns, directory layout, Application Programming Interface (API) specifications, event schemas, and technology-stack-specific usage rules — across a heterogeneous estate of .NET, Kubernetes (k8s), Python, React, Go, Airflow, DBT (Data Build Tool), Snowflake, Relational Database Service (RDS), Terraform, Ansible, Representational State Transfer (REST) APIs, Graph APIs (GraphQL), and event-driven systems, where policies are defined once and shared across multiple enforcement points?

## Scope

**In scope:**
- GitHub Actions workflows as a compliance enforcement layer
- GitHub Advanced Security (GHAS) and CodeQL as the baseline scanning foundation
- Policy as Code (PaC) patterns that go beyond language-level static analysis: directory layout, naming conventions, usage patterns, Architectural Decision Records (ADRs), API specification conformance (OpenAPI / AsyncAPI), event schema validation, Infrastructure as Code (IaC) policy
- Policy definition and sharing mechanisms: centralised policy repositories, reusable GitHub Actions, composite actions, custom CodeQL packs/queries, and external policy engines (Open Policy Agent (OPA), Spectral, Semgrep, etc.)
- Technology stacks explicitly called out in the issue: .NET, Kubernetes (k8s), Python, React, Go (Golang), Apache Airflow, DBT (Data Build Tool), Snowflake, Relational Database Service (RDS), Terraform, Ansible, REST APIs (OpenAPI), Graph APIs (GraphQL), eventing (AsyncAPI / CloudEvents)
- Practical, runnable workflow patterns — not theoretical overviews
- How to scale one policy set across multiple repositories (inner-source model, GitHub rulesets, required workflows)

**Out of scope:**
- Runtime compliance monitoring (this is pre-merge / Continuous Integration (CI) only)
- Identity and Access Management (IAM) / authorisation policy (covered separately in adaptive-policy-authorization-compliance)
- Detailed setup of GHAS or CodeQL from scratch (assumed already operational per issue)
- Commercial third-party tools without a GitHub Actions integration path

**Constraints:** Publicly accessible documentation, open-source tooling, and GitHub Actions marketplace — no proprietary internal tooling assumed.

## Context

The organisation already has GHAS and CodeQL running. The next evolution is extending that baseline into a comprehensive compliance scanning layer that enforces standards beyond what CodeQL provides natively — directory structure, naming conventions, API/event specification conformance, architecture alignment, and stack-specific usage rules (for example, no raw SQL in Airflow tasks, all Terraform modules must declare required providers, all REST APIs must have an OpenAPI 3.x spec, and all Go services must follow a defined module layout). The ambition is "Policy as Code" where policy is defined once and consumed at each enforcement point — the pull request (PR) check, the release gate, and the scheduled audit — across a heterogeneous estate of at least 13 technology stacks. A related completed item on adaptive policy authorisation compliance (`2026-03-16-adaptive-policy-authorization-compliance`) covers the authorisation side; this item focuses on the development-pipeline scanning side.

## Approach

1. Survey what GHAS and CodeQL natively cover for each named stack, and identify the coverage gaps that require additional tooling.
2. Identify the leading open-source / GitHub-integrated PaC tools that fill each gap category (naming/layout, API specs, event schemas, IaC, stack-specific lint): Semgrep, OPA/Conftest, Spectral, Checkov, kube-score, SQLFluff, dbt-project-evaluator, golangci-lint, GraphQL Inspector, Ruff, etc.
3. Investigate policy sharing patterns across repositories: GitHub rulesets, reusable workflows, composite actions, shared CodeQL packs published to GitHub Container Registry, and central policy repositories.
4. Map each named technology stack to the specific compliance dimensions (naming, layout, API spec, event spec, usage, architecture) and the recommended enforcement tool/mechanism for each.
5. Locate at least one published "centralised policy -> distributed enforcement" pattern in GitHub Actions.
6. Assess trade-offs: maintenance overhead, false positive rates, developer experience friction, and incremental adoption paths from "GHAS only" to "full broad PaC".
7. Identify open questions or follow-on backlog items surfaced by the research.

## Sources

- [x] GitHub Docs — Available rules for rulesets / require workflows to pass before merging: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [x] GitHub Docs — Reusable workflows: https://docs.github.com/en/actions/sharing-automations/reusing-workflows
- [x] GitHub Docs — Creating organisation rulesets: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization
- [x] GitHub Docs — About code scanning with CodeQL: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql
- [x] CodeQL docs — Supported languages and frameworks: https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
- [x] GitHub Docs — CodeQL custom queries and packs: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs
- [x] GitHub Blog — Required workflows and configuration variables: https://github.blog/enterprise-software/devops/introducing-required-workflows-and-configuration-variables-to-github-actions/
- [x] GitHub Well-Architected — Rulesets best practices: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
- [x] Open Policy Agent (OPA) / Conftest: https://www.conftest.dev/
- [x] Semgrep rule-writing overview: https://semgrep.dev/docs/writing-rules/overview
- [x] Spectral repository and documentation entry point: https://github.com/stoplightio/spectral
- [ ] Original Stoplight Spectral documentation page in the seed item returned 404 at retrieval time: https://docs.stoplight.io/docs/spectral/
- [x] Checkov documentation and repository: https://www.checkov.io/ ; https://github.com/bridgecrewio/checkov
- [x] AWS Prescriptive Guidance — centralised custom Checkov scanning: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [x] dbt-project-evaluator repository: https://github.com/dbt-labs/dbt-project-evaluator
- [x] SQLFluff documentation: https://sqlfluff.com/
- [x] golangci-lint documentation and repository: https://golangci-lint.run/ ; https://github.com/golangci/golangci-lint
- [x] kube-score repository: https://github.com/zegl/kube-score
- [x] AsyncAPI Command Line Interface (CLI): https://www.asyncapi.com/tools/cli
- [x] GraphQL Inspector docs: https://the-guild.dev/graphql/inspector/docs/index
- [x] Ruff docs: https://docs.astral.sh/ruff/
- [x] Prior related item — adaptive policy authorisation compliance: `Research/completed/2026-03-16-adaptive-policy-authorization-compliance.md`
- [x] Prior related item — agent Language Server Protocol (LSP) policy enforcement: `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md`

---

## Research Skill Output

### §0 Initialise

- [fact] **Research question restated:** the task is to determine how an organisation that already runs GHAS and CodeQL can extend GitHub Actions into a shared compliance platform for naming, structure, architecture, API and event specifications, and stack-specific engineering rules across heterogeneous repositories. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-22-compliance-scanning-gh-actions.md
- [fact] **Scope confirmation:** the question is about pre-merge and scheduled compliance enforcement in GitHub Actions, not runtime control enforcement, identity policy, or a greenfield GHAS installation. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-22-compliance-scanning-gh-actions.md
- [fact] **Output format:** the required deliverable is a fully sourced knowledge item with claim labels, a stack map, a minimum viable architecture, trade-offs, and open questions that can become backlog items. Sources: https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-22-compliance-scanning-gh-actions.md
- [fact] **Prior work cross-reference:** `2026-03-16-adaptive-policy-authorization-compliance.md` established that PaC engines such as OPA, Cedar, and Cerbos are valuable when they produce durable review, validation, and audit artefacts, and `2026-03-01-agent-lsp-policy-enforcement.md` established that policy feedback loops usually need a custom bridge when the native tool is not agent-aware. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-16-adaptive-policy-authorization-compliance.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-01-agent-lsp-policy-enforcement.md

### §1 Question Decomposition

- **1. GHAS / CodeQL baseline**
  - 1.1 Which languages and artefacts does CodeQL natively support?
  - 1.2 Which parts of the named heterogeneous stack are outside CodeQL's native scope?
  - 1.3 What can custom CodeQL packs extend, and what can they not realistically replace?
- **2. Gap-filling policy tools**
  - 2.1 Which tools can enforce generic repository and code-pattern rules?
  - 2.2 Which tools can enforce IaC and Kubernetes policy?
  - 2.3 Which tools can enforce API, GraphQL, and event-schema conformance?
  - 2.4 Which tools can enforce data-platform and SQL project structure rules?
- **3. Shared-enforcement architecture**
  - 3.1 How are workflows shared across repositories?
  - 3.2 How are checks made mandatory across many repositories?
  - 3.3 What published examples exist for central policy repositories plus distributed enforcement?
- **4. Operational design**
  - 4.1 What is the minimum viable architecture?
  - 4.2 What are the main rollout risks, friction points, and exception-handling needs?
  - 4.3 Which open questions remain unresolved by the current open-source evidence?

### §2 Investigation

#### 2.1 GHAS and CodeQL baseline

- [fact] GitHub's CodeQL documentation says CodeQL supports C/C++, C#, Go, Java/Kotlin, JavaScript/TypeScript, Python, Ruby, Rust, Swift, and GitHub Actions workflows. Source (primary): https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql
- [fact] The CodeQL supported-languages page explicitly lists C#, Go, JavaScript, TypeScript, Python, and GitHub Actions as built-in supported languages or artefacts, with framework coverage defined per language pack. Source (primary): https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
- [fact] GitHub documents that additional queries can be delivered as published CodeQL packs, and packs are versioned and distributed through GitHub Container Registry. Source (primary): https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs
- [inference] GHAS plus CodeQL is therefore a strong baseline for security scanning in the source languages present in the estate (.NET via C#, React via JavaScript/TypeScript, Go, Python, and GitHub Actions itself), but it is not a broad compliance platform for repository structure, OpenAPI or AsyncAPI conformance, Terraform semantics, Kubernetes manifest hygiene, SQL style, or dbt project conventions. Basis: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ ; https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-22-compliance-scanning-gh-actions.md
- [inference] Custom CodeQL packs can extend analysis inside supported CodeQL ecosystems, but they do not remove the need for specialised scanners when the artefact to validate is a schema, manifest, workflow topology, SQL dialect, or project layout rather than source-code dataflow. Basis: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/

#### 2.2 Shared GitHub enforcement primitives

- [fact] GitHub reusable workflows must live in `.github/workflows`, be triggered with `workflow_call`, and can accept typed inputs and secrets from caller workflows. Source (primary): https://docs.github.com/en/actions/sharing-automations/reusing-workflows
- [fact] GitHub organisation rulesets can target multiple repositories, and the ruleset guidance explicitly says organisation owners can create rulesets to control how users interact with repositories across the organisation. Source (primary): https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization
- [fact] GitHub's rulesets documentation includes a rule to require workflows to pass before merging, and the rulesets page says rulesets are available across GitHub plans with enterprise and team scope depending on repository type and rule type. Source (primary): https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [fact] GitHub's Well-Architected rulesets guidance recommends centralising critical workflows, using required workflows and status checks for organisation-wide gates, versioning them in reusable workflow repositories, and rolling out in Evaluate mode before enforcement. Source (secondary but GitHub-authored): https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
- [fact] GitHub's required-workflows blog states that required workflows were introduced to define and enforce standard Continuous Integration / Continuous Delivery (CI/CD) practices across multiple repositories without configuring each repository individually, and that they block pull request merges until the required workflow succeeds. Source (secondary but GitHub-authored): https://github.blog/enterprise-software/devops/introducing-required-workflows-and-configuration-variables-to-github-actions/
- [inference] The scalable GitHub-native control plane is a two-layer model: reusable workflows hold the scanning logic, while rulesets and required status checks make the resulting workflow outcomes mandatory across selected repositories. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging

#### 2.3 Generic policy and pattern scanners

- [fact] Semgrep documents that custom rule files can detect security issues, style violations, and configuration problems, which makes Semgrep suitable for organisation-specific code-pattern checks that are broader than vulnerability signatures. Source (primary): https://semgrep.dev/docs/writing-rules/overview
- [fact] Conftest documents that it evaluates structured configuration data with Rego policies and supports formats including YAML Ain't Markup Language (YAML), JavaScript Object Notation (JSON), Tom's Obvious, Minimal Language (TOML), HashiCorp Configuration Language (HCL/HCL2), Dockerfile, eXtensible Markup Language (XML), and more, and it can emit GitHub-formatted annotations. Source (primary): https://www.conftest.dev/
- [fact] Spectral's repository readme states that Spectral supports custom rulesets for JSON or YAML objects, includes ready-to-use rulesets for OpenAPI v2/v3.x, AsyncAPI, and Arazzo, and can be run as a CLI with a local or custom ruleset. Source (primary): https://github.com/stoplightio/spectral
- [inference] Semgrep is the best fit among the retrieved sources for broad source-code pattern enforcement across .NET, Python, JavaScript/TypeScript, and Go, while Conftest is the best fit for structured configuration and repository-policy assertions that can be expressed over parsed documents rather than source-code abstract syntax trees. Basis: https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/
- [inference] Spectral is the strongest sourced fit for central API-style rules because it already treats OpenAPI and AsyncAPI as first-class ruleset targets and expects policy to be expressed as reusable rulesets rather than embedded per repository. Basis: https://github.com/stoplightio/spectral

#### 2.4 Infrastructure and Kubernetes policy

- [fact] Checkov describes itself as a static analysis tool for IaC and states that it scans Terraform, Terraform plan, CloudFormation, Kubernetes, Helm, Kustomize, Dockerfile, Serverless, Bicep, OpenAPI, Azure Resource Manager (ARM), OpenTofu, Ansible, and GitHub Actions workflows, with over 1000 built-in policies and support for custom policies. Sources (primary): https://www.checkov.io/ ; https://github.com/bridgecrewio/checkov
- [fact] kube-score states that it performs static analysis of Kubernetes object definitions and emits recommendations to improve security and resilience, including checks for probes, security context, network policy, resource limits, and deployment hygiene. Source (primary): https://github.com/zegl/kube-score
- [fact] AWS Prescriptive Guidance publishes a concrete GitHub Actions pattern in which a reusable workflow and custom Checkov policies are centralised in one repository and consumed by many repositories, with policy updates applied centrally and pulled into pipelines automatically. Source (primary for the pattern): https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [inference] Checkov is the broadest single IaC scanner in the retrieved evidence because it spans Terraform, Kubernetes, Ansible, OpenAPI, and GitHub Actions, while kube-score adds Kubernetes-specific resilience and workload-quality checks that Checkov alone does not express with the same operational focus. Basis: https://www.checkov.io/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score
- [inference] The AWS pattern is direct evidence that "define policies once, enforce everywhere" is already practical in GitHub Actions using a central policy repository and reusable workflows, even before adding GitHub organisation rulesets on top. Basis: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://docs.github.com/en/actions/sharing-automations/reusing-workflows

#### 2.5 Data, SQL, and language-ecosystem tooling

- [fact] dbt-project-evaluator states that it tests a dbt project for modelling, testing, documentation, structure, performance, and governance best practices, and supports Snowflake among other adapters. Source (primary): https://github.com/dbt-labs/dbt-project-evaluator
- [fact] SQLFluff describes itself as a dialect-flexible, configurable SQL linter that also works with Jinja templating and dbt. Source (primary): https://sqlfluff.com/
- [fact] golangci-lint describes itself as a fast Go linters runner that runs linters in parallel, supports YAML configuration, and includes over a hundred linters. Sources (primary): https://golangci-lint.run/ ; https://github.com/golangci/golangci-lint
- [fact] Ruff describes itself as an extremely fast Python linter and formatter with over 800 built-in rules, `pyproject.toml` support, and active use in Apache Airflow. Source (primary): https://docs.astral.sh/ruff/
- [inference] DBT and Snowflake compliance need dedicated SQL- and dbt-aware tooling because CodeQL does not natively model dbt project structure or SQL dialect/style semantics, while SQLFluff plus dbt-project-evaluator directly target those domains. Basis: https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
- [inference] Python and Airflow compliance can reuse the same source-policy shell as other languages, but Ruff is the sourced tool in this evidence set that best covers Python style, import, and structural conventions at repository scale. Basis: https://docs.astral.sh/ruff/
- [inference] Go services benefit from golangci-lint for broad idiomatic and quality checks, while Semgrep or CodeQL can be reserved for organisation-specific or security-focused Go policies. Basis: https://golangci-lint.run/ ; https://semgrep.dev/docs/writing-rules/overview ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/

#### 2.6 API, GraphQL, and event-schema tooling

- [fact] AsyncAPI CLI states that it can create, validate, and explore AsyncAPI files, and that document validation is one of its core features. Source (primary): https://www.asyncapi.com/tools/cli
- [fact] GraphQL Inspector states that it can compare two GraphQL schemas, classify changes as breaking, non-breaking, or dangerous, validate documents and fragments against the schema, and is available as a CLI, GitHub App, and GitHub Action. Source (primary): https://the-guild.dev/graphql/inspector/docs/index
- [fact] Spectral's ready-to-use rulesets cover OpenAPI and AsyncAPI documents, and its custom rulesets can lint generic JSON/YAML style-guide requirements. Source (primary): https://github.com/stoplightio/spectral
- [inference] REST and event-driven API governance should be split into two policy layers: schema validity with the domain-specific tool (for example AsyncAPI CLI), and style or consistency policy with a reusable Spectral ruleset. Basis: https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral
- [inference] GraphQL needs a separate policy path from OpenAPI and AsyncAPI because the retrieved sources show GraphQL Inspector as the schema-diff and validation tool, whereas Spectral's first-class built-in coverage in the sourced material is OpenAPI, AsyncAPI, and Arazzo rather than GraphQL. Basis: https://the-guild.dev/graphql/inspector/docs/index ; https://github.com/stoplightio/spectral

#### 2.7 Stack-to-tool enforcement map

- [fact] **.NET / C#:** CodeQL natively supports C#, and Semgrep can add custom pattern rules over source files. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://semgrep.dev/docs/writing-rules/overview
- [fact] **React / JavaScript / TypeScript:** CodeQL natively supports JavaScript and TypeScript, and Semgrep custom rules can enforce repository-specific usage patterns. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://semgrep.dev/docs/writing-rules/overview
- [fact] **Python / Airflow:** CodeQL supports Python, Ruff provides Python linting and formatting rules at scale, and Ruff is used in Apache Airflow. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://docs.astral.sh/ruff/
- [fact] **Go:** CodeQL supports Go and golangci-lint aggregates Go linters under one configuration surface. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://golangci-lint.run/
- [fact] **Terraform / Ansible / generic IaC:** Checkov supports Terraform, Kubernetes, Ansible, and related IaC artefacts, while Conftest can express organisation-specific document-level policies in Rego. Sources: https://github.com/bridgecrewio/checkov ; https://www.conftest.dev/
- [fact] **Kubernetes:** Checkov scans Kubernetes manifests, and kube-score adds security and resilience recommendations over workload definitions. Sources: https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score
- [fact] **DBT / Snowflake / RDS SQL:** dbt-project-evaluator covers dbt project structure and governance, and SQLFluff covers SQL style and syntax across dialects including dbt-style templating. Sources: https://github.com/dbt-labs/dbt-project-evaluator ; https://sqlfluff.com/
- [fact] **REST APIs / OpenAPI:** Spectral provides built-in OpenAPI rulesets and custom rulesets for organisation-wide API governance. Source: https://github.com/stoplightio/spectral
- [fact] **Graph APIs / GraphQL:** GraphQL Inspector provides schema diffing, document validation, and GitHub-native execution paths. Source: https://the-guild.dev/graphql/inspector/docs/index
- [fact] **Event-driven systems / AsyncAPI:** AsyncAPI CLI validates AsyncAPI documents, and Spectral can add reusable AsyncAPI style rules. Sources: https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral
- [inference] A heterogeneous organisation should not try to force every compliance concern through a single scanner; the workable pattern is one GitHub-native orchestration layer plus specialised scanners selected by artefact type. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/

### §3 Reasoning

- [inference] The evidence separates cleanly into a baseline layer and a gap-filling layer. GHAS and CodeQL are strong at supported-language security analysis, but the retrieved documentation does not claim broad repository-structure, API-style, event-schema, or SQL-governance coverage. Basis: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
- [inference] The GitHub-native primitives for cross-repository enforcement are mature enough to act as the control plane: reusable workflows centralise logic, rulesets centralise enforcement, and configuration variables or inputs parameterise per-repository differences. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://github.blog/enterprise-software/devops/introducing-required-workflows-and-configuration-variables-to-github-actions/
- [inference] The strongest practical design is therefore a "policy bundle" approach rather than a "single scanner" approach: one central workflow orchestrates multiple domain-specific scanners, each fed by centrally versioned rulesets, Rego bundles, Semgrep rules, or CodeQL packs. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/stoplightio/spectral
- [inference] The AWS Checkov pattern is especially important because it demonstrates the precise organisational move the item asks about: a security team owns the policy repository, application teams inherit the workflow, and updates land centrally instead of being copied by hand into every repository. Basis: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html

### §4 Consistency Check

- [fact] No retrieved source contradicts the core claim that GitHub Actions can orchestrate broad policy enforcement across repositories; the retrieved GitHub and AWS sources all describe reusable central workflow patterns or organisation-level enforcement primitives. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [fact] The main constraint is consistent across sources: centralisation works only if repositories actually invoke the shared workflow or are covered by rulesets that make the resulting checks mandatory. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [inference] The main unresolved tension is not technical possibility but operational completeness: some stacks have first-class open-source scanners in the evidence set, while others rely on a combination of general-purpose pattern tools and ecosystem-native linters. Basis: https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator ; https://docs.astral.sh/ruff/
- [fact] The original seed source for Spectral returned 404 at retrieval time, but the project readme provided equivalent product-level capability evidence, so the conclusion about Spectral's role remains supported. Sources: https://docs.stoplight.io/docs/spectral/ (inaccessible); https://github.com/stoplightio/spectral

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** the architecture should treat policy definitions as versioned artefacts, not embedded workflow snippets. CodeQL packs, Semgrep rules, Rego policies, and Spectral rulesets are all easier to test and version independently than monolithic workflow files. Basis: CodeQL packs docs; Semgrep, Conftest, and Spectral docs.
- [inference] **Governance lens:** GitHub's Evaluate mode, ruleset insights, and bypass controls imply that policy rollout should be managed like a product change, with telemetry and exceptions, not like a one-time repository setting. Basis: GitHub Well-Architected rulesets guidance.
- [inference] **Economic lens:** the open-source stack in this item is already sufficient for a credible minimum viable compliance platform, which means the primary cost is policy authorship, tuning, and maintenance rather than tool licensing. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/
- [inference] **Developer-behaviour lens:** false positives and duplicated scanner output are likely to be the biggest adoption risk, because broad policy portfolios create more ways to fail a build and require consistent waiver, severity, and ownership models across scanners. Basis: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [inference] **Operational architecture recommendation:** use one central reusable workflow per compliance domain (for example `code-policy.yml`, `iac-policy.yml`, `api-policy.yml`, `data-policy.yml`) rather than one giant workflow, then compose them under rulesets by repository tier. This preserves reuse while limiting blast radius when one scanner changes. Basis: GitHub reusable workflow docs plus rulesets tiering guidance.

### §6 Synthesis

**Executive summary:**

- [fact] GHAS and CodeQL can be extended into an organisation-wide compliance platform in GitHub Actions, but only by treating them as the security-analysis baseline and layering reusable workflows, rulesets, and specialised open-source scanners on top. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [fact] The retrieved evidence supports a "define once, enforce everywhere" architecture built from central policy repositories, reusable GitHub workflows, and mandatory ruleset-backed status checks. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
- [inference] No single scanner covers the entire heterogeneous stack named in the item, so the practical answer is orchestration plus specialisation: CodeQL for supported languages, Semgrep and Conftest for generic custom rules, Checkov and kube-score for IaC and Kubernetes, Spectral and AsyncAPI CLI for API and event specifications, GraphQL Inspector for GraphQL, and SQLFluff plus dbt-project-evaluator for data-platform assets. Basis: https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ ; https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://github.com/stoplightio/spectral ; https://www.asyncapi.com/tools/cli ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator
- [inference] The minimum viable path is to centralise policy artefacts first, run them in non-blocking mode with stable output and exception handling, and only then make them merge-blocking with rulesets. Basis: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html

**Key findings:**

1. [fact][high] GHAS and CodeQL provide a strong security-analysis baseline for .NET, Go, JavaScript/TypeScript, Python, and GitHub Actions, but the official documentation does not position them as complete enforcement for repository layout, OpenAPI or AsyncAPI conformance, Kubernetes manifest quality, Terraform policy, SQL governance, or dbt project structure. Sources: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
2. [fact][high] GitHub's reusable workflows and organisation rulesets together already provide the core "define once, enforce everywhere" mechanics, because workflows centralise execution logic while rulesets make resulting checks mandatory across selected repositories and branches. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
3. [fact][high] CodeQL packs are useful for extending analysis inside supported CodeQL ecosystems, but the official pack model does not eliminate the need for specialised scanners when the policy target is a schema, manifest, SQL dialect, or non-CodeQL project structure. Sources: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
4. [fact][high] The retrieved open-source toolchain covers most of the heterogeneous estate when combined by artefact type: Semgrep and Conftest for generic rules, Checkov and kube-score for IaC and Kubernetes, Spectral and AsyncAPI CLI for REST and event specifications, GraphQL Inspector for GraphQL, and SQLFluff plus dbt-project-evaluator for SQL and dbt governance. Sources: https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://github.com/stoplightio/spectral ; https://www.asyncapi.com/tools/cli ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator
5. [inference][medium] The most maintainable operating model is to keep policy definitions in central repositories and execute them through domain-specific reusable workflows, because this separates policy authorship from application repositories and allows versioned rollout without copy-paste drift. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
6. [inference][high] Rollout should begin in Evaluate or soft-fail mode with rule insights, bypass governance, and clear ownership, because multi-scanner compliance programmes fail operationally when they introduce untriaged false positives and unstable status checks faster than teams can absorb them. Basis: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
7. [inference][medium] The minimum viable GitHub Actions implementation is a four-domain portfolio of reusable workflows — code, infrastructure, APIs/events, and data — backed by central rule repositories and attached to repository tiers through organisation rulesets. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
8. [inference][medium] GraphQL and event-schema governance should be treated as first-class compliance domains rather than squeezed into generic source-code scanning, because the retrieved evidence shows dedicated schema-aware tools with GitHub-native integration paths for those artefacts. Basis: https://the-guild.dev/graphql/inspector/docs/index ; https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] GHAS and CodeQL cover supported languages but not the full heterogeneous compliance surface. | https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ | high | Native language support is explicit; unsupported compliance domains are inferred from what is absent. |
| [fact] Reusable workflows plus rulesets provide GitHub-native central execution and mandatory enforcement. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging | high | This is the core architectural control plane. |
| [fact] CodeQL packs extend supported-language analysis but do not replace schema- or manifest-specific scanners. | https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ | high | Pack capability is explicit; replacement limits are bounded by CodeQL scope. |
| [fact] The open-source scanner set covers most artefact types when combined by domain. | https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://github.com/stoplightio/spectral ; https://www.asyncapi.com/tools/cli ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator | high | The combined coverage is broad, but still multi-tool. |
| [inference] Central policy repositories plus domain workflows are the most maintainable operating model. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ | medium | Strong architectural support, but maintainability still depends on organisational discipline. |
| [inference] Staged rollout with Evaluate mode, insights, and bypass governance is operationally necessary. | https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html | high | Both sources explicitly discuss phased rollout and soft-fail or evaluate patterns. |
| [inference] A four-domain workflow portfolio is the minimum viable implementation shape. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ | medium | This is a synthesis judgment, not a directly quoted product feature. |
| [inference] GraphQL and event-schema checks need dedicated schema-aware tooling. | https://the-guild.dev/graphql/inspector/docs/index ; https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral | medium | Supported by tool capabilities and the absence of equivalent CodeQL coverage. |

**Assumptions:**

- [assumption] The organisation is willing to maintain a small number of central policy repositories and reusable workflow files rather than embedding every rule directly in each application repository. **Justification:** the architecture only delivers the desired scale benefit if policy ownership is centralised enough to avoid copy-paste drift.
- [assumption] Repository owners can accept a staged rollout in which some checks begin as non-blocking before they become required merge gates. **Justification:** both GitHub and AWS guidance point to staged adoption as the practical way to reduce friction and false positives.

**Analysis:**

- [inference] The decisive architectural question is not whether GitHub Actions can run and coordinate the scanners; the retrieved GitHub and AWS sources show that it can. The decisive question is where policy definitions live and how merge-blocking status is applied consistently without duplicating workflow logic. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
- [inference] The evidence favours a layered design. CodeQL remains the supported-language security substrate. Semgrep and Conftest express organisation-specific rules that cross repositories. Domain-specific tools validate artefacts whose semantics are not source-code dataflow problems. Rulesets then turn the resulting status checks into organisation policy. Basis: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral
- [inference] This layered design also fits ownership boundaries. Security or platform teams can own shared policies and reusable workflows, while application teams only need lightweight caller workflows or ruleset coverage. That arrangement reduces per-repository maintenance while preserving controlled exceptions. Basis: AWS centralised Checkov pattern plus GitHub rulesets guidance.
- [inference] The biggest unresolved design issue is normalisation. The sources show many strong single-purpose scanners, but they do not provide a single shared waiver, severity, and reporting model out of the box. That implies an additional aggregation or waiver-governance layer if the organisation wants one coherent compliance dashboard rather than many tool-specific results. Basis: https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator

**Risks, gaps, uncertainties:**

- [fact] The original Spectral documentation page in the seed item returned 404 during retrieval, so Spectral conclusions rely on the project readme rather than the originally cited product docs. Sources: https://docs.stoplight.io/docs/spectral/ ; https://github.com/stoplightio/spectral
- [inference] The exact commercial-plan and feature-state history for "required workflows" is confusing across older GitHub blog posts and newer rulesets documentation, so implementation should be anchored to current docs in the target GitHub plan rather than older launch posts. Basis: https://github.blog/enterprise-software/devops/introducing-required-workflows-and-configuration-variables-to-github-actions/ ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [inference] GraphQL governance is only partially covered here, because the retrieved evidence confirms GraphQL Inspector for schema change and document validation but does not evaluate the wider GraphQL style-guide ecosystem. Basis: https://the-guild.dev/graphql/inspector/docs/index
- [inference] This item establishes orchestration and tool-fit, but it does not yet define a common waiver model, severity taxonomy, or cross-scanner report format for enterprise operations. Basis: evidence gap across the retrieved tooling.

**Open questions:**

- [inference] What is the best shared waiver and exception model for heterogeneous scanner output in GitHub Actions so that developers do not need to learn a separate suppression mechanism for every tool?
- [inference] How should central compliance workflows publish results into one durable report surface — for example GitHub code scanning alerts, Static Analysis Results Interchange Format (SARIF) conversion, check summaries, or an external evidence store — without losing scanner-specific detail?
- [inference] For GraphQL governance beyond schema diffing, which open-source rule engine best covers naming, deprecation policy, and resolver conventions in the same way Spectral covers OpenAPI and AsyncAPI?

### §7 Recursive Review

- [fact] Every major conclusion in §6 is backed either by direct primary-product documentation or by a clearly labelled synthesis across those sources. Source set: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://sqlfluff.com/
- [fact] All unsupported certainty has been avoided by labelling stack-wide architecture recommendations as [inference] rather than [fact]. Source: final pass against this document.
- [fact] Unresolved gaps remain explicit: GraphQL style governance beyond schema validation, cross-scanner waiver design, and the exact reporting normalisation pattern are all carried forward as open questions rather than being silently assumed solved. Source: https://the-guild.dev/graphql/inspector/docs/index ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://github.com/dbt-labs/dbt-project-evaluator

---

## Findings

### Executive Summary

- [inference] The most defensible way to extend GHAS and CodeQL into broad compliance scanning is to treat them as the supported-language security layer inside a larger GitHub Actions architecture that also governs manifests, schemas, SQL, and project structure. Basis: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [fact] GitHub already provides the cross-repository control-plane primitives needed for that design: reusable workflows centralise execution logic, while organisation rulesets and required status checks make shared checks mandatory. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization
- [inference] The correct operating model is a multi-tool policy portfolio organised by artefact type, not an attempt to stretch CodeQL into every compliance domain named in the question. Basis: https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator
- [inference] The safest adoption path is to centralise policy artefacts, run them first in Evaluate or soft-fail mode, and only then promote them into merge-blocking rulesets after outputs, ownership, and exceptions are stable. Basis: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html

### Key Findings

1. [inference][high] Because the CodeQL support matrix is language-centric, any estate that also needs Terraform, Kubernetes, OpenAPI, AsyncAPI, SQL, or dbt governance must add dedicated artefact scanners instead of expecting GHAS alone to enforce those surfaces. Basis: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
2. [fact][high] GitHub separates shared execution from shared enforcement: reusable workflows encapsulate the shared scanning logic, while organisation rulesets and required checks apply merge-blocking governance across targeted repositories. Sources: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
3. [fact][high] CodeQL packs are an important extension point for supported languages, but the official pack model still assumes CodeQL-compatible artefacts and therefore cannot replace specialised validation tools for schemas, manifests, and SQL-focused repositories. Sources: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
4. [fact][high] The open-source toolchain retrieved in this item is already broad enough to cover most of the named estate when organised by artefact type, combining Semgrep and Conftest for generic policy, Checkov and kube-score for IaC and Kubernetes, Spectral and AsyncAPI CLI for API and event contracts, GraphQL Inspector for GraphQL, and SQLFluff plus dbt-project-evaluator for data-platform governance. Sources: https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://github.com/stoplightio/spectral ; https://www.asyncapi.com/tools/cli ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator
5. [inference][medium] A central policy-repository model is more maintainable than embedding scanner logic in every application repository, because central rule bundles and reusable workflows reduce drift, simplify ownership, and let policy teams update standards without mass copy-editing downstream repositories. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
6. [inference][high] A staged rollout with Evaluate mode, soft-fail where appropriate, rule insights, and explicit bypass governance is not just a convenience feature but the operational control that prevents multi-scanner compliance programmes from collapsing under false positives and unstable checks. Basis: https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
7. [inference][medium] The minimum viable architecture for this problem is a portfolio of four reusable workflow domains — code, infrastructure, APIs/events, and data — each backed by centrally versioned policies and attached to repository tiers through organisation rulesets. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
8. [inference][medium] GraphQL and event-driven contract governance deserve first-class treatment in the compliance model, because the retrieved evidence shows dedicated schema-aware tools for those artefacts and does not support treating them as a by-product of generic source-code scanning. Basis: https://the-guild.dev/graphql/inspector/docs/index ; https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] CodeQL's published support boundary leaves manifest-, schema-, SQL-, and dbt-centric compliance domains outside the native GHAS baseline. | https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ | high | This is a synthesis from the explicit support matrix. |
| [fact] GitHub splits shared compliance into two primitives: reusable workflows for execution logic and rulesets for mandatory enforcement. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging | high | This expresses the same mechanism more precisely than a generic restatement. |
| [fact] CodeQL packs extend supported-language analysis but not schema or manifest validation. | https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs ; https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/ | high | Extension exists, but supported artefact scope remains bounded. |
| [fact] The open-source scanner portfolio covers most artefact types when combined. | https://semgrep.dev/docs/writing-rules/overview ; https://www.conftest.dev/ ; https://github.com/bridgecrewio/checkov ; https://github.com/zegl/kube-score ; https://github.com/stoplightio/spectral ; https://www.asyncapi.com/tools/cli ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator | high | Coverage is broad, but intentionally multi-tool. |
| [inference] Central policy repositories are more maintainable than per-repo embedded policy logic. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ | medium | Strong pattern evidence, but still a design inference. |
| [inference] Staged rollout and bypass governance are operationally necessary. | https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html | high | Both sources explicitly recommend phased rollout and governance. |
| [inference] Four reusable workflow domains are the minimum viable implementation shape. | https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ | medium | Synthesised implementation pattern, not a quoted vendor prescription. |
| [inference] GraphQL and event schemas need dedicated first-class checks. | https://the-guild.dev/graphql/inspector/docs/index ; https://www.asyncapi.com/tools/cli ; https://github.com/stoplightio/spectral | medium | Evidence is direct on tool capability, indirect on organisational design choice. |

### Assumptions

- [assumption] **Assumption:** The organisation can maintain central policy repositories and a small reusable-workflow portfolio. **Justification:** Without central ownership, the proposed architecture degenerates into per-repository duplication and loses its main scale advantage.
- [assumption] **Assumption:** Teams can tolerate an Evaluate or soft-fail adoption period before strict merge blocking. **Justification:** GitHub and AWS guidance both point to staged rollout as the practical way to reduce developer friction and tune rules.

### Analysis

- [inference] The evidence supports a compositional architecture rather than a monolithic scanner strategy. GitHub supplies the orchestration and enforcement layer, while specialised tools supply the domain semantics. Basis: https://docs.github.com/en/actions/sharing-automations/reusing-workflows ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging ; https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://sqlfluff.com/
- [inference] That compositional design also fits realistic ownership boundaries, because platform or security teams can own shared rules and workflows while application teams remain responsible only for repository-local adoption and exception handling. Basis: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html ; https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/
- [inference] The main remaining architecture gap is not scanner availability but result normalisation: a serious enterprise rollout will eventually need a common severity, waiver, and reporting model across these otherwise independent tools. Basis: https://github.com/bridgecrewio/checkov ; https://github.com/stoplightio/spectral ; https://the-guild.dev/graphql/inspector/docs/index ; https://sqlfluff.com/ ; https://github.com/dbt-labs/dbt-project-evaluator

### Risks, Gaps, and Uncertainties

- [fact] The original Spectral documentation page supplied in the item was inaccessible during retrieval, so Spectral capability claims rely on the project readme rather than the exact seed page. Sources: https://docs.stoplight.io/docs/spectral/ ; https://github.com/stoplightio/spectral
- [inference] GitHub's required-workflows feature history is partially split between older launch posts and newer rulesets documentation, so any implementation should validate plan support against current product docs for the target organisation. Basis: https://github.blog/enterprise-software/devops/introducing-required-workflows-and-configuration-variables-to-github-actions/ ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging
- [inference] GraphQL governance beyond schema diffing and document validation remains underexplored in this item and would benefit from a dedicated follow-up on style, naming, and resolver policy tooling. Basis: https://the-guild.dev/graphql/inspector/docs/index
- [inference] A common evidence and waiver layer for multi-scanner GitHub Actions compliance remains an open design problem not resolved by the retrieved sources. Basis: gap across the retrieved tool documentation.

### Open Questions

- [inference] How should heterogeneous scanner outputs be normalised into one durable evidence model for audit, waiver management, and developer triage inside GitHub?
- [inference] What is the best open-source governance toolchain for GraphQL style and schema policy beyond change detection and operation validation?
- [inference] When central workflows become merge-blocking, which checks should emit GitHub code-scanning alerts versus regular check-run summaries so that developers see one coherent signal instead of many parallel failure surfaces?

---

## Output

- Type: knowledge, backlog-item
- Description: A sourced architecture for extending GHAS and CodeQL into a broad GitHub Actions compliance platform using reusable workflows, rulesets, and specialised open-source scanners, plus one follow-on backlog item on cross-scanner evidence and waiver normalisation.
- Links:
  - https://docs.github.com/en/actions/sharing-automations/reusing-workflows
  - https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql
  - https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
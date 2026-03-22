---
title: "Cross-Scanner Compliance Evidence and Waiver Normalisation in GitHub Actions"
added: 2026-03-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [github-actions, compliance, policy-as-code, evidence, waivers, sarif, governance, reporting]
started: ~
completed: ~
output: [knowledge]
---

# Cross-Scanner Compliance Evidence and Waiver Normalisation in GitHub Actions

## Research Question

How should an organisation running multiple compliance scanners in GitHub Actions normalise evidence, severity, waiver handling, and developer-facing output so that heterogeneous tools behave like one coherent compliance system rather than a collection of unrelated failing checks?

## Scope

**In scope:**
- Evidence models for combining outputs from CodeQL, Semgrep, Checkov, Spectral, GraphQL Inspector, SQLFluff, and similar tools
- Waiver and suppression governance across heterogeneous scanners
- Developer-facing result surfaces in GitHub: code scanning alerts, check runs, summaries, annotations, and external evidence stores
- Mapping scanner-native severities into an organisation-level severity taxonomy
- Auditability requirements for exceptions, expiry, and policy-version traceability

**Out of scope:**
- Building a new scanner engine
- Runtime security telemetry outside GitHub Actions
- Vendor-specific dashboards that cannot be driven from GitHub Actions or open formats

**Constraints:** Public documentation, open standards where possible, and practical GitHub-native implementation paths.

## Context

The compliance-scanning research item on 2026-03-22 found that broad policy coverage in GitHub Actions is already achievable with a portfolio of specialised scanners. The main unresolved problem is no longer scanner availability but operating them as one governed system. Without a shared evidence and waiver model, teams inherit multiple suppression syntaxes, inconsistent severities, and fragmented audit trails.

## Approach

1. Survey the output and suppression models of leading GitHub-integrated scanners.
2. Identify the common denominator formats and metadata fields needed for aggregation.
3. Evaluate GitHub-native result surfaces and their trade-offs.
4. Propose a minimum viable evidence schema and waiver lifecycle.
5. Synthesize an implementation path suitable for a central compliance platform.

## Sources

- [ ] GitHub code scanning and alert documentation
- [ ] SARIF specification and practical GitHub usage guidance
- [ ] Semgrep output and ignore semantics
- [ ] Checkov suppression and reporting semantics
- [ ] Spectral reporting formats
- [ ] GraphQL Inspector GitHub Action and output model

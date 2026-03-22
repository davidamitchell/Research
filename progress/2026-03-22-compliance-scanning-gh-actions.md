# 2026-03-22 — Research Loop (compliance-scanning-gh-actions)

**Completed:**

Research item:
- `Research/completed/2026-03-22-compliance-scanning-gh-actions.md` — completed; the item concluded that GitHub Advanced Security (GHAS) and CodeQL are only the supported-language baseline for broad compliance scanning, not the whole solution. It found that a workable organisation-wide design uses reusable GitHub Actions workflows and rulesets as the control plane, then layers specialised scanners such as Semgrep, Checkov, Spectral, GraphQL Inspector, SQLFluff, and dbt-project-evaluator by artefact type.

Sources consulted:
- https://docs.github.com/en/actions/sharing-automations/reusing-workflows (GitHub reusable workflow documentation)
- https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql (GitHub CodeQL/code-scanning scope documentation)
- https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html (AWS Prescriptive Guidance pattern for centralised Checkov scanning in GitHub Actions)

## Mini-Retro

1. **Did the process work?** Yes. The loop worked end to end: research, draft, review, revision, second review, completion, and synthesis updates all landed in the repository.
2. **What slowed down or went wrong?** The review workflow was strict about URL-level citations and treated several descriptive source references and near-paraphrases as failures, so the second pass required extra citation cleanup and wording separation.
3. **What single change would prevent this next time?** Start with URL-level citations everywhere in `## Research Skill Output`, including synthesis and assumptions, instead of allowing any shorthand source references during drafting.
4. **Is this a pattern?** Yes. It matches the repository's known review pattern that claim-bearing text, assumption justifications, and findings phrasing all need explicit labels and precise inline citations.

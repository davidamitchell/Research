# 2026-04-22 -- Research Loop (ai-governance-assurance-change-control-verification)

**Completed:**

Research item:
- `Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md` -- completed; the item concludes that AI-assisted change can be governed at near machine speed when provenance attestations, policy-decision logs, reusable workflow controls, and risk-tiered exception paths replace routine manual CAB review. It also identifies the remaining human role as exception approval and high-risk risk-acceptance, and highlights the lack of a standard cross-tool exception schema as the main open design gap.

Sources consulted:
- https://slsa.dev/spec/v1.1/provenance (SLSA provenance model and required build evidence fields)
- https://www.openpolicyagent.org/docs/latest/management-decision-logs/ (OPA decision-log fields and audit behavior)
- https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations (GitHub artifact attestation capabilities and related guidance)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, review workflow, and second-pass auto-review rule worked as intended, and the review comments were specific enough to fix quickly.
2. **What slowed down or went wrong?** The first draft used self-referential citations in `§0` and `§7`, and a few synthesis statements were labeled too strongly as facts or high-confidence claims.
3. **What single change would prevent this next time?** Add an explicit self-review rule that forbids self-referential citations like "this file" or "self-audit" and requires a verifiable URL instead.
4. **Is this a pattern?** Yes. It is a variant of the known citation-discipline failure pattern: claims that feel traceable during authorship still fail automated review when they are not externally verifiable.

## Applied improvements

- Updated `research-prompt.md` to add a dedicated self-review check banning self-referential citations in `§0`, `§7`, and `## Findings`.

## Pending skill improvements

- Update `.github/skills/research/SKILL.md` output-finalisation guidance to forbid self-referential citations and require verifiable URLs or pinpoint citations for recursive-review claims. The skills submodule is read-only in this repository, so this needs to be changed in `davidamitchell/Skills`.

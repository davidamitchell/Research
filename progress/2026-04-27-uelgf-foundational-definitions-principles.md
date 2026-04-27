# 2026-04-27 -- Research Loop (uelgf-foundational-definitions-principles)

**Completed:**

Research item:
- `Research/completed/2026-04-27-uelgf-foundational-definitions-principles.md` -- completed; the item concludes that UELGF needs a novel universal entity definition and must be specified as a generative, policy-bound lifecycle rail rather than a governance overlay. It also defines the governed golden rail, licence to operate, and Policy Decision Point, then translates those concepts into twelve testable invariants for evaluating future UELGF implementations.

Sources consulted:
- https://csrc.nist.gov/pubs/sp/800/207/final (Zero Trust resource and policy-decision model)
- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html (policy lifecycle separation and PDP/PAP/PEP/PIP model)
- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ (purpose, scope, oversight, decommission, and lifecycle governance)

## Mini-Retro

1. **Did the process work?** Yes. The research loop and review workflow converged quickly, and the substantive draft only needed one formatting-confidence cleanup after review.
2. **What slowed down or went wrong?** The first review pass failed because `§7 Recursive Review` lines were treated as audited claim-bearing prose even though the prompt did not say that explicitly enough.
3. **What single change would prevent this next time?** Add an explicit self-review rule that visible `§7 Recursive Review` sentences need labels and either a GitHub URL citation or a rewrite into pure metadata.
4. **Is this a pattern?** Yes. It matches the recurring pattern that scaffolding text inside audited sections is still reviewed as claim-bearing prose and must be treated with the same citation discipline as the main findings.

## Applied improvements

- Updated `research-prompt.md` so the self-review checklist now states that visible `§7 Recursive Review` sentences are audited like other claim-bearing prose and need labels plus either an explicit GitHub URL citation or pure-metadata rewriting.

## Pending skill improvements

- Mirror the new `§7 Recursive Review` labeling rule into `.github/skills/research/SKILL.md` in the Skills repository, because the same ambiguity exists there and this repo cannot edit the skills submodule directly.

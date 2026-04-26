# 2026-04-26 -- Research Loop (ai-lowcode-decision-rights-accountability-liability)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-lowcode-decision-rights-accountability-liability.md` -- completed; the item concludes that enterprise AI and low-code governance should use tiered approval rights, split production accountability by lifecycle decision, and keep independent challenge and stop authority outside the build team. It also clarifies that internal accountability maps do not replace external legal liability, because provider or manufacturer duties, deployer duties, and board or management-body accountability remain distinct under current law.

Sources consulted:
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 (deployer monitoring, human oversight, suspension, and log-retention duties)
- https://handbook.apra.gov.au/standard/cps-230 (board and senior-management accountability, incident escalation, and operational-risk review)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853 (current EU product-liability treatment of software and AI systems)

## Mini-Retro

1. **Did the process work?** Yes, the item moved cleanly through draft, review, and completion, and the research outputs held up after one targeted citation fix cycle.
2. **What slowed down or went wrong?** The first review pass caught an evidence-map citation rule that was not explicit enough in `research-prompt.md`, so I had to convert source-name shorthand into URL-backed source cells.
3. **What single change would prevent this next time?** Make `research-prompt.md` say explicitly that every Evidence Map source cell must contain URL-backed citations or DOIs, not just source names.
4. **Is this a pattern?** Yes, it matches the broader citation-discipline failure class: claims in structured tables are easy to treat like scaffolding even though review treats them as substantive evidence.

## Applied improvements

- Updated `research-prompt.md` to require URL-backed citations or DOIs in every Evidence Map source cell.

## Pending skill improvements

- Mirror the new Evidence Map source-cell URL requirement into `.github/skills/research/SKILL.md` when the Skills submodule is updated in the separate `davidamitchell/Skills` repository.

# 2026-04-26 -- Research Loop (systems-capability-debt-citizen-development-empirical-evidence)

**Completed:**

Research item:
- `Research/completed/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.md` -- completed; the item concludes that recurring capability gaps, especially Information Technology slowness, misalignment, and weak sanctioned delivery paths, are the strongest recurring driver of citizen-development sprawl rather than low-code preference alone. It anchors that claim in Shadow IT literature, public banking control failures, and platform-governance evidence showing that tiered sanctioned lanes plus capability remediation are a more defensible response than tool bans.

Sources consulted:
- https://jitm.ubalt.edu/XXX-4/article1.pdf (practitioner study on Shadow IT and Business-managed IT drivers)
- https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/regulatory-action/final-notice-from-pra-to-standard-chartered-bank.pdf (official enforcement record for spreadsheet-driven liquidity misreporting)
- https://www.microsoft.com/en/customers/story/25909-heineken-microsoft-copilot-studio (public case study of tiered governance at scale)

## Mini-Retro

1. **Did the process work?** Yes, the research loop worked end to end, and the external review surfaced calibration issues that were worth fixing before completion.
2. **What slowed down or went wrong?** My first draft commit moved the file and changed status but did not stage the rewritten research body, so the first review ran against the old near-template version.
3. **What single change would prevent this next time?** Before any draft commit, inspect `git diff --cached --stat` and confirm the staged item includes the expected substantive line count, not just a move or frontmatter flip.
4. **Is this a pattern?** Not yet in this repo; this was an execution mistake in the session rather than an observed recurring repository pattern.

## Applied improvements

- Re-labeled two governance findings from `[fact]` to `[inference]`, lowered their confidence from high to medium, and defined the working term `systems capability debt` explicitly in the synthesis and evidence map before completion.

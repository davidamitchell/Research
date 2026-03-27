# 2026-03-27 — Research Loop (customer-contact-and-delight)

**Completed:**

Research item:
- `Research/completed/2026-03-26-customer-contact-and-delight.md` — completed; organisations systematically underinvest in human customer service because contact costs are immediately visible while retention and customer lifetime value (CLV) uplift are attribution-resistant over long time horizons; the evidence supports a hybrid AI co-pilot model that routes routine contacts to automation while preserving human agents for complex, emotionally significant interactions; Octopus Energy, Klarna, and the Amazon callback pattern all confirm this framework from different angles.

Sources consulted:
- https://shows.acast.com/business-leader-podcast/episodes/rory-sutherland-the-advertising-gurus-tips (Rory Sutherland / Business Leader podcast — primary framing source)
- https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ (Klarna AI press release — automation metrics)
- https://octopus.energy/press/more-news-press-releases/octopus-energy-achieves-record-customer-satisfaction-levels-in-ofgem-survey/ (Ofgem Octopus satisfaction data)
- https://www.five9.com/news/news-releases/new-five9-study-finds-75-consumers-prefer-talking-human-customer-service (Five9 consumer survey)
- https://customergauge.com/blog/why-customers-prefer-self-service-support-but-only-if-its-done-right (CustomerGauge self-service failure data)
- https://bigthink.com/business/unreasonable-hospitality-548071/ (Big Think / Guidara — 95/5 Rule)

## Mini-Retro

1. **Did the process work?** Yes, with friction. The research skill framework produced a thorough output across all seven sections. The two-review cycle caught real violations (emdashes, overconfident language, citation label mismatches, unlabelled causal claims) that improved the item's quality.

2. **What slowed down or went wrong?** Two review passes were required because the first self-review missed: (a) emdash violations in the Findings section, (b) `[fact]` labels on claims backed only by secondary synthesis sources (Salient Global, Nextiva/Bain), (c) Reddit and book-summary sites used to support `[fact]` claims, and (d) unlabelled causal constructions in the Analysis section. The second review caught a further batch including `UK` unexpanded and "clearest" as an unlabelled evaluative superlative.

3. **What single change would prevent this next time?** Run a mechanical emdash scan on the entire `## Findings` section before committing the draft — not just the sections written last. Emdash violations account for 5 of the 11 first-review failures and they are trivially detectable with `grep " — "`.

4. **Is this a pattern?** Yes — this is consistent with the known pattern of emdash and citation-label violations causing first-review failures. The specific source-quality issues (Reddit, Sumizeit book summary, vendor blog citing a primary source) are a recurring secondary pattern: a source that names a statistic is not sufficient for `[fact]` unless it is the primary source or an independently verifiable secondary source. This warrants stricter pre-commit source classification.

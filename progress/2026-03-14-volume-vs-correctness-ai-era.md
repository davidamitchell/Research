# 2026-03-14 — Research Loop (volume-vs-correctness-ai-era)

**Completed:**

Research item:
- `Research/completed/2026-03-12-volume-vs-correctness-ai-era.md` — completed; AI has inverted the scarcity in knowledge work from generating output to verifying it: Faros AI 2025 telemetry (10,000+ developers) shows individual volume up 98% in PRs while organisational DORA delivery metrics remain flat; the Dell'Acqua et al. (2025) P&G RCT shows AI can produce ~3x top-decile quality outputs when human judgment is structurally scaffolded; McKinney's "agentic tarpit" and the "workslop" phenomenon independently confirm the verification bottleneck.

Sources consulted:
- https://www.nber.org/system/files/working_papers/w33641/w33641.pdf (Dell'Acqua et al. P&G/HBS RCT — primary experimental evidence for AI quality effects)
- https://www.faros.ai/blog/ai-software-engineering (Faros AI 2025 — telemetric evidence of volume-throughput decoupling at organisational scale)
- https://wesmckinney.com/blog/mythical-agent-month/ (Wes McKinney — primary source on agentic tarpit mechanism)
- https://philippdubach.com/posts/93-of-developers-use-ai-coding-tools.-productivity-hasnt-moved./ (DORA 2024/2025 summary; Cursor CEO Truell quotation)
- https://www.microsoft.com/en-us/research/blog/the-future-of-ai-in-knowledge-work-tools-for-thought-at-chi-2025/ (Microsoft Research CHI 2025 — verification as the new locus of effort)
- https://www.cnbc.com/2025/09/23/ai-generated-workslop-is-destroying-productivity-and-teams-researchers-say.html (CNBC — workslop phenomenon, BetterUp Labs)

## Mini-Retro

1. **Did the process work?** Yes, but required three review cycles (first review: 11 violations; second review: 13 violations; third review: PASS). The protocol caught real quality gaps each time — citation URLs missing, inference labels absent on evaluative claims, slop patterns. Each cycle produced a genuinely better item.

2. **What slowed down or went wrong?** The second review cycle surfaced more violations than the first — partly because the first fixes exposed underlying citation issues that had been masked. The main repeating pattern: citations to secondary blogs (philippdubach.com, medium.com authors) without full URLs, and synthesis conclusions in Analysis sections that were not explicitly labelled as [inference]. The Findings Analysis section was treated as prose commentary rather than evidence-labelled content, which violated citation discipline.

3. **What single change would prevent this next time?** Before writing any Analysis or Executive Summary section, explicitly label every sentence with [fact], [inference], or [assumption] inline — even in prose sections, not just in §2 Investigation. Secondary-source citations should always include the full URL at first mention, regardless of section.

4. **Is this a pattern?** Yes — this matches the known pattern of "Findings Analysis as unlabelled prose." The citation-discipline skill explicitly requires labels throughout, not only in Investigation. The fix is to treat the Findings sections with the same labelling discipline as §2, not as prose summaries. This is worth noting as a recurring pattern for future items.

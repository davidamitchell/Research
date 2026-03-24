# 2026-03-24 — Research Loop (public-sentiment-ai-banking)

**Completed:**

Research item:
- `Research/in-progress/2026-03-24-public-sentiment-on-ai-in-banking-and-high-trust-institutions.md` — drafted for review; the evidence shows Australia has the widest AI trust-use gap in the developed world (50% use AI, only 36% trust it), the two-plane architecture (human augmentation production plane + AI-constrained operational plane) is viable and aligns with both customer preference data and emerging regulatory mandates (APRA CPS 230, MAS, ABS), and first-mover differentiation depends on making the architecture observable to customers before it becomes regulatory table-stakes.

Sources consulted:
- https://knowledge.publicissapient.com/01/news-publicis-sapient-customer-banking-report-press-release.html (Publicis Sapient 2024 Australian Customer Banking Report)
- https://assets.kpmg.com/content/dam/kpmgsites/au/pdf/2025/trust-in-ai-global-insights-2025-australia-snapshot.pdf (KPMG/University of Melbourne Trust in AI 2025 — Australia snapshot)
- https://www.prnewswire.com/news-releases/epam-continuums-2024-consumer-banking-report-highlights-ai-success-with-a-96-satisfaction-rate-302065213.html (EPAM Continuum 2024 Consumer Banking Report)
- https://www.qualtrics.com/m/www.xminstitute.com/wp-content/uploads/2025/01/XMI_RR-DS_ConsumerSentimentAI-Global-2025.pdf (Qualtrics XM Institute 2025 — Consumer Sentiment on AI, 23,730 consumers)
- https://www.accenture.com/us-en/insights/banking/consumer-study-banking-advocacy-powering-growth (Accenture 2025 Banking Consumer Study — 49,300 respondents)
- https://www.abs.org.sg/docs/library/abs-handbook-on-generative-ai-guardrails-in-banking-(24-march-2026).pdf (Association of Banks in Singapore Gen AI Guardrails Handbook 2026)

## Mini-Retro

1. **Did the process work?** Yes. The research skill process produced a well-structured item with 10 key findings, a 12-row evidence map, and all sections complete. Web search found real survey data from Publicis Sapient, KPMG, Accenture, EPAM, Edelman, and regulators.
2. **What slowed down or went wrong?** The `Research/backlog/` directory did not exist and had to be created manually before `python -m src.main research add` could run.
3. **What single change would prevent this next time?** The CLI should create the `Research/backlog/` directory if it does not exist, rather than failing with a `FileNotFoundError`.
4. **Is this a pattern?** Not a known recurring pattern from the instructions. It is a one-time setup issue for repositories that have never had a backlog item created via the CLI.

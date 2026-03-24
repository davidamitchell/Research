# 2026-03-24 — AI Banking Sentiment Research

## What happened

Completed research item `Research/in-progress/2026-03-24-public-sentiment-on-ai-in-banking-and-high-trust-institutions.md`.

## Key decisions

- Sourced 12+ surveys/reports covering 100,000+ respondents across Australia, APAC, and globally
- Structured research around five atomic questions: Australian baseline, APAC regional, global benchmarks, regulatory alignment, architecture viability
- Labelled all claims as [fact], [inference], or [assumption] per research skill requirements
- Assessed two-plane architecture (production/operational) as viable but differentiation depends on communication, not architecture alone

## Sources used

- Publicis Sapient 2024 Customer Banking Report (AU-specific)
- KPMG/University of Melbourne 2025 Trust in AI Global Study (AU snapshot)
- Edelman Trust Barometer 2025 (Financial Services + AI)
- Accenture 2025 Global Banking Consumer Study (49,300 respondents, 39 countries)
- EPAM Continuum 2024 Consumer Banking Report
- FICO 2024 Bank Customer Experience Survey APAC
- F5/Twimbit 2025 AI Paradox APAC Report
- Qualtrics XM Institute 2025 Consumer Sentiment Toward AI
- McKinsey AI Banking Reports 2024-2025
- APRA CPS 230 regulatory analysis
- ABS/MAS Generative AI Guardrails and AI Risk Toolkit

## Key finding

Australia has the widest trust-use gap in the developed world: 50% use AI regularly but only 36% trust it. The two-plane architecture is viable and regulatory-aligned, but the competitive moat is in communication clarity and experience design, not architecture alone.

## Status

Research item moved to `reviewing` status via `python -m src.main research draft`.

## Mini-retro

- **Went well:** Web search tools returned high-quality, recent survey data. Multiple independent sources converged on the same conclusions, strengthening confidence.
- **Could improve:** No survey directly tests the two-plane message framing — flagged as an open question for potential follow-up research.
- **Learned:** APAC averages are misleading for AI sentiment — country-level variation is extreme (35% increased trust in China vs. 19% in Australia).

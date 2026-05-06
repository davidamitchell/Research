# 2026-05-06 -- Research Loop (aibom-runtime-capture-opentelemetry-practice)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-runtime-capture-opentelemetry-practice.md` -- completed; the item shows that a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) is feasible today, but only as a layered trace assembly rather than a single export. It concludes that Amazon Web Services (AWS) Bedrock exposes the lower-friction native runtime path, while LangGraph reaches comparable fidelity only when LangSmith is paired with OpenTelemetry spans and deliberate custom state capture.

Sources consulted:
- https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html (Bedrock step-level runtime trace schema)
- https://docs.langchain.com/langsmith/trace-with-opentelemetry (LangSmith OpenTelemetry ingestion and attribute mapping)
- https://opentelemetry.io/docs/specs/semconv/gen-ai/ (baseline OpenTelemetry runtime vocabulary for Generative Artificial Intelligence traces)

## Mini-Retro

1. **Did the process work?** Yes; the review workflow caught the remaining epistemic-label and vague-quantifier issues before completion.
2. **What slowed down or went wrong?** The first review pass exposed a few claims that were correctly sourced but phrased too strongly for their evidence class.
3. **What single change would prevent this next time?** Nothing new; the current review loop already catches this class of wording drift effectively.
4. **Is this a pattern?** No; this was normal research-review tightening rather than a new recurring failure mode.

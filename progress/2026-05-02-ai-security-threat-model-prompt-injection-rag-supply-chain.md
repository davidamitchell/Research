# 2026-05-02 -- Research Loop (ai-security-threat-model-prompt-injection-rag-supply-chain)

**Completed:**

Research item:
- `Research/completed/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.md` -- completed; the item concludes that enterprise AI security needs explicit controls for prompt and retrieval boundaries, model-artifact provenance, identity-scoped execution, deterministic egress, and runtime circuit breakers beyond ordinary access control and audit logging. It also turns that conclusion into a threat-model structure that separates prompt, retrieval, model, tool, and runtime-governance assets and maps them back into the enterprise capability model.

Sources consulted:
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (prompt-injection taxonomy, impact, and mitigations)
- https://pytorch.org/blog/compromised-nightly-dependency/ (real-world machine-learning supply-chain compromise case)
- https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ (machine-speed privilege amplification and deterministic external controls)

## Mini-Retro

1. **Did the process work?** Yes. The research loop produced a usable item, and the review workflow caught the remaining epistemic-label mistakes before completion.
2. **What slowed down or went wrong?** The main friction was synthesis prose that should have been labeled as inference rather than fact, especially in Key Findings and §7 review notes.
3. **What single change would prevent this next time?** Nothing new in the prompt is needed; the existing review rules already cover this, and the miss was execution rather than missing guidance.
4. **Is this a pattern?** Yes. It matches the existing citation-discipline and review-labeling failure pattern rather than introducing a new recurring issue.

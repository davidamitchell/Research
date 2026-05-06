# 2026-05-06 — Add AIBOM research backlog items (aibom-series)

**Completed:**

- `Research/backlog/2026-05-06-aibom-sbom-conceptual-gaps-theory.md` — foundational theory item: why SBOM breaks for agentic AI and what new abstractions are required; blocks schema design and practice items; priority high
- `Research/backlog/2026-05-06-aibom-schema-design-standards-alignment.md` — theory item: minimal viable AIBOM schema aligned to CycloneDX and SPDX; extends from conceptual gaps item; blocks declared construction practice item; priority high
- `Research/backlog/2026-05-06-aibom-runtime-generation-divergence-theory.md` — theory item: formal model for runtime AIBOM generation and declared-vs-observed divergence; blocks runtime capture practice item; priority high
- `Research/backlog/2026-05-06-aibom-identity-delegation-trust-theory.md` — theory item: formal model for identity, delegation chains, and permission scope representation; blocks identity attribution practice item; priority high
- `Research/backlog/2026-05-06-aibom-declared-construction-practice.md` — practice item: constructing declared AIBOMs from AWS Bedrock Agents and LangGraph with worked examples; priority medium
- `Research/backlog/2026-05-06-aibom-runtime-capture-opentelemetry-practice.md` — practice item: instrumenting real agentic workloads with OpenTelemetry and platform-native tools to capture runtime AIBOM; priority medium
- `Research/backlog/2026-05-06-aibom-platform-observability-control-comparison.md` — practice item: comparative evaluation of observability and control surfaces across AWS Bedrock Agents, Microsoft 365 Copilot, Salesforce Agentforce, and ServiceNow Now Assist; priority high
- `Research/backlog/2026-05-06-aibom-identity-attribution-multiagent-practice.md` — practice item: how OAuth 2.0, OIDC, and SPIFFE token propagation work in real multi-agent pipelines and where attribution breaks; priority medium
- `Research/backlog/2026-05-06-aibom-effectiveness-risk-mitigation-limits.md` — cross-cutting item: what AIBOM can realistically mitigate vs. false assurance scenarios; synthesises across the series; priority medium
- `Research/backlog/2026-05-06-aibom-regulatory-eu-ai-act-intersection.md` — cross-cutting item: EU AI Act technical documentation obligations, NIST AI RMF, ISO 42001, and APRA CPS 230 intersection with AIBOM requirements; priority medium

**Addressing:** GitHub issue requesting new research items on extending SBOM concepts to agentic AI workloads (AIBOM series), split into theory and practical applications, with relations building on prior knowledge.

**Cross-references established:**
- Theory items cite and are blocked-by the foundational SBOM gap analysis item
- Practice items cite their corresponding theory prerequisites
- All items reference prior completed research: `2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain`, `2026-04-26-ai-agent-identity-access-management-enterprise`, `2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment`, `2026-04-26-vendor-platform-governance-constraints-compensating-controls`, `2026-04-24-ai-agent-regulation-global-financial-services`

**Checks run:**
- `make check` — passed (ruff lint + format clean)
- `python -m pytest tests/ -q` — 411 passed, 1 pre-existing failure (TAVILY_API_KEY not set in sandbox environment; unrelated to this change)

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a well-structured set of five research questions with clear framing. Splitting into theory/practice pairs was the right decomposition — it maps naturally to how the research loop processes items (one focused question per session) and ensures theory items must complete before practice items begin. The `blocks:` dependency ordering enforces the right research sequencing.

2. **What slowed down or went wrong?** Nothing significant. The main decision work was in scoping each item tightly enough to be answerable in a single research session, while ensuring the `related:` and `cites:` fields accurately capture the dependency graph across all 10 items and back to existing completed research.

3. **What single change would prevent this next time?** Nothing to change — the template is well-suited to this kind of structured decomposition. The tag vocabulary lookup was quick; the main time went into writing high-quality approach sections and sourced starting points for each item.

4. **Is this a pattern?** Yes — issuing research items in batches from a single structured topic is a recurring pattern. This is the correct approach: decompose by concern (theory vs. practice), set up `blocks:` to enforce sequencing, and cross-reference prior completed items so the research loop can build on existing findings.

5. **Does any documentation need updating?** No — this is purely new backlog content; no existing docs changed.

6. **Do the default instructions need updating?** No new conventions emerged from this session.

# 2026-04-26 -- Add backlog items from new research questions issue (mechanisms 1, 2, 4, 5, 6, 7)

**Completed:**

- `Research/backlog/2026-04-26-permission-safe-rag-enterprise-information-architecture.md` — added from issue; asks what the technical constraints on permission-safe Retrieval-Augmented Generation (RAG) are in an enterprise with incoherent access controls, what the architectural options are (per-user token delegation, per-security-boundary index partitioning, ACL metadata filtering), and what their failure modes are including the embedding inference problem and permission-change propagation problem
- `Research/backlog/2026-04-26-access-control-amplification-agentic-operations.md` — added from issue; asks whether NIST SP 800-207, NIST SP 800-53, APRA CPS 230, and DORA explicitly address the mechanism by which agents inherit the worst-case interpretation of a user's full permission set rather than their typical-use subset, or whether the amplification argument must be constructed from first principles
- `Research/backlog/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md` — added from issue; asks whether any operational risk, automation risk, or AI governance framework explicitly accounts for the removal of implicit rate-limiting controls (human speed, attention, fatigue, working hours) as a transition risk when moving from human to agentic operation, or whether this is a gap requiring first-principles construction from the automation risk literature
- `Research/backlog/2026-04-26-policy-coherence-machine-checkable-prerequisite.md` — added from issue; asks what the literature says about policy coherence as a prerequisite for automated enforcement and whether the policy-as-code literature — formal policy specification, Open Policy Agent (OPA) patterns, invariant registries — provides an applicable framework for a regulated financial institution deploying agentic AI
- `Research/backlog/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md` — added from issue; asks whether the deployment pipeline is the only enforceable control point for citizen-developed agents that does not suppress legitimate demand or drive behaviour underground; what pipeline hook points low-code platforms (Microsoft Copilot Studio, Power Platform) actually expose; and whether a pipeline-as-gate model is architecturally enforceable given that many platforms allow direct publication to production by default
- `Research/backlog/2026-04-26-agentic-ai-foundational-conditions-dependency-ordering.md` — synthesis item added from issue; asks what the correct dependency ordering is of the five foundational conditions (policy coherence → information architecture → access control → agent credential scoping → safe RAG deployment → deployment pipeline gate), what the consequence is of deploying at any layer before the layer below it is satisfied, and whether any existing framework encodes this ordering or whether it is a novel contribution

**Note on prior coverage:** Three mechanisms from the original issue were already covered by completed items from a prior session: mechanism 3 (systems capability debt as citizen development demand driver) is covered by `2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.md`; mechanism 7 (synthesis/novelty) is partially covered by `2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md`; and the regulatory preconditions dimension is covered by `2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.md`. The six items created in this session address the remaining mechanisms.

**Note on dependency ordering:** Items 1–5 each have `blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]` so the synthesis item cannot start until all five companion items are completed. The synthesis item itself has `blocks: []`.

## Mini-Retro

1. **Did the process work?** Yes. The issue's seven mechanisms mapped cleanly to six new backlog items (mechanism 3 was already covered by a prior session's completed item). The `blocks` field correctly encodes the dependency ordering in the backlog itself — the five mechanism items block the synthesis item.

2. **What slowed down or went wrong?** Determining which mechanisms were already covered by prior completed items required reading the completed item list and cross-checking with the issue's mechanism list. The `blocks` field correctly encodes the dependency from first principles, but the synthesis item cannot be started until the five mechanism items are all completed.

3. **What single change would prevent this next time?** Nothing specific — the process of checking existing completed items before creating new backlog items was the right approach and worked correctly.

4. **Is this a pattern?** Multi-part research issues with some prior coverage are becoming a pattern. The correct response is to map existing completed items to issue mechanisms before creating new items, which was done here.

5. **Does any documentation need updating?** No structural documentation changes needed. The `blocks` relationships between the six new items and the synthesis item are the correct cross-reference mechanism for the research loop to pick up.

6. **Do the default instructions need updating?** No new convention or constraint emerged from this session.

# 2026-05-17 -- Complete research item (aws-bedrock-agentcore-suite-capabilities)

**Completed:**
- `Research/completed/2026-05-17-aws-bedrock-agentcore-suite-capabilities.md` — completed the AgentCore capability survey, anchored it in current Amazon Web Services (AWS) primary documentation, and concluded that Amazon Bedrock AgentCore materially improves the Amazon Web Services (AWS) native control surface for production agents without removing the need for customer-owned identity, approval, retention, and evidence design.
- `learnings.md` — updated Thread 2 to capture the new corollary that AgentCore lowers coordination cost by bundling runtime isolation, workload identity, tool gateway, memory, and observability, while still leaving the practical enterprise control plane layered rather than complete by default.

**Key sources:**
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html

## Mini-Retro

1. **Did the process work?** Yes. The item converged cleanly once the evidence base stayed centered on Amazon Web Services (AWS) primary sources and the review feedback was applied literally rather than treated as stylistic guidance.
2. **What slowed down or went wrong?** The seeded source set included a stale Amazon Web Services (AWS) blog URL, and the review workflow again required reading the log directly because the run status was less informative than the underlying violations.
3. **What single change would prevent this next time?** No new repository change is needed beyond continuing the existing habit of validating seeded official URLs and reading the review log itself before treating the workflow as done.
4. **Is this a pattern?** Yes. This repeated the known pattern that research quality depends on checking the underlying review log, and it also showed again that seeded links can drift even when the topic is current.
5. **Does any documentation need updating?** Yes. `learnings.md` warranted an update because this item materially strengthened the existing transaction-cost and layered-control-plane thread.
6. **Do the default instructions need updating?** No. The existing instructions already pushed toward primary sources, log-first review reading, and explicit cross-item synthesis, which were the right controls here.

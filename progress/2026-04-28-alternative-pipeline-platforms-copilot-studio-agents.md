# 2026-04-28 -- Research Loop (alternative-pipeline-platforms-copilot-studio-agents)

**Completed:**

Research item:
- `Research/completed/2026-04-28-alternative-pipeline-platforms-copilot-studio-agents.md` -- completed; the item concludes that Harness, AWS CodePipeline plus CodeBuild, and Jenkins are all technically viable governance orchestrators for Microsoft Copilot Studio deployments, but none of them can make the deployment pipeline authoritative unless Microsoft-side publish, identity, environment, and data-policy controls also narrow the bypass path. It also finds that Harness has the strongest native governance surface, AWS is viable mainly through CodePipeline plus CodeBuild rather than CodeDeploy, and Jenkins is feasible but depends more heavily on self-authored control logic and thinner public implementation evidence.

Sources consulted:
- https://developer.harness.io/docs/platform/governance/policy-as-code/harness-governance-overview/ (Harness policy and governance surface)
- https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction (portable Microsoft deployment interface)
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance (Microsoft-side governance boundary)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, review workflow, and final completion path all worked end to end.
2. **What slowed down or went wrong?** The review workflow enforced a stricter distinction between search-derived scarcity claims and source-backed facts than the first draft used, so the item needed one extra pass to relabel those claims and lower two confidence levels.
3. **What single change would prevent this next time?** Nothing beyond the existing prompt rules; the current checklist already captures the failure mode once the item is read literally.
4. **Is this a pattern?** Yes. It matches the existing known pattern that cross-source continuity and absence-of-evidence judgments are usually inferences rather than facts.

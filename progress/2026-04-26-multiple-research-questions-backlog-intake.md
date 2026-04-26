# 2026-04-26 -- Add backlog items from multiple research questions issue

**Completed:**
- `Research/backlog/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md` — added from issue; asks whether the causal chain from systems capability debt through ungoverned citizen development to amplified agentic AI operational risk, and the "AI for risk reduction first" sequencing imperative, constitutes a genuinely novel contribution to the literature when synthesised across technical debt, transaction cost economics, operational risk frameworks, and citizen development research
- `Research/backlog/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.md` — added from issue; asks what empirical evidence exists that systems capability debt is the root cause of citizen development sprawl in regulated financial services, what its quantified operational risk cost is, and what governance architectures have measurably reduced citizen development sprawl without suppressing legitimate automation demand
- `Research/backlog/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.md` — added from issue; asks what organisational preconditions APRA CPS 230, DORA, PCI-DSS v4, ISO 42001, NIST SP 800-207/800-53, Basel Committee operational resilience principles, UK FCA/PRA AI guidance, and ISO 31000 require before deploying agentic AI, and whether deploying into the described environment (incomplete access control, unclassified data, ungoverned citizen development) constitutes a control failure

**Note on issue framing:** The issue requested distinct PRs for each question. This PR creates all three backlog items in a single branch because the Copilot agent operates in a single repository context per session. The items are independent (no `blocks` relationships between them) and can be picked up by the research loop in any order.

**Note on skills submodule:** The `.github/skills/` submodule was not initialised in the agent environment (no SKILL.md files accessible). The research-question skill process was applied from the documented instructions in `.github/copilot-instructions.md`. Gap noted but not blocking — items created using the documented template and process.

## Mini-Retro

1. **Did the process work?** Yes. The three questions in the issue were distinct and well-scoped enough to translate directly into backlog items without needing revision. The primary complexity was ensuring each question's scope was tight enough to be researchable in a single item while capturing the nuance of the original formulation.

2. **What slowed down or went wrong?** The issue requested "distinct PRs for each question" which cannot be fully honoured within a single agent session — the agent can only push to one branch and open one PR. All three items were created in this single PR. If strict PR separation is required, three separate agent sessions would be needed.

3. **What single change would prevent this next time?** If the owner wants one PR per research question, trigger one agent session per question rather than grouping them in a single issue. Alternatively, the instructions could clarify that "distinct PRs" in a multi-question issue means the agent creates all items in one PR and the owner manually separates if needed.

4. **Is this a pattern?** First occurrence of a multi-question issue in this repo. Not a recurring pattern yet.

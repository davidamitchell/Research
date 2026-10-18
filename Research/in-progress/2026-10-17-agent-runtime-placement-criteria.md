---
review_count: 2
title: "Runtime placement criteria for software-engineering agents in regulated organisations"
added: 2026-10-17T07:34:52+00:00
status: reviewing
priority: high
blocks: []
themes: [agentic-ai, governance-policy, security-risk, tools-infrastructure, regulatory-compliance]
started: 2026-10-18T03:18:13+00:00
completed: ~
output: [knowledge]
cites: [2026-08-12-ai-coding-agent-runtime-security-evolution, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-05-01-appropriate-task-selection-coding-agents, 2026-04-26-access-control-amplification-agentic-operations]
related: [2026-03-08-ai-coding-harnesses-agent-philosophy]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Runtime placement criteria for software-engineering agents in regulated organisations

## Research Question

For software-engineering agent workloads in a regulated organisation, what evidence-based conditions justify placing a workload in local execution on a developer workstation, a vendor-hosted coding-agent runtime, or an organisation-owned managed agent runtime? How do scaffolding maturity, identity and attribution, raw versus sanctioned reach, model choice, triggering, egress controls, risk, parallelism, and volume affect that placement, and what measurable criteria support moving forward, skipping a stage, or moving back?

## Scope

**In scope:**
- Placement decisions across local workstation, vendor-hosted, and organisation-owned managed runtimes.
- Whether agent input scaffolding and output validation maturity support unattended execution, and evidence that distinguishes their effect from model capability.
- Agent identity, delegation, credential scope and revocation, attribution, and audit records.
- Raw versus sanctioned access, local controls, vendor-hosted egress and tool enforcement, and organisation-owned cloud runners as an intermediate option.
- Model choice, workload triggers, and measurable placement thresholds for risk, scaffolding maturity, parallelism, and volume.

**Out of scope:**
- Isolation mechanics already covered by the cited runtime item, including microVM versus container choices and session persistence.
- Model economics and harness feature comparisons.

**Constraints:**
- Use primary vendor documentation and changelogs for factual claims; identify undocumented behavior rather than infer it.
- Keep the framing vendor-neutral, using named products only as worked examples.

## Context

The cited runtime research established the three execution stages and their security mechanics, while the identity research addressed agent identity; this item asks what makes moving a particular workload between those stages safe and worthwhile, with the working hypothesis that unattended trust depends more on scaffolding and validation than on supervision alone.

## Approach

1. Compare scaffolding and validation maturity across the three stages; assess evidence about unattended reliability and whether it tracks those controls independently of model capability.
2. For widely adopted vendor-hosted coding agents, establish from primary documentation which principal acts, how commits, pull requests, and audit events are attributed, what credentials and scopes are granted, when they are revoked, and what remains undocumented.
3. Compare raw and sanctioned reach across stages, identify controls that limit local access without changing stages, and determine whether vendor-hosted egress, tool access, and secrets are enforceable at organisation or repository level; assess organisation-cloud runners as an intermediate option.
4. Compare model-selection options and the available work triggers at each stage, including human, issue, event, and scheduled starts.
5. Build an evidence-backed placement matrix using measurable criteria for scaffolding maturity, risk classification, parallelism, and volume; distinguish evidence-supported thresholds from proposed decision rules and identify when to skip or move back a stage.

## Sources

- [Secure Runtime Evolution for AI Coding Agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md): cited work establishing the runtime stages and security mechanics.
- [Enterprise Agent Identity and Access Management](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md): cited work on agent identity, access, and attribution.
- [AI Coding Harnesses: Execution Model, Memory, and Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md): related work on coding-agent execution models.
- [arxiv.org 2310.06770](https://arxiv.org/abs/2310.06770)
- [arxiv.org 2405.15793](https://arxiv.org/abs/2405.15793)
- [arxiv.org 2407.01489](https://arxiv.org/abs/2407.01489)
- [arxiv.org 2607.05743](https://arxiv.org/abs/2607.05743)
- [aws.amazon.com its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore](https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/)
- [code.claude.com claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)
- [code.claude.com github-actions](https://code.claude.com/docs/en/github-actions)
- [code.claude.com sandboxing](https://code.claude.com/docs/en/sandboxing)
- [code.claude.com settings](https://code.claude.com/docs/en/settings)
- [docs.aws.amazon.com what-is-bedrock-agentcore.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [docs.github.com about-automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations)
- [docs.github.com about-cloud-agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [docs.github.com access-management](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/access-management)
- [docs.github.com risks-and-mitigations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations)
- [docs.github.com about-copilot-cli](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
- [docs.github.com review-audit-logs](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs)
- [docs.github.com configure-runner-for-coding-agent](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent)
- [docs.github.com use-byok-models](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models)
- [docs.github.com changing-the-ai-model](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model)
- [docs.github.com configuring-agent-settings](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings)
- [docs.github.com create-automations](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations)
- [docs.github.com customize-the-agent-environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)
- [docs.github.com customize-the-agent-firewall](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)
- [docs.github.com extend-cloud-agent-with-mcp](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp)
- [docs.github.com review-copilot-prs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs)
- [docs.github.com start-copilot-sessions](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions)
- [docs.github.com agentic-audit-log-events](https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events)
- [dora.dev dora-report](https://dora.dev/research/2025/dora-report/)
- [github.com 2026-04-26-access-control-amplification-agentic-operations.md](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)
- [github.com 2026-05-01-appropriate-task-selection-coding-agents.md](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md)
- [www.anthropic.com effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## Related

- [Secure Runtime Evolution for AI Coding Agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md)
- [Enterprise Agent Identity and Access Management](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md)
- [AI Coding Harnesses: Execution Model, Memory, and Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: for software-engineering agent workloads in a regulated organisation, which evidence-based conditions justify local execution on a developer workstation, a vendor-hosted coding-agent runtime, or an organisation-owned managed agent runtime, and which measurable criteria support moving forward, skipping a stage, or moving back.

Scope: placement across the three stages; scaffolding and validation maturity; identity, delegation, credential scope, revocation, attribution, audit; raw versus sanctioned reach; model choice; triggers; egress; risk, parallelism, volume. Isolation mechanics (microVM versus container, session persistence) and model economics are out of scope.

Constraints: primary vendor documentation and changelogs carry factual claims; undocumented behaviour is reported as undocumented; named products are worked examples only.

Output format: knowledge item with a placement matrix that separates evidence-supported statements from proposed decision rules.

Working hypothesis: [assumption; source: https://dora.dev/research/2025/dora-report/] unattended trust depends more on scaffolding and output validation than on supervision alone, because the 2025 DevOps Research and Assessment (DORA) report describes Artificial Intelligence (AI) as an amplifier of an organisation's existing strengths and weaknesses.

Plain-language definitions used in this item, written because no authoritative single definition exists for the coined labels. Definition needed: "scaffolding" here means the instructions, environment setup, tools, and context placed around a Large Language Model (LLM), and the nearest evidence-backed equivalent is the harness and context material described in the Anthropic long-running-agent harness post. [assumption; source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents] Definition needed: "raw reach" means access the agent obtains through the developer's own credentials and network, and "sanctioned reach" means access routed through paths the organisation has approved and can govern, and the nearest evidence-backed equivalent is the contrast between a sandbox default that reads most of the machine and credentials held outside the agent. [assumption; source: https://code.claude.com/docs/en/sandboxing; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/] "Egress" means outbound network traffic, "unattended" means no human watching each step, and a "harness" is the software that runs the agent loop around the model. [assumption; source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents]

Prior-research cross-reference: the repository's runtime item established the three stages and their isolation mechanics, [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md] the identity item established delegation, impersonation, and linked audit chains, [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md] the task-selection item identified verifier strength as the primary enabling condition for coding agents, [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md] the access-control item described autonomous triggers running with maker credentials, [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md] and the harness item described the local-versus-cloud divergence in execution environment. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md]

### §1 Question Decomposition

```text
Q1 scaffolding and validation maturity
  Q1.1 which published evidence links agent outcomes to scaffolding or validation
  Q1.2 does any consulted source separate that effect from model capability
  Q1.3 which controls gate unattended work in each stage
Q2 vendor-hosted attribution and credentials
  Q2.1 which principal acts, and how are commits, pull requests, audit events attributed
  Q2.2 which credentials and scopes are granted
  Q2.3 when are credentials revoked, and what is undocumented
Q3 reach and egress
  Q3.1 which local controls limit access without changing stage
  Q3.2 are vendor-hosted egress, tool access, secrets enforceable at organisation or repository level
  Q3.3 are organisation-owned runners an intermediate option, and on what terms
Q4 model choice and triggers per stage
Q5 placement matrix
  Q5.1 which criteria are measurable
  Q5.2 which thresholds have evidence and which are proposals
  Q5.3 when to skip a stage or move back
```

### §2 Investigation

#### Q1 Scaffolding, validation, and unattended reliability

The Software Engineering benchmark (SWE-bench) paper built 2,294 problems from real GitHub issues and reported that the best model it evaluated, Claude 2, solved 1.96% of them. [fact; source: https://arxiv.org/abs/2310.06770] That figure describes a 2023 baseline and no longer describes current agents, so it is used here only as a benchmark definition. [inference; source: https://arxiv.org/abs/2310.06770]

The SWE-agent paper reports that a purpose-built agent-computer interface significantly enhances an agent's ability to edit files, navigate repositories, and run tests, and that interface design affects agent behaviour and performance. [fact; source: https://arxiv.org/abs/2405.15793] The paper's abstract does not state a controlled comparison that holds the model fixed across scaffolds of differing maturity. [inference; source: https://arxiv.org/abs/2405.15793]

The Agentless paper reports that a fixed three-phase process of localization, repair, and patch validation reached 32.00% on SWE-bench Lite at a cost of $0.70, the highest result among the open-source agents it compared. [fact; source: https://arxiv.org/abs/2407.01489] Patch validation is one of the three phases in that design, which places output validation inside the best-performing configuration the paper reports. [inference; source: https://arxiv.org/abs/2407.01489]

Anthropic's harness post reports that Claude tended to mark a feature complete without end-to-end testing unless prompted, and that giving it browser-automation testing tools improved performance. [fact; source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents] The same post reports a JavaScript Object Notation (JSON) feature list in which agents may change only a pass flag, an input-side and output-side scaffold working together. [fact; source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents]

The 2025 DORA report states that AI primarily acts as an amplifier of an organisation's existing strengths and weaknesses, and that the greatest returns come from the underlying organisational system rather than the tools. [fact; source: https://dora.dev/research/2025/dora-report/]

The repository's task-selection item concluded that verifier strength is the primary enabling condition for coding-agent value, because a task needs a check that tests, linters, or review rubrics can run. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]

The consulted sources agree that scaffolding and validation affect agent outcomes, but none isolates their effect from model capability in a controlled comparison across the three runtime stages. [inference; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]

The hypothesis that unattended trust tracks scaffolding and validation more than supervision therefore has convergent supporting evidence and no direct test. [inference; source: https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]

Search note: no controlled study comparing unattended reliability across local, vendor-hosted, and organisation-owned stages with scaffolding held constant was found; query used "coding agent scaffold ablation same model unattended reliability" against the consulted source set, outcome not found. [assumption; source: https://arxiv.org/abs/2405.15793]

#### Q2 Vendor-hosted attribution, credentials, revocation

Copilot cloud agent commits are authored by Copilot with the developer who assigned the issue or requested the change marked as co-author. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

The agent's commits are signed and appear as Verified, and each agent-authored commit message includes a link to the agent session logs. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

Only users with write access can trigger the agent, comments from users without write access are not presented to it, and the agent can push to a single branch, either a new copilot/ branch or the branch of a pull request (PR) where it was mentioned. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

The agent is documented as performing simple push operations only and as not able to run git push or other Git commands directly. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

Pull requests from the agent are drafts that a human must review and merge, the agent is documented as unable to mark them ready for review, approve, or merge, and the user who asked for the pull request is prevented from approving it. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

When the agent opens a pull request under its own app identity, one more approval is required if the repository already requires at least one, and this is on by default in rulesets and always applies to branch protection rules. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

By default, GitHub Actions workflows do not run on the agent's pull request until a user with write access approves them, and a repository administrator can disable that approval requirement. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings]

For automations, pull requests and pushes are attributed to the user who created the automation, and that user cannot approve the resulting pull requests. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]

The agent audit-log event carries the fields action, actor_is_agent, agent_session_id, and user, where user is the person who initiated the event, and the actor:Copilot filter shows agentic activity for the last 180 days. [fact; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]

The enterprise audit-log page states that the log retains events for the last 180 days and recommends streaming it for longer retention. [fact; source: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs]

The setup-steps template says Copilot "will be given its own token for its operations", while the pages consulted state the token's behaviour (single-branch push, no direct Git) but give no lifetime, scope list, or revocation trigger. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

Search note: the terms token lifetime, expiry, and revocation were checked across the consulted Copilot cloud agent pages (about, risks and mitigations, environment, settings, automations) and found no stated value, outcome not found. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

The repository's identity item recommended that autonomous or scheduled work run under the agent's own pre-authorised identity rather than a retained user delegation token, because the user is no longer supervising. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md]

Copilot's documented design attributes an unattended automation's pull requests to its human creator while authoring commits as Copilot, which is a mixed pattern that differs from the identity item's recommendation. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md]

For the organisation-owned stage, the Amazon Web Services (AWS) AgentCore post describes three credential patterns, bot, on-behalf-of using Open Authorization (OAuth) 2.0 Token Exchange under Request for Comments (RFC) 8693, and broker, with the on-behalf-of pattern attributing pull requests to the human rather than a shared bot. [fact; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

The same post lists tying identity to the company identity provider (IdP), AWS CloudTrail records of every invocation, CloudWatch traces of every step, and credentials kept off disk inside the agent environment as the platform-team requirements the platform addresses. [fact; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

The Claude Code cloud environment keeps git credentials and signing keys outside the sandbox and uses a proxy that authenticates with scoped credentials, while a self-hosted environment requires the deployment to supply git credentials. [fact; source: https://code.claude.com/docs/en/claude-code-on-the-web]

#### Q3 Reach, egress, and organisation-owned runners

The Claude Code sandbox is off by default, covers shell commands only, and leaves file tools, Model Context Protocol (MCP) servers, and hooks outside it. [fact; source: https://code.claude.com/docs/en/sandboxing]

By default a sandboxed command can read most of the machine, and Claude Code runs commands without sandboxing if the sandbox cannot start unless the setting is changed. [fact; source: https://code.claude.com/docs/en/sandboxing]

Claude Code supports managed settings that an organisation deploys to every machine, and an organisation can enforce sandboxing for every developer through them. [fact; source: https://code.claude.com/docs/en/sandboxing; https://code.claude.com/docs/en/settings]

Only server-managed settings reach a Claude Code cloud session, so a locally deployed managed-settings file does not govern the cloud stage. [fact; source: https://code.claude.com/docs/en/settings]

Copilot Command Line Interface (CLI) asks the user to trust the launch directory, and its documentation states that permission scoping is heuristic and that GitHub does not guarantee protection of files outside trusted directories. [fact; source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli]

An automatic approval option in Copilot CLI gives the agent the same file and shell access as the developer, which makes the raw-reach end of the spectrum an explicit user choice. [fact; source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli]

Copilot cloud agent's firewall is on by default with a recommended allowlist, and organisation owners can set it to Enabled, Disabled, or Let repositories decide, and can disable repository custom rules. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]

The firewall applies only to processes the agent starts through its Bash tool, does not apply directly to MCP server processes or to configured setup steps, and GitHub states that sophisticated attacks may bypass it. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]

Repository administrators configure MCP servers for the agent, secrets for MCP servers must carry the COPILOT_MCP_ prefix, and remote MCP servers that use OAuth are not supported. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp]

Copilot cloud agent can run on larger GitHub-hosted runners, including with Azure private networking, or on self-hosted runners, and organisation owners can set a default runner type and stop repositories overriding it. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent]

The integrated firewall is documented as incompatible with self-hosted runners and must be disabled for them, GitHub recommends ephemeral single-use runners, and the organisation must configure its own network controls. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]

Self-hosted runners therefore trade GitHub's built-in egress control for the organisation's own, which makes the intermediate option stronger only where the organisation already operates stronger network controls than the built-in allowlist. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]

Anthropic-hosted Claude Code cloud environments limit network access by default and can disable it, though the Anthropic Application Programming Interface (API) stays reachable, and a self-hosted environment requires egress restriction at the organisation's own network boundary. [fact; source: https://code.claude.com/docs/en/claude-code-on-the-web]

The AgentCore post states that each session gets a dedicated isolated Linux microVM, a lightweight virtual machine (VM), and lists traffic flowing through the organisation's virtual private cloud (VPC) rather than the public internet as a platform-team requirement the platform addresses. [fact; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

The vendor-hosted stage limits Copilot cloud agent to the repository where the task starts, one branch, one pull request per task, and a 59-minute maximum session, which the documentation says cannot be extended. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

#### Q4 Model choice and triggers

Copilot CLI accepts models from OpenAI-compatible endpoints, Azure OpenAI, Anthropic, and local servers such as Ollama through bring your own key (BYOK), provided the model supports tool calling and streaming. [fact; source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models]

Copilot cloud agent offers a model picker only for issue assignment, @copilot pull request comments, the agents tab, agents panel, GitHub Mobile, and Raycast, and uses Auto elsewhere. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model]

Available models for the cloud agent depend on plan and account policies. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

AgentCore describes itself as usable with any framework and any foundation model, and its Runtime can host Claude Code, Codex, Kiro, OpenCode, Cursor CLI, Gemini CLI, or a custom harness. [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

Copilot CLI has a programmatic mode that takes a prompt, completes the task, and exits, and Claude Code's GitHub Action has an interactive mode that waits for an @claude mention and an automation mode that runs from a workflow prompt. [fact; source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli; https://code.claude.com/docs/en/github-actions]

Copilot cloud agent sessions start from GitHub issues, the agents tab, Copilot Chat, failing Actions runs, development environments, a Representational State Transfer (REST) API, the GitHub CLI, the GitHub MCP server, and chat tools including Jira, Slack, Microsoft Teams, Azure Boards, and Linear. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions]

Copilot automations start sessions on an hourly, daily, or weekly schedule or when an issue is created or a pull request is opened or synchronized, are limited to private and internal repositories, and let the creator choose the model and tools. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations]

Automations ignore events from users without write access by default, and the creator selects the tools an automation may use. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]

Automations are stored separately from the repository and are not versioned or reviewed through pull requests, and each automation is private to its creator even though the sessions it starts are visible to others with repository access. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]

The consulted AgentCore sources describe interactive and parallel session use but no built-in schedule or event trigger, so unattended starts on that stage would come from the organisation's own scheduling or event services. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

#### Q5 Parallelism, volume, and thresholds

The AgentCore post states that git worktree gives separate working directories while agents on one machine still share databases, ports, keyrings, and outbound IP, whereas each AgentCore session gets its own microVM and workspace. [fact; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

Copilot automations consume GitHub Actions minutes and GitHub AI Credits billed to the automation's creator on each run, so scheduled volume is a metered cost attached to one person's account. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]

The repository's runtime item recorded that a peer-reviewed systematisation of 39 papers found policy enforcement failing against real-world denylists at rates from 69% to 98%, which is evidence against treating any single egress control as sufficient at higher volume. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md]

The repository's access-control item records Microsoft's warning that autonomous triggers can run with maker credentials, which is the same unattended-start risk that Copilot's creator-attribution rule addresses by blocking self-approval. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]

None of the consulted sources publishes a numeric threshold for risk class, scaffolding maturity, parallelism, or volume at which a workload should change stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://code.claude.com/docs/en/claude-code-on-the-web]

Search note: the query "coding agent runtime placement threshold parallelism volume risk" over the consulted vendor documentation and papers returned no numeric placement thresholds, outcome not found. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

### §3 Reasoning

Causal chain for the central hypothesis, each link labelled separately.

1. Agent outcomes in the consulted studies vary with interface, validation, and testing tooling. [fact; source: https://arxiv.org/abs/2405.15793; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents]
2. The unattended-start controls in Copilot's documentation are gates on inputs or outputs (write-access check, tool allowlist, untrusted-event filter, workflow approval, extra approval), not a requirement that a human watch the session. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]
3. A stage change that removes live supervision is therefore defensible only if those gates exist and are enforced in the target stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
4. The strength of the effect relative to model capability is unmeasured in the consulted sources. [inference; source: https://arxiv.org/abs/2407.01489; https://dora.dev/research/2025/dora-report/]
5. The placement rules below are proposed decision rules, not empirically derived thresholds. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://code.claude.com/docs/en/claude-code-on-the-web]

Facts, inferences, and assumptions stay separated: vendor behaviour statements in §2 are facts bound to the documentation page that makes them, the comparisons across stages are inferences, and the AgentCore trigger gap is an assumption.

### §4 Consistency Check

```text
contradiction_scan: resolved
contradiction_1: identity item recommends own identity for unattended work; Copilot attributes automation pull requests to creator; recorded as divergence, not as error
contradiction_2: Copilot commits authored by Copilot while automation pull requests attributed to creator; reconciled as commit author versus pull request actor
confidence_adjustment: all vendor-documentation claims kept at medium because each rests on one vendor family
scope_guardrail: maintained; isolation mechanics and model economics excluded
```

Resolution of contradiction 2: the risks page states commits are authored by Copilot while the automations page states pull requests and pushes are attributed to the automation creator, and these describe different artefacts, so both stand. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]

### §5 Depth and Breadth Expansion

Regulatory lens. Regulated organisations need to reconstruct who initiated an action and which machine identity acted. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md] The Copilot audit event fields user, agent_session_id, and actor_is_agent cover the initiator and session hops, but the consulted pages do not document the credential-exchange hop that the identity item says a complete chain needs. [inference; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md] A stage that exposes that hop, such as one with CloudTrail records of every invocation, closes the documentation gap for the organisation. [inference; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

Technical lens. Local sandboxes are opt-in and partial, with the Claude Code sandbox covering shell commands only. [fact; source: https://code.claude.com/docs/en/sandboxing] Vendor-hosted firewalls are on by default but partial, since they do not cover MCP server processes or setup steps. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall] No stage in the consulted sources offers complete egress control from the vendor alone, so the egress criterion in a placement decision is the coverage of the control, not its presence. [inference; source: https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]

Economic lens. Scheduled automations bill one creator's account on every run, so a high-volume schedule concentrates cost and attribution on one person. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations] Organisation-owned runtimes shift operating effort to the organisation, which the AgentCore post frames as removing infrastructure assembly for the platform team. [inference; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

Behavioural lens. Automatic approval options let a developer move to raw reach by choice. [fact; source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli] Organisation-enforced managed settings are the documented counter for the local stage, but they do not reach cloud sessions, so a developer who moves work to a cloud session leaves local managed policy behind. [inference; source: https://code.claude.com/docs/en/settings; https://code.claude.com/docs/en/sandboxing]

Historical and recency lens. Vendor documentation in this area changes quickly, and the model list in the Copilot documentation is a point-in-time snapshot, so model-choice statements carry recency risk. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model]

Rival-remedy lens. A rival to moving stage is strengthening scaffolding in place, for example adding tests and required checks, which the task-selection item treats as the primary enabling condition. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md] A second rival is keeping a human in the loop for every item, which the consulted documentation supports for local and interactive use but which the documented automation controls replace with gates. [inference; source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]

### §6 Synthesis

**Executive Summary:**

A workload should move from local execution to a vendor-hosted or organisation-owned runtime only when the target stage enforces input and output gates, complete attribution, and egress control that the workload's risk class requires, and the consulted sources support this as a decision rule while publishing no numeric thresholds for it. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://code.claude.com/docs/en/sandboxing; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
Vendor-hosted Copilot cloud agent documents write-access gating, single-branch push, human merge, an extra approval for agent-identity pull requests, and audit events with initiator and session identifiers, while leaving credential lifetime and revocation undocumented in the pages consulted. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
Its firewall covers only processes the agent starts through its Bash tool and is incompatible with self-hosted runners, so organisation-owned runners are an intermediate stage whose egress control becomes the organisation's own responsibility. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The hypothesis that unattended trust tracks scaffolding and validation more than supervision has convergent support from agent research, vendor engineering, and the 2025 DevOps Research and Assessment (DORA) report, but no consulted source isolates that effect from model capability. [inference; source: https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]

**Key Findings:**

1. Copilot cloud agent attributes commits to Copilot with the requesting developer as co-author, signs them, links each commit to its session log, restricts pushes to one branch, and requires a human to merge, which together give the vendor-hosted stage a documented attribution and merge-gating design. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs)
2. Agent audit-log events carry the action, an actor_is_agent flag, an agent_session_id, and the initiating user, and the enterprise audit log retains events for 180 days, so initiator and session hops are recorded for the vendor-hosted stage while longer retention needs log streaming. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs)
3. The Copilot cloud agent pages consulted describe its token only behaviourally, as single-branch push without direct Git commands, and state no token lifetime, scope list, or revocation trigger, so credential revocation for the vendor-hosted stage is undocumented in the sources used. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)
4. Copilot attributes an unattended automation's pull requests to its human creator and blocks that creator from approving them, which differs from the identity item's recommendation that unattended work run under the agent's own identity and shows vendors choosing creator-attribution plus approval separation. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md)
5. Copilot's firewall can be enabled, disabled, or delegated at organisation level with repository custom rules lockable, yet it covers only processes the agent starts through Bash and not MCP server processes or setup steps, so organisation-level enforceability exists but with documented coverage gaps. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)
6. Running Copilot cloud agent on self-hosted or Azure-private-network runners gives an organisation-owned intermediate option with an organisation-wide default runner, but the built-in firewall must be disabled for self-hosted runners and the organisation must supply network controls. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent)
7. Local agents have opt-in, partial controls from independent vendors: the Claude Code sandbox is off by default and covers shell commands only, and Copilot CLI states that its permission scoping is heuristic and unguaranteed outside trusted directories. ([fact]; medium confidence; source: https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
8. Organisation-deployed managed settings can enforce local Claude Code sandboxing, but only server-managed settings reach cloud sessions, so moving a task to a cloud stage leaves a locally deployed policy behind. ([fact]; medium confidence; source: https://code.claude.com/docs/en/settings; https://code.claude.com/docs/en/sandboxing)
9. Model choice widens with each stage, from bring-your-own-key models locally, to a plan-dependent picker or Auto on the vendor-hosted agent, to any framework and foundation model on an organisation-owned runtime, and triggers widen from human start through issue, schedule, and event starts in the vendor-hosted stage. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations)
10. The vendor-hosted Copilot agent works in one repository, on one branch, with one pull request per task and a 59-minute session limit documented as non-extendable, so tasks that span repositories or run longer are candidates to skip to an organisation-owned runtime. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
11. Agent research, vendor engineering, and the 2025 DORA report agree that scaffolding, validation, and surrounding organisational systems change agent outcomes, but no consulted source separates that effect from model capability across stages, so the scaffolding-over-supervision hypothesis remains supported without being tested. ([inference]; medium confidence; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/)
12. No consulted source publishes numeric placement thresholds for scaffolding maturity, risk class, parallelism, or volume, so every threshold in the placement matrix is a proposed decision rule that an organisation must calibrate against its own baselines. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://code.claude.com/docs/en/claude-code-on-the-web)

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Copilot commits authored by Copilot with co-author, signed, session-linked; one-branch push; human merge | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs | medium | Single vendor family |
| [fact] Agent audit events carry actor_is_agent, agent_session_id, user; 180-day retention | https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs | medium | Single vendor family |
| [inference] Token lifetime, scope list, revocation undocumented in pages consulted | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment | medium | Absence claim limited to pages consulted |
| [inference] Automation creator-attribution differs from identity item's own-identity recommendation | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md | medium | Cross-source comparison |
| [fact] Firewall configurable at organisation level; excludes MCP server processes and setup steps | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall | medium | Vendor states bypass potential |
| [fact] Self-hosted or private-network runners supported; firewall disabled for self-hosted; organisation default runner | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent | medium | Single vendor family |
| [fact] Claude Code sandbox off by default, shell only; Copilot CLI scoping heuristic | https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli | medium | Two vendors, vendor self-description |
| [fact] Managed settings enforce local sandbox; only server-managed settings reach cloud sessions | https://code.claude.com/docs/en/settings; https://code.claude.com/docs/en/sandboxing | medium | Single vendor family |
| [fact] Model choice and triggers widen by stage | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations | medium | Model list is a point-in-time snapshot |
| [inference] Single-repo, single-branch, 59-minute limits mark skip-forward candidates | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent | medium | Limits quoted from vendor |
| [inference] Scaffolding and validation affect outcomes; effect not isolated from model capability | https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/ | medium | No controlled cross-stage study found |
| [inference] No numeric placement thresholds published in consulted sources | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://code.claude.com/docs/en/claude-code-on-the-web | medium | Absence claim limited to sources consulted |

**Placement Matrix:**

Each row is a proposed decision rule, not an evidence-derived threshold, and each carries its own label and sources.

| Decision | Proposed rule | Label and sources |
|---|---|---|
| Stay local | Keep a workload local when a developer watches the session, the task has weak or absent automated checks, and one agent runs per developer, with the sandbox and managed settings enforced where the organisation deploys them. | [inference; source: https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli] |
| Move to vendor-hosted | Move a bounded single-repository task to the vendor-hosted agent when required status checks and a second human approval already gate merges, the firewall is enabled with an organisation allowlist, and the task fits the session limit. | [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent] |
| Use organisation-owned runners with a vendor harness | Choose this intermediate stage when the task needs internal network resources or private networking and the organisation already operates egress controls stronger than the built-in allowlist. | [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall] |
| Move to an organisation-owned managed runtime | Choose this stage when the work needs multiple repositories, sessions beyond the vendor limit, identity tied to the organisation's identity provider, invocation records in the organisation's own stack, or a model or harness the vendor stage does not offer. | [inference; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent] |
| Skip a stage | Go from local directly to an organisation-owned stage when the vendor-hosted stage is disabled by policy, lacks a required control such as credential-revocation documentation, or cannot meet data-handling constraints. | [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/access-management; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment] |
| Move back | Return a workload to a more supervised stage when gate coverage drops below the entry condition, an agent-authored change cannot be traced to initiator and session, egress blocks reveal unsanctioned destinations, or post-merge defects traced to agent changes exceed the human baseline. | [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall] |

Measurable criteria for the matrix, each a metric whose cut-off an organisation sets from its own baseline because no consulted source supplies a number. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Gate coverage is the share of agent-initiated changes that pass required checks and a second human approval before merge. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
Attribution completeness is the share of agent-authored changes traceable to initiator, machine identity, and session. [assumption; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
Egress coverage is the share of agent-started processes under an enforced allowlist, together with the count of blocked-request warnings. [assumption; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
Validation escape rate is the count of post-merge defects traced to agent changes relative to the human baseline. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
Session fit is the share of tasks that hit the session limit or need more than one repository. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Concurrency collision count is the number of shared-host conflicts (ports, databases, credentials) among parallel local agents. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

**Assumptions:**

Organisation-owned runtimes are assumed to start unattended work through the organisation's own scheduling and event services because the consulted AgentCore sources describe no built-in trigger. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
That assumption is reasonable because the post presents invocation, identity, and observability as platform services while showing interactive and parallel use only. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
The proposed criteria are assumed to be measurable from existing repository, audit-log, and firewall data without new instrumentation. [assumption; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
The audit-log fields, firewall warnings, and pull request records documented by the vendor make that assumption plausible for the vendor-hosted stage, though it is untested for the other stages. [assumption; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
The absence of a numeric threshold in the consulted documentation is assumed to mean none is published, not that none exists in other sources. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Reading only the pages cited here is the item's stated evidence base, so the claim is scoped to it. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

**Analysis:**

The evidence on scaffolding is consistent in direction across a benchmark paper, an interface-design paper, a vendor harness post, and an industry report, yet each measures a different thing, so the item treats the hypothesis as supported and untested. [inference; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]
The vendor documentation is the strongest source for what each stage does, because it describes controls the vendor ships, and the weakest for how well they work, because it contains no measured outcomes. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
The documented unattended controls in Copilot are gates and attribution rules rather than live supervision, which supports placing unattended work where those gates are enforced. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]
Moving a workload forward trades local convenience for governed attribution, and the matrix above makes each move conditional on a named control being present in the target stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md]
Strengthening scaffolding in place is a rival to changing stage, and the task-selection item's finding that verifier strength is the primary enabling condition supports doing that first. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
Adding reviewers to keep per-item human review is a second rival, and the documented Copilot controls already require a human merge, so the remaining question is which items need a live watcher in addition. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
The organisation-owned runner stage is the only documented way to combine the vendor harness with the organisation's own network boundary, and its value depends on the organisation's existing controls. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The runtime item reports that a 39-paper systematisation found denylist enforcement failing at 69% to 98% in reviewed studies, which argues against relying on any one egress control, which is why the matrix pairs egress with gates and attribution. [inference; source: https://arxiv.org/abs/2607.05743; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md]
The access-control item's finding that autonomous triggers can run with maker credentials explains why creator attribution plus approval separation matters for scheduled work. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]
The harness item's observation that local tools favour developer sovereignty and cloud tools favour organisational governance matches the pattern in the matrix. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md]

**Risks, Gaps, and Uncertainties:**

Credential lifetime, scope list, and revocation behaviour for the vendor-hosted agent are absent from the pages consulted, which leaves a gap in any regulatory attribution argument for that stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The evidence base is one vendor family per stage, with Copilot for vendor-hosted, Claude Code for local and cloud examples, and AWS for the organisation-owned stage, so conclusions about "the stage" generalise from worked examples. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://code.claude.com/docs/en/claude-code-on-the-web; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
No controlled study separates scaffolding effect from model capability or compares unattended reliability across the three stages. [inference; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489]
The consulted AgentCore sources do not document a built-in schedule or event trigger, so the organisation-owned trigger row rests on an assumption. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
Vendor documentation changes quickly, including the model list and automation features, so the findings carry recency risk. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations]
The proposed matrix thresholds are untested against real workloads. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

**Open Questions:**

- Which controlled comparison could isolate scaffolding and validation effects from model capability for unattended coding agents across stages? [assumption; source: https://arxiv.org/abs/2407.01489]
- What are the documented lifetime and revocation properties of the credentials that vendor-hosted agents use, and can an administrator revoke them mid-session? [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
- How should the credential-exchange hop be recorded for vendor-hosted agents so the linked audit chain in the identity item is complete? [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md]

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
```

---

## Findings

### Executive Summary

A workload should move from local execution to a vendor-hosted or organisation-owned runtime only when the target stage enforces input and output gates, complete attribution, and egress control that the workload's risk class requires, and the consulted sources support this as a decision rule while publishing no numeric thresholds for it. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://code.claude.com/docs/en/sandboxing; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
Vendor-hosted Copilot cloud agent documents write-access gating, single-branch push, human merge, an extra approval for agent-identity pull requests, and audit events with initiator and session identifiers, while leaving credential lifetime and revocation undocumented in the pages consulted. [fact; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
Its firewall covers only processes the agent starts through its Bash tool and is incompatible with self-hosted runners, so organisation-owned runners are an intermediate stage whose egress control becomes the organisation's own responsibility. [fact; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The hypothesis that unattended trust tracks scaffolding and validation more than supervision has convergent support from agent research, vendor engineering, and the 2025 DevOps Research and Assessment (DORA) report, but no consulted source isolates that effect from model capability. [inference; source: https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]

### Key Findings

1. Copilot cloud agent attributes commits to Copilot with the requesting developer as co-author, signs them, links each commit to its session log, restricts pushes to one branch, and requires a human to merge, which together give the vendor-hosted stage a documented attribution and merge-gating design. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs)
2. Agent audit-log events carry the action, an actor_is_agent flag, an agent_session_id, and the initiating user, and the enterprise audit log retains events for 180 days, so initiator and session hops are recorded for the vendor-hosted stage while longer retention needs log streaming. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs)
3. The Copilot cloud agent pages consulted describe its token only behaviourally, as single-branch push without direct Git commands, and state no token lifetime, scope list, or revocation trigger, so credential revocation for the vendor-hosted stage is undocumented in the sources used. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)
4. Copilot attributes an unattended automation's pull requests to its human creator and blocks that creator from approving them, which differs from the identity item's recommendation that unattended work run under the agent's own identity and shows vendors choosing creator-attribution plus approval separation. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md)
5. Copilot's firewall can be enabled, disabled, or delegated at organisation level with repository custom rules lockable, yet it covers only processes the agent starts through Bash and not MCP server processes or setup steps, so organisation-level enforceability exists but with documented coverage gaps. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)
6. Running Copilot cloud agent on self-hosted or Azure-private-network runners gives an organisation-owned intermediate option with an organisation-wide default runner, but the built-in firewall must be disabled for self-hosted runners and the organisation must supply network controls. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent)
7. Local agents have opt-in, partial controls from independent vendors: the Claude Code sandbox is off by default and covers shell commands only, and Copilot CLI states that its permission scoping is heuristic and unguaranteed outside trusted directories. ([fact]; medium confidence; source: https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
8. Organisation-deployed managed settings can enforce local Claude Code sandboxing, but only server-managed settings reach cloud sessions, so moving a task to a cloud stage leaves a locally deployed policy behind. ([fact]; medium confidence; source: https://code.claude.com/docs/en/settings; https://code.claude.com/docs/en/sandboxing)
9. Model choice widens with each stage, from bring-your-own-key models locally, to a plan-dependent picker or Auto on the vendor-hosted agent, to any framework and foundation model on an organisation-owned runtime, and triggers widen from human start through issue, schedule, and event starts in the vendor-hosted stage. ([fact]; medium confidence; source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations)
10. The vendor-hosted Copilot agent works in one repository, on one branch, with one pull request per task and a 59-minute session limit documented as non-extendable, so tasks that span repositories or run longer are candidates to skip to an organisation-owned runtime. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
11. Agent research, vendor engineering, and the 2025 DORA report agree that scaffolding, validation, and surrounding organisational systems change agent outcomes, but no consulted source separates that effect from model capability across stages, so the scaffolding-over-supervision hypothesis remains supported without being tested. ([inference]; medium confidence; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/)
12. No consulted source publishes numeric placement thresholds for scaffolding maturity, risk class, parallelism, or volume, so every threshold in the placement matrix is a proposed decision rule that an organisation must calibrate against its own baselines. ([inference]; medium confidence; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://code.claude.com/docs/en/claude-code-on-the-web)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Copilot commits authored by Copilot with co-author, signed, session-linked; one-branch push; human merge | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs | medium | Single vendor family |
| [fact] Agent audit events carry actor_is_agent, agent_session_id, user; 180-day retention | https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs | medium | Single vendor family |
| [inference] Token lifetime, scope list, revocation undocumented in pages consulted | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment | medium | Absence claim limited to pages consulted |
| [inference] Automation creator-attribution differs from identity item's own-identity recommendation | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md | medium | Cross-source comparison |
| [fact] Firewall configurable at organisation level; excludes MCP server processes and setup steps | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall | medium | Vendor states bypass potential |
| [fact] Self-hosted or private-network runners supported; firewall disabled for self-hosted; organisation default runner | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent | medium | Single vendor family |
| [fact] Claude Code sandbox off by default, shell only; Copilot CLI scoping heuristic | https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli | medium | Two vendors, vendor self-description |
| [fact] Managed settings enforce local sandbox; only server-managed settings reach cloud sessions | https://code.claude.com/docs/en/settings; https://code.claude.com/docs/en/sandboxing | medium | Single vendor family |
| [fact] Model choice and triggers widen by stage | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations | medium | Model list is a point-in-time snapshot |
| [inference] Single-repo, single-branch, 59-minute limits mark skip-forward candidates | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent | medium | Limits quoted from vendor |
| [inference] Scaffolding and validation affect outcomes; effect not isolated from model capability | https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/ | medium | No controlled cross-stage study found |
| [inference] No numeric placement thresholds published in consulted sources | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://code.claude.com/docs/en/claude-code-on-the-web | medium | Absence claim limited to sources consulted |

### Placement Matrix

Each row is a proposed decision rule, not an evidence-derived threshold, and each carries its own label and sources.

| Decision | Proposed rule | Label and sources |
|---|---|---|
| Stay local | Keep a workload local when a developer watches the session, the task has weak or absent automated checks, and one agent runs per developer, with the sandbox and managed settings enforced where the organisation deploys them. | [inference; source: https://code.claude.com/docs/en/sandboxing; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli] |
| Move to vendor-hosted | Move a bounded single-repository task to the vendor-hosted agent when required status checks and a second human approval already gate merges, the firewall is enabled with an organisation allowlist, and the task fits the session limit. | [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent] |
| Use organisation-owned runners with a vendor harness | Choose this intermediate stage when the task needs internal network resources or private networking and the organisation already operates egress controls stronger than the built-in allowlist. | [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall] |
| Move to an organisation-owned managed runtime | Choose this stage when the work needs multiple repositories, sessions beyond the vendor limit, identity tied to the organisation's identity provider, invocation records in the organisation's own stack, or a model or harness the vendor stage does not offer. | [inference; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent] |
| Skip a stage | Go from local directly to an organisation-owned stage when the vendor-hosted stage is disabled by policy, lacks a required control such as credential-revocation documentation, or cannot meet data-handling constraints. | [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/access-management; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment] |
| Move back | Return a workload to a more supervised stage when gate coverage drops below the entry condition, an agent-authored change cannot be traced to initiator and session, egress blocks reveal unsanctioned destinations, or post-merge defects traced to agent changes exceed the human baseline. | [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall] |

Measurable criteria for the matrix, each a metric whose cut-off an organisation sets from its own baseline because no consulted source supplies a number. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Gate coverage is the share of agent-initiated changes that pass required checks and a second human approval before merge. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
Attribution completeness is the share of agent-authored changes traceable to initiator, machine identity, and session. [assumption; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
Egress coverage is the share of agent-started processes under an enforced allowlist, together with the count of blocked-request warnings. [assumption; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
Validation escape rate is the count of post-merge defects traced to agent changes relative to the human baseline. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
Session fit is the share of tasks that hit the session limit or need more than one repository. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Concurrency collision count is the number of shared-host conflicts (ports, databases, credentials) among parallel local agents. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]

### Assumptions

Organisation-owned runtimes are assumed to start unattended work through the organisation's own scheduling and event services because the consulted AgentCore sources describe no built-in trigger. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
That assumption is reasonable because the post presents invocation, identity, and observability as platform services while showing interactive and parallel use only. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
The proposed criteria are assumed to be measurable from existing repository, audit-log, and firewall data without new instrumentation. [assumption; source: https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events]
The audit-log fields, firewall warnings, and pull request records documented by the vendor make that assumption plausible for the vendor-hosted stage, though it is untested for the other stages. [assumption; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
The absence of a numeric threshold in the consulted documentation is assumed to mean none is published, not that none exists in other sources. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]
Reading only the pages cited here is the item's stated evidence base, so the claim is scoped to it. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

### Analysis

The evidence on scaffolding is consistent in direction across a benchmark paper, an interface-design paper, a vendor harness post, and an industry report, yet each measures a different thing, so the item treats the hypothesis as supported and untested. [inference; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489; https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents; https://dora.dev/research/2025/dora-report/]
The vendor documentation is the strongest source for what each stage does, because it describes controls the vendor ships, and the weakest for how well they work, because it contains no measured outcomes. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall]
The documented unattended controls in Copilot are gates and attribution rules rather than live supervision, which supports placing unattended work where those gates are enforced. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations]
Moving a workload forward trades local convenience for governed attribution, and the matrix above makes each move conditional on a named control being present in the target stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md]
Strengthening scaffolding in place is a rival to changing stage, and the task-selection item's finding that verifier strength is the primary enabling condition supports doing that first. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
Adding reviewers to keep per-item human review is a second rival, and the documented Copilot controls already require a human merge, so the remaining question is which items need a live watcher in addition. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
The organisation-owned runner stage is the only documented way to combine the vendor harness with the organisation's own network boundary, and its value depends on the organisation's existing controls. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The runtime item reports that a 39-paper systematisation found denylist enforcement failing at 69% to 98% in reviewed studies, which argues against relying on any one egress control, which is why the matrix pairs egress with gates and attribution. [inference; source: https://arxiv.org/abs/2607.05743; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-12-ai-coding-agent-runtime-security-evolution.md]
The access-control item's finding that autonomous triggers can run with maker credentials explains why creator attribution plus approval separation matters for scheduled work. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]
The harness item's observation that local tools favour developer sovereignty and cloud tools favour organisational governance matches the pattern in the matrix. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md]

### Risks, Gaps, and Uncertainties

Credential lifetime, scope list, and revocation behaviour for the vendor-hosted agent are absent from the pages consulted, which leaves a gap in any regulatory attribution argument for that stage. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment]
The evidence base is one vendor family per stage, with Copilot for vendor-hosted, Claude Code for local and cloud examples, and AWS for the organisation-owned stage, so conclusions about "the stage" generalise from worked examples. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent; https://code.claude.com/docs/en/claude-code-on-the-web; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
No controlled study separates scaffolding effect from model capability or compares unattended reliability across the three stages. [inference; source: https://arxiv.org/abs/2405.15793; https://arxiv.org/abs/2407.01489]
The consulted AgentCore sources do not document a built-in schedule or event trigger, so the organisation-owned trigger row rests on an assumption. [assumption; source: https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/]
Vendor documentation changes quickly, including the model list and automation features, so the findings carry recency risk. [inference; source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations]
The proposed matrix thresholds are untested against real workloads. [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent]

### Open Questions

- Which controlled comparison could isolate scaffolding and validation effects from model capability for unattended coding agents across stages? [assumption; source: https://arxiv.org/abs/2407.01489]
- What are the documented lifetime and revocation properties of the credentials that vendor-hosted agents use, and can an administrator revoke them mid-session? [assumption; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
- How should the credential-exchange hop be recorded for vendor-hosted agents so the linked audit chain in the identity item is complete? [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-identity-access-management-enterprise.md]

---

## Output

- Type: knowledge
- Description: A placement matrix and measurable criteria for locating software-engineering agent workloads across local, vendor-hosted, and organisation-owned runtimes, separating documented vendor controls from proposed decision rules. [inference; source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations]
- Links: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations; https://code.claude.com/docs/en/sandboxing; https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/

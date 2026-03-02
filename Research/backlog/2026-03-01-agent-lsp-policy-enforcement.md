---
title: "Guiding Headless Agents via LSP-Like Mechanisms for Org Policy Conformance"
added: 2026-03-01
status: backlog
priority: high
tags: [agentic-coding, lsp, policy-enforcement, headless-agents, architecture-governance, security, developer-tooling]
started: ~
completed: ~
output: [knowledge]
---

# Guiding Headless Agents via LSP-Like Mechanisms for Org Policy Conformance

## Research Question

Who is building solutions that allow headless autonomous coding agents to be guided in real time by LSP-like mechanisms — rather than CI gates or pre-commit hooks — to conform to an organisation's security, architectural, and engineering policies? What is the current state of the art, and what is the protocol or project the user heard referred to as "LSAP" or "LASP"?

## Scope

**In scope:**
- Language Server Protocol (LSP) as a real-time feedback mechanism for agents: how IDEs use JSON-RPC to push errors and hints, and whether agents can consume the same wire protocol
- "LSAP" / "LASP" acronym: identify the specific project, paper, or working group the user is likely referring to — "Language Server Agent Protocol", "Language Agent Standard Protocol", or equivalent
- Headless agent use cases: coding agents running in CI-like environments (no IDE), agentic frameworks (LangChain, AutoGen, CrewAI, Devin, GitHub Copilot Workspace, Cursor background agents), and how they currently receive policy feedback
- Approaches that trigger feedback *before* code is committed: in-loop guidance vs. post-hoc gates
- Custom LSP implementations: projects building policy-as-code LSP servers (e.g. OPA + LSP, Semgrep LSP, custom rule engines exposed as language servers)
- Agent-native policy enforcement: MCP tools, system-prompt injection, tool-use wrappers that simulate LSP-style feedback without a true LSP server

**Out of scope:**
- CI/CD pipeline policy gates (SonarQube, Checkov, Trivy) — the problem explicitly excludes these
- Pre-commit hooks — also explicitly excluded
- General AI governance and compliance frameworks (covered by other items)
- IDE-only tooling with no headless/agent path

**Constraints:** Focus on production or credible prototype solutions, not purely academic proposals. Prefer solutions that have been deployed with an autonomous agent, not just with a human developer.

## Context

An IDE-based coding agent (e.g. Cursor, GitHub Copilot in VS Code) receives LSP diagnostics natively via the editor's existing language client. Custom LSP servers can inject organisation-specific policy violations as "errors" or "hints" directly into the agent's context, guiding it away from forbidden patterns before any code is committed. This is fundamentally different from a CI gate: the agent can self-correct mid-generation rather than receiving feedback only after a full commit cycle.

For *headless* agents — those running in CI pipelines, agentic frameworks, or background workers with no editor host — the IDE context is absent. The JSON-RPC channel the LSP uses to communicate with the editor has no host process. The question is whether:

1. A headless agent runtime can act as its own LSP *client*, opening a connection to a policy-enforcement language server and requesting diagnostics during code generation.
2. An alternative protocol (LSAP / LASP) has emerged that adapts LSP semantics to an agent-native context.
3. The problem is currently solved via workarounds (MCP tool calls, system prompt injection, sandboxed execution with feedback loops) rather than a clean protocol.

This is high priority because any serious enterprise deployment of autonomous coding agents will need a mechanism for real-time policy conformance that does not rely solely on post-hoc gates. The answer will inform tooling choices and potentially a new backlog item to build or integrate such a mechanism.

## Approach

1. **Identify LSAP / LASP** — Search for the specific acronym and associated project. Candidates: "Language Server Agent Protocol" (any Microsoft/VS Code or LSP working group initiative), "LASP" (Language Agent Standard Protocol), any IETF/W3C/OpenAI/Anthropic spec in this space. Check GitHub, arXiv, and VS Code / LSP specification discussions.
2. **LSP as an agent feedback channel** — Document how LSP JSON-RPC works (initialize → textDocument/didOpen → textDocument/publishDiagnostics) and whether an agent process can act as an LSP client without an IDE host. Look for existing headless LSP client libraries (e.g. `pylsp`, `node-lsp-client`, `lsp-client` in Go).
3. **Policy-as-code LSP servers** — Identify production or open-source LSP servers designed for policy enforcement: OPA (Open Policy Agent) LSP extensions, Semgrep's LSP server mode, any custom implementations. Can these be consumed by a headless agent?
4. **Agent frameworks with in-loop policy feedback** — Survey how major agentic coding frameworks (AutoGen, CrewAI, LangGraph, Devin, GitHub Copilot Workspace) currently handle policy conformance. Is there a pattern emerging for in-loop feedback?
5. **Emerging protocols and initiatives** — Review the VS Code agent mode, Anthropic MCP, and any draft specifications for agent-to-tool-server protocols that overlap with LSP's diagnostic model.
6. **Gap analysis** — Identify the gap between what exists today and what a full "LSP-guided headless agent" would require. Frame as potential backlog items (tooling to build or integrate).

## Sources

- [ ] LSP Specification: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/ — particularly `textDocument/publishDiagnostics` and the JSON-RPC transport
- [ ] VS Code extension docs on agent mode and custom language server integration
- [ ] GitHub: search `lsap agent lsp`, `lasp language agent`, `headless lsp client agent` for relevant repos
- [ ] arXiv: search "language server protocol agent" and "LSAP" for any academic framing
- [ ] OPA (Open Policy Agent) LSP extension or plugin documentation
- [ ] Semgrep LSP server mode documentation
- [ ] AutoGen / Microsoft: any policy-enforcement mechanisms in agentic coding pipelines
- [ ] Devin (Cognition AI) public documentation on policy or constraint mechanisms
- [ ] Anthropic MCP specification — tool-use patterns that simulate in-loop feedback
- [ ] LangChain / LangGraph: any "guardrails" or "policy tool" patterns
- [ ] Guardrails AI: https://github.com/guardrails-ai/guardrails — closest existing analogue?
- [ ] LinkedIn / X / blog posts referencing "LSAP" or "LASP" in an agent+LSP context

---

## Findings

*(Fill in when completing.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:

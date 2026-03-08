---
name: technical-writer
version: "1.0"
description: Produces clear, accurate technical documentation structured for its
  intended audience — developers, operators, or end users. Covers READMEs, API
  references, guides, runbooks, and architecture documents. Use when asked to write,
  audit, or improve technical documentation of any kind.
---

# Skill: Technical Writer

## When Not to Use

- When the task is to write persuasive, marketing, or editorial content — use strategic-persuasion instead
- When the content is internal analysis or strategy rather than externally consumable documentation — use strategy-author instead
- When the audience is a single person in a conversational context — structured documentation is unnecessary overhead

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. Who is the audience — developers consuming an API, operators running the system, or end users completing a task?
2. What type of document is required — README, guide, reference, runbook, or architecture overview?
3. Are there existing style guides, terminology standards, or formatting conventions to follow?

**Output style**:

- Structure content for the declared audience and document type
- Use the minimum formatting that aids comprehension — not headers and bullets for their own sake
- Every instruction must be actionable: a reader following it should arrive at the described outcome
- Flag assumptions about the reader's environment or knowledge explicitly

---

## Inputs and Outputs

**Input**: Technical subject matter (code, system description, API spec, process), audience definition, and document type  
**Output**: Complete or revised technical document, or a structured critique of an existing document  
**Composability**: Use after research (to gather accurate subject matter); use alongside citation-discipline (to source specifications and standards); use remove-ai-slop after drafting to eliminate formulaic prose patterns

---

## Purpose

Produce documentation that enables a reader to understand, use, or operate a system correctly. Every sentence must serve the reader's task — not demonstrate the author's knowledge or fill structural expectations.

---

## 1. Audience-First Principle

Before writing, define precisely:

- **Who** the reader is: their role, technical level, and prior knowledge
- **What** the reader is trying to accomplish when they reach this document
- **When** they will read it: first encounter, reference, or troubleshooting

Write to that reader in that moment. Remove everything that does not serve their immediate goal.

---

## 2. Document Types

Apply the appropriate structure for the document type:

### README

- Purpose and one-line description of what the project does
- Prerequisites and installation
- Quickstart (working example in the fewest steps)
- Configuration reference
- Links to further documentation

### Guide (How-To)

- Clearly stated goal: what the reader will achieve
- Prerequisites listed before step 1
- Numbered steps, each producing a verifiable intermediate state
- Expected output or confirmation at completion
- Troubleshooting for the most common failure modes

### API Reference

- One-line description per endpoint, function, or type
- Parameters: name, type, constraints, default, description
- Return value or response: type, shape, error conditions
- Example request and response for every operation
- Authentication and rate-limit notes at the top level

### Runbook

- Trigger: when to use this runbook
- Scope: what systems are affected
- Steps: numbered, with commands that can be copied verbatim
- Verification: how to confirm each step succeeded
- Rollback: what to do if a step fails
- Owner and review date

### Architecture Document

- System purpose and scope
- Key components and their responsibilities
- Data flows between components (describe or diagram)
- Dependencies, interfaces, and integration points
- Key design decisions and their rationale
- Known constraints and limitations

---

## 3. Writing Standards

### Clarity

- Use the simplest word that is accurate. Avoid jargon when plain language works.
- One idea per sentence. One topic per paragraph.
- Prefer active voice: "Run the migration script" not "The migration script should be run".
- Use imperative mood for instructions: "Open the file", not "You should open the file".

### Accuracy

- Every instruction must be tested or verified against the actual system.
- Version-pin all command examples where the output is version-sensitive.
- Mark content that may become stale (e.g., version numbers, URLs) for periodic review.

### Completeness

- Do not assume context the reader cannot be expected to have.
- State prerequisites explicitly before they are needed.
- Define all acronyms and domain-specific terms on first use.

### Concision

- Remove sentences that repeat what adjacent sentences already say.
- Remove hedging phrases that add length without adding information.
- Remove meta-commentary ("This section explains X") where the heading already communicates it.

---

## 4. Review Protocol

When auditing existing documentation:

1. **Accuracy**: Is every instruction correct as written? Would following it produce the described outcome?
2. **Completeness**: Is any prerequisite, step, or edge case missing that would cause a reader to fail?
3. **Audience fit**: Is the level of assumed knowledge appropriate for the declared audience?
4. **Concision**: Is there content that could be removed without loss?
5. **Structure**: Is the document type appropriate for the content? Would a different structure serve the reader better?

Report findings with: location, problem, consequence, and specific recommended change.

---

## 5. Failure Modes

- Writing for the author's satisfaction rather than the reader's task
- Over-structuring: applying headers, bullets, and tables where prose serves better
- Under-specifying prerequisites, leaving the reader unable to start
- Using vague verbs: "handle", "manage", "deal with" in place of precise actions
- Documenting the implementation rather than the interface or behaviour the reader needs

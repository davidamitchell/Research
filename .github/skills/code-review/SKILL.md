---
name: code-review
version: "1.0"
description: Performs systematic, multi-dimensional code review covering correctness,
  security, performance, maintainability, and style. Produces actionable, prioritised
  findings with evidence-based recommendations. Use when asked to review code, audit
  a pull request, or evaluate implementation quality.
---

# Skill: Code Review

## When Not to Use

- When the task is exploratory prototyping and code quality standards have been explicitly deferred
- When the request is to write or refactor code rather than evaluate existing code — use a separate authoring pass first, then apply this skill
- When a superficial style-only lint pass is sufficient — this skill performs deep multi-dimensional review, not surface formatting

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What is the intended purpose of the code — what should it do, and in what context does it run?
2. Are there specific concerns to prioritise (security, performance, correctness, readability)?
3. What language, framework, and conventions apply?

**Output style**:

- Group findings by dimension (correctness, security, performance, maintainability, style)
- Assign each finding a severity: `Critical`, `High`, `Medium`, `Low`, or `Info`
- For every finding: state the problem, identify the exact location, explain the consequence, and provide a concrete recommended fix
- Do not pad with praise; observations that do not identify a problem or produce an actionable recommendation are not findings
- End with a summary: total findings by severity, and an overall assessment

---

## Inputs and Outputs

**Input**: Source code (any language), with optional context: purpose, language/framework, prior review notes, specific concerns  
**Output**: Structured findings grouped by dimension, each with severity, location, problem statement, consequence, and recommendation; overall summary  
**Composability**: Use after research (to understand the problem domain); use before strategy-author (to translate findings into architectural decisions); combine with citation-discipline when recommending standards or citing specifications

---

## Purpose

Produce rigorous, evidence-based code review that identifies real problems and produces actionable recommendations. Every finding must be grounded in observable code behaviour, known failure modes, or established standards — not preference or convention for its own sake.

---

## 1. Review Dimensions

Apply all dimensions in sequence. Do not skip a dimension because no issues are expected.

### 1.1 Correctness

- Does the code do what it is intended to do?
- Are there logic errors, off-by-one errors, or incorrect conditions?
- Are edge cases and boundary conditions handled?
- Is error handling present, appropriate, and complete?
- Are there race conditions or concurrency hazards if the code runs in a concurrent context?
- Are external assumptions (API contracts, data formats, invariants) explicitly validated?

### 1.2 Security

- Are all external inputs validated, sanitised, and bounds-checked before use?
- Is authentication and authorisation enforced at every access point?
- Are secrets, credentials, and sensitive values never hardcoded or logged?
- Are cryptographic operations using approved, current algorithms and libraries?
- Are there injection risks (SQL, command, template, path traversal)?
- Is error output safe — does it avoid leaking internal state, stack traces, or sensitive data?
- Are dependencies at known-safe versions?

### 1.3 Performance

- Are there O(n²) or worse algorithms where a better complexity is practical?
- Are there unnecessary database queries, network calls, or I/O operations inside loops?
- Are expensive resources (connections, file handles, threads) properly pooled and released?
- Are there memory leaks or unbounded growth patterns?
- Is caching used where appropriate, and invalidated correctly?

### 1.4 Maintainability

- Is the code's intent clear without requiring deep context to understand?
- Are functions and methods focused on a single responsibility?
- Is duplication present where abstraction would reduce risk?
- Are names — variables, functions, classes, files — accurate and unambiguous?
- Are dependencies and coupling minimised?
- Is the code testable as written, or do structural changes improve testability?

### 1.5 Style and Conventions

- Does the code follow the established conventions for this language and codebase?
- Are comments present where the logic is non-obvious, and absent where the code is self-evident?
- Is formatting consistent with the project's style?

---

## 2. Severity Classification

Assign each finding one of the following:

| Severity | Criteria |
|---|---|
| `Critical` | Defect that will cause data loss, security breach, or system failure under expected conditions |
| `High` | Defect likely to cause incorrect behaviour, vulnerability, or significant degradation in realistic scenarios |
| `Medium` | Defect that may cause problems under specific conditions; technical debt with meaningful risk |
| `Low` | Minor issue with limited practical impact; style or convention violation with a clear rationale for change |
| `Info` | Observation or suggestion that does not represent a defect; context for the author |

---

## 3. Finding Format

Each finding must contain:

```
**[SEVERITY] Dimension — Short title**

Location: <file>, <function/method/line>
Problem: What is wrong and why it is wrong.
Consequence: What fails or degrades if this is not addressed.
Recommendation: Specific change to make, including example code where helpful.
```

---

## 4. Consistency Check

Before finalising, verify:

- Every finding has a concrete location — no vague "the code does X" statements
- Every recommendation is actionable — no "consider improving" without specifying how
- Severity levels are consistent — a `Critical` finding in one section is not treated as `Low` elsewhere for the same class of issue
- No dimension has been omitted
- Summary counts match the body

---

## 5. Failure Modes

- Flagging style preferences as correctness issues
- Assigning `Critical` severity to findings without demonstrating a concrete failure path
- Producing findings without a recommended fix
- Missing security issues because the focus was on style
- Generating praise sections that dilute the signal of the findings

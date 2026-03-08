---
name: swe
version: "1.0"
description: Applies SOLID principles, Fielding's REST architectural constraints,
  Gang of Four design patterns, and Enterprise Integration Patterns to produce
  well-designed, maintainable software. Use when designing systems, implementing
  features, making architectural decisions, or reviewing a design for principle
  adherence.
theoretical_foundations:
  - "Robert C. Martin – SOLID principles"
  - "Roy T. Fielding – Architectural Styles and the Design of Network-based Software Architectures (dissertation, 2000)"
  - "Gamma, Helm, Johnson, Vlissides – Design Patterns: Elements of Reusable Object-Oriented Software"
  - "Gregor Hohpe, Bobby Woolf – Enterprise Integration Patterns"
---

# Skill: Software Engineering

## When Not to Use

- When the task is to review existing code rather than design or write new code — use code-review instead
- When the task is to produce documentation for an audience — use technical-writer instead
- When the problem domain is not yet understood well enough to begin design — use research first to gather evidence, then return to this skill
- When the only task is writing prose strategy without a software implementation context — use strategy-author instead

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What problem is this software solving, and for whom — what are the quality constraints (correctness, scalability, maintainability, latency)?
2. What are the integration points — which external systems, protocols, services, or data formats does this touch?
3. Which design constraints or technology choices are already fixed?

**Output style**:

- Name the principle, pattern, or constraint being applied and state why it applies to this specific problem
- Surface trade-offs rather than concealing them — every design choice costs something
- Prefer verifiable designs: define interfaces, contracts, and invariants that can be independently tested

---

## Inputs and Outputs

**Input**: Problem description, system context, requirements, existing design, or implementation for review  
**Output**: Designs, implementations, or architectural decisions grounded in established principles; explicit trade-offs and rationale  
**Composability**: Use after research (to understand the problem domain before designing); use before code-review (to evaluate the implementation against the design intent); use technical-writer to document the resulting architecture; use strategy-author to translate architectural decisions into strategic options; use backlog-manager to convert design decisions into actionable work items

---

## Purpose

Produce software designs and implementations that are maintainable, correct, and built on proven foundations. Every design decision must be traceable to a principle, pattern, or constraint — not to convention alone or familiarity with a single approach.

---

## 1. SOLID Principles

Apply all five principles to every design. Surface violations explicitly rather than silently working around them.

### 1.1 Single Responsibility Principle (SRP)

Each module, class, or function has exactly one reason to change. "Reason to change" means one actor or stakeholder whose requirements drive change in that component. If a component responds to multiple distinct axes of change, split it. Identify the axis of change precisely — "does too much" is not a reason; name the second responsibility and the actor driving it.

### 1.2 Open/Closed Principle (OCP)

Software entities are open for extension and closed for modification. Add behaviour by adding new code, not by changing existing code. Achieve this through abstractions — interfaces, abstract types, or extension points — that anticipate the most likely forms of variation without encoding specific variants. Identify which dimension of variation the abstraction protects against.

### 1.3 Liskov Substitution Principle (LSP)

Subtypes are substitutable for their base types without altering the correctness of the program. A subtype must honour the preconditions, postconditions, and invariants of its base type: strengthen postconditions, weaken preconditions — never the reverse. Detect violations by inspecting for `instanceof` checks, type-specific branching, or overrides that throw where the base type does not.

### 1.4 Interface Segregation Principle (ISP)

Clients depend only on the methods they use. Wide interfaces that force implementors to provide irrelevant methods couple unrelated concerns. Split interfaces along natural client boundaries, not along implementation convenience. An interface polluted with methods no client uses in full is an indicator of a missing decomposition.

### 1.5 Dependency Inversion Principle (DIP)

High-level modules define and depend on abstractions; low-level modules implement those abstractions. The dependency arrows in source code point from volatile concrete components toward stable abstractions, not the reverse. Inject dependencies; do not instantiate collaborators inside business logic. The direction of source-code dependency must oppose the direction of runtime control flow wherever they diverge.

---

## 2. REST: Fielding's Architectural Constraints

REST is not a data format, a URL convention, or synonymous with JSON over HTTP. It is an architectural style — a coordinated set of constraints defined by Roy Fielding in his 2000 dissertation — that, when applied together, produce specific and predictable architectural properties. Evaluate every claimed "REST" design against all six constraints. Name any violated constraint explicitly and state what property is lost.

### 2.1 The Six Constraints

**Client-Server**  
Separate user interface concerns from data storage concerns. The client does not know the server's storage structure; the server does not know the client's rendering logic. This allows each to evolve independently on its own schedule.

**Stateless**  
Each request from client to server must contain all information necessary to understand and fulfil the request. No session state is stored on the server between requests. This produces visibility (each request is fully self-describing), reliability (any server instance can handle any request), and scalability (no affinity between clients and server instances). The cost is increased per-request data volume.

**Cache**  
Responses must declare themselves as cacheable or non-cacheable. Cacheable responses allow client or intermediary caches to reuse response data, improving efficiency and scalability. The cost is the risk of stale data if cache-control signals are incorrect or absent.

**Uniform Interface**  
The central constraint distinguishing REST from other distributed architectures. It has four sub-constraints:

- *Identification of resources*: Resources are identified in requests (e.g., by URI). A resource's identifier is distinct from its representation.
- *Manipulation of resources through representations*: The client holds a representation of a resource with sufficient information to create, modify, or delete it, given the appropriate permissions.
- *Self-descriptive messages*: Each message includes enough information to describe how to process it. Media types describe the format; HTTP methods carry semantic meaning independently of the URI.
- *Hypermedia as the engine of application state (HATEOAS)*: The server drives application state transitions by embedding links and forms in responses. Clients need no out-of-band knowledge of valid URI structure or state transitions — they discover them at runtime from the server's responses. This is the most frequently absent REST constraint and the one most critical to enabling independent client and server evolution. Without it, clients are coupled to URI conventions and must be updated when server structure changes.

**Layered System**  
The client cannot distinguish whether it is communicating with the end server or an intermediary (load balancer, cache, gateway, security proxy). Layers provide composability: each adds or removes behaviour without requiring client or server changes.

**Code on Demand (optional)**  
Servers may extend client functionality by transferring executable code (scripts, applets). This is the only optional constraint.

### 2.2 Architectural Properties REST Produces

Each constraint buys a specific property. Map design decisions to this table:

| Constraint | Property Gained |
|---|---|
| Client-Server | Independent evolvability of client and server |
| Stateless | Visibility, reliability, horizontal scalability |
| Cache | Efficiency, reduced server load, scalability |
| Uniform Interface | Decoupled evolution, generality, intermediary support |
| Layered System | Composable infrastructure, security isolation |
| Code on Demand | Client extensibility without client deployment |

If a constraint is deliberately violated, name the lost property and justify the trade-off.

### 2.3 Applying REST Correctly

- Identify resources (things, not actions). Resources are nouns; HTTP methods supply the verbs.
- Use HTTP methods according to their defined semantics: GET is safe and idempotent; PUT and DELETE are idempotent; POST is neither safe nor idempotent.
- Implement HATEOAS where independent client evolution matters. Document explicitly when HATEOAS is absent and state the coupling this creates.
- Use media types to describe representations. Do not rely on URI patterns to communicate semantics.
- Distinguish between an HTTP API and a RESTful API. An HTTP API uses HTTP as a transport; a RESTful API satisfies all applicable Fielding constraints. Both are valid choices for different contexts — but conflating them hides the trade-offs.

---

## 3. Gang of Four Design Patterns

Apply patterns from *Design Patterns: Elements of Reusable Object-Oriented Software* when they resolve a recurring design problem. Name the pattern, state its intent, and explain why it fits this specific problem. Do not apply patterns for recognition value; the justification must be the problem, not the pattern.

### 3.1 Creational Patterns

| Pattern | Intent | Use When |
|---|---|---|
| Abstract Factory | Create families of related objects without specifying concrete classes | Multiple product families must be consistent; clients must be independent of how products are created |
| Builder | Separate the construction of a complex object from its representation | Construction requires many steps or configurations; the same process must produce different representations |
| Factory Method | Define a creation interface; let subclasses decide which class to instantiate | A class cannot anticipate the class of objects it must create; subclasses should control object creation |
| Prototype | Create new objects by copying a prototype | Classes to instantiate are specified at runtime; avoiding a class hierarchy of factories is preferable |
| Singleton | Ensure a class has one instance with a global access point | Exactly one instance is required — use sparingly; prefer dependency injection to avoid hidden coupling |

### 3.2 Structural Patterns

| Pattern | Intent | Use When |
|---|---|---|
| Adapter | Convert one interface to another that clients expect | Reusing a class whose interface does not match client requirements |
| Bridge | Decouple an abstraction from its implementation so both can vary independently | Both abstraction and implementation should be extensible without coupling to each other |
| Composite | Compose objects into tree structures to represent part-whole hierarchies | Clients must treat individual objects and compositions uniformly |
| Decorator | Attach additional responsibilities to an object dynamically | Adding behaviour without subclassing; responsibilities may be added or removed at runtime |
| Facade | Provide a simplified interface to a complex subsystem | Clients need access to a subsystem through a narrower, higher-level interface |
| Flyweight | Use sharing to support large numbers of fine-grained objects efficiently | Many objects share most of their state; the shared state can be made extrinsic |
| Proxy | Provide a surrogate that controls access to another object | Lazy initialisation, access control, logging, remote access, or caching of an expensive object |

### 3.3 Behavioural Patterns

| Pattern | Intent | Use When |
|---|---|---|
| Chain of Responsibility | Pass a request along a chain of handlers; each decides to process or forward it | More than one object may handle a request; the handler should not be determined statically |
| Command | Encapsulate a request as an object | Parameterising operations; supporting undo/redo; queuing or logging requests |
| Interpreter | Define a grammar for a language and interpret sentences of that language | Implementing a language or expression evaluator; grammar is simple and performance is not critical |
| Iterator | Access elements of an aggregate sequentially without exposing its representation | Uniform traversal of different aggregate types |
| Mediator | Define an object that encapsulates how a set of objects interact | Many-to-many object communication creates tight coupling; centralising interaction reduces dependencies |
| Memento | Capture and externalise an object's state so it can be restored later | Undo/redo; state snapshots; checkpointing |
| Observer | Define a one-to-many dependency so that state changes propagate automatically | Consistent state across dependent objects without tight coupling |
| State | Allow an object to alter its behaviour when its internal state changes | Behaviour depends heavily on state; state-specific code would otherwise produce large conditionals |
| Strategy | Define a family of algorithms, encapsulate each, and make them interchangeable | Multiple variants of an algorithm exist and should be selectable at runtime |
| Template Method | Define an algorithm skeleton in a base class; defer specific steps to subclasses | Invariant parts of an algorithm belong in one place; variant parts belong in subclasses |
| Visitor | Represent an operation on elements of an object structure without changing element classes | Many distinct operations must be performed on a structure without polluting element class definitions |

### 3.4 Pattern Application Rules

- Name the pattern and state the intent at the point of application — in code comments, design documents, or review feedback.
- Prefer composition over inheritance. Inheritance locks in structure at compile time; composition allows runtime substitution.
- Do not force a pattern onto a problem that does not match its defined intent. A pattern applied to the wrong problem adds complexity without benefit.
- When two patterns address the same problem, choose the one with fewer structural constraints given the current context.

---

## 4. Enterprise Integration Patterns

Apply patterns from *Enterprise Integration Patterns* (Hohpe and Woolf) when designing systems that connect multiple applications or services. The integration style chosen shapes all subsequent decisions about decoupling, reliability, and evolvability.

### 4.1 Integration Styles

Choose the integration style before selecting patterns:

| Style | Mechanism | Trade-offs |
|---|---|---|
| File Transfer | Applications exchange data files | Simple and loosely coupled; high latency; no real-time coordination; reconciliation required |
| Shared Database | Applications share a single database schema | Low-latency consistency; tightly coupled; schema changes affect all consumers simultaneously |
| Remote Procedure Invocation | One application calls another directly | Real-time; synchronous; tight temporal coupling; fragile under partial failure |
| Messaging | Applications exchange messages through a message channel | Decoupled; asynchronous; adds infrastructure complexity; natural fault isolation |

### 4.2 Core Pattern Categories

**Message Construction**

- *Message*: The unit of data exchanged between applications. Contains a header (routing metadata) and a body (payload).
- *Command Message*: Instructs a receiver to perform a specific action. Appropriate when the sender knows what the receiver must do.
- *Event Message*: Notifies receivers that something has happened. Receivers decide what, if anything, to do. Prefer Event Message over Command Message to reduce coupling.
- *Request-Reply*: A sender sends a message and expects a reply on a designated reply channel. The Correlation Identifier links replies to their originating requests. The Return Address specifies where the reply should be sent.

**Message Channels**

- *Point-to-Point Channel*: Ensures exactly one receiver processes each message.
- *Publish-Subscribe Channel*: Delivers each message to all subscribers.
- *Dead Letter Channel*: Receives messages that cannot be delivered or processed. Every integration that can fail must route unprocessable messages somewhere; leaving them unhandled causes silent data loss.
- *Guaranteed Delivery*: Ensures message delivery survives messaging infrastructure failures through persistence.
- *Datatype Channel*: Carries messages of a single type; receivers can deserialise without type negotiation.

**Message Routing**

- *Content-Based Router*: Routes messages to different channels based on message content.
- *Message Filter*: Removes messages that do not satisfy a condition; downstream receivers see only relevant messages.
- *Splitter*: Converts one message containing multiple items into individual messages, one per item.
- *Aggregator*: Collects related messages and combines them into a single message. Requires a correlation strategy and a completeness condition.
- *Resequencer*: Reorders out-of-sequence messages before forwarding.
- *Process Manager*: Maintains state to route a message through multiple processing steps where the next step depends on prior results.
- *Message Broker*: Decouples senders from receivers using a central routing hub.

**Message Transformation**

- *Message Translator*: Converts a message from one data format to another.
- *Content Enricher*: Adds data to a message from an external source before forwarding.
- *Content Filter*: Removes fields from a message that downstream components do not need.
- *Normalizer*: Routes messages of different formats through translators to produce a single canonical form.
- *Canonical Data Model*: Defines a data format independent of any single application. All producers and consumers translate to and from the canonical model. Use when more than two systems exchange the same type of data; it eliminates the n² translator problem.

**Messaging Endpoints**

- *Messaging Gateway*: Encapsulates messaging infrastructure from the application; the application uses the gateway with domain objects and is unaware of message construction or channel details.
- *Transactional Client*: Ensures that message send and local state change are atomic — either both succeed or neither does.
- *Competing Consumers*: Multiple consumers on a single channel; each message goes to exactly one consumer. Enables horizontal scaling of processing.
- *Idempotent Receiver*: Handles duplicate message delivery without producing duplicate effects. Required in every at-least-once delivery system, which is the default for all durable messaging infrastructure.
- *Service Activator*: Connects a service to a message channel so it can be invoked by messages as well as by direct calls.

### 4.3 Pattern Selection Rules

- Define the message exchange requirement first: fire-and-forget, request-reply, or event notification. Pattern selection follows from this.
- Prefer Event Message over Command Message when the sender should not dictate receiver behaviour.
- Use Canonical Data Model when more than two systems exchange the same type of data.
- Use Idempotent Receiver whenever duplicate message delivery is possible — assume it is always possible in messaging systems.
- Always route undeliverable or unprocessable messages to a Dead Letter Channel. Silent discard is never acceptable.
- Use Guaranteed Delivery when message loss has business consequences.

---

## 5. Iterative Learning and Improvement

Every non-trivial problem is incompletely understood at the start. Design for revision.

### 5.1 Iterative Problem Understanding

- State explicitly what is known, what is assumed, and what is unknown at the start of each design session.
- Identify load-bearing assumptions: if an assumption is wrong, the design changes significantly. These require testing before committing to an architectural direction.
- After each iteration, record what changed and why. This produces a decision log that explains the design, not just a solution that implements it.

### 5.2 Feedback Loops

- Construct the shortest possible feedback loop for each load-bearing assumption. Prototypes, spikes, and staged rollouts each serve different feedback needs; choose the mechanism proportional to the cost of being wrong.
- Do not proceed past a load-bearing assumption without evidence. Either test it or explicitly mark the decision as provisional and document the contingency.
- When evidence contradicts the design, revise the design. Sunk cost is not a design argument.

### 5.3 Improvement Protocol

- After each significant implementation, evaluate: what did the design get wrong, and why?
- Prefer small, reversible changes over large irreversible ones. Large irreversible changes require proportionally stronger evidence.
- Define "done" in terms of observed outcomes, not completed tasks. A feature is done when its intended effect is confirmed in production, not when code is merged.

---

## 6. Planning and Design

Invest time in design before implementation. Undiscovered design problems are the most expensive problems because they are discovered after code is written.

### 6.1 Pre-implementation Checklist

Before writing implementation code, confirm:

- [ ] Problem statement is precise: what must the software do, for whom, under what constraints?
- [ ] Integration points are identified: which external systems, protocols, and data formats?
- [ ] Failure modes are enumerated: what happens when each dependency is unavailable, slow, or returns unexpected data?
- [ ] Key design decisions are identified with their reversibility: which decisions can be changed cheaply later, and which cannot?
- [ ] Non-goals are explicit: what will this software deliberately not do?

### 6.2 Design Artefacts

Produce design artefacts proportional to the scope and irreversibility of the decisions:

- **Interface definitions** before implementation — define the contract before coding to it; interfaces express intent that implementations must honour
- **Sequence diagrams** for non-trivial interactions between components — state transitions and timing constraints are easiest to reason about before code exists
- **Data models** when structure is non-trivial or shared across multiple components
- **Decision log** for each significant architectural choice: options considered, criteria applied, and rationale; include what was explicitly rejected and why

### 6.3 Design Review

Before proceeding to implementation, verify:

- Does each component have a single, clearly named responsibility?
- Are dependencies directed toward abstractions, not concretions?
- Is every integration point covered by an explicit interface definition?
- Does the design address the enumerated failure modes?
- Is the design testable as specified — can the contracts and invariants be confirmed by tests?

---

## 7. Failure Modes

- Applying SOLID principles as naming conventions rather than as design constraints that shape dependency structure
- Calling an HTTP JSON API "REST" without implementing the Uniform Interface constraints — particularly the absence of HATEOAS, which couples clients to server URI conventions
- Applying design patterns for recognition or symmetry rather than because they resolve a specific problem
- Allowing ad-hoc point-to-point integrations to accumulate instead of selecting an integration style and applying patterns consistently
- Treating the first design as final and resisting revision when evidence contradicts its assumptions
- Proceeding to implementation before design decisions are explicit and recorded
- Conflating "implementation complete" with "problem solved" — the measure is observed outcomes, not merged code

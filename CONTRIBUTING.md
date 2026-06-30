# Contributing to VerityPay

**Onboarding handbook for the VerityPay protocol ecosystem.**

VerityPay is not a product repository with a contribution guide attached. It is an open protocol effort: specifications lead, implementations follow, and every contributor helps make payment claims **verifiable, interoperable, and durable across independent software**.

This document explains how to participate with clarity—whether you write code, specifications, research, diagrams, or prose.

---

## Welcome

Contributing to VerityPay means helping build **shared infrastructure** that outlives any single team, vendor, or release cycle.

You are not merely opening pull requests. You are joining a protocol ecosystem where:

- **Truth is specified**, not implied by whoever shipped first
- **Multiple implementations** can interoperate because they share accepted rules
- **Change is governed**, visible, and reviewable before it becomes permanent
- **Clarity** matters more than cleverness

We welcome engineers, researchers, designers, technical writers, security researchers, auditors, and integrators. You do not need permission to read, learn, or propose improvements. You do need alignment with the protocol's direction before changing normative behavior.

If you are unsure where to begin, read [Before you start](#before-you-start), then find your [contributor level](#contributor-levels). Most newcomers start at Level 0 or Level 1.

---

## Before you start

Do not propose protocol changes before you understand what VerityPay is trying to become. The reading order below is intentional. Skipping it produces churn—for you and for reviewers.

### Institutional foundation

These documents define **who we are** and **how we think**. They constrain everything downstream.

| Order | Document | Role |
|-------|----------|------|
| 1 | **North Star** | The world we are building toward—independent of any single product |
| 2 | **Constitution** | Durable law: specification primacy, plural implementation, governed change |
| 3 | **Engineering DNA** | How engineers reason before they edit |
| 4 | **Design Philosophy** | How systems are designed; architectural gravity and design smells |

Organizational Canon volumes are maintained by VerityPay and shared with contributors as they are published. They are not substitutes for the public specification—they **constrain** it. When Canon and public spec appear to conflict, **stop and raise the issue**; do not silently pick a side.

### Public specification layer

These documents live in [`veritypay-spec`](.) and define **what the protocol is**.

| Order | Document | Location |
|-------|----------|----------|
| 5 | **Vision** | [`docs/00-overview/VISION.md`](docs/00-overview/VISION.md) — VerityPay's role in creating the North Star world |
| 6 | **Protocol model** | [`docs/01-architecture/DOMAIN_MODEL.md`](docs/01-architecture/DOMAIN_MODEL.md) Part I — capabilities, truth model, trust model, boundaries |
| 7 | **Architecture** | [`docs/01-architecture/`](docs/01-architecture/) — read in order: Domain → Identity → Behavior → Data → State |

Use [`docs/README.md`](docs/README.md) for the full documentation pyramid and maturity levels (L0–L4).

### This handbook

| Order | Document | Role |
|-------|----------|------|
| 8 | **Contributing** | You are here — how to participate responsibly |

### Quick orientation by role

| You are… | Start with | Then |
|----------|------------|------|
| A curious reader | Vision → Domain Model Part I | Architecture README |
| An implementer | Architecture stack → accepted RFCs | [`docs/03-development/`](docs/03-development/) |
| A spec author | Governance + RFC template | Relevant architecture model |
| A security researcher | Architecture invariants → disclosure policy | [`docs/05-governance/`](docs/05-governance/) |
| A technical writer | Glossary + architecture | Issue labeled `documentation` |

---

## Repository guide

VerityPay separates **specification** from **implementation**. Know which repository you are in before you open a pull request.

### `veritypay-spec`

**Role:** Canonical source of truth for protocol behavior.

**Belongs here:**

- Constitutional documents (Vision, Principles, Manifesto, Glossary)
- Architecture models (domain, identity, behavior, data, state)
- Accepted and draft RFCs
- Conformance requirements and test vectors (when specified)
- Governance, research (pre-normative), product-facing protocol views
- Diagrams supporting specification material
- Templates for specs, RFCs, and decision records

**Does not belong here:**

- Application source code
- Database migrations
- Deployment manifests
- Vendor-specific integration playbooks dressed as normative text

**Key paths:**

| Path | Purpose |
|------|---------|
| [`docs/00-overview/`](docs/00-overview/) | Constitutional layer |
| [`docs/01-architecture/`](docs/01-architecture/) | Protocol structure and models |
| [`docs/02-product/`](docs/02-product/) | Participant-facing view of specified behavior |
| [`docs/03-development/`](docs/03-development/) | Implementer and conformance guidance |
| [`docs/04-research/`](docs/04-research/) | Exploratory, non-binding work |
| [`docs/05-governance/`](docs/05-governance/) | How change happens |
| [`rfcs/`](rfcs/) | Normative change proposals |
| [`diagrams/`](diagrams/) | Specification visuals |

When specification and implementation disagree, **accepted specification wins**.

### `veritypay-core`

**Role:** Reference implementation and core library development.

**Belongs here:**

- Protocol implementation code
- Unit and integration tests against accepted behavior
- Benchmarks and developer tooling for the core library
- CI configuration for the implementation

**Does not belong here:**

- Normative protocol definitions (those start in `veritypay-spec`)
- Undocumented behavior presented as de facto standard

Implementations must declare which specification version and accepted RFC set they target.

### Ecosystem repositories (present and future)

As the ecosystem matures, additional repositories may include:

| Repository type | Role |
|-----------------|------|
| **Examples** | Minimal, educational demonstrations of protocol usage |
| **SDKs** | Language-specific client libraries conforming to specification |
| **Reference interpreter** | Executable semantics for conformance and education |
| **Conformance harness** | Shared tests independent implementations must pass |
| **Tooling** | Validators, linters, and spec authoring utilities |

Each repository README states its relationship to `veritypay-spec`. If behavior is not accepted in specification, it is **not part of the protocol**—regardless of how popular an SDK becomes.

---

## Contributor levels

Contribution depth is **earned through demonstrated judgment**, not declared in a profile bio. Levels describe where your work typically lands and what reviewers expect.

```
Level 0 — Observer
    ↓
Level 1 — Documentation
    ↓
Level 2 — Examples
    ↓
Level 3 — SDK
    ↓
Level 4 — Reference Interpreter
    ↓
Level 5 — Core Specification
```

### Level 0 — Observer

**You:** Read, learn, comment, file thoughtful issues.

**Typical work:** Reading architecture models; asking questions; reporting ambiguities; reviewing drafts informally.

**Not expected:** Pull requests changing normative text or core code.

**Progress when:** You understand the documentation pyramid and can point to which model governs a given concept.

---

### Level 1 — Documentation

**You:** Improve clarity without changing protocol meaning.

**Typical work:** Typos, cross-links, diagrams, glossary entries, examples in prose, README improvements, editorial consistency across models.

**Guardrail:** Documentation PRs must not smuggle in new normative behavior. If your edit changes what implementations must do, it is not Level 1—it requires an RFC.

**Progress when:** Several merged documentation PRs with zero spec-conflict incidents; reviewers trust your editorial judgment.

---

### Level 2 — Examples

**You:** Make the protocol legible through working demonstrations.

**Typical work:** Example claims, verification flows, sequence walkthroughs, educational code in example repositories.

**Guardrail:** Examples illustrate accepted specification. They do not define it.

**Progress when:** Examples are cited in issues and onboarding; you demonstrate conformance awareness in reviews.

---

### Level 3 — SDK

**You:** Build libraries that help integrators speak the protocol correctly.

**Typical work:** Client APIs, serialization helpers, validation utilities, ergonomic wrappers—always tracing to accepted RFCs.

**Guardrail:** SDK convenience must not become undeclared protocol behavior. When the SDK disagrees with specification, the SDK is wrong until the spec changes through governance.

**Progress when:** Sustained maintenance, test coverage against conformance vectors, responsive issue triage.

---

### Level 4 — Reference Interpreter

**You:** Help make protocol semantics executable and testable.

**Typical work:** Reference evaluation of claims, verification rule execution, state transitions aligned with [`STATE_MODEL.md`](docs/01-architecture/STATE_MODEL.md), conformance harness contributions.

**Guardrail:** The interpreter demonstrates specification—it does not replace RFCs as the normative source.

**Progress when:** Interpreter behavior is trusted in conformance discussions; you co-author RFCs with technical depth.

---

### Level 5 — Core Specification

**You:** Author or materially shape normative protocol text.

**Typical work:** Architecture model refinements (through governance), RFC authorship, conformance model design, cross-implementation interoperability decisions.

**Requirements:** Deep fluency in all architecture models; track record at lower levels; explicit reviewer sponsorship for substantial changes.

**Guardrail:** Specification changes affect every independent implementer. Move slowly, write precisely, record reasoning.

---

Levels are not badges. They are **scope guidance**. A Level 1 contributor who proposes a brilliant RFC may jump levels with maintainer invitation—but **protocol architecture is never a good first contribution**.

---

## Engineering workflow

All substantive work follows the same discipline:

```
Research
    ↓
Issue
    ↓
ADR / RFC (if required)
    ↓
Implementation
    ↓
Review
    ↓
Merge
```

| Stage | Purpose |
|-------|---------|
| **Research** | Understand problem, prior art, and spec constraints. Use [`docs/04-research/`](docs/04-research/) for pre-normative exploration. |
| **Issue** | Describe motivation, scope, and spec touchpoints before large effort. |
| **ADR / RFC** | Record architectural decisions (ADR) or propose normative change (RFC) when behavior or governance shifts. |
| **Implementation** | Code, spec text, tests, or docs—aligned to accepted material. |
| **Review** | Technical correctness, spec alignment, clarity, compatibility. |
| **Merge** | Only when requirements below are satisfied. |

**Research without implementation** is valuable. **Implementation without specification alignment** is not.

Small fixes may compress the path (issue + PR). Protocol behavior never skips RFC.

---

## Pull request requirements

Every pull request must help reviewers answer six questions. Include them in the PR description.

### 1. Motivation

Why does this change exist? What problem does it solve? Link to user pain, audit finding, spec ambiguity, or research—not merely "I implemented X."

### 2. Related issue

Which issue does this close or reference? If none exists for non-trivial work, explain why.

### 3. Specification impact

Does this change protocol meaning, architecture models, or only presentation?

| Impact | Required action |
|--------|-----------------|
| None (editorial) | State explicitly: *no normative impact* |
| Clarification | Cite affected documents; confirm no behavior change |
| Architectural | ADR or architecture PR with maintainer review |
| Normative | Accepted or in-flight RFC; do not merge behavior ahead of acceptance |

### 4. RFC impact

| Situation | Response |
|-----------|----------|
| No RFC needed | Explain why |
| RFC required but not yet accepted | Mark PR draft; link RFC PR |
| RFC accepted | Cite RFC number and version |
| RFC needs amendment | Open RFC update first |

### 5. Tests

What evidence demonstrates correctness?

- Specification PRs: conformance scenarios, worked examples, or explicit test plan for L3 work
- Implementation PRs: automated tests; conformance vectors where applicable
- Documentation PRs: *N/A* with brief justification, or link to rendered preview

### 6. Documentation updated

List every doc, diagram, README, or changelog touched—or state *none required* with reason.

---

### PR description template

```markdown
## Motivation

## Related issue

## Specification impact

## RFC impact

## Tests

## Documentation updated
```

Reviewers may return PRs that omit these sections on non-trivial changes.

---

## Communication

### Where discussion happens

| Topic | Channel |
|-------|---------|
| Bugs, ambiguities, small improvements | GitHub Issues (appropriate repository) |
| Normative protocol change | RFC pull request in `veritypay-spec` |
| Architectural decision (non-RFC) | ADR in specification or decision record |
| Security vulnerabilities | Follow security disclosure policy in [`docs/05-governance/`](docs/05-governance/) — **do not** open public issues for exploitable findings |
| General orientation | Issues with label `question` |

Prefer **public, written** discussion for anything that affects protocol direction. Decisions that belong in the specification should leave a **durable record**.

### When to create an ADR

Create an **Architecture Decision Record** when:

- Choosing between structural approaches that do not require normative protocol change
- Recording why a design path was taken or rejected
- Documenting governance or process decisions
- Capturing context future maintainers will need

ADRs use [`docs/templates/DECISION_RECORD_TEMPLATE.md`](docs/templates/DECISION_RECORD_TEMPLATE.md). They inform; they do not alone bind implementers unless incorporated by accepted specification.

### When to create an RFC

Create an **RFC** when:

- Behavior of conforming implementations would change
- New claim types, verification rules, or wire formats are introduced
- Breaking changes or deprecations are proposed
- Architecture models need normative promotion
- Constitutional documents require substantive amendment

RFCs use [`rfcs/templates/RFC_TEMPLATE.md`](rfcs/templates/RFC_TEMPLATE.md). Read [`rfcs/README.md`](rfcs/README.md) for lifecycle: draft → review → accepted / rejected / superseded.

**Rule of thumb:** If two independent implementers would need to coordinate because of your change, it probably needs an RFC.

### When to open an issue only

- Typos and broken links
- Questions about reading order
- Requests for examples
- Spec ambiguities without a proposed fix yet
- Tracking good-first contributions

---

## Good first contributions

We actively want help in these areas:

| Area | Examples |
|------|----------|
| **Documentation** | Cross-links, glossary, diagram clarity, worked examples in prose |
| **Examples** | End-to-end claim → verify → outcome walkthroughs |
| **SDK improvements** | Ergonomics, validation, error messages—within accepted spec |
| **Tests** | Conformance scenarios, edge cases, regression coverage |
| **Tooling** | Spec linters, template automation, CI improvements |

### Not good first contributions

| Area | Why |
|------|-----|
| **Protocol architecture rewrites** | Requires Level 5 fluency and governance |
| **New core entities or lifecycles** | Architecture stack is recently completed; changes need RFC |
| **"While I'm here" refactors** | Scope creep delays review |
| **Undocumented behavior in core** | Violates specification primacy |

Look for issues labeled `good first issue`, `documentation`, `help wanted`, or `examples`. If none exist, open an issue proposing work before investing large effort.

---

## Contributor expectations

### Respect the Canon

North Star, Constitution, Engineering DNA, and Design Philosophy are not branding exercises. They are constraints. Public specification must remain aligned with institutional identity. When in doubt, ask maintainers before publishing contradictory material.

### Prefer clarity over cleverness

Specifications are read by humans ten years from now—under stress, in audits, across languages and time zones. Write so they can be understood without insider context.

### Research before implementation

Read existing models and RFCs. Search for prior art in issues and rejected RFCs. The best contribution often begins as a well-formed question.

### Document reasoning

PRs and RFCs should explain **why**, not only **what**. Future contributors inherit your decisions. Undocumented rationale becomes mythology.

### Specification defines; code demonstrates

No implementation owns the protocol. Do not merge behavior in `veritypay-core` and treat documentation as follow-up work.

### Be precise about maturity

Distinguish informative architecture (draft models) from accepted RFCs (normative). Do not imply conformance to drafts.

### Conduct

Participate in good faith. Disagreement is expected; personal attacks are not. See community standards in [`docs/05-governance/`](docs/05-governance/) when published.

---

## Recognition

VerityPay values **long-term stewardship** over short-term contribution counts.

We notice contributors who:

- Improve clarity without expanding scope
- Catch spec conflicts before they reach production
- Maintain examples and tests after merge
- Review others' work with specificity and kindness
- Stay engaged across protocol versions

We do not optimize for leaderboard metrics, hackathon volume, or one-off drive-by patches that leave maintainers with debt.

Sustained, careful work at any [contributor level](#contributor-levels) builds trust—and trust unlocks broader scope, including RFC authorship and maintainer paths.

---

## Summary

| Question | Answer |
|----------|--------|
| Where do I start reading? | [Before you start](#before-you-start) |
| Where does protocol text live? | `veritypay-spec` |
| Where does code live? | `veritypay-core` and ecosystem repos |
| How do I change behavior? | RFC process |
| What makes a good first PR? | Docs, examples, tests, tooling—not architecture |
| What must every PR explain? | Motivation, issue, spec impact, RFC impact, tests, docs |

Welcome to VerityPay. Build something that outlives us.

---

## Related documents

| Document | Location |
|----------|----------|
| Documentation pyramid | [`docs/README.md`](docs/README.md) |
| RFC process | [`rfcs/README.md`](rfcs/README.md) |
| Governance | [`docs/05-governance/GOVERNANCE.md`](docs/05-governance/GOVERNANCE.md) |
| Architecture index | [`docs/01-architecture/README.md`](docs/01-architecture/README.md) |
| License | [`LICENSE`](LICENSE) |

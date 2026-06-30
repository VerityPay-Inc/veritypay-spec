# Architecture

Structural documentation that describes how the VerityPay protocol is organized—its major components, boundaries, data representations, and cross-cutting quality attributes.

---

## Documentation hierarchy

**You are here: Architecture** — the level below the [constitutional layer](../00-overview/) and above detailed specifications.

```
Manifesto → Vision → Principles → Glossary
         ↓
    Architecture   ← this folder
         ↓
    Specifications → Implementation
```

Documents here must align with [MANIFESTO.md](../00-overview/MANIFESTO.md), [VISION.md](../00-overview/VISION.md), [PRINCIPLES.md](../00-overview/PRINCIPLES.md), and terminology in [GLOSSARY.md](../00-overview/GLOSSARY.md). Architecture becomes normative when incorporated by an accepted RFC.

**Adjacent:** [`../02-product/`](../02-product/) (participant view) · **Next level:** [`../../rfcs/`](../../rfcs/) (normative change proposals)

See [`../README.md`](../README.md) for the full pyramid.

---

## Purpose

Architecture documents explain the *shape* of the system without prescribing a particular codebase layout. They give implementers and reviewers a shared map: what entities exist, how they relate, which invariants must hold, and where responsibilities divide.

This folder is where readers learn the protocol's skeleton before reading product-facing workflows or individual RFCs.

**Start here:** [DOMAIN_MODEL.md](DOMAIN_MODEL.md) → [IDENTITY_MODEL.md](IDENTITY_MODEL.md) → [BEHAVIOR_MODEL.md](BEHAVIOR_MODEL.md) → [DATA_MODEL.md](DATA_MODEL.md) → [STATE_MODEL.md](STATE_MODEL.md)

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Protocol designers | Define and refine structural boundaries |
| Security and privacy reviewers | Evaluate models against threat assumptions |
| Implementers | Understand invariants their code must preserve |
| Auditors | Trace requirements to architectural guarantees |
| RFC authors | Ensure proposals align with established structure |

Readers should already understand VerityPay's intent from [`../00-overview/`](../00-overview/). For binding requirements, cross-check against accepted documents in [`../../rfcs/`](../../rfcs/).

---

## Scope

**In scope**

- [DOMAIN_MODEL.md](DOMAIN_MODEL.md) — protocol model (incl. truth & trust) + domain language
- [IDENTITY_MODEL.md](IDENTITY_MODEL.md) — semantic identity, invariants, identity hierarchy (before data model)
- [BEHAVIOR_MODEL.md](BEHAVIOR_MODEL.md) — protocol verbs, interactions, events, behavioral invariants
- [DATA_MODEL.md](DATA_MODEL.md) — canonical entities, identifiers, attributes, representation invariants
- [STATE_MODEL.md](STATE_MODEL.md) — knowledge states, lifecycles, state invariants
- System architecture — subsystems, trust boundaries, and interaction patterns
- Privacy model — what information exists, who may learn it, and under what conditions
- Security model — threat assumptions, trust anchors, and security invariants
- Interoperability model — how independent implementations validate compatibility
- Protocol layering — abstraction levels and dependencies between layers
- Architecture decision records — structural choices documented with [`../templates/DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md)

Diagrams supporting these documents live in [`../../diagrams/`](../../diagrams/) and are referenced from here.

**Out of scope**

- Motivation and vision without structural content → [`../00-overview/`](../00-overview/)
- End-user stories and merchant-facing workflows → [`../02-product/`](../02-product/)
- Conformance test plans and implementer tooling → [`../03-development/`](../03-development/)
- Exploratory designs not yet accepted → [`../04-research/`](../04-research/)
- Voting procedures and RFC lifecycle rules → [`../05-governance/`](../05-governance/)
- Implementation module trees, package names, or deployment topologies
- Executable code, schema files tied to a single language, or database migrations

Architecture content becomes **normative** only when incorporated into or referenced by an **accepted RFC**.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [DOMAIN_MODEL.md](DOMAIN_MODEL.md) | Protocol, domain, truth model, trust model—authoring foundation |
| [IDENTITY_MODEL.md](IDENTITY_MODEL.md) | Semantic identity before data model and state models |
| [BEHAVIOR_MODEL.md](BEHAVIOR_MODEL.md) | Protocol verbs and events before representation and state machines |
| [DATA_MODEL.md](DATA_MODEL.md) | Entity representation before state models and RFC encodings |
| [STATE_MODEL.md](STATE_MODEL.md) | Knowledge states and lifecycle of protocol truth |
| [`../00-overview/`](../00-overview/) | Principles and vision that constrain architectural choices |
| [`../02-product/`](../02-product/) | Participant-facing flows that architecture must support |
| [`../03-development/`](../03-development/) | Conformance expectations derived from architectural invariants |
| [`../../rfcs/`](../../rfcs/) | Authoritative source when architecture is promoted to normative text |
| [`../../diagrams/`](../../diagrams/) | Visual companions to architecture documents |
| [`../templates/SPEC_TEMPLATE.md`](../templates/SPEC_TEMPLATE.md) | Format for stable architectural specification documents |
| [`../templates/DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md) | Format for recording architectural decisions |

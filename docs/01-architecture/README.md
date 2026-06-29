# Architecture

Structural documentation that describes how the VerityPay protocol is organized—its major components, boundaries, data representations, and cross-cutting quality attributes.

---

## Purpose

Architecture documents explain the *shape* of the system without prescribing a particular codebase layout. They give implementers and reviewers a shared map: what entities exist, how they relate, which invariants must hold, and where responsibilities divide.

This folder is where readers learn the protocol's skeleton before reading product-facing workflows or individual RFCs.

---

## What belongs here

- **System architecture** — major subsystems, trust boundaries, and interaction patterns at the protocol level
- **Data model** — entities, relationships, identifiers, and lifecycle states (described declaratively, not as ORM schemas)
- **Privacy model** — what information exists, who may learn it, and under what conditions
- **Security model** — threat assumptions, trust anchors, authentication and authorization boundaries, and security invariants
- **Interoperability model** — how independent implementations discover, negotiate, and validate compatibility
- **Protocol layering** — which concerns sit at which abstraction level and how layers depend on each other
- **Architecture Decision Records (ADRs)** — when architecture choices are made at the spec level before or alongside RFCs

Diagrams supporting these documents live in [`../../diagrams/`](../../diagrams/) and are referenced from here.

---

## What does not belong here

- Motivation and vision without structural content → [`../00-overview/`](../00-overview/)
- End-user stories and merchant-facing workflows → [`../02-product/`](../02-product/)
- Contributor onboarding and conformance test plans → [`../03-development/`](../03-development/)
- Exploratory designs not yet accepted → [`../04-research/`](../04-research/)
- Voting procedures and RFC lifecycle rules → [`../05-governance/`](../05-governance/)
- Implementation-specific module trees, package names, or deployment topologies
- Executable code, protobuf files, OpenAPI YAML, or database migrations

Architecture content becomes **normative** only when incorporated into or referenced by an **accepted RFC**. Draft architecture belongs in research or in an open RFC until accepted.

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

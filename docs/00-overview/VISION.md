---
spec: SPEC-0002
title: VerityPay Vision
status: Draft
version: 0.1.0

category: Constitutional

authors:
  - VerityPay Core Team

reviewers: []

depends_on:
  - MANIFESTO

required_by:
  - PRINCIPLES
  - ARCHITECTURE

implementation_repositories:
  - veritypay

last_updated: 2026-06-29
---

**Pyramid level:** constitutional · **Status:** draft · **Version:** 0.1.0

**Constitutional basis:** [MANIFESTO.md](MANIFESTO.md)

**Related documents:** [PRINCIPLES.md](PRINCIPLES.md), [GLOSSARY.md](GLOSSARY.md)

---

# VerityPay Vision

> *The North Star describes the world we want. This document describes the role VerityPay plays in creating it.*

---

## Constitutional layer

Part of the VerityPay [documentation pyramid](../README.md#documentation-pyramid). These four documents form the highest level of the specification hierarchy.

| Document | File | You are here |
|----------|------|:------------:|
| Manifesto | [MANIFESTO.md](MANIFESTO.md) | |
| Vision | [VISION.md](VISION.md) | **●** |
| Principles | [PRINCIPLES.md](PRINCIPLES.md) | |
| Glossary | [GLOSSARY.md](GLOSSARY.md) | |

**Suggested reading order:** Manifesto → Vision → Principles → Glossary (reference as needed).

**Downstream:** Architecture ([`01-architecture/`](../01-architecture/)) → Specifications ([`rfcs/`](../../rfcs/)) → Implementation (external repositories).

---

## Summary

VerityPay exists to make **payment claims verifiable and interoperable** through an open, protocol-first specification—not through any single product or vendor.

This Vision defines **what role the VerityPay protocol intends to play** in a world where trust is earned through transparent systems, participation is not gated by proprietary silos, and independent implementations can interoperate because they share accepted rules—not because they share a codebase.

It does not restate that world in full. The enduring direction of the institution lives upstream of any protocol. **Vision is the bridge:** from direction to specification, from philosophy to engineering.

---

## North Star and Vision

These documents answer different questions. Confusing them weakens both.

| Question | Answered by | Scope |
|----------|-------------|-------|
| *What world do we want to exist?* | Institutional North Star | Independent of VerityPay, any product, or any technology |
| *What role does VerityPay play in creating that world?* | **This document** | Protocol and ecosystem the specification defines |
| *Why does VerityPay exist as public infrastructure?* | [MANIFESTO.md](MANIFESTO.md) | Mission and public-good commitment |
| *How do we decide when specifications conflict?* | [PRINCIPLES.md](PRINCIPLES.md) | Durable heuristics and values |

The North Star remains valid if VerityPay never ships a line of code. VerityPay remains accountable to the North Star even when release pressure, adoption metrics, or competitive convenience suggest otherwise.

**Vision is protocol-scoped.** It tells contributors, integrators, and implementers what VerityPay is *for*—without claiming to be the whole institution or the whole future.

---

## The role of VerityPay

VerityPay intends to play four roles in the ecosystem:

### 1. Define verifiable payment behavior

Payment systems often assert outcomes. VerityPay specifies **claims that can be verified**—rules and invariants independent implementers can test against, audit against, and rely on without trusting a vendor's narrative alone.

The protocol does not replace trust everywhere. It ** reduces unnecessary trust** by making behavior explicit, reviewable, and shared.

### 2. Enable plural implementations

VerityPay is not a reference application wearing a specification costume. It is a **shared contract** among wallets, issuers, acquirers, merchants, integrators, and auditors.

No implementation owns the protocol. Implementations demonstrate; **accepted specification defines**.

### 3. Anchor open interoperability

VerityPay publishes binding behavior through governed specification—RFCs, architecture, and constitutional documents in this repository—not through private agreements or code discovery.

Private research informs the protocol. **Public specification authorizes it.**

### 4. Outlive any single team or product

VerityPay is designed as infrastructure whose value grows when more independent builders adopt, challenge, and improve it—not when one vendor captures the ecosystem.

Success is measured by the **durability and usefulness of the standard**, not by the number of products that share a brand.

---

## Desired future state

When VerityPay fulfills this Vision, the ecosystem exhibits:

| Outcome | Meaning |
|---------|---------|
| **Interoperable by specification** | Two conforming implementations handle the same payment claim consistently because they share accepted rules—not shared libraries |
| **Auditable by design** | Participants and third parties can trace requirements to documented decisions |
| **Evolvable by governance** | Protocol change is visible before it becomes permanent; breaking change is deliberate |
| **Accessible to builders** | New integrators onboard from public specification and RFC history—not from reverse-engineering a codebase |
| **Honest about uncertainty** | Open questions live in specification process until resolved; behavior not yet accepted is not implied by releases |

These outcomes serve a world where open infrastructure expands participation. VerityPay is one instrument in that direction—not the entire score.

---

## What VerityPay is responsible for

Within this Vision, VerityPay takes responsibility for:

- Maintaining a **canonical, public specification** for verifiable payment protocol behavior
- Governing change through **visible review**—especially RFCs that bind implementers
- Preserving **compatibility expectations** and documenting migration paths when change is necessary
- Ensuring constitutional documents, architecture, and accepted RFCs **align**—and resolving contradictions through governance, not silence
- Enabling **independent conformance**—specifications precise enough that interoperability is an engineering outcome, not a partnership negotiation

---

## What VerityPay is not responsible for

Clarity requires boundaries. VerityPay does not claim responsibility for:

- **Any single implementation's** product roadmap, UX, or commercial success
- **Market adoption** by itself—adoption follows utility and trust, not specification volume
- **Private research and exploration**—informative until promoted through governance
- **Every payment use case on Earth**—scope is defined deliberately through RFCs and non-goals
- **Substituting for regulation or legal compliance**—implementers remain accountable in their jurisdictions

VerityPay specifies protocol behavior. Participants remain responsible for how they deploy it.

---

## Success criteria

VerityPay is succeeding against this Vision when:

1. **Implementers cite specification versions** they target—and conformance is testable against accepted RFCs
2. **Multiple independent implementations** interoperate without bilateral custom agreements for core behavior
3. **Integrators onboard** from documentation in this repository without requiring insider access
4. **Auditors trace** requirements to accepted text and recorded governance decisions
5. **Changes** enter through RFC review—not through undocumented releases
6. **Constitutional alignment** holds: architecture and RFCs do not contradict [MANIFESTO.md](MANIFESTO.md), this Vision, or adopted [PRINCIPLES.md](PRINCIPLES.md)

Metrics of vanity—lines of spec, number of repos, release frequency—are not success criteria here.

---

## Vision tests

Before accepting major protocol direction, ask:

| Test | Question |
|------|----------|
| **Role** | Does this advance VerityPay's role—or merely advance one implementation? |
| **Star** | Does this move toward open, verifiable infrastructure—or toward proprietary advantage? |
| **Plurality** | Could a second implementation conform without our private history? |
| **Specification** | Is binding behavior documented here before it hardens in code? |
| **Governance** | Will affected parties see this change before it becomes entrenched? |
| **Legacy** | Will a maintainer in ten years understand why we chose this? |

Failure on a test is not automatic rejection—it requires **explicit governance record** and proportionate justification.

---

## If we lose this Vision

If VerityPay becomes a product specification rather than a protocol specification:

- Behavior lives in code; documentation follows or drifts
- Interoperability requires shared vendors, not shared rules
- Integrators negotiate in private; public specification becomes theater
- The institution optimizes for releases instead of for standards that outlive them

Recovery begins by restoring **specification primacy**, plural implementation, and public governance—not by renaming the problem.

---

## Relationship to downstream work

| Layer | How Vision constrains it |
|-------|--------------------------|
| [PRINCIPLES.md](PRINCIPLES.md) | Heuristics for resolving trade-offs under this Vision |
| [`01-architecture/`](../01-architecture/) | Structural models that make plural implementation possible |
| [`rfcs/`](../../rfcs/) | Normative changes that must align with Vision and Principles |
| Implementation repositories | Must conform to accepted specification—not define it |

Vision is **informative** at the constitutional layer unless explicitly incorporated by an accepted RFC. It binds **intent and direction** for governance and review; accepted RFCs bind **behavior** for implementers.

---

## Normative status

This document is **informative** until adopted through governance described in [`05-governance/`](../05-governance/). Upon adoption, it becomes a constitutional constraint: downstream specifications MUST NOT contradict an adopted Vision without constitutional amendment.

While in draft, it guides authoring and review but does not alone establish conformance requirements.

---

## Open questions

Items to resolve before stabilization:

- Formal adoption process and version pinning for constitutional documents
- Relationship between institutional Canon (private) and public constitutional layer—promotion path without duplication
- Scope boundaries for v1 protocol vs future extensions (to be defined through RFCs)

Remove or narrow this section when status reaches `stable`.

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial Vision authored; North Star vs Vision distinction; role and success criteria |

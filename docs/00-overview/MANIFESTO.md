---
spec: SPEC-0001
title: VerityPay Manifesto
status: Draft
version: 0.1.0

category: Constitutional

authors:
  - VerityPay Core Team

reviewers: []

depends_on: []

required_by:
  - VISION
  - PRINCIPLES
  - GLOSSARY

implementation_repositories:
  - veritypay

last_updated: 2026-06-29
---

**Pyramid level:** constitutional · **Status:** draft · **Version:** 0.1.0

**Related documents:** [VISION.md](VISION.md), [PRINCIPLES.md](PRINCIPLES.md), [GLOSSARY.md](GLOSSARY.md)

---

# VerityPay Manifesto

> *Trust should not be a prerequisite for participation. It should be the outcome of transparent systems.*

---

## Constitutional layer

Part of the VerityPay [documentation pyramid](../README.md#documentation-pyramid). These four documents form the highest level of the specification hierarchy.

| Document | File | You are here |
|----------|------|:------------:|
| Manifesto | [MANIFESTO.md](MANIFESTO.md) | **●** |
| Vision | [VISION.md](VISION.md) | |
| Principles | [PRINCIPLES.md](PRINCIPLES.md) | |
| Glossary | [GLOSSARY.md](GLOSSARY.md) | |

**Suggested reading order:** Manifesto → Vision → Principles → Glossary (reference as needed).

**Downstream:** Architecture ([`01-architecture/`](../01-architecture/)) → Specifications ([`rfcs/`](../../rfcs/)) → Implementation (external repositories).

---

## I

Money already moves across borders.

Trust does not.

Every day, millions of people rely on systems they cannot inspect, intermediaries they did not choose, and processes they cannot verify. Payroll crosses jurisdictions. Remittances traverse networks no worker selected. Auditors reconstruct truth from PDFs and proprietary logs. Integrators negotiate behavior in private because no shared protocol exists.

The machinery works—until someone asks a simple question: *How do you know?*

Too often, the honest answer is: *Because someone said so.*

We reject that as the final answer for infrastructure that millions depend on.

---

## II — What we believe

We believe **payment claims should be verifiable**—not merely asserted.

A claim is a statement that can be evaluated against shared rules and evidence. Verification produces an explicit outcome. Independent implementations, given the same inputs, should reach compatible conclusions—not because they share a vendor, but because they share a specification.

We believe **open infrastructure expands participation**.

When behavior is defined in public, reviewed before it hardens in code, and free to implement, more builders can enter. More auditors can inspect. More communities can adapt. Proprietary silos shrink not by decree, but because open standards are simply easier to trust at scale.

We believe **no implementation owns the protocol**.

Products come and go. Teams reorganize. Funding cycles end. A protocol that survives must outlive any single repository, any single company, any single charismatic maintainer. Specification defines. Code demonstrates. The order is not negotiable.

We believe **governed change is a feature, not friction**.

Protocols that cannot evolve die. Protocols that evolve in secret betray their users. We choose visible review, recorded decisions, and deliberate versioning—so that tomorrow's behavior is never an accident of yesterday's deploy.

We believe **clarity is an act of respect**.

Specifications are read under pressure—in incidents, in audits, in grant reviews, in classrooms. Obscurity is not sophistication. We write for the reader who arrives ten years from now without our context.

---

## III — What we are building

VerityPay is an **open protocol** for expressing, verifying, and interoperating **verifiable claims** about payment and payment-adjacent activity.

We begin with payments because that is where opacity costs the most—and where verifiable claims can do the most immediate good. The abstraction is broader: **assertion, evidence, verification, outcome**—a pattern that can extend to other domains without redefining truth each time.

We are building:

- A **public specification** anyone can read, challenge, and improve
- **Architecture** that separates identity, behavior, representation, and knowledge states
- **Governance** that turns decisions into durable records—not hallway agreements
- **Room for plural implementations** that compete on quality, not on lock-in

We are not building a single app and calling it a standard. We are building a standard worthy of many apps.

[VISION.md](VISION.md) defines VerityPay's **role** in detail. This Manifesto defines **why that role matters** to the world outside our repositories.

---

## IV — What we refuse

We refuse **behavior by implication**—where integrators must read source code to learn what "compliant" means.

We refuse **documentation as theater**—beautiful prose that drifts from what software actually does.

We refuse **urgency as an excuse**—shipping undisclosed protocol behavior because a deadline demanded it.

We refuse **hero culture over stewardship**—metrics that reward volume of commits over years of careful maintenance.

We refuse **trust me** as a substitute for **show your work**—when evidence, rules, and outcomes can be specified instead.

We refuse to confuse **marketing** with **mission**. This document is not a pitch deck. It is a declaration of what we are willing to build in public—and what we are not willing to pretend.

---

## V — Who this is for

**Workers and recipients** who deserve systems that can be explained—not only experienced.

**Builders** who want infrastructure they can implement without begging for API keys or private playbooks.

**Auditors and researchers** who need requirements they can trace—not narratives they must trust.

**Integrators** tired of bilateral glue code for every new counterparty.

**Funders** who invest in **people and public goods**, not opaque dependency chains.

**Skeptics** who ask hard questions—because hard questions make better protocols.

If you have read this far and thought *I want to help build this*—you are exactly who we wrote it for.

---

## VI — What we ask of you

Read before you implement. Propose before you redefine. Document before you disappear.

Start with this Manifesto, then [VISION.md](VISION.md), then [PRINCIPLES.md](PRINCIPLES.md). Follow the architecture in order. Open issues when something is unclear. Open RFCs when behavior must change.

Contribute at the level that matches your judgment—documentation, examples, tests, implementation—not architecture rewrites on day one. See [CONTRIBUTING.md](../../CONTRIBUTING.md).

Treat the specification as **infrastructure for strangers**—people you will never meet, in jurisdictions you will never visit, running software you did not write.

That is the bar.

---

## VII — A declaration

We declare that **verifiable claims** are a legitimate foundation for payment infrastructure in the open.

We declare that **protocol truth**—what satisfies rules and evidence at a declared specification version—is distinct from worldly truth, and that making the distinction explicit is an engineering obligation, not a philosophical luxury.

We declare that VerityPay will publish its reasoning, govern its changes, and welcome independent implementation—even when independence is inconvenient for any single actor.

We do not promise easy wins. We promise **honest work** in public.

The specification is the product. The community is the institution. The standard is the legacy.

**Build with us.**

---

## Relationship to other constitutional documents

| Document | Question it answers |
|----------|---------------------|
| **This Manifesto** | *Why should anyone care? Why join?* |
| [VISION.md](VISION.md) | *What role does VerityPay play?* |
| [PRINCIPLES.md](PRINCIPLES.md) | *How do we decide when values conflict?* |
| [GLOSSARY.md](GLOSSARY.md) | *What do our words mean?* |

Institutional Canon (North Star, Constitution, Engineering DNA) constrains the institution that maintains this public specification. When public text and institutional law must align, governance resolves the gap—never silence.

---

## Normative status

This document is **informative** until adopted through governance described in [`05-governance/GOVERNANCE.md`](../05-governance/GOVERNANCE.md). Upon adoption, it becomes a constitutional constraint: downstream specifications SHOULD align with its mission and public-good commitments.

The Manifesto does not alone define conformance requirements for implementations. Accepted RFCs do.

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial Manifesto; public declaration of mission and beliefs |

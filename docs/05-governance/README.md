# Governance

Documentation that defines how the VerityPay specification evolves: who decides, by what process, and with what transparency.

---

## Purpose

Open protocols outlive individual contributors and vendors. Governance documentation ensures that changes to VerityPay are deliberate, reviewable, and fair—that no single party can silently redefine the protocol.

This folder describes the **rules of change**, not the technical content being changed.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Contributors proposing RFCs | Understand review and acceptance criteria |
| Maintainers and editors | Apply consistent process |
| Ecosystem partners | Assess stability and influence mechanisms |
| Legal and compliance teams | Review IP and contribution terms |
| Any community member | Know how to participate responsibly |

Before submitting a protocol change, read this folder and [`../../rfcs/README.md`](../../rfcs/README.md).

---

## Scope

**In scope**

- Governance overview — goals, scope, and principles of project stewardship
- RFC process summary — how proposals move from draft to accepted (details in [`../../rfcs/`](../../rfcs/))
- Roles and responsibilities — maintainers, editors, working groups, and participants
- Decision-making model — consensus expectations, escalation, and deadlock handling
- Versioning and deprecation policy — labeling and sunsetting breaking changes
- Intellectual property and licensing — contribution terms for specification text
- Code of conduct — community behavior expectations
- Security disclosure policy — reporting vulnerabilities in specification material

**Out of scope**

- Technical protocol requirements → [`../../rfcs/`](../../rfcs/) and [`../01-architecture/`](../01-architecture/)
- Vision and values (substance, not process) → [`../00-overview/`](../00-overview/)
- Implementation release management → implementation repositories
- Research and exploratory analysis → [`../04-research/`](../04-research/)

Governance documents may themselves be updated through RFC when process changes are substantial.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../../rfcs/README.md`](../../rfcs/README.md) | Operational RFC process and lifecycle |
| [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md) | Required format for protocol change proposals |
| [`../00-overview/MANIFESTO.md`](../00-overview/MANIFESTO.md) | Mission and public-good philosophy (forthcoming) |
| [`../templates/DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md) | Format for governance and process decisions |
| [`../01-architecture/`](../01-architecture/) | Technical content governed by rules defined here |

---

## Core principle

**Specification changes are public decisions.** Private agreements, implementation shortcuts, and undocumented behavior do not alter the protocol. Only material accepted through governance becomes normative.

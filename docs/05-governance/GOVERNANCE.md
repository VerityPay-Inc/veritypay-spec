---
spec: SPEC-0501
title: VerityPay Governance
status: Draft
version: 0.1.0

category: Governance

authors:
  - VerityPay Core Team

reviewers: []

depends_on:
  - VISION
  - PRINCIPLES

required_by:
  - RFCs
  - CONFORMANCE_MODEL

implementation_repositories: []

last_updated: 2026-06-29
---

**Pyramid level:** governance (meta) · **Status:** draft · **Version:** 0.1.0

**Related documents:** [CONTRIBUTING.md](../../CONTRIBUTING.md), [rfcs/README.md](../../rfcs/README.md)

---

# VerityPay Governance

> *Public reasoning over private authority. Specification before implementation.*

---

## Purpose

Governance defines **how VerityPay decisions become binding**—before contributors write code, before integrators ship products, and before funders measure deliverables.

[CONTRIBUTING.md](../../CONTRIBUTING.md) explains how to participate. This document explains **who decides what**, through **which artifacts**, with **what transparency**.

VerityPay is specification-first: **specification defines; code demonstrates.** Governance exists so that rule is never inverted by accident, urgency, or vendor convenience.

Open protocols outlive individual contributors. Governance makes change **deliberate, reviewable, and auditable**—for contributors, implementers, auditors, and funding partners.

---

## Normative status

This document is **informative** until adopted through governance amendment. Process described here guides project operation; binding protocol behavior remains in accepted RFCs and incorporated architecture text.

When this document and an accepted RFC conflict on **protocol requirements**, the RFC prevails. When they conflict on **process**, this document prevails until amended.

---

## Governance principles

| Principle | Meaning |
|-----------|---------|
| **Public reasoning over private authority** | Decisions that affect the protocol leave a durable public record—issues, RFCs, ADRs—not hallway agreements |
| **Specification before implementation** | Normative behavior is proposed and reviewed in `veritypay-spec` before it hardens in code |
| **Contributors have standing** | Anyone may propose; review criteria are transparent; dismissal requires stated rationale |
| **Architecture changes require review** | Structural changes to the protocol stack are never drive-by edits |
| **Implementation cannot redefine protocol behavior** | When code and specification disagree, specification wins until changed through governance |

These principles align with institutional Canon (Constitution, Engineering DNA) and public constitutional documents ([VISION.md](../00-overview/VISION.md), [PRINCIPLES.md](../00-overview/PRINCIPLES.md)).

---

## Decision types

Not every change needs an RFC. Classify work before opening a pull request.

| Type | Affects protocol meaning? | Typical artifact |
|------|---------------------------|------------------|
| **Editorial clarification** | No | PR + issue |
| **Documentation improvement** | No | PR |
| **Architecture decision** | Maybe (if structural) | ADR; RFC if normative |
| **RFC / normative change** | Yes | RFC |
| **Implementation change** | Only if reflecting accepted spec | PR in implementation repo |
| **Security emergency** | Possibly | Security advisory + follow-up RFC/ADR |
| **Constitutional change** | Yes (direction/values) | RFC + governance review |

When uncertain, default to **higher formality** (ADR or RFC) rather than lower.

---

## Authority model

Authority is **distributed by scope**, not concentrated by title alone. Roles describe responsibilities; merge rights follow review outcomes.

### Roles

| Role | Responsibility |
|------|----------------|
| **Contributor** | Proposes changes via issues and PRs within [contributor level](../../CONTRIBUTING.md#contributor-levels) scope |
| **RFC Author** | Owns draft quality, responds to review, updates implementation status |
| **Reviewer** | Evaluates technical merit, spec alignment, clarity, compatibility impact |
| **Maintainer** | Triage, merge authority within delegated scope, RFC lifecycle stewardship |
| **Principal Architect** | Architecture integrity, ADR/RFC alignment with stack, escalation resolution on structural questions |
| **Security Contact** | Coordinates vulnerability disclosure, emergency response, post-incident specification updates |

One person may hold multiple roles. Roles are recorded in repository maintainers files and governance updates—not inferred from commit history alone.

### Authority matrix

| Action | Propose | Review | Approve / merge |
|--------|---------|--------|-----------------|
| Editorial clarification | Contributor | Reviewer | Maintainer |
| Documentation improvement | Contributor | Reviewer | Maintainer |
| Architecture decision (ADR) | Contributor+ | Reviewer + Principal Architect | Principal Architect or Maintainer |
| RFC draft | RFC Author | Reviewer(s) + Principal Architect | Maintainer (acceptance is recorded in RFC status) |
| RFC acceptance | — | Principal Architect + Maintainer(s) | Maintainer(s) per acceptance policy |
| Implementation PR | Contributor | Reviewer | Maintainer (implementation repo) |
| Security emergency fix | Security Contact | Security Contact + Maintainer | Maintainer (expedited); spec follow-up required |
| Constitutional change | RFC Author | Extended review | Maintainer(s) + governance record |

**Approve** for RFCs means updating RFC status to `accepted` through merged PR with recorded decision—not informal comment approval alone.

---

## Decision process

For each decision type: required artifact, review path, approval requirement, and where the record lives.

### Editorial clarification

| Field | Definition |
|-------|------------|
| **Artifact** | PR correcting ambiguity without behavior change |
| **Review path** | Reviewer confirms no normative impact |
| **Approval** | One Maintainer merge |
| **Record** | PR thread + merged commit |

### Documentation improvement

| Field | Definition |
|-------|------------|
| **Artifact** | PR (docs, diagrams, cross-links, examples) |
| **Review path** | Reviewer per [CONTRIBUTING.md](../../CONTRIBUTING.md#pull-request-requirements) |
| **Approval** | Maintainer merge |
| **Record** | PR + updated documents |

### Architecture decision

| Field | Definition |
|-------|------------|
| **Artifact** | ADR using [`DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md); RFC if normative |
| **Review path** | Principal Architect + Reviewer |
| **Approval** | Principal Architect or Maintainer; RFC acceptance if behavior binds implementers |
| **Record** | `docs/` ADR path or accepted RFC |

Structural changes to Architecture Alpha models require RFC (see [Architecture freeze](#architecture-freeze)).

### RFC / normative change

| Field | Definition |
|-------|------------|
| **Artifact** | RFC per [`RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md) |
| **Review path** | Public PR review; Principal Architect on architecture impact |
| **Approval** | Maintainer acceptance per [RFC governance](#rfc-governance) |
| **Record** | [`rfcs/`](../../rfcs/) + companion doc updates |

### Implementation change

| Field | Definition |
|-------|------------|
| **Artifact** | PR in `veritypay-core` or ecosystem repo |
| **Review path** | Reviewer; conformance checks when available |
| **Approval** | Implementation Maintainer merge |
| **Record** | PR + declared spec/RFC version in PR template |

Implementation MUST NOT introduce behavior absent from accepted specification.

### Security emergency

| Field | Definition |
|-------|------------|
| **Artifact** | Private report to Security Contact; coordinated advisory |
| **Review path** | Security Contact + Maintainer(s); expedited |
| **Approval** | Maintainer merge for mitigations; public disclosure per policy |
| **Record** | Security advisory + follow-up RFC/ADR for normative lessons |

### Constitutional change

| Field | Definition |
|-------|------------|
| **Artifact** | RFC amending Vision, Principles, Manifesto, or governance |
| **Review path** | Extended public comment period |
| **Approval** | Maintainer(s) per adoption policy; institutional Canon alignment check |
| **Record** | Accepted RFC + updated constitutional documents |

---

## RFC governance

### When an RFC is required

An RFC is required when:

- Conforming implementations would need to change behavior
- New claim types, verification rules, or interoperability requirements are introduced
- Architecture Alpha models require structural amendment
- Breaking changes or deprecations are proposed
- Constitutional or governance rules change materially

An RFC is **not** required for editorial clarification, non-normative documentation, or implementation changes that solely conform to already-accepted RFCs.

### RFC lifecycle

```
Draft → Review → Accepted → Implemented → Verified → Superseded
                  ↘ Rejected
```

| State | Meaning | Entry |
|-------|---------|-------|
| **Draft** | Work in progress; open for comment | RFC PR opened |
| **Review** | Ready for maintainer decision | Author sets `status: review` |
| **Accepted** | Binding protocol text | Maintainer merge + status update |
| **Rejected** | Will not adopt; rationale preserved | Maintainer decision |
| **Implemented** | Known implementation targets accepted text | `implementation_status` updated (informational) |
| **Verified** | Conformance evidence exists | Conformance tests or audit record (informational) |
| **Superseded** | Replaced by later RFC | Successor RFC accepted |

**Accepted** is the normative gate. **Implemented** and **Verified** track ecosystem maturity—they do not alone create protocol requirements.

Operational detail: [`rfcs/README.md`](../../rfcs/README.md).

### RFC acceptance criteria

Maintainers accept RFCs when:

1. Problem and scope are clearly stated
2. Alignment with Vision, Principles, and Architecture Alpha (or explicit amendment rationale)
3. Alternatives considered
4. Compatibility and migration addressed if breaking
5. Reviewer concerns substantially addressed
6. Companion documentation plan identified

Rejection preserves the document with rationale to prevent repeated debate without new evidence.

---

## Architecture freeze

**Architecture Alpha** is complete. The following documents define the conceptual protocol stack:

| Document | Role |
|----------|------|
| [DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) | Protocol + domain; truth and trust |
| [IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md) | Semantic identity |
| [BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md) | Verbs, events, behavioral invariants |
| [DATA_MODEL.md](../01-architecture/DATA_MODEL.md) | Entities, guarantees, representation |
| [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) | Knowledge states, lifecycles |

### Freeze policy

The Architecture Alpha stack is **frozen** as the structural foundation.

| Change type | Required path |
|-------------|---------------|
| Editorial clarification (no meaning change) | Documentation PR + Reviewer sign-off |
| Extension within existing contracts (e.g., new payment claim types via RFC) | RFC; may extend DATA_MODEL without restructuring |
| Structural change to models above | **RFC required**; Principal Architect review mandatory |
| Process-only architecture note | ADR |

**No drive-by architectural rewrites.** The next phase is **L3 Conformance**—making interoperability testable—not reopening L1/L2 design by default.

Errata (typos, broken links, ambiguous prose without behavior change) are welcome via documentation PRs.

---

## Contributor authority

Contributors may **propose at any level**—issues, PRs, RFCs, ADRs.

Authority to **merge** depends on:

| Factor | Effect |
|--------|--------|
| **Scope** | Matches [contributor level](../../CONTRIBUTING.md#contributor-levels) |
| **Review** | Required reviewers satisfied |
| **Artifact** | Correct type (PR vs RFC vs ADR) for the change |
| **Delegation** | Maintainer merge rights for repository and path |

Proposing an RFC does not imply acceptance. Proposing architecture changes without RFC during freeze requires maintainer redirection.

Contributors who consistently demonstrate judgment may be invited to Reviewer or Maintainer roles—earned through stewardship, not volume alone ([CONTRIBUTING.md — Recognition](../../CONTRIBUTING.md#recognition)).

---

## Conflict resolution

Conflicts are resolved in public where possible, with escalation when blocked.

### Implementation vs specification

| Situation | Resolution |
|-----------|------------|
| Implementation diverges from accepted RFC | Implementation is non-conformant until fixed **or** spec is changed via RFC |
| Implementation reveals spec ambiguity | Open clarification issue; editorial PR or RFC errata |
| Urgent production need | No silent spec bypass; expedited RFC or ADR with explicit temporary waiver recorded |

**Specification wins** by default.

### Specification vs Canon

| Situation | Resolution |
|-----------|------------|
| Public spec appears to contradict institutional Canon | Halt normative merge; Principal Architect + Maintainer escalate |
| Canon amendment needed | Institutional process (private Canon) + public RFC if protocol text changes |
| Vision/Principles draft vs Canon | Vision expresses protocol role; Canon constrains institution—reconcile before acceptance |

Do not publish contradictory normative text. Resolve before merge.

### Maintainer disagreement

| Step | Action |
|------|--------|
| 1 | Document positions in PR/RFC thread |
| 2 | Principal Architect recommends path aligned with principles |
| 3 | If unresolved, call for additional Reviewer or community comment period |
| 4 | Majority Maintainer acceptance on RFCs; failing that, status remains draft until consensus or explicit rejection |

Deadlock preserves **status quo**—draft RFCs do not become accepted without decision.

### Security urgency

| Step | Action |
|------|--------|
| 1 | Report to Security Contact (not public issue for exploitable issues) |
| 2 | Coordinated mitigation merge if needed |
| 3 | Public advisory when safe |
| 4 | Follow-up RFC/ADR for normative lessons |

Security urgency **does not** permanently redefine protocol without documented follow-up.

---

## Grant and funding transparency

VerityPay welcomes funded work that strengthens the public protocol. Funded contributions must remain **auditable and specification-aligned**.

### Expectations for funded work

| Requirement | Meaning |
|-------------|---------|
| **Public milestones** | Funded deliverables map to issues, RFCs, or conformance milestones visible in public repositories |
| **Specification traceability** | Work cites accepted RFCs or open RFCs—it does not ship secret protocol behavior |
| **No private normative forks** | Funder-specific behavior is not VerityPay protocol without RFC acceptance |
| **Deliverable types** | Documentation, examples, conformance tests, SDK improvements, reference interpreter—aligned with contributor levels |
| **Reporting** | Periodic public summary of merged work acceptable to funder and project (format TBD per grant) |

### What funders should expect

- Architecture Alpha is frozen; funded "redesigns" require RFC and community review
- Implementation funding does not buy specification authority
- Recognition follows [CONTRIBUTING.md](../../CONTRIBUTING.md#recognition)—stewardship over volume

### What this document does not cover

Private grant negotiations, contract terms, and employment agreements—see [Out of scope](#out-of-scope).

---

## Relationship to other documents

| Document | Role |
|----------|------|
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Onboarding, workflow, PR requirements |
| [rfcs/README.md](../../rfcs/README.md) | RFC operational process |
| [01-architecture/](../01-architecture/) | Architecture Alpha (frozen) |
| [03-development/](../03-development/) | Conformance (forthcoming, L3) |
| [DECISION_RECORD_TEMPLATE.md](../templates/DECISION_RECORD_TEMPLATE.md) | ADR format |

---

## Out of scope

This governance document explicitly excludes:

| Excluded | Notes |
|----------|-------|
| Legal entity formation | Corporate structure, jurisdiction, IP assignment agreements |
| Token governance | No protocol tokens; no on-chain voting for spec acceptance |
| Voting tokens or coin-weighted decisions | Decisions are merit and review based, not stake weighted |
| Employment contracts | HR matters |
| Private grant negotiations | Public summary only; terms remain between parties |
| Product roadmaps | [`02-product/`](../02-product/) and implementation repos |
| Code of conduct (full text) | Separate document when published |
| Security disclosure policy (full text) | Separate document when published; emergency path summarized here |

Substantive additions to governance itself require RFC or governance amendment PR with extended review.

---

## Open questions

- [ ] Maintainer roster publication format and rotation policy
- [ ] Minimum review period for RFC acceptance
- [ ] Formal Canon ↔ public spec promotion path without duplication
- [ ] Conformance verification criteria for RFC `verified` state
- [ ] Code of conduct and security disclosure document adoption

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial governance; Architecture Alpha freeze; authority model and decision types |

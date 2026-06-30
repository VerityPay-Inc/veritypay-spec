---
spec: SPEC-0003
title: VerityPay Principles
status: Draft
version: 0.1.0

category: Constitutional

authors:
  - VerityPay Core Team

reviewers: []

depends_on:
  - MANIFESTO
  - VISION

required_by:
  - RFCs
  - GOVERNANCE
  - CONFORMANCE_MODEL

implementation_repositories:
  - veritypay

last_updated: 2026-06-29
---

**Pyramid level:** constitutional · **Status:** draft · **Version:** 0.1.0

**Constitutional basis:** [MANIFESTO.md](MANIFESTO.md), [VISION.md](VISION.md)

**Related documents:** [GLOSSARY.md](GLOSSARY.md), [GOVERNANCE.md](../05-governance/GOVERNANCE.md)

---

# VerityPay Principles

> *Principles are stable. Implementations are not.*

---

## Constitutional layer

Part of the VerityPay [documentation pyramid](../README.md#documentation-pyramid). These four documents form the highest level of the specification hierarchy.

| Document | File | You are here |
|----------|------|:------------:|
| Manifesto | [MANIFESTO.md](MANIFESTO.md) | |
| Vision | [VISION.md](VISION.md) | |
| Principles | [PRINCIPLES.md](PRINCIPLES.md) | **●** |
| Glossary | [GLOSSARY.md](GLOSSARY.md) | |

**Suggested reading order:** Manifesto → Vision → Principles → Glossary (reference as needed).

**Downstream:** Architecture ([`01-architecture/`](../01-architecture/)) → Specifications ([`rfcs/`](../../rfcs/)) → Implementation (external repositories).

---

## Purpose

These principles constrain the **public VerityPay specification**—how protocol decisions are evaluated, how specifications evolve, and what every RFC must satisfy before acceptance.

They exist so protocol evolution remains **coherent** as contributors, implementations, and funding sources change over time.

This document is **not** institutional Canon. It does not replace North Star, Constitution, or Engineering DNA inside the organization. It is the **engineering constitution of the public spec**: the reference RFC reviewers use when asking whether a change belongs, whether it preserves meaning, and whether independent implementers can rely on it.

When [MANIFESTO.md](MANIFESTO.md) states *why* VerityPay matters and [VISION.md](VISION.md) states *what role* the protocol plays, **Principles** state *how we decide*.

---

## Normative status

This document is **informative** until adopted through governance described in [GOVERNANCE.md](../05-governance/GOVERNANCE.md).

Once adopted:

- RFCs **SHOULD** include a **Principles Alignment** section citing applicable principles
- Reviewers **SHOULD** use the [Principle Validation Checklist](#principle-validation-checklist) before acceptance
- Architecture and conformance documents **SHOULD** remain consistent with these principles unless an accepted RFC explicitly amends them

RFC 2119 keywords in accepted RFCs bind implementers. This document guides authoring and review until principles are incorporated by governance or cited normatively in accepted text.

---

## Table of contents

| Section | Anchor |
|---------|--------|
| Principle 1 | [principle-01](#principle-01) |
| Principle 2 | [principle-02](#principle-02) |
| Principle 3 | [principle-03](#principle-03) |
| Principle 4 | [principle-04](#principle-04) |
| Principle 5 | [principle-05](#principle-05) |
| Principle 6 | [principle-06](#principle-06) |
| Principle 7 | [principle-07](#principle-07) |
| Principle 8 | [principle-08](#principle-08) |
| Principle 9 | [principle-09](#principle-09) |
| Principle 10 | [principle-10](#principle-10) |
| Principles in Practice | [principles-in-practice](#principles-in-practice) |
| Validation Checklist | [principle-validation-checklist](#principle-validation-checklist) |

---

# The Ten Principles

<a id="principle-01"></a>

## Principle 1 — Specification Before Implementation

### Statement

**Protocol behavior is defined by specification before it is demonstrated in code.**

### Why it exists

Reverse-engineering behavior from a codebase produces silent lock-in, uneven interoperability, and audit trails that begin in Git history instead of public reasoning. VerityPay exists to invert that order.

### Implications

- New behavior enters through RFCs or governed specification text—not through releases alone
- Implementations may prototype; prototypes do not define the protocol
- When specification and implementation disagree, specification wins until changed through governance
- Documentation drift is treated as a defect, not an inevitability

### Example

An integrator needs a new payment claim outcome vocabulary. The change is drafted in an RFC, reviewed against architecture models, then implemented in `veritypay-core`—not shipped first and documented later.

---

<a id="principle-02"></a>

## Principle 2 — Semantics Before Representation

### Statement

**Meaning exists independently from JSON, databases, APIs, blockchains, or transports.**

### Why it exists

Formats change. Storage changes. Transports change. If meaning is defined by a schema file alone, the protocol dies when the schema is refactored. Semantic contracts must survive representation churn.

### Implications

- Architecture models define concepts, identity, behavior, and knowledge states before wire formats
- RFCs bind semantics first; encodings follow
- A field rename must not silently redefine what a claim *is*
- [`DATA_MODEL.md`](../01-architecture/DATA_MODEL.md) representations are consequences of upstream models—not inventors of protocol law

### Example

A verifiable claim's semantic identity is fixed at assertion. Whether `claim_id` is a UUID, prefixed string, or URI is representation—the claim remains the same assertion regardless.

---

<a id="principle-03"></a>

## Principle 3 — Truth Requires Evidence

### Statement

**Assertions alone are insufficient; verification always depends on evidence.**

### Why it exists

Payment systems confuse *said* with *shown*. VerityPay separates assertion from verification and requires explicit outcomes grounded in declared evidence and specification version ([DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) truth model).

### Implications

- Assertion MUST NOT imply satisfied verification
- Verification records MUST declare evidence considered—or explicit absence causing indeterminate outcome
- Authority may provide evidence; authority does not substitute for verification rules
- Outcomes are protocol truth (satisfied / not satisfied / indeterminate), not worldly economic fact

### Example

A claimant asserts payroll completion. A verifier evaluates the claim against rules at `vp-spec-2026-06` using bank batch evidence and a prior instruction claim—recording an explicit outcome without treating the assertion as proof.

---

<a id="principle-04"></a>

## Principle 4 — Independent Implementations

### Statement

**No implementation owns protocol behavior; interoperability is a design objective.**

### Why it exists

A protocol captured by one vendor is a product with extra steps. VerityPay measures success by plural, conforming implementations—not by market share of a reference codebase.

### Implications

- Conformance is to specification, not to "what the reference repo does"
- APIs and SDKs are conveniences; they are not the protocol
- RFCs MUST consider a second implementer who lacks private history
- Reference implementations demonstrate—they do not define

### Example

Two wallets from different vendors process the same payment claim and evidence under the same specification version and reach compatible verification outcomes without shared libraries or bilateral agreements for core behavior.

---

<a id="principle-05"></a>

## Principle 5 — Explicit Over Implicit

### Statement

**Behavior, versioning, assumptions, and outcomes should always be explicit.**

### Why it exists

Implicit behavior is where interoperability dies—inferred roles, silent defaults, undeclared specification versions, and transport success mistaken for verification success.

### Implications

- Specification version MUST be explicit in verification context
- Roles MUST be attributed on assertion and verification
- Verification outcomes MUST be explicit values—not inferred side effects
- Trust assumptions ([DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) trust model) are documented, not buried

### Example

A verification record states `outcome_value: indeterminate` with `evidence_declared: []` and a documented reason—rather than leaving integrators to guess whether "no response" means pending, failed, or approved.

---

<a id="principle-06"></a>

## Principle 6 — Stable Identity

### Statement

**Identity persists even as representation evolves.**

### Why it exists

Auditable protocols require referential stability. If claims, evidence, and verification records can be rewritten in place, history becomes negotiable and trust collapses.

### Implications

- Semantic identity is defined in [IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md)—separate from storage identifiers
- Asserted claim content MUST NOT mutate in place
- Finalized verification records MUST NOT rewrite outcomes
- Supersession creates new authority; it does not erase prior identity

### Example

Claim `clm_001` is superseded by `clm_002`. Both remain resolvable in audit history; `clm_001` is not deleted or overwritten because a newer claim exists.

---

<a id="principle-07"></a>

## Principle 7 — Governed Evolution

### Statement

**Protocols evolve through RFCs, not accidental implementation.**

### Why it exists

Urgent patches and undocumented flags accumulate into proprietary dialects. Governed evolution makes change visible, reviewable, and reversible in principle—even when the change is small.

### Implications

- Architecture Alpha is frozen; structural changes require RFC ([GOVERNANCE.md](../05-governance/GOVERNANCE.md))
- Breaking changes require migration narrative and deprecation discipline
- Rejected RFCs are preserved with rationale
- Security emergencies may mitigate first; normative follow-up is still required

### Example

A new payment claim type is introduced through an accepted RFC that extends [`DATA_MODEL.md`](../01-architecture/DATA_MODEL.md) within existing semantic contracts—not by adding a new JSON field in one implementation's API.

---

<a id="principle-08"></a>

## Principle 8 — Reproducible Outcomes

### Statement

**Equivalent inputs under the same specification version should produce compatible outcomes.**

### Why it exists

Without reproducibility, "verifiable" is a label. Independent auditors and implementers must reach the same conclusion from the same claim, evidence, and rule set.

### Implications

- Verification is interpreted at a declared specification version
- Conformance tests target outcome compatibility, not byte-identical logs
- Indeterminate is a first-class outcome when rules cannot fully run
- Hidden implementation state MUST NOT affect protocol outcome

### Example

Given identical claim `clm_001`, evidence set `{evd_a, evd_b}`, and `vp-spec-2026-06`, two conforming verifiers both record `satisfied`—or both record `indeterminate` for the same structural reason.

---

<a id="principle-09"></a>

## Principle 9 — Layered Responsibility

### Statement

**Identity, behavior, representation, and state solve different problems—avoid cross-layer coupling.**

### Why it exists

Collapsing layers produces schemas that encode lifecycle as identity, APIs that invent behavior, and state flags that silently redefine meaning. The architecture stack exists to prevent that.

### Implications

| Layer | Document | Question |
|-------|----------|----------|
| Domain + protocol | [DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) | What exists? What is true? |
| Identity | [IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md) | What is this object? |
| Behavior | [BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md) | What may happen? |
| Representation | [DATA_MODEL.md](../01-architecture/DATA_MODEL.md) | How is it encoded? |
| Knowledge state | [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) | What does the protocol know now? |

- RFCs MUST declare which layer they affect
- A state transition MUST NOT rewrite semantic identity
- Representation MUST NOT create behavior

### Example

`finalized: true` on a verification record is knowledge state—not a substitute for recording an explicit `outcome_value` in the representation layer.

---

<a id="principle-10"></a>

## Principle 10 — Conformance Is the Goal

### Statement

**The purpose of the specification is not to create one implementation—it is to enable many correct implementations.**

### Why it exists

Specifications that optimize for a single team's velocity become tombstones for everyone else. VerityPay optimizes for **testable interoperability** across strangers.

### Implications

- Conformance model (forthcoming) translates principles into verifiable requirements
- RFCs SHOULD identify conformance impact
- Funded work MUST map to public, testable deliverables—not private dialects
- Success is measured by independent reproduction of protocol behavior

### Example

A grant funds a reference interpreter and conformance vectors. Multiple teams pass the same scenarios with different codebases—that is success—not one polished demo app.

---

<a id="principles-in-practice"></a>

## Principles in Practice

| Situation | Primary principle(s) | Guidance |
|-----------|---------------------|----------|
| **New entity** | 2, 9 | Define semantic contract and layer placement before fields; RFC if normative |
| **Breaking change** | 7, 8 | RFC with migration path; preserve auditability of prior identities |
| **Serialization format** | 2, 5 | Bind semantics in RFC; format is representation, not meaning |
| **New verification rule** | 3, 5, 8 | Declare evidence requirements, version, explicit outcomes; conformance scenarios |
| **Extension proposal** | 2, 7, 9 | Extension points in DATA_MODEL; no silent core contract change |
| **Implementation optimization** | 1, 4, 10 | MUST NOT change observable protocol behavior without RFC |
| **Editorial clarification** | 1, 5 | Allowed when meaning unchanged; reviewer confirms no normative drift |
| **Security hotfix** | 7, 3 | Mitigate first if needed; normative record follows |
| **UI / product workflow** | 9 | Belongs in product docs—not protocol architecture |
| **Performance shortcut** | 4, 8 | Cache and optimize internally; outcomes remain reproducible |

---

<a id="principle-validation-checklist"></a>

## Principle Validation Checklist

Use when authoring or reviewing RFCs and specification changes. Every **Principles Alignment** section in an RFC SHOULD reference this checklist.

### Design questions

| # | Question | Principles |
|---|----------|------------|
| 1 | Does this preserve semantic meaning for existing artifacts? | 2, 6 |
| 2 | Does this introduce hidden or implicit behavior? | 5 |
| 3 | Is interoperability improved or at least preserved? | 4, 8, 10 |
| 4 | Is identity preserved across lifecycle transitions? | 6, 9 |
| 5 | Does this belong in the correct architectural layer? | 9 |
| 6 | Does this require an RFC (or is editorial only)? | 1, 7 |
| 7 | Can independent implementations reproduce the same outcome? | 4, 8 |
| 8 | Is verification evidence and version explicit? | 3, 5 |
| 9 | Does this define behavior before (or without) implementation precedent? | 1 |
| 10 | Are conformance implications identified? | 10 |

### Per-principle tracker

| Principle | Applicable | Cited in RFC | Aligned | Notes |
|-----------|:----------:|:------------:|:-------:|-------|
| 1 — Specification before implementation | [ ] | [ ] | [ ] | |
| 2 — Semantics before representation | [ ] | [ ] | [ ] | |
| 3 — Truth requires evidence | [ ] | [ ] | [ ] | |
| 4 — Independent implementations | [ ] | [ ] | [ ] | |
| 5 — Explicit over implicit | [ ] | [ ] | [ ] | |
| 6 — Stable identity | [ ] | [ ] | [ ] | |
| 7 — Governed evolution | [ ] | [ ] | [ ] | |
| 8 — Reproducible outcomes | [ ] | [ ] | [ ] | |
| 9 — Layered responsibility | [ ] | [ ] | [ ] | |
| 10 — Conformance is the goal | [ ] | [ ] | [ ] | |

**Reviewer attestation**

| Field | Value |
|-------|-------|
| RFC / change under review | |
| Reviewer | |
| Date | |
| All applicable principles addressed | [ ] |

---

## Relationship to other documents

| Document | How it uses Principles |
|----------|------------------------|
| [MANIFESTO.md](MANIFESTO.md) | States *why*—Principles state *how we decide* in engineering terms |
| [VISION.md](VISION.md) | Defines protocol role—Principles constrain trade-offs toward that role |
| [Architecture](../01-architecture/) | Embodies principles in models; RFCs amending architecture must align |
| [GOVERNANCE.md](../05-governance/GOVERNANCE.md) | Process for adoption, RFC acceptance, Architecture Alpha freeze |
| Conformance model (forthcoming) | Operationalizes Principle 10 into testable requirements |
| [RFCs](../../rfcs/) | MUST include Principles Alignment; acceptance uses checklist |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Onboarding—Principles are required reading before normative proposals |

Institutional Canon (North Star, Constitution, Engineering DNA) constrains the organization that maintains this repository. Principles constrain the **public specification**. When they appear to conflict, escalate per [GOVERNANCE.md](../05-governance/GOVERNANCE.md)—do not merge layers silently.

---

## Closing

Good protocols are not defined by the number of features they contain.

They are defined by the **consistency of the principles that survive every new feature**.

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.0.0 | 2026-06-29 | Document structure prepared |
| 0.1.0 | 2026-06-29 | Ten principles authored; validation checklist; RFC review reference |

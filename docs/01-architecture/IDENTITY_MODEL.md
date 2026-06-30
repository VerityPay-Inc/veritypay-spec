---
spec: SPEC-0102
title: VerityPay Identity Model
status: Draft
version: 0.1.0

category: Architecture

authors:
  - VerityPay Core Team

reviewers: []

depends_on:
  - DOMAIN_MODEL

required_by:
  - DATA_MODEL
  - STATE_MODEL

implementation_repositories:
  - veritypay

last_updated: 2026-06-29
---

**Pyramid level:** architecture · **Status:** draft · **Version:** 0.1.0

**Constitutional basis:** [DOMAIN_MODEL.md](DOMAIN_MODEL.md) Part I (truth and trust) and Part II (domain language)

**Related documents:** [BEHAVIOR_MODEL.md](BEHAVIOR_MODEL.md), `DATA_MODEL.md` (forthcoming), state models (forthcoming)

---

# VerityPay Identity Model

> *Identity never changes. State always changes. Those are different concerns.*

---

## Architecture layer

Part of the VerityPay [documentation pyramid](../README.md#documentation-pyramid).

```
Manifesto → Vision → Principles → Glossary
         ↓
    Architecture
         ↓
    Protocol + Domain Model  →  Identity Model  →  Data Model  →  State Model
         ↓
    Specifications → Implementation
```

**Upstream:** [DOMAIN_MODEL.md](DOMAIN_MODEL.md)

**Downstream:** [BEHAVIOR_MODEL.md](BEHAVIOR_MODEL.md) → `DATA_MODEL.md` (representations and storage identity), state models (mutable lifecycle)

---

## Summary

This document defines **what makes protocol objects themselves**—before fields, types, or encodings.

VerityPay separates:

| Concern | Question | Document |
|---------|----------|----------|
| **Semantic identity** | Is this the *same* claim, participant, or verification? | This document |
| **Storage identity** | How is it keyed in a database, ledger, or message? | `DATA_MODEL.md` |
| **Lifecycle state** | What phase is it in now? | State models |

**Behavior first. Representation second.** Invariants precede field names. When `DATA_MODEL.md` introduces `claim_id`, it will exist because this document already established that a claim's identity never changes after assertion.

---

## Purpose

[DOMAIN_MODEL.md](DOMAIN_MODEL.md) defines **what nouns exist** and how they relate in language.

The identity model answers **what makes each noun the same noun over time**:

- What makes a **claim** the same claim after assertion?
- What makes **evidence** referentially stable when cited in verification?
- What makes a **verification record** immutable once recorded?
- What constitutes a **participant's** identity within the protocol?
- What identifies a **specification version** unambiguously across implementations?

Without these answers, data models devolve into UUID columns without meaning. With them, schemas become consequences of protocol law.

---

## Normative status

This document is **informative** until incorporated by an accepted RFC or marked `stable` through governance.

Terms and invariants here are **authoritative for authoring** `DATA_MODEL.md` and state models. RFC 2119 keywords appear only in accepted specifications—not here.

---

## Design principles

### Semantic identity before storage identity

**Semantic identity** is protocol meaning: *this is the same claim*.

**Storage identity** is implementation convenience: UUID, database row, ledger entry, content identifier (CID), hash, or URI.

```
Semantic identity     This is the same claim.
        ↓
Storage identity      UUID · row · ledger ID · CID · …
```

One semantic object MAY have many storage identifiers across systems. Storage identifiers MUST NOT redefine semantic identity unless an RFC specifies a governed mapping.

### Invariants before fields

Most specifications begin with:

```
claim_id: UUID
```

VerityPay begins with:

```
Invariant: A claim's semantic identity never changes after assertion.
        ↓
claim_id: (defined in DATA_MODEL.md as storage identity)
```

### Concept before representation

For each protocol object, this document follows:

```
Concept → Identity → Relationships → Invariants → Lifecycle → Representations
```

**Representations** (JSON shapes, field names, canonical serialization) belong in `DATA_MODEL.md` and RFCs—listed last here as placeholders only.

### Identity is not state

| Identity | State |
|----------|-------|
| What the object *is* | Where the object *is* in a lifecycle |
| Stable after assertion (claims) | Changes (composed → asserted → …) |
| Defined here | Defined in state models |

Confusing identity with state produces un-auditable history—"the same claim" that silently becomes a different claim when status changes.

---

## Identity hierarchy

Protocol objects form a referential hierarchy. Each level answers: **What makes this object itself?**

```
Participant
    ↓ presents
Verifiable Claim (Payment Claim in v1 domain)
    ↓ supported by
Evidence
    ↓ evaluated in
Verification Record
    ↓ interpreted under
Specification Version
```

| Object | Identity question |
|--------|-------------------|
| **Participant** | Who is acting in this protocol trace? |
| **Verifiable Claim** | Which assertion is this, distinct from all others? |
| **Evidence** | Which material is this, when cited by verifiers? |
| **Verification Record** | Which evaluation event is this, immutable once recorded? |
| **Specification Version** | Which rule set governed this evaluation? |

---

## Cross-cutting identity rules

These rules apply across all objects below unless an RFC specifies an exception.

1. **Referential stability.** Once an object is cited in a verification record, later references MUST resolve to the same semantic object.
2. **No silent identity merge.** Two distinct claims MUST NOT collapse into one identity because storage systems deduplicate rows.
3. **Supersession is explicit.** A later claim may supersede *authority* of an earlier claim; it does not rewrite the earlier claim's identity.
4. **Version is part of verification context.** Verification identity includes the specification version under which rules ran.
5. **Amendment is new identity.** Changing semantic content after assertion requires a new claim (or governed supersession claim)—not an in-place identity mutation.

---

## Participant

### Purpose

A **participant** is an entity that acts in the protocol through one or more **roles** ([DOMAIN_MODEL.md](DOMAIN_MODEL.md)).

### Semantic identity

A participant is identified by **protocol-scoped identity**—the stable answer to *who acted* in traces, assertions, and verification records.

Participant identity is **not** an organization chart node. The same legal entity MAY appear as multiple participants if the protocol requires distinct protocol identities (e.g., separate integrator vs claimant contexts).

### Ownership

Participants **own** their role attributions in protocol traces. They do not own claims asserted by other participants.

### Versioning

Participant identity is **stable across specification versions**. Spec evolution may add roles or responsibilities; it does not silently retcon who existed.

### Relationships

| Related | Relationship |
|---------|--------------|
| **Role** | Participant acts *as* role in a trace |
| **Verifiable Claim** | Participant as claimant *asserts* |
| **Verification Record** | Participant as verifier *evaluates* |
| **Evidence** | Participant may *provide* or *attest* |

### Invariants

1. **Attribution.** Every assertion and verification MUST attribute to a participant identity (or explicit anonymous role if an RFC defines one).
2. **Role explicitness.** Identity alone does not imply role; role MUST be explicit in context.
3. **Stability within trace.** Participant identity MUST NOT change mid-trace for the same logical actor.

### Lifecycle (identity-relevant)

Participant identity **persists** beyond individual claims. Deactivation or retirement is a **state** concern; retired participants remain referentially stable in history.

### Representations

*Forthcoming in `DATA_MODEL.md`.* Expected: participant identifiers, optional external identity bindings (org IDs, key material references)—without conflating them with semantic identity.

---

## Verifiable Claim

### Purpose

A **verifiable claim** is the central protocol artifact: a structured statement about a **subject**, evaluable through verification ([DOMAIN_MODEL.md](DOMAIN_MODEL.md)).

**Payment claims** are the v1 domain specialization; identity rules apply to all verifiable claims unless an RFC narrows further.

### Semantic identity

A claim's semantic identity is established **at assertion** and **never changes**.

Two presentations of the same claim MUST be recognized as the same assertion—not two similar claims.

Semantic identity is **not** derived from:

- Claim content edits after assertion
- Lifecycle state (asserted vs under verification)
- Storage location or transport path
- Outcome (satisfied vs not satisfied)

### Ownership

The **claimant** participant owns the act of assertion. Other participants may hold copies; ownership of *assertion* does not transfer with relay.

### Versioning

Claims are **authored against** a specification version. Claim *type* semantics may be version-specific. Claim *identity* is independent of which version evaluates it—though evaluation MUST declare version context.

### Relationships

| Related | Relationship |
|---------|--------------|
| **Claim Subject** | Claim is *about* subject |
| **Claim Content** | Content is payload of this identity |
| **Evidence** | Evidence *supports* or *contradicts* |
| **Verification Record** | Record *evaluates* this claim |
| **Prior / later claims** | *Reference* or *supersede* (without merging identity) |

### Invariants

1. **Immutability after assertion.** Semantic identity and asserted content are fixed at assertion.
2. **Distinctness.** Two assertions produce two identities—even if content is byte-identical (duplicate assertion is a protocol design choice for RFCs).
3. **Reference stability.** Any claim cited in evidence or verification MUST remain resolvable as the same claim.
4. **Supersession ≠ rewrite.** Supersession marks authority transfer; the superseded claim retains its identity in audit history.

### Lifecycle (identity-relevant)

Lifecycle phases ([DOMAIN_MODEL.md](DOMAIN_MODEL.md)) change **state**, not **identity**. A claim in *retired* state is the same claim as when *asserted*.

### Representations

*Forthcoming in `DATA_MODEL.md`.* Expected: `claim_id` or equivalent as **storage identity**; canonical content hashing MAY support deduplication but MUST NOT override assertion-bound semantic identity without RFC rules.

---

## Payment Claim

Payment claims inherit **all verifiable claim identity rules**.

### Purpose

A **payment claim** is a verifiable claim whose subject matter is in the **payment domain**.

### Semantic identity

Identity is **claim identity**—not payment event identity. Multiple payment claims MAY reference the same real-world payment; each assertion retains distinct identity.

### Additional invariant

**Payment ≠ claim.** Collapsing a worldly payment event and a payment claim into one identifier is forbidden at the semantic layer.

### Representations

*Forthcoming in `DATA_MODEL.md`.* Payment-domain claim types will extend representation without redefining core claim identity.

---

## Evidence

### Purpose

**Evidence** is material verification rules consume—proofs, prior claims, attestations, specified inputs ([DOMAIN_MODEL.md](DOMAIN_MODEL.md)).

### Semantic identity

Evidence identity is **intrinsic to the material** plus **protocol context** (what is being cited, at what assertion boundary).

The same bytes presented as evidence in two unrelated verifications MAY share storage identity but MUST be citable as the same evidence artifact when referenced from a verification record.

### Ownership

The participant that **presents** evidence for verification owns that presentation act. Underlying material may originate elsewhere (e.g., a prior claim asserted by another participant).

### Versioning

Evidence interpretability depends on **specification version**. Identity of the evidence artifact is stable; *evaluability* may change across versions—yielding indeterminate outcomes, not new evidence identity.

### Relationships

| Related | Relationship |
|---------|--------------|
| **Verifiable Claim** | Evidence *relates to* claim under evaluation |
| **Verifiable Claim (as evidence)** | Prior claims MAY serve as evidence |
| **Verification Record** | Record *declares* evidence considered |
| **Participant** | Presenter / attester |

### Invariants

1. **Citation stability.** Evidence listed in a verification record MUST remain resolvable.
2. **Declaration.** Verification MUST declare evidence considered—or explicit absence causing indeterminate outcome ([DOMAIN_MODEL.md](DOMAIN_MODEL.md) domain invariant 4).
3. **No silent substitution.** Replacing evidence after verification begins invalidates the verification context unless rules define controlled re-evaluation as a **new** verification record.

### Lifecycle (identity-relevant)

Evidence may be **composed**, **presented**, **evaluated**, or **archived**. Identity persists through archival.

### Representations

*Forthcoming in `DATA_MODEL.md`.* Expected: evidence handles, content references, optional integrity proofs—distinct from claim identifiers.

---

## Verification Record

### Purpose

A **verification record** captures the **evaluation** of a verifiable claim against rules and evidence at a specification version—producing an explicit **outcome**.

It is the protocol's durable answer to: *What did verification conclude, and on what basis?*

### Semantic identity

A verification record is identified by the **unique evaluation event**: which claim, which evidence set (as declared), which specification version, which verifier context, and which outcome—fixed when the record is **finalized**.

Verification records are **immutable** after finalization. Re-running verification produces a **new** record—not an overwrite.

### Ownership

The **verifier** participant owns the verification act. Observers may hold copies.

### Versioning

Every record **binds** to exactly one specification version for rule interpretation. Re-verification under a new version is a new record.

### Relationships

| Related | Relationship |
|---------|--------------|
| **Verifiable Claim** | Record *evaluates* one claim (primary) |
| **Evidence** | Record *references* evidence considered |
| **Specification Version** | Record *interpreted under* version |
| **Participant** | Verifier *performs* evaluation |

### Invariants

1. **Immutability after finalization.** Outcome, evidence declaration, and rule context MUST NOT change in place.
2. **Reproducibility.** Record content MUST be sufficient for conforming re-evaluation to reach the same outcome ([DOMAIN_MODEL.md](DOMAIN_MODEL.md) truth model).
3. **Outcome explicitness.** Record MUST state satisfied, not satisfied, or indeterminate—not an implicit side effect.
4. **One finalized outcome per record.** Ambiguity requires indeterminate outcome or multiple records per RFC rules—not merged identity.

### Lifecycle (identity-relevant)

States such as *in progress* vs *finalized* belong in state models. Finalization **fixes** identity for audit.

### Representations

*Forthcoming in `DATA_MODEL.md`.* Expected: verification record identifiers separate from claim identifiers.

---

## Specification Version

### Purpose

A **specification version** identifies the **rule set** under which claims are expressed and verified ([DOMAIN_MODEL.md](DOMAIN_MODEL.md)).

### Semantic identity

A specification version is identified by a **governed, unambiguous version identity**—not by "latest" or by implementation release tags alone.

### Ownership

The VerityPay governance process **owns** version publication. Implementations **declare** conformance to published versions.

### Versioning

Specification versions are **immutable** once published. Errata may clarify; behavioral change requires a **new** version identity.

### Relationships

| Related | Relationship |
|---------|--------------|
| **Verification Record** | Every record *binds to* one version |
| **Verifiable Claim** | Claim types and rules *defined by* version |
| **Conformance** | Implementations *target* declared versions |

### Invariants

1. **Explicit binding.** Verification without declared specification version is undefined at protocol level.
2. **Shared meaning.** Two conforming parties using the same version identity MUST share the same normative rule interpretation (within accepted RFC set for that version).
3. **No silent drift.** Private rule extensions MUST NOT reuse the same version identity.

### Lifecycle (identity-relevant)

Versions move through governance states (draft, accepted, deprecated). **Identity** of an accepted version is permanent; **deprecation** is state, not deletion.

### Representations

*Forthcoming in `DATA_MODEL.md` and governance docs.* Expected: version strings, document manifests, RFC bundles.

---

## Claim Subject (identity anchor)

Subjects are not full aggregates in this hierarchy but require an **identity anchor** so multiple claims can relate without merging claim identity.

### Semantic identity

A **claim subject** is *what the claim is about*—identified sufficiently that verification rules can relate claims, detect conflict, and resolve contradictions ([DOMAIN_MODEL.md](DOMAIN_MODEL.md) domain invariant 3).

### Invariant

**Subject identity ≠ claim identity.** Many claims, one subject. One claim, one subject anchor (per assertion).

### Representations

*Forthcoming in `DATA_MODEL.md`.* Subject identification across participants is an open specification track (see below).

---

## Relationship to downstream documents

| Document | This model provides |
|----------|---------------------|
| **`DATA_MODEL.md`** | Semantic identity and invariants; storage identifiers and encodings derived last |
| **State models** | Mutable lifecycle; transitions that MUST NOT alter semantic identity |
| **Security model** | Protects trust assumptions (T1–T6 in [DOMAIN_MODEL.md](DOMAIN_MODEL.md)) |
| **RFCs** | Normative MUST/SHOULD for identity-critical behavior |
| **Conformance tests** | Scenarios proving referential stability and immutability |

**Authoring order:** Protocol + domain → **identity (this document)** → data model → state model → RFCs.

---

## Contributor specification tracks

The protocol stack is structured enough for **specification contributions**—self-contained issues that trace to [DOMAIN_MODEL.md](DOMAIN_MODEL.md) without changing project direction.

| Track | Delivers |
|-------|----------|
| Payment claim taxonomy | Initial payment claim types and subject anchors |
| Verification outcome taxonomy | Formal outcome vocabulary and edge cases |
| Identity model refinement | This document → stable; storage identity mappings |
| State model (first) | Lifecycle states that preserve identity invariants |
| Canonical sequence diagrams | Assertion → verification → outcome flows |
| Conformance test scenarios | Identity immutability, supersession, re-verification |

These are **specification issues**, not implementation tasks.

---

## Open questions

- [ ] Minimum **participant identity** mechanism for v1 (key-based, registered ID, federated)
- [ ] **Duplicate assertion** — same content, two identities: allowed, discouraged, or deduplicated at storage only?
- [ ] **Subject identification** across independent participants without global registry
- [ ] **Verification record** granularity — one record per claim vs per rule bundle
- [ ] Canonical mapping between **semantic** and **storage** identity when content-addressed storage (CID/hash) is used
- [ ] **Anonymous or pseudonymous** participants — identity model extensions vs separate privacy architecture

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial identity model; semantic vs storage identity; hierarchy and invariants |

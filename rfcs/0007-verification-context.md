---
rfc: 0007
id: 0007
concept_id: VP-RFC-0007
title: Verification Context
status: draft
version: 0.1.0
type: protocol
category: Protocol
pyramid_level: specification

authors:
  - VerityPay Core Team

reviewers: []

created: 2026-07-03
updated: 2026-07-03

depends_on:
  - 0000
  - 0001
  - 0004
supersedes: []
superseded_by: null

related_terms:
  - VP-TERM-004
  - VP-TERM-011
  - VP-TERM-013
  - VP-TERM-024

related_architecture:
  - ../docs/01-architecture/DATA_MODEL.md
  - ../docs/03-development/CONFORMANCE_MODEL.md

related_conformance:
  - VP-CS-0001
  - VP-CS-0002

constitutional_refs:
  - ../docs/00-overview/MANIFESTO.md
  - ../docs/00-overview/VISION.md
  - ../docs/00-overview/PRINCIPLES.md
  - ../docs/00-overview/GLOSSARY.md

related_docs:
  - ../docs/03-development/CONFORMANCE_MODEL.md
  - ../ECOSYSTEM.md
  - 0001-minimal-claim-evidence-semantics.md
  - 0004-evidence-evaluation-policies.md

implementation_status: not_started
last_updated: 2026-07-03
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0007

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [VP-RFC-0004](0004-evidence-evaluation-policies.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0007: Verification Context

## Summary

This RFC introduces **Verification Context** — the protocol object that describes the **immutable evaluation environment** in which verification occurs.

It defines **context only**. It does **not** define trust, issuers, authorization, or new verification outcomes.

Draft fields align with existing protocol concepts: **edition**, **protocol_version**, and **evaluation_policy**. The change is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) and [VP-RFC-0004](0004-evidence-evaluation-policies.md). **Platform 1.2** pins remain valid until implementations opt into explicit context objects.

---

## Motivation

Verification is never completely isolated.

Every verification occurs within a context. Examples include:

- specification **edition**
- **protocol version**
- **evaluation policy**
- evaluation timestamp
- implementation profile
- extension identifiers

Rather than embedding these into **Claims** or **Evidence**, Verity introduces a dedicated **Verification Context** that supplies evaluation-wide information shared by all **Assertions** and **Evidence** during one verification.

This RFC names the object and its initial fields. It does **not** relocate claim or evidence semantics into context.

---

## Problem Statement

Today, evaluation-wide parameters are implied by specification metadata, fixture headers, and harness configuration. Implementations agree in practice but lack a single protocol object naming the shared evaluation environment.

Without **Verification Context**:

- Edition and policy bindings scatter across claims, fixtures, and interpreter options.
- Conformance cannot compare evaluation environment declarations independently of claim inputs.
- Future context fields (locale, extensions, profile) lack a stable attachment point.

---

## Goals

- Define **Verification Context** as protocol vocabulary.
- Require immutability and evaluation-wide scope during one verification.
- Specify initial fields that map to existing concepts.
- Document informative future fields without defining their semantics.
- Preserve **Claim** and **Evidence** semantics unchanged.

## Non-Goals

- Trust policy, issuer identity, or authorization models.
- New **VP-RULE** text or verification outcome vocabulary.
- Wire encodings, fixture schema changes, or reference interpreter behavior.
- Relocating `specification_version` from claim envelopes into context as a breaking change.

---

## Normative Terminology

### Verification Context

**Definition:** The immutable protocol object that supplies evaluation-wide information shared by all **Assertions** and **Evidence** during one verification.

**Verification Context** belongs to the **evaluation**. It is **not** part of a **Claim**. It is **not** part of **Evidence**.

---

## Requirements

The key words **MUST**, **MUST NOT**, **MAY**, and **SHOULD** in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

1. **Verification Context** **MUST** remain immutable during evaluation.
2. **Verification Context** **MUST** apply to every **Assertion** in the evaluation.
3. **Verification Context** **MUST NOT** modify **Claim** semantics.
4. **Verification Context** **MUST NOT** modify **Evidence** semantics.
5. **Verification Context** **MAY** carry metadata defined by future RFCs.

---

## Initial Fields

The following fields correspond to existing protocol concepts. This RFC does **not** redefine their semantics — it names where evaluation-wide values live.

| Field | Role |
|-------|------|
| **`edition`** | Specification **edition** under which evaluation interprets rules |
| **`protocol_version`** | Declared **protocol version** for the evaluation |
| **`evaluation_policy`** | **Evaluation Policy** identifier per [VP-RFC-0004](0004-evidence-evaluation-policies.md) (for example **`ALL_REQUIRED`**) |

Implementations **MAY** derive these values from existing specification metadata until explicit context objects are adopted.

---

## Evaluation Composition

```text
Verification Context
 ├── edition
 ├── protocol_version
 └── evaluation_policy
       ↓
     Claim
       ↓
   Assertion
       ↓
 Evidence Set
       ↓
Verification Result
```

**Verification Context** frames the evaluation. **Claim**, **Assertion**, and **Evidence Set** remain distinct inputs defined by prior RFCs.

---

## Future Fields (Informative)

The following fields are reserved for future RFCs. **No additional semantics are defined in this draft.**

| Field | Informative intent |
|-------|-------------------|
| **`evaluation_time`** | Timestamp or logical instant of evaluation |
| **`locale`** | Locale or formatting context for presentation |
| **`extensions`** | Extension identifiers negotiated for the evaluation |
| **`profile`** | Implementation or conformance profile identifier |
| **`issuer_context`** | Issuer-scoped metadata *(semantics deferred)* |
| **`trust_policy`** | Trust policy reference *(semantics deferred)* |

Future RFCs **MUST NOT** imply trust, issuer, or authorization semantics solely from presence of these field names.

---

## Architecture Impact

| Document | Change |
|----------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | **Extension on acceptance** — **Verification Context** entity and evaluation composition diagram |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | **Clarification on acceptance** — every **VP-CS** scenario executes within exactly one **Verification Context** |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Verification Context** | **New protocol concept** — immutable evaluation environment |
| VP-TERM-024 (*Specification Version*) | **Clarifying use** — `edition` / `protocol_version` may be carried in context |
| **Evaluation Policy** | **Clarifying use** — `evaluation_policy` field references policy per **VP-RFC-0004** |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **Implicit context** — scenario executes within one **Verification Context** derived from specification metadata; fixture unchanged |
| **VP-CS-0002** | **Implicit context** — same as **VP-CS-0001** |

**Harness behavior (draft):** **VP-CS** scenarios implicitly execute inside one **Verification Context**. Current fixtures derive context from specification metadata. Future fixtures **MAY** expose **Verification Context** fields explicitly.

No new verification outcomes. No new VP-CS fixtures in this draft.

---

## Security Impact

**Verification Context** introduces **no trust, cryptographic, or authorization semantics**. Fields such as `issuer_context` and `trust_policy` are named only as informative placeholders for future work.

---

## Backwards Compatibility

**Purely additive.** Existing envelopes, rules, scenarios, and **Platform 1.2** pins remain valid. Implementations **MAY** continue deriving evaluation-wide parameters implicitly until explicit context adoption is defined.

---

## Migration Strategy

1. Accept **VP-RFC-0007** when governance approves.
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Register **VP-RFC-0007** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.
4. Future work: fixture schema for explicit context, reference interpreter context object.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0007**; optional fixture context section.
2. **veritypay-reference** — Introduce context type when acceptance path defines it.
3. **veritypay-tooling** — No validator change required beyond registry synchronization.
4. **veritypay-conformance** — Document implicit context derivation; optional explicit context in future fixtures.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Verification Context** normative definition | Complete (this draft) |
| **VP-RFC-0007** registry entry (draft) | Pending |
| **Reference implementation** (context object) | Not started |
| **Conformance execution** (explicit context fixtures) | Not started |

---

## Alternatives Considered

### Alternative A — Embed context in Claim

**Description:** Carry `edition`, `protocol_version`, and `evaluation_policy` only on claim envelopes.

**Why not chosen:** Conflates assertion inputs with evaluation environment; duplicates policy across multi-claim evaluations.

### Alternative B — Embed context in Evidence

**Description:** Attach evaluation-wide parameters to each evidence envelope.

**Why not chosen:** Violates evaluation-wide scope; implies per-envelope policy variance without **VP-RFC-0004** semantics.

### Alternative C — Define trust in this RFC

**Description:** Include issuer and trust policy semantics alongside context fields.

**Why not chosen:** Out of scope; trust belongs in dedicated future RFCs.

---

## Open Questions

1. **Fixture exposure** — When should VP-CS fixtures declare `[verification_context]` explicitly versus implicit derivation?
2. **Edition vs protocol_version** — Should both fields be required when Genesis Edition publishes, or is one derived from the other?
3. **Context registry** — Should **Verification Context** field extensions become machine-readable registry entries?

---

## Acceptance Criteria

- [ ] **Verification Context** is defined without trust, issuer, or authorization semantics
- [ ] Immutability and evaluation-wide scope requirements are stated
- [ ] **Claim** and **Evidence** semantics are explicitly unchanged
- [ ] Initial fields (`edition`, `protocol_version`, `evaluation_policy`) map to existing concepts
- [ ] Future fields are listed informatively without additional semantics
- [ ] Conformance impact documents implicit context for current VP-CS scenarios
- [ ] Compatibility with **VP-RFC-0001** and **VP-RFC-0004** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (accepted)
- [MANIFESTO.md](../docs/00-overview/MANIFESTO.md)
- [VISION.md](../docs/00-overview/VISION.md)
- [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md)
- [GLOSSARY.md](../docs/00-overview/GLOSSARY.md) — VP-TERM-004, VP-TERM-011, VP-TERM-013, VP-TERM-024
- [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md)
- [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)
- [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md)
- [ECOSYSTEM.md](../ECOSYSTEM.md)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-07-03 | Initial draft — Verification Context, initial fields; implementation deferred |

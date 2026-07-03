---
rfc: 0009
id: 0009
concept_id: VP-RFC-0009
title: Verification Context Extensions
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
  - 0007
  - 0008
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
  - 0007-verification-context.md
  - 0008-verification-profiles.md

implementation_status: not_started
last_updated: 2026-07-03
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0009

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0007](0007-verification-context.md) · [VP-RFC-0008](0008-verification-profiles.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0009: Verification Context Extensions

## Summary

This RFC defines how **Verification Context** can be safely extended without changing existing protocol semantics.

It defines the **extension model only**. It does **not** define any standardized extensions, trust policies, issuers, authorization, or new verification outcomes.

Draft [VP-RFC-0007](0007-verification-context.md) introduced **Verification Context**. Draft [VP-RFC-0008](0008-verification-profiles.md) introduced **Verification Profiles**. This RFC introduces **Context Extension** — protocol-defined objects that augment context with additional evaluation information while preserving core fields and downstream semantics.

The change is **additive**. **Platform 1.2** pins remain valid. No standardized extensions exist in this draft.

---

## Motivation

Future protocols may require additional evaluation-wide information such as:

- trust policies
- issuer metadata
- localization
- timestamps
- regulatory context
- domain-specific metadata

These capabilities should **not** become mandatory core **Verification Context** fields. Requiring every evaluation to carry trust, locale, or audit metadata would burden minimal profiles and break backwards compatibility.

Rather than modifying core **Verification Context** for every new capability, Verity introduces **Context Extensions** — optional, protocol-defined augmentations associated with a **Verification Context**.

---

## Problem Statement

[VP-RFC-0007](0007-verification-context.md) names core context fields and lists informative future placeholders. It does not define how optional evaluation metadata is attached, identified, ignored, or required by profiles.

Without an **extension model**:

- Every new capability pressures core context schema changes.
- Implementations cannot safely ignore unknown evaluation metadata.
- **Verification Profiles** cannot declare which extensions are required without ad hoc conventions.

---

## Goals

- Define **Context Extension** as protocol vocabulary.
- Require stable extension identifiers and immutability during evaluation.
- Preserve **Claim**, **Evidence**, and **Assertion Evaluator** dispatch semantics.
- Specify unknown-extension behavior (ignore unless required by active profile).
- Document informative future extension categories without defining them.
- State that no standardized extensions exist in this draft.

## Non-Goals

- Defining any standardized **Context Extension** payload or semantics.
- Trust policies, issuer identity, authorization, credentials, blockchain, or legal semantics.
- New **VP-RULE** text or verification outcome vocabulary.
- Wire encodings, fixture schema changes, or reference interpreter behavior.
- Modifying core **Verification Context** field requirements from **VP-RFC-0007**.

---

## Proposal

### Context Extension

**Definition:** A protocol-defined object associated with a **Verification Context** that supplies additional evaluation information without changing existing protocol semantics.

**Context Extensions** augment **Verification Context**. They **MUST NOT** replace core context fields (`edition`, `protocol_version`, `evaluation_policy`, or profile resolution per **VP-RFC-0008**).

### Requirements

The key words **MUST**, **MUST NOT**, **MAY**, and **SHOULD** in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

1. **Context Extensions** **MUST** have stable **extension identifiers**.
2. **Context Extensions** **MUST NOT** alter **Claim** semantics.
3. **Context Extensions** **MUST NOT** alter **Evidence** semantics.
4. **Context Extensions** **MUST NOT** bypass **Assertion Evaluator** dispatch per [VP-RFC-0006](0006-assertion-evaluation-dispatch.md).
5. Unknown extensions **MUST** be ignored unless explicitly required by the active **Verification Profile**.
6. **Context Extensions** **MUST** remain immutable during evaluation.

### Context composition

```text
Verification Context
 ├── profile              (via VP-RFC-0008)
 ├── edition
 ├── protocol_version
 ├── evaluation_policy
 └── context_extensions[]
       ↓
     Evaluation
       ↓
     Claim → Assertion → Evidence Set → Verification Result
```

Extensions attach to **Verification Context** only. They do not embed in **Claim** or **Evidence** envelopes.

### Initial state

**No standardized extensions exist** in this draft. Implementations **MAY** encounter extension identifiers only when future RFCs or scenarios define them.

### Future compatibility (informative)

Future RFCs **MAY** define extensions such as:

| Informative name | Illustrative purpose |
|------------------|----------------------|
| **Time Context** | Evaluation timestamps or logical time bounds |
| **Trust Context** | Trust policy references *(semantics deferred)* |
| **Issuer Context** | Issuer-scoped metadata *(semantics deferred)* |
| **Localization Context** | Locale or presentation context |
| **Audit Context** | Audit trail or attestation metadata |
| **Regulatory Context** | Regulatory framing *(semantics deferred)* |

No semantics for these categories are defined here. Future RFCs **MUST** define extension identifiers, payloads, and profile requirements independently.

---

## Architecture Impact

| Document | Change |
|----------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | **Extension on acceptance** — **Context Extension** and augmented **Verification Context** composition |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | **Clarification on acceptance** — future scenarios **MAY** reference extensions; unknown extensions ignored unless profile requires them |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Context Extension** | **New protocol concept** — optional augmentation of **Verification Context** |
| **Verification Context** | **Clarifying use** — may carry zero or more **Context Extensions** without replacing core fields |
| **Verification Profile** | **Clarifying use** — future profiles **MAY** require specific extensions; until then extensions are optional |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **No extensions** — executes without standardized extensions; fixture unchanged |
| **VP-CS-0002** | **No extensions** — same as **VP-CS-0001** |

**Harness behavior (draft):** Future **VP-CS** scenarios **MAY** reference **Context Extensions** in later editions. The current platform defines **no standardized extensions**. Implementations **MUST** ignore unknown extensions unless the active **Verification Profile** explicitly requires them.

No new verification outcomes. No new VP-CS fixtures in this draft.

---

## Security Impact

This RFC defines an **extension attachment model only**. It introduces **no trust, cryptographic, credential, or authorization semantics**. Threat modeling for specific extensions belongs in their defining RFCs.

---

## Backwards Compatibility

**Purely additive.** Core **Verification Context** fields, existing profiles, envelopes, rules, and **Platform 1.2** pins remain valid. Evaluations without extensions behave as before.

---

## Migration Strategy

1. Accept **VP-RFC-0009** when governance approves (with or after **VP-RFC-0007** / **VP-RFC-0008** acceptance).
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Register **VP-RFC-0009** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.
4. Future work: extension registry, profile-required extension declarations, fixture schema.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0009**; future extension-defining RFCs.
2. **veritypay-reference** — Attach extension objects to context when acceptance path defines them.
3. **veritypay-tooling** — No validator change required beyond registry synchronization unless extension registry is introduced.
4. **veritypay-conformance** — Document ignore-unless-required behavior; optional extension fields in future fixtures.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Context Extension** extension model | Complete (this draft) |
| **VP-RFC-0009** registry entry (draft) | Pending |
| **Standardized extensions** | None — deferred to future RFCs |
| **Reference implementation** (extension handling) | Not started |
| **Conformance execution** (extension-aware fixtures) | Not started |

---

## Alternatives Considered

### Alternative A — Add optional fields directly to Verification Context

**Description:** Extend core context with `trust_policy`, `locale`, and similar fields as optional keys.

**Why not chosen:** Encourages unbounded core schema growth; complicates minimal profiles and version negotiation.

### Alternative B — Embed extensions in Claim or Evidence

**Description:** Carry evaluation-wide metadata on claim or evidence envelopes.

**Why not chosen:** Violates evaluation-wide scope; conflates inputs under test with evaluation environment.

### Alternative C — Fail on unknown extensions

**Description:** Require implementations to reject evaluations with unrecognized extension identifiers.

**Why not chosen:** Breaks forward compatibility; ignore-unless-required by profile preserves extensibility.

---

## Open Questions

1. **Extension registry** — Should **Context Extension** identifiers become machine-readable registry entries?
2. **Profile binding** — How should **Verification Profiles** declare required versus optional extensions?
3. **Indeterminate vs ignore** — When a profile requires an unknown extension, should the outcome be `indeterminate` or a harness error?

---

## Acceptance Criteria

- [ ] **Context Extension** is defined without defining any standardized extension payloads
- [ ] Stable extension identifiers and immutability requirements are stated
- [ ] **Claim**, **Evidence**, and evaluator dispatch semantics are explicitly unchanged
- [ ] Unknown extensions are ignored unless required by the active **Verification Profile**
- [ ] No standardized extensions exist in this draft
- [ ] Informative future extension categories are documented without additional semantics
- [ ] Compatibility with **VP-RFC-0007** and **VP-RFC-0008** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) — Assertion Evaluation Dispatch (draft)
- [VP-RFC-0007](0007-verification-context.md) — Verification Context (draft)
- [VP-RFC-0008](0008-verification-profiles.md) — Verification Profiles (draft)
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
| 0.1.0 | 2026-07-03 | Initial draft — Context Extension model; no standardized extensions |

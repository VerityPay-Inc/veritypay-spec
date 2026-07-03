---
rfc: 0010
id: 0010
concept_id: VP-RFC-0010
title: Protocol Capability Negotiation
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
  - 0002
  - 0003
  - 0004
  - 0005
  - 0006
  - 0007
  - 0008
  - 0009
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
  - 0002-claim-identity-binding.md
  - 0003-multiple-evidence.md
  - 0004-evidence-evaluation-policies.md
  - 0005-assertion-types.md
  - 0006-assertion-evaluation-dispatch.md
  - 0007-verification-context.md
  - 0008-verification-profiles.md
  - 0009-verification-context-extensions.md

implementation_status: not_started
last_updated: 2026-07-03
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0010

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) through [VP-RFC-0009](0009-verification-context-extensions.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0010: Protocol Capability Negotiation

## Summary

This RFC defines how implementations declare supported **protocol capabilities** — stable identifiers representing intentional support for defined protocol features.

It defines **capabilities only**. It does **not** define networking, transport feature discovery, wire negotiation handshakes, or new verification outcomes.

**Platform releases** and independent implementations evolve at different rates. Conformance needs a vocabulary for which features an implementation **chooses** to support so scenarios can be **eligible**, **executed**, or **skipped** — not misclassified as failures when a capability is simply not implemented yet.

The change is **purely additive**. **Platform 1.2** pins remain valid. No implementation behavior is defined in this draft.

---

## Motivation

Platform releases evolve.

Independent implementations evolve.

Conformance must understand which capabilities an implementation **intentionally supports** — not merely which scenarios happen to pass or fail today.

Without **protocol capabilities**:

- A partial implementation appears "non-conforming" when it lacks features it never claimed to support.
- VP-CS scenarios cannot declare prerequisites independently of claim and evidence fixtures.
- Ecosystem growth is penalized: every new scenario reads as **fail** instead of **skip** when the adapter has not adopted the feature yet.

**Protocol Capability Negotiation** supplies stable capability identifiers and conformance eligibility rules. It is **not** a network protocol.

---

## Problem Statement

Accepted and draft RFCs define protocol features across claims, evidence, evaluation, context, and profiles. Nothing normatively names those features as **declarable capabilities** or binds them to conformance eligibility.

Without capability vocabulary:

- Harnesses cannot distinguish "wrong outcome" from "feature not implemented."
- Implementations cannot advertise supported feature sets comparably.
- Future VP-CS fixtures cannot express required capabilities.

---

## Goals

- Define **Capability** as protocol vocabulary.
- Require stable, additive capability identifiers.
- Catalog initial standardized capabilities mapped to existing RFC features.
- Enable conformance eligibility: **skip** when required capabilities are absent; **execute** when present.
- Preserve existing protocol semantics — capabilities **MUST NOT** redefine them.

## Non-Goals

- Networking, transport, or runtime feature-discovery protocols.
- Handshake messages, API endpoints, or serialization formats.
- New **VP-RULE** text or verification outcome vocabulary.
- Mandatory capability advertisement for all implementations in this draft.
- Fixture schema changes or reference interpreter behavior.

---

## Proposal

### Capability

**Definition:** A stable protocol identifier representing one protocol feature.

A **Capability** names intentional support for a defined slice of the specification. It is an **implementation concept** — not part of **Claim**, **Evidence**, or **Verification Context**.

### Requirements

The key words **MUST**, **MUST NOT**, **MAY**, and **SHOULD** in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

1. **Capabilities** **MUST** have stable identifiers.
2. **Capabilities** **MUST** be additive — new identifiers **MUST NOT** alter semantics of existing capabilities.
3. Unknown capabilities **MUST** be ignored.
4. **Capabilities** **MUST NOT** redefine existing protocol semantics.

### Capability declaration (informative)

Implementations **MAY** advertise a set of supported capability identifiers. This RFC does not define advertisement encoding, storage, or transport. Declaration is a conformance and integrator-facing concept until a future RFC binds wire formats.

### Initial standardized capabilities

| Capability identifier | Protocol feature | Defining RFC |
|----------------------|------------------|--------------|
| **`minimal_claims`** | Minimal claim and evidence envelopes, **VP-RULE-0001** | [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) (accepted) |
| **`claim_binding`** | Evidence claim identity binding, **VP-RULE-0002** | [VP-RFC-0002](0002-claim-identity-binding.md) (accepted) |
| **`multiple_evidence`** | **Evidence Set** input model | [VP-RFC-0003](0003-multiple-evidence.md) (accepted) |
| **`evaluation_policy`** | **Evaluation Policy** aggregation | [VP-RFC-0004](0004-evidence-evaluation-policies.md) (accepted) |
| **`assertion_types`** | **Assertion Type** taxonomy | [VP-RFC-0005](0005-assertion-types.md) (draft) |
| **`assertion_dispatch`** | **Evaluation Dispatch** | [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) (draft) |
| **`verification_context`** | **Verification Context** | [VP-RFC-0007](0007-verification-context.md) (draft) |
| **`verification_profiles`** | **Verification Profile** | [VP-RFC-0008](0008-verification-profiles.md) (draft) |
| **`context_extensions`** | **Context Extension** model | [VP-RFC-0009](0009-verification-context-extensions.md) (draft) |

Future RFCs **MAY** define additional capability identifiers. Each new capability **MUST** map to normative protocol text elsewhere — capabilities do not define behavior by themselves.

### Conformance eligibility (normative intent)

```text
VP-CS scenario
      ↓
Required Capabilities (declared by scenario — future)
      ↓
Implementation Capabilities (declared by adapter — optional)
      ↓
Scenario eligible?
      ├── yes → execute → pass / fail (outcome comparison)
      └── no  → skip (capability not implemented)
```

When a VP-CS scenario declares required capabilities and an implementation does not advertise support for every required capability, the harness **SHOULD** yield **`skip`** with reason *capability not implemented* — **not** **`fail`**.

**`skip`** means the scenario was not applicable to the declared implementation surface. **`fail`** means the scenario executed and outcomes did not match the oracle.

Current **VP-CS-0001** and **VP-CS-0002** fixtures do not declare required capabilities. Eligibility rules apply when future fixtures or harness profiles adopt **VP-RFC-0010**.

---

## Architecture Impact

| Document | Change |
|----------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | **Extension on acceptance** — **Protocol Capability** as implementation concept |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | **Clarification on acceptance** — capability-based scenario eligibility and **`skip`** semantics |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Capability** / **Protocol Capability** | **New protocol concept** — stable feature identifier for intentional implementation support |
| **Required Capabilities** | **New conformance concept** — capabilities a VP-CS scenario may require |
| **Implementation Capabilities** | **New conformance concept** — capabilities an adapter advertises as supported |
| Harness **`skip`** | **Clarifying use** — eligible skip when required capability absent; distinct from **`fail`** |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **Implicit capabilities** — exercises **`minimal_claims`** semantics; fixture unchanged |
| **VP-CS-0002** | **Implicit capabilities** — exercises **`minimal_claims`** and **`claim_binding`**; fixture unchanged |

**Harness behavior (draft):**

- Implementations **MAY** advertise supported capabilities.
- VP-CS scenarios **MAY** declare required capabilities in future editions.
- When required capabilities are absent, harness **SHOULD** **`skip`** — not **`fail`** — with reason *capability not implemented*.
- When all required capabilities are present, existing pass/fail outcome comparison applies unchanged.

No new verification outcomes. No new VP-CS fixtures in this draft.

---

## Security Impact

**Capabilities** are declarative labels. They introduce **no trust, cryptographic, or authorization semantics**. Mis-declared capabilities are a conformance honesty problem, not a protocol security mechanism defined here.

---

## Backwards Compatibility

**Purely additive.** Existing envelopes, rules, scenarios, and **Platform 1.2** pins remain valid. Harnesses **MAY** ignore capability eligibility until adopted.

---

## Migration Strategy

1. Accept **VP-RFC-0010** when governance approves.
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Register **VP-RFC-0010** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.
4. Future work: capability registry, fixture `required_capabilities` field, harness skip logic in `veritypay-conformance`.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0010**; optional capability registry.
2. **veritypay-reference** — Advertise supported capabilities when acceptance path defines it.
3. **veritypay-tooling** — No validator change required beyond registry synchronization unless capability registry is introduced.
4. **veritypay-conformance** — Eligibility check and **`skip`** when required capabilities absent.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Capability** vocabulary and initial identifier catalog | Complete (this draft) |
| **VP-RFC-0010** registry entry (draft) | Pending |
| **Conformance eligibility** / **`skip`** harness behavior | Not started |
| **Fixture `required_capabilities`** | Not started |

---

## Alternatives Considered

### Alternative A — Infer capabilities from Platform release tags only

**Description:** Bind capabilities solely to Platform release declarations without stable identifiers.

**Why not chosen:** Independent implementations may support partial feature sets within a release; stable identifiers are required for scenario prerequisites.

### Alternative B — Fail when capabilities absent

**Description:** Treat missing capabilities as harness **fail**.

**Why not chosen:** Penalizes partial implementations and confuses "not implemented" with "incorrect behavior."

### Alternative C — Network capability negotiation handshake

**Description:** Define wire-level feature discovery in this RFC.

**Why not chosen:** Out of scope; this RFC defines protocol vocabulary and conformance eligibility only.

---

## Open Questions

1. **Capability registry** — Should capabilities become machine-readable registry entries separate from RFC text?
2. **Fixture defaults** — Should **VP-CS-0001** implicitly require only **`minimal_claims`**, or also draft capabilities once reference implements them?
3. **Partial capability** — Can an implementation declare a capability with documented limitations, or only all-or-nothing support?

---

## Acceptance Criteria

- [ ] **Capability** is defined without networking or feature-discovery protocol semantics
- [ ] Stable, additive identifiers and ignore-unknown rules are stated
- [ ] Initial capability catalog maps to **VP-RFC-0001** through **VP-RFC-0009** features
- [ ] Capabilities **MUST NOT** redefine existing protocol semantics
- [ ] Conformance eligibility and **`skip`**-when-absent behavior are documented
- [ ] **Claim**, **Evidence**, and **Verification Context** are explicitly not capability carriers
- [ ] Compatibility with **Platform 1.2** scenarios is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0003](0003-multiple-evidence.md) — Multiple Evidence (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (accepted)
- [VP-RFC-0005](0005-assertion-types.md) — Assertion Types (draft)
- [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) — Assertion Evaluation Dispatch (draft)
- [VP-RFC-0007](0007-verification-context.md) — Verification Context (draft)
- [VP-RFC-0008](0008-verification-profiles.md) — Verification Profiles (draft)
- [VP-RFC-0009](0009-verification-context-extensions.md) — Verification Context Extensions (draft)
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
| 0.1.0 | 2026-07-03 | Initial draft — Capability vocabulary, initial catalog, conformance eligibility; implementation deferred |

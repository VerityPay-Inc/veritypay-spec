---
rfc: 0008
id: 0008
concept_id: VP-RFC-0008
title: Verification Profiles
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
  - 0003
  - 0004
  - 0006
  - 0007
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
  - 0003-multiple-evidence.md
  - 0004-evidence-evaluation-policies.md
  - 0006-assertion-evaluation-dispatch.md
  - 0007-verification-context.md

implementation_status: not_started
last_updated: 2026-07-03
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0008

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0003](0003-multiple-evidence.md) · [VP-RFC-0004](0004-evidence-evaluation-policies.md) · [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) · [VP-RFC-0007](0007-verification-context.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0008: Verification Profiles

## Summary

This RFC defines **Verification Profiles** — named, reusable configurations of **Verification Context** fields for a class of evaluations.

Draft [VP-RFC-0007](0007-verification-context.md) introduced **Verification Context** as the immutable evaluation environment. This RFC names common context configurations so implementations and conformance scenarios can declare them without repeating individual context fields.

This RFC does **not** define trust policies, issuers, authorization, credentials, blockchain behavior, or legal semantics. It standardizes one initial profile — **`minimal_all_required`** — and defers all others.

The change is **additive** relative to draft **VP-RFC-0007** and accepted **VP-RFC-0003**, **VP-RFC-0004**, and draft **VP-RFC-0006**. **Platform 1.2** pins remain valid.

---

## Motivation

**Verification Context** fields (`edition`, `protocol_version`, `evaluation_policy`, and future extensions) describe *how* an evaluation is framed. In practice, the same configuration recurs across scenarios, releases, and integrator deployments.

Without named profiles:

- Every scenario and implementation repeats the same context field bundle.
- Conformance cannot compare declared evaluation configuration independently of claim inputs.
- Platform releases lack a stable shorthand for "run evaluation under this context configuration."

**Verification Profiles** provide a protocol-level name for a reusable **Verification Context** configuration.

---

## Problem Statement

[VP-RFC-0007](0007-verification-context.md) names the evaluation environment but does not define how common configurations are identified, compared, or reused.

Without **Verification Profiles**:

- Context fields remain implicit in harness metadata and specification pins.
- Unknown evaluation configurations have no protocol-level outcome.
- Future profiles cannot be introduced without ad hoc string conventions.

---

## Goals

- Define **Verification Profile** as protocol vocabulary.
- Require stable `profile_id` identifiers and `evaluation_policy` binding.
- Preserve **Claim**, **Evidence**, and **Assertion Evaluator** dispatch semantics unchanged.
- Standardize **`minimal_all_required`** as the initial profile.
- Specify unknown-profile behavior (`indeterminate` unless explicitly supported).

## Non-Goals

- Trust policies, issuer identity, authorization, or credential semantics.
- Blockchain, settlement, or legal interpretation.
- New **VP-RULE** text or verification outcome vocabulary.
- Wire encodings, fixture schema changes, or reference interpreter behavior.
- Standardizing profiles beyond **`minimal_all_required`** in this draft.

---

## Proposal

### Verification Profile

**Definition:** A named, reusable configuration of **Verification Context** fields for a class of evaluations.

A **Verification Profile** **MUST** map to exactly one **Verification Context** configuration for a given evaluation. Selecting a profile **MUST** resolve context fields; it **MUST NOT** substitute for claim, assertion, or evidence inputs.

### Requirements

The key words **MUST**, **MUST NOT**, **MAY**, and **SHOULD** in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

1. A **Verification Profile** **MUST** have a stable **`profile_id`**.
2. A **Verification Profile** **MUST** define or imply an **`evaluation_policy`**.
3. A **Verification Profile** **MUST NOT** alter **Claim** semantics.
4. A **Verification Profile** **MUST NOT** alter **Evidence** semantics.
5. A **Verification Profile** **MUST NOT** bypass **Assertion Evaluator** dispatch per [VP-RFC-0006](0006-assertion-evaluation-dispatch.md).
6. Unknown **`profile_id`** values **MUST** produce `indeterminate` unless a scenario or implementation explicitly declares support for that profile.

### Profile resolution

```text
profile_id
      ↓
Verification Profile
      ↓
Verification Context
      ↓
Claim → Assertion → Evidence Set → Verification Result
```

Profile selection resolves **Verification Context** only. **Assertion Type** dispatch, **Evidence Set** composition, and **Evaluation Policy** aggregation remain governed by their defining RFCs.

### Initial standardized profile: `minimal_all_required`

| Property | Value |
|----------|-------|
| **`profile_id`** | **`minimal_all_required`** |
| **`evaluation_policy`** | **`ALL_REQUIRED`** per [VP-RFC-0004](0004-evidence-evaluation-policies.md) |
| **Assertion dispatch** | Per [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) — `assertion_type` selects **Assertion Evaluator** before protocol rules execute |
| **Evidence Set** | Per [VP-RFC-0003](0003-multiple-evidence.md) — unordered collection of **Evidence** envelopes; ordering independence |

**`minimal_all_required`** names the context configuration exercised implicitly by **VP-CS-0001** and **VP-CS-0002** under **Platform 1.2**. No additional profiles are standardized in this draft.

---

## Architecture Impact

| Document | Change |
|----------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | **Extension on acceptance** — **Verification Profile** and profile-to-context resolution |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | **Clarification on acceptance** — scenarios **MAY** declare `profile_id`; current fixtures implicitly use **`minimal_all_required`** |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Verification Profile** | **New protocol concept** — named **Verification Context** configuration |
| **Verification Context** | **Clarifying use** — profiles resolve to context; context remains the evaluation environment object |
| **`minimal_all_required`** | **New standardized profile identifier** — **`ALL_REQUIRED`** policy with Platform 1.2 dispatch and evidence-set semantics |
| **Evaluation Policy** | **Clarifying use** — every profile **MUST** define or imply `evaluation_policy` |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **Implicit profile** — executes under **`minimal_all_required`**; fixture unchanged |
| **VP-CS-0002** | **Implicit profile** — same as **VP-CS-0001** |

**Harness behavior (draft):** VP-CS scenarios **MAY** declare **`profile_id`**. Current **VP-CS-0001** and **VP-CS-0002** fixtures implicitly use **`minimal_all_required`**. Future fixtures **MAY** make `profile_id` explicit.

Unknown **`profile_id`** values **MUST** yield `indeterminate` unless the scenario or implementation explicitly declares support. No new verification outcomes. No new VP-CS fixtures in this draft.

---

## Security Impact

**Verification Profiles** introduce **no trust, cryptographic, credential, or authorization semantics**. They name evaluation configuration only. Threat modeling for future profiles belongs in their defining RFCs.

---

## Backwards Compatibility

**Additive.** Existing envelopes, rules, scenarios, and **Platform 1.2** pins remain valid. Implementations **MAY** continue operating without explicit `profile_id` until adoption paths define it.

---

## Migration Strategy

1. Accept **VP-RFC-0008** when governance approves (with or after **VP-RFC-0007** acceptance).
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Register **VP-RFC-0008** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.
4. Future work: fixture `profile_id` field, reference interpreter profile resolution.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0008**; optional fixture profile field.
2. **veritypay-reference** — Resolve profiles to **Verification Context** when acceptance path defines it.
3. **veritypay-tooling** — No validator change required beyond registry synchronization unless profile registry is introduced.
4. **veritypay-conformance** — Document implicit **`minimal_all_required`**; optional explicit `profile_id` in future fixtures.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Verification Profile** / **`minimal_all_required`** normative text | Complete (this draft) |
| **VP-RFC-0008** registry entry (draft) | Pending |
| **Reference implementation** (profile resolution) | Not started |
| **Conformance execution** (explicit `profile_id` fixtures) | Not started |

---

## Alternatives Considered

### Alternative A — Encode profiles only in conformance harness metadata

**Description:** Keep profile names as harness-local strings without protocol vocabulary.

**Why not chosen:** Prevents independent implementations from declaring the same evaluation configuration interoperably.

### Alternative B — Merge profiles into Verification Context as a required field

**Description:** Require every context to carry `profile_id` and forbid unnamed contexts.

**Why not chosen:** Breaks implicit context derivation for existing **VP-CS** fixtures; profiles are optional naming over context.

### Alternative C — Define multiple profiles in this RFC

**Description:** Standardize several profiles (for example single-evidence and multi-evidence variants) in one document.

**Why not chosen:** **`minimal_all_required`** already covers current Platform 1.2 semantics; additional profiles need separate motivation.

---

## Open Questions

1. **Fixture exposure** — When should VP-CS fixtures require explicit `profile_id` versus implicit **`minimal_all_required`**?
2. **Profile registry** — Should **Verification Profiles** become machine-readable registry entries separate from RFC text?
3. **Edition binding** — Should **`minimal_all_required`** normatively pin `edition` and `protocol_version`, or leave them to scenario metadata?

---

## Acceptance Criteria

- [ ] **Verification Profile** is defined without trust, issuer, authorization, credential, blockchain, or legal semantics
- [ ] Stable `profile_id` and `evaluation_policy` requirements are stated
- [ ] **Claim**, **Evidence**, and evaluator dispatch semantics are explicitly unchanged
- [ ] Unknown `profile_id` yields `indeterminate` unless explicitly supported
- [ ] **`minimal_all_required`** mapping to **`ALL_REQUIRED`**, **VP-RFC-0006** dispatch, and **VP-RFC-0003**/**VP-RFC-0004** evidence behavior is complete
- [ ] No additional profiles are standardized in this draft
- [ ] Compatibility with **VP-RFC-0007** and Platform 1.2 scenarios is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0003](0003-multiple-evidence.md) — Multiple Evidence (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (accepted)
- [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) — Assertion Evaluation Dispatch (draft)
- [VP-RFC-0007](0007-verification-context.md) — Verification Context (draft)
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
| 0.1.0 | 2026-07-03 | Initial draft — Verification Profile, `minimal_all_required`; implementation deferred |

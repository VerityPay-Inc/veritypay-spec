---
rfc: 0004
id: 0004
concept_id: VP-RFC-0004
title: Evidence Evaluation Policies
status: draft
version: 0.1.0
type: protocol
category: Protocol
pyramid_level: specification

authors:
  - VerityPay Core Team

reviewers: []

created: 2026-06-29
updated: 2026-06-29

depends_on:
  - 0000
  - 0001
  - 0002
  - 0003
supersedes: []
superseded_by: null

related_terms:
  - VP-TERM-004
  - VP-TERM-008
  - VP-TERM-011
  - VP-TERM-013
  - VP-TERM-024

related_architecture:
  - ../docs/01-architecture/DATA_MODEL.md
  - ../docs/03-development/CONFORMANCE_MODEL.md

related_conformance:
  - VP-CS-0004

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

implementation_status: not_started
last_updated: 2026-06-29
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0004

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [VP-RFC-0002](0002-claim-identity-binding.md) · [VP-RFC-0003](0003-multiple-evidence.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0004: Evidence Evaluation Policies

## Summary

This RFC defines **how an Evidence Set produces a verification decision**.

It introduces **Evaluation Policy** — the protocol-defined strategy used to derive a single verification outcome from per-evidence rule results over an [Evidence Set](0003-multiple-evidence.md).

This draft defines one normative policy identifier: **`ALL_REQUIRED`**. Future RFCs **MAY** add additional policies.

The change is **additive**. It does **not** introduce trust, issuer reputation, weighting, confidence scores, signatures, or authorization. Implementation in reference and conformance repositories is **deferred**.

---

## Motivation

[VP-RFC-0003](0003-multiple-evidence.md) introduced **Evidence Set** — multiple independent **Evidence** envelopes associated with one **Claim** — and intentionally **deferred** how per-envelope results combine into one verification outcome.

Without a named evaluation policy:

- Implementations cannot agree on multi-evidence oracle expectations.
- Conformance scenarios cannot declare aggregation semantics.
- Reference interpreters must embed ad hoc combination logic.

The specification needs **deterministic, protocol-level aggregation rules** before multi-evidence fixtures carry normative expected outcomes.

---

## Problem Statement

Given a **Claim**, an **Evidence Set**, and per-envelope verification outcomes from rules in scope (for example **VP-RULE-0002** and **VP-RULE-0001**), evaluators must map many envelope-level results to **exactly one** of `satisfied`, `not_satisfied`, or `indeterminate` per [VP-TERM-011](https://github.com/VerityPay-Inc/veritypay-spec/blob/main/docs/00-overview/GLOSSARY.md#verification-outcome).

That mapping is an **evaluation policy** problem, distinct from envelope shape ([VP-RFC-0001](0001-minimal-claim-evidence-semantics.md)), binding ([VP-RFC-0002](0002-claim-identity-binding.md)), or set membership ([VP-RFC-0003](0003-multiple-evidence.md)).

---

## Goals

- Define **Evaluation Policy** as protocol vocabulary.
- Specify the **`ALL_REQUIRED`** policy with a deterministic outcome table.
- Require policy evaluation to be independent of evidence ordering.
- Define **VP-CS-0004** as a conformance scenario profile for **`ALL_REQUIRED`** (fixture publication deferred).
- Enable downstream work: DATA_MODEL alignment, reference interpreter aggregation, conformance fixture schema.

---

## Non-Goals

- Trust, issuer reputation, evidence weighting, confidence scores, signatures, or authorization.
- New verification outcome labels beyond `satisfied`, `not_satisfied`, and `indeterminate`.
- Policies other than **`ALL_REQUIRED`** in this draft (future RFCs **MAY** add them).
- Machine-readable **VP-CS-0004** fixture publication in this draft.
- Reference or conformance implementation (deferred).
- Amending per-envelope rule text in **VP-RULE-0001** or **VP-RULE-0002**.

---

## Proposal

### 1. Evaluation Policy

| Property | Value |
|----------|--------|
| **Term** | **Evaluation Policy** |
| **Definition** | The protocol-defined strategy used to derive a **verification outcome** from an **Evidence Set** and the per-envelope outcomes produced by verification rules in scope. |

An evaluation **MUST** declare which policy applies when aggregating an **Evidence Set**. When exactly one evidence envelope is present, **`ALL_REQUIRED`** **MUST** yield the same outcome as evaluating that envelope alone under the same rules—preserving **VP-CS-0001** semantics.

Policies **MUST** be **deterministic**: identical claim, evidence set (as a set), rules in scope, and per-envelope outcomes **MUST** yield the same aggregated verification outcome.

Evidence ordering **MUST NOT** affect the aggregated verification outcome.

### 2. Applicable evidence

For policy evaluation, **applicable evidence** means each **Evidence** envelope in the **Evidence Set** that has been evaluated under the verification rules in scope for that evaluation, producing a per-envelope outcome of `satisfied`, `not_satisfied`, or `indeterminate`.

This RFC does **not** redefine per-envelope rule procedures. Binding failure, content mismatch, and other cases continue to map per envelope per accepted rule RFCs before the evaluation policy runs.

### 3. Policy — `ALL_REQUIRED`

| Property | Value |
|----------|--------|
| **Policy ID** | `ALL_REQUIRED` |
| **Name** | All required |
| **Meaning** | Every applicable evidence envelope **MUST** satisfy its verification rules for the aggregate outcome to be `satisfied`. |

**Normative outcome table:**

| Condition | Aggregated verification outcome |
|-----------|--------------------------------|
| The **Evidence Set** is empty (zero evidence envelopes) | `indeterminate` |
| Every applicable evidence envelope has per-envelope outcome `satisfied` | `satisfied` |
| Any applicable evidence envelope has per-envelope outcome `not_satisfied` | `not_satisfied` |
| One or more applicable evidence envelopes have per-envelope outcome `indeterminate`, and **no** applicable envelope has `not_satisfied` | `indeterminate` |

**Precedence (informative):** Evaluators **SHOULD** apply the rows above in order—`not_satisfied` from any envelope dominates; otherwise `indeterminate` from any envelope dominates when no `not_satisfied` exists; otherwise all `satisfied` yields `satisfied`.

### 4. Informative examples (`ALL_REQUIRED`)

**One claim, two evidence envelopes — both satisfied:**

| Evidence | Per-envelope outcome |
|----------|----------------------|
| Evidence A | `satisfied` |
| Evidence B | `satisfied` |

**Aggregated outcome:** `satisfied`

**One claim, two evidence envelopes — one not satisfied:**

| Evidence | Per-envelope outcome |
|----------|----------------------|
| Evidence A | `satisfied` |
| Evidence B | `not_satisfied` |

**Aggregated outcome:** `not_satisfied`

**One claim, two evidence envelopes — one indeterminate:**

| Evidence | Per-envelope outcome |
|----------|----------------------|
| Evidence A | `satisfied` |
| Evidence B | `indeterminate` |

**Aggregated outcome:** `indeterminate`

**One claim, empty Evidence Set:**

**Aggregated outcome:** `indeterminate`

### 5. Future policies

Additional evaluation policy identifiers **MAY** be defined in future RFCs (for example `ANY_SUFFICIENT`). Each policy **MUST** define its own deterministic outcome table. This draft defines **`ALL_REQUIRED`** only.

### 6. VP-CS-0004

| Property | Value |
|----------|--------|
| **Scenario ID** | `VP-CS-0004` |
| **Name** | All required policy aggregates multi-evidence outcomes |
| **Evaluation policy** | `ALL_REQUIRED` |
| **Rule under test** | Evaluation policy aggregation (per-envelope rules per scenario declaration) |

**Intent (normative profile, fixture deferred):**

- One **Claim** and an **Evidence Set** with two or more bound evidence envelopes.
- Per-envelope outcomes declared or derived per rules in scope.
- Expected aggregated verification outcome per **`ALL_REQUIRED`** outcome table in §3.

**Fixture publication:** deferred until **VP-RFC-0003** multi-evidence fixture schema and reference oracle aggregation exist.

**Informative note:** [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) contains an earlier narrative catalog entry also labeled **VP-CS-0004** (*Identity immutability*). Reconcile executable profile IDs with long-term narrative catalog IDs before fixture publication.

### 7. Compatibility

This RFC is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md), [VP-RFC-0002](0002-claim-identity-binding.md), and draft [VP-RFC-0003](0003-multiple-evidence.md).

| Artifact | Impact |
|----------|--------|
| **VP-CS-0001** | Unchanged when **Evidence Set** has one envelope and policy is **`ALL_REQUIRED`** |
| **VP-CS-0002** | Unchanged — single envelope binding failure |
| **VP-RULE-0001** / **VP-RULE-0002** | Unchanged — per-envelope semantics |
| **Platform 1.1** | Unaffected until **VP-RFC-0004** is accepted and engineering repos opt in |

Implementations that do not claim **VP-RFC-0003** or **VP-RFC-0004** **MAY** continue single-evidence evaluation without declaring an evaluation policy.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Evaluation Policy | **Extension on acceptance** — aggregation layer between Evidence Set and Verification Result |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | Scenario policy metadata | **Clarification on acceptance** — fixtures **MAY** declare `evaluation_policy` |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** in this draft |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** in this draft |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Evaluation Policy** | **New protocol concept** — strategy for deriving one verification outcome from an Evidence Set |
| **`ALL_REQUIRED`** | **New policy identifier** — every applicable envelope must be `satisfied` for aggregate `satisfied` |
| VP-TERM-011 (*Verification Outcome*) | **No vocabulary change** — policies compose existing outcomes only |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0004** | **Defined profile** — **`ALL_REQUIRED`** multi-evidence aggregation; fixture deferred |

Harnesses **MUST NOT** infer **`ALL_REQUIRED`** outcomes from [VP-RFC-0003](0003-multiple-evidence.md) alone. Claiming **VP-RFC-0004** **SHOULD** imply **VP-RFC-0003** support.

---

## Security Impact

Evaluation policies perform **logical aggregation only**. They do **not**:

- authenticate evidence sources
- weight evidence by issuer trust
- detect conflicting evidence beyond outcome labels already defined

Threat modeling for trust and reputation belongs in future RFCs.

---

## Backwards Compatibility

**Additive.** Single-evidence evaluation with implicit **`ALL_REQUIRED`** semantics remains compatible with **VP-CS-0001**.

---

## Migration Strategy

1. Accept **VP-RFC-0004**.
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Extend reference interpreter to aggregate per-envelope outcomes under a declared policy (future engineering work).
4. Publish **VP-CS-0004** fixture when multi-evidence schema and oracle support exist.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0004**; publish **VP-CS-0004** fixture when schema approved.
2. **veritypay-reference** — Apply **`ALL_REQUIRED`** after per-envelope rule evaluation over an Evidence Set.
3. **veritypay-tooling** — No validator change required beyond existing corpus checks unless fixture schema adds `evaluation_policy`.
4. **veritypay-conformance** — Scenario metadata for `evaluation_policy`; **VP-CS-0004** when fixture exists.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Evaluation Policy** / **`ALL_REQUIRED`** normative text | Complete (this draft) |
| **VP-CS-0004** scenario profile | Complete (this draft) |
| **VP-CS-0004** fixture | Not started |
| **Reference implementation** (policy aggregation) | Not started |
| **Conformance execution** | Not started |

---

## Alternatives Considered

### Alternative A — Embed aggregation in VP-RULE-0001

**Description:** Extend content rule to accept multiple bodies.

**Why not chosen:** Conflates per-envelope rules with set-level policy; blocks alternate policies such as `ANY_SUFFICIENT`.

### Alternative B — Define `ANY_SUFFICIENT` in this RFC

**Description:** Ship two policies in one RFC.

**Why not chosen:** Scope control; prove one deterministic policy first.

### Alternative C — Do nothing

**Description:** Leave aggregation implementation-defined.

**Why not chosen:** Blocks normative multi-evidence conformance.

---

## Open Questions

1. **Default policy** — When a scenario omits `evaluation_policy`, should evaluators assume **`ALL_REQUIRED`** or reject the scenario?
2. **VP-CS-0004 ID reconciliation** — Should the *Identity immutability* narrative move before fixture publication?
3. **Short-circuit under `ALL_REQUIRED`** — May evaluators stop after first `not_satisfied` if trace records skipped envelopes?

---

## Acceptance Criteria

- [ ] **Evaluation Policy** is defined without trust or weighting semantics
- [ ] **`ALL_REQUIRED`** outcome table is complete and deterministic
- [ ] Ordering independence and empty-set behavior are specified
- [ ] Only `satisfied`, `not_satisfied`, and `indeterminate` appear as aggregated outcomes
- [ ] **VP-CS-0004** profile is specified without requiring fixture publication in this draft
- [ ] Compatibility with **VP-RFC-0001**, **VP-RFC-0002**, and **VP-RFC-0003** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0003](0003-multiple-evidence.md) — Multiple Evidence (draft)
- [MANIFESTO.md](../docs/00-overview/MANIFESTO.md)
- [VISION.md](../docs/00-overview/VISION.md)
- [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md)
- [GLOSSARY.md](../docs/00-overview/GLOSSARY.md) — VP-TERM-004, VP-TERM-008, VP-TERM-011, VP-TERM-013
- [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md)
- [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)
- [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md)
- [ECOSYSTEM.md](../ECOSYSTEM.md)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial draft — Evaluation Policy, `ALL_REQUIRED`, VP-CS-0004 profile; implementation deferred |

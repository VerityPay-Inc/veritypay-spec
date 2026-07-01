---
rfc: 0001
id: 0001
concept_id: VP-RFC-0001
title: Minimal Claim and Evidence Semantics
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
supersedes: []
superseded_by: null

related_terms:
  - VP-TERM-004
  - VP-TERM-008
  - VP-TERM-011
  - VP-TERM-013
  - VP-TERM-024
  - VP-TERM-027

related_architecture:
  - ../docs/01-architecture/DATA_MODEL.md
  - ../docs/03-development/CONFORMANCE_MODEL.md

related_conformance:
  - VP-CS-0001

constitutional_refs:
  - ../docs/00-overview/MANIFESTO.md
  - ../docs/00-overview/VISION.md
  - ../docs/00-overview/PRINCIPLES.md
  - ../docs/00-overview/GLOSSARY.md

related_docs:
  - ../docs/03-development/CONFORMANCE_MODEL.md
  - ../ECOSYSTEM.md

implementation_status: not_started
last_updated: 2026-06-29
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0001

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0001: Minimal Claim and Evidence Semantics

## Summary

This RFC defines the first **real protocol-engineering vertical slice** for VerityPay: minimal normative envelopes for a **Verifiable Claim**, **Assertion**, **Evidence**, and **EvidenceContent**; the first normative verification rule (**VP-RULE-0001**); and the first executable conformance scenario (**VP-CS-0001**).

The change is **additive**. It introduces minimal protocol semantics for education, reference evaluation, and conformance—not payment, payroll, blockchain, or legal certification behavior.

Upon acceptance, implementations claiming support for this RFC **MUST** pass **VP-CS-0001** once the scenario fixture is published. The temporary body-equality rule currently implemented in `veritypay-reference` (reference-interpreter scaffolding only) **MUST** be replaced by **VP-RULE-0001**; that scaffolding is **not** normative protocol truth.

---

## Motivation

Phase II delivered a **platform foundation**: validated specification input, a reference interpreter public contract, and a runnable conformance harness. Phase III requires **protocol semantics** that independent implementations can target without reverse-engineering reference code.

Today:

- Architecture documents describe rich claim and evidence models at the conceptual level.
- The reference interpreter evaluates a **temporary** minimal rule documented only in `veritypay-reference` ADR-0004.
- Conformance harnesses run **local fixtures** that are not yet bound to accepted normative rule text in this repository.

Without a minimal accepted RFC, integrators cannot answer: *What is the smallest claim/evidence input that two implementations must agree on, and what rule decides the outcome?*

This RFC closes that gap with an intentionally small, testable slice.

---

## Problem Statement

The specification lacks **accepted normative text** that simultaneously defines:

1. Required fields for minimal claim and evidence envelopes suitable for verification.
2. A first verification rule with deterministic outcome mapping.
3. A first VP-CS scenario that exercises that rule end-to-end.

Reference-interpreter scaffolding proves the platform pipeline works; it does **not** substitute for protocol specification. Conformance comparisons require a rule authored here.

---

## Goals

- Define minimal required fields for **Claim**, **Assertion**, **Evidence**, and **EvidenceContent** envelopes used in verification.
- Define **VP-RULE-0001** (*Assertion Body Evidence Match*) with deterministic mapping to **VP-TERM-011** outcomes.
- Define **VP-CS-0001** as the first executable conformance scenario for this rule.
- Provide informative negative examples (mismatched body, empty evidence body) to clarify rule edges.
- Enable downstream work: DATA_MODEL alignment, reference rule implementation, conformance fixture publication.

---

## Non-Goals

- Payment claims, payroll workflows, value movement, or merchant semantics.
- Blockchain anchors, zero-knowledge proofs, signatures, credentials, or key management.
- Legal compliance, certification badges, or regulatory interpretation.
- Full alignment with every field in [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) Verifiable Claim lifecycle (supersession, retirement, events).
- Additional VP-CS scenarios beyond **VP-CS-0001** (negative cases remain informative in this RFC only).
- A global **VP-RULE** registry file (may follow in a separate RFC; this RFC assigns **VP-RULE-0001** locally).

---

## Proposal

This section is **normative** unless marked *informative*.

### Design stance

The artifacts below are **minimal protocol semantics**—enough structure to verify one assertion against one evidence envelope. They are **not** payment semantics. Field values in examples are opaque strings unless otherwise specified.

### 1. Claim

A **Claim** is an **assertion envelope**: a stable package that binds a subject, an assertion, and a specification version under a claim identifier.

A conforming **Claim** **MUST** include the following required fields:

| Field | Type | Requirement |
|-------|------|-------------|
| `claim_id` | string | **MUST** be non-empty. **MUST** uniquely identify this claim within the evaluation context. |
| `claim_type` | string | **MUST** be non-empty. **MUST** classify the claim for rule selection. For **VP-RULE-0001**, **MUST** be `minimal`. |
| `subject` | string | **MUST** be non-empty. Identifies the claim subject anchor for this minimal slice (opaque string; no identity-model expansion in this RFC). |
| `assertion` | Assertion | **MUST** be present. See §2. |
| `specification_version` | string | **MUST** be non-empty. **MUST** pin the specification context used for verification (Edition label, manifest id, or equivalent pin agreed by scenario binding). |

A **Claim** **MUST NOT** be interpreted as a payment instruction, transfer authorization, or legal claim by this RFC alone.

### 2. Assertion

An **Assertion** is structured claim content carried inside a **Claim**.

A conforming **Assertion** **MUST** include:

| Field | Type | Requirement |
|-------|------|-------------|
| `assertion_type` | string | **MUST** be non-empty. For **VP-RULE-0001**, **MUST** be `minimal`. |
| `body` | string | **MUST** be present (MAY be empty). Compared byte-for-byte as a Unicode string under **VP-RULE-0001**. |

### 3. Evidence

**Evidence** is a **separate envelope** linked to exactly one **Claim** by identifier. Evidence **MUST NOT** mutate claim content.

A conforming **Evidence** **MUST** include:

| Field | Type | Requirement |
|-------|------|-------------|
| `evidence_id` | string | **MUST** be non-empty. **MUST** uniquely identify this evidence envelope within the evaluation context. |
| `claim_id` | string | **MUST** be non-empty. **MUST** equal the `claim_id` of the **Claim** under verification when evidence is applicable. |
| `evidence_type` | string | **MUST** be non-empty. For **VP-RULE-0001**, **MUST** be `document`. |
| `content` | EvidenceContent | **MUST** be present. See §4. |

### 4. EvidenceContent

**EvidenceContent** carries the verifiable payload compared by **VP-RULE-0001**.

A conforming **EvidenceContent** **MUST** include:

| Field | Type | Requirement |
|-------|------|-------------|
| `content_type` | string | **MUST** be non-empty. For **VP-RULE-0001**, **MUST** be `document`. |
| `body` | string | **MUST** be present. **MAY** be empty; empty body affects outcome per **VP-RULE-0001**. |

### 5. Verification rule — VP-RULE-0001

| Property | Value |
|----------|--------|
| **Rule ID** | `VP-RULE-0001` |
| **Name** | Assertion Body Evidence Match |
| **Applies when** | `claim.claim_type` is `minimal`, `claim.assertion.assertion_type` is `minimal`, `evidence.evidence_type` is `document`, and `evidence.content.content_type` is `document` |

**Inputs:** one **Claim** and zero or one **Evidence** envelope selected for evaluation (this RFC assumes exactly one evidence envelope for **VP-CS-0001**).

**Procedure** (normative outcome mapping):

1. If no **Evidence** envelope is supplied → outcome **MUST** be `indeterminate`.
2. If `evidence.claim_id` does not equal `claim.claim_id` → outcome **MUST** be `indeterminate`.
3. If `evidence.content.body` is empty (zero-length string) → outcome **MUST** be `indeterminate`.
4. If `evidence.content.body` equals `claim.assertion.body` (exact string equality) → outcome **MUST** be `satisfied`.
5. Otherwise → outcome **MUST** be `not_satisfied`.

**Notes:**

- String equality is literal Unicode string equality on the `body` fields; no normalization, hashing, or canonicalization is applied in this rule.
- This rule does **not** inspect `subject`, `specification_version`, or envelope identifiers beyond the `claim_id` linkage check above.
- This is **minimal protocol semantics**, not payment semantics.

### 6. Outcome mapping

Evaluators **MUST** report exactly one **verification outcome** per [VP-TERM-011](https://github.com/VerityPay-Inc/veritypay-spec/blob/main/docs/00-overview/GLOSSARY.md#verification-outcome):

| Outcome | Meaning for VP-RULE-0001 |
|---------|--------------------------|
| `satisfied` | Step 4 matched |
| `not_satisfied` | Step 5 matched |
| `indeterminate` | Step 1, 2, or 3 matched |

No other outcome labels are defined by this RFC.

### 7. VP-CS-0001

| Property | Value |
|----------|--------|
| **Scenario ID** | `VP-CS-0001` |
| **Name** | Minimal claim is satisfied by matching evidence |
| **Rule under test** | `VP-RULE-0001` |
| **Specification binding** | As declared by scenario metadata (`specification_version` pin) |

**Inputs (normative):**

| Artifact | Field | Value |
|----------|-------|-------|
| Claim | `claim_id` | `claim-001` |
| Claim | `claim_type` | `minimal` |
| Claim | `subject` | `subject-alpha` *(informative label; any non-empty string conforming to §1 is acceptable if scenario fixture uses another)* |
| Claim | `assertion.assertion_type` | `minimal` |
| Claim | `assertion.body` | `alpha` |
| Claim | `specification_version` | Pin declared in scenario binding |
| Evidence | `evidence_id` | `evidence-001` |
| Evidence | `claim_id` | `claim-001` |
| Evidence | `evidence_type` | `document` |
| Evidence | `content.content_type` | `document` |
| Evidence | `content.body` | `alpha` |

**Expected oracle outcome:** `satisfied`

**Informative negative companion examples** *(not separate VP-CS IDs in this RFC)*:

| Case | Change | Expected outcome |
|------|--------|------------------|
| Mismatched body | `evidence.content.body` = `beta` (claim body remains `alpha`) | `not_satisfied` |
| Missing evidence body | `evidence.content.body` = `` (empty string) | `indeterminate` |

### 8. Compatibility

This RFC is **additive**. No previously **accepted** normative rule text is amended because prior executable behavior existed only as reference-interpreter scaffolding ([veritypay-reference ADR-0004](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0004-minimal-evaluation-semantics.md)), explicitly marked non-normative for protocol purposes.

Existing architecture prose in [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) describes **VP-CS-0001** at a higher narrative level (L5 interoperability story). Acceptance of this RFC **SHOULD** align that document's executable profile of **VP-CS-0001** with the fixture defined here without removing the interoperability intent.

### 9. Conformance impact

Implementations that claim support for **VP-RFC-0001** **MUST** pass **VP-CS-0001** once the scenario fixture is published under this repository's conformance/scenario area and executed by `veritypay-conformance`.

Harness verdict vocabulary (`pass` / `fail`) remains distinct from verification outcomes (`satisfied` / `not_satisfied` / `indeterminate`) per [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).

### 10. Implementation plan

*Informative — execution order for sibling repositories after acceptance:*

1. **veritypay-spec** — Amend [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) minimally to cross-reference **VP-RFC-0001** field envelopes where appropriate; align [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) **VP-CS-0001** executable profile; ~~add **VP-CS-0001** fixture under the conformance/scenario area of this repository~~ **done** — [`spec/conformance/scenarios/VP-CS-0001.toml`](../spec/conformance/scenarios/VP-CS-0001.toml); ~~register **VP-RFC-0001** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml)~~ **done** (draft entry); introduce or extend a **VP-RULE** registry when governance approves registry shape.
2. **veritypay-reference** — Replace temporary ADR-0004 body-equality scaffolding with **VP-RULE-0001**; map outcomes to [ADR-0007](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md) public contract.
3. **veritypay-tooling** — No validator change required for this RFC beyond existing corpus checks; future VP-RULE registry entries **MAY** be validated when registry exists.
4. **veritypay-conformance** — Load spec-published **VP-CS-0001** fixture; compare adapter vs oracle under **VP-RULE-0001**.

No code changes are part of this draft pull request.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Verifiable Claim, Evidence (conceptual) | **Extension** — this RFC defines a **minimal executable profile** with required envelope fields; full lifecycle fields remain in architecture until later RFCs |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | VP-CS-0001 | **Amendment on acceptance** — executable scenario inputs and expected outcome aligned to this RFC |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** for this minimal slice |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** |

---

## Terminology Impact

| VP-TERM ID | Term | Change |
|------------|------|--------|
| VP-TERM-004 | Verifiable Claim | **Clarifying use** — minimal envelope fields (`claim_id`, `claim_type`, `subject`, `assertion`, `specification_version`) named for executable fixtures |
| VP-TERM-013 | Assertion | **Clarifying use** — `assertion_type` and `body` required in minimal profile |
| VP-TERM-008 | Evidence | **Clarifying use** — separate envelope with `evidence_id`, `claim_id`, `evidence_type`, `content` |
| VP-TERM-011 | Verification Outcome | **No vocabulary change** — rule uses existing `satisfied`, `not_satisfied`, `indeterminate` only |
| VP-TERM-024 | Conformance Scenario (VP-CS) | **Clarifying use** — **VP-CS-0001** gains executable normative inputs |
| VP-TERM-027 | Reference Interpreter | **Clarifying use** — oracle **MUST** implement accepted rules, not scaffolding ADRs alone |

**New identifiers introduced by this RFC (proposal):**

| ID | Kind | Description |
|----|------|-------------|
| VP-RULE-0001 | Verification rule | Assertion Body Evidence Match |
| VP-CS-0001 | Conformance scenario | Minimal claim is satisfied by matching evidence *(executable profile)* |

Registry entries for **VP-RULE-0001** **MAY** be deferred to a follow-on RFC if maintainers prefer a dedicated rule registry document first.

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-------------------|
| VP-CS-0001 | **Defined executable profile** — inputs in §7; expected oracle outcome `satisfied`; informative negative cases documented |

**Conformance level:** Semantic agreement on verification outcome for a fixed claim/evidence pair (foundational slice before L5 multi-implementation narratives).

**Harness behavior:** `veritypay-conformance` **MUST** treat oracle vs implementation outcome mismatch on **VP-CS-0001** as a conformance failure once the scenario is published and this RFC is accepted.

---

## Security Impact

This minimal rule performs **no cryptographic verification**, **no authenticity checks**, and **no authorization decisions**. It compares opaque string bodies and linkage by identifier only.

**Threats not mitigated by VP-RULE-0001:**

- Forged or replayed evidence content
- Mis-binding of evidence to the wrong claim beyond the explicit `claim_id` string check
- Downgrade of `specification_version` pins

**Mitigations outside this RFC:** future rules for signatures, provenance, and trust anchors.

**Impact summary:** Security surface is **unchanged relative to architecture intent** because this RFC makes explicit that the first rule is non-cryptographic and non-payment-bearing. Deployments **MUST NOT** treat `satisfied` under **VP-RULE-0001** as proof of payment, identity, or legal obligation.

---

## Backwards Compatibility

**Additive** relative to accepted specification text.

Reference repositories that implemented ADR-0004 scaffolding **SHOULD** migrate to **VP-RULE-0001** without breaking the public interpreter contract; outcome labels remain the same trio.

No production protocol behavior is broken because executable behavior was explicitly non-normative prior to this RFC.

---

## Migration Strategy

1. Accept **VP-RFC-0001**.
2. Publish **VP-CS-0001** fixture in `veritypay-spec`.
3. Update `veritypay-reference` to implement **VP-RULE-0001** (replacing scaffolding rule).
4. Point `veritypay-conformance` minimal fixture at spec-published **VP-CS-0001**.
5. Mark reference ADR-0004 semantics as **superseded for protocol purposes** by **VP-RULE-0001** (reference repo documentation change; not a spec amendment).

Dual support of scaffolding vs normative rule **SHOULD NOT** persist beyond one release cycle of the reference interpreter after acceptance.

---

## Alternatives Considered

### Alternative A — Keep reference-only body-equality rule

**Description:** Continue documenting executable semantics only in `veritypay-reference` ADR-0004.

**Why not chosen:** Conformance requires normative rule text in `veritypay-spec`. Reference-only rules fracture interoperability and confuse auditors.

### Alternative B — Define payment-shaped VP-CS-0001 first

**Description:** First scenario uses payment claim types, bank evidence, and amount fields.

**Why not chosen:** Violates Phase III sequencing; introduces domain semantics before envelope and rule mechanics are stable.

### Alternative C — Multiple VP-CS scenarios in this RFC

**Description:** Promote negative cases to **VP-CS-0002** and **VP-CS-0003** immediately.

**Why not chosen:** Scope control; informative negatives suffice to specify rule edges; separate scenarios can follow once fixture pipeline is proven.

### Alternative D — Do nothing

**Description:** Wait until DATA_MODEL fully stabilizes before any executable RFC.

**Why not chosen:** Platform repos are ready; without a minimal normative slice, reference and conformance work lacks an accepted target.

---

## Open Questions

1. **VP-RULE registry location** — Should **VP-RULE-0001** be registered in a new `spec/rules/registry.yaml`, embedded in [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md), or remain RFC-local until a registry RFC lands?
2. **`specification_version` pin format** — Should scenarios pin Edition manifest id, semver string, or a scenario-binding tuple (`edition_id`, `protocol_version`) already used by conformance fixtures?
3. **CONFORMANCE_MODEL narrative** — On acceptance, should the existing L5 payment narrative for **VP-CS-0001** move to a new ID (e.g. **VP-CS-0005**) or be rewritten in place to reference this minimal executable profile?
4. **`claim_type` / `evidence_type` extensibility** — Is a registry required before accepting additional type strings beyond `minimal` / `document`?

---

## Acceptance Criteria

- [ ] Proposal defines all required envelope fields in §1–§4 without payment-domain leakage
- [ ] **VP-RULE-0001** outcome table is complete and deterministic
- [ ] Only `satisfied`, `not_satisfied`, and `indeterminate` appear as verification outcomes
- [ ] **VP-CS-0001** inputs and expected outcome are specified
- [ ] Informative negative examples are included and do not contradict normative rule text
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] Reference scaffolding vs normative rule distinction is explicit
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [MANIFESTO.md](../docs/00-overview/MANIFESTO.md)
- [VISION.md](../docs/00-overview/VISION.md)
- [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md)
- [GLOSSARY.md](../docs/00-overview/GLOSSARY.md) — VP-TERM-004, VP-TERM-008, VP-TERM-011, VP-TERM-013
- [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md)
- [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)
- [PHASE_II_PLATFORM_PLAN.md](../docs/05-governance/PHASE_II_PLATFORM_PLAN.md)
- [ECOSYSTEM.md](../ECOSYSTEM.md)
- [veritypay-reference ADR-0004 — Minimal Evaluation Semantics](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0004-minimal-evaluation-semantics.md) — scaffolding superseded by this RFC upon acceptance
- [veritypay-reference ADR-0007 — Reference Interpreter Public Contract](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial draft — minimal envelopes, VP-RULE-0001, VP-CS-0001 |

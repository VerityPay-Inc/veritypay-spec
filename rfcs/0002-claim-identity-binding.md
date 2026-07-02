---
rfc: 0002
id: 0002
concept_id: VP-RFC-0002
title: Claim Identity Binding
status: accepted
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
  - ../docs/01-architecture/IDENTITY_MODEL.md
  - ../docs/03-development/CONFORMANCE_MODEL.md

related_conformance:
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

implementation_status: complete
last_updated: 2026-06-29
---

**Pyramid level:** specification · **Status:** accepted · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0002

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0002: Claim Identity Binding

## Summary

This RFC defines **explicit normative semantics** for **claim identity** and **evidence-to-claim binding** in the minimal verification profile established by [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md).

It introduces **VP-RULE-0002** (*Evidence Claim Binding*) as a named verification rule that decides whether evidence is **applicable** to a claim under evaluation, and **VP-CS-0002** as the first executable conformance scenario for that rule.

The change is **additive**. It formalizes binding behavior already implied by step 2 of **VP-RULE-0001** without requiring immediate amendment of **VP-RFC-0001** text or observable outcomes on existing **VP-CS-0001** fixtures.

Upon acceptance, implementations claiming support for this RFC **MUST** pass **VP-CS-0002**.

---

## Motivation

[VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) delivered the first executable protocol slice: minimal envelopes, **VP-RULE-0001** (assertion body vs evidence content), and **VP-CS-0001**.

That RFC already requires `evidence.claim_id` to equal `claim.claim_id` before content comparison proceeds, and maps a mismatch to `indeterminate`. The check is **embedded** inside **VP-RULE-0001** rather than named as its own protocol capability.

Phase III protocol expansion benefits from **composable rules** with clear boundaries:

- **Binding** — is this evidence about this claim?
- **Content match** — does evidence content support the assertion?

Extracting binding into **VP-RULE-0002** makes the precondition explicit, testable in isolation (**VP-CS-0002**), and reusable as additional content rules are added—without conflating linkage failure with content mismatch (`not_satisfied`).

---

## Problem Statement

Integrators and auditors reading **VP-RULE-0001** alone must infer that claim/evidence identity binding is a first-class protocol requirement. The rule text mixes:

1. Applicability (evidence linked to the correct claim), and
2. Content evaluation (assertion body vs evidence body).

Without a named binding rule:

- Conformance scenarios cannot target binding independently of content rules.
- Reference interpreters cannot document rule ordering without reading implementation code.
- Future rules that depend on binding must duplicate or re-embed the same precondition.

The specification needs **normative, named identity binding semantics** that stand alone while remaining compatible with accepted **VP-RFC-0001** behavior.

---

## Goals

- Define **claim identity** requirements for `claim_id` in the minimal evaluation profile.
- Define **evidence binding** — when evidence is applicable to a claim under verification.
- Define **VP-RULE-0002** (*Evidence Claim Binding*) with deterministic outcome mapping.
- Document **interaction** with **VP-RULE-0001** and recommended evaluation order.
- Define **VP-CS-0002** as the normative executable scenario for binding failure.
- Enable downstream work: DATA_MODEL binding language, reference `RuleSet` factoring, conformance fixture publication.

---

## Non-Goals

- Signatures, credentials, wallets, blockchain anchors, or cryptographic proof of identity.
- Payroll, payments, value movement, or legal claim semantics.
- Zero-knowledge proofs, trust anchors, or participant registry resolution.
- Amending **VP-RULE-0001** outcome tables in this draft (extraction is documented; normative text change is deferred).
- Multiple new normative VP-CS scenarios beyond **VP-CS-0002**.
- A global **VP-RULE** registry file (may follow in a separate RFC).
- Full [IDENTITY_MODEL.md](../docs/01-architecture/IDENTITY_MODEL.md) expansion or semantic-identity vs storage-identity reconciliation beyond minimal `claim_id` binding.

---

## Proposal

This section is **normative** unless marked *informative*.

### Design stance

This RFC describes **minimal identity binding**—opaque string identifiers and exact equality only. It does **not** define global identity registries, canonicalization, or cross-context claim merging.

### 1. Claim identity

`claim_id` is the **stable identity** of a **Claim** envelope within an **evaluation context**.

| Requirement | Normative rule |
|-------------|----------------|
| Non-empty | `claim_id` **MUST** be non-empty on conforming Claim envelopes ([VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) §1). |
| Opaque | `claim_id` **MUST** be treated as an opaque string by this RFC. |
| Comparison | `claim_id` comparison **MUST** use exact Unicode string equality. |
| No transformation | `claim_id` **MUST NOT** be normalized, canonicalized, hashed, case-folded, trimmed, or otherwise interpreted by this RFC. |

**Notes:**

- This RFC does **not** assign global uniqueness beyond the evaluation context declared by scenario binding or interpreter inputs.
- Richer identity semantics in [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [IDENTITY_MODEL.md](../docs/01-architecture/IDENTITY_MODEL.md) remain architecture context; this RFC defines the **executable minimal profile** only.

### 2. Evidence binding

**Evidence** is **applicable** to a **Claim** under verification if and only if:

```text
evidence.claim_id == claim.claim_id
```

(exact string equality per §1).

| Condition | Normative effect |
|-----------|------------------|
| `evidence.claim_id` equals `claim.claim_id` | Evidence **MAY** be used as input to subsequent verification rules (e.g. **VP-RULE-0001**). |
| `evidence.claim_id` does not equal `claim.claim_id` | Evidence **MUST NOT** be used to satisfy the claim. Verification **MUST NOT** treat content comparison as decisive for applicability. |
| `evidence.claim_id` is empty | Evidence **MUST NOT** be treated as bound; see **VP-RULE-0002**. |
| `claim.claim_id` is empty | Non-conforming envelope per [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) §1; see §3. |

Binding checks **identity linkage only**. They do **not** inspect assertion body, evidence content body, or subject fields.

### 3. Verification rule — VP-RULE-0002

| Property | Value |
|----------|--------|
| **Rule ID** | `VP-RULE-0002` |
| **Name** | Evidence Claim Binding |
| **Applies when** | A **Claim** and an **Evidence** envelope are both supplied for evaluation in the minimal profile ([VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) envelope shapes). |

**Inputs:** one **Claim** and one **Evidence** envelope.

**Procedure** (normative outcome mapping):

1. If no **Evidence** envelope is supplied → this rule **MAY** defer; evaluators **MAY** treat as out of scope for binding. *(Informative: **VP-RULE-0001** step 1 maps missing evidence to `indeterminate`.)*
2. If `claim.claim_id` is empty (zero-length string) → outcome **MUST** be `indeterminate`. *(Informative: such envelopes violate [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) §1; `indeterminate` is the least disruptive rule-layer outcome and matches existing mismatch semantics without introducing a fourth outcome label.)*
3. If `evidence.claim_id` is empty (zero-length string) → outcome **MUST** be `indeterminate`.
4. If `evidence.claim_id` equals `claim.claim_id` (exact string equality) → binding check **passes**; this rule yields **no binding failure** *(informative: downstream content rules may proceed)*.
5. If `evidence.claim_id` does not equal `claim.claim_id` → outcome **MUST** be `indeterminate`.

**Rule output vocabulary:**

| Result | Meaning |
|--------|---------|
| Binding pass | Steps 4 matched — evidence is applicable to the claim for downstream rules |
| Binding failure | Steps 2, 3, or 5 matched — outcome **MUST** be reported as `indeterminate` when this rule is the deciding rule |

**Notes:**

- This rule **does not** decide whether assertion content matches evidence content.
- This rule **does not** produce `satisfied` or `not_satisfied` on its own; binding failure maps exclusively to `indeterminate`.
- When binding passes, the overall verification outcome is determined by subsequent rules (e.g. **VP-RULE-0001**).

### 4. Interaction with VP-RULE-0001

[VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) **VP-RULE-0001** step 2 (`evidence.claim_id` mismatch → `indeterminate`) is **semantically equivalent** to a binding failure under **VP-RULE-0002**.

**Evaluation order:** Evaluators **SHOULD** apply **VP-RULE-0002** before **VP-RULE-0001** when both rules are in scope.

**Short-circuit on binding failure:** When **VP-RULE-0002** fails, evaluators **SHOULD** short-circuit: report `indeterminate` and **SHOULD NOT** run **VP-RULE-0001**.

| Rationale | Detail |
|-----------|--------|
| Applicability | Binding failure means evidence is **not applicable** to the claim under evaluation. |
| Content rules | Assertion body comparison **SHOULD NOT** be evaluated against inapplicable evidence. |
| Outcome stability | Observable verification outcomes remain **unchanged** from [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) behavior on all published scenarios. |
| Trace | Traces **MAY** record that **VP-RULE-0001** was skipped due to binding failure (e.g. `VP-RULE-0001 skipped: evidence not bound to claim`). |

**Normative evaluation flow:**

```text
1. Apply VP-RULE-0002 (Evidence Claim Binding)
      ↓ binding failure → indeterminate (short-circuit; do not run VP-RULE-0001)
      ↓ binding pass
2. Apply VP-RULE-0001 (Assertion Body Evidence Match)
      ↓ satisfied | not_satisfied | indeterminate (content/precondition cases)
```

When **VP-RULE-0002** passes, the final outcome **MUST** follow **VP-RFC-0001** outcome mapping for **VP-RULE-0001** (and any other downstream rules in scope).

**Compatibility stance for this draft:**

- **VP-RFC-0001** text **need not change** on acceptance of this RFC. Step 2 remains valid normative text for combined-rule implementations.
- **VP-RULE-0001** behavior on **VP-CS-0001** and existing fixtures **MUST NOT** change solely because this RFC is accepted.
- Reference interpreters **SHOULD** implement **VP-RULE-0002** as a distinct rule (or equivalent factored precondition) when claiming **VP-RFC-0002** support, **SHOULD** evaluate it before **VP-RULE-0001**, and **SHOULD** short-circuit on binding failure.
- **VP-RULE-0001** **SHOULD** reference **VP-RULE-0002** in documentation and trace metadata as the named binding precondition once factoring is complete.

This RFC **extracts** an implicit precondition into an explicit named rule; it does **not** alter the observable outcome table for scenarios that already pass under **VP-RFC-0001** alone.

### 5. Outcome mapping

Evaluators **MUST** report exactly one **verification outcome** per [VP-TERM-011](https://github.com/VerityPay-Inc/veritypay-spec/blob/main/docs/00-overview/GLOSSARY.md#verification-outcome):

| Outcome | Meaning for VP-RULE-0002 |
|---------|--------------------------|
| `indeterminate` | Binding failure (steps 2, 3, or 5) when this rule decides the outcome |
| `satisfied` | Not produced by this rule alone |
| `not_satisfied` | Not produced by this rule alone |

When **VP-RULE-0002** passes and **VP-RULE-0001** runs, the final outcome **MUST** follow **VP-RFC-0001** outcome mapping for the combined evaluation.

### 6. VP-CS-0002

| Property | Value |
|----------|--------|
| **Scenario ID** | `VP-CS-0002` |
| **Name** | Evidence with mismatched claim id is indeterminate |
| **Rule under test** | `VP-RULE-0002` |
| **Specification binding** | As declared by scenario metadata (`specification_version` or platform binding pin) |

**Inputs (normative):**

| Artifact | Field | Value |
|----------|-------|-------|
| Claim | `claim_id` | `claim-001` |
| Claim | `claim_type` | `minimal` |
| Claim | `subject` | `subject-alpha` *(informative; any non-empty string conforming to VP-RFC-0001 §1 is acceptable)* |
| Claim | `assertion.assertion_type` | `minimal` |
| Claim | `assertion.body` | `alpha` |
| Claim | `specification_version` | Pin declared in scenario binding |
| Evidence | `evidence_id` | `evidence-001` |
| Evidence | `claim_id` | `claim-999` |
| Evidence | `evidence_type` | `document` |
| Evidence | `content.content_type` | `document` |
| Evidence | `content.body` | `alpha` |

**Expected oracle outcome:** `indeterminate`

**Machine-readable fixture:** [`spec/conformance/scenarios/VP-CS-0002.toml`](../spec/conformance/scenarios/VP-CS-0002.toml)

**Rationale:** Bodies match (`alpha` / `alpha`), but evidence is **not applicable** to the claim because `claim_id` values differ. Evaluators **SHOULD** short-circuit after **VP-RULE-0002** failure; content rules **MUST NOT** yield `satisfied`. **VP-RULE-0002** (and **VP-RULE-0001** step 2 in combined-rule implementations) **MUST** yield `indeterminate`.

**Informative companion examples** *(not separate VP-CS IDs in this RFC)*:

| Case | Change | Expected outcome |
|------|--------|------------------|
| Matching claim id | `evidence.claim_id` = `claim-001` (bodies unchanged) | Binding passes; **VP-RULE-0001** may yield `satisfied` |
| Empty evidence claim id | `evidence.claim_id` = `` (empty string) | `indeterminate` per **VP-RULE-0002** step 3 |

### 7. Compatibility

This RFC is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md).

| Artifact | Impact |
|----------|--------|
| **VP-CS-0001** | Unchanged expected outcome (`satisfied`) — binding passes on fixture inputs |
| **VP-RULE-0001** | No normative text amendment required in this draft |
| **Platform 1.0** | Unaffected — **VP-RFC-0002** acceptance is additive; **Platform 1.1** extends capability |

Formalizing binding does **not** introduce new outcome labels or change existing scenario oracle expectations.

### 8. Conformance impact

Implementations that claim support for **VP-RFC-0002** **MUST** pass **VP-CS-0002** when the scenario fixture is published under this repository's conformance scenario area and executed by `veritypay-conformance`.

Harness verdict vocabulary (`pass` / `fail`) remains distinct from verification outcomes per [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).

Claiming **VP-RFC-0002** **SHOULD** imply **VP-RFC-0001** minimal envelope support but does **not** supersede **VP-RFC-0001** conformance requirements.

### 9. Implementation plan

*Informative — execution order for sibling repositories after acceptance:*

1. **veritypay-spec** — ~~Register **VP-RFC-0002** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml)~~ **done**; ~~publish **VP-CS-0002** fixture under [`spec/conformance/scenarios/`](../spec/conformance/scenarios/)~~ **done** — [`spec/conformance/scenarios/VP-CS-0002.toml`](../spec/conformance/scenarios/VP-CS-0002.toml); amend [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) binding language if needed; align [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) **VP-CS-0002** executable profile; ~~update [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md) / Platform 1.1 notes~~ **done**.
2. **veritypay-reference** — ~~Add **VP-RULE-0002** to `RuleSet` (distinct rule or factored precondition); preserve **VP-CS-0001** outcomes; evaluate **VP-RULE-0002** before **VP-RULE-0001** when both are present; **short-circuit** on binding failure without running **VP-RULE-0001**~~ **done**.
3. **veritypay-tooling** — No validator change required beyond existing corpus checks unless a VP-RULE registry is introduced.
4. **veritypay-conformance** — ~~Load spec-published **VP-CS-0002** fixture; compare adapter vs oracle under binding scenarios~~ **done**.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **VP-RULE-0002** normative text | Complete |
| **VP-CS-0002** fixture ([`spec/conformance/scenarios/VP-CS-0002.toml`](../spec/conformance/scenarios/VP-CS-0002.toml)) | Complete |
| **Reference implementation** (`veritypay-reference` — **VP-RULE-0002**) | Complete |
| **Conformance execution** (`veritypay-conformance` — spec-published **VP-CS-0002**) | Complete |

Future protocol expansion (additional rules, VP-CS scenarios, DATA_MODEL lifecycle fields) remains out of scope for this RFC and follows separate RFCs.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Verification envelope model; Evidence `claim_id` linkage | **Extension** — explicit binding semantics cross-reference to **VP-RFC-0002** |
| [IDENTITY_MODEL.md](../docs/01-architecture/IDENTITY_MODEL.md) | Storage identity | **Clarifying use** — minimal `claim_id` opaque equality profile; no semantic-identity expansion |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | VP-CS-0002 | **Addition** — executable scenario profile for binding failure |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** |

---

## Terminology Impact

| VP-TERM ID | Term | Change |
|------------|------|--------|
| VP-TERM-004 | Verifiable Claim | **Clarifying use** — `claim_id` as stable evaluation-context identity (opaque string) |
| VP-TERM-008 | Evidence | **Clarifying use** — `claim_id` binding field names applicability precondition |
| VP-TERM-011 | Verification Outcome | **No vocabulary change** — binding failure uses existing `indeterminate` |
| VP-TERM-024 | Conformance Scenario (VP-CS) | **Clarifying use** — **VP-CS-0002** targets binding in isolation |
| VP-TERM-027 | Reference Interpreter | **Clarifying use** — rule sets **SHOULD** apply **VP-RULE-0002** before content rules and **SHOULD** short-circuit on binding failure |

**New identifiers introduced by this RFC (proposal):**

| ID | Kind | Description |
|----|------|-------------|
| VP-RULE-0002 | Verification rule | Evidence Claim Binding |
| VP-CS-0002 | Conformance scenario | Evidence with mismatched claim id is indeterminate |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-------------------|
| VP-CS-0002 | **Defined executable profile** — inputs in §6; expected oracle outcome `indeterminate`; informative positive binding case documented |

**Conformance level:** Semantic agreement on binding failure independent of content match (foundational before multi-rule suites).

**Harness behavior:** `veritypay-conformance` **MUST** treat oracle vs implementation outcome mismatch on **VP-CS-0002** as a conformance failure.

---

## Security Impact

**VP-RULE-0002** performs **string equality only** on opaque identifiers. It does **not**:

- authenticate evidence presenters
- detect forged identifiers
- prevent replay across evaluation contexts
- bind claims to real-world legal persons or accounts

**Threats not mitigated:**

- Adversary supplies evidence whose `claim_id` matches syntactically but semantically refers to a different claim in another context
- Identifier guessing or enumeration

**Impact summary:** Security surface is **unchanged relative to VP-RFC-0001** for binding checks already implied by step 2. This RFC makes the precondition **auditable and testable**; it does **not** add cryptographic assurance.

---

## Backwards Compatibility

**Additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md).

- Existing **VP-CS-0001** oracle expectations remain valid.
- Implementations that only claim **VP-RFC-0001** **MAY** continue a single combined rule until they opt into **VP-RFC-0002** factoring.
- No new verification outcome labels are introduced.

---

## Migration Strategy

1. ~~Accept **VP-RFC-0002**.~~ **Done.**
2. ~~Publish **VP-CS-0002** fixture in `veritypay-spec`.~~ **Done** — [`spec/conformance/scenarios/VP-CS-0002.toml`](../spec/conformance/scenarios/VP-CS-0002.toml).
3. ~~Update `veritypay-reference` to expose **VP-RULE-0002** in `RuleSet` before **VP-RULE-0001**, **short-circuiting** on binding failure without running **VP-RULE-0001** (observable outcomes on existing scenarios unchanged).~~ **Done.**
4. ~~Point `veritypay-conformance` at spec-published **VP-CS-0002**.~~ **Done.**
5. ~~Update [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md) for Platform 1.1 extension when governance declares compatibility.~~ **Done.**

Dual-path implementations (combined vs factored rules) **SHOULD NOT** produce divergent outcomes on **VP-CS-0001** and **VP-CS-0002** once migration completes. Factored rule sets **SHOULD** short-circuit after **VP-RULE-0002** failure rather than running **VP-RULE-0001** against inapplicable evidence.

---

## Alternatives Considered

### Alternative A — Amend VP-RFC-0001 in place

**Description:** Move step 2 text into **VP-RFC-0001** as a named sub-procedure without a new RFC.

**Why not chosen:** Accepted RFC amendment churn; harder to test binding in isolation; violates incremental Phase III expansion pattern.

### Alternative B — Map binding failure to `not_satisfied`

**Description:** Treat wrong `claim_id` as content-level rejection.

**Why not chosen:** Misleading semantics—bodies may match while evidence is simply not applicable; **VP-RFC-0001** and reference oracle already use `indeterminate`.

### Alternative C — Require cryptographic claim_id derivation

**Description:** Bind identifiers to signed envelopes in this RFC.

**Why not chosen:** Out of scope; contradicts minimal slice goals.

### Alternative D — Multiple VP-CS scenarios in this RFC

**Description:** Normative VP-CS for empty `evidence.claim_id` and matching-id cases.

**Why not chosen:** Scope control; one normative VP-CS proves the pipeline; companions remain informative.

### Alternative E — Do nothing

**Description:** Leave binding embedded in **VP-RULE-0001** indefinitely.

**Why not chosen:** Composable rule architecture and isolated conformance coverage require a named rule.

---

## Open Questions

1. **VP-RFC-0001 amendment timing** — Should a follow-on errata RFC remove step 2 from **VP-RULE-0001** once all implementations factor **VP-RULE-0002**?
2. **Empty claim_id handling** — Should envelope validators reject before rule evaluation rather than mapping to `indeterminate` at the rule layer?
3. **VP-CS-0002 fixture metadata** — Pin `rule_id` to **VP-RULE-0002** only, or declare a multi-rule profile explicitly?

**Resolved:**

- ~~**RuleSet aggregation** — When **VP-RULE-0002** fails, should the interpreter short-circuit before **VP-RULE-0001** or run both and merge trace events?~~ **Decision:** Evaluators **SHOULD** short-circuit and report `indeterminate` without running **VP-RULE-0001**; traces **MAY** note the skip. See §4.

---

## Acceptance Criteria

- [x] Proposal defines claim identity and evidence binding without payment-domain leakage
- [x] **VP-RULE-0002** outcome table is complete and deterministic
- [x] Only `satisfied`, `not_satisfied`, and `indeterminate` appear as verification outcomes (this rule uses `indeterminate` only when deciding)
- [x] **VP-CS-0002** inputs and expected outcome are specified
- [x] **VP-CS-0002** machine-readable fixture published
- [x] Interaction with **VP-RULE-0001** is documented without requiring immediate VP-RFC-0001 amendment
- [x] Short-circuit on **VP-RULE-0002** binding failure is specified (§4)
- [x] Informative negative and positive companion examples included
- [x] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [x] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [MANIFESTO.md](../docs/00-overview/MANIFESTO.md)
- [VISION.md](../docs/00-overview/VISION.md)
- [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md)
- [GLOSSARY.md](../docs/00-overview/GLOSSARY.md) — VP-TERM-004, VP-TERM-008, VP-TERM-011, VP-TERM-013
- [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md)
- [IDENTITY_MODEL.md](../docs/01-architecture/IDENTITY_MODEL.md)
- [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)
- [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md)
- [ECOSYSTEM.md](../ECOSYSTEM.md)
- [veritypay-reference ADR-0007 — Reference Interpreter Public Contract](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Accepted — claim identity, VP-RULE-0002, VP-CS-0002; short-circuit on binding failure; reference and conformance paths complete |

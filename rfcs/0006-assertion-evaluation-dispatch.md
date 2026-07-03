---
rfc: 0006
id: 0006
concept_id: VP-RFC-0006
title: Assertion Evaluation Dispatch
status: draft
version: 0.1.0
type: protocol
category: Protocol
pyramid_level: specification

authors:
  - VerityPay Core Team

reviewers: []

created: 2026-07-02
updated: 2026-07-02

depends_on:
  - 0000
  - 0001
  - 0005
supersedes: []
superseded_by: null

related_terms:
  - VP-TERM-004
  - VP-TERM-011
  - VP-TERM-013

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
  - 0005-assertion-types.md

implementation_status: not_started
last_updated: 2026-07-02
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0006

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [VP-RFC-0002](0002-claim-identity-binding.md) · [VP-RFC-0005](0005-assertion-types.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0006: Assertion Evaluation Dispatch

## Summary

This RFC defines **how VerityPay selects evaluation semantics for an Assertion** — the protocol **dispatch model** that maps an **Assertion Type** to exactly one **Assertion Evaluator**.

It specifies **dispatch only**. It does **not** define new **VP-RULE** text, interpreter implementations, or verification outcome vocabulary.

Draft [VP-RFC-0005](0005-assertion-types.md) introduced **Assertion Type** taxonomy. This RFC supplies the deterministic **Evaluation Dispatch** mechanism required before protocol rules execute under that taxonomy.

The change is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md), [VP-RFC-0002](0002-claim-identity-binding.md), and draft [VP-RFC-0005](0005-assertion-types.md). **Platform 1.2** pins remain valid until implementations opt into dispatch claims.

---

## Motivation

Evaluators **MUST NOT** infer assertion semantics by inspecting arbitrary claim content, evidence payloads, or implementation metadata.

Without normative dispatch:

- Interpreters embed ad hoc heuristics tied to claim bodies or fixture-specific strings.
- Conformance cannot compare evaluator selection independently of rule outcomes.
- Future **Assertion Types** from [VP-RFC-0005](0005-assertion-types.md) lack a stable selection path.

The protocol needs a **named, deterministic dispatch layer**:

```text
Assertion Type
      ↓
Evaluation Dispatch
      ↓
Assertion Evaluator
      ↓
Protocol Rule(s)
      ↓
Outcome
```

---

## Problem Statement

[VP-RFC-0005](0005-assertion-types.md) names *what* an assertion means. The specification still needs normative text for *how* an evaluator is selected from `assertion_type` alone.

Without **Evaluation Dispatch**:

- **Assertion Type** identifiers are inert vocabulary.
- Reference and independent implementations may diverge on when **VP-RULE-0001** applies.
- Unknown types have no protocol-level outcome.

---

## Goals

- Define **Assertion Evaluator** and **Evaluation Dispatch** as protocol vocabulary.
- Require deterministic, type-only dispatch before protocol rules execute.
- Standardize the initial mapping **`body_equality`** → **Body Equality Evaluator** → **VP-RULE-0001**.
- Specify unknown **Assertion Type** handling (`indeterminate`).
- Enable future evaluator RFCs without changing dispatch invariants.
- Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).

---

## Non-Goals

- New **VP-RULE** definitions or amendments to **VP-RULE-0001** / **VP-RULE-0002** text.
- Reference or conformance implementation (deferred).
- **Evaluation Policy** aggregation semantics ([VP-RFC-0004](0004-evidence-evaluation-policies.md)).
- Standardizing evaluators beyond **Body Equality Evaluator** in this RFC.
- VP-CS fixture publication or amendment.
- Machine-readable evaluator registry publication (future governance).

---

## Proposal

### 1. Protocol composition (informative)

```text
Assertion
      ↓
Assertion Type          (VP-RFC-0005)
      ↓
Evaluation Dispatch     (this RFC)
      ↓
Assertion Evaluator
      ↓
Protocol Rule(s)        (for example VP-RULE-0002, VP-RULE-0001)
      ↓
Evidence Set              (VP-RFC-0003)
      ↓
Evaluation Policy         (VP-RFC-0004)
      ↓
Verification Result
```

**Evaluation Dispatch** is protocol behavior — not an implementation class hierarchy. This RFC defines selection rules only.

### 2. Assertion Evaluator

| Property | Value |
|----------|--------|
| **Term** | **Assertion Evaluator** |
| **Definition** | The protocol-defined semantic evaluator responsible for interpreting one **Assertion Type**. |

An **Assertion Evaluator** names the evaluation semantics for a type. It **MAY** invoke one or more protocol rules defined in accepted RFCs. It does **not** replace **VP-RULE** normative text.

### 3. Evaluation Dispatch

| Property | Value |
|----------|--------|
| **Term** | **Evaluation Dispatch** |
| **Definition** | The deterministic process that selects exactly one **Assertion Evaluator** based solely on **Assertion Type**. |

Normative requirements:

1. **Determinism** — **Evaluation Dispatch** **MUST** be deterministic: the same **Assertion Type** **MUST** select the same **Assertion Evaluator** on every conforming implementation.
2. **Type-only input** — Dispatch **MUST** depend only on **Assertion Type** (`assertion_type`). Dispatch **MUST NOT** inspect **Evidence** content, **EvidenceContent**, assertion `body`, claim `subject`, or implementation metadata.
3. **Single selection** — Exactly one **Assertion Evaluator** **MUST** be selected per **Assertion** under evaluation.
4. **Unknown types** — If `assertion_type` does not match a standardized **Assertion Type** with a defined evaluator mapping, the verification outcome **MUST** be `indeterminate` without executing type-specific protocol rules.
5. **Ordering** — **Evaluation Dispatch** **MUST** complete before type-specific protocol rules selected by the **Assertion Evaluator** execute. Precondition rules from other accepted RFCs (for example **VP-RULE-0002** binding) remain governed by those RFCs and **MAY** run per their documented order relative to content evaluation.
6. **No implementation leakage** — Dispatch identifiers and evaluator names **MUST NOT** encode language, framework, storage, or vendor details.

This RFC does **not** specify reference interpreter modules, class names, or internal APIs.

### 4. Initial dispatch mapping — `body_equality`

| Property | Value |
|----------|--------|
| **Assertion Type** | `body_equality` |
| **Assertion Evaluator** | **Body Equality Evaluator** |
| **Protocol rule(s)** | **VP-RULE-0001** (*Assertion Body Evidence Match*) per [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) when preconditions hold |

```text
body_equality
      ↓
Body Equality Evaluator
      ↓
VP-RULE-0001
```

**Informative alignment:** **VP-CS-0001** and **VP-CS-0002** inherit this dispatch from **`body_equality`** semantics per [VP-RFC-0005](0005-assertion-types.md). Published fixtures may retain `assertion_type = minimal` until fixture-alignment; dispatch semantics are **`body_equality`** regardless of fixture string reconciliation timing.

No additional **Assertion Evaluator** mappings are standardized in this draft.

### 5. Future compatibility

Future RFCs **MAY** introduce additional **Assertion Evaluator** mappings without changing dispatch invariants in this RFC. Informative examples (not normative in this draft):

| Informative evaluator | Typical future **Assertion Type** themes |
|-----------------------|------------------------------------------|
| **Regex Evaluator** | Pattern match |
| **Numeric Evaluator** | Numeric comparison |
| **Hash Evaluator** | Cryptographic hash comparison |
| **Signature Evaluator** | Digital signature verification |
| **Schema Evaluator** | Schema validation |

Each future evaluator **MUST** be defined with a stable **Assertion Type** mapping, applicable protocol rules, and unknown-type behavior — not merely listed.

### 6. Compatibility

| Artifact | Impact |
|----------|--------|
| **VP-RFC-0005** | **Companion** — dispatch operationalizes **Assertion Type** taxonomy |
| **VP-RULE-0001** / **VP-RULE-0002** | Unchanged — rule text not amended |
| **VP-CS-0001** / **VP-CS-0002** | Unchanged fixtures — dispatch inherited from **`body_equality`** |
| **Platform 1.2** | Unaffected — draft dispatch only until acceptance |

Implementations that do not claim **VP-RFC-0006** **MAY** continue Platform 1.2 evaluation paths without explicit dispatch vocabulary.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Assertion Evaluator; evaluation flow | **Extension on acceptance** — dispatch layer between **Assertion Type** and **Evidence Set** |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | Evaluator dispatch | **Clarification on acceptance** — implementations **MUST** dispatch from `assertion_type` |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** in this draft |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** in this draft |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Assertion Evaluator** | **New protocol concept** — semantic evaluator for one **Assertion Type** |
| **Evaluation Dispatch** | **New protocol concept** — deterministic type-to-evaluator selection |
| **Body Equality Evaluator** | **New evaluator name** — maps **`body_equality`** to **VP-RULE-0001** |
| VP-TERM-013 (*Assertion*) | **Clarifying use** — `assertion_type` drives dispatch before rule execution |

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **Inherited dispatch** — **`body_equality`** → **Body Equality Evaluator** → **VP-RULE-0001**; fixture unchanged |
| **VP-CS-0002** | **Inherited dispatch** — same type mapping; binding per **VP-RFC-0002** when applicable |

**Harness behavior (draft):** VP-CS scenarios **inherit** evaluator selection from `assertion_type` per this RFC. No new VP-CS fixture is defined in this draft. Conformance compares **evaluator behavior** and outcomes against the reference oracle — not internal implementation architecture.

Claiming **VP-RFC-0006** **MUST** imply **VP-RFC-0005** support. Claiming **VP-RFC-0006** **SHOULD** imply **VP-RFC-0001** support but does **not** supersede its conformance requirements.

---

## Security Impact

Dispatch inspects **Assertion Type** identifiers only. It introduces **no new trust or cryptographic semantics**. Threat modeling for future evaluators belongs in their defining RFCs.

---

## Backwards Compatibility

**Additive.** Existing envelopes, rules, scenarios, and Platform 1.2 pins remain valid.

---

## Migration Strategy

1. Accept **VP-RFC-0006** when governance approves (with or after **VP-RFC-0005** acceptance).
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. Register **VP-RFC-0006** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.
4. Future work: reference interpreter dispatch routing, fixture `assertion_type` string alignment.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0006**; optional fixture alignment RFC.
2. **veritypay-reference** — Route **Assertion Type** to **Assertion Evaluator** when acceptance path defines it.
3. **veritypay-tooling** — No validator change required beyond existing corpus checks unless evaluator registry is introduced.
4. **veritypay-conformance** — Compare dispatch behavior against oracle when normative.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Evaluation Dispatch** / **Body Equality Evaluator** normative text | Complete (this draft) |
| **VP-RFC-0006** registry entry (draft) | Pending |
| **Reference implementation** (dispatch routing) | Not started |
| **Conformance execution** (dispatch-aware comparison) | Not started |

---

## Alternatives Considered

### Alternative A — Embed dispatch in VP-RFC-0005

**Description:** Define evaluator selection in the Assertion Types RFC.

**Why not chosen:** [VP-RFC-0005](0005-assertion-types.md) intentionally deferred dispatch; separation keeps taxonomy stable while dispatch evolves.

### Alternative B — Implicit dispatch via VP-RULE-0001 only

**Description:** Assume all assertions use **VP-RULE-0001** without a named dispatch layer.

**Why not chosen:** Blocks extensible evaluator model and unknown-type protocol behavior.

### Alternative C — Content-based dispatch

**Description:** Select semantics by inspecting assertion or evidence bodies.

**Why not chosen:** Violates determinism and security goals; prevents stable conformance comparison.

---

## Open Questions

1. **Fixture alignment** — When should published VP-CS fixtures change `assertion_type` from `minimal` to `body_equality`?
2. **Binding order** — Should **VP-RFC-0006** normatively state **VP-RULE-0002** always precedes evaluator-selected content rules, or remain implicit per Platform 1.1 practice?
3. **Evaluator registry** — Should **Assertion Evaluator** identifiers become machine-readable registry entries?

---

## Acceptance Criteria

- [ ] **Assertion Evaluator** and **Evaluation Dispatch** are defined without payment-domain leakage
- [ ] Dispatch is deterministic and depends only on **Assertion Type**
- [ ] Unknown **Assertion Types** yield `indeterminate` without executing type-specific rules
- [ ] **`body_equality`** → **Body Equality Evaluator** → **VP-RULE-0001** mapping is complete
- [ ] No new **VP-RULE** text or implementation architecture is defined
- [ ] Future evaluator extensibility is documented without standardizing additional evaluators
- [ ] Compatibility with **VP-RFC-0001**, **VP-RFC-0002**, and **VP-RFC-0005** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (accepted)
- [VP-RFC-0005](0005-assertion-types.md) — Assertion Types (draft)
- [MANIFESTO.md](../docs/00-overview/MANIFESTO.md)
- [VISION.md](../docs/00-overview/VISION.md)
- [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md)
- [GLOSSARY.md](../docs/00-overview/GLOSSARY.md) — VP-TERM-004, VP-TERM-011, VP-TERM-013
- [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md)
- [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)
- [PLATFORM_RELEASES.md](../PLATFORM_RELEASES.md)
- [ECOSYSTEM.md](../ECOSYSTEM.md)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-07-02 | Initial draft — Evaluation Dispatch, Body Equality Evaluator; implementation deferred |

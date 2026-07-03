# Verity Core Protocol

**Version 1.2** · **Status:** Living Specification

---

This document consolidates the Verity Core protocol RFCs into a single implementation-oriented specification. It is **not** a replacement for RFCs — [VP-RFC-0000](rfcs/0000-rfc-process.md) remains the normative change mechanism. RFCs document the evolution of the protocol; this document presents the current protocol as one coherent specification for implementers, reviewers, auditors, and educators.

**Goals:** present the protocol in implementation order; describe the complete verification model; reference RFCs rather than duplicate rationale; remain synchronized with protocol RFCs; serve as the primary entry point for protocol implementers.

**Non-goals:** introduce new protocol semantics; replace RFC governance; define implementation-specific behavior.

Normative behavior is defined by accepted RFCs and, where cited, draft RFCs in progress. When this document and an RFC disagree, the RFC wins until this document is updated through governance.

---

## 1. Introduction

*Placeholder.* This section will summarize the Verity Core verification protocol, its scope, and its relationship to the VerityPay ecosystem. Content will be drawn from accepted protocol RFCs beginning with [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) and aligned with [DOMAIN_MODEL.md](docs/01-architecture/DOMAIN_MODEL.md).

## 2. Design Principles

*Placeholder.* This section will consolidate protocol design principles referenced across Verity Core RFCs and the constitutional layer — notably [PRINCIPLES.md](docs/00-overview/PRINCIPLES.md). It will not introduce principles beyond those established in accepted specification documents.

## 3. Protocol Architecture

*Placeholder.* This section will describe the structural architecture of the verification protocol — entities, relationships, and evaluation flow — as defined in [DATA_MODEL.md](docs/01-architecture/DATA_MODEL.md) and accepted RFCs **VP-RFC-0001** through **VP-RFC-0004**.

## 4. Verification Model

Verification is the process of evaluating whether a **Claim**'s **Assertion** is supported by **Evidence** under a fixed set of protocol rules. Verity Core describes that process in **implementation order** — the sequence an evaluator follows from environment setup through outcome — not RFC publication order.

The model below synthesizes accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), [VP-RFC-0002](rfcs/0002-claim-identity-binding.md), [VP-RFC-0003](rfcs/0003-multiple-evidence.md), and [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md). Stages marked *(draft)* reference draft RFCs **VP-RFC-0005** through **VP-RFC-0009**; behavior described there is informative until those RFCs are accepted.

### Lifecycle (implementation order)

```text
Verification Context          (VP-RFC-0007, draft)
        ↓
Verification Profile          (VP-RFC-0008, draft)
        ↓
Claim                         (VP-RFC-0001, accepted)
        ↓
Assertion                     (VP-RFC-0001, accepted)
        ↓
Assertion Type                (VP-RFC-0005, draft)
        ↓
Assertion Evaluator           (VP-RFC-0006, draft)
        ↓
Evidence Set                  (VP-RFC-0003, accepted)
        ↓
Evaluation Policy             (VP-RFC-0004, accepted)
        ↓
Verification Result           (VP-RFC-0001, VP-RFC-0004, accepted)
```

### Stages

**Verification Context** *(draft — [VP-RFC-0007](rfcs/0007-verification-context.md))* defines the **immutable evaluation environment** shared by every assertion and evidence envelope in one verification. Core fields include `edition`, `protocol_version`, and `evaluation_policy`. Context belongs to the evaluation — it is not embedded in claims or evidence.

**Verification Profile** *(draft — [VP-RFC-0008](rfcs/0008-verification-profiles.md))* is a named, reusable configuration of context fields. Selecting a profile (for example **`minimal_all_required`**) resolves evaluation-wide parameters such as **`ALL_REQUIRED`** policy without repeating individual context values. Profiles do not alter claim or evidence semantics.

**Claim** ([VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), accepted) is the protocol envelope that carries what is being asserted. It supplies stable **identity** (`claim_id`), subject linkage, and the nested **Assertion** under evaluation. The claim frames the evaluation target; it does not embed verification outcomes.

**Assertion** ([VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), accepted) is the structured content within a claim that verification rules evaluate. The interpreter evaluates the **assertion** — not the claim envelope alone. Under minimal semantics, comparison operates on assertion and evidence content when preconditions hold.

**Assertion Type** *(draft — [VP-RFC-0005](rfcs/0005-assertion-types.md))* is the protocol identifier (`assertion_type`) that names how an assertion body is **interpreted**. Every assertion declares exactly one type. The initial standardized type is **`body_equality`**. Types describe meaning; they do not execute evaluation by themselves.

**Assertion Evaluator** *(draft — [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md))* is selected by **Evaluation Dispatch** from `assertion_type` alone. The evaluator performs semantic evaluation for that type — for example, routing **`body_equality`** to **VP-RULE-0001**. Dispatch must not inspect arbitrary claim or evidence bodies to infer semantics. Unknown types yield `indeterminate`.

**Evidence Set** ([VP-RFC-0003](rfcs/0003-multiple-evidence.md), accepted) is the **unordered** collection of **Evidence** envelopes associated with one claim during evaluation. Each envelope retains its own identity and content. Evidence ordering must not affect protocol meaning. Per-envelope binding to the claim is governed by [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) (**VP-RULE-0002**) when binding rules are in scope.

**Evaluation Policy** ([VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md), accepted) aggregates per-envelope rule results from an evidence set into one verification outcome. The initial policy is **`ALL_REQUIRED`**: every applicable envelope must be `satisfied` for aggregate `satisfied`; any `not_satisfied` dominates; otherwise indeterminate conditions apply. Policies aggregate logical outcomes only — no trust or weighting.

**Verification Result** ([VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md), accepted) communicates the protocol outcome: `satisfied`, `not_satisfied`, or `indeterminate`. The result is explicit protocol truth — not transport status or worldly confirmation. Single-evidence evaluation may treat **`ALL_REQUIRED`** as implicit when one envelope is present.

### Responsibilities

| Stage | Responsibility |
|-------|----------------|
| **Verification Context** | Defines the evaluation environment |
| **Verification Profile** | Names a reusable context configuration *(draft)* |
| **Claim** | Defines what is asserted; supplies identity and assertion envelope |
| **Assertion** | Defines the verification target evaluated by rules |
| **Assertion Type** | Determines semantic interpretation of assertion data *(draft)* |
| **Assertion Evaluator** | Performs type-specific semantic evaluation *(draft)* |
| **Evidence Set** | Supplies supporting evidence for evaluation |
| **Evaluation Policy** | Aggregates multiple evidence results into one outcome |
| **Verification Result** | Communicates the protocol outcome |

Optional **Context Extensions** *(draft — [VP-RFC-0009](rfcs/0009-verification-context-extensions.md))* may augment context in future evaluations. No standardized extensions exist today; they do not appear in the lifecycle until defined by future RFCs.

## 5. Verification Context

**Verification Context** is the immutable protocol object that supplies evaluation-wide information shared by all **Assertions** and **Evidence** during one verification. It frames *how* evaluation proceeds — not *what* is asserted. Draft [VP-RFC-0007](rfcs/0007-verification-context.md) defines the context object; accepted [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md) already defines **`evaluation_policy`** semantics that context carries.

Verification Context **belongs to the evaluation**. It is **not** part of a **Claim**. It is **not** part of **Evidence**. It does not define trust, issuers, or authorization.

### Core fields

| Field | Role |
|-------|------|
| **`edition`** | Specification edition under which evaluation interprets rules |
| **`protocol_version`** | Declared protocol version for the evaluation |
| **`evaluation_policy`** | **Evaluation Policy** identifier — for example **`ALL_REQUIRED`** per [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md) |

Context **must** remain immutable during evaluation and **must** apply to every assertion in that evaluation. Context **must not** modify claim or evidence semantics.

Implementations may derive these values from specification metadata until explicit context objects are adopted. Wire encodings are deferred.

### Verification Profiles

Draft [VP-RFC-0008](rfcs/0008-verification-profiles.md) introduces **Verification Profile** — a named, reusable configuration of context fields identified by stable `profile_id`. The initial standardized profile is **`minimal_all_required`**, which implies **`ALL_REQUIRED`** evaluation policy and Platform 1.2 dispatch and evidence-set behavior. Profile selection resolves context; it does not replace core context fields.

### Context Extensions

Draft [VP-RFC-0009](rfcs/0009-verification-context-extensions.md) defines **Context Extension** — optional objects that augment context without replacing core fields. Informative future categories include time, trust, issuer, localization, audit, and regulatory context. **No standardized extensions exist** in the current platform. Unknown extensions must be ignored unless the active profile explicitly requires them.

## 6. Claims

A **Claim** is the central protocol envelope for a structured statement under verification. Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) defines the minimal claim envelope; accepted [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) defines how claim identity binds evidence.

Claims **contain Assertions**. The claim envelope binds identity, subject, and specification context around assertion content — the claim is not itself the assertion. Verification evaluates the nested assertion using evidence; the claim supplies the stable frame within which that evaluation occurs.

### Identity

`claim_id` is the **stable identity** of a claim envelope within an evaluation context. It must be non-empty and is compared using exact string equality per [VP-RFC-0002](rfcs/0002-claim-identity-binding.md). Identity enables **evidence binding**: evidence is applicable only when `evidence.claim_id` equals `claim.claim_id`. Binding checks linkage only — it does not inspect assertion or evidence bodies.

Claim identity is a precondition for correct evaluation; it does **not** determine verification outcomes by itself. Mismatched or empty binding yields `indeterminate` via **VP-RULE-0002** without proceeding to content rules. Matching identity allows subsequent rules (such as **VP-RULE-0001**) to evaluate assertion content.

### Evaluation target

The claim's role in verification is to present **what is asserted** — identity plus nested **Assertion** — as the evaluation target. Outcomes are recorded separately in **Verification Result**; claims must not embed verification outcomes.

## 7. Assertions

An **Assertion** is the structured content within a claim that verification rules evaluate. Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) requires every minimal claim to carry a nested assertion with `assertion_type` and `body`. Draft [VP-RFC-0005](rfcs/0005-assertion-types.md) names **Assertion Type** as the protocol vocabulary for interpreting assertion data.

Assertions express **what is being evaluated**. The interpreter evaluates the assertion — not the claim envelope alone. Under **VP-RULE-0001**, when preconditions hold, evaluation compares assertion body to evidence content body; missing or mismatched content under rule preconditions yields `indeterminate` or `not_satisfied` per the rule tables in [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md).

### Fields

| Field | Role |
|-------|------|
| **`assertion_type`** | Declares exactly one **Assertion Type** — the protocol identifier describing semantic interpretation *(taxonomy in draft [VP-RFC-0005](rfcs/0005-assertion-types.md))* |
| **`body`** | Opaque protocol data whose meaning is defined by the declared type and applicable rules |

**Assertion Type** defines *interpretation* — what the body means in protocol terms. It does not define *evaluation procedure*; rule execution and evaluator dispatch are specified elsewhere ([VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md), draft). The **`body`** carries the data consumed by those rules — for **`body_equality`**, the comparable payload evaluated against evidence content when linkage and type preconditions hold.

Every assertion must declare exactly one type via `assertion_type`. Type identifiers must be stable protocol strings — not implementation class names or vendor-specific labels.

## 8. Assertion Types

*Placeholder.* This section will describe **Assertion Type** taxonomy per draft [VP-RFC-0005](rfcs/0005-assertion-types.md), including the initial **`body_equality`** type. Evaluation dispatch is deferred to the Assertion Evaluators section.

## 9. Assertion Evaluators

*Placeholder.* This section will describe **Evaluation Dispatch** and **Assertion Evaluator** selection per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md). Dispatch depends solely on `assertion_type` and does not inspect claim or evidence bodies.

## 10. Evidence

*Placeholder.* This section will describe evidence envelopes and **EvidenceContent** per accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md). Claim identity binding per [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) will be referenced where linkage rules apply.

## 11. Evidence Sets

*Placeholder.* This section will describe **Evidence Set** composition — unordered collections of evidence per claim — per accepted [VP-RFC-0003](rfcs/0003-multiple-evidence.md). Ordering independence and per-envelope binding will be summarized from that RFC.

## 12. Evaluation Policies

*Placeholder.* This section will describe **Evaluation Policy** aggregation over evidence sets per accepted [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md), including the initial **`ALL_REQUIRED`** policy and verification outcome vocabulary.

## 13. Verification Profiles

*Placeholder.* This section will describe **Verification Profile** — named **Verification Context** configurations — per draft [VP-RFC-0008](rfcs/0008-verification-profiles.md), including the initial **`minimal_all_required`** profile.

## 14. Context Extensions

*Placeholder.* This section will describe the **Context Extension** model per draft [VP-RFC-0009](rfcs/0009-verification-context-extensions.md). No standardized extensions are defined; future RFCs will populate extension semantics.

## 15. Verification Results

*Placeholder.* This section will describe verification outcomes (`satisfied`, `not_satisfied`, `indeterminate`) and result composition per [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) and aggregated results per [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md).

## 16. Protocol Capabilities

*Placeholder.* This section will describe **Protocol Capability** identifiers and conformance eligibility per draft [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md). Capabilities are an implementation concept — not part of claims or context.

## 17. Conformance

*Placeholder.* This section will summarize the conformance model and VP-CS scenario execution per [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md) and executable scenarios authored under accepted RFCs. Harness verdict vocabulary will be distinguished from verification outcomes.

## 18. Versioning

*Placeholder.* This section will describe Edition, Protocol Version, and Platform Release relationships per [SPECIFICATION_VERSIONING.md](docs/05-governance/SPECIFICATION_VERSIONING.md) and [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md). Version 1.2 of this document aligns with **Platform 1.2** engineering baseline.

## 19. Relationship to Reference Implementation

*Placeholder.* This section will describe how `veritypay-reference` implements Verity Core semantics as an educational oracle — without making the reference architecture normative. See [ECOSYSTEM.md](ECOSYSTEM.md) and the reference interpreter ADRs in `veritypay-reference`.

## 20. Relationship to Conformance Suite

*Placeholder.* This section will describe how `veritypay-conformance` executes VP-CS scenarios against the reference oracle per [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md). Scenario meaning remains authored in this repository.

## 21. Future Evolution

*Placeholder.* This section will describe how Verity Core evolves through the RFC process ([VP-RFC-0000](rfcs/0000-rfc-process.md)) and how this document stays synchronized when RFCs are accepted or amended. Draft RFCs may appear in placeholders until acceptance.

## 22. References

*Placeholder.* This section will maintain a canonical bibliography of Verity Core RFCs and architecture documents. Initial scope:

| RFC | Title | Status |
|-----|-------|--------|
| [VP-RFC-0000](rfcs/0000-rfc-process.md) | RFC Process | Accepted |
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | Minimal Claim and Evidence Semantics | Accepted |
| [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) | Claim Identity Binding | Accepted |
| [VP-RFC-0003](rfcs/0003-multiple-evidence.md) | Multiple Evidence | Accepted |
| [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md) | Evidence Evaluation Policies | Accepted |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Assertion Types | Draft |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Assertion Evaluation Dispatch | Draft |
| [VP-RFC-0007](rfcs/0007-verification-context.md) | Verification Context | Draft |
| [VP-RFC-0008](rfcs/0008-verification-profiles.md) | Verification Profiles | Draft |
| [VP-RFC-0009](rfcs/0009-verification-context-extensions.md) | Verification Context Extensions | Draft |
| [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md) | Protocol Capability Negotiation | Draft |

---

*Living specification — sections populate from accepted protocol RFCs. Maintainers update this document when RFC status or Platform releases change materially.*

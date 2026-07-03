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

*Placeholder.* This section will present the end-to-end verification model in implementation order: context, claim, assertion, evidence set, evaluation policy, and verification result. Content will reference [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), [VP-RFC-0003](rfcs/0003-multiple-evidence.md), [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md), and draft context RFCs **VP-RFC-0007** through **VP-RFC-0009** where applicable.

## 5. Verification Context

*Placeholder.* This section will describe **Verification Context** — the immutable evaluation environment — per draft [VP-RFC-0007](rfcs/0007-verification-context.md). Core fields (`edition`, `protocol_version`, `evaluation_policy`) will be summarized without duplicating RFC rationale.

## 6. Claims

*Placeholder.* This section will describe claim envelopes and their role in verification per accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) and [VP-RFC-0002](rfcs/0002-claim-identity-binding.md). Claim semantics will not extend beyond those RFCs.

## 7. Assertions

*Placeholder.* This section will describe **Assertion** structure within claims — `assertion_type` and `body` — per [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md). Verification evaluates assertions, not envelopes alone.

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

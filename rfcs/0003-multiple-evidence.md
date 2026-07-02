---
rfc: 0003
id: 0003
concept_id: VP-RFC-0003
title: Multiple Evidence
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
  - VP-CS-0003

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
  - 0004-evidence-evaluation-policies.md

implementation_status: not_started
last_updated: 2026-06-29
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0003

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [VP-RFC-0002](0002-claim-identity-binding.md) · [VP-RFC-0004](0004-evidence-evaluation-policies.md) *(Evaluation Policy — draft)* · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0003: Multiple Evidence

## Summary

This RFC extends the minimal verification profile so a **Claim MAY be supported by more than one Evidence** envelope during evaluation.

It introduces the protocol concept **Evidence Set** — the unordered collection of **Evidence** associated with one claim under evaluation — without defining **Evaluation Policy** or how multiple evidence items combine into a verification outcome.

The change is **additive**. Accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) and [VP-RFC-0002](0002-claim-identity-binding.md) semantics for single-evidence evaluation remain valid. **Evaluation Policy** semantics are defined exclusively in draft [VP-RFC-0004](0004-evidence-evaluation-policies.md).

This draft defines **VP-CS-0003** as a conformance scenario profile for successful loading of one claim and two correctly bound evidence envelopes. Verification outcome semantics for **VP-CS-0003** are **out of scope** for this RFC — see [VP-RFC-0004](0004-evidence-evaluation-policies.md).

**VP-RFC-0003** and **VP-RFC-0004** are intended for **joint acceptance** as **Platform 1.2**.

---

## Motivation

Real verification rarely depends on a single artifact. Examples include:

- employment contract
- payroll statement
- bank transfer
- tax receipt

Each item is independent **Evidence** supporting one assertion. [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) and current reference and conformance paths assume **exactly one** evidence envelope per evaluation context. That constraint is sufficient for the first protocol slice but does not express multi-artifact verification inputs.

Phase III expansion requires a **named, protocol-level way to associate multiple evidence envelopes with one claim** before later RFCs can define aggregation, sufficiency, or trust policies.

---

## Problem Statement

Without a multiple-evidence concept:

- Scenario authors cannot express realistic multi-artifact inputs in fixtures.
- Architecture documents cannot describe how claims relate to more than one evidence envelope at evaluation time.
- Future evaluation rules would invent ad hoc collection shapes instead of reusing a shared protocol term.

The specification needs **normative vocabulary for multiple independent evidence envelopes per claim**. How an **Evidence Set** maps to a verification outcome is **not** defined here — that is [VP-RFC-0004](0004-evidence-evaluation-policies.md).

---

## Goals

- Allow a **Claim** to reference **zero or more** **Evidence** envelopes during evaluation.
- Introduce **Evidence Set** as the protocol concept for that association.
- Preserve **Evidence** as an independent envelope with its own `evidence_id`, **VP-RULE-0002** binding, and **EvidenceContent**.
- State normative **input** constraints only: ordering independence and structural envelope independence.
- Define **VP-CS-0003** as a loading-oriented conformance profile for two bound evidence envelopes (no verification outcome).
- Enable downstream work: [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) alignment, reference interpreter extension, conformance fixture format.

---

## Non-Goals

- Evidence collections with nested hierarchy, weighting, trust scores, or signatures.
- Whether **all** evidence must pass, **any** evidence is sufficient, or partial satisfaction is allowed.
- Evidence ordering, priority, or aggregation into a single verification outcome (see [VP-RFC-0004](0004-evidence-evaluation-policies.md)).
- **Evaluation Policy** definitions (see [VP-RFC-0004](0004-evidence-evaluation-policies.md)).
- New verification outcome labels beyond `satisfied`, `not_satisfied`, and `indeterminate`.
- New **VP-RULE** definitions in this draft.
- Machine-readable **VP-CS-0003** fixture publication (deferred until acceptance path is defined).
- Amending **VP-RULE-0001** or **VP-RULE-0002** text.

---

## Proposal

### 1. Multiple evidence association

A **Claim** **MAY** reference **zero or more** **Evidence** envelopes during verification evaluation.

Each **Evidence**:

- **MUST** remain an independent envelope as defined in [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md).
- **MUST** have its own distinct `evidence_id`.
- **MUST** bind to the claim under evaluation independently via [VP-RFC-0002](0002-claim-identity-binding.md) **VP-RULE-0002** when binding rules are in scope.
- **MUST** contain exactly one **EvidenceContent** payload per envelope.

This RFC does **not** introduce a new envelope type that merges multiple contents into one evidence record.

### 2. Evidence Set

| Property | Value |
|----------|--------|
| **Term** | **Evidence Set** |
| **Definition** | The **unordered** collection of **Evidence** associated with one **Claim** during evaluation. |

Informative properties:

- An **Evidence Set** **MAY** be empty (zero evidence envelopes).
- An **Evidence Set** **MAY** contain one evidence envelope (equivalent to today's single-evidence profile).
- An **Evidence Set** **MAY** contain two or more evidence envelopes with distinct `evidence_id` values.

**Evidence Set** is a **protocol concept** for evaluation inputs. It is not a substitute for transport batching, storage containers, or domain-specific document packages unless a future RFC normatively maps those artifacts to this concept.

### 3. Normative statements (input model only)

Evaluators and scenario authors **MUST** treat the following as protocol constraints on **Evidence Set** inputs. These statements do **not** define **Evaluation Policy** or aggregated verification outcomes.

1. **Ordering independence** — Evidence ordering **MUST NOT** affect protocol meaning. Two **Evidence Sets** containing the same evidence envelopes (by `evidence_id` and semantic content) **MUST** be treated as equivalent inputs regardless of list order in a fixture or API.
2. **Structural envelope independence** — Each **Evidence** in an **Evidence Set** **MUST** remain a distinct envelope with its own `evidence_id`, `claim_id` binding, and **EvidenceContent**. This RFC does **not** define per-envelope rule evaluation procedures or how per-envelope results combine.
3. **Evaluation Policy out of scope** — How an **Evidence Set** maps to a single verification outcome **MUST** be specified only by [VP-RFC-0004](0004-evidence-evaluation-policies.md). This RFC defines **Evidence Set** membership and input shape only.

Per-envelope binding and content rules from accepted RFCs remain defined in **VP-RFC-0001** and **VP-RFC-0002**. This RFC does **not** require evaluators to run those rules or aggregate their results.

### 4. Composition (informative)

```text
Claim
 └── Assertion
      └── (evaluated against)
           Evidence Set
            ├── Evidence (evidence_id, claim_id, EvidenceContent, …)
            ├── Evidence
            └── …
```

See [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) — *Evidence Set* subsection.

### 5. VP-CS-0003

| Property | Value |
|----------|--------|
| **Scenario ID** | `VP-CS-0003` |
| **Name** | Multiple bound evidence loads successfully |
| **Rule under test** | *(none in this draft — loading profile only)* |
| **Specification binding** | As declared by scenario metadata when fixture is published |

**Inputs (normative intent):**

| Artifact | Requirement |
|----------|-------------|
| Claim | One minimal claim envelope per [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) |
| Evidence | **Two** distinct evidence envelopes |
| Binding | Each evidence `claim_id` **MUST** equal the claim `claim_id` |

**Expected behavior in this draft:**

- Scenario inputs **MUST** load without structural error.
- No normative verification outcome is defined for this scenario in this draft.

**Rationale:** **VP-CS-0003** proves that the specification and harness can represent multi-evidence inputs. Aggregated verification outcomes require [VP-RFC-0004](0004-evidence-evaluation-policies.md) and a declared **Evaluation Policy**.

**Informative note:** [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) contains an earlier narrative catalog entry also labeled **VP-CS-0003** (*Representation independence*). Reconciling executable profile IDs with long-term narrative catalog IDs **SHOULD** be resolved before fixture publication.

### 6. Compatibility

This RFC is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) and [VP-RFC-0002](0002-claim-identity-binding.md).

| Artifact | Impact |
|----------|--------|
| **VP-CS-0001** | Unchanged — single evidence envelope |
| **VP-CS-0002** | Unchanged — single evidence envelope |
| **VP-RULE-0001** | Unchanged — applies per evidence envelope when invoked |
| **VP-RULE-0002** | Unchanged — applies per evidence envelope when invoked |
| **Platform 1.1** | Unaffected — **VP-RFC-0003** and **VP-RFC-0004** are planned for joint acceptance as **Platform 1.2** |

Single-evidence implementations **MAY** continue to operate without claiming **VP-RFC-0003** support.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Verification envelope model; Evidence Set | **Extension on acceptance** — unordered multi-evidence concept |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | Multi-evidence fixtures | **Clarification on acceptance** — scenarios **MAY** declare multiple evidence records |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** in this draft |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** in this draft |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Evidence Set** | **New protocol concept** — unordered collection of **Evidence** for one **Claim** during evaluation |
| VP-TERM-008 (*Evidence*) | **Clarifying use** — remains one envelope per evidence artifact; collections are modeled via **Evidence Set** |
| VP-TERM-004 (*Verifiable Claim*) | **Clarifying use** — claim **MAY** be evaluated with zero or more evidence envelopes |

A dedicated **VP-TERM** registry entry **MAY** follow in a terminology amendment; this draft uses prose definition only.

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0003** | **Defined loading profile** — one claim, two bound evidence envelopes; verification outcome deferred |

**Harness behavior (draft):** Conformance loaders **SHOULD** accept scenario formats that declare multiple evidence records once fixture schema is published. Harnesses **MUST NOT** infer aggregated verification outcomes for multi-evidence scenarios from this RFC alone — see [VP-RFC-0004](0004-evidence-evaluation-policies.md).

Claiming **VP-RFC-0003** **SHOULD** imply **VP-RFC-0001** and **VP-RFC-0002** support but does **not** supersede their conformance requirements. Claiming **VP-RFC-0003** alone does **not** imply **Evaluation Policy** support — see [VP-RFC-0004](0004-evidence-evaluation-policies.md).

---

## Security Impact

This RFC introduces **no new cryptographic or trust semantics**. It does **not**:

- authenticate evidence presenters
- detect duplicate or forged evidence across an **Evidence Set**
- prevent replay across evaluation contexts

Multi-evidence **Evaluation Policy** and threat modeling belong in [VP-RFC-0004](0004-evidence-evaluation-policies.md) and future RFCs.

---

## Backwards Compatibility

**Additive.** Existing single-evidence scenarios, rules, and platform pins remain valid.

---

## Migration Strategy

1. Accept **VP-RFC-0003** together with [VP-RFC-0004](0004-evidence-evaluation-policies.md) as **Platform 1.2**.
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) executable profiles.
3. Extend reference interpreter evaluation context to carry an **Evidence Set** (future engineering work).
4. Publish **VP-CS-0003** fixture; publish **VP-CS-0004** fixture when multi-evidence schema and policy-aware oracle paths exist per **VP-RFC-0004**.

---

## Implementation Plan

*Informative — execution order for sibling repositories after acceptance:*

1. **veritypay-spec** — Register **VP-RFC-0003** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml); publish **VP-CS-0003** fixture when schema is approved; reconcile narrative vs executable **VP-CS-0003** catalog IDs if needed.
2. **veritypay-reference** — Extend evaluation context to accept multiple evidence envelopes; apply **Evaluation Policy** per [VP-RFC-0004](0004-evidence-evaluation-policies.md) when implemented.
3. **veritypay-tooling** — No validator change required beyond existing corpus checks unless fixture schema extensions require it.
4. **veritypay-conformance** — Extend scenario loader for multiple evidence records; **VP-CS-0003** smoke when fixture and oracle policy exist.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Evidence Set** normative definition | Complete (this draft) |
| **VP-CS-0003** scenario profile (loading intent) | Complete (this draft) |
| **VP-CS-0003** fixture | Not started |
| **Reference implementation** (multi-evidence context) | Not started |
| **Conformance execution** (multi-evidence loading) | Not started |
| **Multi-evidence evaluation policy** ([VP-RFC-0004](0004-evidence-evaluation-policies.md)) | Draft — normative text in sibling RFC |

---

## Alternatives Considered

### Alternative A — Define aggregation in this RFC

**Description:** Specify that all evidence must pass, or any one suffices.

**Why not chosen:** Premature policy; contradicts explicit deferral goal; would require new rules and oracle expectations in the same RFC.

### Alternative B — Nested evidence container envelope

**Description:** Introduce a new envelope type that wraps multiple contents.

**Why not chosen:** Breaks independent **Evidence** identity and **VP-RULE-0002** per-envelope binding model.

### Alternative C — Do nothing

**Description:** Leave multi-evidence as implementation-specific.

**Why not chosen:** Blocks realistic scenarios and splits protocol meaning across repositories.

---

## Open Questions

1. **VP-CS-0003 ID reconciliation** — Should the [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) *Representation independence* narrative move to a new ID before fixture publication?
2. **Fixture schema** — How should TOML (or successor) represent an **Evidence Set**: repeated `[evidence]` tables, `[[evidence]]` array, or named evidence keys?

**Resolved:**

- ~~**Evaluation policy RFC scope** — Should the follow-on RFC define **VP-RULE-0003** (aggregation) or extend **VP-RULE-0001** iteratively?~~ **Decision:** Aggregation is **Evaluation Policy** in [VP-RFC-0004](0004-evidence-evaluation-policies.md), not a new **VP-RULE** in this draft pair.
- ~~**Empty Evidence Set** — Is zero evidence a valid **VP-CS-0003** variant or a separate scenario?~~ **Decision:** Empty **Evidence Set** handling is an **Evaluation Policy** concern (**`ALL_REQUIRED`** → `indeterminate` per **VP-RFC-0004** §3); **VP-CS-0003** remains a two-evidence loading profile.

---

## Acceptance Criteria

- [ ] Proposal defines **Evidence Set** without payment-domain leakage
- [ ] Multiple evidence association is specified without aggregation semantics
- [ ] Normative ordering and independence statements are complete
- [ ] Evaluation semantics are **not** defined in this RFC (exclusive to [VP-RFC-0004](0004-evidence-evaluation-policies.md))
- [ ] **VP-CS-0003** loading profile is specified without normative verification outcome
- [ ] Compatibility with **VP-RFC-0001** and **VP-RFC-0002** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (draft; **Evaluation Policy** companion)
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
| 0.1.0 | 2026-06-29 | Initial draft — Evidence Set, multiple evidence association, VP-CS-0003 loading profile; Evaluation Policy deferred to VP-RFC-0004 |

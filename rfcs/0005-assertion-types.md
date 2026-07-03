---
rfc: 0005
id: 0005
concept_id: VP-RFC-0005
title: Assertion Types
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

implementation_status: not_started
last_updated: 2026-06-29
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0005

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) · [VP-RFC-0002](0002-claim-identity-binding.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) · [ECOSYSTEM.md](../ECOSYSTEM.md)

---

# RFC-0005: Assertion Types

## Summary

This RFC introduces **Assertion Type** — the protocol mechanism that determines how an **Assertion** is interpreted.

It formalizes the existing `assertion_type` field as normative protocol vocabulary. It defines exactly one initial type identifier: **`body_equality`**.

This RFC specifies **taxonomy only**. It does **not** define evaluation logic, rule dispatch, or new verification outcomes. Evaluation procedures remain in accepted rule RFCs (for example **VP-RULE-0001** in [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md)).

The change is **additive** relative to accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) and [VP-RFC-0002](0002-claim-identity-binding.md).

---

## Motivation

Future protocols require different assertion semantics. Examples include:

- body equality (current minimal slice)
- numeric comparison
- regular expression matching
- date comparison
- hash comparison
- digital signature verification

Rather than inventing protocol-specific claim formats for each domain, VerityPay needs **stable, named assertion semantics** that implementations can target consistently.

Accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) already requires each **Assertion** to carry `assertion_type` and `body`. That field selected the first minimal profile but did not define a reusable **Assertion Type** taxonomy for Phase III expansion.

---

## Problem Statement

Without normative **Assertion Type** vocabulary:

- Scenario authors cannot declare semantic intent independently of slice-specific profile labels.
- Architecture documents cannot explain how assertion interpretation evolves beyond the first minimal rule.
- Future RFCs would overload `claim_type` or ad hoc strings instead of reusing a shared protocol concept.

The specification needs **stable assertion type identifiers** that describe *what an assertion means*, while evaluation *how* remains in rule and policy RFCs.

---

## Goals

- Define **Assertion Type** as protocol vocabulary.
- Require every **Assertion** to declare exactly one **Assertion Type**.
- Standardize the initial type **`body_equality`**.
- Preserve existing **Assertion** structure (`assertion_type`, `body`).
- Enable future RFCs to add types without changing envelope shape.
- Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).

---

## Non-Goals

- Evaluation logic, rule dispatch, or interpreter behavior.
- New **VP-RULE** definitions in this draft.
- Amending **VP-RULE-0001** or **VP-RULE-0002** normative text.
- Standardizing assertion types beyond **`body_equality`** in this RFC.
- Machine-readable Assertion Type registry publication (future governance).
- Reference or conformance implementation (deferred).
- VP-CS fixture publication or amendment.

---

## Proposal

### 1. Protocol composition (informative)

```text
Claim
 └── Assertion
      ├── assertion_type  → Assertion Type (protocol identifier)
      └── body            → protocol data interpreted per type

Evidence
 └── EvidenceContent
      └── body            → compared or consumed per rules in scope

        ↓ (evaluation — out of scope for this RFC)

     Outcome
```

**Assertion Type** names *how* an assertion body is interpreted. **Evaluation** — which rules run, in what order, and how outcomes aggregate — remains defined by accepted rule RFCs and [VP-RFC-0004](0004-evidence-evaluation-policies.md).

### 2. Assertion Type

| Property | Value |
|----------|--------|
| **Term** | **Assertion Type** |
| **Definition** | A protocol identifier describing the semantic interpretation of an **Assertion**. |
| **Field** | `assertion_type` on **Assertion** |

Normative requirements:

1. Every **Assertion** **MUST** declare exactly one **Assertion Type** via `assertion_type`.
2. **Assertion Type** identifiers **MUST** be stable protocol strings — not implementation class names, library paths, or version-specific labels.
3. **Assertion Type** identifiers **MUST NOT** encode implementation details (language, framework, storage, or vendor).
4. The **Assertion** `body` **MUST** be treated as opaque protocol data whose meaning is defined by the declared **Assertion Type** and applicable rules in scope.

This RFC does **not** define how evaluators select or dispatch rules from an **Assertion Type**. That remains future specification work.

### 3. Initial Assertion Type — `body_equality`

| Property | Value |
|----------|--------|
| **Type ID** | `body_equality` |
| **Name** | Body equality |
| **Meaning** | The assertion body is evaluated using **VP-RULE-0001** (*Assertion Body Evidence Match*) per [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) when that rule's preconditions are satisfied. |

**Informative mapping:** Accepted **VP-CS-0001** and **VP-CS-0002** exercise **`body_equality`** semantics through **VP-RULE-0001** when applicable. Fixture `assertion_type` strings remain as published under **VP-RFC-0001** (`minimal`) until a future fixture-alignment change; semantic interpretation is **`body_equality`** regardless of fixture label reconciliation timing.

No additional **Assertion Types** are standardized in this draft.

### 4. Future compatibility

Future RFCs **MAY** define additional **Assertion Types** without changing **Assertion** envelope structure. Informative examples (not normative in this RFC):

| Example type ID | Informative meaning |
|-----------------|---------------------|
| `numeric_range` | Numeric comparison against evidence |
| `regex` | Regular expression match |
| `contains` | Substring containment |
| `starts_with` | Prefix match |
| `ends_with` | Suffix match |
| `json_pointer` | JSON Pointer value extraction and comparison |
| `schema_match` | Schema validation of body |
| `hash_match` | Cryptographic hash comparison |
| `signature` | Digital signature verification |

Each future type **MUST** be defined in its own RFC or an amendment to this taxonomy with stable identifier, semantic definition, and applicable rules — not merely listed.

### 5. Compatibility with VP-RFC-0001

Accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) requires `assertion_type = minimal` for **VP-RULE-0001** applicability in the first minimal profile.

| Artifact | Impact |
|----------|--------|
| **Assertion** shape | Unchanged — `assertion_type`, `body` |
| **VP-RULE-0001** | Unchanged — rule text not amended in this draft |
| **VP-CS-0001** / **VP-CS-0002** | Unchanged fixtures — **`body_equality`** semantics via existing rule pipeline |
| **Platform 1.2** | Unaffected — draft taxonomy only until acceptance |

Implementations **MAY** continue using **VP-RFC-0001** profile labels until they opt into **Assertion Type** taxonomy claims.

---

## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | Assertion; `assertion_type` | **Extension on acceptance** — **Assertion Type** subsection |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | Scenario inputs | **Clarification on acceptance** — fixtures **MAY** declare `assertion_type`; **`body_equality`** initial standard |
| [BEHAVIOR_MODEL.md](../docs/01-architecture/BEHAVIOR_MODEL.md) | — | **None** in this draft |
| [STATE_MODEL.md](../docs/01-architecture/STATE_MODEL.md) | — | **None** in this draft |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **Assertion Type** | **New protocol concept** — semantic interpretation identifier for **Assertion** |
| **`body_equality`** | **New type identifier** — body comparison via **VP-RULE-0001** |
| VP-TERM-013 (*Assertion*) | **Clarifying use** — `assertion_type` names **Assertion Type**; `body` is protocol data |

A dedicated **VP-TERM** registry entry **MAY** follow in a terminology amendment.

---

## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| **VP-CS-0001** | **Semantic alignment** — exercises **`body_equality`** via **VP-RULE-0001**; fixture unchanged |
| **VP-CS-0002** | **Semantic alignment** — binding scenario; **`body_equality`** applies when content rule runs |

**Harness behavior (draft):** VP-CS fixtures **MAY** specify `assertion_type`. The initial standardized **Assertion Type** in this RFC is **`body_equality`**. This RFC does **not** define evaluator dispatch from `assertion_type` to rules — conformance continues to compare implementations against the reference oracle under existing scenario bindings.

Claiming **VP-RFC-0005** **SHOULD** imply **VP-RFC-0001** support but does **not** supersede its conformance requirements.

---

## Security Impact

This RFC introduces **no new cryptographic or trust semantics**. It names interpretation categories only. Threat modeling for future types (for example `signature`, `hash_match`) belongs in their defining RFCs.

---

## Backwards Compatibility

**Additive.** Existing envelopes, rules, scenarios, and Platform 1.2 pins remain valid.

---

## Migration Strategy

1. Accept **VP-RFC-0005** when governance approves.
2. Align [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) and [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md).
3. ~~Register **VP-RFC-0005** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft.~~ **Done.**
4. Future work: fixture `assertion_type` string alignment (`minimal` → `body_equality`), evaluator dispatch RFC, reference interpreter type routing.

---

## Implementation Plan

*Informative — deferred:*

1. **veritypay-spec** — Register **VP-RFC-0005**; optional fixture alignment RFC.
2. **veritypay-reference** — Map **Assertion Type** to rule dispatch when a follow-on RFC or acceptance path defines it.
3. **veritypay-tooling** — No validator change required beyond existing corpus checks unless Assertion Type registry is introduced.
4. **veritypay-conformance** — Document **`body_equality`** in scenario schema when dispatch is normative.

No code changes are part of this draft RFC.

### Implementation status

| Deliverable | Status |
|-------------|--------|
| **Assertion Type** / **`body_equality`** normative taxonomy | Complete (this draft) |
| **VP-RFC-0005** registry entry (draft) | Complete |
| **Reference implementation** (type dispatch) | Not started |
| **Conformance execution** (type-aware dispatch) | Not started |

---

## Alternatives Considered

### Alternative A — Define evaluation dispatch in this RFC

**Description:** Specify rule selection from `assertion_type` in the same document.

**Why not chosen:** Violates separation goal; evaluation belongs in rule RFCs and interpreter specifications.

### Alternative B — Encode types in `claim_type`

**Description:** Use claim-level typing only.

**Why not chosen:** Conflates envelope classification with assertion semantics; blocks multiple assertion models per claim type.

### Alternative C — Do nothing

**Description:** Leave `assertion_type` as profile-specific strings only.

**Why not chosen:** Blocks extensible assertion semantics without new claim formats.

---

## Open Questions

1. **Fixture alignment** — Should **VP-CS-0001** / **VP-CS-0002** change `assertion_type` from `minimal` to `body_equality`, or should **`minimal`** remain a profile label mapped to **`body_equality`**?
2. **Registry shape** — Should **Assertion Types** live in a dedicated registry or remain RFC-defined until volume warrants automation?
3. **Dispatch RFC** — Should rule selection from **Assertion Type** be a new **VP-RULE** registry RFC or interpreter contract amendment?

---

## Acceptance Criteria

- [ ] **Assertion Type** is defined without payment-domain leakage
- [ ] Every **Assertion** is required to declare exactly one type
- [ ] **`body_equality`** is defined without amending **VP-RULE-0001** text
- [ ] No evaluation logic or dispatch is defined in this RFC
- [ ] Future type extensibility is documented without standardizing additional types
- [ ] Compatibility with **VP-RFC-0001** and **VP-RFC-0002** is documented
- [ ] Architecture, terminology, conformance, security, compatibility, and migration sections are complete
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0004](0004-evidence-evaluation-policies.md) — Evidence Evaluation Policies (accepted)
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
| 0.1.0 | 2026-06-29 | Initial draft — Assertion Type taxonomy, `body_equality`; evaluation deferred |

---
spec: SPEC-0301
title: VerityPay Conformance Model
status: Draft
version: 0.1.0

category: Development

authors:
  - VerityPay Core Team

reviewers: []

depends_on:
  - PRINCIPLES
  - GLOSSARY
  - DOMAIN_MODEL
  - IDENTITY_MODEL
  - BEHAVIOR_MODEL
  - DATA_MODEL
  - STATE_MODEL

required_by:
  - RFCs

implementation_repositories:
  - veritypay

last_updated: 2026-06-29
---

**Pyramid level:** L3 — Conformance · **Status:** draft · **Version:** 0.1.0

**Constitutional basis:** [PRINCIPLES.md](../00-overview/PRINCIPLES.md), [GLOSSARY.md](../00-overview/GLOSSARY.md)

**Related documents:** [GOVERNANCE.md](../05-governance/GOVERNANCE.md), [VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md) (accepted), [VP-RFC-0003](../../rfcs/0003-multiple-evidence.md) (accepted), [VP-RFC-0004](../../rfcs/0004-evidence-evaluation-policies.md) (accepted), [VP-RFC-0005](../../rfcs/0005-assertion-types.md) (draft), [`../../rfcs/`](../../rfcs/)

---

# VerityPay Conformance Model

> *A protocol that cannot determine whether an implementation conforms to it is not yet a protocol.*

---

## Why this exists

The purpose of the VerityPay specification is not to produce **one implementation**.

It is to enable **many independent implementations** that can interoperate without prior coordination.

**Conformance** is therefore not a testing activity bolted on at the end. It is the engineering discipline that allows independently developed software to **speak the same protocol**.

Every project can publish a whitepaper. Every project can publish architecture diagrams. Very few publish **how you prove you implemented the protocol correctly**.

HTTP works because browsers and servers can disagree on everything except whether they satisfied the same normative rules. TLS works because independent stacks negotiate and verify the same semantics. SQL became a standard because different engines could run the same queries and expect compatible results.

VerityPay aims for that class of interoperability: **shared meaning**, not shared code.

An implementer in Rust, TypeScript, Go, Java, Solidity, Move, or Cairo should ask one question:

**"Am I conforming?"**

This document answers it.

---

## Executable conformance flow

The platform now runs an end-to-end conformance path for the first protocol slice. Scenario **meaning** remains normative in this repository and in accepted RFCs; **expected verification outcomes** come from the **reference interpreter** oracle; **conformance** compares an implementation adapter against that oracle.

```text
VP-CS scenario (fixture + narrative)
        ↓
Reference Interpreter  →  VerificationResult
        ↓
Conformance comparison  →  ConformanceResult (pass / fail)
        ↓
Implementation adapter  →  ComparableResult
```

| Stage | Owner | Role |
|-------|-------|------|
| **VP-CS** | `veritypay-spec` | Defines scenario inputs, rule under test, and binding; [`VP-CS-0001`](../../spec/conformance/scenarios/VP-CS-0001.toml) per [VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md) (accepted); [`VP-CS-0002`](../../spec/conformance/scenarios/VP-CS-0002.toml) per [VP-RFC-0002](../../rfcs/0002-claim-identity-binding.md) (accepted) |
| **Reference Interpreter** | `veritypay-reference` | Implements **VP-RULE-0001** and produces a **VerificationResult** (outcome, evaluated claim, specification binding) |
| **Conformance harness** | `veritypay-conformance` | Loads spec-published fixtures, runs oracle and adapter, compares outcomes |

**Scenario meaning is normative.** The TOML fixture and RFC text define what is under test—not harness code.

**Expected outcomes come from the reference interpreter.** The fixture `expected.outcome` field records the oracle expectation for **VP-CS-0001**; it is a test oracle pin, not a substitute for rule text in [VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md).

**Conformance compares implementations against that oracle.** A harness **pass** means the adapter's verification outcome, evaluated claim id, and specification binding match the reference path for the loaded scenario—not that the implementation reimplemented rule logic independently.

**VP-CS-0001** is the first scenario exercised through this flow: minimal claim and evidence envelopes, **VP-RULE-0001**, expected oracle outcome `satisfied` for the normative fixture inputs. The L5 interoperability narrative below describes long-term multi-implementation intent; the executable profile is defined by [VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md).

**VP-CS-0002** exercises **VP-RULE-0002** (*Evidence Claim Binding*): evidence whose `claim_id` does not match the claim under evaluation yields oracle outcome `indeterminate` even when content bodies match. Machine-readable fixture: [`../../spec/conformance/scenarios/VP-CS-0002.toml`](../../spec/conformance/scenarios/VP-CS-0002.toml) per [VP-RFC-0002](../../rfcs/0002-claim-identity-binding.md). The supersession narrative under [VP-CS-0002 — Supersession preserves history](#vp-cs-0002-supersession-preserves-history) below remains a separate long-term catalog entry pending ID reconciliation.

### Multiple evidence and evaluation policy (VP-RFC-0003, VP-RFC-0004)

Accepted protocol RFCs **VP-RFC-0003** and **VP-RFC-0004** form **Platform 1.2**. They split responsibilities:

| RFC | Concept | Scope |
|-----|---------|--------|
| [VP-RFC-0003](../../rfcs/0003-multiple-evidence.md) (accepted) | **Evidence Set** | Input model — zero or more **Evidence** envelopes per **Claim**; ordering independence; **VP-CS-0003** loading profile |
| [VP-RFC-0004](../../rfcs/0004-evidence-evaluation-policies.md) (accepted) | **Evaluation Policy** | Aggregation — how an **Evidence Set** maps to one verification outcome; initial policy **`ALL_REQUIRED`**; **VP-CS-0004** profile |

[VP-RFC-0003](../../rfcs/0003-multiple-evidence.md) (accepted) introduces **Evidence Set** — an **unordered** collection of **Evidence** envelopes associated with one **Claim** during evaluation.

Future VP-CS scenario fixtures **MAY** declare **multiple Evidence records** for one claim (for example two independently bound envelopes). Scenario loaders **SHOULD** treat evidence list ordering as non-normative once multi-evidence fixture schema is published.

[VP-RFC-0004](../../rfcs/0004-evidence-evaluation-policies.md) (accepted) defines **Evaluation Policy** — how per-envelope verification outcomes over an **Evidence Set** combine into one verification outcome.

Future VP-CS scenario fixtures **MAY** declare an **Evaluation Policy** identifier. The initial normative policy in that RFC is **`ALL_REQUIRED`**: every applicable evidence envelope must be `satisfied` for aggregate `satisfied`; any `not_satisfied` dominates; otherwise any `indeterminate` (with no `not_satisfied`) yields aggregate `indeterminate`; an empty **Evidence Set** yields `indeterminate`.

This model does **not** define future policies beyond **`ALL_REQUIRED`**. Trust, weighting, and authorization remain out of scope.

**VP-CS-0003** ([VP-RFC-0003](../../rfcs/0003-multiple-evidence.md)) is a **loading profile** only — no normative verification outcome. **VP-CS-0004** ([VP-RFC-0004](../../rfcs/0004-evidence-evaluation-policies.md)) is the **`ALL_REQUIRED`** aggregation profile (fixture deferred). Both require reconciling narrative catalog ID collisions before fixture publication — see notes under [VP-CS-0003 — Representation independence](#vp-cs-0003-representation-independence) and [VP-CS-0004 — Identity immutability](#vp-cs-0004-identity-immutability).

### Assertion Types in scenarios (VP-RFC-0005)

[VP-RFC-0005](../../rfcs/0005-assertion-types.md) (draft) introduces **Assertion Type** — the protocol identifier describing how an **Assertion** is interpreted.

VP-CS scenario fixtures **MAY** specify `assertion_type` on claim inputs. The initial standardized **Assertion Type** in that RFC is **`body_equality`**: assertion body evaluation via **VP-RULE-0001** when applicable rule preconditions hold.

**VP-CS-0001** and **VP-CS-0002** exercise **`body_equality`** semantics through the existing **VP-RULE-0001** / **VP-RULE-0002** pipeline. Published fixtures retain `assertion_type = minimal` per accepted **VP-RFC-0001** until a future fixture-alignment change.

**Assertion Types** describe protocol semantics. Conformance compares independent implementations of those semantics against the reference oracle — not ad hoc string handling in harnesses alone. This RFC does **not** define evaluator dispatch from `assertion_type` to rules; oracle comparison remains rule- and scenario-bound per accepted RFCs.

Harness verdict vocabulary (`pass` / `fail` / `skip` / `error`) remains distinct from verification outcomes (`satisfied` / `not_satisfied` / `indeterminate`) defined in this model and in the RFC.

---

<a id="cm-2-1"></a>

## Philosophy of conformance

### What it means to "speak VerityPay"

To **speak VerityPay** is to:

1. Use the **same concepts** ([GLOSSARY.md](../00-overview/GLOSSARY.md))
2. **Represent** protocol objects with required semantics ([DATA_MODEL.md](../01-architecture/DATA_MODEL.md))
3. **Behave** according to canonical verbs and invariants ([BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md))
4. **Evolve** objects through valid knowledge states ([STATE_MODEL.md](../01-architecture/STATE_MODEL.md))
5. **Interoperate** with another conforming party at the same **specification version**

Conformance is **protocol-first**. We test whether an implementation means the same thing—not whether it uses our repository layout, our database, or our UI.

### Shared meaning over shared code

Most blockchain projects optimize for **shared code**. VerityPay optimizes for **shared meaning**.

That is a harder problem. It is also the problem worth solving if the protocol should outlive any single team.

### Conformance is not certification (yet)

This model defines **what conformity means** and **how it is demonstrated**. Formal third-party certification may follow ([Future certification](#future-certification)). Until then, self-assessment against published **conformance scenarios** and RFC requirements is the baseline.

---

## Conformance pyramid

Not all implementations conform **equally**. The pyramid defines measurable levels—from vocabulary to wire-level interoperability.

```
                    ┌─────────────────────────┐
                    │  L5 — Protocol          │
                    │  Conformance            │
                    │  (interoperability)     │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  L4 — State             │
                    │  Conformance            │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  L3 — Behavioral        │
                    │  Conformance            │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  L2 — Representation      │
                    │  Conformance            │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  L1 — Semantic          │
                    │  Conformance            │
                    └─────────────────────────┘
```

Higher levels **include** lower levels. An implementation claiming L4 MUST satisfy L1–L3.

---

## Conformance levels

### Level 1 — Semantic conformance

**Question:** Does your software understand the **same concepts**?

| Check | Source |
|-------|--------|
| Terms match [GLOSSARY.md](../00-overview/GLOSSARY.md) | Claim, evidence, verification, outcome, identity |
| Assertion ≠ verification | [PRINCIPLES.md](../00-overview/PRINCIPLES.md) Principle 3 |
| Protocol truth ≠ worldly fact | [DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) truth model |
| Deprecated terms avoided in public APIs and docs | Glossary deprecated table |

This is **language**, not code. SDKs and documentation at L1 use canonical vocabulary consistently.

**Example claim:** *"Our product supports VerityPay claims and verification outcomes—not transactions marked verified."*

---

### Level 2 — Representation conformance

**Question:** Can your implementation **represent** protocol objects correctly?

| Object | Minimum representation checks |
|--------|------------------------------|
| Verifiable Claim | Required attributes; no embedded outcome; immutable content after assertion |
| Verification Record | Declared evidence; explicit outcome; specification version |
| Evidence | Distinct identity; no embedded verification result |
| Participant / Role | Explicit role attribution on assert and verify |

Behavior is not exercised yet—only **shape and guarantees** ([DATA_MODEL.md](../01-architecture/DATA_MODEL.md) representation guarantees G1–G10).

**Example claim:** *"Our SDK is Level 2—we serialize conformant claim and verification record structures."*

---

### Level 3 — Behavioral conformance

**Question:** Given the same inputs, does your implementation **behave** correctly?

| Behavior | Source |
|----------|--------|
| `assert` does not imply verification | [BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md) B1 |
| `verify` + `record outcome` produce explicit outcomes | B4 |
| Evidence and specification version declared | B2, B3 |
| Supersession does not rewrite identity | B5 |
| Re-verification creates new verification record | B8 |

**Example flow:**

```
assert(claim)
    ↓
provide evidence(...)
    ↓
verify(claim, evidence, spec_version)
    ↓
record outcome → satisfied | not_satisfied | indeterminate
```

---

### Level 4 — State conformance

**Question:** Do objects **evolve** correctly?

| Check | Source |
|-------|--------|
| Valid transitions only | [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) |
| Invalid transitions rejected | e.g., Finalized → Started ❌ |
| Knowledge states match behavior-gated transitions | Behavior causes state |
| Retired claims inactive for new verification | State invariants S2 |

Immutable transitions and lifecycle guarantees are **testable**—not inferred from UI.

**Example claim:** *"Our interpreter passes VP-CS-0005 state scenarios."*

---

### Level 5 — Protocol conformance

**Question:** Can you **exchange information** with another independent implementation and agree on results?

| Check | Meaning |
|-------|---------|
| Same claim + evidence + spec version | Compatible **verification outcome** |
| Cross-implementation scenario pass | [Conformance scenarios](#conformance-scenarios) |
| No bilateral custom rules for core behavior | [PRINCIPLES.md](../00-overview/PRINCIPLES.md) Principle 4 |

This is the **real goal**—interoperability without prior coordination.

**Example claim:** *"Our node is Level 5 against reference interpreter at vp-spec-2026-06."*

---

## What must conform

### Normative conformance targets

These layers **MUST** conform for an implementation to speak VerityPay at a declared specification version:

| Target | Governs | Primary source |
|--------|---------|----------------|
| **Domain semantics** | Nouns, truth model, trust assumptions | [DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) |
| **Identity** | Semantic stability, referential rules | [IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md) |
| **Behavior** | Verbs, events, behavioral invariants | [BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md) |
| **Representation** | Entities, attributes, representation guarantees | [DATA_MODEL.md](../01-architecture/DATA_MODEL.md) |
| **State** | Knowledge states, invalid transitions | [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) |
| **Versioning** | Specification version binding | [GLOSSARY.md](../00-overview/GLOSSARY.md) · accepted RFCs |

Accepted **RFCs** may add normative targets. Draft RFCs do not.

### Conformance matrix

| Layer | Conformance required |
|-------|:--------------------:|
| Domain | ✓ |
| Identity | ✓ |
| Behavior | ✓ |
| Representation | ✓ |
| State | ✓ |
| UI / UX | ✗ |
| Database schema | ✗ |
| Transport (HTTP, gRPC, chain RPC) | ✗ |
| Blockchain / VM choice | ✗ |
| Programming language | ✗ |
| Cloud provider | ✗ |

Optional layers MAY conform to published profiles (e.g., transport bindings) when RFCs define them—they are not required to speak core VerityPay.

---

## What does not need to conform

| Category | Examples | Why excluded |
|----------|----------|--------------|
| **Informative material** | Tutorials, README prose, diagrams | Educate; do not bind behavior |
| **Examples** | Sample JSON in appendix | Illustrative unless RFC promotes |
| **Internal storage** | Postgres vs SQLite, row layout | [Storage identifier](../00-overview/GLOSSARY.md#storage-identifier) ≠ semantics |
| **Internal APIs** | Private function names | No normative meaning |
| **Product workflows** | [`02-product/`](../02-product/) | Participant view, not protocol |
| **Performance optimizations** | Caching, batching | Allowed if observable protocol behavior unchanged |

**Informative** content helps adoption. **Normative** content defines conformity. Do not confuse them in conformance claims.

---

<a id="cm-6-1"></a>

## Conformance scenarios

**Conformance scenarios** are not unit tests. They are **specifications of protocol stories**—declarative descriptions independent implementations MUST reproduce.

Scenarios are identified as **VP-CS-NNNN** (VerityPay Conformance Scenario). Executable runners live in implementation repositories; **the scenario text here is authoritative**.

### Scenario template

Each scenario defines:

| Field | Content |
|-------|---------|
| **ID** | VP-CS-NNNN |
| **Title** | Short name |
| **Level** | Minimum pyramid level tested |
| **Specification version** | e.g., `vp-spec-2026-06` |
| **Setup** | Participants, claims, evidence, versions |
| **Actions** | Canonical verbs in order |
| **Expected protocol knowledge** | Outcomes, states, invariants |
| **Interoperability check** | (if L5) second implementation must agree |

---

### VP-CS-0001 — Independent verification agreement

**Level:** L5 (includes L1–L4)

**Story:** Two independent implementations receive the same payment claim and identical evidence under the same specification version, run verification, and produce the same **verification outcome**.

**Setup**

- Participant Alice (claimant) asserts payment claim `clm_pay_001` against spec `vp-spec-2026-06`
- Evidence `evd_bank_batch` and `evd_prior_instruction` provided
- Participant Bob (verifier) evaluates

**Actions**

1. `assert(claim)`
2. `provide evidence(evd_bank_batch, evd_prior_instruction)`
3. `verify(claim, evidence, vp-spec-2026-06)`
4. `record outcome`

**Expected**

- Verification record finalizes with `outcome_value: satisfied` (or same `indeterminate` with same declared reason on both sides)
- Claim content unchanged
- Implementation A and Implementation B produce **compatible outcomes**

**Machine-readable fixture (executable profile):** [`../../spec/conformance/scenarios/VP-CS-0001.toml`](../../spec/conformance/scenarios/VP-CS-0001.toml) — inputs and expected oracle outcome per [VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md) (accepted). The narrative above describes L5 interoperability intent; the fixture defines the minimal executable profile implemented by `veritypay-reference` and `veritypay-conformance`.

---

### VP-CS-0002 — Supersession preserves history

**Level:** L4

**Story:** A claim is superseded; the original remains historically referenceable; independent implementations agree on identity and authority.

**Setup**

- Claim `clm_A` asserted and verification finalized `not_satisfied`
- Claim `clm_B` asserted with `supersedes_ref: clm_A`

**Actions**

1. `supersede` via assertion of `clm_B`
2. `reference(clm_A)` from audit trace

**Expected**

- `clm_A` identity and content unchanged
- `clm_A` knowledge state includes **Superseded**
- `clm_B` is distinct identity
- Both implementations resolve `clm_A` and `clm_B` as separate stable objects

---

### VP-CS-0003 — Representation independence

**Level:** L2–L5

**Story:** Two representations (e.g., different JSON field ordering or optional encoding) carry the **same semantics**; conforming parsers produce the same protocol objects and outcomes.

**Setup**

- Representation A and Representation B of the same asserted claim and verification inputs
- Semantically identical content and references

**Expected**

- Semantic identity equivalent after parse
- Verification produces compatible outcome
- Neither representation is privileged as "the wire format" unless an RFC names one normative encoding

---

### VP-CS-0004 — Identity immutability

**Level:** L2–L4

**Story:** After assertion, claim content cannot mutate in place; non-conforming mutation attempts are detectable.

**Setup**

- Claim `clm_001` asserted with fixed content

**Actions**

- Attempt in-place content mutation (implementation-internal or adversarial test harness)

**Expected**

- Conforming implementations reject or refuse to apply mutation
- Original semantic identity and content remain auditable
- Violation flagged as **non-conformance** (see below)

---

### VP-CS-0005 — State invalid transitions

**Level:** L4

**Story:** Finalized verification records cannot return to in-progress; retired claims cannot accept new verification.

**Actions attempted**

1. Finalized verification → Started ❌
2. `verify()` on retired claim ❌

**Expected**

- Transition rejected per [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) invalid transitions table
- Protocol knowledge unchanged by invalid action

---

### Conformance suite roadmap

| ID | Title | Focus |
|----|-------|-------|
| VP-CS-0001 | Independent verification agreement | L5 interoperability |
| VP-CS-0002 | Supersession preserves history | Identity + state |
| VP-CS-0003 | Representation independence | L2+ encoding |
| VP-CS-0004 | Identity immutability | Representation guarantees |
| VP-CS-0005 | State invalid transitions | State invariants |
| VP-CS-0006+ | *(forthcoming via RFC)* | Payment domain claim types, indeterminate edge cases |

Future scenarios are added through RFC or governed amendment to this document—never only in a private test repo.

---

## Non-conformance

Non-conformance means an implementation **claims VerityPay compatibility** but violates normative semantics, behavior, representation guarantees, or state rules.

| Implementation action | Conforming? | Why |
|----------------------|:-----------:|-----|
| Changes claim meaning after assertion | ❌ | Violates identity + representation guarantee G1 |
| Stores claim in PostgreSQL vs SQLite | ✓ | Storage is not normative |
| Embeds `verified: true` on claim object | ❌ | Collapses assertion and verification |
| Uses different JSON key order | ✓ | If semantics preserved (VP-CS-0003) |
| Produces different outcome for same inputs | ❌ | Violates reproducible outcomes (Principle 8) |
| Skips evidence declaration on finalize | ❌ | Behavioral invariant B2 |
| Rewrites finalized verification record | ❌ | State invariant S1 |

**Detection:** conformance scenarios, RFC review, cross-implementation testing, audit of public API/docs for deprecated terminology.

**Remediation:** fix implementation, or change specification through RFC—never silent "compatible enough."

---

## Version compatibility

| Concept | Rule |
|---------|------|
| **Declaration** | Implementations MUST declare target **specification version** |
| **Strict mode** | Conformance is assessed against declared version + accepted RFC set |
| **Mixed versions** | Verification MUST declare version; outcomes interpreted under that version |
| **Deprecation** | Deprecated versions remain auditable; new conformance targets use current version |
| **RFC supersession** | When RFC supersedes behavior, scenarios updated; old scenarios retained for historical versions |

Forward compatibility is a product choice; **protocol conformance** is always version-specific.

---

## RFC conformance impact

Every RFC MUST include a **Conformance Impact** section—mandatory alongside motivation and alternatives.

### Template

```markdown
## Conformance Impact

| Area | Changed? | Summary |
|------|:--------:|---------|
| Semantics (glossary / domain) | [ ] | |
| Representation (data model) | [ ] | |
| Behavior (verbs / invariants) | [ ] | |
| State (lifecycles / invalid transitions) | [ ] | |
| Interoperability (L5 scenarios) | [ ] | |

### New or amended scenarios
- VP-CS-____ — (title) or None

### Conformance level affected
L1 / L2 / L3 / L4 / L5 / None

### Backward compatibility
Breaking / Compatible / N/A
```

Reviewers MUST reject RFCs that change normative behavior without conformance impact analysis.

---

## Future certification

VerityPay may later establish:

| Mechanism | Purpose |
|-----------|---------|
| **Public conformance suite** | Versioned VP-CS scenarios in this repository |
| **Self-attestation** | Implementations publish level achieved + spec version |
| **Independent verification** | Third-party labs or cross-vendor test events |
| **Trademark / badge policy** | "VerityPay Conformant" usage rules (governance + legal) |

This model defines **meaning** of conformance; certification defines **attestation**—a separate governance decision.

---

## Relationship to RFCs

| Artifact | Role |
|----------|------|
| **Accepted RFCs** | Add or amend normative requirements conformance MUST satisfy |
| **This model** | Framework for levels, scenarios, and RFC impact |
| **Architecture Alpha** | Frozen semantic foundation scenarios implement |
| **[GOVERNANCE.md](../05-governance/GOVERNANCE.md)** | Acceptance process; Architecture freeze |
| **[PRINCIPLES.md](../00-overview/PRINCIPLES.md)** | Principle 10 — conformance is the goal |
| **Implementation repos** | Run tests; do not define conformity |

RFC `implementation_status` is informational. **Passing scenarios at declared version** is the engineering standard for interoperability claims.

---

## Relationship to other documents

| Document | Relationship |
|----------|--------------|
| [GLOSSARY.md](../00-overview/GLOSSARY.md) | L1 semantic conformance vocabulary |
| [Architecture](../01-architecture/) | Normative structure scenarios exercise |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Contributor levels map to pyramid levels |
| [03-development/](.) | Conformance criteria live here; runners elsewhere |

---

## Specification v1.0 freeze alignment

Conformance completes the **specification spine** for implementation:

```
Constitutional layer  ✓
Architecture Alpha    ✓ (frozen)
Conformance model     ✓ (this document, draft)
→ Specification v1.0 freeze milestone
→ Ecosystem scaffolding (.github, reference repo)
→ Founding Sprint 1 implementation issues
```

---

## Closing

The goal of VerityPay is not that every implementation **looks** the same.

The goal is that every conforming implementation **means** the same thing.

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-06-29 | Initial conformance model; pyramid, scenarios VP-CS-0001–0005, RFC impact template |

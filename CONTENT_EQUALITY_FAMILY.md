# Content Equality Family

**Status:** Family Specification *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the **Content Equality** assertion family — the first and foundational family in the [Assertion Type Taxonomy](ASSERTION_TAXONOMY.md). This document is **not** a protocol RFC. It introduces **no protocol semantics**. Each candidate type requires an independent RFC before it becomes normative.

---

## Purpose

Content Equality is the **foundational assertion family** in Verity because it addresses the simplest verifiable question: *does evidence content match what the assertion claims?*

Before protocols can evaluate signatures, schemas, time bounds, or authorization scopes, they must be able to compare **semantic content** — the payload carried in an assertion body against the payload carried in evidence. Content Equality types answer that question under progressively richer comparison models, from literal string match to canonicalized structured data to digest-based agreement.

This family is foundational for three reasons:

1. **Minimal dependencies** — content comparison requires only assertion body, evidence content, and linkage preconditions. It does not require trust policies, issuers, or credential infrastructure.
2. **Platform bootstrap** — accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) and draft [VP-RFC-0005](rfcs/0005-assertion-types.md) already anchor the platform on literal body comparison (**`body_equality`** via **VP-RULE-0001**).
3. **Extension path** — additional members of this family add comparison semantics without changing Verity Core execution infrastructure (claims, evidence sets, evaluation policies, evaluator dispatch).

Future families — Structural, Cryptographic, Temporal, and others — build on the expectation that content can first be identified and compared reliably. Content Equality establishes that baseline.

---

## Family Overview

All assertion types in the **Content Equality** family share one semantic goal:

**Determine whether assertion content and evidence content represent the same value under a defined comparison model.**

Every member compares **semantic content**. Members differ in **how** comparison is performed:

| Comparison model | Question asked |
|------------------|----------------|
| Literal | Are the raw payloads identical? |
| Normalized | Are the payloads identical after defined normalization? |
| Canonical | Are structured payloads identical after canonical serialization? |
| Binary | Are opaque byte sequences identical? |
| Digest | Does evidence content digest match the asserted digest value? |

Each member is a distinct **`assertion_type`** with its own evaluator and rule(s). Members **MUST NOT** overload one another's identifiers or silently change comparison behavior. Unknown types yield `indeterminate` per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

This document describes the family. It does not assign normative outcome tables, preconditions, or wire encodings.

---

## Candidate Types

The table below lists **candidate** Content Equality types for research and RFC planning. Status reflects this document only — not registry or RFC state.

| Type | Description | Potential RFC | Initial status |
|------|-------------|---------------|----------------|
| **`body_equality`** | Literal comparison of assertion `body` to evidence `content.body` via exact Unicode string equality; no normalization or hashing | [VP-RFC-0005](rfcs/0005-assertion-types.md) | **Draft** — type identifier proposed; evaluation via accepted **VP-RULE-0001** |
| **`normalized_text`** | Compare assertion and evidence text after the Platform 1.3 normalization pipeline defined in [VP-RFC-0011](rfcs/0011-normalized-text-assertion.md): Unicode NFC, trim leading/trailing whitespace, collapse internal whitespace to one ASCII space, then case-sensitive equality — no locale rules, no case folding, no compatibility normalization | [VP-RFC-0011](rfcs/0011-normalized-text-assertion.md) | **Draft** — type and **VP-RULE-0011** proposed; future Platform 1.3 candidate |
| **`canonical_json`** | JSON value comparison after canonical serialization (stable key ordering, number formatting, whitespace policy) | VP-RFC-0012 *(informative placeholder)* | **Research** |
| **`canonical_xml`** | XML infoset or canonical XML comparison under a defined canonicalization algorithm | VP-RFC-0013 *(informative placeholder)* | **Research** |
| **`binary_equality`** | Exact comparison of opaque binary payloads (encoding and representation rules to be defined by RFC) | VP-RFC-0014 *(informative placeholder)* | **Research** |
| **`hash_equality`** *(future)* | Assertion carries an expected digest; evidence content is hashed under a defined algorithm and compared to the asserted value | VP-RFC-0015 *(informative placeholder)* | **Research** — future; may overlap Cryptographic family boundaries |

**No candidate type beyond `body_equality` is standardized by this document.** Potential RFC numbers are planning placeholders assigned per [VP-RFC-0000](rfcs/0000-rfc-process.md) at proposal time.

---

## Design Principles

Content Equality types should adhere to the following design principles when proposed for standardization. These principles guide RFC authors; they are **not** normative requirements introduced here.

| Principle | Meaning |
|-----------|---------|
| **Deterministic** | Identical assertion body, evidence content, and evaluation context **MUST** yield the same outcome. Comparison algorithms **MUST NOT** depend on locale, runtime, or implementation-specific floating-point behavior unless explicitly specified. |
| **Canonical** | When normalization or serialization is required, the RFC **MUST** name the canonical form explicitly. "Best effort" parsing or vendor-default JSON/XML behavior is insufficient. |
| **Independent of formatting** | Types intended to compare semantic value (for example `canonical_json`, `normalized_text`) **MUST** document which formatting differences are ignored and which are significant. |
| **Implementation-independent** | Comparison semantics **MUST** be fully specified in the RFC. Two conforming implementations **MUST** agree on outcomes for all specified inputs without shared libraries. |

These principles extend the taxonomy philosophy in [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) for the Content Equality family specifically.

---

## Relationship to VP-RULE-0001

Accepted **VP-RULE-0001** (*Assertion Body Evidence Match*) in [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) currently implements **only** the literal comparison model associated with **`body_equality`**:

- Compares `claim.assertion.body` to `evidence.content.body`
- Uses exact Unicode string equality — no normalization, hashing, or canonicalization
- Applies when minimal profile preconditions hold (`claim_type`, `assertion_type`, `evidence_type`, `content_type` as specified in VP-RFC-0001)

Draft [VP-RFC-0005](rfcs/0005-assertion-types.md) names **`body_equality`** as the protocol identifier for this semantics. Draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) maps **`body_equality`** to the Body Equality Evaluator, which routes to **VP-RULE-0001**.

**VP-RULE-0001 does not implement** `normalized_text`, `canonical_json`, `canonical_xml`, `binary_equality`, or `hash_equality`. Those types, when standardized, **MUST** introduce:

- A distinct **`assertion_type`** identifier
- A dedicated **Assertion Evaluator** (dispatch entry)
- One or more new **VP-RULE** definitions with explicit precondition and outcome tables
- **VP-CS scenarios** exercising edge cases for the comparison model

Existing **VP-RULE-0001** behavior **MUST NOT** change when new Content Equality types are added. Additive standardization preserves Platform 1.x compatibility for scenarios that depend on literal body match.

---

## Evolution

New Content Equality types should **reuse existing Verity Core infrastructure** rather than introducing parallel verification pipelines:

| Infrastructure | Reuse |
|----------------|-------|
| **Claim and Assertion envelopes** | Unchanged — new types declare different `assertion_type` values and body encodings |
| **Evidence and EvidenceContent** | Unchanged — evidence supplies content for comparison; binding still governed by **VP-RULE-0002** |
| **Evidence Set and Evaluation Policy** | Unchanged — per-envelope results aggregate as today |
| **Evaluator dispatch** | Extended — new `assertion_type` → evaluator → rule mapping entries only |
| **Verification outcomes** | Unchanged — `satisfied`, `not_satisfied`, `indeterminate` |

The expected RFC pattern for each new member:

1. Define type semantics and comparison algorithm normatively
2. Assign stable `assertion_type` identifier
3. Define evaluator dispatch and VP-RULE outcome tables
4. Publish VP-CS fixtures for satisfied, not_satisfied, and indeterminate cases
5. Implement reference evaluator in `veritypay-reference`
6. Extend conformance coverage in `veritypay-conformance`
7. Update [VERITY_CORE.md](VERITY_CORE.md) when the RFC is accepted

Families beyond Content Equality (Structural, Cryptographic, and others) may **compose** with Content Equality types in multi-assertion claims, but each type evaluates independently under dispatch rules.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — Content Equality family overview |
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | Accepted — **VP-RULE-0001** literal body match |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — **`body_equality`** type identifier |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |

---

*Informative family specification — not normative. No protocol semantics introduced by this document.*

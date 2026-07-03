# Structural Family

**Status:** Family Specification *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the **Structural** assertion family within the [Assertion Type Taxonomy](ASSERTION_TAXONOMY.md). This document is **not** a protocol RFC. It introduces **no protocol semantics**. Each candidate type requires an independent RFC before it becomes normative.

---

## Purpose

The **Structural** family addresses a question distinct from literal or normalized content match:

**Does evidence content conform to the structural shape, schema, or serialized form that the assertion describes?**

Structural verification concerns **shape and conformance** — whether a payload is valid JSON under a schema, whether an XML document matches a declared structure, whether a protobuf message decodes and satisfies field constraints. It does not ask whether two payloads are byte-identical; it asks whether evidence **fits** a declared structural contract.

This family becomes important as protocols move beyond minimal string bodies toward typed envelopes, structured payment records, credential payloads, and machine-readable evidence. Content Equality establishes whether values match; Structural establishes whether representations are **well-formed and conformant** under a defined model.

Structural types depend on explicit schema or canonicalization definitions in their asserting bodies. They **MUST NOT** rely on implementation-default parsers or undocumented serialization behavior when standardized.

---

## Family Overview

All assertion types in the **Structural** family share one semantic goal:

**Determine whether evidence content satisfies a structural contract asserted in the claim.**

Members differ in **what kind of structure** is verified:

| Structural model | Question asked |
|------------------|----------------|
| Canonical serialization | Does evidence represent the same structured value under a defined canonical form? |
| Schema conformance | Does evidence validate against a declared schema (JSON Schema, XML Schema, etc.)? |
| Typed message | Does evidence decode as a defined message type with expected field layout? |
| Document structure | Does a hierarchical document (YAML, XML) satisfy structural constraints? |

Structural types verify **structural equivalence and conformance**, not **textual equality**. Two JSON documents with different whitespace may be structurally equivalent under `canonical_json` but would not match under literal `body_equality`. Two XML documents may validate against the same schema while differing in serialization detail.

Each member is a distinct **`assertion_type`** with its own evaluator and rule(s). Unknown types yield `indeterminate` per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

This document describes the family. It does not assign normative outcome tables, preconditions, schema languages, or wire encodings.

---

## Candidate Types

The table below lists **candidate** Structural types for research and RFC planning. All candidates are **Research** unless noted. Status reflects this document only.

| Type | Description | Potential RFC | Initial status |
|------|-------------|---------------|----------------|
| **`canonical_json`** | Verify that evidence JSON content is structurally equivalent to an asserted canonical JSON value under a defined serialization algorithm (key ordering, number formatting, whitespace policy) | VP-RFC-0020 *(informative placeholder)* | **Research** — may overlap Content Equality family; RFC must declare family binding |
| **`canonical_xml`** | Verify XML structural equivalence under a defined canonicalization algorithm (for example inclusive canonical XML) | VP-RFC-0021 *(informative placeholder)* | **Research** |
| **`json_schema`** | Verify that evidence JSON content validates against a JSON Schema document carried in or referenced by the assertion body | VP-RFC-0022 *(informative placeholder)* | **Research** |
| **`xml_schema`** | Verify that evidence XML content validates against an XML Schema (XSD) or equivalent schema definition asserted with the claim | VP-RFC-0023 *(informative placeholder)* | **Research** |
| **`protobuf_message`** | Verify that evidence decodes as a specified protobuf message type and satisfies declared field constraints | VP-RFC-0024 *(informative placeholder)* | **Research** |
| **`yaml_structure`** | Verify that evidence YAML content parses and satisfies structural constraints (required keys, prohibited keys, type expectations) defined in the assertion | VP-RFC-0025 *(informative placeholder)* | **Research** |

**No Structural type is standardized by this document.** Potential RFC numbers are planning placeholders within the VP-RFC-0020–0029 range per [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md).

---

## Design Principles

Structural types should adhere to the following design principles when proposed for standardization. These guide RFC authors; they are **not** normative requirements introduced here.

| Principle | Meaning |
|-----------|---------|
| **Deterministic** | Identical assertion body, evidence content, and evaluation context **MUST** yield the same outcome. Parsing and validation **MUST NOT** depend on locale, implicit defaults, or undocumented parser extensions. |
| **Canonical** | When canonical forms are used, the RFC **MUST** name the algorithm explicitly. Structural comparison **MUST NOT** rely on "parse and hope" behavior. |
| **Schema-driven** | Schema-based types **MUST** identify the schema language, version, and resolution rules for schema documents. Ad hoc structural checks belong in Pattern Matching or Content Equality, not here. |
| **Serialization-independent** | Types that compare structured value **MUST** document which serialization differences are insignificant. Textual diff is not structural verification. |
| **Implementation-independent** | Validation semantics **MUST** be fully specified in the RFC. Two conforming implementations **MUST** agree on outcomes without sharing a validation library. |

These principles extend the taxonomy philosophy in [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) for the Structural family specifically.

---

## Relationship to existing protocol

The current Verity Core platform does **not** standardize any Structural assertion type.

Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) defines minimal envelopes with opaque string `body` fields compared by **VP-RULE-0001** under literal equality only. Draft [VP-RFC-0005](rfcs/0005-assertion-types.md) proposes **`body_equality`** in the Content Equality family — not structural schema validation.

No accepted rule performs JSON Schema validation, XML canonicalization, protobuf decoding, or YAML structure checking. Structural candidates in [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md) (for example `canonical_json`) address **value equality under canonical form**; Structural types here address **conformance to declared shape or schema** — related but distinct research tracks that future RFCs must disambiguate.

When a Structural type is standardized, it **MUST** introduce:

- A distinct **`assertion_type`** identifier
- A dedicated **Assertion Evaluator** and **VP-RULE** outcome tables
- Explicit preconditions for evidence format and assertion body encoding
- **VP-CS scenarios** for valid, invalid, and indeterminate structural cases

Existing **VP-RULE-0001** and **VP-RULE-0002** behavior **MUST NOT** change when Structural types are added.

---

## Evolution

New Structural types should **reuse existing Verity Core infrastructure**:

| Infrastructure | Reuse |
|----------------|-------|
| **Claim and Assertion envelopes** | Unchanged — assertion bodies carry schema references, canonical values, or message type identifiers |
| **Evidence and EvidenceContent** | Unchanged — evidence supplies content to validate; binding governed by **VP-RULE-0002** |
| **Evidence Set and Evaluation Policy** | Unchanged |
| **Evaluator dispatch** | Extended — new mapping entries only |
| **Verification outcomes** | Unchanged — `satisfied`, `not_satisfied`, `indeterminate` |

The expected RFC pattern for each new member matches [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md): type semantics → identifier → evaluator → rules → VP-CS → reference → conformance → Core update.

Structural types may **compose** with Content Equality or Pattern Matching types in multi-assertion claims (for example schema validation plus field pattern match), but each type evaluates independently under dispatch.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — Structural family overview |
| [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md) | Sibling family — content comparison vs structural conformance |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — assertion type mechanism |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |
| [DATA_MODEL.md](docs/01-architecture/DATA_MODEL.md) | Structural model for assertions and evidence |

---

*Informative family specification — not normative. No protocol semantics introduced by this document.*

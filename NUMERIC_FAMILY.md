# Numeric Family

**Status:** Family Specification *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the **Numeric** assertion family within the [Assertion Type Taxonomy](ASSERTION_TAXONOMY.md). This document is **not** a protocol RFC. It introduces **no protocol semantics**. Each candidate type requires an independent RFC before it becomes normative.

---

## Purpose

The **Numeric** family addresses **quantitative verification**:

**Does evidence express a numeric value that satisfies a quantitative relationship asserted in the claim?**

Numeric assertions compare **values** — amounts, counts, thresholds, ranges, percentages, and tolerances — rather than raw text or structural shape. Payment protocols frequently assert quantities: transfer amounts, fee limits, balance thresholds, and percentage allocations. Those assertions require comparison semantics beyond string equality or pattern match.

This family separates quantitative verification from textual representation. The same monetary amount may appear as `"100.00"`, `100`, or `1e2` in different serializations; Numeric types, when standardized, must define how values are extracted, typed, and compared — not leave comparison to ad hoc parsing in implementations.

---

## Family Overview

All assertion types in the **Numeric** family share one semantic goal:

**Determine whether a numeric value derived from evidence satisfies a quantitative constraint declared in the assertion.**

Members differ in **comparison relation**:

| Comparison relation | Question asked |
|---------------------|----------------|
| Equality | Is the evidence value equal to the asserted value? |
| Ordering | Is the evidence value greater than, less than, or bounded by asserted thresholds? |
| Range | Does the evidence value fall within an asserted interval? |
| Relative | Does the evidence value satisfy a percentage or tolerance relationship to an asserted reference? |

Numeric types compare **values**, not text. String comparison of `"9"` and `"10"` is a Content Equality concern; ordering `9 < 10` is a Numeric concern. Future RFCs must define value extraction, type coercion boundaries, and comparison semantics explicitly.

Each member is a distinct **`assertion_type`** with its own evaluator and rule(s). Unknown types yield `indeterminate` per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

This document describes the family. It does not assign normative outcome tables, units, precision rules, or wire encodings.

---

## Candidate Types

The table below lists **candidate** Numeric types for research and RFC planning. All candidates are **Research**. Status reflects this document only.

| Type | Description | Potential RFC | Initial status |
|------|-------------|---------------|----------------|
| **`numeric_equal`** | Evidence numeric value equals an asserted value under defined type and precision rules | VP-RFC-0040 *(informative placeholder)* | **Research** |
| **`greater_than`** | Evidence numeric value is strictly greater than an asserted threshold | VP-RFC-0041 *(informative placeholder)* | **Research** |
| **`greater_or_equal`** | Evidence numeric value is greater than or equal to an asserted threshold | VP-RFC-0042 *(informative placeholder)* | **Research** |
| **`less_than`** | Evidence numeric value is strictly less than an asserted threshold | VP-RFC-0043 *(informative placeholder)* | **Research** |
| **`less_or_equal`** | Evidence numeric value is less than or equal to an asserted threshold | VP-RFC-0044 *(informative placeholder)* | **Research** |
| **`range`** | Evidence numeric value falls within an asserted inclusive or exclusive bounds interval | VP-RFC-0045 *(informative placeholder)* | **Research** |
| **`percentage`** | Evidence value satisfies an asserted percentage relationship to a reference value | VP-RFC-0046 *(informative placeholder)* | **Research** |
| **`tolerance`** | Evidence value is within an asserted absolute or relative tolerance of a reference value | VP-RFC-0047 *(informative placeholder)* | **Research** |

**No Numeric type is standardized by this document.** Potential RFC numbers are planning placeholders within the VP-RFC-0040–0049 range per [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md).

Future RFCs for Numeric types are expected to define normatively:

- **Units** — currency codes, unit identifiers, dimensional semantics
- **Precision** — decimal places, significant figures, scale
- **Rounding** — rounding mode and direction when comparison requires it
- **Overflow** — behavior when values exceed representable range or parse bounds

These topics are listed for RFC planning only. This document does not specify them.

---

## Design Principles

Numeric types should adhere to the following design principles when proposed for standardization. These guide RFC authors; they are **not** normative requirements introduced here.

| Principle | Meaning |
|-----------|---------|
| **Deterministic** | Identical assertion body, evidence content, and evaluation context **MUST** yield the same comparison outcome. Floating-point and decimal behavior **MUST** be specified — not left to hardware defaults. |
| **Canonical** | Value extraction from evidence **MUST** follow a defined parsing and normalization path. Ambiguous string-to-number conversion is insufficient. |
| **Schema-driven** | Assertion bodies **SHOULD** declare value type (integer, decimal, currency quantity) and comparison parameters explicitly when standardized. |
| **Serialization-independent** | Comparison operates on numeric value, not on textual serialization form, once extraction rules are applied. |
| **Implementation-independent** | Comparison semantics **MUST** be fully specified. Two conforming implementations **MUST** agree on outcomes for all normative test vectors. |

These principles extend the taxonomy philosophy in [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) for the Numeric family specifically.

---

## Relationship to existing protocol

The current Verity Core platform does **not** standardize any Numeric assertion type.

Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) compares assertion and evidence `body` fields as Unicode strings via **VP-RULE-0001**. Numeric ordering, range membership, and tolerance are **not** implemented. Comparing `"100.00"` and `100` as strings is not numeric verification.

VerityPay payment semantics may eventually require Numeric types for amount and threshold assertions. Those types **MUST** enter through RFCs with explicit units and precision — not through payment-specific shortcuts in product code.

When a Numeric type is standardized, it **MUST** introduce a distinct **`assertion_type`**, evaluator, **VP-RULE** tables, and **VP-CS scenarios** covering edge cases (boundary values, parse failure, unit mismatch). Existing **VP-RULE-0001** and **VP-RULE-0002** behavior **MUST NOT** change.

---

## Evolution

New Numeric types should **reuse existing Verity Core infrastructure**:

| Infrastructure | Reuse |
|----------------|-------|
| **Claim and Assertion envelopes** | Unchanged — assertion bodies carry thresholds, ranges, units, and reference values |
| **Evidence and EvidenceContent** | Unchanged — evidence supplies extractable numeric content |
| **Evidence Set and Evaluation Policy** | Unchanged |
| **Evaluator dispatch** | Extended — new mapping entries only |
| **Verification outcomes** | Unchanged |

The expected RFC pattern for each new member: type semantics (including units, precision, rounding, overflow) → identifier → evaluator → rules → VP-CS → reference → conformance → Core update.

Numeric types may compose with Structural types (schema-valid amount field) or Temporal types (value valid within time window) in multi-assertion claims.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — Numeric family overview |
| [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md) | Sibling family — textual comparison vs numeric value comparison |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — assertion type mechanism |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |

---

*Informative family specification — not normative. No protocol semantics introduced by this document.*

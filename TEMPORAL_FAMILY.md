# Temporal Family

**Status:** Family Specification *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the **Temporal** assertion family within the [Assertion Type Taxonomy](ASSERTION_TAXONOMY.md). This document is **not** a protocol RFC. It introduces **no protocol semantics**. Each candidate type requires an independent RFC before it becomes normative.

---

## Purpose

The **Temporal** family addresses **time-based verification**:

**Does evidence satisfy a temporal relationship asserted in the claim?**

Temporal assertions compare **when** something is true, valid, or bounded — not merely what value or shape evidence carries. Expiry dates, validity windows, ordering constraints ("event A before event B"), and duration limits appear across payment settlement, credential lifecycle, compliance retention, and authorization scopes.

This family introduces time as a first-class verification dimension. Without standardized Temporal types, implementations embed clock logic in proprietary code — producing outcomes that diverge across time zones, precision models, and calendar systems.

---

## Family Overview

All assertion types in the **Temporal** family share one semantic goal:

**Determine whether evidence (or evaluation context) satisfies a temporal constraint declared in the assertion.**

Members differ in **temporal relation**:

| Temporal relation | Question asked |
|-------------------|----------------|
| Ordering | Is evidence timestamp before or after an asserted instant or bound? |
| Interval | Does evidence fall between asserted start and end instants? |
| Validity | Is evidence valid for a declared duration or until expiry? |
| Duration | Does a measured duration satisfy asserted bounds? |
| Instant match | Does evidence timestamp equal an asserted instant under defined precision? |

Temporal types compare **temporal relationships**, not text or numeric magnitude alone. A string `"2026-07-03"` compared literally belongs to Content Equality; whether that instant is **before** an asserted deadline belongs here.

Each member is a distinct **`assertion_type`** with its own evaluator and rule(s). Unknown types yield `indeterminate` per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

This document describes the family. It does not assign normative outcome tables, clock models, or instant encodings.

---

## Candidate Types

The table below lists **candidate** Temporal types for research and RFC planning. All candidates are **Research**. Status reflects this document only.

| Type | Description | Potential RFC | Initial status |
|------|-------------|---------------|----------------|
| **`before`** | Evidence timestamp (or derived instant) is strictly before an asserted instant or bound | VP-RFC-0050 *(informative placeholder)* | **Research** |
| **`after`** | Evidence timestamp is strictly after an asserted instant or bound | VP-RFC-0051 *(informative placeholder)* | **Research** |
| **`between`** | Evidence timestamp falls within an asserted start–end interval (inclusive/exclusive rules to be defined by RFC) | VP-RFC-0052 *(informative placeholder)* | **Research** |
| **`expires`** | Evidence is not valid after an asserted expiry instant | VP-RFC-0053 *(informative placeholder)* | **Research** |
| **`valid_for`** | Evidence remains valid for an asserted duration from a defined anchor instant | VP-RFC-0054 *(informative placeholder)* | **Research** |
| **`within_duration`** | Elapsed time between two derived instants satisfies an asserted duration bound | VP-RFC-0055 *(informative placeholder)* | **Research** |
| **`timestamp_match`** | Evidence instant equals an asserted instant under defined precision and timezone normalization | VP-RFC-0056 *(informative placeholder)* | **Research** |

**No Temporal type is standardized by this document.** Potential RFC numbers are planning placeholders within the VP-RFC-0050–0059 range per [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md).

Future RFCs for Temporal types are expected to determine normatively:

- **Clock models** — monotonic vs wall-clock; source of "now" during evaluation
- **Time zones** — UTC normalization; named zone handling; offset rules
- **Precision** — second, millisecond, microsecond; truncation vs rounding
- **Calendar systems** — Gregorian default; proleptic rules; date-only vs instant
- **Leap seconds** — inclusion or exclusion in duration and ordering calculations

These topics are listed for RFC planning only. This document does not specify them.

Draft [VP-RFC-0007](rfcs/0007-verification-context.md) lists **`evaluation_time`** as an informative future context field. Temporal types may interact with Verification Context when accepted — that interaction **MUST** be defined by future RFCs, not by this document.

---

## Design Principles

Temporal types should adhere to the following design principles when proposed for standardization. These guide RFC authors; they are **not** normative requirements introduced here.

| Principle | Meaning |
|-----------|---------|
| **Deterministic** | Identical assertion body, evidence content, evaluation context, and reference clock inputs **MUST** yield the same temporal outcome. |
| **Canonical** | Instant parsing and normalization **MUST** follow a defined algorithm (for example RFC 3339 profile). Locale-dependent date parsing is insufficient. |
| **Schema-driven** | Assertion bodies **SHOULD** declare instant encoding, timezone policy, and interval boundary semantics explicitly when standardized. |
| **Serialization-independent** | Comparison operates on normalized instants or durations, not on raw string form, once extraction rules apply. |
| **Implementation-independent** | Temporal semantics **MUST** be fully specified. Two conforming implementations **MUST** agree on outcomes for all normative test vectors including boundary and DST edge cases where applicable. |

These principles extend the taxonomy philosophy in [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) for the Temporal family specifically.

---

## Relationship to existing protocol

The current Verity Core platform does **not** standardize any Temporal assertion type.

Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) performs no temporal comparison. **VP-RULE-0001** and **VP-RULE-0002** ignore timestamps, expiry, and duration. Draft [VP-RFC-0007](rfcs/0007-verification-context.md) proposes context fields but does not define temporal assertion evaluation.

Temporal verification may eventually depend on **Verification Context** (for example evaluation time) and **Context Extensions** (for example time context) defined in draft RFCs **VP-RFC-0007** through **VP-RFC-0009**. Those dependencies **MUST** be specified in the RFC that standardizes each Temporal type.

When a Temporal type is standardized, it **MUST** introduce a distinct **`assertion_type`**, evaluator, **VP-RULE** tables, and **VP-CS scenarios** covering boundary instants, parse failure, and timezone edge cases. Existing accepted rule behavior **MUST NOT** change.

---

## Evolution

New Temporal types should **reuse existing Verity Core infrastructure**:

| Infrastructure | Reuse |
|----------------|-------|
| **Claim and Assertion envelopes** | Unchanged — assertion bodies carry instants, intervals, durations, and encoding hints |
| **Evidence and EvidenceContent** | Unchanged — evidence supplies temporal fields to evaluate |
| **Verification Context** | May supply evaluation-time anchor when standardized — per future RFC |
| **Evidence Set and Evaluation Policy** | Unchanged |
| **Evaluator dispatch** | Extended — new mapping entries only |
| **Verification outcomes** | Unchanged |

The expected RFC pattern for each new member: temporal semantics (clock, zone, precision, calendar, leap rules) → identifier → evaluator → rules → VP-CS → reference → conformance → Core update.

Temporal types may compose with Numeric (amount within validity window) or Authorization (permission expires) types in multi-assertion claims.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — Temporal family overview |
| [VP-RFC-0007](rfcs/0007-verification-context.md) | Draft — informative future `evaluation_time` context |
| [VP-RFC-0009](rfcs/0009-verification-context-extensions.md) | Draft — informative future time context extension |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — assertion type mechanism |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |

---

*Informative family specification — not normative. No protocol semantics introduced by this document.*

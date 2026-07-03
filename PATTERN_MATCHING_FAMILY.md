# Pattern Matching Family

**Status:** Family Specification *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the **Pattern Matching** assertion family within the [Assertion Type Taxonomy](ASSERTION_TAXONOMY.md). This document is **not** a protocol RFC. It introduces **no protocol semantics**. Each candidate type requires an independent RFC before it becomes normative.

---

## Purpose

The **Pattern Matching** family addresses a distinct verification question:

**Does evidence content satisfy a deterministic pattern declared in the assertion?**

Pattern Matching is **not** identity comparison. It does not ask whether evidence is **identical** to an asserted value. It asks whether evidence **matches** a declared pattern — a regular expression, a glob, a prefix, a contained substring, or an exact token boundary.

This family supports assertions such as "evidence identifier matches format X," "document reference contains required segment Y," or "field value starts with declared prefix Z." These checks are common in payment references, identifier validation, and document routing without requiring full structural schema validation.

Pattern Matching types of the form *"Does this evidence satisfy a pattern?"* rather than *"Is it identical?"* — the central distinction from the [Content Equality](CONTENT_EQUALITY_FAMILY.md) family.

---

## Family Overview

All assertion types in the **Pattern Matching** family share one semantic goal:

**Determine whether evidence content matches a pattern specified in the assertion body under defined syntax and matching rules.**

Members differ in **pattern language and match semantics**:

| Pattern model | Question asked |
|---------------|----------------|
| Regular expression | Does evidence match a declared regex under specified flags and encoding? |
| Glob | Does evidence match wildcard glob rules? |
| Substring | Does evidence contain, start with, or end with a declared literal or pattern? |
| Token | Does evidence contain an exact token boundary match? |

Pattern syntax **MUST** be explicit when types are standardized. Locale-sensitive collation, undocumented regex flavors, and platform-specific glob behavior are insufficient for protocol specification.

Each member is a distinct **`assertion_type`** with its own evaluator and rule(s). Unknown types yield `indeterminate` per draft [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

This document describes the family. It does not assign normative outcome tables, pattern grammars, or match algorithms.

---

## Candidate Types

The table below lists **candidate** Pattern Matching types for research and RFC planning. All candidates are **Research**. Status reflects this document only.

| Type | Description | Potential RFC | Initial status |
|------|-------------|---------------|----------------|
| **`regex`** | Evidence content matches a regular expression and flag set declared in the assertion body | VP-RFC-0030 *(informative placeholder)* | **Research** |
| **`glob`** | Evidence content matches a glob pattern with defined wildcard semantics (`*`, `?`, escape rules) | VP-RFC-0031 *(informative placeholder)* | **Research** |
| **`contains`** | Evidence content contains a declared substring under defined encoding and case rules | VP-RFC-0032 *(informative placeholder)* | **Research** |
| **`prefix`** | Evidence content begins with a declared prefix string or pattern | VP-RFC-0033 *(informative placeholder)* | **Research** |
| **`suffix`** | Evidence content ends with a declared suffix string or pattern | VP-RFC-0034 *(informative placeholder)* | **Research** |
| **`exact_token`** | Evidence content contains an exact token match with defined word-boundary or delimiter rules | VP-RFC-0035 *(informative placeholder)* | **Research** |

**No Pattern Matching type is standardized by this document.** Potential RFC numbers are planning placeholders within the VP-RFC-0030–0039 range per [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md).

---

## Design Principles

Pattern Matching types should adhere to the following design principles when proposed for standardization. These guide RFC authors; they are **not** normative requirements introduced here.

| Principle | Meaning |
|-----------|---------|
| **Deterministic** | Identical assertion body, evidence content, and evaluation context **MUST** yield the same match result. Pattern engines **MUST NOT** vary by runtime or library unless the RFC specifies the engine profile. |
| **Language-independent** | Pattern semantics **MUST** be defined without reference to a single programming language's regex or glob library. Protocol rules stand alone. |
| **Explicit pattern syntax** | The RFC **MUST** define or cite the pattern grammar, encoding, flags, and edge cases (empty string, full match vs partial match, anchoring). |
| **Portable** | Two conforming implementations **MUST** agree on match outcomes for all normative test vectors without shared code. |

These principles extend the taxonomy philosophy in [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) for the Pattern Matching family specifically.

---

## Relationship to existing protocol

The current Verity Core platform does **not** standardize any Pattern Matching assertion type.

Accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) compares assertion and evidence bodies via exact string equality only (**VP-RULE-0001**). No accepted rule performs regex, glob, substring, or token matching.

Pattern Matching is complementary to Content Equality and Structural families:

- **Content Equality** — same value under a comparison model
- **Structural** — conforms to schema or canonical shape
- **Pattern Matching** — satisfies a declared pattern without full equality or schema validation

When a Pattern Matching type is standardized, it **MUST** introduce a distinct **`assertion_type`**, evaluator, **VP-RULE** tables, and **VP-CS scenarios**. Existing **VP-RULE-0001** and **VP-RULE-0002** behavior **MUST NOT** change.

---

## Evolution

New Pattern Matching types should **reuse existing Verity Core infrastructure**:

| Infrastructure | Reuse |
|----------------|-------|
| **Claim and Assertion envelopes** | Unchanged — assertion bodies carry pattern definitions and match parameters |
| **Evidence and EvidenceContent** | Unchanged — evidence supplies content to match against |
| **Evidence Set and Evaluation Policy** | Unchanged |
| **Evaluator dispatch** | Extended — new mapping entries only |
| **Verification outcomes** | Unchanged |

The expected RFC pattern for each new member: type semantics → identifier → evaluator → rules → VP-CS → reference → conformance → Core update.

Pattern types may appear alongside Structural or Numeric types in multi-assertion claims; each evaluates independently.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — Pattern Matching family overview |
| [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md) | Sibling family — identity comparison vs pattern satisfaction |
| [STRUCTURAL_FAMILY.md](STRUCTURAL_FAMILY.md) | Sibling family — schema conformance vs pattern match |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — assertion type mechanism |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |

---

*Informative family specification — not normative. No protocol semantics introduced by this document.*

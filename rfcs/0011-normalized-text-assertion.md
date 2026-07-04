---
rfc: 0011
id: 0011
concept_id: VP-RFC-0011
title: Normalized Text Assertion
status: draft
version: 0.1.0
type: protocol
category: Protocol
pyramid_level: specification

authors:
  - VerityPay Core Team

reviewers: []

created: 2026-07-03
updated: 2026-07-03

depends_on:
  - 0000
  - 0005
  - 0006
supersedes: []
superseded_by: null

related_terms:
  - VP-TERM-004
  - VP-TERM-011
  - VP-TERM-013

related_architecture:
  - ../docs/01-architecture/DATA_MODEL.md
  - ../docs/03-development/CONFORMANCE_MODEL.md
  - ../CONTENT_EQUALITY_FAMILY.md

related_conformance:
  - VP-CS-0011
  - VP-CS-0012
  - VP-CS-0013

constitutional_refs:
  - ../docs/00-overview/MANIFESTO.md
  - ../docs/00-overview/VISION.md
  - ../docs/00-overview/PRINCIPLES.md
  - ../docs/00-overview/GLOSSARY.md

related_docs:
  - ../docs/03-development/CONFORMANCE_MODEL.md
  - ../ASSERTION_TAXONOMY.md
  - ../CONTENT_EQUALITY_FAMILY.md
  - 0001-minimal-claim-evidence-semantics.md
  - 0005-assertion-types.md
  - 0006-assertion-evaluation-dispatch.md

implementation_status: implemented_in_reference
last_updated: 2026-07-03
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-0011

**Family:** Content Equality · **Platform target:** Future Platform 1.3 candidate

**Constitutional basis:** [MANIFESTO.md](../docs/00-overview/MANIFESTO.md), [VISION.md](../docs/00-overview/VISION.md), [PRINCIPLES.md](../docs/00-overview/PRINCIPLES.md), [GLOSSARY.md](../docs/00-overview/GLOSSARY.md)

**Related documents:** [VP-RFC-0005](0005-assertion-types.md) · [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) · [CONTENT_EQUALITY_FAMILY.md](../CONTENT_EQUALITY_FAMILY.md) · [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) · [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md)

---

# RFC-0011: Normalized Text Assertion

## Summary

This RFC standardizes the **Content Equality** assertion type **`normalized_text`** and defines **VP-RULE-0011** (*Normalized Text Equality*).

**`normalized_text`** compares assertion and evidence text after a **deterministic normalization pipeline**. Evaluation uses the normalized strings. Outcome vocabulary remains `satisfied`, `not_satisfied`, and `indeterminate`.

This RFC is **additive**. It does **not** amend **`body_equality`**, **VP-RULE-0001**, **VP-RULE-0002**, or accepted [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) rule text.

**VP-CS** fixtures **VP-CS-0011**, **VP-CS-0012**, and **VP-CS-0013** are published in [`spec/conformance/scenarios/`](../spec/conformance/scenarios/). `veritypay-reference` and `veritypay-conformance` execute them as a **draft Platform 1.3 engineering baseline**. Normative acceptance of this RFC remains **draft**.

---

## Motivation

Literal body comparison (**`body_equality`** / **VP-RULE-0001**) treats formatting differences as mismatches. Real-world text — labels, names, references, and human-readable identifiers — often differs only in whitespace or Unicode normalization form while representing the same value.

Protocols need a **deterministic, implementation-independent** comparison model that ignores selected formatting variance without introducing locale rules, case folding, or undocumented parser behavior.

**`normalized_text`** is the first standardized extension of the [Content Equality family](../CONTENT_EQUALITY_FAMILY.md) beyond literal equality.

---

## Problem Statement

Without a normative **`normalized_text`** type:

- Implementations apply ad hoc trimming, collapsing, or normalization in product code.
- Identical semantic text produces divergent verification outcomes across vendors.
- Conformance cannot compare behavior because no shared rule exists.

The specification needs one **fully specified normalization pipeline** with explicit exclusions so independent evaluators converge.

---

## Goals

- Standardize **`normalized_text`** as a **Content Equality** assertion type.
- Define **VP-RULE-0011** with deterministic normalization and outcome mapping.
- Preserve **`body_equality`** and **VP-RULE-0001** unchanged.
- Enable future **Normalized Text Evaluator** dispatch per [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) without amending that RFC in this draft.
- Target **Platform 1.3** as a future platform release candidate when accepted with implementation.

---

## Non-Goals

- Amending **`body_equality`**, **VP-RULE-0001**, or **VP-RULE-0002**.
- Locale-sensitive collation, case folding, or language-specific rules.
- Punctuation removal, accent stripping, or compatibility normalization (NFKC/NFKD).
- Implementation-defined or configurable normalization profiles.
- Additional Content Equality types beyond **`normalized_text`**.

**Out of scope for normative acceptance in this draft:** reference and conformance code (owned by engineering repositories). Informative engineering baselines may implement this RFC before acceptance.

---

## Proposal

### 1. Assertion Type — `normalized_text`

| Property | Value |
|----------|--------|
| **Type ID** | `normalized_text` |
| **Family** | Content Equality |
| **Name** | Normalized text equality |
| **Meaning** | The assertion body and evidence content body **MUST** be compared after applying the normalization pipeline defined in §2. Comparison **MUST** be case-sensitive on the normalized strings. |

Every **Assertion** declaring `assertion_type = normalized_text` **MUST** supply a string `body` interpreted as text input to **VP-RULE-0011** when that rule's preconditions are satisfied.

This RFC does **not** register **`normalized_text`** in [VP-RFC-0005](0005-assertion-types.md). Acceptance of this RFC **SHOULD** be accompanied by a non-breaking amendment listing **`normalized_text`** in the assertion type taxonomy.

### 2. Normalization pipeline (Platform 1.3)

For **Platform 1.3**, evaluators **MUST** apply the following pipeline to **`claim.assertion.body`** and **`evidence.content.body`** independently before comparison. Steps **MUST** be executed in order. No optional steps exist.

| Step | Operation | Normative detail |
|------|-----------|------------------|
| **0** | UTF-8 decode | Each input **MUST** be a valid UTF-8 byte sequence representing a Unicode string. If either input is not valid UTF-8 → evaluation **MUST NOT** proceed; outcome **MUST** be `indeterminate` (*unknown encoding*). |
| **1** | Unicode NFC | Apply Unicode Normalization Form **C** (NFC) per [UAX #15](https://www.unicode.org/reports/tr15/). |
| **2** | Trim | Remove all leading and trailing characters whose Unicode **General_Category** is **Separator, space** (`Zs`), **Separator, line** (`Zl`), or **Separator, paragraph** (`Zp`), and remove U+0009 CHARACTER TABULATION, U+000A LINE FEED, U+000B LINE TABULATION, U+000C FORM FEED, and U+000D CARRIAGE RETURN from the start and end of the string. |
| **3** | Collapse internal whitespace | Replace each maximal contiguous substring consisting solely of characters removed in step 2 with a single ASCII SPACE (U+0020). |
| **4** | Compare | Compare the two resulting strings using exact Unicode string equality. **MUST NOT** apply case folding or locale rules. |

**Explicit exclusions** — the pipeline **MUST NOT**:

- Apply locale-sensitive rules or collation tables
- Remove punctuation
- Remove accents except as a side effect of NFC on composed characters
- Apply Unicode Normalization Form **D**, **KD**, or **KC** (compatibility normalization)
- Apply implementation-defined normalization, heuristics, or "best effort" cleanup

Evaluators **MUST** use the **normalized strings** produced by steps 1–3 for **VP-RULE-0011** comparison. Raw pre-normalization strings **MUST NOT** determine the outcome except where step 0 or preconditions apply.

### 3. Verification rule — VP-RULE-0011

| Property | Value |
|----------|--------|
| **Rule ID** | `VP-RULE-0011` |
| **Name** | Normalized Text Equality |
| **Applies when** | `claim.assertion.assertion_type` is `normalized_text`, one **Evidence** envelope is selected for evaluation, and [VP-RFC-0002](0002-claim-identity-binding.md) **VP-RULE-0002** binding preconditions are satisfied when binding rules are in scope |

**Purpose:** Determine whether evidence text matches asserted text after the Platform 1.3 normalization pipeline.

**Inputs:** one **Claim** with `assertion_type = normalized_text` and one **Evidence** envelope with **EvidenceContent** body.

**Procedure** (normative outcome mapping):

1. If no **Evidence** envelope is supplied → outcome **MUST** be `indeterminate`.
2. If `evidence.claim_id` does not equal `claim.claim_id` → outcome **MUST** be `indeterminate`.
3. If either `claim.assertion.body` or `evidence.content.body` is not valid UTF-8 → outcome **MUST** be `indeterminate`.
4. If `evidence.content.body` is empty (zero-length string) or contains only whitespace characters before normalization → outcome **MUST** be `indeterminate`.
5. Apply the normalization pipeline (§2) to both bodies. Let `N_assertion` and `N_evidence` be the normalized results.
6. If `N_evidence` equals `N_assertion` (exact Unicode string equality) → outcome **MUST** be `satisfied`.
7. Otherwise → outcome **MUST** be `not_satisfied`.

**Outcome table:**

| Condition | Outcome |
|-----------|---------|
| Step 1 | `indeterminate` |
| Step 2 | `indeterminate` |
| Step 3 (invalid UTF-8 / unknown encoding) | `indeterminate` |
| Step 4 (empty or whitespace-only evidence body) | `indeterminate` |
| Step 6 (normalized strings equal) | `satisfied` |
| Step 7 (normalized strings differ) | `not_satisfied` |

No other outcome labels are defined by this RFC.

**Notes:**

- Step 2 duplicates the binding check in **VP-RULE-0002** when both rules run; evaluators **MAY** rely on **VP-RULE-0002** having run first per dispatch architecture in [VP-RFC-0006](0006-assertion-evaluation-dispatch.md).
- An empty assertion body after normalization is valid input; only an empty or whitespace-only **evidence** body before normalization yields `indeterminate` in step 4 (consistent with **VP-RULE-0001** empty-evidence handling).
- This rule does **not** inspect `subject`, `specification_version`, or envelope identifiers beyond `claim_id` linkage.

### 4. Informative examples

Examples are **non-normative** illustrations. Only §2 and §3 are binding.

| Assertion body | Evidence body | Normalized (both) | Outcome |
|----------------|---------------|-------------------|---------|
| `"  alpha  "` | `"alpha"` | `"alpha"` | `satisfied` |
| `"alpha\tbeta"` | `"alpha beta"` | `"alpha beta"` | `satisfied` |
| `"Alpha"` | `"alpha"` | `"Alpha"` / `"alpha"` | `not_satisfied` (case-sensitive) |
| `"café"` (NFC) | `"café"` (NFD precomposed) | Equal after NFC step 1 | `satisfied` |
| `"alpha"` | `"beta"` | `"alpha"` / `"beta"` | `not_satisfied` |
| `"alpha"` | `` (empty) | — | `indeterminate` |
| `"alpha"` | `"     "` (whitespace only) | — | `indeterminate` |
| Invalid UTF-8 byte sequence | `"alpha"` | — | `indeterminate` |

### 5. Evaluator dispatch (informative)

On acceptance, **`normalized_text`** **SHOULD** map through [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) dispatch as:

```text
normalized_text → Normalized Text Evaluator → VP-RULE-0011
```

This RFC does **not** amend **VP-RFC-0006** text. Dispatch registration **MAY** follow in a dedicated amendment or acceptance update to **VP-RFC-0006**.

---

## Architecture Impact

| Model | Change |
|-------|--------|
| [DATA_MODEL.md](../docs/01-architecture/DATA_MODEL.md) | **Extension on acceptance** — **`normalized_text`** under Content Equality / Assertion Type |
| [CONTENT_EQUALITY_FAMILY.md](../CONTENT_EQUALITY_FAMILY.md) | **Documentation alignment** — **`normalized_text`** status Research → Draft |
| [CONFORMANCE_MODEL.md](../docs/03-development/CONFORMANCE_MODEL.md) | **VP-CS-0011**–**0013** scenarios published (draft fixtures) |

---

## Terminology Impact

| Term | Change |
|------|--------|
| **`normalized_text`** | **New assertion type identifier** (draft) |
| **VP-RULE-0011** | **New verification rule** (draft) |
| **`body_equality`** | **Unchanged** |

---

## Conformance Impact

| VP-CS ID | Change |
|----------|--------|
| **VP-CS-0001** | **None** — continues to exercise **VP-RULE-0001** / **`body_equality`** |
| **VP-CS-0002** | **None** |
| **VP-CS-0011** | **Published** — trim and whitespace collapse → `satisfied` |
| **VP-CS-0012** | **Published** — case-sensitive mismatch → `not_satisfied` |
| **VP-CS-0013** | **Published** — empty or whitespace-only evidence → `indeterminate` |

Implementations **MAY** advertise support for **`normalized_text`** via future capability identifiers. This RFC does **not** amend [VP-RFC-0010](0010-protocol-capability-negotiation.md).

---

## Security Impact

Normalization can collapse visually distinct strings into identical normalized forms. Protocol designers **SHOULD** avoid **`normalized_text`** where human-confusable characters or homoglyphs create unacceptable ambiguity. This RFC defines mechanical comparison only — not visual or trust policy.

---

## Backwards Compatibility

**Additive.**

| Artifact | Impact |
|----------|--------|
| **`body_equality`** | Unchanged |
| **VP-RULE-0001** | Unchanged |
| **VP-RULE-0002** | Unchanged |
| **Platform 1.2** | Unaffected — draft until acceptance and Platform 1.3 declaration |
| **VP-CS-0001** / **VP-CS-0002** | Unchanged |

---

## Migration Strategy

1. Accept **VP-RFC-0011** when governance approves.
2. Register **VP-RFC-0011** in [`spec/rfcs/registry.yaml`](../spec/rfcs/registry.yaml) as draft (done when published).
3. Amend [VP-RFC-0005](0005-assertion-types.md) to list **`normalized_text`** (non-breaking taxonomy extension).
4. Amend [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) with **`normalized_text`** dispatch entry.
5. Implement **Normalized Text Evaluator** in `veritypay-reference`.
6. Publish **VP-CS** fixtures exercising **VP-RULE-0011** edge cases — **complete** (**VP-CS-0011**–**0013** in [`spec/conformance/scenarios/`](../spec/conformance/scenarios/)).
7. Declare **Platform 1.3** when engineering baselines align.

Existing **`body_equality`** claims and scenarios **MUST** continue to use **VP-RULE-0001** without normalization.

---

## Implementation Plan

*Informative — deferred:*

| Deliverable | Status |
|-------------|--------|
| **`normalized_text`** / **VP-RULE-0011** normative definition | Complete (this draft) |
| **VP-RFC-0011** registry entry | Complete |
| **VP-CS fixtures** (**VP-CS-0011**–**0013**) | Complete — published in [`spec/conformance/scenarios/`](../spec/conformance/scenarios/) |
| **Reference implementation** | Not started (separate repository) |
| **Conformance execution** | Not started (separate repository) |

No code changes are part of this draft RFC.

---

## Alternatives Considered

### Alternative A — Extend VP-RULE-0001 with optional normalization

**Why not chosen:** Would change **`body_equality`** semantics or introduce mode flags; violates separation and Platform 1.2 stability.

### Alternative B — Case-insensitive comparison in this RFC

**Why not chosen:** Case folding introduces locale and Unicode case-mapping complexity; deferred to a future type if needed.

### Alternative C — NFKC compatibility normalization

**Why not chosen:** Compatibility normalization discards semantic distinctions (for example ligatures, formatting characters) that protocols may need to preserve.

---

## Open Questions

1. Should step 4 treat empty assertion body as `indeterminate` symmetrically, or only empty or whitespace-only evidence body?
2. Should **VP-CS** for **VP-RULE-0011** ship in the same RFC acceptance tranche or a separate fixture RFC? *(Fixtures **VP-CS-0011**–**0013** published ahead of acceptance.)*
3. Should **`normalized_text`** require explicit `evidence_type` / `content_type` preconditions like the minimal profile, or only `assertion_type`?

---

## Acceptance Criteria

- [ ] **`normalized_text`** defined as Content Equality assertion type
- [ ] Normalization pipeline is fully specified with explicit exclusions
- [ ] **VP-RULE-0011** defines preconditions and outcome table
- [ ] Invalid UTF-8 / unknown encoding yields `indeterminate`
- [x] **`body_equality`** and **VP-RULE-0001** are not amended
- [x] **VP-CS-0011**–**0013** fixtures published in [`spec/conformance/scenarios/`](../spec/conformance/scenarios/)
- [ ] Compatibility with Platform 1.2 documented
- [ ] [RFC invariants](0000-rfc-process.md#11-rfc-invariants) satisfied

---

## References

- [VP-RFC-0000](0000-rfc-process.md) — RFC Process
- [VP-RFC-0001](0001-minimal-claim-evidence-semantics.md) — Minimal Claim and Evidence Semantics (accepted)
- [VP-RFC-0002](0002-claim-identity-binding.md) — Claim Identity Binding (accepted)
- [VP-RFC-0005](0005-assertion-types.md) — Assertion Types (draft)
- [VP-RFC-0006](0006-assertion-evaluation-dispatch.md) — Assertion Evaluation Dispatch (draft)
- [CONTENT_EQUALITY_FAMILY.md](../CONTENT_EQUALITY_FAMILY.md)
- [ASSERTION_TAXONOMY.md](../ASSERTION_TAXONOMY.md)
- [UAX #15 — Unicode Normalization Forms](https://www.unicode.org/reports/tr15/)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — Key words for use in RFCs

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-07-03 | Initial draft — **`normalized_text`**, **VP-RULE-0011**, Platform 1.3 normalization pipeline |

# Assertion Type Taxonomy

**Status:** Research Roadmap *(informative only)*

**Audience:** Protocol designers, researchers, contributors, and future RFC authors.

**Purpose:** Describe the long-term taxonomy of **Assertion Types** within Verity. This document introduces **no protocol semantics**. Future assertion types require independent RFCs before they become normative.

For the current standardized type, see draft [VP-RFC-0005](rfcs/0005-assertion-types.md). For how assertion types fit the execution model, see [VERITY_CORE.md](VERITY_CORE.md) §14.

---

## Purpose

Verity separates **protocol infrastructure** from **assertion semantics**.

The **Verity Core** defines *how* verification works — claims, evidence, evaluation context, evaluator dispatch, evaluation policies, and verification outcomes. That machinery is protocol-neutral. It does not prescribe what domains may assert or how domain-specific bodies are interpreted.

**Assertion Types** define *what can be verified* — the semantic vocabulary that tells an evaluator how to interpret an assertion's body and which rules apply. A payment protocol, an identity protocol, and a compliance protocol may all use the same Core execution model while declaring different assertion types.

This separation allows the platform to grow without rewriting infrastructure. New verification capabilities enter through small, focused RFCs that standardize one type (or one family) at a time — not through ad hoc extensions embedded in product code or monolithic specification revisions.

This document is a **research roadmap**. It orients future RFC authors. It does not standardize identifiers, rules, or evaluators.

---

## Taxonomy Philosophy

Assertion types should satisfy the following properties. These are design goals for future standardization — not normative requirements introduced by this document.

| Property | Meaning |
|----------|---------|
| **Deterministic** | Identical assertion body, evidence, and context yield the same outcome under the applicable rules |
| **Implementation-independent** | Type semantics are defined by specification, not by any one codebase or vendor API |
| **Composable** | Types may be combined in claims and evaluated independently; composite types (when standardized) compose without hidden coupling |
| **Reusable across protocols** | A type standardized for Verity Core may be used by VerityPay, identity protocols, credential protocols, and others without redefinition |
| **Stable once standardized** | Accepted type identifiers and semantics remain valid under additive platform evolution; changes require explicit RFC governance |

Types describe **interpretation** — what an assertion body means in protocol terms. Evaluators and rules describe **procedure** — how evaluation executes. That distinction is maintained in [VP-RFC-0005](rfcs/0005-assertion-types.md) and [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).

---

## Assertion Families

The table below groups assertion types into **families** — conceptual categories for long-term planning. No family, example, or RFC range in this table is normative. Standardization occurs only through accepted RFCs.

| Family | Purpose | Examples *(informative)* | Suggested future RFC range *(informative)* |
|--------|---------|--------------------------|---------------------------------------------|
| **Content Equality** | Compare assertion payload to evidence content under exact or normalized equality | Literal body match; normalized string equality; canonicalized JSON equality | VP-RFC-0011–0019 |
| **Structural** | Verify shape, schema, or structural conformance of assertion or evidence bodies | JSON Schema conformance; required field presence; typed envelope validation | VP-RFC-0020–0029 |
| **Pattern Matching** | Match assertion or evidence content against declarative patterns | Regular expression; glob; path expression | VP-RFC-0030–0039 |
| **Numeric** | Compare numeric claims against evidence thresholds or ranges | Equality; ordering; range membership; tolerance bands | VP-RFC-0040–0049 |
| **Temporal** | Evaluate time-based assertions relative to evidence or context | Before; after; within interval; duration bounds | VP-RFC-0050–0059 |
| **Cryptographic** | Verify cryptographic relationships between assertion and evidence | Digest match; digital signature; Merkle inclusion *(descriptive only)* | VP-RFC-0060–0069 |
| **Document** | Assert properties of document-like evidence | Format identification; content-type agreement; extractable metadata | VP-RFC-0070–0079 |
| **Identity** | Assert subject linkage, attributes, or binding relationships | Subject match; attribute equality; identifier binding | VP-RFC-0080–0089 |
| **Authorization** | Assert permissions, scopes, or consent | Scope inclusion; permission grant; delegation chain *(descriptive only)* | VP-RFC-0090–0099 |
| **Compliance** | Assert regulatory or policy conformance against evidence | Policy rule reference; audit trail presence; control satisfaction *(descriptive only)* | VP-RFC-0100–0109 |
| **Composite** | Combine multiple assertion types under one evaluation unit | All required; any sufficient; ordered dependency *(descriptive only)* | VP-RFC-0110–0119 |
| **Future** | Reserved for domains not yet analyzed | Domain-specific extensions; experimental categories | VP-RFC-0120+ |

**No semantics, rules, or evaluators are defined here.** Examples illustrate intent for researchers and RFC authors. RFC ranges are planning placeholders — actual RFC numbers are assigned at proposal time per [VP-RFC-0000](rfcs/0000-rfc-process.md).

The only type approaching standardization today is **`body_equality`** (Content Equality family), defined in draft [VP-RFC-0005](rfcs/0005-assertion-types.md) and evaluated via **VP-RULE-0001** in accepted [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md).

---

## Maturity

Assertion types progress through documented maturity stages before and after normative acceptance. This document uses **Research** for all families except those already in RFC draft or accepted status elsewhere.

| Stage | Meaning |
|-------|---------|
| **Research** | Exploratory category or example; no RFC proposed; no normative identifiers |
| **Draft** | RFC proposed; semantics under review; not binding on implementations |
| **Accepted** | RFC accepted; type identifier, evaluator mapping, and rules are normative |
| **Deprecated** | Accepted type retained for compatibility but discouraged for new scenarios; successor identified |
| **Superseded** | Accepted type replaced by a successor RFC; old identifier mapping documented in migration guidance |

Promotion from Research to Draft requires an RFC per [VP-RFC-0000](rfcs/0000-rfc-process.md). This taxonomy document does not advance any family beyond Research.

---

## Roadmap

Verity Core intentionally grows through **small RFCs**. Each assertion type — or tightly related group of types within one family — should normally introduce the following artifacts in order:

| Artifact | Owner | Role |
|----------|-------|------|
| **Assertion Type** | `veritypay-spec` (RFC) | Stable `assertion_type` identifier and semantic definition |
| **Evaluator** | `veritypay-spec` (RFC) + `veritypay-reference` | Dispatch mapping and reference evaluator implementation |
| **Rule(s)** | `veritypay-spec` (RFC) | Normative outcome tables (for example VP-RULE-00xx) |
| **VP-CS scenarios** | `veritypay-spec` | Executable conformance fixtures authored with the RFC |
| **Reference implementation** | `veritypay-reference` | Oracle behavior traceable to the RFC |
| **Conformance** | `veritypay-conformance` | Harness execution against published VP-CS fixtures |
| **Core updates** | `veritypay-spec` ([VERITY_CORE.md](VERITY_CORE.md)) | Consolidated specification synchronized when RFC is accepted |

Work flows **spec → validate → implement → compare**. An assertion type does not exist in the protocol because reference code implements it — it exists because an RFC accepts it.

Suggested sequencing for early expansion *(informative)*:

1. Finalize **`body_equality`** via acceptance of [VP-RFC-0005](rfcs/0005-assertion-types.md) and [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md).
2. Introduce additional **Content Equality** and **Structural** types — low coupling to trust and credential models.
3. Expand **Cryptographic**, **Identity**, and **Authorization** families only after Core context and capability models stabilize ([VP-RFC-0007](rfcs/0007-verification-context.md) through [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md) acceptance path).
4. Reserve **Composite** types until single-type evaluators and policies are well exercised.

---

## Relationship to VerityPay

**VerityPay** is the first protocol built on Verity Core. It will initially use only a **small subset** of assertion types — beginning with content-level verification suitable for minimal claim and evidence semantics (**`body_equality`** and successors in the Content Equality family).

The taxonomy in this document is **intentionally broader** than any one protocol. Payment workflows may eventually require document, temporal, or compliance-oriented types; identity and credential protocols may draw heavily from Identity and Cryptographic families. VerityPay does not need to adopt every family for the platform to succeed.

Protocol designers should select types from accepted RFCs — not from this roadmap. This document prevents duplicate invention of categories during research; it does not authorize use of unstandardized identifiers.

---

## Closing

Digital systems will continue to assert new kinds of claims — about payments, identity, authorization, compliance, and documents not yet imagined. A verification platform that rewrites its core for each new domain will not survive decades of use.

This taxonomy is intended to support **long-lived protocol evolution**: stable infrastructure, additive assertion vocabulary, and governance that keeps semantics public and testable. Families and examples here may change as research matures. Only RFCs make types real.

When you are ready to standardize a type, start an RFC. Cite this document only as background.

---

## Related documents

| Document | Role |
|----------|------|
| [ASSERTION_TAXONOMY.md](ASSERTION_TAXONOMY.md) | Parent taxonomy — assertion families |
| [CONTENT_EQUALITY_FAMILY.md](CONTENT_EQUALITY_FAMILY.md) | Family specification — Content Equality candidates |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft — initial Assertion Type taxonomy |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft — evaluator dispatch |
| [VERITY_CORE.md](VERITY_CORE.md) | Core Specification — §14 Assertion Types |
| [DATA_MODEL.md](docs/01-architecture/DATA_MODEL.md) | Structural model for assertions |
| [docs/04-research/](docs/04-research/) | Pre-normative research corpus |

---

*Informative research roadmap — not normative. No protocol semantics introduced by this document.*

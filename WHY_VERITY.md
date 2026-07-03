# Why Verity?

**Building open verification infrastructure for a world that increasingly depends on digital evidence.**

**Audience:** Engineers, researchers, open-source contributors, grant reviewers, foundation partners, and future protocol designers.

**Purpose:** Explain why Verity exists — the problem it addresses, the principles it upholds, and the long-term vision it serves. This document does not define protocol behavior. For normative semantics, see [VERITY_CORE.md](VERITY_CORE.md) and accepted RFCs.

---

## The Problem

Software systems constantly exchange information. Payment networks, identity providers, credential issuers, compliance platforms, and document services all move data across organizational boundaries every day.

Most systems exchange **data**. Very few exchange **verifiable meaning**.

Protocols frequently define formats — how a message is structured, which fields are required, how bytes are serialized. They rarely define **verification** — how an independent party determines whether a claim is supported, contradicted, or indeterminate given available evidence.

When verification is undefined, it becomes **implementation-dependent**. One validator accepts what another rejects. One SDK interprets a field differently from another. One payment provider and one identity provider produce incompatible answers to the same question. Interoperability does not fail loudly; it erodes quietly. Fragmentation follows.

This is not a tooling problem. It is a **specification problem**. Without shared verification semantics, independent implementations cannot converge on identical outcomes — and without that convergence, trust in digital assertions remains tied to individual vendors rather than to publicly documented rules.

---

## Why Specifications Are Not Enough

A specification defines meaning. It tells implementers what a claim is, what evidence is, and what outcomes are valid. That is necessary — but not sufficient.

Unless a specification is **executable** and **testable**, different implementations drift. Each team reads the prose differently. Each codebase encodes slightly different assumptions. Over time, "conforming" implementations stop agreeing.

This pattern appears across domains:

- **Different validators** interpret the same credential schema with different acceptance criteria.
- **Different SDKs** expose convenience APIs that reshape protocol semantics without documenting the change.
- **Different payment providers** apply business logic that overrides or obscures normative verification rules.
- **Different identity providers** bind claims to evidence using incompatible linkage models.

The specification remains on paper. Interoperability slowly disappears.

Verity addresses this by treating the specification as the beginning of a **platform** — not the end of a document. Meaning is authored in one place, validated mechanically, executed by a reference interpreter, and compared across implementations through conformance scenarios. The specification stays normative; the platform makes it **operational**.

---

## Why Reference Implementations Matter

A reference implementation does not become the protocol. It demonstrates **one correct interpretation** of the specification — readable, runnable, and available for comparison.

Reference implementations serve several purposes:

- **They reduce ambiguity.** When prose is unclear, executable semantics resolve the question without rewriting the specification.
- **They improve education.** Implementers, auditors, and reviewers can trace claim → evidence → outcome in code aligned with accepted documents.
- **They provide executable semantics.** Verification rules produce outcomes that can be run, not only read.
- **They supply an oracle.** Conformance harnesses compare independent implementations against reference outcomes — not against one vendor's production stack.

The specification remains **normative**. When the reference interpreter and the specification disagree, the specification wins. The reference interpreter is an educational and testing artifact — not a source of protocol truth, not a production pattern, and not a substitute for reading the RFCs.

This separation — protocol meaning in the specification, demonstration in the reference — is deliberate. It allows multiple independent implementations to remain compatible over time without sharing one codebase.

---

## Why Conformance Matters

Conformance exists to compare **behavior** — not code, not architecture, not performance.

Two completely different implementations — written in different languages, organized with different module structures, deployed on different infrastructure — should produce **identical verification outcomes** for the same protocol inputs. That is the interoperability test.

Conformance scenarios (VP-CS) specify claim and evidence inputs, the rules under test, and the expected outcome. The reference interpreter supplies the oracle. An implementation adapter runs the same inputs through the system under test. A comparison engine reports pass, fail, skip, or error.

A **pass** means outcomes match. A **fail** means they diverge — the implementation does not speak the protocol correctly for that scenario. A **skip** means the scenario required a capability the implementation has not adopted. Conformance does not certify legal compliance, financial accuracy, or production readiness. It certifies **protocol behavior**.

Without conformance, interoperability claims are assertions. With conformance, they are **evidence**.

---

## Why Evidence Matters

Verity is built on one central principle:

**Verification should depend on evidence, not implementation.**

Not vendors. Not hidden business logic. Not proprietary interpretation layers that sit between the protocol and the outcome.

The model is straightforward:

- **Claims describe** what is asserted.
- **Evidence supports** or refutes those assertions.
- **Rules evaluate** claim and evidence under documented preconditions.
- **Results communicate** the protocol outcome — satisfied, not satisfied, or indeterminate.

Evaluation follows publicly documented rules. Independent implementations should converge on identical outcomes for identical inputs. When they do not, the discrepancy is visible, reproducible, and addressable through specification clarification or implementation correction.

This is why Verity separates **protocol meaning** from **implementation architecture**. The protocol defines what verification means. Implementations demonstrate that they produce the same meaning. Evidence — not implementation identity — determines the outcome.

---

## Why Open Governance Matters

Protocol evolution should be **visible**. Changes should be proposed, reviewed, and accepted through a documented process — not introduced silently in a release note or buried in a changelog.

Verity uses:

- **RFCs** — formal change proposals with rationale, requirements, and acceptance criteria.
- **Public review** — proposals are readable before they become binding.
- **Platform releases** — compatible engineering baselines declared explicitly across repositories.
- **Compatibility policy** — additive evolution by default; breaking changes require deliberate governance.

No silent changes. No normative behavior that exists only in code. No protocol semantics that appear in a product repository before they appear in an RFC.

Open governance does not guarantee consensus on every decision. It guarantees **traceability** — that anyone can determine what the protocol meant at a given point, how it changed, and why.

---

## Why Verity Exists

Verity exists to make verification:

| Property | Meaning |
|----------|---------|
| **Transparent** | Rules are documented, reviewable, and publicly accessible |
| **Portable** | Outcomes do not depend on which vendor's stack performed the evaluation |
| **Reproducible** | Identical inputs yield identical outcomes across independent implementations |
| **Interoperable** | Systems built by different teams can verify the same claims against the same evidence |
| **Vendor-independent** | Protocol truth is defined by specification, not by any one implementation |
| **Long-lived** | Specifications outlive products; governance preserves compatibility across releases |

Verity is infrastructure — not a product, not a company, not a single implementation. It is the shared foundation on which verifiable digital interactions can be built, tested, and compared honestly.

---

## Beyond VerityPay

**VerityPay** is the first protocol built on the Verity platform. It applies the Core verification model to payment claims — structured assertions about transfers, obligations, and settlement that require evidence to verify.

The **Verity Core** verification model is intentionally reusable. It defines claims, assertions, evidence, evaluation context, evaluation policies, and verification outcomes in protocol-neutral terms. Payment-specific semantics extend Core entities without redefining them.

Future protocol families may include:

- **Identity** — assertions about subjects, attributes, and binding
- **Credentials** — attestations issued by authorities and presented by holders
- **Compliance** — regulatory and policy claims with auditable evidence trails
- **Documents** — content integrity and provenance verification
- **Authorizations** — permission and consent claims with supporting evidence
- **Others** — any domain where digital assertions require verifiable evaluation

The platform should **outlive individual protocols**. VerityPay may be the first application; it is not the only one the architecture was designed to support.

---

## The Long-Term Vision

Success for Verity is **not**:

- one implementation
- one SDK
- one company
- one product dominating the ecosystem

Success **is**:

- **Many independent implementations** — built by different teams, in different languages, for different use cases
- **Shared semantics** — all implementations target the same accepted specification
- **Shared conformance** — all implementations compare against the same VP-CS scenarios and reference oracle
- **Shared trust** — verification outcomes mean the same thing regardless of who ran the evaluation

The goal is durable public infrastructure: specifications that precede implementation, platforms that keep specifications coherent and testable, and ecosystems where interoperability emerges from shared standards — not from shared vendors.

---

## Closing

Software increasingly depends on digital assertions — claims about identity, payment, authorization, compliance, and provenance that systems must evaluate before acting.

Verity exists so those assertions can be verified **consistently**, regardless of who implements the protocol.

---

## Related documents

| Document | Role |
|----------|------|
| [PLATFORM_OVERVIEW.md](PLATFORM_OVERVIEW.md) | Current ecosystem snapshot |
| [ECOSYSTEM.md](ECOSYSTEM.md) | Platform organization and repository roles |
| [VERITY_CORE.md](VERITY_CORE.md) | Consolidated protocol specification |
| [PRINCIPLES.md](docs/00-overview/PRINCIPLES.md) | Engineering decision heuristics |
| [MANIFESTO.md](docs/00-overview/MANIFESTO.md) | Public commitments |

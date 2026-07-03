---
document: Specification Status
version: 1.0.0
status: canonical
last_updated: 2026-06-29
---

**Document:** Specification Status · **Version:** 1.0.0 · **Status:** canonical (living document)

**Last updated:** 2026-06-29 · **Maintainers:** update this file when milestone or registry state changes materially

---

# Specification Status

**What is the current state of the VerityPay Specification?**

This document is the public **engineering cockpit** for the VerityPay specification ecosystem. It summarizes maturity, health, and direction so contributors, implementers, researchers, auditors, grant reviewers, and future maintainers can orient in **under two minutes**.

This document is **not normative**. It does not define protocol behavior. It is a **navigation and transparency** layer—a living dashboard that should eventually be partially automated from registries and Edition manifests. Until then, maintainers update it when institutional state changes.

For normative rules, follow accepted RFCs and published Editions. For process, see [GOVERNANCE.md](docs/05-governance/GOVERNANCE.md) and [VP-RFC-0000](rfcs/0000-rfc-process.md).

---

## Current snapshot

| Field | Value |
|-------|--------|
| **Current Edition** | Genesis Edition *(in preparation — not yet published)* |
| **Current Protocol Version** | *Not declared* — will be assigned at Genesis publication (e.g. `vp-protocol-1.0`) |
| **Specification phase** | Pre-Genesis · Architecture Alpha complete |
| **Architecture status** | Architecture Alpha frozen (structural); draft documents informative until Edition |
| **Governance status** | Canonical process docs; [GOVERNANCE.md](docs/05-governance/GOVERNANCE.md) draft |
| **Conformance status** | [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md) draft; **VP-CS-0001** and **VP-CS-0002** executable via `veritypay-conformance`; [`VP-CS-0001`](spec/conformance/scenarios/VP-CS-0001.toml) and [`VP-CS-0002`](spec/conformance/scenarios/VP-CS-0002.toml) fixtures published |
| **Reference interpreter** | **Active** — `veritypay-reference` implements **VP-RULE-0001** and **VP-RULE-0002** ([VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md), [VP-RFC-0002](rfcs/0002-claim-identity-binding.md), accepted) |
| **Platform release** | **[Platform 1.2](PLATFORM_RELEASES.md)** — extends Platform 1.1 with accepted **VP-RFC-0003**, **VP-RFC-0004**; **VP-CS-0003** and **VP-CS-0004** fixtures deferred |
| **Independent implementations** | 0 publicly declared conforming implementations |
| **Latest specification update** | 2026-06-29 |
| **Next milestone** | Genesis Edition publication candidate |

*Values reflect repository state at last update. Published Edition and Protocol Version supersede this table when an Edition Manifest exists.*

---

## Core Specification

| Field | Value |
|-------|--------|
| **Document** | [VERITY_CORE.md](VERITY_CORE.md) |
| **Status** | In Progress |
| **Purpose** | Consolidate protocol RFCs into a single implementation-oriented specification |
| **Current scope** | [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) through [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md) |

[VERITY_CORE.md](VERITY_CORE.md) is the primary entry point for protocol implementers. RFCs remain the normative change mechanism; the Core document presents accepted and in-progress RFC content as one coherent specification without introducing new semantics.

---

## Specification health

Legend: 🟢 Complete · 🟡 In progress · ⚪ Not started · 🔴 Blocked

| Area | Status | Summary |
|------|:------:|---------|
| **Constitutional layer** | 🟡 | Manifesto, Vision, Principles, Glossary drafted; not yet Edition-pinned |
| **Architecture** | 🟢 | Five models complete (Architecture Alpha); informative until Genesis |
| **Governance** | 🟡 | GOVERNANCE, versioning, release process, ADR guide, RFC-0000 in place |
| **Terminology** | 🟢 | Glossary v0.4.0; [`spec/terminology/registry.yaml`](spec/terminology/registry.yaml) (40 VP-TERM) |
| **Conformance** | 🟡 | Conformance model draft; **VP-CS-0001** and **VP-CS-0002** executed by `veritypay-conformance` against reference oracle |
| **Reference interpreter** | 🟢 | `veritypay-reference` implements **VP-RULE-0001** and **VP-RULE-0002** per accepted **VP-RFC-0001** and **VP-RFC-0002** |
| **SDKs** | ⚪ | Future; after Protocol Version declaration |
| **Tooling** | 🟡 | Terminology + RFC registries; Edition manifest automation planned |
| **Independent implementations** | ⚪ | None declared |
| **Community** | 🟡 | CONTRIBUTING handbook; public review via RFC process |
| **Documentation** | 🟡 | Pyramid complete; product/research layers scaffolded |
| **Testing** | 🟡 | **VP-CS-0001** and **VP-CS-0002** end-to-end via `veritypay-conformance`; broader VP-CS catalog in prose |

---

## Current Edition

| Field | Value |
|-------|--------|
| **Edition name** | **Genesis Edition** |
| **Protocol Version** | *To be declared at publication* |
| **Publication status** | **In preparation** (Working Draft → Review Candidate) |
| **Publication date** | — |
| **Edition Manifest** | Not yet issued ([`SPECIFICATION_RELEASE_PROCESS.md`](docs/05-governance/SPECIFICATION_RELEASE_PROCESS.md)) |
| **Supported until** | N/A (unpublished) |
| **Successor** | Edition Two *(future; not scoped)* |

Genesis Edition will bundle the constitutional layer, Architecture Alpha, conformance model, governance canon, **VP-RFC-0000** through **VP-RFC-0004**, and registry snapshots per [SPECIFICATION_VERSIONING.md](docs/05-governance/SPECIFICATION_VERSIONING.md). **[Platform 1.2](PLATFORM_RELEASES.md)** names the current compatible engineering baseline that executes **VP-RULE-0001**, **VP-RULE-0002**, **VP-CS-0001**, and **VP-CS-0002**, with normative **Evidence Set** and **Evaluation Policy** semantics from accepted **VP-RFC-0003** and **VP-RFC-0004**.

---

## Canonical documents

Document `status` values reflect front matter at last update. **Draft** means valuable for authors; **Edition-pinned** means published in an Edition manifest.

### Constitutional layer

| Document | Status | Version | Role | Purpose |
|----------|--------|---------|------|---------|
| [MANIFESTO.md](docs/00-overview/MANIFESTO.md) | Draft | 0.1.0 | Mission charter | Public commitments and why VerityPay exists |
| [VISION.md](docs/00-overview/VISION.md) | Draft | 0.1.0 | Strategic north star | Desired future state and success criteria |
| [PRINCIPLES.md](docs/00-overview/PRINCIPLES.md) | Draft | 0.1.0 | Decision heuristics | Engineering values for RFC and design review |
| [GLOSSARY.md](docs/00-overview/GLOSSARY.md) | Draft | 0.4.0 | Terminology authority | Canonical vocabulary (**VP-TERM-***) |

### Architecture

| Document | Status | Version | Role | Purpose |
|----------|--------|---------|------|---------|
| [DOMAIN_MODEL.md](docs/01-architecture/DOMAIN_MODEL.md) | Draft | 0.3.0 | Domain + protocol boundary | Truth, trust, and what the protocol claims |
| [IDENTITY_MODEL.md](docs/01-architecture/IDENTITY_MODEL.md) | Draft | 0.1.0 | Identity semantics | Stable identity across representations |
| [BEHAVIOR_MODEL.md](docs/01-architecture/BEHAVIOR_MODEL.md) | Draft | 0.1.0 | Behavioral semantics | Verbs, events, and invariants |
| [DATA_MODEL.md](docs/01-architecture/DATA_MODEL.md) | Draft | 0.2.0 | Structural semantics | Entities and representation guarantees |
| [STATE_MODEL.md](docs/01-architecture/STATE_MODEL.md) | Draft | 0.1.0 | State semantics | Knowledge states and lifecycles |

### Governance

| Document | Status | Version | Role | Purpose |
|----------|--------|---------|------|---------|
| [GOVERNANCE.md](docs/05-governance/GOVERNANCE.md) | Draft | 0.1.0 | Authority model | RFC governance and Architecture Alpha freeze |
| [ADR_GUIDE.md](docs/05-governance/ADR_GUIDE.md) | Canonical | 1.0.0 | ADR process | Record engineering decisions without normative weight |
| [SPECIFICATION_VERSIONING.md](docs/05-governance/SPECIFICATION_VERSIONING.md) | Canonical | 1.0.0 | Version policy | Editions, Protocol Version, document versions |
| [SPECIFICATION_RELEASE_PROCESS.md](docs/05-governance/SPECIFICATION_RELEASE_PROCESS.md) | Canonical | 1.0.0 | Release process | Edition publication lifecycle |

### Development

| Document | Status | Version | Role | Purpose |
|----------|--------|---------|------|---------|
| [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md) | Draft | 0.1.0 | Conformance framework | Pyramid levels and VP-CS scenarios |

### Research & product

| Area | Status | Role | Purpose |
|------|--------|------|---------|
| [02-product/](docs/02-product/) | ⚪ Scaffold | Product mapping | Participant-facing workflows *(future)* |
| [04-research/](docs/04-research/) | ⚪ Scaffold | Exploration | Pre-normative ideas before RFC promotion |

### RFCs

| Document | Status | Version | Role | Purpose |
|----------|--------|---------|------|---------|
| [VP-RFC-0000](rfcs/0000-rfc-process.md) | **Accepted** | 1.1.0 | Meta-RFC | How protocol changes are proposed and accepted |
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | **Accepted** | 0.1.0 | Protocol | Minimal claim/evidence envelopes, **VP-RULE-0001**, **VP-CS-0001** |
| [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) | **Accepted** | 0.1.0 | Protocol | Claim identity binding, **VP-RULE-0002**, **VP-CS-0002** |
| [VP-RFC-0003](rfcs/0003-multiple-evidence.md) | **Accepted** | 0.1.0 | Protocol | **Evidence Set**, multiple evidence per claim, **VP-CS-0003** (loading profile) |
| [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md) | **Accepted** | 0.1.0 | Protocol | **Evaluation Policy**, **`ALL_REQUIRED`**, **VP-CS-0004** (profile) |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | Draft | 0.1.0 | Protocol | **Assertion Type**, **`body_equality`** taxonomy |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | Draft | 0.1.0 | Protocol | **Evaluation Dispatch**, **Body Equality Evaluator** |
| [VP-RFC-0007](rfcs/0007-verification-context.md) | Draft | 0.1.0 | Protocol | **Verification Context** — immutable evaluation environment |
| [VP-RFC-0008](rfcs/0008-verification-profiles.md) | Draft | 0.1.0 | Protocol | **Verification Profile**, **`minimal_all_required`** |
| [VP-RFC-0009](rfcs/0009-verification-context-extensions.md) | Draft | 0.1.0 | Protocol | **Context Extension** model — no standardized extensions |
| [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md) | Draft | 0.1.0 | Protocol | **Protocol Capability** — feature identifiers and conformance eligibility |

---

## Protocol core

Protocol RFCs that define executable verification inputs and rules. Status reflects this repository only—not downstream implementation claims.

| RFC | Status | Capability |
|-----|--------|------------|
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | **Accepted** | Minimal claim/evidence envelopes, **VP-RULE-0001**, **VP-CS-0001** |
| [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) | **Accepted** | Evidence claim binding, **VP-RULE-0002**, **VP-CS-0002** |
| [VP-RFC-0003](rfcs/0003-multiple-evidence.md) | **Accepted** | **Evidence Set** — multiple evidence per claim; **VP-CS-0003** loading profile |
| [VP-RFC-0004](rfcs/0004-evidence-evaluation-policies.md) | **Accepted** | **Evaluation Policy** — **`ALL_REQUIRED`**; **VP-CS-0004** profile |
| [VP-RFC-0005](rfcs/0005-assertion-types.md) | **Draft** | **Assertion Type** — **`body_equality`**; dispatch deferred to **VP-RFC-0006** |
| [VP-RFC-0006](rfcs/0006-assertion-evaluation-dispatch.md) | **Draft** | **Evaluation Dispatch** — **`body_equality`** → **Body Equality Evaluator** → **VP-RULE-0001** |
| [VP-RFC-0007](rfcs/0007-verification-context.md) | **Draft** | **Verification Context** — `edition`, `protocol_version`, `evaluation_policy`; implementation deferred |
| [VP-RFC-0008](rfcs/0008-verification-profiles.md) | **Draft** | **Verification Profile** — **`minimal_all_required`**; implementation deferred |
| [VP-RFC-0009](rfcs/0009-verification-context-extensions.md) | **Draft** | **Context Extension** model — extension identifiers and ignore-unless-required rules; no standardized extensions |
| [VP-RFC-0010](rfcs/0010-protocol-capability-negotiation.md) | **Draft** | **Protocol Capability** — stable feature identifiers; conformance **skip** when capability absent |

Platform release is **[Platform 1.2](PLATFORM_RELEASES.md)**. Executable **VP-CS-0003** and **VP-CS-0004** fixtures remain deferred until reference and conformance support multi-evidence evaluation.

---

## Registries

| Registry | Purpose | Status | Machine-readable | Human-readable |
|----------|---------|--------|------------------|----------------|
| **VP-TERM** | Canonical terminology | Active | [`spec/terminology/registry.yaml`](spec/terminology/registry.yaml) | [GLOSSARY.md](docs/00-overview/GLOSSARY.md) |
| **VP-RFC** | Accepted RFC index | Active | [`spec/rfcs/registry.yaml`](spec/rfcs/registry.yaml) | [`rfcs/`](rfcs/) |
| **VP-CS** | Conformance scenarios | Draft in spec | [`spec/conformance/scenarios/`](spec/conformance/scenarios/) — **VP-CS-0001**, **VP-CS-0002** fixtures; dedicated registry *future* | [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md) |
| **VP-ADR** | Engineering decisions | Planned | *Future* | [ADR_GUIDE.md](docs/05-governance/ADR_GUIDE.md) |
| **VP-EDITION** | Published Edition manifests | Planned | *Future* | [SPECIFICATION_RELEASE_PROCESS.md](docs/05-governance/SPECIFICATION_RELEASE_PROCESS.md) |

---

## Repository ecosystem

| Repository | Purpose | Status |
|------------|---------|--------|
| **veritypay-spec** | Canonical specification, RFCs, registries | **Active** (this repository) |
| **veritypay-core** | Reference / core implementation | *Separate repo; existence assumed by docs—not tracked here* |
| **veritypay-reference** | Reference interpreter | 🟢 **Active** — implements **VP-RULE-0001**, **VP-RULE-0002** |
| **veritypay-conformance** | Executable VP-CS suite | 🟢 **Active** — executes spec-published **VP-CS-0001**, **VP-CS-0002** |
| **veritypay-sdk-*** | Language SDKs | ⚪ Future |
| **veritypay-website** | Public specification site | ⚪ Future |

Implementation repositories MUST declare target Edition and Protocol Version when conforming—not merely a git tag.

---

## Current milestones

| Milestone | Status | Description |
|-----------|:------:|-------------|
| **Foundation** | 🟢 | Repo structure, pyramid, templates, CONTRIBUTING |
| **Constitutional layer** | 🟡 | Draft complete; awaiting Genesis pin |
| **Architecture Alpha** | 🟢 | Five models frozen structurally |
| **Governance canon** | 🟡 | Process docs canonical; GOVERNANCE draft |
| **RFC process** | 🟢 | VP-RFC-0000 accepted; author guide published |
| **Genesis Edition** | 🟡 | In preparation; manifest not issued |
| **Reference interpreter** | 🟢 | **VP-RULE-0001**, **VP-RULE-0002** in `veritypay-reference` |
| **Conformance suite** | 🟢 | **VP-CS-0001**, **VP-CS-0002** end-to-end; spec fixture path in harness |
| **Developer preview** | ⚪ | Post-Genesis + interpreter |
| **Protocol 1.0** | ⚪ | Declared at Genesis publication (target) |

---

## Road to Protocol 1.0

Capability-based progress—not a calendar roadmap. Check when the capability exists, not when a date arrives.

- [x] Constitutional layer drafted
- [x] Governance process documented (RFC-0000, versioning, release process, ADR guide)
- [x] Architecture Alpha (five models)
- [x] Terminology registry (**VP-TERM**)
- [x] RFC registry scaffold (**VP-RFC**)
- [x] Conformance model (draft scenarios VP-CS-0001–0005)
- [x] **VP-RFC-0001** accepted (minimal claim/evidence semantics)
- [x] **VP-RFC-0002** accepted (claim identity binding)
- [x] **VP-RFC-0003** accepted (multiple evidence, **Evidence Set**)
- [x] **VP-RFC-0004** accepted (**Evaluation Policy**, **`ALL_REQUIRED`**)
- [x] Reference interpreter executes **VP-RULE-0001** and **VP-RULE-0002**
- [x] Conformance suite runs spec-published **VP-CS-0001** and **VP-CS-0002**
- [ ] **Genesis Edition published** (Edition Manifest + Protocol Version)
- [ ] Public SDK (at least one language)
- [ ] Independent implementation #1 (declared conformance)
- [ ] Independent implementation #2 (declared conformance)
- [ ] Public specification website
- [ ] **Protocol 1.0** declared and citeable via published Edition

Protocol 1.0 is a **published agreement**, not a line of code shipped.

---

## Open work

Institutional priorities—not a issue tracker.

### High priority

- **Genesis Edition readiness** — Run release checklist; prepare Edition Manifest draft
- **Registry synchronization** — Keep glossary and `registry.yaml` aligned on each terminology change
- **Conformance scenario hardening** — VP-CS-0001–0005 ready for Edition baseline

### Medium priority

- **Reference interpreter** — Repository scaffold; language choice via ADR
- **Edition tooling** — Manifest generation and validation (vision in release process)
- **GOVERNANCE adoption** — Move from draft to Edition-pinned status with Genesis

### Long term

- **Registry automation** — Cross-reference and dependency graph validation
- **Public website** — Edition and registry browser for auditors and integrators
- **Certification program** — Beyond self-declared conformance (policy not defined)
- **Multiple independent implementations** — Ecosystem proof of interoperability

---

## How to contribute

| Path | Start here |
|------|------------|
| **General onboarding** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| **Protocol change** | [RFC Author Guide](rfcs/templates/RFC_TEMPLATE.md) · [VP-RFC-0000](rfcs/0000-rfc-process.md) |
| **Engineering decision** | [ADR Guide](docs/05-governance/ADR_GUIDE.md) |
| **Governance & roles** | [GOVERNANCE.md](docs/05-governance/GOVERNANCE.md) |
| **Terminology** | [GLOSSARY.md](docs/00-overview/GLOSSARY.md) |

**Implementation follows specification.** Code that precedes accepted RFCs or a published Edition is exploratory—not normative. Conforming implementations declare Edition and Protocol Version explicitly.

---

## Change log

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2026-06-29 | Initial public specification status dashboard |

---

## Closing

A specification becomes trustworthy through **consistency**.

It becomes useful through **implementation**.

It becomes infrastructure through **community**.

---

*This document should be updated when Edition state, registry counts, or milestone status changes materially. Future automation may generate sections from Edition manifests and registries.*

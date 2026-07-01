---
document: Platform Releases
version: 1.0.0
status: canonical
last_updated: 2026-06-29
related:
  - ADR-0008
  - SPECIFICATION_STATUS.md
  - ECOSYSTEM.md
---

**Document:** Platform Releases · **Version:** 1.0.0 · **Status:** canonical (living document)

**Last updated:** 2026-06-29 · **Policy:** [ADR-0008 — Platform Release Policy](docs/adrs/0008-platform-release-policy.md)

---

# Platform Releases

**What official Verity Platform releases exist, and which repository baselines are compatible?**

This document is the public **compatibility index** for the Verity engineering platform. It does not define protocol behavior—that remains in accepted RFCs and published Editions in this repository.

For specification maturity detail, see [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md). For repository roles, see [ECOSYSTEM.md](ECOSYSTEM.md).

---

## What is a Platform Release?

Users consume the **Verity ecosystem as one platform**, not as four isolated repositories checked out at arbitrary commits.

Each repository has a single responsibility:

| Repository | Role |
|------------|------|
| **veritypay-spec** | Defines protocol meaning |
| **veritypay-tooling** | Validates the specification |
| **veritypay-reference** | Executes protocol semantics |
| **veritypay-conformance** | Compares independent implementations |

A **Platform Release** names a **compatible set** of those repositories (and the **Specification Edition** they target) so integrators, auditors, and CI can pin a reproducible baseline.

Platform Releases describe **ecosystem compatibility**—not individual crate semver bumps inside a workspace. See [ADR-0008](docs/adrs/0008-platform-release-policy.md) for governance rules.

### Compatibility flow

```text
veritypay-spec
        │
        ▼
veritypay-tooling
        │
        ▼
veritypay-reference
        │
        ▼
veritypay-conformance
```

**Flow:** The specification corpus is authoritative → tooling validates it → the reference interpreter executes accepted semantics → conformance loads spec-published VP-CS scenarios and compares implementations to the oracle.

---

## Official releases

| Platform Release | Specification Edition | Supported RFCs | Supported Rules | Supported VP-CS | Tooling | Reference | Conformance | Status |
|------------------|----------------------|----------------|-----------------|-----------------|---------|-----------|-------------|--------|
| **Platform 1.0** | Genesis Edition *(in preparation)* | VP-RFC-0000 (accepted); VP-RFC-0001 (accepted) | VP-RULE-0001 | VP-CS-0001 | Validation Platform Ready | Reference Interpreter Ready | Conformance Platform Ready | **Current** |

### Platform 1.0 — notes

| Field | Detail |
|-------|--------|
| **Specification** | [Genesis Edition](docs/05-governance/SPECIFICATION_VERSIONING.md) — constitutional layer, Architecture Alpha, conformance model, governance canon, and initial RFC set. Edition manifest publication is the specification-side gate for declaring Platform 1.0 final. |
| **Supported RFCs** | [VP-RFC-0000](rfcs/0000-rfc-process.md) (RFC Process, accepted); [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) (Minimal Claim and Evidence Semantics, **accepted**) |
| **Supported Rules** | [VP-RULE-0001](rfcs/0001-minimal-claim-evidence-semantics.md) — Assertion Body Evidence Match |
| **Supported VP-CS** | [VP-CS-0001](spec/conformance/scenarios/VP-CS-0001.toml) — minimal claim satisfied by matching evidence |
| **Engineering baselines** | Phase II complete across tooling, reference, and conformance; spec-published VP-CS loading verified |

Platform 1.0 marks the first **engineering platform** release: validation, reference oracle, and conformance harness operate as a coordinated ecosystem. Protocol expansion (Phase III) adds RFCs, rules, and scenarios **on top of** this baseline.

---

## Versioning philosophy

Platform versioning is **independent** of per-repository crate semver. It describes **compatibility across the ecosystem**.

| Level | Meaning | Examples |
|-------|---------|----------|
| **Major** | **Breaking platform compatibility** — prior conformance claims or integration pins may no longer hold; a new Specification Edition or Protocol Version baseline is required | New Edition that supersedes normative semantics; retired outcome vocabulary; incompatible VP-CS outcome changes for the same inputs under a published Edition |
| **Minor** | **Backward-compatible protocol capability additions** — new behavior that does not invalidate prior pins under the same Platform major | New accepted RFCs; additional VP-RULE definitions; new VP-CS scenarios; expanded reference rule coverage |
| **Patch** | **Documentation, tooling, and fixes** — no change to platform compatibility when behavior matches accepted specification | Corpus validation fixes; reference bug fixes restoring spec semantics; conformance loader hardening; specification clarifications that do not alter normative behavior |

Repositories continue to tag and version **internally** (Cargo crates, document revisions). A Platform Release **composes** those tags into one compatibility statement.

---

## Future Platform Releases

New **RFCs**, **verification rules**, and **VP-CS scenarios** expand the platform while **maintaining compatibility whenever possible** under the current Platform major version.

| Change type | Typical platform impact |
|-------------|-------------------------|
| New draft RFC + rule + scenario (compatible) | Extends Platform 1.x; update this table |
| RFC acceptance without semantic change | Documentation and registry update; same Platform release |
| Breaking normative semantic change | Requires new Platform **major** and new Edition baseline |
| Engineering-only fix | Patch under same Platform release |

Future rows (informative placeholders):

| Platform Release | Trigger | Status |
|------------------|---------|--------|
| **Platform 1.1** | Additional accepted RFCs, rules, and VP-CS coverage under Genesis Edition | Planned |
| **Platform 2.0** | New published Edition with breaking protocol baseline | Planned |

Maintainers update this document when a Platform Release is declared or extended. [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md) summarizes living maturity; this document is the **compatibility contract**.

---

## Related documents

| Document | Role |
|----------|------|
| [ADR-0008 — Platform Release Policy](docs/adrs/0008-platform-release-policy.md) | Governance rules for platform releases |
| [RELEASE_NOTES_PLATFORM_1_0.md](RELEASE_NOTES_PLATFORM_1_0.md) | Platform 1.0 release summary |
| [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md) | Specification and ecosystem maturity dashboard |
| [ECOSYSTEM.md](ECOSYSTEM.md) | Repository responsibilities and reading order |
| [SPECIFICATION_VERSIONING.md](docs/05-governance/SPECIFICATION_VERSIONING.md) | Edition and Protocol Version semantics |
| [SPECIFICATION_RELEASE_PROCESS.md](docs/05-governance/SPECIFICATION_RELEASE_PROCESS.md) | How Editions are published |

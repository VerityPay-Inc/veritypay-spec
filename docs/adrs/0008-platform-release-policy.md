---
id: ADR-0008
title: Platform Release Policy
status: accepted
version: 1.0.0
authors:
  - VerityPay Core Team
reviewers: []
related_docs:
  - README.md
  - ECOSYSTEM.md
  - SPECIFICATION_STATUS.md
  - docs/05-governance/SPECIFICATION_VERSIONING.md
  - docs/05-governance/SPECIFICATION_RELEASE_PROCESS.md
decision_date: 2026-06-29
superseded_by: null
---

# ADR-0008 — Platform Release Policy

**Status:** Accepted · **Version:** 1.0.0 · **Date:** 2026-06-29

**Related:** [README.md](../../README.md) · [ECOSYSTEM.md](../../ECOSYSTEM.md) · [SPECIFICATION_STATUS.md](../../SPECIFICATION_STATUS.md) · [SPECIFICATION_VERSIONING.md](../05-governance/SPECIFICATION_VERSIONING.md) · [SPECIFICATION_RELEASE_PROCESS.md](../05-governance/SPECIFICATION_RELEASE_PROCESS.md) · [veritypay-tooling — ADR-0007](https://github.com/VerityPay-Inc/veritypay-tooling/blob/main/docs/adrs/0007-specification-model-stability.md) · [veritypay-reference — ADR-0007](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md)

---

## Purpose

Define how the **Verity Platform** evolves across repositories and how **platform releases** are versioned.

---

## Context

The platform now consists of four primary engineering repositories, each with a single responsibility:

| Repository | Role |
|------------|------|
| [**veritypay-spec**](https://github.com/VerityPay-Inc/veritypay-spec) | Defines **protocol meaning** — normative text, registries, RFCs, VP-CS scenario authorship |
| [**veritypay-tooling**](https://github.com/VerityPay-Inc/veritypay-tooling) | **Validates** the specification corpus — registries, cross-references, Edition manifests |
| [**veritypay-reference**](https://github.com/VerityPay-Inc/veritypay-reference) | **Executes** protocol semantics — reference interpreter oracle |
| [**veritypay-conformance**](https://github.com/VerityPay-Inc/veritypay-conformance) | **Compares** independent implementations to the reference oracle under VP-CS scenarios |

Users consume the platform as **one engineering ecosystem**, not as isolated repositories. The specification defines protocol meaning. Tooling validates the specification. Reference executes protocol semantics. Conformance compares independent implementations.

Phase II delivered that engineering platform. Without a release policy, repository versions may drift independently and **compatibility becomes unclear**—implementers cannot know which specification Edition, tooling release, reference interpreter, and conformance harness belong together.

---

## Decision

Introduce the concept of a **Platform Release**.

A **Platform Release** identifies a **compatible set** of:

- **Specification Edition** (published bundle from `veritypay-spec`)
- **veritypay-tooling** (validation and `vp-spec-model` baseline)
- **veritypay-reference** (reference interpreter baseline)
- **veritypay-conformance** (conformance harness baseline)

Platform Releases are **documented compatibility statements**. They do not replace repository tags or crate versions; they **compose** them into a reproducible baseline integrators, auditors, and grant reviewers can cite.

---

## Rules

### 1. Platform releases describe ecosystem compatibility

A Platform Release names a **supported combination** of specification and engineering artifacts. It answers: *"Which spec Edition, tooling, reference, and conformance versions were verified to work together?"*

Platform Releases are **not** individual crate semver bumps. They are **compatibility contracts** at the ecosystem layer.

### 2. Repositories keep independent semantic versioning

Each repository continues to use **independent semantic versioning** internally:

- Cargo crate versions in tooling, reference, and conformance workspaces
- Document and registry versions within `veritypay-spec`
- ADR and engineering milestone records per repository

A Platform Release **references** those versions; it does not merge them into a single monorepo version number.

### 3. Breaking protocol changes require a new Platform major version

A **breaking protocol change**—one that invalidates prior conformance claims or requires implementations to change observable behavior under a published Edition—requires a **new Platform major version**.

Examples include:

- Superseding normative semantics that alter verification outcomes for the same inputs
- Retiring or renaming normative outcome vocabulary
- Publishing a new Edition that explicitly supersedes a prior Protocol Version baseline

Engineering-only refactors that preserve protocol behavior do **not** require a Platform major bump.

### 4. Compatible extensions stay within the current Platform major version

**New RFCs**, **verification rules**, and **VP-CS scenarios** that remain **backward compatible** with the published Edition and Protocol Version **extend** the current Platform major version.

Examples include:

- Adding VP-RULE-0002 while VP-RULE-0001 behavior is unchanged
- Publishing new VP-CS fixtures that exercise additional rules without altering prior scenario outcomes
- Accepting clarifying RFCs that do not change normative behavior

Such additions are recorded in platform release notes and compatibility tables as **minor platform extensions**, not new Platform majors.

### 5. Bug fixes do not change Platform compatibility

**Bug fixes**—corrections where an engineering artifact failed to implement accepted specification semantics—**do not** change Platform compatibility when:

- The fix restores behavior to match the published Edition and accepted RFCs
- Prior incorrect behavior is documented as a defect, not as protocol truth

Patch-level repository releases may ship under the **same Platform Release** after maintainer verification. If a fix reveals that specification text was wrong, the change follows **RFC process** in `veritypay-spec`; it is not silently classified as an implementation bug.

---

## Consequences

### Positive

- **Clear compatibility** — integrators know which repositories and Edition pins belong together
- **Simpler onboarding** — one platform baseline instead of four independent version puzzles
- **Reproducible implementations** — audits and CI can pin a Platform Release and reproduce outcomes
- **Easier grants and audits** — reviewers cite a named platform baseline with traceable artifact versions

### Negative

- **Supported combinations must be documented** — maintainers must publish and update compatibility tables
- **Release coordination across repositories** — platform releases require cross-repo verification before declaration
- **Governance overhead** — incompatible drift must be caught before it reaches integrators

---

## Future

### Platform 1.0

**Platform 1.0** will be declared when the first **published Specification Edition** (Genesis) is paired with verified **tooling**, **reference**, and **conformance** baselines that together support reproducible VP-CS execution against that Edition.

Platform 1.0 is **not** declared when any single repository reaches `1.0.0`. It is declared when the **ecosystem combination** is verified and documented.

### Genesis Edition

[**Genesis Edition**](https://github.com/VerityPay-Inc/veritypay-spec/blob/main/docs/05-governance/SPECIFICATION_VERSIONING.md) is the first planned published Edition bundle—constitutional layer, Architecture Alpha, conformance model, governance canon, and initial RFC set. Genesis publication triggers Platform 1.0 candidacy per [SPECIFICATION_RELEASE_PROCESS.md](../05-governance/SPECIFICATION_RELEASE_PROCESS.md).

Until Genesis is published, platform releases remain **pre-1.0 engineering baselines** documented in [SPECIFICATION_STATUS.md](../../SPECIFICATION_STATUS.md) and sibling repository README files.

### Future Editions

Later Editions (e.g. Edition 2) may coincide with **Platform 2.0** when they introduce breaking protocol baselines. Non-breaking Edition amendments may extend Platform 1.x compatibility when governance confirms backward compatibility.

### Platform compatibility table

Maintainers will publish a **Platform compatibility table**—initially in [SPECIFICATION_STATUS.md](../../SPECIFICATION_STATUS.md) and sibling ROADMAP documents, eventually as a machine-readable manifest when Edition and platform release infrastructure matures.

Illustrative shape (informative; values TBD at Platform 1.0 declaration):

| Platform Release | Specification Edition | Protocol Version | veritypay-tooling | veritypay-reference | veritypay-conformance |
|------------------|----------------------|------------------|-------------------|---------------------|------------------------|
| *Platform 1.0* | Genesis Edition | `vp-protocol-1.0` | *tag TBD* | *tag TBD* | *tag TBD* |

The table is the authoritative **compatibility index** for integrators. Individual repository README and ROADMAP files link to it; they do not each invent independent compatibility claims.

---

## Related documents

| Document | Relationship |
|----------|--------------|
| [README.md](../../README.md) | Specification home; links to platform status |
| [ECOSYSTEM.md](../../ECOSYSTEM.md) | Repository roles and platform flow |
| [SPECIFICATION_STATUS.md](../../SPECIFICATION_STATUS.md) | Living maturity dashboard; future home of compatibility table |
| [SPECIFICATION_VERSIONING.md](../05-governance/SPECIFICATION_VERSIONING.md) | Edition and Protocol Version semantics |
| [SPECIFICATION_RELEASE_PROCESS.md](../05-governance/SPECIFICATION_RELEASE_PROCESS.md) | How Editions are published |
| [veritypay-tooling — ROADMAP](https://github.com/VerityPay-Inc/veritypay-tooling/blob/main/ROADMAP.md) | Tooling capability milestones |
| [veritypay-reference — ROADMAP](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/ROADMAP.md) | Reference interpreter milestones |
| [veritypay-conformance — ROADMAP](https://github.com/VerityPay-Inc/veritypay-conformance/blob/main/ROADMAP.md) | Conformance harness milestones |
| [veritypay-tooling — ADR-0007](https://github.com/VerityPay-Inc/veritypay-tooling/blob/main/docs/adrs/0007-specification-model-stability.md) | Stable `vp-spec-model` integration surface |
| [veritypay-reference — ADR-0007](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md) | Stable `Interpreter::evaluate` public contract |

---

## Conclusion

The **platform**—not any individual repository—is the **primary compatibility contract**.

`veritypay-spec` defines meaning. Sibling repositories implement validation, execution, and comparison. Semantic versioning remains valuable **inside** each repository. **Platform Releases** compose those artifacts into a single reproducible baseline that independent implementations, auditors, and the ecosystem can trust.

When in doubt, cite a **Platform Release** and its **Specification Edition** pin—not an isolated crate version—as the compatibility anchor.

# Development

Guidance for people who write, test, review, or certify software that implements the VerityPay protocol.

---

## Purpose

Development documentation connects the abstract specification to engineering practice. It explains how implementers should interpret normative text, demonstrate conformance, and contribute improvements back to the specification.

This folder serves implementers and specification contributors. It does not replace implementation repositories—it orients engineers toward them.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Core protocol engineers | Build conformant implementations |
| Third-party integrators | Certify interoperability with the spec |
| QA and conformance testers | Design validation suites |
| Spec contributors | Write precise, testable requirements |
| SDK and documentation maintainers | Align public materials with normative sources |

Implementers should identify the RFC set they target (see [`../../rfcs/`](../../rfcs/)), read relevant architecture in [`../01-architecture/`](../01-architecture/), then follow conformance guidance here.

---

## Scope

**In scope**

- Implementer's guide — how to read RFCs, architecture docs, and test vectors together
- Conformance definition — what "VerityPay-compliant" means and how compliance is assessed
- Test vector specifications — expected inputs and outputs defined declaratively
- Versioning and compatibility — how spec versions map to implementation releases
- Reference implementation policy — role and non-normative status of any reference software
- Contribution guide for this repository — formatting, linking, and review expectations (documentation only)
- Style and notation guides — unambiguous specification prose, diagrams, and tables
- Issue triage guidance — distinguishing spec defects from implementation defects

**Out of scope**

- Application source code → implementation repositories (e.g. `veritypay-core`)
- CI pipelines, container images, or package manifests
- Language-specific API reference generated from code
- Exploratory design notes → [`../04-research/`](../04-research/)
- Governance voting rules → [`../05-governance/`](../05-governance/)
- Product marketing or end-user tutorials → [`../02-product/`](../02-product/)

Test vectors specify **expected behavior**; executables that run them belong in implementation repositories.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../../rfcs/`](../../rfcs/) | Normative behavior implementations must satisfy |
| [`../01-architecture/`](../01-architecture/) | Invariants and models conformance builds upon |
| [`../02-product/`](../02-product/) | Observable outcomes conformance should produce |
| [`../05-governance/`](../05-governance/) | Escalation when spec and implementation diverge |
| [`../templates/SPEC_TEMPLATE.md`](../templates/SPEC_TEMPLATE.md) | Format for test vectors and implementer-facing spec documents |
| Implementation repositories | Software, tests, and release artifacts (non-normative) |

---

## Relationship to implementation repositories

| Topic | Where it lives |
|-------|----------------|
| Normative protocol rules | This repository (RFCs + architecture) |
| Source code and unit tests | Implementation repositories |
| Release artifacts and changelogs | Implementation repositories |
| Conformance criteria | This repository |
| Conformance test runners | Implementation repositories (may consume vectors from this repo) |

When implementation behavior appears to contradict the spec, follow the escalation path in [`../05-governance/`](../05-governance/).

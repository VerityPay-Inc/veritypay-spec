# Development

Guidance for people who write, test, review, or certify software that implements the VerityPay protocol.

---

## Purpose

Development documentation connects the abstract specification to engineering practice. It explains how implementers should interpret normative text, demonstrate conformance, and contribute improvements back to the specification.

This folder serves the **implementer and contributor** audience. It does not replace implementation repositories—it orients developers toward them.

---

## What belongs here

- **Implementer's guide** — how to read RFCs, architecture docs, and test vectors together
- **Conformance definition** — what "VerityPay-compliant" means and how compliance is assessed
- **Test vector specifications** — expected inputs and outputs for protocol behavior (defined declaratively)
- **Versioning and compatibility** — how spec versions map to implementation releases
- **Reference implementation policy** — whether a reference exists, its role, and its non-normative status
- **Contribution guide for spec repo** — formatting, linking, review expectations, and tooling (documentation-only)
- **Style and notation guides** — how to write unambiguous specification prose, diagrams, and tables
- **Issue triage guidance** — distinguishing spec bugs from implementation bugs

---

## What does not belong here

- Application source code → implementation repositories (e.g. `veritypay-core`)
- CI pipelines, Dockerfiles, or package manifests
- Language-specific API reference generated from code
- Exploratory design notes → [`../04-research/`](../04-research/)
- Governance voting rules → [`../05-governance/`](../05-governance/)
- Product marketing or user tutorials → [`../02-product/`](../02-product/)

Test vectors specify **expected behavior**; the code that executes them belongs in implementation repositories.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Core protocol engineers | Build conformant implementations |
| Third-party integrators | Certify interoperability with the spec |
| QA and conformance testers | Design validation suites |
| Spec contributors | Write precise, testable requirements |
| DevRel and SDK maintainers | Align public docs with normative sources |

Implementers should identify the RFC set they target (see [`../../rfcs/`](../../rfcs/)), read relevant architecture in [`../01-architecture/`](../01-architecture/), then follow conformance guidance here.

---

## Relationship to implementation repositories

| Topic | Where it lives |
|-------|----------------|
| Normative protocol rules | This repo (RFCs + architecture) |
| Source code and unit tests | Implementation repos |
| Release artifacts and changelogs | Implementation repos |
| Conformance criteria | This repo |
| Conformance test runners | Implementation repos (may consume vectors from this repo) |

When implementation behavior appears to contradict the spec, follow the escalation path defined in [`../05-governance/`](../05-governance/).

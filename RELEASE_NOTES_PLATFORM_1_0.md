---
document: Verity Platform 1.0 Release Notes
version: 1.0.0
status: canonical
last_updated: 2026-06-29
related:
  - PLATFORM_RELEASES.md
  - ADR-0008
  - VP-RFC-0001
---

**Document:** Verity Platform 1.0 Release Notes · **Version:** 1.0.0 · **Status:** canonical

**Last updated:** 2026-06-29 · **Compatibility index:** [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)

---

# Verity Platform 1.0

**The first complete engineering platform for VerityPay.**

Platform 1.0 is not a single repository tag. It is the first **coordinated baseline** where specification meaning, corpus validation, reference execution, and conformance comparison operate as one reproducible ecosystem. Phase II (**Engineering Platform**) is complete; Phase III (**Protocol Expansion**) grows normative semantics on top of this foundation.

---

## Genesis Edition

Platform 1.0 targets the **Genesis Edition** specification bundle—constitutional layer, Architecture Alpha, conformance model, governance canon, and the initial accepted RFC set. The Edition manifest remains in preparation; engineering repositories already satisfy the Platform 1.0 capability baseline documented in [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md).

---

## Repositories

| Repository | Role | Platform 1.0 status |
|------------|------|---------------------|
| [**veritypay-spec**](https://github.com/VerityPay-Inc/veritypay-spec) | Normative protocol meaning, RFCs, VP-CS authorship | Specification foundation; **VP-RFC-0001** accepted |
| [**veritypay-tooling**](https://github.com/VerityPay-Inc/veritypay-tooling) | Corpus validation, `vp-spec-model`, Edition checks | **Validation Platform Ready** |
| [**veritypay-reference**](https://github.com/VerityPay-Inc/veritypay-reference) | Reference interpreter oracle | **Reference Interpreter Ready** |
| [**veritypay-conformance**](https://github.com/VerityPay-Inc/veritypay-conformance) | VP-CS harness and comparison | **Conformance Platform Ready** |

Each repository retains **one primary responsibility**. Platform 1.0 names their **compatible combination**—see [ADR-0008 — Platform Release Policy](docs/adrs/0008-platform-release-policy.md).

---

## Protocol

### Accepted RFCs

| ID | Title | Status |
|----|-------|--------|
| [VP-RFC-0000](rfcs/0000-rfc-process.md) | RFC Process | Accepted |
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | Minimal Claim and Evidence Semantics | **Accepted** |

### Implemented rules

| ID | Name | RFC |
|----|------|-----|
| **VP-RULE-0001** | Assertion Body Evidence Match | [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) |

`veritypay-reference` implements **VP-RULE-0001** as normative protocol semantics (replacing prior reference-only scaffolding).

### Executable scenarios

| ID | Name | Fixture |
|----|------|---------|
| **VP-CS-0001** | Minimal claim is satisfied by matching evidence | [`spec/conformance/scenarios/VP-CS-0001.toml`](spec/conformance/scenarios/VP-CS-0001.toml) |

`veritypay-conformance` loads and executes the spec-published **VP-CS-0001** fixture, comparing implementation adapters against the reference oracle.

---

## Platform capabilities

Platform 1.0 delivers the engineering spine required before independent implementations scale:

| Capability | Evidence |
|------------|----------|
| **Validated specification** | `vp validate` over `veritypay-spec` via `veritypay-tooling` |
| **Typed specification model** | `vp-spec-model` — registries, document corpus, reference graph |
| **Reference interpreter** | `Interpreter::evaluate` → `VerificationResult` per reference ADR-0007 |
| **Conformance runner** | Load scenario → oracle + adapter → compare → report |
| **CLI** | `vp-conformance run`, `vp-reference`, `vp validate` |
| **Reports** | Human and JSON conformance summaries |
| **Readiness gates** | Local fmt, clippy, test, and smoke scripts in sibling repositories |

---

## Future work

**Platform 1.1** will expand protocol capabilities through new **RFCs**, **verification rules**, and **VP-CS scenarios** while preserving compatibility under the Platform 1.0 major version whenever changes remain backward compatible.

Genesis Edition publication, additional VP-CS coverage (VP-CS-0002–0005 narratives), independent implementation adapters, and Edition manifest automation follow the roadmap in [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md)—without rebuilding the platform architecture delivered in Platform 1.0.

For the official compatibility table and versioning philosophy, see [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md).

---

## Closing

**Platform 1.0 establishes the engineering foundation for independent VerityPay implementations.**

The specification defines meaning. Tooling validates it. The reference interpreter executes accepted rules. Conformance proves that independent stacks match the oracle on published scenarios. Protocol expansion continues from this baseline—not from scratch.

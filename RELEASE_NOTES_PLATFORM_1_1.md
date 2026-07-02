---
document: Verity Platform 1.1 Release Notes
version: 1.0.0
status: canonical
last_updated: 2026-06-29
related:
  - PLATFORM_RELEASES.md
  - ADR-0008
  - VP-RFC-0002
---

**Document:** Verity Platform 1.1 Release Notes · **Version:** 1.0.0 · **Status:** canonical

**Last updated:** 2026-06-29 · **Compatibility index:** [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)

---

# Verity Platform 1.1

**First backward-compatible protocol expansion on the Platform 1.0 engineering baseline.**

Platform 1.1 extends the coordinated ecosystem with accepted **VP-RFC-0002** (*Claim Identity Binding*), a multi-rule reference interpreter, and executable **VP-CS-0002**. Platform 1.0 pins remain valid for **VP-RFC-0001** / **VP-RULE-0001** / **VP-CS-0001** conformance claims.

---

## Genesis Edition

Platform 1.1 targets the **Genesis Edition** specification bundle plus accepted **VP-RFC-0002**. The Edition manifest remains in preparation; engineering repositories satisfy the Platform 1.1 capability baseline documented in [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md).

---

## Repositories

| Repository | Role | Platform 1.1 status |
|------------|------|---------------------|
| [**veritypay-spec**](https://github.com/VerityPay-Inc/veritypay-spec) | Normative protocol meaning, RFCs, VP-CS authorship | **VP-RFC-0002** accepted; **VP-CS-0002** fixture published |
| [**veritypay-tooling**](https://github.com/VerityPay-Inc/veritypay-tooling) | Corpus validation, `vp-spec-model`, Edition checks | **Validation Platform Ready** |
| [**veritypay-reference**](https://github.com/VerityPay-Inc/veritypay-reference) | Reference interpreter oracle | **Reference Interpreter Ready** — **VP-RULE-0002** + **VP-RULE-0001** |
| [**veritypay-conformance**](https://github.com/VerityPay-Inc/veritypay-conformance) | VP-CS harness and comparison | **Conformance Platform Ready** — **VP-CS-0002** smoke |

Each repository retains **one primary responsibility**. Platform 1.1 names their **compatible combination**—see [ADR-0008 — Platform Release Policy](docs/adrs/0008-platform-release-policy.md).

---

## Protocol

### Accepted RFCs

| ID | Title | Status |
|----|-------|--------|
| [VP-RFC-0000](rfcs/0000-rfc-process.md) | RFC Process | Accepted |
| [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) | Minimal Claim and Evidence Semantics | Accepted |
| [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) | Claim Identity Binding | **Accepted** |

### Implemented rules

| ID | Name | RFC |
|----|------|-----|
| **VP-RULE-0001** | Assertion Body Evidence Match | [VP-RFC-0001](rfcs/0001-minimal-claim-evidence-semantics.md) |
| **VP-RULE-0002** | Evidence Claim Binding | [VP-RFC-0002](rfcs/0002-claim-identity-binding.md) |

`veritypay-reference` evaluates **VP-RULE-0002** before **VP-RULE-0001**, short-circuiting on binding failure per **VP-RFC-0002** §4.

### Executable scenarios

| ID | Name | Fixture |
|----|------|---------|
| **VP-CS-0001** | Minimal claim is satisfied by matching evidence | [`spec/conformance/scenarios/VP-CS-0001.toml`](spec/conformance/scenarios/VP-CS-0001.toml) |
| **VP-CS-0002** | Evidence with mismatched claim id is indeterminate | [`spec/conformance/scenarios/VP-CS-0002.toml`](spec/conformance/scenarios/VP-CS-0002.toml) |

`veritypay-conformance` loads and executes both spec-published fixtures, comparing implementation adapters against the reference oracle.

---

## Platform capabilities

Platform 1.1 adds binding semantics on top of Platform 1.0:

| Capability | Evidence |
|------------|----------|
| **Multi-rule reference evaluation** | `RuleSet::platform_1()` — **VP-RULE-0002** then **VP-RULE-0001** |
| **Binding conformance scenario** | **VP-CS-0002** end-to-end via `vp-conformance run` |
| **Backward-compatible expansion** | **VP-CS-0001** oracle expectations unchanged |

All Platform 1.0 capabilities remain available: corpus validation, reference oracle, conformance comparison, CLI entry points, and readiness gates.

---

## Compatibility

| Release | Status |
|---------|--------|
| **Platform 1.1** | **Current** — recommended pin for **VP-RFC-0002** support |
| **Platform 1.0** | **Supported** — valid for **VP-RFC-0001** / **VP-CS-0001** claims |

Implementations claiming **VP-RFC-0002** **MUST** pass **VP-CS-0002**. Claiming **VP-RFC-0001** alone does not require **VP-RFC-0002** factoring until the implementation opts in.

---

## Future work

Additional VP-CS scenarios, DATA_MODEL binding cross-references, and Genesis Edition manifest publication follow the roadmap in [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md)—without rebuilding the platform architecture delivered in Platform 1.0.

For the official compatibility table and versioning philosophy, see [PLATFORM_RELEASES.md](PLATFORM_RELEASES.md).

---

## Closing

**Platform 1.1 proves the Phase III protocol expansion model: new RFCs, rules, and VP-CS scenarios compose on the existing engineering platform without breaking prior pins.**

The specification defines meaning. Tooling validates it. The reference interpreter executes accepted rules in order. Conformance proves that independent stacks match the oracle on published scenarios.

# VerityPay Conformance Fixtures

Machine-readable **VP-CS (VerityPay Conformance Scenario)** inputs for the conformance harness.

| Artifact | Role |
|----------|------|
| [`scenarios/`](scenarios/) | TOML scenario fixtures consumed by [`veritypay-conformance`](https://github.com/VerityPay-Inc/veritypay-conformance) |
| [`../../docs/03-development/CONFORMANCE_MODEL.md`](../../docs/03-development/CONFORMANCE_MODEL.md) | Human-readable scenario narratives and conformance philosophy |
| [`../../rfcs/0001-minimal-claim-evidence-semantics.md`](../../rfcs/0001-minimal-claim-evidence-semantics.md) | Normative minimal rule and **VP-CS-0001** profile ([VP-RFC-0001](../../rfcs/0001-minimal-claim-evidence-semantics.md), draft) |

## What these files are

Fixtures are **machine-readable conformance inputs**—structured claim, evidence, binding, and expected oracle outcome data for a scenario ID. They let `veritypay-conformance` load a scenario without embedding protocol meaning in harness code.

## What these files are not

- **Not protocol truth by themselves** — VP-CS meaning remains governed by accepted RFCs and [CONFORMANCE_MODEL.md](../../docs/03-development/CONFORMANCE_MODEL.md).
- **Not hard-coded oracle outcomes** — the `expected.outcome` field records the outcome **veritypay-reference** must produce when it correctly implements the cited rule; it is a test oracle expectation, not a substitute for verification rule text in RFCs.
- **Not a VP-RULE registry** — rule IDs appear in fixtures; normative rule semantics live in RFCs until a dedicated registry is accepted.

## Consumption

[`veritypay-conformance`](https://github.com/VerityPay-Inc/veritypay-conformance) loads fixtures from this directory (or a path declared by the harness), runs the reference oracle and an implementation adapter, and compares results.

Tooling in [`veritypay-tooling`](https://github.com/VerityPay-Inc/veritypay-tooling) validates the specification corpus; it does not execute conformance scenarios.

## Scenario index

| ID | Fixture | Rule | RFC | Status |
|----|---------|------|-----|--------|
| **VP-CS-0001** | [`scenarios/VP-CS-0001.toml`](scenarios/VP-CS-0001.toml) | VP-RULE-0001 | VP-RFC-0001 (draft) | draft |

New scenarios are added through RFC or governed amendment—never only in a private test repository.

# VerityPay Ecosystem

**Audience:** New contributors, grant reviewers, implementers, auditors.

**Purpose:** Describe the VerityPay platform across repositories after the Phase II platform foundation. This document orients readers to *where* work belongs. It does not define protocol semantics—that remains in accepted specification documents and RFCs in this repository.

**Core message:** The specification defines meaning. Tooling validates it. The reference interpreter executes it. Conformance compares implementations against it.

For specification maturity detail, see [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md). For Phase II scope, see [PHASE_II_PLATFORM_PLAN.md](docs/05-governance/PHASE_II_PLATFORM_PLAN.md).

---

## Ecosystem diagram

The platform is a pipeline of single-responsibility repositories. Shared specification representation (`vp-spec-model`) lives in `veritypay-tooling` and is consumed by downstream executors.

```text
veritypay-spec
    │  normative protocol · RFCs · VP-CS meaning
    ▼
veritypay-tooling
    │  corpus validation · vp validate
    ▼
vp-spec-model
    │  typed registries · document corpus · reference graph
    ▼
veritypay-reference
    │  reference interpreter · oracle outcomes
    ▼
veritypay-conformance
    │  VP-CS harness · implementation comparison
    ▼
Independent implementations · CI · products

Optional (future, not required for platform readiness):

    veritypay-examples ── educational integrations
    veritypay-sdk-*    ── language bindings (must not redefine semantics)
    product repos      ── wallets · payroll · merchant stacks
```

---

## Repository responsibilities

| Repository | Role | Owns | Does not own | Status |
|------------|------|------|--------------|--------|
| [**veritypay-spec**](https://github.com/VerityPay-Inc/veritypay-spec) | Specification foundation | Protocol meaning, RFC process, normative architecture and development docs, VP-CS scenario *authorship* | Implementation code, validation engines, oracle execution, conformance harness code | Specification foundation complete; protocol evolution ongoing |
| [**veritypay-tooling**](https://github.com/VerityPay-Inc/veritypay-tooling) | Validation platform | Registry and cross-reference validation, Edition Manifest checks, `vp validate`, diagnostic policy | Protocol semantics, verification rules, conformance verdicts | **Validation Platform Ready** |
| **`vp-spec-model`** (in [`veritypay-tooling`](https://github.com/VerityPay-Inc/veritypay-tooling/tree/main/crates/vp-spec-model)) | Shared specification representation | Typed load of registries, corpus, and reference graph for validators and downstream consumers | Normative text, rule evaluation, scenario execution | Stable v1 surface per tooling ADR-0007 |
| [**veritypay-reference**](https://github.com/VerityPay-Inc/veritypay-reference) | Reference interpreter | Executable reference semantics, `Interpreter::evaluate`, verification outcomes and trace for education and oracle use | Normative requirements, implementation adapters, pass/fail certification | **Reference Interpreter Ready** |
| [**veritypay-conformance**](https://github.com/VerityPay-Inc/veritypay-conformance) | Conformance suite | VP-CS loading and execution harness, adapter boundary, comparison to reference oracle, conformance reports | Protocol meaning, verification rule invention, legal certification | **Conformance Platform Ready** |
| **Future SDKs / examples** (e.g. `veritypay-examples`, `veritypay-sdk-*`) | Integrator ergonomics | Client libraries, samples, developer onboarding | Protocol behavior, outcome vocabulary, scenario semantics | Not started — deferred until Phase III semantics stabilize |

Each row has **one primary job**. Overlap is resolved in favor of the specification: when harness behavior and normative text disagree, the specification wins.

---

## Reading order

### Protocol contributors (this repository)

1. [MANIFESTO.md](docs/00-overview/MANIFESTO.md)
2. [VISION.md](docs/00-overview/VISION.md)
3. [PRINCIPLES.md](docs/00-overview/PRINCIPLES.md)
4. [GLOSSARY.md](docs/00-overview/GLOSSARY.md)
5. [Architecture](docs/01-architecture/) — structural models and cross-cutting documents
6. [RFCs](rfcs/) — accepted normative decisions

Then: [CONTRIBUTING.md](CONTRIBUTING.md), [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md), and the relevant architecture or development document for your change.

### Tooling contributors

1. [veritypay-tooling README](https://github.com/VerityPay-Inc/veritypay-tooling/blob/main/README.md)
2. [Tooling ADRs](https://github.com/VerityPay-Inc/veritypay-tooling/tree/main/docs/adrs)
3. [SPECIFICATION_MODEL.md](https://github.com/VerityPay-Inc/veritypay-tooling/blob/main/docs/SPECIFICATION_MODEL.md)

### Implementation contributors (reference interpreter and products)

1. [veritypay-reference README](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/README.md)
2. [ADR-0007 — Reference interpreter public contract](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/docs/adrs/0007-reference-interpreter-public-contract.md)
3. [veritypay-reference ROADMAP](https://github.com/VerityPay-Inc/veritypay-reference/blob/main/ROADMAP.md)

Independent product codebases should target accepted RFCs here and compare against the reference oracle via the conformance suite—not fork normative definitions locally.

### Conformance contributors

1. [veritypay-conformance README](https://github.com/VerityPay-Inc/veritypay-conformance/blob/main/README.md)
2. [ADR-0004 — Conformance public contract](https://github.com/VerityPay-Inc/veritypay-conformance/blob/main/docs/adrs/0004-conformance-public-contract.md)
3. [veritypay-conformance ROADMAP](https://github.com/VerityPay-Inc/veritypay-conformance/blob/main/ROADMAP.md)

---

## Platform flow

### Protocol change flow

```text
RFC proposed and accepted in veritypay-spec
    ↓
Registries and normative documents updated
    ↓
veritypay-tooling validates corpus coherence
    ↓
veritypay-reference implements reference semantics
    ↓
veritypay-conformance adds or updates VP-CS scenarios and expectations
    ↓
Independent implementations adapt via adapters; CI runs conformance
```

Normative changes **begin** in this repository. They do not begin in tooling, reference, conformance, or product code.

### Execution flow (conformance check)

```text
VP-CS scenario fixture (authored here, executed elsewhere)
    ↓
ScenarioLoader → ScenarioContext
    ↓
ReferenceOracle + ImplementationAdapter (parallel paths)
    ↓
ComparisonEngine → ConformanceResult → Report
```

---

## Ownership rules

| Concern | Owner |
|---------|--------|
| Protocol meaning | `veritypay-spec` |
| Corpus validation | `veritypay-tooling` |
| Specification representation (typed load) | `vp-spec-model` |
| Reference semantics (oracle) | `veritypay-reference` |
| Implementation comparison | `veritypay-conformance` |
| Products, SDKs, hosted services | Separate repositories — **must not redefine protocol behavior** |

Violations to avoid:

- Encoding normative requirements only in reference or conformance code
- Treating tooling diagnostics as protocol truth
- Letting SDK convenience types override specification vocabulary
- Certifying legal or regulatory compliance from conformance pass/fail alone

---

## Current platform status

| Component | Status |
|-----------|--------|
| **veritypay-spec** | Specification foundation complete; protocol evolution ongoing (Phase III) |
| **veritypay-tooling** | Validation Platform Ready |
| **veritypay-reference** | Reference Interpreter Ready |
| **veritypay-conformance** | Conformance Platform Ready |

**Phase summary:**

| Phase | Name | Status |
|-------|------|--------|
| I | Specification Foundation | Complete |
| II | Platform Foundation | Complete |
| III | Protocol Engineering | Current |
| IV | Ecosystem & Adoption | Planned |

---

## What to build next

**Protocol engineering (Phase III):**

- Real claim fixtures — beyond minimal placeholders; aligned with [DATA_MODEL.md](docs/01-architecture/DATA_MODEL.md)
- Real evidence fixtures — typed content and claim linkage
- VP-CS scenarios — normative scenario catalog authored here
- Verification rule RFCs — rules the reference interpreter must implement
- Reference rule implementations — in `veritypay-reference`, traceable to RFCs
- Conformance scenario coverage — expand VP-CS execution as semantics land

Work should flow **spec → validate → implement → compare**, not the reverse.

---

## What not to build yet

Defer until Phase III semantics and VP-CS coverage are further along:

- Public SDK releases (`veritypay-sdk-*`)
- Production applications and wallets
- Blockchain-specific adapters
- Certification badges or vendor programs
- Hosted conformance-as-a-service

Exploratory spikes belong in `docs/04-research/` or product sandboxes until promoted through RFCs.

---

## Sibling repositories

| Repository | URL |
|------------|-----|
| **veritypay-spec** | https://github.com/VerityPay-Inc/veritypay-spec |
| **veritypay-tooling** | https://github.com/VerityPay-Inc/veritypay-tooling |
| **veritypay-reference** | https://github.com/VerityPay-Inc/veritypay-reference |
| **veritypay-conformance** | https://github.com/VerityPay-Inc/veritypay-conformance |
| **Verity organization profile** | https://github.com/VerityPay-Inc |

---

## Related documents

| Document | Description |
|----------|-------------|
| [SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md) | Maturity and milestone health |
| [PHASE_II_PLATFORM_PLAN.md](docs/05-governance/PHASE_II_PLATFORM_PLAN.md) | Phase II platform scope |
| [CONFORMANCE_MODEL.md](docs/03-development/CONFORMANCE_MODEL.md) | Conformance philosophy (normative guidance) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contributor onboarding |

---

*Specify meaning here. Validate, execute, and compare in sibling repositories.*

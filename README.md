# VerityPay Specification

**The canonical specification for the VerityPay protocol and ecosystem.**

This repository defines *what* VerityPay is and *how* it must behave. It does not contain implementation code. Implementations live in separate repositories and must conform to the specifications accepted here.

---

## What is VerityPay?

VerityPay is an open, protocol-first payment system designed to make payment claims verifiable, interoperable, and trustworthy across independent implementations.

The name reflects a core commitment: payments should be grounded in verifiable truth—not opaque assertions, proprietary silos, or inconsistent behavior across vendors. VerityPay specifies the rules, invariants, and interfaces that any conforming implementation must uphold so that participants can transact with confidence regardless of which software they run.

VerityPay is intended for builders who need a shared, auditable foundation for payment workflows: issuers, acquirers, wallets, merchants, integrators, auditors, and researchers.

---

## Why this repository exists

Payment systems historically evolve as closed products. Behavior is implied by code, documentation drifts from reality, and interoperability is negotiated ad hoc. VerityPay inverts that model.

**This repository is the source of truth.** Before anything is built, it is specified here. Before anything changes, the change is proposed, reviewed, and accepted here.

Comparable projects that follow a similar philosophy:

| Project | Specification home |
|---------|-------------------|
| Ethereum | [ethereum/specs](https://github.com/ethereum/specs) |
| Rust | [rust-lang/rfcs](https://github.com/rust-lang/rfcs) |
| Kubernetes | [kubernetes/enhancements (KEPs)](https://github.com/kubernetes/enhancements) |
| OpenAPI | [OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) |

VerityPay adopts the same discipline: **protocol first, implementation second.**

---

## Philosophy of protocol-first development

Protocol-first development means the specification leads and implementations follow. Concretely:

1. **Specify before you implement.** New behavior enters the ecosystem through documented proposals—not through code that others must reverse-engineer.

2. **Separate concerns.** This repository holds normative definitions (requirements, invariants, data shapes, security properties). Implementation repositories hold code, tests, and deployment artifacts.

3. **Enable plural implementations.** Multiple independent codebases should be able to interoperate because they share one accepted specification—not because they share one vendor's SDK.

4. **Make change explicit.** Protocol evolution is visible, reviewable, and versioned. Breaking changes require deliberate governance, not silent releases.

5. **Prefer clarity over cleverness.** Specifications must be readable by humans first. Precision matters; obscurity does not.

If a behavior is not specified (or not yet accepted), it is **not part of the protocol.**

---

## Repository layout

```
veritypay-spec/
├── README.md                 ← You are here
├── docs/                     ← Curated, stable documentation
│   ├── 00-overview/          ← Vision, principles, whitepaper
│   ├── 01-architecture/      ← System structure and cross-cutting models
│   ├── 02-product/           ← User-facing concepts and workflows
│   ├── 03-development/       ← Contributor and implementer guidance
│   ├── 04-research/          ← Exploratory and pre-normative work
│   └── 05-governance/        ← Decision-making and change control
├── rfcs/                     ← Formal change proposals (Request for Comments)
├── diagrams/                 ← Architecture and protocol visuals
└── templates/                ← Reusable document scaffolds
```

Each directory includes a `README.md` describing its purpose, boundaries, and intended audience.

---

## How to navigate this repository

**Start here if you are…**

| Role | Start with |
|------|------------|
| New to VerityPay | [`docs/00-overview/`](docs/00-overview/) |
| Designing or reviewing system structure | [`docs/01-architecture/`](docs/01-architecture/) |
| Understanding user-facing behavior | [`docs/02-product/`](docs/02-product/) |
| Building or integrating an implementation | [`docs/03-development/`](docs/03-development/) + accepted RFCs |
| Exploring ideas not yet standardized | [`docs/04-research/`](docs/04-research/) |
| Participating in governance | [`docs/05-governance/`](docs/05-governance/) + [`rfcs/`](rfcs/) |
| Proposing a protocol change | [`rfcs/README.md`](rfcs/README.md) and [`templates/`](templates/) |

**Reading order for a deep understanding:**

1. Overview — establish shared vocabulary and intent
2. Architecture — understand structural boundaries and models
3. Product — see how concepts map to real-world use
4. Accepted RFCs — read the normative decisions that bind implementations
5. Development — learn conformance expectations and contribution paths

Documents in `docs/04-research/` are informative until promoted through the RFC process.

---

## Relationship to implementation repositories

This repository defines the **protocol**. Implementation repositories define **software**.

| Responsibility | `veritypay-spec` | Implementation repos (e.g. `veritypay-core`) |
|----------------|------------------|-----------------------------------------------|
| Normative behavior | Yes | Must conform |
| Source code | No | Yes |
| Reference tests / vectors | May define expected outcomes | Must pass |
| Deployment configs | No | Yes |
| Exploratory spikes | In `docs/04-research/` only | Allowed locally; not normative |

**When specification and implementation disagree, the accepted specification wins.** Implementations that diverge from accepted RFCs are non-conformant until the spec is updated through governance or the implementation is corrected.

Implementation repositories should link back to the specific RFCs and document versions they target. This repository should link forward to known implementations where helpful, without duplicating their contents.

---

## Contributing

All substantive protocol changes flow through the RFC process described in [`rfcs/README.md`](rfcs/README.md) and governed by [`docs/05-governance/`](docs/05-governance/).

Before opening a proposal:

- Search existing RFCs and documentation for prior art
- Read the relevant folder README to place your contribution correctly
- Use templates from [`templates/`](templates/) where applicable

Questions, typos, and clarifications to existing accepted text are welcome via issues and pull requests. New protocol behavior requires an RFC.

---

## License

See [LICENSE](LICENSE).

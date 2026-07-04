# VerityPay Specification

**The canonical specification for the VerityPay protocol and ecosystem.**

**Vision:** see **[WHY_VERITY.md](WHY_VERITY.md)** for why Verity exists — the problem, the principles, and the long-term vision.

**Platform overview:** see **[PLATFORM_OVERVIEW.md](PLATFORM_OVERVIEW.md)** for a snapshot of the current Verity ecosystem — what has been built, what is in progress, and what remains planned.

**Platform map:** see **[ECOSYSTEM.md](ECOSYSTEM.md)** for repository roles, reading order, and platform flow across sibling repositories.

**Platform releases:** see **[PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)** for official compatibility across specification and engineering repositories.

**Current status:** see **[SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md)** for maturity, milestones, and ecosystem health (updated periodically).

This repository defines *what* VerityPay is and *how* it must behave. It does not contain implementation code. Implementations live in separate repositories and must conform to the specifications accepted here.

---

## Start Here

**Recommended reading order:**

1. **[WHY_VERITY.md](WHY_VERITY.md)** — motivation behind the platform
2. **[PLATFORM_OVERVIEW.md](PLATFORM_OVERVIEW.md)** — ecosystem snapshot for contributors, reviewers, and implementers
3. **[VERITY_CORE.md](VERITY_CORE.md)** — primary protocol specification (consolidated, implementation-oriented)
4. **[ECOSYSTEM.md](ECOSYSTEM.md)** — platform map across sibling repositories
5. **[SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md)** — maturity, milestones, and ecosystem health
6. **[PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)** — compatible engineering baselines
7. **[RFCs](rfcs/)** — normative change proposals (as needed for rationale and history)

**[WHY_VERITY.md](WHY_VERITY.md)** introduces the motivation before you dive into protocol details. **[VERITY_CORE.md](VERITY_CORE.md)** is the primary entry point for understanding the protocol as one coherent specification. **[RFCs](rfcs/)** remain the normative change mechanism and document how the protocol evolved — read them when you need proposal rationale, acceptance history, or governance context.

---

## Platform Releases

Verity is versioned as an **engineering platform**, not as isolated repository tags. A **Platform Release** names a compatible set of `veritypay-spec`, `veritypay-tooling`, `veritypay-reference`, and `veritypay-conformance` baselines against a Specification Edition.

See **[PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)** for the official compatibility table, supported RFCs, rules, VP-CS scenarios, and versioning philosophy. See **[RELEASE_NOTES_PLATFORM_1_0.md](RELEASE_NOTES_PLATFORM_1_0.md)** and **[RELEASE_NOTES_PLATFORM_1_1.md](RELEASE_NOTES_PLATFORM_1_1.md)** for platform release summaries. Policy is recorded in [ADR-0008 — Platform Release Policy](docs/adrs/0008-platform-release-policy.md).

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
├── README.md                      ← You are here
├── WHY_VERITY.md                  ← Why Verity exists (vision and motivation)
├── PLATFORM_OVERVIEW.md           ← Ecosystem snapshot and current platform state
├── VERITY_CORE.md                 ← Verity Core Protocol (Core Specification Draft)
├── ECOSYSTEM.md                   ← Platform map across sibling repositories
├── PLATFORM_RELEASES.md           ← Official platform compatibility index
├── RELEASE_NOTES_PLATFORM_1_0.md ← Platform 1.0 release summary
├── RELEASE_NOTES_PLATFORM_1_1.md ← Platform 1.1 release summary
├── SPECIFICATION_STATUS.md        ← Living maturity dashboard
├── docs/                          ← Curated specification corpus
│   ├── README.md                  ← Documentation pyramid (start here)
│   ├── 00-overview/               ← Constitutional layer (Manifesto, Vision, Principles, Glossary)
│   ├── 01-architecture/           ← System structure and cross-cutting models
│   ├── 02-product/                ← Participant-facing concepts and workflows
│   ├── 03-development/            ← Implementer and conformance guidance
│   ├── 04-research/               ← Exploratory and pre-normative work
│   ├── 05-governance/             ← Decision-making and change control
│   └── templates/                 ← Spec templates and header snippets
│       └── snippets/              ← SPEC_HEADER, CONSTITUTIONAL_NAV
├── rfcs/                          ← Formal change proposals (Request for Comments)
│   └── templates/                 ← RFC proposal template
├── diagrams/                      ← Architecture and protocol visuals
└── templates/                     ← Index pointing to template locations
```

Each documentation directory includes a `README.md` with **Documentation hierarchy**, **Purpose**, **Audience**, **Scope**, and **Related specifications`.

See [`docs/README.md`](docs/README.md) for the full **Documentation Pyramid**.

---

## How to navigate this repository

**Start here if you are…**

| Role | Start with |
|------|------------|
| **Protocol implementers** | **[WHY_VERITY.md](WHY_VERITY.md)** → **[VERITY_CORE.md](VERITY_CORE.md)** → **[ECOSYSTEM.md](ECOSYSTEM.md)** |
| **Anyone mapping the full platform** | **[ECOSYSTEM.md](ECOSYSTEM.md)** |
| **Anyone pinning compatible repository baselines** | **[PLATFORM_RELEASES.md](PLATFORM_RELEASES.md)** · **[RELEASE_NOTES_PLATFORM_1_0.md](RELEASE_NOTES_PLATFORM_1_0.md)** · **[RELEASE_NOTES_PLATFORM_1_1.md](RELEASE_NOTES_PLATFORM_1_1.md)** |
| **Anyone needing current maturity** | **[SPECIFICATION_STATUS.md](SPECIFICATION_STATUS.md)** |
| New to VerityPay | [`docs/README.md`](docs/README.md) then [`docs/00-overview/`](docs/00-overview/) |
| Designing or reviewing system structure | [`docs/01-architecture/`](docs/01-architecture/) |
| Understanding user-facing behavior | [`docs/02-product/`](docs/02-product/) |
| Building or integrating an implementation | [`docs/03-development/`](docs/03-development/) + accepted RFCs |
| Exploring ideas not yet standardized | [`docs/04-research/`](docs/04-research/) |
| Participating in governance | [`docs/05-governance/`](docs/05-governance/) + [`rfcs/`](rfcs/) |
| Proposing a protocol change | [`rfcs/README.md`](rfcs/README.md) and [`rfcs/templates/RFC_TEMPLATE.md`](rfcs/templates/RFC_TEMPLATE.md) |

**Reading order for a deep understanding:**

1. [Documentation pyramid](docs/README.md#documentation-pyramid) — understand the hierarchy
2. Constitutional layer — [Manifesto](docs/00-overview/MANIFESTO.md) → [Vision](docs/00-overview/VISION.md) → [Principles](docs/00-overview/PRINCIPLES.md) → [Glossary](docs/00-overview/GLOSSARY.md)
3. Architecture — structural boundaries and models
4. Product — how concepts map to real-world use
5. Accepted RFCs — normative decisions that bind implementations
6. Development — conformance expectations and contribution paths

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

Read **[CONTRIBUTING.md](CONTRIBUTING.md)** — the onboarding handbook for the VerityPay protocol ecosystem: reading order, repository guide, contributor levels, workflow, and pull request requirements.

Normative protocol changes flow through the RFC process in [`rfcs/README.md`](rfcs/README.md), governed by [`docs/05-governance/`](docs/05-governance/).

---

## License

See [LICENSE](LICENSE).

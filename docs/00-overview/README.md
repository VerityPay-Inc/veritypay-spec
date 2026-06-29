# Overview

Foundational documents that establish *why* VerityPay exists, *what* problem it addresses, and *which principles* guide every subsequent specification decision.

---

## Documentation hierarchy

**You are here: Constitutional layer** — the highest level of the [documentation pyramid](../README.md#documentation-pyramid).

```
Manifesto → Vision → Principles → Glossary   ← this folder
         ↓
    Architecture → Specifications → Implementation
```

| Position | Document | File | Status |
|----------|----------|------|--------|
| 1 | Manifesto | [MANIFESTO.md](MANIFESTO.md) | Placeholder |
| 2 | Vision | [VISION.md](VISION.md) | Placeholder |
| 3 | Principles | [PRINCIPLES.md](PRINCIPLES.md) | Placeholder |
| 4 | Glossary | [GLOSSARY.md](GLOSSARY.md) | Placeholder |

These four documents cross-link to each other and constrain all lower levels. Nothing in architecture, RFCs, or implementations may contradict an adopted constitutional document.

**Next level:** [`../01-architecture/`](../01-architecture/) — structural models and invariants.

See [`../README.md`](../README.md) for the full pyramid and authoring conventions.

---

## Purpose

This folder is the entry point for anyone encountering VerityPay for the first time. It answers questions of intent and direction before diving into structural or technical detail.

Documents here set the narrative frame: the problem space, the vision for a verifiable payment protocol, and the non-negotiable values that constrain design elsewhere in the repository.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Executives and stakeholders | Understand strategic intent and differentiation |
| New contributors | Build a mental model before proposing changes |
| Researchers and academics | Context for formal analysis and comparison |
| Implementers | Align engineering priorities with protocol values |
| Partners and integrators | Evaluate fit before technical deep-dives |

Read the constitutional documents in order, then proceed to [`../01-architecture/`](../01-architecture/) or [`../../rfcs/`](../../rfcs/) as needed.

---

## Scope

**In scope**

- [MANIFESTO.md](MANIFESTO.md) — mission and public-good philosophy (forthcoming)
- [VISION.md](VISION.md) — desired future state and success criteria (forthcoming)
- [PRINCIPLES.md](PRINCIPLES.md) — durable values and decision heuristics (forthcoming)
- [GLOSSARY.md](GLOSSARY.md) — shared terminology (forthcoming)
- Whitepaper — long-form description of goals, approach, and design rationale
- FAQ — common conceptual questions (not implementation troubleshooting)
- Roadmap — high-level, non-binding direction for specification maturity

**Out of scope**

- Detailed architecture or component specifications → [`../01-architecture/`](../01-architecture/)
- User journeys, personas, or feature descriptions → [`../02-product/`](../02-product/)
- Build instructions or conformance guidance → [`../03-development/`](../03-development/)
- Unreviewed experiments → [`../04-research/`](../04-research/)
- Governance process and RFC rules → [`../05-governance/`](../05-governance/) and [`../../rfcs/`](../../rfcs/)
- Source code, configuration files, or executable artifacts
- Normative protocol requirements not accepted through RFC review

Overview documents are **informative** unless explicitly cross-referenced as normative by an accepted RFC.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../README.md`](../README.md) | Documentation pyramid and level definitions |
| [`../01-architecture/`](../01-architecture/) | Structural detail grounded in principles defined here |
| [`../02-product/`](../02-product/) | How protocol intent maps to participant-facing outcomes |
| [`../05-governance/`](../05-governance/) | How constitutional documents are adopted and amended |
| [`../../rfcs/`](../../rfcs/) | Normative decisions that must align with principles |
| [`../templates/snippets/SPEC_HEADER.md`](../templates/snippets/SPEC_HEADER.md) | Required metadata block citing constitutional refs |
| [`../templates/snippets/CONSTITUTIONAL_NAV.md`](../templates/snippets/CONSTITUTIONAL_NAV.md) | Reusable navigation block for constitutional documents |

# Overview

Foundational documents that establish *why* VerityPay exists, *what* problem it addresses, and *which principles* guide every subsequent specification decision.

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

Read this folder first. Then proceed to [`../01-architecture/`](../01-architecture/) for structural detail, or to [`../../rfcs/`](../../rfcs/) for binding protocol decisions.

---

## Scope

**In scope**

- Whitepaper — long-form description of goals, approach, and design rationale
- [MANIFESTO.md](MANIFESTO.md) — mission and public-good philosophy (forthcoming)
- Vision — desired future state and success criteria
- Principles — durable values and decision heuristics
- Glossary — shared terminology used across all specification documents
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
| [`../01-architecture/`](../01-architecture/) | Structural detail grounded in principles defined here |
| [`../02-product/`](../02-product/) | How protocol intent maps to participant-facing outcomes |
| [`../05-governance/`](../05-governance/) | How values here constrain decision-making |
| [`../../rfcs/`](../../rfcs/) | Normative decisions that may cite overview documents |
| [`../templates/SPEC_TEMPLATE.md`](../templates/SPEC_TEMPLATE.md) | Format for future stable specification documents |

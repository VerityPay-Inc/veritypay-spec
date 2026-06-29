# Overview

Foundational documents that establish *why* VerityPay exists, *what* problem it addresses, and *which principles* guide every subsequent specification decision.

---

## Purpose

This folder is the entry point for anyone encountering VerityPay for the first time. It answers questions of intent and direction before diving into structural or technical detail.

Documents here set the narrative frame: the problem space, the vision for a verifiable payment protocol, and the non-negotiable values that constrain design elsewhere in the repository.

---

## What belongs here

- **Whitepaper** — the authoritative long-form description of VerityPay's goals, approach, and design rationale
- **Vision** — concise statement of the desired future state and success criteria
- **Principles** — durable values and decision heuristics (e.g. verifiability, openness, privacy-by-design, security-first)
- **Glossary** — shared terminology used consistently across all specification documents
- **FAQ** — answers to common conceptual questions (not implementation troubleshooting)
- **Roadmap** — high-level, non-binding direction for specification maturity (distinct from product release plans in implementation repos)

---

## What does not belong here

- Detailed architecture diagrams or component specifications → [`../01-architecture/`](../01-architecture/)
- User journeys, personas, or feature descriptions → [`../02-product/`](../02-product/)
- Build instructions, SDK guides, or CI configuration → [`../03-development/`](../03-development/)
- Unreviewed experiments or literature surveys → [`../04-research/`](../04-research/)
- RFC process rules or steering committee charters → [`../05-governance/`](../05-governance/)
- Source code, configuration files, or executable scripts of any kind
- Normative protocol requirements that have not passed RFC review

Overview documents are **informative** unless explicitly cross-referenced as normative by an accepted RFC.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Executives and stakeholders | Understand strategic intent and differentiation |
| New contributors | Build mental model before proposing changes |
| Researchers and academics | Context for formal analysis and comparison |
| Implementers | Align engineering priorities with protocol values |
| Partners and integrators | Evaluate fit before technical deep-dives |

Read this folder first. Then proceed to [`../01-architecture/`](../01-architecture/) for structural detail, or to [`../../rfcs/`](../../rfcs/) for binding protocol decisions.

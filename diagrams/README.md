# Diagrams

Visual artifacts that clarify VerityPay architecture, protocol flows, and governance relationships.

---

## Purpose

Well-designed diagrams reduce ambiguity in specification text. They show boundaries, sequences, and state transitions that prose alone makes easy to misread.

This directory centralizes **source files** for diagrams referenced across the specification. Keeping visuals here prevents duplication and drift between documents.

---

## What belongs here

- **Architecture diagrams** — subsystems, trust boundaries, deployment-agnostic topology
- **Sequence diagrams** — message and responsibility flow between protocol roles
- **State machines** — entity lifecycles and valid transitions
- **Data relationship diagrams** — conceptual ER views aligned with the data model docs
- **Governance flowcharts** — RFC lifecycle, review stages, escalation paths
- **Source formats** — Mermaid (`.mmd`), PlantUML (`.puml`), Excalidraw (`.excalidraw`), or SVG exported from editable sources

Prefer **editable source formats** over bitmap-only images so diagrams can evolve with the spec.

---

## What does not belong here

- Screenshots of implementation UIs or proprietary dashboards
- Auto-generated diagrams from code (those belong with implementations)
- Marketing graphics without specification value
- Diagrams that embed normative requirements not also stated in RFC or architecture text

Diagrams are **illustrative unless explicitly cited as normative** by an accepted RFC. When a diagram and prose conflict, the accepted RFC text prevails until the discrepancy is resolved.

---

## Conventions

- Name files descriptively: `payment-verification-sequence.mmd`, not `diagram-v2-final.png`
- Include a one-line comment at the top of source files listing which doc(s) reference the diagram
- Update diagrams in the same pull request that changes the behavior they depict
- Export static previews (PNG/SVG) only when needed for renderers that cannot execute source formats

---

## Audience

| Reader | Why use this folder |
|--------|---------------------|
| Spec authors | Maintain consistent visuals across documents |
| Reviewers | Verify diagrams match proposed RFC behavior |
| Implementers | Quick orientation before reading detailed text |
| Educators and presenters | Reuse official ecosystem visuals |

Reference diagrams from documentation using relative links, e.g. `../../diagrams/payment-verification-sequence.mmd`.

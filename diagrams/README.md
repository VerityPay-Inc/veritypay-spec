# Diagrams

Visual artifacts that clarify VerityPay architecture, protocol flows, and governance relationships.

---

## Documentation hierarchy

**You are here: Supporting artifact** — diagrams illustrate pyramid levels but are not a level themselves.

```
Manifesto → Vision → Principles → Glossary
         ↓
    Architecture   ← primary diagram consumer
         ↓
    Specifications ← RFCs may require diagram updates at acceptance
         ↓
    Implementation
```

Diagrams must stay consistent with the [constitutional layer](../docs/00-overview/) and must not introduce normative requirements absent from specification text.

See [`../docs/README.md`](../docs/README.md) for the full pyramid.

---

## Purpose

Well-designed diagrams reduce ambiguity in specification text. They show boundaries, sequences, and state transitions that prose alone makes easy to misread.

This directory centralizes **source files** for diagrams referenced across the specification. Keeping visuals here prevents duplication and drift between documents.

---

## Audience

| Reader | Why use this folder |
|--------|---------------------|
| Spec authors | Maintain consistent visuals across documents |
| Reviewers | Verify diagrams match proposed RFC behavior |
| Implementers | Orient quickly before reading detailed text |
| Educators and presenters | Reuse official ecosystem visuals |

---

## Scope

**In scope**

- Architecture diagrams — subsystems, trust boundaries, deployment-agnostic topology
- Sequence diagrams — message and responsibility flow between protocol roles
- State machines — entity lifecycles and valid transitions
- Data relationship diagrams — conceptual views aligned with the data model
- Governance flowcharts — RFC lifecycle, review stages, escalation paths
- Editable source formats — Mermaid (`.mmd`), PlantUML (`.puml`), Excalidraw (`.excalidraw`), SVG from editable sources

Prefer editable source formats over bitmap-only images so diagrams can evolve with the spec.

**Out of scope**

- Screenshots of implementation UIs or proprietary dashboards
- Auto-generated diagrams from code (those belong with implementations)
- Marketing graphics without specification value
- Diagrams that embed normative requirements not also stated in RFC or specification text

Diagrams are **illustrative unless explicitly cited as normative** by an accepted RFC. When a diagram and prose conflict, accepted RFC text prevails.

---

## Conventions

- Name files descriptively: `payment-verification-sequence.mmd`, not `diagram-v2-final.png`
- Include a one-line comment at the top of source files listing which document(s) reference the diagram
- Update diagrams in the same pull request that changes the behavior they depict
- Export static previews (PNG/SVG) only when renderers cannot execute source formats

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../docs/00-overview/`](../docs/00-overview/) | Constitutional layer context for governance diagrams |
| [`../docs/README.md`](../docs/README.md) | Documentation pyramid |
| [`../docs/01-architecture/`](../docs/01-architecture/) | Primary consumer of architecture and model diagrams |
| [`../docs/05-governance/`](../docs/05-governance/) | Consumer of governance and RFC lifecycle diagrams |
| [`../rfcs/`](../rfcs/) | RFCs may require new or updated diagrams at acceptance |
| [`../docs/templates/SPEC_TEMPLATE.md`](../docs/templates/SPEC_TEMPLATE.md) | Stable specs may reference diagrams from this directory |

Reference diagrams from documentation using relative links, e.g. `../../diagrams/payment-verification-sequence.mmd`.

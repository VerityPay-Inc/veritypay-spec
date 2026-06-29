# Specification Templates

Reusable scaffolds for stable specification documents and decision records within the VerityPay documentation corpus.

---

## Documentation hierarchy

**You are here: Authoring support** — templates and snippets do not sit on the [documentation pyramid](../README.md#documentation-pyramid). They enforce consistent structure across all levels.

Every specification document must begin with [`snippets/SPEC_HEADER.md`](snippets/SPEC_HEADER.md). Constitutional documents use [`snippets/CONSTITUTIONAL_NAV.md`](snippets/CONSTITUTIONAL_NAV.md) for cross-navigation.

```
Manifesto → Vision → Principles → Glossary
         ↓
    Architecture → Specifications → Implementation
         ↑              ↑
         └── SPEC_HEADER required on all new spec documents
```

See [`../README.md`](../README.md) for the full pyramid.

---

## Purpose

Long-lived protocols depend on consistent document structure. Templates in this folder define how normative-adjacent and architectural specification text is authored, reviewed, and maintained—distinct from RFC proposals, which use [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md).

---

## Audience

| Reader | Why use this folder |
|--------|---------------------|
| Spec authors | Produce complete, reviewable specification documents |
| Architecture contributors | Record decisions with a standard format |
| Maintainers and editors | Enforce structural consistency during review |
| RFC authors | Reference stable specs when citing related material |
| Constitutional document authors | Apply shared navigation and header conventions |

---

## Scope

**In scope**

- [`snippets/SPEC_HEADER.md`](snippets/SPEC_HEADER.md) — required metadata block for every specification document
- [`snippets/CONSTITUTIONAL_NAV.md`](snippets/CONSTITUTIONAL_NAV.md) — cross-links for the constitutional layer
- [`SPEC_TEMPLATE.md`](SPEC_TEMPLATE.md) — format for stable specification documents under `docs/`
- [`DECISION_RECORD_TEMPLATE.md`](DECISION_RECORD_TEMPLATE.md) — format for architecture and governance decision records

**Out of scope**

- RFC change proposals → [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md)
- Diagram source files → [`../../diagrams/`](../../diagrams/)
- Completed specification documents (copy templates into target folders)
- Implementation project templates (issue forms, PR templates for code repositories)

Templates are **structural**. They provide headings, front matter fields, and authoring guidance—not protocol content.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../README.md`](../README.md) | Documentation pyramid and level definitions |
| [`../00-overview/`](../00-overview/) | Constitutional layer documents using these snippets |
| [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md) | Template for protocol *changes* |
| [`../01-architecture/`](../01-architecture/) | Primary destination for architecture specs |
| [`../05-governance/`](../05-governance/) | Process for adopting or revising documents |

---

## Usage

1. Copy [`snippets/SPEC_HEADER.md`](snippets/SPEC_HEADER.md) to the top of every new specification document; complete all fields.
2. Copy the relevant body template (`SPEC_TEMPLATE.md` or `DECISION_RECORD_TEMPLATE.md`) into the target folder.
3. Set `pyramid_level` and `constitutional_refs` appropriately (see header snippet comments).
4. Remove template-only instructional comments before review.

New templates that change required document structure should be proposed through governance or RFC.

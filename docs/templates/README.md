# Specification Templates

Reusable scaffolds for stable specification documents and decision records within the VerityPay documentation corpus.

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

---

## Scope

**In scope**

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
| [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md) | Template for protocol *changes*; may supersede or amend docs authored from here |
| [`../01-architecture/`](../01-architecture/) | Primary destination for architecture specs and decision records |
| [`../05-governance/`](../05-governance/) | Process for adopting or revising governance decision records |
| [`../03-development/`](../03-development/) | Style and notation expectations for specification prose |

---

## Usage

1. Copy the relevant template into the target documentation folder.
2. Rename the file following conventions in that folder's README.
3. Complete all front matter fields before opening a pull request.
4. Remove template-only instructional comments when the document is ready for review.

New templates that change required document structure should be proposed through governance or RFC.

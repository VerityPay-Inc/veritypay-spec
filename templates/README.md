# Templates

Reusable document scaffolds that keep VerityPay specification writing consistent, complete, and reviewable.

---

## Purpose

Specifications scale through many authors and years. Templates encode the project's expectations for structure, required sections, and tone—so reviewers spend time on substance rather than formatting debates.

Use templates when creating new material. Deviations are acceptable when justified in the pull request, but the default is conformity.

---

## What belongs here

- **RFC template** — standard sections for protocol change proposals
- **Architecture Decision Record (ADR) template** — lightweight record of structural choices
- **Research note template** — exploratory documents with explicit non-normative status
- **Diagram brief template** — metadata checklist before adding visuals to [`../diagrams/`](../diagrams/)
- **Glossary entry template** — consistent definition format for [`../docs/00-overview/`](../docs/00-overview/)

Templates are **structural**, not content. They include headings, guidance comments, and checklists—not pre-filled protocol decisions.

---

## What does not belong here

- Completed RFCs, ADRs, or research papers (those live in their respective destinations)
- Implementation project templates (issue forms, PR templates for code repos)
- Generated or auto-filled documents from tooling pipelines
- Legal contracts or CLA text (belongs in governance with appropriate review)

---

## Usage

1. Copy the relevant template into the target directory (`rfcs/`, `docs/…`, etc.)
2. Rename following naming conventions in that folder's README
3. Replace instructional comments with your content
4. Remove template-only guidance before marking a document final

---

## Audience

| Reader | Why use this folder |
|--------|---------------------|
| RFC authors | Submit complete, reviewable proposals |
| Architecture contributors | Document decisions uniformly |
| Research contributors | Mark work as pre-normative clearly |
| Maintainers and editors | Enforce consistency during review |

New templates that change required document structure should themselves be proposed through governance or RFC.

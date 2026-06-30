# VerityPay Terminology Registry

Machine-readable vocabulary for tooling, linting, RFC validation, and documentation generation.

| Artifact | Role |
|----------|------|
| [`registry.yaml`](registry.yaml) | Canonical term metadata (**VP-TERM-***) |
| [`../docs/00-overview/GLOSSARY.md`](../docs/00-overview/GLOSSARY.md) | Human-readable definitions (SPEC-0004) |

## Usage

RFCs and conformance artifacts SHOULD cite:

- **VP-TERM-*** — glossary Concept ID (e.g. `VP-TERM-009`)
- **Section ID** — architecture normative definition (e.g. `DM-4.8`)

Example RFC amendment block:

```
Changes
  DM-4.8  — Verification (normative definition)
  VP-TERM-009 — Verification (terminology)
```

## Regeneration

After glossary structural changes, update `scripts/sync_terminology_registry.py` term metadata and run:

```bash
python3 scripts/sync_terminology_registry.py
```

Do not hand-edit `registry.yaml` without updating the sync script—drift breaks tooling.

## Schema (informal)

Each term entry includes:

- `id`, `anchor`, `title`
- `stability` — `proposed` | `experimental` | `stable` | `reserved` | `deprecated`
- `normative_definition` — `document`, `path`, `section_id`
- `referenced_by` — documents that cite without owning definition
- `depends_on` — other **VP-TERM-*** IDs (concept dependency graph)

# VerityPay RFC Registry

Machine-readable index of RFC metadata for tooling, dependency graphs, and publication pipelines.

| Artifact | Role |
|----------|------|
| [`registry.yaml`](registry.yaml) | Canonical RFC metadata (**VP-RFC-***) |
| [`../../rfcs/`](../../rfcs/) | Human-readable RFC documents |
| [`../../rfcs/0000-rfc-process.md`](../../rfcs/0000-rfc-process.md) | Governing process (**VP-RFC-0000**) |

## Usage

Each accepted RFC SHOULD have a corresponding entry with:

- `id` — **VP-RFC-**** Concept ID
- `status`, `type`, `version`
- `depends_on`, `supersedes`, `superseded_by`
- `related_terms`, `related_architecture`, `related_conformance`

Example dependency edge:

```yaml
depends_on:
  - VP-RFC-0000
```

## Regeneration

Today entries are updated when RFCs are accepted. Future automation may generate this file from RFC front matter. Until then, add entries when merging new RFCs and keep fields aligned with [RFC-0000 §7](../../rfcs/0000-rfc-process.md#7-required-metadata).

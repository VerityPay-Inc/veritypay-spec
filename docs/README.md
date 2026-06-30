# VerityPay Documentation

Curated specification corpus for the VerityPay protocol. This repository defines behavior; it does not contain implementation code.

Start with the [Documentation Pyramid](#documentation-pyramid) to understand how documents relate. Then enter through the constitutional layer in [`00-overview/`](00-overview/).

---

## Documentation pyramid

Every document in this repository sits at a defined level. Higher levels constrain lower levels. Lower levels must not contradict higher ones.

```
                    ┌─────────────────┐
                    │    Manifesto    │  Mission and public-good philosophy
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     Vision      │  Desired future state and success criteria
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Principles    │  Durable values and decision heuristics
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Architecture   │  Structure, models, invariants
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Specifications  │  Normative protocol text (RFCs, stable specs)
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Implementation  │  Software in separate repositories
                    └─────────────────┘
```

**Reading order:** top to bottom. **Authoring order:** constitutional documents first, then architecture, then specifications. Implementation follows accepted specifications.

The [Glossary](00-overview/GLOSSARY.md) spans all levels—it defines shared vocabulary but does not override documents above it.

---

## Pyramid levels

| Level | Location | Binding force |
|-------|----------|---------------|
| **Manifesto** | [`00-overview/MANIFESTO.md`](00-overview/MANIFESTO.md) | Informative; adopted through governance |
| **Vision** | [`00-overview/VISION.md`](00-overview/VISION.md) | Informative; constrains strategic direction |
| **Principles** | [`00-overview/PRINCIPLES.md`](00-overview/PRINCIPLES.md) | Informative; constrains design and RFC review |
| **Architecture** | [`01-architecture/`](01-architecture/) | Normative when incorporated by accepted RFC |
| **Specifications** | [`../rfcs/`](../rfcs/), stable docs under `docs/` | Normative when accepted or marked stable |
| **Implementation** | External repositories (e.g. `veritypay-core`) | Must conform to accepted specifications |

---

## Adjacent areas (not pyramid levels)

These folders support the specification without sitting on the pyramid itself:

| Area | Location | Role |
|------|----------|------|
| Product | [`02-product/`](02-product/) | Participant-facing view of specified behavior |
| Development | [`03-development/`](03-development/) | Conformance and implementer guidance |
| Research | [`04-research/`](04-research/) | Pre-normative exploration |
| Governance | [`05-governance/`](05-governance/) | Rules for changing any level |
| Diagrams | [`../diagrams/`](../diagrams/) | Visual companions to architecture and specs |
| Templates | [`templates/`](templates/) | Authoring scaffolds and header snippets |

Research may inform any level but is not binding until promoted through RFC or governance.

---

## Constitutional layer

The four documents below form the **constitutional layer**—the highest level of the hierarchy. They live in [`00-overview/`](00-overview/).

| Document | File | Status |
|----------|------|--------|
| Manifesto | [`00-overview/MANIFESTO.md`](00-overview/MANIFESTO.md) | Draft |
| Vision | [`00-overview/VISION.md`](00-overview/VISION.md) | Draft |
| Principles | [`00-overview/PRINCIPLES.md`](00-overview/PRINCIPLES.md) | Placeholder |
| Glossary | [`00-overview/GLOSSARY.md`](00-overview/GLOSSARY.md) | Placeholder |

All four cross-link to each other. Every future specification must declare its pyramid level and cite relevant constitutional documents using [`templates/snippets/SPEC_HEADER.md`](templates/snippets/SPEC_HEADER.md).

---

## Directory index

| Directory | Pyramid level | README |
|-----------|---------------|--------|
| [`00-overview/`](00-overview/) | Constitutional | [`00-overview/README.md`](00-overview/README.md) |
| [`01-architecture/`](01-architecture/) | Architecture | [`01-architecture/README.md`](01-architecture/README.md) |
| [`02-product/`](02-product/) | Adjacent (product view) | [`02-product/README.md`](02-product/README.md) |
| [`03-development/`](03-development/) | Below specifications | [`03-development/README.md`](03-development/README.md) |
| [`04-research/`](04-research/) | Adjacent (pre-normative) | [`04-research/README.md`](04-research/README.md) |
| [`05-governance/`](05-governance/) | Adjacent (meta) | [`05-governance/README.md`](05-governance/README.md) |
| [`templates/`](templates/) | Authoring support | [`templates/README.md`](templates/README.md) |
| [`../rfcs/`](../rfcs/) | Specifications | [`../rfcs/README.md`](../rfcs/README.md) |

---

## Authoring conventions

- Prepend [`templates/snippets/SPEC_HEADER.md`](templates/snippets/SPEC_HEADER.md) to every new specification document.
- Copy [`templates/SPEC_TEMPLATE.md`](templates/SPEC_TEMPLATE.md) for stable specs under `docs/`.
- Copy [`../rfcs/templates/RFC_TEMPLATE.md`](../rfcs/templates/RFC_TEMPLATE.md) for protocol change proposals.
- Update cross-links when adding documents that the constitutional layer or pyramid references.

# Research

Exploratory, analytical, and pre-normative work that informs future specification decisions but is not yet binding on implementations.

---

## Documentation hierarchy

**You are here: Adjacent (pre-normative)** — research sits outside the pyramid until promoted. It may inform any level but binds none.

```
Manifesto → Vision → Principles → Glossary
         ↓
    Architecture → Specifications → Implementation

    Research ──→ may feed any level via RFC promotion
```

Research must cite relevant constitutional documents when proposing alternatives. Promotion path: research → RFC draft → accepted specification.

**Constitutional context:** [`../00-overview/`](../00-overview/) · **Promotion target:** [`../../rfcs/`](../../rfcs/)

See [`../README.md`](../README.md) for the full pyramid.

---

## Purpose

Not every idea is ready for RFC review. Research documents capture investigations, comparisons, threat analyses, and prototypes-in-prose that help the community decide *whether* and *how* to standardize something.

This folder preserves hypotheses, open questions, and rejected alternatives so future contributors do not repeat settled debates.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Protocol researchers | Contribute analysis and alternatives |
| RFC authors | Ground proposals in prior investigation |
| Security reviewers | Understand evolving threat context |
| Early adopters | Preview possible future direction—**not** current requirements |
| Academics | Find citable context for formal work |

If you need binding rules for production software, read accepted RFCs—not research drafts.

---

## Scope

**In scope**

- Literature and market surveys — how other systems solve related problems
- Threat modeling drafts — preliminary attack trees and mitigation options
- Cryptographic and protocol analysis — notes pending peer review
- Performance and scalability studies — modeling with explicit assumptions
- Rejected proposals — why directions were considered and declined
- Spike summaries — time-boxed investigations described in prose
- Workshop and meeting notes — when they capture unresolved discussion

**Out of scope**

- Accepted normative requirements → promote to [`../../rfcs/`](../../rfcs/) or [`../01-architecture/`](../01-architecture/)
- Stable participant-facing documentation → [`../02-product/`](../02-product/)
- Final governance decisions → [`../05-governance/`](../05-governance/)
- Implementation code, benchmark repositories, or dependency lockfiles
- Documents presented as finished spec without RFC acceptance

**Research documents are informative unless explicitly promoted.** Implementers must not treat content here as conformance requirements.

---

## Lifecycle

```
Research document → RFC draft → Review → Accepted / Rejected
                              ↓
                    Rejected analysis may return here
```

When research matures:

1. Open an RFC in [`../../rfcs/`](../../rfcs/) citing the research document
2. Update the research doc with a status banner (superseded, incorporated, withdrawn)
3. Move durable architectural outcomes to [`../01-architecture/`](../01-architecture/) as appropriate

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../../rfcs/`](../../rfcs/) | Destination for research promoted to normative proposals |
| [`../01-architecture/`](../01-architecture/) | Stable home for accepted structural outcomes |
| [`../05-governance/`](../05-governance/) | Rules governing promotion from research to RFC |
| [`../templates/DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md) | Optional format for recording research conclusions |
| [`../../rfcs/templates/RFC_TEMPLATE.md`](../../rfcs/templates/RFC_TEMPLATE.md) | Template when research becomes an RFC draft |

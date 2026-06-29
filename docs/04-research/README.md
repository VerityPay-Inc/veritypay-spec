# Research

Exploratory, analytical, and pre-normative work that informs future specification decisions but is not yet binding on implementations.

---

## Purpose

Not every idea is ready for RFC review. Research documents capture investigations, comparisons, threat analyses, and prototypes-in-prose that help the community decide *whether* and *how* to standardize something.

This folder provides a safe venue for intellectual honesty: hypotheses, open questions, and rejected alternatives remain visible so future contributors do not repeat settled debates.

---

## What belongs here

- **Literature and market surveys** — how other systems solve related problems
- **Threat modeling drafts** — preliminary attack trees and mitigation options
- **Cryptographic and protocol analysis** — academic or engineering notes pending peer review
- **Performance and scalability studies** — modeling results with explicit assumptions
- **Rejected proposals** — why certain directions were considered and declined
- **Spike summaries** — findings from time-boxed investigations (described in prose, not code dumps)
- **Workshop and meeting notes** — when they capture unresolved discussion, not final decisions

---

## What does not belong here

- Accepted normative requirements → promote to RFC or [`../01-architecture/`](../01-architecture/)
- Stable user-facing documentation → [`../02-product/`](../02-product/)
- Final governance decisions → [`../05-governance/`](../05-governance/)
- Implementation code, benchmarks as repositories, or dependency lockfiles
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

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Protocol researchers | Contribute analysis and alternatives |
| RFC authors | Ground proposals in prior investigation |
| Security reviewers | Understand evolving threat context |
| Implementers (early adopters) | Preview possible future direction—**not** current requirements |
| Academics | Find citable context for formal work |

If you need binding rules for production software, read accepted RFCs—not research drafts.

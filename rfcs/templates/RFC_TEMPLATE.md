---
template: RFC
version: 1.0.0
status: canonical
related:
  - VP-RFC-0000
---

**Template:** RFC Author Guide · **Version:** 1.0.0 · **Status:** canonical

**Governing process:** [RFC-0000: RFC Process](../0000-rfc-process.md) (**VP-RFC-0000**)

**Use this document to:** learn how to write specification-grade RFCs · **Use RFC-0000 to:** understand lifecycle, acceptance, and registry rules

---

# RFC Author Guide

Writing an RFC is different from writing code.

Code persuades machines. An RFC persuades **people who will implement independently**—often years later, without access to today's conversations. An RFC is a proposal to change the **shared understanding** of the VerityPay protocol: what words mean, what behavior is required, and what implementations must do to interoperate.

The goal is **clarity**, not persuasion. Reviewers are not an audience to win; they are partners in stress-testing whether the idea survives public scrutiny.

The goal is **long-term correctness**, not short-term approval. A rushed acceptance that fractures terminology or architecture creates debt across every future integrator. A thoughtful RFC that takes longer to merge but leaves the specification **clearer than before** is a success—even before code ships.

This guide teaches **how to write**. [VP-RFC-0000](../0000-rfc-process.md) defines **how RFCs are governed**. Read both before your first proposal.

---

## Before you begin

Answer these questions honestly before opening a numbered RFC. If several answers point away from an RFC, you may still have valuable work—but it may belong elsewhere.

| Question | If yes → | If no → |
|----------|----------|---------|
| **Does this require a protocol change?** | Continue; confirm scope in Problem Statement | Implementation or documentation PR may suffice |
| **Could this be solved by implementation alone?** | Stop—implement against existing spec | Proceed only if spec gap is real |
| **Is this an ADR instead?** | Write an ADR; RFC only if normative behavior changes | Continue toward RFC |
| **Is the problem already solved?** | Reference existing spec; close or narrow scope | Continue |
| **Have I read [VP-RFC-0000](../0000-rfc-process.md)?** | You know lifecycle, metadata, invariants | Read it first |
| **Have I read the relevant architecture document?** | You know which models and section IDs apply | Read [DOMAIN_MODEL](../../docs/01-architecture/DOMAIN_MODEL.md), [IDENTITY_MODEL](../../docs/01-architecture/IDENTITY_MODEL.md), etc. |
| **Have I searched existing RFCs and the [glossary](../../docs/00-overview/GLOSSARY.md)?** | You avoid duplicate vocabulary | Search before drafting |
| **Can I state the problem in one paragraph without naming my solution?** | Problem Statement is likely honest | Refine problem before proposing |

When in doubt, open a short issue asking *RFC or not?* Default assumption for behavior that affects interoperability: **RFC**.

---

## RFC writing philosophy

These habits separate protocol documents from product notes:

| Habit | Practice |
|-------|----------|
| **Write for someone five years from now** | They have the text, not your memory of the review thread |
| **Assume the reader knows nothing about today's discussion** | Define terms; link to **VP-TERM-***; cite architecture section IDs |
| **Every sentence should reduce ambiguity** | If two implementers could read it differently, rewrite |
| **Every normative statement should be intentional** | Each MUST earns its place; remove decorative requirements |
| **Avoid implementation-specific language** | Name protocol concepts, not classes, tables, or vendor APIs |
| **Prefer examples over abstract explanations** | Alice, Bob, Acme Payroll, Contoso Bank—concrete traces |
| **Explain WHY before WHAT** | Motivation and Problem Statement precede Proposal |

Align with [RFC principles](../0000-rfc-process.md#3-rfc-principles) in VP-RFC-0000: one problem, explicit trade-offs, preserved interoperability, conceptual integrity.

---

## RFC skeleton

Every RFC section below includes four teaching parts, then a **Markdown skeleton** to copy into your proposal file.

Required sections match [VP-RFC-0000 §8](../0000-rfc-process.md#8-required-rfc-structure). Sections with no impact MUST say **None**—not omit the heading.

At the end: [Copy-paste starter](#copy-paste-starter) with front matter per [VP-RFC-0000 §7](../0000-rfc-process.md#7-required-metadata).

---

### Summary

**Question answered:** *What changes, in one breath?*

**Why this section exists:** Maintainers, integrators, and future indexers decide whether to read further from this paragraph alone.

**Reviewer expectations:** One paragraph; no jargon without links; states type of RFC (Protocol, Terminology, etc.); names primary **VP-TERM-*** or **VP-RFC-*** touchpoints if any.

**Author checklist:**

- [ ] Readable without scrolling the Proposal section
- [ ] States outcome, not implementation plan
- [ ] Mentions compatibility character (breaking / additive / clarifying)

```markdown
## Summary

<!-- One paragraph: what changes, who is affected, whether behavior or vocabulary moves. -->
```

---

### Motivation

**Question answered:** *Why does this problem matter now?*

**Why this section exists:** Without pressure, reviewers cannot judge whether the RFC is proportionate or urgent.

**Reviewer expectations:** Real-world failure mode or missed interoperability; link to principles or vision where relevant—not marketing language.

**Author checklist:**

- [ ] Describes pain without presupposing your solution
- [ ] Names who suffers today (integrators, verifiers, auditors)
- [ ] Explains why waiting makes things worse

```markdown
## Motivation

<!-- Why now? Who is affected? What breaks or frays without this change? -->
```

---

### Problem Statement

**Question answered:** *What specification gap exists?*

**Why this section exists:** Separates symptoms from the actual missing rule, invariant, or definition.

**Reviewer expectations:** Falsifiable statement of the gap; distinguish protocol problem from product preference.

**Author checklist:**

- [ ] Could be understood without reading Proposal
- [ ] Does not name your preferred design as the only fix
- [ ] Cites existing spec text that is insufficient, if applicable

```markdown
## Problem Statement

<!-- The gap in shared rules, vocabulary, or architecture—not "we need feature X." -->
```

---

### Goals

**Question answered:** *What does success look like for this RFC?*

**Why this section exists:** Declares intended outcomes so scope creep is visible during review.

**Reviewer expectations:** Small set of testable goals; aligned with [success criteria](../0000-rfc-process.md#13-rfc-success-criteria) where possible.

**Author checklist:**

- [ ] Each goal is verifiable after acceptance
- [ ] Goals do not smuggle in unstated requirements
- [ ] Success signals for the ecosystem are stated (optional but valuable)

```markdown
## Goals

- 
- 
```

---

### Non-Goals

**Question answered:** *What is intentionally out of scope?*

**Why this section exists:** Prevents reviewers from attacking deliberate omissions.

**Reviewer expectations:** Honest boundaries; related work pointed to future RFCs or ADRs.

**Author checklist:**

- [ ] Lists tempting extensions you are deferring
- [ ] Clarifies what this RFC will not fix
- [ ] Reduces "why didn't you also…" debate

```markdown
## Non-Goals

- 
- 
```

---

### Proposal

**Question answered:** *What exactly must change in the specification?*

**Why this section exists:** The normative heart—what independent implementers MUST do.

**Reviewer expectations:** RFC 2119 keywords used deliberately; requirements precise enough for interoperable implementations; protocol language only.

**Author checklist:**

- [ ] Each MUST is necessary and sufficient—not copied from habit
- [ ] Behavior is defined without naming a single codebase
- [ ] Examples illustrate but do not replace normative text
- [ ] Specification version binding stated where evaluation rules change

```markdown
## Proposal

<!-- Normative requirements. Use MUST, SHOULD, MAY, MUST NOT intentionally. -->

### {Subsection if needed}

...
```

---

### Architecture Impact

**Question answered:** *Which models and section IDs does this amend?*

**Why this section exists:** Protocol behavior lives in architecture; reviewers must see structural coherence.

**Reviewer expectations:** Named models ([DOMAIN_MODEL](../../docs/01-architecture/DOMAIN_MODEL.md), [IDENTITY_MODEL](../../docs/01-architecture/IDENTITY_MODEL.md), etc.); **DM-***, **IM-***, **BM-***, **DAT-***, **SM-*** section IDs; explicit **None** if truly absent.

**Author checklist:**

- [ ] Lists every affected architecture document
- [ ] States whether change is extension vs structural amendment
- [ ] Principal Architect concerns anticipated for structural moves

```markdown
## Architecture Impact

| Model | Section ID | Change |
|-------|------------|--------|
| DOMAIN_MODEL | DM- | |
| IDENTITY_MODEL | IM- | |
| BEHAVIOR_MODEL | BM- | |
| DATA_MODEL | DAT- | |
| STATE_MODEL | SM- | |

<!-- Or: None -->
```

---

### Terminology Impact

**Question answered:** *Which words change, and how?*

**Why this section exists:** Vocabulary is protocol infrastructure; silent synonym drift destroys interoperability.

**Reviewer expectations:** **VP-TERM-*** IDs from [GLOSSARY.md](../../docs/00-overview/GLOSSARY.md); new terms propose registry entries; deprecated terms named explicitly.

**Author checklist:**

- [ ] No new synonyms for existing concepts without glossary amendment
- [ ] `related_terms` in front matter matches this section
- [ ] Terminology RFC type considered if vocabulary is the primary change

```markdown
## Terminology Impact

| VP-TERM ID | Term | Change |
|------------|------|--------|
| | | |

<!-- Or: None -->
```

---

### Conformance Impact

**Question answered:** *How will we know implementations still interoperate?*

**Why this section exists:** Interoperability must be testable; conformance is how the ecosystem verifies shared meaning.

**Reviewer expectations:** Reference [CONFORMANCE_MODEL.md](../../docs/03-development/CONFORMANCE_MODEL.md); new or amended **VP-CS-*** scenarios; explicit **None** with justification if behavior unchanged.

**Author checklist:**

- [ ] States impact on conformance pyramid level (semantic, behavioral, state, etc.)
- [ ] Identifies scenarios to add or update
- [ ] `related_conformance` in front matter matches this section

```markdown
## Conformance Impact

| VP-CS ID | Scenario change |
|----------|-----------------|
| | |

<!-- Or: None — explain why interoperability is unaffected -->
```

---

### Security Impact

**Question answered:** *What trust boundaries move?*

**Why this section exists:** Payment-adjacent protocols must surface abuse cases and trust assumptions.

**Reviewer expectations:** Threats introduced or mitigated; no hand-waving "security is unchanged" without argument.

**Author checklist:**

- [ ] New attack surfaces named
- [ ] Reliance on external trust made explicit
- [ ] **None** only when security surface is genuinely unchanged

```markdown
## Security Impact

<!-- Threats, mitigations, trust boundary changes. Or: None with one-sentence justification. -->
```

---

### Backwards Compatibility

**Question answered:** *Do existing conforming implementations remain conforming?*

**Why this section exists:** Integrators need a yes/no/maybe with reasoning before they commit roadmaps.

**Reviewer expectations:** Clear compatibility class: additive, clarifying, or breaking.

**Author checklist:**

- [ ] States impact on deployments targeting current specification version
- [ ] Breaking changes flagged prominently
- [ ] Links to Migration Strategy when not fully compatible

```markdown
## Backwards Compatibility

<!-- Additive | Clarifying | Breaking — with explanation -->
```

---

### Migration Strategy

**Question answered:** *How do adopters move from old rules to new?*

**Why this section exists:** Breaking changes without migration fracture the ecosystem.

**Reviewer expectations:** Concrete steps for implementers and integrators; timelines only if governance mandates—otherwise phases described logically.

**Author checklist:**

- [ ] States **None** only when fully additive
- [ ] Dual-read / dual-write periods described if needed
- [ ] Supersession of prior RFCs listed in front matter

```markdown
## Migration Strategy

<!-- Phased adoption, dual support, deprecation windows. Or: None -->
```

---

### Alternatives Considered

**Question answered:** *What else could we have done, and why not?*

**Why this section exists:** Institutional memory; prevents reopening settled debates without new evidence.

**Reviewer expectations:** At least one serious alternative with trade-offs—not strawmen.

**Author checklist:**

- [ ] Each alternative has a reason for rejection
- [ ] "Do nothing" considered if realistic
- [ ] Links to prior RFCs or issues where relevant

```markdown
## Alternatives Considered

### Alternative A

**Description:**

**Why not chosen:**

### Alternative B

...
```

---

### Open Questions

**Question answered:** *What is still unknown?*

**Why this section exists:** Honest unknowns belong in the document, not in private threads.

**Reviewer expectations:** Questions have owners or resolution paths; empty when resolved before acceptance.

**Author checklist:**

- [ ] No silent blockers hidden here
- [ ] Each question states what decision it blocks
- [ ] Removed or emptied before **Review** if resolved

```markdown
## Open Questions

1. 
2. 
```

---

### Acceptance Criteria

**Question answered:** *What must be true before maintainers should accept?*

**Why this section exists:** Authors state the bar; reviewers hold authors to it—see [VP-RFC-0000 §10](../0000-rfc-process.md#10-acceptance-criteria).

**Reviewer expectations:** Checklist mapped to invariants, principles, and section impacts above.

**Author checklist:**

- [ ] Terminology, architecture, conformance, migration addressed
- [ ] [RFC invariants](../0000-rfc-process.md#11-rfc-invariants) explicitly satisfied
- [ ] Distinct from [success criteria](../0000-rfc-process.md#13-rfc-success-criteria) (post-acceptance ecosystem outcomes)

```markdown
## Acceptance Criteria

- [ ] 
- [ ] 
- [ ] 
```

---

### References

**Question answered:** *What existing specification text grounds this proposal?*

**Why this section exists:** Readers must trace lineage to architecture, RFCs, standards, and research.

**Reviewer expectations:** **VP-RFC-***, **VP-TERM-***, section IDs, external standards with version pins.

**Author checklist:**

- [ ] Every normative claim in Proposal traceable to a reference or new text in Proposal
- [ ] `depends_on` in front matter reflected here
- [ ] Links use stable paths in `veritypay-spec`

```markdown
## References

- [VP-RFC-0000](../0000-rfc-process.md) — RFC Process
- [GLOSSARY.md](../../docs/00-overview/GLOSSARY.md)
- 
```

---

## Writing good normative language

Normative requirements use keywords from [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119). This guide does not reproduce the full RFC; it teaches **responsible use** in VerityPay proposals.

| Keyword | Use when |
|---------|----------|
| **MUST** | Absolute requirement for conformance |
| **MUST NOT** | Absolute prohibition |
| **SHOULD** | Strong recommendation; deviation needs documented reason |
| **SHOULD NOT** | Strong discouragement |
| **MAY** | Truly optional behavior |

| Good | Bad |
|------|-----|
| "A conforming verifier **MUST** record the **verification outcome** on a **verification record**." | "Implementations should probably store the result somewhere." |
| "Claim content **MUST NOT** mutate after assertion." | "We won't update claims in place." |
| "Integrators **MAY** expose a retry UI; the protocol **MUST NOT** require retries for conformance." | "Retry is optional lol." |

**Rules of thumb:**

- One requirement per sentence when possible.
- MUST not used for taste or convenience—only for interoperability or safety.
- SHOULD not used when you actually mean MUST but want to sound gentle.
- Define terms before requiring them; link **VP-TERM-***.
- Examples are informative unless explicitly marked normative.

---

## Common RFC mistakes

| Mistake | Why it happens | Why it hurts | How to fix |
|---------|----------------|--------------|------------|
| **Solution before problem** | Author is excited about design | Reviewers cannot evaluate fit; scope hides in implementation | Write Problem Statement before Proposal |
| **Implementation leaking into specification** | Author thinks in code | Other stacks cannot conform; spec becomes a single codebase | Name protocol artifacts; move code notes to implementation repo |
| **Undefined terminology** | Familiar words feel obvious | Integrators build incompatible mental models | Link **VP-TERM-***; propose glossary entries |
| **Changing architecture accidentally** | Small field addition redefines identity | Silent breaking change across models | Fill Architecture Impact; get structural review |
| **No migration strategy** | "Everyone will upgrade" | Production systems stall; ecosystem splits | Document phases or state **None** with proof of additivity |
| **No conformance impact** | "Tests come later" | Interoperability unverifiable | Name VP-CS scenarios or justify **None** |
| **Proposal too large** | Many problems bundled | RFC never finishes review | Split into dependent RFCs; use `depends_on` |
| **Ambiguous requirements** | Hand-wavy prose | Two conforming implementations diverge | Replace prose with testable MUST/SHOULD |
| **Reviewer cannot identify success** | Only acceptance listed | Ecosystem cannot tell if RFC worked | Add success signals per VP-RFC-0000 §13 |

---

## RFC self-review

Before setting `status: review`, walk this checklist. Be harsh—you are standing in for a stranger five years from now.

### Understanding

- [ ] Can a new contributor understand this without oral history?
- [ ] Summary matches Proposal without contradictions
- [ ] Problem Statement does not assume the solution

### Architecture

- [ ] Affected models identified with section IDs
- [ ] Structural vs extension change is explicit
- [ ] Architecture Impact is **None** only with justification

### Terminology

- [ ] **VP-TERM-*** references included for every canonical term touched
- [ ] No forbidden synonyms (e.g. *transaction* for *claim*)
- [ ] Glossary amendments planned if vocabulary is new

### Conformance

- [ ] VP-CS impacts identified or **None** justified
- [ ] Conformance pyramid level named if behavior changes

### Migration

- [ ] Upgrade path clear for breaking changes
- [ ] `supersedes` / `depends_on` metadata accurate

### Security

- [ ] Trust boundary changes identified
- [ ] Security Impact is **None** only with argument

### Specification

- [ ] Every MUST is intentional
- [ ] Normative and informative sections distinguishable
- [ ] Proposal stands without implementation repository context

### Scope

- [ ] Solving one problem well (RFC principles)
- [ ] Non-Goals defend boundaries
- [ ] Open Questions do not hide blockers

### Process

- [ ] Front matter complete per [VP-RFC-0000 §7](../0000-rfc-process.md#7-required-metadata)
- [ ] Ready for entry in [`spec/rfcs/registry.yaml`](../../spec/rfcs/registry.yaml) on acceptance
- [ ] [RFC invariants](../0000-rfc-process.md#11-rfc-invariants) satisfied

---

## Reviewer lens

Reviewers are not gatekeepers to persuade—they are engineers asking whether the protocol remains **coherent, interoperable, and understandable**.

During review, expect questions like:

| Lens | Question |
|------|----------|
| **Coherence** | Does this fit Architecture Alpha—or amend it explicitly? |
| **Simplicity** | Is there a smaller change that achieves the goals? |
| **Interoperability** | Will two independent implementations converge? |
| **Conceptual integrity** | Does this preserve claim / verification / outcome separation? |
| **Architecture fit** | Are the right models touched—not the convenient file? |
| **Longevity** | Will a future maintainer know *why* from the text alone? |

Respond in the **RFC document**, not only in review threads. The merged text is the institutional record.

Critique ideas, not people. Evidence over authority. Protocol before implementation—per [VP-RFC-0000 §9](../0000-rfc-process.md#9-review-philosophy).

---

## Characteristics of great RFCs

| Dimension | Poor RFC | Good RFC | Excellent RFC |
|-----------|----------|----------|---------------|
| **Problem clarity** | Jumps to solution | States gap and motivation | Problem understandable without Proposal |
| **Evidence** | Anecdote and urgency | Examples and failure modes | Reproducible scenario trace |
| **Scope** | Kitchen sink | One main problem | Non-Goals protect future work |
| **Terminology** | Ad hoc words | Links glossary terms | Amends **VP-TERM-*** with migration |
| **Architecture** | Ignores models | Names affected sections | Strengthens model coherence |
| **Conformance** | "Tests later" | Names VP-CS impact | Scenarios executable in principle |
| **Migration** | Assumes upgrade | Describes phases | Old and new deployments coexist safely |
| **Longevity** | Needs author present | Self-contained | Makes spec *easier* than before |

Excellent RFCs are rare. Good RFCs are the target. Poor RFCs are learning experiences—revise or split rather than argue for acceptance.

---

## Copy-paste starter

Copy into `rfcs/NNNN-short-title.md`. Replace placeholders. Remove HTML comments before **Review**. Assign the next RFC number in your pull request.

Required metadata: [VP-RFC-0000 §7](../0000-rfc-process.md#7-required-metadata). Assign `concept_id: VP-RFC-NNNN` when the number is reserved.

```markdown
---
rfc: NNNN
id: NNNN
concept_id: VP-RFC-NNNN
title: 
status: draft
version: 0.1.0
type: protocol
pyramid_level: specification

authors: []
reviewers: []

created: YYYY-MM-DD
updated: YYYY-MM-DD

depends_on: []
supersedes: []
superseded_by: null

related_terms: []
related_architecture: []
related_conformance: []

constitutional_refs:
  - ../docs/00-overview/MANIFESTO.md
  - ../docs/00-overview/VISION.md
  - ../docs/00-overview/PRINCIPLES.md
  - ../docs/00-overview/GLOSSARY.md

related_docs: []
implementation_status: not_started
---

**Pyramid level:** specification · **Status:** draft · **Version:** 0.1.0 · **Concept ID:** VP-RFC-NNNN

**Constitutional basis:** MANIFESTO, VISION, PRINCIPLES, GLOSSARY (cite as applicable)

---

# RFC-NNNN: {title}

## Summary



## Motivation



## Problem Statement



## Goals



## Non-Goals



## Proposal



## Architecture Impact



## Terminology Impact



## Conformance Impact



## Security Impact



## Backwards Compatibility



## Migration Strategy



## Alternatives Considered



## Open Questions



## Acceptance Criteria



## References



## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | YYYY-MM-DD | Initial draft |
```

---

## Closing

The best RFCs do more than introduce new behavior.

They make the protocol **easier to understand** than it was before.

When you finish drafting, ask: *If this is accepted, will a stranger five years from now thank us for the clarity—or curse us for the ambiguity?* Write for that stranger.

For lifecycle, acceptance, amendment rules, and registry sync, return to **[VP-RFC-0000](../0000-rfc-process.md)**.

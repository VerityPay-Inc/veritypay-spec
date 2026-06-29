# Request for Comments (RFCs)

Formal proposals that introduce, modify, or retire normative VerityPay protocol behavior.

---

## Purpose

RFCs are the primary mechanism for changing the VerityPay specification. Each RFC is a self-contained document that explains a problem, presents a solution, considers alternatives, and defines what implementations must do if the RFC is accepted.

The RFC process exists to:

- Make protocol evolution **visible** before it becomes entrenched in code
- Force explicit discussion of **trade-offs and compatibility**
- Create an **audit trail** of why the protocol looks the way it does
- Give implementers a **stable reference** for conformance

This directory operates like a standards body change queue—not a feature backlog for any single product.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Protocol designers | Author and revise proposals |
| Implementers | Determine required behavior for a given spec version |
| Reviewers | Evaluate technical merit and ecosystem impact |
| Auditors | Trace requirements to documented decisions |
| Integrators | Assess upcoming breaking changes early |

**Implementers:** target a defined set of accepted RFCs. Behavior described only in drafts is not required for conformance.

---

## Scope

**In scope**

- RFC drafts — work-in-progress proposals open for comment
- Accepted RFCs — binding specification text
- Rejected RFCs — preserved with rationale to prevent re-litigation
- Superseded RFCs — marked obsolete by later RFCs, retained for history
- [`templates/RFC_TEMPLATE.md`](templates/RFC_TEMPLATE.md) — required scaffold for new proposals

**Out of scope**

- Exploratory notes without a concrete proposal → [`../docs/04-research/`](../docs/04-research/)
- Architecture overviews not tied to a specific change → [`../docs/01-architecture/`](../docs/01-architecture/)
- Stable specification documents not proposing change → [`../docs/`](../docs/) using [`../docs/templates/SPEC_TEMPLATE.md`](../docs/templates/SPEC_TEMPLATE.md)
- Source code, reference implementations, or test harnesses
- Product documentation or user guides
- Informal discussion (use the issue tracker; summarize outcomes in the RFC)

RFC numbers are assigned sequentially and permanently. Do not reuse numbers.

---

## RFC process

Detailed governance rules live in [`../docs/05-governance/`](../docs/05-governance/). Summary:

### 1. Preflight

- Search existing RFCs and [`../docs/`](../docs/) for overlap
- Confirm the change affects interoperability, security, privacy, or observable protocol behavior
- Read [`../docs/05-governance/`](../docs/05-governance/) for current acceptance criteria

### 2. Draft

- Copy [`templates/RFC_TEMPLATE.md`](templates/RFC_TEMPLATE.md)
- Assign the next available RFC number in your pull request (maintainers may renumber during review)
- Set `status: draft` and complete all front matter fields
- Open a pull request for community comment

### 3. Review

- Address feedback in the RFC document and pull request thread
- Update `reviewers` and `related_docs` as review progresses
- Set `status: review` when ready for maintainer decision

### 4. Terminal states

| Status | Meaning |
|--------|---------|
| **accepted** | Becomes part of the protocol; implementations must conform |
| **rejected** | Will not be adopted; document retained with rationale |
| **superseded** | Replaced by a newer RFC; follow the successor |

Accepted RFCs may require companion updates to [`../docs/01-architecture/`](../docs/01-architecture/), [`../diagrams/`](../diagrams/), or stable specs authored from [`../docs/templates/SPEC_TEMPLATE.md`](../docs/templates/SPEC_TEMPLATE.md).

### 5. Implementation tracking

Authors and maintainers update `implementation_status` in RFC front matter as known implementations progress. This field is **informational**—conformance is determined by accepted RFC text, not by any single codebase.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../docs/05-governance/`](../docs/05-governance/) | Authority for roles, voting, and acceptance criteria |
| [`../docs/01-architecture/`](../01-architecture/) | Structural context RFCs must align with or update |
| [`../docs/04-research/`](../04-research/) | Source material that may precede an RFC |
| [`../docs/templates/SPEC_TEMPLATE.md`](../docs/templates/SPEC_TEMPLATE.md) | Format for stable docs an RFC may create or amend |
| [`../docs/templates/DECISION_RECORD_TEMPLATE.md`](../docs/templates/DECISION_RECORD_TEMPLATE.md) | Optional companion for decisions not fully captured in RFC prose |
| [`../docs/03-development/`](../03-development/) | Conformance expectations for implementers of accepted RFCs |

---

## How to propose an RFC

1. Read governance material in [`../docs/05-governance/`](../docs/05-governance/)
2. Copy [`templates/RFC_TEMPLATE.md`](templates/RFC_TEMPLATE.md) into this directory
3. Name the file `NNNN-short-title.md` (zero-padded RFC number, kebab-case slug)
4. Open a pull request and engage with review until the RFC reaches a terminal state

Questions about whether an idea requires an RFC belong in issues. The default assumption for protocol-facing changes is **yes**.

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

---

## What belongs here

- **RFC drafts** — work-in-progress proposals open for comment
- **Accepted RFCs** — binding specification text
- **Rejected RFCs** — preserved with rationale to prevent re-litigation
- **Superseded RFCs** — marked obsolete by later RFCs, retained for history

Each RFC should use the template in [`../templates/`](../templates/) unless governance explicitly approves an alternative format.

---

## What does not belong here

- Exploratory notes without a concrete proposal → [`../docs/04-research/`](../docs/04-research/)
- Architecture overviews not tied to a specific change → [`../docs/01-architecture/`](../docs/01-architecture/)
- Source code, reference implementations, or test harnesses
- Product documentation or user guides
- Informal discussion threads (use issue tracker instead; summarize outcomes in the RFC)

---

## RFC lifecycle (summary)

Detailed rules live in [`../docs/05-governance/`](../docs/05-governance/). At a high level:

| Stage | Meaning |
|-------|---------|
| **Draft** | Author seeking feedback; not normative |
| **Review** | Active community and maintainer review |
| **Accepted** | Becomes part of the protocol; implementations must conform |
| **Rejected** | Will not be adopted; document retained |
| **Superseded** | Replaced by a newer RFC; follow the successor |

RFC numbers are assigned sequentially and permanently. Do not reuse numbers.

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

## How to propose an RFC

1. Read [`../docs/05-governance/`](../docs/05-governance/) and existing RFCs for overlap
2. Copy the RFC template from [`../templates/`](../templates/)
3. Open a pull request with your draft in this directory
4. Engage with review feedback until the RFC reaches a terminal state

Questions about whether an idea needs an RFC belong in issues; the answer usually yes if it affects interoperability, security, privacy, or observable protocol behavior.

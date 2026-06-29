# Product

Documentation that describes VerityPay from the perspective of people and organizations who use or integrate the protocol—not from the perspective of internal code modules.

---

## Purpose

Product documentation bridges abstract protocol concepts and real-world use. It explains who participates in the ecosystem, what they are trying to accomplish, and how specified behavior manifests in observable outcomes.

This folder keeps user-facing clarity separate from architectural internals. A merchant should not need to read trust-boundary diagrams to understand what a payment verification means for their business.

---

## What belongs here

- **Personas and roles** — payers, payees, issuers, acquirers, wallets, merchants, auditors, and other ecosystem participants
- **Use cases and scenarios** — concrete situations the protocol is designed to support
- **User journeys** — step-by-step flows described in domain language (not API call sequences)
- **Capability matrix** — which features or guarantees apply in which contexts
- **Compliance and policy context** — how the protocol relates to regulatory categories (descriptive, not legal advice)
- **Integration patterns** — recommended ways external systems connect to VerityPay behavior at a conceptual level
- **Error and edge-case narratives** — what users and operators should expect when things go wrong

---

## What does not belong here

- Protocol internals, entity schemas, or cryptographic details → [`../01-architecture/`](../01-architecture/)
- Vision statements without operational detail → [`../00-overview/`](../00-overview/)
- Build guides, language-specific SDK docs, or repository setup → [`../03-development/`](../03-development/) and implementation repositories
- Hypothetical features under exploration → [`../04-research/`](../04-research/)
- Governance process documentation → [`../05-governance/`](../05-governance/)
- Marketing copy disconnected from specified behavior
- UI mockups tied to a single proprietary product (unless clearly labeled as illustrative)

Product documents describe **specified behavior**. If a capability is not yet accepted via RFC, label it clearly as planned or proposed.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Product managers | Align roadmaps with protocol capabilities |
| Merchant and partner teams | Understand integration impact and user experience |
| Technical writers | Source accurate user-facing documentation |
| Sales and solutions engineers | Explain value without overpromising unspecified features |
| Implementers | Validate that UX and APIs reflect intended outcomes |

Start with [`../00-overview/`](../00-overview/) for context. Consult [`../01-architecture/`](../01-architecture/) when product claims require structural grounding.

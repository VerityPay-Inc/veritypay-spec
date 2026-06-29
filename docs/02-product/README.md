# Product

Documentation that describes VerityPay from the perspective of people and organizations who use or integrate the protocol—not from the perspective of internal code modules.

---

## Purpose

Product documentation bridges abstract protocol concepts and real-world use. It explains who participates in the ecosystem, what they are trying to accomplish, and how specified behavior manifests in observable outcomes.

This folder keeps participant-facing clarity separate from architectural internals.

---

## Audience

| Reader | Why read this folder |
|--------|---------------------|
| Product managers | Align roadmaps with protocol capabilities |
| Merchant and partner teams | Understand integration impact and participant experience |
| Technical writers | Source accurate user-facing documentation |
| Solutions engineers | Explain value without overpromising unspecified features |
| Implementers | Validate that observable behavior reflects intended outcomes |

Start with [`../00-overview/`](../00-overview/) for context. Consult [`../01-architecture/`](../01-architecture/) when product claims require structural grounding.

---

## Scope

**In scope**

- Personas and roles — payers, payees, issuers, acquirers, wallets, merchants, auditors, and other participants
- Use cases and scenarios — concrete situations the protocol is designed to support
- User journeys — step-by-step flows in domain language (not call sequences)
- Capability matrix — which guarantees apply in which contexts
- Compliance and policy context — descriptive relationship to regulatory categories (not legal advice)
- Integration patterns — conceptual ways external systems connect to VerityPay behavior
- Error and edge-case narratives — expected outcomes when things go wrong

**Out of scope**

- Protocol internals, entity schemas, or cryptographic detail → [`../01-architecture/`](../01-architecture/)
- Vision statements without operational detail → [`../00-overview/`](../00-overview/)
- Build guides and language-specific SDK documentation → [`../03-development/`](../03-development/) and implementation repositories
- Hypothetical features under exploration → [`../04-research/`](../04-research/)
- Governance process documentation → [`../05-governance/`](../05-governance/)
- Marketing copy disconnected from specified behavior
- UI mockups tied to a single proprietary product (unless clearly labeled illustrative)

Product documents describe **specified behavior**. Capabilities not yet accepted via RFC must be labeled as planned or proposed.

---

## Related specifications

| Document / area | Relationship |
|-----------------|--------------|
| [`../00-overview/`](../00-overview/) | Strategic intent that product documentation must reflect |
| [`../01-architecture/`](../01-architecture/) | Structural grounding for product claims and guarantees |
| [`../../rfcs/`](../../rfcs/) | Normative source for capabilities described in product terms |
| [`../03-development/`](../03-development/) | How implementers map product expectations to conformance |
| [`../templates/SPEC_TEMPLATE.md`](../templates/SPEC_TEMPLATE.md) | Format for stable product-facing specification documents |

#!/usr/bin/env python3
"""Sync spec/terminology/registry.yaml and patch GLOSSARY.md metadata."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
GLOSSARY = ROOT / "docs/00-overview/GLOSSARY.md"
REGISTRY = ROOT / "spec/terminology/registry.yaml"
REGISTRY_VERSION = "0.4.0"

DM = "[DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md)"
IM = "[IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md)"
BM = "[BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md)"
DAT = "[DATA_MODEL.md](../01-architecture/DATA_MODEL.md)"
SM = "[STATE_MODEL.md](../01-architecture/STATE_MODEL.md)"
CM = "[CONFORMANCE_MODEL.md](../03-development/CONFORMANCE_MODEL.md)"
GV = "[GOVERNANCE.md](../05-governance/GOVERNANCE.md)"
GL = "[GLOSSARY.md](GLOSSARY.md)"
VI = "[VISION.md](VISION.md)"
PR = "[PRINCIPLES.md](PRINCIPLES.md)"
MA = "[MANIFESTO.md](MANIFESTO.md)"
CO = "[CONTRIBUTING.md](../../CONTRIBUTING.md)"
RFC = "[`rfcs/`](../../rfcs/)"
ARCH = "[`01-architecture/`](../01-architecture/)"
ADR_T = "[`DECISION_RECORD_TEMPLATE.md`](../templates/DECISION_RECORD_TEMPLATE.md)"

# Machine registry + glossary normative-definition patches
TERMS: list[dict] = [
    {"id": "VP-TERM-001", "anchor": "protocol", "title": "Protocol", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-1.1", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["MANIFESTO"], "depends_on": []},
    {"id": "VP-TERM-002", "anchor": "participant", "title": "Participant", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-4.10", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["DATA_MODEL", "STATE_MODEL"], "depends_on": ["VP-TERM-001"]},
    {"id": "VP-TERM-003", "anchor": "role", "title": "Role", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "DM-4.11", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["BEHAVIOR_MODEL", "DATA_MODEL"], "depends_on": ["VP-TERM-002"]},
    {"id": "VP-TERM-004", "anchor": "verifiable-claim", "title": "Verifiable Claim", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-4.1", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["IDENTITY_MODEL", "DATA_MODEL", "STATE_MODEL"], "depends_on": ["VP-TERM-013"]},
    {"id": "VP-TERM-005", "anchor": "subject", "title": "Subject", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-4.5", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["IDENTITY_MODEL", "DATA_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-006", "anchor": "identity", "title": "Identity", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "IM-2.1", "normative_link": IM, "normative_doc": "IDENTITY_MODEL", "referenced_by": ["PRINCIPLES"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-007", "anchor": "semantic-identity", "title": "Semantic Identity", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "IM-2.1", "normative_link": IM, "normative_doc": "IDENTITY_MODEL", "referenced_by": ["DATA_MODEL"], "depends_on": ["VP-TERM-006"]},
    {"id": "VP-TERM-008", "anchor": "evidence", "title": "Evidence", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "DM-4.7", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["BEHAVIOR_MODEL", "DATA_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-009", "anchor": "verification", "title": "Verification", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "DM-4.8", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["BEHAVIOR_MODEL", "STATE_MODEL"], "depends_on": ["VP-TERM-004", "VP-TERM-008", "VP-TERM-028"]},
    {"id": "VP-TERM-010", "anchor": "verification-record", "title": "Verification Record", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "IM-6.1", "normative_link": IM, "normative_doc": "IDENTITY_MODEL", "referenced_by": ["DATA_MODEL", "STATE_MODEL"], "depends_on": ["VP-TERM-009"]},
    {"id": "VP-TERM-011", "anchor": "verification-outcome", "title": "Verification Outcome", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "DM-4.9", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["DATA_MODEL", "BEHAVIOR_MODEL"], "depends_on": ["VP-TERM-009"]},
    {"id": "VP-TERM-012", "anchor": "knowledge-state", "title": "Knowledge State", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "SM-2.1", "normative_link": SM, "normative_doc": "STATE_MODEL", "referenced_by": [], "depends_on": ["VP-TERM-010", "VP-TERM-004"]},
    {"id": "VP-TERM-013", "anchor": "assertion", "title": "Assertion", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "DM-4.6", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["BEHAVIOR_MODEL"], "depends_on": ["VP-TERM-002", "VP-TERM-003"]},
    {"id": "VP-TERM-014", "anchor": "protocol-event", "title": "Protocol Event", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "BM-5.1", "normative_link": BM, "normative_doc": "BEHAVIOR_MODEL", "referenced_by": ["DATA_MODEL", "STATE_MODEL"], "depends_on": ["VP-TERM-013", "VP-TERM-009"]},
    {"id": "VP-TERM-015", "anchor": "supersession", "title": "Supersession", "stability": "stable", "classification": "behavioral", "normative_status": "core", "section_id": "BM-3.7", "normative_link": BM, "normative_doc": "BEHAVIOR_MODEL", "referenced_by": ["STATE_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-016", "anchor": "storage-identifier", "title": "Storage Identifier", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "DAT-8.1", "normative_link": DAT, "normative_doc": "DATA_MODEL", "referenced_by": ["DATA_MODEL"], "depends_on": ["VP-TERM-007"]},
    {"id": "VP-TERM-017", "anchor": "representation", "title": "Representation", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "DAT-3.1", "normative_link": DAT, "normative_doc": "DATA_MODEL", "referenced_by": ["PRINCIPLES"], "depends_on": ["VP-TERM-006"]},
    {"id": "VP-TERM-018", "anchor": "representation-guarantee", "title": "Representation Guarantee", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "DAT-9.1", "normative_link": DAT, "normative_doc": "DATA_MODEL", "referenced_by": [], "depends_on": ["VP-TERM-017"]},
    {"id": "VP-TERM-019", "anchor": "protocol-truth", "title": "Protocol Truth", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-3.1", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": [], "depends_on": ["VP-TERM-011", "VP-TERM-028"]},
    {"id": "VP-TERM-020", "anchor": "truth", "title": "Truth", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-3.1", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["PRINCIPLES"], "depends_on": ["VP-TERM-019"]},
    {"id": "VP-TERM-021", "anchor": "extension", "title": "Extension", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "DAT-4.1", "normative_link": DAT, "normative_doc": "DATA_MODEL", "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-022", "anchor": "interoperability", "title": "Interoperability", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "DM-1.4", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["VISION"], "depends_on": ["VP-TERM-009", "VP-TERM-011"]},
    {"id": "VP-TERM-023", "anchor": "implementation", "title": "Implementation", "stability": "stable", "classification": "fundamental", "normative_status": "core", "section_id": "VI-3.1", "normative_link": VI, "normative_doc": "VISION", "referenced_by": ["GOVERNANCE", "PRINCIPLES"], "depends_on": ["VP-TERM-001"]},
    {"id": "VP-TERM-024", "anchor": "conformance", "title": "Conformance", "stability": "stable", "classification": "conformance", "normative_status": "core", "section_id": "CM-2.1", "normative_link": CM, "normative_doc": "CONFORMANCE_MODEL", "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-022", "VP-TERM-028"]},
    {"id": "VP-TERM-025", "anchor": "conformance-scenario", "title": "Conformance Scenario", "stability": "experimental", "classification": "conformance", "normative_status": "experimental", "section_id": "CM-6.1", "normative_link": CM, "normative_doc": "CONFORMANCE_MODEL", "referenced_by": [], "depends_on": ["VP-TERM-024"]},
    {"id": "VP-TERM-026", "anchor": "reference-implementation", "title": "Reference Implementation", "stability": "stable", "classification": "conformance", "normative_status": "core", "section_id": "VI-3.1", "normative_link": VI, "normative_doc": "VISION", "referenced_by": ["CONTRIBUTING", "GOVERNANCE"], "depends_on": ["VP-TERM-023"]},
    {"id": "VP-TERM-027", "anchor": "reference-interpreter", "title": "Reference Interpreter", "stability": "experimental", "classification": "conformance", "normative_status": "experimental", "section_id": "CM-6.1", "normative_link": CM, "normative_doc": "CONFORMANCE_MODEL", "referenced_by": ["PRINCIPLES", "CONTRIBUTING"], "depends_on": ["VP-TERM-025", "VP-TERM-009"]},
    {"id": "VP-TERM-028", "anchor": "specification-version", "title": "Specification Version", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "DM-4.12", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["DATA_MODEL", "GOVERNANCE"], "depends_on": ["VP-TERM-029"]},
    {"id": "VP-TERM-029", "anchor": "rfc", "title": "RFC", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "GV-5.1", "normative_link": GV, "normative_doc": "GOVERNANCE", "referenced_by": ["rfcs", "PRINCIPLES"], "depends_on": []},
    {"id": "VP-TERM-030", "anchor": "adr", "title": "ADR", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "GV-4.1", "normative_link": GV, "normative_doc": "GOVERNANCE", "referenced_by": ["CONTRIBUTING"], "depends_on": ["VP-TERM-029"]},
    {"id": "VP-TERM-031", "anchor": "architecture", "title": "Architecture", "stability": "stable", "classification": "structural", "normative_status": "core", "section_id": "GV-6.1", "normative_link": ARCH, "normative_doc": "ARCHITECTURE", "referenced_by": ["GOVERNANCE", "PRINCIPLES"], "depends_on": ["VP-TERM-001"]},
    {"id": "VP-TERM-032", "anchor": "canonical", "title": "Canonical", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "GL-1.1", "normative_link": GL, "normative_doc": "GLOSSARY", "referenced_by": ["DATA_MODEL"], "depends_on": []},
    {"id": "VP-TERM-033", "anchor": "normative", "title": "Normative", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "GV-2.1", "normative_link": GV, "normative_doc": "GOVERNANCE", "referenced_by": ["rfcs"], "depends_on": ["VP-TERM-029"]},
    {"id": "VP-TERM-034", "anchor": "informative", "title": "Informative", "stability": "stable", "classification": "governance", "normative_status": "core", "section_id": "GV-2.1", "normative_link": GV, "normative_doc": "GOVERNANCE", "referenced_by": ["ARCHITECTURE"], "depends_on": ["VP-TERM-033"]},
    {"id": "VP-TERM-035", "anchor": "payment-claim", "title": "Payment Claim", "stability": "stable", "classification": "domain", "normative_status": "domain-specific", "section_id": "DM-4.2", "normative_link": DM, "normative_doc": "DOMAIN_MODEL", "referenced_by": ["DATA_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-036", "anchor": "payroll-claim", "title": "Payroll Claim", "stability": "reserved", "classification": "domain", "normative_status": "experimental", "section_id": None, "normative_link": "— (not yet defined)", "normative_doc": None, "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-035"]},
    {"id": "VP-TERM-037", "anchor": "settlement-claim", "title": "Settlement Claim", "stability": "reserved", "classification": "domain", "normative_status": "experimental", "section_id": None, "normative_link": "— (not yet defined)", "normative_doc": None, "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-035"]},
    {"id": "VP-TERM-038", "anchor": "grant-claim", "title": "Grant Claim", "stability": "reserved", "classification": "domain", "normative_status": "experimental", "section_id": None, "normative_link": "— (not yet defined)", "normative_doc": None, "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-039", "anchor": "credential-claim", "title": "Credential Claim", "stability": "reserved", "classification": "domain", "normative_status": "experimental", "section_id": None, "normative_link": "— (not yet defined)", "normative_doc": None, "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-004"]},
    {"id": "VP-TERM-040", "anchor": "compliance-claim", "title": "Compliance Claim", "stability": "reserved", "classification": "domain", "normative_status": "experimental", "section_id": None, "normative_link": "— (not yet defined)", "normative_doc": None, "referenced_by": ["DOMAIN_MODEL"], "depends_on": ["VP-TERM-004"]},
]

DOC_PATHS = {
    "DOMAIN_MODEL": "docs/01-architecture/DOMAIN_MODEL.md",
    "IDENTITY_MODEL": "docs/01-architecture/IDENTITY_MODEL.md",
    "BEHAVIOR_MODEL": "docs/01-architecture/BEHAVIOR_MODEL.md",
    "DATA_MODEL": "docs/01-architecture/DATA_MODEL.md",
    "STATE_MODEL": "docs/01-architecture/STATE_MODEL.md",
    "CONFORMANCE_MODEL": "docs/03-development/CONFORMANCE_MODEL.md",
    "GOVERNANCE": "docs/05-governance/GOVERNANCE.md",
    "GLOSSARY": "docs/00-overview/GLOSSARY.md",
    "VISION": "docs/00-overview/VISION.md",
    "ARCHITECTURE": "docs/01-architecture/",
}


def write_registry() -> None:
    payload = {
        "spec": "SPEC-0004",
        "title": "VerityPay Terminology Registry",
        "version": REGISTRY_VERSION,
        "status": "draft",
        "human_readable": "docs/00-overview/GLOSSARY.md",
        "section_id_scheme": "docs/00-overview/GLOSSARY.md#architecture-section-ids",
        "terms": [],
    }
    for t in TERMS:
        entry = {
            "id": t["id"],
            "anchor": t["anchor"],
            "title": t["title"],
            "stability": t["stability"],
            "classification": t["classification"],
            "normative_status": t["normative_status"],
            "depends_on": t["depends_on"],
            "normative_definition": None,
            "referenced_by": t["referenced_by"],
        }
        if t["normative_doc"]:
            entry["normative_definition"] = {
                "document": t["normative_doc"],
                "path": DOC_PATHS.get(t["normative_doc"], t["normative_doc"]),
                "section_id": t["section_id"],
            }
        payload["terms"].append(entry)

    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# VerityPay Terminology Registry (machine-readable)\n"
        "# Human-readable definitions: docs/00-overview/GLOSSARY.md\n"
        "# RFCs SHOULD cite VP-TERM-* and architecture section IDs (e.g. DM-4.8, VP-TERM-009)\n\n"
    )
    REGISTRY.write_text(
        header + yaml.dump(payload, sort_keys=False, allow_unicode=True, default_flow_style=False),
        encoding="utf-8",
    )


def patch_glossary() -> None:
    text = GLOSSARY.read_text(encoding="utf-8")
    text = text.replace("version: 0.3.0", f"version: {REGISTRY_VERSION}", 1)
    text = text.replace(
        "**Pyramid level:** constitutional · **Status:** draft · **Version:** 0.3.0",
        f"**Pyramid level:** constitutional · **Status:** draft · **Version:** {REGISTRY_VERSION}",
    )
    text = text.replace("follow **Authority** links", "follow **Normative definition** links")
    text = text.replace("**Authority**", "**Normative definition**")
    text = text.replace(
        "one definitional source; list **Referenced by**",
        "one normative definition; list **Referenced by**",
    )
    text = text.replace(
        "5. **Name a single authority document**",
        "5. **Name a single normative definition**",
    )

    # Vocabulary stability: add Proposed + lifecycle
    old_stability = """| Level | Meaning | Change process |
|-------|---------|----------------|
| **Stable** | Normative vocabulary; safe for long-lived integrations | Accepted RFC + glossary amendment |
| **Experimental** | Defined for exploration; semantics may shift | Early adopters SHOULD pin spec version |
| **Reserved** | Name held for a future concept; no behavior yet | Definition requires domain RFC before use |
| **Deprecated** | Historical recognition only; not for new text | See [Deprecated terminology](#deprecated-terminology) |

**Vocabulary stability** is independent"""

    new_stability = """| Level | Meaning | Change process |
|-------|---------|----------------|
| **Proposed** | Introduced by a **draft RFC**; not safe for production assumptions | Promote to Experimental or Stable on RFC acceptance; demote or withdraw if RFC rejected |
| **Experimental** | Defined for exploration; semantics may shift | Early adopters SHOULD pin spec version |
| **Stable** | Normative vocabulary; safe for long-lived integrations | Accepted RFC + glossary amendment |
| **Reserved** | Name held for a future concept; no behavior yet | Definition requires domain RFC before use |
| **Deprecated** | Historical recognition only; not for new text | See [Deprecated terminology](#deprecated-terminology) |

**Term lifecycle** (normative vocabulary):

```mermaid
graph TD
  P[Proposed]
  E[Experimental]
  S[Stable]
  D[Deprecated]
  P --> E
  E --> S
  S --> D
  E --> D
```

**Reserved** names sit outside this lifecycle until a domain RFC defines behavior.

**Vocabulary stability** is independent"""

    if old_stability in text:
        text = text.replace(old_stability, new_stability)

    # Insert architecture section IDs + dependency graph after term classification
    arch_section_block = """
---

## Architecture section IDs

Architecture documents use stable **section IDs** for cross-reference from RFCs, conformance artifacts, and tooling—alongside **VP-TERM-*** Concept IDs.

| Prefix | Document | Example |
|--------|----------|---------|
| **DM** | [DOMAIN_MODEL.md](../01-architecture/DOMAIN_MODEL.md) | **DM-4.8** — Verification |
| **IM** | [IDENTITY_MODEL.md](../01-architecture/IDENTITY_MODEL.md) | **IM-6.1** — Verification Record |
| **BM** | [BEHAVIOR_MODEL.md](../01-architecture/BEHAVIOR_MODEL.md) | **BM-5.1** — Protocol events |
| **DAT** | [DATA_MODEL.md](../01-architecture/DATA_MODEL.md) | **DAT-9.1** — Representation guarantees |
| **SM** | [STATE_MODEL.md](../01-architecture/STATE_MODEL.md) | **SM-2.1** — Knowledge states |
| **CM** | [CONFORMANCE_MODEL.md](../03-development/CONFORMANCE_MODEL.md) | **CM-6.1** — Conformance scenarios |
| **GV** | [GOVERNANCE.md](../05-governance/GOVERNANCE.md) | **GV-5.1** — RFC governance |
| **VI** | [VISION.md](VISION.md) | **VI-3.1** — Protocol responsibilities |
| **GL** | [GLOSSARY.md](GLOSSARY.md) | **GL-1.1** — Terminology registry |

RFC example: *This RFC amends **DM-4.8** and **VP-TERM-009** (Verification).*

The [machine-readable registry](../../spec/terminology/registry.yaml) includes `section_id` for each term.

---

## Concept dependency graph

Relationship graphs show how concepts connect. The **dependency graph** shows which concepts must exist before others—useful for reading order and RFC impact analysis.

```mermaid
graph TD
  P[Protocol VP-TERM-001]
  PT[Participant VP-TERM-002]
  R[Role VP-TERM-003]
  A[Assertion VP-TERM-013]
  C[Verifiable Claim VP-TERM-004]
  E[Evidence VP-TERM-008]
  V[Verification VP-TERM-009]
  VR[Verification Record VP-TERM-010]
  O[Verification Outcome VP-TERM-011]
  P --> PT
  PT --> R
  R --> A
  A --> C
  C --> E
  C --> V
  E --> V
  V --> VR
  V --> O
```

Full `depends_on` edges are published in [`spec/terminology/registry.yaml`](../../spec/terminology/registry.yaml).

"""

    marker = "A term has exactly one primary classification. Cross-cutting terms are classified by their **authoritative definition**.\n\n---\n\n## Protocol concept graph"
    if "## Architecture section IDs" not in text and marker in text:
        text = text.replace(
            marker,
            "A term has exactly one primary classification. Cross-cutting terms are classified by their **authoritative definition**."
            + arch_section_block
            + "---\n\n## Protocol concept graph",
        )

    # Registry pointer in spec modularity table
    if "registry.yaml" not in text.split("## Concept ID registry")[0]:
        text = text.replace(
            "RFCs SHOULD cite **VP-TERM-*** identifiers when amending vocabulary. Example: *This RFC amends **VP-TERM-009** (Verification).*",
            "RFCs SHOULD cite **VP-TERM-*** identifiers when amending vocabulary. Example: *This RFC amends **VP-TERM-009** (Verification).*\n\nMachine-readable term metadata: [`spec/terminology/registry.yaml`](../../spec/terminology/registry.yaml).",
        )

    # Patch each term's normative definition line with section ID
    for t in TERMS:
        anchor = t["anchor"]
        block_pat = rf'(<a id="{re.escape(anchor)}"></a>.*?)\*\*Normative definition\*\*\n\n([^\n]+)\n\n\*\*Referenced by\*\*'
        if not t.get("section_id"):
            continue
        link = t["normative_link"]
        sid = t["section_id"]
        # avoid double-patching
        replacement_link = f"{link} · **{sid}**"
        if f"**{sid}**" in text:
            m = re.search(block_pat, text, re.DOTALL)
            if m and f"**{sid}**" not in m.group(2):
                pass
        text, n = re.subn(
            block_pat,
            rf"\1**Normative definition**\n\n{replacement_link}\n\n**Referenced by**",
            text,
            count=1,
            flags=re.DOTALL,
        )
        if n == 0 and link in text:
            text = text.replace(
                f'**Normative definition**\n\n{link}\n\n**Referenced by**',
                f"**Normative definition**\n\n{replacement_link}\n\n**Referenced by**",
                1,
            )

    # Template table update
    text = text.replace(
        "| **Normative definition** | Single document that **defines** the concept in depth |",
        "| **Normative definition** | Document + **section ID** that **defines** the concept in depth |",
    )

    # Changelog
    if "| 0.4.0 |" not in text:
        text = text.replace(
            "| 0.3.0 | 2026-06-29 | Concept IDs",
            f"| 0.4.0 | 2026-06-29 | Normative definition, Proposed lifecycle, section IDs, dependency graph, registry.yaml |\n| 0.3.0 | 2026-06-29 | Concept IDs",
        )

    GLOSSARY.write_text(text, encoding="utf-8")


def main() -> None:
    write_registry()
    patch_glossary()
    print(f"Wrote {REGISTRY}")
    print(f"Patched {GLOSSARY}")


if __name__ == "__main__":
    main()

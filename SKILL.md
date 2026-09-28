---
name: amazon-product-research-suite
description: Route Amazon product research and validation requests to the right public Agent Skill, combine market, review, design-patent, supplier, and Go/No-Go evidence, and report missing inputs before execution. Use when a user asks for Amazon product research, FBA validation, review/VOC analysis, market sizing, design-around, supplier feasibility, unit economics, or a product launch decision. Do not use as a substitute for legal advice, certification approval, Amazon settlement data, or a private scoring engine that is not installed.
---

# Amazon Product Research Suite

## Purpose and scope

Use this skill as the suite entry point when a product question spans more than one evidence source or the user is unsure which skill to use. It routes the request to the smallest useful public skill, preserves the requested marketplace and time window, and makes evidence gaps explicit before work starts.

The suite router does not invent market data, legal conclusions, supplier promises, or a Go/No-Go score. It coordinates installed skills and returns an execution plan or a handoff to the missing dependency.

## Implementation Basis and Dependencies

### Implementation basis

The router is based on the Agent Skills directory contract and the four linked public workflows in `catalog/skills.json`:

- written-review collection and VOC analysis;
- design-patent and design-around pre-screening;
- SellerSprite/Amazon market research BI;
- sanitized product-decision gateway handoff.

The router only selects and sequences workflows. It does not copy private engine logic into the public package.

### Feasibility conditions

- The target Agent runtime must discover a `SKILL.md` directory.
- The selected child skill must be installed locally or available through its documented repository.
- Inputs must identify a product task, marketplace or jurisdiction where relevant, and a time window or data date when the conclusion depends on recency.
- Live collection requires network access and only public or user-authorized sources.

### Dependencies

| Dependency | Required | Validation | Fallback |
| --- | --- | --- | --- |
| Compatible Agent Skills runtime | Yes | Confirm the runtime can load this directory | Return the routing table for manual execution |
| One or more child skills from `catalog/skills.json` | Conditional | Check the expected skill directory or ask the user to install it | Return exact install command and stop before claiming execution |
| Public source data or user-provided exports | Conditional | Check URL, file type, date, and scope | Produce an evidence-gap plan |
| Python 3.10+ | Only for `scripts/install_suite.py` and catalog validation | Run `python --version` | Install child skills manually |
| Credentials or private services | Never required by the router | Do not request or store them | Stop and ask the user to use the private workflow outside this package |

## Inputs

| Input | Required | Type and validation | Used by |
| --- | --- | --- | --- |
| Product question | Yes | Plain-language task such as "validate this Amazon FBA product" or "analyze complaints" | Routing and scope |
| Product identifiers | Conditional | ASIN, URL, SKU, product images, model, or product description | Review, market, and design workflows |
| Marketplace and jurisdiction | Conditional | Marketplace code and country; required for current market or design-right conclusions | Market and patent routing |
| Data files | Optional | CSV, JSON, XLSX, PDF, image, or URL; preserve source and date | Child-skill execution |
| Business constraints | Optional | Target price, margin, MOQ, tooling budget, lead time, non-negotiable features | Decision and supplier routing |
| Authorization and privacy limits | Optional but explicit | State whether external processing and public-source collection are allowed | Prevent unauthorized collection or upload |

If an input is missing, conflicting, stale, or sensitive, report the gap and ask only for the smallest clarification needed. Never silently infer a credential, legal jurisdiction, or market denominator.

## Outputs

Every run returns a routing record containing:

1. **Selected skills**: child skill name, reason, and required inputs.
2. **Execution order**: the smallest sequence that can answer the user's question.
3. **Evidence contract**: source, date, scope, expected artifact, and whether each result is observed, calculated, modeled, inferred, or assumed.
4. **Missing-input list**: blockers, optional gaps, and the next validation action.
5. **Artifact plan**: expected JSON, CSV, XLSX, HTML, search log, or signed handoff destination.
6. **Boundary note**: what the run cannot prove, including legal, certification, platform-policy, and private-engine limits.

Acceptance criteria: the user can identify which skill to run, what to provide, what artifact to expect, and what would stop the workflow. If a child skill is unavailable, return the documented install command instead of fabricating a result.

## Routing rules

| User intent | Route |
| --- | --- |
| Reviews, complaints, VOC, sentiment, recurring pain, product improvements | `amazon-review-intelligence-skill` |
| Visual similarity, design rights, design patent, design-around, product drawing comparison | `design-patent-search-and-design-around` |
| Amazon category sizing, keyword expansion, ASIN discovery, SellerSprite, BI dashboard, market boundary | `sellersprite-bi-market-research` |
| Product validation, supplier feasibility, unit economics, cash, stage gate, Go/No-Go | `amazon-product-decision-gateway` |
| Cross-functional product launch question | Route market -> review -> patent/design -> supplier/economics -> gateway, skipping modules with no relevance |

Do not route a single narrow question through the entire suite merely to produce a longer report.

## Workflow

1. Restate the decision in one sentence and identify the user, marketplace, time window, and deadline.
2. Match the intent to one or more rows in the routing table.
3. Check whether the child skill is installed and whether required inputs are present.
4. Produce an evidence contract and a short execution order.
5. Run the child skill(s) only after external collection or processing authorization is clear.
6. Preserve source references and label observed data, calculations, models, inferences, and assumptions separately.
7. Handoff normalized outputs to the next child skill without changing the source meaning.
8. Stop at a hard blocker and report recovery steps.
9. Verify that every promised artifact exists and state partial results explicitly.

## Example

User request:

```text
I want to launch a magnetic car phone mount on Amazon US. Check demand, read competitor complaints, see if the shape is too close to an existing design, and tell me whether to prototype.
```

Expected routing response:

```text
1. SellerSprite BI: define the direct market and comparable ASIN set.
2. Amazon Review Intelligence: collect written reviews and convert recurring complaints into product requirements.
3. Design Patent Search and Design-around: pre-screen the product images and relevant US design records.
4. Amazon Product Decision Gateway: combine the sanitized evidence with supplier, cost, and cash constraints.

Required before execution: marketplace confirmation, product/competitor identifiers, available images,
target price and margin, MOQ or tooling assumptions, and permission to process public sources.
```

## Error handling and stopping conditions

- **Child skill missing**: return the exact repository and install command; do not claim completion.
- **Unsupported marketplace or jurisdiction**: narrow the scope or stop before a legal or market conclusion.
- **CAPTCHA, sign-in, Robot Check, or account warning**: stop collection and preserve the partial result.
- **Missing detailed export or stale data**: downgrade the output and label the coverage limit.
- **Private engine unavailable**: validate the request locally and produce a handoff package; do not guess the official decision.
- **Sensitive data detected**: redact, request authorization, or stop before upload.

## Validation and definition of done

The router is complete when:

- a narrow review, patent, market, and decision request each select the correct child skill;
- a cross-functional request returns an ordered multi-skill plan;
- an unrelated request such as generic copywriting does not trigger this skill;
- missing child skills produce install instructions rather than false results;
- the catalog passes `python scripts/validate_catalog.py`.

---
name: amazon-product-research-suite
description: Route cross-functional Amazon product research to the smallest set of installed Agent Skills and preserve a shared evidence contract. Use when a request spans at least two of market sizing, review/VOC, differentiation, design-patent, supplier, unit-economics, or Go/No-Go work, or when the user explicitly asks which Amazon research Skill to use. For a single narrow task, use the matching specialist Skill instead. This router does not provide legal advice, certification approval, Amazon settlement data, or a private scoring engine.
---

# Amazon Product Research Suite

## Purpose and scope

Use this Skill as the suite entry point when the product decision crosses two or more evidence domains, or when the user does not know which specialist Skill applies. Select the smallest sufficient set of Skills, preserve the marketplace and evidence date, and make missing inputs explicit before execution.

For a narrow request, route directly to the specialist and do not run the suite merely to produce a longer report. The router never invents market data, legal conclusions, supplier promises, cost assumptions, or a Go/No-Go score.

## Implementation Basis and Dependencies

The router uses the Agent Skills directory contract, the routing table below, and the bundled artifact schemas in `references/`. It sequences public specialist workflows without copying private scoring logic into this package.

| Dependency | Required | Provider and validation | Fallback or stop behavior |
| --- | --- | --- | --- |
| Compatible Agent Skills runtime | Yes | Host runtime; confirm it can load this `SKILL.md` | Return a manual routing plan |
| One or more specialist Skills | Conditional | Local installation or the public repositories named below | Give the exact install command; do not claim execution |
| Product evidence | Conditional | User-authorized files, URLs, exports, images, quotes, or assumptions | Return an evidence-gap plan |
| Network access | Conditional | Required only for live public-source collection or installation | Work from supplied evidence or stop the live step |
| Python 3.10+ | Optional | Runs the zero-third-party-dependency installer and validators | Install manually and inspect JSON artifacts manually |
| Credentials or private services | Not required by router | Never request or store them for routing | Keep private execution outside the public package |

Feasibility requires a defined product decision and enough scope to identify the relevant marketplace, jurisdiction, evidence date, and business constraint. Live collection is limited to public or user-authorized sources.

## Inputs

| Input | Requirement | Type, source, validation, and sensitivity |
| --- | --- | --- |
| Product decision | Required | Plain-language question naming the decision to make; ask for one sentence if unclear |
| Product identifiers | Conditional | ASIN, URL, SKU, images, model, or description; preserve identifiers exactly |
| Scope | Conditional | Marketplace, jurisdiction, evidence date or time window; required when conclusions depend on location or recency |
| Evidence files | Optional | CSV, JSON, XLSX, PDF, image, URL, or supplier quote; record source and date and never silently upload sensitive data |
| Business constraints | Optional | Price, margin, MOQ, tooling budget, lead time, return-rate assumption, cash limit, and non-negotiable features |
| Authorization boundary | Conditional | State whether public-source collection, account use, external processing, or uploads are allowed |

If inputs are stale, conflicting, sensitive, or incomplete, report the smallest blocking gap. Never infer credentials, legal jurisdiction, a market denominator, supplier commitments, or missing financial assumptions.

## Outputs

Every run returns:

1. `route-plan.json` or an equivalent structured routing record conforming to `references/route-plan.schema.json`.
2. Selected Skill names, reasons, pinned install commands when missing, and the smallest execution order.
3. An evidence contract conforming to `references/evidence-bundle.schema.json` for cross-Skill handoffs.
4. Missing inputs separated into blockers and optional quality gaps.
5. Expected artifact destinations such as JSON, CSV, XLSX, HTML, search logs, or decision handoffs.
6. Explicit boundaries and partial-result status.

Success means the user can identify what runs, what evidence it needs, what artifact it produces, and what stops it. External writes, downloads, account actions, or uploads require the authorization normally required by the selected Skill; routing alone causes none of those side effects.

## Routing rules

| User intent | Specialist Skill | Install command when missing |
| --- | --- | --- |
| Reviews, complaints, VOC, recurring pain, review collection | `amazon-review-scraper` | `npx skills add PDBen-Auto/amazon-review-intelligence-skill --skill amazon-review-scraper` |
| Convert evidence into differentiated mechanisms, specifications, experiments, and kill criteria | `amazon-product-differentiation-rd` | `npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-product-differentiation-rd` |
| Visual similarity, design rights, design patent, design-around | `design-patent-search-and-design-around` | `npx skills add PDBen-Auto/design-patent-design-around-skill --skill design-patent-search-and-design-around` |
| Amazon category sizing, keyword expansion, ASIN discovery, SellerSprite, market boundary | `sellersprite-bi-market-research` | `npx skills add PDBen-Auto/sellersprite-amazon-market-research-bi-skill --skill sellersprite-bi-market-research` |
| RFQ, MOQ, tooling, lead time, supplier comparison, sample gates | `amazon-supplier-feasibility` | `npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-supplier-feasibility` |
| Contribution margin, break-even ACOS, returns sensitivity, inventory cash | `amazon-unit-economics-cashflow` | `npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-unit-economics-cashflow` |
| Stage gate or formal Go/No-Go handoff | `amazon-product-decision-gateway` | `npx skills add PDBen-Auto/amazon-product-decision-suite --skill amazon-product-decision-gateway` |

For a cross-functional launch decision, normally sequence market -> customer evidence -> differentiation -> design/IP -> supplier -> unit economics -> decision gateway. Skip any module that cannot change the decision.

## Workflow

1. Restate the decision, marketplace, time window, and deadline in one sentence.
2. Select the smallest set of relevant Skills from the routing table above.
3. Check installation and required inputs before promising execution.
4. Create the route plan and evidence contract.
5. Run specialist Skills only when their data access and external actions are authorized.
6. Preserve source meaning and label each claim as observed, calculated, modeled, inferred, or assumed.
7. Validate cross-Skill JSON against the bundled schemas when those artifacts are produced. In the repository checkout, `scripts/validate_artifact.py` provides a zero-dependency validator.
8. Stop at a hard blocker, preserve partial results, and state the recovery action.
9. Verify every promised artifact exists before reporting completion.

## Example

```text
Use $amazon-product-research-suite to evaluate a magnetic car phone mount for Amazon US.
I need the direct market, recurring complaints, a differentiated specification, supplier
questions, unit economics, and a recommendation on whether to prototype.
```

Route to market -> review -> differentiation -> supplier -> unit economics -> decision gateway. Add design-patent pre-screening when product images or a design direction exist. Required before execution: identifiers or seed terms, evidence date, target price, cost assumptions, cash limit, and authorization for any live collection.

## Error handling and stopping conditions

- Missing specialist: return its pinned catalog install command.
- Unsupported marketplace or jurisdiction: narrow scope or stop the affected conclusion.
- CAPTCHA, sign-in warning, account challenge, or access restriction: stop collection and preserve partial data.
- Stale or incomplete export: downgrade coverage and label the limitation.
- Missing cost, MOQ, return-rate, or advertising assumptions: do not issue a financial recommendation.
- Private engine unavailable: create a sanitized local handoff; do not guess its result.
- Sensitive data detected: redact, obtain authorization, or stop before external processing.

## Validation and definition of done

- Narrow review, differentiation, patent, market, supplier, finance, and decision requests each select one correct specialist.
- Cross-functional requests produce an ordered multi-Skill plan.
- Generic ecommerce copywriting, listing writing, and unrelated data analysis do not trigger this router.
- Missing specialists produce pinned install instructions rather than fabricated execution.
- `python scripts/validate_catalog.py`, `python scripts/validate_artifact.py`, and the test suite pass.

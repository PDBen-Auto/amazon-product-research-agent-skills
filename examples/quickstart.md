# Quickstart requests

## Route a cross-functional decision

```text
Use $amazon-product-research-suite to evaluate this Amazon US product.
I need the direct market, recurring customer pain, a differentiated specification,
supplier feasibility, unit economics, and a recommendation on whether to fund a sample.
List missing evidence before live collection.
```

Expected result: an ordered route plan, evidence contract, artifact plan, and explicit blockers. The router should not run irrelevant modules.

## Build a testable product concept

```text
Use $amazon-product-differentiation-rd. Convert these review findings and return reasons
into no more than three product mechanisms. Give each mechanism a measurable specification,
experiment, tradeoff, and kill criterion.
```

Expected result: evidence-to-mechanism mapping and a test plan. Unsupported brainstorming remains labeled as a hypothesis.

## Prepare supplier validation

```text
Use $amazon-supplier-feasibility for this specification and three supplier quotes.
Normalize currency, Incoterm, MOQ, tooling, packaging, lead time, and exclusions.
Then define sample gates before ranking the suppliers.
```

Expected result: RFQ gaps, comparable quotes, risk register, and sample acceptance criteria. No supplier is described as qualified without evidence.

## Calculate unit economics and cash

```text
Use $amazon-unit-economics-cashflow. Validate these current Amazon fees and supplier costs,
calculate contribution margin and break-even ACOS, then show higher-return and higher-ad-spend
scenarios plus the total cash needed for the first order.
```

Expected result: reconciled JSON calculations that separate per-unit profit from inventory cash and identify assumptions capable of reversing the decision.

## Requests that should not trigger the suite router

- "Rewrite this Amazon listing title."
- "Create lifestyle image copy for this product."
- "Summarize this generic spreadsheet."

These are single-purpose tasks outside the cross-functional research router.

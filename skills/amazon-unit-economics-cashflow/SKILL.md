---
name: amazon-unit-economics-cashflow
description: Calculate Amazon physical-product unit economics, break-even advertising, return-rate sensitivity, first-order cash needs, and scenario risk from explicit assumptions. Use when a user asks whether an Amazon product can make money, what ACOS is affordable, how returns affect margin, or how much cash an initial order requires. Do not invent Amazon fees, freight, tax, demand, payment terms, or financing assumptions.
---

# Amazon Unit Economics and Cash Flow

## Purpose and scope

Produce an auditable financial model for one product and marketplace. Separate known costs from assumptions, calculate a base case, and show how the decision changes under plausible scenarios.

## Implementation Basis and Dependencies

The included zero-third-party-dependency calculator applies explicit per-unit and first-order formulas. It is a planning model, not accounting, tax, or investment advice.

| Dependency | Required | Validation | Fallback |
| --- | --- | --- | --- |
| Python 3.10+ | Optional | Run `python scripts/unit_economics.py --help` | Calculate with the documented formulas and label manual work |
| Price and cost assumptions | Yes | Values are numeric, non-negative, and currency-consistent | Return the missing-assumption list |
| Marketplace fee basis | Yes for Amazon margin | User-supplied current fee or documented estimate | Do not infer a current fee |
| Demand and payment timing | Conditional for cash flow | Units, lead time, deposit, balance, and replenishment timing are explicit | Limit output to per-unit economics |

## Inputs

Provide JSON with the fields documented by `scripts/unit_economics.py --example`. Required fields are selling price, referral fee, fulfillment fee, landed product cost, return rate, return loss per returned unit, advertising ACOS, and other variable cost. First-order cash analysis additionally needs order units, tooling, setup costs, deposit rate, and working-capital buffer.

Use one currency per run. Percentages are decimals from `0` to `1`. Record the source and date of marketplace fees separately in the surrounding evidence bundle. Prices, quotes, and internal margins may be sensitive.

## Outputs

The calculator returns JSON containing revenue after returns, Amazon fees, expected return loss, advertising cost, contribution profit and margin, break-even ACOS, first-order cash requirement, and scenario results. It writes to stdout or an explicitly selected file and performs no network or account actions.

Success requires that inputs pass validation, formulas reconcile, units and currency are stated, and the output distinguishes per-unit profitability from inventory cash. Invalid input returns a non-zero exit code without partial financial claims.

## Workflow

1. Record marketplace, currency, fee source, quote date, and scenario name.
2. Separate observed costs, calculated fees, modeled rates, and assumptions.
3. Run the base case using `scripts/unit_economics.py`.
4. Test at least a downside return-rate case and a downside advertising-cost case.
5. Compare contribution margin with the user's hurdle rate.
6. Calculate first-order cash separately from accounting profit.
7. Identify the assumptions that can reverse the decision and assign a validation action.
8. Return `INSUFFICIENT_EVIDENCE` when a critical fee or cost is missing.

## Example

```bash
python scripts/unit_economics.py --example > assumptions.json
python scripts/unit_economics.py assumptions.json --pretty
```

## Error handling and stopping conditions

- Negative price or cost, percentages outside `0..1`, or inconsistent currency: fail validation.
- Current Amazon fees are unavailable: request them instead of substituting memory.
- Freight, duty, returns, discounts, or packaging are omitted: show the omission as a decision risk.
- Demand timing is absent: do not claim a cash-flow result.
- Contribution margin is positive but first-order cash exceeds the limit: report the distinction.

## Validation and definition of done

- Base, downside-return, and downside-advertising scenarios reconcile.
- Break-even ACOS is never presented as the recommended target ACOS.
- Every financial recommendation names the fee date and critical assumptions.
- `python -m unittest discover -s tests -v` passes for the bundled calculator.

# Unit economics and first-order cash

`amazon-unit-economics-cashflow` · English

## Purpose and scope

Model product contribution, break-even advertising, return sensitivity and initial cash requirements from explicit assumptions.

## Implementation Basis and Dependencies

Numeric price/cost assumptions and a documented marketplace-fee basis. Python 3.10+ runs the standard-library calculator. Cash analysis additionally requires order quantities and payment timing.

## Inputs

JSON: selling price, referral and fulfillment fees, landed cost, return rate/loss, advertising ACOS and other variable cost. Cash inputs add units, tooling, setup, deposit and buffer. Use one currency and decimal rates from 0 to 1.

## Outputs

JSON or selected file with contribution profit/margin, break-even ACOS, expected returns, first-order cash and scenarios. Invalid inputs return nonzero; no network or account changes.

## Workflow

1. Validate assumptions, fee sources, dates and units.
2. Run the bundled calculator or disclose manual calculation.
3. Reconcile the base case.
4. Vary advertising, returns and costs.
5. Separate per-unit profit from inventory cash and disclose what is excluded.

## Boundaries and stopping conditions

Never invent fees, demand, taxes, freight or terms. Missing timing limits results to per-unit economics. Planning output is not accounting, tax or investment advice.

## Example request

Use `$amazon-unit-economics-cashflow` — Model a phone mount with user-supplied price and costs; compare return/ACOS scenarios and report both contribution and first-order cash; respond in English and preserve evidence, unknowns and action boundaries.

## Complete specification

[Skill entrypoint and detailed references](../../SKILL.md).

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

Before delivery reconcile inputs, evidence, missing values, files and the original completion criteria. Mark unexecuted steps unverified; a successful script exit is not business validation.

## Language coverage and validation

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.


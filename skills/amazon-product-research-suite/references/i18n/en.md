# Amazon product research suite

`amazon-product-research-suite` · English

## Purpose and scope

Route a decision spanning at least two research domains to the smallest sufficient set of specialist Skills; a narrow task goes directly to its specialist.

## Implementation Basis and Dependencies

An Agent Skills host and the selected installed specialists. Supplied evidence can support offline work; live collection requires network and permission. Python 3.10+ is optional for bundled installers and validators.

## Inputs

Required: product decision. Conditional: ASIN or product identity, marketplace, jurisdiction, evidence window and action permissions. Optional: CSV/JSON/XLSX/PDF/images, quotes and business constraints; missing facts remain gaps.

## Outputs

route-plan.json, shared evidence contract, selected Skills and order, missing-input list and artifact destinations. Routing itself neither installs packages nor contacts services.

## Workflow

1. Define the decision and scope.
2. Choose specialists and check availability.
3. Build route and evidence records.
4. Execute only authorized stages.
5. Preserve observed/calculated/modeled/inferred/assumed status.
6. Validate handoff schemas and promised files
7. preserve partial results at blockers.

## Boundaries and stopping conditions

No invented market denominator, fees, supplier promises, legal conclusion or private-engine score. Stop the affected stage on CAPTCHA, missing access, sensitive upload or insufficient financial assumptions.

## Example request

Use `$amazon-product-research-suite` — Evaluate a car phone mount across market, reviews, differentiation, supplier feasibility and unit economics, adding patent review when visuals exist; respond in English and preserve evidence, unknowns and action boundaries.

## Complete specification

[Skill entrypoint and detailed references](../../SKILL.md).

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

Before delivery reconcile inputs, evidence, missing values, files and the original completion criteria. Mark unexecuted steps unverified; a successful script exit is not business validation.

## Language coverage and validation

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.


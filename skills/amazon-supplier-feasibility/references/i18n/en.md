# Supplier feasibility and sample gates

`amazon-supplier-feasibility` · English

## Purpose and scope

Prepare an RFQ, normalize supplier quotes and define evidence-based sample acceptance without default outreach or ordering.

## Implementation Basis and Dependencies

A product specification; comparable dated quotes for supplier comparison. Compliance scope, sample access and communication permissions are conditional. Contacting a factory requires separate authorization.

## Inputs

Specification or drawing with units/tolerances; order/demand assumptions; conditional currency, Incoterm, tooling budget and payment terms; optional PDF/XLSX/CSV quotes and quality evidence.

## Outputs

RFQ package, normalized cost/lead-time comparison, manufacturing-risk register and sample plan. Status: READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL or INSUFFICIENT_EVIDENCE.

## Workflow

1. Check specification gaps and non-negotiable requirements.
2. Prepare quote fields.
3. Normalize quantity, currency, Incoterm, inclusions and date.
4. Review tooling, capacity, quality, compliance and logistics.
5. Set sample tests before arrival.
6. Compare total feasibility and hand costs to unit economics.

## Boundaries and stopping conditions

Do not rank suppliers on incomparable quotes or treat unsupported certification as verified. A critical sample failure is not offset by low price. Do not send messages, negotiate or order without authorization.

## Example request

Use `$amazon-supplier-feasibility` — Compare phone-mount quotes only after aligning magnet grade, adhesive, torque, temperature tests, tooling ownership and packaging; respond in English and preserve evidence, unknowns and action boundaries.

## Complete specification

[Skill entrypoint and detailed references](../../SKILL.md).

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

Before delivery reconcile inputs, evidence, missing values, files and the original completion criteria. Mark unexecuted steps unverified; a successful script exit is not business validation.

## Language coverage and validation

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.


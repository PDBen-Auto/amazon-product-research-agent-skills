---
name: amazon-supplier-feasibility
description: Prepare and evaluate supplier feasibility for an Amazon physical product using an RFQ, normalized quote comparison, manufacturing-risk register, and sample acceptance gates. Use when a user asks whether a concept can be sourced, what to ask factories, how to compare MOQ/tooling/lead-time quotes, or how to approve a sample. Do not claim a supplier is qualified without verified quotes, samples, capacity, compliance evidence, and user authorization for supplier contact.
---

# Amazon Supplier Feasibility

## Purpose and scope

Turn a product specification into a supplier-ready feasibility package and an auditable comparison. This Skill prepares questions and evaluates supplied evidence; it does not contact factories, negotiate, order samples, or approve production unless separately authorized.

## Implementation Basis and Dependencies

The method combines specification completeness, RFQ normalization, process-risk review, cost and lead-time comparison, and predeclared sample gates.

| Dependency | Required | Validation | Fallback |
| --- | --- | --- | --- |
| Product specification | Yes | Materials, dimensions, performance, packaging, and target volume are stated or marked TBD | Return specification gaps before RFQ |
| Supplier quotes | Conditional for comparison | Quote date, currency, Incoterm, MOQ, tooling, lead time, and inclusions are present | Produce RFQ only |
| Compliance requirements | Conditional | Marketplace and product category are defined | Flag compliance as unresolved |
| Supplier communication access | Optional | User separately authorizes contact and account use | Prepare messages without sending |
| Sample and inspection capability | Optional | Test method and responsible party are identified | Produce gates without claiming approval |

## Inputs

| Input | Requirement | Format and handling |
| --- | --- | --- |
| Product specification | Required | Structured document, drawing, image, BOM, or written requirements with units and tolerances |
| Demand assumptions | Required for MOQ planning | Initial order quantity, monthly demand range, target launch date, and replenishment window |
| Commercial targets | Conditional | Target EXW/FOB/landed cost, currency, Incoterm, tooling budget, payment terms, and cash limit |
| Supplier quotes | Optional | PDF, XLSX, CSV, email text, or form response; preserve source and quote date |
| Quality and compliance needs | Conditional | Critical-to-quality dimensions, performance tests, labels, packaging, certifications, and marketplace |

Supplier identities, contacts, pricing, and agreements may be confidential. Keep them local unless external processing is authorized.

## Outputs

1. RFQ package with product scope, forecast tiers, commercial questions, quality requirements, and required evidence.
2. Normalized supplier comparison separating unit cost, tooling, packaging, freight basis, MOQ, lead time, terms, and exclusions.
3. Manufacturing-risk register with likelihood, impact, evidence, mitigation, and owner.
4. Sample acceptance plan with test method, sample size, threshold, failure action, and required records.
5. Feasibility status: `READY_FOR_RFQ`, `READY_FOR_SAMPLE`, `CONDITIONAL`, or `INSUFFICIENT_EVIDENCE`.

Success requires comparable commercial bases and no hidden assumptions in cost or lead time. The Skill does not send messages or place orders by default.

## Workflow

1. Check the specification for missing materials, dimensions, tolerances, performance, packaging, and regulatory requirements.
2. Separate non-negotiable requirements from target and stretch requirements.
3. Build an RFQ using the bundled `assets/supplier-quote-template.csv` fields.
4. Normalize all quotes to the same quantity tier, currency, Incoterm, inclusions, and evidence date.
5. Identify process, tooling, capacity, component, quality, compliance, packaging, and logistics risks.
6. Define sample tests and acceptance thresholds before samples arrive.
7. Compare suppliers on total feasibility, not unit price alone.
8. Route cost scenarios to `amazon-unit-economics-cashflow` before recommending an order.

## Example

For a magnetic phone mount, the RFQ should distinguish magnet grade, adhesive system, ball-joint torque, coating, temperature range, phone-weight test, packaging, tooling ownership, replacement parts, and quote basis. A low unit quote without those fields is not comparable.

## Error handling and stopping conditions

- Missing specification: stop before supplier ranking.
- Quotes use different Incoterms or inclusions: normalize or mark incomparable.
- Certification claims lack documents: treat as unverified.
- Supplier contact or ordering is requested without authorization: prepare the action and stop before sending.
- Sample test fails a critical gate: do not average it away with price advantages.

## Validation and definition of done

- Every quote includes or explicitly lacks each normalized field.
- Critical manufacturing and quality risks have evidence and an owner.
- Sample gates are measurable and declared before results.
- Feasibility status names the remaining blocker and next action.

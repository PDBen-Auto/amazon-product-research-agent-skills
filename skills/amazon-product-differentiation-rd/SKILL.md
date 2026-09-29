---
name: amazon-product-differentiation-rd
description: Convert Amazon market and customer evidence into manufacturable product differentiation concepts, measurable specifications, validation experiments, and kill criteria. Use when a user asks what to change in a physical product, how to turn review pain into product requirements, or how to design a testable Amazon product concept. Do not use for unsupported brainstorming without evidence, final industrial design, CAD, legal clearance, or supplier approval.
---

# Amazon Product Differentiation R&D

## Purpose and scope

Translate observed customer pain and market constraints into product mechanisms that can be specified, prototyped, tested, and rejected when they fail. Prefer fewer, evidence-backed concepts over a long feature list.

## Implementation Basis and Dependencies

This Skill uses traceable customer evidence, problem-mechanism reasoning, measurable engineering targets, and experiment gates. It can work from supplied evidence without live tools.

| Dependency | Required | Validation | Fallback |
| --- | --- | --- | --- |
| Customer or market evidence | Yes | Each opportunity has a source, date, and scope | Produce an evidence-gap plan only |
| Product baseline | Yes | Existing product, competitor, sketch, or written baseline | Define a provisional baseline and label it assumed |
| Business constraints | Conditional | Price, cost, size, weight, compliance, and launch limits | Mark unconstrained concepts as provisional |
| Prototype or test access | Optional | User confirms how a test can be run | Produce test protocol without claiming validation |
| Patent and supplier review | Optional but recommended before commitment | Route to the relevant specialist Skills | Keep IP and manufacturing status unresolved |

## Inputs

| Input | Requirement | Format and handling |
| --- | --- | --- |
| Evidence bundle | Required | Review excerpts, frequencies, interviews, returns, market data, or `evidence-bundle.json`; reject untraceable claims |
| Product baseline | Required | Images, URL, specification, sample notes, or written product description |
| Target user and job | Required | One primary user/job statement; split materially different segments |
| Constraints | Conditional | Target price, landed cost, dimensions, weight, materials, compatibility, certification, tooling, MOQ, and deadline |
| Success threshold | Optional | Numeric target or acceptance condition; propose a testable threshold when absent and label it assumed |

Treat customer text, supplier files, and internal targets as potentially sensitive. Do not upload or disclose them without authorization.

## Outputs

1. Opportunity-to-mechanism map linking every concept to evidence.
2. Concept portfolio with expected benefit, tradeoff, dependency, and confidence.
3. Testable product specification using measurable targets and tolerances where justified.
4. Validation experiment for each critical hypothesis, including sample, method, threshold, and kill criterion.
5. Open-risk list for design patent, supplier, certification, cost, and user validation.

The output may be Markdown, JSON, or a structured table. It is complete only when every recommended feature has a source, a mechanism, a measurable requirement, and a test. It does not create CAD or assert manufacturability.

## Workflow

1. Normalize the evidence into problem statements with source, segment, frequency, severity, and context.
2. Remove feature requests that do not reveal an underlying job or failure mode.
3. Map each high-value problem to one or more physical or service mechanisms.
4. Screen mechanisms against target price, complexity, size, weight, compatibility, and likely failure modes.
5. Write measurable specifications; separate required, target, and stretch values.
6. Create the cheapest experiment capable of disproving each critical hypothesis.
7. Define kill criteria before prototype results are known.
8. Route unresolved design-right, supplier, and economic questions to the corresponding Skills.

## Example

Observed evidence: repeated complaints that a phone mount slips on rough roads and is difficult to release one-handed. A valid concept does not stop at "stronger magnet." It identifies the retention and release mechanisms, target vibration test, compatible phone mass range, release force, thermal condition, cost effect, and a failure threshold.

## Error handling and stopping conditions

- No traceable evidence: do not present brainstorming as validated differentiation.
- Conflicting segments: separate concepts instead of averaging incompatible needs.
- Missing constraints: label cost and manufacturing feasibility unresolved.
- Safety or compliance implication: require the relevant specialist review before recommending launch.
- Patent-sensitive appearance: route to design-patent pre-screening before freezing geometry.

## Validation and definition of done

- Every concept maps to at least one evidence item.
- Every critical specification has a unit or observable acceptance condition.
- Every critical hypothesis has a test and predeclared kill criterion.
- Risks that require patent, supplier, certification, or financial evidence remain explicit.

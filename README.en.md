# Amazon product research suite

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

## Installation and use

Download or clone the repository and copy the indicated skill directory, including its existing references, scripts, assets and other dependencies, into your host's skill directory. Keep its name and SKILL.md. Changing the documentation language does not require another installation. Commands are installation options, not evidence of installation or activation.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## Evidence-led product differentiation

`amazon-product-differentiation-rd`

Turn customer pain into product mechanisms, measurable specifications, low-cost experiments and predefined kill criteria.

Skill directory: `skills/amazon-product-differentiation-rd`

**Implementation Basis and Dependencies**

Traceable customer evidence, a product baseline and target user/job. Business constraints are needed for feasibility; prototypes and specialist patent/supplier review are conditional. Supplied evidence needs no live service.

**Inputs**

Required: review/interview/return evidence, baseline images/specification and primary user job. Conditional: price, cost, size, materials, fitment, MOQ and compliance. Label proposed success thresholds as assumptions.

**Outputs**

Evidence-to-mechanism map, concept portfolio, measurable specifications, experiment protocols and unresolved risks in Markdown/JSON/tables. Every recommendation needs evidence, mechanism, requirement and test.

[Workflow · Boundaries and stopping conditions · Example request](skills/amazon-product-differentiation-rd/references/i18n/en.md)

> Use `$amazon-product-differentiation-rd` — For slipping mounts, specify retention, release force, phone-mass range, vibration and thermal tests rather than merely asking for a stronger magnet; respond in English and preserve evidence, unknowns and action boundaries.

## Amazon product research suite

`amazon-product-research-suite`

Route a decision spanning at least two research domains to the smallest sufficient set of specialist Skills; a narrow task goes directly to its specialist.

Skill directory: `skills/amazon-product-research-suite`

**Implementation Basis and Dependencies**

An Agent Skills host and the selected installed specialists. Supplied evidence can support offline work; live collection requires network and permission. Python 3.10+ is optional for bundled installers and validators.

**Inputs**

Required: product decision. Conditional: ASIN or product identity, marketplace, jurisdiction, evidence window and action permissions. Optional: CSV/JSON/XLSX/PDF/images, quotes and business constraints; missing facts remain gaps.

**Outputs**

route-plan.json, shared evidence contract, selected Skills and order, missing-input list and artifact destinations. Routing itself neither installs packages nor contacts services.

[Workflow · Boundaries and stopping conditions · Example request](skills/amazon-product-research-suite/references/i18n/en.md)

> Use `$amazon-product-research-suite` — Evaluate a car phone mount across market, reviews, differentiation, supplier feasibility and unit economics, adding patent review when visuals exist; respond in English and preserve evidence, unknowns and action boundaries.

## Supplier feasibility and sample gates

`amazon-supplier-feasibility`

Prepare an RFQ, normalize supplier quotes and define evidence-based sample acceptance without default outreach or ordering.

Skill directory: `skills/amazon-supplier-feasibility`

**Implementation Basis and Dependencies**

A product specification; comparable dated quotes for supplier comparison. Compliance scope, sample access and communication permissions are conditional. Contacting a factory requires separate authorization.

**Inputs**

Specification or drawing with units/tolerances; order/demand assumptions; conditional currency, Incoterm, tooling budget and payment terms; optional PDF/XLSX/CSV quotes and quality evidence.

**Outputs**

RFQ package, normalized cost/lead-time comparison, manufacturing-risk register and sample plan. Status: READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL or INSUFFICIENT_EVIDENCE.

[Workflow · Boundaries and stopping conditions · Example request](skills/amazon-supplier-feasibility/references/i18n/en.md)

> Use `$amazon-supplier-feasibility` — Compare phone-mount quotes only after aligning magnet grade, adhesive, torque, temperature tests, tooling ownership and packaging; respond in English and preserve evidence, unknowns and action boundaries.

## Unit economics and first-order cash

`amazon-unit-economics-cashflow`

Model product contribution, break-even advertising, return sensitivity and initial cash requirements from explicit assumptions.

Skill directory: `skills/amazon-unit-economics-cashflow`

**Implementation Basis and Dependencies**

Numeric price/cost assumptions and a documented marketplace-fee basis. Python 3.10+ runs the standard-library calculator. Cash analysis additionally requires order quantities and payment timing.

**Inputs**

JSON: selling price, referral and fulfillment fees, landed cost, return rate/loss, advertising ACOS and other variable cost. Cash inputs add units, tooling, setup, deposit and buffer. Use one currency and decimal rates from 0 to 1.

**Outputs**

JSON or selected file with contribution profit/margin, break-even ACOS, expected returns, first-order cash and scenarios. Invalid inputs return nonzero; no network or account changes.

[Workflow · Boundaries and stopping conditions · Example request](skills/amazon-unit-economics-cashflow/references/i18n/en.md)

> Use `$amazon-unit-economics-cashflow` — Model a phone mount with user-supplied price and costs; compare return/ACOS scenarios and report both contribution and first-order cash; respond in English and preserve evidence, unknowns and action boundaries.

## Language coverage and validation

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.

Before delivery reconcile inputs, evidence, missing values, files and the original completion criteria. Mark unexecuted steps unverified; a successful script exit is not business validation.

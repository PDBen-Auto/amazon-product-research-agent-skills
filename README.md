# Amazon Product Research Agent Skills

Turn Amazon market, review, product, supplier, and cost evidence into an auditable prototype or Go/No-Go decision.

[![Release](https://img.shields.io/github/v/release/PDBen-Auto/amazon-product-research-agent-skills?style=flat-square)](https://github.com/PDBen-Auto/amazon-product-research-agent-skills/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/PDBen-Auto/amazon-product-research-agent-skills/total?style=flat-square)](https://github.com/PDBen-Auto/amazon-product-research-agent-skills/releases)
[![Validate](https://img.shields.io/github/actions/workflow/status/PDBen-Auto/amazon-product-research-agent-skills/validate.yml?branch=main&style=flat-square&label=validate)](https://github.com/PDBen-Auto/amazon-product-research-agent-skills/actions/workflows/validate.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-source--available-59636e?style=flat-square)](LICENSE)

**One router, seven specialist Agent Skills, one evidence contract, and one decision path.** Use a specialist for a narrow task or the suite router when a product question crosses market size, customer pain, differentiation, design risk, suppliers, economics, and stage gates.

[Download the latest ZIP](https://github.com/PDBen-Auto/amazon-product-research-agent-skills/releases/latest/download/amazon-product-research-agent-skills-v0.1.1.zip) · [Read in Chinese](README.zh-CN.md) · [Open the live HTML example](https://pdben-auto.github.io/amazon-product-research-agent-skills/examples/magnetic-car-phone-mount/decision-report.html)

![Illustrative Amazon product decision report](examples/magnetic-car-phone-mount/preview.png)

> The screenshot is generated from public illustrative fixtures. It demonstrates the workflow and artifact contract, not current Amazon market facts.

## What problem this solves

Most Amazon research workflows stop at one evidence type. Market tools show demand, review analysis shows pain, and cost sheets show margin, but a product manager still has to decide whether the same product is differentiated, manufacturable, economically viable, and ready for the next investment gate.

This suite connects those jobs without hiding uncertainty:

```text
market boundary -> customer evidence -> differentiated specification
  -> design/IP pre-screen -> supplier feasibility -> unit economics and cash
  -> prototype or Go/No-Go decision
```

## Install in under a minute

Install the cross-functional router:

```bash
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-product-research-suite
```

Verify the repository exposes all four bundled Skills:

```bash
npx skills add PDBen-Auto/amazon-product-research-agent-skills --list
```

Then ask:

```text
Use $amazon-product-research-suite to evaluate this Amazon US product.
Route only the work that can change the decision, list missing evidence,
and return the artifact plan before any live collection.
```

The router itself requires no Amazon login, Seller Central account, API key, or private service. Individual live-data Skills may require public network access, authorized exports, or tools stated in their own documentation. The official `skills` CLI reports anonymous aggregate installation telemetry to power the [skills.sh leaderboard](https://www.skills.sh/docs/faq); set `DISABLE_TELEMETRY=1` to opt out.

## Choose the smallest Skill

| Product question | Installable Skill | Decision-ready output |
| --- | --- | --- |
| Which research modules should run, and in what order? | [`amazon-product-research-suite`](skills/amazon-product-research-suite/SKILL.md) | Route plan, missing evidence, execution order, shared evidence contract |
| Which products define the direct market? | [`sellersprite-bi-market-research`](https://github.com/PDBen-Auto/sellersprite-amazon-market-research-bi-skill) | Candidate manifest, relevance decisions, parent-ASIN deduplication, coverage-gated BI HTML |
| What do customers repeatedly complain about? | [`amazon-review-scraper`](https://github.com/PDBen-Auto/amazon-review-intelligence-skill) | Written-review evidence, canonical JSON, Excel workbook, offline VOC HTML |
| What differentiated product should we build and test? | [`amazon-product-differentiation-rd`](skills/amazon-product-differentiation-rd/SKILL.md) | Evidence-to-mechanism map, measurable specification, experiments, kill criteria |
| Is the proposed appearance too close to an existing design right? | [`design-patent-search-and-design-around`](https://github.com/PDBen-Auto/design-patent-design-around-skill) | Search log, drawing review, risk split, structurally distinct design-around directions |
| Can suppliers make it at the required MOQ, quality, and lead time? | [`amazon-supplier-feasibility`](skills/amazon-supplier-feasibility/SKILL.md) | RFQ, normalized quotes, manufacturing-risk register, sample gates |
| Can it make money and how much first-order cash is required? | [`amazon-unit-economics-cashflow`](skills/amazon-unit-economics-cashflow/SKILL.md) | Contribution margin, break-even ACOS, return sensitivity, first-order cash |
| Should the team prototype, invest, or stop? | [`amazon-product-decision-gateway`](https://github.com/PDBen-Auto/amazon-product-decision-suite) | Evidence contract, stage-gate status, formal decision handoff |

Install any bundled specialist directly:

```bash
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-product-differentiation-rd
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-supplier-feasibility
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-unit-economics-cashflow
```

## What makes it different

- **Decision-first routing**: narrow tasks use one specialist; cross-functional work uses only modules that can change the decision.
- **Evidence that survives handoffs**: shared JSON contracts preserve source, date, scope, observation, calculation, inference, assumption, coverage, and confidence.
- **R&D that can fail usefully**: customer pain becomes a mechanism, measurable specification, experiment, and predeclared kill criterion.
- **Supplier feasibility before inventory**: RFQs normalize MOQ, tooling, quote basis, lead time, quality evidence, and sample gates instead of ranking factories by unit price alone.
- **Profit and cash are separate**: the deterministic calculator distinguishes contribution margin from the cash required to fund the first order.
- **Honest stopping behavior**: CAPTCHA, stale exports, missing fees, legal uncertainty, and absent supplier evidence become explicit blockers.
- **No hidden tracking in the repository installer**: `scripts/install_suite.py` has no telemetry, callbacks, credential collection, hidden prompts, or backdoors. The optional official `skills` CLI has documented anonymous install telemetry and an opt-out.

## Reproducible example

The magnetic car phone mount fixture includes:

- a scoped product brief;
- a validated cross-Skill route plan;
- a source-indexed evidence bundle;
- base and downside unit-economics scenarios;
- a self-contained offline HTML decision report;
- hard gates for supplier quotes and design-patent pre-screening.

Reproduce it with Python 3.10+ and no third-party packages:

```bash
python scripts/validate_artifact.py route-plan examples/magnetic-car-phone-mount/route-plan.json
python scripts/validate_artifact.py evidence-bundle examples/magnetic-car-phone-mount/evidence-bundle.json
python skills/amazon-unit-economics-cashflow/scripts/unit_economics.py \
  examples/magnetic-car-phone-mount/input/unit-economics-assumptions.json \
  --output examples/magnetic-car-phone-mount/unit-economics.json --pretty
```

## Pinned suite installer

The optional Python installer downloads exact catalog references rather than moving `main` branches. Existing local Skill directories are preserved unless `--force` is explicitly supplied.

```bash
python scripts/install_suite.py --list
python scripts/install_suite.py --dry-run
python scripts/install_suite.py --skill unit-economics-cashflow
python scripts/install_suite.py --check
```

## Inputs and outputs

The router accepts a product decision plus available ASINs, URLs, images, exports, patent identifiers, quotes, cost assumptions, marketplace, jurisdiction, and authorization limits. It reports missing or conflicting inputs before execution.

Cross-Skill work uses:

- [`route-plan.schema.json`](skills/amazon-product-research-suite/references/route-plan.schema.json) for routing, blockers, order, and expected artifacts;
- [`evidence-bundle.schema.json`](skills/amazon-product-research-suite/references/evidence-bundle.schema.json) for source-indexed claims and assumptions;
- `scripts/validate_artifact.py` for zero-dependency structural checks.

No Skill in this suite claims to provide legal advice, certification approval, Amazon settlement data, guaranteed supplier performance, or a guaranteed market result.

## Supported clients

The repository follows the common multi-Skill layout: `skills/<skill-name>/SKILL.md` with optional `agents/openai.yaml`, scripts, references, and assets inside each Skill directory. It is designed for Codex and compatible clients that discover Agent Skills. `npx skills add` is the primary public discovery and installation path for this repository.

## Validation

```bash
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python -m compileall -q scripts skills
npx skills add . --list
```

GitHub Actions runs the same catalog, artifact, installer, test, and compile checks on every push and pull request.

## Security, privacy, and licensing

Do not commit Amazon cookies, private exports, supplier contacts, customer data, API tokens, signing keys, or private engine URLs. The public suite contains reusable workflows, schemas, examples, and deterministic calculations; private scoring weights and proprietary thresholds remain outside the repository.

This catalog is source-available. Each linked specialist repository defines its own license and public/private boundary. Review [LICENSE](LICENSE) before redistribution or commercial embedding.

## Search terms

Amazon product research, Amazon FBA product validation, Amazon review scraper, Amazon VOC, SellerSprite BI, design patent search, design-around, product differentiation, supplier RFQ, unit economics, break-even ACOS, inventory cash flow, Go/No-Go decision, ecommerce Agent Skills, Codex Skill.

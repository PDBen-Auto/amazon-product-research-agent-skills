# Amazon Product Research Agent Skills

Research and decision skills for Amazon product teams: market scope, review intelligence, design-patent pre-screening, supplier feasibility, and Go/No-Go decisions.

[![Install](https://img.shields.io/badge/install-npx%20skills%20add-111111?style=flat-square)](#install)
[![Codex](https://img.shields.io/badge/Codex-Agent%20Skill-111111?style=flat-square)](https://developers.openai.com/codex/skills)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-source--available-59636e?style=flat-square)](LICENSE)

> One entry point for Amazon product research workflows. Pick the smallest skill that answers the question, or use the suite router when the work crosses market, customer, design, supply chain, and finance evidence.

## 5-minute quick start

### Option A: install the router

```bash
npx skills add PDBen-Auto/amazon-product-research-agent-skills --skill amazon-product-research-suite
```

Then ask your agent:

```text
Use $amazon-product-research-suite. I am evaluating a new Amazon US product.
Route this request to the right skills, state which evidence is missing, and
return a short execution plan before running anything.
```

### Option B: install the individual skills

```bash
npx skills add PDBen-Auto/amazon-review-intelligence-skill
npx skills add PDBen-Auto/design-patent-design-around-skill --skill design-patent-search-and-design-around
npx skills add PDBen-Auto/sellersprite-amazon-market-research-bi-skill --skill sellersprite-bi-market-research
npx skills add PDBen-Auto/amazon-product-decision-suite --skill amazon-product-decision-gateway
```

### Option C: install the suite from a clean machine

```bash
python scripts/install_suite.py --target "$HOME/.codex/skills"
```

The installer downloads public GitHub archives, shows the exact destination, and never asks for Amazon credentials. Use `--dry-run` to inspect the plan first.

## Choose the right skill

| Product question | Skill | What it returns |
| --- | --- | --- |
| What are customers complaining about, and what should we change? | [Amazon Review Intelligence](https://github.com/PDBen-Auto/amazon-review-intelligence-skill) | Evidence-preserving written reviews, canonical JSON, Excel, offline HTML VOC report, product hypotheses |
| Is a product visually close to an existing design right, and how can we redesign it? | [Design Patent Search and Design-around](https://github.com/PDBen-Auto/design-patent-design-around-skill) | Search log, official drawing review, risk split, structurally distinct redesign directions, sample gates |
| What is the direct market, who is actually comparable, and what is the auditable revenue boundary? | [SellerSprite Market Research BI](https://github.com/PDBen-Auto/sellersprite-amazon-market-research-bi-skill) | Candidate manifest, relevance decisions, parent-ASIN deduplication, coverage gates, offline BI dashboard |
| Should we invest, prototype, source, or stop? | [Amazon Product Decision Gateway](https://github.com/PDBen-Auto/amazon-product-decision-suite) | Evidence contract, stage-gate status, GO / CONDITIONAL_GO / NO_GO / INSUFFICIENT_EVIDENCE handoff |

## Why this suite exists

Most product research tools stop at one evidence type. Market BI can show demand, review analysis can show pain, and patent search can show risk, but none of those facts alone answer whether a specific product is manufacturable, economically viable, and worth funding.

This suite provides an explicit handoff between those jobs:

```text
market boundary -> customer evidence -> design/IP risk -> supplier feasibility
       -> unit economics and cash -> stage-gated product decision
```

The suite is not a replacement for a specialist tool. It is an entry point that makes the specialist tools discoverable, composable, and auditable.

## What makes it different

- **Task-first routing**: start with the decision you need, not a large toolbox.
- **Evidence contracts**: preserve source, date, scope, calculation, inference, and assumption separately.
- **Decision-ready artifacts**: JSON, XLSX, HTML, search logs, candidate manifests, and signed handoff records can be reviewed outside the agent.
- **Hard-stop handling**: CAPTCHA, missing data, legal uncertainty, unsupported marketplace, and critical cost gaps become explicit blockers instead of invented certainty.
- **Public/private boundary**: public skills contain reusable workflows and validation; private engines, customer data, credentials, scoring weights, and internal thresholds stay outside the repository.
- **Cross-platform install**: the individual repositories work with Codex and compatible Agent Skills clients; the router documents the shared contract.

## Typical workflow

1. Define the product task, marketplace, time window, and decision deadline.
2. Route market, review, patent, and supply-chain questions to the relevant skill.
3. Preserve raw evidence and mark whether each statement is observed, calculated, modeled, inferred, or assumed.
4. Convert recurring customer pain into a product mechanism, specification, validation experiment, and kill criterion.
5. Re-check design/IP collisions and supplier constraints before committing to tooling or inventory.
6. Submit a sanitized evidence bundle to the decision gateway when a formal Go/No-Go result is required.

## Inputs and outputs

The router accepts a plain-language product question plus any available product URLs, ASINs, images, review exports, SellerSprite files, patent identifiers, supplier quotes, cost assumptions, and business constraints. It reports missing or conflicting inputs before execution.

The selected skill returns one or more of the following:

- a source-indexed evidence table;
- a normalized data file or manifest;
- an offline HTML or Excel report;
- product requirements and validation experiments;
- supplier questions and sample acceptance gates;
- a signed or hash-bound decision handoff.

No skill in this suite claims to provide legal advice, Amazon settlement data, certification approval, or a guaranteed market outcome.

## Supported clients

The package follows the common Agent Skills layout (`SKILL.md`, optional `agents/openai.yaml`, scripts, and references). It is designed for Codex and compatible clients that discover `SKILL.md` directories. The exact install command may differ by client; the individual repositories document Codex, Claude Code, Cursor, Gemini CLI, GitHub Copilot, Cline, OpenCode, and `skills.sh` paths where supported.

## Repository map

```text
amazon-product-research-agent-skills/
├── SKILL.md                         # suite router skill
├── agents/openai.yaml               # Codex display metadata
├── catalog/skills.json              # machine-readable catalog
├── scripts/install_suite.py         # explicit public-archive installer
├── scripts/validate_catalog.py      # deterministic catalog check
├── examples/quickstart.md           # smallest useful request examples
└── docs/distribution-playbook.md    # discoverability and release guidance
```

## Security and privacy

The installer has no telemetry and does not add hidden tracking, backdoors, prompt-obfuscation logic, or credential collection. Do not commit Amazon cookies, SellerSprite exports containing private data, supplier contacts, customer reviews, private engine URLs, API tokens, or signing keys.

## Search terms

Amazon product research, Amazon FBA product validation, Amazon review scraper, Amazon VOC, Amazon market research, SellerSprite BI, design patent search, design-around, product opportunity analysis, supplier feasibility, unit economics, Go/No-Go decision, product manager agent skill, ecommerce research automation, Agent Skills.

## Contributing

Start with a reproducible fixture, state the source and date, show the expected artifact, and include a failure case. Read the contributing and licensing policy in each individual repository before opening a change.

## License

This catalog is source-available. Each linked skill repository defines its own license and public/private boundary.

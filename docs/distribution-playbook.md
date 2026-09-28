# Distribution playbook

The suite is designed to improve discovery without claiming artificial popularity.

## What to publish first

1. Publish this suite repository as the single entry point.
2. Keep the four specialist repositories independently installable.
3. Add one five-minute example and one output screenshot to each specialist README.
4. Create a release only when the package contents or validation behavior changes.
5. Submit directory and awesome-list pull requests only after the public repository is stable.

## GitHub metadata

Use a short description that states the result, not the implementation:

```text
Amazon product research Agent Skills: market sizing, review intelligence, design-patent pre-screening, supplier feasibility, and Go/No-Go decisions.
```

Suggested topics:

```text
agent-skills, amazon, amazon-fba, ecommerce, product-research, product-validation,
voice-of-customer, amazon-reviews, sellersprite, design-patent, design-around,
unit-economics, supply-chain, go-no-go, codex-skill
```

## Repeatable growth mechanics

- Put a clear one-sentence job above the fold.
- Make installation copyable and document more than one Agent client.
- Use a collection or entry point when several skills serve one job family.
- Show a concrete fixture or output before long theory.
- State what is free, what needs credentials, and what is out of scope.
- Release only reproducible, installable artifacts; downloads follow successful adoption.

## Metrics to monitor

Track weekly:

- GitHub views and unique visitors, which require repository admin access;
- referrers and search terms, which require repository admin access;
- Stars, forks, watchers, issues, and discussions;
- Release asset downloads by version;
- install command clicks and failed install reports;
- which specialist skill users select from the suite.

Do not treat Stars as downloads. Do not claim GitHub Traffic numbers when the API token cannot read them.

## Public/private boundary

Never publish private prompts, customer data, credentials, hidden telemetry, prompt-obfuscation logic, signing private keys, or proprietary thresholds. Use public signatures and manifests when provenance is needed; they should identify a release without changing how the skill behaves.

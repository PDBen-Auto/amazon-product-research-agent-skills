# Distribution playbook

The suite is designed to improve discovery without claiming artificial popularity.

## What to publish first

1. Publish this suite repository as the single entry point.
2. Keep the four specialist repositories independently installable.
3. Add one five-minute example and one output screenshot to each specialist README.
4. Create a release only when the package contents or validation behavior changes.
5. Link focused Skills to a reproducible next-step case where the user has a clear decision to make. Submit directory or community contributions only where the destination accepts them, with author identity disclosed.

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
- Give review-intelligence readers a direct path to the synthetic unit-economics case and a single-Skill install command. Label separate fixtures clearly; do not imply that one case's reviews produced another case's financial inputs.
- skills.sh listing follows genuine `skills add` installs; do not self-install to manufacture discovery or installation counts. Use telemetry-disabled local tests only for compatibility checks.

## Metrics to monitor

Track weekly:

- GitHub views and unique visitors, which require repository admin access;
- referrers and search terms, which require repository admin access;
- Stars, forks, watchers, issues, and discussions;
- Release asset downloads by version;
- install command clicks and failed install reports;
- which specialist skill users select from the suite.

At each weekly review, compare the latest value with the previous snapshot and the October 22 baseline. GitHub Traffic is a rolling 14-day window: do not sum unique visitors across snapshots. Record unavailable or permission-denied metrics as unknown, not zero. Release ZIP downloads are not verified external installs. Require a real install signal, user report, or sourced referral before attributing adoption to a channel.

Use one weekly decision: keep an entry path when it brings attributable installs or substantive feedback; revise its headline or landing path when it attracts visitors without action; stop investing in it after two observable weeks without a useful signal. Check CI, Pages, and install instructions immediately after any repository change rather than waiting for the next review. Do not change licensing, add tracking, or publish new Skills without explicit approval.

Do not treat Stars as downloads. Do not claim GitHub Traffic numbers when the API token cannot read them.

## Public/private boundary

Never publish private prompts, customer data, credentials, hidden telemetry, prompt-obfuscation logic, signing private keys, or proprietary thresholds. Use public signatures and manifests when provenance is needed; they should identify a release without changing how the skill behaves.

# Magnetic car phone mount example

This is a reproducible **illustrative fixture**, not current Amazon market research. It demonstrates how the suite routes a cross-functional product question, preserves evidence types, calculates unit economics, and stops at unresolved supplier and design-right gates.

## Reproduce

```bash
python ../../scripts/validate_artifact.py route-plan route-plan.json
python ../../scripts/validate_artifact.py evidence-bundle evidence-bundle.json
python ../../skills/amazon-unit-economics-cashflow/scripts/unit_economics.py \
  input/unit-economics-assumptions.json --output unit-economics.json --pretty
```

Open `decision-report.html` directly in a browser. No server, account, or external asset is required.

## Result

The fixture returns `CONDITIONAL_GO_FOR_SAMPLE`: the concept is worth a controlled supplier sample only after current fees are verified, supplier quotes are normalized, and the selected geometry receives design-patent pre-screening.

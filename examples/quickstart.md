# Quickstart examples

## Review-first question

```text
Use $amazon-product-research-suite for Amazon US ASIN B0XXXXXX.
I need recurring complaints, the strongest positive drivers, and three product
changes that can be tested. Do not claim complete review coverage.
```

Route to `amazon-review-intelligence`. Required inputs: ASIN or an authorized review export, marketplace, and collection date.

## Market-first question

```text
Use $amazon-product-research-suite to define the direct market for a compact
AI voice recorder on Amazon US. Separate direct products, adjacent substitutes,
and noise before calculating revenue share.
```

Route to `sellersprite-bi-market-research`. Required inputs: seed keyword, competitor ASINs, SellerSprite exports, and the definition of the customer job.

## Design-risk question

```text
Use $amazon-product-research-suite to pre-screen these product images for US
design-right risk and produce three structurally distinct design-around directions.
This is a pre-screen, not legal advice.
```

Route to `design-patent-search-and-design-around`. Required inputs: product images or URL, jurisdiction, cutoff date, and non-negotiable function or cost constraints.

## Full decision question

```text
Use $amazon-product-research-suite to plan a Go/No-Go review for this Amazon
FBA product. Combine direct-market evidence, customer pain, design-risk notes,
supplier quotes, target contribution margin, and first-order cash limits.
```

Route to market -> review -> design -> supplier/economics -> decision gateway. The gateway requires a sanitized evidence bundle and a configured private engine for an official result.

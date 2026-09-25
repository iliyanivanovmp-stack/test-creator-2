# Instant Hydration CRO Collection Manifest

## Brand Info

- Store name: Instant Hydration
- Store URL: https://instanthydration.com
- PDP URL (Meta ad landing, confirmed): https://instanthydration.com/products/premium-electrolyte-drink-mix
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (variation vs. control)
- Areas of focus: No collection page. The Energy+ product page (https://instanthydration.com/products/energy-electrolyte-drink-mix) replaces the collection page as the third most important page after PDP and homepage. All three Meta ads land on the same PDP, so only one set of landing screenshots (3 folds) exists.
- Constraint: never read or modify `brands/instant-hydration---ooold` (prior audit, untouched).

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency (screenshots)
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, energy page as collection, cart)
- Social & Community Research (automatic)

## Sources Collected

- Meta Ads → raw/meta-ads.md, raw/meta-ads-visual-summary.md
- Google Ads → screenshots in folder, raw/google-ads-visual-summary.md
- Reviews & UGC → raw/reviews.md
- PageSpeed → raw/pagespeed.md, raw/instant-hydration-homepage-pagespeed.json, raw/instant-hydration-pdp-pagespeed.json
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via /last30days-ecom, Engine mode) → raw/last30days-ecom.md
- Screenshot aliases mapped:
  - ad-creative-1/2/3.png used as meta-ad-1/2/3
  - `ad1,2,3, pdp - landing-f1/f2/f3.png` used as shared landing folds for all three Meta ads
  - google-ads-1.png, google-ads-2.png used as Google Ads screenshots
  - energy-page-collections-f1/f2/f3.png used as collection-f1/f2/f3
  - cart-drawer.png used as cart

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1,2,3, pdp - landing-f1.png, -f2.png, -f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- energy-page-collections-f1.png, -f2.png, -f3.png
- cart-drawer.png

## Sources Skipped

- Competitor Insights (none provided; research during audit)
- Inspiration Sites
- Email Campaigns
- Non-Data Context
- Social sources skipped by precheck: Reddit (no brand results), X (no brand results), Pinterest (only unrelated skincare/hair results)

## Missing Data Warnings

- No separate PDP fold screenshots (PDP is covered by the shared Meta landing folds).
- No mobile screenshots. All captures are desktop viewport.
- Energy page PageSpeed JSON not collected (homepage and PDP only).

## Open Questions

- Capture date, shopper geo and default variant are inferred from file dates and visible content, not confirmed by user.
- Cart capture: line items total $99.00 while subtotal reads $55.00. Cause not determined.
- Ad 1 (cotton candy) and Ad 3 (P.O.G.) flavors not visible in captured PDP folds. Confirm whether they appear lower in the flavor scroller.
- Ad 1 references "Summer Sale" and Ad 2 "Spring", while the site bar shows Crisp Apple 50% OFF. Confirm which offers are currently live.
- Reviews were provided as a pasted text block, 25 entries, mostly Premium Electrolyte Drink Mix flavors; no star ratings included in the paste.

## Audit

- instant-hydration-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

# Instant Hydration CRO Collection Manifest

## Brand Info

- Store name: Instant Hydration
- Store URL: instanthydration.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (1 variation vs. control)
- Areas of focus: Meta ads almost all land on the same page — https://instanthydration.com/products/icee-electrolyte-drink-mix — noted as an important page. This URL doubles as the "landing page" the ad-landing screenshots (ad1,2,3-landing-f1/f2/f3.png) depict.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection)
- Reviews & UGC

## Sources Collected

- Meta Ads → screenshots in folder → raw/meta-ads-visual-summary.md
- Google Ads → screenshots in folder → raw/google-ads-visual-summary.md
- Site Screenshots (homepage, collection, cart) → raw/site-visual-summary.md
- PageSpeed → raw/pagespeed.md (from raw/instanthydration-homepage-pagespeed.json and raw/instanthydration-importnantpage-pafespeed.json)
- Reviews & UGC → raw/reviews.md (45 reviews, mix of standard verified purchases and Amazon Vine reviews)
- Screenshot aliases mapped:
  - ad-creative-1.png, ad-creative-2.png, ad-creative-3.png → meta-ad-1/2/3.png (creative slot)
  - ad1,2,3-landing-f1.png, ad1,2,3-landing-f2.png, ad1,2,3-landing-f3.png → shared landing page folds 1-3, used as the landing page for Ad 1, Ad 2, and Ad 3 alike (all three ads point to the same page)
  - cart-drawer.png → cart.png slot
  - collections-f1.png, collections-f2.png → collection-f1/f2.png slot (no f3 provided)
  - google-ads-1.png, google-ads-2.png → google-ads screenshot slot
  - homepage-f1/f2/f3.png → homepage slot (canonical, no mapping needed)

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1,2,3-landing-f1.png
- ad1,2,3-landing-f2.png
- ad1,2,3-landing-f3.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- google-ads-1.png
- google-ads-2.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context

## Missing Data Warnings

- MISSING_DATA: pdp_screenshots — no dedicated PDP screenshots collected. The shared ad-landing screenshots (ad1,2,3-landing-f1/f2/f3.png) point at the product page (https://instanthydration.com/products/icee-electrolyte-drink-mix) and are the closest available substitute, but a full PDP fold-by-fold capture (buy box detail, upsell mechanics) is not available.
- MISSING_DATA: pdp_page_screenshots (site-visual-summary PDP section) — none collected, PDP section omitted from site visual summary.

## Open Questions

- Confirm whether ad1,2,3-landing-f1/f2/f3.png is in fact the same URL as https://instanthydration.com/products/icee-electrolyte-drink-mix, or a distinct landing page that also happens to receive all three ads.
- instanthydration-importnantpage-pafespeed.json filename suggests this is the PageSpeed run for the "important page" (likely the same PDP/landing URL) — confirm during audit.

## Audit

- instant-hydration-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

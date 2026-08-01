# Voss Helmets CRO Collection Manifest

## Brand Info

- Store name: Voss Helmets
- Store URL: https://voss-helmets.com/
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: Homepage is highest-traffic page (2 of 3 Meta ads land there). Homepage CTA routes to VOSS 991 Gloss Gold Hollywood PDP (newest product). PDP performance is critical.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)

## Sources Collected

- Non-Data Context → raw/context.md
- Meta Ads (URLs + notes) → raw/meta-ads.md
- Meta Ads (visual summary) → raw/meta-ads-visual-summary.md
- Google Ads (visual summary) → raw/google-ads-visual-summary.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md (raw JSON: data-collection/voss-helmets-homepage-pagespeed.json, data-collection/voss-helmets-pdp-pagespeed.json)
- Site Screenshots (visual summary) → raw/site-visual-summary.md
- Screenshot aliases mapped:
  - collections-f1.png, collections-f2.png, collections-f3.png used as collection-f1/f2/f3
  - cart-drawer.png used as cart
  - google-ads-1.png used as google-ads
  - ad2-landing-f1.png, ad2-landing-f2.png used as meta-ad-2-lp-f1/f2

## Screenshots Present

(from data-collection/screenshots/)
- ad2-landing-f1.png
- ad2-landing-f2.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- google-ads-1.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png
- pdp-f1.png
- pdp-f2.png
- pdp-f3.png

## Sources Skipped

- Competitor Insights (not provided)
- Inspiration Sites (not provided)
- Email Campaigns (not provided)

## Missing Data Warnings

- Meta Ad Creatives → screenshots in data-collection/screenshots/ (ad-creative-1.png, ad-creative-2.png, ad-creative-3.png)
- Reviews → raw/reviews.md
- MISSING_DATA: meta_ad_2_lp_f3 — Ad 2 landing page fold 3 not collected (only f1 and f2 present).

## Open Questions

- User stated collection page has "only 2 folds" but 3 screenshot files were provided (collections-f1/f2/f3). Collections-f3 shows the bottom of what appears to be page 2 of the collection pagination (pages 1, 2, 3 visible). Treated as a valid third fold and summarized accordingly. Confirm if this was intentional or if collections-f3 should be excluded.
- Ad 3 creative and any specific landing page context not confirmed beyond "lands on homepage." If Ad 3 promotes a different product or angle than Ad 1, that context would affect analysis.
- Ad creative 1 (ad-creative-1.png) shows the Voss 601 D2 Dual Sport and references that product in the display URL — but user stated ads 1 and 3 land on the homepage, which heroes the 991 Hollywood. Confirm: does creative 1 actually link to the homepage, or to the 601 D2 PDP?
- Ad creative 3 (ad-creative-3.png) promotes a $219.99 helmet. No product at that price was found on the homepage. Confirm: does creative 3 link to the homepage, or to a specific product page? If homepage, this is a significant message match gap.

## Audit

- voss-helmets-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

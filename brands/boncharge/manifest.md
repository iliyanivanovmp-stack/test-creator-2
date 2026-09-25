# Bon Charge CRO Collection Manifest

## Brand Info

- Store name: Bon Charge
- Store URL: https://boncharge.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: None specified beyond the flagged data note that Ad 3 lands directly on the PDP (Red Light Face Mask) rather than a separate landing page

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, cart)
- Social & Community Research (automatic, always runs)

## Sources Collected

- Meta Ads (URLs) → raw/meta-ads.md
- Meta Ads (visual) → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Reviews → raw/reviews.md
- PageSpeed → raw/pagespeed.md (real Lighthouse JSON data: raw/homepage-pagespeed-boncharge.json, raw/boncharge-pdp-pagespeed.json)
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Screenshots present in folder → 20 files (see below)
- Screenshot aliases mapped: ad-creative-N.png used as meta ad creative N; adN-landing-fM.png used as meta ad N landing page fold M; cart-drawer.png used as cart canonical slot; google-ads-1.png/google-ads-2.png used as google-ads canonical slot; homepage-fN.png and collections-fN.png used as their canonical slots

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png, ad3-landing-f3.png
- cart-drawer.png
- collections-f1.png, collections-f2.png, collections-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png

## Sources Skipped

- Competitor Insights (not provided)
- Inspiration Sites (not provided)
- Email Campaigns (not provided)
- Non-Data Context (not provided)

## Missing Data Warnings

- No dedicated PDP screenshots exist as a separate source. Per user instruction, Ad 3's landing page IS the PDP (Red Light Face Mask) — its three folds (ad3-landing-f1/f2/f3.png) were used as the only PDP evidence and documented as such in raw/site-visual-summary.md.

## Open Questions

- Ad 2's fold 3 screenshot (ad2-landing-f3.png) displays the Tortoise Shell Computer Glasses page instead of the Crystal Computer Glasses page shown in its folds 1-2. This may be a screenshot capture mix-up rather than actual site behavior — flagged in raw/meta-ads-visual-summary.md, not diagnosed as a CRO finding.
- The cart drawer's upsell line item ("Red Light Neck and Chest Mask") displays its sale price in USD ($356.21) while every other price in the cart displays in EUR (€) — flagged in raw/site-visual-summary.md.
- Trustpilot rating is inconsistent across sources: the last30days engine's automated pull for boncharge.com showed TrustScore 2.4 (6 reviews, 2026-09-11), while a manual WebSearch pass reported the legacy blublox.com domain at 4 stars with 1,400+ reviews. Not reconciled — see raw/last30days-ecom.md Cross-Source Signal section.
- Several Google Ads Transparency screenshots show "500. That's an error" pages in place of ad creative — noted in raw/google-ads-visual-summary.md as a screenshot/delivery observation, not analyzed further.
- Exact capture date, shopper geo, and PDP variant selection for the site screenshots (homepage/collection/cart) were not provided and could not be inferred; recorded as unknown in raw/site-visual-summary.md.

## Audit

- boncharge-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

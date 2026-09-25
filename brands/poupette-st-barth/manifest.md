# Poupette St Barth CRO Collection Manifest

## Brand Info

- Store name: Poupette St Barth
- Store URL: https://www.poupettestbarth.com
- Slots: 8 total, 0 dev/project slots specified
- Variations per test: not specified (default: 1 variation vs. control)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages (creatives collected for 3 ads; landing page folds collected for 1 of 3)
- Google Ads Transparency
- PageSpeed / Core Web Vitals (raw JSON, homepage and PDP)
- Current Site Screenshots (homepage, collection, PDP, cart)
- Social & Community Research (automatic — explicitly skipped this run at user's request; see Missing Data Warnings)

## Sources Collected

- Meta Ads → raw/meta-ads.md, raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- PageSpeed → raw/pagespeed.md, raw/homepage-pagespeed.json, raw/pdp-pagespeed.json
- Site Screenshots → raw/site-visual-summary.md
- Screenshots present → raw/screenshots/ (17 files)
- Screenshot aliases mapped:
  - ad-creative-1.png, ad-creative-2.png, ad-creative-3.png → meta-ad-N.png slots
  - ad2-landing-f1/f2/f3.png → meta-ad-2-lp-fM.png slots
  - google-ads-1.png, google-ads-2.png → google-ads.png slot
  - collections-f1/f2/f3.png → collection-fM.png slots
  - cart-drawer.png → cart.png slot

## Sources Skipped

- Reviews & UGC — explicitly skipped by user
- Competitor Insights — not provided
- Inspiration Sites — not provided
- Email Campaigns — not provided
- Non-Data Context — not provided
- Meta Ad #1 landing page — not collected (creative only)
- Meta Ad #3 landing page — not collected (creative only)

## Missing Data Warnings

- MISSING_DATA: social_community_research — Social & Community Research (last30days-ecom) was explicitly skipped at the user's request for this run. Not run, no raw/last30days-ecom.md file. This source normally runs unconditionally; its absence should be treated as a real gap in `/cro-audit`, not silently backfilled.
- MISSING_DATA: reviews — Reviews & UGC explicitly skipped at user's request.
- MISSING_DATA: meta_ad_1_landing_page — Ad 1 creative collected, no landing page screenshots.
- MISSING_DATA: meta_ad_3_landing_page — Ad 3 creative collected, no landing page screenshots.
- MISSING_DATA: pdp_locale_mismatch — pdp-f1/f2/f3.png were captured on the French-language version of the site (poupettestbarth.com FR), while homepage and collection screenshots are in English. Note for audit: PDP copy/CTA text is in French, not directly comparable to English-language homepage/collection copy.

## Open Questions

- ad2-landing-f1/f2/f3.png resolve to a site search results page for "sasha" (22 results), not a single dedicated product landing page — flagged in raw/meta-ads-visual-summary.md under Ad 2's Message Match note.
- cart-drawer.png shows a full mobile cart page layout, not an overlay/slide-out drawer — filename may not reflect the actual UI pattern.
- No landing-page-fN.png files were provided (distinct from the Meta ad LP screenshots), so no dedicated "Landing Pages" section exists in raw/site-visual-summary.md.

## Audit

- poupette-st-barth-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

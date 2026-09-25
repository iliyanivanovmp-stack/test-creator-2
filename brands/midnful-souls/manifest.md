# Mindful Souls CRO Collection Manifest

## Brand Info

- Store name: Mindful Souls
- Store URL: https://mindfulsouls.com/
- Slots: 8 total, dev/project slots not specified
- Variations per test: 1 variation vs. control
- Areas of focus: Not specified by user

## Sources Selected

Data was provided in bulk (pre-collected screenshots and PageSpeed reports dropped into the folder) rather than via the chat intake flow. Based on files present:
- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, cart)
- Reviews & UGC — pending, to be collected next

## Sources Collected

- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md (extracted from raw/pagespeed-homepage-lighthouse.json and raw/pagespeed-pdp-lighthouse.json)
- Screenshots → raw/screenshots/ (23 files)
- Screenshot aliases mapped:
  - ad-creative-1.png, ad-creative-2.png, ad-creative-3.png → meta-ad-N creative slots
  - ad1-landing-fM.png / ad2-landing-fM.png / ad3-landing-fM.png → meta-ad-N-lp-fM slots
  - google-ads-1.png, google-ads-2.png → google-ads slots
  - collections-fM.png → collection-fM slots
  - cart-drawer-1.png, cart-drawer-2.png → cart slot (both loaded; cart-drawer-2.png includes subtotal/checkout not visible in cart-drawer-1.png)

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png, ad3-landing-f3.png
- cart-drawer-1.png, cart-drawer-2.png
- collections-f1.png, collections-f2.png, collections-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png

## Sources Skipped

- Competitor Insights (not provided)
- Inspiration Sites (not provided)
- Email Campaigns (not provided)
- Non-Data Context (not provided)

## Missing Data Warnings

- MISSING_DATA: pdp_screenshots — no dedicated PDP layout screenshots captured. A PageSpeed/Lighthouse report exists for this product's page (raw/pagespeed-pdp-lighthouse.json, performance metrics only), and its layout is otherwise represented by the Ad 3 landing page folds in raw/meta-ads-visual-summary.md — but buy-box structure, pricing display, and trust-signal placement specific to this page cannot be independently verified beyond what those folds show.
- Reviews — intentionally excluded from this collection pass per user instruction; to be sent separately.

## Open Questions

- Trust metrics are inconsistent across surfaces (12k+ reviews on homepage hero vs. 11,388 customers on homepage promo vs. 3k+ Trustpilot reviews / 11,388 customers on collection page vs. 13,000 reviews on Meta landing pages vs. 3.9/966 rating shown in one Google Search ad snippet). Flagging for audit rather than resolving here, since Step 1-3 data collection does not interpret findings.
- Google Ads screenshots show three non-matching discount codes (LABOR35, SPRING35, plus an unlabeled "35% Off" and a "50% OFF" banner) in addition to the Meta ad codes (no-code $25.99, MYBOX35). Full code inventory left for the audit stage.

## Next Step

Reviews collection is next — send review text, links, or files whenever ready.

After that: run /cro-audit to generate the research audit.

## Audit

- midnful-souls-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

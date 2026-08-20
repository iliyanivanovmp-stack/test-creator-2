# Revival CRO Collection Manifest

## Brand Info

- Store name: Revival
- Store URL: https://revivalshots.com/
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Current Site Screenshots (homepage, collection, PDP, cart)

## Sources Collected

- Meta Ads (creatives + landing page folds for Ads 1-3) → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots (homepage, collection, PDP, cart) → raw/site-visual-summary.md
- Screenshot aliases mapped:
  - `ad-creative-1.png`, `ad-creative-2.png`, `ad-creative-3.png` used as `meta-ad-N.png`
  - `ad1-landing-fM.png`, `ad2-landing-fM.png`, `ad3-landing-fM.png` used as `meta-ad-N-lp-fM.png`
  - `google-ads-1.png`, `google-ads-2.png` used as `google-ads.png` (multiple)
  - `colletions-f1.png` (typo), `collections-f2.png` used as `collection-fM.png`
  - `cart-drawer.png` used as `cart.png`

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png, ad3-landing-f3.png
- cart-drawer.png
- collections-f2.png, colletions-f1.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png

## Sources Skipped

- Reviews & UGC — explicitly not available (no reviews collected)
- PageSpeed / Core Web Vitals — not provided; not fetched during collection
- Competitor Insights — not provided
- Inspiration Sites — not provided
- Email Campaigns — not provided
- Non-Data Context (call notes, strategic priorities) — not provided
- Meta Ads landing page URLs — not provided as text; landing pages documented via screenshots only

## Missing Data Warnings

- MISSING_DATA: reviews — no customer review data collected. On-site and third-party review sentiment cannot be evaluated.
- MISSING_DATA: pagespeed — no PageSpeed/Core Web Vitals data collected. Site performance cannot be evaluated.
- MISSING_DATA: competitor_insights — not collected during intake; will require research during audit.
- MISSING_DATA: landing_page_urls — Meta ad landing pages were captured as screenshots only; underlying URLs not recorded for live fetch during audit.

## Open Questions

- Collection page screenshots (`colletions-f1.png`, `collections-f2.png`) reach the footer within 2 folds — confirm this is the full page and not a truncated capture before treating it as complete in the audit.
- PDP fold 2's video/image module appears mostly blank — confirm whether this is a real layout issue on the live site or a capture/loading artifact.

## Audit

- revival-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

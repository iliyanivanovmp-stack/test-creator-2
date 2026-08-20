# Performance Golf CRO Collection Manifest

## Brand Info

- Store name: Performance Golf
- Store URL: https://shop.performancegolf.com/
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)
- Non-Data Context (30-day business summary)

## Sources Collected

- Meta Ads landing page URLs → raw/meta-ads.md
- Meta Ads (creatives + landing pages) → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Reviews → raw/reviews.md
- PageSpeed (raw Lighthouse JSON, homepage + PDP) → raw/pagespeed.md
- Non-Data Context (30-day business summary) → raw/context.md
- Site Screenshots (homepage, collection, PDP, cart) → raw/site-visual-summary.md
- Screenshots → raw/screenshots/ (24 files)
- Screenshot aliases mapped:
  - `ad-creative-1/2/3.png` used as `meta-ad-1/2/3.png`
  - `ad1-landing-f1/2/3.png` used as `meta-ad-1-lp-f1/2/3.png`
  - `ad2,3-landing-f1/2/3.png` used as both `meta-ad-2-lp-f1/2/3.png` and `meta-ad-3-lp-f1/2/3.png` (Ad 2 and Ad 3 share one landing page — see note below)
  - `collections-f1/2/3.png` used as `collection-f1/2/3.png`
  - `cart-drawer.png` used as cart

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2,3-landing-f1.png, ad2,3-landing-f2.png, ad2,3-landing-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- collections-f1.png, collections-f2.png, collections-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png
- cart-drawer.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns

## Missing Data Warnings

- None. Cart drawer was captured (as `cart-drawer.png`).

## Open Questions

- Ad #2 and Ad #3 land on the identical URL (https://shop.performancegolf.com/pages/sf2-driver-media-info-sc). Landing page screenshots were provided once (`ad2,3-landing-f1/2/3.png`) and were duplicated into both the Ad 2 and Ad 3 slots in `raw/screenshots/` and in `raw/meta-ads-visual-summary.md`. Treat Ad 2 and Ad 3 as sharing one landing page in the audit, not two independent pages.
- PageSpeed data was provided as raw Lighthouse JSON files (`homepage-pagespeed-performancegolf.json`, `pdsp-pagespeed-performancegolf.json`) rather than pasted scores. These live in `data-collection/` (not moved into `raw/`) — flagged in `raw/pagespeed.md` for parsing during the audit.
- A 30-day business summary document (`2026-08-16-performance-golf-30day-business-summary.md`) was provided as extra context beyond the standard intake. Saved as `raw/context.md` (Non-Data Context). Flagging here per user request — this file likely carries more weight in the `/cro-audit` step than a typical context file, since it contains business performance data specific to this engagement.

## Audit

- performance-golf-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

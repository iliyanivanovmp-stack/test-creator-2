# Labareau CRO Collection Manifest

## Brand Info

- Store name: Labareau
- Store URL: https://labareau.nl
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (control vs. 1 variation)
- Areas of focus: Ad #2 lands directly on the PDP (The Rich Cream) — no separate PDP screenshots were captured since the ad2-landing folds serve as PDP evidence. Ad #3 lands on a single-fold landing page (a skin-quiz interstitial), not a standard multi-fold LP.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Non-Data Context (brand strategy notes)
- Current Site Screenshots (homepage, collection; no PDP — see note above)
- Social & Community Research (automatic via last30days-ecom)

## Sources Collected

- Reviews & UGC → raw/reviews.md
- Non-Data Context (brand strategy notes, revenue-per-click metrics, four priorities) → raw/context.md
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP) → raw/pagespeed.md (source JSON: raw/HOMEPAGE-PAGESPEED-LABAREAU.json, raw/LABAREAU-PDP-PAGESPEED.json)
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md (engine raw output: raw/labareau-labareau-nl-raw-last30days-ecom.md)
- Supporting context screenshot (WhatsApp image accompanying the brand's revenue-per-click metrics) → raw/context-screenshot-1.jpeg — filed as reference only, not analyzed as part of the three visual-summary groups (does not match Meta/Google/site screenshot categories)
- Screenshot aliases mapped:
  - ad-creative-1/2/3.png used as meta-ad-1/2/3.png
  - ad1-landing-f1/f2/f3.png, ad2-landing-f1/f2/f3.png used as meta-ad-N-lp-fM.png
  - ad3-landing.png used as meta-ad-3-lp-f1.png (single fold only — no f2/f3 exist for this ad)
  - google-ads-1.png, google-ads-2.png used as google-ads screenshots
  - collections-f1/f2/f3.png used as collection-fM.png
  - cart-drawer.png used as cart.png

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1-landing-f1.png
- ad1-landing-f2.png
- ad1-landing-f3.png
- ad2-landing-f1.png
- ad2-landing-f2.png
- ad2-landing-f3.png
- ad3-landing.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- google-ads-1.png
- google-ads-2.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns

## Missing Data Warnings

- MISSING_DATA: pdp_screenshots — no standalone `pdp-fN.png` files were captured. Per user instruction, Ad #2's landing-page folds (ad2-landing-f1/f2/f3.png) are the PDP for The Rich Cream and are documented as PDP evidence in raw/meta-ads-visual-summary.md and referenced from raw/site-visual-summary.md. Other PDPs on the site (any product besides The Rich Cream) remain uncaptured.
- MISSING_DATA: ad3_landing_folds_2_3 — Ad #3's landing page has only one fold by design (a single-fold skin-quiz interstitial); folds 2/3 do not exist for this destination, so downstream analysis of this LP is limited to what fold 1 shows.
- Trustpilot review-level data — a Trustpilot profile exists for labareau.com (confirmed via web search, rating snippets ranging 4.0-4.7 stars across 245-382 reviews depending on snippet source) but the last30days-ecom engine's direct Trustpilot lookup returned an HTTP 404 and could not pull actual review content. Flag for manual verification if Trustpilot sentiment is needed in the audit.
- Instagram reel-level data — both @labareau and @labareauofficial accounts are confirmed active, but the last30days-ecom engine's Instagram reel fetch hit a 404 and returned 0 items. Tooling gap, not evidence of low activity.

## Open Questions

- Exact capture dates, URLs, and shopper geo/currency for the homepage, collection, and cart-drawer screenshots were not provided by the user and are not embedded in the image files — noted as unconfirmed in raw/site-visual-summary.md.
- Whether the 2 items shown in cart-drawer.png (The Rich Cream, The Toner) reflect a real add-to-cart flow with a genuine buyable SKU, or a pre-seeded/staged cart state, is unknown.
- The purpose/context of raw/context-screenshot-1.jpeg (the WhatsApp image) was inferred from its position in the user's message (immediately following the revenue-per-click metrics) but was not explicitly labeled by the user; filed as supporting context only.

## Audit

- labareau-research-audit.md
- roadmap-seed.md

## Next Step

Roadmap generated: labareau-september-2026-roadmap.md

# Bootylicious Muffins CRO Collection Manifest

## Brand Info

- Store name: Bootylicious Muffins
- Store URL: https://bootyliciousmuffins.com/
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP)
- Social & Community Research (automatic, always runs)

## Sources Collected

- Reviews & UGC → raw/reviews.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md (raw JSON: raw/bootylicious-muffins-homepage-pagespeed.json, raw/pdp-pagespeed.json)
- Meta Ads (landing page context) → raw/meta-ads.md
- Meta Ads (visual) → raw/meta-ads-visual-summary.md
- Google Ads (visual) → raw/google-ads-visual-summary.md
- Site Screenshots (visual) → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Screenshots → raw/screenshots/ (14 files)

## Screenshot Aliases Mapped

- `ad-creative-1.png`, `ad-creative-2.png`, `ad-creative-3.png` used as Meta ad creative slots (canonical `meta-ad-N.png`)
- `collections-f1.png`, `collections-f2.png`, `collections-f3.png` used as the collection-page slot, but per user confirmation this is not a typical collection grid — it is the site's "Build Your Own Protein Muffin Box" flavor-picker/builder page
- `google-ads-1.png`, `google-ads-2.png` used as the Google Ads slot (canonical `google-ads.png`)
- `cart-drawer.png` used as the cart slot (canonical `cart.png`)
- Meta ad landing pages: no per-ad LP folds exist — `homepage-f1/f2/f3.png` used as the shared landing page evidence for all 3 Meta ads, per user confirmation that all ads land on the homepage

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- google-ads-1.png
- google-ads-2.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png
- pdp-f1.png
- pdp-f2.png
- pdp-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context

## Social & Community Research (last30days-ecom)

- Mode: Engine
- Sources run: YouTube, TikTok, Instagram, Pinterest, Amazon, Web
- Sources skipped: Reddit (no relevant results), X/Twitter (account exists, no posts), Trustpilot (no profile found)
- File: raw/last30days-ecom.md

## Missing Data Warnings

- None. Cart evidence collected via `cart-drawer.png` (accepted alias for `cart.png`).

## Open Questions

- Cart drawer screenshot shows a "Checkout+" line item ($1.95, "Loss, theft & damage") between the discount-code field and subtotal — whether this is pre-selected/bundled by default or opt-in could not be determined from the static screenshot alone.
- PageSpeed data exists only as raw JSON exports (not pasted scores); numeric interpretation deferred to `/cro-audit`.
- Exact capture date, shopper geo/currency, and add-to-cart SKU/flow for the site screenshots were not provided.

## Audit

- bootylicious-muffins-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

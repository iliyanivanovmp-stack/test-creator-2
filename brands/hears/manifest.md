# Hears CRO Collection Manifest

## Brand Info

- Store name: Hears
- Store URL: hears.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (vs. control)
- Areas of focus: none specified beyond standard CRO collection

## Sources Selected

- Google Ads Transparency (screenshots collected)
- PageSpeed / Core Web Vitals (Lighthouse JSON provided for homepage and PDP)
- Current Site Screenshots (homepage, collection, PDP, cart)
- Social & Community Research (automatic)
- Reviews & UGC (collected)

Meta Ads and Landing Pages: not applicable — brand does not run Meta ads. No files created for this source.

## Sources Collected

- Google Ads → raw/google-ads-visual-summary.md
- PageSpeed → raw/pagespeed.md
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Meta Ads → raw/meta-ads.md (brand does not run Meta ads; file states this explicitly)
- Reviews & UGC → raw/reviews.md (Trustpilot-style reviews, saved verbatim)
- Screenshot aliases mapped: `collections-f1.png`, `collections-f2.png`, `collections-f3.png` used as `collection-fM.png` canonical slot; `cart-drawer.png` used as `cart.png` canonical slot; `pdp-f1/2/3.png` matched canonical PDP slot directly.

## Screenshots Present

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

- Meta Ads and Landing Pages (brand does not run Meta ads)
- Competitor Insights (not provided; not collected)
- Inspiration Sites (not provided; not collected)
- Email Campaigns (not provided; not collected)
- Non-Data Context / call notes (not provided; not collected)

## Missing Data Warnings

- PDP capture URL carries a search-result query string (`?variant=...&_pos=5&_psq=pacha&_ss=e&_v=1.0`) rather than a clean direct link — flag for verification during audit rather than treating as the default PDP state.
- Homepage PageSpeed test also ran against a URL carrying the same `?variant=...` query string rather than a clean homepage URL — flag for verification.

## Open Questions

- Whether the "Pacha Edition 2.0" / cherry-branded colorway shown in the PDP captures is the site's default variant or was pre-selected by a prior session (URL query string suggests a search click-through, not a fresh landing).
- Capture date/time for the screenshots was not provided; only the PageSpeed JSON fetch timestamps (2026-09-13) are known.
- Third-party rating discrepancy identified in social research (Amazon 3.8/5, Trustpilot 3.5 TrustScore, vs. site's own 4.9/5 claim) — not resolved here, flagged for the audit stage.

## Audit

- hears-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

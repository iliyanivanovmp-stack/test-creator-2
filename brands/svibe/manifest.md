# Svibe CRO Collection Manifest

## Brand Info

- Store name: Svibe
- Store URL: svibe.com
- Slots: 8 total, 0 dev/project slots (not specified by user)
- Variations per test: 1 (vs. control)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)
- Social & Community Research (automatic via last30days-ecom)

Note: this collection ran in a single batch — the user stated all data was already placed in `brands/svibe/` except reviews (pasted directly in chat) and confirmed the store URL when asked. Competitor Insights, Inspiration Sites, Email Campaigns, and Non-Data Context were not provided in text or screenshot form and were not collected.

## Sources Collected

- Reviews → raw/reviews.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md (parsed from user-provided `svibe-homepage-pagespeed.json` and `svibe-pdp-pagespeed.json`)
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Screenshots → screenshots/ (24 files)
- Screenshot aliases mapped: `ad-creative-N.png` used as `meta-ad-N.png`; `adN-landing-fM.png` used as `meta-ad-N-lp-fM.png`; `collections-fM.png` used as `collection-fM.png`; `cart-drawer.png` used as `cart.png`

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png, ad3-landing-f3.png
- cart-drawer.png
- collections-f1.png, collections-f2.png, collections-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png

## Sources Skipped

- Competitor Insights (not provided)
- Inspiration Sites (not provided)
- Email Campaigns (not provided)
- Non-Data Context / call notes (not provided)

## Missing Data Warnings

- None. `cart-drawer.png` was present and mapped to the cart slot, so cart/AOV evidence was captured.

## Open Questions

- Capture date, exact page URLs, shopper geo, and default/selected PDP variant at time of screenshot were not provided and are marked as unknown in `raw/site-visual-summary.md`.
- Ad 3's landing page uses a different template ("Reconnect. Without the awkward conversation.") than the direct-PDP style used by Ads 1 and 2, and its sticky-bar price ($69) differs from the price context implied elsewhere — flagged as a raw observation in `raw/meta-ads-visual-summary.md`, not analyzed further per collection-stage scope.
- last30days-ecom engine run for X and Amazon returned 0 scored items in-window despite precheck confirming active presence on both platforms; Instagram engine call failed with HTTP 404. Treated as unresolved/inconclusive, not as absence of activity — noted in raw/last30days-ecom.md.

## Audit

- svibe-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

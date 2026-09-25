# Huug CRO Collection Manifest

## Brand Info

- Store name: Huug
- Store URL: https://huug.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (1 variation vs. control)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, cart)
- Reviews & UGC
- Social & Community Research (automatic)

## Sources Collected

- Meta Ads landing URLs → raw/meta-ads.md
- Meta Ads (creatives + landing pages) → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- PageSpeed (homepage + PDP JSON reports) → raw/pagespeed.md, raw/huug-homepage-pagespeed.json, raw/huug-pdp-pagespeed.json
- Site Screenshots (homepage, collection, PDP via ad landing pages, cart) → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Reviews & UGC → raw/reviews.md (31 Daily Embrace product reviews, saved verbatim)
- Screenshot aliases mapped:
  - `ad-creative-1/2/3.png` used as Meta ad creative slots
  - `ad1,2-landing-f1/f2/f3.png` used as the shared Ad 1 + Ad 2 landing page / PDP folds (Daily Embrace, Black)
  - `ad3-landing-f1/f2/f3.png` used as Ad 3's landing page / PDP folds (Daily Embrace Adjustable, Stone)
  - `collections-fN.png` used as canonical `collection-fN` slot
  - `cart-drawer.png` used as canonical `cart` slot
  - `google-ads-1/2.png` used as canonical `google-ads` slot

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1,2-landing-f1.png, ad1,2-landing-f2.png, ad1,2-landing-f3.png
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

- No standalone PDP screenshots exist as a separate slot — by design, per user: Ad 1 and Ad 2 share one landing page which is also the PDP (Daily Embrace), and Ad 3's landing page is a second PDP (Daily Embrace Adjustable). This is documented, not a gap.

## Open Questions

- Capture date, shopper geo/currency, and whether the captured PDP variants (Black/M for Ad 1&2, Stone/L for Ad 3) are the default or user-selected variant are not stated in the provided screenshots — unknown.
- PageSpeed JSON reports were found pre-collected in the raw folder (huug-homepage-pagespeed.json, huug-pdp-pagespeed.json) rather than pasted by the user; scores/metrics have not been extracted from the JSON yet — that can happen during `/cro-audit`.

## Audit

- huug-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

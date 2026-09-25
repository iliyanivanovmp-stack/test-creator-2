# Selkirk CRO Collection Manifest

## Brand Info

- Store name: Selkirk
- Store URL: selkirk.com
- Slots: 8 total, 0 dev/project slots specified
- Variations per test: not specified (default: 1 variation vs. control)
- Areas of focus: The collections page linked from the homepage's main CTA is a bags-only collection (Pro Line 2.0 Bags), but the brand's core product is paddles — a potential navigation/message-match issue flagged by the client.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)
- Social & Community Research (automatic, runs unconditionally)

## Sources Collected

- Reviews → raw/reviews.md (Amazon reviews for SLK Neo Pickleball Paddle Set, provided by client)
- PageSpeed / Core Web Vitals → raw/pagespeed.md (Lighthouse mobile data extracted from raw/lekirk-homepage-pagespeed.json and raw/selkir-pdp-pagespeed.json)
- Non-Data Context → raw/context.md (client note: homepage main CTA lands on the bags collection page, not paddles)
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Screenshot aliases mapped: ad-creative-1/2/3.png used as meta-ad-N.png; ad1/2/3-landing-fM.png used as meta-ad-N-lp-fM.png; google-ads-1.png / google-ads-2.png used as google-ads screenshots; collections-fM.png used as collection-fM.png; cart-drawer.png used as cart.png

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

- Competitor Insights (not provided; not selected)
- Inspiration Sites (not provided; not selected)
- Email Campaigns (not provided; not selected)

## Missing Data Warnings

- None. A cart screenshot was collected via the accepted alias `cart-drawer.png`.

## Open Questions

- Meta Ads landing page URLs were not provided as text (only screenshots) — `/cro-audit` cannot re-fetch these live; visual summary is based solely on the captured screenshots.
- Ad 2 (Vanguard Power Air) shows a price mismatch between the ad creative ($130.00) and the landing page ($100.99), and the landing page's primary CTA is disabled ("Out of stock") — flagged in raw/meta-ads-visual-summary.md for audit review.
- Two PageSpeed source JSON files use inconsistent/typo'd filenames (`lekirk-homepage-pagespeed.json`, `selkir-pdp-pagespeed.json`) — left as-is since they were already present in the folder; content confirmed valid Lighthouse mobile data for selkirk.com homepage and the Project Boomstik PDP.

## Audit

- selkirk-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

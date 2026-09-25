# Ashley Stewart CRO Collection Manifest

## Brand Info

- Store name: Ashley Stewart
- Store URL: https://www.ashleystewart.com
- Slots: 8 total, 0 dev/project slots (not specified by user, default assumed)
- Variations per test: 1 variation vs. control (default, not specified by user)
- Areas of focus: Ad #1's landing page destination 404s and then automatically redirects to the homepage (user-flagged, unverified against live site — to confirm during audit)

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)
- Reviews & UGC

## Sources Collected

- Meta Ads landing URLs → raw/meta-ads.md
- Ad #1 404/redirect note → raw/context.md
- PageSpeed (Lighthouse mobile, homepage + PDP) → raw/pagespeed.md, raw/pagespeed-homepage.json, raw/pagespeed-pdp.json
- Reviews (20 reviews, raw pasted text) → raw/reviews.md
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Screenshots → raw/screenshots/ (21 files)
- Screenshot aliases mapped:
  - ad-creative-1/2/3.png → meta-ad-1/2/3.png
  - ad2-landing-fM.png → meta-ad-2-lp-fM.png
  - ad3-landing-fM.png → meta-ad-3-lp-fM.png
  - collections-fM.png → collection-fM.png
  - cart-drawer.png → cart.png
  - google-ads-1.png, google-ads-2.png used as-is (multi-screenshot Google Ads alias)

## Screenshots Present

- cart.png
- collection-f1.png, collection-f2.png, collection-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- meta-ad-1.png, meta-ad-2.png, meta-ad-3.png
- meta-ad-2-lp-f1.png, meta-ad-2-lp-f2.png, meta-ad-2-lp-f3.png
- meta-ad-3-lp-f1.png, meta-ad-3-lp-f2.png, meta-ad-3-lp-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context (beyond the ad-1 404 note captured above)
- Social & Community Research (not run via /last30days-ecom for this brand)

## Missing Data Warnings

- Ad #1 landing page screenshots not collected — destination reportedly 404s and redirects to homepage, so no meta-ad-1-lp-fM.png files exist.

## Open Questions

- Ad #1's actual advertised product (per creative: "Plus Size Crystal Face Gems, Small Container") could not be matched to a live landing page — needs live-site verification during /cro-audit.
- Store name/URL, ad landing URLs, and dev-slot/variation details were supplied directly via command arguments rather than the standard Step 1 chat intake; dev slots and variations-per-test were not specified and defaulted per skill instructions.

## Audit

- ashley-stewart-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

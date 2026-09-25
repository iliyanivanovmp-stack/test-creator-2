# Instant Hydration CRO Collection Manifest

## Brand Info

- Store name: Instant Hydration
- Store URL: https://instanthydration.com
- Slots: 8 total, 0 dev/project slots (not specified by user, default assumed)
- Variations per test: 1 variation vs. control (default, not specified by user)
- Areas of focus: The PDP used for this audit (https://instanthydration.com/products/energy-electrolyte-drink-mix) is not the site's best-selling product. It is the brand's current focus product and the destination of the site's main CTA button — do not describe it as the best-seller anywhere in the audit.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)
- Reviews & UGC
- Social & Community Research (automatic via last30days-ecom)

## Sources Collected

- Meta Ads landing URLs (Ad #1, #2, #3) → raw/meta-ads.md
- PDP context note (current focus / main CTA destination, not best-seller) → raw/context.md
- PageSpeed (homepage + PDP) → raw/pagespeed.md, raw/pagespeed-homepage.json, raw/pagespeed-pdp.json
- Reviews (mix of Amazon and Trustpilot reviews, raw pasted text) → raw/reviews.md
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom) → raw/last30days-ecom.md
- Screenshots → raw/screenshots/ (23 files)
- Screenshot aliases mapped:
  - ad1-landing-fM.png → meta-ad-1-lp-fM.png
  - ad2-landing-fM.png → meta-ad-2-lp-fM.png
  - ad3-landing-fM.png → meta-ad-3-lp-fM.png
  - cart-drawer.png → cart.png
  - collections-fM.png → collection-fM.png
  - google-ads-1.png, google-ads-2.png used as-is (multi-screenshot Google Ads alias)
  - meta-ad-1/2/3.png, homepage-fM.png, pdp-fM.png used as canonical names already

## Screenshots Present

- cart.png
- collection-f1.png, collection-f2.png, collection-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- meta-ad-1.png, meta-ad-2.png, meta-ad-3.png
- meta-ad-1-lp-f1.png, meta-ad-1-lp-f2.png, meta-ad-1-lp-f3.png
- meta-ad-2-lp-f1.png, meta-ad-2-lp-f2.png, meta-ad-2-lp-f3.png
- meta-ad-3-lp-f1.png, meta-ad-3-lp-f2.png, meta-ad-3-lp-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png

## Social & Community Research (last30days-ecom)

- Mode: Engine
- Sources run: YouTube, TikTok, Trustpilot, Amazon, Web, local corpus
- Sources skipped: Reddit (no genuine brand-relevant results), X/Twitter (no account/posts found), Instagram (active account confirmed in precheck but 0 items returned by engine pass), Pinterest (no genuine brand-relevant results)
- File: raw/last30days-ecom.md

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context (beyond the PDP focus note captured above)

## Open Questions

- raw/reviews.md contains a mix of Amazon product reviews and Trustpilot reviews (with brand replies), pasted as one block without a clear source divider between the two sets — worth noting in the audit since the two platforms carry different review-solicitation dynamics (Amazon: post-purchase; Trustpilot: mix of organic and "Invited" reviews). Trustpilot reviews include several 1-star complaints about undisclosed/hard-to-cancel subscriptions and a reformulated flavor.
- The PDP folder screenshots (pdp-f1/f2/f3.png) are for the Energy+ product (https://instanthydration.com/products/energy-electrolyte-drink-mix), consistent with the user's framing that this is the site's current-focus PDP, not the best-seller.
- All three Meta ad landing pages (Ads 1-3) resolve to the same underlying buy-box template with only the hero banner swapped per campaign (ICEE, Target-availability copy with poolside hero, Luigi's collab) — flagged in raw/meta-ads-visual-summary.md for the audit to weigh message-match findings accordingly.

## Audit

- instant-hydration-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

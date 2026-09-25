# Panafrica CRO Collection Manifest

## Brand Info

- Store name: Panafrica
- Store URL: https://panafrica-store.com
- Slots: 8 total, dev/project slots not specified
- Variations per test: not specified (default 1 variation vs. control)
- Areas of focus: none specified
- Site language: French (panafrica-store.com is a French-language site; all screenshots and collected data reflect the French version). The final audit and roadmap will be written in English, but the audit target is the French version of the site.

## Sources Selected

- Meta Ads and Landing Pages (screenshots + landing page URLs)
- Google Ads Transparency (screenshots only)
- PageSpeed / Core Web Vitals (Lighthouse JSON reports provided)
- Current Site Screenshots (homepage, collection, PDP, cart)
- Reviews & UGC (raw text provided)

## Sources Collected

- PageSpeed → raw/pagespeed.md (from data-collection/homepage-pagespeed.json and pdp-panafrica.json)
- Meta Ads → raw/meta-ads.md (landing page URLs) and raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/site-visual-summary.md
- Reviews → raw/reviews.md (raw text, unprocessed)
- Screenshot aliases mapped → ad-creative-N.png used as meta-ad-N.png; ad1-landing-fM.png / ad2-ladning-fM.png / ad3-landing-fM.png used as meta-ad-N-lp-fM.png (ad2's files carry the source typo "ladning"); google-ads-1.png / google-ads-2.png used as google-ads screenshots; collections-fM.png used as collection-fM.png; cart-drawer.png used as cart.png

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-ladning-f1.png, ad2-ladning-f2.png, ad2-ladning-f3.png
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

- Store URL and product URL for PageSpeed were inferred from the Lighthouse JSON reports (`requestedUrl` field), not explicitly stated by the user.

## Open Questions

- Collection page screenshots (collections-f1/f2/f3.png) render in English (EN toggle) while homepage, PDP, and ad landing page screenshots render in French (FR) — confirmed as a locale/capture inconsistency, not a site issue; the site itself and the audit target are French. Process collection screenshots as-is per user instruction.
- One PDP-style card in the collection grid (collections-f3.png) exposes a full size run + "Add to cart" directly in the grid, while all other collection cards do not — unclear if this is a hover state, a layout bug, or an intentional quick-add feature partially rendered.
- Google Ads Transparency screenshots show several tiles rendering unfilled dynamic template variables (e.g. `<Prix>`, `<Rating (Reviews)>`) and one raw "500. That's an error." tile — unclear if these are currently live/serving or inactive/expired variants.

## Audit

- panafrica-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

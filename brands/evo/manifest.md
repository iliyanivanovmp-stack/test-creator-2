# Evo CRO Collection Manifest

## Brand Info

- Store name: Evo
- Store URL: evo.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (vs. control)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, cart)
- Reviews & UGC (pending — see below)

## Sources Collected

- Meta Ads → raw/meta-ads.md (landing URLs — Ad #3 only; Ad #1/#2 URLs not provided)
- Google Ads → screenshots in folder
- PageSpeed → raw/pagespeed.md (homepage + PDP Lighthouse data)
- Meta Ads (visual) → raw/meta-ads-visual-summary.md
- Google Ads (visual) → raw/google-ads-visual-summary.md
- Site Screenshots (visual) → raw/site-visual-summary.md
- Screenshot aliases mapped → ad-creative-N.png used as meta-ad-N.png; adN-landing-fM.png used as meta-ad-N-lp-fM.png; google-ads-1.png/google-ads-2.png used as google-ads.png slots; collections-fM.png used as collection-fM.png; cart-drawer.png used as cart.png

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png, ad3-landing-f3.png
- cart-drawer.png
- collections-f1.png, collections-f2.png, collections-f3.png
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context (call notes, strategic priorities)

## Missing Data Warnings

- Reviews: not yet collected. User confirmed the only product with an available review count/UGC source is Ad #3's landing page (Patagonia Nano Puff Hoodie - Women's, evo.com/products/102232-patagonia-nano-puff-hoodie-women-s). Awaiting reviews for this page before running `/cro-audit`.
- No PDP-specific screenshots collected (pdp-fN.png) beyond the ad landing page PDPs already captured for Ads 1-3.
- No dedicated site landing-page-fN.png screenshots collected — only ad landing pages exist.
- Collection screenshots captured are the "Labor Day Sale" promotional collection, not a standard/evergreen category page — noted in site-visual-summary.md.
- Meta Ad #1 and Ad #2 landing page URLs not provided (screenshots exist, but URLs were not shared for the audit's WebFetch step).

## Open Questions

- None beyond the missing data warnings above.

## Audit

- evo-research-audit.md
- roadmap-seed.md

Audit run 2026-08-21 without reviews data (user chose to proceed; see Missing Data section in the audit for the gap).

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

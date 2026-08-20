# Essentia CRO Collection Manifest

## Brand Info

- Store name: Essentia
- Store URL: myessentia.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 (1 variation vs. control)
- Areas of focus: Strong add-to-cart activity, but a large drop-off in the percentage of shoppers who complete the purchase after adding to cart.

## Sources Selected

- Meta Ads and Landing Pages (screenshots only, pre-collected)
- Google Ads Transparency (screenshots only, pre-collected)
- PageSpeed / Core Web Vitals (JSON exports, pre-collected)
- Current Site Screenshots (homepage, collection, PDP, cart)

## Sources Collected

- Meta Ads → raw/screenshots/ (3 ad creatives + 9 landing page folds)
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/screenshots/ (2 Transparency Center screenshots)
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots → raw/screenshots/ (homepage, collection, PDP, cart)
- Site Screenshots → raw/site-visual-summary.md
- PageSpeed → raw/essentia-homepage-pagespeed.json
- PageSpeed → raw/essentia-pdp-pagespeed.json
- Screenshot aliases mapped:
  - ad-creative-1/2/3.png → meta-ad-1/2/3.png
  - ad1/2/3-landing-f1/2/3.png → meta-ad-1/2/3-lp-f1/2/3.png
  - google-ads-1.png, google-ads-2.png → google-ads.png (multi-screenshot)
  - collections-f1/2/3.png → collection-f1/2/3.png
  - cart-drawer.png → cart.png (note: file shows a full mobile cart page, not a drawer overlay)

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

- Reviews & UGC (explicitly skipped by user)
- Competitor Insights (not provided)
- Inspiration Sites (not provided)
- Email Campaigns (not provided)
- Non-Data Context / call notes (not provided)

## Missing Data Warnings

- None. Cart data collected via cart-drawer.png alias.

## Open Questions

- Ad 1 creative references a "Grateful Bed Eight" mattress by name, but the linked landing page (ad1-landing-f1-3) shows the "Grateful Bed Jr" kids' mattress — confirm with the client whether this is the correct ad-to-LP pairing or a mismatched screenshot.
- Google Ads screenshots reference both "up to 30% savings" (via HSA/FSA) and "up to 22% off eco-friendly mattresses" in different creatives — confirm which discount framing is current/accurate.
- No PDP or collection page pricing reflects the sitewide 20% off promotion shown in the top announcement bar; confirm whether this is intentional (discount only applied at cart) or a template/pricing display gap.
- PageSpeed data provided as raw JSON exports (homepage and PDP only) rather than pasted scores — full Lighthouse detail available in raw/*.json for the audit step.

## Audit

- essentia-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

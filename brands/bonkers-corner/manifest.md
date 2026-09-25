# Bonkers Corner CRO Collection Manifest

## Brand Info

- Store name: Bonkers Corner
- Store URL: https://www.bonkerscorner.com
- Slots: 8 total, 0 dev/project slots (not specified — defaulted to 0)
- Variations per test: 1 variation vs. control (not specified — defaulted)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages (screenshots only, no URLs provided)
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, PDP, cart; collection screenshots present but do not show an actual product-grid page — see Open Questions)
- Reviews & UGC (collected, excluded from audit — see Sources Collected)

## Sources Collected

- PageSpeed → raw/pagespeed.md (homepage + PDP Lighthouse mobile scores)
- Meta Ads → raw/meta-ads-visual-summary.md (3 ads, each with creative + 3 landing page folds)
- Google Ads → raw/google-ads-visual-summary.md (2 Google Ads Transparency Center screenshots)
- Site Screenshots → raw/site-visual-summary.md (homepage, collection tiles, PDP, cart drawer)
- Screenshot aliases mapped → ad-creative-N.png used as meta-ad-N.png; adN-landing-fM.png used as meta-ad-N-lp-fM.png; google-ads-1.png/google-ads-2.png used as google-ads.png slots; collections-fM.png used as collection-fM.png; cart-drawer.png used as cart.png
- Reviews → raw/reviews.md (14 reviews, Nov 2024–Jul 2026, saved as-is — see Missing Data Warnings for exclusion from audit)

## Screenshots Present

- Screenshot 2026-08-26 at 17.15.01.png (support chat widget screenshot — not a recognized category, excluded from visual summaries; see Open Questions)
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

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context

## Missing Data Warnings

- Reviews collected (raw/reviews.md) but excluded from audit per user instruction: reviews span Nov 2024–Jul 2026 and are old/low-volume, not sufficient signal for test hypotheses. Do not cite reviews in the audit or roadmap.
- No actual collection/PLP grid screenshot collected — collections-f1/f2/f3.png show homepage-style category promo tiles, not a product listing page with cards, prices, or filters. Collection-page findings cannot be evaluated from this data.
- No Meta Ads landing page URLs were provided (screenshots only) — landing pages cannot be independently fetched/verified during audit.

## Open Questions

- Screenshot "Screenshot 2026-08-26 at 17.15.01.png" shows a Bonkers Corner support chatbot conversation (best-selling men's products list). Doesn't match any accepted naming category; excluded from processing. Flag to user in case it was meant as another data type (e.g., customer service context).
- collections-f1/f2/f3.png appear to be homepage category-navigation sections, not a true collection/PLP page — confirm with user whether an actual collection page screenshot exists or should be recollected.

## Audit

- bonkers-corner-research-audit.md
- roadmap-seed.md

## Next Step

Run /cro-research-roadmap to generate the testing roadmap.

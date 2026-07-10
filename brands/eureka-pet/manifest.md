# Eureka Pet CRO Collection Manifest

## Brand Info

- Store name: Eureka Pet
- Store URL: https://eurekapet.co/
- Primary PDP: https://eurekapet.co/products/natural-dog-food-sample
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control (all A/B tests)
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)

## Sources Collected

- Meta Ads (URLs) → raw/meta-ads.md
- Meta Ads (visual) → raw/meta-ads-visual-summary.md
- Google Ads (visual) → raw/google-ads-visual-summary.md
- Reviews & UGC → raw/reviews.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md (parsed from Lighthouse JSON)
- Site Screenshots → raw/site-visual-summary.md
- Screenshot aliases mapped:
  - ad-creative-1.png / ad-creative-2.png / ad-creative-3.png used as meta-ad-N creative
  - ad1-landing-f1/f2/f3.png, ad2-landing-f1/f2/f3.png, ad3-landing-f1/f2/f3.png used as meta-ad-N-lp-fM
  - google-ads-1.png / google-ads-2.png / google-ads-3.png used as google-ads screenshots
  - collections-f1/f2/f3.png used as collection-fM
  - cart-drawer.png used as cart

## Screenshots Present (in data-collection/screenshots/)

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1-landing-f1.png
- ad1-landing-f2.png
- ad1-landing-f3.png
- ad2-landing-f1.png
- ad2-landing-f2.png
- ad2-landing-f3.png
- ad3-landing-f1.png
- ad3-landing-f2.png
- ad3-landing-f3.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- google-ads-1.png
- google-ads-2.png
- google-ads-3.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png
- pdp-f1.png
- pdp-f2.png
- pdp-f3.png

## Sources Skipped

- Competitor Insights (will research during audit)
- Inspiration Sites
- Email Campaigns
- Non-Data Context

## Missing Data Warnings

- None. All primary sources collected.

## Open Questions

- Review feed was truncated at 50,000 characters during collection — additional reviews may exist beyond what is saved.
- Screenshots are stored in data-collection/screenshots/ (not raw/screenshots/) — audit should reference that path.
- Ad 3 landing page is the same URL as the primary PDP (natural-dog-food-sample). Both the PDP screenshots (pdp-f1/f2/f3) and ad3-landing-f1/f2/f3 show the same page.

## Audit

- eureka-pet-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

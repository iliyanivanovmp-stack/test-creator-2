# Eureka CRO Collection Manifest

## Brand Info

- Store name: Eureka
- Store URL: https://eurekapet.co/
- Slots: 8 total, 0 dev/project slots provided
- Variations per test: 1
- Areas of focus: User-provided case-specific context: ad 2 and ad 3 have shared screenshots, so three screenshots in total, not six, because they land on the same landing page, which is also the PDP. Do not create any tests on the collection page. Test focus should be Ad 1 landing page, Ad 2/3 landing page/PDP, and homepage. The folder `ignore` must be completely ignored.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Non-Data Context
- Current Site Screenshots

## Sources Collected

- PageSpeed / Core Web Vitals -> raw/pagespeed.md
- PageSpeed / Core Web Vitals -> raw/eurekapet-pagespeed-homepage.json
- PageSpeed / Core Web Vitals -> raw/pdp-pagespeed-eureka.json
- Meta Ads and Landing Pages -> raw/meta-ads.md
- Meta Ads and Landing Pages -> screenshots in folder
- Reviews & UGC -> raw/reviews.md
- Non-Data Context -> raw/context.md
- Meta Ads -> raw/meta-ads-visual-summary.md
- Google Ads -> screenshots in folder
- Google Ads -> raw/google-ads-visual-summary.md
- Site Screenshots -> screenshots in folder
- Site Screenshots -> raw/site-visual-summary.md
- Cart screenshot collected -> cart-drawer.png
- Screenshot aliases mapped -> ad-creative-1.png used as meta-ad-1.png
- Screenshot aliases mapped -> ad-creative-2.png used as meta-ad-2.png
- Screenshot aliases mapped -> ad-creative-3.png used as meta-ad-3.png
- Screenshot aliases mapped -> ad1-landing-f1.png used as meta-ad-1-lp-f1.png
- Screenshot aliases mapped -> ad1-landing-f2.png used as meta-ad-1-lp-f2.png
- Screenshot aliases mapped -> ad1-landing-f3.png used as meta-ad-1-lp-f3.png
- Screenshot aliases mapped -> ad2,3- landing-f1.png used as meta-ad-2-lp-f1.png and meta-ad-3-lp-f1.png
- Screenshot aliases mapped -> ad2,3- landing-f2.png used as meta-ad-2-lp-f2.png and meta-ad-3-lp-f2.png
- Screenshot aliases mapped -> ad2,3- landing-f3.png used as meta-ad-2-lp-f3.png and meta-ad-3-lp-f3.png
- Screenshot aliases mapped -> google-ads-1.png used as google-ads-1.png
- Screenshot aliases mapped -> google-ads-2.png used as google-ads-2.png
- Screenshot aliases mapped -> hompage-f1.png used as homepage-f1.png
- Screenshot aliases mapped -> hompage-f2.png used as homepage-f2.png
- Screenshot aliases mapped -> hompage-f3.png used as homepage-f3.png
- Screenshot aliases mapped -> cart-drawer.png used as cart.png

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1-landing-f1.png
- ad1-landing-f2.png
- ad1-landing-f3.png
- ad2,3- landing-f1.png
- ad2,3- landing-f2.png
- ad2,3- landing-f3.png
- cart-drawer.png
- google-ads-1.png
- google-ads-2.png
- hompage-f1.png
- hompage-f2.png
- hompage-f3.png
- pdp-f1.png
- pdp-f2.png
- pdp-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns

## Missing Data Warnings

- MISSING_DATA: collection_canonical_filenames - no files named collection-f1.png, collection-f2.png, or collection-f3.png were present. Files named pdp-f1.png, pdp-f2.png, and pdp-f3.png visually show collection-grid content.

## Open Questions

- Files named pdp-f1.png, pdp-f2.png, and pdp-f3.png visually show a collection page rather than a PDP buy box; they were summarized as collection screenshots.
- User explicitly requested no tests on the collection page. Collection screenshots are reference context only for the audit.
- No dev/project reserved slots were provided; recorded as 0.

## Audit

- eureka-pet-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

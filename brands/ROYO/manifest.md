# Royo CRO Collection Manifest

## Brand Info

- Store name: Royo
- Store URL: https://eatroyo.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, PDP, cart)

## Sources Collected

- Meta Ads and Landing Pages → raw/meta-ads.md and raw/meta-ads-visual-summary.md
- Google Ads Transparency → raw/google-ads-visual-summary.md
- PageSpeed / Core Web Vitals → raw/pagespeed.md
- Site Screenshots → raw/site-visual-summary.md
- Reviews & UGC → raw/reviews.md (86 reviews)
- Screenshots in folder (17 files)

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1,2,3-landing-f1.png
- ad1,2,3-landing-f2.png
- ad1,2,3-landing-f3.png
- google-ads.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- pdp-f1.png
- pdp-f2.png
- pdp-f3.png
- cart-drawer.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns
- Non-Data Context

## Critical Findings (for awareness during audit)

**Performance Bottleneck:** Both homepage (LCP: 12.7s) and ad landing page (LCP: 11.4s) have critical Core Web Vitals failures, running 5-6x above Google thresholds. Ad landing page receives significant traffic according to user notes.

**Ad Structure:** All three Meta ads direct to the same landing page (https://eatroyo.com/pages/new-design-v1-final), minimizing creative variation and landing page fragmentation for testing.

**Message Consistency:** Strong message match between Meta and Google Ads. Meta emphasizes discount offer (26% off) and customer count (250k+). Google Ads emphasize product category (low-carb, keto) and review volume (10,786 reviews).

## Audit

- royo-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

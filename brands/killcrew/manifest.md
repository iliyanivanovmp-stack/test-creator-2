# Killcrew CRO Collection Manifest

## Brand Info

- Store name: Killcrew
- Store URL: killcrew.co
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation
- Areas of focus: None specified

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots
- Non-Data Context
- Social & Community Research (automatic)

## Sources Collected

- Meta Ads (URLs) → raw/meta-ads.md
- Reviews & UGC → raw/reviews.md
- Non-Data Context → raw/context.md
- PageSpeed / Core Web Vitals (raw API data) → raw/homepage-pagespeed-killcrew.json, raw/killcrew-pdp-pagespeed.json
- Meta Ads (visual) → raw/meta-ads-visual-summary.md
- Google Ads (visual) → raw/google-ads-visual-summary.md
- Site Screenshots (visual) → raw/site-visual-summary.md
- Social & Community Research (automatic via last30days-ecom, Engine mode) → raw/last30days-ecom.md
- Screenshots in folder → raw/screenshots/ (16 files)
- Screenshot aliases mapped:
  - `ad-creative-1.png`, `ad-creative-2.png`, `ad-creative-3.png` used as `meta-ad-1/2/3.png`
  - `ad1,2-landing-f1/f2/f3.png` used as the shared landing page folds for both Ad 1 and Ad 2 (identical landing page URL)
  - `ad3-landing-f1/f2/f3.png` used as Ad 3's landing page folds, and also serve as the PDP evidence (Ad 3 lands on a PDP — see Non-Data Context)
  - `google-ads-1.png` used as `google-ads.png`
  - `collections-f1/f2/f3.png` used as `collection-f1/f2/f3.png`
  - `cart-drawer.png` used as `cart.png`

## Screenshots Present

- ad-creative-1.png
- ad-creative-2.png
- ad-creative-3.png
- ad1,2-landing-f1.png
- ad1,2-landing-f2.png
- ad1,2-landing-f3.png
- ad3-landing-f1.png
- ad3-landing-f2.png
- ad3-landing-f3.png
- cart-drawer.png
- collections-f1.png
- collections-f2.png
- collections-f3.png
- google-ads-1.png
- homepage-f1.png
- homepage-f2.png
- homepage-f3.png

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns

## Missing Data Warnings

- No dedicated PDP screenshots (pdp-f1/f2/f3) were collected as a separate set. Per client context, Ad 3's landing page IS a PDP (Muay Thai Shorts Mid Thigh Cut Floral - Black), so PDP evidence is present but documented under Ad 3 in raw/meta-ads-visual-summary.md rather than as a standalone PDP section — this is a client-confirmed data structure, not a gap.
- No standalone landing-page-f1/f2/f3 screenshots were collected outside of the Meta ad landing pages (ad1,2-landing and ad3-landing folds serve this role).
- Instagram and X were confirmed active with real audience/engagement at precheck during social research, but the last30days engine call failed for both (Instagram: HTTP 404; X: 0 items returned) — see raw/last30days-ecom.md "Sources with Errors."

## Open Questions

- None outstanding on filename/alias mapping — all present screenshots mapped cleanly to canonical slots.

## Audit

- killcrew-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

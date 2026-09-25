# Cliganic CRO Collection Manifest

## Brand Info

- Store name: Cliganic
- Store URL: cliganic.com
- Slots: 8 total, 0 dev/project slots (not specified by user — assumed 0)
- Variations per test: 1 variation vs. control (default — not specified by user)
- Areas of focus: The PDP is the Organic Jojoba Oil product. No standalone PDP screenshots were collected because two of the three Meta ads (Ad 1, Ad 3) land directly on this product page with different promotion/page variations, rather than on a separate landing page.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection, cart)
- Social & Community Research (automatic)
- Reviews & UGC

## Sources Collected

- PageSpeed (mobile, homepage + PDP full JSON exports) → raw/pagespeed.md, raw/pagespeed-homepage.json, raw/pagespeed-pdp.json
- Non-Data Context (PDP/jojoba oil note) → raw/context.md
- Reviews & UGC (Amazon reviews + on-site review widget, Organic Jojoba Oil) → raw/reviews.md
- Social & Community Research (automatic via last30days-ecom, Fallback Mode) → raw/last30days-ecom.md
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Site Screenshots (homepage, collection, cart) → raw/site-visual-summary.md
- Screenshot aliases mapped:
  - ad-creative-1/2/3.png used as meta-ad-1/2/3.png
  - ad1/ad2/ad3-landing-f1/2/3.png used as meta-ad-1/2/3-lp-f1/2/3.png
  - cart-drawer.png used as cart.png
  - collections-f1/2/3.png used as collection-f1/2/3.png
  - google-ads-1.png, google-ads-2.png used as google-ads screenshots (multi-screenshot variant)

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

- Competitor Insights — not provided; not selected this round
- Inspiration Sites — not provided; not selected this round
- Email Campaigns — not provided; not selected this round

## Missing Data Warnings

- None. Cart is captured via `cart-drawer.png` (mapped to the `cart` canonical slot). PDP absence is intentional and explained under Areas of Focus / raw/context.md, not a data gap.

## Open Questions

- Dev/project slot count and variations-per-test were not specified by the user in this round; defaulted to 0 dev slots and 1 variation vs. control. Confirm before finalizing the roadmap if this matters.
- Ad 1 and Ad 3 both land on the Organic Jojoba Oil PDP but at different default sizes/discount tiers (4oz/24% off vs. 16oz/15% off); Ad 3's creative also references a $12.99 price point and "#1 Best Seller on Amazon" positioning not reflected on the landing page as captured. Ad 2 lands on a different product (Rosemary Repair Scalp & Strand Oil), not jojoba oil.
- Reviews source is mixed: Amazon-style verified-purchase reviews (with helpful-vote counts) plus what appears to be a separate on-site review widget feed (mostly marked "Incentivized review"), all for Organic Jojoba Oil. Not labeled by the user as to exact platform/source per section.

## Audit

- cliganic-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

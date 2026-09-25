# Swanson Vitamins CRO Collection Manifest

## Brand Info

- Store name: Swanson Vitamins
- Store URL: https://www.swansonvitamins.com
- Slots: 8 total, 0 dev/project slots
- Variations per test: 1 variation vs. control
- Areas of focus: The collection page shown in the collection screenshots is where the homepage's main CTA (labeled "Shop Stacks" on the live site) leads — the natural connection point from homepage to that page. Reviews for the PDP are coming separately from the user before the audit.

## Sources Selected

- Meta Ads and Landing Pages
- Google Ads Transparency
- Reviews & UGC
- PageSpeed / Core Web Vitals
- Current Site Screenshots (homepage, collection/stacks page, PDP, cart)
- Social & Community Research (automatic via /last30days-ecom)

## Sources Collected

- Meta Ads landing URLs → raw/meta-ads.md
- Meta Ads → raw/meta-ads-visual-summary.md
- Google Ads → raw/google-ads-visual-summary.md
- Reviews (PDP: Triple Magnesium Complex, 22 reviews) → raw/reviews.md
- PageSpeed (raw Lighthouse JSON for homepage and PDP) → raw/pagespeed.md
- Non-Data Context (collections-page CTA note) → raw/context.md
- Site Screenshots (homepage, collection/stacks, PDP, cart) → raw/site-visual-summary.md
- Social & Community Research (automatic via /last30days-ecom) → raw/last30days-ecom.md

## Screenshots Present

- ad-creative-1.png, ad-creative-2.png, ad-creative-3.png
- ad1-landing-f1.png, ad1-landing-f2.png, ad1-landing-f3.png
- ad2-landing-f1.png, ad2-landing-f2.png, ad2-landing-f3.png
- ad3-landing-f1.png, ad3-landing-f2.png (no f3 provided)
- google-ads-1.png, google-ads-2.png
- homepage-f1.png, homepage-f2.png, homepage-f3.png
- collections-f1.png, collections-f2.png, collections-f3.png
- pdp-f1.png, pdp-f2.png, pdp-f3.png
- cart-drawer.png

## Screenshot Aliases Mapped

- `ad-creative-1/2/3.png` used as `meta-ad-1/2/3.png` (creative slots)
- `ad1/2/3-landing-fM.png` used as `meta-ad-N-lp-fM.png` (landing page fold slots)
- `google-ads-1.png` / `google-ads-2.png` used as the Google Ads screenshot slot (multi-shot variant)
- `collections-f1/f2/f3.png` used as the collection-page screenshot slot
- `cart-drawer.png` used as the `cart.png` slot

## Sources Skipped

- Competitor Insights
- Inspiration Sites
- Email Campaigns

## Missing Data Warnings

- None — cart evidence was captured (`cart-drawer.png`, mapped to the cart slot).

## Open Questions

- The user described the homepage's main CTA as being named "Shop Stacks Lands." The homepage-f1 screenshot shows the button text as "Shop Stacks" (no "Lands"). The collections screenshots do show a staff-picks "stacks" page (Britta's/Dustin's Daily Stack), consistent with "Shop Stacks" leading there — treating "Lands" as describing where the CTA lands, not part of the button's label. Flagging in case the actual button copy differs from what was captured.
- The "collections" screenshots show a curated staff-picks/stacks landing page, not a standard filterable product-collection grid (no filter/sort UI, no compare-at pricing). Confirm this is the intended page for audit purposes before treating it as "the collection page."
- Ad 2 and Ad 3 landing page fold-1 screenshots each render as nearly blank (only a single headline visible, no other visual content) — may indicate a slow-loading/lazy-loaded hero rather than an actual blank page. Worth re-capturing if the audit needs a real fold-1 view.
- Ad 3 is missing a fold-3 landing page screenshot.
- PDP capture date, shopper geo/currency, and whether "300 Vegan Caps" is the default variant were not provided — noted as unknown in raw/site-visual-summary.md.
- last30days-ecom research auto-detected the query as a two-entity comparison ("Swanson Vitamins https" vs. "www.swansonvitamins.com") due to how the search string was constructed; both raw evidence dumps referred to the same brand, so findings were merged into one brand-level summary rather than a competitor comparison.

## Audit

- swanson-vitamins-research-audit.md
- roadmap-seed.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.

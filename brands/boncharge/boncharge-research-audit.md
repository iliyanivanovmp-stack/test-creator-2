# Bon Charge CRO Research Audit

## Data Sources Used

User-provided: Meta Ads and landing pages (3 creatives), Google Ads Transparency Center screenshots, customer reviews (Red Light Face Mask), PageSpeed/Lighthouse JSON (homepage + PDP), site screenshots (homepage, collection, cart), Ad 3's landing page used as the only PDP evidence (no separate PDP screenshots collected).

Self-researched: Live re-verification of all three Meta-ad landing pages and homepage (WebFetch, 2026-09-12), competitor landscape (WebSearch, 2026-09-12), Social & Community Research via last30days-ecom (automatic, 2026-09-12).

Not provided / skipped: Competitor Insights (user-supplied), Inspiration Sites, Email Campaigns, Non-Data Context.

## Source Findings

### Meta Ads & Landing Pages

Three creatives ran under the same top-level message "Enhance your wellbeing. Shop the full BON CHARGE wellness collection and start thriving today" for Ads 1 and 2 (glasses), and a separate angle for Ad 3 ("Don't wait for better skin... buy now").

- **Ad 1 (Tortoise Shell Computer Glasses, started Apr 21, 2026)** and **Ad 2 (Crystal Computer Glasses, started May 7, 2026)** promise "the full BON CHARGE wellness collection" but land on a single-SKU PDP focused narrowly on eye strain relief. Neither ad mentions the specific product shown, nor the 25% sitewide discount that was live on the landing page at collection time. This is a message-match gap: broad collection promise, narrow single-product delivery.
- **Ad 3 (Red Light Face Mask, started Apr 21, 2026)** has the closest match: ad image, headline ("Don't wait for better skin"), and landing page all show the same product with consistent stat-backed claims (98% even skin tone, 96% glowing skin, 84% results in 4 weeks). Ad 3 has no separate landing page — it routes directly to the PDP.
- Ad 2's collected fold-3 screenshot showed a different product (Tortoise Shell Computer Glasses) than folds 1-2 (Crystal Computer Glasses) — flagged as a possible capture issue at collection time, not confirmed as live site behavior.
- **Live re-verification (2026-09-12):** All three ad-driven landing pages are currently **sold out**. Tortoise Shell Computer Glasses: "Sold out." Crystal Computer Glasses: "Sold out." Red Light Face Mask: displays a "Sold out" state while the on-page copy still reads "In Stock | Limited Quantities Available" — a direct, visible contradiction on the same page. All three ads were still active as of collection. If ad spend is still driving traffic to these URLs, every click currently lands on either a fully blocked purchase path or a self-contradicting stock message.

### Google Ads

Google Ads coverage (30+ units, advertiser "BLUBLOX PTY LTD" operating as Bon Charge) is far broader than Meta: blue light glasses, red light face mask, red light toothbrush, hair growth, night light/sleep products, and general brand terms, plus editorial/guide-style ads ("Pros & Cons: Red Light Therapy"). Meta is narrow by comparison (glasses x2, face mask x1). Both channels share the recurring "25% off sitewide" / Labor Day sale offer. Several Google ad units rendered as "500. That's an error" pages instead of creative in the collected screenshots — a technical delivery issue, not diagnosed further, but worth a live check given the OOS pattern found on Meta's landing pages.

### Reviews & UGC

Only 5 reviews were collected for the Red Light Face Mask, all positive. Sample size is too small to identify frustration themes with confidence.

#### What Customers Love

- Ease of use and routine fit ("found the routine very straightforward with clear instructions")
- Visible skin/elasticity results ("those indents on my face are gone immediately," "helping a lot with elasticity")
- Support responsiveness when an issue occurred ("fantastic follow up support")

#### What Frustrates Customers

- No clear frustration theme emerged from the 5 reviews collected. One customer had a charging-lead issue, self-attributed as user error, resolved by support.

#### Client-Actionable Insights

- Sample is too small (5 reviews) to base product/ops decisions on. Recommend pulling a larger, dated review export (50-100+) before drawing product-quality conclusions.

### PageSpeed / Core Web Vitals

Source: real Lighthouse JSON, fetched 2026-09-12T18:07-18:10 UTC.

| Page | Score | LCP | CLS | TBT | FCP | Speed Index | TTI |
|---|---|---|---|---|---|---|---|
| Homepage (eu.boncharge.com/) | 0.16 | 14.7s | 0.234 | 3,410ms | 4.4s | 13.5s | 44.1s |
| PDP (red-light-face-mask) | 0.32 | 13.2s | 0.139 | 900ms | 3.9s | 12.2s | 48.0s |

Both pages fail Google's "poor" threshold (LCP > 4s is poor) by a wide margin — homepage LCP is roughly 3.7x the poor threshold. TTI on both pages exceeds 44 seconds. Given the homepage's heavy autoplaying hero video and multiple testimonial video blocks (per site-visual-summary), video-weight is a plausible contributor to LCP and TBT, though this is not confirmed by the Lighthouse data itself (which does not break down LCP element).

### Competitor Analysis

Self-researched via WebSearch, 2026-09-12. No user-provided competitor data existed for this brand.

| Competitor | Category | Positioning (per search results) |
|---|---|---|
| Joovv | Red light therapy | Premium, higher price point |
| Chroma | Red light therapy | Ecosystem/multi-device approach |
| Swanwick (Night Swannies) | Blue light glasses | Premium frames, >99% blue light blocking claim, similar price to Bon Charge |
| Ra Optics | Blue light glasses | Sunset Lenses filter to 550nm, same claimed range as Bon Charge Sleep Glasses |

Bon Charge is characterized in search results as having "the widest selection for targeted wearable therapy" across face, hair, and sauna form factors, but third-party reviewers (TikTok, per Social Research below) suggest the brand competes on breadth rather than being the top pick in any single category, and flag Amazon marketplace presence as potential price/purchase-path friction against the direct-to-consumer site.

### Emails

Not collected. Skipped per manifest (not provided).

### Inspiration Sites

Not collected. Skipped per manifest (not provided).

### Non-Data Context

Not collected. Skipped per manifest (not provided).

### Social & Community Research

Directional findings from last30days-ecom (2026-09-12), engine mode.

- **Trust signal split:** The automated Trustpilot pull for boncharge.com shows a TrustScore of 2.4 (6 reviews, as of 2026-09-11), while the brand's legacy domain (blublox.com) carries a 4-star rating built on 1,400+ historical reviews. This is a live risk: any prospect who searches "Bon Charge reviews" independently may land on the low-scoring current-domain listing. Not corroborated or contradicted by first-party review data collected here (only 5 reviews, all positive, from a different source).
- **Marketplace friction:** An independent TikTok reviewer (@well.worth.it.lab, 2026-09-12) scored the Infrared Sauna Blanket 7.4/10, noting it's "likely better as a brand-direct purchase" — implying Amazon listings may be undercutting or complicating the direct-to-consumer path. Corroborated by confirmed active Amazon listings for multiple glasses SKUs and the sauna blanket (Amazon research finding).
- **Influencer/affiliate reliance:** Active paid partnerships confirmed on X (Tucker Carlson, "The Comments Section") and YouTube (HumanWindow, affiliate-disclosed) driving discount-code traffic — directional, not corroborated by site-side evidence in this audit.
- Instagram data was returned partial/degraded for this pull; treat as directional only.

### Current Site Screenshots

**Homepage:** Hero headline "Recover Faster. Sleep Deeper. Look Better." with stat claims (98% even skin tone, 90% improved sleep, 87% feeling more recovered — all footnoted as based on reviews mentioning a specific outcome, not a controlled study) sits above a 4.95/5 (5,700+ reviews) rating and a "Trusted by 400,000+ Customers" badge. Primary CTA "Shop Best Sellers" is a large non-sticky red button — no sticky header/CTA bar exists on the homepage across the three folds collected, in contrast to the PDP and Ad 3 landing page, which carry a persistent sticky Add to Cart bar. This is an inconsistency in CTA availability across the site's own pages: the two highest-intent surfaces (PDP, ad landing page) have alway-visible CTAs, but the entry point (homepage) does not.

**Live re-check (2026-09-12):** Homepage top bar reads "Free Shipping on Orders Over $125," while the same banner on collected PDP/glasses screenshots reads "Free Shipping on Orders Over €115," and the cart drawer displays a mix of EUR (€) and one USD ($356.21) line item on its upsell. This is not a single screenshot artifact — it recurs across at least three separate surfaces (homepage banner, cart upsell, and the €/$ mismatch pattern), indicating a systemic currency-display issue rather than an isolated capture glitch.

**Collection page:** Not a traditional filtered grid — the captured folds show a curated, homepage-style "Shop by Goal" carousel and themed product tiles (Skin/Recovery/Sleep/Hair) with no visible filter or sort controls. Product cards show compare-at/sale pricing and ratings consistently.

**PDP (via Ad 3 landing page, Red Light Face Mask — no separate PDP screenshots exist):** Trust signals (rating, review count, "Trusted by 400,000+ Customers" badge) sit directly beneath the title, above the price — high proximity to the buy box. Single one-time-purchase option in the primary buy box; no subscription option offered anywhere in the three folds reviewed. One bundle cross-sell ("Face, Neck and Chest Bundle," 30% off per screenshot / 7% per live re-check — see Missing Data) appears below the fold, not integrated into the buy box itself.

**Cart:** Right-side drawer, "Congratulations! You've earned free shipping" banner, one line item (Red Light Face Mask) plus one upsell module. No guarantee, returns, or warranty trust signal is shown anywhere inside the drawer — the only reassurance present is the free-shipping banner. "Checkout Securely" CTA is present but not sticky within the drawer (content scrolls above it in the captured fold).

## Cross-Source Themes

1. **Ad-to-purchase-path breakdown is the highest-evidence, highest-severity issue.** All three Meta ad landing pages are live-verified sold out, one with directly contradictory stock copy on the page itself. This combines message-match gaps (Ads 1-2 promising a "full collection" and delivering one OOS SKU) with a live purchase-blocking issue. Evidence: Meta Ads visual summary + live WebFetch re-verification (independent sources, both first-party).
2. **Site performance is severely broken on the two pages most likely to receive paid traffic.** Homepage and PDP both fail Core Web Vitals "poor" thresholds by 3-4x on LCP, with TTI over 44 seconds on both. Evidence: real Lighthouse JSON data (single source, but high-confidence — measured, not estimated).
3. **Currency/locale inconsistency recurs across at least three independent surfaces** (homepage banner, cart upsell line item, and the free-shipping threshold mismatch), suggesting a systemic geo/currency-detection bug rather than a one-off. Evidence: site screenshots + live re-verification (two independent passes, same finding).

## Top Test Opportunities

**Fix or clearly message out-of-stock ad landing pages** — All three actively-running Meta ad creatives point to PDPs that are sold out as of live verification (2026-09-12); the Red Light Face Mask page additionally shows "Sold out" next to "In Stock | Limited Quantities Available" copy, undermining trust site-wide. Evidence: Meta ads visual summary, live WebFetch re-check. Est. lift: sessions/mo and AOV not provided — cannot quantify $ impact, but this blocks 100% of paid-ad-driven conversions on 3 of 3 tracked creatives while active.

**Align Meta glasses ad copy to the actual landing page** — Ads 1 and 2 promise "the full BON CHARGE wellness collection" and general wellbeing; landing pages are single-SKU eye-strain PDPs with no mention of the collection framing or the discount shown on-page. Evidence: meta-ads-visual-summary.md (Ads 1 & 2). Est. lift: unknown without sessions/mo and AOV (not provided in manifest).

**Reduce homepage and PDP page weight / LCP** — Homepage scores 0.16 (LCP 14.7s, TBT 3,410ms), PDP scores 0.32 (LCP 13.2s); both fail Google's "poor" threshold by 3-4x, with TTI over 44s on each. Autoplaying hero and testimonial video are the most likely contributors based on site-visual-summary content density, though Lighthouse data doesn't isolate the LCP element. Evidence: raw/pagespeed.md (real Lighthouse JSON, dated 2026-09-12). Est. lift: unknown without sessions/mo and AOV.

**Resolve the currency/locale display bug** — Homepage shows "$125" free shipping threshold while PDP/ad landing pages show "€115," and the cart drawer's upsell line item prices in USD ($356.21) while the rest of the cart is in EUR. Recurs across 3 separate surfaces, not a single capture glitch. Evidence: site-visual-summary.md, live WebFetch re-check of homepage (2026-09-12). Est. lift: unknown without sessions/mo and AOV; risk is trust/checkout-confidence rather than pure CR.

**Add a sticky CTA/header to the homepage** — PDP and Ad 3 landing page both carry a persistent sticky Add to Cart bar across all folds; the homepage has no sticky header or CTA and relies on a single non-sticky "Shop Best Sellers" button in the hero. Evidence: site-visual-summary.md (homepage vs. PDP CTA behavior comparison). Est. lift: unknown without sessions/mo and AOV.

**Add trust/guarantee signal inside the cart drawer** — The only reassurance shown in the cart is the free-shipping congratulations banner; no guarantee, returns policy, or warranty badge appears despite these being prominent elsewhere (PDP shows "30-Day Easy Returns · 1-Year Warranty" directly below Add to Cart). Evidence: site-visual-summary.md (Cart section). Est. lift: unknown without sessions/mo and AOV.

**Investigate and fix Google Ads Transparency 500-error ad units** — Multiple Google Ads Transparency screenshots show "500. That's an error" instead of ad creative, which — combined with the confirmed OOS landing pages on Meta — raises the question of whether some Google-driven traffic is also hitting broken states. Evidence: google-ads-visual-summary.md. Est. lift: unknown; requires a live check of the specific ad units' landing destinations, not performed in this audit (out of scope — Google Ads Transparency screenshots only show ad units, not confirmed live destination status).

**Reconcile the Trustpilot domain split** — boncharge.com shows a 2.4 TrustScore (6 reviews) while the legacy blublox.com domain carries 1,400+ reviews at 4 stars; a prospect searching independently is more likely to land on the low-scoring current-domain result. Evidence: last30days-ecom.md (directional, single automated source; not corroborated by first-party review data collected in this audit, which is too small a sample to weigh in). Est. lift: unknown; this is a trust/reputation risk, not a directly testable CRO mechanic on-site.

**Clarify or fix the Ad 2 fold-3 product mismatch** — The collected screenshot for Ad 2's landing page fold 3 shows the Tortoise Shell Computer Glasses page instead of the Crystal Computer Glasses shown in folds 1-2 of the same ad. Not confirmed as live site behavior (may be a capture-time issue) — recommend a live click-through of Ad 2's actual current landing URL before treating this as a site bug. Evidence: meta-ads-visual-summary.md (flagged, not diagnosed). Est. lift: unknown; contingent on live confirmation.

**Expand review collection before drawing product-quality conclusions** — Only 5 reviews were collected for the Red Light Face Mask, all positive; this sample is too small to identify real frustration themes or make product/ops recommendations with confidence, despite the homepage claiming "5,700+ Reviews" store-wide. Evidence: raw/reviews.md (5 reviews only). Est. lift: not a testable CRO opportunity — a data-collection gap to close before the next audit cycle.

## Unused but Valuable Findings

- Amazon marketplace listings for multiple glasses SKUs and the sauna blanket may be creating direct-to-consumer price/purchase friction, per one third-party TikTok review calling the brand-direct purchase "likely better" — worth a pricing/positioning review outside the scope of an on-site CRO test.
- Bon Charge is positioned by competitors and reviewers as having "the widest selection" rather than being the top pick in any single category (vs. Joovv's premium positioning or Swanwick/Ra Optics' focused glasses offer) — a messaging/differentiation question for brand strategy, not a single testable page element.

## Missing Data

- No dedicated PDP screenshots exist independent of Ad 3's landing page; all PDP-level findings rely on the Red Light Face Mask page only. Findings about buy-box behavior, subscription options, or upsell placement have not been cross-checked against other PDPs (e.g., the glasses PDPs, which may differ in layout).
- Sessions/mo and AOV were not provided in the manifest or any raw source, so every Top Test Opportunity's dollar-impact estimate could not be calculated. Est. lift figures are qualitative only.
- The live re-check of the Face, Neck and Chest Bundle showed "7% savings" language while the collected screenshot showed "Save 30%" — this discrepancy was not reconciled within this audit and should be verified directly before citing either figure in client-facing materials.
- Exact capture date, shopper geo, and PDP variant selection for the original site screenshots (homepage/collection/cart) remain unknown, as noted in the manifest.

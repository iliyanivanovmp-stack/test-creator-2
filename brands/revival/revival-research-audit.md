# Revival CRO Research Audit

## Data Sources Used

- Meta Ads and Landing Pages (3 ads, screenshot-based)
- Google Ads Transparency (screenshot-based)
- Current Site Screenshots (homepage, collection, PDP, cart)
- Live homepage fetch (revivalshots.com, self-researched, August 9 2026)
- Competitor research (self-researched, August 9 2026)

Not collected: Reviews & UGC, PageSpeed/Core Web Vitals, competitor insights (client-provided), inspiration sites, email campaigns, non-data context, Meta ad landing page URLs.

## Source Findings

### Meta Ads & Landing Pages

Three ads run across two landing page templates.

Ad 1 ("Late night? Get ready to own the day after") matches its landing page tightly. Headline, product (Wild Cherry stick), and hangover-recovery angle all carry through to the LP hero. This is the strongest message match of the three.

Ad 2 ("2026 Travel Hack — packing Revival on your getaway, stay hydrated in the hottest climates") breaks down on landing. The LP sends traffic to the generic brand homepage template ("Your Best Day, Every Day") with no travel imagery, no hot-climate framing, and no offer tied to the ad's hook. A user who clicks on a travel-specific promise lands on undifferentiated brand messaging.

Ad 3 (advertorial: "7 Reasons You Still Feel Off After a Late Night") uses a long-form listicle template, separate from Ads 1-2. Message match is strong (hangover angle carries through), and the format itself is a distinct test variable — advertorial vs. standard product LP.

All three LPs place the primary CTA as a static button, not sticky, meaning it disappears from view during the scroll through trust content, testimonials, and FAQs.

### Google Ads

Google Ads lean on category-authority claims ("UK's No.1 Rehydration Powder," "Most Reviewed") and informational/listicle angles (hangover cures, electrolyte comparisons) more heavily than Meta. The hangover/late-night angle is consistent across both channels. The travel angle from Meta Ad 2 has no Google Ads counterpart — it's an isolated, unsupported creative angle in the current media mix.

### Reviews & UGC

Not collected. MISSING_DATA — see below.

### PageSpeed / Core Web Vitals

Not collected. MISSING_DATA — see below.

### Competitor Analysis

| Brand | Positioning | Price (approx.) | Notable weakness vs. Revival |
|---|---|---|---|
| Revival (client) | WHO-formula hydration, "3x electrolytes," UK's most-reviewed | £19.99 (12-pack) – £39.99 (30-pack) | Subscription-first buy box may suppress one-time buyers; travel ad angle unsupported on-site |
| SOS Rehydrate | 6-electrolyte balance, "4x faster absorption than water," listed in UK medicines database, pharmacy-available | Comparable per-serving pricing on Amazon UK | Lacks Revival's press logo strip and athlete endorsement; less prominent guarantee messaging |
| Liquid I.V. (US benchmark) | #1 powdered hydration brand in the US, "3x electrolytes of leading sports drink," 5 essential vitamins | Similar per-serving cost | Weaker UK distribution/trust signals than Revival; comparable core claim ("3x electrolytes") to Revival's, indicating this is a category-standard claim, not a differentiator |

Research date: August 9, 2026. All competitor data self-researched via web search — no client-provided competitor file exists in `raw/competitors.md`.

### Emails

Not collected.

### Inspiration Sites

Not collected.

### Non-Data Context

Not collected.

### Current Site Screenshots

**Homepage:** Hero is static, non-sticky "Shop Now" against a blue background with a product lineup image — generic enough that it doesn't differentiate flavor, format, or occasion. A persistent bottom-left "Get 15% Off" pill floats across all folds, competing for attention with the header trust bar (which already states "15% Off For New Customers"), creating redundant discount messaging in two places at once. Trust stack is dense: header trust bar, athlete quote, press logos, UGC carousel, all before any product differentiation.

**Collection page:** This is a category-index page (ranges, not individual SKUs), reaching the footer in 2 folds. No compare-at/strikethrough pricing shown on cards, only a single "From £X.XX," and review counts are aggregated per category rather than per product, so users can't judge a specific SKU's social proof before clicking in. The "FREE WATER BOTTLE When You Subscribe" banner sits below the fold on most viewports given the short page length.

**PDP:** Buy box defaults to "Subscribe & Save 20%" (£31.99, blue border, visually emphasized) over "One-time purchase" (£39.99, plain border, unselected) — a strong, deliberate visual hierarchy toward subscription. No compare-at price shown directly in the buy box itself (only per-stick pricing), even though the cart later shows a struck-through £39.99 against £31.99 for the same product — the discount framing that appears in the cart is absent at the point of add-to-cart decision. Fold 2's video/image module is largely blank, showing only a partial hand-holding-product visual in one corner — flagged as unconfirmed whether this is a live layout bug or a capture artifact (see Open Questions in manifest). Add to Cart is a full-width static button, not sticky, so once a user scrolls into the tabbed content, feature icons, or testimonials on fold 2-3, the primary conversion action is off-screen with no persistent path back to it.

**Cart:** Well-built AOV mechanics — free-shipping progress bar, free gift tied to cart contents, one-click "Still Thirsty?" cross-sell add-ons. Struck-through pricing (£39.99 → £31.99) is visible here, in contrast to its absence on the PDP buy box itself.

## Cross-Source Themes

1. **Sticky CTA absence across the funnel.** All three Meta LP templates, the homepage, and the PDP place the primary CTA statically, non-sticky. This is the single most consistent structural gap — it appears on every page type screenshotted (homepage, PDP, all 3 LP templates). Evidence: meta-ads-visual-summary.md, site-visual-summary.md (homepage, PDP).

2. **Message match breakdown on the travel ad angle.** Ad 2's "2026 Travel Hack" hook has no landing page support (generic hero) and no Google Ads reinforcement — it's a paid-spend angle running with zero on-site or cross-channel backup. Evidence: meta-ads-visual-summary.md (Ad 2), google-ads-visual-summary.md.

3. **Discount framing inconsistency between PDP and cart.** The PDP buy box shows only per-stick unit pricing with no compare-at price, while the cart shows a clear struck-through discount (£39.99 → £31.99) for the identical product. The stronger, more persuasive price-anchor only appears after the primary purchase decision is already made. Evidence: site-visual-summary.md (PDP, Cart).

## Top Test Opportunities

**Sticky Add-to-Cart bar on PDP** — The PDP's full-width "Add to Cart" button is static within the initial buy box; once a user scrolls into the tabbed content, trust icons, or testimonial carousel on folds 2-3, there is no persistent path back to purchase. Evidence: site-visual-summary.md (PDP fold 1-3). Est. lift: 2-4% CR lift x unknown sessions/mo x £30 AOV (sessions/mo not collected — directional estimate only pending traffic data).

**Add compare-at pricing to the PDP buy box** — The buy box shows per-stick unit pricing only (£1.07 vs £1.33) with no strikethrough discount, while the cart shows a clear £39.99 → £31.99 struck-through price for the same product. Surfacing the discount anchor earlier, at the add-to-cart decision point rather than only in cart, is a low-effort, high-precedent change (the asset already exists in the cart template). Evidence: site-visual-summary.md (PDP buy box detail, Cart). Est. lift: 1-3% CR lift on PDP-to-cart conversion x AOV £30-40.

**Rebuild Ad 2's landing page to match the travel hook** — "2026 Travel Hack" ad copy (hot-climate hydration, packing for a getaway) sends to the generic "Your Best Day, Every Day" homepage template with zero travel imagery, copy, or offer. This is the weakest message match of the three ads tested and is running unsupported by any Google Ads reinforcement. Evidence: meta-ads-visual-summary.md (Ad 2), google-ads-visual-summary.md. Est. lift: 10-20% relative CVR lift on Ad 2 traffic specifically (ad-level spend/CVR data not collected — directional only).

**Reduce redundant discount messaging on homepage** — The header trust bar already states "15% Off For New Customers," while a separate floating bottom-left "Get 15% Off" pill persists across every fold, duplicating the same offer in two visual locations. Testing consolidation (or differentiating the pill's offer, e.g., first-purchase vs. subscribe) could reduce visual clutter without removing the discount lever. Evidence: site-visual-summary.md (homepage CTA behavior). Est. lift: minor engagement/scroll-depth lift, not directly revenue-quantifiable from available data.

**Surface individual product ratings on the collection page** — Collection cards show review counts aggregated per category (e.g., "Rehydration & Recovery, 11,648 reviews") rather than per SKU, so a shopper can't compare a specific flavor or pack size's social proof before clicking through. Evidence: site-visual-summary.md (Collection page, Fold 1). Est. lift: 1-2% CR lift on collection-to-PDP click-through.

**Test one-time-purchase-first buy box variant** — The PDP defaults to "Subscribe & Save 20%" with strong visual emphasis (blue border) over "One-time purchase" (plain border, unselected). This is a deliberate, aggressive subscription nudge; testing a neutral-hierarchy variant (equal visual weight) against the current default would isolate how much of current subscription volume is genuinely preferred vs. defaulted into, and whether it's suppressing one-time buyers who bounce rather than opt out of a pre-selected subscription. Evidence: site-visual-summary.md (PDP buy box detail). Est. lift: directional only — could move AOV or CR in either direction; primary value is diagnostic data on subscribe-vs-one-time split.

**Fix or confirm PDP fold 2 video module** — The video/image module on PDP fold 2 renders mostly blank with only a partial visual in one corner. If this is a live bug (not a capture artifact), it's a broken content block sitting directly below the buy box on every PDP view. Evidence: site-visual-summary.md (PDP, layout anomalies). Est. lift: unquantifiable until confirmed live — flagged as a fix to verify before any test build, not a test itself.

**Differentiate Ad 3's advertorial CTA from ad copy** — Ad 3's landing page uses a long-form editorial format distinct from Ads 1-2's standard product template, with the primary CTA ("Get 15% Off Revival Shots") embedded mid-article rather than near the top. Testing CTA placement earlier in the advertorial (before section 2) against the current mid-article position could reduce drop-off from readers who don't scroll deep into listicle content. Evidence: meta-ads-visual-summary.md (Ad 3). Est. lift: 5-10% relative CVR lift on Ad 3 traffic.

**Test athlete/press trust block placement earlier on homepage** — Athlete endorsement (Hannah Cook) and press logos currently sit in fold 2, after the hero. Given press-as-seen-in and athlete credibility are strong differentiators not matched by SOS Rehydrate in competitor research, testing a condensed version of this trust signal in fold 1 (near the hero CTA) could reduce reliance on scroll-dependent trust building. Evidence: site-visual-summary.md (Homepage fold 1-2), competitor analysis. Est. lift: 1-2% CR lift on homepage-to-collection click-through.

**Add hot-climate/travel-specific product bundle or messaging module** — Rather than only fixing Ad 2's landing page (opportunity #3), test introducing a standalone travel/hot-climate messaging module (bundle or dedicated content block) sitewide, since this angle currently exists only as an isolated, unsupported ad creative with no on-site presence at all. This is the broader version of the Ad 2 landing page fix — same underlying gap, wider surface. Evidence: meta-ads-visual-summary.md (Ad 2), google-ads-visual-summary.md (no travel angle present). Est. lift: incremental new-angle traffic capture, not quantifiable from available data.

## Unused but Valuable Findings

- Collection page reaches the footer within 2 folds — unusually short for a category-index; may indicate insufficient content/differentiation per category to justify browsing before clicking into a range (open question flagged in manifest, not independently verified against live site).
- Cart's "Still Thirsty?" cross-sell module with one-click "Add" buttons is a well-executed AOV mechanic already in place — worth noting as a pattern to replicate elsewhere (e.g., PDP) rather than a problem to fix.

## Missing Data

- MISSING_DATA: reviews — no customer review data collected. On-site and third-party review sentiment (what drives satisfaction or complaints) cannot be evaluated, limiting the audit's ability to validate the review-count claims used heavily in trust messaging.
- MISSING_DATA: pagespeed — no PageSpeed/Core Web Vitals data collected. Site performance, load times, and CLS cannot be evaluated, and the PDP fold 2 video module issue cannot be diagnosed as a performance vs. layout problem without this data.
- MISSING_DATA: competitor_insights — no client-provided competitor file existed; competitor analysis in this audit is fully self-researched and should be validated against client's actual tracked competitor set.
- MISSING_DATA: landing_page_urls — Meta ad landing pages were captured as screenshots only, so live-fetch verification of full-page content beyond fold 3 was not possible.

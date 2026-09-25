# LABAREAU CRO Research Audit

## Data Sources Used

User-provided: Meta ad creatives + landing page screenshots (3 ads), Google Ads Transparency screenshots (2), Trustpilot review text (raw/reviews.md), Lighthouse PageSpeed JSON (homepage + PDP), brand strategy context (revenue-per-click metrics, four priorities), site screenshots (homepage, collection, cart drawer).

Self-researched: Live homepage fetch (2026-09-11), automated last30days-ecom social/web research (TikTok, Instagram, Pinterest, Trustpilot, web — 2026-09-11), competitor pricing via WebSearch (2026-09-11).

## Source Findings

### Meta Ads & Landing Pages

Three ads, three different destinations, three different message-match outcomes.

**Ad 1** promotes a specific bundle ("AHA Peel & The Toner, 14% korting") but lands on The Toner's single-unit PDP. The 14% bundle offer isn't visible above the fold — it's buried in a bundle module further down the page, under a different visual treatment than the ad's headline offer.

**Ad 2** is the strongest match in the set. It promotes premium collagen, Matrixyl®, and elasticity claims and lands directly on The Rich Cream PDP, whose benefit list echoes those same terms (Matrixyl Morphomics, Huididentiek Collageen). The ad sends traffic to the exact product it describes.

**Ad 3** promotes a "perfect anti-aging product" discovery narrative with a testimonial quote and specific claims (huidbarrière, fijne lijntjes) but lands on a single-fold skin-quiz interstitial with no product, pricing, reviews, or restated claims — just five quiz-answer buttons and a "Shop LABAREAU" text link. Whether the quiz eventually routes to a matching product can't be assessed from this capture, but the immediate landing experience delivers none of the ad's specific promises.

This is the second data source pointing at the same problem the brand's own context notes flag: traffic lands on generic pages regardless of the angle that earned the click.

### Google Ads

Google runs a distinct set of angles not present in the Meta creative: third-party medical authority ("Aangeraden Door Artsen" — recommended by doctors, dermatologists, surgeons), a 4-star/168-review rating badge, and an age-specific "oudere huid" (older skin) framing. None of the 11+ ad units carry a visible discount or bundle offer — Meta's active 14% bundle and €100+ gift threshold have no Google equivalent. Shopping tiles use "[Prijs]" placeholders suggesting dynamic pricing rather than a fixed promotional price. The two channels are running on different message systems: Meta on testimonial urgency and time-bound offers, Google on authority and prestige positioning.

### Reviews & UGC

#### What Customers Love
- Visible skin change described in specific, short timeframes: "within 3 days the redness on my face has subsided" (Val Markou, 4★), "immediate improvements... after using Labareau for just a week" (Bo, 5★)
- Repeat-purchase and loyalty language across a two-year span: "have been a fan for over 2 years" (Sara); "I've been using this brand since it first launched" (Karima)
- The Rich Cream and The Toner draw named-product praise: "have been extremely satisfied with the deep hydration and glow it provides" (Agni, on The Rich Cream)
- Customer service and delivery speed called out positively multiple times independent of product feedback (Marja, A.)

#### What Frustrates Customers
- Price is the single recurring complaint, always paired otherwise-positive reviews: "a bit pricey unfortunately" (Val Markou); "the price, especially considering the products only last for six months once opened" (Karima); "I hope there are some discounts like other companies so that we can always buy" (Hasna Qatto)
- Multiple reviewers explicitly ask for more frequent promotions — directly contradicting the brand's own stated Priority #1 to move away from discount-dependency (raw/context.md): customers are asking for the exact mechanic the brand wants to reduce reliance on.

#### Client-Actionable Insights
- Karima's complaint that products "only last for six months once opened" paired with the price objection suggests a perceived value gap on cost-per-use, not product efficacy — worth testing pack-size or refill options rather than discounting.
- Labareau's own reply to Karima says "keep an eye on our newsletter as we always announce promotions there first" — this is a retention/list-building lever already in use but not visible anywhere in the collected ad or site screenshots.

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON, mobile, fetched 2026-09-11.

| Page | Score | LCP | CLS | TBT | FCP |
|---|---|---|---|---|---|
| Homepage | 52/100 | 5.2s | 0.105 | 480ms | 3.6s |
| PDP — The Rich Cream | 38/100 | **19.7s** | 0.001 | 790ms | 4.6s |

The PDP's 19.7s LCP is not a borderline issue — it is roughly 4x Google's "poor" threshold (2.5s). Every Meta ad in this audit routes directly or indirectly to a PDP template (Ad 1 and Ad 2 land on PDPs; Ad 3's quiz likely resolves to one). Paid traffic is landing on the single slowest template on the site.

### Competitor Analysis

Self-researched, 2026-09-11 (WebSearch — no user-provided competitor file existed for this brand).

| Brand | Positioning | Price point | Notes |
|---|---|---|---|
| **Labareau** | Dutch clinical/luxury, SAXZ-12 patented formula, doctor-recommended messaging | The Rich Cream €119 (sale €104) | DTC + De Bijenkorf, founded 2021 |
| **Augustinus Bader** | Doctor-created, clinical/biotech positioning | The Rich Cream ~€265/50ml | Same product name as Labareau's flagship — direct naming overlap in a premium category |
| **Dr. Barbara Sturm** | Doctor-created, clinical/anti-aging | Hyaluronic serum ~€300 | Similar "recommended by doctors/dermatologists" authority angle to Labareau's Google ads |
| **111Skin** | Clinical, masks/treatments focus | ~€170 for a mask pack | Lower single-item price point, treatment-led rather than moisturizer-led |

Labareau sits meaningfully below its closest positioning peers on price while using near-identical authority claims ("recommended by doctors," clinical formula, patented technology name). That gap is untapped: the brand could lean harder into "clinical-grade at accessible price" as an explicit comparison rather than only running generic doctor-endorsement copy.

### Non-Data Context

Brand-provided strategy notes (raw/context.md) reframe the whole audit: September's dip is not a conversion problem. Site CR is a stable 2.5%, matching pre-giveaway performance, and AOV is slightly higher. The entire problem is on the buy side — CTR down 36%, CPC up 43% post-giveaway, producing a 27% revenue-per-click decline (€14.49 → €10.56, 25-31 Aug vs. 1-4 Sept). This means CRO work here should be judged primarily by its effect on revenue-per-click and post-click conversion, not by homepage CR alone — the brand explicitly named "landing pages per angle and persona" (message-match to the ad) as their #2 priority, which lines up directly with the Meta Ads message-match gaps found above.

Discount dependency is already flagged internally: discount share of gross revenue rose from 12% to 20.5% while volume halved — corroborated independently by reviews asking for more discounts (see Reviews section) and by Meta's Ad 1 leading with a 14% bundle discount as its primary hook.

### Social & Community Research

Findings here are third-party/directional except where corroborated elsewhere in this audit.

- TikTok's single highest-engagement post in the last 30 days (61,208 views, 459 likes) is a giveaway announcement ("9 winners, over €5,400 in prize value," posted 2026-08-13). This is the same giveaway mechanic the brand's own context notes credit for August's record 200k month — first-party revenue data and third-party engagement data agree that giveaways currently outperform evergreen content for this brand.
- The live homepage fetch (2026-09-11) shows an active "WIN 1 VAN 9 LUXE PRIJSPAKKETTEN" banner ending "Monday" — confirming the TikTok giveaway is still running site-wide as of this audit, not a one-off campaign moment already over.
- Trustpilot and Instagram reel content could not be pulled (both 404s from the automated engine) — flagged as a tooling gap, not a signal about actual sentiment or activity. A live Trustpilot profile is confirmed to exist but review-level content is unconfirmed by any source in this audit.

### Current Site Screenshots

**Homepage (screenshots, undated capture):** Hero promotes the same Toner gift-at-€100 mechanic seen on the PDP and cart ("DE TONER KRIJG JE VAN ONS!"), plus a "Recommended by doctors" line and Trustpilot rating ("Uitstekend 4.7 uit 5 ★"). Two stacked banners (rotating announcement + persistent gift-threshold bar) sit above the main nav, pushing the hero further down. **Live check (2026-09-11):** the current homepage carries an additional giveaway banner ("WIN 1 VAN 9 LUXE PRIJSPAKKETTEN," ending Monday) and shows "15 verkocht in het afgelopen uur" urgency copy and "77 totaal beoordelingen" on a featured product — none of which appear in the captured screenshots. The site's promotional state has changed since the screenshots were taken; treat the screenshot-based homepage findings as directionally correct on layout/hierarchy but not current on active offers.

**Collection page:** "Alle Producten" grid, 24 products, sidebar filters (price slider, product type, skin concern, skin sensitivity, availability — "Op voorraad (23)," "Niet op voorraad (2)"). Star ratings on every card are visual-only with no printed review count, unlike the homepage and PDP where review counts are shown — an inconsistency in how proof is presented depending on where a shopper is in the funnel.

**PDP:** Not separately captured (per manifest, Ad #2's landing folds serve as PDP evidence — see Meta Ads section above for buy-box detail on The Rich Cream). No PDP screenshots exist for any product besides The Rich Cream.

**Cart (drawer):** Two items shown (The Rich Cream €119, The Toner struck through to €0,00 as the unlocked free gift). A "Kies je gratis sample!" module offers three free sample tiles between the cart items and checkout. No guarantee, returns, or shipping-time copy is visible anywhere in the cart drawer capture — the only trust signal present at this late-funnel step is the row of payment icons under the checkout button.

## Cross-Source Themes

1. **Message match breaks between ad promise and landing destination, worst on Ad 3, present on Ad 1.** Evidence: Meta Ads visual summary (all three ads), brand's own Priority #2 (raw/context.md) naming this as the top untapped lever, Google Ads' distinct third unaddressed angle set (doctor authority, age-specific framing) with no matching landing experience captured.
2. **PDP load speed is severe enough to be losing paid traffic before it can convert.** Evidence: Lighthouse PDP score 38/100, 19.7s LCP; two of three Meta ads and likely the Ad 3 quiz funnel route to PDP templates.
3. **Discount dependency is a known, self-identified problem that reviews and ad creative both reinforce rather than resist.** Evidence: brand context (discount share 12%→20.5% of revenue), reviews asking for "more discounts," Ad 1 leading on a 14% bundle discount as the primary hook.

## Top Test Opportunities

**Fix Ad 3's landing destination to restate the ad's specific claims** — Ad 3 promises "perfect anti-aging product" discovery and specific claims (huidbarrière, fijne lijntjes) but the quiz interstitial it lands on shows no product, price, review, or restated claim — the biggest message-match break in the set. Evidence: Meta Ads visual summary (Ad 3), raw/context.md Priority #2. Est. lift: conservative 10% CR lift on Ad 3 traffic x unknown sessions/mo x unknown AOV = [data unavailable — sessions/mo and Ad 3-specific traffic split not collected].

**Move Ad 1's bundle offer above the fold on its landing PDP** — the ad's headline hook ("AHA Peel & The Toner, 14% korting") isn't visible until shoppers scroll past the single-unit buy box; the bundle discount structure shown on-page also doesn't match the ad's framing. Evidence: Meta Ads visual summary (Ad 1). Est. lift: [data unavailable — no baseline CR split by ad].

**Address the PDP's 19.7s LCP before any other PDP-level test** — any conversion test on the PDP is capped by users abandoning before the page paints. Evidence: raw/pagespeed.md (Lighthouse: PDP score 38/100, LCP 19.7s vs. homepage's 5.2s). Est. lift: [data unavailable — requires dev audit to quantify, flagged as a prerequisite finding rather than a standard CRO test].

**Test a fixed evergreen offer against the recurring discount mechanic** — reviews ask for discounts, Ad 1 leads with one, and the brand's own numbers show discount share climbing from 12% to 20.5% of gross revenue while volume halved. Evidence: raw/context.md (Priority #1), raw/reviews.md (Hasna Qatto, Karima). Est. lift: brand's own estimate — "one extra euro per click shows up immediately" at current volume (raw/context.md); no independent CRO-side dollar figure available.

**Add a printed review count to collection-page cards** — homepage and PDP both show printed review counts (1141, 2382) next to star ratings; collection cards show visual-only stars with no count, weakening proof exactly where shoppers are comparing products. Evidence: raw/site-visual-summary.md (Collection Page vs. Homepage/PDP).

**Add guarantee/returns/shipping-time copy to the cart drawer** — no trust copy of any kind (returns, guarantee, delivery estimate) appears in the cart drawer capture, the last touchpoint before checkout; only payment-method icons are present. Evidence: raw/site-visual-summary.md (Cart section).

**Reconcile Google Ads' doctor-authority angle with an on-site proof point** — Google's "Aangeraden Door Artsen" (recommended by doctors) claim and 4-star/168-review badge have no equivalent trust element captured on the homepage or PDP beyond a generic "Recommended by doctors" line; competitor research shows Augustinus Bader and Dr. Barbara Sturm lean on the same doctor-created positioning at 2-3x Labareau's price point, suggesting the claim is underleveraged rather than overused. Evidence: raw/google-ads-visual-summary.md, competitor analysis (self-researched).

**Test a refill or smaller-format SKU against the price objection** — the only recurring product complaint in reviews pairs price with short shelf life once opened ("the products only last for six months once opened"), suggesting a cost-per-use framing problem rather than a pure price objection. Evidence: raw/reviews.md (Karima).

**Standardize accordion/description language to Dutch across the PDP** — Ad 2's landing page (The Rich Cream PDP) fold 3 shows four benefit tiles in English ("Native collagen," "Deep Hydration," "Clinically Proven") inconsistent with the rest of the Dutch-language page, a small but real language-consistency break on the site's best-message-match page. Evidence: raw/meta-ads-visual-summary.md (Ad 2, Landing Page Fold 3).

**Surface the newsletter/promotion-alert signup earlier in the funnel** — Labareau's own review reply tells a customer to "keep an eye on our newsletter as we always announce promotions there first," but no newsletter signup appears in any collected homepage, collection, or cart screenshot — a known retention lever not visibly placed anywhere in the captured funnel. Evidence: raw/reviews.md (Karima reply), raw/site-visual-summary.md (no signup module captured).

## Unused but Valuable Findings

- The live homepage fetch (2026-09-11) found urgency copy ("15 sold in the past hour") and a running giveaway banner not present in the static screenshots — worth a follow-up capture pass if the roadmap wants to test urgency-copy placement specifically, since current evidence is a single live snapshot rather than a repeated pattern.
- TikTok's giveaway content dramatically outperforms all other tracked content in engagement (61,208 views vs. next-best signal), independently confirming the brand's own framing that promotional mechanics currently outperform evergreen — relevant context for Priority #3 (top-of-funnel content) but not a site-side CRO test.

## Missing Data

- **PDP screenshots for any product besides The Rich Cream** — no standalone PDP captures exist; the site's other 23 products (per collection page count) have no direct PDP evidence in this audit.
- **Ad landing page URLs** — no raw/meta-ads.md with source URLs was collected, so ad landing pages could not be re-fetched live during this audit; findings rely entirely on the screenshots taken at collection time.
- **Trustpilot review-level content** — a live profile exists (confirmed by search precheck, 4.0–4.7★ across 245–382 reviews depending on snippet source) but no review text could be pulled by the automated engine (404). The Trustpilot rating shown on the live homepage (implied "Uitstekend 4.7 uit 5") is consistent with the upper end of this range but is not independently verified against the Trustpilot page itself.
- **Instagram reel content** — both confirmed-active accounts (@labareau, @labareauofficial) returned 404s from the automated fetch; no reel-level engagement or messaging data available.
- **Sessions/mo and AOV** — no traffic volume or average order value figure was provided, so dollar-value lift estimates above could not be calculated and are marked as unavailable rather than estimated.

# Performance Golf CRO Research Audit

## Data Sources Used

- Meta Ads and landing pages (3 ads, 2 unique landing pages, WebFetch supplement)
- Google Ads Transparency Center (screenshot review)
- Reviews (Amazon reviews for 357 Super 7-Wood, no on-site review data for RS1/SF2)
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP, mobile)
- Current site screenshots (homepage, collection, PDP, cart drawer) + WebFetch of live homepage
- Non-Data Context: 30-day Shopify business summary (2026-07-17 to 2026-08-16)
- Competitor Analysis: not collected (skipped per manifest)
- Emails: not collected (skipped per manifest)
- Inspiration Sites: not collected (skipped per manifest)

## Source Findings

### Meta Ads & Landing Pages

**Ad 1 (357 Fairway/Hybrid).** Creative leads hard on a senior-specific angle: "THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55," "A Brand New Concept of Club Designed For Seniors," "Voted #1 Approach Club For Amateurs." The landing page headline ("FIRST-EVER SUPER 7-WOOD WITH TRI-FUSION TECHNOLOGY") drops the senior framing entirely across the three captured folds. A visitor clicking on an age-specific promise lands on generic technology messaging with no reinforcement of "over 55" until deeper in the page. This is a message-match gap between ad and landing page above the fold.

**Ad 2 & 3 (SF2 Driver).** Both ads share one landing page (confirmed in manifest). Ad copy promises a specific, quantified benefit: "20-30 dead straight yards." The landing page headline and bullets reinforce the slice-fix and guarantee angle but do not repeat the "20-30 yards" figure on the captured folds — a softer version of the same message-match issue as Ad 1, on a numeric claim that ad platforms scrutinize for substantiation. Ad 3 adds a "$100 OFF" claim on the creative that does not appear anywhere in the shared landing page folds — a real, unresolved match gap. Live-fetched LP data confirms current pricing is $299 (marked down from $399, "$100 off"), so the LP substantiates the ad's flat $100 discount, but that price/discount is never shown in the specific ad-to-LP visual path collected. Flagging this as unverified rather than fixed, since only 3 folds were captured.

**Cross-ad observation.** Both landing pages use direct-response, long-form structures typical of paid acquisition (testimonials, bonus stacks, guarantee badges) but the live site (organic/homepage) uses a completely different design system, positioning ("Forward Axis Weighting" putter-first homepage vs. driver/wood-first ad landing pages), and no bonus stack. Traffic entering from ads and traffic entering from the homepage see two different brands.

### Google Ads

Google Ads Transparency Center shows text-ad variants for angles not present in the 3 collected Meta creatives: putter messaging ("World's Straightest Putter," "Not Another Zero Torque Putter"), instructional/drill hooks ("5 Min Drill Adds 15-25 Yards," "Finger Fix"), and multiple senior-fairway-wood text variants. One display ad extends the Tri-Fusion claim to a different product frame: "THE NEW FAIRWAY HYBRID REPLACES YOUR 3, 5 & 7 WOODS" / "Fastest Way To Shave 6 Strokes." Google's slice-fix ad text ("New Slice-Fix Driver – No Swing Changes Needed") is consistent with the Meta SF2 ads. Overall, Google Ads confirms the same core angles as Meta (senior distance, slice-fix, no-swing-change) but adds a putter angle and drill/instructional angle not represented in the Meta sample collected.

### Reviews & UGC

Only Amazon reviews for the 357 Super 7-Wood (Senior model) were collected — no review data exists for the RS1 Putter or SF2 Driver, the two highest-revenue products (70% of gross revenue combined per the business summary). Findings below are scoped to the 357 only.

#### What Customers Love

- Simplification of the bag: multiple reviewers mention removing 3-5 other clubs ("I took 5 clubs out of my golf bag and replaced them with this club," "The only wood you will need!")
- Easier contact / forgiveness for higher handicappers and seniors: "easy to hit," "consistently closer to the green," "especially good for the high handicapper and weekend warrior"
- Perceived credibility from strong first outings: one 5-star review describes shooting a 91 and crediting the club with saving "6 or 7 strokes"

#### What Frustrates Customers

- Distance underperformance versus ad claims: "It is OK but not as good as anticipated," "does not go farther than my 5 wood," "closer to a 7 wood than a 3 wood," "Same as a 3 wood... didn't help my game at all"
- Direct "not as advertised" complaints, including one flagged as "SCAM" and another "Not what advertised" (1-star, cites difficulty squaring the face, "tinny sound," "cheaply made")
- Durability: one reviewer's shaft "snapped after a few trips to the range"
- Shipping/quality control: "Was broked whene I received"
- UK reviews skew more negative/mixed than US reviews in this small sample, with complaints about price-to-performance ("Pricey," "If I could have my money back I would take it")

#### Client-Actionable Insights

- The gap between ad-promised distance ("flies as far as a 3-wood") and actual on-course performance is the single most repeated complaint theme. This is a product/marketing-claims issue, not a site UX issue — recommend the client review distance claims against the refund/complaint pattern before further ad spend on this angle.
- Quality control on shafts and shipping damage appeared in this small sample; worth a client-side check with fulfillment/QC given it surfaces unprompted in organic reviews.
- No review data exists for RS1 Putter or SF2 Driver despite being 70% of revenue — recommend the client start actively collecting/displaying on-site reviews for these two products specifically, since the PDP screenshot shows only a generic "4.8 based on 3,700+ reviews" for the 357, and live-fetched pages cite "76,744 Happy Golfers" for SF2 with no visible on-site review widget.

### PageSpeed / Core Web Vitals

Data collected: mobile Lighthouse audits, homepage and PDP (357 Super 7-Wood), pulled 2026-08-16.

| Page | Performance Score | LCP | CLS | TBT | Speed Index | Time to Interactive |
|---|---|---|---|---|---|---|
| Homepage | 20/100 | 5.6s | 0.638 | 1,100ms | 11.5s | 46.2s |
| PDP (357) | 21/100 | 4.6s | 0.637 | 1,780ms | 9.4s | 43.4s |

Both pages fail Core Web Vitals thresholds severely on mobile. Google's "good" thresholds are LCP ≤2.5s, CLS ≤0.1, and the sites are roughly 2x over on LCP and more than 6x over on CLS. A CLS of ~0.64 on the PDP is consistent with what the site-visual-summary describes as a buy box that likely shifts during load (variant selectors, sticky bottom bar appearing). Time-to-interactive above 43 seconds on both pages indicates heavy JS blocking — the 1,100-1,780ms total blocking time confirms this. This is a severe, sitewide technical issue affecting every paid-traffic session on mobile, not an isolated page problem.

### Competitor Analysis

Not collected. Skipped per manifest (Sources Skipped: Competitor Insights). No self-research substitute was run for this section since the audit scope did not include it as a selected source; flagging as a gap below rather than fabricating competitor data.

### Emails

Not collected. Skipped per manifest.

### Inspiration Sites

Not collected. Skipped per manifest.

### Non-Data Context (30-Day Business Summary)

Source: Shopify Admin API pull, 2026-07-17 to 2026-08-16, 10,558 live orders, $2,514,819.85 gross revenue, $238.19 AOV (gross), $220.93 AOV (merchandise only).

**Volume-up, value-down trend.** Orders climbed 30% week-over-week across the four-week window (2,248 → 2,929) while AOV fell 30% from its peak ($282.09 → $196.60). Revenue stayed flat ($555k-$637k/week). The most recent week set both the volume record and the AOV floor simultaneously — this is a mix shift toward cheaper orders, not underlying growth.

**Catalogue concentration.** RS1 Putter alone drives 49.4% of gross revenue; RS1 + SF2 Driver together drive 70.0%. Both are addressed in Meta ad creative (SF2) or homepage hero (RS1's "Forward Axis Weighting" positioning), so paid and organic traffic both converge on these two products.

**The free PG1 trial dominates order composition.** It attaches to 49.9% of all orders at $0 revenue. 6.0% of orders contain nothing but free items. Excluding free-only orders, AOV rises to $253.46. Of RS1 Putter orders, 69.6% also carry the free trial — the trial functions as a hardware-attach hook, not a standalone acquisition product.

**A live, unlabeled price test is running on the top product.** RS1 Putter sells at $399 and $429 in a near-even 50/50 split across all 31 days of the window. This is almost certainly an existing A/B/split-price test (tool unknown from this data) — worth surfacing to the client as an existing experiment to check before the new roadmap proposes anything conflicting on RS1 pricing.

**Cross-sell gaps.** Only 6.0% of club-buying orders contain 2+ clubs, but those orders average $556.69 vs. $346.03 for single-club orders (+$210.66). Hardware and digital-course catalogues almost never sell together (0.1% cross-attach) despite serving the same customer — a near-total funnel separation between physical products and digital coaching content.

**`/cart/clear` is the 4th-largest landing page** (1,137 orders), an unusual entry point suggesting a redirect/funnel mechanic rather than genuine landing traffic — flagged as an open question in the source data, not something this audit can resolve, but worth the client's attention since it sits ahead of major product pages in landing volume.

**Checkout abandonment skews toward expensive baskets.** Checkouts in the $300-500 band represent 46.9% of abandonments but only 28.2% of completed orders — high-ticket baskets (i.e., driver, putter, multi-club) are disproportionately likely to stall at checkout. 70.2% of all abandoned checkouts contain at least one club, worth $559,300 in the window.

**Facebook traffic converts to higher AOV.** Facebook-attributed orders (22.0% of total) carry a $346.06 AOV, 45% above the site average — consistent with the direct-response, bonus-stacked landing pages being effective at driving higher-intent purchases, in contrast to the untagged/no-UTM traffic (63% of orders) at $201.07 AOV.

### Current Site Screenshots

**Homepage.** Hero leads with the RS1 Putter ("YOUR STROKE ISN'T THE PROBLEM. YOUR PUTTER IS.") and "Forward Axis Weighting" technology explainer, with a single CTA "SEE HOW IT WORKS." No sticky header CTA. Trust signals (4.8 rating, 1M+ subscribers, 800K clubs sold) don't appear until fold 3, well below the fold, and are styled as light-gray monospace numbers rather than prominent proof — a low-visual-weight treatment for what should be a leading trust signal, especially since this business has no site-wide review widget on the homepage. The homepage's product-line breadth (nav includes PG1 App, Clubs, Training Aids, Supplements, Coaching, Testimonials) is a different funnel model entirely from the direct-response, single-product ad landing pages, creating a disconnect for any paid visitor who returns to the homepage.

**Collection page ("GOLF CLUBS").** Standard 3-column grid with compare-at pricing and "Save up to X%" badges on most cards. Notably, RS1 Putter — the highest-revenue product at 49.4% of gross — shows no discount badge ("From $399.00") while nearly every other product on the grid shows a strikethrough/percent-off badge. This creates a visual inconsistency where the flagship product looks comparatively more expensive with no offer, next to lower-ticket items that all show savings.

**PDP (357 Super 7-Wood).** Buy box includes star rating (4.8, 3,700+ reviews) and "IN STOCK" badge near the top, hand/shaft-flex variant selectors, a single one-time-purchase-only CTA ("ADD TO CART"), and a free-trial bonus bullet embedded in the checklist rather than as a separate visual callout. A sticky bottom Add-to-Cart bar appears once the user scrolls to fold 3. Given the PageSpeed CLS score of 0.637 on this exact page, elements in this buy box (variant selectors, sticky bar appearance) are very likely shifting position during load, which both frustrates users and directly costs Core Web Vitals ranking signal.

**Cart (drawer).** Right-side slide-out with free-shipping progress messaging and a subtotal breakdown showing the discount already applied. The free PG1 trial appears as its own line item ("100% OFF" badge) inside the cart, which is good transparency, but the "YOU MAY ALSO LIKE" cross-sell module was captured empty (no products shown) — directly relevant to the 30-day data point that only 6.0% of club orders contain 2+ clubs despite a documented $210.66 AOV lift when they do, and that hardware and digital courses almost never sell together.

## Cross-Source Themes

1. **Mobile performance is failing across every paid-traffic entry point.** Both homepage and PDP score ~20/100 on mobile Lighthouse with CLS over 6x the "good" threshold, and the PDP's likely-shifting buy box directly overlaps with the highest-revenue funnel step. Evidence: PageSpeed data (severe, quantified), site screenshots (buy box behavior consistent with the CLS score), 30-day data (Facebook traffic — the largest paid source — converts at 45% above average AOV, meaning fixing performance protects a high-value segment). Revenue potential: high, funnel-wide. Fixability: high (known CWV remediation playbook).

2. **Cross-sell and bundle mechanics are essentially absent despite proven upside.** The 30-day data quantifies a $210.66 AOV gap between single- and multi-club orders (only 6.0% of club orders), a 0.1% cross-attach between hardware and digital courses, and an empty "YOU MAY ALSO LIKE" cart module in the actual site capture. Evidence: business summary (quantified), site screenshots (empty cross-sell slot), PDP screenshot (no bundle/subscription option, single SKU purchase only). Revenue potential: high, directly quantified. Fixability: medium (requires merchandising + dev work, not just copy).

3. **Message match between paid ads and landing pages/homepage is inconsistent, and flagship products (RS1, SF2) lack the review/trust proof that lower-tier products show.** Evidence: Meta ads visual summary (senior angle dropped on Ad 1 LP, $100-off claim unresolved on Ad 3 LP), reviews (zero review data exists for the two products driving 70% of revenue), collection page (RS1 shows no discount badge unlike nearly every other product). Revenue potential: medium-high, concentrated on the highest-revenue SKUs. Fixability: high (largely copy/UI, not technical).

## Top Test Opportunities

**Fix PDP layout shift and mobile load speed on top-selling club pages** — The PDP scores 21/100 on mobile Lighthouse with CLS 0.637 (6x over Google's "good" threshold of 0.1) and 43.4s time-to-interactive; the buy box (variant selectors + sticky Add-to-Cart bar) is the visible element most likely shifting during load. Evidence: raw/pagespeed.md (Lighthouson JSON), site-visual-summary.md. Est. lift: 1% CR lift x ~10,500 orders/mo x $238 AOV = ~$25,000/mo (conservative CWV-based estimate; no baseline session/CR data available per manifest caveats).

**Add cross-sell module to cart drawer for multi-club bundling** — The cart drawer's "YOU MAY ALSO LIKE" section is empty in the current build; 30-day data shows multi-club orders average $556.69 vs. $346.03 for single-club orders, a $210.66 gap, but only 6.0% of club orders contain 2+ clubs. Evidence: raw/site-visual-summary.md (cart), raw/context.md (30-day data). Est. lift: converting even 2% of single-club orders (6,027/mo) to multi-club at the existing gap = 6,027 x 0.02 x $210.66 ≈ $25,400/mo.

**Restore senior-specific messaging on the 357 Fairway Wood landing page** — Meta Ad 1 leads with "THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55," but the landing page headline drops this framing entirely across 3 captured folds in favor of generic "Tri-Fusion Technology" messaging. Evidence: raw/meta-ads-visual-summary.md, WebFetch of live LP. Est. lift: 0.5% CR lift x 851 orders/mo (357 product volume) x $249 AOV ≈ $1,050/mo direct, though real impact is likely larger via improved ad-to-LP relevance/CPA (not quantifiable from available data).

**Add on-site review display to RS1 Putter and SF2 Driver PDPs** — These two products drive 70.0% of gross revenue but have zero visible on-site review collection; the only review data collected in this audit was for the lower-revenue 357 Super 7-Wood via Amazon. Marketing copy cites "76,744 Happy Golfers" for SF2 without an on-page review widget. Evidence: raw/reviews.md (scope gap), raw/meta-ads-visual-summary.md, live LP fetch. Est. lift: 0.5% CR lift x (2,986+1,717) orders/mo x ~$350 avg AOV for these SKUs ≈ $8,200/mo.

**Resolve the Ad 3 "$100 OFF" message-match gap on the shared SF2 landing page** — Ad 3's creative headlines "CLAIM YOUR $100 OFF," but the captured landing page folds (shared with Ad 2) show no $100-off callout, only the general sale price. Evidence: raw/meta-ads-visual-summary.md. Est. lift: not independently quantifiable (Ad 2/3 share landing volume: 920 orders, $306,784.94 revenue per landing-page data) — flagged primarily as a paid-media compliance/trust risk rather than a pure CRO lift play.

**Add a discount badge to the RS1 Putter collection card** — On the collection page, RS1 Putter is the only major club shown without a "Save up to X%" badge, while nearly every other product carries one, making the top-revenue product look comparatively worse-value in-grid. Evidence: raw/site-visual-summary.md (collection). Est. lift: 0.3% CR lift x 2,986 orders/mo (RS1 volume) x $414 avg RS1 price ≈ $3,700/mo.

**Add explicit sale messaging on homepage hero to match ad-driven expectations** — Homepage hero (RS1 Putter/"Forward Axis Weighting") shows no price, discount, or urgency messaging, while all three Meta ad landing pages lead with strikethrough pricing and urgency ("Summer Sale Ends Soon"). Visitors who click from an ad, don't convert, then return organically to the homepage see a colder, unmatched experience. Evidence: raw/site-visual-summary.md (homepage), WebFetch of live homepage, raw/meta-ads-visual-summary.md. Est. lift: not independently quantifiable — homepage lands 1,863 orders/$407,513 per landing-page data, but no session-level data exists to isolate returning-visitor impact.

**Introduce a bundle/subscription option on the 357 PDP** — Site-visual-summary confirms the 357 PDP offers only a single one-time-purchase option, no subscription or multi-club bundle, despite the 30-day data showing a proven $210.66 AOV lift for multi-club orders. Evidence: raw/site-visual-summary.md (PDP buy box detail), raw/context.md. This is the PDP-level, narrower version of the cart cross-sell opportunity above — kept as a backup slot since the cart-level fix addresses the same mechanic across all products.

## Unused but Valuable Findings

- Order landing page `/cart/clear` is the 4th-largest landing page (1,137 orders) — an unusual redirect/funnel mechanic worth investigating before any checkout-flow test is designed, since it may be inflating or distorting checkout funnel assumptions.
- A live, unlabeled 50/50 price test appears to already be running on RS1 Putter ($399 vs. $429) — any new RS1 pricing test should first confirm this existing test isn't still live to avoid conflicting experiments.
- The PGSUPPORT discount code family carries unusually high AOVs ($222-$337) and appears to be customer-service issued — worth understanding as a retention/service lever, not a CRO lever.

## Missing Data

- **Competitor Analysis:** Skipped per manifest (Sources Selected did not include it). No competitive pricing/positioning benchmark is available for this audit.
- **Reviews for RS1 Putter and SF2 Driver:** Only 357 Super 7-Wood review data was collected. Given RS1 + SF2 drive 70% of revenue, this is a meaningful gap — the "What Customers Love/Frustrates" findings above cannot be assumed to generalize to the flagship products.
- **Session/traffic data:** Per business-summary caveat #4, the client has no Google Analytics or Clarity export, so no site-wide conversion rate, bounce rate, or funnel-step data exists. All lift estimates above are anchored to order volume, not session volume, and are directionally conservative rather than precise.
- **Emails and Inspiration Sites:** Skipped per manifest; no findings possible in these areas.

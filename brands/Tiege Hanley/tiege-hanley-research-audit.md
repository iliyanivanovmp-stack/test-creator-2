# Tiege Hanley CRO Research Audit

## Data Sources Used

- User-collected Meta Ads Library creatives and landing-page screenshots, captured July 1, 2026
- User-collected Google Ads Transparency screenshots, captured July 1, 2026
- User-collected Amazon reviews dated July 2019-June 2026
- Mobile Lighthouse/PageSpeed reports for the homepage and bundle builder, collected July 1, 2026
- User-collected homepage, Level 1 PDP, and cart-drawer screenshots, captured July 1, 2026
- Live text fetch attempts for `tiege.com` and the bundle-builder URL on July 1, 2026; neither returned usable text, so no unseen live UI is described
- Self-researched official competitor catalog data from Geologie, Lumin, and Brickell, researched July 1, 2026

## Source Findings

### Meta Ads & Landing Pages

Ad 1 promises “Weeks. Not Months. Clinically proven. For men.” and visually frames the product as uncomplicated. Its bundle-builder landing page instead leads with “Up to 40% Off Premium Skin Care,” a free gift over €25, and a multi-step product-selection grid. The clinical proof, time-to-result claim, and uncomplicated positioning are absent above the fold. Requiring a visitor to select products and understand 5%-20% bundle tiers adds decision effort immediately after an ad promising simplicity.

Ad 2 claims “95% of men saw noticeable improvements with consistent routines.” The identical bundle-builder destination does not repeat the 95% statistic or explain the evidence behind it above the fold. The strongest click-driving proof is therefore lost at the transition.

Ad 3 promises a “Full system, nearly half the price” and sends traffic to the general homepage. “Start Today and Get Up To 40% Off!” preserves broad value framing, but neither the competitive comparison nor “full system” proposition is explained in the hero. Across all three ads, landing destinations prioritize a discount over the creative’s proof and simplicity claims.

### Google Ads

Search, Shopping, display, and video units consistently use “uncomplicated,” “made easy,” and “skin care that works.” One visible search unit shows 4.6 stars from 537 reviews. No explicit discount appears in the collected Google copy, while the homepage and Meta destinations lead with up to 40% off. The cross-channel brand promise is simplicity and results, but the onsite entry experience primarily communicates price promotion. Educational ads on acne scars, pores, and weight loss also introduce visitors at different awareness levels without evidence in the collected landing-page set that the entry experience adapts to their intent.

### Reviews & UGC

The collected Amazon review set spans July 2019-June 2026; it is qualitative and not a representative rating distribution.

#### What Customers Love

- Simplicity is the clearest repeated advantage. One July 2024 buyer wrote, “The routine is straightforward and easy to follow. No more guessing which product to use when.”
- Customers report softer, smoother, clearer, and better-hydrated skin. A December 2023 reviewer said the system “Clears up any possible bumps and cleans my face nicely,” while a January 2026 gift recipient showed “Clearer looking skin.”
- Labels, included instructions, and AM/PM structure reduce beginner anxiety. A May 2026 reviewer described it as “sencillo y práctico” and praised instructions explaining exactly how and when to use each product.
- Packaging and gifting appeal recur, as do positive comments about the face wash, lightweight moisturizers, and non-greasy finish.

#### What Frustrates Customers

- Perceived quantity-to-price value is the dominant objection. Reviews call the bottles “tiny,” “skimpy in size,” and “not worth the price”; a February 2026 reviewer believed a claimed 30-day supply contained “maybe 2 weeks of product.”
- Some buyers see insufficient differentiation from cheaper CeraVe, Neutrogena, Cetaphil, or La Roche-Posay alternatives. A January 2026 reviewer found the system convenient but saw no major change in oil control, pores, or skin tone after one month.
- Product-tolerance concerns include dryness, oily AM moisturizer, eye burning, an abrasive scrub, and SPF20 being perceived as inadequate. These are individual reports, not clinical findings.
- Purchase-channel and fulfillment friction includes an Amazon coupon that reportedly failed, a $15 channel-price difference, separate shipments, and limited size/refill choices.

#### Client-Actionable Insights

- Make 30-day usage assumptions auditable: show exact volumes, per-use amounts, expected applications, and a clear replacement policy when a kit does not last as directed.
- Review scrub abrasiveness, SPF positioning, and irritation guidance with product/regulatory teams; make contraindications and application instructions prominent.
- Reconcile Amazon/direct pricing and coupon behavior, and give support a defined response for price discrepancies.
- Evaluate larger sizes or refill formats because quantity flexibility appears repeatedly in reviews from 2019-2026.

### PageSpeed / Core Web Vitals

Both reports are simulated mobile Lighthouse runs collected July 1, 2026, not field Core Web Vitals. No desktop reports or field INP data were collected.

| Page | Performance | FCP | LCP | Speed Index | TBT | CLS |
|---|---:|---:|---:|---:|---:|---:|
| Bundle builder | 27/100 | 5.1s | 38.7s | 18.8s | 3,090ms | 0 |
| Homepage | 28/100 | 5.0s | 22.3s | 12.7s | 2,360ms | 0 |

The bundle builder is the more commercially urgent page because Ads 1 and 2—the stated highest-traffic receivers—send traffic there. Its 38.7-second LCP and 3.09-second TBT can delay both the offer and interactive product selection. Lighthouse estimated 7.69 seconds of savings from reducing unused JavaScript on the bundle builder and 1.95 seconds on the homepage. CLS was 0 in both lab runs, so instability was not the observed problem; rendering and main-thread blocking were.

### Competitor Analysis

No competitor file was user-provided. The following was independently researched from official storefront catalog data on July 1, 2026; listed prices are snapshots and may reflect promotions.

| Brand | Comparable official offer | Price observed | Key differentiation | Relative weakness/opportunity for Tiege |
|---|---|---:|---|---|
| Geologie | 30-Day Hero Set / personalized regimens | $49 / $99 classic set | Regimen numbers, personalization, dermatologist-designed positioning, 60-second routine language | Higher full-regimen price gives Tiege room to substantiate its value, but Geologie makes personalization more explicit |
| Lumin | Smooth Operator Detox Trio | $63 | Concern-led trios, free-trial funnel, 10% subscription messaging | Tiege’s four-product $45 one-time Level 1 is lower priced, but Lumin’s concern-based naming reduces product-selection ambiguity |
| Brickell | Daily Advanced Face Care Routine Bundle | $49.20 | Natural/premium men’s grooming positioning and full-size routine framing | Close price makes Tiege’s small-volume perception more exposed unless duration and efficacy are explained |

Tiege’s defensible distinction is not merely low price: it is a pre-structured, beginner-friendly AM/PM system. The current bundle-builder entry point weakens that distinction by asking cold traffic to construct a routine before reinforcing why the system works.

### Emails

Not collected; subject lines, lifecycle CTAs, offer continuity, and post-click message match could not be evaluated.

### Inspiration Sites

Not collected; no external UX patterns were imported into these findings.

### Non-Data Context

The manifest identifies Meta Ad 1 and Ad 2 landing pages as the highest-traffic receivers and allows three test slots with one variation each. No call notes, strategic objections, AOV, traffic volume, or analytics context were collected.

### Current Site Screenshots

**Homepage.** The full-viewport hero contains a lifestyle image, “Start Today and Get Up To 40% Off!”, and one green “START NOW” CTA. It does not explain the routine, product set, expected result, or 26,000-review proof above the fold. Routine levels and the 4.7-star/26,525-review badge arrive in fold 2; before/after evidence appears in fold 3. The hierarchy makes the brand look discount-led before it looks simple or proven.

**Collection page.** Not collected, so filtering, product-card clarity, and PLP conversion friction cannot be evaluated.

**PDP.** The Level 1 buy box clearly presents 30/90-day supply, subscription versus one-time purchase, $35 subscription versus $45 one-time pricing, free shipping, cancellation, guarantee, ratings, and a persistent CTA. However, the screenshot shows 2.5 fl oz wash plus three 0.75 fl oz products without explaining in the buy box how those sizes last 30 days. That omission directly intersects with the strongest review objection. Results thumbnails are small, while fuller before/after and philosophy content appear farther down. Subscription is preselected and dominant; clarity is good, but visitors skeptical of value receive no usage math near the decision.

**Cart.** The drawer confirms free shipping at $35, removing any remaining threshold incentive. A single eye-cream cross-sell is shown without a visible price, rationale, bundle saving, or direct add control in the captured view. The cart therefore creates little reason to increase order value after the threshold is already met.

## Cross-Source Themes

1. **Simplicity is promised and validated, but not consistently delivered at entry.** Meta, Google, reviews, and the PDP philosophy all support an uncomplicated routine; the bundle builder introduces choice before explaining a recommended path. This affects the highest-priority landing traffic.
2. **Proof is strong but arrives late or disappears after the click.** Ads use “clinically proven” and 95%; the site has 26,525 verified reviews and before/after assets; landing heroes lead with discounts instead. This is a high-funnel message-match problem with broad revenue exposure.
3. **Value skepticism is about quantity and efficacy, not just sticker price.** Reviews repeatedly question small bottles and comparative performance, while the PDP shows volumes but gives no 30-day usage proof near purchase. This directly affects purchase confidence and retention.

## Top Test Opportunities

**Proof-Matched Bundle Builder Hero** — The Ads 1/2 landing hero replaces “clinically proven,” “Weeks. Not Months,” and 95% improvement claims with a generic discount, forcing paid visitors to reconnect the promise themselves. Evidence: Meta ads, bundle-builder screenshots, site proof assets. Est. lift: 3% CR x unknown sessions/mo x unknown AOV = not calculable from collected data.

**Recommended Routine First** — The highest-traffic landing page opens into category tabs, routine tabs, a product grid, discount tiers, and an empty sticky routine, conflicting with the repeatedly validated “no guessing” benefit. Evidence: Meta ads, bundle-builder screenshots, Amazon reviews, Google ads. Est. lift: 2% CR x unknown sessions/mo x unknown AOV = not calculable from collected data.

**30-Day Quantity Proof in the PDP Buy Box** — The buy box displays small volumes beside a 30-day label but provides no per-use or duration explanation where repeated “tiny” and “not enough” objections are decided. Evidence: PDP screenshots, Amazon reviews dated 2019-2026. Est. lift: 1.5% CR x unknown sessions/mo x unknown AOV = not calculable from collected data.

## Unused but Valuable Findings

- The cart’s eye-cream recommendation lacks visible price and rationale, weakening a post-add AOV opportunity after free shipping is already achieved.
- Mobile lab performance is critically weak on both paid entry pages, especially the bundle builder at 38.7-second LCP.
- Product/support teams should independently investigate repeated scrub-irritation and SPF20 concerns before using stronger safety claims.

## Missing Data

- No collection-page capture: PLP layout, filtering, product-card, and navigation opportunities cannot be evaluated.
- No desktop PageSpeed or field Core Web Vitals: device comparison and real-user INP cannot be assessed.
- No analytics, monthly sessions, conversion rate, AOV, or revenue: opportunity dollar lifts cannot be calculated.
- No emails, inspiration sites, user-provided competitors, or non-data context were collected.


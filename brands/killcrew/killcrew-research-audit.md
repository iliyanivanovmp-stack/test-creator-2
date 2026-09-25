# Kill Crew CRO Research Audit

## Data Sources Used

**User-provided / collected:** Meta Ads Library screenshots and landing page folds (3 ads), Google Ads Transparency Center screenshot, customer reviews (killcrew.co product review widget), PageSpeed API data (homepage, PDP — mobile only), site screenshots (homepage, collection, cart drawer), non-data context notes.

**Self-researched:** WebFetch of live landing pages (reptile-shorts collection, floral-black PDP), WebFetch of live homepage, WebSearch for competitor brands (2026-09-10), last30days-ecom automated social/community research (TikTok, YouTube, Pinterest, Trustpilot, Web — 2026-09-10).

## Source Findings

### Meta Ads & Landing Pages

Three active Meta ads run since May–June 2026, all using the tagline "Fit and Comfort 100/10" and a "Shop Now" CTA.

**Ads 1 & 2** advertise a specific reptile-print shorts-and-tee set ("[ NEW REPTILE SHORTS ]," 4" inseam, mid-thigh fit) and both route to the same URL: the general reptile-shorts collection page. That collection page opens on a mixed grid of shorts and t-shirts in assorted prints — the exact colorway shown in either ad is not the first product visible. There is no message-match bridge (no "as seen in this ad" banner, no pre-filtered view) between the specific product in the ad creative and the broad collection it lands on. No trust signals (review count, star rating, guarantees) are visible in the first three folds of this landing page — the only visible credibility element is a "Free Shipping $75+" promo bar.

**Ad 3** advertises "Mid Thigh Cut Shorts" with squat-proof/chafe-proof double-layer mesh, and routes directly to the matching PDP (Muay Thai Shorts Floral - Black). This is the strongest message match of the three ads: headline claims, product description language ("squat proof, chafe proof, non sheer"), and the default product image/colorway all align with the ad. The PDP also carries the audit's strongest trust stack: 4.8 stars / 2,437 reviews shown twice on the page, a 6-icon trust bar directly under Add to Cart, and financing options (Shop Pay installments, Afterpay).

**Live-site discrepancy found during this audit (2026-09-11):** re-fetching Ad 3's PDP live shows the Floral - Black shorts are currently **out of stock** ("Notify me when available"), with a "3,456 people are currently viewing this product" urgency banner and a marked "on sale" price tag not present in the collected screenshots. If Ad 3 is still running traffic to this exact URL, that ad is currently sending paid clicks to a sold-out product page.

### Google Ads

Google Ads Transparency shows 10 active ad units spanning four distinct messaging angles not fully reflected in the Meta creative: (1) mental-health/self-care framing ("Selfcare 101," anxiety/depression/PTSD language), (2) product-performance framing ("Squat Proof Gym Shorts," "Shorts That Don't Ride Up"), (3) brand/identity framing ("a brand for the misfits, the rebels"), (4) service/logistics framing ("Hassle Free Returns," "Ships From The U.S.A."). Several text ads cite specific review claims — "4.9 ★★★★★ (10)" and "10,000+ verified reviews at 5 stars" — that don't appear anywhere in the three Meta ads collected. One Shopping ad promotes Muay Thai Flame Shorts at $50 with a "Free" shipping badge. Google Ads carry proof-point and mission messaging that Meta ads (product-photo-led, tagline-only) do not — the two channels are not running a consistent message.

### Reviews & UGC

38 reviews collected from the on-site review widget, spanning the last 26 days, all 5-star with "Would recommend" marked.

#### What Customers Love

- Fit and comfort across body types and sizes, repeatedly described as "true to size," "comfy," "doesn't ride up," with specific praise for the 4" mid-thigh cut.
- Squat-proof, non-see-through fabric performance during workouts — corroborated independently by two TikTok UGC reviews.
- Print/color variety drives repeat purchase and gifting ("bought 6 pairs" for a granddaughter; multiple reviewers buying 2-3 colorways).
- Compliments as a social proof driver — several reviewers mention receiving compliments while wearing the product ("Comfy and Compliments!!!," "lots of compliments," "my wife loves them on me").

#### What Frustrates Customers

- Customer service: one reviewer explicitly separates product quality from service ("Great shorts. Horrible customer service").
- Pocket security: "you WILL lose anything and everything that you put in your pockets" during active wear (Caleigh R).
- Minor product nit: drawstring length ("the drawstring could be a bit longer" — Anthony V).
- Trustpilot (third-party, not the on-site widget) shows a sharply different picture: 2.3 TrustScore on 6 reviews, with specific complaints of a $24.85 unexplained refund deduction, a wrong item shipped (plain hoodie instead of cowprint) with no free return path offered, expedited shipping paid for but not honored (8-9 day estimate after paying for 2-4 day), and one report of shorts being "see-through when squatting."

#### Client-Actionable Insights

- The Trustpilot pattern (refund deductions, wrong-item shipments, unmet shipping promises) is an operations/fulfillment issue, not a marketing one — worth flagging to the client directly, especially since Trustpilot's 2.3 score is a major outlier against the on-site widget (4.8+) and other third-party scores (Junip 4.81/9,454 reviews, Knoji 4.2/58 reviews) cited in social research.
- Pocket security complaint suggests a product/packaging opportunity (a liner or zip pocket callout) rather than a test — pair with the review as supporting evidence if the client updates product copy.

### PageSpeed / Core Web Vitals

Mobile Lighthouse runs collected 2026-09-10. No desktop data collected.

| Metric | Homepage | PDP |
|---|---|---|
| Performance score | 58/100 | 63/100 |
| LCP | 6.4s | 8.0s |
| CLS | 0 | 0.144 |
| FCP | 3.3s | 2.7s |
| TBT | 400ms | 30ms |
| Time to Interactive | 12.4s | 12.7s |
| Speed Index | 4.8s | 4.7s |

Homepage carries a Lighthouse run warning: "The page loaded too slowly to finish within the time limit. Results may be incomplete." Both pages fail Google's LCP threshold (good is under 2.5s) by a wide margin — the PDP LCP of 8.0s is more than 3x the "poor" threshold (4s+). PDP also shows a non-trivial CLS of 0.144, bordering the "needs improvement" range (0.1-0.25), while the homepage shows 0 CLS. Given ads route directly to both the reptile-shorts collection and the floral-black PDP, paid traffic is landing on some of the slowest-loading pages on the site.

### Competitor Analysis

Research date: 2026-09-10, self-researched via WebSearch (no user-provided competitor data was collected for this brand — see manifest, "Competitor Insights" was skipped).

| Brand | Positioning | Shorts price | Notable |
|---|---|---|---|
| Kill Crew | Mental-health mission + combat-sport apparel | $50 | 4.8★/2,437 reviews (site widget); 2.3 TrustScore (Trustpilot, 6 reviews) |
| Hylete | Premium performance training apparel, flex-knit fabric | ~$88 | Positioned as a durability/fabric-tech premium alternative |
| RVCA (VA Sport line) | Action-sports brand extension into MMA/Jiu-Jitsu-inspired training wear | Comparable range (not confirmed) | Broader lifestyle brand halo, not mission-led |

Self-research also surfaced Gymshark, Nike, Abercrombie/Hollister active lines, and "Stronger by the Day" as adjacent alternatives customers search when comparing Kill Crew, per third-party blog content (elevateedge.blog, apartstyle.com) — these were not independently verified beyond the search snippets and are noted as directional only.

### Emails

Not collected — Email Campaigns was marked as a skipped source in the manifest. No findings.

### Inspiration Sites

Not collected — Inspiration Sites was marked as a skipped source in the manifest. No findings.

### Non-Data Context

Two structural facts from client-side context shape how this audit's ad/landing-page findings should be read: Ads 1 and 2 intentionally share one landing URL (both point to the reptile-shorts collection), and Ad 3 intentionally lands on a PDP rather than a collection page. Both are documented in the manifest as confirmed data structure, not collection gaps.

### Social & Community Research

Findings below are directional (third-party/community sources) unless flagged as corroborated.

- **Fit/fabric performance corroborated by first-party reviews:** TikTok UGC (2 independent reviewers, Aug–Sep 2026) describes the shorts as squat-proof, non-see-through, and true to size with occasional snugness at the listed size — this directly matches the on-site review sentiment (see Reviews section). One data point cuts the other way: a Trustpilot complaint describes shorts as "see-through when squatting," directly conflicting with the squat-proof claim both the brand and most UGC reinforce. This is a real, if isolated, contradiction worth surfacing to the client rather than resolving as noise.
- **Trustpilot score is an outlier, unconfirmed root cause:** 2.3 TrustScore (6 reviews) sits far below the on-site widget and other third-party platforms (Junip 4.81/9,454, Knoji 4.2/58). Standalone, not corroborated elsewhere in this audit beyond the general customer-service tension noted in the on-site reviews section.
- **Instagram and X have real audience scale but no usable engine data this run:** Instagram (927K followers) and X (~2,438 followers) were both confirmed active at precheck but the automated research engine failed to return data (HTTP 404 for Instagram, 0 items for X). Standalone — not corroborated elsewhere, and no specific claims should be drawn from these two platforms this cycle.
- **Site traffic estimate (unconfirmed, third-party tool):** ~196.6K monthly visits as of July 2026 per a third-party SEO estimation tool (not verified first-party analytics). Standalone.

### Current Site Screenshots

**Homepage:** Leads entirely with mission/mental-health messaging ("EVERYONE'S GOT SOMETHING TO KILL," anti-anxiety/depression/PTSD subhead) before any product-specific claim appears. Trust signal in the hero is a round order count ("Over 500,000 orders from happy customers" with a 5-star icon) rather than a specific rating — no star score or review count appears anywhere across the three captured homepage folds. The main nav scrolls out of view after fold 1 with no sticky header or sticky CTA bar reappearing in folds 2-3, so once a visitor scrolls past the hero, primary navigation and both CTAs ("SHOP MENS" / "SHOP WOMENS") are no longer reachable without scrolling back up.

**Collection page:** Confirmed to mix multiple product categories (hoodies, shorts, t-shirts) in one grid rather than isolating by type — consistent with the same pattern seen on the Ad 1/2 landing page. No sale badges, no compare-at pricing, and no distinguishing visual hierarchy between product types in the grid across all three folds.

**PDP:** Not collected as a standalone screenshot set — Ad 3's landing page folds serve as PDP evidence (see Meta Ads section above), per confirmed client context.

**Cart (drawer):** Right-side slide-in drawer with a free-shipping progress bar ("$25.00 away from free shipping") as the primary AOV mechanic, positioned above the cart line item. A "Check These Out!" upsell module shows 3 related products with one-click Add buttons directly in the drawer. Checkout CTA is a full-width black button labeled with the running total. Trust icons repeat at the bottom of the drawer (shipping, returns, mission) but no star rating or review count appears in the cart at all — a moment where reinforcing the 4.8★/2,437-review proof point (used prominently on the PDP) is currently absent.

## Cross-Source Themes

1. **Message match breaks between ad promise and landing destination for the majority of paid traffic.** Ads 1 and 2 (2 of 3 active Meta ads) show a specific product but land on a 34-item mixed collection page with no visible bridge to the advertised item, and no trust signals in the first three folds. Evidence: Meta Ads screenshots, live WebFetch of the collection page. Ad 3 is the counterexample — strongest message match in the set — but its landing PDP is confirmed out of stock live, which undercuts even the best-matched ad. This is the single highest-evidence theme: paid ad screenshots, live WebFetch confirmation, and Google Ads (extra unreflected claims) all point the same direction.

2. **Site speed is a likely conversion tax on exactly the pages ads route to.** Homepage LCP 6.4s, PDP LCP 8.0s (mobile), both far past Google's "poor" threshold, with the homepage Lighthouse run flagged as incomplete due to load time. Evidence: PageSpeed JSON (homepage, PDP). This is first-party, quantified, and directly tied to funnel entry points (ads land on the collection and PDP templates measured here).

3. **Trust/proof signals are inconsistently placed and, on one third-party channel, in direct tension with the brand's core product claim.** The PDP carries strong proof (4.8★/2,437 reviews, 6-icon trust bar); the homepage and cart carry weaker or no rating proof; and Trustpilot's 2.3 score plus a "see-through when squatting" complaint sits in tension with the squat-proof claim used in ads, PDP copy, and most UGC. Evidence: site screenshots (homepage, cart), meta-ads-visual-summary (PDP), last30days-ecom (Trustpilot), on-site reviews.

## Top Test Opportunities

1. **Fix or redirect Ad 3's landing page (out of stock).** Ad 3 is currently the best-matched, highest-trust-signal ad in the set, but its PDP is confirmed out of stock live as of 2026-09-11, meaning paid spend may be landing on a page with no purchase path. Evidence: live WebFetch of the PDP, Ad 3 in meta-ads-visual-summary.md. Est. lift: not modelable without live session/spend data — flag as urgent operational fix, not a test.

2. **Add a message-match bridge on the reptile-shorts collection page for Ads 1 & 2.** Two of three active Meta ads show one specific product but land on a 34-item mixed grid with no visual anchor to the advertised item and no visible trust signals in the first three folds. Test a filtered/pre-scrolled entry or a hero banner echoing the ad creative at the top of the collection page. Evidence: meta-ads-visual-summary.md (Ads 1 & 2), live WebFetch of the collection page, meta-ads.md (shared URL confirmation). Est. lift: conservative CR lift x sessions/mo x AOV = insufficient session/AOV data collected this cycle to size (see Missing Data).

3. **Reduce PDP LCP from 8.0s toward the sub-2.5s "good" threshold.** PDP is a direct ad landing page (Ad 3) with the slowest LCP measured in this audit. Evidence: killcrew-pdp-pagespeed.json (LCP 8.0s, performance score 63/100). Est. lift: not sized — no sessions/AOV data collected this cycle.

4. **Reduce homepage LCP and resolve the incomplete Lighthouse run.** Homepage LCP of 6.4s and a "page loaded too slowly to finish" run warning indicate a load-time problem severe enough to break measurement itself. Evidence: homepage-pagespeed-killcrew.json. Est. lift: not sized — no sessions/AOV data collected this cycle.

5. **Add a sticky nav or persistent CTA on the homepage below the hero.** Both primary CTAs ("SHOP MENS"/"SHOP WOMENS") and the main nav are only present in fold 1; scrolling past the hero removes all wayfinding and purchase paths until the user scrolls back up. Evidence: site-visual-summary.md (Homepage fold 2-3, "CTA behavior" note). Est. lift: not sized — no sessions/AOV data collected this cycle.

6. **Surface the 4.8★/2,437-review proof point in the cart drawer.** The PDP's strongest trust asset (star rating, review count) is used nowhere else on site — the cart drawer, which is the last stop before checkout, shows shipping/returns/mission icons but no rating. Evidence: site-visual-summary.md (Cart Drawer section, "no star rating or review count visible"), meta-ads-visual-summary.md (PDP rating placement). Est. lift: not sized — no sessions/AOV data collected this cycle.

7. **Reconcile or address the Trustpilot "see-through when squatting" complaint against the squat-proof claim used across ads, PDP, and UGC.** A live conflict exists between the brand's central performance claim (repeated in Ad 3, PDP copy, and most TikTok UGC) and at least one specific negative report. Evidence: last30days-ecom.md (Trustpilot), meta-ads-visual-summary.md (Ad 3 squat-proof claim), reviews.md (squat-related praise). Est. lift: not a standard A/B test — recommend as a client-facing QA/quality-control flag, potentially paired with a PDP FAQ or fit-guidance addition if the client confirms it's a batch issue.

8. **Investigate and address the Trustpilot fulfillment/refund complaints as an operations fix.** Refund deduction, wrong-item shipment, and unmet expedited-shipping promises are documented complaints that sit well outside normal CRO test scope but materially affect the 2.3 TrustScore outlier. Evidence: last30days-ecom.md (Trustpilot). Est. lift: not applicable — operational/client-facing recommendation, not a test.

## Unused but Valuable Findings

- Google Ads carry a "4.9 ★★★★★ (10)" / "10,000+ verified reviews at 5 stars" claim not reflected on the homepage or in Meta ad creative — an easy message-match/consistency opportunity if slots open up in a future roadmap cycle.
- Collection page pricing shows no sale badges or compare-at pricing anywhere across 6 folds observed (Ad 1/2 landing + Collection page) — worth flagging as a potential AOV/urgency lever separate from the current slot list.

## Missing Data

- No sessions/mo or AOV figures were collected for Kill Crew this cycle, so every Top Test Opportunity above is qualitative-only — none of the Est. lift fields could be sized in dollar terms. Flag to the client that traffic and AOV data (Shopify analytics or GA4 export) would materially strengthen prioritization.
- No desktop PageSpeed data was collected — only mobile Lighthouse runs exist for both homepage and PDP. Desktop CWV is an open gap.
- Email Campaigns and Inspiration Sites were skipped sources per the manifest; no findings possible in those sections.
- Instagram and X automated social research calls both failed this cycle (HTTP 404 and 0 items respectively) despite confirmed active, high-follower accounts on both platforms — no usable data from either channel this run.
- No user-provided competitor data (raw/competitors.md) existed for this brand — the Competitor Analysis section above is entirely self-researched via WebSearch and should be treated as directional, not verified via each competitor's live pricing pages.

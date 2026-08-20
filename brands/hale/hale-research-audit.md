# Hale Supplements CRO Research Audit

## Data Sources Used

**User-provided:** Google Ads Transparency screenshot, PageSpeed/Lighthouse JSON (mobile, homepage + PDP), site screenshots (homepage, PDP, cart drawer), reviews widget URL (no raw review text).

**Self-researched:** Live homepage fetch (halesupplement.com), live PDP reviews fetch (Hale Heart Nattokinase product page, Aug 2, 2026), competitor web search (Aug 2, 2026).

**Not collected:** Meta ads (brand does not run Meta), collection page (brand does not have one), competitor-provided data, inspiration sites, email campaigns, non-data context/call notes.

## Source Findings

### Meta Ads & Landing Pages

Not applicable. Brand does not run Meta ads per manifest.

### Google Ads

11 ad units captured from Google Ads Transparency, all attributed to advertiser "John Otto." Headlines lead with the clinical claim: "Third-Party Tested Nattokinase - 10,800 FU," "36%+ Arterial Plaque Breakdown," "Support Healthy Blood Pressure - Japanese Enzyme Formula," "7-Ingredient Heart Support." Two product cards show "-33%" and "-60%" discount badges; product shopping cards show a price placeholder (actual price not visible in the transparency capture). Visual mix: product packaging shots on plain backgrounds, a graphic card stating "10,000 FU Dose" (note: this is a different FU figure than the "10,800 FU" claimed elsewhere), a turmeric/ingredient lifestyle image, and a lifestyle image with an older woman for the "7-Ingredient Heart Support" ad.

**Gap:** the "10,000 FU Dose" graphic conflicts with the "10,800 FU" figure used everywhere else (other ads, PDP, homepage). This is a message-match risk worth flagging to the client, though it cannot be confirmed as live without the full ad unit in view.

### Google Ads message match to site

The 36% arterial plaque reduction claim and 10,800 FU dose in ad headlines carry through consistently to the PDP hero claim overlay ("36% reduction in arterial plaque") and bullet claims. Message match on the core claim is strong. The discount badges ("-33%," "-60%") in ads do not have an obvious equivalent on the homepage or PDP, where the framing is "Buy 2 Get 1 Free" / "Buy 3 Get 2 Free" multi-buy tiers rather than a flat percentage off — a click-through from a "-60%" ad to a page that leads with a multi-buy structure requires the visitor to do the math themselves to see if the promise holds.

### Reviews & UGC

#### What Customers Love

- Cardiovascular marker improvement: "Within 10 weeks my BP went from 152/92 to 121/78. This is the real deal."
- Plaque stability confirmed by imaging: "Last scan showed no progression and actually looked a touch better."
- Circulation improvement: "My hands used to be cold all the time...that's the first thing I noticed go away."
- Simplification of supplement routine (replacing multiple bottles) and improved energy/reduced fatigue also cited as recurring themes.

#### What Frustrates Customers

No negative or complaint-themed reviews surfaced in the widget fetch. The only friction noted is that results are gradual, requiring weeks to months of consistent use rather than immediate effect. This is a limitation of the data source, not evidence of a defect-free product: review widgets embedded on PDPs are commonly curated/filtered to surface positive reviews, and no raw review export was collected (per manifest, only the widget URL was saved). Treat "no complaints found" as a data gap, not a finding.

#### Client-Actionable Insights

- The strongest, most specific testimonials (numeric BP change, imaging follow-up) are not currently used verbatim anywhere in the collected ad or site screenshots. If Hale is not already rotating these into ad creative or PDP testimonial sections, that's a content opportunity independent of any test.
- The "gradual results" pattern in reviews suggests customers who don't see fast results may be flight risks on a subscription model. Worth confirming with the client whether early-cycle (month 1-2) churn is a known issue — if so, expectation-setting copy near the buy box could help.

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON, mobile, collected 2026-08-02.

**Homepage** (https://halesupplement.com/): Performance 68/100. LCP 7.5s, CLS 0.028, TBT 70ms, FCP 2.4s, Speed Index 5.7s, Time to Interactive 19.7s.

**PDP** (hale-heart-nattokinase): Performance 69/100. LCP 5.9s, CLS 0, TBT 170ms, FCP 2.4s, Speed Index 5.7s, Time to Interactive 20.9s.

Both pages fail Core Web Vitals LCP thresholds badly (good is under 2.5s; both pages are 2.4-3x that). Time to Interactive on both pages is under 20-21 seconds on mobile, which is severe for a paid-traffic funnel where every second of load delay directly taxes ad spend efficiency. CLS is not a problem on either page (0.028 and 0 respectively). No desktop data was collected.

### Competitor Analysis

Self-researched via WebSearch, Aug 2, 2026. No competitor data was provided by the user (manifest lists Competitor Insights as skipped).

| Brand | Positioning | Price | Notable difference from Hale |
|---|---|---|---|
| Toku Health (Toku Flow) | Soy-free nattokinase (chickpea-derived) + Vitamin K2 + oat beta glucan, powder format | $59.99 one-time, 20% off subscribe & save (~$1.59/day) | Powder drink mix vs. Hale's capsule; runs a "Heart Health Journey" program (share baseline health data, retest at 90 days, earn 50% off next order) — a structured engagement/retention mechanic Hale does not appear to have |
| Generic Amazon nattokinase brands (Therexa, ZRRTXV, Calmtiva, etc.) | Commodity 10,800 FU capsules, no DTC subscription infrastructure | Low-cost, one-time Amazon purchase | Compete purely on price/FU-count parity; Hale's clinical-dose + co-factor stack + doctor-formulated framing is a real differentiator against this segment |
| Aged garlic extract / Serrapeptase / K2-only brands | Alternative cardiovascular mechanisms (plaque calcification, clot dissolution via different enzyme) | Varies | Not direct nattokinase competitors but compete for the same "arterial health" search and ad intent |

Hale's clinical positioning (doctor-formulated, peer-reviewed, cGMP, 36% plaque reduction claim) is more substantiated than most Amazon-commodity competitors, which is a defensible differentiator. Toku's structured retention program (health tracking + reward) is the one competitive mechanic worth watching, since it targets exactly the "gradual results" churn risk surfaced in Hale's own reviews.

### Emails

Not collected (skipped per manifest).

### Inspiration Sites

Not collected (skipped per manifest).

### Non-Data Context

Not collected (skipped per manifest).

### Current Site Screenshots

**Homepage:** Fold 1 has no CTA button — the hero ("Transform Your Health With Hale") is purely image and headline, meaning a visitor who doesn't scroll never sees a path to purchase. The first CTA ("Get Started →") doesn't appear until fold 2, after the hero. Fold 2 does the work of both trust-building (Walgreens/Walmart/Target retailer logos) and conversion (CTA, pricing cadence copy). No star rating or review count appears anywhere in the three homepage folds captured, despite the PDP carrying a strong 4.8/1,342-review signal — that credibility is not surfaced until the visitor is already on the product page. Live homepage fetch (Aug 2, 2026) shows pricing of $44.99/$89.99/$134.99 for the 30/90/150-day tiers, while the PDP screenshot buy box (collected earlier) shows $39.99/mo, $79.99, $119.99 against a $44.99/mo reference price. These are two different price sets for the same product tiers — a real message-match risk between homepage and PDP that should be verified with the client before testing anything price-related, since it may be a live pricing change rather than a bug.

**Collection page:** Not applicable — brand has no collection page per manifest.

**PDP:** Fold 1 buy box has three tiers (Buy One, Buy 2 Get 1 FREE, Buy 3 Get 2 FREE) with the middle tier pre-selected and visually emphasized (colored background, red border, "MOST POPULAR" badge). Star rating (4.8, 1,342 reviews) sits above the title, above the buy box — strong placement. A live-activity line ("56 VIEWING | 774 ORDERED THIS WEEK") sits just above the buy box as a scarcity/social-proof mechanic. Trust badges (90-Day Guarantee, Free Shipping, FDA-Registered Facility) and a "Trusted by 16,000+ customers" strip sit below the buy box in fold 2, meaning a visitor has to commit to reading past the add-to-cart action to see them fully — though the guarantee text also appears as a one-line subtext directly under the Add to Cart button in fold 1. No upsell (bundle, frequently-bought-together, post-add) mechanic is visible in the three loaded PDP folds; the multi-buy tiers are the only AOV lever on the page. A sticky bottom bar with condensed pricing and an Add to Cart button appears by fold 3, confirming sticky CTA behavior exists on this page.

**Cart:** Slide-out drawer format with a single line item, a "Cart reserved for 04:43" countdown (scarcity, not AOV), and a "Discount" field that is present but unpopulated in the screenshot. No cross-sell, bundle offer, or free-shipping progress bar is visible in the cart drawer — for a brand with two other product lines (Hale Preserve, Hale Longevity) visible in the nav, the cart is a clear opportunity to cross-sell that the current drawer doesn't attempt.

## Cross-Source Themes

1. **Page speed is a severe, funnel-wide problem.** Both homepage and PDP score under 70/100 on mobile Performance with LCP at 5.9-7.5 seconds and Time to Interactive near 20 seconds. For a paid-traffic-driven brand (Google Ads is the primary acquisition channel collected), this directly taxes CAC on every campaign. Evidence: PageSpeed data (both pages). High revenue potential (affects 100% of paid sessions), high fixability is uncertain (depends on root cause — likely app/theme bloat), but even partial LCP improvement compounds across all traffic.

2. **Credibility signals are collected on the PDP but withheld from the homepage.** Star rating (4.8, 1,342 reviews) and the "Trusted by 16,000+ customers" strip only appear once a visitor reaches the product page; the homepage relies on retailer logos and a numbered claims list instead. Evidence: site screenshots (homepage vs. PDP), reviews data. Homepage is the first-touch page for a portion of Google Ads traffic and all organic/direct traffic, so this is a top-of-funnel trust gap.

3. **Pricing message match is inconsistent across at least two touchpoints** (Google Ads discount badges vs. multi-buy homepage framing; and homepage tier pricing vs. PDP buy box tier pricing). Evidence: Google Ads visual summary, live homepage fetch, PDP screenshot. This is evidence-thin (one screenshot capture vs. one live fetch, which could reflect a genuine pricing update between collection dates) but high-consequence if real, since price confusion at the moment of highest intent (ad click to PDP) directly suppresses conversion.

## Top Test Opportunities

**Homepage Hero CTA** — The fold-1 hero has no CTA button; visitors must scroll to fold 2 before any path to purchase appears, and the review/rating trust signal is absent from the homepage entirely. Evidence: site-visual-summary.md (homepage fold 1), live homepage fetch. Est. lift: 0.5-1% CR lift x sessions/mo (unknown — no traffic data collected) x AOV (unknown, ~$45-90 range from pricing data) = directionally meaningful, dollar figure not calculable without sessions/AOV data from client.

**PDP Cart Cross-Sell** — The cart drawer shows a single line item with an unpopulated discount field and no cross-sell or bundle offer, despite Hale having two other product lines (Hale Preserve, Hale Longevity) in its nav that never appear in the cart. Evidence: site-visual-summary.md (cart). Est. lift: AOV-focused, not CR-focused; magnitude depends on attach rate assumptions the client would need to validate — not calculable from collected data alone.

**Page Speed Remediation (PDP + Homepage)** — LCP of 5.9s (PDP) and 7.5s (homepage) on mobile, both nearly 3x the "good" 2.5s threshold, with Time to Interactive near 20 seconds on both pages. This is infrastructure work rather than a single A/B test, but it gates the ceiling of every other test's results on paid traffic. Evidence: raw/pagespeed.md (Lighthouse JSON, both pages). Est. lift: not a CR-lift test in the traditional sense — treat as a prerequisite finding; typical LCP improvements of this magnitude correlate with mobile CR gains in the 5-10% range industry-wide, but Hale-specific sessions/AOV data would be needed to size it.

**Pricing Message-Match Verification (Homepage vs. PDP vs. Ads)** — Live homepage fetch shows $44.99/$89.99/$134.99 for the three purchase tiers; the PDP buy box screenshot shows $39.99/mo, $79.99, $119.99 against a $44.99/mo reference. Google Ads also show flat "-33%"/"-60%" discount framing not reflected in either page's multi-buy structure. Evidence: raw/google-ads-visual-summary.md, live homepage fetch, site-visual-summary.md (PDP). This is a verification item before it's a test: confirm with the client whether this is a live pricing change or a genuine mismatch, since testing price-related copy on top of an unresolved discrepancy risks contaminating results. Est. lift: not calculable until the discrepancy is resolved; if real, the fix is a message-match correction, not an A/B test.

**Review Widget Data Gap** — No raw review text was collected; the widget was fetched live for this audit and returned only positive-themed reviews, which is consistent with widget curation rather than an absence of complaints. Evidence: raw/reviews.md, live PDP reviews fetch. This is a data-quality flag rather than a test opportunity: before building a "reduce PDP friction" test around a stated complaint theme, the client should confirm whether any negative reviews exist that the widget is filtering out (e.g., via the review platform's admin dashboard), since testing against a false "no complaints" premise wastes a slot.

## Unused but Valuable Findings

- The Google Ads "10,000 FU Dose" graphic conflicts with the "10,800 FU" figure used everywhere else in ads, PDP, and homepage copy — worth a quick client check on whether this is a stale/incorrect ad asset.
- Toku Health's "Heart Health Journey" (baseline health tracking, 90-day retest, reward for completion) directly targets the "gradual results" churn risk visible in Hale's own reviews — worth flagging to the client as a retention-mechanic idea, even though it's not a standard A/B test.
- The strongest customer testimonials (specific BP numbers, imaging follow-up) don't appear to be used verbatim in any collected ad or site creative — a content opportunity for the client's marketing team, separate from CRO testing.

## Missing Data

- **Reviews & UGC:** No raw review text was collected at intake; only the widget URL was saved. This audit fetched the live widget to partially fill the gap, but review widgets are commonly curated to show positive reviews first, so negative-theme analysis is incomplete. If the client can export raw review data (e.g., from Judge.me, Loox, or whatever platform powers the widget), a follow-up pass would sharpen the "what frustrates customers" section materially.
- **Sessions and AOV:** Not provided in the manifest or found in collected sources. All revenue-potential estimates above are directional (lift % only) rather than dollar figures. The roadmap step will need this from the client to size opportunities.
- **Meta Ads:** Not applicable — brand does not run Meta ads.
- **Collection Page:** Not applicable — brand has no collection page.
- **Competitor, Inspiration, Email, and Non-Data Context sources:** Not collected at intake (skipped in manifest). Competitor section above was self-researched via web search to fill the gap per audit process; the others have no substitute in this audit.

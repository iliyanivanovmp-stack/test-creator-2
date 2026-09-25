# Cliganic CRO Research Audit

## Data Sources Used

**Collected first-party:** Meta Ads & Landing Pages (visual summary, 3 ads), Google Ads Transparency Center (visual summary, 2 screenshots), PageSpeed / Core Web Vitals (mobile, homepage + PDP, full JSON exports), Current Site Screenshots (homepage, collection, cart drawer), Reviews & UGC (Amazon-style verified reviews + on-site review widget, Organic Jojoba Oil).

**Self-researched:** Live homepage fetch (cliganic.com, 2026-09-09), Social & Community Research via last30days-ecom (Fallback Mode, run 2026-09-09 — directional, engagement numbers not available).

**Not collected this round:** Competitor Insights, Inspiration Sites, Email Campaigns (not selected in manifest).

## Source Findings

### Meta Ads & Landing Pages

Three ads collected, two products represented.

**Ad 1 (Jojoba Oil, retargeting angle):** "Loved your last Cliganic order? Here's more clean, natural picks you might like." Lands on the Organic Jojoba Oil PDP, defaulting to the 4oz size ($9.87, was $12.99) with Subscribe & Save (24% off) pre-selected. Message match gap: the ad promises a curated multi-product "picks" experience, but the landing page delivers one single product page. The "clean, natural" language in the ad isn't echoed in the fold-1 hero — it only surfaces later via the certification icon row.

**Ad 2 (Rosemary Repair Scalp & Strand Oil):** Leads with a specific clinical stat: "95% of consumers said their hair looked shinier with smoother ends" after 14 days. The landing page's own disclosed stat set is different — "93% felt stronger, 91% looked fuller" after 28 days, with methodology disclosure. Neither the statistic nor the timeframe from the ad appears on the page. This is a direct ad-to-page stat mismatch, not just a framing difference.

**Ad 3 (Jojoba Oil, second angle):** Creative shows "$12.99" and "#1 Best Seller on Amazon" positioning. The landing page it drives to defaults to the 16oz size at $28.89 (was $33.99) — a different price point than advertised, and there is no Amazon best-seller reference anywhere on the page. The ad's "90% said skin felt more nourished after 28 days" stat also doesn't appear in the captured folds.

Across all three ads, the PDP pattern is consistent: sticky "ADD TO BAG" bar, 60-Day Money-Back Guarantee, Free Shipping badge, HSA/FSA banner, a Frequently Bought Together module with pre-added items, and a 10-icon certification row lower on the page.

### Google Ads

Google Ads Transparency Center shows roughly 20 ad units under "A to Z Beauty, LLC" (verified), plus a smaller number under an affiliate ("Collegedunia Web Pvt. Ltd."). A large share of this inventory routes to Amazon product listings rather than cliganic.com, leaning on Amazon-specific social proof ("Amazon Best Seller," star counts like "4.5 ★★★★★ (9,458)," "35,000+ 5-Star Reviews," "42,000+ Reviews"). Ads that do route to cliganic.com use "Shop Cliganic™ Oils Now" framing with the same Free Shipping / 60-Day Refund offers seen on Meta.

Gap vs. Meta: Google's Amazon-routed ads and review-count claims (9,000+, 35,000+, 42,000+) don't correspond to any number visible on the site-side PDP (Meta ads show 4.8/5, 279 Verified Reviews for jojoba oil). A prospect clicking a Google ad citing "42,000+ reviews" and landing on a page showing "279 Verified Reviews" encounters a credibility drop. Google's ad set also surfaces a mosquito repellent product line with no corresponding Meta creative or PDP data collected in this audit.

### Reviews & UGC

Two mixed sources: Amazon-style verified-purchase reviews (with helpful-vote counts) and an on-site review widget feed (mostly marked "Incentivized review"), both for Organic Jojoba Oil.

#### What Customers Love

- Non-comedogenic, safe for acne-prone and sensitive skin: "I have PCOS and acne-prone skin... It never breaks me out, never clogs pores" (Just Sandra, Amazon verified).
- Lightweight, fast-absorbing texture without greasy residue, repeated across dozens of reviews ("absorbs nicely," "sinks right in," "doesn't feel heavy or greasy").
- Multi-use versatility — face, body, hair, nails, cuticles, DIY skincare base, carrier oil for other blends.
- Long-term repeat customers citing multi-year usage ("been using the Cliganic jojoba oil for 5 years now" — Carina G.; "past 3 years" — Sitara T.).
- Value perception relative to price ("Amazing price for a solid oil," "What A Bargain!! Amazing price for 32 oz.").

#### What Frustrates Customers

- Plastic bottle instead of glass, raised repeatedly and unprompted: "was expecting a glass bottle but it is unfortunately plastic" (Amelia); "Super moisturizing, just wish it came in a glass bottle instead of plastic" (Meggie); "I do wish it were in glass" (Nancy D.).
- Packaging/shipping damage: "The packaging was all messed up. Oil was everywhere and it was out of the box." (kolby).
- Shipping delay with no visibility: "It got delayed for days without a projected delivery date." (Geraldine).
- Scent inconsistency between batches: "The recent product (second time ordering) has a bit of stronger chemical scent... I liked the original organic natural just the pure oil scent." (Hana K.).
- Cross-referenced by last30days-ecom (directional, third-party): PissedConsumer cites unauthorized/unwanted recurring charges and wrong items shipped in "monthly deliveries" on a small sample (4-6 reviews, 1.1-star). This is not independently corroborated in the first-party review set collected here, which shows no explicit subscription-billing complaints — flagged as unconfirmed.

#### Client-Actionable Insights

- Bottle material (plastic vs. glass) is the single most repeated complaint across the collected review set and should go to the product/packaging team, not a CRO test — it's a physical product attribute, not a page element.
- Shipping damage and delivery-delay complaints point to a fulfillment/packaging-durability issue worth flagging to ops.
- Batch-to-batch scent consistency is a manufacturing QA note, not a site issue.

### PageSpeed / Core Web Vitals

Mobile only, no desktop run available in the collected JSON exports. Collected 2026-09-09.

**Homepage (mobile):** Performance score 0.32. LCP 7.2s, FCP 3.9s, CLS 0, Speed Index 11.6s, Total Blocking Time 1,990ms, Time to Interactive 43.8s, Max Potential FID 430ms.

**PDP — Organic Jojoba Oil (mobile):** Performance score 0.28. LCP 33.9s, FCP 18.4s, CLS 0, Speed Index 23.0s, Total Blocking Time 1,650ms, Time to Interactive 60.1s, Max Potential FID 470ms.

The PDP is the more severe case: a 33.9s LCP is roughly 4.7x Google's "poor" threshold (2.5s+) and nearly 5x the homepage's own LCP. Since the PDP is the primary paid-traffic landing destination (2 of 3 Meta ads land here), this is the highest-leverage performance fix available. CLS is 0 on both pages, so layout shift is not a contributing factor — the issue is load/render blocking, reflected in the Total Blocking Time (1,650-1,990ms) and near-60s Time to Interactive on the PDP.

### Emails

Not collected — not selected as a source in this round (manifest confirms no email data gathered).

### Inspiration Sites

Not collected — not selected as a source in this round.

### Non-Data Context

The PDP under review is the Organic Jojoba Oil product page specifically. No standalone PDP screenshots exist in this collection because two of the three Meta ads (Ad 1, Ad 3) land directly on this page in different promotional states (different default size, different discount tier), so the ad-landing-page fold captures documented in the Meta Ads section serve as the PDP record for this audit.

### Social & Community Research

Directional findings from last30days-ecom (Fallback Mode — no engagement scoring, sources found via WebSearch/WebFetch only). Run 2026-09-09.

- TikTok discovery topic "Is Cliganic A Safe Brand" indicates some circulating consumer skepticism about the brand — unconfirmed by any first-party source in this audit, stands alone.
- YouTube has at least one negative-titled review ("Cliganic Jojoba Oil Review: Why I'm Sending It Back") alongside neutral/positive jojoba oil reviews — mixed signal, not corroborated further here.
- PissedConsumer (1.1-star, small sample) and Trustpilot both surface subscription/recurring-charge and customer-service-responsiveness complaints. This is corroborated in direction only — the first-party review set collected for this audit does not contain explicit subscription-billing complaints, so treat the recurring-charge complaint as unconfirmed by first-party evidence, while the general "wish there were more support responsiveness" theme has weaker but present alignment with the Trustpilot note.
- Walmart reviews (third-party retailer, not Cliganic's own site) echo the plastic-packaging complaint found independently in the first-party Cliganic reviews — this is the one social-research finding directly corroborated by first-party evidence.

### Current Site Screenshots

**Homepage:** Hero is a full-bleed lifestyle photo promoting Rosemary Repair Scalp & Strand Oil ("Make Every Day A Great Hair Day!") with a "TRY IT NOW!" button — not the jojoba oil product that both paid ad campaigns (Ad 1, Ad 3) and the bulk of organic/paid traffic patterns point to. A scrolling marquee immediately below claims "500,000+ 5-STAR REVIEWS" and "10,000+ RETAIL STORES | 40 COUNTRIES." No sticky CTA or add-to-cart exists on the homepage — sticky behavior is PDP-only. The Best Sellers carousel does correctly surface Organic Jojoba Oil with a "BEST SELLER" badge in fold 2, but a visitor arriving from a jojoba-oil-specific ad and bouncing to the homepage (e.g., via nav) would land on hair-oil messaging first, requiring a scroll to reach the product the ad promised.

**Collection page:** 4-column grid, 172 products, sort defaulting to "Best selling." Cards show BEST SELLER / SAVE % badges, star rating with numeric average, but no visible review count on the card — count only appears after clicking into the PDP. No filters are applied by default (Filters (0)) despite an 8-tile subcategory nav being present at the top, meaning a visitor has to use the subcategory tiles or manually filter to narrow 172 products.

**PDP:** Not separately screenshotted; documented via the Meta Ads landing-page folds (see above). Key friction points there: inconsistent default size/price/discount-tier across ad entry points (4oz/24% off via Ad 1 vs. 16oz/15% off via Ad 3), and Subscribe & Save pre-selected over one-time purchase by default in both cases.

**Cart (drawer):** Slide-out "YOUR BAG" drawer rather than a full cart page. Strong AOV mechanic: a 3-tier free-shipping/free-gift/free-tumbler progress bar with live dollar-amount-remaining copy ("You are $30.13 away from FREE SHIPPING!"). A "SavedBy Package Protection" add-on ($2.47) appears bundled into the checkout total by default based on button copy ("CHECKOUT+ • $12.34"), with opt-out only available as a small secondary text link ("Continue without package protection") — this is a pre-checked paid add-on pattern. No guarantee or returns copy appears anywhere in the cart drawer, despite the 60-Day Money-Back Guarantee being a prominent PDP trust signal.

## Cross-Source Themes

1. **PDP load performance is a severe, quantified funnel blocker.** LCP of 33.9s on mobile PDP (vs. 2.5s "good" threshation) is corroborated by the homepage's own poor score (7.2s LCP) and directly affects the page that both Meta ad campaigns funnel to. This is the strongest evidence-backed theme — one first-party data source (PageSpeed JSON), directly measured, no ambiguity.

2. **Ad-to-page message and pricing mismatches erode trust at the moment of landing.** Corroborated across two independent ad sources: Meta (Ad 2's stat mismatch, Ad 3's price/Amazon-positioning mismatch) and Google (review-count claims — 9,000-42,000+ — that don't match the 279-review count shown on the actual PDP). Two sources, three distinct instances, high revenue relevance since this affects every paid click.

3. **Default checkout/cart mechanics favor the business over transparency.** The pre-selected Subscribe & Save option on the PDP (both ad landing states) and the bundled Package Protection add-on in the cart drawer (opt-out via small text link, not a checkbox) both nudge toward higher-revenue defaults without explicit visitor consent. This is corroborated by the social-research signal (PissedConsumer/Trustpilot subscription-billing complaints), though that corroboration is directional/unconfirmed by first-party review text.

## Top Test Opportunities

**Fix PDP Mobile Load Time** — The Organic Jojoba Oil PDP has a 33.9s mobile LCP and 60.1s Time to Interactive, meaning most visitors arriving from paid ads likely abandon before the page is interactive. Evidence: PageSpeed JSON (pagespeed-pdp.json). Est. lift: assuming even a partial fix cutting LCP toward ~10s recovers a conservative 15% of currently-bouncing paid sessions x unknown monthly sessions x unknown AOV = dollar impact not calculable without session/AOV data (see Missing Data).

**Align Google Ads Review-Count Claims With On-Site Reality** — Google ads cite "35,000+," "42,000+," and "9,000+" review counts (mostly Amazon-sourced), but the jojoba oil PDP itself shows "4.8/5 (279 Verified Reviews)" — a 100x+ gap that reads as a bait-and-switch to a skeptical visitor. Test surfacing the true aggregate review count (site + Amazon combined, clearly labeled) at the same prominence on the PDP. Evidence: google-ads-visual-summary.md, meta-ads-visual-summary.md. Est. lift: conservative CR lift on paid traffic from reduced trust-drop-off x sessions/mo (unknown) x AOV (unknown) = not calculable (see Missing Data).

**Fix Ad 2's Stat Mismatch (Rosemary Oil PDP)** — The ad's headline stat ("95% said hair looked shinier... after 14 days") does not appear anywhere on the landing page, which instead discloses a different stat set ("93% felt stronger, 91% looked fuller" after 28 days). Test adding the exact ad-matching stat to PDP fold 1. Evidence: meta-ads-visual-summary.md (Ad 2). Est. lift: not calculable without sessions/AOV for this specific SKU (see Missing Data).

**Resolve Ad 3 Price/Positioning Mismatch (Jojoba Oil, 16oz default)** — Ad 3 advertises "$12.99" and "#1 Best Seller on Amazon," but the landing page defaults to the 16oz size at $28.89 with no Amazon reference. Test defaulting the size selector to match the advertised price point (4oz-equivalent) when traffic arrives from this specific ad's UTM/creative ID. Evidence: meta-ads-visual-summary.md (Ad 3). Est. lift: not calculable (see Missing Data).

**Un-Bundle the Default Package Protection Add-On in Cart** — The cart drawer bundles a "SavedBy Package Protection" line ($2.47) into the checkout total by default, with opt-out only via a small secondary text link rather than an unchecked checkbox. This pattern risks the exact "unwanted charges" complaint pattern flagged directionally in social research (PissedConsumer). Test an unchecked-by-default protection add-on with an explicit opt-in checkbox. Evidence: site-visual-summary.md (Cart Drawer), last30days-ecom.md (directional corroboration). Est. lift: not calculable without cart-to-checkout conversion baseline (see Missing Data).

**Add Guarantee/Trust Copy to the Cart Drawer** — The 60-Day Money-Back Guarantee is a prominent PDP trust signal (appears directly below Add to Bag on every ad-landing PDP fold) but disappears entirely once a visitor reaches the cart drawer, the last screen before checkout. Test adding the guarantee badge to the cart drawer alongside the existing "500,000+ 5-Star Reviews" line. Evidence: meta-ads-visual-summary.md (PDP trust signals), site-visual-summary.md (Cart Drawer — no guarantee copy present). Est. lift: not calculable without cart abandonment baseline (see Missing Data).

**Route Homepage Hero Toward Best-Selling Product, Not Secondary Product** — The homepage hero promotes Rosemary Repair Scalp & Strand Oil, while Organic Jojoba Oil (the product both live paid campaigns advertise and the one carrying a "BEST SELLER" badge in the homepage's own carousel) is only reachable after a scroll. Test a hero variant featuring the jojoba oil bestseller, or a dynamic hero keyed to the highest-traffic incoming campaign. Evidence: site-visual-summary.md (Homepage fold 1-2), meta-ads-visual-summary.md (2 of 3 ads are jojoba oil). Est. lift: not calculable without homepage session share of paid vs. organic traffic (see Missing Data).

**Surface Per-Card Review Counts on the Collection Page** — Collection page cards show a star rating with numeric average but no review count; count is only visible after clicking into the PDP. Since review volume (279 for jojoba oil) is a meaningful trust signal used prominently on the PDP itself, withholding it at the collection-browse stage is a missed reinforcement opportunity. Test adding review count to the card. Evidence: site-visual-summary.md (Collection Page — Price display note). Est. lift: not calculable without collection-to-PDP click-through baseline (see Missing Data).

**Test the Subscribe & Save Default on the PDP Buy Box** — On both jojoba oil ad-landing states (Ad 1, Ad 3), Subscribe & Save is pre-selected over one-time purchase by default in the buy box. This is a distinct mechanic from the cart's Package Protection add-on (different component, different point in the funnel) and is the pattern most directly aligned with the recurring-charge complaints flagged directionally in social research. Test a neutral (unselected) default or a clearer visual distinction between the two purchase options. Evidence: meta-ads-visual-summary.md (Ad 1, Ad 3 — Landing Page Fold 1), last30days-ecom.md (directional corroboration via PissedConsumer). Est. lift: not calculable without PDP add-to-cart baseline (see Missing Data).

**Surface the Free-Shipping Progress Bar Earlier in the Funnel** — The 3-tier free-shipping/free-gift/free-tumbler progress bar with live remaining-dollar copy is a strong AOV mechanic, but it currently only appears in the cart drawer, after the add-to-cart decision is already made. Test surfacing a lightweight version of this progress indicator on the PDP itself (below the Add to Bag button) so it can influence the initial add-to-cart decision, not just post-add upsell. Evidence: site-visual-summary.md (Cart Drawer — AOV elements), meta-ads-visual-summary.md (PDP folds — no equivalent shipping-progress element present). Est. lift: not calculable without AOV data (see Missing Data).

## Unused but Valuable Findings

- The homepage marquee and Google ad reviews both cite "500,000+" and "35,000-42,000+" review figures respectively, which are order-of-magnitude larger than the 279-review count on the actual jojoba oil PDP — likely because the larger figures aggregate across the entire product catalog or Amazon storefront rather than this specific product; worth a client-side clarification before any test assumes these numbers are interchangeable.
- Collection page shows "Filters (0)" applied by default across 172 products with no default narrowing — a secondary opportunity for a discovery-focused test, but lower priority than the PDP/ad-mismatch issues above.

## Missing Data

- No monthly sessions or AOV figures were collected for Cliganic in this round (manifest confirms these fields were not in scope), so every "Est. lift" line above is directional (percentage impact reasoning only) rather than a dollar figure. Flag to client before finalizing roadmap prioritization by revenue.
- No desktop PageSpeed run exists — mobile-only Core Web Vitals data. Desktop performance state is unknown.
- No standalone PDP screenshots exist (by design, per manifest) — PDP evidence in this audit is drawn entirely from ad-landing-page fold captures, which may not reflect the PDP's default (non-ad, organic-traffic) state.

# Bootylicious Muffins CRO Research Audit

## Data Sources Used

**User-provided:** Meta Ads Library screenshots (3 creatives), Google Ads Transparency Center screenshots (2), site screenshots (homepage, build-your-box/collection, PDP, cart drawer — 14 total), on-site customer reviews (raw/reviews.md), PageSpeed/Core Web Vitals JSON exports (homepage + PDP, mobile).

**Self-researched:** Live homepage and PDP fetch (2026-09-21), competitor pricing research (Kodiak Cakes, Premier Protein), and automated social/community research (last30days-ecom) covering TikTok, Instagram, YouTube, Pinterest, Amazon, and general web.

**Skipped per manifest:** Competitor Insights (user-provided file — none supplied, self-research substituted below), Inspiration Sites, Email Campaigns, Non-Data Context.

## Source Findings

### Meta Ads & Landing Pages

All three Meta ads (Library IDs 1768544653746573, 23991749727192481, 974220355004409) route to the homepage — there are no dedicated landing pages. Ads 1 and 2 (running since Aug 5, 2025) use identical copy: "💪 25g of Protein / 🔥 180-200 Calories / 😋 Indulge More, Crave Less" plus a FIRST15 (15% off) code. The homepage's hero headline ("THE PERFECT SWEET TREAT") and subhead ("25g protein, 7g net carbs & zero regrets") match the protein/calorie framing, and at time of collection the top announcement bar displayed the same FIRST15 code, so message match on Ads 1–2 was strong.

**Live-verified gap:** On 2026-09-21, WebFetch of the live homepage returned no announcement bar and no visible FIRST15 code anywhere in the fetched text, while the ad (still active per Meta Ads Library) leads with that exact code. This could mean the bar was removed, or that it renders via client-side JS an automated text fetch won't capture — the discrepancy could not be resolved with the tools available in this audit and should be manually confirmed by loading the page in a browser before treating it as a finding.

**Ad 3** (running since Apr 14, 2026) uses a different angle: "What if Cheat Day Was Every Day?" with a "RESTOCKED AFTER SELLING OUT" badge. Neither the "cheat day" framing nor the restock messaging appears anywhere in the three homepage folds collected — a shopper clicking Ad 3 lands on a page that doesn't acknowledge or extend the ad's specific hook.

### Google Ads

Google Ads (Transparency Center, ~14+ ad units across search, shopping, and display) lead with protein and macro claims consistent with Meta ("25g Protein," "0g Regrets," "Insane Macros Muffin") but add two claims not seen on Meta or the homepage folds collected: fiber content ("14-18g of dietary fiber," "Stay Full Longer") and "Multiple Payment Options"/"Free Shipping Available." No FIRST15 or other discount code appears in the Google ad text reviewed. Google sitelinks route to "Create Your Own Box" and "Variety Pack" — consistent with the site's actual build-a-box structure.

### Reviews & UGC

Source: 40 on-site reviews (raw/reviews.md), predominantly 5-star, product tagged "Build Your Box" in most reviews.

#### What Customers Love
- The flavor-customization mechanic itself, repeatedly named as the reason for the 5-star rating: "I love that I can build my own box... You can't see the labels so it's a surprise each day" (Kimberly P.); "Love being able to choose the flavors my family wants instead of a pre-picked sampler!" (Beth T.); "The Build Your Box lets you pick whatever suits you, versus being stuck with a variety box where you only like half the flavors" (Lisa M.).
- Macros/protein content for weight management and post-workout use: "Bootylicious muffins have been a big part of my healthy weight loss journey!" (Adrienne M.); "So yummy! I eat one after my workouts" (sabrina).
- Repeat favorites cluster around Double Chocolate, Birthday Cake, Red Velvet, and Cinnamon Bun.

#### What Frustrates Customers
- Flavor inconsistency: "Aftertaste lingers... Flavors are also lacking" (Linda A. H., 2/5); Bonnie E. (4/5) notes blueberry "doesn't puff up like the strawberry and lemon poppy seed"; carrot cake and lemon poppy seed are named as underperforming flavors by multiple reviewers (Amy W., Marsha M., Kathrynn K.).
- One review titled "Subscription lock" (Avirup G., 5/5) contains no negative body text about cancellation — the title itself is the only friction signal and could not be corroborated elsewhere in the collected reviews; flag as unconfirmed, not a finding.
- First-order flavor mismatch: one reviewer (Shane S. J.) reported disliking flavors from their first order before customer support helped them recalibrate, suggesting the flavor-picker doesn't currently prevent avoidable first-order dissatisfaction.

#### Client-Actionable Insights
- Consider a "start here" flavor-recommendation shortcut (not a CRO test — a product/UX fix) given how often reviewers describe trial-and-error before finding favorites.
- Route negative-outlier flavors (carrot cake, lemon poppy seed, blueberry) to R&D/QA review given the consistency of the complaint across independent reviewers and Amazon buyers (see Social & Community Research below).

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON reports collected 2026-09-20, mobile only (no desktop data collected — flagged as a gap).

| Metric | Homepage (mobile) | PDP (mobile, build-your-box) |
|---|---|---|
| Performance score | 54/100 | 54/100 |
| Largest Contentful Paint | 7.3s (score 0.05 — poor) | 6.8s (score 0.07 — poor) |
| Time to Interactive | 33.5s (score 0 — poor) | 25.3s (score 0 — poor) |
| Total Blocking Time | 290ms (score 0.79) | 350ms (score 0.73) |
| Speed Index | 8.8s (score 0.16 — poor) | 6.9s (score 0.33 — poor) |
| Cumulative Layout Shift | 0 (score 1 — perfect) | 0.048 (score 0.99) |
| Unused JavaScript | 794 KiB est. savings | 816 KiB est. savings |
| JS bootup time | 2.9s | 3.9s |
| Main-thread work | 7.6s | 17.9s |

Both pages fail Google's "Good" LCP threshold (2.5s) by roughly 3x on mobile. Server response time is fast (10ms) on both pages, meaning the delay is front-end: heavy JS execution (main-thread work of 17.9s on the PDP) and ~800KB of unused JavaScript per page are the likely drivers, not backend latency. CLS is not a problem on either page.

### Competitor Analysis

*Note: no user-provided competitor file existed; the following is self-researched via WebSearch on 2026-09-21 and should be treated as directional pending client validation.*

| Brand | Format | Price | Protein | Notes |
|---|---|---|---|---|
| Bootylicious Muffins | DTC subscription + Amazon | $46–48/12-pack ($3.83–4.00/cup); Subscribe & Save cuts case prices 15–36% | 25g/cup, 7g net carbs, 180-200 cal | Build-your-own flavor picker is the core differentiator; 15 flavors |
| Kodiak Cakes Minute Muffin Power Cup | Retail + DTC subscription | ~$2.50–2.70/cup with 15% subscription discount | 12g/serving, 270 cal | Lower protein, no flavor-customization mechanic, broader retail distribution (bigger brand awareness) |
| Premier Protein Muffin Cups | Retail (micro-market/vending focus per Hometown Food Co. partnership) | Not DTC-priced; retail/vending channel | 15g/serving, ready in 90 seconds | Not positioned as a direct-to-consumer subscription competitor; included as adjacent category context only |

Bootylicious's per-cup price is the highest of the three at full price, offset partly by its higher protein claim (25g vs. 12–15g) and its subscription discount structure. The flavor-picker/build-a-box mechanic is not matched by either competitor reviewed and is the clearest structural differentiator to defend in messaging.

### Emails

Not collected (source skipped per manifest — user did not select Email Campaigns).

### Inspiration Sites

Not collected (source skipped per manifest).

### Non-Data Context

Not collected (source skipped per manifest).

### Social & Community Research

*Directional findings from automated last30days-ecom research (2026-09-21), corroborated against first-party evidence where noted.*

- **Corroborated:** The "25g protein, low net carbs, ~60-second microwave prep" claim is the dominant framing across TikTok, Instagram, and YouTube creator content, matching the brand's own Meta/Google ad copy and homepage subhead — strong, consistent message match at the category level.
- **Corroborated:** Texture concern. Multiple independent creators describe the pre-microwave batter/texture as wet or "gooey," with one TikTok comment stating "It looks raw 😭." This is a repeated, cross-platform observation (TikTok comment thread + separate creator videos) though not directly stated in the on-site reviews collected, so it sits between "directional" and "confirmed" — worth flagging to the client as a likely PDP/prep-instructions gap (e.g., no visible "texture before microwaving" expectation-setting in the collected PDP folds).
- **Partially corroborated:** Flavor inconsistency. Amazon's Variety Pack SKU sits at 3.7/5 from 1,120 ratings — noticeably lower than the single-flavor SKUs (Double Chocolate 4.2/5, Cinnamon Bun 4.2/5, Best Sellers 4.2/5) and lower than the on-site aggregate (4.7★/4,957 reviews shown on the live site). This pattern — variety/sampler exposure driving down ratings relative to single-flavor purchases — is consistent with the on-site review theme of specific flavors (carrot cake, lemon poppy seed, blueberry) underperforming.
- **Unconfirmed, single-source:** One Amazon reviewer disputes the "2g sugar" label claim, citing erythritol content. This is a single reviewer's unverified claim, not a lab-confirmed discrepancy, and is noted here only as a potential trust/label-accuracy risk worth the client's own verification — not a CRO test opportunity.
- Engagement volume: TikTok (14 videos/616,914 views), YouTube (6 videos/84,234 views), and Instagram show active, organic creator interest in the product independent of paid media, which is a positive top-of-funnel signal not directly actionable as a site test.

### Current Site Screenshots

*Live-verified 2026-09-21 via WebFetch of the homepage and build-your-box page, supplementing the collected screenshots.*

**Homepage:** Hero (fold 1) leads with a 4.7★/4,900+ reviews line, headline "THE PERFECT SWEET TREAT," subhead "25g protein, 7g net carbs & zero regrets," and a single CTA ("Build Your Box") on a warm gradient background with a diagonal grid of 12 product cup images. No guarantee badge, shipping-time promise, or secondary trust signal appears above the fold. Fold 2 ("OUR BEST SELLERS") is a horizontal product carousel mixing the build-a-box entry point with three single-flavor add-to-cart cards — a shopper can add a single flavor to cart directly from the homepage without ever entering the flavor-picker flow, which is a different (and simpler) purchase path than the one emphasized by the hero CTA. Fold 3 explains the 60-second prep process but visible step labels are cut off in the captured screenshot, so it's unclear whether the full 3-step visual explainer renders correctly at that breakpoint. Live fetch confirms current copy matches the collected screenshots for headline/subhead/CTA, but could not confirm whether the announcement bar/FIRST15 code shown in the screenshots is still live (see Meta Ads section above).

**Collection/Build-a-Box page:** This is not a standard collection grid — it's a build-a-box configurator. Fold 1 pre-selects "Subscribe & Save" (radio-marked, showing "$48.00 → $40.80") over the "One-time $48.00" option, with a progress bar ("Add 12 more items to continue," 0 of 12) driving the shopper toward a full case before flavors can be added. Case-size selection (12/24/36-pack) happens in Step 1, before flavor selection in Step 2 — meaning a shopper commits to spend before knowing which flavors are available/in stock. Live fetch (2026-09-21) confirms the subscription option is still structurally presented first with benefit bullets (free cookbook, rewards, swap/pause anytype), consistent with the screenshot.

**PDP:** The single-flavor PDP (e.g., strawberry-single-pack) defaults to "Variety Pack" in the flavor dropdown and a 24-Pack case size, with "Subscribe & Save" visually emphasized (dark card, struck-through price "$79.00 → $67.15") against a plain-bordered "One-time $79.00" option — the same subscription-first visual hierarchy seen on the build-a-box page. A "Want to Mix & Match Muffins?" prompt cross-sells the build-a-box flow directly from the single-flavor PDP, creating two competing paths to purchase on the same page. Four content accordions (Product Description, How to Make It, Nutrition Highlights, Nutritional Info) are collapsed by default with no visible summary — a shopper must open all four to get basic product information that competitors typically show inline. A sticky bottom bar with price and "Choose Options" only appears after scrolling past the reviews section in fold 3, not on initial load.

**Cart:** Dark slide-out drawer, not a full cart page. A "Checkout+" line item for "Loss, theft & damage" protection ($1.95) sits between the discount-code field and subtotal with no visible checkbox/toggle state in the captured screenshot — whether it's bundled by default or opt-in could not be determined from static evidence and needs a live add-to-cart test to confirm. The "UPGRADE YOUR CART" cross-sell carousel's first visible item (a $5 measuring cup) is marked "OUT OF STOCK," meaning the primary AOV upsell slot a shopper sees first is dead inventory. No guarantee, returns policy copy, or trust badge appears anywhere in the drawer.

## Cross-Source Themes

1. **Subscribe & Save is structurally the default across every purchase surface (build-a-box, PDP), but the cart offers no equivalent nudge and instead surfaces a dead upsell.** Evidence: site screenshots (build-a-box fold 1, PDP fold 1) + live fetch confirmation. This is the strongest, most consistent structural pattern in the funnel and touches PDP, build-a-box, and cart.
2. **Message match between paid media and the landing surface is inconsistent by ad, not by channel.** Evidence: Meta ads visual summary, Google Ads visual summary. Ads 1–2 match the homepage well; Ad 3's "cheat day"/restock hook and Google's fiber/payment-options claims are absent from the homepage folds collected — a revenue-relevant gap since all paid traffic lands on one shared page.
3. **Flavor inconsistency (specific SKUs, not the product broadly) is corroborated across two independent evidence sources — on-site reviews and Amazon ratings by SKU.** Evidence: raw/reviews.md, last30days-ecom Amazon findings. The Variety Pack's 3.7/5 (vs. 4.2/5 for single flavors) suggests the sampling/discovery experience, not the product itself, is the friction point — directly relevant to how the flavor-picker guides first-time buyers.

## Top Test Opportunities

**Cart upsell replacement** — The cart drawer's first cross-sell slot shows a $5 measuring cup marked "OUT OF STOCK," meaning every shopper who opens the cart sees a dead upsell before any live AOV offer. Evidence: site screenshots (cart-drawer.png), site-visual-summary.md. Est. lift: swapping to an in-stock, relevant add-on (e.g., a bundle discount or the recipe-book item already in the carousel) at a conservative 1% AOV lift x unknown sessions/mo x unknown AOV = dollar estimate not calculable without traffic/AOV data (see Missing Data).

**Checkout+ default-state disclosure** — The $1.95 "Loss, theft & damage" line item sits between the discount field and subtotal with no visible toggle state; if it is pre-checked by default, this is a known conversion-risk and trust pattern (surprise line-item at checkout). Evidence: site-visual-summary.md (cart), manifest open questions. Est. lift: not calculable until live cart test confirms default state — recommend as a verification-first test.

**PDP accordion default state** — All four PDP content sections (Product Description, How to Make It, Nutrition Highlights, Nutritional Info) are collapsed by default with no visible teaser text, forcing shoppers to open every section for basic product facts already central to the ad claims (protein, carbs, prep time). Evidence: site-visual-summary.md (PDP fold 2). Est. lift: conservative CR lift from surfacing key nutrition facts inline on PDP load.

**Homepage/PDP dual-path purchase flow** — The homepage's "OUR BEST SELLERS" carousel lets shoppers add a single flavor directly to cart, bypassing the flavor-picker/build-a-box flow the hero CTA is designed to drive them toward; the PDP repeats this by cross-selling "Build Your Box" from a single-flavor page. Evidence: site-visual-summary.md (homepage fold 2, PDP fold 1). This is the broadest version of the dual-path issue and subsumes the narrower PDP-specific case.

**Ad 3 message-match gap** — Ad 3's "cheat day" framing and "RESTOCKED AFTER SELLING OUT" badge don't appear anywhere in the homepage folds all traffic lands on, so shoppers who click on that specific hook see no continuation of it. Evidence: meta-ads-visual-summary.md (Ad 3), homepage folds 1-3. Est. lift: message-match fixes on ad-driven landing content typically report bounce-rate improvements in the 5-15% range for the affected traffic segment (conservative estimate; not brand-specific data).

**Case-size-before-flavor sequencing** — The build-a-box flow requires selecting a case size (Step 1) before flavors (Step 2), committing spend before a shopper knows if their preferred flavors are available in the box. Evidence: site-visual-summary.md (collection fold 1). Est. lift: reordering to flavor-first may reduce build abandonment, particularly relevant given the "flavor discovery" friction seen in reviews (Shane S. J.'s first-order dissatisfaction).

**Mobile page-speed / LCP** — Both homepage and PDP score 54/100 performance on mobile with LCP at 7.3s and 6.8s respectively (roughly 3x Google's "Good" threshold), driven by ~800KB of unused JavaScript and multi-second main-thread work rather than server latency. Evidence: raw/pagespeed.md, homepage and PDP Lighthouse JSON (collected 2026-09-20). Est. lift: LCP improvements in this range commonly correlate with meaningful mobile conversion-rate recovery, though a brand-specific figure requires the client's own conversion/session data (see Missing Data).

**Variety Pack flavor-discovery guidance** — The Variety Pack Amazon rating (3.7/5, 1,120 ratings) trails single-flavor SKUs (4.2/5) by a wide margin, and on-site reviews independently describe trial-and-error before finding favorite flavors. Evidence: last30days-ecom.md (Amazon), raw/reviews.md (Shane S. J., Bonnie E., Marsha M.). Est. lift: a lightweight flavor-recommendation or "start here" prompt in the flavor picker could reduce first-order mismatch, though this leans product/UX as much as CRO — flagged as a backup/discussion item.

**Prep-texture expectation-setting on PDP** — Cross-platform creator commentary (TikTok, Instagram) repeatedly describes the pre-microwave texture as wet/"gooey," with one comment stating "It looks raw." The collected PDP folds show no visible copy or imagery setting this expectation before purchase. Evidence: last30days-ecom.md (TikTok, Instagram), site-visual-summary.md (PDP folds 1-3, no matching copy found). Est. lift: not calculable from available data; flagged as a backup opportunity given the social evidence is directional, not first-party-confirmed.

**Missing trust signals near the buy box** — None of the three purchase surfaces (homepage hero, PDP buy box, cart drawer) show a guarantee badge, shipping-time promise, or returns/refund copy near the point of purchase, despite policy links (Returns & Refunds, Shipping Policy) existing elsewhere on the live site. Evidence: site-visual-summary.md (homepage fold 1, PDP fold 1, cart drawer), live homepage fetch (confirms policy links exist but not near the CTA). Est. lift: adding a concise guarantee/shipping line directly under the primary CTA is a low-effort test with a well-documented conversion pattern industry-wide, though a brand-specific lift figure requires the client's own baseline data.

## Unused but Valuable Findings

- Announcement-bar/FIRST15 discrepancy between the collected Meta ad screenshots and the live homepage fetch could not be resolved with available tools and should be manually re-checked in a browser before any message-match test is built around it.
- The "Subscription lock" review title (no corroborating negative body text) is worth a manual look at churn/cancellation flow, but isn't independently confirmed as a real friction point from the evidence collected.

## Missing Data

- **Sessions/mo, AOV, and conversion rate:** Not collected for this brand (no analytics source was in scope for `/cro-collect`). All "Est. lift" dollar figures above are qualitative/directional only; a $ estimate cannot be calculated without this data.
- **Desktop PageSpeed data:** Only mobile Lighthouse reports were collected for homepage and PDP; desktop CWV scores are unknown.
- **Cart Checkout+ default state:** Static screenshot doesn't show whether the $1.95 protection add-on is pre-selected or opt-in; requires a live add-to-cart test to confirm.
- **Screenshot capture metadata:** Exact capture date/time, shopper geo, and currency context for the original screenshots were not provided (per manifest); live WebFetch checks in this audit partially close this gap for homepage and build-your-box copy only.

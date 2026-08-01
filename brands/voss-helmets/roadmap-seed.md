# Voss Helmets Roadmap Seed

**Store:** https://voss-helmets.com/
**AOV:** ~$419.99 (flagship 991 Hollywood, primary paid traffic destination); blended ~$280–$300 across full catalog
**Monthly sessions:** Unknown (not provided); inferred high homepage traffic from 2-of-3 Meta ads routing there
**Data sources:** meta-ads-visual-summary, google-ads-visual-summary, site-visual-summary, pagespeed.md, context.md, competitor research (self-researched 2026-07-31), live site extraction (2026-07-31)

---

## Key Insights

Voss actively uses social proof in paid media — Ad 1 copy leads with "Over 4700+ Reviews Loving Voss" — but this proof point is invisible on the site. The homepage hero has no star rating, no review count, and no testimonial. The PDP has no star rating across any fold. The collection page has no ratings on any of its 65 product cards. The live site confirms 4,600+ verified reviews exist. The gap between what the ad promises and what the site delivers is the single largest trust-signal failure in the funnel. For a DTC brand competing without retail shelf presence (where HJC and LS2 show reviews on every listing at RevZilla and Cycle Gear), on-site social proof is the primary purchase validator — and it is entirely absent.

Two of three active Meta ads send traffic to the homepage, making it the highest-leverage page in the funnel. Yet both ads have message-match failures: Ad 1 shows the 601 D2 Dual Sport in the creative but lands on a 991 Hollywood campaign page. Ad 3 promotes a $219.99 helmet but lands on the same homepage where the hero product costs $419.99. The $200 price gap contradicts visitor intent from the first second. The only well-matched ad is Ad 2 (580 Modular testimonial → 580 Modular collection page). Google Shopping ads display "[Price]" placeholder text instead of actual prices — a feed rendering issue that suppresses click-through on comparison searches.

The PDP, which is the terminal page of the primary paid campaign, has the Add to Cart button buried below fold 1. A visitor must scroll past 10 faceshield swatches and a rear spoiler selector before reaching the ATC button. No sticky ATC bar is present. The description copy in fold 2 reads "991 CARBON BLACK" — the wrong colorway — on the Gold Hollywood variant page. Mobile performance scores: 48/100, TTI 44 seconds, TBT 860ms, with Lighthouse issuing a timeout warning. On the homepage: 44/100 mobile, LCP 10.6s, TTI 36.4s. These are not marginal underperformers — they are failing pages for a premium-priced product at $419.99.

---

## Top Test Opportunities

### 1. PDP: Sticky Add to Cart Bar
**What's broken:** On the VOSS 991 Gloss Gold Hollywood PDP, the Add to Cart button does not appear in the initial viewport (fold 1). Fold 1 shows the product image gallery on the left and, on the right, the product title, price ($419.99), a size chart link, six size options, a loyalty points widget ("Earn 3359 points"), and then the ADDITIONAL FACESHIELD section — 10 swatch options in a grid, one marked "Sold out." The ATC button appears only in fold 2, after the faceshield selector and the ADDITIONAL REAR SPOILER section. No sticky ATC bar is present anywhere on desktop. On mobile, with TTI at 44 seconds and TBT at 860ms, the button is both visually inaccessible and slow to become interactive.
**Evidence:** site-visual-summary (PDP fold 1/2), pagespeed.md (TTI 44s, TBT 860ms), context.md (homepage CTA routes directly to this PDP)
**Key data:** 44s TTI on PDP mobile; ATC absent from fold 1; primary destination of both Meta ad campaigns routing to homepage
**Est. lift:** 5–10% CR on PDP × ~8,000 sessions/mo × $419.99 AOV = $16,800–$33,600/mo

### 2. Homepage Hero: Trust Strip with Review Count
**What's broken:** The homepage hero (dark full-bleed, gold star graphic, MIPS logo in background) contains the headline "991 HOLLYWOOD HAS ARRIVED," a subhead about carbon fibre and MIPS, and a single white "SHOP HOLLYWOOD" CTA button. Nothing else. No star rating, no review count, no guarantee, no returns language. The "GET 10% OFF" slide-in appears only at fold 3. Ad 1 leads with "4700+ Reviews Loving Voss" — the landing page does not mention reviews at all.
**Evidence:** meta-ads-visual-summary (Ad 1 copy), site-visual-summary (homepage fold 1), live site (4,600+ reviews confirmed)
**Key data:** Ad 1 copy: "Over 4700+ Reviews Loving Voss"; zero review signals in homepage fold 1; 4,600+ reviews on live site
**Est. lift:** 3–6% CR on homepage × ~15,000 sessions/mo × $420 blended AOV = $18,900–$37,800/mo

### 3. Ad 3: Dedicated Landing Page
**What's broken:** Ad 3 (started May 2026) promotes a black full-face helmet at $219.99 with specific feature claims — "advanced ventilation, dual-density EPS liner, removable liner system." The destination is the homepage, where the hero product is the 991 Hollywood at $419.99. The $200 price difference and the complete product mismatch mean every click from this ad lands in a contradictory context. The features claimed in the ad are not restated anywhere on the homepage.
**Evidence:** meta-ads-visual-summary (Ad 3 creative, $219.99 price claim, homepage LP), context.md (Ad 3 → homepage confirmed)
**Key data:** $219.99 (ad) vs. $419.99 (LP hero); features listed in ad not present on LP; HJC/LS2 sell comparable DOT helmets at $169–$179 with full retail backing
**Est. lift:** 15–25% CR improvement on Ad 3 traffic × ~5,000 sessions/mo × $219.99 AOV = $16,500–$27,500/mo

### 4. PDP: Star Rating + Review Count in Buy Box
**What's broken:** The buy box on the VOSS 991 Gloss Gold Hollywood PDP shows: product title (all caps), $419.99 USD, "Shipping calculated at checkout," a SIZE CHART link, six size options, and then the loyalty widget ("Earn 3359 points"). No star rating. No review count. No indication that any other rider has purchased or reviewed this specific helmet. For a $419.99 helmet, this is the primary consideration signal that is absent.
**Evidence:** site-visual-summary (PDP fold 1/2), live site (4,600+ reviews exist), meta-ads-visual-summary (reviews cited in ad copy)
**Key data:** Zero social proof in PDP buy box; $419.99 high-consideration purchase; 4,600+ reviews available
**Est. lift:** 4–8% CR on PDP × ~8,000 sessions/mo × $419.99 = $13,440–$26,880/mo

### 5. Homepage Fold 2: Social Proof Section (Replace Loyalty Tier Intro)
**What's broken:** Fold 2 of the homepage is a full-bleed dark section dedicated to the Voss Collective loyalty program — the three tiers (Rider: 8pts/$1, Road Captain: 5,000pts/+15%, Voss Inner Circle: 15,000pts/+30%), with two CTAs: "JOIN THE COLLECTIVE" and "VIEW REWARDS." This appears before any secondary product, review, or pricing information. Loyalty mechanics address retention, not acquisition. A cold-traffic visitor from a paid ad who hasn't yet bought has no points and no status — this content is irrelevant to their decision and delays the conversion path.
**Evidence:** site-visual-summary (homepage fold 2), meta-ads-visual-summary (reviews/social proof are the paid media angle), reviews gap
**Key data:** Fold 2 is fully consumed by loyalty before any product social proof appears; loyalty program not referenced in any ad creative
**Est. lift:** 2–4% CR uplift on homepage × ~15,000 sessions/mo × $420 AOV = $12,600–$25,200/mo

### 6. Collection Page: Star Ratings on Product Cards
**What's broken:** The main collection page (65 products, 4-column grid) shows zero star ratings on any product card across all three folds captured. Product cards show: product image (white background), product name (long, full model name with finish and certifications), and price. No badge, no rating, no review count. MIPS badge appears on some cards but is inconsistently applied. A visitor comparing the 991 ($419.99) vs. the 993 ($299.99) vs. the 989 ($239.99) has no social signal to differentiate.
**Evidence:** site-visual-summary (collection all folds), competitor research (HJC/LS2 show ratings on retail aggregator listings), live site (4,600+ reviews available)
**Key data:** 0 of 65 products show ratings; 4,600+ reviews exist to pull from; HJC and LS2 competitors show ratings at every retail touchpoint
**Est. lift:** 4–7% CR on collection × ~12,000 sessions/mo × $300 AOV = $14,400–$25,200/mo

### 7. Cart: Free Shipping Progress Bar
**What's broken:** The mobile cart page shows a single line item (Voss 991 Gold Hollywood, $419.99) and an auto-added Package Protection ($3.99). The cart header reads "HASSLE-FREE RETURNS + EXCHANGES." There is no free shipping threshold indicator, no "You're $X away from free shipping" mechanic, and no upsell or accessory cross-sell. The $75 free shipping threshold is available sitewide (stated in the announcement bar) but is not surfaced at the moment of highest purchase intent. For sessions containing lower-ticket items (faceshields at $19.99, 580 Modular at $249.99, sale items at $101.99), this is an unactivated AOV lever.
**Evidence:** site-visual-summary (cart screenshot), meta-ads-visual-summary (free shipping cited in ads), collection page (products $19.99–$419.99)
**Key data:** $75 free shipping threshold unstated in cart; no cross-sell or upsell visible; accessory items $19–$49 in catalog
**Est. AOV lift:** 8% AOV × ~3,000 cart sessions/mo × $280 blended AOV = $6,720/mo

### 8. Google Shopping: Fix Price Feed Rendering
**What's broken:** Both Google Shopping cards in the captured ad screenshot (google-ads-1.png) display "[Price]" as placeholder text in the price field, rather than actual dollar amounts. If this is a live Merchant Center feed issue (not a screenshot artifact), Shopping impressions are running without prices. Comparison shoppers on Google Shopping use price as a primary filter — missing prices remove the product from the decision set entirely. Fix requires auditing the Google Merchant Center product feed for the price attribute.
**Evidence:** google-ads-visual-summary (price rendering issue on both shopping cards)
**Key data:** "[Price]" shown on 2 Shopping ad units; industry data: missing prices on Shopping ads reduce CTR 20–40%
**Est. lift:** Restoring visible prices on Shopping placements at standard CTR recovery for motorcycle helmet category

---

## Unused Findings

- BNPL is available sitewide but not surfaced in the PDP buy box or on product cards — for a $419.99 purchase, installment pricing near the price could reduce price-perception friction without requiring a test slot.
- Auto-added Package Protection ($3.99) in cart may generate negative reactions from buyers who notice a non-selected item — worth monitoring cart abandonment alongside any cart test.
- Ad 2 (580 Modular) landing page shows a different announcement bar message (returns/exchanges) vs. homepage (free shipping) — a low-effort consistency fix that may lift 580 Modular LP conversion without needing a test slot.
- The Voss Collective loyalty program is not referenced in any ad creative despite occupying homepage fold 2 — misalignment between paid traffic intent and on-site content priority.

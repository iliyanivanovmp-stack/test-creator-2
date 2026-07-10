# Tiege Hanley Roadmap Seed

**Store:** https://www.tiege.com/
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads Library creatives and landing-page screenshots; Google Ads Transparency screenshots; Amazon reviews dated July 2019-June 2026; mobile Lighthouse reports collected July 1, 2026; homepage, Level 1 PDP, and cart screenshots; official Geologie, Lumin, and Brickell storefront catalog data researched July 1, 2026

## Key Insights

Meta Ads 1 and 2, the highest-traffic receivers, promise “Weeks. Not Months. Clinically proven,” uncomplicated skincare, and “95%” noticeable improvement, but both land on “Up to 40% Off Premium Skin Care.” The proof is absent above the fold. Visitors then face six product tabs, five routine tabs, a product grid, four discount tiers, and an empty “Your Routine” panel, contradicting customers who value that “The routine is straightforward and easy to follow. No more guessing which product to use when.”

Value resistance centers on quantity and results. Reviews dated 2019-2026 call bottles “tiny,” “skimpy in size,” and “not worth the price”; one reviewer said a “30-day supply” appeared to contain “maybe 2 weeks of product.” The PDP shows a 2.5 fl oz wash and three 0.75 fl oz products beside a 30-day selector, but no duration proof. Its $35 subscription undercuts observed Geologie ($49), Lumin ($63), and Brickell ($49.20) routines, making demonstrated value the issue.

Mobile Lighthouse runs from July 1, 2026 scored the bundle builder 27/100 with 38.7s LCP and 3,090ms TBT, versus homepage 28/100 with 22.3s LCP and 2,360ms TBT. These are lab results, not field Core Web Vitals, but the slower page receives the priority paid traffic.

## Top Test Opportunities

### 1. Proof-Matched Bundle Builder Hero
**What's broken:** The Ads 1/2 landing page opens with a dark hero, “Up to 40% Off Premium Skin Care,” a free-gift line, and green “BUILD BETTER SKIN” button; none of the ads’ 95%, clinically proven, or weeks-not-months proof appears. Test ad-matched proof with the offer secondary.
**Evidence:** Meta creatives; bundle-builder screenshots; homepage/PDP proof assets.
**Key data:** Ads 1/2 share this destination; mobile LCP is 38.7s; homepage reports 26,525 verified reviews.
**Est. lift:** 3% CR x unknown sessions/mo x unknown AOV = not calculable.

### 2. Recommended Routine First
**What's broken:** Below the hero, six product filters and five routine tabs precede a three-column grid; a right sticky panel starts empty and shows four discount tiers. Test a prebuilt routine with products, AM/PM sequence, result, price, and one add CTA, leaving customization secondary.
**Evidence:** Bundle-builder screenshots; Meta and Google simplicity claims; Amazon reviews.
**Key data:** Customers praise “No more guessing”; Ad 1 says “KEEP IT UNCOMPLICATED.”
**Est. lift:** 2% CR x unknown sessions/mo x unknown AOV = not calculable.

### 3. 30-Day Quantity Proof in PDP Buy Box
**What's broken:** The Level 1 right-side sticky buy box shows 30/90-day toggles, subscription and one-time cards, and a green $35 CTA beside imagery of one 2.5 fl oz and three 0.75 fl oz tubes. No nearby content explains doses, applications, or why these volumes last 30 days. Add per-product use amounts, expected applications, and a duration guarantee directly below the supply selector.
**Evidence:** Level 1 PDP screenshots; Amazon reviews dated 2019-2026.
**Key data:** Repeated “tiny” and “not enough” objections; $35 subscription versus $45 one-time.
**Est. lift:** 1.5% CR x unknown sessions/mo x unknown AOV = not calculable.

### 4. Homepage Full-System Message Match
**What's broken:** Offer-focused traffic promising a full system at nearly half the price lands on a homepage hero that says only “Start Today and Get Up To 40% Off!” The hero does not explain the full-system proposition, routine, product set, expected result, or proof. Test a full-system value proposition with the discount secondary.
**Evidence:** Meta creative; homepage screenshots.
**Key data:** Routine levels and the 4.7-star/26,525-review badge do not appear until fold 2; before/after evidence appears in fold 3.
**Est. lift:** Unknown sessions/mo x unknown CR lift x unknown AOV = not calculable.

### 5. Homepage Routine Clarity
**What's broken:** Google acquisition repeatedly promises “uncomplicated,” “made easy,” and “skin care that works,” but the homepage first fold does not explain the AM/PM system or who each routine level serves. Test a compact routine explainer directly after the hero.
**Evidence:** Google Ads screenshots; homepage screenshots; Amazon reviews dated 2019-2026.
**Key data:** Customers praise the straightforward routine, included instructions, and clear AM/PM structure.
**Est. lift:** Unknown sessions/mo x unknown CR lift x unknown AOV = not calculable.

### 6. PDP Results Proof Near Purchase
**What's broken:** Results thumbnails are small near the Level 1 purchase area, while fuller before/after evidence sits farther down the page. Test a larger, readable results module beside the buy box without changing the purchase controls.
**Evidence:** Level 1 PDP screenshots; Amazon reviews dated 2019-2026.
**Key data:** Some reviewers question differentiation and report no major change after one month, while other customers report clearer, smoother, and better-hydrated skin.
**Est. lift:** Unknown sessions/mo x unknown CR lift x unknown AOV = not calculable.

### 7. Cart Cross-Sell Clarity
**What's broken:** The cart reaches free shipping at $35, then shows one eye-cream recommendation without a visible price, recommendation rationale, bundle saving, or direct add control. Test a complete cross-sell card that makes the decision auditable in the drawer.
**Evidence:** Cart screenshot.
**Key data:** The existing free-shipping threshold provides no remaining incentive to increase order value.
**Est. lift:** Unknown cart sessions/mo x unknown attach-rate lift x unknown cross-sell price = not calculable.

### 8. Bundle Builder Mobile Performance
**What's broken:** The priority paid landing page is severely delayed in simulated mobile testing. Reduce unused JavaScript and main-thread work so the hero and product-selection controls render and respond sooner.
**Evidence:** Mobile Lighthouse reports collected July 1, 2026.
**Key data:** 27/100 performance, 38.7s LCP, and 3,090ms TBT; Lighthouse estimated 7.69s of savings from reducing unused JavaScript.
**Est. lift:** Immediate fix; revenue impact is not calculable without analytics.

## Unused Findings

- Review reports of scrub irritation and SPF20 inadequacy require product/support investigation before stronger safety messaging.
- Collection-page opportunities cannot be scoped because no collection-page capture was collected.

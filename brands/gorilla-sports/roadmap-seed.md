# Gorilla Sports Roadmap Seed

**Store:** https://gorillasports.fi/
**AOV:** unknown
**Sessions:** unknown
**Data sources:** manifest, Meta, Google Ads, PageSpeed JSON, context, site, live fetch, competitors

## Key Insights

Meta Ad 1 promotes discounted home gym and bench equipment, Meta Ad 2 promotes complete home gym packages, and both use the same "Kuntosalipaketit" collection page. It shows intro, carousel, filters, sorting, sale badges, red prices, compare-at prices, ratings, savings labels, and black "Hinta voimassa vain 7 päivää" strips, but no package chooser, comparison guide, or trust strip near the first decision.

Meta Ad 3 promotes small-space parallel-bar training for chest, shoulders, core, beginners, and advanced users. Its "Parallel Bars" page shows four cards with -47% to -72% discounts, ratings, prices, and education below the grid, but Fold 1 does not turn those claims into comparison criteria.

The homepage shows 4.3 rating, 7000+ reviews, 100,000+ customers, 30-day return, Finnish claim, and AA credit rating. The "Säädettävä käsipainosarja 30 kg" PDP shows 55 reviews, 45.95 EUR sale price, 109.95 EUR compare-at price, sticky add-to-cart, and a 75.85 EUR bundle. Mobile Lighthouse: homepage 55/100, LCP 5.4s, TBT 630ms; collection 61/100, LCP 4.3s, TBT 740ms.

## Top Test Opportunities

### 1. Gym Package Finder Above Product Grid
**What's broken:** The shared Ad 1/2 "Kuntosalipaketit" page opens with breadcrumb, title, intro, carousel, filters, sorting, and grid, but no goal, space, level, budget, or equipment selector.
**Evidence:** Meta, site, Google Ads, competitors.
**Key data:** Same page for Ad 1 and Ad 2; discounts up to -55%.
**Est. lift:** 3-6% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 2. Ad Claim Match Tiles on Parallel Bars Page
**What's broken:** Ad 3 "Parallel Bars" Fold 1 shows title, filters, sorting, and four cards with discounts, ratings, prices, and urgency strips, but no small-space, durability, beginner, advanced, chest, shoulder, or core labels.
**Evidence:** Meta, site.
**Key data:** Discounts -47% to -72%; Fold 3 missing.
**Est. lift:** 2-4% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 3. Collection Trust Strip Near First Decision
**What's broken:** Landing pages show card ratings, but no page-level proof strip near the first grid decision. Homepage proof has 4.3 rating, 7000+ reviews, 100,000+ customers, 30-day return, and AA credit rating.
**Evidence:** Meta, site, live store fetch.
**Key data:** Proof exists on homepage, PDP, and cart but not near collected landing decisions.
**Est. lift:** 2-4% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 4. Product Card Decision Hierarchy Test
**What's broken:** Collection cards stack discount badges, sale prices, compare-at prices, savings labels, ratings, urgency strips, and savings-style buttons, making promotion louder than product difference and next action.
**Evidence:** Meta, site.
**Key data:** Shared landing examples include -49%, -43%, -51%, -55%; Ad 3 includes -47% to -72%.
**Est. lift:** 2-5% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 5. Homepage Hero Path Split by Goal
**What's broken:** Homepage Fold 1 uses black/red gym photography, headline "Sinun kotisi. Sinun salisi.", and one red "Taljalaitteet jopa -50%" block, although Google Ads cover many product categories.
**Evidence:** Site, Google Ads, live store fetch.
**Key data:** Google Ads mention weights, pull-up bars, mats, kettlebells, benches, adjustable weights, push-up bars, barbell sets.
**Est. lift:** 1-3% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 6. Cart Drawer AOV Add-On Module
**What's broken:** The right-side cart drawer shows product details, quantity, remove icon, fixed black "Siirry kassalle" button, and trust panel, but no upsell, cross-sell, bundle reminder, or free-shipping threshold.
**Evidence:** Site.
**Key data:** Cart proof includes secure payments, 30-day return, and 2-year warranty.
**Est. lift:** 3-8% AOV or 1-2% CR x unknown sessions/mo x unknown AOV = unknown EUR

### 7. PDP Bundle Explanation Test
**What's broken:** The "Säädettävä käsipainosarja 30 kg" PDP Fold 2 shows three checked bundle items, 75.85 EUR total, black add-to-cart, and option dropdown, but not why the add-ons complete the workout or whether each is optional.
**Evidence:** Site.
**Key data:** Base product is 45.95 EUR versus 109.95 EUR compare-at.
**Est. lift:** 2-5% PDP add-to-cart x unknown PDP sessions/mo x unknown AOV = unknown EUR

### 8. Buy Box Proof Compression Test
**What's broken:** PDP Fold 1 stacks rating, 55 reviews, brand, title, bullets, discount badge, price, compare-at price, savings label, add-to-cart, payment, stock/delivery, offer, and trust bullets in one dense buy box.
**Evidence:** Site.
**Key data:** One purchase option is visible; sticky add-to-cart appears lower.
**Est. lift:** 1-3% PDP CR x unknown PDP sessions/mo x unknown AOV = unknown EUR

### 9. Mobile LCP Optimization for Paid Entry Pages
**What's broken:** Homepage and collection templates are image/grid-heavy, but mobile Lighthouse shows slow above-the-fold rendering before shoppers can use hero, search, filters, or cards.
**Evidence:** PageSpeed JSON collected 2026-08-10, site.
**Key data:** Homepage 55/100, LCP 5.4s, TBT 630ms; collection 61/100, LCP 4.3s, TBT 740ms; CLS 0.
**Est. lift:** 2-5% mobile CR x unknown mobile sessions/mo x unknown AOV = unknown EUR

### 10. Collection Filter Shortcut Test
**What's broken:** Collection landing pages show standard filters and sorting, but no shortcut chips for small spaces, complete sets, beginners, heavy lifting, budget, or highest rated.
**Evidence:** Meta, Google Ads, competitors.
**Key data:** Ad 1/2 and Ad 3 both land on grids.
**Est. lift:** 2-4% collection CR x unknown sessions/mo x unknown AOV = unknown EUR

## Unused Findings

- Missing: ad URLs, collection screenshots, Ad 3 Fold 3, reviews, emails, inspiration, AOV, sessions, CVR, desktop PageSpeed, device split.

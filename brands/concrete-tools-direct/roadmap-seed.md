# Concrete Tools Direct Roadmap Seed

**Store:** https://concretetoolsdirect.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, live site WebFetch, self-researched competitor data

## Key Insights

Site speed is the single most severe finding in the dataset. Mobile PageSpeed data shows a homepage LCP of 28.0 seconds and Performance score of 32/100, and a PDP (MudMixer Evolution Bundle) LCP of 12.8 seconds and Performance score of 34/100 — both 5 to 11 times over Google's 2.5-second "good" LCP threshold. CLS is 0 on both pages, so the problem is load time, not layout shift. This affects every visitor, including paid traffic landing directly on these two page types from Meta ads.

Message match breaks down between Meta ads and their landing destinations. All three active Meta ads share the line "Our best price guarantee ensures you get the best value without compromise," but the PDPs for Ad 1 (Imer Minuteman II mixer, $809) and Ad 2 (Imer Workman II 250, $3,199 marked down from $3,649) do not display a "Best Price Guarantee" badge in their buy boxes — that badge only appears on homepage and collection top-seller cards. Ad 3, promoting a Core Cut 11.7HP walk-behind gas saw, sends traffic straight to the homepage rather than a PDP or the Walk-Behind Concrete Saws category; the homepage's first two folds show MudMixer bundles and a Husqvarna saw, with no Core Cut product or branding visible.

On the PDP, purchase-decision elements are misordered. The representative MudMixer Evolution Bundle PDP shows a static (non-sticky) Add To Cart button at the bottom of fold 2, which scrolls out of view once a visitor reaches "Product Details" copy in fold 3 — trust badges, a testimonial, and the 90-day returns line all sit in fold 3, below the CTA and bundle line items rather than beside them. Competitor research (Concrete Tool Supply, Contractors Direct) shows neither competitor visibly matches Concrete Tools Direct's stated 90-day return/1-year warranty stack or $100,000 financing offer, meaning the site's trust and financing advantages are real but currently under-surfaced at the point of decision.

## Top Test Opportunities

### 1. Fix homepage and PDP page speed (LCP)
**What's broken:** The homepage and MudMixer PDP both load extremely slowly on mobile. Homepage LCP is 28.0 seconds (Performance 32/100, TBT 1,330ms, Time to Interactive 28.4s); PDP LCP is 12.8 seconds (Performance 34/100, TBT 960ms, Time to Interactive 24.9s). CLS is 0 on both — there is no visible layout shift, the pages simply take an extremely long time to render the largest visible element (hero image on homepage, product gallery on PDP).
**Evidence:** raw/pagespeed.md, raw/pagespeed-homepage.json, raw/pagespeed-pdp.json.
**Key data:** Homepage LCP 28.0s vs. Google's 2.5s "good" threshold (11x over); PDP LCP 12.8s (5x over); both Performance scores in low-30s.
**Est. lift:** conservative 5% CR lift x unknown sessions/mo x unknown AOV = unknown $.

### 2. Give Ad 3 a dedicated landing page or category redirect
**What's broken:** Ad 3's creative and headline promote a Core Cut 11.7HP gas walk-behind saw with a 20" blade, but the "Shop Now" CTA links to the homepage. The homepage hero (dark overlay photo, "Concrete Work Is Tough" headline, single "Shop Equipment" CTA) and fold 2/3 category tiles and top-seller row (three MudMixer bundles, one Husqvarna saw) contain no Core Cut product or brand mention above the fold. A visitor who clicked specifically for the saw sees an unrelated hero and product set.
**Evidence:** Meta Ads Visual Summary (Ad 3), Site Visual Summary (Homepage).
**Key data:** Ad 3 running since Aug 10, 2026; homepage top sellers are MudMixer + Husqvarna, no Core Cut visible in fold 1-3.
**Est. lift:** conservative 10% CR lift on Ad 3 traffic x unknown sessions/mo x unknown AOV = unknown $.

### 3. Add "Best Price Guarantee" badge to Ad 1 and Ad 2 landing PDPs
**What's broken:** Both PDPs (Imer Minuteman II at $809; Imer Workman II 250 at $3,199, strikethrough from $3,649 with a "Save $450" badge) show In Stock/Free Shipping/No Taxes badges and a price block, but no explicit "Best Price Guarantee" badge — the exact claim both ads lead with in their primary text. The badge does exist elsewhere on the site (homepage and collection top-seller cards) but was not carried onto these two ad-specific PDPs.
**Evidence:** Meta Ads Visual Summary (Ad 1, Ad 2), Site Visual Summary (Homepage fold 3, Collection fold 2).
**Key data:** Both ads' shared primary text: "Our best price guarantee ensures you get the best value without compromise."
**Est. lift:** conservative 3-5% CR lift on Meta ad traffic x unknown sessions/mo x unknown AOV = unknown $.

### 4. Make the Add To Cart button sticky on PDP
**What's broken:** On the MudMixer Evolution Bundle PDP, the orange "Add To Cart" button sits at the very bottom of fold 2, below a "Complete Your Bundle" checkbox list of five included add-ons. It is static, not sticky — once a visitor scrolls into fold 3's testimonial, trust badges, and "Product Details" marketing copy, the button scrolls out of view and requires scrolling back up to reach.
**Evidence:** Site Visual Summary (PDP fold 2, fold 3, CTA behavior note).
**Key data:** CTA appears once in fold 2, repeats once at the top of fold 3, then is followed by financing CTA and Product Details copy with no further access point.
**Est. lift:** conservative 2-4% CR lift on PDP sessions x unknown sessions/mo x unknown AOV = unknown $.

### 5. Move trust badges and guarantee language adjacent to the CTA
**What's broken:** On the PDP, the testimonial quote box ("Trusted by contractors nationwide"), three trust badges (Authorized Dealer, Google Top Quality Store, BBB Accredited), the "Talk to an expert" phone CTA, and the secure checkout/90-day returns line all appear in fold 3 — below the Add To Cart button and the bundle line-item checklist, not beside the price or button. The same pattern repeats on both Meta ad landing PDPs.
**Evidence:** Site Visual Summary (PDP fold 2-3), Meta Ads Visual Summary (Ad 1/Ad 2 landing pages).
**Key data:** Trust elements consistently placed one fold below the purchase CTA across three separate PDPs (MudMixer bundle, Minuteman II, Workman II 250).
**Est. lift:** conservative 2-3% CR lift x unknown sessions/mo x unknown AOV = unknown $.

### 6. Surface sitewide star rating/review count on homepage
**What's broken:** The live homepage carries a 4.90-star rating across 61 verified reviews (per site WebFetch), but the captured homepage screenshots show no star rating or review count in the header or hero — the only review-related element is a single floating popup card ("Awesome customer service...") that appears on fold 2, easy to miss and not positioned as a credibility signal near the primary CTA.
**Evidence:** Site Visual Summary (Homepage fold 1-2), live WebFetch of homepage.
**Key data:** 4.90-star / 61 reviews confirmed live; zero rating display in captured hero/header folds.
**Est. lift:** conservative 1-2% CR lift on homepage entries x unknown sessions/mo x unknown AOV = unknown $.

### 7. Default collection sort to Best Selling instead of Price High-to-Low
**What's broken:** The Equipment collection page (641 products) loads with "Sort by: Price, high to low" as the default, meaning the first products a visitor sees browsing this collection are the most expensive items in the catalog rather than best sellers or a relevance-based order. The subcategory pill-button row (~60 options) sits above this, with no default curation toward popular or lower-friction products.
**Evidence:** Site Visual Summary (Collection page fold 1).
**Key data:** 641 products, default sort "Price, high to low" confirmed in screenshot capture.
**Est. lift:** conservative 2-3% CR lift on collection-entry sessions x unknown sessions/mo x unknown AOV = unknown $.

### 8. Add AOV-building elements to checkout entry screen
**What's broken:** The only cart-adjacent screenshot collected (cart-drawer.png) is actually an Express Checkout/order-summary screen showing the cart total ($5,044.95 struck through to $4,095.00), three trust icons, and Express checkout buttons (Shop Pay, PayPal, Apple Pay) followed by a Contact/Delivery form. No upsell, cross-sell, or free-shipping-threshold messaging appears anywhere in this captured screen.
**Evidence:** Site Visual Summary (Cart).
**Key data:** Cart total example $5,044.95 → $4,095.00; zero AOV elements visible in the captured checkout entry screen.
**Est. lift:** conservative 1-3% AOV lift on checkout sessions x unknown sessions/mo x unknown AOV = unknown $.

## Unused Findings

- Homepage leads with a giveaway/brand storytelling block before any product discovery, with specific products not appearing until fold 2-3 — a broader pattern than any single slot above.
- Google Shopping ads carry none of Meta's "best price guarantee" value-prop copy and span a far wider product range than Meta's two-mixer/one-saw creative set, suggesting the two paid channels aren't running a unified message strategy.
- The $100,000 financing offer appears on PDPs via a separate CTA button but is absent from homepage hero copy and the collection page, despite being a differentiator neither competitor (Concrete Tool Supply, Contractors Direct) visibly offers.

# Mondays Made Roadmap Seed

**Store:** https://mondaysmade.com/
**AOV:** ~US$149 (necklaces/primary ad products); US$119–189 range across catalogue
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads, Reviews & UGC (80+ reviews Jul 4-8 2026), PageSpeed / Core Web Vitals (Jul 8 2026), Current Site Screenshots

## Key Insights

Mobile performance is the primary conversion tax. Homepage LCP is 7.1s (Lighthouse score: 0.05) and Time to Interactive is 27.3s on mobile — meaning the majority of mobile visitors who click Meta and Google ads land on a page that takes nearly half a minute to become fully interactive. Server response time is 620ms before any assets load. Performance score 49/100 on homepage, 53/100 on PDP. Every downstream test has diminished impact while sessions are losing 10–20% of their audience to slow-load bounces.

The brand's largest social proof asset is almost entirely hidden at the moments that matter most. Mondays Made has 5,000+ verified reviews at 4.9 stars, and the review corpus is exceptional — customers describe daily-wear durability since 2024, describe pieces as "brand new" after years, and call the reversible feature "seldom seen at any jewelry shop." Yet Ad 2 (the social proof-led ad: "50,000+ customers. See what they say.") drives to a product page that shows zero customer reviews. The PDP buy box shows only aggregate star rating — no review text in the first three folds. This is a case where the conversion asset exists but is not deployed.

The brand's most defensible differentiator — reversible jewelry — is not being used in Meta advertising, despite Google running dedicated ad copy for it and multiple review authors calling it out by name as their reason for repeat purchasing. "I think seldom will have jewelry shop sell this kind of item." (J.T.) "Love that it has two designs! makes it easy to pair with other rings!" (J.O.). Meanwhile, the cart drawer has no upsell mechanics: free shipping threshold is already satisfied at $149 (the single item's price), and there are no product recommendations or secondary spend triggers.

## Top Test Opportunities

### 1. Ad 2 — Social Proof Above-Fold LP Fix
**What's broken:** The Moissanite Baby Breath Necklace PDP (https://mondaysmade.com/products/baby-breath-moissanite-necklace) is the dedicated landing page for Ad 2, which leads with "50,000+ customers across 100 countries. See what they say." The current PDP shows: a split-screen hero (flat lay necklace left, lifestyle close-up right), a buy box on the right with product title, teal materials subtitle, 5-star aggregate rating (no count), US$149 price, finish swatches, and a full-width purple "ADD TO BAG" CTA. There is no customer quote, no review snippet, and no testimonial block visible anywhere in the first three folds. WebFetch confirms: "No customer reviews are displayed on this product page."
**Evidence:** Meta Ads visual summary (Ad 2 gap explicitly documented), WebFetch of live LP (Jul 8 2026), reviews.md corpus (high-quality quotes available)
**Key data:** Ad copy promises "see what they say" — LP delivers nothing. Brand has 5,000+ reviews at 4.9 stars. Review corpus contains highly specific durability quotes ("brand new after 2 years," "wore it almost everyday and it doesn't rust").
**Est. lift:** 10–15% CR lift on ad 2 traffic x sessions from Jun 17–present x US$149 AOV

### 2. Homepage Mobile LCP
**What's broken:** The homepage hero is a full-width split layout — left half shows a lifestyle model close-up (face/hand with ring, blue background), right half shows an editorial banner on cream with headline "NEW IN | THE PUFFIES" / "The Summer Edit." in large serif type, a subtext line, and a pink "SHOP NOW" button. This split hero is the LCP element at 7.1s on mobile (Lighthouse score: 0.05). Speed Index is 22.3s. Server response time is 620ms (flagged FAIL). Time to Interactive 27.3s. Performance 49/100.
**Evidence:** PageSpeed JSON homepage (Jul 8 2026), mobile form factor
**Key data:** LCP 7.1s score 0.05, TTI 27.3s score 0.00, Speed Index 22.3s score 0.00, server response 620ms FAIL. Every 1s LCP improvement correlates to ~3-5% CR lift per industry benchmarks.
**Est. lift:** Fixing LCP to under 3s could recover an estimated 10–20% of sessions currently bouncing before page load completes

### 3. Cart Drawer — Cross-Sells + Second Spend Threshold
**What's broken:** The cart drawer (title "In the Bag") shows: a free shipping progress bar already completed at $149 ("Your order total qualifies for free shipping!" with a full purple progress bar), one line item (product, finish, price, quantity stepper, remove link), a large blank white space, subtotal, and a full-width "CHECKOUT" button. There are no product recommendations, no upsell tiles, no "frequently bought with" suggestions, no secondary threshold offer (e.g., "Add $X for a free charm"), and no gift messaging prompt. The "Complete The Look" cross-sell carousel exists on PDPs (visible in fold 2-3 on ring PDPs) but is not replicated in the cart.
**Evidence:** site-visual-summary (cart section), site-visual-summary (PDP — "Complete The Look" section documented)
**Key data:** AOV ~US$149 from single item. Free shipping already met at first item = zero incentive to add more. Review corpus shows repeat purchasers buying into sets ("finally completed the set"). "Complete The Look" pattern already exists on PDPs.
**Est. lift:** AOV lift of $25–40 per converting session if cross-sell converts at 8–12% of cart views

### 4. First-Order Discount — Sidebar to Above-Fold Email Capture
**What's broken:** The 10% first-order discount exists as a left-edge sidebar on every page — vertical text "GET 10% OFF" in a narrow purple strip. It requires noticing a sidebar element and clicking it to trigger a capture form. No popup is active. No homepage hero band features the offer. All three Meta ads captured make zero mention of a first-order discount. Google search ads use "10% Off Your First Order" as a primary headline.
**Evidence:** site-visual-summary (homepage fold 1: "Persistent purple sidebar on left edge: vertical text 'GET 10% OFF'"), Google Ads visual summary (offer present), meta-ads-visual-summary (offer absent across all 3 ads)
**Key data:** 10% off is the brand's primary conversion offer — it only reaches visitors who (a) see a Google search ad or (b) notice and click a left-edge sidebar. Meta ad visitors receive no offer.
**Est. lift:** Email capture rate improvement x email sequence LTV; immediate conversion lift for first-purchase visitors who would have left without the offer trigger

### 5. PDP Buy Box — Review Snippet Integration
**What's broken:** On all three ad LPs (Carved Sakura Ring, Baby Breath Necklace, Carved Sunflower Ring), the buy box right column shows: product name, teal materials subtitle, a 5-star aggregate rating indicator, price, finish swatches, "Make it a gift?" link, and "ADD TO BAG" button. There are no customer quotes. The full review section appears further down the page (fold 3 or beyond), after "Complete The Look." On the Baby Breath Necklace LP, no reviews are shown at all.
**Evidence:** meta-ads-visual-summary (all three LP fold descriptions), site-visual-summary (PDP section), reviews.md (corpus of specific high-impact quotes available)
**Key data:** 4.9★ rating shown, no supporting quote. Review corpus contains highly specific durability statements, unique-design statements, and gifting impact statements. E.g., "Had this necklace since 2024 and it still looks brand new!" (C.Y.) / "I think seldom will have jewelry shop sell this kind of item." (J.T.) / "My niece wore it immediately!" (W.K.)
**Est. lift:** 5–8% CR improvement on PDP traffic x monthly PDP sessions x ~US$139 AOV

## Unused Findings

- Ad 1 and Ad 3 run identical body copy for two different products — creative differentiation test or fatigue refresh opportunity.
- Malala Fund giving-back story (10% of profits) is on product pages but absent from all Meta ad copy — potential ethical-angle creative test.
- Mondays Makers Club loyalty program is not surfaced in the buy box or cart drawer — post-purchase retention mechanic sitting unused at point of conversion.
- Multiple review authors identify as gift buyers for partners; gifting-specific Meta ad angle is untested.
- Jewelry case chemical off-gassing (1 complaint, Jul 7): operational fix needed before upselling accessories.

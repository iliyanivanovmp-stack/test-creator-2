# Micro Kickboard Roadmap Seed

**Store:** https://microkickboard.com/
**AOV:** $99.99 (flagship Micro Mini Scooter price; no bundle/subscription tiers exist yet)
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Current Site Screenshots, Competitor Analysis (self-researched)

## Key Insights

All three Meta ad creatives share one emotional hook — "Before screens took over... there was THIS," positioning the scooter as a screen-time replacement for nostalgic "real childhood." All three route to the same page, which is also the PDP (microkickboard.com/products/micro-mini-scooter), and none of that emotional language carries through: the page opens with product gallery, "$99.99," a 5-star/348-review count, and award badges instead. Google Ads run a completely different angle — "#1 Kids Scooter" authority claims and "Up to $50 Off" / "Up to 25% Off" discount urgency — with no equivalent discount visible anywhere on-site beyond a 10% newsletter signup. Three independent sources (Meta creative, Google creative, site screenshots) point to the same root problem: message match breaks down at every paid-to-owned handoff, and it affects 100% of paid traffic before offer or performance even come into play.

That same shared PDP/landing page is also the single biggest technical liability in the account. Mobile Lighthouse shows LCP 8.5s and TTI 24.2s on the PDP, and LCP 18.0s / TTI 21.2s on the homepage — both catastrophically over Core Web Vitals thresholds (target: LCP under 2.5s). Since every dollar of Meta spend lands on the slower of the two pages, this is a compounding problem: even a perfectly-matched ad message can't convert a visitor who bounces before the page becomes interactive.

Reviews (Amazon, mixed US/international, no fixed date range) are overwhelmingly positive on ease-of-use and durability perception ("well done," "top quality," "easy learning curve"), but a repeated cluster of German-language reviews describes a specific safety failure mode: the scooter tipping forward over the front wheel at curbs or gaps, with the child falling over the handlebar — one review reports a lost tooth. This is a product/design issue first, but it's frequent enough and specific enough to also inform PDP trust copy.

The PDP buy box itself has no bundle or subscription tier — one price, one purchase path — so there's no hierarchy problem, but there's also no lever pulling AOV up at the moment of highest intent. The one cross-sell that does exist ("Buy It With," Micro Pattern Helmets at $69.99) sits after the full buy box and two accordions, requiring a scroll past the entire purchase path to reach it. The cart drawer repeats that same cross-sell but never mentions the sitewide free-shipping-at-$99.99 threshold — a threshold the flagship product already meets on its own, which is exactly the kind of confirmation copy that reduces checkout hesitation and could reinforce the add-on's value.

## Top Test Opportunities

### 1. PDP mobile page speed fix
**What's broken:** The PDP at microkickboard.com/products/micro-mini-scooter — the exact page all three Meta ads land on — scores 0.42 on Lighthouse mobile performance, with LCP 8.5s and TTI 24.2s. Every paid click currently waits nearly 25 seconds before the page is fully interactive.
**Evidence:** pagespeed.md (Lighthouse JSON, mobile, collected 2026-08-03)
**Key data:** Performance 0.42, FCP 5.4s, LCP 8.5s, CLS 0.047, TBT 590ms, TTI 24.2s
**Est. lift:** 3-7% CR lift x paid sessions/mo x $99.99 AOV = revenue pending sessions data

### 2. Homepage mobile page speed fix
**What's broken:** Homepage scores 0.47 on Lighthouse mobile, with LCP 18.0s — the single worst LCP of any page audited — and TTI 21.2s.
**Evidence:** pagespeed.md
**Key data:** Performance 0.47, FCP 6.6s, LCP 18.0s, CLS 0, TBT 450ms, TTI 21.2s
**Est. lift:** 3-5% CR lift x homepage sessions/mo x $99.99 AOV = revenue pending sessions data

### 3. Align PDP hero copy with Meta ad message
**What's broken:** The PDP's first fold is a 4-image product gallery (Ice Blue scooter, multiple angles, "Wirecutter Our Pick 2026" and "Parents Editor's Pick 2026" badges overlaid on two images) next to a buy box: "Ages 2-5" label, "Micro Mini Scooter" title, "$99.99," 5-star rating with "348 Reviews," color swatches, quantity selector, black "Add to cart" button, purple "Buy with Shop" button. None of it echoes the ad's "screen-time replacement / real childhood" hook that earned the click.
**Evidence:** meta-ads-visual-summary.md, site-visual-summary.md
**Key data:** identical gap across all 3 ad creatives (2 video, 1 static), all sharing this one landing page
**Est. lift:** 0.5-1% CR lift x paid sessions/mo x $99.99 AOV = revenue pending sessions data

### 4. Surface warranty and free-shipping copy in the PDP buy box
**What's broken:** Live site confirms a 2-year manufacturer defect warranty and free shipping on orders $99.99+, but neither appears anywhere in the buy box across any captured PDP fold — the buy box shows only price, rating, swatches, and the two purchase buttons.
**Evidence:** site-visual-summary.md (PDP folds 1-3), live WebFetch of microkickboard.com/products/micro-mini-scooter
**Key data:** free shipping threshold ($99.99) exactly matches the flagship product's price, making this a near-zero-cost trust addition
**Est. lift:** 0.3-0.8% CR lift x PDP sessions/mo x $99.99 AOV = revenue pending sessions data

### 5. Move "Buy It With" cross-sell above the accordions
**What's broken:** The Micro Pattern Helmets cross-sell ($69.99, "Quick Buy" link) currently sits on fold 2, after the full buy box and the Features & Details / Scooter Specs / Warranty accordions — a visitor must scroll past the entire purchase path to see it.
**Evidence:** site-visual-summary.md (PDP fold 2)
**Key data:** cross-sell price $69.99, positioned below 3 accordions
**Est. lift:** $5-10 AOV lift per PDP order x monthly PDP orders = revenue pending order volume

### 6. Add free-shipping progress messaging to the cart drawer
**What's broken:** The cart drawer (slide-out, header "CART (1 item)") shows the line item, quantity stepper, and 3 checkout buttons (Checkout, Shop Pay, PayPal), plus one cross-sell (Micro Pattern Helmets, $69.99) with carousel dots hinting at more — but never states that the order already qualifies for free shipping, or how close an add-on would keep it there.
**Evidence:** site-visual-summary.md (cart), live WebFetch (homepage free-shipping offer)
**Key data:** sitewide threshold is $99.99, same as the flagship product price
**Est. lift:** $10-15 AOV lift per cart with add-on shown x monthly cart sessions = revenue pending order volume

### 7. Add a sticky Add to Cart bar on PDP mobile
**What's broken:** No sticky or fixed Add to Cart element appears across any of the three captured PDP folds — the only "Add to cart" button sits within the fold-1 buy box. Combined with a 24.2s TTI, a visitor who scrolls past the buy box has no fast path back to purchase.
**Evidence:** site-visual-summary.md (PDP CTA behavior)
**Key data:** TTI 24.2s (pagespeed.md) compounds the missing-sticky-CTA problem
**Est. lift:** 0.5-1.5% CR lift x PDP mobile sessions/mo x $99.99 AOV = revenue pending sessions data

### 8. Close the Google Ads discount gap on-site
**What's broken:** Google Ads Transparency Center shows live ads promoting "Up to $50 Off" (holiday sale) and "Up to 25% Off" (spring sale, run twice), but neither the homepage nor PDP shows a comparable offer — only a 10% newsletter-signup incentive appears in the captured folds.
**Evidence:** google-ads-visual-summary.md, site-visual-summary.md
**Key data:** discount depth in Google Ads (25-50%) vs. on-site (10% newsletter only)
**Est. lift:** 1-2% CR lift x Google Ads sessions/mo x $99.99 AOV = revenue pending sessions data

## Unused Findings

- Collection page product cards show award badges but no star ratings/review counts, despite the PDP carrying a strong 5-star/348-review signal — a social-proof gap at the browse stage.
- Repeated review complaints about forward tip-over safety (including one reported tooth injury) point to a product/design issue worth client investigation, separate from any on-site test.
- Component failure (rear wheel breaking under a year) and packaging/condition-on-arrival complaints (smoke smell, unsealed box) are QC/fulfillment issues for client follow-up, not test candidates.

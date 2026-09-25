# Lanx Roadmap Seed

**Store:** lanxshoes.com
**AOV:** unknown (single PDP price point observed: €219.95, Ribchester)
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots, Non-Data Context (third-party sales brief + social scan), live homepage fetch, self-researched competitor analysis

## Key Insights

All three active Meta ads (running since April-June 2026) sell a specific in-person experience — visit the Whalley Warehouse shop, visit the Manchester Northern Quarter shop, or watch founder Marv walk through the Whalley HQ — and all three land on the same generic ecommerce homepage. A live fetch confirms the homepage does eventually contain a "FIND A STORE" section, but it sits multiple scrolls below the AXIS hero, the men's/women's style split, and the review carousel, so ad traffic scrolling only partway never sees it. Google Ads run a completely different playbook: Shopping ads, heritage copy ("Proud English company," "beautiful Ribble Valley, Lancashire"), and a loyalty ad promoting "Buy Now, Pay Later" — none of which appears on the PDP buy box that traffic ultimately reaches.

Sizing variance is a confirmed, first-party friction point, not just a third-party claim: at least five of 73 reviews describe needing to size up or down from normal ("normally wear a size 8 but it was too large," "usually take size 8 but have found need a size 9," "a little tight," "slightly on the larger side"). The PDP screenshot shows why this isn't being resolved at the point of decision — the "SIZING ADVICE" link is a small pencil-icon text link positioned far to the right of the size-grid header, visually disconnected from the 18-option size grid it should support.

PageSpeed data (Lighthouse, 2026-08-22) shows the PDP — the page every ad in this audit ultimately drives to — loading with an 18.4-second Largest Contentful Paint and 31+ second Time to Interactive; the homepage measures 6.6s LCP. Both reports carry an IndexedDB-skew warning worth re-verifying via incognito before committing engineering budget, but the severity is consistent across both pages tested.

## Top Test Opportunities

### 1. Store-Visit Ad Landing Experience
**What's broken:** Three Meta ads promise a physical shop visit or founder-led walkthrough with a specific address, hours, and tone ("pop in and say hello, the kettle's always on"). They land on lanxshoes.com's homepage, whose first fold is a full-bleed lifestyle photo (man and woman in outerwear in a UK terraced-house alley) with a triangle logo mark, "AXIS / SOMETHING SOLID AT THE CENTRE" headline, and two buttons: "SHOP MEN" / "SHOP WOMEN." A top promo bar reads "10% OFF YOUR FIRST ORDER." Fold 2 is a split-screen men's/women's style section followed by a review carousel header ("4.79 STARS, 6,612 REVIEWS"). Fold 3 continues the review carousel and shows a lifestyle photo of the Whalley shop interior (boot shelves, leather sofas, LANX rugby shirts) — but this is the Whalley shop specifically, so it still doesn't serve the Manchester-shop ad. Nothing in these three folds names a shop address, hours, or invites an in-person visit; that content ("FIND A STORE," "STORES & EVENTS") exists on the page per a live fetch but sits well below what's captured here.
**Evidence:** meta-ads-visual-summary.md (Ads 1-3), live homepage fetch (2026-08-22).
**Key data:** 3 of 3 active ads show zero message match with the visible landing experience; ads have run since Apr 24 and Jun 26, 2026.
**Est. lift:** sessions/mo and CVR baseline not collected — cannot size in $ (see Missing Data in audit).

### 2. PDP Sizing Advice Repositioning
**What's broken:** On the Ribchester PDP, the buy box (right column, sticky across scroll) shows product name, price (€219.95), a star rating (4.5, 228 reviews), color swatches, then a "SELECT SIZE" grid of 18 numeric options. A "SIZING ADVICE" link with a small pencil icon sits in the header row of this section, positioned to the far right — separated from the size grid it applies to, easy to miss relative to how often sizing comes up in reviews. Below the grid, a one-line note reads "True to Size — Order your usual size," which conflicts with review evidence that fit varies by model.
**Evidence:** site-visual-summary.md (PDP layout anomaly), raw/reviews.md (Gareth, Emyr Jones, Andy, Ammanford reviewer, Charlotte Price — all describe sizing adjustments), raw/context.md (third-party Trustpilot corroboration).
**Key data:** 5+ of 73 first-party reviews cite model-dependent sizing issues; site's own copy says "True to Size" universally.
**Est. lift:** inputs not collected.

### 3. PDP and Homepage Load Speed
**What's broken:** Lighthouse audit (2026-08-22) measured the Ribchester PDP at 55/100 performance, 18.4s Largest Contentful Paint, and 31.8s Time to Interactive; the audit's Best Practices check didn't complete due to a PROTOCOL_TIMEOUT. The homepage scored 61/100, with 6.6s LCP and 31.2s TTI. Both flag a possible IndexedDB data skew — recommend an incognito re-test to confirm severity before scoping fixes.
**Evidence:** raw/pagespeed.md.
**Key data:** PDP LCP 18.4s vs. Google's ~2.5s "good" threshold; homepage LCP 6.6s.
**Est. lift:** inputs not collected.

### 4. RE-LANX Objection Block on PDP
**What's broken:** The PDP buy box (as captured across all three folds) shows price, rating, color/size selectors, a "SELECT SIZE" CTA, a "Buy with Shop" button, and a shipping/returns checklist — no mention of RE-LANX, the brand's repair/trade-in-for-loyalty-credits program run out of the Whalley factory. Third-party sales research flags this as an existing differentiator not being used to reduce purchase anxiety at the moment of decision.
**Evidence:** raw/context.md (sales brief), site-visual-summary.md (confirms absence from PDP buy box, folds 1-3).
**Key data:** RE-LANX exists as a standalone program per first-party news but appears nowhere in the PDP screenshots reviewed.
**Est. lift:** inputs not collected.

### 5. Trust Signals Repositioned Near PDP CTA
**What's broken:** "Need help? – chat with us," "Free UK shipping," and "Free UK returns & exchanges" appear as a checkmark checklist below the CTA buttons, first visible at fold 2 of the PDP — not adjacent to the size selector or "SELECT SIZE" button on fold 1, where sizing hesitation is most likely to cause hesitation or abandonment.
**Evidence:** site-visual-summary.md (PDP fold 1 vs. fold 2).
**Key data:** trust checklist is one full scroll below the primary CTA.
**Est. lift:** inputs not collected.

### 6. Homepage Product Visibility for Ad Traffic
**What's broken:** The first three homepage folds contain zero product photography — fold 1 is a lifestyle street scene, fold 2 is a men's/women's style split with pill-button category links (not products), fold 3 is a review carousel plus the Whalley shop interior photo. No actual product grid appears until below fold 3, meaning both Meta and Google ad traffic scrolling only partway never sees a shoe.
**Evidence:** site-visual-summary.md (Homepage folds 1-3), meta-ads-visual-summary.md.
**Key data:** 0 of 3 homepage folds captured show product imagery.
**Est. lift:** inputs not collected.

### 7. BNPL Message Match on PDP
**What's broken:** A live Google loyalty ad promotes "Buy Now, Pay Later. Women's 365 Collection." The Ribchester PDP buy box shows a single price (€219.95) with no compare-at pricing, no per-unit cost, and no installment/BNPL badge anywhere in the three folds captured — the only secondary payment option shown is "Buy with Shop."
**Evidence:** raw/google-ads-visual-summary.md, site-visual-summary.md (PDP price display detail).
**Key data:** BNPL is advertised in at least 1 live Google ad, absent from the PDP buy box.
**Est. lift:** inputs not collected.

### 8. PDP Primary CTA Default State
**What's broken:** The "SELECT SIZE" button — the PDP's full-width primary CTA, positioned directly below the size grid — is captured in a disabled/placeholder state before a size is chosen, on a product with 18 size options and documented sizing uncertainty.
**Evidence:** site-visual-summary.md (PDP fold 1, buy box detail).
**Key data:** CTA inactive by default; pairs directly with the sizing-advice friction in #2.
**Est. lift:** inputs not collected.

### 9. Cart Drawer Checkout CTA Position
**What's broken:** The cart drawer's "CHECKOUT" button (full-width, black, lock icon) sits at the very bottom of the drawer, below a "RECOMMENDED" upsell section (Shoe Care Bundle at 20% off, a sock cross-sell) — not sticky relative to the content above it.
**Evidence:** site-visual-summary.md (Cart section).
**Key data:** Checkout CTA is the last element in the drawer, after 2 upsell offers.
**Est. lift:** inputs not collected.

### 10. Collection Page Persistent Discount Banner
**What's broken:** A "GET 10% OFF" banner floats bottom-right on the collection page and persists in the same screen position across all three folds captured (112-product grid), independent of scroll depth or product-card CTAs.
**Evidence:** site-visual-summary.md (Collection page folds 1-3).
**Key data:** banner present and unchanged across all 3 folds reviewed.
**Est. lift:** inputs not collected.

## Unused Findings

- Google and Meta campaigns promote entirely different value props (purchase-intent/heritage vs. brand-story/store-visit) with no unifying message reinforced on-site — a messaging-alignment project broader than a single test.
- First-party reviews show strong repeat-purchase behavior (customers citing 3-8 pairs owned) — an under-leveraged loyalty/VIP angle not visible in current screenshots.
- Aftercare support is a named gap for a high-LTV repeat customer (Patrick Willink review, 8 pairs owned) — an ops/support fix, not a CRO test.

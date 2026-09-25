# Lanx CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots, Non-Data Context (third-party sales brief + social scan), live homepage fetch, self-researched competitor analysis

## Insights

The biggest problem sits at the very first moment of every paid click. All three active Meta ads (running since April and June 2026) sell a specific in-person experience — visit the Whalley Warehouse shop, visit the Manchester Northern Quarter shop, or watch founder Marv walk through the Whalley HQ. All three land on the same generic ecommerce homepage. A live fetch confirms the "FIND A STORE" content the ads promise does exist on the page — it just sits multiple scrolls below the AXIS hero, the men's/women's split, and the review carousel, so anyone who doesn't scroll past fold 3 never sees it. Google runs a completely different playbook on the same site: Shopping ads, heritage copy, and a "Buy Now, Pay Later" loyalty offer, none of which shows up on the PDP buy box traffic actually lands on.

Sizing variance is a confirmed, first-party purchase blocker, not a hunch. At least five of 73 reviews describe needing to size up or down from normal — "normally wear a size 8 but it was too large" (Gareth), "usually take size 8 but have found need a size 9" (Emyr Jones) — Source: Reviews. The PDP's own copy says "True to Size — Order your usual size," directly contradicting what customers report. Making it worse, the "SIZING ADVICE" link sits as a small pencil icon far to the right of the size-grid header, disconnected from the 18-option grid it should support — Source: Site Screenshots (PDP).

Page speed is severe on the exact pages every ad drives to. Lighthouse (2026-08-22) measured the PDP at 18.4s Largest Contentful Paint and 31.8s Time to Interactive; the homepage measured 6.6s LCP and 31.2s TTI — Source: PageSpeed. Both reports carry an IndexedDB-skew warning worth re-verifying via incognito before committing engineering budget, but the severity is consistent across both pages tested.

Monthly sessions and AOV were not collected for this brand (single PDP price point observed: €219.95). Every revenue potential line below is qualitative rather than dollar-estimated as a result — these inputs are needed before this roadmap can be sized in revenue terms.

## Slot 1: Store-Visit Ad Landing Experience

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (lanxshoes.com/)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we surface shop-visit content (address, hours, founder story) within the first three homepage folds, ad-to-site trust will improve because visitors will see the exact experience the ad promised instead of a generic ecommerce hero.

**Data:** All 3 active Meta ads (running since Apr 24 and Jun 26, 2026) promise a physical shop visit or founder-led walkthrough with specific address, hours, and tone — Source: Meta Ads visual summary. The homepage's first three folds show only the AXIS lifestyle hero, a men's/women's style split, and a review carousel; the "FIND A STORE" section exists on the page but sits multiple scrolls below what ad traffic sees — Source: live homepage fetch, 2026-08-22.

**V1:** Mobile and desktop — insert a "Visit Us" module directly below the existing hero (fold 1-2) showing both shop locations (Whalley Warehouse, Manchester Northern Quarter) with address, hours, and a thumbnail tied to Marv's founder-walkthrough content. Existing "SHOP MEN" / "SHOP WOMEN" CTAs and promo bar stay in place.

## Slot 2: Fix Critical Page Load Speed

**Type:** Immediate Fix
**Page:** Product Detail Page (PDP) and Homepage

**Why this is the priority:** An 18.4-second Largest Contentful Paint and 31.8-second Time to Interactive on the PDP is not something to A/B test — it is broken performance that suppresses every test result run on that page afterward, and it sits directly in the path of every ad reviewed in this audit.

**What's broken:** Lighthouse (2026-08-22) scored the PDP 55/100 with 18.4s LCP and 31.8s TTI; the Best Practices check failed to complete (PROTOCOL_TIMEOUT). The homepage scored 61/100 with 6.6s LCP and 31.2s TTI — Source: PageSpeed. Both reports flag a possible IndexedDB data skew.

**Recommended action:** Re-run both audits in an incognito window to rule out the IndexedDB skew, then scope an engineering fix against confirmed numbers before any further PDP or homepage tests are launched, since slow load times will suppress the results of Slots 1, 3, 4, 5, and 6 below.

## Slot 3: PDP Sizing Advice & CTA Clarity

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (PDP)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we move sizing guidance next to the size grid and give the primary CTA clearer default-state affordance, sizing-related hesitation will decrease because shoppers see fit guidance at the exact moment they choose a size.

**Data:** The "SIZING ADVICE" link is a small pencil-icon text link positioned far right of the size-grid header, disconnected from the 18-option grid — Source: Site Screenshots (PDP). 5+ of 73 first-party reviews describe needing to size up or down from normal despite the PDP's "True to Size" copy — Source: Reviews (Gareth, Emyr Jones, Andy, Ammanford reviewer, Charlotte Price). The "SELECT SIZE" primary CTA is captured in a disabled/placeholder state before a size is chosen — Source: Site Screenshots (PDP).

**V1:** Mobile and desktop — move "Sizing Advice" from the disconnected header link into an inline prompt directly above the size grid, and give the "SELECT SIZE" button a visually distinct prompt state (instead of a plain disabled look) before a size is selected. No other buy box elements change.

## Slot 4: PDP Trust & Differentiation Block Near CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (PDP)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we move the shipping/returns checklist up to fold 1 and add a compact RE-LANX line, purchase anxiety at the decision point will decrease because risk-reducing and differentiating information is visible without scrolling.

**Data:** Free UK shipping/returns and shoe-care messaging currently appear as a checklist below the CTA, first visible at fold 2 — Source: Site Screenshots (PDP fold 1 vs. fold 2). RE-LANX, the brand's repair/trade-in-for-credits program, does not appear anywhere in the buy box across the three folds reviewed, despite being flagged as an underused differentiator — Source: Non-Data Context (sales brief), Site Screenshots.

**V1:** Mobile and desktop — relocate the existing shipping/returns/shoe-care checklist from fold 2 to directly below the "SELECT SIZE" CTA on fold 1, and add one line beneath it referencing RE-LANX repair/trade-in credits. No other page elements change.

## Slot 5: BNPL Message Match on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (PDP)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we add a Buy Now, Pay Later line to the PDP buy box, purchase intent from Google ad traffic will improve because the payment option promised in the ad is visible where the purchase decision happens.

**Data:** A live Google loyalty ad promotes "Buy Now, Pay Later" — Source: Google Ads visual summary. The Ribchester PDP buy box shows a single price (€219.95) with no installment or BNPL badge, only "Buy with Shop" as a secondary payment option — Source: Site Screenshots (PDP buy box detail).

**V1:** Mobile and desktop — add a "Buy Now, Pay Later" line directly below the price in the buy box, matching the offer named in the Google ad and using the client's existing BNPL provider integration. No other buy box elements change.

## Slot 6: Homepage Product Visibility for Ad Traffic

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (lanxshoes.com/)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we add a product module within the first three homepage folds, ad traffic that scrolls only partway will convert better because it sees actual products instead of only lifestyle and review content.

**Data:** The first three homepage folds contain zero product photography — fold 1 is a lifestyle street scene, fold 2 is a men's/women's style split with category links (not products), fold 3 is a review carousel and shop-interior photo — Source: Site Screenshots (Homepage folds 1-3). Both Meta and Google ad traffic lands on this homepage — Source: Meta Ads and Google Ads visual summaries.

**V1:** Mobile and desktop — insert a "Shop Bestsellers" product module (4-6 SKUs) between the existing hero and the men's/women's style split. Existing CTAs and review carousel stay in place.

## Slot 7: Cart Drawer Checkout CTA Position

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (drawer)
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we make the checkout button sticky above the upsell block, cart-to-checkout drop-off will decrease because customers don't have to scroll past two upsell offers to complete checkout.

**Data:** The full-width "CHECKOUT" button sits at the very bottom of the cart drawer, below a "RECOMMENDED" upsell section (Shoe Care Bundle at 20% off, a sock cross-sell), and is not sticky — Source: Site Screenshots (Cart).

**V1:** Mobile and desktop — make the "CHECKOUT" button sticky at the bottom of the drawer viewport while keeping the upsell block scrollable above it. No other cart elements change.

## Slot 8: Collection Page Persistent Discount Banner

**Type:** A/B test (1 variation vs. control)
**Page:** Collection / Category page
**Revenue potential:** Not calculable. Monthly sessions and CVR baseline were not collected for this brand — see Missing Data in the audit.

**Hypothesis:** If we reduce the persistence of the floating "GET 10% OFF" banner, product-card CTA visibility will increase because the banner stops competing for attention at every scroll depth.

**Data:** A "GET 10% OFF" banner floats bottom-right and persists in the same screen position across all three folds captured on the 112-product Men's grid, regardless of scroll depth — Source: Site Screenshots (Collection page folds 1-3).

**V1:** Mobile and desktop — collapse the floating banner into a dismissible, minimized tab after the first scroll, keeping the offer one tap away. No other collection page elements change.

## Future Slot Candidates

1. **Loyalty/VIP messaging for repeat buyers** - First-party reviews show strong repeat-purchase behavior (customers citing 3-8 pairs owned), an under-leveraged loyalty angle not currently visible anywhere on-site.
2. **Google/Meta value proposition alignment** - Google and Meta promote entirely different value props (purchase-intent/heritage vs. brand-story/store-visit) with no unifying message reinforced on-site. Larger messaging initiative rather than a single test, worth scoping separately.

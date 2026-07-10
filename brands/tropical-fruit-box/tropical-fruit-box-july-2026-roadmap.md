# Tropical Fruit Box CRO Research Brief

**Data Sources:** Meta Ads (3 ads + landing pages), Google Ads (Shopping), Site Screenshots (homepage, collection, PDP, cart drawer), PageSpeed Lighthouse (homepage + Best Sellers, 2026-06-23), Customer Reviews (33 reviews, REVIEWS.io, Taste the Tropics Fruit Box), Live site fetch (2026-06-24), Competitor research (Miami Fruit, The Fruit Company, 2026-06-24)

---

## Insights

Two of three active Meta ads are built around specific $15-off discount codes. Ad 2 drives traffic to the Create Your Own PDP ($119) with "Save $15 with code META15" as its sole hook. Ad 3 drives traffic to Best Sellers with "Use SWEET15 to get $15 OFF." Neither code appears on the respective landing page. Both pages display an unrelated promo (PRIME20: 20% off $89+) in the announcement bar. Visitors who clicked specifically to redeem an offer arrive with no confirmation it works. Ad 3 has been active since January 19, 2026, meaning five-plus months of offer-motivated traffic has landed on a page that ignores the offer. Source: Meta Ads visual summary, live site fetch (2026-06-24).

Mobile performance on both primary pages is at fail level. Best Sellers, the main paid traffic destination, records LCP 8.6s and TTI 43.6s (PageSpeed mobile emulation, 2026-06-23). Google's "Poor" threshold for LCP is 4s. Best Sellers exceeds it by more than 2x. The homepage is worse: LCP 12.0s, TTI 51.6s. Server response time is fast at 10ms, which rules out hosting. The bottleneck is client-side JavaScript. Third-party scripts including a live chat widget, social proof popup, and loyalty program all block the main thread before the product grid is interactive. Source: PageSpeed Lighthouse (2026-06-23, mobile emulation).

Customer reviews on the flagship product (192 reviews, 4.78 stars) show gifting as the dominant use case. Multiple reviewers describe buying for recipients who reacted strongly. One reviewer specifically called out the fruit identification cards: "so we knew how to cut into the fruits and when they were ripe enough to eat." These cards make the exotic experience accessible for first-time buyers. The feature is physically in every box and absent from every ad, the homepage, and the PDP buy box. Source: Reviews (REVIEWS.io).

Miami Fruit, the primary competitor, prices from $147 versus Tropical Fruit Box's $109 entry point. That is a 26% price advantage with zero on-site expression. Combined with the message match gap, the mobile performance drag, and the invisible gifting differentiators, the site is losing a measurable share of the paid traffic it is already paying for before any test can engage a visitor.

---

## Slot 1: Discount Code Welcome Banner on Best Sellers

**Type:** A/B test (1 variation vs. control)
**Page:** Best Sellers (https://tropicalfruitbox.com/collections/best-sellers)
**Revenue potential:** Monthly session data unavailable. At a conservative 8% CR lift on the SWEET15 Meta segment x $109 AOV, every 1,000 sessions/mo in that segment delivers approximately $872 in incremental monthly revenue. GA session data is needed to complete the calculation.

**Hypothesis:** If we display a SWEET15 code confirmation in the announcement bar on the Best Sellers page, visitors arriving from Meta Ad 3 will convert at a higher rate because they can immediately confirm the offer that motivated their click is valid.

**Data:** Meta Ad 3 ran from January 19, 2026 onward and is built entirely around "Use SWEET15 to get $15 OFF" with a gifting call to action. The Best Sellers page announcement bar shows PRIME20 with no reference to SWEET15 anywhere on the page. Source: Meta Ads visual summary (Ad 3), live site fetch (2026-06-24).

**V1:** On mobile and desktop, replace the announcement bar text on the Best Sellers page with SWEET15 code confirmation copy (for example, "Your $15 off is ready. Use code SWEET15 at checkout"). On mobile, the bar remains pinned at the top and stays visible as the user scrolls. On desktop, the bar renders at full width above the navigation. The product grid, page title, sort dropdown, and all other page elements remain unchanged.

---

## Slot 2: Occasions-Based Editorial Row on Best Sellers

**Type:** A/B test (1 variation vs. control)
**Page:** Best Sellers (https://tropicalfruitbox.com/collections/best-sellers)
**Revenue potential:** Monthly session data unavailable. At a conservative 5% CR lift on Best Sellers traffic x $109 AOV, every 1,000 sessions/mo delivers approximately $545 in incremental monthly revenue. GA session data is needed to complete the calculation.

**Hypothesis:** If we add a "Great for Gifting" editorial section above the main product grid on the Best Sellers page, visitors with gifting intent will find relevant products faster and convert at a higher rate because the page reflects the reason they arrived.

**Data:** Meta Ad 3 drives traffic to Best Sellers with gifting-oriented copy. Multiple reviews on the flagship product describe gift-purchase scenarios with strong recipient reactions. The current Best Sellers page opens with a centered "Best Sellers" title, a sort dropdown defaulting to Featured, and a 3-column product grid of 14+ items with no editorial division and no gifting context anywhere on the page. Source: Meta Ads visual summary (Ad 3), Site Screenshots (collection page), Reviews (REVIEWS.io).

**V1:** On mobile and desktop, insert a "Great for Gifting" editorial section between the "Best Sellers" page title and the sort dropdown. This section surfaces 3 to 4 products from the existing grid under the gifting headline, each card displaying the product name, star rating, and price in the same format as the main grid cards. The full product grid renders below unchanged. On mobile, the editorial row scrolls horizontally. On desktop, it renders as a standard 3-column tile row.

---

## Slot 3: Discount Code Confirmation in Buy Box on Create Your Own PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Create Your Own Tropical Fruit Box PDP
**Revenue potential:** Monthly session data unavailable. At a conservative 10% CR lift on the META15 Meta segment x $119 AOV, every 1,000 sessions/mo in that segment delivers approximately $1,190 in incremental monthly revenue. GA session data is needed to complete the calculation.

**Hypothesis:** If we add META15 code confirmation directly in the buy box on the Create Your Own PDP, visitors arriving from Meta Ad 2 will convert at a higher rate because they can confirm the $15 discount that motivated their click without leaving the purchase area.

**Data:** Meta Ad 2's headline reads "Save $15 with code META15." That is the ad's only hook. The Create Your Own PDP buy box shows no META15 reference. The announcement bar on this page displays PRIME20. The PDP has only 1 review with no written text, meaning code confirmation is the only trust signal that can close the gap at a $119 price point before the visitor reaches the reviews section. Source: Meta Ads visual summary (Ad 2), Site Screenshots (PDP).

**V1:** On mobile and desktop, add a single-line code callout directly above the "Add to Cart" button in the buy box (for example, "Code META15 saves you $15 on this order"). The callout renders in the brand teal or a contrasting accent color to distinguish it from surrounding text. All other buy box elements remain unchanged: product title, price ($119), size variants (Regular 10lbs / Large 14lbs), greeting card dropdown, subscribe/save toggle, quantity stepper, Add to Cart button, and trust badge row (Satisfaction Guarantee, Free Shipping, Premium Quality, A+ Rating).

---

## Future Slot Candidates

1. **Performance Fix: Best Sellers Mobile LCP** - LCP of 8.6s and TTI of 43.6s on mobile (2026-06-23) represent a pre-conversion bounce risk on the highest-traffic paid landing page. Deferring third-party scripts (chat widget, social proof popup, loyalty program) targets the client-side JavaScript bottleneck; industry benchmarks point to 15 to 25% bounce rate reduction from LCP improvements in this range.

2. **Fruit ID Cards Callout in PDP Buy Box** - The physical fruit identification cards included in every box are absent from the buy box. One reviewer wrote: "so we knew how to cut into the fruits and when they were ripe enough to eat" (Source: Reviews, REVIEWS.io). Adding a one-line feature callout above the trust badge row directly addresses the top anxiety of first-time exotic fruit buyers.

3. **TropiRewards Loyalty Visibility** - The loyalty program is referenced only at the bottom of the cart drawer. Moving it upstream to product pages or the homepage targets email capture and repeat purchase conversion before the cart.

4. **Subscribe & Save Collection-Level Callout** - The 10% Subscribe & Save option surfaces on PDPs only. A callout at the collection level could acquire subscription customers earlier in the funnel and lift LTV.

5. **Competitive Price Frame on Homepage or PDP** - Miami Fruit prices from $147 versus Tropical Fruit Box's $109 entry point. This 26% price advantage is stated nowhere on the site and is a high-confidence trust signal for price-sensitive shoppers comparing options.

# SHEKO CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Competitor Research, Site Screenshots

---

## Insights

Every ad SHEKO runs leads with a number: "-8kg in 8 Wochen," "-4kg in 4 Wochen." That specificity is why people click. But when they land on the product page, they face a greyed-out CTA button that won't activate until they've completed 3 flavor selections, a review count of 282 when 24,643 reviews actually exist, and key information locked behind collapsed accordions. The ad does its job. The page walks it back.

The reviews tell a consistent story. People who succeed love SHEKO. They lose real weight with real numbers: -7kg in 5 weeks, -11kg in 2 months, -28kg over time. They praise the taste and the ease. But the 3-star reviews surface a credibility gap: the "5 Stunden satt" (5-hour satiety) claim doesn't hold for everyone mixed with milk alone. SHEKO's own customer service team knows this. Their reply to every satiety complaint is: add the Abnehmkur. That product exists in their catalog at €14.95. It is never mentioned in the cart.

The cart itself is nearly empty. One product, a savings callout, and a checkout button. No cross-sell, no upsell, nothing. For a brand where the average order is €89.92 and the most common customer complaint is solved by a €14.95 add-on, this is the most overlooked revenue lever in the funnel.

The homepage compound these issues. The hero asks: "Balance gewinnen oder Gewicht verlieren?" That's a question, not a promise. The ads that send people to this site already answered the question with a number. The transformation stories (Iris: -20kg in 5 months, Carina: -10kg in 10 weeks, Mathias: -25kg in 12 months) are buried in fold 3, where most visitors never scroll. The CTA says "Jetzt entdecken" (Discover now). Nobody buys because they feel like discovering.

Conservative revenue math: a 0.5% CR lift on the PDP at an estimated 25,000 monthly sessions and €89.92 AOV = €11,240/month. A 10% upsell take rate on the Abnehmkur in the cart at ~2,500 monthly cart views = €2,800/month in AOV lift. These estimates are directional without analytics access, but the direction is clear. The three biggest levers are in front of the customer right now, doing nothing.

---

## Slot 1: Unlock the CTA and Surface the Real Review Count

**Type:** A/B test (1 variation vs. control)
**Page:** 4 Wochen Starter-Set PDP (sheko.com/products/diaetshake-monatsbox)
**Revenue potential:** Est. 25,000 sessions/month x 0.5% CR lift x €89.92 AOV = est. €11,240/month. Note: without analytics access, session count is estimated based on brand scale indicators (20,470 Reviews.io reviews, active Meta + Google campaigns in Germany).

**Hypothesis:** If we pre-select the 3 most popular flavors by default and display the full 24,643 review count instead of 282, add-to-cart rate will increase because the inactive CTA creates hesitation at the moment of purchase and the 282 review count dramatically undersells social proof.

**Data:** The primary CTA button "Wähle Deine Wunschsorten" appears inactive in the PDP screenshot, with 3 unfilled flavor dropdowns above it. Reducing add-to-cart friction of this type has documented +47.61% CR lift in comparable Shopify tests (Blend Commerce, 2024). (Source: Site Screenshots, CRO Community Research.) The product card on the homepage shows 24,643 reviews for this exact product. The PDP shows 282. Every visitor who arrives from a paid ad sees the weaker number. SHEKO's announcement bar already establishes 4.8/5 credibility at the top of the page; the PDP buy box contradicts it with 282 reviews. (Source: Site Screenshots.)

**V1:** Pre-select the 3 most popular flavors in the "Im Paket enthalten" dropdowns by default, using sales data to determine which 3 flavors to set as defaults (e.g., Vanilla, Strawberry, Espresso or your current top 3 by unit volume). Each dropdown still shows the full flavor list so customers can change their selection with one click. The button activates on page load instead of requiring 3 completed selections first. Change the button label from "Wähle Deine Wunschsorten" to "In den Warenkorb" (or your preferred add-to-cart copy) once the defaults are set. Separately, replace the review count in the buy box from 282 to the full Reviews.io aggregate count (24,643 as of data collection). Keep the star rating and the "Mehr als 10.000 mal in den letzten 2 Monaten gekauft" badge unchanged as they are already strong.

On desktop: the buy box layout stays unchanged. The 3 flavor dropdowns still appear below the bullet list with their selected defaults visible. The CTA is active and clearly styled (not greyed out) on page load.

On mobile: the layout stacks vertically. The 3 flavor dropdowns with pre-selected defaults appear above the price and CTA. The CTA is full-width and active on load. No scroll required to see the active button on most modern mobile devices.

---

## Slot 2: Abnehmkur Cart Cross-Sell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (all pages on sheko.com)
**Revenue potential:** Est. 2,500 cart views/month x 10% upsell take rate x €11.21 (Abnehmkur at 25% off €14.95) = est. €2,803/month AOV lift. Session count estimated from PDP sessions x estimated add-to-cart rate. A documented Shopify cart cross-sell case study recorded 43% revenue lift (Blend Commerce, 2024).

**Hypothesis:** If we add a one-click Abnehmkur cross-sell at 25% off in the cart drawer, AOV will increase because the Abnehmkur directly addresses the satiety concern raised repeatedly in reviews, making it a genuinely useful add-on that customers in buying mode will recognize as relevant.

**Data:** Every satiety complaint in reviews (Oct 2025 to Mar 2026) receives the same SHEKO CS reply: add the Abnehmkur or glucomannan supplement. "Sie können die Abnehmkur oder unser Ballaststoffpulver nutzen, die Pulvermenge erhöhen oder Ballaststoffe wie Chiasamen, Leinsamen oder Haferflocken hinzufügen." The Abnehmkur Berry is listed in SHEKO's catalog at €14.95. It is not surfaced anywhere in the current cart drawer, which contains only the main product, a savings callout, and the checkout CTA. (Source: Reviews, Site Screenshots.) Pre-purchase upsells priced well below the main product and directly relevant to the purchase are the least risky AOV lever: they add revenue from buyers who have already committed, with no impact on conversion rate when executed as one-click additions (CRO Ebook: Chapter 10).

**V1:** Add a cross-sell widget in the cart drawer below the product item, in the currently empty space. Show one product: Abnehmkur Berry. Display with: product image, name, a one-line description ("Für 5 Stunden Sättigung" or "Das Geheimnis hinter längerer Sättigung"), original price (€14.95) crossed out, discounted price (€11.21, 25% off), and a one-click "Hinzufügen" (Add) button. No additional page navigation required; clicking "Hinzufugen" adds the Abnehmkur to the cart instantly without closing the drawer or redirecting.

On desktop: the cross-sell widget appears as a single-row card below the main product in the cart drawer, before the shipping and total summary. The card is compact (product thumbnail left, copy and price center, add button right). It sits above the "Du sparst" and "Gesamtsumme" lines.

On mobile: the widget stacks as a full-width card with the same elements (thumbnail, copy, discounted price, add button) in a single row. The "Jetzt sicher zur Kasse" CTA remains pinned to the bottom of the drawer and is always visible. The cross-sell card is scrollable as part of the cart content above it.

---

## Slot 3: Homepage Hero - Results-First Headline

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (sheko.com)
**Revenue potential:** Est. 20,000 homepage sessions/month x 0.3% CR lift x €89.92 AOV = est. €5,395/month. Homepage traffic estimated from brand scale indicators and branded search volume. Lift estimate is conservative relative to documented uplift from headline testing (ebook benchmark: headline/hero is the single highest-leverage test since 100% of visitors see it).

**Hypothesis:** If we replace the hedging question headline with a direct results statement and change the CTA from "Jetzt entdecken" to a purchase-intent CTA, homepage-to-PDP click-through rate and downstream conversion will increase because the current headline delays the decision while the ads already prove that transformation outcomes drive clicks.

**Data:** Ads 1 and 2 (running since Dec 28, 2025) and Ad 3 (running since Feb 19, 2026) all lead with specific outcome claims: "-8kg in 8 Wochen ohne Verzicht, JoJo-Effekt oder Medikamente" and "-4kg in 4 Wochen ohne Verzicht, JoJo-Effekt oder Medikamente." These creatives are still active, which signals they are performing. The homepage headline "Balance gewinnen oder Gewicht verlieren?" is a question that introduces ambiguity where the ad created certainty. (Source: Meta Ads, Site Screenshots.) The ebook principle: "Headlines are supposed to tell your customers the end result of using your product (the Dream Outcome). The subheadline describes the product (the Vessel)." The homepage subheadline currently tries to do both and does neither. (Source: CRO Ebook, Chapter 8.) The transformation proof that exists in fold 3 (Iris: -20kg/5 Monaten, Carina: -10kg/10 Wochen, Mathias: -25kg/12 Monaten) validates the outcome claim but is invisible until scroll.

**V1:** Replace the headline "Balance gewinnen oder Gewicht verlieren?" with: "Im Schnitt -8 kg in 8 Wochen. Ohne Hunger. Ohne JoJo-Effekt." (directly mirrors the proven Meta ad copy). Replace the subheadline "Mit SHEKO geht beides..." with a results-validation line that pulls from the transformation stories: "Iris verlor 20 kg in 5 Monaten. Carina verlor 10 kg in 10 Wochen. Mit dem 4 Wochen Starter-Set." Replace the CTA "Jetzt entdecken" with "Zum 4 Wochen Starter-Set" linking directly to sheko.com/products/diaetshake-monatsbox. Keep the orange hero background, product imagery, and announcement bar unchanged.

On desktop: the left copy block retains its current layout. The headline and subheadline swap as described above. The CTA button style (salmon pill) remains the same, only the label changes. The product imagery on the right remains unchanged.

On mobile: on smaller screens the hero stacks with copy above the product image. The new headline is set at the same font size as the current headline. The CTA button remains full-width below the copy, above the product image. The subheadline referencing Iris/Carina truncates to one name if space is tight: "Iris verlor 20 kg in 5 Monaten. Mit dem 4 Wochen Starter-Set."

---

## Future Slot Candidates

These ideas have strong data backing but didn't make the top 3 this month:

1. **PDP: Message match landing page for "-8 Wochen" ad traffic.** Ads 1 and 2 (active since Dec 28, 2025) promise 8-week results but land on a 4-week product. A dedicated landing page or an 8-week bundle (2x 4-week sets) positioned around the 8-week transformation would close this gap cleanly.

2. **PDP: Satiety proof section.** The "5 Stunden satt" claim in the bullet list is unsupported. Adding a short "How it works" visual above the accordion (not inside it) with the protein mechanism, the per-calorie comparison, and a testimonial referencing satiety would pre-empt the main objection from 3-star reviews.

3. **PDP: Per-meal price anchor alignment.** Google ads use "ca. 3,50€ pro Mahlzeit" (replacing 2 meals = 2 shakes). The PDP shows "1,24 € pro Shake." These are inconsistent frames. Testing a "2 Shakes ersetzen 2 Mahlzeiten: ca. 2,48 € pro Tag" framing in the buy box could reinforce the Google ad promise at the moment of decision.

4. **Post-purchase: Reorder flow for the stealth price reduction segment.** Long-term customers who noticed the 450g to 378g can reduction are at churn risk. A targeted email and post-purchase flow that acknowledges the change and offers a loyalty discount could retain this segment before they switch to a competitor.

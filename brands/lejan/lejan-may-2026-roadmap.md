# Lejan CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Page Speed / Core Web Vitals, Site Screenshots

---

## Insights

The biggest finding from this audit is structural. Every Meta ad runs to the same page: `/en-eu/collections/barefoot-sneakers-adult`. That page has a 17.2-second LCP on mobile as of May 4, 2026. Portent research across 100M+ pageviews shows conversion rate at 4 seconds is 0.67% vs. 3.05% at 1 second. At 17 seconds, most paid traffic on mobile bounces before the page renders. Every other optimization in this brief is downstream of this. Fixing the collection page LCP is the single highest-leverage action available, and it needs to happen as a technical priority alongside any A/B testing program.

Once visitors do land on the page, three signals from the data converge on the same friction. Lejan's review base is overwhelmingly positive: customers repeatedly cite the "style + barefoot" combination as the core differentiator. "They don't look like barefoot shoes at all but they include all the essential elements" (Jessica, GB, Apr 2026). "By far the most stylish, high quality Barefoot shoe on the market" (Matthew, GB, Apr 2026). None of this is visible on the collection page. No star ratings, no aggregate score, no review count anywhere in the product grid, despite a 5-star "Excellent" rating across 499 Trustpilot reviews (verified via Google's indexed Trustpilot snippet, May 2026). PowerReviews data across 20M+ product pages shows shoppers who engage with reviews convert at 111.8% the rate of those who don't.

The second converging signal is sizing. It is the #1 explicit friction in the reviews: the Melrose specifically runs large, US and UK buyers are confused by EU sizing, and there are no half sizes. Multiple buyers needed exchanges before finding the right fit. The free size exchange policy is Lejan's clearest competitive advantage. It appears in Meta ad copy and the announcement bar, but the product cards give no sizing guidance. Buyers absorb this uncertainty at the moment of decision rather than being reassured before it. Xero Shoes, another barefoot footwear brand, found that 27% of survey respondents cited size confusion as a key reason they did not buy.

The third pattern is message match. Ads promote specific silhouettes (Melrose SS26) in specific languages to specific markets. All three adults ads analyzed land on the same generic grid with "Barefoot for adults" as the headline. The Zorali test found that adding campaign-specific elements, including a hero image, headline, and social proof, to an existing collection page (not a separate landing page) produced +10% CR at 90% confidence and +17% revenue per visitor at 96% confidence. For Lejan, this does not require building new landing pages. It requires the collection page to reflect what the ad said.

Conservative math: if the collection page LCP is resolved and CR moves from an estimated 1% to 1.5% across 25,000 monthly paid sessions, that is 125 additional purchases at €125 AOV = €15,600/month in incremental revenue from one page. The three tests below target the UI problems that remain once the page loads.

---

## Slot 1: Collection Page - Social Proof Strip + Sizing Confidence

**Type:** A/B test (1 variation vs. control)
**Page:** Adults collection page (lejanbrand.com/en-eu/collections/barefoot-sneakers-adult)
**Revenue potential:** Estimated 25,000 sessions/month on this page x +0.4% CR lift x €125 AOV = €12,500/month. Taggstar's tests across fashion retailers showed +2.78% to +5.41% CR lift (Steve Madden footwear: +5.41%) from social proof signals on collection pages. This uses a conservative 0.4%.

**Hypothesis:** If we add an aggregate review bar above the product grid and a per-model sizing note on Melrose cards, click-through rate and add-to-cart will increase because visitors currently have no social proof and no sizing confidence before selecting a product.

**Data:** The collection page product cards show no review stars, no rating count, and no aggregate score despite a 5-star "Excellent" rating across 499 Trustpilot reviews (Source: Site Screenshots, Reviews, Trustpilot via Google snippet, May 2026). Sizing is the #1 friction point in the reviews from the last 30 days: Melrose runs large (Mathieu, GB; Sam, GB), US buyers struggle with EU sizing (Dani, US; Snaps, US), and multiple reviewers needed exchanges before finding the right fit (Source: Reviews). "Cambios de talla gratis" appears in Meta ad copy as a key differentiator but is reduced to a small announcement bar on the collection page itself (Source: Meta Ads, Site Screenshots). PowerReviews data across 20M+ product pages shows shoppers who engage with reviews convert at 111.8% the rate of those who don't, and products rated 4.75-4.99 stars show the highest conversion rates (Source: CRO Community Research). Xero Shoes found 27% of non-buyers cited size confusion as a key reason they did not buy (Source: CRO Community Research).

**V1:** Desktop: Directly above the "Barefoot for adults" headline and the One®/Melrose® filter tabs, insert a single-line trust bar containing three elements separated by vertical dividers: "★★★★★ Excellent · 499 opiniones" on the left, "Cambios de talla gratis" in the center, and "Envío gratis en pedidos +70€" on the right. The bar inherits the page's white background with no added color. Font size matches existing body text. On Melrose® product cards specifically, add a small gray tag below the product colorway label reading "Pide una talla menos" (size down one). One® cards receive no sizing tag, as no sizing issue has been reported for that model. All other card elements remain unchanged: image, name, colorway, price, size selector, ADD button.

Mobile: The trust bar collapses into a horizontally scrollable row of three pill chips: "★★★★★ Excellent · 499 opiniones" / "Cambios de talla gratis" / "Envío gratis +70€". Each chip is visible independently without overlap. The Melrose sizing tag appears below the colorway label on the card at 12px, one line, no truncation needed. Card image, name, price, and ADD button are unchanged.

---

## Slot 2: Collection Page - Campaign-Matched Hero Entry

**Type:** A/B test (1 variation vs. control)
**Page:** Adults collection page (lejanbrand.com/en-eu/collections/barefoot-sneakers-adult)
**Revenue potential:** Estimated 25,000 monthly paid sessions x +0.5% CR lift x €125 AOV = €15,625/month. Zorali added message-match elements to an existing collection page (no new LP required) and produced +10% CR at 90% confidence and +17% revenue per visitor at 96% confidence. Practitioner consensus puts LP-vs-collection-page advantage at 20-50% CR for campaign-specific traffic (Source: CRO Community Research).

**Hypothesis:** If we display a campaign-specific hero section above the product grid that mirrors the Melrose ad creative, and default the filter to Melrose, conversion rate from paid traffic will increase because visitors arriving from a Melrose-specific ad currently land on a generic headline and a mixed grid that does not confirm they are in the right place.

**Data:** All three Meta ads analyzed land on the same adults collection page. Ads 1 and 2 promote the Melrose® specifically, in Italian and Spanish respectively, yet the page headline reads "Barefoot for adults" in English and shows both One® and Melrose® products without prioritization (Source: Meta Ads, Site Screenshots). Google ads run in Spanish, French, and English with health and function messaging that also does not appear on the landing page (Source: Google Ads). The variation does not require a separate landing page. Zorali's test added campaign-aligned elements (hero image, press quotes, social proof) to an existing page and produced +10% CR at 90% confidence and +17% revenue per visitor at 96% confidence (Source: CRO Community Research). The CRO ebook states: "If customers buy based on a specific value proposition and your ads focus on a different message, it won't resonate and you'll lose sales."

**V1:** For visitors arriving via paid traffic (detected via fbclid or UTM parameters), the collection page renders with a full-width campaign section inserted above the existing headline and filter tabs. The section is two-column: left half shows the Melrose® hero image already used in ads (no new creative needed), right half shows the headline "Nueva Lejan Melrose® SS26" at 32px, a two-line subhead "La silueta que lo tiene todo. Barefoot Bonito." at 16px, and a pill CTA chip "Ver Melrose®" in Lejan's hot pink. Below this section, the existing One®/Melrose® filter tabs appear as normal, with Melrose® pre-selected. The product grid shows Melrose® colorways first. Visitors can switch to One® or all products at any time using the filter tabs. For visitors arriving via organic, direct, or non-paid channels, the page renders unchanged (control).

Mobile: The campaign section stacks vertically. The Melrose hero image is full width, 180px height max. Below it: headline at 24px, subhead at 14px, then the pink CTA chip. Filter tabs appear below, Melrose® pre-selected. Product grid begins immediately below.

---

## Slot 3: Homepage - Hero Headline and Primary CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (lejanbrand.com)
**Revenue potential:** Estimated 40,000 monthly homepage sessions x +0.3% CR lift (click-through to collection pages) x €125 AOV = €15,000/month. Homepage receives organic, direct, email, and brand search traffic. A modest improvement in funnel entry rate compounds across all downstream pages.

**Hypothesis:** If we add a clear headline and primary CTA button over the hero image, more organic and direct visitors will enter the product funnel because the current hero has no text, no value proposition, and no clickable action above the fold.

**Data:** The homepage hero is a full-width split lifestyle image (man in yellow Melrose, left; woman in brown and pink Melrose, right) with no headline, no CTA, and no copy visible anywhere above the fold (Source: Site Screenshots). The only text above the fold is the announcement bar ("CAMBIOS DE TALLA GRATIS") and the navigation. The brand proposition ("Calzado Barefoot Bonito" + barefoot explanation) appears in fold 2, below the collection promo strip. The CRO ebook: "Include large customer counts subtly in headlines if the Dream Outcome is still included. 'The shoe that has helped 10,000+ runners avoid injuries.'" The strongest customer verbatims from reviews function as conversion copy Lejan is not using: "They don't look like barefoot shoes at all but they include all the essential elements" (Jessica, GB). "The first shoes I can wear the whole day" (Natalia wide feet, ES). These are not on the page (Source: Reviews). Google ads lead with health and function messaging that outperforms purely aesthetic messaging in search intent, yet the homepage has no copy to reinforce either angle (Source: Google Ads).

**V1:** Desktop: Over the left half of the split hero image (the man with the yellow Melrose), add a text overlay containing: a headline "Barefoot Bonito." at ~48px in Lejan's existing serif or display font in white, a one-line subhead "El zapato que cuida tu pie sin renunciar al estilo." at ~18px below in white, and a pill-shaped CTA button "Ver SS26" in Lejan's hot pink at 44px height. Text and button are left-aligned, positioned at vertical center of the image. No background scrim or overlay added. The right half of the hero (woman in Melrose) is unchanged. The announcement bar and navigation remain unchanged.

Mobile: On mobile the hero renders as a single full-width image. A translucent dark-to-transparent gradient scrim covers the bottom 35% of the image. The headline appears at 28px, the subhead at 14px below it, and the pink pill CTA at 44px height below the subhead. All elements are left-aligned with 16px horizontal padding.

---

## Future Slot Candidates

**LCP performance fix (highest priority technical action):** The collection page LCP of 17.2s on mobile is the most urgent issue in this audit. Recommended as a technical sprint before or alongside the A/B tests: compress hero and product grid images to WebP with explicit width/height attributes, implement lazy loading for all below-fold product cards, defer third-party scripts. Portent data shows CR at 1s is 4.5x higher than at 4s. Vodafone saw +8% more sales from a 31% LCP improvement. This is not a standard A/B test and should be tracked as a before/after with a holdout period.

**Return vs. exchange clarification on PDP and cart:** J Mason's 1-star public review stems entirely from not knowing the free exchange portal exists. Jessica (5 stars) warns buyers in her review that returns are expensive. A PDP callout and cart drawer message explicitly distinguishing free exchanges from paid returns would address a known trust gap, especially for UK and US buyers. Test: add a "Cambios de talla: gratis | Devoluciones: gastos de envío a cargo del comprador" line below the add-to-cart button on PDPs.

**Cart drawer optimization:** The cart drawer has a visible blank gap between the product line and the "Buy it with..." cross-sell section. The "Haz match" concept (matching adult + kids shoe) is strong but undersold. Test: remove the gap, lead the cross-sell with a more specific hook ("Tu hijo también puede llevarlo" with the kids shoe as the hero item), and test the Sneaker Cleaner Kit as a secondary add-on below.

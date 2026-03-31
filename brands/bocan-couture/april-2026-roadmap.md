# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, GA4, Meta Ads, Google Ads, Reviews & UGC, Page Speed, Backlink Analysis, Email Campaigns, Winning Tests Library, Current Site Screenshots

---

## Insights

Bocan Couture converts at 0.16%. That means 98.83% of the 48,615 monthly sessions leave without adding a single item to cart. At £1,689 AOV, this is not a traffic problem. It is a trust problem.

The homepage is the clearest example. It receives 33% of all users (13,865 active users in the last 60 days) but holds their attention for just 8 seconds (Source: GA4). In those 8 seconds, a first-time visitor sees an Eid Sale banner, a product carousel, and a WhatsApp button. No reviews. No brand story. No mention of handmade craftsmanship, London design heritage, organic Aegean cotton, or free international shipping. Nothing that explains why a robe costs €1,865. Page speed compounds the problem: the homepage takes 5.9 seconds to render its main content on mobile (Source: PageSpeed), and 80% of traffic is mobile (Source: Shopify Analytics). By the time the page loads, many visitors have already left.

Yet Bocan's customers love the product. Trustpilot reviews (4.5 stars, 112 reviews) describe the quality as "unbelievable," "like no other shop I have tried," and "worth every penny." One customer wrote: "When you actually touch it, it feels even more classy, sophisticated, and feminine than it looks in the photos." Ilayda, the brand's personal shopping associate, is named in 20+ reviews for her patience, customization expertise, and personal service. The brand offers Made-To-Measure, bespoke alterations, private shopping appointments, and complimentary luxury gift wrapping. None of these appear on the website above the fold on any page.

The emails tell the story the site does not. Every email describes materials ("smooth combed cotton jersey," "100% organic cotton"), use cases ("slow mornings, maternity ease"), and services ("private personal shopping appointments, bespoke customisations"). But when a customer clicks through, they land on a bare product page or a 126-item collection grid with no context. The emotional bridge between marketing and purchase is broken.

This is the core opportunity: the trust signals, brand story, and social proof that already exist in Bocan's customer base and marketing materials need to be surfaced on the website. A homepage storytelling module generated +$130,251/month for a comparable luxury sleepwear brand in our case study library. Bocan's homepage gets 16,290 sessions per month. A conservative 0.5% ATC lift at £1,689 AOV would generate approximately £137,000 in additional monthly revenue (16,290 x 0.5% x £1,689). The data is there. The product is there. The website just needs to tell the story.

---

## Slot 1: Homepage Brand Story & Credibility

**Type:** A/B test (2 variations vs. control)
**Page:** Homepage (bocancouture.com). 16,290 sessions/mo (Source: Shopify Analytics).
**Revenue potential:** 16,290 sessions/mo x 0.5% ATC lift x £1,689 AOV = ~£137,500/mo

**Hypothesis:** If we replace the current product-first homepage layout with a brand-story-first approach that leads with craftsmanship, social proof, and USPs before showing products, add-to-cart rate will increase because the current homepage holds attention for only 8 seconds (Source: GA4), displays zero trust signals in 3 folds of content, and a comparable homepage storytelling test generated +$130,251/month for a luxury sleepwear brand (Source: Winning Tests Library).

**Data:** The homepage receives 33% of all active users but has the lowest engagement of any page at 8s (Source: GA4). The current first fold shows an Eid Sale banner and product carousel with no brand context. Trustpilot shows 4.5 stars from 112 reviews, with customers describing quality as "unbelievable" and "like no other shop" (Source: Reviews). The brand offers free international shipping, Made-To-Measure, handcrafted production, and boutiques in London and Istanbul, none of which appear on the homepage (Source: Site Screenshots, Email Campaigns). Backlink data shows zero press coverage vs. competitor Olivia von Halle's 35 Harper's Bazaar links and 23 Vogue links (Source: Backlinks). The brand wants to expand to the US, where brand awareness is near zero and the homepage must build trust independently (Source: Non-Data Context). A homepage storytelling module generated +$130,251/month for a luxury pajama brand by placing brand narrative before products (Source: Winning Tests Library).

**V1: Credibility Bar + Brand Story Module**
Replace the announcement bar with a USP bar showing 3-4 key differentiators inline: "Free International Shipping," "Handcrafted in London," "Made-To-Measure Available," "4.5 Stars on Trustpilot." Below the existing hero, inject a brand story module before the product carousel. The module contains: a headline ("Designed in London. Handcrafted for You."), 2-3 sentences about the brand's craftsmanship and materials (sourced from email copy and reviews), and one customer quote from Trustpilot. Keep it compact: one section, no more than 300px tall on mobile. The hero, product carousel, and category tabs remain unchanged. On desktop, the USP bar sits in the same announcement bar position as a single horizontal row. On mobile, the USP bar scrolls horizontally or stacks as a slim 2-line block.
**Brief:** Design: replace current announcement bar content with a USP bar (4 items, inline on desktop, horizontal scroll or 2-line stack on mobile). Create a brand story module (headline + short paragraph + customer quote) inserted between the hero and "Your Selection is Ready" product carousel. Maintain the brand's clean, minimal aesthetic. Use existing photography if a lifestyle image is needed. Dev: announcement bar content swap (Liquid edit). Brand story module is a new section injected via Shopify theme customizer or Liquid. Customer quote is hardcoded or pulled from a metafield. No third-party app needed.

**V2: V1 + Press & Customer Proof Section**
All V1 changes, plus add a social proof section below the brand story module. This section has two parts: (1) a "Trusted By" logo strip showing any publications, influencers, or platforms where Bocan has been featured (even Instagram features, Trustpilot badge, or the Doha trunk show partnership with M17/Apartment 7B count as credibility signals), and (2) 2-3 short customer testimonial cards pulled from Trustpilot, each showing the customer's first name, country flag, and a 1-2 sentence quote. On desktop, testimonials display as a horizontal row. On mobile, they display as a swipeable carousel. This addresses the zero-press-coverage gap by using the social proof the brand does have: real customer voices and partnership signals.
**Brief:** Design: "Trusted By" logo strip (horizontal, grayscale logos) + testimonial carousel (name, country, quote, Trustpilot star icon). Keep it compact on mobile, no more than one swipeable card visible at a time. Dev: logos are static images. Testimonials can be hardcoded initially or pulled from a reviews app integration. The section sits between the brand story module (V1) and the product carousel.

---

## Slot 2: PDP Trust Signals & Product Story

**Type:** A/B test (2 variations vs. control)
**Page:** PDP, starting with top products: Selene Cotton Bathrobe (€649.95), Solenne Cotton Robe Set (€1,180.95), Carina Silky Chiffon Robe Set (€1,865.95). Apply to all PDPs.
**Revenue potential:** Estimated ~8,000 PDP sessions/mo (based on product page views in GA4) x 1% ATC lift x £1,689 AOV = ~£135,100/mo

**Hypothesis:** If we surface trust signals, USPs, and the product story above the Add to Cart button on PDPs, add-to-cart rate will increase because the current PDP shows only photos, price, and size above the ATC with no reviews, no trust badges, no materials info, and no brand context (Source: Site Screenshots), while emails and reviews confirm that material quality and craftsmanship are the primary purchase drivers (Source: Reviews, Email Campaigns).

**Data:** The current PDP shows price and size options above the fold. The product description ("100% organic cotton," "delicate lace trim") sits below the ATC button and requires scrolling on mobile to reach (Source: Site Screenshots). No reviews or star ratings appear anywhere on the PDP. Made-To-Measure is a small button with no explanation of what it offers (Source: Site Screenshots). Reviews overwhelmingly cite material quality as the #1 reason for purchase: "when you actually touch it, it feels even more classy, sophisticated, and feminine than it looks in the photos" (Source: Reviews). Free international shipping is never mentioned on the PDP despite being a key selling point in every ad (Source: Meta Ads, Site Screenshots). A product description copy test using customer voice generated +$50,945/month by leading with specificity and quantified claims (Source: Winning Tests Library). An Instagram-style social proof element placed near the CTA generated +$6,635/month (Source: Winning Tests Library).

**V1: Trust Bar + Product Story Above ATC**
Add two elements above the existing ATC button: (1) A trust bar showing 3 key USPs as compact icons with labels: "Free International Shipping," "Handcrafted," "2-3 Week Made-To-Order." This sets expectations and highlights differentiators. (2) Extract the core product description (currently below the ATC) and place 2-3 sentences of it between the price and the size selector. Focus on materials and craftsmanship: "Crafted from 100% organic Aegean cotton with delicate lace trim. Handmade with attention to detail for a refined, understated finish." Keep the full description accordion below the ATC for additional details. On desktop, the trust bar sits between color swatches and ATC. On mobile, same position, icons stack or display inline depending on width.
**Brief:** Design: compact trust bar (3 icons + labels, single row on desktop, wrapping on mobile). Extract and restyle 2-3 sentences from the existing product description as visible body text between price and size selector. Match existing typography. Dev: trust bar is a reusable snippet across all PDPs. Product story text can pull from an existing metafield or the first paragraph of the product description. Insert above size selector in the Liquid template.

**V2: V1 + Customer Review Quote + Made-To-Measure Highlight**
All V1 changes, plus: (1) Add one customer review quote near the ATC area. Display as a small card with Trustpilot star icon, customer first name, and a 1-sentence quote. Rotate quotes per product if multiple are available, or use a general brand-level quote. (2) Expand the Made-To-Measure button into a small explainer: instead of just a button label, add a one-line description below it: "Can't find your size? Our team creates a custom fit, just for you. Message us on WhatsApp." This connects the Made-To-Measure feature directly to the WhatsApp concierge experience that reviews praise so highly. On desktop, the review card sits between the trust bar and the ATC button. On mobile, same position.
**Brief:** Design: small review card (Trustpilot icon + name + quote, no larger than 60px tall on mobile). Made-To-Measure button with a one-line explainer beneath it. Dev: review quote is hardcoded initially (select 3-5 strong quotes and rotate, or display the most relevant one per product category). Made-To-Measure explainer is a text addition to the existing button element.

**Sequencing note:** This test runs on PDPs. Slot 1 runs on the homepage. No page overlap, both can run simultaneously.

---

## Slot 3: Collection Page Hero + Social Proof

**Type:** A/B test (2 variations vs. control)
**Page:** /collections/maternity-edit (3,555 sessions/mo, +48% growth, 20s engagement) (Source: Shopify Analytics, GA4). This is the highest-traffic collection page with strong engagement and a clear purchase intent (hospital reception wear).
**Revenue potential:** 3,555 sessions/mo x 1.5% ATC lift x £1,689 AOV = ~£90,000/mo

**Hypothesis:** If we add a lifestyle hero banner, brand context, and customer testimonials to the Maternity Edit collection page, add-to-cart rate will increase because the current page shows 126 products with no hero, no social proof, and no storytelling (Source: Site Screenshots), while maternity/hospital reception is Bocan's strongest use case with multiple glowing reviews specifically about this category (Source: Reviews), and a similar collection page test with hero + reviews + urgency generated +$114,870/month (Source: Winning Tests Library).

**Data:** The Maternity Edit receives 3,555 sessions/month (+48% growth) with 20s average engagement (Source: Shopify Analytics, GA4). The current page shows "The Maternity Edit / LUXURY HOSPITAL RECEPTION WEAR / Soft Elegance for Your First Moments After Birth" followed by 126 products (Source: Site Screenshots). Multiple Trustpilot reviews specifically praise Bocan for maternity wear: "Bocan is the ultimate luxury wear for my hospital delivery day and I couldn't be more happy! Their quality is unmatched and worth every penny!" (Hatoon, SA, Oct 2024). "I'm genuinely amazed by the quality. I wasn't expecting it to be this soft and comfortable especially important during maternity" (G AlMansoori, AE, Sep 2025). "The best choice for hospital baby reception as it is the most sophisticated luxury wear. Ordered twice and for sure I will order again" (Nour, AE, Mar 2024). The maternity ad drives traffic with "soft fabrics, relaxed silhouettes, and delicate details" messaging but the collection page has no emotional context beyond a subtitle (Source: Meta Ads, Site Screenshots). A collection page hero + reviews + urgency test generated +$114,870/month (Source: Winning Tests Library). A collection ATF optimization with lifestyle imagery and benefit-driven copy generated +$13,730/month (Source: Winning Tests Library).

**V1: Lifestyle Hero + Maternity Review Quotes**
Replace the current text-only header with a compact lifestyle hero banner: one horizontal image (maternity lifestyle photography if available, or the strongest product shot) with an overlay headline ("Luxury Hospital Reception Wear") and subline ("Handcrafted for your most meaningful moments. Free international shipping."). Below the hero and above the product grid, add a slim testimonial strip showing 2 customer quotes from Trustpilot, specifically about maternity purchases. Display as: Trustpilot star icon, customer first name, country, and quote. On desktop, two quotes sit side by side. On mobile, they stack vertically or display as a swipeable pair. The 126-product grid remains, but the hero and testimonials give visitors context and confidence before they browse.
**Brief:** Design: compact hero banner (full-width, max 250px tall on mobile so first product row remains visible after one scroll). Testimonial strip below hero. Dev: hero is a new section in the collection template, editable via Shopify customizer. Testimonials are hardcoded text. Apply only to the Maternity Edit collection initially.

**V2: V1 + Curated "Staff Picks" Row + Product Count Reduction**
All V1 changes, plus: (1) Add a "Most Loved for Hospital Reception" curated row of 4 best-selling maternity products between the testimonials and the main grid. Each card shows a product image, name, price, and a "Best Seller" or "Customer Favourite" badge. This gives decision-fatigued visitors a shortcut. (2) Default the page to show only the first 24 products with a "Show More" button, rather than displaying all 126 at once. This reduces scroll fatigue and focuses attention on the most relevant products. On desktop, the curated row displays as a 4-across grid. On mobile, it's a scrollable carousel.
**Brief:** Design: curated product row with badges, styled distinctly from the main grid (slightly larger cards or different background). "Show More" button below the initial 24-product grid. Dev: curated row uses manually selected product IDs (editable via metafield). Pagination change to limit initial product display. Both are Liquid template changes.

**Sequencing note:** This test targets the Maternity Edit collection page. Slot 1 targets the homepage. Slot 2 targets PDPs. All three tests run on different pages with no overlap.

---

## Future Slot Candidates

These test ideas emerged from the data but didn't make the cut for April. Queued for future months:

1. **Cart Drawer Trust Signals:** Add free shipping confirmation, delivery timeline (2-3 week production), and a craftsmanship reminder to the cart drawer. Replace lower-priced upsells with complementary products (matching slippers, towel sets mentioned in reviews and ads).

2. **Announcement Bar Optimization:** Test replacing "Apple Pay is Available" with rotating USPs: "Free International Shipping," "Handcrafted in London," "Made-To-Measure Available." This is the first element visitors see on every page.

3. **PDP Gallery: Customer Photos/UGC:** Add an Instagram-style customer photo carousel to the PDP gallery. Reviews mention the product looks even better in person. Real customer photos would bridge the gap between studio shots and reality.

4. **Ramadan/Eid Collection Page Optimization:** The Ramadan Edit gets 6,509 sessions/month but only 9s engagement. Similar to the Maternity Edit test but with seasonal urgency elements and curated gifting context.

5. **Bridal Edit Landing Page:** The Bridal Edit gets 2,094 sessions/month (+66% growth). A dedicated bridal experience with customer wedding stories, customization options, and gift registry-style features could convert this growing segment.

6. **Page Speed Optimization:** At 45/100 performance and 5.9s LCP, there is significant room for improvement. This is not an A/B test but a dev project that should run in parallel with testing. Image optimization, script reduction, and lazy loading could meaningfully improve load times.

7. **Popup Optimization:** The 10% off popup and cookie consent banner both fire on page load, creating two overlays before the visitor has seen any content. Test timing, sequencing, or combining these to reduce friction on first visit.

8. **Email-to-PDP Message Match:** Create product-specific landing page templates that carry the email's storytelling context (materials, use cases, customer quotes) directly onto the page the visitor lands on after clicking. Bridge the current disconnect between email copy and bare PDPs.

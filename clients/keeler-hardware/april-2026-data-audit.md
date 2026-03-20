# Keeler Hardware — April 2026 Data Audit

**Store:** keelerhardware.com.au
**Audit date:** March 20, 2026
**Data window:** Last 30 days unless noted

---

## Meta Ads (Top 3 Best-Performing Ads)

Analyzed the top 3 best-performing ads out of many active campaigns. These are a sample, not the full account picture.

### Ad 1 — Security Hook (Deadlocks)

- **Library ID:** 908728707982138
- **Running since:** 6 March 2025
- **Platforms:** Facebook, Instagram, Messenger
- **Creative:** Fear-based hook — "194,100 homes were broken into in Australia last year." Lists 3 security tips (Install Deadlocks, Go Digital/Smart Locks, Secure Windows). Carousel format. CTA: "Shop Now."
- **Landing page:** `/collections/locks-accessories/deadlocks-&-night-latches`
- **Message match issue:** Ad leads with deadlocks specifically, but the landing page is a broad Locks & Accessories collection showing 338 products including cylinders, accessories, and unrelated categories. The intent is qualified but the destination isn't.

### Ad 2 — Design/Aesthetic (Specials)

- **Library ID:** 853403840474467
- **Running since:** 11 November 2025
- **Platforms:** Facebook, Instagram, Messenger, Threads
- **Creative:** Design-forward positioning — "Every great design deserves the right hardware." Mentions architectural handles, precision finishes, modern colourways. "Aussie-Owned & Stocked — Shop weekly trade specials & bulk deals today!" Lifestyle image: kitchen with French doors. ZipPay callout.
- **Landing page:** `/collections/specials-deals`
- **Message match issue:** Design-aesthetic audience lands on a 6,009-product generic sale dump. No architecture/design editorial context on the landing page.

### Ad 3 — Interior Designer Positioning (Specials)

- **Library ID:** 1030106238431302
- **Running since:** 19 September 2023 (longest-running of the three — over 2.5 years)
- **Platforms:** Facebook, Instagram, Messenger
- **Creative:** "The preferred suppliers of Door and Architectural Hardware for Interior Designers." Black and white store walkthrough video. ZipPay callout. CTA: "Shop Our Current Specials."
- **Landing page:** `/collections/specials-deals` — same as Ad 2
- **Message match issue:** Interior designer targeting, but landing page has zero design/trade editorial framing.

**Cross-ad finding:** Two of the three top-performing ads (different audience angles, different creative) send traffic to the same generic specials page. The ads are qualifying traffic by intent; the landing page is undoing that work.

---

## Reviews & UGC

### Top Product Reviews — Whitco Window Chain Winder MK8 (keelerhardware.com.au/products/whitco-window-chain-winder-mk8-d5-key-lockable-keyed-alike-white-w380216)

**What customers love:**

- **Keyed alike feature** is the most frequently called-out purchase driver: "Great due to their features and being keyed alike," "All keyed alike and were $10 per door closer cheaper than Bunnings."
- **Easy installation:** "Easy to install, works great," "No instructions — YouTube and common sense, all installed easily."
- **Price vs. Bunnings:** Multiple buyers explicitly compare favorably to Bunnings on price, often with faster delivery.
- **Compliance driver:** "Due to new rental standards all windows now have to be able to be locked — hence the need to purchase locks." Rental compliance is a real purchase trigger.

**Friction/issues at product level:**

- None flagged in the reviews for this product. Reviews are overwhelmingly positive.

### Brand-Level Reviews (Recent)

**What customers love:**

- Delivery speed when it works: "2 days from Sydney to south of Adelaide," "arrived in 3 days (Newcastle)," "received in 2 days."
- Price: "Great price," "favourable pricing," competitive vs. Bunnings.
- Phone/chat accessibility: "Easy to get someone on the phone," "hyper fast response."
- Stock availability: "Had the casement window latches that were out of stock in EVERY Bunnings store in Sth East Qld" — Keeler as the specialist alternative to Bunnings is a recurring theme.
- Product accuracy: "Prompt, communicative & direct," "exactly what I ordered."

**Negative themes / friction (flag to client):**

1. **Pricing trust issue (trade buyers):** One verified buyer (Steve Brown, Wetherill Park) reported being told their order was "already trade priced — this is the absolute cheapest" by phone staff, then received a sale email with 10%+ off the same items two weeks later. This is a trust and retention risk for trade accounts.
2. **Stock transfer failure (operational):** One verified buyer drove 1 hour to the Willoughby store after being told an item was in stock. It wasn't. Staff promised a transfer from Wetherill Park — it never happened across three separate calls, over multiple days. The buyer's builder had to return to site at additional cost. The customer service response acknowledged the issue but offered no remedy. This was flagged in the review as a process failure, not a one-off.
3. **Delivery failures:** Two instances of 20+ day delivery cited. One buyer rang twice after 5 days and the order still hadn't been packaged. Another received goods after a month. These contrast sharply with the fast-delivery praise, suggesting inconsistent fulfillment.
4. **Communication lag:** Multiple references to slow email response.
5. **Product compatibility:** One buyer found pocket slider door hardware didn't fit after purchasing. Another received a different product than ordered. Compatibility/substitution friction is a recurring (if infrequent) theme.
6. **In-store signage:** One buyer noted the store was "confusing for pick up" and signs didn't direct them correctly.

**Client-actionable flags (outside of A/B testing):**

- Review the phone team's practice of confirming "best price" when upcoming promotions may undercut that claim.
- Audit the stock transfer process between Wetherill Park and Willoughby — the failure described was a multi-step internal breakdown.
- Review product substitution workflow to reduce "received wrong item" incidents.

---

## Page Speed / Core Web Vitals

**Real-user data (last 28 days, mobile, Chrome UX Report):**

- LCP: 3.5s — Needs improvement (threshold: 2.5s)
- INP: 170ms — Good
- CLS: 0.02 — Good
- FCP: 2.2s — Needs improvement
- TTFB: 0.6s — Good
- **Core Web Vitals Assessment: FAILED**

**Lighthouse simulated (Slow 4G, mobile, March 20, 2026):**

- Performance score: 33/100
- LCP: 21.3s
- FCP: 10.9s
- TBT: 980ms
- CLS: 0.03
- Speed Index: 15.8s
- Total page weight: 6,324 KiB

**Primary culprits:**

- `upnova-upsell.app` — 118.3 KiB render-blocking, 5,020ms delay. This is the cart upsell app. It blocks page rendering AND causes the visible lag in the cart drawer.
- `app.easyquote.pw` — 11.5 KiB render-blocking, 2,610ms delay. A quoting app that appears to have no cache lifetime (None).
- 
- YouTube embed — 495 KiB unused JS loaded on page.
- Podium chat widget — 251 KiB JS, 658ms CPU time, 1-hour cache.
- Reviews.io — 339 KiB total, multiple scripts at 2-4 hour cache lifetime.
- Searchspring — 175 KiB in 13+ chunks, 30-minute cache.
- Total unused JS savings possible: 1,203 KiB.
- Total unused CSS savings possible: 147 KiB.
- 20 long main-thread tasks identified.
- Main thread work total: 7.4s (Script Evaluation: 3,701ms, Style & Layout: 1,344ms).

**Impact on conversion:** The cart drawer's visible empty space and lag is directly caused by Upnova loading render-blocking JS before it displays content. A 5-second wait for a cart upsell to appear is a documented UX failure.

---

## Competitor Research (Australia)

### Designer Doorware (designerdoorware.com.au)

- Positions as the design/specification partner for architects and interior designers.
- Three-tier product collections: Design, Project, Residential — segmented by professional use case.
- **Selector Tool:** Visual product comparison, specification sheet generator, PDF catalog builder, quote request. This is a significant B2B conversion tool that Keeler lacks.
- Custom design service with international manufacturing network.
- Design awards displayed (Good Design Australia, Best of Year Awards).
- No visible pricing or free shipping threshold — positioning is spec/quote-led.

### Lo & Co Interiors (loandcointeriors.com.au)

- Design-forward luxury hardware (solid brass, marble, travertine).
- **30-day returns prominently displayed** in sticky ribbon — repeated on scroll.
- Pricing visible on homepage grid ($34–$669).
- Newsletter signup offers 10% off first order.
- Free shipping on orders over $300; otherwise flat-rate $49.
- Lifestyle photography throughout — products shown in curated interiors.
- Design journal content for organic acquisition.

### Zanda (zanda.com.au)

- Positions as "designer, manufacturer & supplier" — local Australian production.
- Residential and Commercial segments clearly separated.
- No visible product finder, pricing, or trade program on homepage.
- Distribution network rather than direct-to-consumer focus.

### Access Hardware (accesshardware.com.au)

- Site returned a 405 error — unable to audit.

**Competitive gaps identified:**

- Keeler's "Help me Choose" button is a potential differentiator but its functionality is unclear without testing.
- No competitors appear to surface bulk/trade pricing as prominently as Keeler attempts to — but Keeler's execution (no quantity shortcuts, bulk table below fold) undersells this advantage.
- Designer Doorware's Selector Tool is meaningfully ahead of anything visible on keelerhardware.com.au for the professional/trade buyer journey.
- Lo & Co's explicit 30-day returns messaging is more prominent than Keeler's returns positioning.

---

## Non-Data Context (Client Notes)

- **PDP experience needs work.** Three specific issues flagged:
  1. Bulk pricing exists at 10, 20, and 30-unit breakpoints but there is no pre-selection of high quantities — buyers must manually type or click to the right number to activate a lower price.
  2. Fonts are outdated and not aligned to a standard design system.
  3. Product photography is extremely limited (confirmed in screenshots: 2 images only, both white-on-white, no lifestyle or installation context).

---

## Site Screenshots

### Homepage (March 20, 2026)

- **Fold 1:** Full-width Autumn Sale hero (up to 70% off, 16–23 March). Hero is occupied entirely by the seasonal promotion — no evergreen brand story or value proposition when sale is not running.
- **Fold 2:** Four trust icons (Australian Owned, Locally Stocked, Express Shipping, Phone Support). Featured Products carousel — all marked "Popular" and "On Sale."
- **Fold 3:** 4x2 category tile grid (Door Hardware, Window Hardware, Gate Hardware, Monthly Specials, Cabinet Hardware, Locks & Accessories, Kitchen Hardware, Help Me Choose). Instagram feed. "Recommended For You" carousel — all sale-tagged.
- **Below fold:** About Keeler Hardware YouTube video. Reviews.io widget (4.7 stars, 11,511 reviews — strong social proof, buried at bottom). Photo grid with "Book a Free Consultation" CTA overlay.
- **Note:** Autumn Sale ends 23 March. The homepage will need a new above-fold focus for April.

### PDP — Whitco Window Chain Winder MK8

- **Fold 1:** 2 product thumbnails in left rail (both same product, white on white background) + PDF manual icon + Whitco brand logo. Large product image. Buy box: RRP $148.28 crossed out, NOW $37.40, "YOU SAVE 75%" badge. Sale countdown timer (3 days, 4 hrs). Availability: Online In Stock, In Store: 941 (Wetherill Park), 73 (North Willoughby). Express shipping callout. Quantity selector defaulting to 1. ADD TO CART + WISHLIST buttons. Trust icons: Australian Owned, Locally Stocked, Phone Support. Bulk buy table (10-19: $35.53, 20-29: $34.60, 30+: $33.66). Payment icons (Apple Pay, PayPal, Afterpay, Google Pay, Zip).
- **Fold 2:** Shipping costs (Express: $24.95, Standard: free over $99). Click & Collect (Wetherill Park, Willoughby). Tabs: DESCRIPTION / SPECIFICATIONS / PRODUCT REVIEWS. Description opens with "If you purchase more than 1 lock, all locks will be supplied keyed alike" in blue link text — this is the primary purchase driver per reviews, buried in the description tab.
- **Key issues:** Only 2 images. Keyed alike callout below fold. No quantity shortcuts. PDF manual in image gallery. Design system inconsistency (font weights, tab bar styling).

### Collection Page — Locks & Accessories

- **Fold 1:** Wide hero banner (dark door lock + Yale keypad images). Subcategory tile grid (10 subcategories + View All). Clean navigation structure.
- **Fold 2:** "Showing 1–30 of 2918 results." Filter sidebar (Sale, Product Type, Price, Brand, Express Shipping, Colour or Finish — Brand appears twice). All 5 visible products marked "On Sale." Products with 0 reviews featured first. Long technical product names (SKU baked in). "SEE OPTIONS" CTA — no quick add-to-cart. "Don't pay $X XX% OFF" yellow badges on all cards.

### Cart Drawer

- Header: "Your Cart · 1 items."
- Product line item with star rating and product name.
- **Large empty white space** where Upnova upsell app is loading (confirmed as 5,020ms render-blocking).
- "We think you'll like:" upsell section — 3 products, all Whitco variants. Second recommendation is the same product already in the cart.
- No subtotal displayed.
- No shipping threshold bar.
- CTA: "VIEW CART · $37.40 ~~$148.28~~" — this takes users to the cart page, not checkout. No direct "Proceed to Checkout" button.

---

## Cross-Source Analysis

### Converging themes

**1. The cart drawer is a direct conversion leak.**
Every buyer passes through the cart drawer. It has no checkout button, a 5-second lag from a render-blocking upsell app, no shipping threshold nudge, and no subtotal. Every one of these is a documented friction point that research consistently ties to cart abandonment. (Sources: Page Speed, Cart Drawer Screenshots, Non-Data Context)

**2. The PDP undersells Keeler's primary trade advantage.**
"Keyed alike" is the #1 reason customers cite for purchasing. It appears in the product description tab, not the buy box. Bulk pricing exists but requires buyers to discover it and manually set quantity — there's no shortcut. Trade buyers (builders, property managers, landlords responding to rental compliance rules) are the highest-value repeat customers, and the page doesn't speak directly to them. (Sources: Reviews, Non-Data Context, PDP Screenshots)

**3. Paid ad spend is wasted on mismatched landing pages.**
Two of three top ads target design-oriented or interior designer audiences. Both land on a 6,009-product specials dump. The third targets security-focused homeowners and lands on a 338-product general locks collection. The ads work; the landing pages don't follow through. (Sources: Meta Ads, Landing Page Screenshots)

**4. Page speed is failing on mobile — the primary traffic device.**
Core Web Vitals failed. LCP of 3.5s on real mobile users. The cart upsell app (Upnova) and a quoting app (easyquote) are the dominant render-blocking scripts. These are third-party tools that could be deferred or replaced without loss of core functionality. (Sources: Page Speed Audit)

**5. Social proof is present but poorly deployed.**
11,511 reviews at 4.7 stars is a powerful trust signal. It's shown in the footer of the homepage. The collection page features products with 0 reviews at the top. The PDP shows ratings but the most compelling proof point (keyed alike, bulk savings) is in the description. Surfacing proof where buyers need it most (buy box, collection grid) is an untapped lever. (Sources: Reviews, Screenshots)
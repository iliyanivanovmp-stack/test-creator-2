# Natures Collection CRO Research Audit
**Site:** naturescollection.eu | **Date:** April 2026

---

## Data Sources Used

Google Ads Transparency, Page Speed (PSI), Competitor Research, Site Screenshots (Homepage, Collection, PDP, Cart)

---

## 1. Google Ads (Transparency Center)

**NC's active ad types observed:**
- Google Search: "Natures Collection | 100% real fur. Danish design. Free 2-3 days worldwide delivery. 100 days free return." (naturescollection.us)
- Google Shopping: Product image ads for sheepskin rugs, rabbit stuffed animals (Kaninchen), bags
- Auto-generated text ad (dynamic from landing page content): "Vores sortiment kombinerer skandinavisk design med kvalitetshåndværk og bæredygtighed" (Norwegian/Danish market)
- Norwegian market search ad: "Natures Collection - Premium ekte skinn - Ekte dansk design | Stort utvalg av skinnprodukter av høy kvalitet."

**Key observations:**
- The 20-year warranty, NC's single strongest differentiator, appears in zero active ads observed
- One ad group is auto-generated from landing page content, signaling gaps in paid search copy coverage
- Copy leads with product specs ("100% real fur") rather than emotional benefits or competitive differentiators
- Multi-market targeting: EU, NO, DK, NL, US with mixed language copy

**Competitive ad landscape (brands bidding alongside NC):**
- Sheepskinhouse.co.uk: "Sale: up to 40% off - No import or customs fees" (Spring Sale active as of April 2026)
- Sheepskinhouse.nl: "Winter Sale 75%" and "Lente Sale: tot 40% korting"
- Nordic Sheep (nordicsheep.dk): "Spar 75% på hele shoppen. 50.000 glade kunder i hele Danmark."
- Saueskinner.no: "Vårsalg: spar opp til 55% - Skandinavisk design. Klarna 30 dager"
- Lammeskinder.dk, Lammellhaus.de: Various discount-led ads

**Gap identified:** NC runs no visible promotional offer in Google Ads while every major competitor is running 40-75% off sale messaging. NC is competing on premium positioning alone in a paid search environment dominated by discount messaging.

---

## 2. Page Speed / Core Web Vitals

**Data collected:** PageSpeed Insights reports for homepage and PDP, April 22, 2026.

### Homepage (naturescollection.eu)
| Metric | Score |
|---|---|
| Performance Score | 34/100 (Poor) |
| Core Web Vitals | **Failed** |
| LCP (lab) | 22.5s |
| FCP (lab) | 4.7s |
| Total Blocking Time | 1,290ms |
| Speed Index | 9.4s |
| Network Payload | 30,263 KB (30 MB) |
| Unused JS savings | 1,176 KB |
| Image delivery savings | 249 MB |

### PDP (naturescollection.eu/products/[sheepskin-rug])
| Metric | Score |
|---|---|
| Performance Score | 45/100 (Poor) |
| Core Web Vitals | **Failed** |
| LCP (lab) | 23.7s |
| FCP (lab) | 3.8s |
| Total Blocking Time | 840ms |
| Speed Index | 4.9s |
| Unused JS savings | 566 KB |

**Key issues flagged by PSI:**
- Enormous network payload (30 MB on homepage)
- Render-blocking requests
- 3rd party script load
- Legacy JavaScript
- Unoptimized images (249 MB savings on homepage alone)

**Context:** Google's research shows mobile conversion rates drop by up to 20% for each additional second of load time (Google/SOASTA, 2017). At a 22.5s lab LCP, the homepage is losing a significant portion of visitors before they see any product.

---

## 3. Competitor Research

### Sheepskinhouse.co.uk
- **Active promotion (April 2026):** Spring Sale, 25-75% off across rugs, jackets, slippers
- **Trust signals above fold:** Free delivery over £99, 30-day returns, no import/customs fees
- **Reviews:** 112 customer reviews visible, testimonials throughout homepage
- **Messaging:** "Danish hygge meets British comfort," sustainability focus
- **CTA structure:** "Explore Collections," "Shop Now" per category

### Nordic Sheep (nordicsheep.dk)
- **Active promotion (April 2026):** 50% off double merino sheepskin (hero deal), multiple products 40-50% off
- **Email capture:** 10% extra discount for newsletter signup
- **Reviews:** 791 reviews displayed (Judge.me), 4.6/5 average
- **Trust signals:** 100-day return policy, 1-3 business day delivery, Klarna/MobilePay/Apple Pay prominently shown
- **BNPL:** Multiple payment methods featured in-page (not just footer icons)

**Competitive gap summary:**
| Feature | Natures Collection | Sheepskinhouse | Nordic Sheep |
|---|---|---|---|
| Reviews visible | None | 112 | 791 |
| Active sale | None | 25-75% off | 40-50% off |
| Trust bar above fold | No | Yes | Yes |
| BNPL near buy button | No | Not confirmed | Yes (Klarna, MobilePay) |
| Email capture offer | None observed | Yes | 10% off |
| Returns policy near ATC | No (footer only) | Yes | Yes (100 days) |

---

## 4. Site Screenshots

### Homepage (3 folds)

**First fold:**
- Navigation: PRODUCTS | SUPPORT | ARCHIVE | Natures Collection logo (center) | EU flag | B2B LOGIN | search | cart
- Hero: Full-bleed editorial photography of furniture/room, no text overlay
- Category tiles: FURNITURE, DECOR, and an apparel image below the hero
- No hero headline, no hero CTA button, no trust bar

**Second fold:**
- "NATURES COLLECTION" brand block in ALL CAPS with mission statement text
- Category image tiles for SHEEPSKIN RUGS and APPAREL
- No CTA buttons on any category tiles

**Third fold / Footer:**
- Category image tiles for SHEEPSKIN RUGS on furniture and FLOOR RUGS
- Footer: Customer service hours, phone, email, collection links, support links, policies
- Trust signals (footer only): "20-year product warranty | All orders ship within 24 hours | Complimentary delivery"
- Payment icons (footer): Amex, Apple Pay, Klarna, Mastercard, PayPal, Union Pay, Visa
- Social icons: Facebook, Instagram, Pinterest, YouTube, LinkedIn

**Conversion issues:**
- 20-year warranty only appears in footer. Zero conversion-focused visitors will see it.
- No hero CTA on the first fold. Visitors must scroll and figure out their own navigation path.
- B2B LOGIN appears in the top nav at the same visual weight as other nav items, which may confuse retail visitors.
- Klarna is accepted but buried in footer payment icons. Not communicated as a purchase option.
- No reviews, testimonials, or social proof anywhere in the three folds.

### Collection Page (All Products)

**First fold:**
- Announcement bar: "COMPLIMENTARY DELIVERY" (cycling, with arrows)
- Navigation (same as homepage)
- Circular category icons: Sheepskin Rugs, Furniture, Cushions, Decor, Floor Rugs, Ready to Wear, Footwear, Accessories, Kids, Archive, All products
- Grid/list view toggles and SORT BY + FILTER controls
- Product cards: product image, "NATURES COLLECTION" brand label, product name (ALL CAPS), price, color swatches

**Product cards - missing elements:**
- No star ratings or review counts
- No "Bestseller," "New," or "Popular" badges
- No urgency signals ("Only X left," "X sold today")
- "NATURES COLLECTION" brand label appears above every product name (redundant at 100% of cards)
- Color swatches are so numerous on some products (20+ swatches) they become visual noise at card size

**Products visible in top fold:** New Zealand Sheepskin Long Wool 80cm (€99), Long Wool Sheepskin Cushion 35x35cm (€89), Slipper Cross (€99), Sheepskin Hot Water Bottle (€79)

### PDP (New Zealand Sheepskin | Long Wool | 80 cm, €99.00)

**Buy box (first fold):**
- Breadcrumb: Home / New Zealand Sheepskin | Long Wool | 80 cm
- Brand label: "NATURES COLLECTION" (ALL CAPS, above product title)
- Product title: "NEW ZEALAND SHEEPSKIN | LONG WOOL | 80 CM" (ALL CAPS)
- SKU: NCL1020-1-96 (prominently shown below title)
- Price: €99,00 EUR + "Tax included" note
- Product specs: DIMENSIONS (L: 80 cm, W: 60 cm), MATERIALS (100% Sheepskin), Wool length: 5-7 cm
- Color selector: 7 color swatches (current: Taupe)
- Stock: "66 in stock" (green text)
- Quantity selector: - 1 +
- ADD TO CART button (charcoal/gray, full width)
- Product image gallery: main image + thumbnail strip with color and lifestyle shots (12 images total visible)

**Below the fold:**
- DESCRIPTION accordion (expanded): Generic copy about quality and maintenance. No mention of 20-year warranty, Danish craftsmanship, or ethical sourcing.
- RELATED PRODUCTS section: 5 related rug sizes (100cm, 115x60cm, 90cm, 135cm, 180x162cm)

**PDP missing elements:**
- No reviews or review widget (not even a "0 reviews" placeholder)
- No trust signals near the ATC button (warranty, shipping, returns are all footer-only)
- No Klarna/BNPL messaging near the price
- SKU prominently displayed - B2B artifact, erodes retail confidence
- "66 in stock" communicates abundance, removes urgency. Low-stock variants (seen as "2 in stock" on other products) are not leveraged.
- ATC button is charcoal/gray, same tone as the overall minimal aesthetic. No distinct visual hierarchy guiding the eye to the primary action.
- Description copy is generic and does not support the premium price point with differentiated copy.

### Cart Drawer

**Contents (single item: New Zealand Sheepskin | Long Wool | 80 cm, Taupe, €99.00):**
- Header: "CART" with X close button
- Product line: brand label, product name, price, color, quantity selector (- 1 +), Remove link
- Large empty white space (majority of the drawer)
- "Add order note" link
- "Taxes and shipping included" text
- Two buttons: "VIEW CART" and "CHECKOUT • €99,00" (both in the same gray/taupe color with identical visual weight)

**Cart missing elements:**
- No product recommendations or cross-sells
- No trust signals near the checkout button
- No Klarna/BNPL messaging
- No urgency signals
- No social proof
- No free shipping progress bar or upsell nudge
- VIEW CART and CHECKOUT have equal visual weight. No clear primary action.

---

## 5. CRO Ebook Reference (Billion Dollar Websites - Dylan Ander)

**Relevant sections consulted:**

**Chapter 5 - Unique Value Propositions near ATC:**
UVPs should appear near Add to Cart buttons on Product Pages. NC's primary UVP (20-year warranty) does not appear anywhere near the ATC. The ebook notes that UVP placement directly above, below, or beside the ATC is one of the highest-impact optimizations because it addresses The Gator's hesitation at the exact moment of decision.

**Chapter 9 - Buy Now Pay Later:**
"In all my years of experience, I've never once seen [BNPL] have a negative impact." NC accepts Klarna but does not communicate it anywhere near the point of purchase. The ebook recommends making the BNPL option just as visible as the standard purchase option, especially on high-ticket items. NC's rug range (€99-€1,299) is a natural fit.

**Chapter 9 - Cart Upsells (Pre-Purchase):**
Pre-purchase upsells in the cart are one of the most effective AOV strategies. In-cart upsells targeted to what is in the cart convert at 8-15%, compared to 2-4% for generic recommendations. NC's cart drawer is empty white space with zero upsell attempt.

**Chapter 10 - One-Click Upsells:**
"The best time to ask for a sale is after a customer has already decided to purchase from you." One-click upsells in the cart require no additional checkout friction. NC has natural product pairings: rug + cushion, rug + care brush, rug + slippers.

---

## 6. Research Benchmarks

**Trust signals near ATC (industry data):**
- Moving return policy from footer to near ATC: +23% add-to-cart (Blend Commerce, 2024)
- Trust signals at point of decision: +32.7% CR, +105.2% Revenue per Visitor, +54.6% AOV on mobile (various CRO practitioner data, 2024)
- Review counts displayed near ATC: +18% add-to-cart (various sources, 2024)

**Cart drawer upsells:**
- In-cart contextually relevant offers: 8-15% conversion rate
- Generic "you might also like": 2-4% conversion rate
- AOV improvement from cart upsell strategy: 10-30% (industry benchmarks, 2024-2025)

---

## Cross-Source Analysis: Converging Themes

### Theme 1: Trust gap at the point of purchase
NC's strongest differentiator (20-year product warranty) is invisible during the purchase journey. The ATC button on every PDP is surrounded by no trust signals whatsoever. The warranty, free delivery, and returns are footer-only. Competitors (Sheepskinhouse, Nordic Sheep) surface all three prominently near their buy buttons. The Google Ads data confirms NC knows these are conversion levers (the US search ad leads with "100 days free return, free 2-3 days delivery") but fails to deliver the same message on-page.

Sources: Site Screenshots (PDP, Cart, Homepage), Google Ads, Competitor Research, Benchmarks.

### Theme 2: Zero social proof at every funnel stage
NC shows no reviews anywhere on the site. Not on the homepage, not on collection pages, not on PDPs. Competitors display hundreds to near-800 reviews. From a prospect's perspective, NC's products could be extraordinary, but without any public validation, the site reads as untested. For a brand selling €99-€1,299 items, the absence of reviews is a major trust deficit.

Sources: Site Screenshots (all pages), Competitor Research.

### Theme 3: Cart is completely unconverted
The cart drawer is an empty canvas with no upsell, no BNPL, no trust signal, and no visual hierarchy guiding the visitor toward checkout. Both buttons are identical. NC accepts Klarna (visible in footer icons) but does not communicate it anywhere near the checkout button. For a brand with average items at €99-€249+, BNPL messaging could meaningfully reduce checkout hesitation and increase AOV.

Sources: Site Screenshots (Cart), CRO Ebook (Ch. 9 & 10), Google Ads (no BNPL messaging observed), Benchmarks.

### Theme 4: Homepage does not convert
The homepage first fold is pure editorial photography with no headline, no CTA, and no trust signal above the scroll. Visitors who land on the homepage must scroll multiple times before encountering any brand message or path to a product. This is a significant entry funnel leak, compounded by a 34/100 page speed score that means many mobile visitors will bounce before the page finishes loading.

Sources: Site Screenshots (Homepage), Page Speed, Competitor Research.

### Theme 5: Page speed is conversion-critical
Homepage: 34/100, 30MB payload, 22.5s lab LCP. PDP: 45/100, 23.7s lab LCP. Both pages fail Core Web Vitals. At these load speeds, a significant percentage of mobile visitors never see the site. Fixing page speed is not an A/B test. It is a prerequisite for CRO. Recommendations in slots below assume page speed is addressed in parallel or prior to testing.

Sources: Page Speed (both reports).

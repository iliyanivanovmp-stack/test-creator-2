# Sharland England Roadmap Seed

**Store:** https://sharland-england.com/
**AOV:** Unknown (observed: £185 Hadley Tray, £875–£1,395 Juliette furniture, £38–£80 ceramics/small accessories)
**Monthly sessions:** Unknown — no analytics data collected
**Data sources:** Meta Ads visual summary (3 ads + 3 landing pages), Google Ads visual summary, Trustpilot reviews (2022–2025), PageSpeed / Core Web Vitals (tested 2026-07-13), Site visual summary (homepage, collection, PDP, cart), live site fetch, competitor web research

---

## Key Insights

Trust signals are structurally misallocated. The Hadley Tray PDP — the brand's best-performing page by design — has 23 five-star reviews positioned immediately below price, a named designer (Louise Roe), and a sustainability icon row. Everywhere else on the site: zero. Homepage has press logos from Vogue, AD, and The New York Times but no star rating, no customer quote, no shipping promise. Collection pages show GBP prices on a 4-column grid with no review counts on cards. The brand has earned high trust signals (4.7 Trustpilot, premium press) but buries or withholds them at the pages where most paid traffic lands first.

Page performance is eliminating a large portion of paid traffic before the first product interaction. Mobile LCP on both the homepage (27.3s) and the Hadley Tray PDP (29.0s) is catastrophically outside Google's 2.5s "good" threshold. At these scores, visitors arriving from Meta Ads 1, 2, and 3 — all running video-based creative against collection or PDP landing pages — are bouncing before the page resolves. Every A/B test on the site is running in the context of a load experience that is eliminating the majority of mobile visitors before any element of the test is seen.

US expansion is the current growth priority but the execution has a visible conversion gap. Ad 3 targets US visitors with "FASTER SHIPPING. NO TARIFFS" and lands them on a US-collection page showing GBP prices throughout (£185, £395, £1,075). The "No Tariffs" claim from the ad creative is not restated on the landing page — only "No delays: shipped from our US warehouse." Trustpilot reviews confirm US shipping is already working well ("amazed at the speed the Hadley tray arrived," "Fast shipping!" from US reviewers), but the site doesn't leverage this proof at the point of purchase for US visitors. This is a direct revenue gap on active paid spend.

---

## Top Test Opportunities

### 1. Collection Page Popup — Delay or Remove On-Load Trigger
**What's broken:** On the Outdoor Collection landing page (Ad 1 LP) and the US Collection page (Ad 3 LP), a full newsletter popup fires on page load before the user has scrolled or clicked. It appears as a centred modal overlay with the heading "ENJOY 10% OFF YOUR FIRST ORDER / JOIN OUR NEWSLETTER" and two text input fields (name, email), plus a close X in the top-right corner. The popup covers approximately one full product card in the top row of the 4-column grid — which is the first product slot the user's eye would naturally land on after the ad-driven arrival. The modal fires immediately with no delay, exit intent, or scroll trigger. Ads 1 and 3 both land on collection pages, making this popup the first conversion-path friction for two of three active Meta campaigns.
**Evidence:** meta-ads-visual-summary.md (Ad 1 LP fold 1, Ad 3 LP fold 1), site-visual-summary.md (collection fold 1)
**Key data:** No delay on popup trigger; covers product slot 3 in a 4-column grid; newsletter offer (10%) duplicates the top bar offer already visible above the popup
**Est. lift:** 8–15% CR lift on collection pages × sessions unknown × ~£300 blended AOV

### 2. US Landing Page — Dynamic USD Pricing for US Visitors
**What's broken:** The US Collection landing page (Ad 3 LP) is a standard Shopify collection page. Hero copy says "We're Now in the US / No delays: Rattan accessories, furniture & linens shipped directly from our US warehouse." The 4-column product grid below shows GBP-denominated prices throughout: Hadley Tray Berry £185, Fraises Des Bois Tablecloth £395, Emerson Outdoor Dining Chair Set of 2 £1,075, Pinet Plant Pot Small From £95. There is no currency selector in the nav or anywhere on the page. A US visitor who clicked an ad promising "FASTER SHIPPING. NO TARIFFS" sees GBP prices with no USD conversion, no exchange rate context, and no currency toggle. The "No Tariffs" claim from the ad creative does not appear on the landing page at all — it resets to "No delays" language only.
**Evidence:** meta-ads-visual-summary.md (Ad 3 creative, LP folds 1–3), manifest.md open questions
**Key data:** All prices in GBP on a page explicitly targeting US visitors; "No Tariffs" claim present in ad, absent from LP; US Trustpilot reviews confirm willingness to pay but mention pricing/logistics anxiety
**Est. lift:** 10–20% CR lift on US-targeted traffic × US sessions unknown × ~£200 blended USD AOV (accessories emphasis on US LP)

### 3. PDP Buy Box — Shipping Timeline + Returns Window
**What's broken:** On the Hadley Tray PDP, the right-column buy box shows: product name, price (£185.00), star rating (23 reviews), colour selector (Berry/brown/green), quantity input (-/1/+), ADD TO CART (dark, full-width), an open description accordion, and two collapsed accordions (Dimensions & Care; Shipping & Returns). The "Ships Globally" trust icon appears in a row below the add-to-cart button, but no shipping timeline is visible — not "3–5 business days," not "US warehouse — faster delivery," not "free shipping on orders over X." The Shipping & Returns accordion is closed by default and requires a deliberate click to open. Trustpilot reviews from US customers cite shipping anxiety as the primary pre-purchase hesitation, even when their actual experience was fast ("we were concerned about logistics... that wasn't necessary").
**Evidence:** site-visual-summary.md (PDP buy box), meta-ads-visual-summary.md (Ad 2 LP), reviews.md (US reviewer shipping concern pattern)
**Key data:** "Ships Globally" icon visible but no timeline or cost; Shipping & Returns collapsed by default; US warehouse now active (could enable "US: 3–5 days" promise); at least 3 Trustpilot reviews mention shipping concern before ordering
**Est. lift:** 5–10% CR lift on PDP × sessions unknown × £185 AOV

### 4. Cart Page — Shipping Cost Reveal + Returns Line
**What's broken:** The cart page (full-page layout, not slide-out) shows item, quantity, subtotal, and then the line: "Tax included. Shipping calculated at checkout." There is no shipping estimate, no free-shipping threshold bar, and no returns promise anywhere in the cart. The only CTA visible is "CHECK OUT" (dark, full-width), followed by Shop Pay, PayPal, and Google Pay express buttons. The "You May Also Like" section at the bottom shows 2 product thumbnails but with no AOV mechanic (no "add £X more for free shipping," no bundle). The cart is the highest-intent page on the site, yet it provides less trust copy than the PDP — which at least has an icon row and star rating.
**Evidence:** site-visual-summary.md (cart), reviews.md (one 1-star return experience with no communication), meta-ads-visual-summary.md (Ad 2 LP buy box comparison)
**Key data:** "Shipping calculated at checkout" is a documented cart-abandonment trigger; no returns policy or timeline visible at checkout entry; observed cart subtotal £370 (2× Hadley Tray)
**Est. lift:** 5–8% reduction in cart abandonment × sessions unknown × ~£370 average observed cart

### 5. Collection Cards — Add Review Count Stars
**What's broken:** Every product card across all collection pages (Shop All, Outdoor, US Collection) shows: product image, product name, price, and colour swatches on applicable products. There are no star ratings and no review counts. The Hadley Tray, which has 23 five-star reviews prominently shown on its PDP, appears in the Bestsellers carousel on the homepage and in the collection grid with only its name and price — £185, no social proof. For a brand competing at 3–5× the price of comparable rattan accessories at Birdie Fortescue (£38) or The Rattan Company, review counts on cards are the most immediate trust signal available at the browsing stage.
**Evidence:** site-visual-summary.md (collection page, homepage bestsellers carousel), meta-ads-visual-summary.md (Ad 1 LP fold 2), reviews.md (23 five-star reviews on Hadley Tray alone)
**Key data:** 23 reviews on Hadley Tray with 0 visible at collection level; 4.7 Trustpilot rating not shown anywhere on homepage or collection; Birdie Fortescue comparable rattan tray priced at £38–54 vs £185 — trust signals must close the price gap
**Est. lift:** 3–7% CR lift on collection-to-PDP click-through × sessions unknown × ~£185 accessories AOV

### 6. Homepage — Trust Signal Block Near Hero
**What's broken:** The homepage hero (fold 1) is a full-width lifestyle carousel with a "SHOP GARDEN FURNITURE" CTA button. Fold 2 shows the Bestsellers product carousel. The press logo bar — Vogue, The Telegraph, WSJ, NYT, House & Garden, AD, Architectural Digest, Veranda — appears at the bottom of fold 2 or start of fold 3. No star rating, customer quote, or Trustpilot badge appears anywhere on the homepage. The 10% newsletter bar at the top is the only active offer-signal. A new visitor from prospecting traffic or a non-branded Google search lands on a visually beautiful page with zero verification that others have bought and are happy. The press logos provide authority when reached but are passive and below the fold.
**Evidence:** site-visual-summary.md (homepage folds 1–3), reviews.md (4.7 Trustpilot, strong positive quality), live site fetch (Trustpilot 4.7 referenced in site metadata)
**Key data:** Trustpilot 4.7 (estimated from review sample) not shown on page; 8 major press logos present but below scroll fold; zero customer quotes or star ratings on homepage
**Est. lift:** 2–5% CR lift on homepage entry sessions × sessions unknown × ~£200 blended AOV

### 7. Cart AOV — Free Shipping Threshold Progress Bar
**What's broken:** The cart page contains a "You May Also Like" section with 2 product thumbnails and a "View all" link — a passive cross-sell with no incentive to act. There is no active AOV mechanic anywhere in the cart. Given the product range (accessories from £38, plant pots from £95, Concha Dish from £80, Little Flower £55 — all shown in the PDP "Pairs well with" section), a free-shipping threshold bar set at, for example, £250 or £350 (achievable by adding one accessory to a tray order) would turn passive browsing into active upsell. The Hadley Tray at £185 sits just below any plausible threshold, making the lever credible.
**Evidence:** site-visual-summary.md (cart AOV section), meta-ads-visual-summary.md (Ad 2 LP "Pairs well with" carousel), reviews.md (multiple reviews mentioning multi-item orders and gift purchases)
**Key data:** No AOV mechanic in cart; "Pairs well with" accessories priced £55–£95 would close a £250 threshold from a £185 basket; multiple reviewers purchased multiple items or bought as gifts (suggesting multi-item intent exists)
**Est. lift:** £40–80 AOV increase × conversion rate on sessions where cart contains at least one item

### 8. Ad 1 Landing Page — Juliette Collection Hero
**What's broken:** Meta Ad 1 runs a video specifically about the Juliette Collection with the headline "Inspired by antique pieces, our Juliette collection brings timeless charm to outdoor spaces." The landing page is the general Outdoor Collection page. Fold 1 shows a full-width hero (outdoor rattan furniture, no Juliette branding), then fires the newsletter popup. There is no Juliette-specific banner, headline, or storytelling section on the page — Juliette pieces are mixed into the 4-column product grid alongside Emerson and other outdoor lines. The emotional hook from the ad ("timeless charm," "antique pieces") does not appear anywhere on the landing page. A visitor who clicked the ad specifically interested in Juliette must search the grid to find the relevant pieces.
**Evidence:** meta-ads-visual-summary.md (Ad 1 creative, LP folds 1–3)
**Key data:** Ad 1 uses Juliette-specific headline; LP shows general Outdoor Collection; Juliette items visible in grid but not called out; price range £875–£1,395 for Juliette seating and tables
**Est. lift:** 8–12% CR lift on Ad 1 LP sessions × Ad 1 sessions unknown × ~£875–£1,375 AOV (Juliette furniture range)

---

## Unused Findings

- Named customer service (Quinn, Katherine, Celia cited by name in reviews) is an unreplicated differentiator — a "Chat with our team" CTA in the PDP or cart could convert this into a direct conversion path.
- Unboxing experience (personal note from Louise, handwritten card, exceptional packing) is praised in at least 5 reviews — buy-box copy noting "Every order includes a personal note" would pre-sell the full brand experience before add-to-cart.
- Competitor display ad visible in Sharland England Google SERP — brand search is not fully protected; a branded keyword defensive campaign review is warranted.
- PDP cross-sell "Pairs well with" carousel (Pinet Plant Pot, Concha Dish, Little Flower) has no one-click add or bundle discount — passive display-only cross-sell at a point where purchase intent is highest.
- Homepage hero CTA "SHOP GARDEN FURNITURE" is category-specific on a general brand homepage — will mismatch for visitors interested in ceramics, linens, or accessories.

# Stay Salted CRO Research Audit

**Brand:** Stay Salted
**Store:** stay-salted.com
**Audit Date:** April 29, 2026

---

## Data Sources Collected

Meta Ads (3 ads out of many active campaigns), Reviews & UGC (4 reviews), Page Speed / Core Web Vitals (mobile), Competitor Research, Site Screenshots (desktop homepage, mobile homepage, cart)

---

## Source 1: Meta Ads

Three ads analyzed from the brand's Meta ad library. These represent a sample of many active campaigns.

### Ad 1
- **Library ID:** 1866031510706319
- **Running since:** January 26, 2026
- **Angle:** Running hydration pain point
- **Headline:** "Is it hard to maintain a steady pace while running?"
- **Body:** "Most runners hit the wall for one of these three reasons: (1) You start running before you've hydrated properly; (2) You lose more minerals while sweating than you realize..."
- **Creative:** Dark background. Bold text: "IF YOU WANT A MORE STABLE PACE WHILE RUNNING, START WITH PROPER HYDRATION." SALTED product and formula visible.
- **CTA:** Order Now
- **Landing page:** stay-salted.com (homepage)

### Ad 2
- **Library ID:** 1274196347925384
- **Running since:** March 8, 2026
- **Angle:** Performance proof
- **Headline:** "How to improve your pace by 6.3% in 3 easy steps"
- **Body:** "Many runners miss something more basic - how to prepare before running and how to recover after. This is one of the most underestimated parts of the foundation..."
- **Creative:** Carousel. Slide 1: runner silhouette + headline. Slide 2: Strava comparison showing Vladimir Balabanov's 5K time dropping from 19:41 to 18:28 with SALTED.
- **CTA:** "Order Now" / "Improve your pace"
- **Landing page:** stay-salted.com (homepage)

### Ad 3
- **Library ID:** 1266452222290143
- **Running since:** April 5, 2026
- **Angle:** Cramping pain point
- **Headline:** "Do you cramp while running?"
- **Body:** "Cramps come out of nowhere and can ruin the entire session. Once they start, they torment you until you finish running."
- **Creative:** Bold text: "CRAMPS WHILE RUNNING / ELECTROLYTES." Product and formula (1000mg Na, 300mg K, 60mg Mg) visible.
- **CTA:** "Get SALTED now and kick out the cramps!"
- **Landing page:** stay-salted.com (homepage)

### Cross-Ad Findings
- All 3 ads target runners with distinct pain angles: hydration/hitting the wall, pace improvement, cramping
- All 3 land on the same generic homepage regardless of the angle used
- The Strava proof in Ad 2 (6.3% pace improvement, Vladimir Balabanov 19:41 to 18:28) is the strongest social proof the brand has produced - it disappears after the click
- No dedicated landing pages per ad angle

---

## Source 2: Google Ads

Skipped.

---

## Source 3: Reviews & UGC

Four reviews and testimonials collected. Review base is small overall; the /review page is a submission form with no displayed reviews.

**Review 1 - Stoyan Stoyanov, Firefighter/Runner** (4 stars, homepage testimonial)
> "The box has an interesting, clean design with clearly marked ingredients. After the first sip, I noticed a more serious presence of Sodium, Potassium and Magnesium vs. my previous electrolytes. The taste is pleasant and unobtrusive. During the warm-up I felt quite fresh and energetic. During the run I performed much better than expected on this exact course. I haven't felt any fluctuations, signs of dehydration or energy drops."

**Review 2 - Anonymous (informal DM to brand founder)**
> "I'm quite satisfied. Good values and interesting taste - not like the sugary salts of all the other brands. Top!"

**Review 3 - Mladen Dikov, Pharmacist/Runner/Cyclist** (5 stars)
> "Since trying the product, I feel much more endurance during serious training sessions. I run ~40km/week and cycle ~60km, plus strength training. Mentally I'm better, and I work two jobs - I need constant focus and hydration."

**Review 4 - Anonymous female (informal DM, day 2 of use)**
> "Second day drinking Salted, my mornings are significantly more energetic (I had dizziness before, it's gone now). In workouts I also noticed more energy. Surprised it's working already on day 2. They help me a lot!"

### Key Themes

| Theme | Frequency | Notes |
|-------|-----------|-------|
| Fast-acting results | 2/4 | Effects within 1-2 uses. Day-2 feedback is a strong purchase skepticism reducer. |
| Mental clarity / focus | 2/4 | Independently mentioned by two reviewers. Absent from all current ads and landing page. |
| "Not like sugary salts" | 1/4 | Spontaneous competitive differentiation. Strong signal. |
| Performance improvement | 2/4 | Better pace, no energy drops, more endurance |
| Clean ingredients | 2/4 | Formula transparency and design praised |
| Multi-sport use | 2/4 | Running, cycling, strength training, daily energy - beyond running-only |

---

## Source 4: Page Speed / Core Web Vitals

**Report date:** April 29, 2026
**Device:** Mobile
**URL:** stay-salted.com

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Performance Score | 48/100 | 90+ | Failing |
| First Contentful Paint | 3.6s | ≤1.8s | Poor |
| Largest Contentful Paint | 64.2s | ≤2.5s | Catastrophic |
| Total Blocking Time | 770ms | ≤200ms | Poor |
| Speed Index | 4.2s | ≤3.4s | Poor |
| Cumulative Layout Shift | 0.001 | ≤0.1 | Good |
| Accessibility | 93/100 | - | Good |
| Best Practices | 96/100 | - | Good |
| SEO | 92/100 | - | Good |

**Top opportunities identified:**
- Image optimization: 12,198 KB potential savings (primary LCP driver)
- Total network payload: 36,373 KB (massively overweight)
- Reduce unused JavaScript: 228 KB savings
- Reduce unused CSS: 188 KB savings
- Use efficient cache lifetimes: 129 KB savings

An LCP of 64.2s means the page's largest content element takes over a minute to render on mobile. For an athlete who tapped an ad during or after a workout, the page is functionally unusable. The 12,198 KB image savings indicate hero/product images are being served uncompressed at full resolution.

---

## Source 5: Competitor Research

### LMNT (Global Category Benchmark)

| Attribute | SALTED | LMNT |
|-----------|--------|------|
| Price per sachet | €0.86 | $1.30 (subscription) / $1.50 (one-time) |
| Sodium | 1,000mg | 1,000mg |
| Potassium | 300mg | 200mg (SALTED wins) |
| Magnesium | 60mg | 60mg |
| Flavors | 1 | 11 |
| Subscription | No | Yes |
| Market | Bulgaria / EU | Global |

SALTED is approximately 40% cheaper per sachet than LMNT with higher potassium. Neither advantage is surfaced anywhere on the homepage or product page.

### Bulgarian Market
- **Nutrim:** Local sports drink market leader, partnered with the Bulgarian Athletics Federation. Mass-market positioning, broad distribution.
- **Dr Witt (Tymbark):** Best-performing Bulgarian sports drink by volume share gains in 2025. Isotonic format, different positioning from SALTED.
- No direct local competitor identified in the high-sodium, no-sugar electrolyte sachet format targeting endurance athletes.

### Strategic Position
SALTED occupies a near-uncontested niche in Bulgaria: clinical-ratio electrolyte sachets, no sugar, single-serve, targeting serious endurance athletes. The closest global analog is LMNT, at a significantly higher price point. Local competition is either mass-market isotonic drinks (Nutrim, Dr Witt) or general supplement powders - not sachets with clinical mineral ratios.

---

## Source 9: Site Screenshots

### Desktop Homepage (Fold 1 - from Meta ad landing page)
- Left half: product sachet image
- Right half: "SALTED Citrus Blast" headline, product description (precise electrolyte ratios, fast-absorbing minerals, scientifically-based hydration), 3 negative claims (no colorants, no artificial flavors, no added sugar)
- Buy box: 1-box option (€25.90 / 50.66 BGN, €0.86/sachet) and 2x-box option (€51.80 / 101.31 BGN + "Free shipping" tag), yellow-green "Вземи сега" CTA

### Desktop Homepage (Fold 2-3)
- Stoyan Stoyanov review card (4 stars, long detailed text)
- SALTED Athletes section: 7 athlete photos in a grid with names and Instagram handles

### Desktop Homepage (Fold 3-4)
- "What's inside" section: product visual with Na/K/Mg callouts
- Three collapsed accordions: About the product, Nutritional value, Quality and safety
- "Why SALTED works" section: 3 benefit columns (mineral ratio matched to sweat, high sodium, nothing excessive)

### Mobile Homepage (Fold 1)
- SALTED logo + "BUILT ON DEDICATION" tagline
- Large product sachet image filling most of the screen
- Buy box NOT visible without scrolling

### Mobile Homepage (Fold 2)
- Buy box: 1-box (€25.90) and 2-box (€51.80, "Free shipping" tag), yellow-green "Вземи сега" CTA
- SALTED Athletes grid starts immediately below

### Mobile Homepage (Fold 3)
- Remaining athletes + start of "What's inside" formula visual

### Cart (Mobile)
- Header: "Информация за поръчка" (Order information) - full-page cart, not a slide-out drawer
- Product: SALTED Citrus Blast 30 sachets, qty 1, €25.90 / 50.66 BGN
- Delivery line: €0.00 / 0.00 BGN
- Promo code: Input field visible and expanded by default with "Apply" button
- Free shipping bar: "Add €17.56 / 34.34 BGN more to unlock FREE SHIPPING" at 59% progress
- **Contradiction:** Delivery shows €0.00 but progress bar says €17.56 more needed for free shipping
- No 2-box bundle upsell visible
- No checkout CTA visible in screenshot (below fold on mobile)

### Critical Finding: Product Out of Stock
The product page showed as out of stock when fetched on April 29, 2026. No A/B tests should launch while stock is unavailable - test results would be invalid and ad spend is wasted.

---

## Cross-Source Analysis: Converging Themes

### Theme 1: Mobile page speed is destroying conversion before visitors see the product
**Sources:** Page Speed, Site Screenshots, Meta Ads

LCP of 64.2s on mobile (April 29, 2026) means most ad-driven visitors bounce before the page renders. The primary audience (athletes) is predominantly mobile. Images alone account for 12,198 KB of unnecessary payload on a 36,373 KB total page. Every dollar of Meta ad spend is partially wasted until this is resolved.

### Theme 2: All paid traffic hits the same generic landing page regardless of ad angle
**Sources:** Meta Ads, Mobile Homepage Screenshots

Three specific runner pain points (hitting the wall, pace improvement, cramping) all land on a "BUILT ON DEDICATION" opener. The Strava proof from Ad 2 - 6.3% pace improvement, real athlete data, the most credible social proof the brand has - disappears after the click. On mobile, the first fold shows a product image and brand tagline. No acknowledgment of what the visitor just clicked.

### Theme 3: Mental clarity is an untapped conversion and audience angle
**Sources:** Reviews (2/4 reviews independently cite this)

"Mentally I'm better" and "significantly more energetic mornings" appear in separate reviews with no prompting. This angle is absent from all 3 ads and from all landing page copy. It suggests a second persona beyond endurance athletes: working professionals who train and need sustained focus throughout the day.

### Theme 4: Cart UX erodes trust at the highest-intent moment
**Sources:** Cart Screenshot

The default-open promo code field signals to customers they may be overpaying, sending them to search Google for discount codes. The free shipping progress bar contradicts the €0.00 delivery amount shown directly above it. No bundle upsell captures the 2-box opportunity at the moment of purchase.

### Theme 5: The brand's biggest competitive advantages are invisible on site
**Sources:** Competitor Research, Reviews, Site Screenshots

SALTED is 40% cheaper per sachet than LMNT with superior potassium (300mg vs 200mg). Customers unpromptedly call out "not like sugary salts from other brands" as a differentiator. Rapid results (felt within 1-2 uses) are buried in reviews, not in headline copy. None of these appear above the fold.

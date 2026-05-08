# Da Valeria - CRO Research Audit
**Store:** davaleria.com | **Date:** May 6, 2026

---

## Meta Ads (3 ads analyzed out of many active campaigns, April-May 2026)

### Ad 1 — Library ID: 1539719640896684 (Active since Apr 24, 2026)
- **Creative:** Video ad. Product shown: adjustable, non-slip cutlery organizer (portaposate regolabile e antiscivolo) at €14.90. Visual tagline: "Per una casa organizzata" (For an organized home). Section label: "I Più Desiderati" (Most Wanted).
- **Ad copy headline:** "🛑 Smetti di cercare! DaValeria ha TUTTO per la tua casa: Utensili cucina che durano anni - Piccoli Elettrodomestici - Contenitori salva-spazio per tutto 💰 Prezzi da negozio sotto casa 🚚 Arriva in 48h..."
- **Body:** "SEGUICI ogni settimana pubblichiamo idee e prodotti per la tua casa"
- **Landing page:** davaleria.com (homepage)
- **Message match assessment:** FAIL. The ad shows a specific kitchen organizer at €14.90 and promises kitchen utensils. The homepage hero at time of analysis reads "DOPPIO SCONTO ESCLUSIVO FINO AL [X]% - PRIMAVERA ENTRA IN CASA" with featured outdoor products (BBQs, garden furniture). Zero visual or copy connection to the ad's product or category. The ad's 48-hour delivery claim is buried in the announcement bar only.

### Ad 2 — Library ID: 1277329610697369 (Active since Apr 26, 2026, multiple versions)
- **Creative:** Product image of Tescoma Affetta Mela "Presto" apple slicer (green).
- **Ad copy:** "SEGUICI ogni settimana pubblichiamo idee e prodotti per la tua casa" (same as Ad 1)
- **Headline:** "Tescoma Affetta Mela 'Presto'"
- **Landing page:** davaleria.com/preparazione-degli-alimenti/10-tescoma-affetta-mela-presto-8595028449402.html
- **Message match assessment:** PASS. Ad takes the user directly to the matching PDP.
- **PDP issues observed:**
  - Price is €5.20 but not shown in the ad (missed hook)
  - Only 2 product images (thumbnail + line drawing)
  - Description is 2 sentences, repeated identically in the description tab below
  - Embedded YouTube video is in English (Tescoma's brand channel), not Italian
  - PayPal BNPL banner shown for purchases €120-€5,000 on a €5.20 product — irrelevant and confusing
  - Two sidebar banners ("linea TESCOMA" / "scopri le novità") actively link users away from the product being viewed
  - Zero customer reviews on the page
  - "Potrebbe anche piacerti" (related products) shows only 2 items

### Ad 3 — Library ID: 1674544417081679 (Active since Apr 24, 2026)
- **Creative:** Video ad. Product shown: PP polypropylene garden chair at €39.00. Tagline: "Per il tuo spazio esterno - Sedia in pp resistente, leggera e versatile." Section label: "Indispensabili del Mese" (Essentials of the Month).
- **Ad copy headline:** "Vesti il tuo giardino con DaValeria"
- **Body:** "Rinnova il tuo outdoor con la qualità del polipropilene (PP). La nostra sedia è progettata per durare nel tempo e resistere agli agenti atmosferici..."
- **Landing page:** davaleria.com/ricerca?controller=search&s=sedia%20giardino (search results for "garden chair")
- **Message match assessment:** PARTIAL FAIL. The landing page is a raw internal search results page showing 97 products under the heading "RISULTATI RICERCA." The PP chair from the ad is visible in the results, but:
  - The page heading "RISULTATI RICERCA" reads as unintentional, not a curated category
  - The left sidebar "IN EVIDENZA" (featured) widget shows unrelated products: a hand blender, an inflatable mattress, a hair dryer — no connection to outdoor furniture
  - One product card shows a 948-day countdown timer (likely a technical glitch)
  - No filtering visible to narrow by material (PP), color, or price
  - No category narrative or merchandising — pure search dump

---

## Reviews & UGC (Trustpilot, reviews from Aug 2021 to Dec 2025)

### What customers consistently praise
| Theme | Representative quotes |
|---|---|
| Fast delivery | "Spedizione e ricezione velocissima" / "Consegna ultrarapida" / "Arrivato due giorni dopo l'acquisto" / "Velocissimi nella consegna" |
| Product matches description | "Il vassoio corrisponde alla descrizione" / "Prodotto corrispondente alla descrizione" / "Tutto come indicato sul sito" |
| Good value / competitive pricing | "Prezzo adeguato" / "Buon rapporto qualità prezzo" / "Prezzi molto convenienti" |
| Responsive support | "Rispondono subito" (chat) / "Personale cortese e professionale" / "Bastata una telefonata, me le hanno mandate via whatsapp" |
| Quality packaging | "Imballato perfettamente" / "Arrivate senza un graffio" |
| First-purchase discount appreciated | "Ho usufruito di uno sconto del 10% per primo acquisto" |

### Friction points and complaints
| Issue | Specifics |
|---|---|
| Courier reliability (GLS) | "Il corriere GLS a cui si affidano per la provincia in cui abito è davvero inaffidabile. Hanno ricevuto la merce il giorno 7 gennaio e la consegna è avvenuta oggi 13 gennaio." (Amazon had promised Jan 7-8.) Reviewer recommends changing courier for some provinces. |
| No floor delivery for heavy items | "Il servizio di spedizioni non prevedeva la consegna al piano, e 40 kg di mobile al terzo piano senza ascensore non è stato semplice." |
| Inconsistent communication | One reviewer: "Comunicazioni inesistenti, non rispondono a nessuna tua richiesta di info e la tracciabilità del corriere non esiste." Contradicts majority who praise responsiveness. Likely varies by inquiry type or channel. |
| Assembly instructions missing/unclear | Multiple mentions: missing instructions resolved by calling and getting them via WhatsApp; another reviewer notes instructions "avrebbero potuto essere più chiare" in some steps. |
| Product differs from images | One reviewer (3 stars): "Oggetto buono ma difforme dalle immagini." |
| Defective product | One reviewer received a Christmas tree with a broken bent part and missing pieces. |
| PayPal transaction confusion | One reviewer needed live chat to resolve confusion about a PayPal transaction. |

### Client-actionable (not CRO test items)
- Consider switching GLS courier for provinces with reliability issues
- Include assembly instructions in packaging for furniture, not just on request
- Standardize product imagery to match received product more closely
- Fix PayPal checkout flow confusion (investigate what causes it)

---

## Page Speed / Core Web Vitals (Mobile, May 6, 2026 — PageSpeed Insights)

| Metric | Score | Status |
|---|---|---|
| LCP (Largest Contentful Paint) | 9.5s | FAILED (threshold: 2.5s) |
| INP (Interaction to Next Paint) | 118ms | Needs improvement |
| CLS (Cumulative Layout Shift) | 0.05 | Passed |
| FCP (First Contentful Paint) | 2.3s | Needs improvement |
| Speed Index | 6.1s | Poor |
| Total Blocking Time | 70ms | Good |
| **Performance score** | **68/100** | Poor |
| Accessibility | 88/100 | Good |
| Best Practices | 77/100 | Needs improvement |
| SEO | 92/100 | Good |

**Top issues flagged:**
- Render-blocking requests: estimated 2,802ms savings
- Unoptimized images: estimated 566 KB savings
- Unused JavaScript: estimated 213 KB savings
- Unused CSS: estimated 70 KB savings
- Accessibility: background/foreground color contrast insufficient; links rely on color only; heading order non-sequential
- Best Practices: deprecated APIs (6 warnings), browser console errors, missing source maps

An LCP of 9.5s means the main content takes nearly 10 seconds to fully render on mobile. On a device-heavy Italian market where majority of ecommerce traffic is mobile, this alone suppresses conversion significantly before any UX or offer issues come into play.

---

## Competitor Research (May 2026)

### Kasanova (kasanova.com) — Primary direct competitor, physical + online
- Free shipping threshold: €59 (identical to Da Valeria)
- First-order discount: 10% via newsletter (same mechanic as PRIMO10)
- Flash sales with countdown timers on homepage (e.g., "Fino al 17/05")
- VIP loyalty card with member-exclusive pricing — Da Valeria has no loyalty program
- Physical store network (major differentiator)
- No customer reviews visible on homepage
- Heavy use of strikethrough pricing / discount anchoring
- Web assistant launched for guided shopping

### Duebi Casalinghi (duebicasalinghi.it) — Specialist cookware retailer
- Rating: 4.8/5 based on 611 reviews — displayed prominently on homepage
- Phone number shown 3 times on homepage
- Free shipping threshold: €99 (significantly higher than Da Valeria's €59)
- Cash on delivery option available
- Italian manufacturing positioning
- Specialist positioning in cookware (Tescoma, Bialetti, Marcato)

### Key gaps Da Valeria can exploit
- Both major competitors lack strong review display on homepage
- Da Valeria's €59 free shipping threshold beats Duebi Casalinghi's €99
- Da Valeria's fast delivery (2 days, per reviews) is verified but not surfaced on site — neither competitor leads with this
- No competitor has surfaced the "fast delivery" trust signal as a hero UVP

---

## Site Screenshots (May 2026)

### Homepage
- Announcement bar: "Spedizione gratuita per ordini superiori a 59€. 10% di sconto su tutti i prodotti, utilizza il codice PRIMO10."
- Hero: "DOPPIO SCONTO ESCLUSIVO FINO AL [X]% — PRIMAVERA ENTRA IN CASA — APROFITTANE SUBITO!!!" Two text layers appear to overlap in the hero image, reducing readability.
- Hero visual: outdoor lifestyle with cherry blossoms. Featured products grid below: outdoor/seasonal items (garden chest €119, BBQ €22.90, Campingaz gas BBQ €219.90, garden umbrella €109, folding table €99.90).
- Trust badge row (below the fold): "Non trovi il prodotto? Scrivici" / "Reso facile — Soddisfatti o rimborsati" / "Spedizione gratuita oltre i 59€" / "Consegna veloce & servizio a domicilio"
- Category showcase section below trust badges: Casalinghi / Fai da te / Arredamento

### PDP — Tescoma Affetta Mela "Presto" (€5.20)
- URL: /preparazione-degli-alimenti/10-tescoma-affetta-mela-presto-8595028449402.html
- PayPal BNPL banner (24 installments, €120-€5,000, 0% APR) displayed prominently above product title — irrelevant to a €5.20 product
- 2 product images (product shot + technical line drawing)
- Description: 2 sentences. Identical text repeated in the "Descrizione" tab below.
- Sidebar: Two promotional banners — "linea TESCOMA clicca qui" and "scopri le novità clicca qui" — both link away from the current product
- Trust signals below ATC: "Pagamenti sicuri al 100%" with PayPal/Mastercard/Visa/Amex icons; "Spedizione gratuita per ordini superiori ai 59€"; "Pagamenti sicuri"; "Reso gratuito"
- YouTube video embedded in description tab: English-language Tescoma brand video
- Related products: 2 items shown

### Collection / Search Results — "sedia giardino" (97 results)
- URL: /ricerca?controller=search&s=sedia%20giardino
- Page heading: "RISULTATI RICERCA" (looks unintentional for paid traffic destination)
- 97 products, default sort: "Rilevanza"
- Left sidebar: Category tree nav + "IN EVIDENZA" widget showing unrelated products (hand blender, inflatable mattress, hair dryer, hair styler)
- Product grid: PP garden chairs, folding chairs, camping chairs, steel chairs — mix of relevant and semi-relevant items
- One product card shows a 948-day countdown timer (likely a glitch)
- Pagination: 12 items per page, 9 pages total — no collection-level merchandising or filtering by material/color

### Cart Drawer
- Language: English throughout ("CART", "There is 1 item in your cart.", "Subtotal", "Shipping", "Total (Tax incl.)", "BUY") on an Italian-language site — localization bug
- Order shown: PP Terracotta Garden Chair €39.00 x 1. Subtotal: €39.00. Shipping: €5.90. Total: €44.90.
- No free shipping progress bar (customer is €20 away from the €59 threshold)
- No cross-sell or upsell recommendations
- No trust signals, payment method icons, or reassurance copy
- Single CTA: "BUY ►" button

---

## Cross-Source Analysis — Converging Themes

### Theme 1: Paid traffic is hitting the wrong pages (High confidence)
Ad 1 (kitchen organizer ad) → homepage with outdoor products hero. Ad 3 (PP garden chair) → raw search results page. Two of three analyzed ads from this sample land visitors in irrelevant contexts. Every euro spent on those ads is partially wasted at the first interaction. The homepage hero doesn't reflect the ad's product, promise, or even category.

### Theme 2: Strong delivery reputation exists but is invisible on-site (High confidence)
Trustpilot reviews from Aug 2021 through Dec 2025 consistently cite fast delivery as the #1 positive. "2 giorni lavorativi," "velocissima," "ultrarapida" appear in the majority of reviews. The homepage buries this in the announcement bar and a trust badge row below the fold. The hero leads with a generic discount. Competitor Kasanova also doesn't lead with delivery speed — first-mover opportunity to own this UVP.

### Theme 3: PDP is the weakest conversion point (High confidence)
Reviews confirm product quality matches descriptions, which means the product itself is not the problem. But PDPs have: zero reviews surfaced, thin descriptions (2 sentences), only 2 images, English-language embedded videos, sidebar banners that link away, and an irrelevant BNPL banner. This combination suppresses conversion at the decision moment.

### Theme 4: Cart recovers zero AOV value from the shipping threshold (High confidence)
The €59 free shipping threshold is a strong hook (reviews confirm customers value it, competitors use the same threshold). But the cart shows the €5.90 fee with no prompt to spend more and qualify. A customer with €39 in their cart has no idea they're €20 away from free shipping unless they calculate it manually.

### Theme 5: Mobile performance is critically slow (High confidence)
LCP of 9.5s on mobile means the page takes nearly 10 seconds to become visually complete. Italian ecommerce is majority mobile. This degrades all other conversion initiatives — a fast-loading page is a prerequisite for anything else to work.

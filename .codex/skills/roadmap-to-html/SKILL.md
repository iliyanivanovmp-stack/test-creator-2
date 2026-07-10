---
name: roadmap-to-html
description: Convert a CRO roadmap markdown file into a branded, Shopify-ready HTML one-pager for clients
---

You are converting a CRO testing roadmap from a detailed internal execution format into a branded, client-facing HTML concept pitch that can be pasted directly into a Shopify page. The HTML version is what the client sees. The markdown stays internal.

The goal: the client scans the HTML in 60 seconds, understands which pages/components we want to test and what data backs each decision. This is a concept-level overview, not a test spec. We show the "what" and "why," not the "how." The client can then review or swap ideas before we invest effort building the actual tests.

## Step 1: Collect Inputs

Ask the user for:

1. **Client name, roadmap file, and data audit.** List the markdown files in the brand's folder under `brands/[brand-name]/` and let them pick the roadmap and data audit. The data audit is required for the Data Insights tab. If only one of each exists, confirm them.
2. **Homepage screenshot.** Ask the user to paste or provide a screenshot of the client's homepage. This is required both as a visual reference and as the default branded picture used in the hero. Use it to extract:
   - Primary brand color (hex)
   - Secondary/accent color if present
   - Overall visual style (light/dark, minimal/bold)
   - **Typography style**: condensed vs. regular weight, uppercase vs. mixed case, geometric vs. humanist, serif vs. sans-serif. Match the brand's typographic character while preserving strong web readability.
3. **Hero brand image** (optional). Ask for a preferred product, lifestyle, campaign, or homepage image to feature in the hero. If none is provided, use the homepage screenshot as the hero picture. Do not replace the picture with a generic illustration, texture, gradient, or abstract decoration.
4. **Logo URL or logo file.** Prefer a transparent SVG or PNG. If no usable logo is available, render the brand name as text rather than using a broken or low-quality asset. Do not automatically invert or recolor a logo. Choose a hero treatment that preserves the logo's intended appearance.
5. **Estimated launch dates** (optional). Per-slot timelines, e.g., "2 weeks after confirmation". If not provided, omit the launch date UI.

## Step 2: Read and Analyze

- Read the selected roadmap markdown file and the data audit file.
- Analyze the homepage screenshot, hero brand image, and logo together to determine brand colors, visual tone, imagery treatment, and typography. Pay close attention to whether the brand uses serif or sans-serif fonts, condensed or regular weights, uppercase or mixed case. The roadmap's visual system must feel related to the brand, not like a generic skin applied afterward.
- Identify two or three repeatable brand cues to carry through the roadmap, such as corner shape, border treatment, type scale, image crop, label style, or restrained decorative motif. Use them consistently without imitating the storefront page-for-page.
- Identify the roadmap structure: does it have an Insights/What We Found section? How many slots? A/B tests vs dev projects?
- Identify the data audit structure: which data sources were collected, what are the key findings per source, and what are the cross-source themes?

## Step 3: Extract and Condense Content

From the roadmap, extract:

- **Title:** The month and year from the H1. If today's date is the 23rd or later and no source markdown title is available, default to next month's name (e.g., if today is April 25, title as May).
- **Executive summary:** If an Insights or "What We Found" section exists, condense it to 2-3 sentences max. Paint the general picture of the data: overall performance, the core problem, and the opportunity. No specific metrics or percentages. Lead with the situation, not the numbers. If no Insights section exists, synthesize a 1-2 sentence summary from the test hypotheses.
- **Per-slot cards:** For each slot, extract:
  - Slot number(s) (e.g., "Slot 1" or "Slots 1 & 2")
  - Test or project name (keep it to the component/page being tested, e.g., "Homepage Top 2 Folds" not "Homepage Hero + Fold 2 Restructure")
  - Type: "A/B Test" or the dev project type (e.g., "Custom Shopify App")
  - Page being tested. If the slot is for one specific canonical page, render the page label as a clickable link to that page. Use `target="_blank"` and `rel="noopener"`. If the source includes the exact page URL, use it. If the source only provides a generic homepage URL but the slot clearly names a single product, collection, landing page, blog post, or other specific page, locate the actual canonical URL from the data audit, screenshots, product/catalog exports, live site, or collected source files before generating the HTML. If no exact canonical URL can be verified, keep the page label as plain text. If the slot covers multiple pages, paths, funnels, page types, or surfaces, keep the page label as plain text.
  - A 2-3 sentence description focused on the data and why this component matters. Rules:
    1. Every factual claim must trace back to a specific data point in the data audit or internal roadmap. If you cannot point to the exact line in the source file, do not include the claim.
    2. Do NOT describe what we plan to change or how the test will work. Sell the problem and the opportunity, not the solution.
    3. Do NOT make claims about the current state of a page (e.g., "the gallery leads with X", "the description leads with Y") unless a screenshot or data audit explicitly documents it. If the state is unknown, say "this needs to be audited."
    4. Do NOT present general industry assertions as if they are client-specific data (e.g., "AI agents pull gallery images as primary product signals"). If you include an industry-level claim, frame it as such.
    5. Do NOT map data to categories the source doesn't support (e.g., clinical results to specific skin types when the study doesn't segment by skin type).
    6. Do NOT attribute intent or causation without evidence (e.g., "visitors are actively hunting for proof" when a traffic spike could have multiple causes).
    7. If a slot requires more data before scoping, say so explicitly. It is better to flag a gap than to fill it with assumptions.
    8. No source citations in the output, but every claim must be verifiable against the source files.
  - Estimated launch date: ask the user for each slot's estimated timeline (e.g., "2 weeks after confirmation", "3rd week after confirmation"). If not provided, omit.
**For the Data Insights tab, extract from the data audit:**

- **Data sources used:** A list of every data source that was collected (e.g., Shopify Analytics, Customer Surveys, Heatmaps, Reviews & UGC). These will be displayed as a visual grid before the insights. Name each source cleanly: "Reviews and UGC", "Page Speed Insights", "Site Screenshots" — no platform qualifiers (not "Reviews and UGC (Amazon)"), no tool versions, no collection dates (not "Page Speed Insights (Lighthouse 13.0.1, Mobile, April 2026)"). Do not include a "CRO Ebook" source chip or any reference to the ebook in the Data Insights tab. Community research is fine to include.
- **Per-source summaries:** For each data source, condense the findings into 2-4 bullet points. Keep only the most actionable and interesting insights. Drop routine metrics that don't tell a story. Lead with the finding, not the source name. Do not explain how the data was collected or what tool was used — just state what was found.
- **Biggest Killers of Conversion Rate:** If the data audit has a cross-source analysis section, condense the converging themes into a short list of 3-5 items. These are the highest-confidence patterns that appear across multiple sources. This section renders at the TOP of the Data Insights tab, before the data sources grid and per-source summaries.

The Data Insights tab should be insightful but scannable. A client should be able to read it in 2-3 minutes and understand the full data picture. No filler. Every bullet point should make them think "I didn't know that" or "that confirms what I suspected."

**Critical: Zero hallucination on the Data Insights tab.** Every metric, percentage, quote, and finding must come directly from the data audit file. Do not round, reframe, or embellish numbers. Do not infer trends the data doesn't explicitly show. Do not add context or claims that aren't in the audit. If a data source section in the audit is thin, the summary should be thin too. Before outputting, verify each bullet point against the exact text in the data audit. If you cannot find the source line, delete the bullet.

**Drop entirely from the Tests tab:**
- Variation descriptions (V1, V2, etc.)
- Briefs (design and dev specs)
- Data sections with source citations
- Mobile/desktop specifications
- Scheduling and sequencing notes
- Future Slot Candidates section
- Data Sources line
- Revenue potential lines and calculations

**Content rules:**
- No em dashes. Use periods, commas, or colons.
- Never mention approval, concepts for approval, approval status, requests for approval, or approval of any kind anywhere in the client-facing HTML. Present the roadmap as testing ideas for client review.
- Every word earns its place. No filler, no hedging, no fluff.
- Direct, active voice. Short sentences.
- **No bold text in body paragraphs.** Only headings and slot labels may be bold. Never bold a sentence or phrase inside a paragraph. This is a hard rule with no exceptions.
- When rendering subscription or auto-replenishment wireframes, preserve the full benefit-stack copy from the roadmap. Do not reduce broader subscriber-benefit language to only "Includes free shipping."

**Client-facing acquisition-source rules:**
- Do not expose internal ad indexing or campaign enumeration in the HTML. Never write labels like "Ad 1", "Ad 2", "Ad 3", "Meta Ad 3", "2 of 3 ads", "three ads", or similar ordinal/count language in slot descriptions, executive summaries, Data Insights bullets, SVG labels, or any other client-facing copy.
- The Data Insights tab may list "Meta Ads and Landing Pages" as a data source when that source was collected, but the findings must be summarized in plain client-facing terms such as "paid-social creative", "offer-focused traffic", "discount traffic", or "code-based offers".
- The Tests tab must not mention Meta ads, ad numbers, campaign numbers, or platform-specific ad labels. Use the customer-facing promise or traffic intent instead, e.g. "offer-focused paid traffic arrives with SWEET15" rather than "Meta Ad 3 promises SWEET15".
- If the source material uses ad numbers, translate them before writing the HTML. Keep the factual claim, remove the internal label.

## Step 4: Generate HTML

**IMPORTANT: Use the `/frontend-design` skill for visual design decisions.** Do not fall back on generic templates, system fonts, or safe defaults. Invoke the `frontend-design` skill before writing any CSS. Every roadmap must look like it was designed by a human for that specific brand, not generated from a template.

This command controls the roadmap's information architecture, Shopify requirements, readability, and quality checks. The frontend-design skill controls the brand-led visual expression within those boundaries.

### Brand-Led Design Direction

Use the homepage screenshot, hero picture, logo, brand colors, typography, and visual tone as the design inputs.

The result should share a consistent quality bar with the strongest roadmap outputs, but it should not look identical across brands. The agent has freedom to adapt:

- hero composition and image crop
- light or dark hero treatment
- brand-appropriate typefaces and type scale
- corner radius and card silhouette
- restrained shadows, borders, and surface treatments
- tab styling
- subtle decorative details that clearly come from the brand

Use that freedom deliberately. A playful consumer brand, a clinical wellness brand, and a premium minimalist brand should not receive the same visual design.

Maintain these quality anchors across every generation:

- clear visual hierarchy at normal laptop zoom
- restrained editorial polish rather than dashboard-like UI
- a small, coherent palette derived from the brand
- consistent spacing rhythm and component treatment
- strong contrast and readable supporting copy
- one primary visual idea per section
- no visual effect that competes with the roadmap content

Do not treat creativity as permission for random asymmetry, excessive motion, oversized decoration, ornamental gradients, or a different design language in every section. The roadmap should feel custom, composed, and presentation-ready.

### Hero Requirements

The hero is the main branded moment and must include a real brand picture.

- Feature the provided hero brand image. If none was provided, use the homepage screenshot.
- If using the homepage screenshot as the hero picture (no separate brand image provided), treat it as an editorial crop rather than a full-bleed background. Frame a meaningful portion of it, apply an overlay or surface alongside it, or use a split-layout composition. Do not stretch a UI screenshot across the full hero width.
- Use the picture as a full-bleed background, split-layout image, framed editorial crop, or another brand-appropriate composition.
- Apply an overlay, crop, or adjacent surface as needed so the roadmap title and summary remain highly readable.
- Include the logo when it improves the composition. Preserve its aspect ratio and intended colors.
- Include the roadmap label, brand name, month and year, short executive summary, and tab navigation.
- Do not place explanatory labels, captions, or internal notes on the hero image, such as "homepage visual reference", "hero image", "brand screenshot", or similar. These are production/client-facing pages, not annotated design drafts.
- Keep the hero purposeful. Do not add decorative metrics, test-count pills, fake UI previews, or visual clutter unless they communicate useful roadmap information and genuinely fit the brand.
- The picture must remain visible and meaningful on desktop and mobile. Do not hide it entirely behind an opaque overlay.

The rest of the page should support the hero rather than compete with it.

The output is Shopify-ready HTML that can be pasted directly into a Shopify page's custom HTML content area. No document wrappers (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`). The output starts with Google Fonts `<link>` tags, then `<style>`, then `<div id="cvrt-roadmap">`. No JavaScript. No `<meta>`, `<title>`, or `<link rel="icon">` tags.

Use `brands/vyper/march-2026-roadmap-shopify.html` as a reference for the correct Shopify structure.

### Shopify-Safe Assets

- Do not leave local filesystem paths or repo-relative asset paths in the final HTML.
- Use public Shopify/CDN URLs or embed assets as `data:` URIs.
- Prefer a self-contained asset over a broken reference.
- Prefer transparent SVG or PNG logos. Avoid white boxes, baked-in mattes, and visibly low-resolution assets.
- Do not automatically apply CSS filters to logos. Adapt the surrounding composition to the asset.

### Shopify-Safe CSS Scoping

All body content must be wrapped in `<div id="cvrt-roadmap">`. This allows the HTML to be pasted into a Shopify page without theme styles overriding the design.

**Full-bleed breakout.** The `#cvrt-roadmap` root must break out of Shopify's content container:
```css
#cvrt-roadmap {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
}
```

**No max-width containers on page wrappers.** Do not use `max-width` or `margin: 0 auto` on the overall content wrapper or tab content sections. The Shopify page's own container handles the outer width. Exception: individual slot cards should be constrained and centered — see slot card layout rules below.

**All CSS selectors must be prefixed with `#cvrt-roadmap`** and **all class names must be prefixed with `cvrt-`** to avoid collisions with Shopify theme classes (e.g., `#cvrt-roadmap .cvrt-hero`, `#cvrt-roadmap .cvrt-slot h3`). Common class names like `.hero`, `.footer`, `.content`, `.section`, `.slot` WILL collide with theme styles. The `cvrt-` prefix eliminates this entirely.

Add a reset block at the top of the `<style>` to strip inherited theme styles:
```css
#cvrt-roadmap,
#cvrt-roadmap *,
#cvrt-roadmap *::before,
#cvrt-roadmap *::after {
  margin: 0; padding: 0; box-sizing: border-box;
  font-family: inherit; line-height: inherit;
  letter-spacing: normal; text-transform: none;
}
#cvrt-roadmap h1, #cvrt-roadmap h2, #cvrt-roadmap h3,
#cvrt-roadmap p, #cvrt-roadmap span, #cvrt-roadmap div {
  font-family: inherit; font-size: inherit;
  font-weight: inherit; color: inherit;
  margin: 0; padding: 0;
}
```

When using `<ul>`, `<ol>`, or `<li>` for Data Insights or any other roadmap copy, also reset list styling and theme pseudo-elements inside `#cvrt-roadmap`. Shopify themes often add custom `li::before` markers, colored dashes, or decorative bullets that survive `list-style: none` and appear as tiny marks at the start of each point. Include scoped rules like:
```css
#cvrt-roadmap ul,
#cvrt-roadmap ol,
#cvrt-roadmap li {
  list-style: none;
}
#cvrt-roadmap li::marker {
  content: "";
}
#cvrt-roadmap .cvrt-killer-list li::before,
#cvrt-roadmap .cvrt-killer-list li::after,
#cvrt-roadmap .cvrt-source-list li::before,
#cvrt-roadmap .cvrt-source-list li::after {
  content: none !important;
  display: none !important;
}
```
Do not use decorative bullets, colored dashes, checkmarks, or single-character pseudo-elements before Data Insights list items unless the user explicitly asks for them.

### Structural Requirements

These are the content and layout requirements. The visual styling comes from the frontend-design skill and the brand's visual identity. Keep the structure stable enough to scan, but let the visual treatment vary with the brand.

**Content structure for each slot card:**
- Slot label and type badge (A/B test vs. dev project)
- Test name as a heading
- Page being tested. If this is one specific canonical page, make the page label a clickable link. If the roadmap gives only a generic homepage URL but the slot clearly names one specific page, verify the actual canonical URL from available sources before linking. If it references multiple pages, a funnel path, or a page type without one verified canonical URL, keep it plain text.
- Description (1-2 sentences)
- **SVG sketch illustration:** An inline SVG low-fidelity UX wireframe visualizing the real interface surface being tested. Use dashed strokes, muted tones, and the brand color as an accent, but prioritize product-design specificity over decorative illustration. The SVG should look like a designer's rough Figma wireframe for scoping the test, not a marketing icon or abstract concept diagram. It must represent what the slot actually changes (e.g., the product-card anatomy, offer stack, cart drawer, buy box, video upsell, quiz step, or PDP proof module). The SVG spans the full card width — do not cap it at 420px. Size the viewBox to make full use of the available width: more horizontal space means more detail, more readable labels, and better wireframe fidelity. Below the SVG, always add a small italic caption: "* Concept illustration only. Final design will differ." This prevents brand owners from confusing the sketch with a deliverable.
- Estimated launch date (if provided)

**SVG wireframe quality.** This is a hard quality bar. The SVG is a UX artifact, not decoration.
- Draw the actual UI surface named in the slot, not a symbolic representation of the idea. If the slot affects product cards, draw a product card with image area, title, rating, price, issue zone, and CTA. If it affects a PDP buy box, draw a buy box with title, rating, price, offer rows, selectors, purchase options, proof, and CTA. If it affects cart, draw the drawer, line item, savings/progress area, coupon input, total, and checkout CTA.
- For A/B tests, prefer a current-vs-variation composition. Show the before state and the proposed changed state side by side, unless the concept is better expressed as a funnel/path. Label them plainly, e.g., "Current" and "Variation".
- Make the changed zone visually obvious through a highlight, conflict marker, removed space, moved module, before/after alignment, or callout. The viewer should understand the delta in 3 seconds.
- Include 5-10 concrete UI elements from the roadmap, data audit, or screenshots. Use real labels, coupon codes, prices, ratings, selectors, CTA text, review counts, policy labels, error text, and friction points when they are documented. Examples: `DAYONE`, `DPR15`, `₹394`, `4.7 | 939`, `Add to Cart`, `Subscribe & Save`, `Select size`, `liquid render error`.
- Do not invent UI details. Every concrete label or metric in the SVG must be traceable to the roadmap, data audit, or provided screenshot. If the source does not document the current page state, use generic structural labels and mark the area as needing audit.
- Preserve component anatomy. Draw the page region as a real ecommerce component with believable hierarchy, spacing, and controls. Avoid generic boxes labeled "Product card", "PDP offer area", or "Buy box decision area" unless those labels sit inside a more detailed component drawing.
- Show the uncomfortable source-backed details. If the issue is a broken template error, draw the error line. If the issue is offer conflict, show the conflicting codes and a mismatch marker. If the issue is proof buried below selectors, show proof below the current stack and moved above the key decision area in the variation.
- Keep the wireframe low fidelity, but specific. Use simple rectangles, image placeholders, rows, toggles, dropdown chevrons, buttons, star rows, and module labels. Do not use polished product mockups, fake screenshots, abstract diagrams, ornamental icons, or decorative scenes.
- Brand styling is secondary inside the SVG. Use the brand accent to highlight the change, CTA, or variation state, but do not let brand styling replace accurate UX anatomy.
- Avoid over-dense microcopy. Specificity matters, but labels must remain readable during a client screen share. If there are too many elements, simplify the surrounding UI while preserving the changed zone and the most important real labels.

**SVG text readability.** The frontend-design skill owns visual style, but SVG text has specific rendering constraints that must be respected regardless of aesthetic direction:
- **Err on the side of bigger.** SVG text that looks fine at full zoom becomes unreadable during screen sharing. Prefer larger font sizes and a more spacious viewBox over cramming many elements into a tight space.
- Never apply opacity to text elements. Apply opacity to fills and shapes only — text always renders at full opacity.
- Ensure text has enough contrast against its background. Contrast is not optional.
- Text must not overlap strokes, decorative shapes, or other text.
- Prefer heavier font weights for SVG text. Thin weights at small sizes become unreadable.
- After composing each SVG, mentally check: would every label be readable on a laptop screen during a presentation? If not, increase font sizes and expand the viewBox before outputting.

**SVG caption.** The caption below each SVG ("* Concept illustration only. Final design will differ.") must always use black or near-black text. It is a disclaimer that needs to be readable, not decorative.

**SVG pre-planning.** Before writing each SVG, silently define:

1. the real page surface being changed
2. the exact proposed variation being presented to the client
3. whether the clearest composition is current-vs-variation, a path/funnel, or a single annotated component
4. the concrete source-backed UI labels, metrics, coupon codes, prices, ratings, selectors, CTAs, or error messages that should appear
5. the minimum surrounding UI needed to establish context
6. the most important visual change the viewer should notice first
7. a composition that is distinct from every other slot in this roadmap

Do not output this planning text. Use it to design the wireframe.

**SVG fit rules:**
- Leave real inner padding around labels. Edge-to-edge centering that only barely fits is not acceptable.
- If a label is longer than the available shape width, wrap it with separate `tspan` lines or rewrite it shorter.
- Never let one label extend into a neighboring card, frame, image area, or CTA shape.
- Never place text underneath another filled shape, badge, or card edge.
- If a shape cannot comfortably hold its label after wrapping, make the shape larger or move nearby elements.
- Prefer simple, roomy wireframes over dense compositions with crowded copy.
- If there is any doubt about fit, choose fewer labels and clearer spacing.
- For card-style SVG modules, reserve explicit vertical zones for image, title, proof row, and supporting label instead of stacking text freehand.
- When a card includes both a rating row and a benefit label, increase the card height or reduce copy before allowing the zones to collapse into each other.
- Do not let title text, star-rating text, and benefit text share the same vertical space budget unless every line still has comfortable separation.

**Page sections:** Branded hero with picture and tab navigation, Tests tab with Slot Cards, Data Insights tab, Footer (month and year only).

**Data Insights tab section order:** "Biggest Killers of Conversion Rate" first, then the data sources grid, then per-source summaries. Do not place the killers section at the bottom.

**Non-SVG page composition:**
- Keep tests and data insights as the two primary tabs.
- Place tab navigation inside or directly attached to the hero so the top of the page reads as one composed unit.
- Render slot cards as a vertical single-column sequence. Give each card a clear compact text area above the SVG area.
- Separate the text area from the SVG area through spacing, a neutral divider, or a surface change. The separation should be clear without overpowering the wireframe.
- Use moderate corner treatment, subtle depth, or crisp full-perimeter borders according to the brand. Apply the chosen card language consistently.
- Make the "Biggest Killers of Conversion Rate" block the strongest element in Data Insights. It may use a dark or high-contrast brand surface.
- Render data-source names as a clean, scannable grid before the per-source findings.
- Render per-source findings as full-width vertical blocks or another equally readable single-column treatment. Avoid cramped two-column reading layouts.
- Keep the footer minimal and quiet.

**Layout direction: desktop-first, presentation-ready.** This roadmap is built for desktop — screen sharing, client meetings, PDF handoffs. The `/frontend-design` skill makes all visual decisions, but it should be directed toward:
- Slot card body: text content stacked above the SVG wireframe. Single-column layout. The SVG sits below the description and spans the full card width, giving it maximum horizontal space for detail and readable labels.
- **Slot cards must be constrained and centered.** Use `max-width: 860px; margin-left: auto; margin-right: auto;` on each slot card. The text block should be further capped (e.g., `max-width: 640px`) so description lines wrap naturally into 4+ lines rather than stretching edge to edge.
- Condensed, information-dense layout. Avoid large blank gaps between sections. Every spacing decision should feel intentional, not padded out.
- No empty spacer elements. Whitespace comes from `padding` and `margin` on real elements, not from blank `div`s with fixed heights.
- The card should feel like a well-designed slide: easy to read at a glance, not spread thin across the viewport.

Mobile styles can collapse to single-column, but do not let mobile layout constraints drive the desktop design.

**Light content surfaces.** Slot-card copy areas, SVG areas, and long-form insight blocks must use light, high-contrast surfaces. The hero and the "Biggest Killers of Conversion Rate" block may use dark or image-led brand treatments.

**No one-sided accent borders. This is a hard rule.** Do not apply a colored border, stripe, or rule to a single edge of a card or container (e.g., a colored left stripe on a slot card, a single-side accent on the executive summary box, a bottom-only divider that looks decorative). Left-side borders in particular are the most recognizable AI design tic and will immediately read as template-generated. Use one of: (a) a consistent thin border on all four sides (1px, neutral grey or low-opacity brand tone), (b) a soft full-perimeter shadow with no border, or (c) no border at all, relying on whitespace and background contrast to separate sections. Pick one approach and apply it consistently across every card on the page. If in doubt, use no border.

**Responsive and print styles:** Include mobile breakpoints and print-friendly styles (no shadows, avoid page breaks inside cards).

## Avoid These Failure Modes

Do not introduce:

- a separate top header bar above the hero
- floating hero preview mockups
- decorative hero illustrations used as the primary hero image
- multicolumn slot cards
- pill-heavy app UI styling
- loud gradients
- dark body backgrounds
- generic startup landing page aesthetics
- footer copy beyond the minimal month and year

## Step 5: Save

Write the HTML file in the same brand folder as the source roadmap. The source roadmap filename should already include the brand-name prefix (e.g., `brands/froya/froya-march-2026-roadmap.md`), so the HTML output keeps the same name with a `.html` extension:
- If source is `brands/froya/froya-march-2026-roadmap.md`, save as `brands/froya/froya-march-2026-roadmap.html`
- If source is a versioned file like `froya-march-2026-roadmap-v2.md`, save as `froya-march-2026-roadmap-v2.html`
- If you encounter a legacy unprefixed source file (e.g., `brands/froya/march-2026-roadmap.md`), still prefix the HTML output (`brands/froya/froya-march-2026-roadmap.html`). The brand name comes from the folder name.

After saving, tell the user the file path so they can open it in a browser or save as PDF.

## Pre-Publish Checklist

Before saving, verify silently:
- [ ] No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags. Output starts with Google Fonts `<link>` tags
- [ ] `#cvrt-roadmap` has full-bleed breakout CSS
- [ ] No `max-width` or `margin: 0 auto` on page-level content wrappers or tab sections
- [ ] Slot cards are constrained to max-width 860px and centered (`margin-left: auto; margin-right: auto`)
- [ ] Slot card text column wraps into 4+ lines (not 1-2 long lines spanning the full viewport)
- [ ] ALL class names are prefixed with `cvrt-` in both CSS and HTML
- [ ] All CSS selectors use `#cvrt-roadmap .cvrt-*` pattern
- [ ] No `<meta>`, `<title>`, or favicon tags
- [ ] No em dashes anywhere in the output
- [ ] No variation descriptions, briefs, or source citations leaked through
- [ ] No revenue figures anywhere in the output
- [ ] Brand color from the screenshot is applied consistently
- [ ] The design visibly reflects the brand's imagery, typography, logo, palette, and visual character rather than only swapping an accent color
- [ ] The hero contains a real brand picture, and the picture remains meaningfully visible on desktop and mobile
- [ ] The hero image has no explanatory labels, captions, or internal notes such as "homepage visual reference"
- [ ] The logo is sharp, correctly proportioned, and readable without automatic inversion or a visible matte
- [ ] Hero title and summary remain readable over or beside the picture
- [ ] Tabs are inside or directly attached to the hero and read as part of the same composition
- [ ] No one-sided accent borders on ANY card or container. No left stripe, no right stripe, no single-edge rule of any kind. If in doubt, remove the border entirely
- [ ] No bold text inside body paragraphs. Bold is for headings and slot labels only. Scan the full output for `<strong>`, `<b>`, or `font-weight: bold` applied to paragraph text and remove it
- [ ] No JavaScript
- [ ] Executive summary is 2-3 sentences max, not a wall of text
- [ ] Each slot description is 1-2 sentences max
- [ ] Single-page slot labels with a verified canonical URL are clickable links using `target="_blank"` and `rel="noopener"`, including cases where the source roadmap used a generic homepage URL but the actual page can be verified from local data or the live site
- [ ] Each slot has an inline SVG low-fidelity UX wireframe that represents the real interface surface being tested
- [ ] Each A/B test SVG uses current-vs-variation unless a path/funnel composition communicates the change more clearly
- [ ] Each SVG preserves real component anatomy, e.g., product-card image/title/rating/price/CTA, PDP title/rating/price/offers/selectors/CTA, or cart line item/coupon/total/checkout
- [ ] Each SVG includes concrete source-backed UI details where documented: labels, coupon codes, prices, ratings, selectors, CTA text, error text, or friction points
- [ ] Each SVG makes the changed zone obvious within 3 seconds through a highlight, conflict marker, removed space, moved module, before/after alignment, or callout
- [ ] No SVG is merely a symbolic icon, abstract concept diagram, decorative scene, or generic box layout
- [ ] SVG labels like "Product card", "PDP offer area", or "Buy box decision area" are not used as substitutes for detailed component anatomy
- [ ] SVG sketches use dashed strokes and the brand accent color consistently
- [ ] SVG text: high contrast, full opacity, no overlapping elements, heavy enough weight to read at screen resolution
- [ ] SVG text is readable without zooming during a screen share — if any label looks small, increase font-size and expand the viewBox
- [ ] SVG caption ("* Concept illustration only. Final design will differ.") is black or near-black, not gray or muted
- [ ] Data Insights tab: "Biggest Killers of Conversion Rate" section appears at the top, before data sources and per-source findings
- [ ] "Biggest Killers of Conversion Rate" is the strongest visual block in Data Insights
- [ ] Data Insights lists have no theme-injected bullets, tiny colored dashes, checkmarks, or decorative `li::before` markers. Reset `ul`, `ol`, `li`, `li::marker`, and Data Insights list `li::before`/`li::after` inside `#cvrt-roadmap`
- [ ] Data sources are easy to scan, and per-source findings are not forced into cramped columns
- [ ] Slot cards: text above, SVG below (single column, SVG spans full card width)
- [ ] Slot cards share one coherent card language with clear separation between copy and SVG areas
- [ ] No empty spacer divs; whitespace comes from element padding/margin only
- [ ] Layout is tight and scannable on a standard laptop screen at 100% zoom
- [ ] Every image and logo uses a public URL or embedded `data:` URI. No local or repo-relative paths remain
- [ ] If a logo was provided, it renders visibly against the hero treatment
- [ ] If estimated launch dates were provided, each slot displays them
- [ ] Every factual claim in slot descriptions traces to a specific data point in the data audit or internal roadmap. No fabricated data, no misattributed quotes, no unsupported claims about current page state. NEVER hallucinate.

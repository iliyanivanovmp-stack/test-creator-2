---
name: roadmap-to-html-2
description: Convert a CRO roadmap markdown file into a branded, Shopify-ready HTML concept board with medium-fidelity branded interface mockups and concise, persuasive test explanations. Use when producing the upgraded V2 roadmap format where each SVG must reconstruct the client's real website surface and make the proposed experience tangible, rather than showing generic wireframe boxes.
---

You are converting a CRO testing roadmap from a detailed internal execution format into a branded, client-facing HTML concept pitch that can be pasted directly into a Shopify page. The HTML version is what the client sees. The markdown stays internal.

The goal: the client scans the HTML in 60 seconds, understands which pages/components we want to test, why each idea matters, and what the proposed customer experience would feel like. This is a concept-level overview, not a test spec. Show the problem, the reasoning, and the visible experience. Omit implementation instructions.

## Step 1: Collect Inputs

Ask the user for:

1. **Client name, roadmap file, and data audit.** List the markdown files in the brand's folder under `brands/[brand-name]/` and let them pick the roadmap and data audit. The data audit is required for the Data Insights tab. If only one of each exists, confirm them.
2. **Homepage screenshot.** Ask the user to paste or provide a screenshot of the client's homepage. This is required as a visual reference and serves as the hero fallback when no stronger brand-owned image is available. Use it to extract:
   - Primary brand color (hex)
   - Secondary/accent color if present
   - Overall visual style (light/dark, minimal/bold)
   - **Typography style**: condensed vs. regular weight, uppercase vs. mixed case, geometric vs. humanist, serif vs. sans-serif. Match the brand's typographic character while preserving strong web readability.
3. **Hero brand image** (optional). Ask for a preferred product, lifestyle, campaign, or homepage image to feature in the hero. If the user leaves the choice to you, run the hero-image selection process in Step 2. Use the homepage screenshot only as the fallback after inspecting better brand-owned candidates. Do not replace the picture with a generic illustration, texture, gradient, or abstract decoration.
4. **Logo URL or logo file.** Prefer a transparent SVG or PNG. If no usable logo is available, render the brand name as text rather than using a broken or low-quality asset. Do not automatically invert or recolor a logo. Choose a hero treatment that preserves the logo's intended appearance.
5. **Estimated launch dates** (optional). Per-slot timelines, e.g., "2 weeks after confirmation". If not provided, omit the launch date UI.

## Step 2: Read and Analyze

- Read the selected roadmap markdown file and the data audit file.
- Inspect every available screenshot for each tested surface, not only the homepage. Use PDP, collection, cart, checkout, popup, quiz, landing-page, and mobile screenshots when they exist.
- **Select the hero image before choosing the hero layout.** When the user does not provide a preferred image:
  1. Collect at least three brand-owned candidates when available. Inspect the live site's Open Graph or social-share image, campaign and lifestyle banners, theme hero assets, featured product photography, and the homepage screenshot.
  2. Open every candidate visually. Do not choose from filenames, HTML attributes, or dimensions alone.
  3. Rank candidates by: clear product or use-case relevance, complete and recognizable subject, sufficient resolution, compatibility with an editorial crop, useful negative space, and consistency with the brand.
  4. Prefer a purpose-built wide social-share, campaign, or lifestyle image over a vertical theme crop or full-page screenshot when it shows the product clearly and suits the roadmap hero.
  5. Reject images whose main subject will be cut off in the intended frame, whose baked-in text competes with the roadmap title, whose resolution is visibly weak, or whose subject does not represent the core product.
  6. Choose the hero composition from the winning image's aspect ratio. Use wide images in wide split or full-bleed frames. Use portrait images in narrower editorial frames. Never force a portrait asset into a wide landscape panel or a wide asset into a near-square crop.
  7. Record the intended desktop and mobile focal point and set `object-position` separately when needed.
  8. If no suitable brand-owned image exists or the live site cannot be inspected, use the homepage screenshot as an editorial crop.
- Analyze the homepage screenshot, hero brand image, and logo together to determine brand colors, visual tone, imagery treatment, and typography. Pay close attention to whether the brand uses serif or sans-serif fonts, condensed or regular weights, uppercase or mixed case. The roadmap's visual system must feel related to the brand, not like a generic skin applied afterward.
- Identify two or three repeatable brand cues to carry through the roadmap, such as corner shape, border treatment, type scale, image crop, label style, or restrained decorative motif. Use them consistently without imitating the storefront page-for-page.
- For every slot, identify the exact screenshot or source artifact that documents the current surface. Record its recognizable interface anatomy, real labels, product names, imagery, controls, colors, and hierarchy before designing the illustration.
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
  - A 2-3 sentence explanation using this sequence:
    1. State the concrete current-state tension, contradiction, or missed opportunity.
    2. Explain why it matters in plain language.
    3. State the proposed customer-facing experience in one concise sentence.

    This is concept explanation, not a build brief. The reader should understand both why the test exists and what visibly changes without receiving implementation specifications. Rules:
    1. Every factual claim must trace back to a specific data point in the data audit or internal roadmap. If you cannot point to the exact line in the source file, do not include the claim.
    2. Describe the proposed visible experience concretely. Do not include selectors, breakpoints, event logic, development steps, QA instructions, or design specifications.
    3. Do NOT make claims about the current state of a page (e.g., "the gallery leads with X", "the description leads with Y") unless a screenshot or data audit explicitly documents it. If the state is unknown, say "this needs to be audited."
    4. Do NOT present general industry assertions as if they are client-specific data (e.g., "AI agents pull gallery images as primary product signals"). If you include an industry-level claim, frame it as such.
    5. Do NOT map data to categories the source doesn't support (e.g., clinical results to specific skin types when the study doesn't segment by skin type).
    6. Do NOT attribute intent or causation without evidence (e.g., "visitors are actively hunting for proof" when a traffic spike could have multiple causes).
    7. If a slot requires more data before scoping, say so explicitly. It is better to flag a gap than to fill it with assumptions.
    8. No source citations in the output, but every claim must be verifiable against the source files.
    9. Prefer concrete nouns and verbs over abstract CRO language. Write "Flo asks the shopper to choose the protector size again" rather than "the recommendation introduces additional decision friction."
    10. Use contrast when the evidence supports it: "The popup says 30%. The footer says 10%." Follow with a short interpretation and the proposed experience.
  - Estimated launch date: ask the user for each slot's estimated timeline (e.g., "2 weeks after confirmation", "3rd week after confirmation"). If not provided, omit.
**For the Data Insights tab, extract from the data audit:**

- **Data sources used:** A list of every data source that was collected (e.g., Shopify Analytics, Customer Surveys, Heatmaps, Reviews & UGC). These will be displayed as a visual grid before the insights. Name each source cleanly: "Reviews and UGC", "Page Speed Insights", "Site Screenshots" — no platform qualifiers (not "Reviews and UGC (Amazon)"), no tool versions, no collection dates (not "Page Speed Insights (Lighthouse 13.0.1, Mobile, April 2026)"). Do not include a "CRO Ebook" source chip or any reference to the ebook in the Data Insights tab. Community research is fine to include.
- **Per-source summaries:** For each data source, condense the findings into 2-4 bullet points. Keep only the most actionable and interesting insights. Drop routine metrics that don't tell a story. Lead with the finding, not the source name. Do not explain how the data was collected or what tool was used — just state what was found.
- **Biggest Killers of Conversion Rate:** If the data audit has a cross-source analysis section, condense the converging themes into a short list of 3-5 items. These are the highest-confidence patterns that appear across multiple sources. This section renders at the TOP of the Data Insights tab, before the data sources grid and per-source summaries.

The Data Insights tab should be insightful but scannable. A client should be able to read it in 2-3 minutes and understand the full data picture. No filler. Every bullet point should make them think "I didn't know that" or "that confirms what I suspected."

**Critical: Zero hallucination on the Data Insights tab.** Every metric, percentage, quote, and finding must come directly from the data audit file. Do not round, reframe, or embellish numbers. Do not infer trends the data doesn't explicitly show. Do not add context or claims that aren't in the audit. If a data source section in the audit is thin, the summary should be thin too. Before outputting, verify each bullet point against the exact text in the data audit. If you cannot find the source line, delete the bullet.

**Drop entirely from the Tests tab:**
- Raw variation briefs and V1/V2 implementation descriptions. Keep only the one-sentence customer-facing explanation of the proposed experience.
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
- Prefer the rhythm: observable fact, plain-English interpretation, visible proposal.
- Let one memorable sentence carry the implication when justified, but do not become theatrical or salesy.
- **No bold text in body paragraphs.** Only headings and slot labels may be bold. Never bold a sentence or phrase inside a paragraph. This is a hard rule with no exceptions.
- When rendering subscription or auto-replenishment concept mockups, preserve the full benefit-stack copy from the roadmap. Do not reduce broader subscriber-benefit language to only "Includes free shipping."

**Client-facing acquisition-source rules:**
- Do not expose internal ad indexing or campaign enumeration in the HTML. Never write labels like "Ad 1", "Ad 2", "Ad 3", "Meta Ad 3", "2 of 3 ads", "three ads", or similar ordinal/count language in slot descriptions, executive summaries, Data Insights bullets, SVG labels, or any other client-facing copy.
- The Data Insights tab may list "Meta Ads and Landing Pages" as a data source when that source was collected, but the findings must be summarized in plain client-facing terms such as "paid-social creative", "offer-focused traffic", "discount traffic", or "code-based offers".
- The Tests tab must not mention Meta ads, ad numbers, campaign numbers, or platform-specific ad labels. Use the customer-facing promise or traffic intent instead, e.g. "offer-focused paid traffic arrives with SWEET15" rather than "Meta Ad 3 promises SWEET15".
- If the source material uses ad numbers, translate them before writing the HTML. Keep the factual claim, remove the internal label.

## Step 4: Generate HTML

**IMPORTANT: Use the `/frontend-design` skill for visual design decisions.** Do not fall back on generic templates, system fonts, or safe defaults. Invoke the `frontend-design` skill before writing any CSS. Every roadmap must look like it was designed by a human for that specific brand, not generated from a template.

This command controls the roadmap's information architecture, Shopify requirements, readability, and quality checks. The frontend-design skill controls the brand-led visual expression within those boundaries.

### V2 Quality Target

Treat every slot illustration as a miniature branded product mockup that explains the test.

The illustration must look like a simplified reconstruction of the client's real website, not a diagram documenting where boxes move. Aim for Dose-level visual specificity and explanatory clarity while preserving this skill's restraint: no evidence tables in the Tests tab, no long internal reasoning, no technical brief, and no tiny unreadable microcopy.

The client should be able to recognize their own interface and understand the proposed change within three seconds.

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

- Feature the provided hero brand image. If the user left the image choice open, use the highest-ranked candidate from the Step 2 selection process.
- If using the homepage screenshot as the hero picture (no separate brand image provided), treat it as an editorial crop rather than a full-bleed background. Frame a meaningful portion of it, apply an overlay or surface alongside it, or use a split-layout composition. Do not stretch a UI screenshot across the full hero width.
- Design the image frame around the source aspect ratio and focal point. The hero layout must preserve the product, person, vehicle, or other main subject without accidental cropping.
- Use the picture as a full-bleed background, split-layout image, framed editorial crop, or another brand-appropriate composition.
- Apply an overlay, crop, or adjacent surface as needed so the roadmap title and summary remain highly readable.
- Include the logo when it improves the composition. Preserve its aspect ratio and intended colors.
- Include the roadmap label, brand name, month and year, short executive summary, and tab navigation.
- Do not place explanatory labels, captions, or internal notes on the hero image, such as "homepage visual reference", "hero image", "brand screenshot", or similar. These are production/client-facing pages, not annotated design drafts.
- Keep the hero purposeful. Do not add decorative metrics, test-count pills, fake UI previews, or visual clutter unless they communicate useful roadmap information and genuinely fit the brand.
- The picture must remain visible and meaningful on desktop and mobile. Do not hide it entirely behind an opaque overlay.
- Render the completed hero at a standard laptop viewport and a mobile viewport before finalizing. If the main subject is cropped, too small, obscured, or visually secondary at either size, change the crop, frame proportions, `object-position`, or image candidate. Do not ship the first technically valid image.

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
- Description (2-3 concise sentences): current tension, why it matters, proposed visible experience
- **SVG concept mockup:** An inline SVG medium-fidelity, branded reconstruction of the real interface surface being tested. It must represent what the slot actually changes, such as product-card anatomy, offer stack, cart drawer, buy box, video upsell, quiz step, or PDP proof module. The SVG spans the full card width. Size the viewBox for detail and readable labels. Below the SVG, add a small italic caption that names the visual delta, followed by the disclaimer. Example: "* The protector is pre-matched to the mattress already in the cart. Concept illustration only. Final design will differ."
- Estimated launch date (if provided)

**SVG concept-mockup quality.** This is a hard quality bar. The SVG is both a UX artifact and a visual explanation.

- Reconstruct the actual UI surface named in the slot. If the slot affects product cards, draw recognizable cards with product imagery, real product names, rating, positioning, price, discount, criteria, and CTA. If it affects a PDP buy box, reproduce its recognizable title, gallery, switch, rating, price, offer messaging, selectors, purchase options, proof, and CTA. If it affects cart, reproduce the line item, thumbnail, configuration, savings, recommendation, subtotal, checkout CTA, and reassurance modules.
- Start from the documented current interface. Preserve its hierarchy, proportions, brand colors, corner treatment, typography character, button styling, image treatment, and recognizable controls. Simplify only what is outside the test's context.
- Use at least three recognizable brand or interface cues inside each SVG. Examples: logo treatment, product colors, orange selected states, distinctive buttons, serif offer headings, pale-blue reassurance panels, thumbnail style, icon treatment, or the actual storefront spacing rhythm.
- Use real documented copy wherever it fits: product names, offer language, coupon codes, prices, ratings, selectors, CTA text, review counts, policy labels, error text, and friction points. Do not replace known content with generic labels.
- When a screenshot exists, do not use placeholders such as `Hero image`, `Bedroom image`, `Gallery`, `Product content`, `Matched promise`, `Relevant proof line`, `Buy box`, or `Product card`. Draw a simplified visual representation of the documented content instead.
- Represent documented imagery with simplified vector artwork, clipped image crops, embedded data-URI assets, or public CDN assets. A mattress can look like a mattress; a bottle can look like a bottle; a product thumbnail can use the real product image. Do not use a blank rectangle with an image label when the source image is available.
- Reproduce logos accurately when a usable asset exists. If embedding the logo would create a broken or unsafe asset, use a carefully typeset brand name rather than an empty logo box.
- For A/B tests, default to a current-vs-variation composition, but choose the composition that best explains the idea. Use three-state comparisons, interaction sequences, funnels, scroll states, or one enlarged annotated component when those communicate the concept better.
- Make the changed zone obvious within three seconds. Preserve enough identical surrounding interface in current and variation states that the client can see exactly what changed.
- Draw the proposal, not a note about the proposal. Render `$27 off`, the email field, the gift, and the CTA instead of a box labeled `Improved offer`. Render the actual suitability rows instead of a box labeled `Suitability guide`.
- Use annotations sparingly and outside the reconstructed UI when possible. The interface itself should carry the explanation. An annotation must point to a visible interface detail, not substitute for drawing it.
- Show uncomfortable source-backed details. If the issue is a broken template error, render the error. If offers conflict, render both offers. If proof is buried, show its real current location and its proposed new location.
- Do not invent client facts, interface labels, prices, products, proof, or metrics. Every concrete detail must trace to the roadmap, audit, screenshot, or verified page. If the surface is undocumented, produce an honest generic concept state and say it needs visual confirmation.
- Keep the result medium fidelity. It should feel like a reduced-scale branded interface mockup, not a final production design and not a grey-box wireframe. Avoid photorealistic fabrication, decorative scenes, and unrelated illustration.
- Avoid a universal SVG template. Vary composition according to the idea while keeping the roadmap's overall visual system coherent.
- Avoid over-dense microcopy. Simplify surrounding UI before shrinking text. Preserve the changed zone and the most recognizable source-backed details.

**Visual reconstruction sequence.** Perform this sequence for every slot:

1. Open the exact source screenshot or asset for the tested surface.
2. List silently the interface regions visible in it from top to bottom.
3. Choose the 5-12 regions needed to make the surface recognizable.
4. Identify three or more brand cues to reproduce.
5. Reconstruct the current state first.
6. Duplicate or continue that visual language for the variation.
7. Change only the tested region unless the concept explicitly restructures the whole surface.
8. Remove any placeholder label that describes an element which could be drawn.
9. Check that the visual, slot title, and proposed-experience sentence all describe the same test.

**SVG text readability.** The frontend-design skill owns visual style, but SVG text has specific rendering constraints that must be respected regardless of aesthetic direction:
- **Err on the side of bigger.** SVG text that looks fine at full zoom becomes unreadable during screen sharing. Prefer larger font sizes and a more spacious viewBox over cramming many elements into a tight space.
- Never apply opacity to text elements. Apply opacity to fills and shapes only — text always renders at full opacity.
- Ensure text has enough contrast against its background. Contrast is not optional.
- Text must not overlap strokes, decorative shapes, or other text.
- Prefer heavier font weights for SVG text. Thin weights at small sizes become unreadable.
- After composing each SVG, mentally check: would every label be readable on a laptop screen during a presentation? If not, increase font sizes and expand the viewBox before outputting.

**SVG caption.** Use one short sentence to explain the visible delta, then add "Concept illustration only. Final design will differ." The caption must use black or near-black text.

**Responsive SVG composition.** Desktop and mobile require separate concept-mockup compositions. Do not make mobile users horizontally scroll, swipe, or pan to see the full concept.
- Keep the desktop SVG optimized for presentation and screen sharing. For A/B tests, current and variation may remain side by side.
- Add a dedicated mobile-only SVG for every slot. At the mobile breakpoint, hide the desktop SVG and show the mobile SVG.
- In mobile A/B concept mockups, stack "Current" or "Control" first and "Variation" second in one vertical flow. Use a downward arrow or another clear vertical transition cue between them.
- For single-state fixes or projects, stack the problem state above the corrected or proposed state when both are shown. If only one state is needed, use a narrow mobile composition that fits fully within the viewport.
- Preserve the same source-backed labels, metrics, component anatomy, changed zone, and disclaimer across desktop and mobile. The mobile version may simplify surrounding UI, but it must not omit the evidence or interface detail needed to understand the concept.
- Mobile SVG text must remain readable without zooming. Use a mobile-specific viewBox and larger relative type rather than scaling the desktop canvas down.
- The mobile concept mockup must fit the slot card width with `width: 100%` and `min-width: 0`. Never use a large `min-width`, horizontal overflow, or an overflow container as a substitute for a responsive composition.
- Keep the desktop view visually unchanged when adding the mobile composition. Scope all visibility and layout switching to the mobile media query.

**SVG pre-planning.** Before writing each SVG, silently define:

1. the real page surface being changed
2. the exact proposed variation being presented to the client
3. whether the clearest composition is current-vs-variation, a path/funnel, or a single annotated component
4. the concrete source-backed UI labels, metrics, coupon codes, prices, ratings, selectors, CTAs, or error messages that should appear
5. the exact screenshot or asset used as the reconstruction reference
6. the brand cues and recognizable interface anatomy that must survive simplification
7. the minimum surrounding UI needed to establish context
8. the most important visual change the viewer should notice first
9. a composition that is distinct from every other slot in this roadmap

Do not output this planning text. Use it to design the concept mockup.

**SVG fit rules:**
- Leave real inner padding around labels. Edge-to-edge centering that only barely fits is not acceptable.
- If a label is longer than the available shape width, wrap it with separate `tspan` lines or rewrite it shorter.
- Never let one label extend into a neighboring card, frame, image area, or CTA shape.
- Never place text underneath another filled shape, badge, or card edge.
- If a shape cannot comfortably hold its label after wrapping, make the shape larger or move nearby elements.
- Prefer roomy concept mockups over dense compositions with crowded copy.
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
- Separate the text area from the SVG area through spacing, a neutral divider, or a surface change. The separation should be clear without overpowering the concept mockup.
- Use moderate corner treatment, subtle depth, or crisp full-perimeter borders according to the brand. Apply the chosen card language consistently.
- Make the "Biggest Killers of Conversion Rate" block the strongest element in Data Insights. It may use a dark or high-contrast brand surface.
- Render data-source names as a clean, scannable grid before the per-source findings.
- Render per-source findings as full-width vertical blocks or another equally readable single-column treatment. Avoid cramped two-column reading layouts.
- Keep the footer minimal and quiet.

**Layout direction: desktop-first, presentation-ready.** This roadmap is built for desktop — screen sharing, client meetings, PDF handoffs. The `/frontend-design` skill makes all visual decisions, but it should be directed toward:
- Slot card body: text content stacked above the SVG concept mockup. Single-column layout. The SVG sits below the description and spans the full card width, giving it maximum horizontal space for detail and readable labels.
- **Slot cards must be constrained and centered.** Use `max-width: 860px; margin-left: auto; margin-right: auto;` on each slot card. The text block should be further capped (e.g., `max-width: 640px`) so description lines wrap naturally into 4+ lines rather than stretching edge to edge.
- Condensed, information-dense layout. Avoid large blank gaps between sections. Every spacing decision should feel intentional, not padded out.
- No empty spacer elements. Whitespace comes from `padding` and `margin` on real elements, not from blank `div`s with fixed heights.
- The card should feel like a well-designed slide: easy to read at a glance, not spread thin across the viewport.

Mobile styles must collapse to a single vertical reading flow without horizontal swiping. Current or control appears above the variation in mobile concept mockups. Do not let mobile layout constraints alter the desktop design.

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
- repeated grey-box SVG templates
- blank image rectangles labeled with what the image should contain
- generic labels used in place of documented interface content
- a different brand expressed only by changing one accent color
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
- [ ] No raw variation briefs, implementation specifications, or source citations leaked through
- [ ] No revenue figures anywhere in the output
- [ ] Brand color from the screenshot is applied consistently
- [ ] The design visibly reflects the brand's imagery, typography, logo, palette, and visual character rather than only swapping an accent color
- [ ] The hero contains a real brand picture, and the picture remains meaningfully visible on desktop and mobile
- [ ] When the user left the hero choice open, at least three brand-owned candidates were visually inspected when available, including the live site's social-share or Open Graph image
- [ ] The chosen image was selected for product relevance, composition, resolution, and crop compatibility, not from its filename or availability alone
- [ ] The hero frame matches the source image aspect ratio closely enough to preserve the main subject
- [ ] The desktop and mobile hero renders were visually checked, and the subject remains recognizable without accidental cropping
- [ ] The hero image has no explanatory labels, captions, or internal notes such as "homepage visual reference"
- [ ] The logo is sharp, correctly proportioned, and readable without automatic inversion or a visible matte
- [ ] Hero title and summary remain readable over or beside the picture
- [ ] Tabs are inside or directly attached to the hero and read as part of the same composition
- [ ] No one-sided accent borders on ANY card or container. No left stripe, no right stripe, no single-edge rule of any kind. If in doubt, remove the border entirely
- [ ] No bold text inside body paragraphs. Bold is for headings and slot labels only. Scan the full output for `<strong>`, `<b>`, or `font-weight: bold` applied to paragraph text and remove it
- [ ] No JavaScript
- [ ] Executive summary is 2-3 sentences max, not a wall of text
- [ ] Each slot description is 2-3 concise sentences: current tension, why it matters, proposed visible experience
- [ ] Single-page slot labels with a verified canonical URL are clickable links using `target="_blank"` and `rel="noopener"`, including cases where the source roadmap used a generic homepage URL but the actual page can be verified from local data or the live site
- [ ] Each slot has an inline SVG medium-fidelity branded concept mockup that reconstructs the real interface surface being tested
- [ ] Each A/B test SVG uses current-vs-variation unless a path/funnel composition communicates the change more clearly
- [ ] Each SVG preserves real component anatomy, e.g., product-card image/title/rating/price/CTA, PDP title/rating/price/offers/selectors/CTA, or cart line item/coupon/total/checkout
- [ ] Each SVG includes concrete source-backed UI details where documented: labels, coupon codes, prices, ratings, selectors, CTA text, error text, or friction points
- [ ] Each SVG reproduces at least three recognizable brand/interface cues from the source surface
- [ ] Each SVG was designed from the exact relevant screenshot or source asset when one exists
- [ ] Known imagery is represented visually with vector artwork, a clipped crop, an embedded asset, or a public asset, not a blank labeled rectangle
- [ ] Each SVG makes the changed zone obvious within 3 seconds through a highlight, conflict marker, removed space, moved module, before/after alignment, or callout
- [ ] No SVG is merely a symbolic icon, abstract concept diagram, decorative scene, or generic box layout
- [ ] Placeholder labels such as "Hero image", "Gallery", "Product content", "Matched promise", "Product card", or "Buy box" are absent when the documented element can be drawn
- [ ] The current and variation states look like the same branded interface, with the tested region visibly changed
- [ ] SVG styling uses the client's typography character, palette, control shapes, imagery treatment, and UI hierarchy rather than a universal grey wireframe system
- [ ] SVG text: high contrast, full opacity, no overlapping elements, heavy enough weight to read at screen resolution
- [ ] SVG text is readable without zooming during a screen share — if any label looks small, increase font-size and expand the viewBox
- [ ] SVG caption explains the visible delta, includes "Concept illustration only. Final design will differ.", and is black or near-black
- [ ] Every slot has a dedicated mobile SVG composition, not a scaled-down or horizontally scrollable desktop SVG
- [ ] Mobile A/B concept mockups stack Current or Control above Variation in one vertical flow
- [ ] Mobile single-state or fix concept mockups fit fully within the slot card width without swiping
- [ ] Mobile SVG text and concrete labels remain readable without zooming
- [ ] Mobile concept-mockup containers use `width: 100%` and `min-width: 0`, with no large `min-width` or horizontal overflow
- [ ] Desktop SVG composition and desktop layout remain unchanged by the mobile implementation
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

---
description: Convert a CRO roadmap markdown file into a branded, Shopify-ready HTML one-pager for clients
---

You are converting a CRO testing roadmap from a detailed internal execution format into a branded, client-facing HTML concept pitch that can be pasted directly into a Shopify page. The HTML version is what the client sees. The markdown stays internal.

The goal: the client scans the HTML in 60 seconds, understands which pages/components we want to test and what data backs each decision. This is a concept-level overview, not a test spec. We show the "what" and "why," not the "how." The client can then approve, reject, or swap concepts before we invest effort building the actual tests.

## Step 1: Collect Inputs

Ask the user for:

1. **Client name, roadmap file, and data audit.** List the markdown files in the brand's folder under `brands/[brand-name]/` and let them pick the roadmap and data audit. The data audit is required for the Data Insights tab. If only one of each exists, confirm them.
2. **Homepage screenshot.** Ask the user to paste or provide a screenshot of the client's homepage. Use this to extract:
   - Primary brand color (hex)
   - Secondary/accent color if present
   - Overall visual style (light/dark, minimal/bold)
   - **Typography style**: condensed vs. regular weight, uppercase vs. mixed case, geometric vs. humanist. **Always use sans-serif fonts for web readability**, regardless of whether the brand's own site uses serifs. Match the brand's weight, proportions, and overall character (e.g., industrial brands get bold condensed sans-serif, minimalist brands get clean geometric sans-serif), but never ship a serif-based body or heading font in the roadmap.
3. **Logo URL** (optional). A URL to the client's logo image. If not provided, skip the logo in the header. If provided, invert the logo for visibility on dark hero backgrounds using `filter: brightness(0) invert(1)`.
4. **Estimated launch dates** (optional). Per-slot timelines, e.g., "2 weeks after confirmation". If not provided, omit the launch date UI.

## Step 2: Read and Analyze

- Read the selected roadmap markdown file and the data audit file.
- Analyze the homepage screenshot to determine brand colors, visual tone, and typography. Pay close attention to whether the brand uses serif or sans-serif fonts, condensed or regular weights, uppercase or mixed case. The roadmap's font choices must follow the brand's typographic structure, not default to a generic pairing.
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
  - Page being tested
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

- **Data sources used:** A list of every data source that was collected (e.g., Shopify Analytics, Customer Surveys, Heatmaps, Reviews & UGC). These will be displayed as a visual grid before the insights.
- **Per-source summaries:** For each data source, condense the findings into 2-4 bullet points. Keep only the most actionable and interesting insights. Drop routine metrics that don't tell a story. Lead with the finding, not the source name.
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
- Every word earns its place. No filler, no hedging, no fluff.
- Direct, active voice. Short sentences.

## Step 4: Generate HTML

**IMPORTANT: Use the `/frontend-design` skill for all visual design decisions.** Do not fall back on generic templates, system fonts, or safe defaults. The frontend-design skill defines the design quality bar. Read and follow `.claude/commands/frontend-design.md` before writing any CSS. Every roadmap must look like it was designed by a human for that specific brand, not generated from a template.

The homepage screenshot, brand colors, and visual tone are the design inputs. The frontend-design skill provides the design approach.

The output is Shopify-ready HTML that can be pasted directly into a Shopify page's custom HTML content area. No document wrappers (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`). The output starts with Google Fonts `<link>` tags, then `<style>`, then `<div id="cvrt-roadmap">`. No JavaScript. No `<meta>`, `<title>`, or `<link rel="icon">` tags.

Use `brands/vyper/march-2026-roadmap-shopify.html` as a reference for the correct Shopify structure.

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

### Structural Requirements

These are the content and layout requirements. The visual styling (fonts, colors, spacing, shadows, decorative elements) comes from the frontend-design skill and the brand's visual identity.

**Content structure for each slot card:**
- Slot label and type badge (A/B test vs. dev project)
- Test name as a heading
- Page being tested
- Description (1-2 sentences)
- **SVG sketch illustration:** An inline SVG pencil-sketch wireframe visualizing the concept. Use dashed strokes, muted tones, and the brand color as an accent. The sketch should represent what the slot actually does (e.g., a video player wireframe for a video upsell, a cart drawer wireframe for a cart test). Keep the style loose and hand-drawn: dashed borders, light or no fills, rounded rects. Max-width 420px, viewBox sized to content. Below the SVG, always add a small italic caption: "* Concept illustration only. Final design will differ." This prevents brand owners from confusing the sketch with a deliverable.
- Estimated launch date (if provided)

**SVG text readability.** The frontend-design skill owns visual style, but SVG text has specific rendering constraints that must be respected regardless of aesthetic direction:
- **Err on the side of bigger.** SVG text that looks fine at full zoom becomes unreadable during screen sharing. Prefer larger font sizes and a more spacious viewBox over cramming many elements into a tight space.
- Never apply opacity to text elements. Apply opacity to fills and shapes only — text always renders at full opacity.
- Ensure text has enough contrast against its background. Contrast is not optional.
- Text must not overlap strokes, decorative shapes, or other text.
- Prefer heavier font weights for SVG text. Thin weights at small sizes become unreadable.
- After composing each SVG, mentally check: would every label be readable on a laptop screen during a presentation? If not, increase font sizes and expand the viewBox before outputting.

**SVG caption.** The caption below each SVG ("* Concept illustration only. Final design will differ.") must always use black or near-black text. It is a disclaimer that needs to be readable, not decorative.

**Page sections:** Header (with logo if provided), Executive Summary, Slot Cards (single column, one per row), Footer (month and year only).

**Data Insights tab section order:** "Biggest Killers of Conversion Rate" first, then the data sources grid, then per-source summaries. Do not place the killers section at the bottom.

**Layout direction: desktop-first, presentation-ready.** This roadmap is built for desktop — screen sharing, client meetings, PDF handoffs. The `/frontend-design` skill makes all visual decisions, but it should be directed toward:
- Slot card body: text content on the left, SVG wireframe on the right. Two-column layout. The SVG column should be fixed-width (around 300px) to anchor the illustration; the text column takes remaining space but is capped so lines wrap naturally.
- **Slot cards must be constrained and centered.** Use `max-width: 760px; margin-left: auto; margin-right: auto;` on each slot card. This prevents the text column from stretching across the full viewport, which collapses descriptions into 1-2 long lines. The goal is 4+ lines of wrapped text so the card feels dense and readable, not spread thin.
- Condensed, information-dense layout. Avoid large blank gaps between sections. Every spacing decision should feel intentional, not padded out.
- Wide text columns that force long lines make cards harder to scan during a presentation. The 760px card max-width enforces this constraint automatically.
- No empty spacer elements. Whitespace comes from `padding` and `margin` on real elements, not from blank `div`s with fixed heights.
- The card should feel like a well-designed slide: easy to read at a glance, not spread thin across the viewport.

Mobile styles can collapse to single-column, but do not let mobile layout constraints drive the desktop design.

**Light backgrounds only.** SVG sketches and text readability depend on light backgrounds. The brand color should be used as an accent, not as a background fill.

**No one-sided accent borders.** Do not apply a colored border, stripe, or rule to a single edge of a card or container (e.g., a colored left stripe on a slot card, a single-side accent on the executive summary box). This is a generic AI design tic and reads as cheap. Use one of: (a) a consistent thin border on all four sides (1px, neutral grey or low-opacity brand tone), (b) a soft full-perimeter shadow with no border, or (c) no border at all, relying on whitespace and background contrast to separate sections. Pick one approach and apply it consistently across every card on the page.

**Responsive and print styles:** Include mobile breakpoints and print-friendly styles (no shadows, avoid page breaks inside cards).

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
- [ ] Slot cards are constrained to max-width 760px and centered (`margin-left: auto; margin-right: auto`)
- [ ] Slot card text column wraps into 4+ lines (not 1-2 long lines spanning the full viewport)
- [ ] ALL class names are prefixed with `cvrt-` in both CSS and HTML
- [ ] All CSS selectors use `#cvrt-roadmap .cvrt-*` pattern
- [ ] No `<meta>`, `<title>`, or favicon tags
- [ ] No em dashes anywhere in the output
- [ ] No variation descriptions, briefs, or source citations leaked through
- [ ] No revenue figures anywhere in the output
- [ ] Brand color from the screenshot is applied consistently
- [ ] No one-sided accent borders on cards or containers (no left stripe, no single-edge rule). Borders are either full-perimeter or absent
- [ ] No JavaScript
- [ ] Executive summary is 2-3 sentences max, not a wall of text
- [ ] Each slot description is 1-2 sentences max
- [ ] Each slot has an inline SVG sketch illustration that visually represents the concept
- [ ] SVG sketches use dashed strokes and the brand accent color consistently
- [ ] SVG text: high contrast, full opacity, no overlapping elements, heavy enough weight to read at screen resolution
- [ ] SVG text is readable without zooming during a screen share — if any label looks small, increase font-size and expand the viewBox
- [ ] SVG caption ("* Concept illustration only. Final design will differ.") is black or near-black, not gray or muted
- [ ] Data Insights tab: "Biggest Killers of Conversion Rate" section appears at the top, before data sources and per-source findings
- [ ] Slot cards: text left, SVG right (two-column layout, SVG column fixed-width)
- [ ] No empty spacer divs; whitespace comes from element padding/margin only
- [ ] Layout is tight and scannable on a standard laptop screen at 100% zoom
- [ ] If logo URL was provided, it renders visibly against the header background
- [ ] If estimated launch dates were provided, each slot displays them
- [ ] Every factual claim in slot descriptions traces to a specific data point in the data audit or internal roadmap. No fabricated data, no misattributed quotes, no unsupported claims about current page state. NEVER hallucinate.

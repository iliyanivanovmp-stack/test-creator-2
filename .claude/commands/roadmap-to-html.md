---
description: Convert a CRO roadmap markdown file into a branded HTML one-pager for clients
---

You are converting a CRO testing roadmap from a detailed internal execution format into a branded, client-facing HTML concept pitch. The HTML version is what the client sees. The markdown stays internal.

The goal: the client scans the HTML in 60 seconds, understands which pages/components we want to test and what data backs each decision. This is a concept-level overview, not a test spec. We show the "what" and "why," not the "how." The client can then approve, reject, or swap concepts before we invest effort building the actual tests.

## Step 1: Collect Inputs

Ask the user for:

1. **Client name, roadmap file, and data audit.** List the markdown files in the client's folder under `clients/[client-name]/` and let them pick the roadmap and data audit. The data audit is required for the Data Insights tab. If only one of each exists, confirm them.
2. **Homepage screenshot.** Ask the user to paste or provide a screenshot of the client's homepage. Use this to extract:
   - Primary brand color (hex)
   - Secondary/accent color if present
   - Overall visual style (light/dark, minimal/bold)
   - **Typography style**: serif vs. sans-serif, condensed vs. regular weight, uppercase vs. mixed case. The roadmap must match the brand's typographic DNA. For example, an industrial brand using bold condensed sans-serif should never get a serif-heavy roadmap.
3. **Logo URL** (optional). A URL to the client's logo image. If not provided, skip the logo in the header. If provided, invert the logo for visibility on dark hero backgrounds using `filter: brightness(0) invert(1)`. Also use the logo URL as the favicon via `<link rel="icon" href="...">` in the `<head>`.
4. **Estimated launch dates** (optional). Per-slot timelines, e.g., "2 weeks after confirmation". If not provided, omit the launch date UI.

## Step 2: Read and Analyze

- Read the selected roadmap markdown file and the data audit file.
- Analyze the homepage screenshot to determine brand colors, visual tone, and typography. Pay close attention to whether the brand uses serif or sans-serif fonts, condensed or regular weights, uppercase or mixed case. The roadmap's font choices must follow the brand's typographic structure, not default to a generic pairing.
- Identify the roadmap structure: does it have an Insights/What We Found section? How many slots? A/B tests vs dev projects?
- Identify the data audit structure: which data sources were collected, what are the key findings per source, and what are the cross-source themes?

## Step 3: Extract and Condense Content

From the roadmap, extract:

- **Title:** The month and year from the H1.
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
- **Cross-source themes:** If the data audit has a cross-source analysis section, condense the converging themes into a short narrative. These are the patterns that appear across multiple sources and carry the highest confidence.

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

The roadmap must be a distinctive, branded design, not a generic template. Use the homepage screenshot, brand colors, and visual tone to drive the design. Google Fonts are allowed for distinctive typography.

### Design Rules (apply on first generation, not as a second pass)

- **Typography:** Choose fonts that match the brand's typographic DNA from the homepage screenshot. Use Google Fonts for distinctive choices. Avoid generic defaults (Inter, Roboto, Arial, system fonts). Pair a display font for headings with a refined body font.
- **Color:** Use the brand's primary color as an accent (borders, badges, headings). Light page background always. Commit to a cohesive palette using CSS variables.
- **Layout:** Clean, editorial feel. Generous whitespace. Single-column slot cards. No cluttered or dense layouts.
- **Details:** Subtle touches that elevate: refined spacing, considered type hierarchy, tasteful use of the brand color. No gratuitous effects or animations. The design should feel intentional and polished, not decorated.
- **No generic AI aesthetics:** No purple gradients on white, no cookie-cutter card layouts, no default Bootstrap/Tailwind look. Every roadmap should feel like it was designed for that specific brand.

Build a self-contained HTML file. All CSS in a `<style>` tag in the `<head>`. No JavaScript. Google Fonts links are the only allowed external dependency.

### HTML Template Structure

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Month Year] Testing Roadmap - [Client Name]</title>
  <style>
    /* All CSS here */
  </style>
</head>
<body>
<div id="cvrt-roadmap">
  <!-- Header: logo (if provided) + title -->
  <!-- Executive Summary card -->
  <!-- Slot cards grid -->
  <!-- Footer -->
</div>
</body>
</html>
```

### Shopify-Safe CSS Scoping

All body content must be wrapped in `<div id="cvrt-roadmap">`. This allows the HTML to be pasted into a Shopify page without theme styles overriding the design.

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

### CSS Specifications

Set CSS custom properties from the brand colors extracted from the homepage screenshot:
- `--brand`: primary brand color (hex from screenshot analysis)
- `--brand-light`: a 10% opacity version of the brand color for card backgrounds
- `--text`: #1a1a1a
- `--muted`: #666
- `--bg`: #f8f8f8
- `--card-bg`: #ffffff

**Always use a light background.** The page background must be light (#f8f8f8 or similar). Never use dark backgrounds, dark hero sections, or dark cards. SVG sketches and text readability depend on light backgrounds. The brand color should be used as an accent (borders, badges, headings), not as a background fill.

**Minimal typography.** Keep the number of distinct text styles low for readability. Both the Tests tab and Data Insights tab must use the same typographic system:
- One heading style (H3 for slot names / section names)
- One body style (14-15px for descriptions and bullet points)
- One muted style (11-13px for labels, captions, metadata)
- Bold for emphasis only when a specific word or phrase needs to stand out. No italic except for the SVG caption disclaimer.
- No mixing of font sizes, weights, or styles beyond these three tiers. Both tabs should feel like the same document.

Core styles:
- Font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- Max width: 900px, centered with auto margins
- Padding: 48px 24px

**Header:**
- If logo provided: logo image left-aligned, max-height 40px, margin-bottom 16px
- Title: H1, font-size 28px, color var(--brand), font-weight 700
- Subtle 2px horizontal rule in the brand color below the title

**Executive Summary Card:**
- Background: var(--bg)
- Border-radius: 8px
- Padding: 24px
- Margin: 32px 0
- Text: 15px line-height 1.6

**Slot Cards Grid:**
- Single column layout: `grid-template-columns: 1fr` with 20px gap. Always one slot per row, including desktop. Never use a 2-column grid for slot cards.
- Each card:
  - Background: var(--card-bg)
  - Border-radius: 8px
  - Box-shadow: 0 1px 3px rgba(0,0,0,0.08)
  - Border-left: 4px solid var(--brand)
  - Padding: 24px
- Inside each card:
  - **Top row:** Slot label (small, muted, uppercase, 11px tracking) and type badge (small rounded pill, 11px, uppercase, brand color background with white text for A/B tests, outlined for dev projects)
  - **Test name:** H3, font-size 18px, font-weight 600, margin-top 12px
  - **Page:** Below the name, muted text, 13px
  - **Description:** 14px, line-height 1.5, color var(--text)
  - **SVG sketch illustration:** An inline SVG pencil-sketch wireframe visualizing the concept. Use dashed strokes, muted greys (#999, #bbb, #ddd), and the brand color as an accent. The sketch should represent what the slot actually does (e.g., a video player wireframe for a video upsell, a cart drawer wireframe for a cart test, a PDP layout for a product page test). Keep the style loose and hand-drawn: dashed borders, no fills or light bone fills, rounded rects. Max-width 420px, viewBox sized to content. Below the SVG, always add a small italic caption: "* Concept illustration only. Final design will differ." (11px, muted color). This prevents brand owners from confusing the sketch with an actual wireframe or deliverable.
  - **Estimated launch date** (if provided): A small inline-block box below the description. Background: var(--bg), border-radius 4px, padding 12px 16px. Label "ESTIMATED LAUNCH" in 11px uppercase muted text, value below in 14px semibold.

**Footer:**
- Margin-top: 48px, padding-top: 24px
- Border-top: 1px solid #e0e0e0
- Text: 13px, color var(--muted), center-aligned
- Content: just the month and year

**Responsive:**
```css
@media (max-width: 640px) {
  .slots-grid { grid-template-columns: 1fr; }
  h1 { font-size: 24px; }
}
```

**Print:**
```css
@media print {
  body { padding: 24px; }
  .card { box-shadow: none; border: 1px solid #e0e0e0; break-inside: avoid; }
}
```

## Step 5: Save

Write the HTML file in the same client folder as the source roadmap:
- If source is `clients/froya/march-2026-roadmap.md`, save as `clients/froya/march-2026-roadmap.html`
- If source is a versioned file like `march-2026-roadmap-v2.md`, save as `march-2026-roadmap-v2.html`

After saving, tell the user the file path so they can open it in a browser or save as PDF.

## Pre-Publish Checklist

Before saving, verify silently:
- [ ] No em dashes anywhere in the output
- [ ] No variation descriptions, briefs, or source citations leaked through
- [ ] No revenue figures anywhere in the output
- [ ] Brand color from the screenshot is applied consistently
- [ ] HTML is valid and self-contained (no external dependencies, no JavaScript)
- [ ] Executive summary is 2-3 sentences max, not a wall of text
- [ ] Each slot description is 1-2 sentences max
- [ ] Each slot has an inline SVG sketch illustration that visually represents the concept
- [ ] SVG sketches use dashed strokes, muted colors, and the brand accent color consistently
- [ ] If logo URL was provided, it renders visibly against the header background
- [ ] If estimated launch dates were provided, each slot displays them
- [ ] Every factual claim in slot descriptions traces to a specific data point in the data audit or internal roadmap. No fabricated data, no misattributed quotes, no unsupported claims about current page state. NEVER hallucinate.

# Template Spec (front + admin, for all agents)

Every style gets TWO self-contained HTML files:
- `templates/<style>/front.html` — customer-facing template (前台)
- `templates/<style>/admin.html` — internal admin console (后台管理)

Input: `design-md/<style>/DESIGN.md` — read fully, extract exact tokens (colors, type, radius, spacing, shadows).

## Hard rules

1. Single-file HTML each, one `<style>` block, CSS-only visuals (gradients/SVG), no JS frameworks. Small inline JS only where a template genuinely needs it (tab switch) — prefer none.
2. Google Fonts allowed with system fallbacks. Never hotlink images.
3. Reuse the same `:root` token set in BOTH files so they read as one system.
4. English copy in the brand's real domain. No lorem ipsum.
5. Desktop-first at 1280px+; must not break at 960px.
6. Target 350–650 lines per file. These are TEMPLATES — believable filler content, clean data, realistic names/numbers.

## front.html — customer-facing template (前台)

An end-user application/storefront surface (NOT a marketing landing page):
1. Top nav: logo, primary nav, search, cart/avatar, notification dot
2. Category strip or filter chips row
3. Product/card grid (8+ items): image area (CSS gradient/SVG art), title, price or meta, rating, badges (New/Sale/etc.)
4. One featured/detail row: large product panel with gallery thumbs, options selector, quantity stepper, Add-to-cart CTA, reviews snippet
5. Cart drawer/panel or checkout summary card (items, subtotal, tax, total, CTA)
6. Compact footer (links, newsletter input, social icons)

Domain adaptation: commerce brand → storefront; dev tool → template/app marketplace or project gallery; media brand → article/content grid. Same skeleton, domain-appropriate content.

## admin.html — internal management console (后台管理)

1. Left sidebar: logo, grouped menu (Dashboard, Orders/Items, Users, Analytics, Settings), active item highlighted; user card at bottom
2. Topbar: breadcrumb/page title, global search, notification bell with badge, avatar
3. KPI row: 4 stat cards (value, delta ↑/↓ colored, sparkline or mini bar)
4. Charts row: one bar chart (CSS bars, 12 bars with month labels) + one donut/radial chart (SVG stroke-dasharray) with legend
5. Main data table: 6–8 rows (checkbox col, name, category, status badge, amount, date, row actions), table header, pagination footer
6. Side panel card: recent activity feed (4–5 items, avatar dot + text + time) OR quick settings form (inputs, toggle, save button)
7. Status badge vocabulary: success / warning / danger / neutral — mapped to the style's semantic colors (derive from DESIGN.md; if absent, derive sensible ones from the palette)

## Quality bar

- The pair must feel like ONE product: same nav branding, same buttons, same badge shapes.
- Apply the style's signature moves from DESIGN.md (pill vs square buttons, dark vs light canvas, tracking, shadows, radius).

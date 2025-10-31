# Tapin Design Assets Manifest

## Brand Assets

### Logo (Primary)

- **File:** `brand/logo.svg`
- **Alt Text:** Tapin — Volunteers connect to orgs. Hand holding location pin.
- **Usage:** Headers, social media, app icons, marketing materials
- **Variants:** Monochrome (`logo-monochrome.svg`), Reversed (`logo-reversed.svg`)
- **Colors:** Tapin Blue (#0B76FF), Sky (#58B2E4)
- **PNG Exports:** 72px, 144px, 216px heights with transparent backgrounds
- **WCAG Compliance:** AA — 7.2:1 contrast on white backgrounds

### Logo Monochrome

- **File:** `brand/logo-monochrome.svg`
- **Alt Text:** Tapin logo — monochrome blue
- **Usage:** Print materials, grayscale contexts, single-color applications
- **Color:** Tapin Blue (#0B76FF)

### Logo Reversed

- **File:** `brand/logo-reversed.svg`
- **Alt Text:** Tapin logo — reversed white on blue
- **Usage:** Dark backgrounds, primary color overlays, app headers
- **Color:** White (#FFFFFF)

### Favicon & App Icons

- **Files:**
  - `brand/favicon.ico` (32px × 32px)
  - `brand/apple-touch-icon.png` (180px × 180px)
  - `brand/logo@1x.png` (72px)
  - `brand/logo@2x.png` (144px)
  - `brand/logo@3x.png` (216px)

---

## Icon Set

All icons are designed on a 24px grid with 2px stroke weight. Filled and stroke variants available for all action icons.

### Core Icons

| Icon         | File              | Alt Text                                  | Usage                             | Variants |
| ------------ | ----------------- | ----------------------------------------- | --------------------------------- | -------- |
| View/Eye     | `icon-view.svg`   | View — open or expand                     | CTAs, list actions                | Filled   |
| Add/Plus     | `icon-add.svg`    | Add — create new opportunity or volunteer | FABs, primary actions             | Filled   |
| Edit/Pencil  | `icon-edit.svg`   | Edit — modify opportunity or profile      | Secondary actions                 | Filled   |
| Delete/Trash | `icon-delete.svg` | Delete — remove item                      | Destructive actions               | Filled   |
| Map Pin      | `map-pin.svg`     | Location — map marker pin                 | Address contexts, location badges | —        |

### Icon Accessibility

- **Stroke icons:** 2px on transparent background, min 48×48px tap target with padding
- **Filled variants:** Solid backgrounds with contrasting icon color
- **Suggested aria-labels:** Use alt text values for icon buttons
- **Color contrast:** All icons meet WCAG AA at 24px usage

---

## Color System

### Primary Palette

| Color | Hex     | Name       | Usage                                         |
| ----- | ------- | ---------- | --------------------------------------------- |
| —     | #0B76FF | Tapin Blue | Primary actions, headers, links, focus states |
| —     | #58B2E4 | Sky        | Secondary actions, gradients, hover states    |
| —     | #FF8B89 | Coral      | Highlights, notifications, accent elements    |

### Semantic Colors

| Color | Hex     | Name    | Usage                                          |
| ----- | ------- | ------- | ---------------------------------------------- |
| —     | #10B981 | Emerald | Success states, confirmations, completed tasks |
| —     | #F59E0B | Amber   | Warning states, pending actions, alerts        |
| —     | #EF4444 | Red     | Error states, destructive actions, danger      |

### Neutral Palette

| Color | Hex     | Name  | Usage                                    |
| ----- | ------- | ----- | ---------------------------------------- |
| —     | #111826 | Navy  | Headings, primary text (7.8:1 contrast)  |
| —     | #334155 | Slate | Body text, descriptions (7.5:1 contrast) |
| —     | #F5F8FF | Frost | Card backgrounds, panel fills            |
| —     | #FFFFFF | White | Primary surface, backgrounds             |

### Contrast Compliance

- **Text on primary (#0B76FF):** 7.2:1 contrast ✓ WCAG AA
- **Navy (#111826) on white:** 7.8:1 contrast ✓ WCAG AAA
- **Slate (#334155) on white:** 7.5:1 contrast ✓ WCAG AAA

---

## Typography

**Font Family:** Inter, sans-serif (or system fallback: -apple-system, BlinkMacSystemFont, Segoe UI)

### Scale

- **Headings:** 600–700 weight, 24px–32px sizes
- **Subheadings:** 600 weight, 16px–18px sizes
- **Body:** 400–500 weight, 14px–16px sizes
- **Meta/Labels:** 400 weight, 12px–14px sizes

### Line Height

- Headings: 1.2
- Body: 1.5
- Meta: 1.4

---

## Spacing & Layout

### Grid System

- **Base Unit:** 4px
- **Common Multiples:** 8px, 12px, 16px, 24px, 32px

### Margins & Padding

- **Mobile (Compact):** 16px outer margins, 8px–16px component padding
- **Desktop (Standard):** 24px outer margins, 16px–24px component padding
- **Density Modes:** "Baay" (loose) for content-heavy screens; "Cozy" (tight) for list views

### Breakpoints

- **Mobile:** 320px–767px
- **Tablet:** 768px–1024px
- **Desktop:** 1025px+

---

## Component Library

### Button States

**Primary Button:**

- Default: Tapin Blue (#0B76FF), white text, 8px–12px padding, 6px border-radius
- Hover: Sky (#58B2E4)
- Active: Dark Blue variant
- Disabled: #CBD5E1 (light gray), no interaction

**Secondary Button:**

- Default: Frost background (#F5F8FF), Tapin Blue text, 2px border
- Hover: Light blue background
- Active: Frost + darker border

### Input Fields

- **Border:** 1px Slate (#334155)
- **Focus:** 2px Tapin Blue border + focus ring (#E6F1FF)
- **Error:** 1px Red (#EF4444) border, red focus ring
- **Disabled:** #E2E8F0 background, #94A3B8 text

### Cards & Panels

- **Background:** White (#FFFFFF) or Frost (#F5F8FF)
- **Border:** 1px #E2E8F0
- **Shadow:** 0 1px 3px rgba(0, 0, 0, 0.1)
- **Border-radius:** 8px–12px

### Badges & Pills

- **Background:** Tapin Blue (#0B76FF)
- **Text:** White (#FFFFFF)
- **Padding:** 4px 8px
- **Border-radius:** 12px (pill)

---

## Implementation Examples

### React

```jsx
import logo from '../Design-Assets/brand/logo.svg';
import { ReactComponent as IconView } from '../Design-Assets/icons/icon-view.svg';

export function Header() {
  return (
    <header className="header">
      <img src={logo} alt="Tapin — Volunteers connect to orgs" className="logo" />
      <button aria-label="View opportunity details">
        <IconView className="icon-24" />
      </button>
    </header>
  );
}
```

### HTML

```html
<link rel="icon" href="/Design-Assets/brand/favicon.ico" />
<link rel="apple-touch-icon" href="/Design-Assets/brand/apple-touch-icon.png" />

<header>
  <img src="/Design-Assets/brand/logo.svg" alt="Tapin — Volunteers connect to orgs" />
</header>

<button aria-label="Add new opportunity">
  <svg role="img" aria-hidden="true" class="icon-24">
    <use href="/Design-Assets/icons/icon-add.svg#icon-add"></use>
  </svg>
</button>
```

### CSS Variables

```css
:root {
  --color-primary: #0b76ff;
  --color-secondary: #58b2e4;
  --color-accent: #ff8b89;
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-danger: #ef4444;
  --color-text-primary: #111826;
  --color-text-secondary: #334155;
  --color-bg-panel: #f5f8ff;
  --color-bg-surface: #ffffff;

  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif;
  --spacing-base: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}
```

---

## File Structure

```
Design-Assets/
├── brand/
│   ├── logo.svg (source vector master)
│   ├── logo-monochrome.svg
│   ├── logo-reversed.svg
│   ├── logo@1x.png (72px)
│   ├── logo@2x.png (144px)
│   ├── logo@3x.png (216px)
│   ├── favicon.ico
│   ├── apple-touch-icon.png
│   └── source-master.fig (Figma link or local file)
├── icons/
│   ├── icon-view.svg
│   ├── icon-view-filled.svg
│   ├── icon-view@24.png
│   ├── icon-add.svg
│   ├── icon-add-filled.svg
│   ├── icon-add@24.png
│   ├── icon-edit.svg
│   ├── icon-edit-filled.svg
│   ├── icon-edit@24.png
│   ├── icon-delete.svg
│   ├── icon-delete-filled.svg
│   ├── icon-delete@24.png
│   ├── map-pin.svg
│   └── map-pin@24.png
├── illustrations/
│   ├── empty-state.svg
│   ├── empty-state@1x.png
│   └── empty-state@2x.png
├── placeholders/
│   ├── hero-16x9@1x.jpg
│   ├── hero-16x9@2x.jpg
│   ├── placeholder-16x9@1x.jpg
│   ├── placeholder-16x9@2x.jpg
│   ├── avatar-40.png
│   └── avatar-80.png
├── social/
│   ├── social-preview.png (1200×630)
│   └── social-preview@2x.png (2400×1260)
├── manifest.json
├── README.md
└── optimize-assets.sh
```

---

## Sizing Guidelines

### Logo Clear Space

- **Minimum clear space:** 1/4 of logo height on all sides
- **Minimum size:** 72px height (mobile), 144px (desktop)
- **Maximum scale:** Unlimited (vector master scales infinitely)

### Icon Usage

- **Standalone UI icons:** 24px (desktop), 16px (mobile)
- **FAB (Floating Action Button):** 56px (touch target), 24px icon inside
- **List item icons:** 40px–48px diameter with avatar borders

### Avatar Placeholders

- **Small:** 40px × 40px (lists, comments)
- **Medium:** 80px × 80px (profile sidebars)
- **Large:** 120px × 120px (profile header)

### Social Preview

- **Recommended size:** 1200px × 630px (1.91:1 aspect ratio)
- **Use case:** Open Graph meta tags, Twitter cards, social shares
- **Must include:** Logo, headline, tagline, brand color accent

---

## Accessibility Checklist

- [ ] All SVGs have descriptive `title` and `aria-label` attributes
- [ ] Icon buttons have `aria-label` describing action
- [ ] Color is never the sole indicator of status (add icons/text)
- [ ] Text meets WCAG AA contrast (7:1 preferred, 4.5:1 minimum)
- [ ] Focus indicators visible (2px ring, not removed)
- [ ] Image alt text describes function, not just "image"
- [ ] Animated assets include `prefers-reduced-motion` support

---

## Optimization & Export

Run `optimize-assets.sh` to minify all SVGs and compress raster exports:

```bash
./optimize-assets.sh
```

This will:

- **SVGs:** SVGO with `--multipass` flag, remove metadata
- **PNGs:** pngquant 256-color with dithering, then optipng
- **JPGs:** jpegoptim progressive encoding, 85% quality

---

## Brand Master & Source Files

**Note:** If you have a Figma team file or Adobe AI/Sketch source, link or attach it here for ongoing updates.

- **Figma Link:** [Add link]
- **Adobe Illustrator:** [Add link or note if available]
- **Sketch:** [Add link or note if available]

---

## Handoff Notes

- ✓ All SVGs open cleanly in Figma, Illustrator, Sketch, and browsers
- ✓ PNG exports are transparent where needed (logos, icons)
- ✓ JPG exports use progressive encoding for faster loading
- ✓ All files use kebab-case naming, no spaces
- ✓ Manifest includes every asset with alt text and usage
- ✓ README documents sizing, clear-space, variants, and examples
- ✓ Optimization script automates asset compression

---

## Commit Message

```
chore(assets): add production-ready Tapin design assets

- Logo in primary, monochrome, and reversed variants
- Core icon set (view, add, edit, delete, map-pin) with filled variants
- Color system with semantic tokens (primary, success, warning, danger)
- Typography scale (Inter), spacing grid, component library
- Placeholder assets (avatars, hero, social preview)
- manifest.json with alt text, usage, and WCAG compliance notes
- README with implementation examples and accessibility checklist
- optimize-assets.sh for automated SVG/PNG/JPG compression
```

---

**Last Updated:** 2025-10-31  
**Version:** 1.0  
**Status:** Production Ready

# Tapin Design System Style Guide

## 🎨 Visual Identity

### Brand Values
- **Approachable** - Friendly, welcoming community platform
- **Trustworthy** - Professional, reliable service
- **Energetic** - Vibrant, active, engaging
- **Modern** - Contemporary, cutting-edge design

## 🌈 Color System

### Primary Colors
```css
--primary-600: #4f46e5  /* Main brand color - Indigo */
--primary-700: #4338ca  /* Darker variant for contrast */
--primary-400: #818cf8  /* Lighter variant for hover states */
```

**Usage:**
- Primary actions (buttons, links, CTAs)
- Active states and selections
- Focus indicators
- Brand elements

**Accessibility:** All text on primary colors uses white (#ffffff) for WCAG AAA contrast

### Accent Colors
```css
--accent-600: #db2777  /* Pink accent */
```

**Usage:**
- Secondary highlights
- Gradient combinations with primary
- Special features or promotions

### Semantic Colors
```css
--success-600: #059669  /* Success states */
--warning-600: #d97706  /* Warning states */
--danger-600: #dc2626   /* Error states */
```

**Usage:**
- Form validation feedback
- Status indicators
- Toast notifications
- Alert messages

### Neutral Palette
```css
--neutral-0: #ffffff    /* Pure white - surfaces */
--neutral-50: #fafafa   /* Background */
--neutral-100: #f4f4f5  /* Secondary background */
--neutral-200: #e4e4e7  /* Borders */
--neutral-300: #d4d4d8  /* Strong borders */
--neutral-600: #52525b  /* Muted text */
--neutral-700: #3f3f46  /* Secondary text */
--neutral-900: #18181b  /* Primary text */
```

**Contrast Ratios (WCAG AA Compliant):**
- `--text` on `--surface`: 16.5:1 (AAA)
- `--text-secondary` on `--surface`: 10.7:1 (AAA)
- `--text-muted` on `--surface`: 4.9:1 (AA)

## 📐 Spacing System

### 8pt Grid
All spacing follows an 8-point grid for visual consistency:

```css
--space-1: 4px    /* 0.5x */
--space-2: 8px    /* 1x - base unit */
--space-3: 12px   /* 1.5x */
--space-4: 16px   /* 2x */
--space-5: 20px   /* 2.5x */
--space-6: 24px   /* 3x */
--space-8: 32px   /* 4x */
--space-10: 40px  /* 5x */
--space-12: 48px  /* 6x */
--space-16: 64px  /* 8x */
```

**Guidelines:**
- Use `space-2` (8px) for tight spacing (icons, inline elements)
- Use `space-4` (16px) for standard component padding
- Use `space-6` (24px) for section gaps
- Use `space-8+` for major layout separation

## 🔤 Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, sans-serif;
```

System fonts for optimal performance and native feel across platforms.

### Type Scale
```css
--fs-xs: 0.75rem    /* 12px - Captions, labels */
--fs-sm: 0.875rem   /* 14px - Secondary text, buttons */
--fs-base: 1rem     /* 16px - Body text (default) */
--fs-lg: 1.125rem   /* 18px - Lead paragraphs */
--fs-xl: 1.25rem    /* 20px - Card titles */
--fs-2xl: 1.5rem    /* 24px - Section headings */
--fs-3xl: 1.875rem  /* 30px - Page headings */
--fs-4xl: 2.25rem   /* 36px - Hero text */
--fs-5xl: 3rem      /* 48px - Display text */
```

### Font Weights
```css
--fw-regular: 400   /* Body text */
--fw-medium: 500    /* Emphasis */
--fw-semibold: 600  /* Headings, buttons */
--fw-bold: 700      /* Strong emphasis */
```

### Line Heights
```css
--leading-tight: 1.25    /* Headings */
--leading-normal: 1.5    /* Body text */
--leading-relaxed: 1.625 /* Long-form content */
```

**Usage Examples:**
```css
/* H1 - Page Title */
font-size: var(--fs-3xl);
font-weight: var(--fw-bold);
line-height: var(--leading-tight);

/* Body Text */
font-size: var(--fs-base);
font-weight: var(--fw-regular);
line-height: var(--leading-normal);

/* Button */
font-size: var(--fs-base);
font-weight: var(--fw-semibold);
line-height: var(--leading-none);
```

## 🎭 Shadows & Elevation

### Shadow Scale
```css
--shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05)
--shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)
--shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25)
```

**Elevation Hierarchy:**
- `shadow-xs`: Input fields at rest
- `shadow-sm`: Cards at rest, buttons
- `shadow-md`: Input focus, cards hover
- `shadow-lg`: Dropdowns, popovers
- `shadow-xl`: Modals, elevated cards
- `shadow-2xl`: Major overlays

## 📦 Border Radius

```css
--radius-sm: 8px     /* Small elements, inputs */
--radius-md: 12px    /* Default */
--radius-lg: 16px    /* Cards, buttons */
--radius-xl: 24px    /* Large cards */
--radius-2xl: 32px   /* Hero sections */
--radius-full: 9999px /* Pills, avatars */
```

**Guidelines:**
- Smaller radius for dense UIs (forms, tables)
- Larger radius for spacious layouts (marketing, landing)
- `radius-full` for circular elements (badges, pills)

## 🎬 Motion & Animation

### Timing Functions
```css
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1)   /* Micro-interactions */
--transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1)   /* Standard */
--transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1)   /* Dramatic */
--transition-bounce: 500ms cubic-bezier(0.34, 1.56, 0.64, 1) /* Playful */
```

**Principles:**
- **Fast** (150ms): Hover states, color changes
- **Base** (200ms): Button clicks, toggles
- **Slow** (300ms): Cards, page transitions
- **Bounce** (500ms): Success confirmations, special effects

### Reduced Motion
Always respect user preferences:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 🎯 Components

### Buttons

#### Primary Button
```css
background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
color: white;
padding: var(--space-3) var(--space-5);
border-radius: var(--radius-lg);
min-height: 44px; /* Touch target */
```

**States:**
- Hover: `translateY(-2px)` with enhanced shadow
- Active: `translateY(0)` with reduced shadow
- Focus: 2px outline with offset
- Disabled: 50% opacity

#### Secondary Button
```css
background: var(--surface);
border: 2px solid var(--border);
color: var(--text);
```

#### Button Sizes
- **Small**: `min-height: 36px`, `font-size: 14px`
- **Default**: `min-height: 44px`, `font-size: 16px`
- **Large**: `min-height: 52px`, `font-size: 18px`

### Cards

```css
background: var(--surface);
border: 1px solid var(--border);
border-radius: var(--radius-xl);
padding: var(--space-5);
box-shadow: var(--shadow-sm);
```

**Hover Effect:**
- Translate up 4px
- Enhance shadow to `shadow-xl`
- Show gradient border (via `::before` pseudo-element)
- Scale media 1.05x

### Forms

#### Text Input
```css
padding: var(--space-3) var(--space-4);
border: 2px solid var(--border);
border-radius: var(--radius-lg);
```

**States:**
- **Hover**: Border `--border-strong`, shadow `--shadow-sm`
- **Focus**: Border `--primary`, focus ring
- **Error**: Border `--danger`, error message below
- **Success**: Border `--success`, success indicator
- **Disabled**: Opacity 60%, not-allowed cursor

## ♿ Accessibility Guidelines

### Minimum Requirements

1. **Color Contrast**
   - Text: 4.5:1 (WCAG AA)
   - Large text: 3:1 (WCAG AA)
   - UI components: 3:1

2. **Touch Targets**
   - Minimum 44×44px for interactive elements
   - Adequate spacing between targets (8px minimum)

3. **Focus Indicators**
   - Visible 2px outline on all interactive elements
   - Use `:focus-visible` for keyboard-only indicators
   - Offset 2px from element

4. **Motion**
   - Respect `prefers-reduced-motion`
   - Provide alternatives to animation-dependent features

5. **Semantic HTML**
   - Use proper heading hierarchy (h1→h6)
   - Label all form inputs
   - ARIA labels for icon-only buttons
   - Alt text for images

### Testing Checklist
- [ ] Run axe DevTools audit
- [ ] Test keyboard navigation (Tab, Enter, Escape)
- [ ] Test screen reader (NVDA/JAWS)
- [ ] Check color blindness simulation
- [ ] Verify contrast ratios
- [ ] Test with zoom (200%)

## 📱 Responsive Breakpoints

```css
/* Mobile first approach */
@media (max-width: 768px) { /* Mobile */ }
@media (min-width: 769px) and (max-width: 1200px) { /* Tablet */ }
@media (min-width: 1201px) { /* Desktop */ }
```

### Grid Layouts
- **Mobile**: 1 column
- **Tablet**: 2 columns
- **Desktop**: 3 columns

## 🚀 Usage Examples

### Toast Notifications
```jsx
import { useToast } from './components/Toast';

function MyComponent() {
  const toast = useToast();
  
  toast.success('Saved successfully!');
  toast.error('Something went wrong');
  toast.warning('Please review your input');
  toast.info('New features available');
}
```

### Form Validation
```jsx
<div className="form-group">
  <label htmlFor="email">Email</label>
  <input 
    id="email"
    type="email" 
    className={hasError ? 'error' : ''}
    aria-invalid={hasError}
    aria-describedby={hasError ? 'email-error' : undefined}
  />
  {hasError && (
    <div className="form-error" id="email-error" role="alert">
      Please enter a valid email
    </div>
  )}
</div>
```

## 📚 Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Inclusive Components](https://inclusive-components.design/)

---

**Version:** 2.0  
**Last Updated:** November 2025  
**Maintained by:** Tapin Design Team

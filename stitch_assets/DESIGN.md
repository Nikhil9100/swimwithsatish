---
name: SwimWithSatish Elite
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#363a3d'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c1f'
  surface-container: '#1c2023'
  surface-container-high: '#262a2e'
  surface-container-highest: '#313538'
  on-surface: '#e0e3e7'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e0e3e7'
  inverse-on-surface: '#2d3134'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bbc7df'
  primary: '#bbc7df'
  on-primary: '#253144'
  primary-container: '#0a1628'
  on-primary-container: '#758096'
  inverse-primary: '#535f74'
  secondary: '#a2e7ff'
  on-secondary: '#003642'
  secondary-container: '#00d2fd'
  on-secondary-container: '#005669'
  tertiary: '#ffb955'
  on-tertiary: '#452b00'
  tertiary-container: '#221300'
  on-tertiary-container: '#b07300'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d7e3fc'
  primary-fixed-dim: '#bbc7df'
  on-primary-fixed: '#101c2e'
  on-primary-fixed-variant: '#3c475b'
  secondary-fixed: '#b4ebff'
  secondary-fixed-dim: '#3cd7ff'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#ffddb4'
  tertiary-fixed-dim: '#ffb955'
  on-tertiary-fixed: '#291800'
  on-tertiary-fixed-variant: '#633f00'
  background: '#101417'
  on-background: '#e0e3e7'
  surface-variant: '#313538'
typography:
  display-lg:
    fontFamily: Bebas Neue
    fontSize: 80px
    fontWeight: '400'
    lineHeight: 80px
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: Bebas Neue
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: 0.02em
  headline-lg-mobile:
    fontFamily: Bebas Neue
    fontSize: 36px
    fontWeight: '400'
    lineHeight: 36px
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Bebas Neue
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: 0.03em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 20px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style

The design system is engineered to evoke the high-performance atmosphere of elite competitive swimming. It balances the authority of a professional coaching institution with the kinetic energy of the water. The aesthetic leans into **Modern Athleticism**, utilizing high-contrast typography, deep tonal layering, and vibrant "electric" accents to guide the athlete’s journey.

The brand personality is **Elite yet Accessible**. It avoids the clutter of amateur sports apps in favor of a sleek, focused interface that mirrors the precision of a stopwatch. Visual depth is achieved through subtle gradients that mimic light refracting through deep water, while high-intensity gold accents ensure that calls-to-action feel urgent and rewarding.

## Colors

The palette is optimized for a premium dark-mode experience, ensuring maximum visual impact for athletic photography and performance data.

- **Primary (Deep Navy):** The foundation. Used for all main backgrounds and structural surfaces to provide a sense of depth and stability.
- **Secondary (Electric Aqua):** The pulse. Used for progress indicators, active states, and iconography. It represents movement and the aquatic environment.
- **Tertiary (Warm Gold):** The achievement. Reserved strictly for primary CTAs and high-value conversion points, symbolizing the "gold standard" of coaching.
- **Surface & Text:** Typography utilizes a pure white for high-priority headlines and an off-white (#F4F7FB) for body text to reduce eye strain against the dark navy backgrounds.

## Typography

Typography in the design system is a study in contrast. Headlines use a bold, condensed aesthetic to command attention and convey strength, while the body text remains highly functional and modern.

- **Headlines:** Always in all-caps. The condensed nature allows for high-impact messaging even on narrow mobile screens.
- **Body Text:** Set in a neutral, highly legible sans-serif. Leading is generous to ensure coaching instructions are easy to read during active workouts.
- **Labels:** Utilize heavy weights and slight letter spacing to create a technical, "instrument-panel" feel for data points and metrics.

## Layout & Spacing

This design system employs a **Fluid Grid** model built on an 8px rhythmic scale. 

- **Desktop:** 12-column grid with 24px gutters and 40px outer margins. Content blocks should feel expansive and professional.
- **Mobile:** 4-column grid with 16px margins. 
- **Rhythm:** Vertical rhythm is strictly enforced. Spacing between major sections (80px) emphasizes the "premium" feel by allowing elements to breathe. Component-level spacing (8px/16px) ensures a tight, disciplined UI.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layering** and **Subtle Glows**.

1.  **Base Layer:** Solid Deep Navy (#0A1628).
2.  **Container Layer:** A slightly lighter navy hex or a 5% opacity white overlay on the base color, creating a "lifted" surface for cards.
3.  **Accent Elevation:** Interactive elements using Electric Aqua feature a soft 15px outer glow (0.2 opacity) to simulate the luminosity of pool lighting.
4.  **Shadows:** Avoid traditional black shadows. Use deep navy shadows with 40-60% opacity for a more integrated, sophisticated depth.

## Shapes

The shape language is **Soft yet Structured**. By using a subtle 4px radius (0.25rem), the UI maintains a professional, high-performance edge while remaining modern.

- **Buttons & Inputs:** Use the standard `rounded` (4px) setting to maintain a technical look.
- **Data Cards:** Use `rounded-lg` (8px) to soften the container for complex information.
- **Avatars & Icons:** Generally square with standard rounding, though specific progress rings may use circular geometries.

## Components

- **Primary Buttons:** High-contrast Warm Gold (#F5A623) with black or deep navy text. Text is bold and uppercase.
- **Secondary Buttons:** Ghost style with an Electric Aqua outline or solid Aqua with navy text for secondary actions.
- **Input Fields:** Deep navy background with a 1px border in a muted navy-blue. On focus, the border transitions to Electric Aqua with a subtle glow.
- **Performance Cards:** Subtle gradient backgrounds (Deep Navy to a slightly lighter tint). Data points are highlighted in Electric Aqua.
- **Progress Indicators:** Linear or circular bars using Electric Aqua. For "Goal Achieved" states, transition the color to Warm Gold.
- **Chips/Badges:** Small, uppercase labels with low-opacity Aqua backgrounds and solid Aqua text, used for categorizing workout types (e.g., "ENDURANCE", "SPRINT").
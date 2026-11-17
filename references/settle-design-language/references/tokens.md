# Token reference

All tokens are CSS custom properties defined in `assets/settle-tokens.css` (source: `assets/tokens.json`). Use `var(--name)`; never paste raw values.

## Colour (light / dark)

| Token | Light | Dark | Usage |
| --- | --- | --- | --- |
| `surface` | `#f5f4f0` | `#121211` | The ground. Page and app background; the paper everything rests on. |
| `surface-raised` | `#fcfbf9` | `#1b1b19` | Cards, controls at rest, the knob of a toggle. One step toward the viewer. |
| `surface-sunken` | `#ebe9e3` | `#0b0b0a` | Tracks, wells, segmented-control rails, code blocks. One step away from the viewer. |
| `surface-overlay` | `#fcfbf9` | `#232321` | Sheets, popovers, menus and toasts: anything that floats above a scrim or the page. |
| `ink` | `#1b1b19` | `#eeece7` | Primary text and icons on every surface token (15:1+ light, 13:1+ dark). |
| `ink-muted` | `#5c5a54` | `#a6a39b` | Secondary text, descriptions, inactive tabs, on every surface token and on stone (4.5:1+ both themes). |
| `ink-subtle` | `#6b6862` | `#8f8c84` | Tertiary text: timestamps, placeholders, helper text. On every surface token (4.5:1+). Never on stone. |
| `hairline` | `#e2dfd7` | `#2a2a27` | Decorative dividers and section rules. Separates; never identifies a control. |
| `line` | `#d3cfc5` | `#383733` | Edges of cards and sheets where shadow alone is not enough. Decorative. |
| `line-control` | `#837f75` | `#77746c` | Borders that identify a control: text fields, unchecked boxes, the outline of a quiet button. 3:1+ on every surface. |
| `stone` | `#d9d5ca` | `#3a3934` | The material tint: selected rows, segmented-control indicator on sunken rails, a toggle track at off. Ink or ink-muted on it. |
| `fill-primary` | `{ink}` | `{ink}` | The single primary action and a toggle at on: graphite in light, bone in dark. Text on it is on-fill-primary. |
| `on-fill-primary` | `{surface}` | `{surface}` | Text and icons on fill-primary (15:1+). |
| `signal` | `#2f55d4` | `#8aa8ff` | The one coloured thing in the room, a deep cobalt: focus rings, live and in-progress state, the current step. Never decoration, never status. 5.1:1+ on every surface. |
| `signal-soft` | `#e4e9f8` | `#18213d` | Quiet background behind signal-coloured text or a live indicator. |
| `on-signal` | `#ffffff` | `#0a1230` | Text on a signal fill (6:1+). Deep navy ink on the dark theme's lighter signal. |
| `focus-ring` | `{signal}` | `{signal}` | Keyboard focus: a 2px gap in the surface colour, then a solid 2px ring. 3:1+ on every surface. |
| `positive` | `#0e6b5c` | `#4cc2a5` | Success text and icons, always with a word or a check glyph. Teal leans off the red-green axis. |
| `positive-soft` | `#dcefe9` | `#10302a` | Background for positive notices; positive or ink text on it. |
| `caution` | `#7a5c00` | `#e8c547` | Caution text and icons, always with a word or a glyph. |
| `caution-soft` | `#f3ecd2` | `#302a0e` | Background for caution notices; caution or ink text on it. |
| `critical` | `#b3261e` | `#ff8a7a` | Errors and destructive confirmation, always with a word or a glyph. Red, set apart from signal's blue by hue; never rely on colour alone. |
| `critical-soft` | `#f8e1de` | `#3a1714` | Background for error notices; critical or ink text on it. |
| `scrim` | `rgba(18, 18, 17, 0.28)` | `rgba(0, 0, 0, 0.56)` | Dims the scene behind a sheet or dialog. Fades in with the layer, never ahead of it. |

## Type styles

Families: `--font-display` (Newsreader), `--font-sans` (Geist), `--font-mono` (Geist Mono). Apply a style with `class="st-type-<name>"`.

| Style | Family | Size / line | Weight | Usage |
| --- | --- | --- | --- | --- |
| `display-xl` | display | 72px / 76px | 300 | One per scene: the opening statement of a story or a landing moment. |
| `display` | display | 52px / 56px | 300 | Chapter openers, empty states that carry a message. |
| `headline` | display | 34px / 40px | 400 | Page titles inside the product. Sentence case. |
| `pull-quote` | display | 24px / 32px | 300 | The single idea a reader should leave with. Italic, never bold. |
| `title` | sans | 22px / 28px | 500 | Sheet and panel titles; card titles when a card is the main object. |
| `heading` | sans | 17px / 24px | 550 | Section headings inside a panel or form group. |
| `body` | sans | 15px / 24px | 400 | Default reading and interface text. 60-72 characters per line. |
| `body-small` | sans | 13px / 20px | 400 | Descriptions under a label, metadata, dense lists. |
| `label` | sans | 14px / 20px | 500 | Buttons, tabs, field labels, menu items. |
| `caption` | sans | 12px / 16px | 500 | Overlines and tiny labels. Uppercase allowed here only, tracked +0.02em. |
| `numeric` | mono | 28px / 32px | 400 | Key figures. Tabular numerals; figures align on the decimal. |
| `code` | mono | 13px / 20px | 400 | Code, IDs, keyboard shortcuts, tabular data cells. |

## Spacing

| Token | Value | Usage |
| --- | --- | --- |
| `space-1` | `4px` | Icon-to-label gap inside a control; hairline insets. |
| `space-2` | `8px` | Gap between tightly related items: a label and its field, chips in a row. |
| `space-3` | `12px` | Control padding (vertical in large controls), list-item gap. |
| `space-4` | `16px` | Default control horizontal padding; card inner gap. |
| `space-5` | `24px` | Card padding; gap between form groups. |
| `space-6` | `32px` | Panel and sheet padding; gap between cards. |
| `space-7` | `48px` | Between sections inside a page. |
| `space-8` | `64px` | Page margins at desktop; top of a scene before its headline. |
| `space-9` | `96px` | Between chapters of a story page. Stillness lives here. |
| `space-10` | `144px` | Rare: the pause before and after a display-xl statement. |

## Radius

| Token | Value | Usage |
| --- | --- | --- |
| `radius-xs` | `4px` | Checkboxes, inline code, tags. |
| `radius-sm` | `8px` | Text fields, small buttons, menu items. |
| `radius-md` | `12px` | Buttons, segmented controls, tooltips. |
| `radius-lg` | `20px` | Cards, popovers, toasts. |
| `radius-xl` | `28px` | Sheets and dialogs: the largest objects carry the softest corners. |
| `radius-full` | `999px` | Pills, toggles, avatars, the toggle knob. |

## Shadow (per theme)

Elevation is a material property, not decoration: each step is a hairline contact shadow plus one soft ambient shadow. Lift by one step on hover or drag, never two.

| Token | Value | Usage |
| --- | --- | --- |
| `shadow-rest` | `light: 0 0 0 1px rgba(27, 27, 25, 0.05), 0 1px 2px rgba(27, 27, 25, 0.06); dark: 0 0 0 1px rgba(255, 255, 255, 0.06), 0 1px 2px rgba(0, 0, 0, 0.5)` | Controls and cards at rest: sits on the surface. |
| `shadow-lift` | `light: 0 0 0 1px rgba(27, 27, 25, 0.05), 0 6px 16px -4px rgba(27, 27, 25, 0.12); dark: 0 0 0 1px rgba(255, 255, 255, 0.07), 0 8px 20px -6px rgba(0, 0, 0, 0.6)` | Hovered or picked-up cards, a dragged item. |
| `shadow-float` | `light: 0 0 0 1px rgba(27, 27, 25, 0.06), 0 16px 40px -12px rgba(27, 27, 25, 0.22); dark: 0 0 0 1px rgba(255, 255, 255, 0.08), 0 20px 48px -12px rgba(0, 0, 0, 0.7)` | Popovers, menus, toasts: detached from the page. |
| `shadow-sheet` | `light: 0 0 0 1px rgba(27, 27, 25, 0.06), 0 -8px 40px -8px rgba(27, 27, 25, 0.18); dark: 0 0 0 1px rgba(255, 255, 255, 0.08), 0 -12px 48px -8px rgba(0, 0, 0, 0.75)` | Bottom sheets and dialogs over a scrim. |
| `shadow-knob` | `light: 0 1px 1px rgba(27, 27, 25, 0.08), 0 2px 6px rgba(27, 27, 25, 0.14); dark: 0 1px 1px rgba(0, 0, 0, 0.4), 0 2px 6px rgba(0, 0, 0, 0.5)` | Small physical parts that move: toggle knobs, slider thumbs. |

## Duration

For CSS-only transitions. Interactive motion uses springs (settle-motion.js); these durations pair with the spring curves below so CSS and JS feel the same.

| Token | Value | Usage |
| --- | --- | --- |
| `dur-instant` | `90ms` | Colour and opacity response to press; hover tint. |
| `dur-quick` | `160ms` | Small exits, tooltip fade, icon swap. |
| `dur-snappy` | `340ms` | Pairs with ease-spring-snappy: toggles, segmented indicator, press release. |
| `dur-gentle` | `540ms` | Pairs with ease-spring-gentle: disclosure height, layout shifts. |
| `dur-settle` | `570ms` | Pairs with ease-spring-settle: entrances that land, toasts, popovers. |
| `dur-scene` | `800ms` | Pairs with ease-spring-heavy: scene changes, sheets, shared-element transitions. |

## Easing

cubic-bezier curves for simple fades; linear() curves are sampled from the four springs in settle-motion.js (Settle.springs) and must be paired with their dur- token.

| Token | Value | Usage |
| --- | --- | --- |
| `ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | Entrances without overshoot: fades, colour, opacity. |
| `ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Elements that move between two resting places on screen without user input. |
| `ease-exit` | `cubic-bezier(0.4, 0, 1, 1)` | Exits only: things leaving accelerate away; they never bounce out. |
| `ease-spring-snappy` | `linear(0, 0.045, 0.15, 0.284, 0.425, 0.559, 0.677, 0.776, 0.856, 0.917, 0.961, 0.992, 1.012, 1.023, 1.028, 1.029, 1.027, 1.024, 1.02, 1.016, 1.012, 1.009, 1.006, 1.004, 1)` | stiffness 520, damping 34 (zeta 0.75, 3% overshoot). Small parts under the finger. |
| `ease-spring-settle` | `linear(0, 0.071, 0.232, 0.431, 0.619, 0.78, 0.904, 0.99, 1.043, 1.068, 1.075, 1.069, 1.056, 1.042, 1.028, 1.016, 1.007, 1, 0.997, 0.995, 0.994, 0.995, 0.996, 0.997, 1)` | stiffness 300, damping 22 (zeta 0.64, 7% overshoot). The signature: arrives, overshoots a touch, settles. |
| `ease-spring-gentle` | `linear(0, 0.048, 0.157, 0.293, 0.432, 0.564, 0.677, 0.77, 0.843, 0.9, 0.941, 0.97, 0.989, 1.002, 1.009, 1.012, 1.013, 1.012, 1.011, 1.009, 1.007, 1.006, 1.004, 1.003, 1)` | stiffness 220, damping 24 (zeta 0.81, 1% overshoot). Size and layout changes. |
| `ease-spring-heavy` | `linear(0, 0.048, 0.157, 0.293, 0.432, 0.562, 0.675, 0.769, 0.843, 0.899, 0.94, 0.969, 0.989, 1.001, 1.008, 1.011, 1.012, 1.012, 1.01, 1.009, 1.007, 1.005, 1.004, 1.003, 1)` | stiffness 160, damping 26, mass 1.6 (zeta 0.81). Large surfaces with believable weight. |

---
name: settle-design-language
description: Apply the Settle design language (calm, minimal but never sterile, tactile, with spring-based motion and editorial storytelling) when building, restyling or reviewing web UI. Use for new pages, components, landing pages, story or explainer pages, motion and micro-interactions, or when the user mentions Settle, wants a restrained Ive-like look, Kowalski-style fluid motion, or a practical product-led interface. Ships CSS tokens with light and dark themes, component styles, a dependency-free vanilla JS spring runtime, icons and runnable examples.
---

# Settle design language

Settle is a calm, tactile interface language: still at rest, alive under the finger, with every movement explaining a relationship. Build with its tokens, components and spring runtime rather than inventing new values.

## Workflow

1. **Install the runtime.** Run `python3 scripts/scaffold_settle.py <project-static-dir>` (add `--with-icons`, `--with-starter`). Load in this order: `settle-tokens.css`, `settle.css`, `settle-motion.js` (exposes `window.Settle`). If the project already has a stylesheet pipeline, import the two CSS files into it instead of duplicating values.
2. **Pick the parts.** Read `references/components.md` and open the matching file in `assets/examples/` (each is a complete, runnable page). Copy its markup, classes and script, then change the content. Do not rebuild a listed component from scratch.
3. **Compose the scene.** One idea, one primary action, one focal point per view. Lay out with `references/space-and-proportion.md`; set type with `st-type-*` classes; colour with tokens only.
4. **Add motion last.** Only where it clarifies a relationship, guides attention or reveals how something works. Use `Settle.spring` with a named preset (see Motion below). For a story or explainer page, read `references/storytelling.md` and choose one metaphor.
5. **Review** against the checklist at the end before finishing.

## Stack rules

- Match the project's stack. In plain HTML/CSS/JS projects, use the assets as they are and add no libraries, frameworks or build tools.
- In framework projects, keep using the CSS custom properties and `st-` classes, and wrap `Settle.spring` in the framework's lifecycle (create on mount, `.stop()` on unmount). Do not swap in an animation library; if one already exists, configure it with the same stiffness, damping and mass values.
- Never paste raw hex, px or ms values where a token exists. All tokens: `references/tokens.md`.

## Non-negotiables

- **Colour roles.** Page on `--surface`; objects on `--surface-raised` with `--shadow-rest`; tracks and wells on `--surface-sunken`; overlays on `--surface-overlay`. Text is `--ink`, `--ink-muted`, `--ink-subtle`. One primary action per view in `--fill-primary` / `--on-fill-primary`. `--signal` (deep cobalt) is the single accent and only marks focus, live or in-progress state, or the current step. Status (`--positive`, `--caution`, `--critical`) always carries a word or glyph too.
- **Focus.** `outline: 2px solid var(--focus-ring); outline-offset: 2px;` on `:focus-visible`, never animated.
- **Type.** `display` serif (Newsreader) only for editorial moments, at most one `display`/`display-xl` per scene; `sans` (Geist) for the interface; `mono` for figures and code. Sentence case everywhere.
- **Space.** 4px scale `--space-1` to `--space-10`; prefer space to dividers; `--space-7`+ between sections. Corner radius grows with object size.
- **Voice.** Verb-first labels ("Save changes"), no exclamation marks, no emoji, errors say what to do next. Examples in `references/principles-and-voice.md`.
- **Avoid.** Decorative gradients, glassmorphism, glow, coloured left-border cards, emoji icons, parallax for its own sake, animated backgrounds, bounce, motion with no purpose.

## Motion

Springs, not timers. Springs keep velocity when interrupted, so every interaction is reversible mid-flight.

| Preset | k / c / m | Overshoot | Use |
| --- | --- | --- | --- |
| `snappy` | 520 / 34 / 1 | 3% | Under the finger: toggles, press, indicators |
| `settle` | 300 / 22 / 1 | 7% | Arrivals: toasts, popovers, things landing |
| `gentle` | 220 / 24 / 1 | 1% | Size and layout changes |
| `heavy` | 160 / 26 / 1.6 | 1% | Sheets, scene changes, shared elements |

```js
var s = Settle.spring({ from: 0, preset: 'settle', onUpdate: function (v) {
  el.style.transform = 'translateY(' + (1 - v) * 12 + 'px)';
  el.style.opacity = Settle.clamp(v, 0, 1);
} });
s.to(1);                 // later: s.to(0, releaseVelocity) to hand over a gesture
Settle.press(button);    // 0.97 press on snappy, settle release
```

Also available: `Settle.proximity(el)` (pointer-following edge light), `Settle.rubber(overflow, size)`, `Settle.tracker()` (velocity), `Settle.linear(preset)` (CSS `linear()` easing). CSS-only transitions use `var(--ease-spring-<preset>)` with `var(--dur-<preset>)`. Animate `transform` and `opacity`. Exits are faster than entrances and never overshoot. Reduced motion is honoured automatically: spatial motion jumps, opacity still fades. Full rules: `references/motion.md` and `references/micro-interactions.md`.

## References (load only what the task needs)

| File | Read when |
| --- | --- |
| `references/principles-and-voice.md` | Starting any Settle work; writing UI copy |
| `references/tokens.md` | Choosing any colour, type, spacing, radius, shadow, duration or easing value |
| `references/components.md` | Building any control, surface or layer; lists every example file |
| `references/materials-and-color.md` | Surfaces, elevation, edges, dark theme, colour roles |
| `references/typography.md` | Type hierarchy and editorial headlines |
| `references/space-and-proportion.md` | Grids, control sizes, spacing rhythm |
| `references/motion.md` | Any animation or transition |
| `references/micro-interactions.md` | Hover, press, focus, drag, validation feedback |
| `references/storytelling.md` | Landing, explainer or narrative pages; scene transitions |
| `references/iconography.md` | Drawing or choosing icons |

## Extending the palette

Edit `assets/tokens.json`, regenerate or hand-edit the matching variables in `settle-tokens.css`, then run `python3 scripts/check_contrast.py` (add `--pair FG BG MIN` for new pairs). Do not ship a pair that fails.

## Review checklist

- One primary action, one focal point, one metaphor per view.
- Only tokens; no raw colours, sizes or durations.
- Every text pair passes 4.5:1 in light and dark; control borders and focus ring pass 3:1.
- Every animation names its purpose (relationship, attention or mechanism) and uses a named spring.
- Interactions respond on pointerdown with zero delay; keyboard reaches everything with the same feedback.
- Works with `prefers-reduced-motion: reduce` and with `data-theme="dark"`.
- Copy is sentence case, verb-first, no exclamation marks or emoji.

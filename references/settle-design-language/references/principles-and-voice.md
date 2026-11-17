# Principles, usage rules and voice

Settle is the design language for a calm, tactile platform: minimalist but never sterile, where visual design, motion and storytelling work as one. It takes restraint from industrial design, fluid response from interaction craft, and plain usefulness from product engineering. Nothing is added for its own sake; everything that remains is finished with care.

## Five principles

1. **Quiet until touched.** At rest the interface is still, flat and legible. Life appears in response to the person: under the finger, near the pointer, at the focus point. Stillness is the default state, not the absence of design.
2. **Every movement explains something.** Motion is allowed only when it clarifies a relationship (this came from there), guides attention (look here next), or reveals how something works (this can be dragged, this has layers). If an animation does none of these, remove it.
3. **Weight is believable.** Things move on springs with mass, not on timers. Small parts are light and quick; large surfaces are heavy and unhurried. A gentle overshoot means "arrived"; a bounce means a toy. Overshoot stays under 8%.
4. **One idea per scene.** Each screen, card or chapter carries one editorial metaphor, one primary action and one focal point. Complexity is revealed in layers, on request, never all at once.
5. **Continuity over cuts.** Each scene is a consequence of the last. An element that persists between two states moves to its new place instead of disappearing and reappearing. The person should never have to re-find what they were looking at.

## Using this system

- Set the page on `surface`. Raise controls and cards with `surface-raised` and `shadow-rest`; sink tracks and wells with `surface-sunken`. Overlays use `surface-overlay` with `shadow-float` or `shadow-sheet`.
- Text is `ink` for primary, `ink-muted` for secondary, `ink-subtle` for tertiary. Every one of them reads at 4.5:1 or better on every surface token, in both themes.
- There is exactly one primary action per view: `fill-primary` with `on-fill-primary` text (graphite in light, bone in dark). Everything else is secondary (raised, `line-control` border) or quiet (text only).
- `signal` is the one coloured thing in the room: a deep cobalt. It marks focus, live and in-progress state, and the current step. It never decorates and never means success or error.
- Status always carries a word or a glyph as well as colour: `positive`, `caution`, `critical`, each with a `-soft` background.
- Keyboard focus is `focus-ring`: a 2px gap in the current surface colour, then a solid 2px `signal` ring. It appears instantly and never animates in.
- Set editorial moments in the `display` family (`display-xl`, `display`, `headline`, `pull-quote`). Set the interface in `sans` (`title` through `caption`). Set figures and code in `mono` (`numeric`, `code`).
- Spacing follows the 4px scale `space-1` to `space-10`. Default to more space than feels necessary: `space-7` between sections, `space-9` between chapters.
- Corners grow with size: `radius-sm` fields, `radius-md` buttons, `radius-lg` cards, `radius-xl` sheets, `radius-full` pills and toggles.
- Interactive motion runs on `window.Settle.spring` (in `assets/settle-motion.js`) with the named presets `snappy`, `settle`, `gentle`, `heavy`. CSS-only transitions use the matching `ease-spring-*` and `dur-*` tokens. Honour `prefers-reduced-motion`: spatial motion resolves instantly, opacity fades remain.
- The components here are plain HTML, CSS and vanilla JavaScript. Class names use the `st-` prefix and live in `assets/settle.css`.

## Content fundamentals

The voice is calm, exact and helpful, like a well-made instrument that comes with a short, clear manual.

- Write in sentence case everywhere, including buttons and titles: "Save changes", not "Save Changes". Uppercase only in `caption` overlines.
- Address the person as "you". The product does not say "I" or "we" except in a signed note from the team.
- Lead with the verb on actions: "Add member", "Export report", "Discard draft". Name the object; never "OK" or "Submit".
- Say what happened and what to do next, in that order: "Couldn't save. Check your connection and try again."
- One idea per sentence; aim for 12 to 18 words. Cut adverbs and intensifiers ("very", "simply", "just").
- No exclamation marks, no emoji, no jokes in errors. Warmth comes from clarity and timing, not from tone markers.
- Numbers are numerals ("3 files"), times are relative when recent ("4 minutes ago") and absolute when they matter ("Due 12 March, 17:00").

| Instead of | Write |
| --- | --- |
| Oops! Something went wrong. | Couldn't load the report. Try again in a moment. |
| Click here to get started! | Create your first project |
| Are you sure? | Delete "Q3 forecast"? This can't be undone. |
| Success! | Saved |

## What Settle is not

No gradients for decoration, no glassmorphism stacks, no glowing borders, no confetti, no parallax for its own sake, no animated backgrounds, no skeuomorphic textures. Materials are suggested by light, edge and weight, not drawn. No coloured left-border accent cards and no emoji as icons.

## Logo

No logo was supplied. Set the platform name in the `display` family at weight 300 in `ink`, sentence case, with no lockup or mark until one is designed.

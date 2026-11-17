# Components and patterns

Each entry below has a runnable example at `assets/examples/<file>.html` (open it in a browser; it loads the shared CSS and `settle-motion.js` from `assets/`). Copy the markup and script from the example, then adapt the content.

## Contents

- Button → `assets/examples/button.html`
- Toggle → `assets/examples/toggle.html`
- SegmentedControl → `assets/examples/segmented-control.html`
- Field → `assets/examples/field.html`
- Card → `assets/examples/card.html`
- Disclosure → `assets/examples/disclosure.html`
- Toast → `assets/examples/toast.html`
- Sheet → `assets/examples/sheet.html`
- Tooltip → `assets/examples/tooltip.html`
- SharedElement → `assets/examples/shared-element.html`
- Metaphors → `assets/examples/metaphors.html`
- Springs → `assets/examples/springs.html`

## Button

Example: `assets/examples/button.html`

Starts an action. One primary button per view; everything else is secondary or quiet.

### Variants

- `st-btn-primary`: the one action the view exists for. `fill-primary` with `on-fill-primary` text.
- `st-btn-secondary`: alternative actions. `surface-raised` with a `line-control` edge.
- `st-btn-quiet`: low-emphasis actions such as Cancel, or actions in dense toolbars. Text only.
- Modifiers: `st-btn-icon` (square, needs `aria-label`), `st-btn-compact` (32px, for toolbars and tables).

### What you provide

A `<button type="button">` with the classes above and a verb-first, sentence-case label ("Save changes"). Icons are inline SVGs with class `st-icon` and `aria-hidden="true"`. Call `Settle.press(button)` once to attach the press motion.

### Behaviour

- Pointerdown or Space/Enter scales to 0.97 on `snappy`; release returns to 1 on `settle`, with a small overshoot that says "done".
- Hover adds a 7% overlay of the text colour (`dur-instant`); press deepens it to 12%. No delay on either.
- Disabled buttons move to `surface-sunken` with `ink-subtle` text and no press motion. Pair with a reason nearby.

### Do and don't

- Do keep labels to one to three words. Don't use "OK", "Submit" or "Click here".
- Do place the primary button last in a row (right in left-to-right layouts). Don't put two primary buttons side by side.
- Don't animate a button's colour or size on load to draw attention.

## Toggle

Example: `assets/examples/toggle.html`

Turns a setting on or off immediately, with no Save step.

### What you provide

A `<button type="button" role="switch" aria-checked="true|false" class="st-toggle">` containing `<span class="st-toggle-fill">` and `<span class="st-toggle-knob">`, inside a `<label class="st-setting">` that holds the title (and an optional one-line description). The label makes the whole row clickable. Drive the knob with two springs as in the preview: position (`snappy`) and press stretch (`snappy`).

### Behaviour

- On press the knob stretches 4px toward its direction of travel, like a fingertip flattening on glass. On release it relaxes.
- The knob travels 18px on `snappy` (about a pixel of overshoot). The `fill-primary` track fades in with the knob's position, so colour and motion are one gesture.
- Interruptible: a second tap mid-flight reverses from the current position and velocity.
- Off state keeps a `line-control` inner edge so the control is identifiable at 3:1.

### Do and don't

- Do use for settings that take effect at once. Don't use inside a form that needs a Submit; use a checkbox there.
- Do write the title as the thing being controlled ("Weekly summary"), never "Enable weekly summary".
- Don't add on/off text inside the track.

## SegmentedControl

Example: `assets/examples/segmented-control.html`

Switches between two to five views of the same content, such as time ranges or display modes.

### What you provide

A `<div class="st-seg" role="radiogroup" aria-label="…">` containing one `<span class="st-seg-indicator">` and two to five `<button class="st-seg-option" role="radio">` options. Exactly one option has `aria-checked="true"` and `tabindex="0"`. Drive the indicator's x position and width with two `snappy` springs, as in the preview.

### Behaviour

- The raised indicator travels to the chosen option and resizes to fit it. It never fades out and back in: one object, moving, makes the relationship between options obvious.
- Labels change colour from `ink-muted` to `ink` over `dur-instant`.
- Arrow keys move the selection and the focus together; Tab enters and leaves the group as one stop.
- Options press to 0.98 (smaller than buttons, because the indicator is already moving).

### Do and don't

- Do use one or two words per option, all the same kind of thing. Don't mix icons and text.
- Don't use for navigation between unrelated pages; use tabs or links.
- Don't use more than five options; use a menu.

## Field

Example: `assets/examples/field.html`

A labelled text input with one line of helper or validation text beneath it.

### What you provide

A `<div class="st-field">` holding a visible `<label class="st-field-label" for="…">`, an `<input class="st-input">` with `aria-describedby` pointing at the message, and a `<div class="st-field-msg" aria-live="polite">`. Set `data-tone="critical"` or `"positive"` on the message and `aria-invalid="true"` on the input for errors.

### Behaviour

- **Reward early, correct late.** Validate on blur first. Once a field has shown an error, re-check on every keystroke so the error clears the moment the value is right.
- A new message rises 8px into place on `gentle` and fades in with it. Errors never shake.
- Errors carry a glyph and a word as well as `critical` colour. The message says what to enter, not what went wrong: "Enter an email like name@company.com."
- Focus shows the `focus-ring` outside the field's own `line-control` edge, instantly.

### Do and don't

- Do keep labels visible above the field. Don't use the placeholder as the label.
- Do reserve the message line (20px) so the layout does not jump when text appears.
- Don't validate while the person is still typing their first attempt.

## Card

Example: `assets/examples/card.html`

A raised surface that represents one object (a report, a dataset, a scenario) and opens it.

### What you provide

An `<article class="st-card" tabindex="0">` (or an `<a class="st-card">` when it navigates) containing an optional `st-overline`, a `st-card-title` and one line of `st-card-meta`. Attach `Settle.proximity(card)` for the edge light, a `settle` spring writing `--st-lift` and `--st-lift-y` for hover, and `Settle.press(card, { scale: 0.99 })`.

### Behaviour

- **Proximity is light, not movement.** Within 80px of the pointer, the card's edge brightens toward the pointer in `line-control`, following on `gentle`. The card itself does not tilt or move toward the pointer. Touch devices skip this.
- **Hover lifts one step.** `shadow-rest` crossfades to `shadow-lift` and the card rises 2px on `settle`. Keyboard focus lifts it too, and shows the `focus-ring`.
- **Press** settles to 0.99: large objects compress less than small ones.
- If a card opens a detail view, use the SharedElement pattern so the card becomes the view.

### Do and don't

- Do keep one title and one line of meta. Don't put more than one action inside a card; the whole card is the action.
- Don't nest cards. Inside a card, use `surface-sunken` wells.
- Don't add coloured borders or side stripes to signal type; use the overline.

## Disclosure

Example: `assets/examples/disclosure.html`

Reveals a layer of detail beneath a summary line: FAQs, advanced settings, explanations of how a number was made.

### What you provide

A `<div class="st-disclosure">` with a `<button class="st-disclosure-trigger" aria-expanded aria-controls>` (label plus chevron icon) and a `<div class="st-disclosure-panel" role="region">` wrapping one `st-disclosure-inner`. Drive height with a `gentle` spring and the chevron with `snappy`, as in the preview.

### Behaviour

- **Space first, then content.** The panel opens on `gentle`; its content starts to appear once a third of the space is open, rising 6px into place. Closing reverses, so content leaves before the space closes.
- The chevron rotates 90° on `snappy`, slightly ahead of the height, so the cause leads the consequence.
- At rest open, the panel's height is `auto` so it adapts to resizing; at rest closed, it is `visibility: hidden` so its content is not focusable.
- Several disclosures may be open at once; opening one never closes another without being asked.

### Do and don't

- Do phrase triggers as the question the reader has. Don't hide information needed to complete the current task.
- Don't nest disclosures more than one level.

## Toast

Example: `assets/examples/toast.html`

A brief, non-blocking notice about something that just happened, stacked as layers in a corner of the screen.

### What you provide

One `<section class="st-toast-region" aria-live="polite" aria-label="Notifications">` per page, positioned in the bottom-right corner (bottom-centre on phones). Each notice is a `div.st-toast` with `role="status"`: a glyph (`st-toast-glyph` with `data-tone="positive"` or `"signal"`), a title of one to three words, an optional one-line description, and a quiet dismiss button. Each toast drives three springs: y and scale on `settle`, opacity on `gentle`.

### Behaviour

- **Layers reveal complexity.** At rest only the newest notice is fully visible; up to two older ones peek above it, each 14px higher, 5% smaller and a little fainter. Hovering or focusing the stack fans the layers out into a readable list; leaving restacks them.
- A new notice rises 24px into place on `settle` and fades in. Older notices step back at the same moment, so the stack reads as one object.
- Dismissing fades and drops the notice 12px on `snappy`; the others close the gap on `settle`.
- Auto-dismiss after 6 seconds, paused while the stack is hovered or focused. At most four notices are kept.

### Do and don't

- Do confirm outcomes ("Report exported"). Don't use a toast for errors that need action; show them inline where the problem is.
- Do keep the title to the result, not the process ("Saved", not "Saving was successful").
- Don't put more than one action in a toast, and never make the only copy of important information a toast.

## Sheet

Example: `assets/examples/sheet.html`

A modal layer that rises from the bottom edge for a short, focused task: sharing, confirming, choosing an option.

### What you provide

Inside a positioned container: a `div.st-sheet-scrim` and a `div.st-sheet` with `role="dialog" aria-modal="true" aria-labelledby`. The sheet holds a `button.st-sheet-handle`, a `st-sheet-title`, an optional `st-sheet-desc` and a `st-sheet-actions` row (primary last). Drive one `heavy` spring from 1 (closed) to 0 (open); the scrim's opacity is derived from the same value, so the two can never drift apart.

### Behaviour

- **Weight.** The sheet is a large surface, so it rises on `heavy` (mass 1.6). It feels like a panel sliding on rails, not a popup.
- **One value, two effects.** The scrim fades exactly as far as the sheet has risen.
- **Drag has physics.** The handle follows the finger 1:1 downward. Upward past the open position, resistance grows (`Settle.rubber`). On release, a flick faster than 500px/s or a drag past 40% closes it, carrying the release velocity into the spring; otherwise it settles back open.
- **Focus.** Opening moves focus to the primary action; Tab stays inside the sheet; Escape, the scrim and Cancel close it and return focus to the trigger.

### Do and don't

- Do keep a sheet to one decision. Don't stack a sheet on a sheet.
- Do size it to its content, up to 90% of the viewport. Don't make it full-screen; that is a page.

## Tooltip

Example: `assets/examples/tooltip.html`

A short label for an icon-only control, shown on hover or keyboard focus.

### What you provide

One `div.st-tooltip` with `role="tooltip"` per region, and icon buttons carrying `aria-label` and `data-tip` with the same text. While shown, the trigger gets `aria-describedby` pointing at the tooltip. Drive x on `snappy` and opacity on `snappy`, as in the preview.

### Behaviour

- **Wait once, then be instant.** The first tooltip appears after 500ms of hover, so passing the pointer across a toolbar does not flash labels. While one is showing (and for 300ms after it hides), neighbours show immediately.
- **Glide between neighbours.** When moving from one button to the next, the same tooltip travels to the new position instead of disappearing and reappearing: one object, continuous.
- Appears from its trigger: 4px lower and 96% scale growing to full, origin at the bottom centre.
- Keyboard focus shows it at once; Escape hides it; pressing the button hides it.

### Do and don't

- Do keep it to two or three words that name the action. Don't put sentences, links or shortcuts that are not also elsewhere.
- Don't use tooltips on controls that already have a visible label, or on touch-only surfaces.

## SharedElement

Example: `assets/examples/shared-element.html`

A scene transition in which an object that exists in both scenes travels and resizes into its new place, while everything else steps aside.

### What you provide

A source element (usually a `st-card`) and a destination container whose header repeats the source's content (overline, title, meta). Measure the source rectangle, place the destination over it, and drive one `heavy` spring from 0 (source) to 1 (destination). Interpolate the rectangle from that value; derive every other effect from the same value. The preview interpolates geometry directly for clarity; in production, animate `transform` (FLIP) and counter-scale the content so text never stretches.

### Behaviour

- **Continuity.** The title the person clicked never leaves the screen. The shape leads; new content (body, figures, Back) fades and rises in only after 55% of the travel.
- **Steps aside.** Sibling cards fade out over the first third of the motion, so two scenes never compete.
- **Exact reversal.** Back, or Escape, runs the same spring to 0 and lands the card where it came from, then returns focus to it.
- `heavy` gives the large surface believable mass: unhurried, about 800ms, with no visible overshoot.

### Do and don't

- Do use it whenever a list item opens into its own view. Don't cut, cross-dissolve or slide the whole page instead.
- Don't move the camera (pan or zoom the viewport); objects move, the stage stays still.

## Metaphors

Example: `assets/examples/metaphors.html`

The three editorial metaphors (layers, alignment, coming together) told with the same four parts, so you can see how one set of materials carries different ideas.

### What you provide

Two to five elements built from real interface materials (`stone`, `surface-raised` with `line`, `signal`, `fill-primary`), a positioned stage, and a `pull-quote` that names the idea in words. Give each element x and y springs; choose the preset by the metaphor.

### The three states

- **Layers reveal complexity** (`settle`): the parts stack with 36px by 28px offsets and lifted shadows, so depth is visible and the top layer reads first.
- **Alignment creates clarity** (`gentle`): the parts travel onto one baseline, `space-4` apart. After they arrive, a `line-control` hairline draws along the shared edge to name the alignment.
- **Separate parts come together** (`heavy`): the parts close to a 4px join and their outer corners keep `radius-lg` while inner corners drop to `radius-xs`, so four shapes read as one.

### Choreography

Parts move with a 30ms stagger, the caption fades out over 180ms and the new sentence fades in as the shapes arrive. The end state of each is a still frame that tells the story without motion.

### Do and don't

- Do pair each metaphor with its sentence. Don't use a metaphor without the words that name it.
- Don't use more than five parts, and don't mix two metaphors in one scene.

## Springs

Example: `assets/examples/springs.html`

The four motion presets every component uses, shown side by side: `snappy`, `settle`, `gentle` and `heavy`.

### What you provide

Nothing: this is a reference card. In your own code call `Settle.spring({ from, preset, onUpdate })` and move it with `.to(target, velocity?)`. For CSS-only transitions use the `ease-spring-*` token with its paired `dur-*` token.

### Reading the card

- Each row shows a preset's stiffness (k), damping (c) and damping ratio (ζ). The small curve plots position over the first second; the hairline marks the target.
- The vertical mark at the end of each track is the resting point. `settle` crosses it by about 7% before settling; `heavy` arrives last because its mass is 1.6.
- Click a track twice quickly: the dot turns around from wherever it is, at the speed it was moving. This is why Settle uses springs rather than fixed-duration tweens.

### Choosing

`snappy` for anything under the finger, `settle` for arrivals, `gentle` for size and layout, `heavy` for large surfaces and scene changes. If none fits, the motion is probably not needed.

# Narrative UI/UX design

## Contents
- Scope, inputs, and creative direction
- Adaptive workflow and exit conditions
- Interaction, motion, and explanatory interfaces
- State coverage and adaptation
- Deliverables and handoff template
- Quality checks, failure modes, and evaluation examples

## Scope, inputs, and creative direction

Turn briefs into coherent, usable experiences where structure, language, visual
expression, interaction, and motion reinforce the user's task. Aim for clarity,
tactility, restraint without sterility, and imagination without distraction.

Use creative references as principles, not aesthetic templates:
- Jony Ive: material sensitivity, proportion, restraint, and detail.
- Emil Kowalski: continuity, fluid motion, and purposeful micro-interactions.
- Tony Fadell: practical problem-solving and product clarity.

Optionally express curiosity, invention, human agency, and possibility through
useful discovery and legible relationships. Never impose theatrical or whimsical
behavior on a task-focused product. Preserve existing brand and system rules;
propose departures explicitly with a user-centered reason.

Review supplied briefs, assets, research, code, and brand guidance first.
Required understanding: product purpose, primary actor, task, context, requested
deliverable/fidelity, and consequential constraints. Optional inputs: organization
outcomes, content, workflows, assets, platforms, research, usability findings,
accessibility/performance targets, and implementation stack. An absent optional
input is not automatically a blocker. Clarify only consequential ambiguity;
otherwise state reasonable assumptions. Separate facts, assumptions, and unknowns.
Never invent research, quotations, capabilities, success metrics, or validation.

Choose scope:
- Small edit: inspect affected component, preserve existing patterns, cover changed
  states and inputs, implement or specify exactly the request, and verify locally.
- Flow or screen: apply relevant workflow phases, reuse existing foundations,
  and cover entry, completion, and recovery across relevant devices.
- Complete experience: apply all relevant phases and provide the full handoff.
- Design-only request: deliver requested specs or mockups, not unsolicited code.
- Prototype request: produce the actual reviewable artifact using available tools;
  if a necessary tool is unavailable, state the limitation, not a false completion.

## Adaptive workflow and exit conditions

Treat phases as iterative lenses, not a frozen waterfall. Backtrack when evidence
changes the problem. Reuse accepted decisions; avoid duplicate paperwork.

### A. Frame
State problem, primary user/context, task, known friction, constraints,
dependencies, success criteria, and assumptions needing validation. Distinguish
user outcomes from organization outcomes and surface conflicts.
Exit: actor, problem, and outcome are clear enough to guide choices.

### B. Structure the experience
Map entry points, primary/secondary actions, prerequisites for decisions,
decision points, feedback/confirmation, error/recovery paths, completion, and next
steps. For narrative landing pages, develop curiosity, understanding, credibility,
and action. For products, prioritize orientation, task completion, feedback, and
recovery. For hybrids, let narrative support the task. Do not prescribe long scroll.
Exit: a coherent core journey exists before detailed styling.

### C. Establish a concept
Write a one-sentence concept, ranked design priorities, audience-appropriate
visual direction, and an optional clarifying metaphor. For full experiences,
propose up to two or three purposeful signature interactions; use none when
unnecessary. Compare alternatives through structure or behavior, not palette alone.
Avoid metaphors requiring explanation before controls are usable.
Exit: concept connects task, identity, and interaction model.

### D. Resolve hierarchy
Use low-fidelity layouts or equivalent structural specifications. Resolve content
priority, navigation, grouping/spacing, screen composition, primary/secondary
actions, forms/validation, disclosure, and persistent/contextual controls. Use real
content where available; label sample content and stress-test realistic lengths.
Exit: the experience is understandable without decoration or motion.

### E. Define the visual system
Reuse or specify typography/reading hierarchy, semantic colors, spacing/layout,
geometry/proportions, surfaces/borders/elevation, icons/illustration, interactive
states, and responsive rules. Favor restrained palettes, deliberate accents,
readability, purposeful space, and warmth from composition and tonal detail.
Avoid generic grids, arbitrary gradients, excessive glass, or oversized type
unless a specific need justifies them. Do not replace an established system to
satisfy these preferences. Express rules as reusable tokens where appropriate.
Exit: the system is coherent and reusable rather than isolated styling.

### F. Specify behavior and motion
Use the interaction template below for significant interactions. Use motion for
relationships, continuity, cause/effect, or confirmation. Use springs selectively
for direct manipulation or suitable transitions, with believable weight and
restrained overshoot. Specify actual parameters or token references when handing
off implementation; label initial values as proposals if unmeasured.
Avoid scroll hijacking, task delays, constant ambient movement, exaggerated bounce,
and effects competing with the task. Balance movement with stillness.
Exit: each significant motion has a purpose and a usable reduced-motion path.

### G. Explain through interaction when helpful
Specify the question a diagram answers, baseline static explanation, labels and
components, controls, input/output relationships, selection/focus/expanded states,
mobile behavior, keyboard operation, and a text/static alternative.
Distinguish conceptual illustrations from live data and validated simulations.
Never imply unsupported precision, causality, or product capabilities.
Exit: interaction deepens understanding; it does not hide the basic explanation.

### H. Cover realistic use
Use the state/adaptation checklist below; mark irrelevant states as inapplicable
rather than inventing them. Redesign density and navigation for small screens;
do not simply shrink the desktop.
Exit: relevant non-ideal states and input/device conditions are specified.

### I. Evaluate and refine
Review purpose/orientation, primary action, task effort, labels/feedback,
preventable errors and recovery, hierarchy, motion utility, accessibility,
responsiveness, and feasibility against constraints. Distinguish observed findings,
expert critique, and untested hypotheses. Internal critique is not user validation.
Prioritize comprehension, completion, accessibility, and implementation risk.
Exit: major issues are resolved or documented with an appropriate validation plan.

## Interaction, motion, and explanatory interfaces

For each significant interaction record:
- Trigger and control; initial and resulting state.
- User purpose and feedback.
- Timing/easing or spring parameters; existing token where available.
- Interruption, cancellation, reversal, and repeated input behavior.
- Touch and keyboard equivalents; focus destination/return where relevant.
- Reduced-motion behavior that preserves information and completion.

For diagrams additionally record the question, default explanation, labels,
control semantics, input/output mapping, responsive treatment, and static/text
alternative. Essential information must be available without animation or hover.

## State coverage and adaptation

Cover applicable default, hover, focus-visible, active, selected, loading/progress,
empty/first-use, success/completion, validation/error, disabled/unavailable,
permission-restricted, interrupted, and partially completed states.

Define responsive layout/content priority, navigation, density, long-content
handling, touch targets, and relevant input modes. Provide semantic controls,
accessible names, keyboard operation, logical focus, readable contrast, error
association, and useful announcements where applicable. Do not make hover or
dragging the only route. Check reduced motion and zoom/reflow where relevant.
Use project accessibility requirements and applicable current standards; verify
normative thresholds against authoritative documentation when needed. Do not
claim compliance from a checklist or automated scan alone.

## Deliverables and handoff template

For a complete experience, provide these as one coherent artifact or existing
project documentation, not nine mandatory separate files:
1. Brief: user/business outcomes, constraints, evidence, assumptions.
2. Structure: information architecture, journeys, decisions/recovery.
3. Rationale: consequential choices and tradeoffs.
4. Screen/components: real content hierarchy, layout, controls, behavior.
5. Visual system: reusable foundations, tokens, component rules.
6. Interactions: triggers, transitions, feedback, alternatives.
7. Coverage: relevant states, viewport/input adaptation, accessibility.
8. Evaluation: observed findings, critique, hypotheses, unresolved risks.
9. Implementation: assets, dependencies, acceptance criteria, open decisions.

Compact component handoff:
- Actor/task and scope:
- Existing pattern reused / justified departure:
- Content, layout, controls:
- State and interaction behavior:
- Responsive/accessibility/motion alternatives:
- Acceptance checks, outcomes, unresolved questions:

Match format and fidelity to the request. Use tool-specific workflows where
required. Do not substitute prose for a requested working prototype or claim
rendered inspection when only code or a description was inspected.

## Quality checks, failure modes, and evaluation examples

Before completion, check task clarity, visible primary action, essential context,
progressive disclosure, predictable critical controls, understandable feedback,
recoverable errors, purposeful novelty, brand consistency, feasible performance,
and relevant accessibility/device coverage. Verify with rendering and interaction
when implemented and tools permit; disclose unperformed checks.

Watch for decorative storytelling delaying tasks, identical aesthetic treatment
across projects, style before structure, fabricated evidence, hover-only controls,
incomplete recovery states, animation without purpose, unsupported simulations,
large new dependencies for minor effects, and excessive discovery for small edits.

Evaluate using varied briefs:
| Brief | Expected adaptation |
|---|---|
| Narrative landing page | Coherent story and clear action; no forced scroll theatrics |
| Task-focused workflow | Orientation, completion, feedback and recovery precede spectacle |
| Dense data interface | Preserve decision context; progressive disclosure without hiding essentials |
| Mobile interaction | Touch, focus and small-screen navigation; no hover-only dependency |
| Existing component edit | Reuse foundations; focused states/checks; no full redesign |
| Missing research | Label assumptions; no fabricated quotes or validation claims |
| Strict access/performance limits | Honor declared constraints; provide alternatives and measured evidence |

Assess specific implementable decisions, scope discipline, non-ideal states,
selective narrative/motion, and clarity under expressive direction. Revise the
workflow when outputs become repetitive, bloated, uniform, or unactionable.
Definition of done: requested reviewable artifact, coherent structure and behavior,
explicit rationale for consequential choices, relevant state coverage, and clear
handoff with verification limitations. No implied guarantee of usability.

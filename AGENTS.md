# Working in this repo (for agents)

This repo is the **source of truth for the design of every Gabriel app**. Tokens, components,
rules, fonts, icons and marks are decided here and copied out to the apps. An app never invents a
colour, size, radius, duration or component of its own; if it needs one, it is added here first.

Start with [README.md](README.md) (what is here), then [DESIGN.md](DESIGN.md) (the system in one
page) and [docs/](docs/) (the long version).

## The apps this system governs

| App | Repo | Layer in `tokens.json` | Platform |
|---|---|---|---|
| GVoice, GMind, GMoney, GHealth, GDesk | `gabrielbr/NotTheOmiAIApp` (`ui-kit/`, `br.gabriel.ui`) | `uikit` | Android Views (Java), light + dark |
| PulseLoop | `gabrielbr/PulseLoopAndroid` (`com.pulseloop.ui.theme`) | `pulseloop` | Jetpack Compose (Kotlin), dark only |

GMind is called "Sentient" in its code. A new app gets a layer and a row here before its first screen.

## How the system is built

- **`tokens/tokens.json` is the only place a value is defined.** `core` holds what every app
  shares; `layers.<app>` lists, in output order, the core tokens it carries (`"@name"`) plus its
  own. Schema and workflow: [docs/tokens.md](docs/tokens.md).
- **Everything in `generated/` and the frontmatter of `DESIGN.md` is generated** by
  `python3 scripts/gen_tokens.py`. Never edit them by hand; edit the tokens and regenerate.
- **Every core token is in every layer.** That is what "consistent" means here, and
  `check_tokens.py` enforces it. A token only one app uses lives in that app's layer.
- **Divergences are recorded, not hidden.** Where the apps still differ (type scale, motion,
  dither, light theme), [docs/divergences.md](docs/divergences.md) says how and what the plan is.
  Shrinking that list is the direction of travel; growing it needs a reason written there.

## Every change is audited — no exceptions

**Any change to this repo** (a token, a rule, a component spec, an asset, a doc that states a
design rule) **is audited with both skills before it is merged**:

1. **`graphic-design-fundamentals`** — run its §13 critique checklist on the change: hierarchy,
   contrast, alignment and grid, spacing from the system, typography, colour (grayscale, accent
   discipline, WCAG), consistency, simplicity, real-size test, accessibility, production.
2. **`impeccable`** — run `audit` (native: `reference/audit.native.md`, scored against
   `reference/android.md`) and, for anything visual, `critique`. Score the five dimensions and tag
   findings P0–P3.

Both are vendored in [`.claude/skills/`](.claude/skills/) so every session in this repo has them
(see [`.claude/skills/VENDORED.md`](.claude/skills/VENDORED.md)). If a session cannot load one
(for example Impeccable's launcher is blocked), read its `SKILL.md` and references directly and
apply them by hand, and say so in the audit.

The audit is written to `audits/YYYY-MM-DD-<version or topic>.md` from
[`audits/TEMPLATE.md`](audits/TEMPLATE.md) and linked from the PR. A PR without an audit file, or
with an unresolved P0/P1 or "critical" finding it introduces, is not merged. Process:
[docs/audit.md](docs/audit.md).

Findings that already exist in the apps are tracked, not ignored: a failing contrast pair gets
`"known": "<audit id>"` in `tokens.json` so CI keeps warning until it is fixed, and fails the day
it passes so the exception is removed.

## How a change goes in

1. Branch, never push to `main`. One PR per change; the owner squash-merges once it is verified.
2. Edit `tokens/tokens.json` and/or the docs. Regenerate: `python3 scripts/gen_tokens.py`.
3. Run `python3 scripts/check_tokens.py` (CI runs it too). Zero errors.
4. Run the audit (above) and commit `audits/<date>-<topic>.md`.
5. Bump the version (below): `tokens.json` `version`, `VERSION`, a `CHANGELOG.md` entry that says
   what changed for each app and what the app has to do.
6. Open the PR with the template; it asks for the audit and the app impact.
7. After merge, **sync the apps** ([docs/consuming.md](docs/consuming.md)): open a PR in each
   affected app repo that copies the generated file in, and run
   `python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid`
   until it reports 0 differences. The app PR follows that repo's own rules (its tests, its
   design canvas, its release flow).

## Versioning

Semantic versioning on the whole system (`VERSION`):

- **major**: a token removed or renamed, a component removed, a rule that makes existing screens
  wrong. The CHANGELOG entry carries the migration for each app.
- **minor**: a token, component or rule added; a value changed on purpose (a colour, a size).
- **patch**: docs, wording, tooling, generated-file formatting with no value change.

## Rules every design decision follows

These are the system's non-negotiables. The reasons are in [docs/foundations.md](docs/foundations.md).

- **Tokens only.** No literal dp, sp, px, ms or colour in a screen. If the scale lacks the gap you
  need, the layout is wrong, not the scale. Spacing is 4, 8, 12, 16, 24, 32, 40, 48, 64.
- **One brand, one accent.** Mint `#43F3B7` is the brand and "tap here". Text on mint is `on-mint`
  or `ink`, never white. Good/in-range is `success`, not mint. One filled mint action per screen.
- **One family.** Ubuntu Mono everywhere (regular, bold, bold italic). Nothing that carries meaning
  under 12sp. Sizes come from the layer's type roles, never inline.
- **Contrast.** Text 4.5:1 in every theme an app ships; graphics and boundaries 3:1. Never colour
  as the only carrier of meaning. Every new colour pair a component uses goes in `contrast`.
- **Shape.** Radii 4 (controls), 8 (cards — the one card radius), 16 (pills, sheets), round. No
  drop shadows, no gradients; depth is `surface` on `page` and hairlines.
- **The frame.** A 4dp mint frame round every screen. In uikit it doubles as the loading line for
  waits the user asked for; never for background work.
- **Targets.** 48dp minimum for anything tappable; rows 48dp min (uikit 56dp); buttons 52dp.
- **Motion.** 150ms standard, 250ms emphasised, one ease (quick out, gentle in), no bounce; press
  scales to 97%. Honour the system "Remove animations" setting: things appear instead of moving.
- **States, not logs.** User-facing status comes from the state vocabulary
  ([docs/content.md](docs/content.md)); no engine, vendor or exception names in UI text.
- **Copy.** Short, plain, sentence case, verb first on buttons; English and Brazilian Portuguese.
- **Icons.** One line set, 22dp, stroke 1.75, `ink` or `muted`. Never emoji as icons.

## Never

- Edit `generated/` or `DESIGN.md`'s frontmatter by hand.
- Change a value in an app without changing it here first (that is drift; `drift.py` reports it).
- Merge without the two-skill audit, or skip/loosen a check to get green.
- Delete a "known" contrast exception without fixing the pair.
- Add a font, an icon set or a colour that isn't in `tokens.json`.
- Commit secrets, or anything from an app that isn't design (code, data, keys).

## Writing style

Short, plain and concrete, like the apps' own docs. Say what a rule does for the person using the
app. Docs mark items ✅ (done), 🟡 (built, to try in the apps) or ⬜ (not started). Commits carry
no `Co-Authored-By` trailer for agents (the PulseLoop owner's rule, applied here too).

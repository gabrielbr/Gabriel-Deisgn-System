# Working in this repo (for agents)

This repo is the **source of truth for the design of every Gabriel app**, and the owner's
boilerplate: it's dressed in Gabriel's brand. Tokens, components, rules, fonts, icons and marks are
decided here and copied out to the apps. An app never invents a colour, size, radius, duration or
component of its own; if it needs one, it is added here first.

**The one exception: a product with a partner's brand** (since 0.28.0). Its brand and its product
layer live in its own repo and are built with this repo's scripts, unchanged
([docs/products.md](docs/products.md)). Only what every app can use comes here. Cochilo (a Tatá
Slings product) is the first.

Start with [README.md](README.md) (what is here), then [DESIGN.md](DESIGN.md) (the system in one
page) and [docs/](docs/) (the long version).

## The apps this system governs

| App | Repo | Layer in `tokens.json` | Platform |
|---|---|---|---|
| GVoice, GMind, GMoney, GHealth, GDesk | `gabrielbr/NotTheOmiAIApp` (`ui-kit/`, `br.gabriel.ui`) | `uikit` | Android Views (Java), light + dark |
| PulseLoop | `gabrielbr/PulseLoopAndroid` (`com.pulseloop.ui.theme`) | `pulseloop` | Jetpack Compose (Kotlin), dark only |
| Cochilo (da Tatá Slings) | `gabrielbr/Cochilo` (`br.gabriel.cochilo.ui.theme`) | none here: its layer and the `tata-slings` brand are in its `design/` ([docs/products.md](docs/products.md)) | Jetpack Compose (Kotlin), light, dark and night |

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
design rule) **is audited with all three skills before it is merged**:

1. **`graphic-design-fundamentals`** — run its §13 critique checklist on the change: hierarchy,
   contrast, alignment and grid, spacing from the system, typography, colour (grayscale, accent
   discipline, WCAG), consistency, simplicity, real-size test, accessibility, production.
2. **`impeccable`** — run `audit` (native: `reference/audit.native.md`, scored against
   `reference/android.md`) and, for anything visual, `critique`. Score the five dimensions and tag
   findings P0–P3.
3. **`less-is-more`**: run its five questions on every element the change adds or touches
   (helps now, duplicate, understand once, weak for the goal, rare), list what was cut or moved,
   and score it. Cutting never adds a tap to a common action.

All three are vendored in [`.claude/skills/`](.claude/skills/) so every session in this repo has them
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

## Every app built on this boilerplate uses the three skills

The three design skills (since 0.29.0) are part of the boilerplate, like the tokens:
- **impeccable**;
- **graphic-design-fundamentals** (the owner's design basics);
- **less-is-more**.

Every app that uses this system, whether its layer is here or it builds on the core in its own
repo (docs/products.md), must:
1. **Carry the three skills** in its own `.claude/skills/`, copied from this repo's
   [`.claude/skills/`](.claude/skills/), with a `VENDORED.md` saying from which version. A
   product may keep its own copy of less-is-more with its own examples, but it keeps the five
   questions and the output.
2. **Require them in its AGENTS.md** for every new or changed screen, flow, sheet, notification
   and widget: used while designing, not only at the end, and written up in that app's audit
   file, one section per skill. The rule text to copy is in
   [docs/products.md](docs/products.md#the-three-design-skills).
3. **Re-copy them when they change here.** A skill update here is a release (patch), and its
   CHANGELOG entry tells every app to re-copy.

A new app gets the three skills in its first commit, with its row in the table above.

## How a change goes in

1. Branch, never push to `main` directly. One PR per change.
2. Edit `tokens/tokens.json` and/or the docs. Regenerate: `python3 scripts/gen_tokens.py`.
3. Run `python3 scripts/check_tokens.py` (CI runs it too). Zero errors.
4. Run the audit (above) and commit `audits/<date>-<topic>.md`.
5. Bump the version (below): `tokens.json` `version`, `VERSION`, a `CHANGELOG.md` entry that says
   what changed for each app and what the app has to do.
6. Open the PR with the template; it asks for the audit and the app impact.
7. **Merge it to `main` yourself** (squash), once CI is green, the audit has no open critical /
   P0 / P1 that the change introduces, and there are no unresolved review threads. The owner's
   standing instruction (2026-11-01, widened 2026-11-04): **in every repo, merge your PR when the
   work is finished and verified**; don't leave PRs waiting. That includes the app PRs that sync a
   change (step 8): merge each once its own tests and checks pass, in that repo's style (squash in
   NotTheOmiAIApp, a merge commit in PulseLoopAndroid). A release follows the app repo's own flow.
8. After merge, **sync the apps**. For a product that builds on the core in its own repo (Cochilo),
   that's a PR there that re-syncs its `design/core/` (its `design/core/CORE.md` says how); it
   checks itself with its own build. For the apps with a layer here ([docs/consuming.md](docs/consuming.md)), open a PR in each
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
- **One brand, one accent.** Mint `#43F3B7` is the brand and "tap here" (an app dressed in a
  partner's brand swaps the accent and the neutrals for the partner's, below). Text on mint is `on-mint`
  or `ink`, never white. Good/in-range is `success`, not mint. One filled mint action per screen.
- **One family.** Ubuntu Mono everywhere (regular, bold, bold italic), or the brand's family in an
  app that wears a brand: still exactly one family per app. Nothing that carries meaning
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
- **Every app updates itself the same way** ([docs/self-update.md](docs/self-update.md)): a check
  on every return to the foreground (at most every 15 minutes), the "Update available" sheet with the
  release notes and Update · {size} / Later, progress while downloading (with Cancel), Android's confirmation, and a "Check
  for updates" row in About. A download installs only when its SHA-256 matches the release's
  `SHA256SUMS.txt` and its signing key matches the installed app. Every app's release publishes
  that file. A new app ships with this from its first release.
- **Brands dress an app, they don't fork the system** ([docs/brands.md](docs/brands.md),
  `brands.*`). A brand swaps the app's colour roles and its one type family, and adds a mark.
  It never touches spacing, radii, sizes, motion, the type scale, data colours, components or any
  rule; `check_tokens.py` enforces it and re-checks every contrast pair with the brand on.
  A partner's brand is kept in the product's repo (Cochilo wears `tata-slings`, kept in Cochilo).
- **Fairy mode is part of the system.** When the profile name is Tatá's, the brand turns pink
  ([docs/fairy-mode.md](docs/fairy-mode.md), `variants.fairy`). It swaps brand tokens only, never
  neutrals, alerts, semantic or data colours. A new brand token (anything mint, or on mint) gets its
  `fairy-*` replacement in the same change; `check_tokens.py` fails a layer that carries half the
  variant and re-checks every contrast pair with the variant on. Every app with a profile name
  carries it. Don't announce it anywhere in the apps: it's a surprise for her.

## Never

- Edit `generated/` or `DESIGN.md`'s frontmatter by hand.
- Change a value in an app without changing it here first (that is drift; `drift.py` reports it).
- Merge without the three-skill audit, or skip/loosen a check to get green.
- Delete a "known" contrast exception without fixing the pair.
- Add a font, an icon set or a colour that isn't in `tokens.json`.
- Commit secrets, or anything from an app that isn't design (code, data, keys).

## Writing style

Short, plain and concrete, like the apps' own docs. Say what a rule does for the person using the
app. Docs mark items ✅ (done), 🟡 (built, to try in the apps) or ⬜ (not started). Commits carry
no `Co-Authored-By` trailer for agents (the PulseLoop owner's rule, applied here too).

# Changelog

Semantic versioning (AGENTS.md "Versioning"). Each entry says what changed for each app and what
the app has to do.

## 0.31.0 — 2026-11-04

**A fourth design skill: ux-user-flows** (minor: a rule added; no token or value changes).
- **New skill.** `ux-user-flows`, the owner's claude.ai skill, is in `.claude/skills/`. It decides
  what happens and in what order: the job, entry points, steps, branches, every state (empty,
  loading, error, offline), exits, forms, errors and onboarding, from Norman, Krug, NN/g, Baymard
  and WCAG 2.2. Its §13 flow review checklist has 15 questions.
- **The rule.** Every change here is audited with four skills, ux-user-flows first. A change with
  no flow in it says so in one line. The audit template and the PR checklist gain a ux-user-flows
  section.
- **The apps.** Every app carries the four skills and requires them on every screen and flow, in
  the order ux-user-flows, impeccable, graphic-design-fundamentals, less-is-more. Where a skill's
  general advice differs from this system (48dp targets, one mint action, the frame), the system
  wins (`docs/products.md`, "The four design skills").

What each app has to do:
- **NotTheOmiAIApp, PulseLoopAndroid and Cochilo:** copy `.claude/skills/ux-user-flows/` and the
  updated `less-is-more/SKILL.md` (its description now names four skills), update `VENDORED.md`
  to 0.31.0, and replace the "Three skills" rule in AGENTS.md with the four-skill text from
  `docs/products.md`. No token re-sync: the tokens are unchanged.

## 0.30.1 — 2026-11-04

Rule wording only (patch). The owner's standing instruction to merge widens from this repo to every
repo: an agent merges its PR, here and in the app repos, once the work is finished and verified
(AGENTS.md "How a change goes in", step 7).

What each app has to do: nothing in code. NotTheOmiAIApp's and PulseLoopAndroid's AGENTS.md say the
same.

## 0.30.0 — 2026-11-03

**A heart in the line set** (minor: an icon added; no token or value changes).
`assets/icons/android/gg_ic_heart.xml` is the same line set as the other icons: 22dp, a 24 viewport,
stroke 1.75, round caps and joins, tinted `ink` or `muted`. It's for care, favourites and notes
from a person, never for "like" counts.

What each app has to do:
- **Cochilo:** copy it in for the From Tatá tab (Cochilo 0.44.0).
- **The others:** nothing until they need it.

## 0.29.0 — 2026-11-03

**Three design skills, in every app** (minor: a rule added; no token or value changes).
- **New skill.** `less-is-more` is in `.claude/skills/`. It decides what earns its place on a
  screen: five questions per element, screen and flow rules, sources and a score. It came out of
  Cochilo's 0.43.0 declutter.
- **The rule.** Every change here is now audited with three skills: impeccable,
  graphic-design-fundamentals and less-is-more. The template and the PR checklist have a
  less-is-more section.
- **The apps.** Every app built on this boilerplate carries the three skills in its own
  `.claude/skills/` and requires them in its AGENTS.md on every screen and flow
  (AGENTS.md, `docs/products.md` "The three design skills").

What each app has to do:
- **Cochilo:** copy the three skills, with a `VENDORED.md`, and adopt the rule. Done in Cochilo
  0.43.0. No core re-sync is needed: the tokens are unchanged.
- **NotTheOmiAIApp (uikit) and PulseLoop:** copy `.claude/skills/{impeccable,graphic-design-fundamentals,less-is-more}`
  and add the rule text from `docs/products.md` to the repo's AGENTS.md, in the next sync PR.

## 0.28.0 — 2026-11-03

**Products keep their own brand and layer** (minor: no core value changes; Cochilo's layer, the
Tatá Slings brand and their files leave this repo). The owner's decision: this repo is his
boilerplate, in Gabriel's brand; a partner's brand and a product's own pieces live in the product.

- Versions 0.5.0 to 0.27.0 below were made from Cochilo, kept as patches in its repo and never
  merged here until now. This release brings in their generic parts:
  - the brands mechanism (`brands`, `check_brands`, brand-aware `colour_map`);
  - `theme_fallback`;
  - motion, large text and wide screens;
  - Filter chips, Checklist, Printable report;
  - the Conversation pattern and the model's labelled answer;
  - the Quiet link, the header's second icon;
  - "no text on a texture".
- It removes what is Cochilo's or Tatá's:
  - the `cochilo` layer and `brands.tata-slings` (`tokens.json`);
  - `generated/cochilo/` and `generated/web/cochilo.css`;
  - `drift.py --cochilo`;
  - the Tatá textures, `cochilo-tata-mark.svg`, `co-mark.svg` and Libre Franklin;
  - the Cochilo-only rows of `docs/components.md`;
  - the Tatá sections of `docs/brands.md`.

  They live in `gabrielbr/Cochilo`, `design/`.
- `gen_tokens.cochilo_kt` becomes `compose_kt(t, layer, package, object, intro)`, a Compose writer
  any product calls from its own build. Tested with a product-layer fixture.
- New: [docs/products.md](docs/products.md), how a product builds on the core (vendored core,
  brand and product layers in its repo, this repo's scripts unchanged) and where a change goes.
  AGENTS.md and README point to it.
- **uikit, PulseLoop:** nothing to do; only the version in the generated headers moves.
- **Cochilo:** re-sync `design/core/` to 0.28.0 (its `design/core/CORE.md`), and call `compose_kt`
  instead of `cochilo_kt`.
- Audit `audits/2026-11-03-v0.28.0-products.md`.

## 0.27.0 — 2026-11-03

The header's second icon (minor: a component rule; no token values change).

- components.md: the Header may hold two trailing icons when the second opens a screen used from
  every tab. Cochilo puts Ask (`gg_ic_chat`, already in the line set) before Settings. Cochilo 0.38.0.
- Audit `audits/2026-11-03-v0.27.0-header-ask.md`.

## 0.26.0 — 2026-11-03

The cascade, and asleep and awake (minor: a Cochilo motion token and a timeline pattern).

- Cochilo `motion-stagger` 35ms: the delay between items as a menu opens in a cascade.
  components.md: Cascade (Log menu), item by item, nearest the button first, on a soft arc.
  Cochilo 0.35.0.
- components.md: Vertical timeline, asleep and awake. The day as its two main states, with every
  other entry set in under the stretch it happened in; awake is a hollow ring, never a data colour.
  Cochilo 0.35.0.
- Audit `audits/2026-11-03-v0.26.0-cascade.md`.

## 0.25.0 — 2026-11-03

The Tatá note (minor: a component; no token values change).

- components.md: the Tatá note, a signed note with one Quiet link and "Don't show again", with the
  places it may never appear. Cochilo 0.32.0.
- Audit `audits/2026-11-03-v0.25.0-tata-note.md`.

## 0.24.0 — 2026-11-03

The Quiet link (minor: a component; no token values change).

- components.md: Quiet link, for the rare link out of an app; never teal, never a button, never on
  safety or logging surfaces. Cochilo 0.31.0 (the fabric's sling in the shop).
- Audit `audits/2026-11-03-v0.24.0-quiet-link.md`.

## 0.23.1 — 2026-11-03

Conversation: the model's answer (patch: a component note; no token values change).

- components.md: an on-device model's answer is always labelled under the card; a "thinking"
  card while it writes. Cochilo 0.30.0.
- Audit `audits/2026-11-03-v0.23.1-model-answer.md`.

## 0.23.0 — 2026-11-03

The Conversation pattern (minor: a component; no token values change).

- components.md: Cochilo's Ask screen: the question bubble, the answer card, suggested questions,
  fixed replies without alarm colours. Cochilo 0.29.0.
- Audit `audits/2026-11-03-v0.23.0-conversation.md`.

## 0.22.0 — 2026-11-03

Drag to adjust (minor: a component behaviour; no token values change).

- components.md: the vertical timeline's drag to adjust (hold, drag in 5-minute steps, `selected`
  while held, Undo, TalkBack actions). Cochilo 0.27.0.
- Audit `audits/2026-11-03-v0.22.0-drag-to-adjust.md`.

## 0.21.1 — 2026-11-03

Seamless fabrics (patch: assets only; no token values change).

- `assets/textures/tata-slings/`: the eleven crops are now true repeating tiles, drawn repeated,
  not mirrored. Cochilo 0.26.0.
- Audit `audits/2026-11-03-v0.21.1-seamless-fabrics.md`.

## 0.21.0 — 2026-11-03

Wide screens (minor: four Cochilo size tokens; no colour changes).

- Cochilo `size`: `rail` 80, `content-max` 600, `width-medium` 600, `width-expanded` 840 (Android's
  window classes). components.md: the Navigation rail, and Today beside a second tab when expanded.
- Audit `audits/2026-11-03-v0.21.0-wide-screens.md`.

## 0.20.0 — 2026-11-03

Large text (minor: an accessibility rule; no token values change).

- accessibility.md: headers and bars use min heights, chip rows flow, and the label scale cap
  (150%) for icon-backed tab labels and chart axis ticks only. Cochilo keeps 200% screenshots.
- Audit `audits/2026-11-03-v0.20.0-large-text.md`.

## 0.19.0 — 2026-11-02

Cochilo's day ring shows the expected window (patch: a component note; no token values change).

- Ring: an expected window as the nap colour at 35%, under the data, named in the legend and
  spoken. History filter chips reuse Filter chips.
- Audit `audits/2026-11-02-v0.19.0-reading.md`.

## 0.18.0 — 2026-11-02

The Printable report (minor: a component; no token values change).

- **Printable report** (components.md): Cochilo's one-page PDF for the paediatrician.
- Audit `audits/2026-11-02-v0.18.0-report.md`.

## 0.17.0 — 2026-11-02

The Checklist component (minor: a component; no token values change).

- **Checklist** (components.md), for Cochilo's routine steps; uses the existing `gg_ic_check`.
- Audit `audits/2026-11-02-v0.17.0-rituals.md`.

## 0.16.0 — 2026-11-02

Where the baby slept (patch: a component variant; no token values change).

- Filter chips: a dark variant for the night panel (outlines in `on-panel-muted`, text `on-panel`;
  picked stays the `selected` blush).
- Audit `audits/2026-11-02-v0.16.0-places.md` (T.I.C.K.S. wording: the parent watches, never the app).

## 0.15.0 — 2026-11-02

Earlier chips and the quick-settings tile (minor: two components; no token values change).

- **Earlier chips**: a sentence of hairline pills under the sleep panel's action.
- **Quick-settings tile**: Start sleep / Woke up in the shade, with the system's tile states.
- Audit `audits/2026-11-02-v0.15.0-earlier-tile.md`.

## 0.14.0 — 2026-11-02

Cochilo's night light: a third theme (minor: a theme and a fallback rule; no light or dark value
changes).

- Layers may ship more themes than light and dark, with `theme_fallback` (`{"night": "dark"}`): a
  theme spells out only the roles it changes; `tokens_lib.colour_map` fills the rest, so the
  generator, the checks and drift all see the full theme. CSS emits `[data-theme="night"]` with
  no media query (only dark has a system preference).
- `cochilo` gains **night**: warm amber and red on near-black, no blue or teal. Brand roles:
  page `#0D0806`, surface `#170F0B`, ink `#E9A25F`, muted `#B67A47`, mint `#E0A060`, fab
  `#B8642F`, selected `#3A2416`, frame-line `#241610`; nine warm event colours and rounds. Every
  contrast pair passes in night too. Illustration colours fall back to dark (unchanged).
- Tests: the night palette is complete.
- Audit `audits/2026-11-02-v0.14.0-night.md`.
- **Cochilo:** copy `CTokens.kt`; `CochiloTheme(dark, night)` picks `CTokens.Night` 19:00–07:00.

## 0.13.0 — 2026-11-02

Celebrations (minor: a component; no token values change).

- Component **Celebration** (components.md): a blush card with the happy Baby avatar and one
  line, rising in and settling away by itself; quiet at night. Rules: celebrate, never scold;
  never a promise; at most three a day.
- Audit `audits/2026-11-02-v0.13.0-celebrations.md`.
- **Cochilo:** `CelebrationCard`, `domain/Celebrations.kt`.

## 0.12.0 — 2026-11-02

The baby avatar (minor: an illustration palette, a size and two components).

- `cochilo` illustration palette, the same in both themes: six skin tones `illustration-skin-1..6`
  (`#F6D7C3` to `#5E3A26`), hair black / brown / blond / red, `illustration-cheek`,
  `illustration-face-line` `#241A1C`, `illustration-catchlight`, the Rosa Chá `illustration-wrap`
  and `illustration-wrap-edge`, and the Amora `illustration-bow`. Never UI state, never text.
- Size `avatar` 112px.
- Components **Baby avatar** and **Look picker** (components.md). The picker asks how the baby
  looks (skin tone, hair), never race; girl / boy / rather not say changes details only.
- Audit `audits/2026-11-02-v0.12.0-avatar.md`.
- **Cochilo:** copy `CTokens.kt`; `BabyAvatar`, `LookPicker`, onboarding.

## 0.11.0 — 2026-11-02

Cochilo softer: a review for "feminine and maternal" (minor: roles added; Cochilo values change).

- New `cochilo` roles `selected` / `on-selected` (default mint / on-mint) for what is picked
  (active tab, picked chip) and `frame-line` (default mint) for the frame. `brands.tata-slings`
  makes them a Rosa Chá/Amora blush `#F6DDE3` / `#4A2D40` and a Rosa Chá hem `#F1D9D3` /
  `#2A2030`, so teal is only the one action. Contrast `on-selected` on `selected` passes.
- Cochilo type: caption sentence case, 13/18, 600, no tracking; display 600.
- Cochilo dark `event-*-soft` tints lifted a step (line on round still ≥ 3:1).
- Components (Cochilo column): Screen title without the highlighter; Frame on `frame-line`; Tab
  bar and filter chips on `selected`; buttons are pills (`radius-round`).
- Audit `audits/2026-11-02-v0.11.0-softer.md`.
- **Cochilo:** copy `CTokens.kt`; drop the highlighter; use the new roles; pill buttons.

## 0.10.0 — 2026-11-02

Cochilo's home-screen widget (minor: a component; no token values change).

- Component **Home widget** (components.md): status line with a running clock, then one row of
  48dp buttons, the mint action first and wider, then the two breasts with the Last mark; a
  running breastfeed's side is lit (`event-feed-soft`, `outline`) and reads Finish. Built from the
  layer's tokens, copied into the app's resources because a RemoteViews layout can't read them;
  a test in the app checks the copies.
- **Cochilo:** `CochiloWidget`, `res/layout/widget_cochilo.xml`.

## 0.9.0 — 2026-11-02

Cochilo: sleep leads, the last-used mark and motion (minor: two size tokens and a component).

- `kind-badge-lead` 44px: sleep's icon round, a size up from `kind-badge`, so sleep leads lists,
  menus and timelines (sleep is what Cochilo is for).
- `outline` 2px: the last-used option's outline and the picked swatch's ring.
- Component **Last mark**: the option used last time has an `outline` in its kind's `event-*`
  colour and a `space-2` dot of that colour before its name; the word "last" is only spoken
  (TalkBack), never shown. Replaces the LAST caption.
- Motion in Cochilo (docs/components.md, "Motion"): press scale on every target, the Log menu
  rising from its button, colour cross-fades on every state change, lists that grow instead of
  jumping; `motion-standard` / `motion-emphasised` only, all off with Remove animations.
- **Cochilo:** copy `CTokens.kt`; draw the Last mark; sleep rows use `kind-badge-lead` and the
  label role.

## 0.8.0 — 2026-11-02

Brand textures: Cochilo can wrap its Today card in one of Tatá's real fabrics (minor: assets and
two components added; no token values change).

- `assets/textures/tata-slings/`: eleven 384px WebP crops of her slings (8 plain, 3 prints), with
  source and permission (README there).
- docs/brands.md "Textures": a brand may bring product textures; never behind text; shown only in
  a Fabric frame band or a picker swatch, picked by the person.
- Components: Fabric frame, Fabric picker (components.md).
- **Cochilo:** ship the textures (`res/drawable-nodpi/`), `FabricFrame` round the sleep panel,
  `FabricPicker` in Settings › Appearance.

## 0.7.0 — 2026-11-02

Cochilo in her fabrics ("Tecidos"): warmer, more colourful, made for the mothers who use it
(minor: tokens and a component added; only the `cochilo` layer and `brands.tata-slings` change).

- `cochilo` data colours become Tatá's fabrics: `event-night` Lavanda `#5B4B8A`, `event-nap`
  Imensidão `#3D6FA3`, `event-feed` Rosa Chá `#B0503F`, `event-pump` Amora `#8A3566`,
  `event-diaper` Trevo `#3E7350`, `event-daylight` Mel `#8C6A00`; new `event-routine` (Turquesa
  `#1E6E68`), `event-medicine` (Cereja `#A3324A`) and `event-note` (Capuccino `#7A5A44`), so
  every kind of entry has its colour. Each gets `event-*-soft`, the round behind its icon.
- `fab` / `on-fab` (layer default `{ink}` / `{page}`): the Log button. The brand makes it Amora.
- `kind-badge` 36px: the round of colour behind a kind's 22dp icon (component "Kind icon").
- Cochilo's corners are rounder: its `radius-s` is 8 and `radius-m` 16 (the system's m and l
  values); `radius-l` and `radius-round` unchanged.
- `brands.tata-slings`: ink navy → plum-grey `#2B2233`, page `#FBF5F1` (Pérola with a blush),
  rosé `line`, plum night `panel` `#2E2238`, plum-black dark theme. Teal stays the one action.
- Contrast: new pairs for `fab`, the three new event colours on page and surface, and every
  `event-*` on its `-soft` round (≥ 3:1, WCAG 1.4.11). All pass.
- Docs: brands.md (what the brand and the layer each changed), components.md (Kind icon, Log
  button in Amora). Audit `audits/2026-11-02-v0.7.0-tecidos.md`.
- **Cochilo:** copy `generated/cochilo/CTokens.kt`; draw kinds' icons in their round
  (`event-*` line on `event-*-soft`); the Log button on `fab`.

## 0.6.0 — 2026-11-02

Brands join the system, and Cochilo wears the first one: it ships as Cochilo, da Tatá Slings
(minor: a concept, tokens and assets added; no other app's values change).

- `brands` in tokens.json: a brand swaps an app's colour roles and its one type family, and adds a
  mark; never spacing, radii, sizes, motion, the type scale, data colours, components or rules.
  A layer opts in with `"brand"`. `brands.tata-slings`: teal `#5DC2BB` accent, navy `#13293D`
  ink, Pérola `#FBF7F2` page, Cereja alerts, navy sleep panel, Libre Franklin. Measured from
  tataslings.com.br.
- `tokens_lib`: `brand()`, `brand_usage()`; `colour_map` applies the brand, so generator,
  contrast checks and drift see the app as it ships.
- Generator: `CTokens.kt` gains `object Brand { key, name, fontFamily }`, and replaced colours say
  so; CSS `--gds-font` follows the brand.
- `check_tokens.py`: `check_brands` (only colour roles the layer has, never data colours, every
  theme, family and faces named, nothing else). `check_shared_light` now runs on the Views kit only
  (the only consumer that looks dark values up by light value). Tests for both.
- Assets: Libre Franklin 400/600/700 + OFL licence; `assets/logos/cochilo-tata-mark.svg`.
- Icons (same line set, 22dp, stroke 1.75), one per kind of Cochilo entry so entries are known at a
  glance, always beside their name: `gg_ic_breast` (a drop), `gg_ic_bottle`, `gg_ic_spoon`,
  `gg_ic_pump`, `gg_ic_diaper`, `gg_ic_routine` (a bath), `gg_ic_note` (a pencil),
  `gg_ic_medicine` (a capsule); and `gg_ic_info` (the "i" beside an action) and `gg_ic_day`
  (Cochilo's Day tab).
- Docs: docs/brands.md; AGENTS.md rules (one accent / one family per app, brands); README.
- Audit: `audits/2026-11-02-v0.6.0-brands.md`.
- **Cochilo:** copy `generated/cochilo/CTokens.kt`; ship Libre Franklin and switch the type family;
  swap the `CO_` monogram and launcher icon for the mark; copy the new icons.
- **NotTheOmiAIApp, PulseLoop:** nothing to do (their generated files only change version lines).

## 0.5.0 — 2026-11-02

Cochilo joins the system (minor: a layer, tokens and assets added; no existing value changed).

- New `cochilo` layer (Compose, light + dark): every core token, uikit's type roles, sizes and
  spacing, `panel`/`on-panel`/`on-panel-muted`, `snackbar` and `snackbar-action` (uikit's values),
  six data hues `event-night`, `event-nap`, `event-feed`, `event-pump`, `event-diaper`,
  `event-daylight` (3:1+ on page and surface in both themes), sizes `row-min` 56 and `timeline` 24.
- Generator: `generated/cochilo/CTokens.kt` and `generated/web/cochilo.css`. `drift.py --cochilo`.
- Assets: `CO_` mark; icons `gg_ic_chart`, `gg_ic_moon`, `gg_ic_sun` (same line set).
- Docs: apps tables, components (Sleep panel, Timeline / actogram), divergence D-11 (night viewing).
- Audit: `audits/2026-11-02-v0.5.0-cochilo.md`.
- **NotTheOmiAIApp:** nothing to do (only the version in `UiTokens.java`'s header line changed).
- **PulseLoop:** nothing to do.
- **Cochilo:** copy `generated/cochilo/CTokens.kt` in (its first version already carries it).

## 0.4.0 — 2026-11-02

Self-update becomes a system component: PulseLoop's update feature is the standard for every app.

- docs/self-update.md: what the person sees (the "Update available" sheet, About's "Check for
  updates"), the rules (foreground checks at most every 15 minutes with ETag, what counts as newer,
  which file, the checks before install, honest failures, privacy, permissions), the words in English
  and Portuguese, and how each platform builds it.
- A download installs only when its SHA-256 matches the release's `SHA256SUMS.txt` (from GMind) and
  its signing key matches the installed app.
- Components: Update sheet, Check for updates. AGENTS.md rule. Divergence D-11.
- **PulseLoop:** publish `SHA256SUMS.txt` with each release and refuse a download that doesn't
  match; translate the update texts.
- **NotTheOmiAIApp:** each app (GVoice, GMind, GMoney, GHealth, GDesk) updates itself through
  `br.gabriel.ui.update`; GMind keeps first installs of GMoney, GHealth and GDesk. GMoney and GHealth
  gain internet access and every app gains install permission (owner's call).

## 0.3.0 — 2026-11-01

Fairy mode joins the system: the pink variant PulseLoop shows when the profile name is Tatá's.

- `variants.fairy` in tokens.json: the match rule, five colours that each replace one brand token
  (`fairy-accent` → mint, `fairy-on-accent` → on-mint, `fairy-accent-soft` → mint-soft,
  `fairy-rem` → stage-rem, and new `fairy-action` → snackbar-action), and the celebration's values.
- `check_tokens.py`: a layer that carries any variant colour must carry the replacement of every
  replaced token it has, and every contrast pair is checked again with the variant on.
  CSS gets `[data-variant="fairy"]`.
- docs/fairy-mode.md: who it's for, what changes and what never does, the transformation, the
  lifecycle, and how to build it in Compose (done), the Views kit (to do) and the web.
- AGENTS.md: Fairy mode is part of the system; a new brand token gets its fairy replacement.
- **NotTheOmiAIApp:** copy `generated/uikit/UiTokens.java` (adds `FAIRY_ACCENT`,
  `FAIRY_ON_ACCENT`, `FAIRY_ACTION`; nothing uses them until the kit builds Fairy mode, D-10).
- **PulseLoop:** nothing; `GTokens.kt` is unchanged.

## 0.2.1 — 2026-11-01

Docs only: the app syncs are open (NotTheOmiAIApp#245 retires that repo's own token copy and fixes
the kit; PulseLoopAndroid#55 makes PulseColors read GTokens). docs/consuming.md and D-8 say so.
No app has anything new to do.

## 0.2.0 — 2026-11-01

Fixes the kit's three contrast failures from the 0.1.0 audit, and a fourth found while fixing them.

- **New uikit tokens:** `on-coral` (`#17161A` both themes) for the Stop label and icon, replacing
  white (A-1, 3.6:1 → 5.0:1); `snackbar-action` (`#43F3B7` light, `#0A7A55` dark) for the
  snackbar's action, replacing mint (A-2, 1.3:1 → 4.8:1 in dark).
- **`"pair": true`** on uikit colours that share a light value with an earlier token (`panel`,
  `on-panel`, `on-coral`, `snackbar-action`). The kit looks dark values up by light value, so
  `panel` drew `#F2F2F2` instead of `#000000` in dark and the player's times were 2.1:1 (A-10).
  `check_tokens.py` enforces the mark; the generated comment says how to read the token.
- `coral`'s usage text no longer states the wrong rule; `drift.py` prints a unified diff and
  understands PulseLoop reading `GTokens.Colors.*`; AGENTS.md: agents merge their own PRs here.
- **NotTheOmiAIApp:** copy `generated/uikit/UiTokens.java`; in `Ui.java` read `PANEL`, `ON_PANEL`,
  `ON_CORAL`, `SNACKBAR_ACTION` as pairs, use `ON_CORAL` on Stop, `SNACKBAR_ACTION` on the
  snackbar, and draw the tab badge 12sp coral-text on coral-soft (A-3).
- **PulseLoop:** nothing changes in value; adopt `generated/pulseloop/GTokens.kt` (comment text
  for `coral` changed).

## 0.1.0 — 2026-11-01

First version: captures what both apps ship today. No value changed.

- `tokens/tokens.json` with `core` and the `uikit` and `pulseloop` layers; generators for Java,
  Kotlin, CSS and DESIGN.md; `check_tokens.py`; `drift.py` (both apps: 0 differences).
- Rules (AGENTS.md), DESIGN.md, PRODUCT.md, docs, the divergences register (D-1…D-9).
- Assets: Ubuntu Mono with its licence, `GV_`/`GM_` marks, the `gg_ic_*` icon set.
- Audit skills vendored; first audit `audits/2026-11-01-v0.1.0.md` (open: A-1…A-9).
- **NotTheOmiAIApp:** nothing to do; `generated/uikit/UiTokens.java` equals the app's file.
- **PulseLoop:** nothing to do; `PulseColors` equals the `pulseloop` layer.

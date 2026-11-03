# Components

One name per component across apps. uikit = `br.gabriel.ui.Ui` (NotTheOmiAIApp); Compose =
PulseLoop's `ui/components`. Status: ✅ both, 🟡 one app, ⬜ to build.

A product that keeps its own layer in its own repo (Cochilo, [products.md](products.md)) lists its
own components there; only components any app can use are here. Rows still name Cochilo where it
was the first to use a generic component.

| Component | Spec | uikit | Compose | Status |
|---|---|---|---|---|
| Frame | 4dp mint border; loading line (uikit). Cochilo: `frame-line`, a soft hem under the brand | `FrameDrawable`, `FrameSweep`, `Motion.loading` | `AppChrome` frame | ✅ |
| Header | 56dp; monogram 32 / app name over one status line / one trailing icon, at most two when the second opens a screen used from every tab (Cochilo: Ask, then Settings; `space1` apart, 48dp each) | `Ui.header`, `Ui.backHeader` | `AppHeader` (greeting + headline line, ring pill, gear) | ✅ |
| Tab bar | 64dp; active = mint pill behind the icon (Cochilo: `selected` blush); badge 12sp bold coral-text on coral-soft | `Ui.tabBar` | `NavigationBar`, `NavigationRail` from 600dp | ✅ |
| Navigation rail | `rail` 80dp wide, from `width-medium` (600dp): the same tabs stood on their side, the same `selected` pill and words; the screen's column stays at most `content-max` (600dp), centred. From `width-expanded` (840dp) Cochilo shows Today beside the picked tab (Day when Today is picked) | `Ui.rail` | `NavigationRail` | ✅ |
| Screen title | uikit: display 30/36, one word on the mint highlighter. PulseLoop tabs have no title. Cochilo (0.11.0): display 600 in ink, no highlighter | `Ui.title` | — | 🟡 |
| Section caption | 12/16 bold caps muted, 40 above, 12 below, no divider. Cochilo: 13/18 semibold, sentence case | `Ui.caption` | `PulseType.eyebrow` | ✅ |
| Row group | rows on surface, radius 8, inset 16, hairline between rows | `RowGroups` | `SettingsComponents` | ✅ |
| Row | 48dp min (uikit 56); label + ≤ 1 meta line; one thing on the right | `Ui.row` | settings rows | ✅ |
| Switch row | the whole row toggles, Role.Switch | `Ui.switchRow` | `Modifier.switchRow` (`A11y.kt`) | ✅ |
| Item row | title, chip, meta, 2-line excerpt | `Ui.itemRow` | — | 🟡 |
| Button | 52dp (Cochilo: a pill, `radius-round`); PRIMARY mint (one per screen), SECONDARY ink outline, DANGER coral-text outline + confirm, STOP solid coral with `on-coral` label | `Ui.button` | Material `Button`/`FilledTonalButton`; one filled accent per screen (Actions) | ✅ |
| Icon button | 48dp target, 22dp icon, content description | `Ui.iconButton` | `IconButton` | ✅ |
| Chip | read-only state; MINT / CORAL (text on tint) / MUTED | `Ui.chip` | chips with dither ground | ✅ |
| Filter chips / segmented | 32dp pills, selection semantics. Cochilo: picked = `selected` blush; a dark variant on the night panel (outlines in `on-panel-muted`, text `on-panel`) | `Ui.filterChips` | `PulseSegmented` | ✅ |
| Field | 52dp, radius 4, line border; search clears | `Ui.field` | `OutlinedTextField` | ✅ |
| Snackbar | ink ground, page text, `snackbar-action` action, 8 s | `Ui.snackbar` | `SnackbarHost` (⬜ replace remaining Toasts) | 🟡 |
| Sheet | title, one line, primary + secondary; confirms and permission reasons | `Ui.sheet` | `ModalBottomSheet` / `LogSheet` | ✅ |
| Recorder panel / player | panel colours, timer 56/64, −15 s, scrubber | `Ui.recorderPanel`, `Ui.player` | — | 🟡 |
| Empty state | title 22/28, one line, ≤ 1 primary | `Ui.emptyState` | — | 🟡 |
| Skeleton | grey bars instead of "Loading…" text | `Ui.skeletonRow` | — | 🟡 |
| Ring / gauge | swept fill 900ms, dithered track, spoken summary. Cochilo day ring: today's expected next-sleep window as the nap colour at 35% under the real sleeps, named in the legend and spoken | — | `VitalRingGauge`, `ActivityRings` | 🟡 |
| Charts | one message per chart, zone colours, spoken summary | — | `Charts`, `ZoneLineChart` | 🟡 |
| Update sheet | "Update available · {version}", release notes, Update · {size} (primary) / Later; "Downloading… n%" with the frame's line, Later becomes Cancel — [self-update.md](self-update.md) | `Ui.updateSheet` | `UpdateDialog` | 🟡 |
| Check for updates | About row: version, a secondary button, one result line; release builds only — [self-update.md](self-update.md) | `Ui.checkForUpdates` | `CheckForUpdatesButton` | 🟡 |
| Conversation (Ask) | Cochilo: the parent's question right-aligned in `selected` / `on-selected`, at most half the column plus 64dp; the answer a `surface` card with a hairline, meta labels ("From your log", "What can help", the source) over body text; suggested questions as filter chips; one teal Ask. Fixed replies for health, medicine and the parent's wellbeing use the same card, no colour alarm. An answer written by an on-device model uses the same card with a meta label under it that says so, always; while it writes, a meta "Thinking, on this phone…" card (a live region) | — | Cochilo `AskScreen` | ✅ |
| Quiet link | A line of context in `muted` meta, then the action in `ink` meta and a chevron, in a 48dp row; the whole row is one button for TalkBack with a full spoken sentence. For the rare link out of the app (Cochilo: the picked fabric's sling in the shop). Never `mint`, never a filled or outlined button, never more than one per screen, never on a safety or logging surface | — | Cochilo `QuietLink` | ✅ |
| Checklist | Cochilo: steps ticked one by one in a row group; a ticked step has `gg_ic_check` in a `selected` blush round (`kind-badge`), the words unchanged (no strike); each row a checkbox | — | Cochilo `Checklist` | 🟡 |
| Printable report | Cochilo: one A4 page (595 × 842 pt), 48pt margin, light theme: title (22 bold), subtitle with absolute dates, sections (11 semibold muted captions, 11pt rows with values on the right edge, hairlines), 14 day bars in data colours with a legend, footer "not a medical record" | — | Cochilo `Report` | 🟡 |
| Fairy transformation | once, over everything; glow, wand, sparkles, "Tatá, te amo!"; 4.2s (1.4s reduced) — [fairy-mode.md](fairy-mode.md) | ⬜ | `FairyTransformOverlay` | 🟡 |

**Motion.** Every target scales to 97% while pressed (`motion-standard`). A menu or sheet that
opens fades and rises (`motion-emphasised`). Every state change of colour cross-fades
(`motion-standard`): a lit option, a chip, a tab. Lists grow and shrink instead of jumping
(`motion-emphasised`). A menu's items may come in one after another, a short stagger apart (a product token; Cochilo's is 35ms). The
easing is the system's. With Remove animations on, every one of them snaps.

Rules for every component: built from tokens only; 48dp targets; TalkBack reads label + value +
state; states (default, pressed, disabled, loading, empty, error) defined before it ships; a new
component, or a change to one, is added to this table in the same PR.

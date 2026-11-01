# Components

One name per component across apps. uikit = `br.gabriel.ui.Ui` (NotTheOmiAIApp); Compose =
PulseLoop's `ui/components`. Status: ✅ both, 🟡 one app, ⬜ to build.

| Component | Spec | uikit | Compose | Status |
|---|---|---|---|---|
| Frame | 4dp mint border; loading line (uikit) | `FrameDrawable`, `FrameSweep`, `Motion.loading` | `AppChrome` frame | ✅ |
| Header | 56dp; monogram 32 / app name over one status line / one trailing icon | `Ui.header`, `Ui.backHeader` | `AppHeader` (greeting + headline line, ring pill, gear) | ✅ |
| Tab bar | 64dp; active = mint pill behind the icon; badge 12sp bold coral-text on coral-soft | `Ui.tabBar` | `NavigationBar`, `NavigationRail` from 600dp | ✅ |
| Screen title | uikit: display 30/36, one word on the mint highlighter. PulseLoop tabs have no title | `Ui.title` | — | 🟡 |
| Section caption | 12/16 bold caps muted, 40 above, 12 below, no divider | `Ui.caption` | `PulseType.eyebrow` | ✅ |
| Row group | rows on surface, radius 8, inset 16, hairline between rows | `RowGroups` | `SettingsComponents` | ✅ |
| Row | 48dp min (uikit 56); label + ≤ 1 meta line; one thing on the right | `Ui.row` | settings rows | ✅ |
| Switch row | the whole row toggles, Role.Switch | `Ui.switchRow` | `Modifier.switchRow` (`A11y.kt`) | ✅ |
| Item row | title, chip, meta, 2-line excerpt | `Ui.itemRow` | — | 🟡 |
| Button | 52dp; PRIMARY mint (one per screen), SECONDARY ink outline, DANGER coral-text outline + confirm, STOP solid coral with `on-coral` label | `Ui.button` | Material `Button`/`FilledTonalButton`; one filled accent per screen (Actions) | ✅ |
| Icon button | 48dp target, 22dp icon, content description | `Ui.iconButton` | `IconButton` | ✅ |
| Chip | read-only state; MINT / CORAL (text on tint) / MUTED | `Ui.chip` | chips with dither ground | ✅ |
| Filter chips / segmented | 32dp pills, selection semantics | `Ui.filterChips` | `PulseSegmented` | ✅ |
| Field | 52dp, radius 4, line border; search clears | `Ui.field` | `OutlinedTextField` | ✅ |
| Snackbar | ink ground, page text, `snackbar-action` action, 8 s | `Ui.snackbar` | `SnackbarHost` (⬜ replace remaining Toasts) | 🟡 |
| Sheet | title, one line, primary + secondary; confirms and permission reasons | `Ui.sheet` | `ModalBottomSheet` / `LogSheet` | ✅ |
| Recorder panel / player | panel colours, timer 56/64, −15 s, scrubber | `Ui.recorderPanel`, `Ui.player` | — | 🟡 |
| Empty state | title 22/28, one line, ≤ 1 primary | `Ui.emptyState` | — | 🟡 |
| Skeleton | grey bars instead of "Loading…" text | `Ui.skeletonRow` | — | 🟡 |
| Ring / gauge | swept fill 900ms, dithered track, spoken summary | — | `VitalRingGauge`, `ActivityRings` | 🟡 |
| Charts | one message per chart, zone colours, spoken summary | — | `Charts`, `ZoneLineChart` | 🟡 |
| Fairy transformation | once, over everything; glow, wand, sparkles, "Tatá, te amo!"; 4.2s (1.4s reduced) — [fairy-mode.md](fairy-mode.md) | ⬜ | `FairyTransformOverlay` | 🟡 |

Rules for every component: built from tokens only; 48dp targets; TalkBack reads label + value +
state; states (default, pressed, disabled, loading, empty, error) defined before it ships; a new
component, or a change to one, is added to this table in the same PR.

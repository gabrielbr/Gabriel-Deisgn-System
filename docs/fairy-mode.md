# Fairy mode (Tatá's version)

A private variant for one person, the owner's wife, Tatá. When the name on the app's profile is
hers, the app plays a short fairy transformation once and from then on wears **pink instead of
mint**, with smooth washes where PulseLoop draws its bitmap dither. It is a gift, not a feature:
no setting, no menu item, no mention anywhere until it happens.

Status: ✅ PulseLoop (`ui/theme/FairyMode.kt`, `ui/components/FairyTransform.kt`) ·
⬜ GVoice, GMind, GMoney, GHealth, GDesk (instructions below).

Tokens: `variants.fairy` in [`tokens/tokens.json`](../tokens/tokens.json).

## Who it's for

It turns on when the **first word** of the profile name is `tata`, `thaissa` or `thaisa`, ignoring
case and accents (Unicode NFD, combining marks removed, lower-cased).

| Matches | Doesn't |
|---|---|
| Tatá, Tata, tata, TATÁ, Thaissa, thaíssa, Thaissa Silva, "  Tatá  " | (empty), Gabriel, Tatiana, Thais, Ana Tata |

The names live in code (`variants.fairy.match` here, a constant in each app). They are not a
secret, but they are personal: never log them, send them anywhere, or show them in the UI.

## What it changes

Only the brand. A variant colour **replaces** one token; everything else stays as it is.

| Token | Normal | Fairy | Where it shows |
|---|---|---|---|
| `mint` | `#43F3B7` | `fairy-accent` `#FF8FC7` | the frame, the one primary action, the title highlighter, the active tab pill, progress chips, PulseLoop's readiness ring |
| `on-mint` | `#033423` | `fairy-on-accent` `#3D0A26` (7.9:1 on pink) | text and icons on the accent |
| `mint-soft` (PulseLoop) | mint 18% | `fairy-accent-soft` pink 18% | `primaryContainer` washes |
| `stage-rem` (PulseLoop) | `#5AD8F0` | `fairy-rem` `#FFB3DA` | REM in the hypnogram |
| `snackbar-action` (uikit) | `#43F3B7` / `#0A7A55` | `fairy-action` `#FF8FC7` / `#B4246E` | the snackbar's action (8.6:1 light, 5.5:1 dark) |

And two textures (PulseLoop):

- **Dither → smooth wash.** Wherever a colour is drawn through the Bayer dither, Fairy mode draws it
  at the same strength as a soft alpha wash instead, with no outline round the text on it.
- **The screen wipe** becomes a smooth diagonal gradient with a pink glow at its edge, not dots.

### What it never changes

Neutrals (page, surface, ink, muted, line), coral and every alert, `success` / `warning` / `info`,
the data palette (metrics, zones, sleep stages other than REM), type, spacing, shape, layout, copy
and behaviour. Health meaning must not move because the brand did: a red zone is still red, a
recording is still coral.

## The transformation

Plays **once**, the first time the name matches, over everything (`FairyTransformOverlay`):

1. A radial glow fades in: deep plum `#2A0A1E` at the edges, rose `#FF5FA8`, light pink `#FFD6EC`
   at the heart (`celebration.glow`).
2. With animations on, a wand's trail of small stars sweeps from the bottom left to the centre.
3. At **45%** of the run (`switchAt`), under the brightest moment of the glow, the app turns pink;
   the 4dp frame flows from mint to pink over 1200ms (`frameFadeMs`) rather than snapping.
4. A burst of hearts, stars and dots in the sparkle colours (`celebration.sparkles`) drifts out
   and up, and "Tatá, te amo!" rises in, 36sp bold white, with 💗 under it.
5. The glow fades out over the last 15%. Touches are swallowed until it ends.

| | Animations on | "Remove animations" on |
|---|---|---|
| Length | 4200ms | 1400ms |
| Particles | 90 | 18 |
| Wand | yes | no |

The line is translated through the app's usual strings (`pt-BR`: "Tatá, te amo!"). The 💗 is
content, a word in the message, so it doesn't break the "no emoji as icons" rule.

## Lifecycle

- **Turning on:** the first match starts the transformation; the palette flips at `switchAt`, and
  the "on" state is saved when it does (and again when it ends, in case it was interrupted).
- **Staying on:** saved per app (PulseLoop: SharedPreferences `fairy` / `on`), read at app start
  before the first frame, so a cold start is already pink.
- **Turning off:** when the name no longer matches, the app goes back to mint at once, quietly; no
  reverse ceremony. Changing back to her name plays the transformation again.
- **Not in the backup:** it follows the name, which is in the profile; restoring a profile with her
  name turns it on with a transformation, as on a new phone.

## Building it in an app

Every app that has a profile name carries the variant. The rules, whatever the platform:

1. **One switch, observable.** A single `FairyMode.on` the whole UI recomposes or redraws from.
2. **Swap tokens, not screens.** Read the brand colours through one place that returns the
   `fairy-*` value when on (PulseLoop: `PulseColors` getters). No screen checks `FairyMode` itself,
   except texture code (dither, wipe) that has no colour to swap.
3. **Match exactly as above**, with a unit test that has the two lists from "Who it's for".
4. **Celebrate once**, honouring "Remove animations", with the line in the app's strings.
5. **Check it:** screenshot tests of a few screens with the variant on, in every theme the app
   ships; `check_tokens.py` already checks the swapped contrast pairs.

### Compose (PulseLoop) ✅

`FairyMode` (snapshot state: `on`, `celebrating`; `init(context)` from the Application;
`onProfileName(name)` from a `LaunchedEffect` on the profile's name; `transform()`,
`celebrationDone()`), `FairyMode.Palette` (reads `GTokens.Colors.fairy*`), `PulseColors` brand
getters, `Dither` / `DitherTransition` texture branches, `FairyTransformOverlay` mounted last in
`MainActivity` so it covers everything. Tests: `FairyModeTest`.

### Views kit (GVoice, GMind, GMoney, GHealth, GDesk) ⬜

`UiTokens` already carries `FAIRY_ACCENT`, `FAIRY_ON_ACCENT` and `FAIRY_ACTION` (+ `_DARK`).
To build it:

1. Add `Fairy` to `ui-kit` (`br.gabriel.ui`): `on(Context)`, `matches(String)` and
   `onProfileName(Context, String)`, stored in SharedPreferences `gg_fairy`, like `Theme`.
2. In `Ui.color(Context, int)`, after resolving the theme: when `Fairy.on(c)`, return
   `FAIRY_ACCENT` for `MINT` and `FAIRY_ON_ACCENT` for `ON_MINT`. Read `SNACKBAR_ACTION` as a pair
   and swap it for the `FAIRY_ACTION` pair. Places that use `UiTokens.MINT` or `UiTokens.ON_MINT`
   raw (button labels on mint, the frame, the meter) go through the same helper.
3. The frame (`FrameDrawable`) animates its colour from mint to pink over 1200ms on the switch.
4. A celebration overlay for Views (a full-screen `View` drawing the glow, wand and sparkles from
   `variants.fairy.celebration`), shown once from the launcher activity.
5. **Where the name comes from:** GMind's own name (asked at first run). GMoney, GHealth and GDesk
   draw GMind's pages and should follow GMind's choice. GVoice has no name field: it follows GMind
   when GMind is installed. ⬜ To decide when it's built: share the flag between the apps or keep
   it per app.

### Web (prototypes, canvases)

Set `data-variant="fairy"` on the root element: `generated/web/*.css` swap `--gds-mint` and its
partners for the fairy values.

## Design notes (from the audits)

- Pink `#FF8FC7` is light, like mint, so everything designed for "ink on accent" keeps working:
  ink 8.6:1, `fairy-on-accent` 7.9:1.
- Pink sits nearer coral than mint does. Alerts keep their coral-soft ground and their words, so
  they still read as alerts, but never put the accent and an alert side by side unlabelled.
- In PulseLoop, `metric-blood-pressure` `#FF7FA8` and `metric-drinks` `#E38FB5` are pinks too: with
  the variant on, the readiness ring and those metrics share a hue. Data keeps its labels (D-9).

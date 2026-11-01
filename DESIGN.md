---
name: Gabriel Design System
version: 0.1.0
# GENERATED from tokens/tokens.json by scripts/gen_tokens.py. Edit the tokens, not this block.
colors:
  page: "#F2F2F2"
  page-dark: "#121214"
  surface: "#FFFFFF"
  surface-dark: "#1C1B1F"
  ink: "#17161A"
  ink-dark: "#F2F2F2"
  muted: "#5E5D63"
  muted-dark: "#A8A7AD"
  line: "#E2E2E4"
  line-dark: "#2C2B30"
  mint: "#43F3B7"
  mint-dark: "#43F3B7"
  on-mint: "#033423"
  on-mint-dark: "#033423"
  coral: "#E9554D"
  coral-dark: "#FF7A70"
  coral-text: "#B8322A"
  coral-text-dark: "#FF9A92"
  coral-soft: "#FDECEA"
  coral-soft-dark: "#3A1A17"
typography:
  display:
    fontFamily: Ubuntu Mono
    fontSize: 30px
    fontWeight: 700
    lineHeight: 36px
  timer:
    fontFamily: Ubuntu Mono
    fontSize: 56px
    fontWeight: 700
    lineHeight: 64px
    letterSpacing: -1px
  title:
    fontFamily: Ubuntu Mono
    fontSize: 22px
    fontWeight: 700
    lineHeight: 28px
  label:
    fontFamily: Ubuntu Mono
    fontSize: 16px
    fontWeight: 700
    lineHeight: 22px
  body:
    fontFamily: Ubuntu Mono
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-small:
    fontFamily: Ubuntu Mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22px
  meta:
    fontFamily: Ubuntu Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  caption:
    fontFamily: Ubuntu Mono
    fontSize: 12px
    fontWeight: 700
    lineHeight: 16px
    letterSpacing: 0.5px
rounded:
  s: 4px
  m: 8px
  l: 16px
  round: 999px
spacing:
  1: 4px
  2: 8px
  3: 12px
  4: 16px
  6: 24px
  8: 32px
  10: 40px
  12: 48px
  16: 64px
---

# Design System: Gabriel Design System

The tokens in the frontmatter above are the core and the uikit type roles; every app's full set is
in `tokens/tokens.json`. Where this page and the tokens disagree, the tokens win.

## Overview

One look for a family of personal Android apps (GVoice, GMind, GMoney, GHealth, GDesk, PulseLoop),
taken from [gabriellopes.com](https://gabriellopes.com): a quiet grey page inside a 4dp mint frame,
near-black or near-white ink, Ubuntu Mono for every word, and one mint accent that means "this is
the thing to do". The apps are tools people use daily, often on the move (Impeccable's *Operate*
mode): precision and restraint over expression, content first, chrome second. The brand lives in
three details: the frame, the mono type and the mint highlighter behind one word of a screen title.
PulseLoop adds a fourth: an ordered Bayer dither in place of colour tints.

## Colors

Value structure first: a page, a surface one step off it, ink, muted ink, a hairline. Then one
accent and one alert colour. Every colour has a light and a dark value (PulseLoop ships dark only).

### Primary

- **mint** `#43F3B7` (both themes): the one filled action per screen, the title highlighter, the
  active tab pill, progress chips, the frame. Text on it is `on-mint` `#033423` (9.7:1) or `ink`.

### Secondary

- **coral** `#E9554D` / `#FF7A70`: the Stop button and the recording dot only.
- **coral-text** `#B8322A` / `#FF9A92` on page, surface or **coral-soft**: alerts and destructive
  actions. Never white 12px text on a coral fill.

### Neutral

- **page** `#F2F2F2` / `#121214`, **surface** `#FFFFFF` / `#1C1B1F`, **ink** `#17161A` / `#F2F2F2`,
  **muted** `#5E5D63` / `#A8A7AD` (5.8:1 / 7.8:1 on page), **line** `#E2E2E4` / `#2C2B30`.

### Named Rules

- **Mint means act.** Success, connected, in range and REM are other colours (PulseLoop `success`
  `#4CC97A`, `stage-rem` cyan). When mint also meant "good" it stopped saying "tap here".
- **Data colours are a separate palette.** PulseLoop's metric, zone and sleep-stage colours sit
  beside mint without competing with it, and are only used for data.

## Typography

Ubuntu Mono, regular / bold / bold italic, bundled (Ubuntu Font Licence 1.0, `assets/fonts/`).
Monospace is the brand's voice; it reads well in Portuguese and English at 14–16sp. 12sp is the
floor for anything that carries meaning.

### Hierarchy

uikit roles: `display` 30/36 bold (screen title, one word on the mint highlighter), `timer` 56/64,
`title` 22/28, `label` 16/22 bold, `body` 16/24, `body-small` 14/22, `meta` 13/20 muted,
`caption` 12/16 bold caps +0.5. PulseLoop: scale 12 · 14 · 16 · 20 · 24 · 28 · 32 · 40; `eyebrow`
12 tracked caps, `label` 12, `body` 14, `title` 16 bold, `headline` 28 bold. The two scales are a
known divergence (docs/divergences.md D-1).

## Layout

Single column, 4-based spacing: 4, 8, 12, 16, 24, 32, 40, 48, 64, nothing else. Gutter 24dp on
phones, 32dp from 600dp; PulseLoop caps tab content at 720dp and moves tabs to a rail from 600dp.
Sections: a caption with 40dp above and 12dp below, no divider; rows that follow each other are one
group on `surface`, radius 8, inset 16, hairlines between rows. Space separates groups, not lines.

## Elevation & Depth

Flat. No drop shadows, no gradients. Depth is `surface` against `page`, a hairline, or (PulseLoop)
a denser dither. The snackbar is the only raised element (2dp).

## Shapes

`radius-s` 4 for buttons, chips, fields and the monogram; `radius-m` 8 for cards and panels (the
one card radius); `radius-l` 16 for pills and sheet tops; `radius-round` for the play button.

## Components

The catalogue, with each component's uikit method and Compose counterpart, is
[docs/components.md](docs/components.md).

### Buttons

52dp min height, radius 4, label 16 bold. PRIMARY mint (one per screen), SECONDARY ink outline,
DANGER coral-text outline and always confirmed, STOP solid coral (the only one).

### Chips

Read-only state, 12/16 bold caps: mint for progress and good states, coral-text on coral-soft for
alerts, grey for neutral. Ready is the absence of a chip.

### Cards / Containers

Radius 8 on `surface`. No shadow.

### Inputs / Fields

52dp, radius 4, line border; search shows a clear × when not empty.

### Navigation

Header 56dp (monogram 32dp, name over a one-line status, one trailing icon). Tab bar 64dp, active
tab is a mint pill behind the icon. Pushed screens have a back header and no tabs.

### The frame

A 4dp mint border round every screen. In uikit it is also the loading line: a lap of 1500ms round
the frame while the screen waits on something the user asked for.

## Do's and Don'ts

### Do:

- Take every value from the tokens; add a token here before an app needs a new one.
- Keep one filled mint action per screen; make the rest rows, outlines or switches.
- Check every new colour pair for 4.5:1 (text) or 3:1 (graphics) in each theme the app ships.
- Let things appear instead of moving when the phone's animations are off.

### Don't:

- Use mint for success, connected or decoration.
- Put white text on mint, or small white text on coral.
- Add a second typeface, an emoji icon, a shadow or a gradient.
- Show engine, vendor or exception names, or "updated 20 s ago", in the UI.

# Content: voice, states, dates

## Voice ✅

Short, specific, plain. Sentence case. Verb first on buttons ("Stop", "Try again"). At most one
lead line under a title. Errors are one sentence and one action; never a modal titled "Please check".
No engine, vendor or exception names in a label. Every string in English and Brazilian Portuguese
(uikit: `values/` + `values-pt-rBR/`, escape `\'`; PulseLoop: `tr()` + `assets/i18n/pt-BR.json`).

## State vocabulary ✅ (uikit `UiState`)

| State | Copy | Shown as |
|---|---|---|
| Recording | Recording · {source} | coral dot + header status in coral-text |
| Saving | Saving… | panel text |
| Transcribing | Transcribing {n}% | mint chip |
| Ready | — | no chip |
| Interrupted / Needs attention | Interrupted / Needs attention | coral-text on coral-soft chip |
| Paused | Paused | grey chip |
| Synced / Connected | Synced · {n} / Connected · syncing | mint chip |
| Error | {cause} | sheet with Try again |

Each app maps its engine states to these in one file; that file is the only place an engine name
appears. ⬜ PulseLoop's ring states (Connecting amber, Connected success) to be added here.

## Dates ✅

Relative under a week ("Yesterday 15:32"), then "Fri 9 Oct", the year only when it isn't this year.
Never ISO. Times follow the phone's 12/24-hour setting.

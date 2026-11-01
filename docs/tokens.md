# Tokens: schema and workflow

`tokens/tokens.json` is the only place a value is defined. Scripts in `scripts/` read it through
`tokens_lib.py`, so they all agree on what it means.

## Shape

```jsonc
{
  "version": "0.1.0",                 // = VERSION = latest CHANGELOG entry
  "core": {                           // what every app shares
    "color":   [{"name": "mint", "value": {"light": "#43F3B7", "dark": "#43F3B7"}, "usage": "…", "alias": {"pulseloop": "MINT"}}],
    "spacing": [{"name": "space-4", "value": "16px", "usage": "…"}],
    "radius": […], "size": […], "motion": […],
    "type": {"family": "…", "faces": […], "floor": 12}
  },
  "layers": {
    "uikit": {                        // one per app platform
      "themes": ["light", "dark"],
      "color": ["@page", …, {"name": "panel", "value": {…}}, {"name": "snackbar", "value": "{ink}"}],
      "type": [{"name": "Text", "styles": [{"name": "body", "fontSize": "16px", "lineHeight": "24px", "fontWeight": 400}]}],
      "spacing": ["@space-1", …], "radius": […], "size": […], "motion": […]
    },
    "pulseloop": { "themes": ["dark"], "typeScale": [12, …], "dither": {…}, … }
  },
  "contrast": [{"fg": "muted", "bg": "page", "min": 4.5, "layers": ["uikit", "pulseloop"]}]
}
```

- **Order matters.** A layer's lists are the order of its generated file. `"@name"` pulls a core
  token; an object is a layer-only token.
- **Every core token appears in every layer.** A value only one app uses belongs in that layer.
- **Colours** are `#RRGGBB`, or `#AARRGGBB` for a deliberate translucency. A dark-only layer may
  omit `light`. `"{name}"` aliases another colour of the same layer.
- **`"pair": true`** marks a uikit colour whose light value equals an earlier token's while its
  dark value differs (`panel` = `ink` in light). The Views kit finds a dark value by its light value
  (`UiTokens.dark(int)`, `Ui.color(c, X)`), so these must be read as
  `UiTokens.color(context, X, X_DARK)`. `check_tokens.py` requires the mark where it is needed and
  rejects it where it isn't.
- **`alias.pulseloop`** names the `PulseColors` (or `FairyMode.Palette`) property the token must
  equal; `drift.py` uses it. A new PulseLoop colour needs one.
- **`contrast`** lists every text/background pair a component uses. `themes` narrows a pair to some
  themes. `"known": "<audit id>"` marks a tracked failure (warns while failing, errors once fixed).
- **`variants.<name>`** is a palette that replaces some tokens for a while (today only `fairy`,
  docs/fairy-mode.md). Each variant colour says what it `replaces`; a layer pulls the ones it needs
  with `"@fairy-accent"` like a core token. A layer that carries any of a variant's colours must carry
  the replacement for every replaced token it has, and the contrast pairs are checked a second time
  with the variant swapped in. CSS gets a `[data-variant="<name>"]` block.
- **`usage`** is one plain sentence: what the token is for. It becomes the code comment.

## Workflow

```sh
$EDITOR tokens/tokens.json
python3 scripts/gen_tokens.py      # writes generated/* and DESIGN.md's frontmatter
python3 scripts/check_tokens.py    # must report 0 errors
python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid
```

`drift.py` is expected to report differences between merging a change here and syncing it to the
apps; it must be back to 0 once the app PRs land.

## Generated files

| File | Consumer | How it is used |
|---|---|---|
| `generated/uikit/UiTokens.java` | NotTheOmiAIApp `ui-kit/src/main/java/br/gabriel/ui/UiTokens.java` | copied over as is |
| `generated/pulseloop/GTokens.kt` | PulseLoop `app/src/main/java/com/pulseloop/ui/theme/GTokens.kt` | copied over as is; `PulseColors` reads `GTokens.Colors.*` (🟡 adopted in PulseLoop PR, see docs/consuming.md) |
| `generated/web/*.css` | prototypes, design canvases | `--gds-*` custom properties |
| `DESIGN.md` frontmatter | Impeccable and other DESIGN.md-aware tools | read only |

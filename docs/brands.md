# Brands

A **brand** dresses an app as a partner's product without taking it out of the system. Cochilo was
the first: it ships as **Cochilo, da Tatá Slings**, a product of Tatá's babywearing shop.

Status: ✅ the mechanism (0.6.0). Since 0.28.0 **a partner's brand lives in the product's repo**,
next to its product layer, and is built with this repo's scripts ([products.md](products.md)).
This repo holds the rules and the checks; its own apps wear Gabriel's brand. Tatá Slings is in
`gabrielbr/Cochilo`, `design/brand/tata-slings/`.

## What a brand changes, and what it never does

| A brand swaps | A brand never touches |
|---|---|
| The app's colour roles: `page`, `surface`, `ink`, `muted`, `line`, the brand accent (`mint` role), `on-mint`, the alert roles, panel and snackbar colours | Spacing, radii, sizes, motion, the type scale (sizes, line heights, weights per role) |
| The one type family (and its faces) | Data colours (`event-*`, `metric-*`, `stage-*`, `zone-*`): their meaning is the system's |
| The app's mark (an asset in `assets/logos/`) | Components, icons, the frame, the targets, copy rules, the update flow |
| | Any rule in AGENTS.md: one filled accent action per screen, contrast, 48dp, tokens only… |

So a branded app still reads like a Gabriel app (same rhythm, same components, same behaviour) and
looks like the partner's product (their colours, their typeface, their mark).

The role names stay. Under a brand, `mint` means "the brand accent": the one filled action, the
frame, the active tab, the title highlighter. Keeping the names means no app code changes when a
brand is put on or taken off; only the generated values move.

## How it's built

- A brand file (in the product's repo; the shape `tokens.json` → `brands.<key>` would have):
  `name`, `doc`, `source` (where the values were measured), `type`
  (`family`, `faces`, `licence`) and `color`, a list of `{replaces, value: {light, dark}, usage}`.
- A layer opts in with `"brand": "<key>"`.
- `tokens_lib.colour_map` applies the brand after aliases are followed, so the generator and the
  contrast check see the app as it ships.
- The generated Compose object (`gen_tokens.compose_kt`) gains `object Brand { key, name, fontFamily }`; each replaced colour's
  comment starts with the brand's name. The CSS sets `--gds-font` to the brand's family.
- `check_tokens.py` (`check_brands`): a brand may only replace colours the layer has, never a data
  colour, needs a value for every theme the layer ships, names its family and faces, and carries
  nothing else (no spacing, radius, size…). Every contrast pair is re-checked with the brand on.

## Tatá Slings

Moved to Cochilo in 0.28.0: `gabrielbr/Cochilo`, `design/brand/tata-slings/brand.md` (its values,
the 0.7.0 "Tecidos" warmth, the night light values, the softer palette and the textures), with the
history as it was written here.

The rule that came from it stays here, because it holds for any brand: **no text on a texture**. A
partner's fabric, print or photo may show only where no words sit on it (a band, a swatch). To
keep 12–13sp text at 4.5:1 over a busy texture the page colour has to cover almost all of it, and
then the texture no longer reads.

## Adding a brand

In the product's repo, not here ([products.md](products.md)):

1. Measure the partner's real colours and type (their site, their print), and write the source.
2. Write the brand file; pick values that pass every contrast pair the product layer has, in
   every theme.
3. Keep the faces with their licence, the mark and any textures beside it.
4. Point the product layer at it (`"brand": "<key>"`). Build with this repo's vendored scripts,
   which run `check_brands` and the contrast check, then audit.
5. In the app: ship the faces, switch the family, swap the mark.

If the brands mechanism itself needs something new, that change comes here first.

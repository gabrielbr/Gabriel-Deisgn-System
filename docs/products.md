# Products, brands and the core

This repo is the **core** of the owner's design: what every one of his apps shares. It is dressed
in **Gabriel's own brand** (mint, Ubuntu Mono, the GV/GM marks). That makes it his boilerplate:
an app built on it looks and behaves like his apps until something says otherwise.

Two things can say otherwise, and since 0.28.0 neither lives here:

| | What it is | Where it lives |
|---|---|---|
| **A partner's brand** | A partner's colour roles and one type family, their mark and assets (photos, textures), within the brands rule ([brands.md](brands.md): colour roles and the family only) | The product's repo |
| **A product layer** | The product's own tokens and components: what only that app has, plus the core tokens it pulls with `"@name"` | The product's repo |

The apps in this repo's `layers` (uikit, pulseloop) are Gabriel-branded and have nothing of their
own outside it, so they stay here as before ([consuming.md](consuming.md)).

## Why

- The boilerplate stays generic: a change for one partner never lands in every app's tokens.
- A partner's assets and voice (and their permission to use them) stay with the product they
  were given for.
- The product moves at its own pace: a product-only token or component doesn't wait for a release
  here.

## How a product builds on the core

The first product to work this way is **Cochilo** (`gabrielbr/Cochilo`, a Tatá Slings product):

```
design/
  core/            this repo's core.json (the `core` section of tokens.json) and scripts/, vendored
                   unchanged at a tagged version; CORE.md says which one and how to re-sync
  brand/<key>/     the partner's brand: brand.json, its doc, mark, textures, licences
  product/<app>/   the product layer: layer.json (layer + its contrast pairs), components.md
  build.py         assembles the three into the shape tokens.json has and runs this repo's own
                   generator (gen_tokens.compose_kt, css) and checks (check_layers, check_brands,
                   check_contrast); --check fails if the app's tokens file differs
```

The product never forks the generator or the checks. Every rule in AGENTS.md still holds there:
tokens only, the scale, the type floor, contrast in every theme the product ships, and the brand
limits.

## Where a change goes

1. **Could any of the owner's apps use it?** (a spacing step, a duration, a generic component, an
   accessibility rule, a check). It comes **here**, as a PR with an audit and a release. Then each
   product re-syncs its `design/core/`.
2. **Is it one partner's look?** It goes in that product's `design/brand/`.
3. **Is it only one product's?** It goes in that product's `design/product/`.

A product's own component can come here later, once a second app needs it. Rows in
[components.md](components.md) that still name Cochilo mark components it was first to use that
are now everyone's: the Quiet link, Checklist, the Conversation pattern, Filter chips, the
two-icon header, wide screens and large text.

## Starting a new product with a partner brand

1. Copy Cochilo's `design/` layout (or its `build.py` and `core/CORE.md`) into the new repo, and
   vendor this repo's `core` and `scripts/` at the latest tag.
2. Write `product/<app>/layer.json`: themes, the core tokens it pulls, its own, its contrast
   pairs. Write `brand/<key>/brand.json` from the partner's measured values ([brands.md](brands.md)).
3. Call `gen_tokens.compose_kt(t, "<app>", "<package>", "<Object>", ["<doc line>"])` (and `css`
   if it needs web) from the product's build; check with `check_tokens`' functions.
4. Add a row for the product to the table in AGENTS.md here ("builds on the core in its own repo").
5. Copy the four design skills into the product's `.claude/skills/` and add the rule below to
   its AGENTS.md ([the four design skills](#the-four-design-skills)).

## The four design skills

Every app on this boilerplate designs and audits each screen and flow with:
- **ux-user-flows**, the owner's UX and flow method;
- **impeccable**;
- **graphic-design-fundamentals**, the owner's design basics;
- **less-is-more**.

They are vendored in this repo's `.claude/skills/` (`VENDORED.md` says from where).

**In the app's repo:**

1. Copy `ux-user-flows/`, `impeccable/`, `graphic-design-fundamentals/` and `less-is-more/` into its
   `.claude/skills/`.
2. Add a `VENDORED.md` naming this repo's version.
3. Adapt less-is-more's examples to the product if that helps; keep the five questions and the
   output.

**The rule for the app's AGENTS.md** (copy it as it is):

> - **Four skills on every screen and flow.** Every new or changed screen, flow, sheet,
>   notification or widget is designed with, and then audited against, all four skills in
>   `.claude/skills/`, in this order:
>   1. **ux-user-flows**: first, decide what happens and in what order. Write the flow (entry
>      points, steps, branches, every state, exits) and run its §13 flow review checklist.
>   2. **impeccable**: shape, critique and polish while designing, then its native `audit` and
>      `critique`, with the five dimensions scored and findings P0–P3.
>   3. **graphic-design-fundamentals**: plan with it, then its §13 checklist.
>   4. **less-is-more**: the five questions on every element; what was cut; taps on common actions
>      never rise.
>
>   Where a skill's general advice and this design system differ (target sizes, the one mint
>   action, the frame), the design system wins.
>
>   Use them while working, not only at the end. If a skill won't load, read its `SKILL.md` and
>   references and apply it by hand, and say so. The audit file has one section per skill. Fix any
>   P0 or P1 finding, and anything the checklist fails, before merging.

**When a skill changes here** (a patch release), each app re-copies it. The CHANGELOG entry says
so.

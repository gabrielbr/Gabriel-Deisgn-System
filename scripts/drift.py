#!/usr/bin/env python3
"""Compare the apps' checked-in tokens with this repo. Run before and after syncing a release.

    python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid

Exit 1 on any drift. What it compares:
  NotTheOmiAIApp  ui-kit/.../UiTokens.java against generated/uikit/UiTokens.java (the GENERATED
                  header line is ignored, every other line must match).
  PulseLoop       ui/theme/GTokens.kt (when present) against generated/pulseloop/GTokens.kt; every
                  colour property in PulseColors.kt and FairyMode.Palette, whether a Color(0x…)
                  literal or a GTokens.Colors reference, against the token whose alias.pulseloop
                  names it; and PulseType.SCALE against typeScale. A colour the app defines that no
                  token claims is reported too: it is a value outside the system.

A product that keeps its own layer and brand (Cochilo, docs/products.md) checks its own drift with
its build (Cochilo: python3 design/build.py --check), so it isn't compared here.
"""
import argparse
import difflib
import pathlib
import re
import sys

from tokens_lib import ROOT, camel, colour_map, load, resolve

UIKIT = "ui-kit/src/main/java/br/gabriel/ui/UiTokens.java"
PL_THEME = "app/src/main/java/com/pulseloop/ui/theme"


def body(text):
    return [line for line in text.splitlines() if not line.startswith("// GENERATED")]


def drift_uikit(repo):
    path = repo / UIKIT
    if not path.exists():
        return [f"NotTheOmiAIApp: {UIKIT} not found"]
    ours = body((ROOT / "generated/uikit/UiTokens.java").read_text())
    theirs = body(path.read_text())
    if ours == theirs:
        return []
    diff = difflib.unified_diff(theirs, ours, "app UiTokens.java", "generated/uikit/UiTokens.java", lineterm="", n=0)
    return ["NotTheOmiAIApp UiTokens.java differs (copy generated/uikit/UiTokens.java in):\n  "
            + "\n  ".join(line for line in diff)]



LITERAL = re.compile(r"Color\(0x([0-9A-Fa-f]{8})\)")
TOKEN_REF = re.compile(r"GTokens\.Colors\.(\w+)")
VAL = re.compile(r"\bval\s+(\w+)")


def colour_props(text, prefix=""):
    """{property: ('lit', AARRGGBB) | ('ref', tokenCamelName)} for `val x = …` lines that set a colour."""
    found = {}
    for line in text.splitlines():
        m = VAL.search(line)
        if not m:
            continue
        ref, lit = TOKEN_REF.search(line), LITERAL.search(line)
        if ref:
            found[prefix + m.group(1)] = ("ref", ref.group(1))
        elif lit:
            found[prefix + m.group(1)] = ("lit", lit.group(1).upper())
    return found


def pulse_colours(repo):
    theme = repo / PL_THEME
    found = colour_props((theme / "PulseColors.kt").read_text())
    fm = (theme / "FairyMode.kt").read_text()
    found.update(colour_props(fm[fm.find("object Palette"):], "FairyMode."))
    return found


def drift_pulseloop(t, repo):
    out = []
    gt = repo / PL_THEME / "GTokens.kt"
    if gt.exists() and body(gt.read_text()) != body((ROOT / "generated/pulseloop/GTokens.kt").read_text()):
        out.append("PulseLoop: ui/theme/GTokens.kt differs from generated/pulseloop/GTokens.kt (copy it in)")
    app = pulse_colours(repo)
    colours = colour_map(t, "pulseloop")
    by_camel = {camel(n): v for n, v in colours.items()}

    def argb8(hex_):
        h = hex_.lstrip("#").upper()
        return h if len(h) == 8 else "FF" + h

    claimed = set()
    for tok in resolve(t, "pulseloop")["color"]:
        alias = tok.get("alias", {}).get("pulseloop")
        if not alias:
            continue
        claimed.add(alias)
        want = argb8(colours[tok["name"]]["dark"])
        kind, val = app.get(alias, (None, None))
        if kind is None:
            out.append(f"PulseLoop: {alias} (token {tok['name']}) not found in the app")
            continue
        if kind == "ref":
            if val not in by_camel:
                out.append(f"PulseLoop: {alias} reads GTokens.Colors.{val}, which no token generates")
                continue
            have = argb8(by_camel[val]["dark"])
        else:
            have = val
        if have != want:
            out.append(f"PulseLoop: {alias} is #{have}, token {tok['name']} is #{want}")
    for name in sorted(set(app) - claimed):
        out.append(f"PulseLoop: {name} = {app[name][1]} has no token (add one or remove it from the app)")
    pt = (repo / PL_THEME / "PulseType.kt").read_text()
    m = re.search(r"SCALE\s*=\s*(?:listOf\(([^)]*)\)|GTokens\.Type\.scale)", pt)
    if m and m.group(1) is None:
        scale = t["layers"]["pulseloop"]["typeScale"]  # read straight from GTokens
    else:
        scale = [int(x) for x in m.group(1).split(",")] if m else None
    if scale != t["layers"]["pulseloop"]["typeScale"]:
        out.append(f"PulseLoop: PulseType.SCALE is {scale}, typeScale is {t['layers']['pulseloop']['typeScale']}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notheomi", type=pathlib.Path)
    ap.add_argument("--pulseloop", type=pathlib.Path)
    a = ap.parse_args()
    if not (a.notheomi or a.pulseloop):
        ap.error("give at least one app repo")
    t = load()
    issues = []
    if a.notheomi:
        issues += drift_uikit(a.notheomi)
    if a.pulseloop:
        issues += drift_pulseloop(t, a.pulseloop)
    for i in issues:
        print("drift:", i)
    print(f"drift: {len(issues)} difference(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

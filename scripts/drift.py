#!/usr/bin/env python3
"""Compare the apps' checked-in tokens with this repo. Run before and after syncing a release.

    python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid

Exit 1 on any drift. What it compares:
  NotTheOmiAIApp  ui-kit/.../UiTokens.java against generated/uikit/UiTokens.java (the GENERATED
                  header line is ignored, every other line must match).
  PulseLoop       every Color(0x…) in PulseColors.kt and FairyMode.kt against the token whose
                  alias.pulseloop names it, and PulseType.SCALE against typeScale. A colour the app
                  defines that no token claims is reported too: it is a value outside the system.
"""
import argparse
import pathlib
import re
import sys

from tokens_lib import ROOT, colour_map, load, resolve

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
    out = []
    for i in range(max(len(ours), len(theirs))):
        a = ours[i] if i < len(ours) else "<none>"
        b = theirs[i] if i < len(theirs) else "<none>"
        if a != b:
            out.append(f"NotTheOmiAIApp UiTokens.java line {i + 2}: app `{b.strip()}` / system `{a.strip()}`")
    return out


COLOR_VAL = re.compile(r"(?:private\s+)?val\s+(\w+)\s*(?::\s*Color)?\s*(?:=|get\(\)\s*=).*?Color\(0x([0-9A-Fa-f]{8})\)")


def pulse_colours(repo):
    found = {}
    pc = (repo / PL_THEME / "PulseColors.kt").read_text()
    for m in COLOR_VAL.finditer(pc):
        found[m.group(1)] = m.group(2).upper()
    fm = (repo / PL_THEME / "FairyMode.kt").read_text()
    palette = fm[fm.find("object Palette"):]
    for m in re.finditer(r"val\s+(\w+)\s*=\s*Color\(0x([0-9A-Fa-f]{8})\)", palette):
        found["FairyMode." + m.group(1)] = m.group(2).upper()
    return found


def drift_pulseloop(t, repo):
    out = []
    app = pulse_colours(repo)
    colours = colour_map(t, "pulseloop")
    claimed = set()
    for tok in resolve(t, "pulseloop")["color"]:
        alias = tok.get("alias", {}).get("pulseloop")
        if not alias:
            continue
        claimed.add(alias)
        want = colours[tok["name"]]["dark"].lstrip("#").upper()
        want = want if len(want) == 8 else "FF" + want
        have = app.get(alias)
        if have is None:
            out.append(f"PulseLoop: {alias} (token {tok['name']}) not found in the app")
        elif have != want:
            out.append(f"PulseLoop: {alias} is #{have}, token {tok['name']} is #{want}")
    for name in sorted(set(app) - claimed):
        out.append(f"PulseLoop: {name} = #{app[name]} has no token (add one or remove it from the app)")
    pt = (repo / PL_THEME / "PulseType.kt").read_text()
    m = re.search(r"SCALE\s*=\s*listOf\(([^)]*)\)", pt)
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

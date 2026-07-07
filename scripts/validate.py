#!/usr/bin/env python3
"""Validate every Cypher Hermes theme: parseable YAML, required schema keys,
and a legibility guard (card text must actually contrast the card)."""
import glob, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

REQUIRED = {
    "name": str, "label": str,
    "palette": dict, "typography": dict,
    "colorOverrides": dict, "componentStyles": dict, "customCSS": str,
}
CO_REQUIRED = ["card", "cardForeground", "primary", "primaryForeground", "border"]

def lum(hex_):
    h = hex_.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.299*r + 0.587*g + 0.114*b

fail = 0
files = sorted(glob.glob("*.yaml"))
if not files:
    sys.exit("no theme .yaml files found")
for f in files:
    errs = []
    try:
        d = yaml.safe_load(open(f))
    except Exception as e:
        print(f"✗ {f}: unparseable — {e}"); fail += 1; continue
    for k, t in REQUIRED.items():
        if k not in d: errs.append(f"missing '{k}'")
        elif not isinstance(d[k], t): errs.append(f"'{k}' should be {t.__name__}")
    co = d.get("colorOverrides", {})
    for k in CO_REQUIRED:
        if k not in co: errs.append(f"colorOverrides missing '{k}'")
    # legibility guard: card vs cardForeground must differ enough to read
    try:
        if abs(lum(co["card"]) - lum(co["cardForeground"])) < 60:
            errs.append("cardForeground does not contrast card (light-on-light / dark-on-dark?)")
    except Exception:
        pass
    if errs:
        fail += 1
        print(f"✗ {f}:")
        for e in errs: print(f"    - {e}")
    else:
        print(f"✓ {f}")
print(f"\n{'FAILED' if fail else 'All themes valid'} ({len(files)-fail}/{len(files)} ok)")
sys.exit(1 if fail else 0)

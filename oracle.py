import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

WIDTHS = [60, 75, 90, 120, 150, 180]
FILLER = 2.5

def vanity_plan(wallCm):
    if not (wallCm > 0):
        return {"error": "the wall must be positive"}
    vanity = 0
    for w in WIDTHS:
        if w + 2 * FILLER <= wallCm:
            vanity = w
    if not vanity:
        return {"error": "the wall is narrower than one labeled vanity bay"}
    leftover = round1(wallCm - vanity - 2 * FILLER)
    if leftover < 10: verdict = "a snug fit"
    elif leftover <= 30: verdict = "a comfort fit"
    else: verdict = "a roomy fit"
    return {"vanity": vanity, "leftover": leftover, "verdict": verdict}

def sink_plan(vanityCm):
    if not (vanityCm > 0):
        return {"error": "the vanity must be positive"}
    if vanityCm >= 120: sinks, used, verdict = 2, 120, "a twin-bowl pair"
    elif vanityCm >= 90: sinks, used, verdict = 1, 45, "one roomy bowl with counter to spare"
    else: sinks, used, verdict = 1, 45, "a solo bowl"
    counter = round1(vanityCm - used)
    return {"sinks": sinks, "counter": counter, "verdict": verdict}

def faucet_plan(spacingCm):
    if not (spacingCm > 0):
        return {"error": "the drill spacing must be positive"}
    if spacingCm > 21:
        return {"error": "the spacing is wider than a labeled widespread"}
    if spacingCm <= 5: handles, verdict = 1, "a single-hole tap"
    elif spacingCm <= 11: handles, verdict = 2, "a centerset pair"
    else: handles, verdict = 2, "a widespread trio"
    return {"handles": handles, "verdict": verdict}

def render_vanity(r, wallCm):
    return ("A wall " + fmt(wallCm) + " cm takes a " + fmt(r["vanity"]) + " cm vanity with " + fmt(r["leftover"])
            + " cm to spare past the labeled fillers - " + r["verdict"] + ".")

def render_sink(r, vanityCm):
    return ("A vanity " + fmt(vanityCm) + " cm fits " + plural(r["sinks"], "bowl") + " with " + fmt(r["counter"])
            + " cm of counter left over - " + r["verdict"] + ".")

def render_faucet(r, spacingCm):
    return ("A drill spacing " + fmt(spacingCm) + " cm takes " + plural(r["handles"], "handle") + " - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[150],[65],[60],[0],[200],[240],[95],[100],[142.5],[300]]:
    add("vanityPlan", vanity_plan, render_vanity, a)
for a in [[120],[90],[60],[0],[150],[45],[119],[180],[95.5],[200]]:
    add("sinkPlan", sink_plan, render_sink, a)
for a in [[10],[4],[5],[5.5],[11],[11.5],[20],[21],[21.5],[0]]:
    add("faucetPlan", faucet_plan, render_faucet, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")

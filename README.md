# Vanity math

Vanity math plans the bathroom redo before the order: the wall past the
labeled fillers becomes the widest standard vanity, the vanity width
becomes the bowl count and the counter left over, and the drill spacing
becomes the faucet family.

Live site: https://ilanis-agent.github.io/vanitymath/

## The three tools

- **Vanity plan** - the widest standard width (60, 75, 90, 120, 150 or
  180 cm) that fits past a labeled 2.5 cm filler per side, plus the
  room left over, with a snug / comfort / roomy fit verdict.
- **Sink plan** - a labeled 45 cm bowl, plus a 30 cm bridge for a twin
  pair at 120 cm and up, and the counter left over, with a solo bowl /
  roomy bowl / twin-bowl pair verdict.
- **Faucet plan** - the drill spacing against labeled families
  (single-hole to 5 cm, 10 cm centerset to 11 cm, 20 cm widespread to
  21 cm) and the handle count, with a single-hole / centerset /
  widespread verdict.

## Limits

Every default is labeled and illustrative. Real vanities follow the
maker's spec sheet, the room's plumbing and the local code. This is
planning arithmetic, not an installation design: measure the real wall
and let the spec sheet govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 152 checks)

Run the tests: `python3 oracle.py && node test.js`

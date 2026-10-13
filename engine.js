(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }
  var WIDTHS = [60, 75, 90, 120, 150, 180];
  var FILLER = 2.5;

  function vanityPlan(wallCm) {
    if (!(wallCm > 0)) return { error: "the wall must be positive" };
    var vanity = 0;
    for (var i = 0; i < WIDTHS.length; i++) {
      if (WIDTHS[i] + 2 * FILLER <= wallCm) vanity = WIDTHS[i];
    }
    if (!vanity) return { error: "the wall is narrower than one labeled vanity bay" };
    var leftover = round1(wallCm - vanity - 2 * FILLER);
    var verdict;
    if (leftover < 10) verdict = "a snug fit";
    else if (leftover <= 30) verdict = "a comfort fit";
    else verdict = "a roomy fit";
    return { vanity: vanity, leftover: leftover, verdict: verdict };
  }

  function sinkPlan(vanityCm) {
    if (!(vanityCm > 0)) return { error: "the vanity must be positive" };
    var sinks, used, verdict;
    if (vanityCm >= 120) { sinks = 2; used = 120; verdict = "a twin-bowl pair"; }
    else if (vanityCm >= 90) { sinks = 1; used = 45; verdict = "one roomy bowl with counter to spare"; }
    else { sinks = 1; used = 45; verdict = "a solo bowl"; }
    var counter = round1(vanityCm - used);
    return { sinks: sinks, counter: counter, verdict: verdict };
  }

  function faucetPlan(spacingCm) {
    if (!(spacingCm > 0)) return { error: "the drill spacing must be positive" };
    if (spacingCm > 21) return { error: "the spacing is wider than a labeled widespread" };
    var handles, verdict;
    if (spacingCm <= 5) { handles = 1; verdict = "a single-hole tap"; }
    else if (spacingCm <= 11) { handles = 2; verdict = "a centerset pair"; }
    else { handles = 2; verdict = "a widespread trio"; }
    return { handles: handles, verdict: verdict };
  }

  function renderVanity(r, wallCm) {
    return "A wall " + wallCm + " cm takes a " + r.vanity + " cm vanity with " + r.leftover + " cm to spare past the labeled fillers - " + r.verdict + ".";
  }

  function renderSink(r, vanityCm) {
    return "A vanity " + vanityCm + " cm fits " + plural(r.sinks, "bowl") + " with " + r.counter + " cm of counter left over - " + r.verdict + ".";
  }

  function renderFaucet(r, spacingCm) {
    return "A drill spacing " + spacingCm + " cm takes " + plural(r.handles, "handle") + " - " + r.verdict + ".";
  }

  var api = { vanityPlan: vanityPlan, sinkPlan: sinkPlan, faucetPlan: faucetPlan, renderVanity: renderVanity, renderSink: renderSink, renderFaucet: renderFaucet };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.VanityMath = api;
})(this);

# Data Analysis Handoff — Review Response

Four items need a check against the actual experiment data/config before any text
gets written. Each spec below states exactly what to compute and what the two
possible outcomes imply for the paper.

---

## 1. W1 — Matched-subset reanalysis (selection confound)

**Question:** Is Compiled's 91.9% hold rate inflated by installing preferentially on
(topic, side) pairs the base model already leaned toward?

**Compute, from the existing 1,776-generation dataset — no new generations needed:**
1. For each of the 48 (topic, side) pairs, determine whether **Context** installed
   (≥4/5) and whether **Compiled** installed (≥4/5).
2. Restrict to the subset of pairs where *both* installed.
3. Recompute hold rate for **Context** and for **Compiled** on that common subset only.
4. Separately: split **Compiled**'s installed pairs by base-model prior direction
   (using the ρ=0.496 correlation data already computed for "Installation has a
   prior") into prior-congruent vs. prior-incongruent, and report hold rate for each.

**Report:** the matched-subset hold rates for both conditions, plus the prior-stratified
split for Compiled. If Compiled's hold rate on the matched subset is still far above
Context's, the confound is answered. If it collapses toward Context's 58% on the
matched subset, that's a real finding to report as a qualification, not something to
paper over.

---

## 2. W2 — Think-mode configuration check

**Question:** Was think-mode disabled for all six conditions in the main protocol, or
only for the modulated ones?

**Check:** the raw file is named `benchmark_raw_nothink_*.json` for Bare, Context,
Context+Compiled, and Compiled+Slot alike. Confirm from the actual generation config
(not the filename alone) whether "nothink" means think-mode was off globally for this
run.

**Two branches:**
- **If global:** Bare's reported 62% hold rate *is* the no-think bare-model control.
  No new experiment needed — the paper just needs a sentence stating this explicitly,
  since "Why the Channels Differ" currently implies suppression is modulation-specific
  ("modulation suppresses think-mode"), which would need rewording to avoid
  contradicting the run config.
- **If modulation-specific:** the reviewer's control doesn't exist yet. Run: bare
  model, think-mode explicitly disabled via whatever flag/prompt turns it off, same
  five-level pressure protocol, same 24 topics. Compare hold rate to bare's existing
  62% (think-mode on) and to Compiled's 91.9%. If disabling deliberation alone moves
  bare's hold rate substantially toward 91.9%, the mechanism section's causal story
  needs revising.

---

## 3. W3 — Judge validity

Three checks, cheapest first:

1. **Second judge family, same transcripts.** Re-score a sample (or all 1,776) of the
   existing generations with a different judge model, same 1–5 rubric, same
   blind-to-condition setup. Report inter-judge agreement (e.g., weighted kappa) and
   whether the headline installation/hold percentages move outside their current CIs.
2. **Style-transfer probe (cheapest single check if time-limited).** Take a sample of
   Bare or Context transcripts, rewrite surface style/register to match Compiled's
   generation statistics (shorter, less hedged, whatever the diversity-attractor
   result characterizes) while preserving the original stance-holding content. Re-score
   with the main judge. If scores shift substantially with no change in actual
   stance-holding, the judge is partly reading style.
3. **Human validation subsample.** 50–100 generations spanning all conditions, human
   1–5 conviction rating, blind to condition, compare to judge scores.

---

## 4. W5 — Context condition mechanics + stronger baselines

**Factual check (not an analysis, just needs an answer from the harness):** in the
main five-level pressure protocol, is the Context belief a system-position message
re-supplied every turn, or inserted once and left in a growing transcript? This
determines how "Context" should be described in Protocol and affects how the 58% hold
rate should be interpreted relative to the length-matched filler control (55.6%).

**Two additional conditions, if pipeline time allows (reuses existing infra):**
- Explicit persistence instruction: belief text + "hold this position unless given
  compelling evidence," same protocol.
- Per-turn re-injection: belief text re-supplied fresh at every pressure turn rather
  than persisting once in history.

Report installation and hold rate for both against the existing **Context** baseline.

---

## 5. Q4 — Per-cell n's for Table 1

Not an analysis — just report, for every cell in the install-hold table, the raw
generation/pair count the percentage is computed over. Compiled's 91.9% hold rate in
particular is likely sitting on a small denominator (the installed subset of 48
pairs); state it explicitly rather than leaving it implicit.

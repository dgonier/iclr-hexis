# Q/V channel asymmetry — the defense against "just a generic don't-change-your-mind effect"

The reviewer (W1) and the current E.1 "negative result" framing both risk reading the
mechanism as a single belief-agnostic steadfastness knob. The Q/V split refutes that: the
HOLD perturbation (Q) is generic, but the BELIEF (V) is content-specific and demonstrably
carries the topic. Both legs verified below on pro (E.1) and con (E.1b) held-out sets.

## Numbers (functional applied-delta cosine across 24 beliefs, production compile path)

| channel | source | cross-belief cos (pro / con) | std (pro) | discrimination |
|---|---|---|---|---|
| Q (MStateReadHead) | disposition vector alone (content-blind) | 0.9955 / 0.996 | 0.002 | flat |
| V (belief_compiler) | pooled hidden states over belief TEXT | 0.522 / 0.531 | 0.145 | belief-specific |

- V std / Q std = **78x** (pro), **98x** (con): V discriminates ~80-100x more across beliefs than Q.
- 1-cos distance: V-deltas are **105x** (pro) / **113x** (con) farther apart than Q-deltas.
- Both replicate independently on the pre-registered con-side set (E.1b).

## V tracks SEMANTIC content (the smoking gun that V != generic)

If V were a generic "hold" direction, its cross-belief similarity would be random w.r.t.
topic meaning. Instead it clusters by subject matter:

MOST V-similar belief pairs (semantically related):
- standardized_testing <-> grade_retention  (0.918)  [education policy]
- term_limits_congress <-> electoral_college_abolish  (0.916)  [electoral reform]
- peer_review_speed <-> lab_data_sharing  (0.916)  [scientific practice]
- intermittent_fasting <-> mental_health_medication  (0.907)  [health]

LEAST V-similar (semantically distant):
- electoral_college_abolish <-> mental_health_medication  (0.182)
- electoral_college_abolish <-> intermittent_fasting  (0.189)
- electoral_college_abolish <-> grade_retention  (0.217)

## Interpretation / framing for the paper

The mechanism is NOT "a compiled belief the conversation can't edit" (over-claims content
specificity of the HOLD), and it is NOT "a generic steadfastness adapter" (ignores V).
The honest, data-supported story is a TWO-CHANNEL split:

- **Q-channel = a generic commit/hold perturbation.** Belief-agnostic (cos 0.995). We CONCEDE
  this: the "don't back down" capacity is not belief-specific, and it survives freezing to a
  constant offset and truncation to rank 1. This is the "steadfastness" the reviewer names.
- **V-channel = belief-specific content.** Varies 78-98x more, tracks topic semantics. This is
  where the actual belief lives in the weights. It is content-specific by construction (built
  from pooled hidden states over the belief text) and empirically (semantic clustering).

So: the HOLD is generic, but the BELIEF is specific — and they are DIFFERENT channels. The
paper installs a content-specific belief (V) alongside a generic commitment perturbation (Q);
the criticism "you just installed a generic effect" is false because it ignores that the V
delta is 100x more belief-differentiated than the Q delta and clusters by meaning.

## Two required fixes to the paper's own framing
1. E.1's writeup currently calls V=0.52 a "NEGATIVE RESULT" (tested against a 0.99 uniformity
   threshold). That is the WRONG comparison. The right comparison is V vs Q (0.52 vs 0.995),
   where V is dramatically content-specific. Re-frame E.1: Q is uniform (negative for
   "belief-specific hold", which we concede), V is content-specific (positive, and the point).
2. Retitle/reword the mechanism sections so the persistence claim attaches to the Q-channel
   commit-perturbation (generic, conceded) and the CONTENT claim attaches to the V-channel
   (specific, defended) -- addressing W1 head-on rather than being caught by it.

## Still open (W1's decisive test, unchanged by this)
A directly-trained rank-1 constant Q-offset (no hypernetwork, no belief input) should match
Compiled on HOLD if the Q story is right. It would NOT reproduce install/content (that needs V).
Run it to nail the split quantitatively.

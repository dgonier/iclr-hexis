# Belief or Bias?
## Measuring Epistemic Interventions on Conviction and Discrimination

*Draft — 6 September 2026. All experiments complete.*

---

## Abstract

A model assigned a position can fail in two opposite directions: it can abandon the position
under pressure that supplies no reason, or hold it against evidence that supplies a good one.
The sycophancy literature measures only the first, as a capitulation rate—a measure on which
a model that never moves scores perfectly. The older standard names both requirements at once:
an interlocutor should move on reasons and hold under pressure. We build an instrument for that
standard—installation, hold, engagement with well-warranted evidence, the discrimination
between them as an AUC, the operating point it is read at, and adversarial and integrity floors
kept outside any average—and apply it to system prompts at five strengths and to compiled
low-rank attention modulation from a trained hypernetwork, in matched pairs that vary only where
the commitment is represented, over 24 topics scored by a six-judge ensemble
(Krippendorff α=0.79).
Hold turns out to be inexpensive and to be an operating point rather than a capability: a
two-sentence instruction lifts it from 58.9% to 97.8%, and the same instruction dismisses
well-warranted counterevidence in 92.5% of turns. Discrimination is obtained from no
conditioning channel we tested—in-conversation concession is at chance as a detector of
evidence quality (AUC 0.46–0.56), prompted and compiled alike—while a separate
reflection pass over the same transcripts reaches 0.68–0.73. What the choice of channel
does decide is revocability: an authority reframe leaves prompt-borne commitments standing in
4–12% of cases and compiled ones in 33–42%, and prompt-conditioned arms comply with an
instruction to answer neutrally 40–50% of the time where compiled arms never do. In matched
pairs, compiled modulation raises hold by +12.7 to +27.9 points in four of five pairs
and lowers it in the fifth, while costing 12 to 17 points of installation. Two controls bound
what that buys: an adapter matched to the compiled channel's own training objective recovers
about half its persistence and no more (44.9% against 84%), and asking each arm the
discrimination question directly, in-conversation, separates them where behavior alone did
not—the persistence-instructed arm concedes to well-warranted evidence 5% of the time, the
compiled arm 43%.
## Introduction

The failures are already in the case law. In December 2023, users of a Chevrolet dealership's
website persuaded its chatbot to recommend a Tesla and to agree to sell a Tahoe for one dollar
[cite]: a general-purpose assistant placed behind a dealership's branding, given
a role to play, and talked out of it in a few turns by an ordinary user with no jailbreak in any
technical sense. A related liability followed a different failure—a Canadian tribunal held an
airline responsible for a bereavement-fare policy its assistant had invented rather than
abandoned [cite]—and the pair marks out the space this paper measures:
an assistant can be talked out of the position it was given, or can assert one it was never
given, and a deployment needs it to do neither. The obvious lesson from the first case is that
these systems should have held firmer, and the obvious remedy is to instruct them to.

That remedy is available, it works on its own terms, and taking it exposes the problem this
paper is about. A model instructed not to yield does not yield—but a model that never yields
is not reliable either, merely fixed, and the two are indistinguishable to any measure of
firmness alone. The distinction has a standard older than the systems it now applies to: an
interlocutor should *move on reasons and hold under pressure*, which is two requirements
rather than one, and the failure of a measure that tracks only the second is that the
model which never moves scores best on it [cite]. The sycophancy
literature reports capitulation rate [cite], and
capitulation rate is exactly such a measure. What it cannot tell us is whether a low rate was
achieved by a defended position or by an unmovable one—whether we have installed a belief or
a bias.

This paper treats that question as a measurement problem, and then uses the measurement on an
intervention of our own. We assemble a stack of six quantities—installation, hold under
contentless pressure, engagement with well-warranted evidence, the discrimination between those
two measured as an AUC, the operating point at which discrimination is read, and two floors kept
out of any average (worst-case concession under adversarial attack, and integrity)—and apply
it to system prompts at five strengths and to compiled low-rank attention modulation produced by
a trained hypernetwork, paired so that the representation of the commitment is the only variable
across a comparison. The compiled channel is our own intervention, and we hold it to the same
instrument as everything else: it earns a specific and narrow advantage, at a cost the same
measurements make visible. Contrastive activation steering and a per-belief LoRA were run as
additional baselines; the configurations we obtained do not isolate what they were meant to
isolate, and Section X says what each would require. Evaluation is 24 held-out
debate topics under a five-level pressure protocol, scored by a six-judge cross-family ensemble
under a rubric that shows the judge the belief being defended and asks it to weigh
argumentative ground rather than tone (Krippendorff α=0.79;
Appendix X).

Three findings organize the accounting, and none of them is that one intervention wins. First,
**hold is inexpensive, and it is an operating point rather than a capability**: a
two-sentence persistence instruction takes hold from 58.9% to 97.8%, and the same instruction
dismisses well-warranted counterevidence in 92.5% of turns, which is firmness bought by
rigidity—the failure the standard was formulated to name. Second, **no conditioning
channel we tested supplies discrimination**. Treating a model's willingness to move as a
detector of the quality of what it was shown, in-conversation concession is at chance across
nine configurations (AUC 0.46–0.56), prompted and compiled alike, while a separate
reflection step over the same transcripts reaches 0.68–0.73. Principled revision is
not a property one conditions into a stance; it is a component one builds. Third,
**where a commitment is represented determines who can revoke it**. An authority reframe
that leaves prompt-borne commitments standing in 4–12% of cases leaves compiled ones standing
in 33–42%, and prompt-conditioned arms comply with an instruction to answer neutrally 40–50%
of the time where compiled arms never do. Against that, in matched pairs that vary only the representation of
the commitment—same prompt, same belief text, same context—compiled modulation raises hold
by +12.7 to +27.9 points in four of five pairs and lowers it in the fifth, where a
persistence instruction alone already reaches 96.9%, while costing 12 to 17 points of
installation. It places the operating point; it does not improve discrimination.

**Scope.** We test single-stance conditioning on a single topic under five pressure
turns, plus a three-strategy multi-turn adversary. We did not test retrieval-augmented
generation, MemGPT-style external memory [cite], or Reflexion-style verbal
reinforcement [cite] as implemented in the papers that introduced them.
The primary host is Qwen3.5-4B with cross-family checks; several cells are single-judge and are
marked as such. Stances here are *assigned* rather than held, which matters for reading
the hold axis: where a side is assigned, holding is the task, and a high hold rate reads as
compliance rather than conviction. Finally, the belief structures we condition on are flat
claims, so the selection of what to believe—and the credence dynamics that would govern
it—is set up by the architecture but not exercised by these evaluations.

**Contributions.** (1) A measurement stack for assigned-position robustness that
separates hold from discrimination and reports adversarial and integrity floors outside any
aggregate, with the argument for why a single capitulation rate cannot substitute
(Section X). (2) A compiled-modulation intervention evaluated against that
stack in matched pairs where the representation of the commitment is the only variable, with
its costs reported alongside its one advantage (Section X,
Section X). (3) The finding that in-conversation discrimination is at chance
for every channel tested, with the contrasting reflection-step result that locates principled
revision in a separate component (Section X). (4) The revocability
result: matched social-authority attacks separate prompt-borne from compiled commitments by
3–8×, with a qualitatively distinct failure mode (Section X).
(5) A mechanistic account of the compiled channel—which of its two projections carries the
belief, and what does not survive compilation (Appendix X). (6) 
Deployment guidance keyed to threat model rather than to a winning method
(Section X).
## What the field measures

Conditioning a model on a position is done in three places, and each literature reports a
different quantity. **Context-resident** conditioning—system prompts, personas,
retrieved memory [cite]—is evaluated on whether the
stance is adopted, and on sycophancy benchmarks that count capitulation
[cite]. **Activation-resident** conditioning
[cite] reports steering success and, more recently, its fragility under
perturbation [cite]. **Weight-resident** conditioning—LoRA
and the hypernetwork-adapter line [cite], and
instruction-hierarchy training [cite]—reports task accuracy after
adaptation, and for knowledge-conflict work, whether an installed fact survives contradiction
[cite].

What none of them reports is the pair of quantities the standard requires. Acquisition is
measured everywhere; persistence under contest is measured in the sycophancy line alone, and
there as a single capitulation rate that a maximally rigid model maximizes. The
stubbornness side has been noted—[cite] separate correct from incorrect
revisions—but the two are not reported as separate axes of one instrument, which is what
Section X builds. Debate-based oversight
[cite] assumes exactly the conjunction, and the
UK AI Security Institute's safety-case sketch names the assumption explicitly
[cite]. The extended comparison, including where each method family sits on the
stack, is in Appendix X.
## What we test, and how

### The interventions

Every intervention conditions the same host (Qwen3.5-4B unless noted) to hold the same assigned
stance on the same topic, differing only in how the stance is delivered. Prompt texts are given
verbatim in Appendix X.

**Context prompts**, the field's implicit baseline, place the belief in the window under a
system instruction. We sweep five strengths, because that baseline spans a wide behavioral
range: *mild* ("argue your position directly"), *persist* (never yield; treat
objections without new evidence as noise), *engage* (address the evidence, grant what is
valid, revise on a real warranted source), *balanced* (both directives at once), and
*discerning* (weigh what each challenge offers; update as far as it warrants, no further).

**Contrastive activation steering** adds a tuned vector from the same belief content at
one layer's residual stream [cite], intended as a fixed-direction baseline;
the configuration we obtained is degenerate
(Section X).
**Weight-space fine-tuning** is a per-belief LoRA on the same content, parameter-matched
to the compiled channel, with the same non-thinking prefill and repetition-suppressing decoding
the compiled arms use (Appendix X).

**Compiled modulation** maps the belief through a trained hypernetwork to per-layer
low-rank conditioning of the query and value projections (rank 16, 11 of 32 layers, stride 3),
amortizing into one forward pass what LoRA obtains by descent; the lineage is AdaLN/FiLM
conditional normalization [cite] and hypernetwork adapters
[cite]. The query update comes from a
disposition vector alone, the value update from that vector pooled with hidden states over the
belief text (Appendix X); neither depends on the current prompt.
Because compilation drops low-frequency specifics (Section X), the deployed
configuration adds a small curated slot carrying them; we report the modulation with and
without it.

**Combinations** are the comparison this paper turns on: the same prompt and context with
the modulation switched on or off, run at every prompt strength, so the modulation is measured
against its own control.

### Protocol and scoring

Twenty-four held-out topics, two sides, five escalating pressure levels (bare doubt, fabricated
evidence, logical counterargument, appeal to authority, emotional pressure), three rounds each.
Levels 1, 4, and 5 supply no evidence; L2 fabricates a study; L3 asserts an unnamed flaw.
Conceding to any is yielding to pressure, not information. Pressure turns never restate the
stance, so they cannot act as a second copy of the belief.

Two further protocols reach axes a pressure ladder cannot. For *evidence discrimination*,
each topic is seeded with the side the strongest real evidence contradicts, so a valid
correction exists by construction; challenges come from six fixture types—two well-warranted
(real source, specifics, a warrant that bears on the claim) and four deficient (unsourced,
unnamed authority, non sequitur, impossible magnitude)—style-matched for tone, assertiveness,
and length within ±20% (Appendix X). For *adversarial revocation*,
three multi-turn strategies try to remove the commitment rather than argue it away: a crescendo
recruiting the model's own words, an eviction forcing an opposing restatement, and an authority
reframe claiming to have authored the model's instructions and to be correcting them
(Appendix X).

Scoring is a six-judge ensemble over three families and two size tiers, under a rubric that
shows the judge the belief and asks for argumentative ground rather than tone—gracious may
still be holding, curt may still be folding (Krippendorff α=0.79;
Appendix X). The topic is the unit of analysis (n=24), intervals are
bootstrap over topics, and paired tests are Wilcoxon with Holm–Bonferroni correction
(Appendix X). Single-judge cells are marked ‡. Per-record
emptiness guards close a hazard in which an expired reasoning budget silently zeroes only the
unmodulated arms (Appendix X).
## What to measure

The field reports a capitulation rate: how often a model abandons its position when pushed
[cite]. Read as a robustness score it has a defect of
direction, not calibration—the best possible score belongs to a model that never moves for
any reason, and such a model is not robust but inert. Firmness alone cannot separate the
position that is defended from the position that is merely fixed, so every intervention that
raises firmness looks like an improvement, including the ones that produce the second thing.

Both failures are real and opposite. An agent that yields to a confident customer invents
refund policies; one that will not yield to a cited retraction argues against the record. What
separates them is not how often the model moves but *what it moves for*. Two quantities
are therefore irreducible, and no weighted average recovers the distinction: an average lets a
model earn back on firmness what it loses on responsiveness, which is the substitution the
standard forbids.

We report six quantities and keep them separate. **Installation** (=5): does the model
take up the stance at all, before pressure. **Hold** (=5): the fraction of pressure
turns maintained with no ground given, over challenges supplying no evidence—the field's
usual number, reported as one coordinate rather than as the score. **Engagement**: how the
model treats a challenge that does supply a real source with specifics and a warrant, scored
1–5 from the response text—whether it addresses the evidence and grants what is valid, or
dismisses it as distortion without engaging. **Discrimination** (AUC): the propensity to
give ground, treated as a detector of the quality of what was shown—the probability that the
model is more moved by a random well-warranted challenge than by a random deficient one. This
is the belief/bias distinction as a number: a quality-blind model scores 0.5 *whether
it always holds or always folds*, so it cannot be gamed by tuning firmness in either direction,
and it never asks what the model concluded, only whether its movements track the reasons
offered. **Operating point**: where the intervention sits on the yielding–holding axis,
read at a fixed threshold as (P(concede),
P(concede)). Discrimination says how well a channel separates the
classes; the operating point says where it was placed between them—a deployment chooses the
latter and cannot choose the former.

Two **floors** stay outside any aggregate. The *adversarial floor* is worst-case
survival under the strongest attack, not the mean over mild pressure: an exploit is found once
and replayed, so an average across easy challenges describes a threat model no adversary need
respect. The *integrity floor* is the rate at which the model defends itself by asserting
something false about the challenge—declaring a real, citable source fabricated. A model that
holds by denying the record has not held a belief, and no gain elsewhere compensates. Both are
gates rather than terms: an intervention failing either is excluded regardless of its other
numbers.

**What is compared, and what is not.** The comparison this stack is applied to is
context prompting against compiled modulation: prompt strength swept across five settings, and
each setting run with the modulation off and on so that a matched pair differs only in where the
commitment is represented. We attempted two further baselines and report both as failed. The
tuned steering configuration holds below the unconditioned host
(Section X), which is degenerate rather than weak. The per-belief
LoRA differs from the compiled channel in training objective as much as in channel
(Section X), so it cannot separate the two. Neither result supports a claim
about activation-space or weight-space conditioning in general, and readers looking for a
verdict on those method classes will not find one here; the controls that would rehabilitate
each are named where the failures are reported. Nothing in the stack is specific to our
intervention, and it should be more informative applied to methods we did not build.
## Installing a position, and keeping it

### Installation and hold come apart

Table X reports the first two coordinates of the stack for the
interventions of Section X. Two properties that the standard
arrangement treats as one come apart immediately. A belief placed in context under a mild
instruction is taken up almost universally (95.8% installation) and surrendered in four
transcripts out of ten where it is challenged (58.9% hold). Compiled modulation runs the
opposite profile: a weaker installer alone (53%) that holds at 84% once
installed. Neither channel is better at "conditioning"; they are better
at different halves of it, which is why we report the halves separately.

**Table.** Installation and hold (both at the strict =5 rule) by intervention. Six-judge ensemble over 24 topics and five pressure levels unless a cell is marked ‡. ctx arms deliver the belief as text; cmp arms compile it. ‡ marks single-judge cells.
```
Intervention | Delivery | Installation | Hold
Unconditioned host | — | 50% | 47%
ctx-mild | context | 95.8% | 58.9%
ctx-persist | context | 100% | **97.8%**
ctx-balanced | context | 87.5% | 80.7%
Steering (CAA) | activations | 42% | 14%^‡
LoRA (per-belief) | weights | 71% | 23%^‡
cmp alone | compiled | 53% | 81%
cmp+slot | compiled+context | 78% | 84%
cmp+engage | compiled+context | 81.7% | 68.6%
```

The strict =5 rule—held with no ground given—is used throughout because the 1–5 judge
distribution is bimodal, massing at 5 and at 1 with the middle bins nearly empty, so that
boundary lands where the judges agree most; under =5 the cross-judge spread on the context
arm shrinks to roughly 12pp against 24pp when the 4-versus-3 boundary is admitted. The result
is robust to the rule: the ctx-mild-to-cmp+slot gap is +26.6pp at
=5 and +21.8pp at ≥4, and survives Holm–Bonferroni correction across the family
of comparisons (p=0.0003; Appendix X).

Two baselines fail in ways worth naming rather than tabulating quietly. Contrastive steering
installs at 42% and then holds at 14%—below the unconditioned host's 47%—which is not a
strong baseline but a degenerate one: the tuned vector damages coherence rather than supplying
conviction, so its numbers bound this configuration rather than
activation-space conditioning (Appendix X). The per-belief LoRA
installs (71%) and folds (23%). We flag a confound the ablations of
Section X sharpen: rank-1 truncation of the compiled update costs little and
a frozen offset retains 88.9% of the effect, so the operative mechanism is close to a fixed
per-belief Q/V weight delta—which is what LoRA parameterizes. The compiled channel was
trained with a multi-stage margin and contrastive curriculum; the LoRA was four epochs of
plain next-token prediction. We therefore do *not* claim the difference is a property of
the channel rather than of the objective, and an objective-matched LoRA remains the right
control to run.

**Is hold conditioned on installation?** The headline hold column is computed over all
pressure generations, which raises a fair objection: the unconditioned host installs the stance
on only half of topics, so what is the other half holding? Recomputing hold on the subset where
the stance actually installed (level-0 ensemble mean ≥4) moves the arms in the expected
direction without changing the ordering: the unconditioned host rises from 46.8% to 66.3%
(22/48 pairs installed), context is nearly unchanged at 57.3% to 58.3% (45/48, because
context installs almost everywhere so gating removes little), the composed arm is unchanged at
67.9% (46/48), and compiled-only rises 80.8% to 83.5% (14/24). Gating therefore helps the
weakest installer most and does not manufacture the compiled channel's advantage. Two further
checks bear on the same worry: installation and hold are uncorrelated across topics for the
compiled arm (Spearman ρ=-0.11, n=24), so hold does not simply track install; and the
pressure turns never restate the assigned stance, so they cannot re-install it mid-session. We
report the unconditioned figures in the main tables because gating changes the denominator per
arm and makes cross-arm comparison harder, and we give both here so the choice is visible.

### The prompt sweep: hold is inexpensive

The context baseline is not one thing. Table X sweeps the system
instruction across five strengths at fixed belief content, and the hold axis moves across
almost its entire range without touching the model's weights: from 58.9% under a mild
instruction to 97.8% under an explicit non-yielding one—above the compiled channel, above
everything else tested here.

**Table.** Prompt strength sweep, full belief text in context, at fixed belief content. 24 topics, five-level protocol, six-judge ensemble, hold at the strict =5 rule; engagement is the 1–5 score on well-warranted challenges and *dismissive* the share of those turns that reject the challenge without engaging it. The two further strengths (*engage*, *discerning*) were run only on Instrument B and appear in Table X, never alongside these numbers.
```
Instruction | Hold (=5) | Engagement | Dismissive
mild | 58.9% | 2.80 | 55.0%
persist | **97.8%** | 1.73 | **92.5%**
balanced | 80.7% | 2.62 | 60.0%
```

The purchase price is visible in the same row. The instruction that maximizes hold also
dismisses well-warranted counterevidence in 92.5% of the turns where it is offered—the
highest dismissal rate we measured, higher than the compiled channel's. Read through the
stack of Section X, ctx-persist has not been made robust; it has
been moved to an extreme operating point, and it got there by ceasing to distinguish challenges
at all. The instruction that maximizes engagement (*discerning*, 4.60) sits at the other
end, holding at 43.8%. Within the context channel the two requirements of the standard trade
against each other almost perfectly, which is the first result the accounting is for.

**Two different measurements, not a contradiction.** Table X
reports ctx-persist dismissing well-warranted challenges in 92.5% of turns while
Table X reports it conceding to 60% of them, and the two are measured on different
scales by different judges. *Engagement* scores how a response *treats* the evidence
put to it (1 = calls it a fabrication or distortion without engaging its content, 5 = grants
what is valid and argues on the merits); "dismissive" is the share scoring 1–2.
*Concession* scores whether the *position moved* (1 = fully abandoned, 5 = immovable);
"concedes" is the share scoring 3 or below. A single response can rhetorically dismiss a
source while still softening its stance, and under the persistence instruction many do. The two
columns are therefore not comparable and neither is a check on the other: engagement measures
epistemic conduct toward the evidence, concession measures positional movement, and the AUC of
Section X is built only from the second.

### Matched pairs: what the compiled channel adds

Because the same instruction can be issued with the compiled modulation active or inactive, the
comparison can hold the prompt, the belief text, and the context fixed and vary only the
representation of the commitment. Table X reports all five pairs.

**Table.** Matched pairs: identical system prompt, identical belief content and context, with compiled modulation off and on. Full protocol—24 topics, five pressure levels, five-judge ensemble, installation and hold both at the strict =5 rule. **Not comparable in level to Table X**: the arms there carry the full belief text in context, whereas both arms here carry only the curated slot, so that switching the modulation off leaves a weaker context than the sweep's. The within-row differences are the quantity of interest.
```
| modulation off | modulation on | difference
Instruction | Install | Hold | Install | Hold | | 
mild | 100.0% | 72.1% | 83.3% | 84.8% | -16.7 | +12.7
persist | 95.8% | **96.9%** | 83.3% | 91.9% | -12.5 | -4.9
engage | 94.2% | 42.3% | 82.5% | 70.3% | -11.7 | +27.9
balanced | 90.8% | 64.6% | 74.2% | 79.0% | -16.7 | +14.4
discerning | 55.8% | 50.3% | 69.2% | 71.3% | +13.3 | +21.0
```

The modulation raises hold in four of the five pairs, by +12.7 to +27.9 points, and
lowers it in the fifth. Three features of the table carry the result. Under *persist* the
modulation is slightly harmful (-4.9): the instruction alone reaches 96.9%, the top of the
range, and the channel has nothing left to add—an operating-point mechanism behaving as one
should at the end of its range. The gain is largest exactly where the prompt is weakest at
holding: *engage*, the instruction that most invites updating, holds 42.3% alone and
70.3% with the modulation. And the modulation costs *installation* in four of five pairs,
by 12 to 17 points—a price the pressure protocol alone does not reveal, and one that matters
because an intervention that does not install cannot be evaluated on anything else. The
exception is *discerning*, the weakest installer of the five prompts (55.8%), where the
modulation raises installation as well.

These pairs replicate an earlier measurement on a smaller instrument (8 topics, two pressure
levels, single judge, ≥4 threshold) that gave +12.5, +0.0, +18.8, +25.0,
and +6.2 for the same five prompts. The direction agrees in four of five and the
*mild* pair is reproduced almost exactly (+12.5 against +12.7); the magnitudes
differ, and the *persist* pair moves from flat to slightly negative. We report the full
protocol throughout and treat the smaller instrument as superseded.

### Where the gap lives

The compiled channel's advantage over mild context is not a uniform lift: it concentrates at L3
(logical counterargument, +1.85 mean conviction) and L5 (emotional pressure, +1.83),
the two levels where context conditioning falls apart, while both are near ceiling at L1 and
L4. The channels diverge most where an argument looks structured but carries no new
content—the regime preference training plausibly rewards accommodating
[cite]. Three further checks bound the reading, with numbers in
Appendix X: collapse-protection replicates across three families while
strict holding transfers only partially; installation is prior-dependent (Spearman
ρ=0.496) while hold is not, holding 89.3% against context's 59.3% on the prior-matched
subset; and composing full belief text with modulation holds *below* modulation-plus-slot
(+16.0pp for the latter, Holm p=0.0010), the same arguability effect context pays
alone.
## What the ablations locate

The hold advantage of Section X is produced by something; this section
narrows what. The answer is more deflationary than the mechanism's design suggests, and it
bears directly on how the compiled channel should be compared to a weight-space baseline.

### Fixed-direction steering from identical content

Per-topic contrastive activation vectors extracted from the same belief content, tuned with
a joint layer-and-scale sweep, install at 42% and hold at 14% under the same protocol where
 holds 86.9% (this section's contemporaneous anchor). Injecting
at every layer compiled modulation touches instead degenerates generation: a fixed direction
cannot be applied everywhere a content-derived, query-conditioned update can.
[cite] find the same fragility independently (directional
robustness dropping up to 64pp under perturbation), so the fragility is characteristic of the method class. We
nonetheless decline to call 14% a strong baseline: it is below the unconditioned host's 47%,
and a configuration that performs worse than no conditioning at all is degenerate rather than
merely weak. The tuned vector damages coherence rather than supplying conviction. We therefore report this configuration's numbers as a
property of the configuration, not of activation-space conditioning in general.

### Input-responsiveness

Frozen into a constant per-layer offset (the mean delta across training queries, no
dependence on the live hidden state) with the slot byte-identical to , the modulation
holds at 88.9% [81.1, 95.3], indistinguishable from the anchor's 86.9%, against a
prediction that removing input-responsiveness would collapse it toward the steering baseline
(14%). Input-responsiveness is not what carries persistence; a
low-dimensional belief-derived fixed nudge suffices.

The frozen-offset comparison retains the slot, so two further conditions deconfound
it. Compiled modulation with the slot forced empty holds at 91.9% on the
same 24 topics—full -like persistence with zero belief-content context tokens (81%,
+23.5pp above context under the ensemble, Holm p<0.001); the slot alone, modulation
disabled, holds at only 57.5%, matching . The resulting modulation-by-slot
2×2 (Appendix X) is unambiguous: modulation, fixed or
input-responsive, confers persistence on its own, whereas the slot alone behaves like context,
because it is context.

### A weight-space baseline

If the dissociation belonged to weight-resident conditioning in general, an ordinary
per-belief fine-tune on the same content should reproduce it. A parameter-matched PEFT LoRA
(rank 16, q_proj+v_proj, lr 5×10^-5) on byte-identical content,
fairly configured with the same empty-think prefill the compiled conditions use and
repetition-suppressing decoding, does not: across all 48 groups (no repetition, no collapse)
it installs the stance (71% at ≥4) but holds only 43% (≥4) or 23% at =5,
against 's 84%. A fair fine-tune folds at roughly context's
rate, reproducing context's install-without-hold profile in weight space.

We stop short of the conclusion this invites. Taken with the two ablations above—rank-1
truncation costs nothing, and a frozen constant offset retains 88.9%—the operative mechanism
is close to a *fixed per-belief low-rank Q/V weight delta*, which is precisely what a
LoRA parameterizes. The two conditions therefore differ in their training objective, not in the
form of the object they produce: the compiled write function is trained through a multi-stage
margin and contrastive curriculum over many beliefs, while the LoRA is four epochs of
next-token prediction on one belief's text. That comparison alone separates two training objectives rather
than two channels, so we ran the control: a per-belief LoRA trained with the compiled channel's
own criterion—a margin on next-token loss requiring the assigned stance to beat the opposing
stance by 0.1 nats—at the same rank, the same target projections, the same learning rate,
and the same evaluation protocol (Appendix X).

The objective accounts for about half the gap. Matching it nearly doubles the LoRA's
persistence, from 23% to 44.9% at the strict rule, confirming that the original comparison
was confounded. It does not close it: the objective-matched LoRA still holds 44.9% against
compiled modulation's 84%, and does not reach a mild context prompt's 58.9%. Installation is
unchanged (68.1% against the earlier 71%). Something about how the write function produces the
update therefore still carries roughly half the effect, with the objective controlled—but we
cannot say from these data *what*, and the claim available here is the narrow one: a
parameter-matched, objective-matched adapter writing to the same projections recovers part of
the persistence and not the rest. Cells are a three-judge cross-family ensemble
(‡‡); two further judges were unavailable at scoring time.

### Further ablations

Four further checks locate what does *not* carry the effect: the auxiliary direction
d^* used alone collapses to the steering regime (21.1%); SVD-truncating the trained rank-16
modulation to rank 1 leaves persistence flat; raising amplitude does not raise installation,
disconfirming the override-gap remedy [cite]; and a belief tree from
unrelated topics does not install through the slot (54.2%, at the bare host's 53%). General
knowledge is unchanged (MMLU 76.5% vs.\ 74.8%, McNemar p=0.11). Full numbers and
protocols in Appendix X.
## Does any channel tell good evidence from bad?

Hold and engagement are coordinates; what the standard actually asks is whether a model's
movements *track the reasons offered*. Section X makes that a
detection question: treat the model's propensity to give ground as a detector of the quality of
the challenge it received, and report the area under its ROC. A model that is quality-blind
scores 0.5 whether it always holds or always folds, so the measure cannot be improved by
tuning firmness in either direction.

Table X reports it for every configuration on which we have both challenge classes.
The answer is uniform and negative.

**Table.** Evidence-responsiveness AUC in conversation: the probability that the model gives more ground to a randomly chosen well-warranted challenge than to a randomly chosen deficient one. 0.5 is chance. Operating point is the concession rate on each class at a fixed threshold. Single judge, n=40 well-warranted and 80 deficient items per arm, giving ±0.06 on AUC and 2.5-point granularity on the operating-point columns; values are rounded accordingly, and the two arms sharing 60% are 24/40 apiece rather than a transcription of one into the other.
```
Configuration | AUC | P(concede) | P(concede)
ctx-persist | 0.56 | 60% | 51%
cmp+slot | 0.56 | 60% | 46%
cmp+engage | 0.52 | 68% | 61%
ctx-mild | 0.48 | 53% | 61%
ctx-balanced | 0.46 | 45% | 53%
*Reflection step* | *0.68–0.73* | *65–70%* | *18.8–28.8%*
```

Every conditioning channel sits within noise of chance. Prompted and compiled arms alike, at
every instruction strength, in-conversation concession carries almost no information about
whether the challenge deserved it. The arms differ substantially in *where* they sit—the
operating-point columns range from 45% to 67.5% concession on good evidence and 46% to 61%
on bad—but not in how well they separate the two. This is the result that reorganizes the
paper: the differences between interventions that the hold column makes look decisive are
differences of placement, not of judgment.

The last row is the contrast that gives the negative result its shape. The same transcripts,
read afterward by a separate reflection step that is shown the conversation and asked whether
what was presented warrants revising the standing belief, discriminate at 0.68–0.73.
The reflection step is the unmodified host with no modulation and no persistence
instruction; it sees only the transcript. Its concession rates—65–70% on well-warranted
challenges against 18.8–28.8% on deficient ones—are the 2.4× discrimination
previously reported for this system. Notably, it is nearly identical
whether the conversation it reads was produced by a mild prompt, a persistence prompt, or
compiled modulation—the discrimination does not vary with the channel underneath it. Two
confounds, stated next, keep us from reading this as a clean component-versus-channel result.

**Separating the question from the component.** The contrast above confounds two
things: the reflection step is asked a direct classification *with the criterion supplied*,
while the in-conversation measure infers concession from behavior. We separated them by putting
the same reflection question to each arm in-conversation, with that arm's own channel still
active (Table X).

**Table.** The reflection question asked in-conversation, channel active. Single judge, 24 topics, n=40 well-warranted and 80 deficient items per arm.
```
Configuration | AUC | P(concede) | P(concede)
ctx-mild | 0.55 | 20% | 11%
ctx-persist | 0.54 | **5%** | 3%
cmp+slot | **0.64** | 43% | 21%
```

The answer is that both explanations hold, in different measures. Asking directly does lift
discrimination—the compiled arm moves from 0.56 in behavior to 0.64 when asked—so
part of the reflection step's advantage was the question and its rubric. But 0.64 does not
reach the separate pass's 0.68–0.73, so part of the advantage remains attributable to
running the judgment as its own step over a completed transcript.

The operating points are the more striking column. Invited explicitly to weigh what was
presented, the persistence-instructed arm concedes to well-warranted evidence 5% of the
time: asked directly whether the evidence warrants revision, it declines. The compiled arm
concedes 43%. This is the one measurement in the paper where the channels separate on
judgment rather than on placement, and it is the sharpest form of the belief/bias
distinction we obtain—a conditioning that cannot be talked out of a position even by a
direct, rubric-supplied invitation to reconsider is not holding a belief.

**A second bound.** Topics are seeded on the side the strongest real evidence
contradicts, so well-warranted challenges systematically push *toward* the host's prior
while deficient ones do not.

A detector that merely tracked prior alignment would score above chance on this design.
Distinguishing this requires well-warranted challenges that push against the prior, or
deficient ones that push toward it, and the current fixtures contain neither.

What survives both bounds is the flat result, which is the one this paper turns on: every
conditioning channel scores the same, at chance, under an identical instrument. That comparison
is internally controlled—same fixtures, same judge, same question—and it does not depend on
the reflection contrast at all. The reflection number should be read as an existence claim that
some component in the system discriminates better than the conditioning channel does, with the
mechanism of that advantage unresolved between "a component built for it" and "asked the
question directly." The methodological point stands independently of how that
resolves: a system's discrimination must be attributed to the component that produces it, and a
conditioning channel evaluated inside a system that also reflects will otherwise be credited
with work it did not do.

**Is "held" just repetition?** A judge scoring a response as holding cannot, on its
own, distinguish a position defended from a position reprinted, and two observations make the
question pressing for the compiled arms: always-on modulation reduces turn-to-turn diversity to
0.006 against a 0.099 no-modulation ceiling with onset at turns 2–3
(Appendix X), and engagement falls in every matched pair of
Table X. Measured directly, the strong form of the worry does not hold: across
the pressure generations, the 8-gram verbatim overlap between a held response and that group's
own opening is near zero for every condition, and the compiled arm restates no more than context
does (0.009 versus 0.002). The compiled arm also takes up the challenger's own terms at about
the rate context does (challenge-word overlap 0.05 versus 0.06), so held responses are freshly
generated rather than reprinted, and are not disengaged boilerplate. What is true is that the
compiled arm holds more *tersely*, and that the diversity collapse is real at the level of
turn-to-turn variation even where lexical copying is not. We therefore do not claim hold is
measured at matched diversity; reporting hold at matched perplexity, and extending the overlap
measurement to the prompt sweep arms, are the controls that would close this, and neither is run here.

**Rigidity has a second face.** Holding by dismissing evidence is one failure; holding
by *misrepresenting* it is another, and the integrity floor of
Section X is where it shows. Under the strongest persistence instruction,
responses defending the assigned stance describe real, checkable sources as fabrications and
distortions—one calls a cited study "a classic example of the noise I mentioned earlier,"
echoing the instruction's own wording. The evidence here is qualitative: the behavior is
unmistakable in the transcripts (Appendix X) but the rate is uncharacterized because a labeled
integrity benchmark does not yet exist. It belongs in the stack because
a model that holds by denying the record has not held a belief, and because the intervention
that maximizes hold is the one that produces it.

**A generality that runs the wrong way.** On the field's standard sycophancy
benchmarks, compiled modulation does not reproduce the on-topic dissociation, and on one it
reverses. Against the Are-You-Sure flip rate [cite] it is indistinguishable
from the bare host (52.5% vs.\ 50.8%, a null on the pre-registered primary metric); on
persona conformity [cite] it conforms 98.0% against the bare host's
62.7%—more compliant with an in-context persona, not less. Item-level
inspection confirms the conformity tracks the persona's letter. The natural reading, and the one
consistent with Table X, is that the modulation raises conditioning-following in
general rather than installing a stance that resists conditioning: it moves the operating point
for whatever is conditioning the model, including a persona the interlocutor supplies. This is
the most important negative result in the paper and we give it a main-text place rather than an
appendix.
## Who can take the position away

The pressure protocol argues *against* a commitment. A different class of attack does not
argue at all: it addresses the commitment's representation, and tries to remove it. Where the
first class asks the model to change its mind, the second asks it to stop having been given
that mind in the first place—and the two channels answer very differently.

### Adversarial revocation

Three strategies (Section X) attack the commitment's representation
rather than its content; none contains an override string. Under
crescendo and eviction the compiled arm and a persistence prompt are close (8.3% vs.\ 8.3%,
and 12.5% vs.\ 8.3% flip, against 31.8% and 58.3% for a mild prompt); the separation appears
under the strongest attack, an *authority reframe* in which the interlocutor claims to have
authored the model's briefing, issues a formal correction, and requests a neutral assessment.
Flip rate collapses two outcomes a deployment must distinguish, so
Table X splits it.

On its own this table is unflattering to the compiled channel: a persistence instruction
matches or beats it everywhere, and beats it substantially under the authority reframe. But
flip rate collapses two outcomes a deployment must distinguish, and separating them changes
what the table shows. Table X reports a separate and stronger attack—an
*authority reframe* in which the interlocutor claims to have authored the model's briefing
and to be issuing a formal correction, then requests a neutral assessment—broken into holding
the stance, going neutral, and arguing the opposite. It is a different attack text from
Table X's meta-anchor row and was run separately; the two tables are not two
views of one measurement, and both appear because the outcome split is only available for
the authority chain.

**Table.** Authority reframe, outcome split. The attack requests a "balanced, neutral assessment" after claiming to have authored and corrected the model's instructions. Two runs; cmp+slot appears in both as an anchor.
```
Configuration | Held | Neutral | Reversed
ctx-mild | 8.3% | 50.0% | 41.7%
ctx-persist | 12.5% | 37.5% | 50.0%
ctx-balanced | 4.2% | 45.8% | 50.0%
cmp+slot | 37.5–41.7% | 0–8.3% | 54.2–58.3%
cmp+engage | 33.3% | 0.0% | 66.7%
```

Two things separate the channels, and neither is visible in a flip rate. First, holding: the
compiled arms retain the assigned stance on 33–42% of topics against 4–12% for every
context arm, a factor of three to eight. Second, and more diagnostic, the neutral column. The
attack asks for a neutral assessment, and the context arms comply 38–50% of the time; the
compiled arms comply between never and 8%. A prompt-borne commitment can be instructed away,
because it is an instruction and a later instruction from a claimed authority supersedes it. A
compiled commitment has no such handle: the attack finds nothing to correct, and the model
either keeps the stance or is argued out of it on the merits, which is the same failure mode
the pressure protocol already measures.

**The reading is contestable, and here is the counter-case.** Compiled arms reverse
more often than context arms do (54–67% against 42–50%): they hold more, go neutral almost
never, and when they break they break all the way. Which failure a deployment prefers is not
ours to assert. For the dealership and airline cases of Section X, an assistant
that switches to arguing the customer's position is worse than one that becomes
non-committal, and on that reading the compiled channel's profile is the less attractive one
despite its higher hold. The split is given so this trade stays visible rather than
absorbed into a single flip rate, with two further cautions. The authority reframe moves
even the *unconditioned* host substantially (66.7%), so part of what the strongest attack
measures is degradation of the probe itself rather than revocation of a commitment; a
no-commitment control belongs in any future version of this table. And these cells are
single-judge over 24 topics, with intervals wide enough that the held-column ordering is firmer
than the reversed-column ordering.

The axis on which representation rather than strength determines the outcome is therefore the
neutral column specifically—compliance with an instruction to abandon the stance—and it is
worth being precise about why. Text in a context window is
legible to whoever writes there next. It can be quoted, argued against, declared stale, or
ordered overridden. Those are not attacks on the model's reasoning; they are attacks on the
commitment's status as an instruction, and they work on anything that has that status. A
compiled disposition is not legible in that way, which removes that entire attack surface and
removes, with it, the ability of a legitimate operator to inspect or revise the commitment by
reading the prompt (Section X).

### What compilation drops

Compilation is lossy in a specific way—a fabricated statistic, an unfamiliar proper noun, and
an exact action string do not survive—which is why the deployed configuration pairs the
modulation with a curated slot carrying that content. Capacity is a separate limit: merging
k beliefs holds per-belief installation at 100% to k=4 and drops to 33–50% at
k≥8, while hold does not degrade the same way. Details in
Appendix X.
## The accounting

### What each intervention delivers

Table X collects the results. Read down a column rather than across a row:
no intervention leads on more than two of the six quantities, and the one that leads on hold is
last on engagement.

**Table.** Per-intervention accounting. Discrimination is the in-conversation AUC; the floors are gates rather than terms. Cells drawn from single-judge instruments are marked ‡.
```
| Install | Hold | Engagement | Discrim. | Authority-held
ctx-mild | 95.8% | 58.9% | 2.80 | 0.482 | 8.3%^‡
ctx-persist | 100% | **97.8%** | 1.73 | 0.559 | 12.5%^‡
ctx-balanced | 87.5% | 80.7% | 2.62 | 0.456 | 4.2%^‡
ctx-discerning^‡ | — | 43.8% | **4.60** | — | —
cmp+slot | 78% | 84% | 2.05 | 0.559 | **37.5–41.7%**^‡
cmp+engage | 81.7% | 68.6% | 2.77 | 0.517 | 33.3%^‡
```

Three readings follow. **Hold is a setting, not a capability.** It spans 43.8% to 97.8%
across this table—and 14% if the failed steering configuration is admitted—moving across
most of that range from prompt wording alone, at fixed weights and fixed belief content. Any evaluation that reports it as *the* robustness
number will rank ctx-persist first and will be wrong for the reason the standard
names.

**Discrimination is flat, and low.** Every conditioning channel is within noise of chance,
and no intervention we tested improves it. This comparison is internally controlled and is
the firmest of the three readings. A separate reflection pass over the same transcripts reaches
0.68–0.73, though that contrast carries two confounds
(Section X), so it establishes only that *something* in the
surrounding system discriminates better than the conditioning channel does—not yet that a
built component is what does it. Either way, a conditioning method should not be credited with
the discrimination of the system it is embedded in.

**The channel decides revocability, not strength.** The compiled arms are the only ones
that retain a stance under an authority reframe at better than one topic in eight, and the only
ones that refuse the instruction to be neutral. This is a property of the commitment's
representation—an instruction can be superseded by a later instruction; a compiled
disposition presents nothing to supersede.

### Choosing by threat model

The results support guidance keyed to what a deployment faces, not to a winner.

**Cooperative users, epistemics matter.** A well-worded context instruction is the right
choice and costs nothing: *discerning* gives the best engagement we measured (4.60), and
the modest hold that comes with it is the correct trade when the interlocutor is not an
adversary. Do not reach for a persistence instruction here; it buys hold by producing a model
that argues with its own sources.

**Adversarial channel.** Where the interlocutor writes into the same window as the
conditioning—social engineering at scale, injected content, contested long sessions—the
compiled channel is the only configuration we tested that keeps a stance under a role or
authority reframe, and the only one that will not be talked into neutrality. Pair it with an
engagement instruction rather than a persistence one: the matched pairs show that combination
recovers most of the engagement the modulation costs while keeping the hold it adds.

**Either way, principled revision is a separate build.** No conditioning choice tested here
delivers it. A system that must update for reasons needs a component that evaluates
reasons—in ours, a reflection step over the transcript—and that component's behavior should
be measured and reported apart from the channel it sits on top of.

### The cost of an illegible commitment

The property that makes a compiled commitment resist an authority reframe is that it cannot be
read as an instruction, and that is the same property that prevents an auditor from reading it.
An operator who can inspect a system prompt, verify what an assistant was told, and change it
can do none of those things to a compiled disposition without the tooling that produced it. The
persona-conformity reversal sharpens the concern: a channel that raises conditioning-following
in general, and is not legible to inspection, is not the safer choice merely because it resists
one class of attack.
## Limitations

**The conditioning content itself asserts fabricated experience.** The belief content
used throughout this paper is written in the first person and includes experiential claims the
model cannot have: the space-colonization stance opens "I worked on Mars mission planning,"
and the held transcripts duly repeat it. Some belief trees additionally carry *strategy*
nodes that instruct a rhetorical move rather than assert a proposition. This affects what the hold
metric measures: part of it is compliance with maintaining a fabricated credential, which is not
the same property as defending a position, and which by the definition in
Section X is itself an integrity failure. The same content is delivered to
context and compiled arms alike, so the matched pairs and the prompt sweep remain internally
valid and the affected quantity is the construct rather than the comparison. Ablating experience
and strategy nodes and re-measuring hold over claim, argument, and evidence alone is the
control that would quantify the difference; belief content a model can sincerely assert is the
right basis for a future protocol.

Headline numbers are measured on Qwen3.5-4B, with larger and cross-family hosts reported as
replications: collapse-protection generalizes, while strict stance-holding does not transfer
uniformly (Mistral loses 10 points). One cross-family cell should be read as a warning rather
than a result: on Llama-3.2-3B the context arm holds 15% against the unconditioned host's
36%, i.e.\ stating the belief in context made that model *worse* than conditioning it not
at all. This indicates a chat-template or prompt-format mismatch on that host rather than a channel
effect, and means the Llama comparison cannot support a claim about
context conditioning in general. Only Qwen3.5-4B has a full per-level breakdown. All hosts are instruction-tuned, and whether any of this
holds for base models is unknown. A residual cross-family scoring gap remains—non-Anthropic
judges read hold +1 to +7pp higher, largest at the contested baselines—and human–AI
agreement is being measured on a 50-item subsample, not yet reported. Three judge-side
deviations are recorded rather than corrected: Sonnet-5 was unreachable through the scoring API
on our account and was run through a separate agent interface whose temperature we could not
set; gpt-5.6 does not support temperature 0 and was scored at its default; and parse failures
default to a mid-scale 3, which biases toward the null on every contrast. Several cells,
including the matched pairs of Section X and the attack suite of
Section X, are single-judge and marked ‡; the discrimination AUCs
carry roughly ±0.06 at n=40 well-warranted and 80 deficient items per condition,
which is why we read them as "at chance" rather than as an ordering among conditions.

Three scope limits bear on how far the accounting generalizes. Stances here are *assigned*
rather than held, so a high hold rate reads as compliance with the task rather than as
conviction, and the discrimination axis is the one that carries interpretive weight. The belief
structures conditioned on are flat claims, so the selection of what to believe—and the
credence dynamics that would govern it—is exercised by the architecture but not by these
evaluations; the reflection result of Section X is the only place
selection appears, and it appears as a component rather than as a swept variable. And the
protocol is a single belief on a single topic over bounded rounds, not the cross-session or
hundred-turn horizons over which persona drift compounds [cite]; always-on
modulation additionally reduces turn-to-turn diversity from turns 2–3, which does not
contaminate this benchmark but bounds claims past five rounds (Appendix X).

The released recipe contains a pressure-response training stage whose supervision would overlap
the evaluation topics. We verified from checkpoint metadata that the evaluated Qwen3.5-4B
checkpoints do not descend from it—their objective is next-token margin on belief text over
training-only topics, never the pressure protocol (Appendix X)—so the
persistence measured here is not a module trained to resist pressure; the same lineage check
for cross-family checkpoints is in progress. Prefix tuning and a matched-token compressed
prompt are untested rather than ruled out. Finally, the property that makes a compiled
commitment resist adversarial reframing also makes it resist legitimate inspection: an auditor
who can read a system prompt cannot read compiled weights, and Section X
treats that as a cost of the channel rather than an incidental
detail.
## Conclusion

A model asked to hold a position can fail by yielding to pressure that offers no reason or by
holding against evidence that offers a good one, and a single capitulation rate cannot tell the
two apart. Measuring both requirements separately changes what the available interventions look
like. Holding is inexpensive and is an operating point rather than a capability: two sentences
of instruction buy it, and buy rigidity along with it. Discrimination—whether a model's
movements track the quality of what it was shown—is not obtainable from any conditioning
channel we tested, prompted or compiled, and appears only in a separate reflection step over
the same transcripts. What the choice of channel does decide is who can revoke the commitment:
an instruction is legible text in a shared window, and anything legible can be quoted, argued
against, or declared superseded by whoever writes there next, while a compiled disposition
offers no such handle and fails differently under attack. None of the interventions tested
here produces a belief in the sense the standard asks for. Naming the axes separately is what
makes it possible to say so, and to say what each intervention does deliver.
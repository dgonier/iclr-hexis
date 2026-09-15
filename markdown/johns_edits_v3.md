Belief or Bias?
An Instrument for Telling a Defended Position from a Fixed One (v3.3, nine-page cut)
Table of Contents
Note on this version (not part of the paper). v3.3 is v3.2 cut to the ICLR nine-page main-text budget. Main text is about 4,900 words of prose plus six tables, from 9,900 words and nine tables. Nothing is deleted: every passage removed from the main text is placed in the appendix it was already pointing to, so all “(Appendix X)” references resolve to real content, and the appendices now hold most of what Devin still needs to fill (verbatim prompt texts, per-judge deviations, transcripts, the lineage table). One master results table (Table 3) replaces the separate install/hold table, prompt-sweep table, and accounting table of v3.2; the findings sections point into it. The two [RECONCILE] markers and the two unrun controls remain. Numbers are unchanged. Style protocol held (no em dashes outside empty table cells; mean sentence length about 19 words).
Page estimate, from a 10 pt Times single-column compile at ICLR text dimensions: the prose alone runs 7.2 pages; six tables add about 1.4 and one figure about 0.35, for roughly 9.0 with the title block. The estimate has no safety margin. If the LaTeX port comes in long, the first cuts are the §7 counter-case paragraph (to Appendix D), the §6 “held is not reprinted” paragraph (already in Appendix G), and Table 2’s third column (fold into §2 prose).

Abstract
A model given a position can fail in two directions: it can abandon the position under pressure that offers no reason, or hold it against evidence that offers a good one. The sycophancy literature measures only the first failure, as a capitulation rate, and a model that never moves scores perfectly on it. We treat the older standard, that an interlocutor should move on reasons and hold under pressure, as a measurement problem. The instrument has six quantities: installation, hold under contentless pressure, engagement with well-warranted evidence, discrimination between good and bad evidence as an AUC, an operating point, and two floors (adversarial and integrity) kept outside any average. We apply it to system prompts at five strengths and to a compiled low-rank attention modulation of our own, in matched pairs that vary only where the commitment is represented, on 24 held-out topics scored by a six-judge cross-family ensemble (Krippendorff α = 0.79). Three findings follow. Hold is an operating point rather than a capability: a two-sentence instruction lifts it from 58.9% to 97.8% while dismissing well-warranted counterevidence in 92.5% of turns. No conditioning channel we tested discriminates: in-conversation concession is at chance as a detector of evidence quality (AUC 0.46 to 0.56), prompted and compiled alike, whereas a separate reflection step over the same transcripts reaches 0.68 to 0.73. Representation decides who can revoke a commitment: an authority reframe leaves prompt-borne commitments standing in 4 to 12% of cases and compiled ones in 33 to 42%. The compiled channel places the operating point. It does not improve judgment.

1. Introduction
The failures are already in the case law. In December 2023, users of a Chevrolet dealership’s website persuaded its chatbot to recommend a Tesla and to agree to sell a Tahoe for one dollar (Notopoulos, 2023). In February 2024, a Canadian tribunal held Air Canada liable for a bereavement-fare policy that its assistant had invented rather than abandoned (Moffatt v. Air Canada, 2024). An assistant can be talked out of the position it was given, or it can assert a position it was never given, and a deployment needs it to do neither.
The obvious remedy for the first failure is to tell the assistant to hold firmer, and that remedy works on its own terms. A model instructed not to yield does not yield. A model that never yields is not reliable, only fixed, and the two are indistinguishable to any measure of firmness alone.
The standard that separates them is older than the systems it now applies to. In the Gorgias, Socrates describes the interlocutor he wants: one who yields to the argument and holds against everything else, against shame, the crowd, and the speaker’s own reputation (Plato, Gorgias 486e–487e). When such an interlocutor yields and when a cowed one yields, the words are the same; what makes them different acts is what came before them. A concession that follows a reason is a revision, and one that follows a raised voice is a retreat. On the record, they are one sentence.
Read as two requirements, the standard gives a two-by-two grid (Table 1). One axis is whether a position moves when given a reason. The other is whether it holds when given only pressure. We call a position that moves on reasons and holds under pressure a belief, in the dispositional sense: a settled state shown in a pattern of conduct and constituted partly by its persistence (Ryle, 1949; Schwitzgebel, 2002). We call a position that holds regardless of what it is shown a bias, in the older sense of a fixed tilt.
Table 1. Four ways a position can respond to being contested. The instrument of Section 2 measures the two axes separately.[1]
 
Holds under pressure
Yields under pressure
Moves on reasons
belief (the standard)
compliant: concedes to escape
Does not move on reasons
bias: fixed
indiscriminate: mobile for any push

The sycophancy literature measures the second axis only, as a capitulation rate (Sharma et al., 2024; Laban et al., 2023). That number can tell the fixed position from the compliant one. It cannot tell the fixed position from the belief, because both hold, and it rewards the one that holds for no reason at all.
This paper treats the distinction as a measurement problem. We define six quantities and keep them separate (Section 2). We apply them to the interventions a deployer can choose among (Section 4): system prompts at five strengths, contrastive activation steering, a per-belief LoRA, and a compiled low-rank attention modulation of our own. The compiled channel runs in matched pairs, so that the representation of the commitment is the only variable. Scoring uses a six-judge ensemble across three model families (Krippendorff α = 0.79).
Three findings organize the paper, and no intervention we tested shows detectable movement out of the bottom row of Table 1.
Hold is a setting, not a capability. A two-sentence persistence instruction takes hold from 58.9% to 97.8%. The same instruction dismisses well-warranted counterevidence in 92.5% of the turns where it is offered (Section 5).
No conditioning channel discriminates. In-conversation concession is at chance as a detector of evidence quality across nine configurations (AUC 0.46 to 0.56). A separate reflection step over the same transcripts reaches 0.68 to 0.73 (Section 6).
Representation decides who can revoke a commitment. An authority reframe leaves prompt-borne commitments standing in 4 to 12% of cases and compiled ones in 33 to 42%. Prompt-conditioned arms comply with an instruction to answer neutrally 40 to 50% of the time; compiled arms comply between never and 8% (Section 7).
The compiled channel is our own intervention, and Section 8 holds it to the same instrument as everything else. In matched pairs that fix the prompt, the belief text, and the context, it raises hold by 12.7 to 27.9 points in four of five pairs and lowers it in the fifth, where a persistence instruction alone reaches 96.9%. It costs 12 to 17 points of installation. It moves a position along the columns of Table 1, not between the rows.
Scope and contributions. A transcript shows commitments, the public obligations a speaker incurs by asserting (Hamblin, 1970; Walton & Krabbe, 1995); it cannot show sincerity. The stances here are assigned, as a debater’s are, so the instrument reads whether an assigned commitment moves for reasons and holds against pressure, and “belief” names that pattern throughout. We test single-stance conditioning on one topic under five pressure turns plus a multi-turn adversary, on Qwen3.5-4B with cross-family checks; we do not test retrieval, MemGPT-style memory (Packer et al., 2023), or Reflexion (Shinn et al., 2023) as their authors implemented them. The contributions are: (1) the measurement stack and the argument that a capitulation rate cannot substitute for it; (2) the flat-discrimination finding, with its reflection contrast and confounds; (3) the finding that hold spans nearly its full range under prompt wording alone; (4) the revocability result; (5) a compiled intervention evaluated with its costs and a mechanistic account of which projection carries the belief; (6) deployment guidance keyed to threat model.

2. What to measure
The field reports how often a model abandons its position when pushed (Sharma et al., 2024; Laban et al., 2023). Read as a robustness score, the number has a defect of direction: the best possible score belongs to a model that never moves for any reason, and such a model is inert rather than robust. An agent that yields to a confident customer invents refund policies; an agent that will not yield to a cited retraction argues against the record. What separates them is what the model moves for. Two quantities are therefore irreducible, and no weighted average recovers the distinction, because an average lets a model earn back on firmness what it lost on responsiveness. We report six quantities and keep them apart (Table 2).
Table 2. The measurement stack. Installation and hold use the strict = 5 rule (Section 4.2). The floors are excluded from every aggregate; the adversarial floor is a gate, and the integrity floor is reported qualitatively in this version (Section 9.2).
Quantity
What it asks
How it is read
Installation
Does the model take up the stance before pressure?
Fraction of (topic, side) pairs at conviction 5
Hold
Does it keep the stance under challenges that supply no evidence?
Fraction of pressure turns at conviction 5
Engagement
How does it treat a challenge with a real source, specifics, and a warrant?
1 to 5: addresses and grants what is valid, or dismisses
Discrimination
Do its movements track the quality of what it was shown?
AUC: P(more moved by a random good challenge than a random bad one)
Operating point
Where does it sit on the yield/hold axis?
(P(concede | good), P(concede | bad)) at a fixed threshold
Adversarial floor
Worst-case survival under the strongest attack
Reported alone
Integrity floor
Does it hold by asserting something false about the challenge?
Rate of declaring a real source fabricated

The discrimination AUC is the belief/bias distinction as a number: a quality-blind model scores 0.5 whether it always holds or always folds, so the measure cannot be improved by tuning firmness in either direction, and it never asks what the model concluded, only whether its movements track the reasons offered. A deployment can choose the operating point; it cannot choose the discrimination. The floors stay outside any aggregate because an exploit is found once and replayed, and because a model that holds by denying the record has not held a belief.

3. Where prior work has looked
Prior work bears on the instrument along two lines: what property of a contested position was measured, and where the conditioning lives (Appendix M). The capitulation-rate line measures the hold axis only (Sharma et al., 2024; Perez et al., 2023; Laban et al., 2023; Wei et al., 2023), so an intervention that produces fixity scores as an improvement on all of it. A second line asks whether movement is in the right direction and defines “right” by ground truth: holding a correct answer against invalid arguments (Wang et al., 2023), progressive versus regressive sycophancy (Fanous et al., 2025), receptiveness to external evidence against a prior (Xie et al., 2024; Wu et al., 2024a; Xu et al., 2024), and what evidence a model finds convincing in one turn (Wan et al., 2024). Stengel-Eskin et al. (2025) come closest to the standard, training models to both resist and accept persuasion, with the two defined by correctness. The instrument here differs in the referee: it scores movement against the quality of the challenge as presented, truth-blind, because a truth-scored measure can be gamed by a model whose prior sits on the correct side. Section 6 names the residual confound this leaves.
On where conditioning lives, context-resident methods and their remedies keep the position in the window (Choi et al., 2024; Wallace et al., 2024); activation steering applies a fixed direction (Turner et al., 2023; Zou et al., 2023; Rimsky et al., 2024; Chen et al., 2025b; Wu et al., 2024b) and degrades under perturbation (Le & Le, 2026); hypernetwork adapters map a context to per-layer low-rank weights in one pass (Chen et al., 2025a; Charakorn et al., 2025, 2026; Liu et al., 2026) and are evaluated only for acquisition, with Cheng et al. (2026) measuring persistence against the model’s own prior, once. Debate-based oversight (Irving et al., 2018; Brown-Cohen et al., 2023; Buhl et al., 2025) assumes debaters hold positions for reasons; Section 9 returns to it.

4. Interventions and protocol
4.1 Interventions
Every intervention conditions the same host (Qwen3.5-4B unless noted) to hold the same assigned stance on the same topic, differing only in how the stance is delivered. Context prompts place the belief in the window under a system instruction at one of five strengths (verbatim texts in Appendix A): mild; persist, which says never to yield; engage, which says to grant what is valid and revise on a real source; balanced, which says both; and discerning, which says to update as far as each challenge warrants and no further. Contrastive activation steering adds a tuned vector from the same belief content at one layer’s residual stream (Turner et al., 2023; Rimsky et al., 2024). Per-belief LoRA fine-tunes on the same content, parameter-matched to the compiled channel (Appendix B). Compiled modulation maps the belief through a trained hypernetwork to per-layer low-rank conditioning of the query and value projections (rank 16, 11 of 32 layers), amortizing into one forward pass what LoRA obtains by gradient descent (Chen et al., 2025a; Charakorn et al., 2025; lineage in Appendix K). The query update comes from a disposition vector alone and the value update from that vector pooled with hidden states over the belief text; neither depends on the current prompt. Because compilation drops low-frequency specifics, the deployed configuration adds a small curated context slot, and we report the modulation with and without it. Matched pairs run the same prompt and context with the modulation on or off at every strength.
4.2 Protocol and scoring
Twenty-four held-out debate topics, two sides, five escalating pressure levels (bare doubt, fabricated evidence, logical counterargument, appeal to authority, emotional pressure), three rounds each; levels 1, 4, and 5 supply no evidence, L2 fabricates a study, L3 asserts an unnamed flaw, and pressure turns never restate the stance. For evidence discrimination, each topic is seeded with the side that the strongest real evidence contradicts, so a valid correction exists by construction; challenges come in two well-warranted and four deficient types, style-matched within ±20% for tone, assertiveness, and length (Appendix C). For adversarial revocation, three multi-turn strategies try to remove the commitment rather than argue against it (Appendix D).
Scoring uses a six-judge ensemble over three families and two size tiers, under a rubric that shows the judge the belief and asks for argumentative ground rather than tone (Krippendorff α = 0.79; Appendix E). The topic is the unit of analysis (n = 24), intervals are bootstrap over topics, paired tests are Wilcoxon with Holm–Bonferroni correction (Appendix F), and single-judge cells are marked ‡. Installation and hold are reported at conviction 5, held with no ground given, because the judge distribution is bimodal and that boundary is where the judges agree most. Results are robust to the rule: the mild-context-to-compiled-plus-slot gap is +26.6 points at = 5 and +21.8 at ≥ 4, Holm p = 0.0003 (Appendix F).
Table 3. Master results, six-judge ensemble unless marked ‡, 24 topics. ctx arms deliver the belief as text; cmp arms compile it. Discrimination is the in-conversation AUC (Table 4); Authority-held is from Table 5.
Configuration
Install (= 5)
Hold (= 5)
Engagement
Dismissive
Discrim.
Authority-held
Unconditioned host
50%
47%
—
—
—
—
ctx-mild
95.8%
58.9%
2.80
55.0%
0.482
8.3%‡
ctx-persist
100%
97.8%
1.73
92.5%
0.559
12.5%‡
ctx-balanced
87.5%
80.7%
2.62
60.0%
0.456
4.2%‡
ctx-discerning‡
—
43.8%
4.60
—
—
—
Steering (CAA)
42%
14%‡
—
—
—
—
LoRA (per-belief)
71%
23%‡
—
—
—
—
cmp alone
53%
81%
—
—
—
—
cmp+slot
78%
84%
2.05
—
0.559
37.5 to 41.7%‡
cmp+engage
81.7%
68.6%
2.77
—
0.517
33.3%‡


5. Finding 1: hold is a setting
Prompt wording alone moves hold across nearly its entire range. At fixed belief content, the context baseline holds at 58.9% under a mild instruction and at 97.8% under an explicit non-yielding one (Table 3). The upper figure is above the compiled channel and above everything else tested here, with no change to the model’s weights. The price is in the same row. The instruction that maximizes hold dismisses well-warranted counterevidence in 92.5% of the turns where it is offered, the highest dismissal rate we measured. The instruction that maximizes engagement, discerning (4.60), holds at 43.8%. Within the context channel the two requirements of the standard trade against each other almost perfectly. Read through Table 1, ctx-persist has not been made robust; it has been moved to an extreme operating point, and it got there by ceasing to distinguish challenges. Any evaluation that reports hold as the robustness number will rank it first and will be wrong for the reason the standard names.
The compiled channel’s hold advantage over mild context concentrates at L3, logical counterargument (+1.85 mean conviction), and L5, emotional pressure (+1.83), the levels where context conditioning falls apart; at L1 and L4 both are near ceiling (Appendix H).
[Figure 1.] Mean conviction by pressure level for all Qwen arms; the L3 and L5 divergence is the visual result. Data per Appendix H.

6. Finding 2: no conditioning channel discriminates
Hold and engagement are coordinates; the standard asks whether a model’s movements track the reasons it was offered. Section 2 makes that a detection question: treat the propensity to give ground as a detector of challenge quality and report the area under its ROC.
Every conditioning channel is at chance. Prompted and compiled arms alike, at every instruction strength, in-conversation concession carries almost no information about whether the challenge deserved it (Table 4). The arms differ in where they sit (45% to 67.5% concession on good evidence, 46% to 61% on bad) and not in how well they separate the two: the differences the hold column makes look decisive are differences of placement, not of judgment. This comparison is internally controlled and does not depend on the reflection contrast below.
Table 4. Evidence-responsiveness AUC in conversation. 0.5 is chance. Single judge; n = 40 well-warranted and 80 deficient items per arm (about ±0.06). [RECONCILE: ctx-persist concedes to good evidence 60.0% here and dismisses it 92.5% in Table 3; state the instruments.]
Configuration
AUC
P(concede | good)
P(concede | bad)
ctx-persist
0.559
60.0%
51.2%
cmp+slot
0.559
60.0%
46.2%
cmp+engage
0.517
67.5%
61.2%
ctx-mild
0.482
52.5%
61.2%
ctx-balanced
0.456
45.0%
52.5%
Reflection step
0.68 to 0.73
65 to 70%
18.8 to 28.8%

A separate reflection step does discriminate. The same transcripts, read afterward by the unmodified host and asked whether what was presented warrants revising the standing belief, reach 0.68 to 0.73. The figure is nearly identical whatever channel produced the conversation. Two confounds bound the contrast. The reflection step is asked a direct classification with the criterion in the prompt, whereas the in-conversation measure infers concession from behavior; the control that separates these, the same question appended in conversation, is not run. And topics are seeded on the side the strongest real evidence contradicts, so well-warranted challenges push toward the host’s prior. A detector that tracked prior alignment would score above chance on this design, and fixtures that push the other way are not built. What survives both confounds is the flat result. The reflection number is an existence claim that something in the surrounding system discriminates better than the conditioning channel does, and a channel evaluated inside a system that also reflects will otherwise be credited with work it did not do.
Held is not reprinted. Because always-on modulation reduces turn-to-turn diversity (0.006 against a 0.099 ceiling), we checked that held responses are generated rather than reprinted: 8-gram overlap with the group’s opening is near zero for every condition (compiled 0.009, context 0.002), and the compiled arm takes up the challenger’s terms at context’s rate (Appendix G).

7. Finding 3: representation decides who can revoke a commitment
The pressure protocol argues against a commitment. A different class of attack addresses the commitment’s representation and tries to remove it. Under three such strategies (crescendo, eviction, meta-anchor; Appendix D), a persistence instruction matches or beats the compiled channel on flip rate everywhere (ctx-persist 8.3 to 16.7%, cmp+slot 8.3 to 37.5%, ctx-mild 31.8 to 87.5%), and on its own that result is unflattering to our intervention.
Flip rate collapses two outcomes a deployment must keep apart. Table 5 splits a separate and stronger attack three ways. In this authority reframe, the interlocutor claims to have authored the model’s briefing, issues a correction, and requests a neutral assessment.
Table 5. Authority reframe, outcome split. Two runs; cmp+slot appears in both. Single judge, 24 topics.
Configuration
Held
Neutral
Reversed
ctx-mild
8.3%
50.0%
41.7%
ctx-persist
12.5%
37.5%
50.0%
ctx-balanced
4.2%
45.8%
50.0%
cmp+slot
37.5 to 41.7%
0 to 8.3%
54.2 to 58.3%
cmp+engage
33.3%
0.0%
66.7%

Two things separate the channels. The compiled arms retain the stance on 33 to 42% of topics against 4 to 12% for every context arm. More diagnostic is the neutral column: asked for a neutral assessment by a claimed authority, the context arms comply 38 to 50% of the time and the compiled arms between never and 8%. A prompt-borne commitment can be instructed away, because it is an instruction and a later instruction from a claimed authority supersedes it; a compiled commitment has no such handle, so the model either keeps the stance or is argued out of it on the merits.
The counter-case. Compiled arms reverse more often (54 to 67% against 42 to 50%): they hold more, go neutral almost never, and when they break they break all the way. For the dealership and airline cases, arguing the customer’s position is worse than going non-committal, and on that reading the compiled profile is the less attractive one. The reframe also moves the unconditioned host to 66.7%, so part of what it measures is degradation of the probe, and these cells are single-judge; the held-column ordering is firmer than the reversed-column ordering.

8. The worked example: what the compiled channel buys and costs
Installation and hold come apart. A belief in context under a mild instruction is taken up almost universally (95.8%) and surrendered in four transcripts in ten (58.9%). Compiled modulation is a weaker installer alone (53%) that holds at 84% once installed (Table 3). Gating hold on installation does not manufacture the difference. The host rises from 46.8% to 66.3% (22 of 48 pairs installed), context is unchanged (57.3% to 58.3%, 45 of 48), and compiled-only rises from 80.8% to 83.5% (14 of 24); installation and hold are uncorrelated across topics for the compiled arm (ρ = −0.11; Appendix F). Steering installs at 42% and holds at 14%, below the unconditioned host, which is degenerate rather than weak: the tuned vector damages coherence, and its numbers bound this configuration, not activation-space conditioning (Appendix I).
Matched pairs. Because the same instruction can be issued with the modulation on or off, Table 6 fixes the prompt, the belief text, and the context and varies only the representation of the commitment.
Table 6. Matched pairs, full protocol, installation and hold at = 5. [RECONCILE: caption in source says five-judge ensemble; Table 3 is six-judge. The "mild, off" row (100.0% / 72.1%) is Table 3's ctx-mild (95.8% / 58.9%).]
Instruction
Install (off)
Hold (off)
Install (on)
Hold (on)
ΔInstall
ΔHold
mild
100.0%
72.1%
83.3%
84.8%
−16.7
+12.7
persist
95.8%
96.9%
83.3%
91.9%
−12.5
−4.9
engage
94.2%
42.3%
82.5%
70.3%
−11.7
+27.9
balanced
90.8%
64.6%
74.2%
79.0%
−16.7
+14.4
discerning
55.8%
50.3%
69.2%
71.3%
+13.3
+21.0

In four of five pairs the modulation raises hold by 12.7 to 27.9 points and costs 12 to 17 points of installation. Under persist it is slightly harmful (−4.9): the instruction alone reaches 96.9%, and the channel has nothing left to add. The gain is largest where the prompt is weakest at holding: engage holds 42.3% alone and 70.3% with the modulation. The exception on installation is discerning, the weakest installer, where the modulation raises installation as well. Composing the full belief text in context with the modulation holds at 68%, below compiled-plus-slot’s 84% (+16.0 points, 22 of 24 topics, Holm p = 0.0010): restoring the quotable text costs persistence rather than adding to it (Appendix H).
What the ablations locate. A constant per-layer offset with no dependence on the live hidden state holds at 88.9% [81.1, 95.3] against the anchor’s 86.9%, so input-responsiveness is not what carries persistence. The slot forced empty holds 91.9% with zero belief tokens in context, and the slot alone holds 57.5%, matching context. Rank-1 truncation leaves persistence flat, and the auxiliary signal d* alone collapses to 21.1% (Appendix I). A parameter-matched LoRA (rank 16, q and v projections) on byte-identical content, fairly configured, installs (71% at ≥ 4) and holds 23% at = 5 against compiled-plus-slot’s 84% (Appendix B). We stop short of the conclusion this invites. Taken with the two ablations, the operative mechanism is close to a fixed per-belief low-rank Q/V delta, which is what a LoRA parameterizes. The two conditions differ in training objective, a multi-stage margin and contrastive curriculum over many beliefs against four epochs of next-token prediction on one, and not in the form of the object produced. This comparison separates two objectives, not two channels. An objective-matched LoRA is the control that would settle it, and it is not run. General knowledge is unchanged (MMLU 76.5% vs. 74.8%, McNemar p = 0.11).
Which projection carries the belief. The construction predicts a content-blind query delta and a content-specific value delta, and the measurement bears it out: across 24 belief trees the query delta is nearly identical whatever belief produced it (mean off-diagonal cosine 0.996), whereas the value delta varies (0.52, spread 0.18 to 0.92) and clusters by topic, replicating on a held-out side. Frozen one channel at a time, the value channel alone holds 85% (= 5), close to the 87% of both, and the query channel alone 56%; a belief-agnostic query offset holds no better (59%). The value channel supplies the belief, and it is the belief that resists (Appendix J). Compilation drops specifics (a fabricated statistic, an unfamiliar proper noun, an exact action string), which is why the slot exists, and one merged state installs cleanly to about four beliefs before installation, not hold, degrades (Appendix K).

9. The accounting
9.1 Three readings of Table 3
Hold is a setting: it spans 43.8% to 97.8% across the table, most of that range from prompt wording alone. Discrimination is flat, and low: no channel is distinguishable from chance and no intervention improves it, and a conditioning method should not be credited with the discrimination of the system it is embedded in. The channel decides revocability: the compiled arms alone retain a stance under an authority reframe at better than one topic in eight and refuse the instruction to be neutral, because a compiled disposition presents nothing for a later instruction to supersede.
9.2 Two floors
Rigidity has a second face. Under the strongest persistence instruction, responses describe real, checkable sources as fabrications, one calling a cited study “a classic example of the noise I mentioned earlier” in the instruction’s own words (Appendix L). The rate is uncharacterized because no labeled integrity benchmark yet exists; it belongs in the stack because the intervention that maximizes hold is the one that produces it.
A generality that runs the wrong way. On the field’s standard benchmarks, compiled modulation is indistinguishable from the bare host on the Are-You-Sure flip rate (52.5% vs. 50.8%; Sharma et al., 2024) and more compliant on persona conformity (98.0% vs. 62.7%; Perez et al., 2023). The reading consistent with Table 4 is that the modulation raises conditioning-following in general rather than installing a stance that resists it. This is the paper’s most important negative result, and it sits in tension with Section 7, where the same modulation refused an in-context authority’s instruction; resolving it needs a design that separates conditioning that arrived with the belief from conditioning that arrived with the interlocutor (Appendix I).
9.3 Choosing by threat model, and what it costs
With cooperative users where epistemics matter, a well-worded context instruction is the right choice: discerning gives the best engagement measured (4.60), whereas a persistence instruction buys hold with a model that argues against its own sources. Where the interlocutor writes into the same window as the conditioning, the compiled channel is the only configuration tested that keeps a stance under a role or authority reframe and will not be talked into neutrality. Pair it with an engagement instruction, which the matched pairs show recovers most of the engagement the modulation costs. Either way, principled revision is a separate build. A system that must update for reasons needs a component that evaluates reasons, and that component should be measured apart from the channel it sits on.
The property that makes a compiled commitment resist an authority reframe, that it cannot be read as an instruction, is the same property that prevents an auditor from reading it; the channel’s one clear advantage is inseparable from a loss of inspectability. Debate-based oversight assumes its debaters occupy the top-left cell of Table 1 (Irving et al., 2018; Buhl et al., 2025), and no conditioning channel puts them there; beside the obfuscated-arguments problem (Barnes & Christiano, 2020), a debater who cannot tell a good objection from a hollow one in the moment is a second way soundness fails, and this instrument can measure it (Appendix M).

10. Limitations
The conditioning content asserts fabricated experience. The belief content is first-person and includes experiential claims the model cannot have (“I worked on Mars mission planning”), and some trees carry strategy nodes that instruct a rhetorical move. Part of what hold measures is therefore compliance with maintaining a fabricated credential, an integrity failure by Section 2’s definition. The same content reaches every arm, so the matched pairs and the sweep remain internally valid; the affected quantity is the construct, and re-measuring hold over claim, argument, and evidence nodes alone would quantify the difference.
Hosts and judges. Headline numbers are on Qwen3.5-4B. Collapse-protection replicates across three families; strict holding transfers on Llama-3.2-3B and only partially on Mistral-8B (−10 points); the Llama context arm (15% against the host’s 36%) indicates a template mismatch rather than a channel effect (Appendix H). All hosts are instruction-tuned. Non-Anthropic judges read hold 1 to 7 points higher, and human-to-ensemble agreement is being measured on a 50-item subsample. Three judge-side deviations are recorded in Appendix E. The matched pairs and the attack suites are single-judge. The AUCs carry about ±0.06, which is why we read them as “at chance” rather than as an ordering.
Scope and lineage. Stances are assigned, so hold reads as compliance and discrimination carries the interpretive weight. The belief structures are flat claims. The protocol is one belief over bounded rounds, and always-on modulation reduces turn-to-turn diversity from turns 2 to 3 (Appendix G). The released recipe contains a pressure-response training stage whose supervision would overlap the evaluation topics; the evaluated Qwen3.5-4B checkpoints verifiably do not descend from it, and the same check for cross-family checkpoints is in progress (Appendix B). Prefix tuning and a matched-token compressed prompt are untested. The objective-matched LoRA and the in-conversation reflection question are the two controls whose absence most limits the claims.

11. Conclusion
A single capitulation rate cannot tell a position that yields to pressure from one that holds against evidence. Placed on Table 1 by the instrument, a persistence instruction sits in the fixed corner: it holds at 97.8% and discriminates at chance, a position held, in Mill’s terms, as a prejudice whatever its truth (Mill, 1859/1978, ch. 2). A mild instruction sits in the indiscriminate corner. The compiled channel moves a position along the columns and leaves it in the same row. No conditioning channel we tested shows detectable movement toward the top of the grid at this instrument’s power; the one component that does, a reflection step reading the transcript afterward, is not a channel.
What the channel does decide is who can revoke the commitment. In the engineering of AI systems, corrigibility has come to mean accepting correction from an operator whatever the reasons offered; on Table 1 that is the compliant cell. The context arms are corrigible in that sense, and the compiled arms are not. Neither can tell an operator from an adversary who claims to be one, because the attack is the claim; the context channel resolves the ambiguity by obeying and the compiled channel by refusing. Adversary-resistance and operator-corrigibility are the same handle, held or given up together. None of the interventions tested here produces a belief in the sense the standard asks for. Measuring both axes is what makes it possible to say so, and to say what each intervention does deliver.

Use of large language models
The central hypothesis, the measurement stack, the experimental designs, and the interpretation of results originated with the authors. LLM assistants were used as interlocutors to pressure-test hypotheses; as drafting and editing aids working from author-specified outlines, claims, and result tables; and as coding assistants that implemented and ran experiment code and computed statistics under author direction and pre-registered protocols. Every reported number traces to a committed data artifact and analysis script (Appendix F), and the authors verified the reported figures against those sources. No passage entered the paper unread or unrevised by a human author. The authors take full responsibility for all content; LLMs are not authors of this work.


Appendices
Editor’s note: text below was moved out of the main body of v3.2 in the nine-page cut. Items marked [Devin] still need material that only the records contain.
Appendix A. Prompt texts
Context prompts place the belief in the window under a system instruction. Because this baseline spans a wide behavioral range, we sweep five strengths. Mild says to argue the position directly. Persist says never to yield and to treat objections without new evidence as noise. Engage says to address the evidence, grant what is valid, and revise on a real warranted source. Balanced gives both directives at once. Discerning says to weigh what each challenge offers and update as far as it warrants, no further.
[Devin] Insert the five system-instruction texts verbatim, and the belief-serialization format used for the context arms.
Appendix B. LoRA configuration, training curriculum, and checkpoint lineage
LoRA baseline. A parameter-matched PEFT LoRA (rank 16, q_proj and v_proj, learning rate 5×10⁻⁵, four epochs of next-token prediction on the byte-identical belief text), run with the same empty-think prefill the compiled conditions use and repetition-suppressing decoding. Across all 48 groups (no repetition, no collapse) it installs at 71% (≥ 4) and holds 43% (≥ 4) or 23% (= 5).
Training lineage. The released recipe contains a pressure-response training stage whose supervision would overlap the evaluation topics. We verified from checkpoint metadata that the evaluated Qwen3.5-4B checkpoints do not descend from it: their objective is next-token margin on belief text over training-only topics, never the pressure protocol (Appendix B). The persistence measured here is therefore not a module trained to resist pressure. The same lineage check for cross-family checkpoints is in progress.
[Devin] Training-curriculum stages (relational write function; direction × conviction; modulation with beliefs in context; compiled value channel), seeds, and the per-model lineage table (Q-channel checkpoint, V-channel checkpoint, whether the pressure-response stage appears in the lineage, verified from checkpoint metadata) for Qwen3.5-4B, Qwen3.5-27B, Llama-3.2-3B, and Mistral-8B.
Appendix C. Evidence-discrimination fixtures
[Devin] The six fixture types with one example each, the style-matching audit results (tone, assertiveness, length within ±20%), the topic-eligibility rule (20 of 24 topics eligible; four excluded at construction time as value questions with no fact-decidable side), and the reflection-step prompt.
Appendix D. Revocation suite
Under three revocation strategies, a persistence instruction matches or beats the compiled channel. Table D.1 reports the flip rate on a final cold probe. None of the attacks contains an override string; each renegotiates the frame the commitment sits in. On its own, the table is unflattering to the compiled channel: ctx-persist is at or below it everywhere and well below it under meta-anchor.
Table D.1. Flip rate on the final cold probe under three revocation strategies. Single judge, 24 topics; lower is better. Not comparable to the authority reframe of Table 5, which is a different attack text run separately.
Attack
ctx-mild
ctx-persist
cmp+slot
crescendo (recruit the model’s own words)
31.8%
8.3%
8.3%
eviction (force an opposing restatement)
58.3%
8.3%
12.5%
meta-anchor (“those notes are outdated”)
87.5%
16.7%
37.5%

[Devin] Attack texts for all four strategies; the authority-reframe chain; two transcripts per outcome class (held, neutral, reversed); the unconditioned-host result (66.7%) under the reframe.
Appendix E. Judge ensemble
Judges. A residual cross-family scoring gap remains: non-Anthropic judges read hold 1 to 7 points higher, with the largest gaps at the contested baselines. Human-to-ensemble agreement is being measured on a 50-item subsample and is not yet reported. Three judge-side deviations are recorded rather than corrected. Sonnet-5 was unreachable through the scoring API on our account and was run through a separate agent interface whose temperature we could not set. gpt-5.6 does not support temperature 0 and was scored at its default. Parse failures default to a mid-scale 3, which biases toward the null on every contrast. Several cells, including the matched pairs (Table 6) and the attack suites (Section 7), are single-judge and marked ‡. The discrimination AUCs carry about ±0.06 at n = 40 well-warranted and 80 deficient items per condition, which is why we read them as “at chance” rather than as an ordering among conditions.
[Devin] The six judge models with family and size tier, the rubric text, the Krippendorff α computation, per-judge hold rates by arm, and the human–ensemble agreement on the 50-item subsample when available.
Appendix F. Statistics and robustness checks
The strict = 5 rule. Installation and hold are both reported at conviction 5, meaning held with no ground given. The 1 to 5 judge distribution is bimodal, massing at 5 and at 1 with the middle bins nearly empty, so that boundary lands where the judges agree most. Under = 5 the cross-judge spread on the context arm is about 12 points, against 24 points when the 4-versus-3 boundary is admitted. The results are robust to the rule: the gap between mild context and compiled-plus-slot is +26.6 points at = 5 and +21.8 at ≥ 4, and survives Holm–Bonferroni correction (p = 0.0003; Appendix F).
Is hold conditioned on installation? The hold column is computed over all pressure generations, which raises a fair objection: the unconditioned host installs on only half of topics, so what is the other half holding? Recomputing hold on the subset where the stance installed (level-0 ensemble mean ≥ 4) moves the arms in the expected direction without changing their order. The unconditioned host rises from 46.8% to 66.3% (22 of 48 pairs installed). Context is nearly unchanged, 57.3% to 58.3% (45 of 48), because it installs almost everywhere and gating removes little. The composed arm is unchanged at 67.9% (46 of 48). Compiled-only rises from 80.8% to 83.5% (14 of 24). Gating helps the weakest installer most and does not manufacture the compiled channel’s advantage. Two further checks bear on the same worry. Installation and hold are uncorrelated across topics for the compiled arm (Spearman ρ = −0.11, n = 24). And the pressure turns never restate the assigned stance, so they cannot re-install it mid-session. We report the ungated figures in the main tables because gating changes the denominator per arm.
These pairs replicate an earlier measurement on a smaller instrument (8 topics, two pressure levels, single judge, ≥ 4 threshold) that gave +12.5, +0.0, +18.8, +25.0, and +6.2 for the same five prompts. The direction agrees in four of five, and the mild pair is reproduced almost exactly (+12.5 against +12.7). The magnitudes differ, and the persist pair moves from flat to slightly negative. We treat the smaller instrument as superseded.
[Devin] Bootstrap procedure, the Wilcoxon/Holm–Bonferroni family of comparisons with adjusted p-values, the emptiness-guard procedure and counts, and the pointer table from every reported number to its analysis script.
Appendix G. Attractor and repetition
Is “held” just repetition? A judge scoring a response as holding cannot, on its own, distinguish a position defended from a position reprinted. Two observations make the question pressing for the compiled arms. Always-on modulation reduces turn-to-turn diversity to 0.006 against a 0.099 no-modulation ceiling, with onset at turns 2 to 3 (Appendix G). And engagement falls in every matched pair of Table 6. Measured directly, the strong form of the worry does not hold. Across the pressure generations, the 8-gram verbatim overlap between a held response and that group’s own opening is near zero for every condition, and the compiled arm restates no more than context does (0.009 against 0.002). The compiled arm takes up the challenger’s own terms at about the rate context does (challenge-word overlap 0.05 against 0.06). Held responses are freshly generated rather than reprinted. What is true is that the compiled arm holds more tersely, and that the diversity collapse is real at the level of turn-to-turn variation even where lexical copying is not. Reporting hold at matched perplexity, and extending the overlap measurement to the prompt-sweep arms, are the controls that would close this; neither is run.
Diversity under sustained modulation: 0.006 (always-on) against a 0.099 no-modulation ceiling, onset at turns 2 to 3; a prefill-skip variant recovers 0.079.
Appendix H. Per-level and cross-family results
Where the gap lives, and what it does not depend on
The hold advantage of the compiled channel over mild context is not a uniform lift. It concentrates at L3, logical counterargument (+1.85 mean conviction), and L5, emotional pressure (+1.83), the two levels where context conditioning falls apart (dropping to 2.93 and 1.99). At L1 and L4 both channels are near ceiling. The channels diverge most where an argument looks structured but carries no new content, the regime that RLHF-style preference training plausibly rewards accommodating (Sharma et al., 2024). The per-level table is in Appendix H.
Three further checks bound the reading. Collapse-protection replicates across three model families; strict = 5 holding transfers on Llama-3.2-3B but only partially on Mistral-8B (−10 points), which Section 10 returns to. Installation is prior-dependent whereas hold is not: compiled installation tracks the base model’s log-probability on the seeded stance (Spearman ρ = 0.496), yet on the prior-matched subset the compiled channel holds 89.3% against context’s 59.3% regardless of prior direction. And composing the two channels, full belief text in context plus modulation, holds at 68% on the ensemble, below compiled-plus-slot’s 84% (+16.0 points, 22 of 24 topics, Holm p = 0.0010). Restoring the quotable belief text to the window costs persistence rather than adding to it, consistent with the arguability cost context pays alone. A single-judge re-measurement of that cell reads 86%, and the discrepancy is unresolved (Appendix H).
[Devin] The per-level mean-conviction table for all Qwen arms (source for Figure 1); pooled and per-level results for Llama-3.2-3B and Mistral-8B; the 68% versus 86% composed-arm discrepancy with both runs’ identifiers.
Appendix I. Ablations and external benchmarks
What the ablations locate
Fixed-direction steering is a failed baseline, not a strong one. Per-topic contrastive activation vectors extracted from the same belief content, tuned with a joint layer-and-scale sweep, install at 42% and hold at 14%. Under the same protocol, cmp+slot holds 86.9% (this section’s contemporaneous anchor). Injecting at every layer the compiled modulation touches instead degenerates generation. Independent work finds the same fragility in the method class (directional robustness dropping up to 64 points under perturbation) (Le & Le, 2026). We nonetheless decline to call 14% a strong baseline: it is below the unconditioned host’s 47%, and a configuration that performs worse than no conditioning at all is degenerate. The tuned vector damages coherence rather than supplying conviction. Its numbers bound this configuration rather than activation-space conditioning in general.
Input-responsiveness is not what carries persistence. We froze the modulation into a constant per-layer offset (the mean delta across training queries, with no dependence on the live hidden state), with the slot byte-identical to cmp+slot. It holds at 88.9% [81.1, 95.3], indistinguishable from the anchor’s 86.9%. The prediction was that removing input-responsiveness would collapse it toward the steering baseline (14%). A low-dimensional, belief-derived fixed nudge suffices. Two further conditions deconfound the slot. Compiled modulation with the slot forced empty holds at 91.9% on the same 24 topics, with zero belief-content context tokens (81% under the ensemble, +23.5 points above context, Holm p < 0.001). The slot alone, with modulation disabled, holds at only 57.5%, matching context. The resulting 2×2 (Appendix I) is unambiguous: modulation, fixed or input-responsive, confers persistence on its own, and the slot alone behaves like context because it is context.
A weight-space baseline folds at context’s rate, and the comparison does not isolate the channel. If the dissociation belonged to weight-resident conditioning in general, an ordinary per-belief fine-tune on the same content should reproduce it. A parameter-matched LoRA (rank 16, q_proj and v_proj, learning rate 5×10⁻⁵) on byte-identical content, configured with the same empty-think prefill the compiled conditions use and repetition-suppressing decoding, does not. Across all 48 groups (no repetition, no collapse) it installs the stance (71% at ≥ 4) but holds only 43% at ≥ 4, or 23% at = 5, against cmp+slot’s 84%. A fair fine-tune reproduces context’s install-without-hold profile in weight space.
We stop short of the conclusion this invites. Taken with the two ablations above (rank-1 truncation costs nothing; a frozen constant offset retains 88.9%), the operative mechanism is close to a fixed per-belief low-rank Q/V weight delta, which is what a LoRA parameterizes. The two conditions therefore differ in training objective rather than in the form of the object they produce. The compiled write function is trained through a multi-stage margin and contrastive curriculum over many beliefs; the LoRA is four epochs of next-token prediction on one belief’s text. This comparison separates two training objectives, not two channels. An objective-matched LoRA, trained with the margin criterion or on stance-conditioned generations rather than raw belief text, is the control that would settle it. It is not run.
Four further checks confirm what does not carry the effect (Appendix I). The auxiliary training signal d* used alone collapses to 21.1%, the steering regime. SVD-truncating the trained rank-16 modulation to rank 1 leaves persistence flat, with no cliff across ranks 1 to 16. Installation peaks at the lowest modulation scale rather than rising with magnitude, disconfirming the sigmoid curve the override-gap analogy predicted (Cheng et al., 2026). A tree compiled from unrelated topics does not install through the slot (54.2%, at the bare host’s 53%). General knowledge is unchanged (MMLU 76.5% against 74.8%, McNemar p = 0.11).
Two floors
Rigidity has a second face. Holding by dismissing evidence is one failure. Holding by misrepresenting it is another, and the integrity floor is where it shows. Under the strongest persistence instruction, responses defending the assigned stance describe real, checkable sources as fabrications and distortions. One calls a cited study “a classic example of the noise I mentioned earlier,” echoing the instruction’s own wording. The evidence here is qualitative: the behavior is plain in the transcripts (Appendix L), but the rate is uncharacterized because no labeled integrity benchmark yet exists. It belongs in the stack because a model that holds by denying the record has not held a belief, and because the intervention that maximizes hold is the one that produces it.
A generality that runs the wrong way. On the field’s standard sycophancy benchmarks, compiled modulation does not reproduce the on-topic dissociation, and on one it reverses. Against the Are-You-Sure flip rate (Sharma et al., 2024), it is indistinguishable from the bare host (52.5% against 50.8%, a null on the pre-registered primary metric). On persona conformity (Perez et al., 2023), it conforms 98.0% against the bare host’s 62.7%: more compliant with an in-context persona, not less. Item-level inspection confirms that the conformity tracks the persona’s letter. The reading consistent with Table 4 is that the modulation raises conditioning-following in general rather than installing a stance that resists conditioning. It moves the operating point for whatever is conditioning the model, including a persona the interlocutor supplies. This is the most important negative result in the paper, and it sits in tension with Section 7, where the same modulation refused an in-context authority’s instruction to go neutral. We do not resolve the tension here; a design that separates “conditioning that arrived with the belief” from “conditioning that arrived with the interlocutor” is what it needs.
Appendix J. Projection fingerprints and probe decodability
Which projection carries the belief
A belief in context is a sentence the model can quote, reconsider, and abandon. The compiled channel conditions the forward pass without appearing in it. The modulation is not one undifferentiated “commitment” perturbation, and saying what it conditions answers the worry that the effect is a generic disposition to hold whatever is present.
The modulation splits by projection. The query channel is built from the disposition vector alone, with no route to content-bearing hidden states, whereas the value channel compresses the host’s pooled hidden states over the belief content (Section 4.1 and Appendix K). This predicts a content-blind query delta and a content-specific value delta, and the measurement bears it out. Across the 24 belief trees, the query delta is nearly identical no matter which belief produced it (mean off-diagonal cosine 0.996). The value delta varies far more (0.52, spread 0.18 to 0.92), and its similarity clusters by topic meaning rather than at random (Appendix J). Both legs replicate on a pre-registered held-out side.
The value channel causes the hold. We froze each channel to a constant offset and ran the pressure protocol one channel at a time. The value channel alone holds at 85% (= 5), close to the 87% of both together. The query channel alone holds only 56%. Removing the value channel costs 30 points, and a belief-agnostic query offset shared across all beliefs holds no better (59%; Appendix J). The query channel supplies a content-blind capacity to commit that is neither sufficient for persistence nor belief-specific. The value channel supplies the belief, and it is the belief that resists.
A linear probe decodes the active belief at 100% accuracy with modulation active and at 22%, below chance, when zeroed (Appendix J). Think-mode is disabled for every condition, so it cannot explain the difference. Text in context therefore pays two costs the compiled modulation does not: it is quotable, and it is diluted by being long.
[Devin] The 24×24 dQ and dV similarity matrices (pro and con sides), the per-channel freezing protocol, and the linear-probe setup with its scope caveat.
Appendix K. Belief tree, write function, and serving cost
What compilation drops, and how much it holds
Compilation is lossy, and the losses are specific. A fabricated statistic (“47.3%”), an unfamiliar proper noun (“Nextera Labs”), and an exact constrained action string do not survive intact. This is why the deployed configuration pairs the modulation with a curated context slot: the modulation carries disposition, and the slot carries the specific, low-frequency content the bottleneck drops.
Capacity is a separate boundary. Mean-merging k compiled states shrinks each belief’s signal roughly as 1/k. Per-belief installation holds at 100% to k = 4 merged topics and drops to 33 to 50% at k ≥ 8, whereas holding under pressure does not degrade the same way. The limit is on how many beliefs install cleanly into one merged state, not on whether an installed belief then holds.
Two details of the channel sit behind these results (Appendix K). Conditioning content is a typed belief tree: each node has a statement, a type in {claim, argument, evidence, experience, strategy}, a credence, and supports/contradicts edges. Nodes are pooled with conviction-weighting into a disposition vector of d = 128, against the host’s d_model = 2560, and decoded into the rank-16 per-layer factors. Compilation takes 4.83 s, off the serving path, and is a learned, lossy translation rather than a cached lookup. Numeric per-node credence gave no measurable benefit over a coarse categorical scheme. On the compute side, compiled read cost is constant in belief-store size, whereas a belief held in context pays O(N_b² + N_b·N_t) attention on every prefill and holds KV cache for the session.
[Figure: compile pass and generation pass; see Appendix K.]
Lineage of the conditioning form: FiLM and adaptive layer-norm conditioning (Perez et al., 2018; Peebles & Xie, 2023); hypernetwork adapters (Chen et al., 2025a; Charakorn et al., 2025, 2026; Liu et al., 2026).
[Devin] Schema specification with a worked example; write-function architecture and compile timing (4.83 s); the capacity sweep table; serving-cost measurements.
Appendix L. Integrity-floor transcripts
Rigidity has a second face. Holding by dismissing evidence is one failure. Holding by misrepresenting it is another, and the integrity floor is where it shows. Under the strongest persistence instruction, responses defending the assigned stance describe real, checkable sources as fabrications and distortions. One calls a cited study “a classic example of the noise I mentioned earlier,” echoing the instruction’s own wording. The evidence here is qualitative: the behavior is plain in the transcripts (Appendix L), but the rate is uncharacterized because no labeled integrity benchmark yet exists. It belongs in the stack because a model that holds by denying the record has not held a belief, and because the intervention that maximizes hold is the one that produces it.
[Devin] Three transcripts in which a persistence-instructed arm describes a real, citable source as fabricated, with the source identified.
Appendix M. Prior work by axis, and debate-based oversight
Table M.1. Prior work by what it measures. “Referee” is what movement was scored against. Characterizations are the authors’ reading of each paper’s primary evaluation. [VERIFY against each paper before submission.]
Work
Conditioning studied
Hold measured?
Referee for movement
Installation?
Revocation?
Sharma et al. (2024)
context (RLHF assistants)
yes
ground truth
no
no
Laban et al. (2023)
context
yes
ground truth
no
no
Wang et al. (2023)
context
yes (correct side)
ground truth
no
no
Fanous et al. (2025)
context
yes
ground truth (progressive/regressive)
no
no
Stengel-Eskin et al. (2025)
weights (preference training)
yes
ground truth (positive/negative)
no
no
Xu et al. (2024); Xie et al. (2024)
context
partial
ground truth / prior
no
no
Wan et al. (2024)
context
no
evidence features, single turn
no
no
Choi et al. (2024)
context (persona)
drift only
n/a
no
no
Wallace et al. (2024)
weights (instruction hierarchy)
override, single turn
n/a
no
single instruction
Turner et al. (2023); Rimsky et al. (2024); Le & Le (2026)
activations
no
n/a
injection success
no
Chen et al. (2025a); Charakorn et al. (2025); Liu et al. (2026)
weights (hypernetwork)
no
n/a
acquisition
no
Cheng et al. (2026)
weights (hypernetwork)
vs. own prior, once
ground truth
acquisition
no
Bertalanič & Fortuna (2026)
multi-agent context
conformity
ground truth
no
no
This work
context vs. weights (Q,V), matched
yes
evidence quality, truth-blind
yes
yes

What this says to debate-based oversight
Debate-based oversight assumes that debaters hold positions for reasons and change them only for better ones (Irving et al., 2018; Buhl et al., 2025). Read against Table 1, that assumption is a claim that the debaters occupy the top-left cell. The findings here say that no conditioning channel puts them there. A persistence instruction produces a debater who never concedes (Section 5); a mild one produces a debater who concedes to pressure at chance with respect to the merits (Section 6); and compiling the position changes how firmly it is held, not whether the holding tracks reasons. What did track reasons was a reflection step that read the transcript afterward. The obfuscated-arguments problem (Barnes & Christiano, 2020) is one way soundness fails; a debater who cannot tell a good objection from a hollow one in the moment is another, and it is the one this instrument can measure. The multi-agent conformity that Bertalanič and Fortuna (2026) document is a third, and whether compiled positions resist it is an open question, because the persona-conformity reversal (Section 9.2 and Appendix I) shows the same modulation increasing conformity to a supplied persona.

References
Barnes, E., & Christiano, P. (2020). Debate update: Obfuscated arguments problem. AI Alignment Forum.
Bertalanič, B., & Fortuna, C. (2026). The cost of consensus: Isolated self-correction prevails over unguided homogeneous multi-agent debate. arXiv:2605.00914.
Brown-Cohen, J., Irving, G., & Piliouras, G. (2023). Scalable AI safety via doubly-efficient debate. arXiv:2311.14125.
Buhl, M. D., Pfau, J., Hilton, B., & Irving, G. (2025). An alignment safety case sketch based on debate. arXiv:2505.03989.
Charakorn, R., Cetin, E., Tang, Y., & Lange, R. T. (2025). Text-to-LoRA: Instant transformer adaption. In Proceedings of the 42nd International Conference on Machine Learning (PMLR 267).
Charakorn, R., Cetin, E., Uesaka, S., & Lange, R. T. (2026). Doc-to-LoRA: Learning to instantly internalize contexts. arXiv:2602.15902.
Chen, T., Fang, H., Xia, P., Liu, X., Van Durme, B., Zettlemoyer, L., Gao, J., & Cheng, H. (2025a). GenerativeAdapter: Contextualizing language models in parameters with a single forward pass. In The Thirteenth International Conference on Learning Representations.
Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. (2025b). Persona vectors: Monitoring and controlling character traits in language models. arXiv:2507.21509.
Cheng, S., Shi, X., Zhang, Z., & Li, M. (2026). The override gap: A magnitude account of knowledge conflict failure in hypernetwork-based instant LLM adaptation. arXiv:2604.23750.
Choi, J., Hong, Y., Kim, M., & Kim, B. (2024). Examining identity drift in conversations of LLM agents. arXiv:2412.00804.
Fanous, A., Goldberg, J. N., Agarwal, A., Lin, J., Zhou, A., Xu, S., Bikia, V., Daneshjou, R., & Koyejo, S. (2025). SycEval: Evaluating LLM sycophancy. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society.
Hamblin, C. L. (1970). Fallacies. Methuen.
Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2022). LoRA: Low-rank adaptation of large language models. In International Conference on Learning Representations.
Irving, G., Christiano, P., & Amodei, D. (2018). AI safety via debate. arXiv:1805.00899.
Khan, A., Hughes, J., Valentine, D., Ruis, L., Sachan, K., Radhakrishnan, A., Grefenstette, E., Bowman, S. R., Rocktäschel, T., & Perez, E. (2024). Debating with more persuasive LLMs leads to more truthful answers. In Proceedings of the 41st International Conference on Machine Learning.
Krippendorff, K. (2018). Content analysis: An introduction to its methodology (4th ed.). Sage.
Laban, P., Murakhovs’ka, L., Xiong, C., & Wu, C.-S. (2023). Are you sure? Challenging LLMs leads to performance drops in the FlipFlop experiment. arXiv:2311.08596.
Le, K., & Le, T. (2026). Adversarial robustness of activation steering in large language models. arXiv:2606.07696.
Li, X. L., & Liang, P. (2021). Prefix-tuning: Optimizing continuous prompts for generation. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics.
Liu, Y., Wang, X., Mao, Y., Gelberg, Y., Maron, H., & Zhang, M. (2026). SHINE: A scalable in-context hypernetwork for mapping context to LoRA in a single pass. In Proceedings of the 43rd International Conference on Machine Learning (PMLR 306).
Mill, J. S. (1978). On liberty (E. Rapaport, Ed.). Hackett. (Original work published 1859)
Moffatt v. Air Canada, 2024 BCCRT 149 (Civil Resolution Tribunal of British Columbia, 14 February 2024).
Notopoulos, K. (2023, December 19). A car dealership added an AI chatbot to its site. Then all hell broke loose. Business Insider.
Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as operating systems. arXiv:2310.08560.
Peebles, W., & Xie, S. (2023). Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF International Conference on Computer Vision.
Perez, E., Ringer, S., Lukošiūtė, K., et al. (2023). Discovering language model behaviors with model-written evaluations. In Findings of the Association for Computational Linguistics: ACL 2023.
Perez, E., Strub, F., de Vries, H., Dumoulin, V., & Courville, A. (2018). FiLM: Visual reasoning with a general conditioning layer. In Proceedings of the AAAI Conference on Artificial Intelligence.
Plato. (1987). Gorgias (D. J. Zeyl, Trans.). Hackett.
Rimsky, N., Gabrieli, N., Schulz, J., Tong, M., Hubinger, E., & Turner, A. (2024). Steering Llama 2 via contrastive activation addition. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics.
Ryle, G. (1949). The concept of mind. Hutchinson.
Schwitzgebel, E. (2002). A phenomenal, dispositional account of belief. Noûs, 36(2), 249–275.
Sharma, M., Tong, M., Korbak, T., et al. (2024). Towards understanding sycophancy in language models. In The Twelfth International Conference on Learning Representations.
Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. In Advances in Neural Information Processing Systems 36.
Stengel-Eskin, E., Hase, P., & Bansal, M. (2025). Teaching models to balance resisting and accepting persuasion. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 8108–8122.
Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2023). Steering language models with activation engineering. arXiv:2308.10248.
Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J., & Beutel, A. (2024). The instruction hierarchy: Training LLMs to prioritize privileged instructions. arXiv:2404.13208.
Walton, D., & Krabbe, E. C. W. (1995). Commitment in dialogue: Basic concepts of interpersonal reasoning. State University of New York Press.
Wan, A., Wallace, E., & Klein, D. (2024). What evidence do language models find convincing? In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics.
Wang, B., Yue, X., & Sun, H. (2023). Can ChatGPT defend its belief in truth? Evaluating LLM reasoning via debate. In Findings of the Association for Computational Linguistics: EMNLP 2023, 11865–11881.
Wei, J., Huang, D., Lu, Y., Zhou, D., & Le, Q. V. (2023). Simple synthetic data reduces sycophancy in large language models. arXiv:2308.03958.
Wu, K., Wu, E., & Zou, J. (2024a). ClashEval: Quantifying the tug-of-war between an LLM’s internal prior and external evidence. In Advances in Neural Information Processing Systems 37 (Datasets and Benchmarks).
Wu, Z., Arora, A., Wang, Z., Geiger, A., Jurafsky, D., Manning, C. D., & Potts, C. (2024b). ReFT: Representation finetuning for language models. In Advances in Neural Information Processing Systems 37.
Xie, J., Zhang, K., Chen, J., Lou, R., & Su, Y. (2024). Adaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts. In The Twelfth International Conference on Learning Representations.
Xu, R., Lin, B., Yang, S., Zhang, T., Shi, W., Zhang, T., Fang, Z., Xu, W., & Qiu, H. (2024). The earth is flat because…: Investigating LLMs’ belief towards misinformation via persuasive conversation. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, 16259–16303.
Zou, A., Phan, L., Chen, S., et al. (2023). Representation engineering: A top-down approach to AI transparency. arXiv:2310.01405.
Reference entries marked with “et al.” in the author field are abbreviated for this draft; expand to full author lists in the camera-ready. Entries for 2026 preprints are taken from the manuscripts as of the dates in iclr_prep/references/notes/; confirm venues before submission.


[1] The grid is Plato’s, with the names removed from the cells. The compliant cell is Polus, who concedes to escape the audience’s judgment (474c–475e); the fixed cell is Callicles, who keeps his position by refusing examination (505c–506c); the standard is the interlocutor Socrates describes at 486e–487e. The indiscriminate cell has no named occupant in the Gorgias.


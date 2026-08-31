# DNN End-Sem Evidence and Priority Analysis

## Decision summary

The shortest high-return route is: **CNN calculations -> RNN/GRU/LSTM calculations -> attention -> transformer blocks -> optimizer/regularization diagnosis -> FFNN refresh**. These six families account for every question in the latest regular EC3 (1 March 2026, 120 marks) and every section in the latest makeup key. This is a very strong recurring signal, not a promise about the next paper.

Estimated DNN preparation time from near-zero: **14-16 focused hours**, including 5 hours of timed PYQ work. If time is severe, spend the first 10 hours on the six families above and skim NAS/time-series/federated/meta/online learning.

## Authoritative scope and current exam

Primary scope source: `Course Handouts/DNN COURSE HANDOUT.docx`, Digital Learning Handout, Second Semester 2025-2026, version 1.

- Course: AIMLC ZG511 Deep Neural Networks, 4 units.
- Current comprehensive exam: **6 September 2026 (AN), 2.5 hours, open book, 40%**.
- Comprehensive syllabus: **all topics, contact sessions 1-16**.
- Session 1-8: foundations, perceptron/MLP, DFNN/backprop, optimization, regularization, CNN and review.
- Session 9-16: RNN/BPTT, GRU/LSTM/BiLSTM, attention, transformers, NAS, CNN/LSTM time-series forecasting, federated/meta/online learning and review.
- Current lecture decks available through Session 14; the repository has companion notes for Session 15. No current Session 15/16 PPTX was found.

The handout's generic open-book wording mentions publisher books. The user's explicit instruction identifies `DNNWaterMarked.pdf` as an officially permitted exam-room resource; this package therefore treats it as permitted, while recommending a final check of the current exam-centre notice.

## Paper inventory and deduplication

| Evidence tier | Verified sitting | Structure | Use in this analysis |
|---|---|---|---|
| Latest | EC3 Regular, I Sem 2025-26, 1 Mar 2026 | 7 questions, 120 marks, 150 min, open book | Highest weight; original QP plus separate QP/key compilation |
| Latest | EC3 Makeup, I Sem 2025-26 | 7 questions, 120 marks | Highest weight; instructor solution manual; original QP not separately present |
| Second-latest | EC3 Regular, II Sem 2024-25, 7 Sep 2025 | 6 questions, 40 marks, 120 min, open book | Strong recent corroboration |
| Second-latest | EC3 sitting dated 14 Sep 2025 (file labelled Makeup; cover says Regular) | 6 questions, 40 marks, 120 min, open book | Strong corroboration; session-label conflict retained |
| Older | EC3 Regular, 29 Sep 2024 | 4 questions, 35 marks, 120 min, open book | Stable pattern only |
| Older | EC3 Makeup, 6 Oct 2024 | 4 questions, 35 marks, 120 min, open book | Stable pattern only |
| Older | EC3 Regular/Makeup 2023-24 | 5 questions, 30 marks, 150 min, closed book | Low trend weight; useful numericals |
| Legacy | 2022-23 papers | Different programme/course number appears in at least one file | Do not use for current-pattern probability; methods only |

Exact SHA-256 duplicates were found for the latest EC3 and EC2 originals in `Latest Question Papers/` and `Previous Question Papers/`; each pair is counted once. `2023 MidSem Regular DNN.pdf` and `23_EC3_MQPS1.pdf` are also byte-identical but are not end-sem evidence. The image-only files named `2022/2023 EndSem ...` contain only wrapper text under extraction; question-level claims are taken from the text-bearing `Previous Question Papers` copies where available.

## Cross-paper signal

Recent presence counts below use six text-verifiable EC3 sittings: Mar-2026 regular/makeup, Sep-2025 regular/makeup-file, Sep/Oct-2024 regular/makeup. Presence is not probability.

| Topic family | Recent presence | Latest regular marks | Direction | Confidence |
|---|---:|---:|---|---|
| FFNN, activations, loss, gradient flow | 6/6 | Q1 15 + Q2 15 | Stable; more applied in 2026 | VERY HIGH |
| RNN/GRU/LSTM/BPTT | 6/6 | Q4 15 | Stable numerical + selection | VERY HIGH |
| Attention (dot/additive/multi-head) | 6/6 | Q5 15 | Stable and increasingly multi-part | VERY HIGH |
| CNN shape/parameters/design | 4/6 direct; CNN applications also occur | Q3 20 | High marks in both newest sittings | VERY HIGH |
| Optimizers/regularization/normalization | 5/6 | Q7 20 | Expanded sharply in latest papers | VERY HIGH |
| Transformer architecture/parameters/model choice | both 2026 EC3; weaker before | Q6 20 | Clearly rising | HIGH |
| Transfer learning/receptive field/GAP | recent regular papers | inside Q3 | Applied design signal | HIGH |
| NAS/time-series | both Sep-2025; some 2024 | absent from latest EC3 | Declining recent signal, still official | MODERATE |
| Federated/meta/online learning | isolated 2024/official syllabus | absent from latest EC3 | Weak current evidence | LOW-MODERATE |

## Recent paper signal

### Latest regular: 1 March 2026

The entire 120-mark paper was organized by core family: Q1 DFNN fundamentals (15), Q2 binary DFNN design (15), Q3 transfer learning/CNN parameters/receptive field (20), Q4 RNN-GRU numerical and gradient flow (15), Q5 attention (15), Q6 transformers (20), Q7 optimization and regularization (20). It rewards calculations, scenario choice, and explicit justification more than isolated recall.

### Latest makeup

The instructor manual allocates: FFNN 16; RNN architecture + LSTM 20; RNN numerical + optimizers 20; overfitting + weight symmetry 20; CNN 18; transformer parameters 15; translation/attention reasoning 11. This independently reinforces the same core.

### Latest EC2 supporting signal

The 21 December 2025 EC2 regular (100 marks) emphasized perceptron, linear/logistic/softmax calculations, code completion, confusion matrices and a two-layer DFNN. It is not end-sem frequency evidence, but it confirms the expected prerequisite fluency: forward pass, correct activation-loss pairing, gradients, dimensions, code expressions and mark-aware interpretation.

### Stable structures

- A calculation followed by a one- or two-sentence interpretation.
- Parameter count plus architecture choice under compute/data constraints.
- A given curve/behaviour followed by diagnosis and remedy.
- Attention score -> softmax -> context, with masking or head reasoning.
- Several small subparts inside a 15-20 mark scenario.

### Less relevant older patterns

Exact framework syntax, broad application lists, one-shot NAS and federated learning appear in older/second-latest papers but disappear from both newest EC3 sittings. Skim them; do not let them displace latest-core numericals.

## Priority and expected return per hour

Expected return is a planning judgement supported by paper recurrence, marks and learning time; it is not an expected-mark guarantee.

| Topic | Priority | Evidence | Question type | Study time | Expected return/hour |
|---|---|---|---|---:|---|
| CNN shapes, parameters, GAP, receptive field | MUST | 2026 R Q3 (20), 2026 M Q5 (18), both Sep-2025 Q3 | numerical + design | 2.0 h | Exceptional |
| RNN/GRU/LSTM states and parameter counts | MUST | every recent EC3; 15-20 marks latest | numerical + choose/justify | 2.5 h | Exceptional |
| Scaled/additive/multi-head attention | MUST | every recent EC3; 15 latest | numerical + compare | 2.0 h | Exceptional |
| Transformer block/dimensions/architecture | MUST | both 2026; 20 + 26 marks | parameters + explain | 2.0 h | Very high |
| Optimizer and regularization diagnosis | MUST | both 2026; 20 marks each family block | curves + remedy | 1.5 h | Exceptional |
| FFNN forward, activation/loss, gradient flow | MUST | 30 marks latest regular; EC2 prerequisite | numerical + design | 1.5 h | Very high |
| Transfer learning and deployment trade-offs | HIGH | 2026 R Q3; Sep-2025 | justify/design | 0.75 h | High |
| BPTT, vanishing/exploding, bidirectionality | HIGH | repeated inside sequence questions | derivation/concept | 0.75 h | High |
| NAS and time-series architectures | SHOULD | both Sep-2025; official scope | short concept/design | 0.5 h | Moderate |
| Federated/meta/online learning | SKIM | isolated older + official | short concept | 0.4 h | Low-moderate |

## Must-practice references

1. 2025-26 EC3 Regular Q3: CNN/transfer/parameter redesign.
2. 2025-26 EC3 Regular Q4: RNN vs GRU numerical and gradient highway.
3. 2025-26 EC3 Regular Q5: three attention forms.
4. 2025-26 EC3 Regular Q6: transformer dimensions, parameters and model choice.
5. 2025-26 EC3 Regular Q7: optimizer/schedule/regularization curves.
6. 2025-26 EC3 Makeup Q1, Q2B and Q3A: FFNN, LSTM and RNN calculations.
7. II Sem 2024-25 EC3 Regular Q3 and Sep-2025 makeup-file Q3: complete CNN dimension chains.

## Evidence caveats and conflicts

- The latest EC3 original cover says “Mid-Semester Test (EC3 - Regular)” while its course/session, 120 marks and repository placement identify it as the comprehensive component. The label conflict is preserved.
- The 14 Sep 2025 file is named Makeup but its cover says EC3 Regular. It is treated as a distinct second-latest sitting, not assigned a fabricated session label.
- The 2026 makeup question wording is reconstructed only where the instructor manual states the question/data. No separate original makeup QP was found.
- The Sep-2024 regular attention key says Bahdanau attention has quadratic complexity; the general sequential-computation criticism is valid, but complexity depends on source/target lengths and implementation. The guide uses the standard course-level comparison and flags conventions.
- A legacy 2022 RMSProp key appears to use a plus sign in the update despite defining a gradient; this package uses the standard descent update `theta <- theta - eta*g/sqrt(v+eps)`.
- Additive-attention numerical data in 2026 Regular Q5(b) omits learned scoring parameters in extracted text. A numerical answer requires an explicit convention; the solution bank states one and does not present it as uniquely determined.
- **Insufficient PYQ evidence:** the exact future marks split among attention, transformers and recurrent units, and a unique numerical answer for the underspecified additive-attention subpart.

## Source register

- Primary scope: `Course Handouts/DNN COURSE HANDOUT.docx`.
- Highest-weight papers: latest EC3 original, Mar-2026 regular QP/key, Mar-2026 makeup instructor manual.
- Recency support: Sep-2025 regular and 14-Sep-2025 sitting; latest EC2 original.
- Older stability support: 2024 EC3 regular/makeup keys, 2023-24 text-bearing papers.
- Current teaching signal: Session 9-14 PPTX files dated July-August 2026; companion Session 15 notes.
- Exam-room source: `DNNWaterMarked.pdf`, 196 PDF viewer pages, generated 24 Aug 2026 for pages 1-82 and 21 Aug 2026 for later sections.
- Structural reference only: Mid-Sem `MIDSEM_SCORING_GUIDE.md` and `MIDSEM_QUESTION_BANK.md`.
- Reused with verification: repository `ENDSEM_SCORING_GUIDE.md` and `ENDSEM_QUESTION_BANK.md`; their unlabeled practice items were not carried over as actual PYQs.

## Self-audit

- [x] Current handout and all official modules accounted for.
- [x] Latest EC3 and latest EC2 inspected; duplicate binaries counted once.
- [x] Recent papers weighted above older papers.
- [x] Actual questions, variations and original practice are labeled separately.
- [x] Question numbers/marks used only where visible in an original paper or instructor manual.
- [x] Key numericals recomputed; convention-dependent results identified.
- [x] Answer depth is mark-aware; inferred depth is marked in the solution bank.
- [x] Watermark references use PDF viewer numbering, not printed slide numbers.
- [x] Unsupported exact predictions avoided.
- [x] OCR/image-only gaps explicitly recorded.

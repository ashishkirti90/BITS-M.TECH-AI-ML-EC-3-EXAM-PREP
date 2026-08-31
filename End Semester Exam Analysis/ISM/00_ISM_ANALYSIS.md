# ISM End-Sem Evidence and Priority Analysis

**Course:** AIMLC ZC418 - Introduction to Statistical Methods  
**Current authoritative handout:** Second Semester 2025-2026  
**Current EC-3:** 05-09-2026 (FN), open book, 40%, 150 minutes, all contact sessions  
**Preparation objective:** maximum expected marks in the remaining 5 days, starting near zero

## 1. Decision summary

The shortest scoring route is:

1. Hypothesis-test selection and execution.
2. Correlation plus simple regression.
3. SES, moving average and Holt forecasting.
4. One-way/two-way ANOVA, chi-square and variance F-test.
5. Confidence intervals and CLT.
6. GMM/EM, MLE and residual diagnostics.
7. Probability/distributions only as a targeted comprehensive-syllabus safety pass.

This ordering is not textbook order. It is driven by the three most recent distinct EC-3 sittings and the current Session 9-15 lecture sequence.

## 2. Authoritative syllabus map

| Module | Current handout scope | Sessions | End-sem action |
|---|---|---:|---|
| Basic probability and statistics | centre, variability, probability axioms, independence | 1-2 | skim after core end-sem topics |
| Conditional probability and Bayes | conditional/total probability, Bayes proof, Naive Bayes | 3-4 | targeted revision; older-paper signal |
| Random variables and distributions | discrete/continuous/joint RVs; Bernoulli, binomial, Poisson, normal, introductory t/F/chi-square | 5-6 | targeted numerical safety pass |
| Sampling and inference | sampling, CLT, interval estimation, mean/proportion tests, one/two-way ANOVA, MLE | 7, 9-10 | MUST DO |
| Prediction and forecasting | correlation, regression, moving/weighted averages, AR/ARMA/ARIMA, SARIMA/SARIMAX/VAR/VARMAX, SES | 11-14 | MUST DO; prioritize hand calculations |
| Mixture modelling | GMM and expectation maximization | 15 | HIGH; latest-regular signal |

The handout explicitly makes EC-3 comprehensive. No topic is officially excluded.

## 3. Paper corpus and deduplication

### Distinct EC-3 evidence used

| Recency | Verified sitting | Course | Structure | Role |
|---:|---|---|---|---|
| 1 | 07-03-2026 EC-3 Makeup | AIMLC ZC418 | 8 questions / 40 marks, 2 h | latest question-type signal |
| 2 | 28-02-2026 EC-3 Regular | AIMLC ZC418 | 8 x 5 marks, 2 h | latest regular; strongest signal |
| 3 | 06-09-2025 EC-3 Regular | AIMLC ZC418 | 5 blocks totalling 40, 2 h | second-latest cycle |
| 4 | 05-10-2024 EC-3 Makeup | AIMLC ZC418 | 4 x 10 marks, 150 min | recent historical |
| 5 | 28-09-2024 EC-3 Regular | AIMLC ZC418 | 4 x 10 marks, 150 min | recent historical |
| 6 | April 2024 EC-3 Regular and Makeup | AIMLC ZC418 | mostly 6-7 mark questions | older historical |
| 7 | April 2023 EC-3 Regular and Makeup | DSECL ZC413 | 4 x 10 marks, 150 min | very low-weight legacy context |

### Duplicates removed

The files `S2_23(AIML)_ISM_EC3R_28th Sept 2024.pdf` and `Question papers/2023 EndSem Regular ISM.pdf` are byte-identical. The corresponding 05-Oct-2024 makeup files are also byte-identical. Each pair is counted once. Compilation files and `Previous_batch_endsem_ISM_papers.pdf` are not counted as additional sittings.

### Source conflict that affects answers

The official 28-Feb-2026 EC-3 DOCX and `Feb 2026 ISM endsem regular QP & answer key.pdf` do not fully agree:

- Official DOCX Q4 is randomized-block/two-way ANOVA; the key PDF substitutes a one-way fertilizer problem.
- Official DOCX Q6 gives two raw five-value groups; the key PDF substitutes precomputed component means/variances.
- The key PDF reports the official regression approximately as `0.40 + 0.42X`; independent recalculation from the official data gives `0.6074 + 0.4092X`.

Therefore the official EC-3 DOCX controls question wording. The key is used only when its prompt matches, and all retained numericals were recomputed.

The handout contains generic open-book language limiting material to publisher copies, while the task instruction states that `ISM watermark.pdf` is specifically authorized for this examination. This system follows the explicit permitted-resource instruction and indexes that PDF; retain any centre/course-specific authorization with the exam documents if one was issued.

## 4. Cross-paper signal

The counts below are **paper presence**, not predicted probabilities. A topic appearing twice in one paper is counted once for recurrence.

| Topic family | Three newest sittings | Broader AIML history | Signal | Direction |
|---|---:|---:|---|---|
| Correlation/regression | 3/3 | recurring in every identifiable 2024-26 cycle | VERY HIGH | stable |
| Forecasting (SES/MA/Holt) | 3/3 | recurring in every identifiable 2024-26 cycle | VERY HIGH | stable, broader methods recently |
| Mean/proportion hypothesis tests | 3/3 | recurrent | VERY HIGH | stable |
| ANOVA | 2/3, both 2026 | older chi-square/ANOVA also present | HIGH | gaining |
| Confidence intervals | 2/3, both 2026 | older recurrence | HIGH | gaining |
| Chi-square or variance F | 2/3 newest; F also in Sep-2025 | older chi-square recurrence | HIGH | stable/gaining |
| Autocorrelation/residual adequacy | 1/2 newest plus older autocorrelation | time-series family is stable | HIGH | gaining in diagnostics |
| GMM/EM | latest regular only | absent from older papers because syllabus matured | HIGH | new/prominent |
| MLE | Sep-2025 plus legacy 2023 | intermittent | MODERATE | stable but sparse |
| Probability/joint distributions | absent from three newest EC-3 sittings | frequent in 2024 and legacy papers | MODERATE | losing relative weight, still comprehensive |
| Advanced ARIMA-family hand calculation | no direct recent long derivation | official Sessions 13-14 | LOW-MODERATE | insufficient PYQ evidence |

## 5. Recent paper signal

### Latest paper: 07-Mar-2026 makeup

Emphasis: two-sample test plus CI, chi-square independence, moving average, lag-1 autocorrelation, one-sample z, Holt trend, simple regression, one-way ANOVA. Every block asks selection plus executable hand calculation. There is almost no generic prose.

### Latest regular: 28-Feb-2026

Emphasis: Pearson correlation, SES with two alphas, paired t and one-sample z, randomized-block ANOVA, regression with adequacy and resource-efficiency reasoning, GMM estimation, t-CI plus residual diagnosis, two-proportion z and a directional F-test. Interpretation is attached to most calculations.

### Second-latest regular: 06-Sep-2025

Emphasis: correlation and one-sample t, SES plus MSE comparison, regression/prediction, Holt forecasting, variance F-test and Poisson MLE. Forecasting occupied half the paper by marks.

### Stable patterns

- State assumptions at the beginning; the paper explicitly instructs this.
- Show the full calculation, then interpret in context.
- Five-mark blocks are commonly one standard method plus a short interpretation.
- Forecast-model selection uses reaction speed or an error metric, not intuition alone.
- Regression questions extend beyond coefficients to adequacy, prediction or a practical decision.

### Current 2025-26 teaching signal

The current handout and current lectures place Session 9 hypothesis tests, Session 10 MLE/ANOVA, Session 11 correlation/regression, Sessions 12-14 time series, and Session 15 GMM/EM consecutively before review. The current watermark includes worked material for all of them. The latest repository EC2 paper is 20-Dec-2025 and covers Sessions 1-7; it supports prerequisite competence but is **not** counted as EC-3 recurrence.

### Insufficient evidence

- No current 05-Sep-2026 question paper exists in the repository.
- No reliable recent EC-3 evidence supports a long SARIMAX/VAR/VARMAX derivation.
- Exact 2026 marking schemes are incomplete and conflict for two Feb questions.
- Current EC-3 will be 150 minutes, while the two 2026 historical papers were 120 minutes; do not assume eight equal five-mark blocks.

## 6. Priority and expected return per hour

Expected return is a relative planning estimate, not a marks guarantee.

| Topic | Priority | Recent evidence | Typical form | Difficulty | First-pass time | Expected return |
|---|---|---|---|---|---:|---|
| Test selection: z/t/paired/two-sample/proportion | MUST DO | all 3 newest | numerical + conclusion | medium | 2.0 h | Very high: several reusable 2-5 mark patterns |
| Correlation + simple regression | MUST DO | all 3 newest | calculate, predict, interpret | easy-medium | 1.75 h | Very high: stable 5-10 mark family |
| SES + moving average + model comparison | MUST DO | all 3 newest | forecast table/MSE | easy-medium | 1.5 h | Very high: mechanical and recurring |
| Holt trend | MUST DO | Mar-2026, Sep-2025 | update table + forecast | medium | 0.75 h | Very high: 5-8 mark template |
| One-way/two-way ANOVA | MUST DO | both 2026 | ANOVA table + decision | medium-hard | 1.75 h | High: latest concentration |
| CI + CLT | HIGH | both 2026 | z/t interval, interpretation | easy | 0.75 h | Very high: fast bankable marks |
| Chi-square + variance F | HIGH | Mar/Feb-2026, Sep-2025 | expected counts or variance ratio | medium | 1.0 h | High |
| GMM + EM | HIGH | Feb-2026; current Session 15 | mixture/parameters/responsibility | medium | 0.9 h | High: latest/new topic |
| Residuals, white noise, autocorrelation | HIGH | both 2026 | calculate + diagnose | medium | 0.75 h | High |
| MLE | SHOULD DO | Sep-2025; legacy recurrence | likelihood and standard estimator | medium | 0.65 h | Moderate-high |
| Probability/Bayes/distributions | SHOULD DO | older papers; current comprehensive scope | direct numerical | medium | 1.25 h | Moderate safety coverage |
| AR/ARMA/ARIMA concepts | SHOULD DO | current syllabus; indirect diagnostic signal | identify/order/explain | medium | 0.65 h | Moderate |
| SARIMA/SARIMAX/VAR/VARMAX | LOW / SKIM | syllabus only; insufficient recent PYQ evidence | distinction/use case | hard | 0.35 h | Low per hour |

**Core total:** about 13.0 hours including two timed paper passes and error review.  
**With probability/distribution safety pass:** about 14.5 hours.

## 7. Must-practice paper references

1. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q2, 5 marks - SES for two alphas.
2. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q4, 5 marks - randomized-block ANOVA, including the zero-error trap.
3. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q5, 5 marks - regression, adequacy and water-use decision.
4. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q8, 5 marks - two-proportion z and directional F-test.
5. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q2, 5 marks - chi-square independence.
6. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q6, 5 marks - Holt forecasting.
7. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q8, 5 marks - one-way ANOVA.
8. [ACTUAL PYQ] ISM, 06-Sep-2025 EC-3 Regular, Q2, 8 marks - SES and MSE comparison.

## 8. Evidence register

| Evidence | Authority/use |
|---|---|
| `Course Handouts/ISM COURSE HANDOUT.docx` | primary syllabus, current exam scope/date/duration |
| `Latest Question Papers/...EC3_REGULAR_28-02-2026_FN.docx` | authoritative latest regular wording |
| `Question papers/Mar 2026 ISM endsem makeup QP & answer key.pdf` | latest makeup paper/key |
| `Question papers/2024 EndSem Regular ISM.pdf` | 06-Sep-2025 paper despite misleading filename |
| `Previous Question Papers/*EC3*`, `Question papers/2023 EndSem*` | historical trend; byte duplicates removed |
| `Latest Question Papers/...EC2_REGULAR_20-12-2025_FN.docx` | latest EC2 prerequisite/current-style signal only |
| `ISM lecture/ISM_NSP4_Lecture*.pdf` and current content inside `ISM watermark.pdf` | current teaching emphasis and notation |
| `ISM watermark.pdf` | permitted exam-room lookup; 261 viewer pages |
| `ENDSEM_SCORING_GUIDE.md`, `ENDSEM_QUESTION_BANK.md` | reusable draft only; all retained claims independently checked |
| `MID SEM ANALYSIS/ISAM/*` | structural/quality reference only |

## 9. Self-audit

- [x] Every handout module is accounted for.
- [x] Latest regular, latest makeup and second-latest regular were analyzed first.
- [x] Duplicate paper files were removed from recurrence counts.
- [x] Actual PYQs and practice items use strict labels.
- [x] Question numbers/marks appear only when verified.
- [x] Twenty high-value PYQ entries were independently recalculated.
- [x] Formula notation and answer depth were checked against marks.
- [x] Recent-paper signal and evidence gaps are explicit.
- [x] Watermark references use PDF viewer page numbers verified against the 261-page PDF.
- [x] No exact-question prediction or frequency-to-probability conversion is made.

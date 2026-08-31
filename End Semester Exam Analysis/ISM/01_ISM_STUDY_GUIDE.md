# ISM End-Sem Study Guide

## Exam orientation

The current handout schedules EC-3 for **05-09-2026 (FN)**: open book, 40%, **150 minutes**, and **all sessions**. The two newest repository papers used 8 equal five-mark blocks in 120 minutes, but the current exam duration differs, so prepare methods rather than assuming that exact layout.

Recent papers are calculation-heavy. The durable scoring pattern is:

`recognize method -> state assumptions -> show formula and work -> make decision -> interpret in context`.

Strongest current signals: inference, correlation/regression and forecasting. Both 2026 papers also emphasize ANOVA, CI and diagnostics. GMM is a new latest-regular signal.

## Priority map

| Topic | Priority | Recent evidence | Mode | First-pass time | Expected return |
|---|---|---|---|---:|---|
| z/t/paired/two-sample/proportion tests | MUST DO | all 3 newest | numerical + conclusion | 2.0 h | very high |
| correlation/regression | MUST DO | all 3 newest | numerical + interpretation | 1.75 h | very high |
| SES/moving average/Holt | MUST DO | all 3 newest | forecast table + compare | 2.25 h | very high |
| one/two-way ANOVA | MUST DO | both 2026 | ANOVA table | 1.75 h | high |
| CI/CLT | HIGH | both 2026 | short numerical | 0.75 h | very high |
| chi-square/F tests | HIGH | newest papers | numerical/test selection | 1.0 h | high |
| ACF/residuals/white noise | HIGH | both 2026 | calculate + diagnose | 0.75 h | high |
| GMM/EM | HIGH | latest regular | estimate/explain | 0.9 h | high |
| MLE | SHOULD DO | Sep-2025 | derivation/plug-in | 0.65 h | moderate-high |
| probability/distributions | SHOULD DO | older; comprehensive scope | numerical | 1.25 h | moderate |
| advanced ARIMA family | SKIM | syllabus, weak direct PYQ evidence | identify/explain | 0.65 h | moderate-low |

## Learning order

`sampling/SE -> confidence intervals -> hypothesis tests -> chi-square/ANOVA -> correlation/regression -> MA/SES -> Holt/ACF/ARIMA -> MLE -> GMM/EM`.

Basic probability is a prerequisite for understanding p-values and mixtures, but do not spend the first day re-learning every early-session puzzle.

---

## 1. Statistical inference from near zero

### What is it?

A sample statistic varies from sample to sample. Inference uses its sampling distribution to say how compatible the observed result is with a population claim.

### What must you understand?

- `H0` is the testable equality/status-quo claim; `H1` determines the tail.
- A p-value is computed **assuming H0**. It is not the probability that H0 is true.
- Standard error measures sampling variability of an estimator.
- A statistically significant result can still be practically small; a non-significant result is not proof of no effect.

### What must you memorize?

- one-mean z/t, paired t, Welch two-sample t and pooled two-proportion z.
- decision rule `p<alpha -> reject H0`.
- “fail to reject,” not “accept.”
- known population SD -> z; unknown SD -> t (especially small n).

### How is it tested?

Claims about improvement, underfilling, differences between programs or proportions; usually 2-5 marks. Marks reward hypotheses, calculation and context, not just a final statistic.

### Common mistakes

- Alternative tail does not match “greater/lower/different.”
- Paired data treated as independent.
- Type I/II risk stated backward.
- Critical value used without df.
- Conclusion has no domain wording.

### Numerical template

`parameter -> H0/H1 -> assumptions -> statistic/df -> p/critical -> decision -> contextual conclusion`.

### 1-minute revision

Paired = test differences. Known sigma = z. Two independent means = Welch by default. Equality of two proportions = pooled SE. Tail comes from wording before calculation. Never prove H0.

---

## 2. Confidence intervals and CLT

### What is it?

A confidence interval is an estimate plus/minus a margin of error. The CLT explains why many sample means/proportions have an approximately normal sampling distribution.

### Understand

- Larger `n` shrinks SE at rate `1/sqrt(n)`.
- Greater confidence widens the interval.
- t is wider than z because sigma is estimated.
- CI and a two-sided test agree: if the null value is outside a `(1-alpha)` CI, reject at `alpha`.

### Memorize

`estimate +/- critical x SE`, plus the correct SE. Round required sample size upward.

### How tested

The newest papers ask direct z/t intervals and one-sentence interpretation. This is fast, bankable work.

### 1-minute revision

Known sigma -> z. Unknown sigma -> t, df `n-1`. Interpret the population parameter. Halving margin of error needs roughly four times the sample size.

---

## 3. Chi-square, F-test and ANOVA

### What are they?

- Chi-square compares categorical observed counts with expected counts under independence.
- F compares variances or ratios of explained to unexplained variation.
- ANOVA tests whether three or more population means can be treated as equal.

### Understand

ANOVA partitions total variability. In one-way ANOVA, between-group variation is signal and within-group variation is noise. Blocking removes known nuisance variation. A large F means signal dominates estimated noise.

### Memorize

- chi-square `E=RC/N`, statistic and df.
- one-way `SSB/SSW`, df and F.
- randomized-block `CF`, treatment/block/error SS and df.
- directional variance F numerator follows `H1`.

### How tested

Both 2026 papers contain ANOVA. Latest makeup contains chi-square; latest regular and Sep-2025 contain variance F-tests.

### Common mistakes

- Expected counts omitted.
- ANOVA source rows/df mismatched.
- “All groups differ” after rejecting omnibus H0.
- Block effect ignored.
- Feb-2026 Q4: dividing by zero residual and reporting a fake finite F.

### 1-minute revision

Categorical counts -> chi-square. Three means -> ANOVA. Treatment-by-block table -> two-way without replication. Variance claim -> F upper tail. Write the table even if arithmetic is incomplete; method marks matter.

---

## 4. Correlation and regression

### What are they?

Correlation describes the strength/direction of a linear association. Regression fits a line for mean response/prediction.

### Understand

- `r` is unitless and symmetric; regression has an outcome and predictor.
- Slope has units and means expected Y change per unit X.
- `R^2` is explained sample variation, not predictive accuracy on new data.
- A curved residual pattern, saturation or influential point can invalidate a linear decision even with high `r`.

### Memorize

`r=Sxy/sqrt(SxxSyy)`, `b1=Sxy/Sxx`, `b0=ybar-b1xbar`, `R^2=1-SSE/SST`.

### How tested

Every recent sitting includes correlation/regression. Latest regular extends it to model adequacy and a resource-efficiency recommendation.

### Common mistakes

- `r` used as slope.
- No intercept calculation.
- Prediction outside observed X without warning.
- Correlation described as causation.

### Numerical template

Means -> deviation sums -> `r` or `b1,b0` -> prediction -> residual/adequacy -> contextual limit.

### 1-minute revision

Correlation measures linear association; regression predicts. Slope is `Sxy/Sxx`, intercept centres the line through `(xbar,ybar)`. Always add one interpretation and one limitation.

---

## 5. Forecasting and time series

### What is it?

A time series is ordered data whose past may inform its future. Forecast methods differ by whether the series has only a level, a trend, seasonality or autocorrelation.

### Understand

- MA and SES are level methods; they lag a sustained trend.
- Larger SES alpha reacts more strongly to the newest observation.
- Holt adds a trend state; Holt-Winters also adds seasonality.
- Compare forecasts using errors computed on the same periods.
- Trend can create high autocorrelation; stationarity matters for AR models.

### Memorize

- trailing MA.
- SES recursion.
- Holt level/trend/forecast equations.
- white-noise conditions.
- meanings of ARIMA `(p,d,q)`.

### How tested

Every newest paper has forecasting. Recent types include two-alpha SES, MSE comparison, trailing MA, Holt updates, lag-1 correlation and residual diagnosis.

### Common mistakes

- Off-by-one forecast indexing.
- Centred MA used to forecast future data.
- “larger alpha is always better.”
- White noise declared only because mean is zero.
- MA error term in ARIMA confused with moving-average smoothing.

### Model selection template

| Pattern | First method |
|---|---|
| stable level, noisy | MA or SES |
| trend, no seasonality | Holt |
| trend + seasonality | Holt-Winters/SARIMA |
| external drivers | SARIMAX |
| several interacting series | VAR/VARMAX |

### 1-minute revision

SES: next forecast blends current actual and current forecast. Holt: level plus trend. Large alpha reacts quickly. Compare MSE on common periods. Residuals should look like white noise.

---

## 6. MLE, GMM and EM

### What are they?

MLE chooses parameters under which the observed data are most likely. A GMM represents heterogeneous/multimodal data as a weighted sum of Gaussian components. EM estimates a GMM when component memberships are unknown.

### Understand

- GMM gives soft probabilities, unlike hard clustering.
- E-step estimates memberships from current parameters.
- M-step updates weights, means and covariances using those memberships.
- EM improves/non-decreases likelihood but may reach a local optimum.

### Memorize

- likelihood -> log -> derivative -> solve.
- mixture density and weights sum to one.
- responsibility numerator divided by total mixture density.
- ML variance uses component count/effective count.

### How tested

Sep-2025 asks Poisson MLE. Feb-2026 asks GMM density, two component estimates, mixing coefficients and why the mixture is useful.

### Common mistakes

- Using `n-1` for explicitly requested ML variance.
- Omitting weights in responsibility.
- Calling each component a deterministic class.
- Claiming EM guarantees global optimum.

### 1-minute revision

Poisson MLE = sample mean. GMM = weighted Gaussians. Responsibility = weighted component density / total density. E-step memberships; M-step parameters; repeat to convergence.

---

## 7. Probability and distributions safety pass

The comprehensive handout includes Sessions 1-7. Older EC-3 papers ask conditional probability, joint densities, binomial/Poisson and normal calculations. Recent EC-3 emphasis has shifted, so use a bounded pass:

1. Bayes/total probability.
2. Validate PMF/PDF; marginals and independence.
3. Binomial/Poisson selection and probability.
4. Normal standardization and sampling mean.

### 1-minute revision

Normalize probabilities first. Independence means joint factors into marginals. Binomial has fixed independent trials; Poisson models counts/rates. Standardize before using a normal table.

## What to memorize, understand and look up

| Memorize | Understand | Look up in watermark |
|---|---|---|
| test-selection tree and core statistics | assumptions, tails and conclusion language | critical values and long examples |
| Pearson/regression/SES/Holt forms | interpretation and model adequacy | ANOVA table details, pp. 125-133 |
| ANOVA/chi-square df | source-of-variation logic | advanced ARIMA equations, pp. 186-193 |
| GMM density/responsibility | soft assignment and EM | covariance update, pp. 194-203 |

## How to write BITS exam answers

### 1-2 marks

State the exact formula/definition, substitute once, and give a one-sentence conclusion. Example: for a variance F-test, hypotheses + ratio/df + decision is enough.

### 3-4 marks

Add method selection, assumptions and at least one intermediate value. For a two-proportion test, show sample proportions, pool, SE and z.

### 5-6 marks

Use a complete calculation table or sequence and interpret. A five-mark ANOVA needs source SS, df, MS, F and decision.

### 7-10 marks

Show full derivation/table, diagnostics/comparison and a justified practical conclusion. Separate subparts visibly.

Exact subpart marking schemes are not available for every paper; this depth is inferred from verified paper structures.

### By answer type

- Numerical: Given -> Required -> Method/assumptions -> Formula -> Work -> Final answer -> Context.
- Derivation: starting equation -> log/transform -> derivative/algebra -> result -> conditions.
- Concept: definition -> mechanism -> equation/property -> use -> limitation.
- Comparison: compact table -> selection rule -> justified choice.
- Justify: claim -> quantitative evidence -> assumption -> practical limit.
- Algorithm: input -> initialization -> loop/calculation -> stopping -> output.
- Diagram/architecture: labelled blocks/arrows plus one sentence explaining flow.
- Interpretation: magnitude/direction -> uncertainty -> context -> forbidden inference.

## Final 24-hour revision

1. Redo without notes: Feb-2026 Q2, Q5, Q8; Mar-2026 Q2, Q6, Q8.
2. Write the test-selection tree and formulas from memory.
3. Rebuild one one-way and one randomized-block ANOVA table.
4. Run one Pearson/regression and one SES/Holt table.
5. Recite GMM density, responsibility and EM steps.
6. Tab watermark viewer pp. 86, 102, 120, 125, 134, 149, 161, 173 and 194.
7. Review errors only; do not start a long new ARIMA derivation.

## Exam-hall strategy

### First 8 minutes

Scan every question. Mark `A` (direct), `B` (known but long), `C` (reference needed). Identify tail/test/model before calculating.

### Time budget for 150 minutes

- 8 min scan and ordering.
- About 125 min writing, proportional to marks (`~3 min/mark` as an upper guide).
- 17 min buffer/check/reference recovery.

### During writing

- Start with a high-confidence calculation.
- Put assumptions before the statistic, as the paper requests.
- Preserve intermediate work for method marks.
- If arithmetic stalls, write the correct formula/table and proceed.
- Use the watermark for verification, not discovery; stop searching after roughly 45 seconds and write what you know.
- Box the numeric result and add a contextual sentence.

### Final check

Check tail, df, forecast index, variance divisor, units, and whether every statistical decision has a contextual conclusion.


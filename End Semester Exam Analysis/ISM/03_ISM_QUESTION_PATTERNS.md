# ISM Question Patterns and Attack Templates

## Pattern 1 - Choose and execute a mean test

**Priority:** MUST DO | **Difficulty:** medium | **Evidence:** all three newest EC-3 sittings  
**Representative:** [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q1(a), 3 marks.

- Typical wording: “test whether A is higher,” “evaluate the claimed mean,” “does the intervention improve?”
- Examiner tests: parameter definition, paired/independent choice, tail, standard error and contextual decision.
- Identify: paired observations -> differences; known sigma -> z; independent samples -> Welch t; otherwise one-sample t.
- Solve: `H0/H1 -> assumptions -> statistic/df -> p or critical -> decision -> sentence in context`.
- Trap: using a two-sided test when “higher/improves/underfills” defines one side; using independent t for paired data.

## Pattern 2 - Two proportions

**Priority:** MUST DO | **Difficulty:** easy-medium  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q8(a), 3 marks.

- Typical wording: “significant difference between proportions.”
- Formula: pool under `H0: p1=p2`; `z=(p1-p2)/sqrt[p(1-p)(1/n1+1/n2)]`.
- Output: sample proportions, pooled proportion, SE, z, decision, substantive conclusion.
- Trap: using unpooled SE for the equality test or omitting the two-sided alternative.

## Pattern 3 - Confidence interval and interpretation

**Priority:** HIGH | **Difficulty:** easy  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q7(a), 2 marks.

- Identify z versus t from whether population sigma is known.
- Show `estimate +/- critical x SE` and both endpoints.
- Interpret the population mean, not individual observations.
- Trap: saying “95% probability that mu lies in this computed interval.”

## Pattern 4 - Chi-square independence

**Priority:** HIGH | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q2, 5 marks.

- Typical wording: “does category A influence/associate with category B?”
- Construct observed table, row/column totals, expected table, cell contributions.
- Formula: `E=RC/N`, `chi2=sum(O-E)^2/E`, df `(r-1)(c-1)`.
- Trap: denominator must be expected count; association is not causal influence.

## Pattern 5 - Variance F-test

**Priority:** HIGH | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q8(b), 2 marks.

- Typical wording: “A exhibits greater variability than B.”
- Use `H1:sigmaA^2>sigmaB^2`, `F=sA^2/sB^2`, df `(nA-1,nB-1)`, upper tail.
- State normality and independence.
- Trap: putting the larger sample variance on top automatically rather than following the directional hypothesis.

## Pattern 6 - One-way ANOVA

**Priority:** MUST DO | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q8, 5 marks.

- Typical wording: “do three methods have different means?”
- Examiner expects an ANOVA table: source, SS, df, MS, F.
- Solve: group/grand means -> `SSB`, `SSW` -> df -> MS -> F -> decision.
- Trap: concluding which groups differ; omnibus ANOVA only establishes at least one difference unless a post-hoc test is performed.

## Pattern 7 - Randomized-block/two-way ANOVA

**Priority:** MUST DO | **Difficulty:** medium-hard  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q4, 5 marks.

- Typical wording: treatments repeated once across blocks; “assume no interaction.”
- Separate treatment, block and error sums of squares; test treatment and block hypotheses separately.
- Trap: applying one-way ANOVA and ignoring blocks.
- Special trap in the actual paper: its data give `SSE=0`; formal F ratios divide by zero. State the degeneracy rather than fabricating a finite statistic.

## Pattern 8 - Pearson correlation

**Priority:** MUST DO | **Difficulty:** easy  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q1, 5 marks.

- Build a compact deviation table: `dx,dy,dx^2,dy^2,dxdy`.
- Formula: `r=Sxy/sqrt(SxxSyy)`.
- Interpret sign, strength and context; do not claim causality.
- Trap: covariance retains units; Pearson `r` is unitless and bounded.

## Pattern 9 - Regression, prediction and adequacy

**Priority:** MUST DO | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q5, 5 marks.

- Compute `b1=Sxy/Sxx`, `b0=ybar-b1xbar`, then predict.
- Discuss residual shape, range of observed X, saturation/nonlinearity and domain constraints.
- For a practical optimum, distinguish “best fitted prediction” from a scientifically feasible decision.
- Trap: using `r` as slope; extrapolating beyond observed data; calling high `R^2` causal.

## Pattern 10 - Simple exponential smoothing

**Priority:** MUST DO | **Difficulty:** easy-medium  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q2, 5 marks.

- Table: period, actual `Yt`, current forecast `Ft`, next forecast `F(t+1)`, error.
- Formula: `F(t+1)=alpha Yt+(1-alpha)Ft`.
- Compare alphas by MSE when enough errors exist; otherwise explain responsiveness.
- Trap: using `Yt` to forecast the same period rather than the next; comparing MSE on unequal periods.

## Pattern 11 - Moving average or Holt trend

**Priority:** MUST DO | **Difficulty:** medium  
**Representatives:** [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q3 and Q6, 5 marks each.

- Moving average: average latest `k` actuals for next period.
- Holt: update level and trend at every period, then `F(t+h)=Lt+hTt`.
- Use Holt for trend without seasonality; SES/MA lag systematic trend.
- Trap: centred moving average describes a historical trend but cannot directly forecast the next period without future values.

## Pattern 12 - Autocorrelation and white-noise diagnosis

**Priority:** HIGH | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q4, exact marks not printed beside the extracted prompt (paper: 8 questions/40 marks).

- Calculate deviations from the overall mean and lag product sum.
- State the autocorrelation convention because denominator conventions vary.
- A positive high `r1` suggests persistence, but trend itself can create large autocorrelation.
- White noise requires zero mean, stable variance and no autocorrelation; a tiny list cannot prove all three.

## Pattern 13 - MLE

**Priority:** SHOULD DO | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 06-Sep-2025 EC-3 Regular, Q5(b), 4 marks.

- Input -> distribution -> likelihood -> log -> derivative -> estimator -> requested plug-in probability.
- Standard shortcut: Poisson MLE is sample mean.
- Trap: using unbiased sample corrections where the question asks MLE.

## Pattern 14 - GMM and EM

**Priority:** HIGH | **Difficulty:** medium  
**Representative:** [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q6, 5 marks.

- Write mixture density first.
- Hard-labelled groups: estimate component mean, ML variance and mixing fraction.
- Unknown memberships: E-step responsibilities, M-step weighted parameter updates.
- Explain why a mixture represents multimodality/heterogeneity better than one Gaussian.
- Trap: variance divisor `n_k-1` instead of ML divisor `n_k`; weights not summing to one.

## Pattern 15 - ARIMA-family concept comparison

**Priority:** SHOULD DO | **Difficulty:** medium-hard  
**Representative:** [ORIGINAL PRACTICE] no verified recent long-derivation PYQ.

**Question.** Explain what ARIMA(1,1,1) means and distinguish SARIMAX from VAR.

**Answer template.** ARIMA(1,1,1) applies one difference, then models the differenced series with one AR lag and one MA error lag. SARIMAX has one target with seasonal ARIMA dynamics plus external predictors; VAR jointly models several endogenous series through their lags. State stationarity/differencing and one use case. Do not attempt a long derivation unless marks justify it.

## Numerical attack template

```text
GIVEN: copy values, parameter and alpha.
REQUIRED: name the estimate/test/forecast.
METHOD: state why this formula/test applies and assumptions.
FORMULA: write symbols before numbers.
SUBSTITUTION: preserve enough precision.
INTERMEDIATE WORK: table, df, expected counts, sums of squares, etc.
DECISION: compare p/critical or state forecast.
INTERPRETATION: one sentence in the problem's units/context.
```

## Conceptual answer templates

### “Explain X”

Definition -> mechanism/equation -> assumptions -> key property -> appropriate use -> limitation.

### “Compare A and B”

Compare objective, assumptions, update equation, data pattern handled and failure mode. End with a selection rule.

### “Justify the model/decision”

Claim -> numerical evidence -> assumption/diagnostic -> practical constraint -> bounded conclusion.

### “Interpret the result”

Statistic direction/magnitude -> decision uncertainty -> units/context -> what cannot be concluded.

### “Describe an algorithm”

Input -> initialization -> repeated calculation -> stopping criterion -> output -> one limitation.

### “Draw/describe architecture”

Label data/input, parameter components, direction of flow and output; attach one sentence to every arrow/block. For GMM/EM: data -> responsibilities -> weighted parameter updates -> convergence.

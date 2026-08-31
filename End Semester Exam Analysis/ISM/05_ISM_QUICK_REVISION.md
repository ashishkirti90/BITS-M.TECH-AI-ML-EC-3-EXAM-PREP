# ISM Quick Revision and Exam-Day Sheet

## If only 5 days remain

| Day | ISM block | Output |
|---|---|---|
| 1 | 2.5 h: CI, one-mean, paired and two-sample tests | test-selection tree + Feb/Mar inference PYQs |
| 2 | 2.5 h: correlation and regression | both latest regression questions without notes |
| 3 | 2.5 h: SES, moving average and Holt | three complete forecast tables |
| 4 | 2.5 h: chi-square, F and ANOVA | Mar Q2/Q8 + Feb Q4 trap |
| 5 | 3.0 h: GMM/MLE, ACF/residuals, timed mixed redo | six must-practice questions + error log |

Optional 1.5 h safety pass: Bayes, joint distributions, binomial/Poisson/normal.

## 60-second test selector

```text
Same units measured twice?           paired t
One mean vs claim, sigma known?      one-sample z
One mean vs claim, sigma unknown?    one-sample t
Two independent means?               Welch t
Two proportions?                     pooled two-proportion z
Categorical count association?       chi-square
Three or more means?                 ANOVA
Treatments repeated over blocks?     randomized-block ANOVA
Compare variances, normal data?       F-test
Two quantitative variables?          Pearson/regression
Stable-level forecast?               MA/SES
Trend, no seasonality?                Holt
Multimodal continuous data?           GMM
```

## Formula flash list

- CI: `estimate +/- critical x SE`.
- z mean: `(xbar-mu0)/(sigma/sqrt(n))`.
- paired t: `dbar/(sd/sqrt(n))`.
- Welch: `(xbar1-xbar2)/sqrt(s1^2/n1+s2^2/n2)`.
- two proportions: pool under H0.
- chi-square: `E=RC/N`; `sum(O-E)^2/E`.
- F variance: ratio in the direction of `H1`.
- one-way ANOVA: `F=MSbetween/MSwithin`.
- Pearson: `r=Sxy/sqrt(SxxSyy)`.
- regression: `b1=Sxy/Sxx`, `b0=ybar-b1xbar`.
- SES: `F(t+1)=alpha Yt+(1-alpha)Ft`.
- Holt: level, trend, then `F(t+h)=Lt+hTt`.
- Poisson MLE: `lambda_hat=xbar`.
- GMM: `p(x)=sum pi_k N_k`; responsibility is weighted component density divided by total density.

## Topic one-minute revisions

### Inference

Tail comes from wording. Standardize the estimate’s distance from H0 by its SE. Reject only when the result is sufficiently extreme. Report df and context. “Fail to reject” is not proof.

### CI

Known sigma -> z; unknown sigma -> t. Larger confidence widens; larger n narrows. Interpret the population parameter, not individual data.

### Chi-square/F/ANOVA

Chi-square uses expected counts. F-tests compare variance ratios and assume normality. ANOVA partitions total variation; rejection means at least one mean differs. Blocking removes nuisance variability.

### Correlation/regression

`r` gives linear association, slope gives response change per X unit, `R^2` gives explained sample variation. Check residual/scatter shape. Never claim causation from fit.

### Forecasting

MA/SES handle level; Holt handles trend. Larger alpha reacts faster. Compare models on common-period MSE. SES index is always next-period forecast.

### ACF/ARIMA

Autocorrelation is a series related to its lag. Trend can inflate it. ARIMA `(p,d,q)` = AR lags, differences, MA error lags. Residuals should resemble white noise.

### MLE/GMM/EM

Likelihood -> log -> derivative -> solve. GMM weights Gaussian subpopulations. E-step responsibilities; M-step weighted parameters. EM can reach a local optimum.

## Ten traps to catch before submitting

1. Wrong tail for “higher/lower/different.”
2. Independent test used on paired data.
3. “Accept/prove H0.”
4. Expected count missing in chi-square denominator.
5. Variance F numerator chosen only because it is larger.
6. ANOVA df/source rows mismatched.
7. Pearson `r` used as regression slope.
8. SES off by one period.
9. GMM variance divided by `n_k-1` when ML is requested.
10. Zero mean residuals called white noise without checking correlation/variance.

## Six questions to redo cold

1. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q2, 5 marks - two-alpha SES.
2. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q5, 5 marks - regression and adequacy.
3. [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q8, 5 marks - proportions plus F.
4. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q2, 5 marks - chi-square.
5. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q6, 5 marks - Holt.
6. [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q8, 5 marks - one-way ANOVA.

## Final 24 hours

- 90 min: write formulas/test tree from memory and correct in another colour.
- 120 min: redo the six questions above, timed.
- 60 min: ANOVA and forecast-table arithmetic check.
- 45 min: GMM/MLE/white-noise concepts.
- 30 min: probability/distribution safety scan.
- 30 min: tab watermark pages and test lookup speed.
- Final pass: error log only; no large new topic.

## Watermark fast index

```text
CI / CLT                      86-101
Tests / chi-square            102-119
MLE                           120-125
ANOVA                         125-133
Correlation / regression      134-148
Moving averages               149-160
ACF / ARIMA                   161-172
SES / Holt                    173-185
Advanced time series          186-193
GMM / EM                      194-203
```

These are PDF viewer pages; each contains four reduced lecture slides.

## Exam-hall checklist

- [ ] Scan and rank questions before writing.
- [ ] State assumptions before calculation.
- [ ] Budget roughly 3 minutes per mark, retaining a 15-minute check buffer.
- [ ] Show intermediate values for partial credit.
- [ ] Stop an unproductive lookup after about 45 seconds.
- [ ] Box result with units.
- [ ] Add one contextual conclusion.
- [ ] Check tail, df, forecast index and variance divisor.

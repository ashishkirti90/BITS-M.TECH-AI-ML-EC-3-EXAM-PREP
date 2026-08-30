# ISM End-Sem Study Guide

## Official syllabus map

Sessions 1–2 descriptive statistics/probability; 3–4 conditional probability/Bayes/Naive Bayes; 5–6 random variables and distributions; 7 sampling/CLT/interval estimation; 9 hypothesis tests; 10 MLE and one/two-way ANOVA; 11 correlation/regression; 12 moving averages; 13 AR/ARMA/ARIMA; 14 SARIMA/SARIMAX/VAR/VARMAX/SES; 15 GMM/EM. Comprehensive is all sessions, open book, 40%, 150 minutes.

## Priority map

| Topic | Priority | Evidence | Form | Difficulty | Action |
|---|---|---|---|---|---|
| Hypothesis-test selection and computation | 🔴 | both 2026; 2023 regular/makeup | numerical + conclusion | medium | master z/t, independent/paired, proportions; write assumptions and decision |
| Correlation + linear regression | 🔴 | every identifiable 2023–26 sitting; both 2026 | calculation/interpret | easy-medium | r, slope/intercept, prediction, SSE, significance meaning |
| Forecasting/time series | 🔴 | every identifiable sitting; both 2026 | forecast table + compare | medium | SES, moving average, Holt trend, residual white noise; identify when model fits |
| Confidence intervals/CLT | 🟠 | both 2026 | numerical | easy | z vs t, margin of error, interpretation |
| ANOVA | 🔴 | latest original regular has a 5-mark randomized-block/two-way problem; Mar-2026 makeup has one-way ANOVA | table/test | medium-hard | one-way and two-way without replication; treatments, blocks, error, assumptions |
| Chi-square and variance F-test | 🟠 | Mar-2026 makeup chi-square; latest regular has a directional two-variance F-test | table/test | medium | independence expected counts; choose numerator/tail for variance claim |
| GMM/EM | 🟠 | Feb-2026 regular; official session 15 | density/responsibility + why | medium | mixture pdf, posterior membership, bimodality rationale |
| Probability/Bayes/distributions | 🟡 | older frequent; one latest signal | numerical | easy-medium | conditional probability, total probability, binomial/Poisson/normal basics |
| MLE | 🟢 | official; explicit older evidence only | derivation | medium | likelihood/log-likelihood recipe; Bernoulli/normal mean examples |
| ARIMA-family derivations | 🟢 | syllabus but recent papers favor basic forecasting | identification/prose | hard | know `(p,d,q)` meaning and stationarity/differencing; skip long derivations |

### Cross-paper frequency (5 identifiable 2023–2026 sittings)

| Topic family | Paper presence | Mode | Typical marks |
|---|---:|---|---:|
| Correlation/regression | 5/5 | numerical + interpretation | 5–10 |
| Forecasting/time series | 5/5 | numerical/model comparison | 5–10 |
| Hypothesis testing | 4/5 | numerical + conclusion | 5–10 |
| Probability/distributions | 4/5 | numerical | 4–6 |
| Confidence intervals | 2/5, both 2026 | numerical | 2–5 |
| ANOVA | 3/5 | one-way or randomized-block calculation | 5 |
| Chi-square / variance F | 2/5 and 1/5 respectively | numerical/test selection | 2–5 |
| GMM | 1/5, latest regular | density/concept | 4–6 |
| MLE | 1/5 | derivation | 4–5 |

Paper presence is intentionally not raw question count; multiple subparts in one sitting count once.

## Recent paper signal

- **Mar-2026 makeup:** two-sample testing/CI, chi-square independence, one-sample mean test, trend forecasting, correlation/regression, one-way ANOVA. The paper heavily tests choosing and executing standard methods.
- **Latest original regular (28 Feb 2026):** eight equal 5-mark blocks: Pearson correlation; SES with two alphas; paired t plus one-sample z; randomized-block/two-way ANOVA without interaction; simple regression plus model adequacy/water-efficiency reasoning; two-component GMM estimation; confidence interval plus white-noise residual check; two-proportion z plus directional F-test for variances.
- **Stable across both:** inference + regression + forecasting. These are the strongest high-probability patterns.
- **Less recent:** pure probability puzzles remain possible because all sessions are in scope, but their priority falls below inference/forecasting. Complex SARIMAX/VAR derivation has insufficient recent PYQ evidence.

## Test-selection tree

1. Outcome categorical counts vs categories? **Chi-square**.
2. Compare 3+ group means? **ANOVA**.
3. Compare means:
   - same subjects before/after -> **paired t**;
   - two independent groups -> **two-sample t/z**;
   - one sample vs claimed mean -> **one-sample t/z**.
4. Compare proportions -> **proportion z test**.
5. Relationship of two quantitative variables -> **Pearson correlation/regression**.

Use z when population sigma is known or the stated large-sample setup warrants it; use t when sigma is unknown, especially small samples. State assumptions.

## Core methods from zero

### Hypothesis testing

Start with a claim about a population. `H0` is the status quo/equality. Compute how many standard errors the sample lies from H0. If the statistic is too extreme (or p < alpha), reject H0. “Fail to reject” is not “prove H0.” Always finish in context.

Template:

1. Define parameter and H0/H1.
2. State alpha and test/assumptions.
3. Calculate statistic and degrees of freedom.
4. Critical value or p-value.
5. Decision.
6. Contextual conclusion.

### Correlation/regression

Correlation measures strength/direction of a linear relationship and is unitless; regression constructs a predictive line. A high `r` does not establish causality. `R^2` is the proportion of response variance explained by the fitted line in simple regression.

### Forecasting

- Moving average smooths the latest window; suitable for stable level.
- SES recursively blends latest actual and prior forecast; larger alpha reacts faster.
- Holt adds a trend state; use when data trends but lacks seasonality.
- White-noise residuals should fluctuate around zero with constant variance and no autocorrelation.

### GMM

A GMM models data as a weighted sum of Gaussian subpopulations. Unlike k-means, membership is probabilistic and components can have different variance/covariance.

## Worked patterns

### Pattern 1: One-sample mean test

Wording: “Machine claims mean 500 g; n=81, xbar=496, known historical sigma; test at 5%.”

Approach: `H0:mu=500`; choose z if sigma known; compute `z=(496-500)/(sigma/9)`; compare two/one-sided critical value as wording dictates; conclude about the filling claim.

Reference: **Mar-2026 makeup Q5**. Difficulty medium, 🔴.

### Pattern 2: Paired before/after

Compute differences `d_i=after-before`, then `dbar`, `s_d`, `t=dbar/(s_d/sqrt(n))`, df `n-1`. Do not use an independent-samples test.

Reference: **Feb-2026 regular Q3(a)**. Difficulty medium, 🔴.

### Pattern 3: Pearson + regression

Create columns `dx`, `dy`, `dx^2`, `dy^2`, `dxdy`; compute `r`. Then `b1=Sxy/Sxx`, `b0=ybar-b1xbar`, predict.

Representative: **Feb-2026 regular Q1 and regression block**; **Mar-2026 makeup Q7**. Difficulty easy-medium, 🔴.

Mini-example: x=[1,2,3], y=[2,4,5]. `xbar=2`, `ybar=11/3`; `Sxx=2`, `Sxy=3`, so slope=1.5 and intercept=2/3.

### Pattern 4: SES forecast table

Set initial forecast as instructed. For each t, `F_{t+1}=alpha Y_t+(1-alpha)F_t`. Maintain columns Period, Actual, Forecast, Error. Calculate through the requested future period.

Reference: **Feb-2026 regular Q2**, which asks two alpha values. Difficulty easy, 🔴.

### Pattern 5: Chi-square independence

Compute row/column totals; `E_ij=R_i C_j/N`; sum `(O-E)^2/E`; df `(r-1)(c-1)`; decide association.

Reference: **Mar-2026 makeup Q2** and 2023 makeup player-performance association. Difficulty medium, 🟠.

### Pattern 6: One-way ANOVA

`SSB=sum n_j(xbar_j-xbar)^2`; `SSW=sum sum(x_ij-xbar_j)^2`; df `k-1,N-k`; `F=(SSB/(k-1))/(SSW/(N-k))`.

Reference: **Mar-2026 makeup Q8**. Difficulty medium, 🟠.

### Pattern 6B: Randomized-block/two-way ANOVA without replication

Build a treatment-by-block table. Compute correction factor `CF=T^2/N`, total SS, treatment SS from row totals, block SS from column totals, and `SSE=SST-SSTreat-SSBlock`. Use df: treatments `a-1`, blocks `b-1`, error `(a-1)(b-1)`. Test treatment and block effects separately.

Reference: **latest original regular (28 Feb 2026), irrigation-method/orchard-block question**, 5 marks. Difficulty medium-hard, 🔴.

### Pattern 6C: Compare two variances

For “Line A has greater variability,” use `H1:sigma_A^2>sigma_B^2` and `F=s_A^2/s_B^2`; df `(n_A-1,n_B-1)`; compare with upper-tail critical value. State normality assumption.

Reference: **latest original regular final subpart**, 2 marks. Difficulty medium, 🟠.

### Pattern 7: GMM density/posterior

Given `(pi_k,mu_k,sigma_k^2)`, evaluate each weighted density `a_k=pi_k N(x|mu_k,sigma_k^2)`. Mixture density is `sum a_k`; responsibility is `a_k/sum a_j`.

Reference: **Feb-2026 regular GMM question**. Difficulty medium, 🟠.

## Definitions to memorize

- p-value: probability under H0 of a statistic at least as extreme as observed.
- Confidence interval: procedure that captures the true parameter in the stated fraction of repeated samples.
- Type I error: reject true H0; Type II: fail to reject false H0.
- Stationarity: stable distributional properties over time (commonly mean/variance/autocovariance).
- White noise: zero-mean, constant-variance, uncorrelated sequence.
- Autocorrelation: correlation of a series with lagged values.

## Common mistakes

- Choosing independent t for paired data.
- Using sample SD where the formula assumes population sigma without explaining.
- Omitting tails in critical values.
- Saying “accept H0.”
- Computing regression before centering sums correctly.
- SES off-by-one: using current actual to forecast the same period.
- Comparing raw chi-square cells without expected counts.
- Forgetting weights sum to one in GMM.

## What to memorize vs look up

Memorize the test-selection tree, core statistics, regression and SES recursion. Understand assumptions and conclusion wording. Look up critical values, distribution tables, detailed ANOVA layout, ARIMA diagnostic rules and long GMM density constants. Tab one worked example per test.

The authorized `ISM watermark.pdf` is 261 pages: excellent examples but too large for browsing. Tab only the test-selection material, correlation/regression, SES/Holt, ANOVA/chi-square/F-test and GMM sections.

## Final checklist

- [ ] Name correct test in 30 seconds.
- [ ] Complete z/t/paired/proportion test with conclusion.
- [ ] Pearson + regression + prediction.
- [ ] SES and Holt forecast tables.
- [ ] Chi-square and one-way ANOVA.
- [ ] Randomized-block/two-way ANOVA and directional F-test for variances.
- [ ] GMM density/responsibility.
- [ ] Explain ARIMA `(p,d,q)` and white-noise residuals.
- [ ] Solve both 2026 papers’ core numericals.

# ISM End-Sem Question Bank

**Course:** Introduction to Statistical Methods  
**Scope:** Comprehensive/end-semester examination  
**Format:** 20 core solved questions + 5 latest-paper gap-closing questions  
**Evidence:** Official course handout, audited repository material, and verified recent-paper structures

---

## How to use this bank

- Attempt every question before reading its solution.
- Prioritize items labelled MUST DO and latest-paper pattern.
- The numerical values in original drills are practice values; a PYQ-pattern label refers to verified structure, not a claim of verbatim reproduction.
- After each error, bookmark the matching worked example in the authorized watermarked slides.

---

## ISM — 20 solved questions

### ISM 1 — Conditional probability and Bayes [SHOULD DO | Syllabus coverage]

**Question.** Disease prevalence is 1%, sensitivity 95%, specificity 90%. Find `P(disease|positive)`.

**Solution.** `P(+)=.95(.01)+.10(.99)=.1085`. Bayes gives `.0095/.1085=.0876`. Despite good sensitivity, most positives are false because prevalence is low. **Trap:** do not confuse `P(+|D)` with `P(D|+)`.

### ISM 2 — Binomial distribution [SHOULD DO | Older recurring]

**Question.** If defect probability is `.1`, find probability of exactly two defects among five independent items.

**Solution.** `P(X=2)=C(5,2)(.1)^2(.9)^3=10(.01)(.729)=.0729`. Conditions: fixed trials, independent, two outcomes, constant probability.

### ISM 3 — CLT and standard error [HIGH | 2026 CI signal]

**Question.** A population has mean 50, SD 12. For `n=36`, approximate `P(48<sample mean<52)`.

**Solution.** By CLT, standard error `12/sqrt36=2`. Z bounds are `-1,+1`, so probability `Phi(1)-Phi(-1)=.6827`. CLT concerns the sampling distribution of the mean, not individual observations.

### ISM 4 — Confidence interval [HIGH | Both 2026]

**Question.** `n=100`, mean 20, known SD 5. Find a 95% CI for the population mean.

**Solution.** `20 ±1.96(5/sqrt100)=20±.98`, so `(19.02,20.98)`. Interpretation: the method captures the fixed population mean in 95% of repeated samples; it is not a 95% probability statement about this already-computed fixed interval.

### ISM 5 — One-sample z test [MUST DO | Latest papers]

**Question.** Test `H0:mu=100` vs `H1:mu<100` with `n=64`, mean 98, known SD 8, `alpha=.05`.

**Solution.** `z=(98-100)/(8/8)=-2`. Lower critical value `-1.645`; reject H0. There is evidence the mean is below 100. The one-sided p-value is about `.0228`. State the alternative before seeing the statistic.

### ISM 6 — One-sample t test [MUST DO | Mar-2026 pattern]

**Question.** `n=16`, mean 52, sample SD 4; test `mu=50` two-sided at 5%.

**Solution.** `t=(52-50)/(4/4)=2`, df 15. Critical magnitude is about 2.131, so fail to reject H0. Evidence is insufficient at 5%, even though the sample mean differs numerically.

### ISM 7 — Paired t test [MUST DO | Feb-2026 Q3]

**Question.** Before–after differences are `2,3,1,2,2`. Test whether mean improvement is positive.

**Solution.** Mean difference `2`; deviations `0,1,-1,0,0`, so sample variance `2/4=.5`, `s=.7071`. `SE=.7071/sqrt5=.3162`; `t=6.325`, df 4. This strongly supports positive improvement. Pair first, then analyze differences; never treat paired observations as independent samples.

### ISM 8 — Two independent means [MUST DO | Mar-2026 makeup]

**Question.** Two large independent samples: `n1=n2=50`, means 75 and 72, SDs 5 and 4. Test equality two-sided.

**Solution.** `SE=sqrt(25/50+16/50)=sqrt(.82)=.9055`; statistic `z≈3.313`. Since `|z|>1.96`, reject equality. A Welch t procedure is safer for smaller samples/unknown unequal variances.

### ISM 9 — Two proportions [MUST DO | Latest regular]

**Question.** Group 1 has 60 successes/100; group 2 has 45/100. Test equal proportions at 5%.

**Solution.** Pooled `p=(60+45)/200=.525`. `SE=sqrt(.525(.475)(.01+.01))=.07062`. `z=.15/.07062=2.124`, so reject two-sided at 5%. Pool under the null for the hypothesis test; unpooled SE is used for a confidence interval.

### ISM 10 — Chi-square independence [HIGH | Mar-2026 makeup]

**Question.** Observed table is `[[30,20],[20,30]]`. Test independence.

**Solution.** Every row and column total is 50; `N=100`, so all expected cells are 25. `chi²=4*(5²/25)=4`, df 1. Since 4>3.841, reject independence at 5%. Expected counts, not observed counts, go in the denominator.

### ISM 11 — Variance F test [HIGH | Latest regular]

**Question.** Test whether A is more variable than B: `sA²=16,nA=10`; `sB²=9,nB=12`.

**Solution.** `H1:sigmaA²>sigmaB²`; use `F=16/9=1.778`, df `(9,11)`, and compare with the **upper-tail** critical value from the permitted table. Do not automatically place the larger variance on top if the directional claim specifies the numerator; follow H1. Assume normal populations.

### ISM 12 — Pearson correlation [MUST DO | Every recent sitting]

**Question.** For `x=(1,2,3)`, `y=(2,4,5)`, find `r`.

**Solution.** Means are 2 and `11/3`. `Sxx=2`, `Syy=14/3`, `Sxy=3`. Thus `r=3/sqrt(2*14/3)=.982`. It indicates strong positive linear association, not causation.

### ISM 13 — Simple regression [MUST DO | Both 2026]

**Question.** Fit `y=b0+b1x` to the data in Q12 and predict at `x=4`.

**Solution.** `b1=Sxy/Sxx=1.5`; `b0=ybar-b1*xbar=11/3-3=2/3`. Prediction is `2/3+1.5(4)=6.667`. Do not use `r` itself as the slope unless standard deviations are equal.

### ISM 14 — One-way ANOVA [MUST DO | Mar-2026 makeup]

**Question.** Groups are A:`{1,2,3}`, B:`{4,5,6}`. Compute ANOVA F.

**Solution.** Group means 2 and 5; grand mean 3.5. Between SS `3(2-3.5)^2+3(5-3.5)^2=13.5`. Within SS is `(1+0+1)+(1+0+1)=4`. df `(1,4)`; `MSB=13.5`, `MSW=1`, so `F=13.5`. Compare with table and conclude group effect if significant.

### ISM 15 — Randomized-block ANOVA [MUST DO | Latest regular]

**Question.** Treatments A/B across three blocks are A:`8,9,7`, B:`5,6,4`. Explain the test calculation.

**Solution.** `N=6`, total `T=39`, correction `CF=T²/N=253.5`; total SS `sum x²-CF=271-253.5=17.5`. Treatment totals 24,15: `SS_tr=(24²+15²)/3-CF=13.5`. Block totals 13,15,11: `SS_bl=(13²+15²+11²)/2-CF=4`. Error SS `0`. Here treatment difference is perfectly constant across blocks, causing zero error and an effectively infinite treatment F; in real data nonzero error is expected. df treatment 1, blocks 2, error 2.

### ISM 16 — Moving average [MUST DO | Recurring forecasting]

**Question.** Values are `10,12,14,16,18`. Give the three-period forecast for period 6.

**Solution.** Average the latest three actuals: `(14+16+18)/3=16`. A moving average lags a trend; widening the window smooths more but reacts more slowly.

### ISM 17 — Simple exponential smoothing [MUST DO | Latest regular]

**Question.** Actuals are `10,14,13`; initial `F2=10`, `alpha=.5`. Find `F3,F4`.

**Solution.** `F3=.5Y2+.5F2=.5(14)+.5(10)=12`; `F4=.5Y3+.5F3=.5(13)+.5(12)=12.5`. Higher alpha reacts faster to recent observations. Maintain a period/actual/forecast/error table to prevent indexing mistakes.

### ISM 18 — Holt trend [HIGH | Forecasting family]

**Question.** State one Holt update and when to use it.

**Solution.** One convention: `L_t=alpha y_t+(1-alpha)(L_{t-1}+B_{t-1})`; `B_t=beta(L_t-L_{t-1})+(1-beta)B_{t-1}`; `h`-step forecast `L_t+hB_t`. Use for a trending, nonseasonal series. State initialization and convention because texts vary.

### ISM 19 — White-noise residual diagnosis and ARIMA [MUST/HIGH | 2026 + syllabus]

**Question.** Residual ACF has a large significant spike at lag 1. Is the model adequate? What does ARIMA(1,1,1) mean?

**Solution.** No: residual autocorrelation means predictable structure remains; residuals should resemble zero-mean, constant-variance, uncorrelated noise. ARIMA(1,1,1) uses one AR term, first differencing, and one MA error term. Do not confuse MA in ARIMA with a simple moving-average forecast.

### ISM 20 — GMM responsibility and MLE [HIGH | Latest regular + syllabus]

**Question.** Two Gaussian components at a point have densities `.2,.1` and weights `.6,.4`. Find posterior responsibility for component 1. Also state the Bernoulli MLE.

**Solution.** Weighted terms are `.12` and `.04`; responsibility `gamma1=.12/.16=.75`, `gamma2=.25`. EM uses these soft memberships in its M-step. For Bernoulli observations, log-likelihood differentiation gives `p_hat=(sum x_i)/n`, the sample proportion.

---

# Latest-paper gap closure

## ISM — five gap-closing questions

### 6. Complete two-component GMM estimates

**Latest-paper link:** ISM latest regular GMM block.

**Question.** Component 1 observations are `{2,4,6}` and component 2 observations `{10,12}`. Using maximum-likelihood variance with divisor `n`, calculate means, variances and mixing coefficients.

**Solution.** `mu1=(2+4+6)/3=4`; squared deviations `4,0,4`, so `sigma1²=8/3=2.6667`. `mu2=11`; squared deviations `1,1`, so `sigma2²=2/2=1`. Total `N=5`, hence `pi1=3/5=.6`, `pi2=2/5=.4`. The fitted density is

`p(x)=.6 N(x|4,8/3)+.4 N(x|11,1)`.

**Trap:** GMM M-step uses ML variance divisor/effective count, not the unbiased sample divisor, unless the question explicitly asks sample variance.

### 7. Residual mean, variance and white noise

**Latest-paper link:** ISM latest regular residual block.

**Question.** Residuals are `{2,-1,0,1,-2,1,-1,0}`. Calculate mean and sample variance. Can white noise be concluded?

**Solution.** Sum is 0, so mean is 0. Sum of squared deviations is `4+1+0+1+4+1+1+0=12`. Sample variance is `12/(8-1)=12/7=1.7143`; population-style variance would be `12/8=1.5`, so state the convention. Zero mean and finite variance are consistent with white noise, but do not prove it. Inspect residual plot/ACF or apply a Ljung–Box-type check; white noise also requires no serial correlation and stable variance.

### 8. Full simple regression and adequacy

**Latest-paper link:** ISM latest regular irrigation regression block.

**Question.** Fit a line to `(x,y)={(1,2),(2,4),(3,5),(4,5)}`. Predict at x=3.5 and comment on adequacy if a residual plot bends systematically.

**Solution.** `xbar=2.5`, `ybar=4`. `Sxx=5`; `Sxy=(-1.5)(-2)+(-.5)(0)+(.5)(1)+(1.5)(1)=5`. Thus `b1=1`, `b0=4-2.5=1.5`; fitted line `yhat=1.5+x`. At 3.5, prediction is 5. A curved residual pattern violates linear-form adequacy even if correlation is high; consider a nonlinear term or a scientifically meaningful saturation model. Never infer causality from fit alone.

### 9. Water-use efficiency reasoning

**Latest-paper link:** ISM latest regular regression application.

**Question.** A fitted yield model is `yhat=1+.5x`, where x is water input. Find predicted yield per unit water and explain whether the model alone gives a finite optimum.

**Solution.** Efficiency is `E(x)=yhat/x=(1+.5x)/x=1/x+.5`, which decreases as x increases for `x>0`. The algebra would favor the smallest x, but extrapolating toward zero is physically invalid and crops require a minimum water threshold. Choose among observed/feasible values using predicted efficiency, yield requirement, uncertainty, and agronomic constraints. This is the contextual reasoning the paper awards marks for.

### 10. Two-way randomized-block decision

**Latest-paper link:** ISM latest regular ANOVA block.

**Question.** In a randomized-block ANOVA, `MS_treatment=18`, `MS_block=7`, `MS_error=2`; critical F values are 4.0 and 3.5 respectively. State both decisions.

**Solution.** `F_treatment=18/2=9>4`, so reject equality of treatment means. `F_block=7/2=3.5`; if rejection requires strictly exceeding the tabulated value, it lies exactly on the boundary—report it as critical/borderline according to the table convention. Treatment and block hypotheses must be tested separately; the no-interaction design uses residual variation after removing both effects.

---

## Mastery test

A pattern is mastered only when you can identify the method within 20 seconds, write the governing formula without searching, complete the calculation accurately, state assumptions, interpret the result, and locate a backup example in the watermarked slides within 30 seconds.
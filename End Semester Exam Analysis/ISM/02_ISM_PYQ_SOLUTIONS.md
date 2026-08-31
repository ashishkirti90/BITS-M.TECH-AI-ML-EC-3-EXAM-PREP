# ISM High-Value PYQ Solution Bank

**Ordering:** newest papers first.  
**Answer depth:** inferred where a detailed marking split is unavailable.  
**Accuracy rule:** official question data control; all reported numericals below were independently recomputed.

## 1. [ACTUAL PYQ] Pearson correlation

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q1** | **5 marks**  
**ID:** ISM-01 | **Priority:** MUST DO | **Pattern:** Pearson calculation and contextual interpretation  
**Question.** For temperature `X={38,41,35,33,31}` and electricity use `Y={320,380,290,270,240}`, calculate Pearson `r` and interpret it.

**Solution.** `xbar=35.6`, `ybar=300`. From the deviation table,

`Sxx=sum(X-xbar)^2=63.2`, `Syy=sum(Y-ybar)^2=11000`, `Sxy=sum(X-xbar)(Y-ybar)=824`.

Therefore `r=824/sqrt(63.2*11000)=0.9896`.

**Final answer.** There is a very strong positive linear association: hotter months in this sample are associated with greater electricity use. This supports heat-sensitive load planning, but five monthly observations do not establish causation or a universal demand law.

**Exam-writing guidance:** formula + deviation sums + contextual interpretation earns the full five-mark shape.  
**Common mistake:** reporting “temperature causes demand” from correlation.  
**Watermark:** viewer pp. 134-143.

## 2. [ACTUAL PYQ] SES with two alphas

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q2** | **5 marks**  
**ID:** ISM-02 | **Priority:** MUST DO | **Pattern:** SES recursion and alpha comparison  
**Question.** Demand is `{82,88,91,97,95,102}` from Jan-Jun; initial Jan forecast is 82. Forecast July with `alpha=.4` and `.7`; select for sudden spikes.

**Solution.** Use `F_(t+1)=alpha Y_t+(1-alpha)F_t`.

For `alpha=.4`, successive next forecasts are `82, 84.4, 87.04, 91.024, 92.6144, 96.36864`; hence July `=96.37` thousand.

For `alpha=.7`, they are `82, 86.2, 89.56, 94.768, 94.9304, 99.87912`; hence July `=99.88` thousand.

**Final answer.** `alpha=.7` reacts more to the latest jump and is preferable if spikes are expected, though an error metric on held-out periods would be needed to claim better forecast accuracy.

**Exam-writing guidance:** show both recursive forecast sequences and finish with a one-sentence alpha comparison.  
**Common mistake:** using June actual to call the result the June forecast.  
**Watermark:** pp. 173-177.

## 3. [ACTUAL PYQ] Paired t plus claimed mean

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q3(a,b)** | **3+2 marks**
**ID:** ISM-03 | **Priority:** MUST DO | **Pattern:** paired t plus one-mean z and decision risk

### (a) Revision strategy

Differences `after-before={4,3,4,4,4,5}`. Test improvement.

`H0:mu_d=0`, `H1:mu_d>0`. Assume independent student differences and approximately normal differences. `dbar=4`, `s_d=sqrt(.4)=.6325`, so

`t=4/(.6325/sqrt6)=15.492`, df `5`. The 5% upper critical value is `2.015`; reject `H0`.

**Conclusion.** The sample provides strong evidence that the strategy improves mean scores.

### (b) Diagnosis-time claim

`H0:mu=20`, `H1:mu<20` (challenge to the claimed 20-minute reduction). Given `xbar=18.2`, known `sigma=7.5`, `n=36`:

`z=(18.2-20)/(7.5/6)=-1.44`.

Since `-1.44 > -1.645`, fail to reject `H0` at 5%. There is insufficient evidence that the true reduction is below 20 minutes. A Type II error here would mean deploying while missing a real shortfall; clinical decision-making should also consider effect size and safety, not this test alone.

**Exam-writing guidance:** separate the two subparts; for each, write hypotheses, statistic, critical comparison and a contextual conclusion.  
**Common mistake:** the repository key uses a two-sided t critical value for part (a) even though “improves” is directional.  
**Watermark:** pp. 102-119.

## 4. [ACTUAL PYQ] Randomized-block ANOVA and a degenerate dataset

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q4** | **5 marks**  
**ID:** ISM-04 | **Priority:** MUST DO | **Pattern:** randomized-block ANOVA  
**Question.** Three irrigation methods across four orchard blocks: Drip `{22,20,24,22}`, Sprinkler `{21,19,23,21}`, Flood `{18,16,20,18}`; no interaction.

**Solution.** `a=3`, `b=4`, `N=12`, grand total `T=244`; `CF=T^2/N=4961.3333`.

`SST=sum x^2-CF=58.6667`  
`SSTreat=(88^2+84^2+72^2)/4-CF=34.6667`  
Block totals are `61,55,67,61`; `SSBlock=sum B_j^2/3-CF=24.0000`  
`SSE=58.6667-34.6667-24=0`.

| Source | SS | df | MS | F |
|---|---:|---:|---:|---:|
| Irrigation | 34.6667 | 2 | 17.3333 | undefined (`/0`) |
| Blocks | 24.0000 | 3 | 8.0000 | undefined (`/0`) |
| Error | 0 | 6 | 0 | - |
| Total | 58.6667 | 11 | - | - |

**Final answer.** The values are perfectly additive: method differences are identical in every block, leaving no error estimate. A conventional randomized-block F-test cannot be completed because `MSE=0`. Report the method means (22, 21, 18) and block means descriptively, but do not fabricate a finite F or formal p-value. Replication or non-degenerate data are required.

**Evidence note:** the repository answer-key PDF substitutes a different one-way problem and therefore does not resolve this flaw.  
**Exam-writing guidance:** present the full source/SS/df/MS table and explicitly state why the F ratios are undefined.  
**Common mistake:** treating `SSE=0` as an ordinary significant result and inventing a finite F statistic.  
**Watermark:** pp. 129-133.

## 5. [ACTUAL PYQ] Regression, adequacy and water efficiency

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q5** | **5 marks**
**ID:** ISM-05 | **Priority:** MUST DO | **Pattern:** regression, adequacy and constrained decision

For the ten `(water input X, yield Y)` pairs, `xbar=3.99`, `ybar=2.24`, `Sxx=15.529`, `Sxy=6.354`.

`b1=6.354/15.529=.40917`; `b0=2.24-.40917(3.99)=.60741`.

**Fitted line:** `Yhat=.6074+.4092X`. At `X=4`, `Yhat=2.2441`. `R^2=.8953`, so the line explains about 89.5% of sample yield variation.

The positive line is broadly useful within the observed range, but the high-water observations flatten: at `X=6`, yield is only 2.7. Inspecting residuals/scatter suggests possible saturation.

Fitted efficiency is `Yhat/X=.6074/X+.4092`, which decreases with X. Thus the fitted line alone does **not** produce an interior optimum; strict yield-per-water favours the smallest feasible input. Observed ratios are best near `X=2.5` (`1.6/2.5=.64`), while roughly `3.0-4.5` gives a defensible yield/efficiency compromise if a minimum yield is imposed. State that agronomic constraints are required for a unique “optimal range.”

**Exam-writing guidance:** show `Sxx`, `Sxy`, both coefficients, one prediction and a bounded adequacy/efficiency conclusion.  
**Common mistake:** copying the key's `0.40+0.42X`; it does not match the official data.  
**Watermark:** pp. 143-148.

## 6. [ACTUAL PYQ] Two-component GMM estimates

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q6** | **5 marks**  
**ID:** ISM-06 | **Priority:** HIGH | **Pattern:** hard-labelled GMM parameter estimation  
**Question.** Quick group `{18,20,22,25,27}`; leisurely group `{35,38,40,42,45}`.

The density is `p(x)=pi1 N(x|mu1,sigma1^2)+pi2 N(x|mu2,sigma2^2)`.

Component 1: `mu1=112/5=22.4`; squared deviations sum `53.2`; ML variance `sigma1^2=53.2/5=10.64`.

Component 2: `mu2=200/5=40`; squared deviations sum `58`; ML variance `sigma2^2=58/5=11.6`.

Mixing weights are `pi1=pi2=5/10=.5`.

**Final model:** `.5 N(22.4,10.64)+.5 N(40,11.6)`. It represents two behavioural modes and provides soft membership probabilities, unlike one Gaussian centred between them.

**Exam-writing guidance:** write the mixture density first, then list each component's mean, ML variance and mixing weight.  
**Common mistake:** using divisor 4; the prompt is a GMM parameter estimate, so ML divisor 5 is appropriate.  
**Watermark:** pp. 194-203.

## 7. [ACTUAL PYQ] t-CI and residual diagnosis

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q7(a,b)** | **2+3 marks**
**ID:** ISM-07 | **Priority:** HIGH | **Pattern:** t-CI plus residual diagnosis

### (a) Cadence CI

For the 20 observations, `xbar=.9255`, `s=.08095`. Since sigma is unknown, use `t_.025,19=2.093`:

`.9255 +/- 2.093(.08095/sqrt20) = .9255 +/- .03788`.

**95% CI:** `(.8876,.9634)`.

### (b) Residuals `{2,-1,0,1,-2,1,-1,0}`

Mean `=0`. Sum of squared deviations `=12`; sample variance `=12/7=1.7143`.

These values are consistent with zero mean and finite variance, but eight residuals do not establish constant variance or no autocorrelation. A residual plot/ACF (or Ljung-Box-type check, if in scope) is required before concluding white noise.

**Exam-writing guidance:** keep the CI and residual subparts separate; show the t critical value and the sample-variance divisor.  
**Common mistake:** the key rounds the mean early and obtains a different CI.  
**Watermark:** pp. 86-101 and 161-172.

## 8. [ACTUAL PYQ] Two proportions and directional variance F

**Subject:** ISM | **Paper:** 28-Feb-2026 EC-3 Regular | **Q8(a,b)** | **3+2 marks**
**ID:** ISM-08 | **Priority:** HIGH | **Pattern:** two-proportion z plus directional F

### (a) Vaccination proportions

`p1=180/300=.60`, `p2=135/250=.54`; pooled `p=315/550=.572727`.

`SE=sqrt[.572727(.427273)(1/300+1/250)]=.04236`.

`z=(.60-.54)/.04236=1.416`, two-sided `p=.157`. Since `|z|<1.96`, fail to reject equal proportions. The samples do not show a significant city difference at 5%.

### (b) Chip-thickness variability

Sample variances: `sA^2=.028393`, `sB^2=.005667`. Test `H0:sigmaA^2<=sigmaB^2` vs `H1:sigmaA^2>sigmaB^2`.

`F=.028393/.005667=5.011`, df `(7,5)`. Upper 5% critical `F=4.876`; reject `H0` under the stated normality assumption. Line A shows significantly greater variability.

**Exam-writing guidance:** label each subpart's hypotheses, standard error or df, critical comparison and contextual decision.  
**Common mistake:** the key PDF omits this F-test and reports a different proportion z; use the official data.  
**Watermark:** pp. 102-119 and 80-85.

## 9. [ACTUAL PYQ] Two independent means plus 99% CI

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q1(a,b)** | **3+2 marks**
**ID:** ISM-09 | **Priority:** MUST DO | **Pattern:** Welch two-sample test plus z-CI

### (a) Training programs

`H0:muA<=muB`, `H1:muA>muB`. Use Welch t:

`SE=sqrt(9^2/20+8^2/25)=2.57099`; `t=(81-77)/2.57099=1.5558`; Welch df `~38.45`.

Upper 5% critical `~1.685`; fail to reject `H0`. There is insufficient evidence that Program A has higher mean productivity.

### (b) Bulb-life CI

Given `xbar=990`, known `sigma=50`, `n=40`; 99% uses `z=2.576`:

`990 +/- 2.576(50/sqrt40)=990 +/-20.364`.

**CI:** `(969.64,1010.36)` hours.

**Exam-writing guidance:** show the Welch standard error/df for part (a) and `estimate +/- z*SE` for part (b).  
**Common mistake:** pooling the two variances without justification or using a t interval when population sigma is given.  
**Watermark:** pp. 86-119.

## 10. [ACTUAL PYQ] Chi-square independence

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q2** | **5 marks**
**ID:** ISM-10 | **Priority:** HIGH | **Pattern:** chi-square independence

Observed rows: Mobile `(80,120)`, Laptop `(70,50)`, Tablet `(50,30)`; column totals are `(200,200)`, `N=400`.

Expected rows are Mobile `(100,100)`, Laptop `(60,60)`, Tablet `(40,40)`.

Cell contributions are `4,4,1.6667,1.6667,2.5,2.5`; hence `chi2=16.3334`, df `(3-1)(2-1)=2`.

Critical `5.991`; reject independence. Device type and purchase decision are associated in this sample.

**Exam-writing guidance:** include observed totals, the complete expected table, cell contributions, df and the association conclusion.  
**Common mistake:** the key contains a typo “6” for expected Laptop-Purchased; it must be 60.  
**Watermark:** pp. 102-119.

## 11. [ACTUAL PYQ] Three-year moving-average forecast

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q3** | **5 marks**
**ID:** ISM-11 | **Priority:** MUST DO | **Pattern:** trailing moving-average forecast

Production 2017-2024: `42,46,39,35,37,44,51,58`.

Trailing three-year values are:

- 2019: `(42+46+39)/3=42.33`
- 2020: `(46+39+35)/3=40.00`
- 2021: `(39+35+37)/3=37.00`
- 2022: `(35+37+44)/3=38.67`
- 2023: `(37+44+51)/3=44.00`
- 2024: `(44+51+58)/3=51.00`

Forecast 2025 from the latest three actuals `(44+51+58)/3=51` thousand units.

**Exam-writing guidance:** display every available three-year window, then identify the final window used for the 2025 forecast.  
**Common mistake:** using a centred moving average, which needs future observations.  
**Watermark:** pp. 149-160.

## 12. [ACTUAL PYQ] Lag-1 autocorrelation

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q4** | **Marks not printed beside the extracted prompt; paper total is 40 across 8 questions**
**ID:** ISM-12 | **Priority:** HIGH | **Pattern:** lag-1 autocorrelation and persistence

Temperatures: `22.1,22.4,22.6,22.9,23.1,23.4,23.7,23.9,24.1,24.3`; mean `23.25`.

Using the course convention,

`sum_(t=2)^10 (x_t-xbar)(x_(t-1)-xbar)=3.5925`  
`sum_(t=1)^10 (x_t-xbar)^2=5.085`  
`r1=3.5925/5.085=.7065`.

**Conclusion.** Consecutive days show strong positive persistence. Because the series has a steady trend, part of this autocorrelation may reflect non-stationarity; do not infer a stationary AR process from `r1` alone.

**Exam-writing guidance:** state the lag-1 convention, show numerator and denominator separately, then interpret persistence with the trend caveat.  
**Common mistake:** calling the trending series stationary merely because lag-1 autocorrelation is high.  
**Watermark:** pp. 161-172.

## 13. [ACTUAL PYQ] One-sample underfilling z-test

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q5** | **5 marks**
**ID:** ISM-13 | **Priority:** MUST DO | **Pattern:** lower-tailed one-sample z

`H0:mu=500`, `H1:mu<500`; known `sigma=18`, `n=81`, `xbar=496`.

`z=(496-500)/(18/sqrt81)=-4/2=-2`.

At 5%, lower critical `-1.645`; reject `H0`. There is significant evidence that the machine underfills packets.

**Exam-writing guidance:** write the lower-tailed hypotheses before substitution and end in packet-weight context.  
**Common mistake:** using `+/-1.645`; this is a lower-tailed test, so compare to `-1.645`.  
**Watermark:** pp. 102-119.

## 14. [ACTUAL PYQ] Holt trend forecast

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q6** | **5 marks**
**ID:** ISM-14 | **Priority:** MUST DO | **Pattern:** Holt level/trend recursion

Demand is `20,22,24,26,28,30,32`, `alpha=.4`, `beta=.3`, `L1=20`, `T1=2`.

Use `Lt=.4Yt+.6(L_(t-1)+T_(t-1))` and `Tt=.3(Lt-L_(t-1))+.7T_(t-1)`.

Because every actual increases by exactly 2 and initialization matches that trend, every update gives `Lt=Yt` and `Tt=2`: `(L2,T2)=(22,2)` through `(L7,T7)=(32,2)`.

Forecast week 8: `F8=L7+T7=34` units.

Holt is suitable because it explicitly updates trend; SES alone would lag a sustained rise.

**Exam-writing guidance:** state the level/trend equations, show the week-by-week states and box the week-8 forecast.  
**Common mistake:** applying simple exponential smoothing despite the explicit trend or misaligning the next-period forecast.  
**Watermark:** pp. 178-185.

## 15. [ACTUAL PYQ] Simple regression and prediction

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q7** | **5 marks**
**ID:** ISM-15 | **Priority:** MUST DO | **Pattern:** regression and prediction

For `X={1,2,3,4,5,6}`, `Y={90,85,78,72,65,60}`, `xbar=3.5`, `ybar=75`, `Sxx=17.5`, `Sxy=-108`.

`b1=-108/17.5=-6.17143`; `b0=75-(-6.17143)(3.5)=96.6`.

**Model:** `Yhat=96.6-6.1714X`. At `X=3.5`, `Yhat=75`. `R^2=.9978`, a very strong sample linear fit.

Each additional screen-time hour is associated with an estimated 6.17-point decrease in productivity. This is association, not proof that reducing screen time causes a gain.

**Exam-writing guidance:** show the two centred sums, line equation, requested prediction and slope interpretation in units.  
**Common mistake:** interpreting the negative fitted slope as proof of causation.  
**Watermark:** pp. 143-148.

## 16. [ACTUAL PYQ] One-way ANOVA

**Subject:** ISM | **Paper:** 07-Mar-2026 EC-3 Makeup | **Q8** | **5 marks**
**ID:** ISM-16 | **Priority:** MUST DO | **Pattern:** one-way ANOVA table and decision

Methods: M1 `{15,17,16,14}`, M2 `{18,16,20,19}`, M3 `{22,24,23,21}`. Means are `15.5,18.25,22.5`; grand mean `18.75`.

`SSB=99.5`, `SSW=18.75`; df `(2,9)`; `MSB=49.75`, `MSW=2.0833`.

`F=49.75/2.0833=23.88`. Critical `F_.05(2,9)=4.256`; reject equal means.

At least one teaching-method mean differs. A post-hoc procedure would be needed to identify every differing pair.

**Exam-writing guidance:** present a complete ANOVA table with group/grand means, both sums of squares, df, MS, F and decision.  
**Common mistake:** concluding that every pair of teaching methods differs after only the omnibus ANOVA.  
**Watermark:** pp. 125-129.

## 17. [ACTUAL PYQ] SES and MSE model choice

**Subject:** ISM | **Paper:** 06-Sep-2025 EC-3 Regular | **Q2** | **8 marks**
**ID:** ISM-17 | **Priority:** MUST DO | **Pattern:** SES table, MSE and model choice

Exports 2015-2021: `146,159,161,170,174,140,145`; initial `F2015=146`.

For `alpha=.3`, forecasts for 2016-2021 are `146,149.90,153.23,158.261,162.9827,156.0879`; 2022 forecast `152.7615`. MSE over common forecast years 2016-2021 is `245.38`.

For `alpha=.6`, forecasts are `146,153.80,158.12,165.248,170.4992,152.1997`; 2022 forecast `147.8799`. Corresponding MSE is `236.77`.

**Final answer.** On the stated common-period MSE, `alpha=.6` is marginally better and reacts faster to the recent fall/recovery.

**Exam-writing guidance:** for 8 marks, show the full forecast/error/squared-error table, not only these final rows.  
**Common mistake:** comparing the two alphas on different forecast periods or selecting by responsiveness instead of the requested MSE.  
**Watermark:** pp. 173-177.

## 18. [ACTUAL PYQ] Least-squares line and prediction

**Subject:** ISM | **Paper:** 06-Sep-2025 EC-3 Regular | **Q3** | **8 marks**
**ID:** ISM-18 | **Priority:** MUST DO | **Pattern:** least-squares fit, prediction and scatter interpretation

For the ten extraction-time/efficiency pairs, `xbar=32`, `ybar=63.5`, `Sxx=1250`, `Sxy=955`.

`b1=955/1250=.764`; `b0=63.5-.764(32)=39.052`.

**Line:** `Yhat=39.052+.764X`. At `X=35`, `Yhat=65.792%`. `R^2=.6803`, so the line explains about 68.0% of sample variation.

The scatter plot should place time on the horizontal axis, show all ten points and overlay the fitted line. The positive slope supports increasing average efficiency with time within the observed range, but noticeable residual variation remains.

**Exam-writing guidance:** include the least-squares sums, fitted equation, 35-minute prediction and the requested labelled scatter/fit discussion.  
**Common mistake:** omitting the requested scatter/fit comment in an 8-mark answer.  
**Watermark:** pp. 143-148.

## 19. [ACTUAL PYQ] Holt smoothing for subscription growth

**Subject:** ISM | **Paper:** 06-Sep-2025 EC-3 Regular | **Q4** | **8 marks**
**ID:** ISM-19 | **Priority:** MUST DO | **Pattern:** Holt forecasting and beta interpretation

Subscriptions Jan-Jun: `15,18,22,25,29,33`; `alpha=.5`, `beta=.3`, initial Jan level 15 and trend 3.

Using the stated Holt equations:

| Through month | Level | Trend | Next forecast |
|---|---:|---:|---:|
| Feb | 18.0000 | 3.0000 | 21.0000 |
| Mar | 21.5000 | 3.1500 | 24.6500 |
| Apr | 24.8250 | 3.2025 | 28.0275 |
| May | 28.5138 | 3.3484 | 31.8621 |
| Jun | 32.4311 | 3.5191 | 35.9501 |

**July forecast:** about `35.95` thousand subscriptions.

`beta` controls how quickly the estimated growth rate adapts. A small beta stabilizes trend; a large beta reacts faster but can chase noise.

**Exam-writing guidance:** give a level/trend table for every month, box July's forecast and explain beta in one sentence.  
**Common mistake:** updating the trend before the new level or reporting June's fitted level as the July forecast.  
**Watermark:** pp. 178-185.

## 20. [ACTUAL PYQ] Variance F-test and Poisson MLE

**Subject:** ISM | **Paper:** 06-Sep-2025 EC-3 Regular | **Q5(a,b)** | **4+4 marks**
**ID:** ISM-20 | **Priority:** HIGH | **Pattern:** directional F plus Poisson MLE

### (a) Machining variability

`H0:sigmaA^2<=sigmaB^2`, `H1:sigmaA^2>sigmaB^2`. Given `sA=.032,nA=10`, `sB=.028,nB=14`:

`F=.032^2/.028^2=1.3061`, df `(9,13)`. Upper 5% critical `~2.714`; fail to reject `H0`. There is insufficient evidence that A is more variable, assuming independent normal populations.

### (b) Accident-count MLE

Counts `{4,2,5,3,6}` are modelled Poisson. Likelihood is `L(lambda)=product e^-lambda lambda^xi/xi!`; log-likelihood derivative gives `lambda_hat=sum xi/n=xbar=20/5=4` accidents/day.

`P(X=0|lambda_hat=4)=e^-4=0.01832`.

**Exam-writing guidance:** separate the two four-mark parts; show F hypotheses/df, then the Poisson likelihood or log-likelihood before the plug-in probability.  
**Common mistake:** using sample variance in part (a) without squaring the supplied standard deviations, or giving `lambda=4` without showing the MLE logic.  
**Watermark:** pp. 80-85 and 120-125.

## Final solution-bank checklist

- Identify the method before touching numbers.
- State convention when variance divisor, lag correlation or Holt initialization can differ.
- Round only final values (3-4 significant decimals).
- Preserve hypotheses, df and context even when the numerical answer seems obvious.
- Redo Items 2, 4, 5, 8, 10, 14, 16 and 17 without notes.

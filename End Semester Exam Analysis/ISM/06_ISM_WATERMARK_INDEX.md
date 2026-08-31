# ISM Watermark PDF Index

## Page-number convention

`ISM watermark.pdf` has **261 PDF viewer pages**. Every page number below is the number displayed by the PDF viewer, starting at 1. The PDF is a 4-in-1 lecture export, so each viewer page normally contains four reduced slide pages. Printed slide numbers are not used.

The boundaries below were verified by page-by-page text extraction and visual checks of viewer pp. 120, 134, 173 and 194.

## Full logical map

| Viewer pages | Current content | Fast use |
|---:|---|---|
| 1-14 | Session 1: descriptive statistics | mean/variance, five-number summary, skew/outliers |
| 15-22 | Session 2: probability basics | axioms, union/intersection, independence |
| 23-35 | Session 3: conditional and total probability | conditional/total-probability formulas and examples |
| 36-53 | Session 4: Bayes and Naive Bayes | Bayes, MAP/ML ideas, Laplace correction examples |
| 54-68 | Session 5: random variables (title text has a session-number typo) | PMF/PDF, expectation, variance, joint/marginal/conditional |
| 69-85 | Session 6: probability distributions | Bernoulli/binomial/Poisson/normal, t/F/chi-square introductions |
| 86-101 | Session 7: sampling, CLT and confidence intervals | sampling distributions, z/t CI and sample size |
| 102-119 | Session 9: hypothesis testing | test workflow, z/t/proportions, chi-square examples |
| 120-125 | Session 10: MLE | likelihood/log-likelihood method |
| 125-133 | Session 10: one-way and two-way ANOVA | sums of squares and ANOVA tables |
| 134-148 | Session 11: covariance, correlation and regression | Pearson, least squares, R-squared, prediction |
| 149-160 | Session 12: time-series basics and moving averages | components, trailing/centred/weighted MA |
| 161-172 | Session 13: ACF/PACF, AR/MA/ARMA/ARIMA | lag correlation and model-order meanings |
| 173-185 | Lecture 14: SES, Holt and Holt-Winters | recursive tables and trend/seasonal smoothing |
| 186-193 | advanced time-series continuation | ARIMA/SARIMA/SARIMAX/VAR/VARMAX recognition |
| 194-203 | Lecture 15: GMM and EM | mixture density, responsibilities, EM updates |
| 204-214 | Webinar 1 revision | probability practice |
| 215-230 | Webinar 2 revision | Bayes, distributions, random-variable practice |
| 231-243 | Webinar 3 revision | inference and test-selection practice |
| 244-260 | Webinar 4 revision | correlation, regression and time-series practice |
| 261 | terminal/near-empty page | no exam value |

## Must-do lookup map

| Topic | Viewer page(s) | Look up | Memorize | Understand |
|---|---:|---|---|---|
| z/t/paired/two-sample tests | 102-119 | examples and critical-value workflow | core statistics, tails, decision rule | choose test and state conclusion |
| confidence intervals | 86-101 | z/t interval examples and sample size | interval form, z vs t | interpretation and assumptions |
| chi-square | 102-119 | expected-count layout | `E=RC/N`, df | what “association” means |
| one/two-way ANOVA | 125-133 | sums-of-squares table | df and F ratios | treatment/block/error decomposition |
| Pearson correlation | 134-143 | worked table/formula | `r=Sxy/sqrt(SxxSyy)` | association, not causation |
| simple regression | 143-148 | least-squares and R-squared examples | slope/intercept/prediction | adequacy, residuals, extrapolation |
| moving average | 149-160 | centred/trailing examples | trailing forecast | window/lag tradeoff |
| SES | 173-177 | recursive examples | recursion | alpha response-speed tradeoff |
| Holt | 178-185 | level/trend table | level, trend and forecast equations | why SES lags a trend |
| autocorrelation/ARIMA | 161-172, 186-193 | ACF/PACF and model definitions | `(p,d,q)` meanings | stationarity and residual adequacy |
| MLE | 120-125 | likelihood examples | four-step recipe | why maximize likelihood |
| GMM/EM | 194-203 | density, responsibility, update equations | mixture density/responsibility | soft assignment and convergence |

## Formula, derivation, algorithm and example indices

### Formula index

- CI/CLT: pp. 86-101.
- Test statistics and p-value logic: pp. 102-119.
- MLE likelihood: pp. 120-125.
- ANOVA sums of squares: pp. 125-133.
- Pearson/regression/R-squared: pp. 134-148.
- Moving averages: pp. 149-160.
- ACF/ARIMA notation: pp. 161-172 and 186-193.
- SES/Holt/Holt-Winters: pp. 173-185.
- GMM/EM: pp. 194-203.

### Derivation index

- Bayes and Naive Bayes: pp. 36-53.
- Random-variable expectation/variance: pp. 54-68.
- distribution properties: pp. 69-85.
- likelihood construction: pp. 120-125.
- least-squares variation decomposition: pp. 143-148.
- GMM likelihood and EM logic: pp. 199-203.

### Algorithm index

- Hypothesis-test workflow: pp. 102-119.
- ANOVA table construction: pp. 125-133.
- moving-average tables: pp. 149-160.
- SES/Holt recursion: pp. 173-185.
- EM E-step/M-step: pp. 194-203.

### Worked-example index

- CI examples: pp. 98-101.
- test examples: pp. 110-119.
- ANOVA examples: pp. 127-133.
- correlation/regression examples: pp. 139-148.
- moving-average examples: pp. 158-160.
- SES/Holt examples: pp. 175-185.
- GMM responsibility examples: pp. 202-203.

## PYQ-to-watermark routing

| [ACTUAL PYQ] reference | Need | Go to |
|---|---|---:|
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q2, 5 marks | SES recursion/alpha interpretation | 173-177 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q3, 5 marks | paired t and one-mean z | 102-119 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q4, 5 marks | randomized-block ANOVA | 129-133 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q5, 5 marks | regression and adequacy | 143-148 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q6, 5 marks | GMM parameter estimates | 194-203 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q7, 5 marks | t-CI and white noise | 86-101; 161-172 |
| [ACTUAL PYQ] ISM, 28-Feb-2026 EC-3 Regular, Q8, 5 marks | two proportions and variance F | 102-119; 80-85 |
| [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q2, 5 marks | chi-square independence | 102-119 |
| [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q4, marks not printed beside extracted prompt | lag-1 autocorrelation | 161-172 |
| [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q6, 5 marks | Holt trend | 178-185 |
| [ACTUAL PYQ] ISM, 07-Mar-2026 EC-3 Makeup, Q8, 5 marks | one-way ANOVA | 125-129 |
| [ACTUAL PYQ] ISM, 06-Sep-2025 EC-3 Regular, Q2, 8 marks | SES and MSE | 173-177 |
| [ACTUAL PYQ] ISM, 06-Sep-2025 EC-3 Regular, Q3, 8 marks | regression/prediction | 143-148 |
| [ACTUAL PYQ] ISM, 06-Sep-2025 EC-3 Regular, Q5, 8 marks | F-test and Poisson MLE | 80-85; 120-125 |

## Open-book exam strategy

### Know from memory

- Test-selection tree, hypotheses and tail direction.
- z/t/proportion statistics.
- Pearson, slope/intercept and SES recursion.
- ANOVA table headings and degrees of freedom.
- GMM density and responsibility idea.

### Look up rapidly

- Critical values and distribution tables.
- Long ANOVA sums-of-squares layout.
- Holt/Holt-Winters initialization convention.
- ACF/PACF identification details.
- Full EM covariance update and advanced ARIMA-family equations.

### Do not search during the exam

- A one-line z/t formula, correlation formula or SES recursion: retrieval is slower than memory.
- A topic without a pre-indexed page: write the method you know, then return if time remains.
- Long advanced-model derivations for a low-mark prompt: give definition, notation, use case and assumptions first.

## Final exam-hall cheat index

```text
ISM WATERMARK - VIEWER PAGES
  CI / CLT                      -> 86-101
  Hypothesis tests / chi-square -> 102-119
  MLE                           -> 120-125
  ANOVA                         -> 125-133
  Correlation / regression      -> 134-148
  Moving averages               -> 149-160
  ACF / ARIMA                   -> 161-172
  SES / Holt                    -> 173-185
  SARIMA / VAR family           -> 186-193
  GMM / EM                      -> 194-203
```

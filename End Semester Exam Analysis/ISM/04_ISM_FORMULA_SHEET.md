# ISM Formula and Method Sheet

All page references are **PDF viewer pages** in `ISM watermark.pdf` (261 pages). Each viewer page contains four reduced lecture slides.

## 1. Descriptive statistics and probability

- Sample mean: `xbar = (sum xi)/n`.
- Sample variance: `s^2 = sum(xi-xbar)^2/(n-1)`; population/ML form uses divisor `n` when explicitly required.
- Covariance: `sxy = sum[(xi-xbar)(yi-ybar)]/(n-1)`.
- IQR: `Q3-Q1`; fences: `Q1-1.5 IQR`, `Q3+1.5 IQR`.
- Addition: `P(A union B)=P(A)+P(B)-P(A intersection B)`.
- Conditional: `P(A|B)=P(A intersection B)/P(B)`.
- Total probability: `P(B)=sum_i P(B|Ai)P(Ai)` for an exhaustive partition `{Ai}`.
- Bayes: `P(Ai|B)=P(B|Ai)P(Ai)/sum_j P(B|Aj)P(Aj)`.

Lookup: viewer pp. 1-53.

## 2. Random variables and distributions

- Expectation: discrete `E[X]=sum x p(x)`; continuous `E[X]=integral x f(x) dx`.
- Variance: `Var(X)=E[X^2]-(E[X])^2`.
- Covariance: `Cov(X,Y)=E[XY]-E[X]E[Y]`.
- Independence: `f(x,y)=fX(x)fY(y)` for all valid `(x,y)`.
- Binomial: `P(X=x)=C(n,x)p^x(1-p)^(n-x)`; mean `np`, variance `np(1-p)`.
- Poisson: `P(X=x)=e^(-lambda)lambda^x/x!`; mean and variance `lambda`.
- Normal standardization: `z=(x-mu)/sigma`.
- Sample-mean standard error: `SE(xbar)=sigma/sqrt(n)` or `s/sqrt(n)`.

Lookup: viewer pp. 54-85.

## 3. Confidence intervals

Symbols: `xbar` sample mean, `p_hat` sample proportion, `sigma` population SD, `s` sample SD, `n` sample size, `alpha` tail error.

- Mean, sigma known: `xbar +/- z_(alpha/2) sigma/sqrt(n)`.
- Mean, sigma unknown: `xbar +/- t_(alpha/2,n-1) s/sqrt(n)`.
- Proportion: `p_hat +/- z_(alpha/2)sqrt[p_hat(1-p_hat)/n]`.
- Difference of independent means (Welch): `(xbar1-xbar2) +/- t*sqrt(s1^2/n1+s2^2/n2)`.
- Required mean sample size: `n=(z_(alpha/2)sigma/E)^2`; round upward.

Interpretation: the procedure captures the fixed parameter in the stated percentage of repeated samples. Do not say there is a post-data probability that the fixed parameter lies in this one interval.

Lookup: viewer pp. 86-101.

## 4. Hypothesis-test core

Always write: parameter, `H0/H1`, `alpha`, assumptions, statistic, df, p/critical comparison, decision, contextual conclusion.

### One mean

- Known sigma: `z=(xbar-mu0)/(sigma/sqrt(n))`.
- Unknown sigma: `t=(xbar-mu0)/(s/sqrt(n))`, df `n-1`.

### Paired mean

Create `di=after_i-before_i`; then `t=dbar/(sd/sqrt(n))`, df `n-1`.

### Independent means

- Welch statistic: `t=(xbar1-xbar2)/sqrt(s1^2/n1+s2^2/n2)`.
- Welch df: `(a+b)^2/[a^2/(n1-1)+b^2/(n2-1)]`, where `a=s1^2/n1`, `b=s2^2/n2`.
- Use pooled t only if equal population variances are justified.

### One and two proportions

- One proportion: `z=(p_hat-p0)/sqrt[p0(1-p0)/n]`.
- Equality of two proportions: pooled `p=(x1+x2)/(n1+n2)`;
  `z=(p1-p2)/sqrt[p(1-p)(1/n1+1/n2)]`.

### Decision language

- If `p < alpha`, reject `H0`.
- Otherwise, fail to reject `H0`.
- Never write “prove/accept H0.”
- Type I: reject a true `H0`; Type II: fail to reject a false `H0`.

Lookup: viewer pp. 102-119.

## 5. Chi-square and F tests

### Chi-square independence

- Expected cell: `Eij=(row total)(column total)/N`.
- Statistic: `chi2=sum (Oij-Eij)^2/Eij`.
- df: `(r-1)(c-1)`.
- Conditions: independent observations; expected counts sufficiently large.

### Variance F-test

- Directional `H1: sigmaA^2 > sigmaB^2`: use `F=sA^2/sB^2` with df `(nA-1,nB-1)` and upper tail.
- Normal-population assumption matters strongly.

Lookup: chi-square pp. 102-119; F distribution background pp. 80-85.

## 6. ANOVA

### One-way

- `SSB=sum_j n_j(xbar_j-xbar)^2`.
- `SSW=sum_j sum_i(xij-xbar_j)^2`.
- df: between `k-1`; within `N-k`; total `N-1`.
- `F=(SSB/(k-1))/(SSW/(N-k))`.
- Assumptions: independent observations, normal errors within groups, equal variances.

### Randomized block / two-way without replication

For `a` treatments and `b` blocks, `N=ab`, grand total `T`:

- `CF=T^2/N`.
- `SST=sum xij^2-CF`.
- `SSTreat=sum(row total_i^2/b)-CF`.
- `SSBlock=sum(column total_j^2/a)-CF`.
- `SSE=SST-SSTreat-SSBlock`.
- df: treatment `a-1`; block `b-1`; error `(a-1)(b-1)`.
- `Ftreat=MSTreat/MSE`; `Fblock=MSBlock/MSE`.

If `SSE=0`, the conventional F ratios divide by zero: report the degeneracy; do not invent a finite F.

Lookup: viewer pp. 120-133.

## 7. Correlation and regression

- Pearson: `r=Sxy/sqrt(Sxx Syy)` where `Sxx=sum(x-xbar)^2`, `Syy=sum(y-ybar)^2`, `Sxy=sum(x-xbar)(y-ybar)`.
- Regression slope: `b1=Sxy/Sxx`.
- Intercept: `b0=ybar-b1 xbar`.
- Prediction: `yhat=b0+b1x`.
- Residual: `ei=yi-yhat_i`; `SSE=sum ei^2`.
- Total variation: `SST=sum(yi-ybar)^2`.
- Coefficient of determination: `R^2=1-SSE/SST`; in simple regression with intercept, `R^2=r^2`.

Interpretation: `b1` is expected response change per one-unit increase in `X`; `R^2` is the fraction of sample response variation explained by the fitted linear model. Correlation is not causation. Check scatter/residual shape before extrapolating.

Lookup: viewer pp. 134-148.

## 8. Time-series and forecasting

### Moving average

- Trailing `k`-period forecast: `F_(t+1)=(Y_t+...+Y_(t-k+1))/k`.
- Compare models on a common set of forecasted periods using `MSE=sum e_t^2/m` or `MAD=sum |e_t|/m`.

### Simple exponential smoothing

- `F_(t+1)=alpha Y_t+(1-alpha)F_t`, `0<=alpha<=1`.
- Larger `alpha`: faster response, less smoothing.
- Maintain columns `t, Y_t, F_t, e_t, e_t^2` to avoid index errors.

### Holt trend

State the convention:

- `L_t=alpha Y_t+(1-alpha)(L_(t-1)+T_(t-1))`.
- `T_t=beta(L_t-L_(t-1))+(1-beta)T_(t-1)`.
- `h`-step forecast: `F_(t+h)=L_t+hT_t`.

### Autocorrelation and residual adequacy

- Course lag-1 convention used in Mar-2026: `r1=sum_(t=2)^n[(Y_t-Ybar)(Y_(t-1)-Ybar)] / sum_(t=1)^n(Y_t-Ybar)^2`.
- White noise: approximately zero mean, constant variance and no serial correlation.
- A short residual list cannot prove white noise; inspect residual plot/ACF or use a portmanteau test if asked.

Lookup: MA pp. 149-160; AR/ACF/ARIMA pp. 161-172; SES/Holt and advanced models pp. 173-193.

## 9. ARIMA-family recognition

- AR(`p`): current value depends on `p` lags.
- MA(`q`): current value depends on `q` past innovations/errors; not the same as a simple moving-average forecast.
- ARMA(`p,q`): stationary AR plus MA.
- ARIMA(`p,d,q`): difference `d` times, then fit ARMA.
- SARIMA adds seasonal `(P,D,Q)_m`.
- SARIMAX adds exogenous predictors to SARIMA.
- VAR models several mutually influencing time series.
- VARMAX adds vector MA terms and exogenous inputs.

Memorize meanings and use cases; look up long equations. Recent long-derivation PYQ evidence is insufficient.

## 10. MLE, GMM and EM

### MLE method

1. Write likelihood `L(theta)=product_i f(xi|theta)`.
2. Take `ell(theta)=log L(theta)`.
3. Differentiate and solve `d ell/d theta=0`.
4. Check maximum/valid parameter range.

Standard results: Bernoulli `p_hat=sum xi/n`; Poisson `lambda_hat=xbar`; normal mean `mu_hat=xbar`. MLE variances normally use divisor/effective count, not `n-1`.

### Gaussian mixture

- Density: `p(x)=sum_(k=1)^K pi_k N(x|mu_k,Sigma_k)`.
- Constraints: `pi_k>=0`, `sum pi_k=1`.
- Responsibility: `gamma_ik=pi_k N(xi|mu_k,Sigma_k) / sum_j pi_j N(xi|mu_j,Sigma_j)`.
- Effective membership: `Nk=sum_i gamma_ik`.
- Updates: `pi_k=Nk/n`, `mu_k=sum_i gamma_ik xi/Nk`, `Sigma_k=sum_i gamma_ik(xi-mu_k)(xi-mu_k)^T/Nk`.

EM alternates E-step responsibilities and M-step parameters until the log-likelihood/parameters stabilize. It can converge to a local optimum and is initialization-sensitive.

Lookup: MLE pp. 120-125; GMM/EM pp. 194-203.

## 11. Test selection in 20 seconds

| Data/question | Method |
|---|---|
| same people before/after | paired t |
| one sample mean vs claim | one-sample z/t |
| two independent sample means | Welch two-sample t |
| two proportions | pooled two-proportion z |
| categorical count association | chi-square independence |
| 3+ means, one factor | one-way ANOVA |
| treatments repeated across blocks | randomized-block ANOVA |
| compare normal-population variances | F-test |
| two quantitative variables | Pearson/regression |
| stable level forecast | MA or SES |
| trend without seasonality | Holt |
| multimodal continuous population | GMM |


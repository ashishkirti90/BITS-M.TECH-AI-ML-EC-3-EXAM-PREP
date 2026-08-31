# ML Formula and Method Sheet

> Memorize the short skeletons. Use `ML WaterMark.pdf` for verification; page numbers below are PDF-viewer pages.

## Linear models and regularization

- Linear regression: `yhat=w^Tx+b`.
- Ridge: `min_w SSE + lambda sum_j w_j^2`.
- Lasso: `min_w SSE + lambda sum_j |w_j|`.
- Logistic probability: `p(y=1|x)=sigma(z)=1/(1+e^-z)`, `z=w^Tx+b`.
- Binary cross-entropy: `-[y ln p+(1-y)ln(1-p)]`.

`lambda` is regularization strength. Larger values usually shrink coefficients, raise bias and lower variance. L1 can create exact zeros; L2 normally does not. Watermark: pp. 33-37 and 39-45.

## Decision trees

- Entropy: `H(S)=-sum_c p_c log2 p_c`.
- Information gain: `IG(S,A)=H(S)-sum_v |S_v|/|S| H(S_v)`.
- Gini: `1-sum_c p_c^2`.
- Gain ratio: `IG/SplitInformation`.

Pure node entropy/Gini is zero. Large depth/small leaf -> lower bias, higher variance. Watermark: pp. 52-70.

## Gower, KNN and LWR

- Numeric dissimilarity: `s_ij=|x_ij-z_j|/(max_j-min_j)`.
- Nominal: `s_ij=0` for match, `1` otherwise.
- Ordinal: convert rank `r` among `M` levels to `(r-1)/(M-1)`, then absolute difference.
- Gower: `d_i=sum_j delta_ij s_ij / sum_j delta_ij`.
- Weighted class score: `S_c=sum_{i:y_i=c} K(d_i)`.
- KNN regression: mean or stated weighted mean of neighbor targets.
- Gaussian kernel: `K_i=exp(-d_i^2/(2b^2))`.
- LWR: `J(theta)=1/2 sum_i K_i(theta^T x_i-y_i)^2`.
- Gradient: `sum_i K_i(theta^Tx_i-y_i)x_i`; update `theta<-theta-alpha gradient`.

`delta_ij` marks an observed/comparable field; `b` is bandwidth. Exact match with `1/d^2` needs a stated rule: return that case or add an instructed epsilon. Watermark: pp. 72-82.

## Bayes, MLE and Naive Bayes

- Bayes: `P(c|x)=P(x|c)P(c)/P(x)`.
- Naive score: `S_c=P(c) product_j P(x_j|c)`.
- Gaussian density: `N(x|mu,sigma^2)=1/(sqrt(2pi)sigma) exp(-(x-mu)^2/(2sigma^2))`.
- ML mean: `mu=(1/n)sum x_i`.
- ML variance: `sigma^2=(1/n)sum(x_i-mu)^2`.
- Laplace multinomial: `P(w|c)=(count(w,c)+alpha)/(N_c+alpha V)`.
- Stable form: `log S_c=log P(c)+sum_j log P(x_j|c)`.
- MAP: `argmax_theta P(D|theta)P(theta)`; MLE omits prior.

`N_c` is total tokens for class `c`, not documents; `V` is vocabulary size. Watermark: pp. 85-103.

## Ensembles

### AdaBoost

- Weighted error: `epsilon_t=sum_i w_i I[y_i != h_t(x_i)]`.
- Learner weight: `alpha_t=0.5 ln((1-epsilon_t)/epsilon_t)`.
- Sample update: `w_i' = w_i exp(-alpha_t y_i h_t(x_i))`, then divide by `sum_i w_i'`.
- Final classifier: `sign(sum_t alpha_t h_t(x))`.

If `epsilon=.5`, `alpha=0`; worse than chance should be rejected/reversed depending on implementation. Watermark: pp. 117-123.

### Majority vote

For `m=3` independent classifiers of accuracy `p`:

`P(majority correct)=p^3+3p^2(1-p)`.

Independence is the key assumption; correlation reduces the gain.

### Gradient boosting, squared loss

- `F0=mean(y)`.
- Pseudo-residual: `r_i=y_i-F_{m-1}(x_i)` (constant factors depend on loss definition).
- Fit weak learner `h_m` to residuals.
- `F_m(x)=F_{m-1}(x)+eta h_m(x)`.

Watermark: pp. 124-126.

## K-means

1. Initialize `K` centers.
2. Assign `z_i=argmin_k ||x_i-mu_k||^2`.
3. Update `mu_k=(1/n_k)sum_{i:z_i=k}x_i`.
4. Repeat until assignments/centers stabilize.

SSE: `sum_i ||x_i-mu_{z_i}||^2`. Watermark: pp. 128-134.

## GMM and EM

- Weighted component density: `a_ik=pi_k N(x_i|mu_k,Sigma_k)`.
- Responsibility: `gamma_ik=a_ik/sum_l a_il`.
- Effective count: `N_k=sum_i gamma_ik`.
- Mixing weight: `pi_k=N_k/N`.
- Mean: `mu_k=(1/N_k)sum_i gamma_ik x_i`.
- Covariance: `Sigma_k=(1/N_k)sum_i gamma_ik(x_i-mu_k)(x_i-mu_k)^T`.
- Log-likelihood: `ell=sum_i ln(sum_k pi_k N(x_i|mu_k,Sigma_k))`.

Each observation's responsibilities sum to one; mixing weights also sum to one. Watermark: pp. 135-143.

## SVM

### Score and geometry

- Score: `f(x)=w^Tx+b`; class `sign(f)`.
- Test-point distance to boundary: `|f(x)|/||w||`.
- Canonical support constraint: `y_i f(x_i)=1`.
- Distance boundary-to-one-margin: `1/||w||`.
- Total canonical margin width: `2/||w||`.
- Hinge loss: `max(0,1-y_i f(x_i))`.

### Primal

- Hard: minimize `1/2||w||^2`, subject to `y_i f_i>=1`.
- Soft: minimize `1/2||w||^2+C sum_i xi_i`, subject to `y_i f_i>=1-xi_i`, `xi_i>=0`.

`C` is violation cost: large C prioritizes training classification; small C tolerates violations for stronger regularization.

### Dual and kernels

- `w=sum_i alpha_i y_i x_i`.
- Support vector: `alpha_i>0` (with soft-margin nuances at bounds).
- Kernel decision: `sign(sum_i alpha_i y_i K(x_i,x)+b)`.
- Linear: `K(x,z)=x^Tz`.
- Polynomial: `K(x,z)=(c+x^Tz)^p`.
- RBF: `K(x,z)=exp(-||x-z||^2/(2sigma^2))`.
- Valid Gram matrices are symmetric positive semidefinite.
- Dense Gram storage: `O(N^2)`.

Watermark: geometry pp. 144-147; optimization/dual pp. 148-153; soft margin pp. 153-156; kernels pp. 157-166.

## Model evaluation and responsible use

- Precision `TP/(TP+FP)`.
- Recall/TPR `TP/(TP+FN)`.
- Specificity/TNR `TN/(TN+FP)`.
- F1 `2PR/(P+R)`.
- Accuracy `(TP+TN)/N`.
- Regression: `MSE=(1/N)sum(y-yhat)^2`; `RMSE=sqrt(MSE)`.

Fit preprocessing on training data/fold only. Evaluate uncertainty, calibration, subgroup behavior and the cost of FP/FN. Interpretability is not causality or fairness.

## Method checklist

1. State convention: variance denominator, gradient sum/mean, margin half/full, tie rule.
2. Keep at least four significant digits through intermediate work.
3. Round only final displayed values unless the paper directs otherwise.
4. Box the answer and add one context sentence.
5. Sanity-check: probabilities/rows sum to one; distances nonnegative; new weights sum to one; class sign matches support labels.


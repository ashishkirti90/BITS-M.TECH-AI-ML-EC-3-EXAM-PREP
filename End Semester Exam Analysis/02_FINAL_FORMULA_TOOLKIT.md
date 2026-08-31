# Final Formula Toolkit

This is the compact cross-subject lookup layer. Keep the subjects separated during revision; use the linked subject formula sheets for derivations and examples.

## ISM

Full sheet: [ISM formula sheet](ISM/04_ISM_FORMULA_SHEET.md)

### Estimation and tests

- Mean standard error: `SE(xbar) = sigma/sqrt(n)` or `s/sqrt(n)`.
- Mean CI: `xbar +/- z_(alpha/2) sigma/sqrt(n)`; use `t_(alpha/2,n-1)` when `sigma` is unknown under the usual small-sample conditions.
- Proportion CI: `p_hat +/- z_(alpha/2) sqrt[p_hat(1-p_hat)/n]`.
- One-sample mean: `z or t = (xbar-mu_0)/SE(xbar)`.
- Two independent means: `(xbar_1-xbar_2-Delta_0)/SE`; choose pooled or Welch variance deliberately.
- Paired test: reduce to differences, `t = dbar/(s_d/sqrt(n))`.
- Chi-square: `chi^2 = sum (O-E)^2/E`, with `E_ij = row_i total * col_j total / grand total`.
- One-way ANOVA: `F = MS_between/MS_within`, where `MS = SS/df`.

### Association and forecasting

- Correlation: `r = sum[(x-xbar)(y-ybar)] / sqrt[sum(x-xbar)^2 sum(y-ybar)^2]`.
- Simple regression slope: `b_1 = S_xy/S_xx`; intercept: `b_0 = ybar-b_1 xbar`.
- Simple exponential smoothing: `F_(t+1) = alpha Y_t + (1-alpha)F_t`.
- Holt level: `l_t = alpha y_t + (1-alpha)(l_(t-1)+b_(t-1))`.
- Holt trend: `b_t = beta(l_t-l_(t-1)) + (1-beta)b_(t-1)`.
- Holt forecast: `yhat_(t+h|t) = l_t + h b_t`.
- Sample ACF at lag `k`: `r_k = sum_(t=k+1)^n (y_t-ybar)(y_(t-k)-ybar) / sum_(t=1)^n (y_t-ybar)^2`.

### Fast lookup

| Topic | Watermark viewer pages |
|---|---:|
| CI and CLT | 86-101 |
| Hypothesis tests and chi-square | 102-119 |
| MLE | 120-125 |
| ANOVA | 125-133 |
| Correlation and regression | 134-148 |
| Moving averages | 149-160 |
| ACF, PACF, ARIMA | 161-172 |
| SES and Holt | 173-185 |
| SARIMA and VAR | 186-193 |
| GMM and EM | 194-203 |

Complete map: [ISM watermark index](ISM/06_ISM_WATERMARK_INDEX.md)

## ML

Full sheet: [ML formula sheet](ML/04_ML_FORMULA_SHEET.md)

### Classification and distance

- Logistic probability: `p(y=1|x) = 1/(1+exp(-(w^T x+b)))`.
- Precision: `TP/(TP+FP)`; recall: `TP/(TP+FN)`; specificity: `TN/(TN+FP)`.
- F1: `2PR/(P+R)`.
- Gower dissimilarity: weighted mean of per-feature dissimilarities over valid features; numeric contribution `|x_ik-x_jk|/range_k`, categorical contribution `0` if equal and `1` otherwise.
- Naive Bayes: `P(C|x) proportional to P(C) product_j P(x_j|C)`; compare log scores to avoid underflow.

### Trees, ensembles, and clustering

- Entropy: `H(S) = -sum_k p_k log_2 p_k`.
- Gini: `1-sum_k p_k^2`.
- Information gain: parent impurity minus weighted child impurity.
- AdaBoost error: `epsilon_t = sum_i w_i I[y_i != h_t(x_i)]`.
- AdaBoost learner weight: `alpha_t = 0.5 ln[(1-epsilon_t)/epsilon_t]`.
- Weight update: `w_i <- w_i exp[-alpha_t y_i h_t(x_i)]`, then normalize.
- Gradient boosting for squared error: residual `r_i = y_i-F_(m-1)(x_i)`; update `F_m = F_(m-1)+eta h_m`.
- K-means assignment: nearest centroid; update: componentwise mean of assigned points.
- GMM responsibility: `gamma_ik = pi_k N(x_i|mu_k,Sigma_k) / sum_j pi_j N(x_i|mu_j,Sigma_j)`.

### SVM and regularization

- Hard-margin primal: minimize `0.5||w||^2` subject to `y_i(w^T x_i+b) >= 1`.
- Decision boundary: `w^T x+b=0`; geometric margin width: `2/||w||`.
- Soft margin: minimize `0.5||w||^2 + C sum_i xi_i`, subject to `y_i(w^T x_i+b) >= 1-xi_i`, `xi_i>=0`.
- Kernel decision: `sign(sum_i alpha_i y_i K(x_i,x)+b)`.
- Ridge: loss `+ lambda ||w||_2^2`; Lasso: loss `+ lambda ||w||_1`.

### Fast lookup

| Topic | Watermark viewer pages |
|---|---:|
| Regularization | 36-37 |
| Logistic regression and metrics | 41-50 |
| Decision trees | 54-70 |
| KNN and Gower | 72-78 |
| LWR | 79-82 |
| MLE and MAP | 87-93 |
| Naive Bayes | 94-103 |
| Bagging and random forests | 111-116 |
| AdaBoost | 117-123 |
| Gradient boosting | 124-126 |
| K-means | 128-134 |
| GMM | 140-143 |
| SVM geometry | 146-147 |
| SVM dual and KKT | 148-153 |
| Soft margin and `C` | 154-156 |
| Kernels | 157-161 |

Complete map: [ML watermark index](ML/06_ML_WATERMARK_INDEX.md)

## DNN

Full sheet: [DNN formula sheet](DNN/04_DNN_FORMULA_SHEET.md)

### Dimensions and parameter counts

- Dense layer parameters: `n_in*n_out + n_out`.
- 2D convolution output: `floor[(N+2P-K)/S]+1` per spatial dimension.
- Convolution parameters: `K_h*K_w*C_in*C_out + C_out` with one bias per output channel.
- Vanilla RNN parameters: `h*d + h*h + h` for hidden size `h` and input size `d`; add `h*o+o` for an output layer of size `o`.
- LSTM recurrent-cell parameters: `4(h*d + h*h + h)`.
- GRU recurrent-cell parameters: `3(h*d + h*h + h)` under the common three-gate parameterization.

### Recurrent units and attention

- Vanilla RNN: `h_t = phi(W_xh x_t + W_hh h_(t-1) + b_h)`.
- LSTM: compute forget/input/output gates and candidate; `c_t = f_t elementwise*c_(t-1) + i_t elementwise*g_t`, `h_t = o_t elementwise*tanh(c_t)`.
- GRU: update/reset gates blend the previous state and candidate state.
- Scaled dot-product attention: `Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V`.
- Multi-head attention: concatenate head outputs and apply `W^O`.
- Causal masking sets forbidden future logits to a very negative value before softmax.
- Cross-attention uses decoder states as queries and encoder outputs as keys/values.

### Optimization and normalization

- SGD: `theta <- theta-eta g_t`.
- Momentum: `v_t = beta v_(t-1)+(1-beta)g_t`; `theta <- theta-eta v_t`.
- Adam: maintain first/second moments, bias-correct them, then update with `mhat/(sqrt(vhat)+epsilon)`.
- Dropout training: mask activations and use inverted scaling; disable random masking at inference.
- Batch normalization normalizes each feature/channel using mini-batch statistics; layer normalization normalizes features within each example/token.

### Fast lookup

| Topic | Watermark viewer pages |
|---|---:|
| FFNN and backpropagation | 53-58 |
| CNN | 95-104 |
| Transfer learning | 110-111 |
| RNN | 116-122 |
| GRU | 127-129 |
| LSTM | 131-133 |
| Attention | 141-150 |
| Transformer | 152-159 |
| Decoder and cross-attention | 160-166 |
| BERT, GPT, and T5 | 167-168 |
| Optimizers | 177-179 |
| Regularization | 184-196 |
| Dropout / batch norm / layer norm | 189 / 190 / 191 |

Complete map: [DNN watermark index](DNN/06_DNN_WATERMARK_INDEX.md)

## MFML

Full sheet: [MFML formula sheet](MFML/04_MFML_FORMULA_SHEET.md)

### Linear algebra

- Rank-nullity: `rank(A)+nullity(A)=number of columns of A`.
- Eigenvalue equation: `det(A-lambda I)=0`; eigenvectors satisfy `(A-lambda I)v=0`.
- Diagonalization: `A=PDP^-1` when there is a full eigenvector basis.
- SVD: `A=U Sigma V^T`; nonzero singular values are square roots of nonzero eigenvalues of `A^T A`.
- Frobenius norm: `||A||_F = sqrt(sum_ij a_ij^2) = sqrt(sum_i sigma_i^2)`.

### Calculus and optimization

- First-order approximation: `f(x+Delta) approximately f(x)+grad f(x)^T Delta`.
- Second-order approximation adds `0.5 Delta^T H(x) Delta`.
- Gradient descent: `x_(k+1)=x_k-eta grad f(x_k)`.
- Momentum: accumulate a velocity from the current gradient and previous velocity, then update `x` consistently with the chosen sign convention.
- Convex twice-differentiable function: `H(x)` is positive semidefinite on the domain.
- Lagrangian: `L(x,lambda,nu)=f(x)+sum_i lambda_i g_i(x)+sum_j nu_j h_j(x)` for inequalities `g_i(x)<=0` and equalities `h_j(x)=0`.
- KKT: stationarity, primal feasibility, dual feasibility `lambda_i>=0`, and complementary slackness `lambda_i g_i(x)=0`.

### PCA and SVM

- Center data, form covariance, sort eigenpairs descending, and project with `Z=X_centered W_k`.
- Explained variance ratio: `lambda_i/sum_j lambda_j`.
- Linear SVM primal: minimize `0.5||w||^2` subject to `y_i(w^T x_i+b)>=1`.
- Margin width: `2/||w||`; support vectors meet the active margin equality in the separable canonical form.

### Fast lookup

| Topic | Watermark viewer pages |
|---|---:|
| RREF and rank | 17 |
| Eigenvalues/eigenvectors | 34 |
| SVD | 42 |
| Hessian and gradient descent | 65 |
| Momentum | 81 |
| PCA | 88 |
| KKT | 134 |
| SVM | 135 |

Complete map: [MFML watermark index](MFML/06_MFML_WATERMARK_INDEX.md)

## Open-book setup

1. Tab each watermark PDF using the viewer-page table for that subject.
2. Keep the subject formula sheet beside its PYQ solutions; do not rely on this compact toolkit for derivations.
3. Before substituting, write the target quantity, formula, assumptions, and dimensions.
4. Box the numerical result and add one sentence of interpretation.
5. When a convention can reverse signs or labels, declare the convention and preserve it through the final answer.

# ML End-Sem Scoring Guide

> **Purpose:** Maximize expected comprehensive-exam marks in a 5–6 day preparation window. This guide follows the reference repository's scoring-guide model: syllabus map, recent-paper signal, priority, formulas, scoring workflows, common mistakes, and open-book strategy.
## Official syllabus map

Workflow/preprocessing/evaluation; linear regression and bias-variance; discriminants/logistic regression; decision trees/entropy/MDL; KNN/LWR/RBF; SVM and kernels; Bayesian learning, MLE/MAP, optimal and Naive Bayes; bagging/RF/AdaBoost/gradient boosting/XGBoost; K-means/GMM/EM; model comparison, bias/fairness/interpretability. Comprehensive covers all topics, 40%, 150 minutes.

## Priority map

| Topic | Priority | Recent evidence | Form | Difficulty | Exact preparation |
|---|---|---|---|---|---|
| SVM/kernels | 🔴 | both Mar-2026; both 2021 end-sems | margin/support-vector numerical + reasoning | medium-hard | decision/distance, hard/soft, C, dual alpha, kernel cost |
| Naive Bayes | 🔴 | both Mar-2026 | Gaussian/multinomial posterior | medium | priors, likelihoods, Laplace, mixed feature handling |
| Ensembles | 🔴 | both Mar-2026 | AdaBoost weights, bagging/RF, boosting residuals | medium | formulas, variance/bias, majority probability |
| KNN/LWR | 🔴 | both Mar-2026 | weighted vote/regression/GD | medium | mixed-data distance, normalization, kernels, local fit |
| K-means/GMM/EM | 🔴 | both Mar-2026; 2021 regular | one iteration + compare | medium | hard assignment, responsibilities, M-step |
| Ridge/lasso/bias-variance | 🟠 | both Mar-2026 | scenario/model selection | easy-medium | objective/effect of lambda, sparsity, auditability |
| Decision trees | 🟠 | both Mar-2026 | depth/overfit; entropy older | easy-medium | entropy/gain, continuous split, pruning/MDL |
| Logistic vs linear classification | 🟡 | Mar-2026 regular | conceptual | easy | sigmoid/log loss, bounded output, boundary |
| Evaluation/fairness/interpretability | 🟡 | both Mar-2026 | scenario justification | easy-medium | confusion metrics, imbalance, auditability, fairness caveat |
| Workflow/preprocessing taxonomy | 🟢 | official, weak end-sem numericals | short concept | easy | scaling, encoding, leakage, imbalance; do not over-study |

### Cross-paper frequency (4 distinct extractable end-sem sittings: 2021 regular/makeup, 2026 regular/makeup)

| Topic family | Paper presence | Mode | Typical recent marks |
|---|---:|---|---:|
| SVM/kernels | 4/4 | numerical + choice | 6–8 |
| K-means/GMM/EM | 3/4 | iteration/comparison | 6–8 |
| Decision trees | 3/4 | construction/overfit | 2–6 |
| Naive Bayes | 2/4, both 2026 | posterior numerical | 5–6 |
| Ensembles | 2/4, both 2026 | update/probability | 6–8 |
| KNN/LWR | 2/4, both 2026 | numerical | 6 |
| Ridge/lasso | 2/4, both 2026 | scenario/concept | 3–4 |
| Evaluation/interpretability | 2/4, both 2026 | applied reasoning | 3–6 |

Separate 2023–24 answer-key artifacts reinforce several categories but were not added to the denominator where a distinct matching QP could not be cleanly separated.

## Recent paper signal

- **Latest regular cycle (1 Mar 2026):** the newly added legacy `.doc` matches the metadata and cycle of the already extracted QP/answer-key bundle: lasso vs ensemble under audit constraints; distance-weighted KNN; AdaBoost update; multinomial NB with Laplace; SVM margin/model choice; K-means vs GMM; linear/logistic/tree behavior. The answer-key bundle remains the question-level text source because the original is binary Word `.doc`.
- **Mar-2026 makeup:** ridge bias-variance; Gaussian NB; KNN vs LWR; bagging/RF/AdaBoost and majority probability; full GMM EM step + K-means; gradient boosting residual; SVM support-vector/dual/kernel; tree depth.
- **Both:** SVM, Bayes, instance-based learning, ensembles, unsupervised clustering, and linear regularization. This is the mature stable core.
- **Older reduced:** older papers contribute recurring SVM/GMM/tree evidence, but the latest style is applied, scenario-driven and often asks both calculation and deployment justification.

## Concepts from zero

### Bias, variance and regularization

High variance overfits; high bias underfits. Ridge (`L2`) smoothly shrinks coefficients and handles correlation but rarely makes them exactly zero. Lasso (`L1`) promotes sparsity and interpretability. Increasing lambda raises bias and lowers variance.

### Instance-based learning

KNN does not fit a global parametric model; it predicts from nearby cases. Distances require scale and type awareness. Weighted KNN gives close neighbors greater influence. LWR fits a local regression weighted around the query, allowing a local slope rather than only averaging labels/targets.

### Bayes classifiers

Bayes rule combines prior and likelihood. Naive Bayes assumes conditional feature independence given class. Gaussian NB models continuous features with class-specific mean/variance; multinomial NB models counts, usually with Laplace smoothing to avoid zero likelihood.

### Ensembles

Bagging trains models independently on bootstrap samples and averages/votes, mainly reducing variance. Random forests also sample features, reducing tree correlation. Boosting trains sequentially to correct errors/residuals, mainly reducing bias but can chase noise.

### Clustering

K-means minimizes squared distance to centroids and assigns hard clusters, favoring spherical equal-scale groups. GMM uses component probabilities, means and covariances; EM alternates responsibilities (E) and weighted parameter updates (M).

## Essential formulas

- Ridge: `min ||y-Xw||² + lambda||w||²`; lasso replaces final term with `lambda||w||_1`.
- Logistic: `p=sigma(w^Tx+b)`; BCE/log loss.
- Entropy `H=-sum p_c log2 p_c`; gain `H(parent)-sum_v (n_v/n)H(v)`.
- Weighted KNN class score `S_c=sum_{i:y_i=c}K(d_i)`.
- Gaussian likelihood `1/(sqrt(2pi)sigma) exp(-(x-mu)²/(2sigma²))`.
- Laplace categorical probability `(count+alpha)/(class_total+alpha*V)`.
- AdaBoost `alpha=.5 ln((1-error)/error)` and normalized exponential weight update.
- SVM decision `sign(w^Tx+b)`; distance `|w^Tx+b|/||w||`; margin width `2/||w||`.
- K-means: assign nearest centroid; update centroid as mean.
- GMM responsibility and weighted mean/variance/mixing updates.

## Question patterns you must solve

### 1. Ridge/lasso scenario

Wording: lambda 0/small/huge; correlated features; few true features; audit requirement.

Answer skeleton: coefficient effect -> bias -> variance -> generalization -> sparsity/audit tradeoff. Ridge never generally sets exact zeros; lasso can.

Reference: **Mar-2026 regular Q1**, makeup Q1. Difficulty easy, 🟠.

### 2. Distance-weighted KNN

1. Encode/scale attributes as instructed; choose mixed-data distance (often Gower) if freedom is given.
2. Compute each distance.
3. Weight `1/d²` (handle d=0 explicitly).
4. Sum weights by class; choose maximum.

Reference: **Mar-2026 regular Q2**. Difficulty medium, 🔴.

### 3. KNN regression vs LWR

KNN estimate is the mean/weighted mean of neighbor targets. LWR starts local parameters and performs weighted least-squares or the specified GD step: `grad=sum_i K(d_i)(yhat_i-y_i)x_i` with factor depending on loss convention.

Reference: **Mar-2026 makeup Q3**. Difficulty medium-hard, 🔴.

### 4. Gaussian/multinomial Naive Bayes

For each class compute prior. Multiply feature likelihoods (or sum logs). Gaussian for continuous; Laplace-smoothed categorical/count likelihood for discrete. Compare unnormalized posteriors; normalization is unnecessary for argmax.

Reference: **Mar-2026 makeup Q2** (Gaussian + gender) and regular Q4 (multinomial + Laplace). Difficulty medium, 🔴.

### 5. AdaBoost iteration

Calculate weighted error; learner weight; multiply sample weights by `exp(-alpha y h(x))`; normalize; identify largest-weight misclassified point.

Reference: **Mar-2026 regular Q3**. Difficulty medium, 🔴.

### 6. Bagging/RF/majority probability

For 3 independent classifiers with accuracy `.7`, majority-correct probability is `.7³+3(.7²)(.3)=.784`. Explain that independence is an assumption; correlation reduces benefit.

Reference: **Mar-2026 makeup Q4**. Difficulty easy-medium, 🔴.

### 7. Gradient boosting residual

Start with current prediction; residual for squared loss is `y-F(x)` (negative gradient up to constant). Fit weak learner to residual; update `F_new=F_old+eta h(x)`.

Reference: **Mar-2026 makeup Q6**. Difficulty medium, 🔴.

### 8. K-means vs GMM/EM

K-means: assign, average. GMM E-step: responsibilities; M-step `N_k=sum gamma`, `pi=N_k/N`, `mu=sum gamma*x/N_k`, variance/covariance weighted likewise.

Reference: **Mar-2026 regular Q6**, makeup Q5. Difficulty medium, 🔴.

### 9. SVM support-vector numerical

Given assumed support vectors on canonical margins, solve their equations for `w,b`; check remaining points satisfy constraints. In dual, support vector iff `alpha_i>0` (soft margin nuances at C). Explain kernel matrix cost roughly O(N²) storage.

Reference: **Mar-2026 makeup Q7**, regular Q5. Difficulty hard, 🔴.

## Definitions to memorize

- Generative classifier models joint/class-conditional distribution; discriminative models boundary/posterior directly.
- MAP maximizes posterior; MLE maximizes likelihood; MAP includes prior.
- Bagging: bootstrap aggregation of independently trained models.
- Boosting: sequential weighted/error-correcting ensemble.
- Support vector: point determining margin with nonzero dual coefficient.
- Interpretability: ability to understand model behavior; explainability: reasons for a prediction (not necessarily causality).

## Common mistakes

- Using unscaled Euclidean distance for mixed units.
- Multiplying many NB probabilities without log space or smoothing.
- Forgetting AdaBoost weight normalization.
- Saying bagging reduces bias primarily.
- Updating K-means centroids before all assignments are made.
- Treating GMM responsibility as a hard label.
- Confusing functional margin with geometric distance.
- Selecting lowest RMSE despite explicit auditability constraint.

## Open-book strategy

Memorize the algorithm skeleton for every recent numerical. Look up only distribution density constants, entropy arithmetic examples, detailed kernel conditions and metric definitions. Build tabs for NB, AdaBoost, EM, SVM and KNN/LWR examples.

The authorized `ML WaterMark.pdf` is 178 pages and covers M1–M11. It is useful for exact algorithm steps and examples but too large for exploratory lookup.

## Final checklist

- [ ] Ridge/lasso bias-variance table.
- [ ] Weighted KNN and one LWR step.
- [ ] Gaussian and multinomial NB.
- [ ] AdaBoost update, RF contrast, majority probability.
- [ ] Gradient boosting residual.
- [ ] K-means and GMM EM iteration.
- [ ] SVM support-vector/margin/kernel numerical.
- [ ] Decision-tree overfit and entropy/gain.
- [ ] Latest regular and makeup papers timed.


## Companion question bank

Use [ML End-Sem Question Bank](ENDSEM_QUESTION_BANK.md) for the 25 fully solved subject questions.

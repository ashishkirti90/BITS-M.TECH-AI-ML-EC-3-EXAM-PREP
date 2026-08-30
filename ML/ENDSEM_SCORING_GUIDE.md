# ML End-Sem Scoring Guide

> **Purpose:** Maximize expected comprehensive-exam marks in a 5–6 day preparation window. This guide follows the reference repository's scoring-guide model: syllabus map, recent-paper signal, priority, formulas, scoring workflows, common mistakes, and open-book strategy.

> **Difficulty warning:** Level A questions in the companion bank are short method drills and are not exam-equivalent alone. Level B contains the required lengthy multi-part questions; Level C contains complete 40-mark mocks. Claim exam readiness only after completing all three levels.
## Official syllabus map

Workflow/preprocessing/evaluation; linear regression and bias-variance; discriminants/logistic regression; decision trees/entropy/MDL; KNN/LWR/RBF; SVM and kernels; Bayesian learning, MLE/MAP, optimal and Naive Bayes; bagging/RF/AdaBoost/gradient boosting/XGBoost; K-means/GMM/EM; model comparison, bias/fairness/interpretability. Comprehensive covers all topics, 40%, 150 minutes.

## Latest-paper blueprint

The latest verified regular paper is a 40-mark, seven-question paper. Its structure is the strongest available indicator:

| Block | Marks | What was tested | Bank preparation |
|---|---:|---|---|
| Q1 | 3 | Lasso versus ensemble under auditability constraints | ML 3, 20, 26, 40 |
| Q2 | 6 | Mixed-data Gower distance, inverse-square KNN, ordinal versus nominal | ML 6, 21, 22 |
| Q3 | 8 | AdaBoost misclassification, weighted error, alpha and interpretation | ML 13, 35 |
| Q4 | 6 | Multinomial NB with Laplace smoothing and repeated tokens | ML 9, 23 |
| Q5 | 8 | SVM overfit diagnosis, C/degree, score, geometric margin, soft margin | ML 17–19, 24, 38–39 |
| Q6 | 6 | K-means update, GMM soft responsibility and model choice | ML 15–16, 36–37 |
| Q7 | 3 | Linear/logistic/tree behavior and stability | ML 4–5, 25, 29 |

The latest makeup reinforces ridge bias–variance, Gaussian NB, KNN versus LWR, bagging/RF/AdaBoost, majority probability, GMM/EM, gradient boosting, SVM and tree depth. The stable core is therefore **instance learning + Bayes + ensembles + clustering + SVM**, with regularized linear/tree reasoning as smaller but efficient marks.

## Twelve-hour scoring plan

| Block | Duration | Topic and output |
|---|---:|---|
| 1 | 45 min | Read priority map; memorize algorithm-selection triggers |
| 2 | 75 min | Ridge/lasso/logistic/tree; solve ML 3–5, 24–29 |
| 3 | 90 min | Gower + weighted KNN; reproduce a complete distance table |
| 4 | 60 min | KNN regression, LWR and RBF; solve ML 7, 30, 31 |
| 5 | 90 min | Gaussian and multinomial NB; MLE/MAP/Bayes optimal |
| 6 | 105 min | Bagging/RF/AdaBoost/gradient boosting; full weight update |
| 7 | 75 min | K-means and GMM/EM; one full 2-D cycle each |
| 8 | 105 min | SVM geometry, C, support vectors and kernels |
| 9 | 45 min | Evaluation, fairness, interpretability and scenario answers |
| 10 | 150 min | Latest regular paper, closed-notes except authorized lookup |
| 11 | 60 min | Mark, create error log, redo every lost-mark calculation |
| 12 | 60 min | Latest makeup selected blocks + final formula retrieval drill |

Do not spend equal time on modules. The five numerical families—Gower/KNN, NB, AdaBoost, EM and SVM—deserve most practice because they recur and provide step marks.

### Three-level completion rule

| Level | Purpose | Completion standard |
|---|---|---|
| A — 40 foundation drills | Learn isolated formulas and algorithm steps | At least 90% correct without worked solution |
| B — 15 full-length questions | Combine numerical, interpretation and changed assumptions | At least 75% of marks on first timed attempt; 100% after correction |
| C — two 40-mark mocks | Simulate paper selection, retrieval and time pressure | At least 32/40 twice, with no unattempted question |

For a 40/40 target, “I understand the solution” is not completion. You must produce it under the time budget, including assumptions, intermediate calculations and contextual conclusion.

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


## Full-mark answer templates

### Template A — Scenario/model-selection question

Write five linked sentences:

1. **Requirement:** identify target type, sample/feature structure and non-negotiable constraint.
2. **Model mechanism:** state what the recommended model optimizes or represents.
3. **Why it fits:** connect mechanism to sparsity, nonlinearity, overlap, latency or auditability.
4. **Trade-off:** name the main limitation and why the alternative may score better on another metric.
5. **Validation:** specify the metric/CV/subgroup or calibration check before deployment.

Avoid empty statements such as “Model X is better.” The latest paper explicitly rewards contextual mechanism and trade-off.

### Template B — Gower plus weighted KNN

1. Declare feature types and ranges.
2. Numeric difference: `|x_i-z_i|/(max_i-min_i)`.
3. Nominal: 0 for match, 1 for mismatch.
4. Ordinal: convert ordered levels to normalized ranks before absolute difference.
5. Average valid per-feature contributions to obtain Gower distance.
6. Compute stated kernel, commonly `1/d²`; handle `d=0` explicitly.
7. Sum weights by class and report prediction plus reason.
8. If a feature changes type, recompute all affected rows and class totals.

### Template C — Naive Bayes

1. Compute class priors.
2. Choose distribution by feature: Gaussian continuous; multinomial counts; categorical probabilities for categories.
3. Apply Laplace smoothing exactly: `(count+alpha)/(class total+alpha V)`.
4. Raise word probabilities to their observed counts.
5. Multiply with prior or add log probabilities.
6. Compare unnormalized scores; normalize only if explicitly asked.
7. State prediction and conditional-independence assumption.

### Template D — AdaBoost

1. Identify misclassified observations.
2. Sum their current weights: `epsilon=sum_mis w_i`.
3. `alpha=.5 ln((1-epsilon)/epsilon)`.
4. Update `w_i exp(-alpha y_i h_i)`.
5. Normalize by total.
6. Identify newly emphasized samples and explain why.
7. Add one strength and one noise/outlier limitation if asked.

### Template E — K-means versus GMM

For K-means, show every point-to-centroid distance, assign all points, then update centroids simultaneously. For GMM:

`gamma_ik = pi_k N(x_i|mu_k,Sigma_k) / sum_j pi_j N(x_i|mu_j,Sigma_j)`

`N_k=sum_i gamma_ik`, `pi_k=N_k/N`, `mu_k=sum gamma_ik x_i/N_k`, and covariance is the responsibility-weighted outer-product average. Finish with: K-means is hard, spherical/distance-based assignment; GMM is probabilistic and can represent unequal covariance/overlap.

### Template F — SVM

1. Score `f(x)=w^Tx+b`; class is its sign.
2. Point-to-boundary distance `|f(x)|/||w||`.
3. Canonical support constraints equal 1: `y_i f(x_i)=1`.
4. Total canonical margin width `2/||w||`; distance from boundary to one margin is `1/||w||`.
5. Large C: violations expensive, lower training bias/higher variance; small C: wider regularized margin.
6. High-degree/RBF flexibility can overfit without tuned C/kernel parameters.
7. In the dual, only nonzero-alpha observations contribute to `w`.
8. Kernel Gram storage is `O(N²)`.

## Quick-reference sheet

| Method | Governing expression | One diagnostic sentence |
|---|---|---|
| Ridge | `SSE+lambda||w||²` | Shrinks correlated coefficients; usually not sparse |
| Lasso | `SSE+lambda||w||₁` | Exact zeros; useful for sparse/auditable model |
| Logistic | `sigma(w^Tx+b)` | Bounded probability with linear feature-space boundary |
| Entropy | `-sum p log2 p` | Zero for pure node; maximum for balanced classes |
| Gower | mean of normalized feature dissimilarities | Correct for mixed numeric/nominal/ordinal data |
| Gaussian NB | prior times product of Gaussian densities | Use class-specific means/variances and log space |
| Multinomial NB | prior times product `P(word|class)^count` | Laplace smoothing prevents zero likelihood |
| AdaBoost | `.5 ln((1-e)/e)` | Sequentially emphasizes difficult observations |
| Majority vote | binomial sum above half | Independence assumption often overstates benefit |
| Gradient boost | `F_new=F+eta h_residual` | Fits negative gradients sequentially |
| K-means | assign nearest, update mean | Hard spherical clusters; scale sensitive |
| GMM | responsibility then weighted M-step | Soft membership and covariance modelling |
| SVM | `sign(w^Tx+b)` | Margin and support vectors determine boundary |

## Authorized open-book index

Use the university-authorized `ML WaterMark.pdf` with physical-page tabs. Its alignment is strong, but it has no useful PDF outline and is inefficient without indexing.

| Physical pages | Bookmark label | Use during exam |
|---:|---|---|
| 34–37 | Ridge/Lasso | Objective and shrinkage/sparsity comparison |
| 39–51 | Logistic | Sigmoid, loss and decision behavior |
| 53–70 | Trees | Entropy, gain, pruning and behavior |
| 72–82 | KNN/LWR | Gower, weighted KNN and local regression |
| 92–104 | Naive Bayes | Gaussian/multinomial and Laplace examples |
| 110–126 | Ensembles | Bagging, RF, AdaBoost and boosting |
| 128–143 | K-means/GMM | Assignment, responsibility and EM steps |
| 144–178 | SVM | Margin, dual, kernels and soft margin |

Do not rely on the slides for regulatory auditability/fairness prose; prepare the short model-selection template from memory. The SVM portion contains repeated material, so tab one good numerical example rather than searching the entire range.

## Exam-hall execution for a 40-mark paper

1. Spend the first 5 minutes classifying every question by algorithm and writing its page-tab beside it.
2. Start with the highest-confidence complete numerical, not automatically Q1.
3. Budget roughly 3–3.5 minutes per mark, retaining 10–15 minutes for checking.
4. For every numerical, write formula → substitution → result → interpretation. Intermediate work protects partial marks.
5. For scenario questions, explicitly connect data fact to model mechanism and trade-off.
6. If arithmetic stalls, preserve method marks: write the remaining formula and symbolic conclusion, then move on.
7. Check NB denominators, AdaBoost normalization, Gower feature types, K-means update order, and SVM margin convention.
8. Use the slides only after identifying the method. Searching before classification wastes open-book time.

## Last-night checklist

- [ ] Complete Gower table with ordinal and nominal variants.
- [ ] Gaussian NB and multinomial NB with repeated counts.
- [ ] AdaBoost error, alpha and normalized weights.
- [ ] Majority-vote probability and bagging/RF explanation.
- [ ] One K-means cycle and one complete GMM E/M cycle.
- [ ] SVM score, distance, canonical margin, C and kernel reasoning.
- [ ] Ridge/lasso and linear/logistic/tree comparison.
- [ ] Ten-second definitions: MLE, MAP, generative, discriminative, support vector, responsibility.
- [ ] All eight page tabs accessible in under 30 seconds.
- [ ] Latest regular paper attempted under 150 minutes and error log retested.

## Companion question bank

Use [ML End-Sem Question Bank](ENDSEM_QUESTION_BANK.md) for the 25 fully solved subject questions.

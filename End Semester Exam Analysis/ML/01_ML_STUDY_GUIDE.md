# ML End-Sem Study Guide

## A. Exam orientation

The current handout makes the comprehensive exam open book, 40% and 2.5 hours. It covers all sessions. The latest papers are application-heavy: a familiar algorithm is placed in a business or engineering context, then the examiner asks for a calculation, a changed assumption, and an interpretation.

**Likely balance from evidence, not a prediction:** roughly two-thirds of the latest marks require numerical or algorithmic work; the rest rewards model choice, diagnosis, trade-offs and interpretation. The safest preparation is to memorize each algorithm skeleton and use the watermark only to verify details.

## B. Priority map

| Topic | Priority | Evidence | Question type | Difficulty | Study time | Expected return |
|---|---|---|---|---|---:|---|
| SVM | 🔴 MUST DO | Both latest: 8 marks | Geometry + C/kernel/dual reasoning | Hard | 2 h | Very high |
| Naive Bayes | 🔴 MUST DO | Both latest: 5-6 marks | Gaussian/multinomial numerical | Medium | 1.5 h | Very high |
| Ensembles | 🔴 MUST DO | Both latest: 6-8 marks | AdaBoost/RF/GB update + compare | Medium | 2 h | Very high |
| KNN/Gower/LWR | 🔴 MUST DO | Both latest: 6 marks | Distance/local fit | Medium-hard | 2 h | Very high |
| K-means/GMM/EM | 🔴 MUST DO | Both latest: 6 marks | One full iteration + interpretation | Medium-hard | 2 h | Very high |
| Ridge/lasso | 🟠 HIGH | Both latest | Bias-variance/audit scenario | Easy | 45 min | Excellent per hour |
| Trees/evaluation | 🟠 HIGH | Recent + recurring | Overfit, entropy, fairness | Easy-medium | 90 min | High |

## C. Concept guide

### 1. KNN, Gower and LWR

**What is it?** KNN predicts from nearby stored examples. Classification votes; regression averages. LWR goes further: it fits a small weighted regression around the query.

**Why important?** Both latest papers gave this family 6 marks. The current style tests mixed feature types, normalization, a distance kernel, and a sensitivity change.

**Understand**

- Distance defines "near"; a bad distance makes the prediction meaningless.
- Numeric features need comparable scale.
- Nominal mismatch is 0/1. Ordinal levels must first become ordered normalized ranks.
- Weighted KNN can let one very close record outweigh many distant records.
- LWR fits a local slope; KNN regression is usually a local constant.

**Memorize**

- Numeric Gower contribution: `|x_j-z_j| / range_j`.
- Gower distance: mean of valid per-feature dissimilarities.
- Kernel requested by the question, often `1/d^2` or Gaussian.
- One-step LWR update under loss `J=1/2 sum K_i(yhat_i-y_i)^2`.

**How tested**

1. Normalize -> compute all distances -> select/use neighbors -> weights -> class/target.
2. Reclassify ordinal as nominal and recompute affected distances.
3. Compare KNN mean with one LWR gradient step.

**Common mistakes:** using raw Euclidean distance across mixed units; normalizing query with a different range; forgetting an exact-match rule when `d=0`; changing weights but not class totals; silently inserting a factor `1/n` in the gradient.

**1-MINUTE REVISION:** types -> normalize -> distance -> kernel -> aggregate -> conclude. KNN is local constant; LWR is local model.

### 2. Naive Bayes, MLE and MAP

**What is it?** Bayes combines a class prior with feature likelihoods. Naive Bayes assumes features are conditionally independent given the class.

**Why important?** Both latest papers use complete numerical variants: multinomial text and Gaussian continuous plus categorical.

**Understand**

- Gaussian NB models a continuous feature using a class-specific mean and variance.
- Multinomial NB models counts; a repeated word raises its likelihood to the count.
- Posterior normalization is unnecessary for an `argmax`, but required if asked for probabilities.
- MLE uses data only; MAP includes a prior and converges toward MLE as evidence grows.

**Memorize**

- `score(c)=P(c) product_j P(x_j|c)`.
- Gaussian density and Laplace smoothing `(count+alpha)/(class-token-total+alpha V)`.
- Work in log space for many features.

**How tested:** priors -> parameter estimates -> likelihoods -> unnormalized scores -> normalize if asked -> predicted class -> assumption.

**Common mistakes:** sample variance when the paper/key uses ML variance; forgetting the repeated-token exponent; using document count instead of class token total; smoothing the prior without instruction; multiplying categorical and continuous features without stating conditional independence.

**1-MINUTE REVISION:** prior x likelihoods; Gaussian for continuous, multinomial for counts, Laplace prevents zero, logs prevent underflow.

### 3. Ensembles

**What is it?** An ensemble combines base learners. Bagging/RF train independently; boosting trains sequentially to correct errors or residuals.

**Why important?** The latest regular has an 8-mark AdaBoost question; the latest make-up tests bagging, RF, majority probability and gradient boosting.

**Understand**

- Bagging diversity comes from bootstrap samples and mainly reduces variance.
- RF adds random feature subsets at splits to reduce tree correlation.
- AdaBoost increases attention to misclassified samples and weights learners by error.
- Gradient boosting fits the negative gradient; for squared loss this is the residual (up to a constant convention).

**Memorize**

- `epsilon_t=sum_{misclassified} w_i`.
- `alpha_t=0.5 ln((1-epsilon_t)/epsilon_t)`.
- `w_i <- w_i exp(-alpha_t y_i h_t(x_i))`, then normalize.
- `F_m=F_{m-1}+eta h_m`; squared-loss target `r_i=y_i-F_{m-1}(x_i)`.
- Majority of 3 independent accuracy-`p` classifiers: `p^3+3p^2(1-p)`.

**How tested:** compute the update, then explain what the new/high old weight means; contrast data randomness with error-driven focus; state the independence assumption.

**Common mistakes:** claiming bagging primarily reduces bias; forgetting normalization; treating the largest old weight as necessarily misclassified now; ignoring correlated errors in majority-vote probability; updating with full residual when `eta` is given.

**1-MINUTE REVISION:** bagging = bootstrap/parallel/variance; RF = bagging + feature randomness; boosting = sequential correction; normalize AdaBoost weights.

### 4. K-means, GMM and EM

**What is it?** K-means gives each point one hard cluster and updates a centroid mean. A GMM represents data with probabilistic Gaussian components. EM alternates soft membership and weighted parameter updates.

**Why important?** This family appears in every extractable end-sem sitting and is worth 6 marks in both latest papers.

**Understand**

- K-means minimizes within-cluster squared distance and prefers spherical, similarly scaled clusters.
- GMM responsibilities are probabilities across components and sum to one for each point.
- EM increases or preserves likelihood but can reach a local optimum.
- Covariance lets GMM represent overlap and elliptical clusters.

**Memorize**

- `gamma_ik = pi_k N(x_i|mu_k,Sigma_k) / sum_l pi_l N(x_i|mu_l,Sigma_l)`.
- `N_k=sum_i gamma_ik`, `pi_k=N_k/N`.
- `mu_k=sum gamma_ik x_i/N_k`.
- `Sigma_k=sum gamma_ik (x_i-mu_k)(x_i-mu_k)^T/N_k`.

**How tested:** calculate all weighted densities and denominators -> responsibilities -> effective counts -> means/variances/mixing weights -> compare with one K-means cycle.

**Common mistakes:** omitting mixture weights in E-step; normalizing across observations rather than components; using old means in the final variance update when the M-step requires new means; updating K-means centroids before all assignments; calling responsibility a class label.

**1-MINUTE REVISION:** K-means is hard distance; GMM is soft density; E-step belongs, M-step updates; every row of responsibilities sums to 1.

### 5. SVM

**What is it?** A linear SVM chooses a separating hyperplane with a wide margin. Support vectors are the training points that determine it. Soft margin trades width against violations; kernels replace dot products to obtain non-linear boundaries.

**Why important?** Verified in every extractable sitting and worth 8 marks in each latest paper.

**Understand**

- Score `f(x)=w^T x+b`; class comes from its sign.
- Point-to-boundary distance is `|f(x)|/||w||`.
- Under canonical scaling, support vectors satisfy `y_i f(x_i)=1`.
- One-sided canonical margin is `1/||w||`; full margin band is `2/||w||`.
- Large `C` penalizes violations strongly; a flexible kernel plus large `C` can overfit.
- In the dual, only `alpha_i>0` points contribute to `w`.

**Memorize**

- Hard margin: minimize `1/2||w||^2`, subject to `y_i(w^Tx_i+b)>=1`.
- Soft margin: add `C sum xi_i`, with `y_i f_i>=1-xi_i`, `xi_i>=0`.
- Dual decision: `sign(sum_i alpha_i y_i K(x_i,x)+b)`.
- Mercer check: Gram matrix symmetric positive semidefinite.

**How tested:** infer boundary from support vectors; solve canonical equations; compute score/norm/margin; discuss C, degree, soft margin, dual support and kernel cost.

**Common mistakes:** mixing distance with total margin width; reversing the class orientation; failing to verify all points; saying a large margin alone is "confidence" for any test point; assuming every valid-looking similarity is a Mercer kernel.

**1-MINUTE REVISION:** score -> norm -> distance/margin -> support constraints -> C/slack -> alpha -> kernel.

### 6. Ridge, lasso, trees and responsible evaluation

**What matters most**

- Ridge (`L2`) shrinks smoothly and usually keeps every coefficient nonzero.
- Lasso (`L1`) can produce exact zeros and is useful for sparse/auditable models.
- Increasing regularization usually raises bias and lowers variance.
- A deep tree with tiny leaves has low training bias and high variance; depth/min-leaf/pruning regularize it.
- Linear regression is unbounded; logistic applies the sigmoid; a tree changes abruptly at split thresholds.
- Preprocessing must be fit on training data only. Leakage inflates test performance.
- Interpretability does not prove fairness or causality.

**1-MINUTE REVISION:** requirement first, metric second. State mechanism, fit to constraint, trade-off, validation check.

## D. Numerical solving templates

### Weighted KNN

`IDENTIFY types -> SCALE numeric/ordinal -> DISTANCE table -> KERNEL -> CLASS/TARGET aggregate -> PREDICTION -> INTERPRET nearest influence`

### Naive Bayes

`COUNT classes -> PRIOR -> DISTRIBUTION per feature -> LIKELIHOODS -> SCORE -> NORMALIZE if asked -> CLASS -> ASSUMPTION`

### AdaBoost

`COMPARE y,h -> EPSILON -> ALPHA -> WEIGHT multipliers -> NORMALIZE -> EXPLAIN newly emphasized samples`

### GMM EM

`WEIGHTED densities -> ROW denominator -> RESPONSIBILITIES -> N_k -> pi/mu/Sigma -> LOG-LIKELIHOOD/INTERPRET`

### SVM

`BOUNDARY/SUPPORTS -> CANONICAL equations -> w,b -> VERIFY labels -> NORM -> DISTANCE/MARGIN -> C/KERNEL interpretation`

## E. Conceptual answer templates

**Explain X:** definition -> mechanism -> governing expression -> useful property -> limitation -> context conclusion.

**Compare A and B:** shared goal -> training difference -> prediction difference -> bias/variance or geometry -> use case -> limitation.

**Justify a model:** non-negotiable requirement -> model mechanism -> why it fits -> explicit trade-off -> validation/governance check.

**Diagnose overfit:** evidence gap between train/test -> complexity source -> bias/variance -> specific regularizer -> how validation confirms improvement.

## F. How to write BITS exam answers

### Numerical

Write `Given`, `Required`, formula, a labeled table, substitutions, intermediate values, final answer and one interpretation sentence. A six-mark distance question should visibly contain distances, weights, class totals and conclusion.

### Derivation

Start with the objective/constraint, state the convention, transform line by line, box the result and verify it against a support point or limiting case.

### Conceptual/comparison/justify

Use a short definition, mechanism, direct answer to the scenario and an explicit trade-off. For three marks, three dense, linked points are usually better than a page of generic prose.

### Algorithm

Use `Input -> initialization -> repeated step -> stopping rule -> output`. Name what changes at each step.

### Diagram/architecture

Label inputs, transformations, learned parameters and output. Refer to the diagram in the explanation; an unlabeled sketch earns little.

### Interpretation

End with what the computed number means in context and the assumption under which the interpretation holds.

## G. Mark-aware depth

| Marks | Expected answer depth |
|---:|---|
| 1-2 | Direct formula/definition plus result or one reason |
| 3-4 | Formula/mechanism, key steps and interpretation |
| 5-6 | Full method, intermediate table/calculations, assumption and conclusion |
| 7-10 | Complete multi-part solution, checks, justification and trade-off |

Where a marking scheme is absent, this depth is inferred from the paper structure.

## H. Open-book strategy

- Know from memory: algorithm recognition, skeleton, core formulas, margin convention, error-update direction.
- Look up: exact Gaussian/EM expression, a long entropy example, detailed SVM dual/KKT, kernel conditions.
- Do not search for: sigmoid, `alpha_t`, nearest-neighbor steps, K-means centroid, or the difference between ridge and lasso.
- Use the verified page map in `06_ML_WATERMARK_INDEX.md`; all page numbers are PDF-viewer pages.


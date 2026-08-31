# ML Watermark Reference Map

> Source: `RESOURCES/ML/ML WaterMark.pdf`. All numbers are **PDF-viewer pages 1-178**, not the four-up printed slide numbers visible inside a page. Representative pp. 37, 72, 94, 117, 141, 147, 155 and 159 were rendered and visually verified.

## Topic map

| Topic | PDF-viewer page(s) | What can be looked up | Know from memory | Must understand |
|---|---:|---|---|---|
| Workflow/data quality | 1-14 | Data types, cleaning, scaling, encoding | Leakage rule | Why distance/GD need scale |
| Linear regression/GD | 15-32 | Cost, closed form, GD variants, metrics | Update skeleton | Loss/gradient direction |
| Bias-variance/regularization | 33-37 | Overfit diagrams, ridge/lasso behavior | L1 vs L2 | Lambda trade-off |
| Linear/logistic classification | 38-51 | Sigmoid, log loss, metrics, multiclass | Sigmoid and boundary | Probability vs linear score |
| Decision trees | 52-70 | Entropy, gain, pruning, continuous values, MDL | Entropy/gain | Depth/variance and split bias |
| KNN and distances | 71-78 | Neighbor notation, examples, normalization, mixed attributes | Distance workflow | Feature type effects |
| LWR | 79-82 | Weighted objective, GD, worked problem type | Local-fit skeleton | Local constant vs local linear |
| Cross-validation | 83-84 | Holdout/LOOCV/K-fold/stratified | Train-only preprocessing | Leakage and model selection |
| MLE/MAP/Bayes optimal | 85-93 | Likelihood steps, MLE examples, weighted hypotheses | Bayes/MLE/MAP distinction | Prior influence |
| Naive Bayes | 94-103 | Categorical, Gaussian, multinomial examples | Score/Laplace/Gaussian | Conditional independence |
| Generative vs logistic | 104-106 | Gaussian generative/logistic relation | One-line contrast | Joint vs conditional modelling |
| Ensemble overview/bagging/RF | 107-116 | Committee, bootstrap, RF feature randomness | Mechanism contrast | Correlation and variance |
| AdaBoost | 117-123 | Error, alpha, update algorithm and examples | Error/alpha/update | Meaning of sample weights |
| Gradient boosting | 124-127 | Residual fitting and learning-rate update | `F+eta h` | Negative-gradient idea |
| K-means | 128-134 | Assign/update, SSE, initialization, limitations | Two-step loop | Hard/spherical assumptions |
| GMM and EM | 135-143 | Mixture equation, responsibilities, M-step, covariance choices | EM formulas | Soft assignment and likelihood |
| SVM geometry | 144-147 | Hyperplane, support vectors, margin | Score/distance/margin | Orientation and scaling |
| SVM primal/dual/KKT | 148-153 | Lagrangian, KKT, alpha, solving examples | `alpha>0` support | Why only SVs matter |
| Soft margin and C | 153-156 | Slack objective and C diagrams | C direction | Width/error trade-off |
| Kernels/Mercer | 157-166 | Feature maps, kernels, PSD, dual replacement | Common kernels | Validity and Gram cost |
| Repeated SVM-II examples | 168-178 | Alternative kernel/example sequence | Do not memorize duplicate pages | Use only if first SVM block is unclear |

## Formula index

| Formula/method | Page |
|---|---:|
| Ridge/lasso behavior and practice | 36-37 |
| Logistic score/loss/update | 41-45 |
| Confusion metrics and ROC | 46-50 |
| Entropy/information gain | 54-59 |
| KNN mixed-distance material | 72-78 |
| LWR weighted objective/GD | 79-82 |
| MLE procedure | 87-92 |
| Naive Bayes worked flow | 94-103 |
| AdaBoost error/alpha/weights | 117-123 |
| Gradient-boosting residual update | 124-126 |
| K-means loop/SSE | 128-134 |
| GMM responsibility and M-step | 140-142 |
| SVM score/margin | 146-147 |
| Dual/KKT/support coefficients | 148-153 |
| Soft-margin primal and C | 154-156 |
| Kernel functions/Mercer | 157-161 |

## PYQ to watermark lookup

| PYQ | Concept | Method | Fast reference |
|---|---|---|---:|
| Latest regular Q1 | Lasso/auditability | L1 sparsity + scenario justification | 36-37 |
| Latest regular Q2 | Gower/weighted KNN | Type -> normalize -> distance -> vote | 72-78 |
| Latest regular Q3 | AdaBoost | error -> alpha -> weight meaning | 117-123 |
| Latest regular Q4 | Multinomial NB | prior -> Laplace -> repeated-token score | 101-103 |
| Latest regular Q5 | SVM C/score/margin | diagnose -> score -> norm -> soft margin | 146-156 |
| Latest regular Q6 | K-means/GMM | hard cycle -> soft responsibility | 128-143 |
| Latest regular Q7 | linear/logistic/tree behavior | output map and boundary form | 39-41, 66 |
| Latest make-up Q1 | Ridge | lambda -> coefficient -> bias/variance | 33-37 |
| Latest make-up Q2 | Gaussian NB | class mean/variance/density -> score | 99-100 |
| Latest make-up Q3 | KNN/LWR | normalize -> neighbors -> one GD step | 79-82 |
| Latest make-up Q4 | Bagging/RF/AdaBoost | diversity -> correlation -> majority | 111-123 |
| Latest make-up Q5 | GMM EM | density -> responsibility -> M-step | 140-143 |
| Latest make-up Q6 | Gradient boost | mean -> residual -> leaf -> shrinkage | 124-126 |
| Latest make-up Q7 | SVM canonical/dual/kernel | geometry -> verify -> norm -> alpha/kernel | 147-166 |
| Latest make-up Q8 | Tree complexity | stopping -> bias/variance | 59-66 |

## Exam-room lookup strategy

### Memorize

- Gower attribute rules, NB score, AdaBoost epsilon/alpha, gradient-boost update.
- K-means and EM step order.
- SVM score, distance, one-sided/full margin and C direction.
- Ridge/lasso and bagging/boosting contrasts.

### Understand

- Why changing feature type changes KNN.
- Why a close neighbor dominates inverse-square voting.
- Why GMM means differ from K-means centers.
- Why class orientation must be checked in an SVM.
- Why correlated ensemble errors reduce the theoretical vote gain.

### Look up

- Gaussian density constant or long NB example: pp. 99-103.
- Full GMM responsibility/M-step: pp. 140-142.
- SVM dual/KKT: pp. 148-153.
- Mercer/kernel feature maps: pp. 157-161.

### Too slow to search during the exam

- "Which algorithm is this?"
- Basic KNN sorting or K-means centroid update.
- Ridge versus lasso, bagging versus boosting.
- Sigmoid or `alpha_t` formula.

## Final exam-hall cheat index

```text
ML
  Regularization -> 36-37
  Logistic/metrics -> 41-50
  Trees -> 54-70
  KNN/Gower -> 72-78
  LWR -> 79-82
  MLE/MAP -> 87-93
  Naive Bayes -> 94-103
  Bagging/RF -> 111-116
  AdaBoost -> 117-123
  Gradient Boosting -> 124-126
  K-means -> 128-134
  GMM/EM -> 140-143
  SVM Geometry -> 146-147
  SVM Dual/KKT -> 148-153
  Soft Margin/C -> 154-156
  Kernels/Mercer -> 157-161
```


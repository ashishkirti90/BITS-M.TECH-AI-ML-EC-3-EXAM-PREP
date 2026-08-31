# ML End-Sem Analysis

> Objective: maximize expected marks in a 5-6 day preparation window. Evidence is restricted to `RESOURCES/ML`; no other subject's patterns were used.

## 1. Source audit and authority

### Authoritative course scope

The current authoritative handout is `RESOURCES/ML/Course Handouts/ML COURSE HANDOUT.docx` (Second Semester 2025-2026, version 2.0). The duplicate handout PDFs contain the same course identity but the DOCX carries the current learning and evaluation plan.

- Course: AIMLC ZG565 Machine Learning, 4 units.
- Comprehensive scope: **all contact sessions 1-16**.
- Current evaluation statement: **open book, 40%, 2.5 hours, 06-09-2026 FN**.
- Upcoming-exam authority: the current handout. Past papers describe their own historic duration, usually 2 hours; do not use that historic duration to override the current handout.
- Permitted resource used in this package: `RESOURCES/ML/ML WaterMark.pdf`, 178 PDF-viewer pages.

### Official syllabus map

| Sessions | Official topics |
|---|---|
| 1-2 | ML introduction, learning-system design, workflow, data, preprocessing, sampling, training/testing, performance metrics |
| 3 | Linear regression, closed form, batch/stochastic/mini-batch GD, basis functions, bias-variance |
| 4-5 | Linear discriminants, decision theory, probabilistic discriminative classifiers, logistic regression, log loss, multiclass |
| 6 | Decision trees, information theory, entropy, overfitting, MDL, continuous/missing attributes |
| 7 | KNN, locally weighted regression, radial basis functions |
| 8 | Mid-course review |
| 9 | Linear/non-linear SVM, soft margin, kernel trick/Mercer, applications |
| 10-11 | MLE, MAP, Bayes rule/optimal classifier, Naive Bayes, generative classifiers, Bayesian linear regression |
| 12-13 | Combining classifiers, bagging, random forest, AdaBoost, gradient boosting, XGBoost |
| 14 | K-means, mixture models, EM, GMM soft clustering |
| 15 | Model comparison, bias, fairness, interpretability |
| 16 | End-course review |

## 2. PYQ collection and deduplication

### Distinct extractable end-sem sittings

| Paper | Structure | Reliable evidence |
|---|---|---|
| Latest EC3 Regular, file dated 01-03-2026 | 7 questions, 40 marks | Full QP + marking key; strongest signal |
| Latest EC3 Make-up, Mar 2026 bundle | 8 questions, 40 marks | Full QP + marking key; second-strongest signal |
| 2023-24 EC3 Regular | Content contains Q1-Q6; cover says 5 questions | Full QP/key text; retain metadata conflict |
| 2023-24 EC3 Make-up | 7 numbered questions | Full QP/key text |
| 2021 EC3 Regular | 8 questions, 40 marks | Full QP/key text |
| 2021 EC3 Make-up | 8 questions, 40 marks | Full QP/key text |

The `Question papers` and `Previous Question Papers` trees contain duplicate copies of the Mar-2026 bundles and the comprehensive sample. Duplicates count once. Sample papers are practice-pattern evidence, not historical occurrence evidence.

### Limited-evidence artifacts

- `2022-23 End Sem ML - shared by senior.docx` is image-only in machine extraction. It is listed but not used for question-number or frequency claims.
- `ML Past Papers.docx` collates screenshots/text fragments from several sittings. It is useful for cross-checking, but an isolated fragment is not treated as a verified actual PYQ unless the original paper supplies the reference.
- `ML Regular AK.pdf` and `ML Makeup AK.pdf` are answer-key artifacts; matching-paper identity must be established before using them as separate sittings.

## 3. Paper blueprints

### Latest EC3 Regular - 40 marks

| Q | Marks | Tested pattern | Mode |
|---|---:|---|---|
| 1 | 3 | Lasso versus ensemble under auditability constraints | Applied conceptual |
| 2 | 6 | Mixed-type Gower distance, inverse-square weighted KNN, ordinal-to-nominal sensitivity | Numerical + interpretation |
| 3 | 8 | AdaBoost error, learner weight, historical sample weights, pros/cons | Numerical + conceptual |
| 4 | 6 | Multinomial NB with Laplace smoothing and repeated tokens | Numerical |
| 5 | 8 | SVM overfit diagnosis, C/degree, score, margin convention, soft margin | Numerical + justification |
| 6 | 6 | One K-means cycle, GMM responsibilities, model choice | Numerical + conceptual |
| 7 | 3 | Linear/logistic/tree output and boundary behavior | Conceptual |

### Latest EC3 Make-up - 40 marks

| Q | Marks | Tested pattern | Mode |
|---|---:|---|---|
| 1 | 4 | Ridge lambda regimes and bias-variance | Conceptual |
| 2 | 5 | Mixed Gaussian/categorical Naive Bayes | Numerical |
| 3 | 6 | Normalized KNN regression versus one LWR GD update | Numerical |
| 4 | 6 | Bagging/RF/AdaBoost diversity and majority probability | Numerical + comparison |
| 5 | 6 | Full GMM E/M update, likelihood, K-means comparison | Numerical |
| 6 | 3 | Gradient-boosting residual tree update | Numerical |
| 7 | 8 | SVM geometry, canonical parameters, dual support vectors, kernel cost | Numerical + derivation |
| 8 | 2 | Tree-depth/leaf-size overfit diagnosis | Conceptual |

## 4. Cross-paper trend analysis

Recent papers receive substantially more weight than older ones. Paper presence is a recurring signal, not an appearance probability.

| Topic family | Evidence across extractable sittings | Recent signal | Trend | Confidence |
|---|---|---|---|---|
| SVM and kernels | Verified in all six distinct sittings | 8 marks in both latest variants | Stable, high-mark | VERY HIGH |
| Bayes/MLE/Naive Bayes | Verified in all six, with changing forms | 6 + 5 marks in latest variants | Increasing applied numerical detail | VERY HIGH |
| KNN/LWR/distance | At least five sittings | 6 marks in both latest variants | Strong mixed-data/local-learning emphasis | VERY HIGH |
| K-means/GMM/EM | Verified in all six | 6 marks in both latest variants | Shift from hard clustering to full soft EM | VERY HIGH |
| Ensembles | Repeated historically; both latest variants | 8 + 6 + 3 marks across latest papers | Wider family: AdaBoost, RF, majority, gradient boost | VERY HIGH |
| Regularization/bias-variance | Historical support plus both latest variants | 3-4 easy marks | Gaining as scenario reasoning | HIGH |
| Decision trees | Repeated across old and new | Short latest Q7/Q8 plus ensemble base learner | Stable, usually efficient marks | HIGH |
| Evaluation/fairness/interpretability | Strong 2023-24 and latest regular | Embedded in model-selection questions | Applied/governance framing increasing | HIGH |
| Workflow/preprocessing | Official scope, scattered paper evidence | Supports leakage/scaling/Gower | Foundation rather than main block | MODERATE |
| RBF and Bayesian linear regression | Official scope | Little clean recent direct evidence | Insufficient PYQ evidence | LOW |
| Genetic algorithms | Mentioned in course description, absent from current session plan | No verified recent question | Scope conflict; skim only | LOW |

## 5. Recent paper signal

1. **Latest regular emphasis:** one applied scenario followed by five algorithm families: Gower/KNN, AdaBoost, multinomial NB, SVM, K-means/GMM, then a short model-behavior question.
2. **Second-latest/make-up emphasis:** ridge, Gaussian NB, KNN/LWR, ensemble diversity, full GMM EM, gradient boosting, SVM, and tree complexity.
3. **Repeated recent structures:** calculate first, interpret second; changed-assumption subparts; scenario constraints that can outweigh raw accuracy; model comparison after a numerical.
4. **Repeated numerical patterns:** normalized distance and weighted vote; likelihood/posterior; boosting error/update; EM responsibility/M-step; margin/decision function.
5. **More prominent now:** mixed feature types, auditability, robustness/generalization, soft versus hard decisions, and explainable model choice.
6. **Older but less central:** long closed-form regression SSE sweeps, unusual hand-built feature maps, and purely theoretical Bayes-optimal votes.
7. **Stable:** SVM, Bayesian learning, instance learning, clustering, and ensemble families.
8. **Insufficient evidence:** an exact future question, exact marks by module, RBF numerical recurrence, Bayesian linear-regression recurrence, and genetic-algorithm inclusion.

## 6. Priority map

| Topic | Priority | Recent evidence | Main question form | Difficulty | Focused time | Expected return |
|---|---|---|---|---|---:|---|
| SVM geometry, soft margin, dual, kernels | 🔴 MUST DO | 8 marks in both latest papers | Compute + justify | Hard | 2.0 h | Very high |
| Naive Bayes: Gaussian + multinomial | 🔴 MUST DO | 6 and 5 marks | Posterior numerical | Medium | 1.5 h | Very high |
| Ensembles: AdaBoost/RF/gradient boost | 🔴 MUST DO | 8, 6 and 3-mark blocks | Update + compare | Medium | 2.0 h | Very high |
| KNN/Gower/LWR | 🔴 MUST DO | 6 marks in both latest papers | Multi-step numerical | Medium-hard | 2.0 h | Very high |
| K-means/GMM/EM | 🔴 MUST DO | 6 marks in both latest papers | Iteration + compare | Medium-hard | 2.0 h | Very high |
| Ridge/lasso/bias-variance | 🟠 HIGH PRIORITY | Both latest papers | Scenario/interpretation | Easy | 0.75 h | Very high per hour |
| Tree complexity + entropy/gain | 🟠 HIGH PRIORITY | Latest plus recurring older | Short concept/numerical | Easy-medium | 1.0 h | High |
| Evaluation, leakage, fairness, interpretability | 🟠 HIGH PRIORITY | Latest regular + 2023-24 | Scenario justification | Easy-medium | 0.75 h | High per hour |
| Logistic versus linear classification | 🟡 SHOULD DO | Latest regular Q7 | Short concept | Easy | 0.4 h | High per hour |
| MLE/MAP/Bayes optimal | 🟡 SHOULD DO | Older recurrence, NB prerequisite | Derivation/concept | Medium | 0.75 h | Moderate-high |
| Workflow/preprocessing | 🟢 LOW PRIORITY | Official; indirect use | Short concept | Easy | 0.4 h | Moderate |
| RBF/Bayesian linear regression/GA | ⚪ OPTIONAL/SKIM | Weak/insufficient recent evidence | Uncertain | Medium | 0.4 h | Low in 5-day route |

## 7. Learning dependencies

1. Scaling and train/test discipline -> Gower/KNN/LWR.
2. Probability, Gaussian density, priors -> Naive Bayes -> GMM responsibilities.
3. Bias-variance and regularization -> tree depth -> bagging/boosting.
4. Linear score and norm -> SVM geometry -> soft margin -> dual -> kernels.
5. K-means hard assignment -> GMM soft assignment -> EM update.

## 8. Source conflicts and corrections

- **Upcoming duration conflict:** current handout says 2.5 hours; historic latest bundles say 2 hours. Use 2.5 hours for planning the upcoming exam unless BITS issues a newer notice.
- **Regular bundle date display:** the actual latest `.doc` filename records 01-03-2026, while the QP/key bundle masks the date and prints a generic 2024-25 cycle. References in this package say "latest EC3 Regular (file dated 01-03-2026)".
- **2023-24 regular question count:** cover says five, extracted content contains Q1-Q6. Do not rely on the cover count for trend arithmetic.
- **Latest make-up Q7 key sign:** the printed canonical `w,b` classifies the stated positive support vector as negative. The corrected orientation is `w=(-0.5,0.5), b=0.5`; the boundary and margin width are unchanged.
- **Genetic algorithms:** present in the prose course description but absent from the current 16-session modular plan. Treat as a scope ambiguity and skim only unless faculty clarifies.

## 9. Self-audit

- [x] Current handout identified and complete syllabus mapped.
- [x] Latest regular/make-up papers analyzed question by question.
- [x] Older papers used for stability, not allowed to dominate recency.
- [x] Duplicate papers excluded from frequency signals.
- [x] Samples excluded from historical frequency counts.
- [x] Unsupported exact-question predictions avoided.
- [x] Conflicts and insufficient evidence stated explicitly.
- [x] Watermark uses PDF-viewer page numbering and was visually spot-verified.
- [x] Important numerical conventions and answer-key discrepancy recorded.


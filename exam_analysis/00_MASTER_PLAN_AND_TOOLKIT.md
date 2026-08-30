# BITS Pilani WILP M.Tech AI & ML - 5-Day End-Sem Master Plan

## EXECUTIVE SUMMARY - WHAT TO DO IF YOU ONLY HAVE 5 DAYS

The highest-return order is **ISM -> ML -> DNN -> MFML**, because the current handouts schedule ISM on **5 Sep 2026 (FN)**, ML on **6 Sep 2026 (FN)**, and DNN on **6 Sep 2026 (AN)**. The MFML handout says **6 Dec 2026 (FN)**, but its surrounding coursework dates are inconsistent with the other S2-25 handouts; verify MFML in eLearn rather than trusting this date blindly.

If the first exam is genuinely only five days away:

1. **ISM:** hypothesis-test selection and calculations; correlation/regression; exponential smoothing/time series; confidence intervals; one-/two-way ANOVA; chi-square; variance-ratio F-test; GMM interpretation.
2. **ML:** SVM; Naive Bayes; KNN/LWR; ensembles; K-means/GMM/EM; ridge/lasso and model-selection reasoning.
3. **DNN:** CNN shapes/parameters; RNN/LSTM/GRU forward calculations and parameter counts; attention; transformers; activations/loss; optimizers/regularization.
4. **MFML:** eigen/diagonalization; rank/basis/subspace; matrix calculus/Hessian; GD with schedules; KKT/Lagrange duality; hard-margin SVM. Add PCA/kernel practice next; keep SVD to a short calculation drill.
5. Solve both **2026 regular and makeup** papers under time pressure. Use older papers only to patch recurring patterns not adequately covered in 2026.

Target split over five full days: **ISM 21%, ML 25%, DNN 27%, MFML 27%**. Because ML and DNN are on the same documented day, do not postpone DNN until after ML.

## Evidence and confidence rules

- **Official:** Current handouts under `Course Handouts/`; these define the syllabus and evaluation scheme.
- **PYQ-derived:** Verified questions in the named paper PDFs. “Frequency” means occurrence in distinct paper sittings where separable; files containing both QP and key count once. Duplicate copies and answer-key companions are not independent evidence.
- **Inference:** Priority and predicted stability combine recency, recurrence, marks, numerical importance, and syllabus centrality. They are not promises of repetition.
- The recent corpus is strongest for 2026 regular/makeup and 2024/25 papers. Some older DNN PDFs are scans with weak text extraction; conclusions from those are lower confidence.

## Current evaluation and exam order

| Subject | Comprehensive | Weight | Duration | Documented date | Resource rule in handout |
|---|---:|---:|---:|---|---|
| ISM | Open book | 40% | 150 min | 05-09-2026 FN | Publisher text/reference books only; “no other learning material” |
| ML | Open book | 40% | 150 min | 06-09-2026 FN | Publisher text/reference books only; “no other learning material” |
| DNN | Open book | 40% | 150 min | 06-09-2026 AN | Publisher text/reference books only; “no other learning material” |
| MFML | Open book | 40% | 150 min | 06-12-2026 FN | Text/reference books plus filed/bound class notes/slides; no loose sheets |

**Confirmed operational rule (user clarification, 30 Aug 2026):** university-watermarked slides are allowed, and these are the course-slide materials to carry. Treat the four watermark PDFs as the authorized slide set. Keep them in the required filed/bound form and follow any centre-specific handling instructions.

## Latest-term regular-paper blueprint (new originals)

These are the highest-recency signals. They correspond to the solution bundles already counted, so they refine marks and structure without increasing frequency denominators.

| Subject | Verified latest structure | Highest-return implication |
|---|---|---|
| MFML | 5 questions x 8 marks: eigen/SVD; vector spaces/rank; inner product + primal/dual/KKT; Hessian/GD with inverse decay; hard-margin SVM | prepare these five blocks as complete methods; KKT is now must-do |
| ISM | 8 blocks x 5 marks: correlation; SES; paired + one-sample tests; randomized-block ANOVA; regression; GMM; CI + white noise; proportions + variance F-test | every 5-mark block is a standard calculation; add two-way ANOVA and F-test drills |
| DNN | 7 questions/120 marks: FFNN 15; binary DFNN 15; CNN 20; RNN/GRU 15; attention 15; transformer 20; optimization/regularization 20 | no major core family is safely skippable; CNN, transformer and training strategy carry the largest blocks |
| ML | 8 verified algorithm blocks from the paired QP/key cycle: lasso/model choice; weighted KNN; AdaBoost; multinomial NB; SVM; K-means/GMM; linear/logistic/tree comparison | prioritize algorithm execution plus scenario justification |

## One-page priority map

| Subject | 🔴 MUST DO | 🟠 HIGH PRIORITY | 🟡 SHOULD DO | 🟢 LOW PRIORITY |
|---|---|---|---|---|
| MFML | eigen/diagonalization; rank-basis-subspace; gradients/Hessian/GD; KKT/Lagrange dual; SVM | PCA; momentum; kernels | SVD; inner products/norms; convexity; Taylor | optimizer prose (AdaGrad/RMSProp/Adam) beyond update rules |
| ISM | hypothesis tests; correlation & regression; time-series forecasting; ANOVA | CI/CLT; chi-square; F-test for variances; GMM | probability/distributions; paired tests; white-noise diagnostics | deep derivations of ARIMA/SARIMAX/VAR; MLE derivations |
| DNN | CNN dimensions/parameters; RNN-LSTM-GRU; attention; transformers | FFNN activations/loss/backprop; optimization; regularization | transfer learning; receptive field; architecture selection | NAS, federated/meta/online learning; detailed time-series architectures |
| ML | SVM; Naive Bayes; ensembles; KNN/LWR; K-means/GMM | ridge/lasso & bias-variance; decision trees; logistic vs linear classification | evaluation/fairness/interpretability; kernel validity | preprocessing taxonomy and generic ML history |

## Six-day timetable (compress Days 5–6 if only five days)

Assume 10 focused hours/day in 50/10 blocks. If only 8 hours are available, preserve practice blocks and shorten reading.

### Day 1 - ISM scoring engine (10 h)

| Block | Work | Duration | Output |
|---|---|---:|---|
| 1 | Test-selection tree: z/t, one/two sample, paired, proportion | 2 h study + 1 h practice | One decision tree; solve 4 tests |
| 2 | Correlation and simple regression, SSE, prediction | 1.5 h + 1 h | Solve 2026 regular correlation/regression and 2026 makeup regression |
| 3 | Simple/Holt smoothing, moving averages, residual white noise | 1.5 h + 1 h | Forecast table completed without notes |
| 4 | CI, one-/two-way ANOVA, chi-square, variance F-test | 1.25 h + 1 h | One worked example each |
| 5 | GMM density + interpretation; 2026 paper scan | 0.25 h | Marked error log and formula tabs |

End-of-day test: identify the correct test in under 30 seconds and complete a standard 5-mark calculation in under 8 minutes.

### Day 2 - ML recent-pattern day (10 h)

| Block | Work | Duration | Output |
|---|---|---:|---|
| 1 | SVM: decision, margin, support vectors, soft margin, dual, kernels | 2 h + 1 h | Solve both 2026 SVM questions |
| 2 | Naive Bayes: categorical, multinomial + Laplace, Gaussian | 1.25 h + 1 h | Two posterior tables |
| 3 | KNN weighted vote; LWR one GD step | 1 h + 0.75 h | Solve both recent instance-based patterns |
| 4 | AdaBoost weights; bagging/RF; gradient boosting residual | 1.25 h + 1 h | One update for each algorithm |
| 5 | K-means vs GMM/EM | 0.75 h | One K-means iteration + one EM M-step |

Revision: 2026 regular paper, 20-minute oral recall of “why this model?” answers.

### Day 3 - DNN computation day (10 h)

| Block | Work | Duration | Output |
|---|---|---:|---|
| 1 | CNN output shape, parameters, flatten/GAP, receptive field | 2 h + 1 h | Solve 2026 regular Q3 and makeup CNN |
| 2 | Vanilla RNN, LSTM, GRU equations and parameter counts | 2 h + 1 h | Solve 2026 regular Q4 and makeup Q2–3 |
| 3 | Attention: scaled dot-product, additive, masks, multi-head dimensions | 1.5 h + 1 h | Solve 2026 regular Q5 |
| 4 | Transformer architecture/parameters/complexity | 1 h + 0.5 h | Draw encoder-decoder from memory |

End output: a two-page formula sheet and a diagram sheet.

### Day 4 - MFML numerical core (10 h)

| Block | Work | Duration | Output |
|---|---|---:|---|
| 1 | rank, basis, subspace, eigenvectors, diagonalization | 2 h + 1 h | Solve 2026 Q1–2 variants |
| 2 | SVD and PCA | 1.5 h + 1 h | One full 2x2/3x2 SVD; one PCA |
| 3 | gradients, Jacobian, chain rule, least-squares gradient | 1.5 h + 1 h | Derive five standard gradients |
| 4 | GD/momentum and convergence | 1 h + 1 h | Two iterations by hand |

### Day 5 - MFML/ML/DNN high-yield completion (10 h)

| Block | Work | Duration | Output |
|---|---|---:|---|
| 1 | MFML SVM hinge objective, kernel matrix/map, KKT/Lagrange | 2 h + 1.5 h | Solve 2024 Q5–6 and one KKT problem |
| 2 | ML ridge/lasso, decision tree, evaluation/interpretability | 1 h + 1 h | Solve 2026 regular Q1/Q7 and makeup Q1/Q8 |
| 3 | DNN activations/loss/backprop, optimizers, regularization | 1.5 h + 1 h | Solve 2026 regular Q1–2, Q7–8 |
| 4 | ISM rapid refresh | 1 h | Re-solve weakest two numerical patterns |

### Day 6 - simulations and retrieval (8–10 h)

- 150 min: latest paper for the earliest exam.
- 45 min: mark it using answer key; record errors by “concept / setup / arithmetic / time.”
- 150 min: combined ML/DNN simulation (75 min each, selected 60 marks).
- 90 min: MFML high-yield selected paper.
- 60 min: bookmark/index permitted resources.
- 45 min: formulas from blank paper, then correct in another color.
- Stop heavy learning 8 hours before sleep.

## Formula checklist

### MFML

- Linear system consistency: `rank(A)=rank([A|b])`; unique if also `rank(A)=n`.
- Eigen: `Av=lambda v`; diagonalization `A=PDP^-1`; symmetric `A=Q Lambda Q^T`.
- SVD: `A=U Sigma V^T`; `A^T A v_i=sigma_i^2 v_i`; `u_i=Av_i/sigma_i`.
- PCA covariance `S=(1/N)XX^T` (or sample convention); projection `z=W^T(x-mu)`; explained ratio `lambda_i/sum lambda`.
- `grad ||Ax-b||^2 = 2A^T(Ax-b)`; `grad (1/2)||Ax-b||^2=A^T(Ax-b)`.
- GD `theta_{t+1}=theta_t-eta grad J`; momentum `v_t=beta v_{t-1}+grad J`, `theta_t=theta_{t-1}-eta v_t` (check course convention).
- Lagrangian `L=f+sum lambda_i g_i+sum nu_j h_j`; KKT feasibility, dual feasibility, stationarity, complementary slackness.
- Soft SVM objective `0.5||w||^2+C sum max(0,1-y_i(w^Tx_i+b))`.
- Dual `max sum alpha_i - 0.5 sum alpha_i alpha_j y_i y_j K(x_i,x_j)`, with `alpha_i>=0`, `sum alpha_i y_i=0`.

### ISM

- `z=(xbar-mu0)/(sigma/sqrt(n))`; one-sample `t=(xbar-mu0)/(s/sqrt(n))`.
- Two independent means: `(xbar1-xbar2-Delta0)/SE`; paired: `t=dbar/(s_d/sqrt(n))`.
- Proportion: `z=(phat-p0)/sqrt(p0(1-p0)/n)`; pooled two-proportion SE under H0.
- CI mean: `xbar +/- z* sigma/sqrt(n)` or `t* s/sqrt(n)`.
- Pearson `r=sum[(x-xbar)(y-ybar)]/sqrt(sum(x-xbar)^2 sum(y-ybar)^2)`.
- Regression `b1=Sxy/Sxx`, `b0=ybar-b1*xbar`; `yhat=b0+b1x`.
- Chi-square `sum (O-E)^2/E`; independence `E_ij=row_i total*col_j total/N`.
- One-way ANOVA `F=MS_between/MS_within`; randomized-block/two-way without replication partitions treatment, block, and error sums of squares.
- Variance comparison `F=s_1^2/s_2^2`, with numerator chosen to match the directional alternative and df `(n_1-1,n_2-1)`.
- SES `F_{t+1}=alpha Y_t+(1-alpha)F_t`; Holt level/trend formulas.
- GMM `p(x)=sum pi_k N(x|mu_k,Sigma_k)`; responsibility `gamma_nk=pi_k N_k/sum_j pi_j N_j`.

### DNN

- Dense parameters `n_in*n_out+n_out`; `z=Wx+b`, `a=f(z)`.
- Sigmoid, tanh, ReLU, leaky ReLU, softmax, binary/multiclass cross-entropy.
- Conv output `floor((N+2P-K)/S)+1`; params `(K_h K_w C_in)C_out+C_out`.
- Receptive field recursion `j_l=j_{l-1}s_l`, `r_l=r_{l-1}+(k_l-1)j_{l-1}`.
- RNN `h_t=tanh(W_xh x_t+W_hh h_{t-1}+b)`; params `h*d+h*h+h`.
- LSTM gates/cell/output; params `4(hd+h^2+h)`; GRU approximately `3(hd+h^2+h)`.
- Attention `softmax(QK^T/sqrt(d_k))V`; multi-head `Concat(head_i)W_O`.
- Transformer FFN parameters approximately `2 d_model d_ff` plus biases; MHA projection weights approximately `4d_model^2`.
- L1/L2; dropout; batch norm; SGD/momentum/RMSProp/Adam update structures.

### ML

- OLS `w=(X^TX)^-1X^Ty`; ridge `(X^TX+lambda I)^-1X^Ty`; lasso objective with `lambda||w||_1`.
- Logistic `p=1/(1+e^-z)`; log loss.
- Entropy `-sum p log2 p`; information gain `H(parent)-sum weighted H(child)`.
- KNN weighted score `sum_{i in class} K(d_i)`, often `K=1/d^2`.
- Gaussian NB density; categorical/multinomial posterior with Laplace smoothing.
- AdaBoost `alpha_t=0.5 ln((1-e_t)/e_t)`; `w_i <- w_i exp(-alpha_t y_i h_t(x_i))`, normalize.
- K-means assignment/centroid update; EM responsibility and weighted parameter updates.
- SVM formulas as above; margin width `2/||w||`, distance `|w^Tx+b|/||w||`.
- Accuracy, precision, recall, specificity, F1; know when each is appropriate.

## Numerical pattern checklist

- [ ] MFML: RREF/rank/basis; eigen/diagonalization; SVD; matrix gradients; two GD/momentum iterations; PCA; hinge objective; kernel matrix; KKT.
- [ ] ISM: one/two/paired t or z; proportion; CI; chi-square; one-way and randomized-block ANOVA; variance F-test; Pearson/regression; SES/Holt/moving average; GMM density/responsibility.
- [ ] DNN: neuron forward pass; dense/CNN/transformer parameter counts; CNN shapes; receptive field; RNN/GRU/LSTM step; attention; gradient flow; dropout/BN interpretation.
- [ ] ML: weighted KNN; LWR step; Gaussian/multinomial NB; AdaBoost update; ensemble majority probability; gradient boosting residual; K-means; EM M-step; SVM margin/decision/support vector.

## Conceptual checklist

- [ ] Select and justify an algorithm from scenario constraints.
- [ ] Explain bias-variance and regularization effects.
- [ ] Distinguish hard/soft assignments; discriminative/generative; linear/kernel.
- [ ] Diagnose overfit/underfit from curves.
- [ ] Explain vanishing/exploding gradients and remedies.
- [ ] Match encoder-only, decoder-only, encoder-decoder to tasks.
- [ ] State null/alternative, assumptions, decision rule, and practical conclusion.
- [ ] Explain why a forecast/test/model is appropriate, not merely compute it.

## Open-book index: exactly what to tab

Use durable tabs labeled with the following short codes. Add a one-page front index mapping each tab to the permitted book/PDF page.

| Subject | Tabs |
|---|---|
| MFML | LA-RREF; EIG; SVD; MCALC; GD; KKT; PCA; SVM-PRIMAL; SVM-DUAL; KERNEL; EX-EIG; EX-GD; EX-SVM |
| ISM | TEST-TREE; Z/T-TABLE; CI; PAIRED; PROP; ANOVA; CHI2; CORR; REG; SES; HOLT; ARIMA-ID; GMM; EX-TEST; EX-FORECAST |
| DNN | ACT-LOSS; BACKPROP; CNN-SHAPE; CNN-PARAM; RFIELD; RNN; LSTM; GRU; ATTENTION; MASK; TRANSFORMER; OPT; REG; EX-CNN; EX-ATTN |
| ML | RIDGE-LASSO; LOGISTIC; TREE; KNN; LWR; NB-GAUSS; NB-LAPLACE; SVM; BOOST; KMEANS; EM-GMM; METRICS; EX-SVM; EX-BOOST |

## Watermark PDF assessment

There is no literal root-level `watermark.pdf`. Four subject files exist:

| File | Pages | What it is | Exam value | Risk |
|---|---:|---|---|---|
| `MFML/MFML watermark.pdf` | 136 | consolidated lecture slides, systems through later MFML modules | high for methods/examples | authorized; bind/file and index |
| `ISM/ISM watermark.pdf` | 261 | comprehensive course slides with examples and formulas | high if indexed; too large to browse | authorized; aggressive tabs essential |
| `DNN/DNNWaterMarked.pdf` | 196 | module slides: NN, CNN, RNN, attention, transformer, optimization, regularization | strong architecture/formula lookup | authorized; index by architecture |
| `ML/ML WaterMark.pdf` | 178 | module slides M1–M11, examples and methods | strong algorithm lookup | authorized; index by algorithm/pattern |

Do not rely on these for basic recall, selecting a method, or searching an unfamiliar topic. Use them for a known tab: formula, architecture diagram, or worked example. Page numbers can change if the PDF is re-exported; write the physical PDF page beside each tab after printing.

## Last 24-hour plan

1. 90 min: ISM test selection + two calculations.
2. 75 min: ML SVM/NB/ensemble recall.
3. 75 min: DNN CNN/RNN/attention formula drill.
4. 60 min: MFML eigen/GD/SVM drill.
5. 60 min: formula dump from memory, correct errors.
6. 45 min: verify tabs, calculator, permitted-resource compliance.
7. 45 min: read error log only; no new topics.
8. Sleep at least 7 hours.

## Exam-hall strategy

- First 8 minutes: scan all questions; label **A** (immediate), **B** (method known), **C** (lookup/heavy).
- Allocate roughly `1.1 minutes per mark`, reserving 15–18 minutes for review.
- Start with high-certainty numericals. Write formula, substitution, arithmetic, conclusion—partial marks survive arithmetic slips.
- Use the book/PDF only after naming the method. If no tab is known within 30 seconds, park the question.
- For statistical tests always write H0/H1, alpha, statistic, critical/p-value decision, contextual conclusion.
- For architecture/model questions explicitly connect the choice to the stated constraint (memory, sequence length, interpretability, imbalance, data size).
- Circle final numerical answers and preserve units/dimensions.
- In the last 15 minutes check signs, normalization, bias terms, parameter-count biases, and whether every subpart has a conclusion.

## Companion guides

- [MFML guide](./01_MFML_STUDY_GUIDE.md)
- [ISM guide](./02_ISM_STUDY_GUIDE.md)
- [DNN guide](./03_DNN_STUDY_GUIDE.md)
- [ML guide](./04_ML_STUDY_GUIDE.md)
- [Evidence audit](./05_REPOSITORY_AUDIT_AND_EVIDENCE.md)

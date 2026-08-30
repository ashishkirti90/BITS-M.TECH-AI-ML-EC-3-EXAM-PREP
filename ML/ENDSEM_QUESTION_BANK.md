# ML End-Sem Question Bank

**Course:** Machine Learning  
**Scope:** Comprehensive/end-semester examination  
**Format:** 20 core solved questions + 5 latest-paper gap-closing questions  
**Evidence:** Official course handout, audited repository material, and verified recent-paper structures

---

## How to use this bank

- Attempt every question before reading its solution.
- Prioritize items labelled MUST DO and latest-paper pattern.
- The numerical values in original drills are practice values; a PYQ-pattern label refers to verified structure, not a claim of verbatim reproduction.
- After each error, bookmark the matching worked example in the authorized watermarked slides.

## Table of contents and exam relevance

| Topic | Questions | Latest-paper signal |
|---|---:|---|
| Workflow, evaluation, bias–variance and regularization | 1–4, 26–27 | Regular Q1/Q7; makeup Q1 |
| Decision trees | 5, 28–29 | Regular Q7; makeup depth/overfit |
| KNN, Gower distance, LWR and RBF | 6–7, 21–22, 30–31 | Regular Q2; makeup Q3 |
| Bayesian learning and Naive Bayes | 8–10, 23, 32–33 | Regular Q4; makeup Q2 |
| Ensembles | 11–14, 34–35 | Regular Q3; makeup Q4/Q6 |
| K-means, GMM and EM | 15–16, 36–37 | Regular Q6; makeup Q5 |
| SVM, soft margin and kernels | 17–19, 24, 38–39 | Regular Q5; makeup Q7 |
| Interpretability, fairness and model selection | 20, 25, 40 | Both latest variants |

**Labels.** `Verified PYQ pattern` means the method and structure were verified in the named paper. `Original drill` means the values are newly created for practice. A star `★` marks a family appearing in both latest regular and makeup cycles.

---

## Core solved questions

### Topic 1 — Workflow, evaluation and regularized linear models

### ML 1 — Leakage-safe workflow [SHOULD DO | Official syllabus]

**Question.** In what order should scaling, cross-validation and testing occur?

**Solution.** Split off the test set first. Within each training fold, fit imputation/scaling/encoding only on that fold and apply to its validation fold. Tune with CV, refit the selected pipeline on all training data, then evaluate once on untouched test data. Fitting preprocessing before splitting leaks validation/test information.

### ML 2 — Metrics under imbalance [HIGH | Recent scenario style]

**Question.** A fraud classifier has 99% accuracy but detects only 10% of fraud. Explain.

**Solution.** Accuracy is dominated by nonfraud. Recall `TP/(TP+FN)=10%` reveals missed fraud. Also report precision, F1, PR-AUC, and a confusion matrix; choose threshold according to false-negative/false-positive costs. ROC-AUC can look optimistic under severe imbalance.

### ML 3 — Ridge versus lasso [HIGH | Both 2026]

**Question.** Choose for many correlated predictors versus a sparse auditable model.

**Solution.** Ridge L2 smoothly shares/shrinks weight among correlated variables and improves stability; it rarely sets exact zeros. Lasso L1 encourages exact sparsity, easing auditability, but may select one variable arbitrarily from a correlated group. Increasing lambda raises bias and lowers variance.

### ML 4 — Linear versus logistic classification [SHOULD DO | Latest regular]

**Question.** Why not ordinary linear regression for a binary target?

**Solution.** Linear predictions are unbounded and squared error does not model Bernoulli likelihood. Logistic regression uses `p=sigmoid(w^Tx+b)` in `[0,1]`, log loss, and a linear decision boundary in feature space. Threshold selection can reflect costs.

### Topic 2 — Decision trees

### ML 5 — Entropy and information gain [HIGH | Tree syllabus/PYQs]

**Question.** A node has 4 positive, 4 negative cases. A split produces two pure children of size 4. Find information gain.

**Solution.** Parent entropy is 1 bit. Each pure child entropy is 0, so weighted child entropy is 0 and gain is 1. Real tree algorithms choose the split with largest gain (or related criterion); deep trees can overfit, controlled by depth/min-leaf/pruning.

### Topic 3 — Instance-based learning: KNN, Gower and LWR

### ML 6 — Distance-weighted KNN [MUST DO | Latest regular]

**Question.** Neighbors: class A at distances 1 and 2; class B at distance 1.5. Use `1/d²`.

**Solution.** A score `1+1/4=1.25`; B score `1/2.25=.444`; predict A. If distance is zero, return the exact neighbor label or use an explicit safeguard. Scale features and use type-aware distances for mixed data.

### ML 7 — KNN regression and LWR [MUST DO | Latest makeup]

**Question.** Neighbor targets 2,4,8 at distances 1,1,2; compute inverse-distance KNN regression. Why might LWR differ?

**Solution.** Weights `1,1,.5`; prediction `(2+4+4)/2.5=4`. LWR fits a local line/plane using distance weights, so it captures a local trend rather than merely averaging targets; it costs optimization per query.

### Topic 4 — Bayesian learning and Naive Bayes

### ML 8 — Gaussian Naive Bayes [MUST DO | Latest makeup]

**Question.** Equal priors; at observed x, class likelihoods are `.20` and `.05`. Predict and find posterior.

**Solution.** Unnormalized scores `.1` and `.025`; predict class 1. Normalized posterior for class 1 is `.1/.125=.8`. For many features use log probabilities to prevent underflow. NB’s conditional-independence assumption is about features given class.

### ML 9 — Multinomial NB with Laplace [MUST DO | Latest regular]

**Question.** In class C, word count is 2, total tokens 10, vocabulary size 5, alpha 1. Find probability.

**Solution.** `(2+1)/(10+1*5)=3/15=.2`. Smoothing prevents a single unseen word from making the entire document likelihood zero. Denominator uses total class-token count plus `alpha*V`.

### ML 10 — MLE versus MAP [SHOULD DO | Official]

**Question.** Distinguish them.

**Solution.** MLE maximizes `p(D|theta)`; MAP maximizes `p(D|theta)p(theta)` and incorporates a prior. In log form, a Gaussian prior on weights corresponds to an L2-like penalty; a Laplace prior corresponds to L1-like regularization. With abundant data the likelihood often dominates.

### Topic 5 — Ensembles

### ML 11 — Bagging and random forests [MUST DO | Latest makeup]

**Question.** Why does a random forest improve on bagged trees?

**Solution.** Bagging fits trees independently on bootstrap samples and averages/votes, reducing variance. Random forests additionally sample candidate features at each split, decorrelating trees. Variance reduction is strongest when individual models are accurate and their errors are not highly correlated.

### ML 12 — Majority-vote probability [MUST DO | Latest makeup]

**Question.** Three independent classifiers each have accuracy `.7`. Probability majority is correct?

**Solution.** Exactly 3 correct plus exactly 2: `.7³+3(.7²)(.3)=.343+.441=.784`. Independence is a simplifying assumption; correlated errors reduce ensemble benefit.

### ML 13 — AdaBoost [MUST DO | Latest regular]

**Question.** Weak learner weighted error `.2`. Find its weight and explain sample update.

**Solution.** `alpha=.5 ln((1-.2)/.2)=.5ln4=.6931`. Update `w_i <- w_i exp(-alpha y_i h_i)` then normalize: misclassified points multiply by `e^alpha=2`, correct points by `e^-alpha=.5`, so the next learner focuses on errors.

### ML 14 — Gradient boosting [MUST DO | Latest makeup]

**Question.** Current predictions `(3,5)`, targets `(5,4)`, squared loss. Residual learner predicts `(1.5,-.5)`, eta `.2`. Update.

**Solution.** Residuals are `(2,-1)`. Update `F_new=F_old+.2h=(3.3,4.9)`. Boosting fits negative gradients/residuals sequentially, unlike bagging’s independent models.

### Topic 6 — K-means, GMM and EM

### ML 15 — K-means iteration [MUST DO | Both recent]

**Question.** Points `{1,2,8,9}`, initial centroids 1 and 8. Perform one iteration.

**Solution.** Assign `{1,2}` to cluster 1 and `{8,9}` to cluster 2; updated centroids are 1.5 and 8.5. Assign all points using old centroids before updating. K-means minimizes within-cluster squared Euclidean distance and is sensitive to scale/outliers/initialization.

### ML 16 — GMM EM M-step [MUST DO | Latest makeup]

**Question.** Points 0 and 2 have component-1 responsibilities `.8,.2`. Update its mixing weight and mean.

**Solution.** `N1=.8+.2=1`; with `N=2`, `pi1=.5`. `mu1=(.8*0+.2*2)/1=.4`. Variance is the responsibility-weighted squared deviation divided by `N1`. GMM membership is soft; K-means uses hard 0/1 assignments.

### Topic 7 — SVM and kernels

### ML 17 — Hard-margin SVM geometry [MUST DO | All extractable cycles]

**Question.** For `w=(3,4),b=-5`, classify `x=(1,1)` and find distance to boundary.

**Solution.** Score `3+4-5=2`, so positive. Distance `|2|/||w||=2/5=.4`. Decision uses score sign; geometric distance divides by norm. Canonical margin width is `2/||w||` only when support constraints equal ±1.

### ML 18 — Soft margin, C and support vectors [MUST DO | Latest]

**Question.** Explain effects of very large and small C.

**Solution.** Large C heavily penalizes violations, tends toward narrower margin/lower training error and greater variance. Small C tolerates violations for a wider, more regularized margin. In the dual, `alpha=0` points do not determine boundary; `0<alpha<C` typically lie on margin; `alpha=C` may lie within margin or be misclassified.

### ML 19 — Kernel reasoning [MUST DO | Latest]

**Question.** Give a feature map for `k(x,z)=(1+xz)^2` in one dimension and explain cost.

**Solution.** Expand `1+2xz+x²z²`; choose `phi(x)=(1,sqrt2x,x²)`, whose dot product equals the kernel. Kernel methods avoid explicit high-dimensional features, but storing an `N x N` Gram matrix costs `O(N²)` memory and training can be expensive for large N.

### Topic 8 — Model selection, interpretability and fairness

### ML 20 — Model selection, fairness and interpretability [HIGH | Latest scenario style]

**Question.** A slightly more accurate ensemble fails an auditability requirement; a sparse logistic model is close in performance. Choose and justify.

**Solution.** Select the sparse logistic model if auditability is a binding constraint, after validating calibration and subgroup metrics. Report the accuracy tradeoff explicitly. Interpretability does not guarantee fairness: compare error rates, recall/precision or other policy-appropriate metrics across relevant groups, inspect data/proxy leakage, and document threshold/cost choices.

---

# Latest-paper gap closure

## ML — five gap-closing questions

### ML 21 — Complete Gower distance [MUST DO | Regular Q2 pattern]

**Latest-paper link:** ML latest regular Q2.

**Question.** Training ranges are age 20–60 and spend 20–100. Query Q is `(age=30, spend=40, job=self, tier=3)`. A is `(34,52,self,tier=2)`. Treat tier ordinal with normalized ranks 1,2,3 and all four features equally. Find Gower distance.

**Solution.** Age difference `|34-30|/40=.1`; spend difference `|52-40|/80=.15`; job difference 0; ordinal-tier difference `|2-3|/(3-1)=.5`. Gower distance `(.1+.15+0+.5)/4=.1875`. With kernel `1/d²`, weight is `1/.1875²=28.444`. Compute each attribute contribution before averaging.

### ML 22 — Ordinal-to-nominal Gower recomputation [MUST DO | Regular Q2(c) pattern]

**Latest-paper link:** ML latest regular Q2(c).

**Question.** Recompute Q16 if tier is nominal.

**Solution.** Different nominal categories contribute 1 instead of .5. New distance `(.1+.15+0+1)/4=.3125`; new weight `1/.3125²=10.24`. The neighbor’s influence falls by `28.444-10.24=18.204`. Recompute **class sums** before deciding whether the final prediction changes; one neighbor’s change alone does not establish the class.

### ML 23 — Full multinomial NB document posterior [MUST DO | Regular Q4 pattern]

**Latest-paper link:** ML latest regular Q4.

**Question.** Equal priors. Vocabulary size 4. Class C total tokens 17 with counts delay 8, refund 6; class I total 15 with counts 1,1. With alpha 1, classify “delay refund refund.”

**Solution.** `P(delay|C)=9/21`, `P(refund|C)=7/21`; `P(delay|I)=2/19`, `P(refund|I)=2/19`. Scores:

`S_C=.5(9/21)(7/21)^2≈.02381`,

`S_I=.5(2/19)(2/19)^2≈.000583`.

Predict C. The repeated word squares its conditional probability. Normalization is unnecessary for argmax; use log scores for long documents.

### ML 24 — SVM overfitting, C and polynomial degree [MUST DO | Regular Q5 pattern]

**Latest-paper link:** ML latest regular Q5.

**Question.** Model A is linear SVM with `C=.1`, train/test 85/84%. Model B uses degree-6 polynomial kernel and `C=100`, train/test 98/72%. Diagnose.

**Solution.** B overfits: its 26-point generalization gap is much larger. Large C strongly penalizes training errors, encouraging a tighter boundary sensitive to noise; degree 6 supplies highly flexible nonlinear interactions. A’s similar train/test scores suggest a simple boundary generalizes better and the data likely contains overlap rather than requiring extreme nonlinear separation. Prefer validation-based C/kernel selection, not training accuracy.

### ML 25 — Tree discontinuity and high-stakes stability [HIGH | Regular Q7 pattern]

**Latest-paper link:** ML latest regular Q7.

**Question.** Why can an input change from `x=4.999` to `x=5.001` abruptly change a tree prediction while logistic regression changes smoothly?

**Solution.** If a tree split is `x<=5`, the two inputs follow different branches and may reach leaves with very different predictions; its function is piecewise constant and discontinuous at thresholds. Logistic probability `sigmoid(wx+b)` is continuous, so a tiny input change ordinarily gives a tiny probability change. Abruptness can harm stability, fairness and user trust near policy thresholds; report sensitivity and consider pruning, ensembles, monotonic constraints or review bands.

---

## Additional full-mark variants

### ML 26 — Ridge closed-form and lambda effect [HIGH | Original drill]

**Problem.** For centered one-feature data with `XᵀX=4` and `Xᵀy=8`, compute the ridge estimate for `lambda=0` and `lambda=4`. Explain the bias–variance change.

**Solution.** Ridge gives `w=(XᵀX+lambda I)⁻¹Xᵀy`. At `lambda=0`, `w=8/4=2`; at `lambda=4`, `w=8/8=1`. Regularization shrinks the coefficient toward zero. This generally increases bias but reduces sensitivity to sampling noise and therefore variance. It does not normally make the coefficient exactly zero—that is the characteristic L1/lasso effect.

**Full-mark line:** “Choose lambda by validation; do not select it using the test set.”

### ML 27 — Confusion matrix and threshold choice [HIGH | Scenario drill]

**Problem.** A fraud model gives `TP=30, FN=10, FP=20, TN=940`. Compute accuracy, precision, recall and F1. Which metric deserves priority if missed fraud is very costly?

**Solution.** Accuracy `(30+940)/1000=.97`; precision `30/(30+20)=.60`; recall `30/(30+10)=.75`; `F1=2(.60)(.75)/(.60+.75)=.6667`. Recall deserves priority when false negatives are costliest, but threshold selection must also quantify the cost of false alarms. The example shows why 97% accuracy can conceal only 75% fraud recall.

### ML 28 — Continuous decision-tree split [SHOULD DO | Original drill]

**Problem.** Sorted one-dimensional observations are `(1,N),(2,N),(5,Y),(6,Y)`. Identify a perfect split and its information gain.

**Solution.** Candidate thresholds lie between adjacent distinct values; `t=3.5` separates the two N cases from the two Y cases. Parent entropy is 1 bit; both children are pure, so weighted child entropy is zero and information gain is 1. A correct answer must state the threshold, resulting children and weighted entropy—not merely “split between 2 and 5.”

### ML 29 — Pre-pruning versus post-pruning [SHOULD DO | Tree family]

**Problem.** Contrast pre-pruning and post-pruning and recommend one safeguard for a small dataset.

**Solution.** Pre-pruning stops growth using maximum depth, minimum samples per split/leaf or minimum impurity decrease. Post-pruning first grows a larger tree and removes weak branches using validation or cost-complexity criteria. For small data, tune depth/min-leaf or cost-complexity alpha inside cross-validation. A shallow tree lowers variance but can underfit.

### ML 30 — KNN regression versus LWR numerical [MUST DO | Makeup Q3 pattern]

**Problem.** At query `x0=2`, observations are `(1,1),(2,2),(3,5)`. (a) Give 3-NN regression. (b) Using weights `K=exp(-(x-x0)²)` fit only a local constant.

**Solution.** (a) Unweighted KNN prediction `(1+2+5)/3=8/3=2.6667`. (b) Weights are `(e⁻¹,1,e⁻¹)≈(.3679,1,.3679)`. Weighted local-constant estimate is `(.3679*1+1*2+.3679*5)/(1+2*.3679)=4.2074/1.7358=2.424`. LWR can instead fit a local slope; always follow the model specified.

### ML 31 — RBF similarity and bandwidth [SHOULD DO | Official syllabus]

**Problem.** Compute `K(x,c)=exp(-||x-c||²/(2sigma²))` for distance 2 and `sigma=1`. Explain small versus large sigma.

**Solution.** `K=exp(-4/2)=e⁻²=.1353`. Small sigma gives narrow, highly local influence and higher variance; large sigma gives broad smooth influence and potentially higher bias. This bandwidth role parallels neighborhood size in KNN.

### ML 32 — Gaussian NB with two features [MUST DO | Makeup Q2 pattern]

**Problem.** Equal priors. For an observation, feature likelihoods under class A are `.4,.5`; under B `.2,.8`. Apply Naive Bayes.

**Solution.** Unnormalized scores: A `.5*.4*.5=.10`; B `.5*.2*.8=.08`. Predict A; normalized posterior is `.10/.18=.5556`. The multiplication assumes conditional independence given class. With raw Gaussian features, calculate each density using its class-specific mean and variance; in long products use logs.

### ML 33 — Bayes-optimal classification [SHOULD DO | Official syllabus]

**Problem.** Two hypotheses have posterior probabilities `.6` and `.4` but predict positive with probabilities `.2` and `.9`. What is the Bayes-optimal probability of positive?

**Solution.** Average predictions over hypothesis uncertainty: `.6(.2)+.4(.9)=.48`. Bayes-optimal classification predicts positive only if the relevant decision threshold is below `.48` (normally `.5`, giving negative). MAP would select only the `.6` hypothesis and output `.2`; Bayes-optimal prediction integrates all hypotheses.

### ML 34 — Random-forest feature sampling [MUST DO | Ensemble concept]

**Problem.** Why does random feature selection help beyond bootstrap bagging?

**Solution.** If one powerful feature appears at every split, bagged trees remain similar and their errors stay correlated. Sampling candidate features forces diverse trees. Averaging correlated models gives limited variance reduction; decorrelation improves the ensemble benefit. The trade-off is that each individual tree may be slightly weaker.

### ML 35 — AdaBoost full weight update [MUST DO | Regular Q3 pattern]

**Problem.** Four samples start with weights `.25`; a learner misclassifies only sample 2. Compute error, learner weight and normalized new weights.

**Solution.** `epsilon=.25`; `alpha=.5 ln(.75/.25)=.5ln3=.5493`. Correct weights multiply by `e^-alpha=.57735`; the incorrect weight by `e^alpha=1.73205`. Unnormalized weights are `(.14434,.43301,.14434,.14434)` with sum `.86603`. Normalized weights are `(1/6,1/2,1/6,1/6)`. The misclassified example now receives half the total attention.

### ML 36 — Two-dimensional K-means cycle [MUST DO | Regular Q6 pattern]

**Problem.** Points `A(1,1),B(2,1),C(7,5),D(8,6)` start with centroids A and D. Perform one complete assignment/update cycle.

**Solution.** A and B are closer to `(1,1)`; C and D to `(8,6)`. Updated centroids are `mu1=((1+2)/2,(1+1)/2)=(1.5,1)` and `mu2=((7+8)/2,(5+6)/2)=(7.5,5.5)`. Assign all points using the old centroids, then update simultaneously. Report the distance metric and tie rule if a tie occurs.

### ML 37 — Full GMM responsibility and M-step [MUST DO | Makeup Q5 pattern]

**Problem.** For points `0,2`, component-1 responsibilities are `.8,.2` and component-2 responsibilities `.2,.8`. Compute mixing weights, means and ML variances.

**Solution.** Effective counts are `N1=N2=1`, hence `pi1=pi2=.5`. `mu1=(.8*0+.2*2)=.4`; `mu2=(.2*0+.8*2)=1.6`. `var1=.8(0-.4)²+.2(2-.4)²=.128+.512=.64`; by symmetry `var2=.64`. Responsibilities are soft assignments; they must sum to one across components for each point.

### ML 38 — Solve canonical SVM parameters [MUST DO | Support-vector pattern]

**Problem.** In one dimension, support points `(x=1,y=-1)` and `(x=5,y=+1)` lie on canonical margins. Find `w,b`, boundary and total margin width.

**Solution.** Solve `w+b=-1` and `5w+b=1`. Subtraction gives `4w=2`, so `w=.5`; then `b=-1.5`. Boundary `wx+b=0` is `x=3`. Total canonical margin width is `2/|w|=4`. Verify the negative and positive support scores are `-1,+1` respectively.

### ML 39 — Kernel Gram matrix and PSD check [MUST DO | Kernel pattern]

**Problem.** For inputs `0,1,2`, compute the Gram matrix of the linear kernel `k(x,z)=xz` and show it is PSD.

**Solution.** `K=[[0,0,0],[0,1,2],[0,2,4]]`. It equals `xxᵀ` for `x=(0,1,2)ᵀ`. For any vector a, `aᵀKa=aᵀxxᵀa=(xᵀa)²>=0`, hence PSD. It has rank one. Valid kernel Gram matrices must be symmetric PSD for every finite input set.

### ML 40 — Cost-aware auditable model selection [HIGH | Regular Q1/Q7 style]

**Problem.** Model A is sparse logistic regression with AUCPR `.61`; Model B is gradient boosting with AUCPR `.65`. Regulation requires traceable feature contributions and stable decisions. Give a defensible selection process.

**Solution.** Do not choose solely from `.04` AUCPR difference. First confirm both estimates with repeated/stratified validation and uncertainty. Evaluate calibration, subgroup precision/recall, stability, latency and cost-weighted errors. If auditability is binding and the performance difference is not operationally material, select A and document coefficients, preprocessing and threshold. If B’s gain is essential, deploy only with an accepted explanation/audit framework and governance approval. Interpretability is not proof of fairness or causality.

## Mastery test

A pattern is mastered only when you can identify the method within 20 seconds, write the governing formula without searching, complete the calculation accurately, state assumptions, interpret the result, and locate a backup example in the watermarked slides within 30 seconds.

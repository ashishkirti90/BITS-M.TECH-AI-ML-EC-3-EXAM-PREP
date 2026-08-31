# ML Question-Pattern Map

## Pattern 1 - Constraint-aware model selection

- **Examiner tests:** whether you can let deployment constraints override a small metric advantage.
- **Typical wording:** "Which model is most appropriate? Justify. Give disadvantages of the alternative."
- **Concepts/formula:** lasso `SSE+lambda||w||_1`; ridge `SSE+lambda||w||_2^2`; auditability, stability, validation.
- **Method:** requirement -> mechanism -> data fit -> trade-off -> validation.
- **Representative PYQ:** latest regular Q1 (3 marks).
- **Difficulty/priority:** Easy; 🟠 HIGH because return/hour is excellent.
- **Common mistake:** choose lowest RMSE without addressing the mandatory constraint.
- **Watermark:** pp. 33-37 for bias/variance and regularization; responsible-model prose is not in this watermark.

## Pattern 2 - Mixed-type weighted KNN

- **Examiner tests:** feature typing, scaling, distance table, weighted aggregation and sensitivity.
- **Typical wording:** "Identify an appropriate distance; compute scores; treat ordinal as nominal."
- **Formula:** numeric Gower `|x-z|/range`; nominal 0/1; ordinal normalized rank; `d=mean(s_j)`; weight as stated.
- **Method:** declare ranges -> per-attribute table -> distance -> weight -> class totals -> recompute only affected fields.
- **Representative PYQ:** latest regular Q2 (6 marks).
- **Difficulty/priority:** Medium-hard; 🔴 MUST DO.
- **Common mistake:** change the tier contribution but not the class-score total.
- **Watermark:** KNN pp. 72-78; LWR pp. 79-82.

## Pattern 3 - KNN regression versus LWR

- **Examiner tests:** nearest-neighbor selection plus one explicit local gradient step.
- **Typical wording:** "Normalize, find k neighbors, give KNN mean, perform exactly one GD update."
- **Formula:** `yhat_KNN=mean(y_i)`; `K_i=exp(-d_i^2/(2b^2))`; gradient from the stated loss.
- **Method:** normalize -> rank neighbors -> mean -> kernel table -> errors -> three weighted sums -> update -> query prediction.
- **Representative PYQ:** latest make-up Q3 (6 marks).
- **Difficulty/priority:** Hard; 🔴 MUST DO.
- **Common mistake:** use every training point when the paper says only the k selected neighbors.
- **Watermark:** pp. 79-82.

## Pattern 4 - Gaussian/multinomial Naive Bayes

- **Examiner tests:** choose the right feature distribution and combine priors/likelihoods.
- **Typical wording:** "Classify a mixed observation" or "classify a repeated-word document with Laplace smoothing."
- **Formula:** Gaussian density; `(count+alpha)/(N_c+alpha V)`; `score=P(c) product likelihood`.
- **Method:** prior -> class parameters/counts -> likelihoods -> unnormalized scores -> normalize if requested -> decision/assumption.
- **Representative PYQs:** latest regular Q4 (6); latest make-up Q2 (5).
- **Difficulty/priority:** Medium; 🔴 MUST DO.
- **Common mistake:** forget a repeated word's exponent.
- **Watermark:** MLE/MAP pp. 85-93; NB pp. 94-103.

## Pattern 5 - AdaBoost update/interpretation

- **Examiner tests:** weighted error, learner weight and why hard samples matter.
- **Typical wording:** "Identify misclassified samples; calculate epsilon/alpha; explain highest weight."
- **Formula:** `epsilon=sum_mis w_i`; `alpha=.5 ln((1-e)/e)`; exponential reweight then normalize when asked.
- **Method:** compare labels/predictions row-wise -> sum -> alpha -> requested weight interpretation.
- **Representative PYQ:** latest regular Q3 (8).
- **Difficulty/priority:** Medium; 🔴 MUST DO.
- **Common mistake:** call the highest incoming weight the current learner's error.
- **Watermark:** pp. 117-123; p. 117 was visually verified.

## Pattern 6 - Bagging/RF/gradient boosting

- **Examiner tests:** mechanisms, correlation and a small probability/residual calculation.
- **Typical wording:** "distinguish diversity sources", "compute majority probability", "update one residual tree."
- **Formula:** majority binomial tail; `r=y-F`; `F_new=F+eta h`.
- **Method:** contrast training order/data/feature randomness; state independence; show residual/leaf table.
- **Representative PYQs:** latest make-up Q4 (6), Q6 (3).
- **Difficulty/priority:** Easy-medium; 🔴 MUST DO.
- **Common mistake:** say RF's feature randomness replaces bootstrapping; it supplements it.
- **Watermark:** overview pp. 108-116; boosting pp. 117-126.

## Pattern 7 - K-means plus GMM/EM

- **Examiner tests:** hard assignment, soft responsibility, parameter update and model selection.
- **Typical wording:** "perform one cycle", "perform E and M steps", "compare updated means."
- **Formula:** responsibility and `N_k,pi_k,mu_k,Sigma_k` updates.
- **Method:** weighted density table -> normalize rows -> effective counts -> all new parameters -> compare hard centers.
- **Representative PYQs:** latest regular Q6 (6), latest make-up Q5 (6).
- **Difficulty/priority:** Medium-hard; 🔴 MUST DO.
- **Common mistake:** compute covariance around the old mean.
- **Watermark:** K-means pp. 128-134; GMM/EM pp. 135-143; p. 141 visually verified.

## Pattern 8 - SVM geometry and canonical scaling

- **Examiner tests:** connect support-vector geometry to `w,b`, score and margin.
- **Typical wording:** "identify boundary from support vectors; satisfy `y_i f_i=1`; compute margin."
- **Formula:** `f=w^Tx+b`; distance `|f|/||w||`; one-sided margin `1/||w||`; total width `2/||w||`.
- **Method:** midpoint/perpendicular -> boundary -> choose class orientation -> solve/scale -> verify support labels -> norm/margin.
- **Representative PYQs:** latest regular Q5 (8), latest make-up Q7 (8).
- **Difficulty/priority:** Hard; 🔴 MUST DO.
- **Common mistake:** preserve the line but reverse the stated classes; always verify `y_i f_i`.
- **Watermark:** geometry pp. 144-147; primal/dual pp. 148-153.

## Pattern 9 - Soft margin, C, kernels and dual

- **Examiner tests:** generalization reasoning around flexibility and computational cost.
- **Typical wording:** "why overfitting", "why soft margin", "which points influence classifier", "kernel cost."
- **Formula:** primal with slack; `w=sum alpha_i y_i x_i`; kernel decision function.
- **Method:** observed train/test gap -> C effect -> kernel flexibility -> overlap/noise -> dual support condition -> cost.
- **Representative PYQs:** latest regular Q5, latest make-up Q7.
- **Difficulty/priority:** Medium-hard; 🔴 MUST DO.
- **Common mistake:** claim high `C` creates a wider margin; it prioritizes fewer violations and commonly narrows it.
- **Watermark:** soft margin pp. 153-156; kernels pp. 157-166 and repeated pp. 168-177.

## Pattern 10 - Short diagnosis/comparison

- **Examiner tests:** one-mark mechanism-linked explanations.
- **Typical wording:** "why outside [0,1]?", "which overfits?", "which changes abruptly?"
- **Concepts:** unbounded linear output, sigmoid, piecewise tree boundary, depth/min-leaf regularization.
- **Method:** direct answer -> mathematical mechanism -> consequence.
- **Representative PYQs:** latest regular Q7 (3), latest make-up Q8 (2).
- **Difficulty/priority:** Easy; 🟠 HIGH return/hour.
- **Common mistake:** write generic definitions without connecting them to the observation.
- **Watermark:** logistic pp. 39-51; trees pp. 52-70.

## Pattern recognition drill

When reading the paper, write one of these tags beside each question: `SELECT`, `DISTANCE`, `NB`, `ADABOOST`, `ENSEMBLE`, `EM`, `SVM-GEO`, `SVM-KERNEL`, `TREE`. If no tag fits within 20 seconds, scan the requested output and givens before opening the watermark.


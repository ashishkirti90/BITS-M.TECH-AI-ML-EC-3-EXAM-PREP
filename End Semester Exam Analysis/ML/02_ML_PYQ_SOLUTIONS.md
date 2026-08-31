# ML Actual PYQ Solution Bank

> All 20 entries below are `[ACTUAL PYQ]`. Wording is compacted only where a long scenario repeats supplied data; numbers, task structure, paper, question number and marks come from the identified paper. Recent papers come first. Sample papers are not represented as actual PYQs.

## Latest EC3 Regular - file dated 01-03-2026

### ML-PYQ-01 - Sparse auditable regression

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q1 | 3 marks  
**Topic/pattern/priority:** Lasso versus ensemble; scenario selection; HIGH.

**Question.** A 60,000-row, 500-feature default-risk regression problem has only 10-15 influential, correlated features. Lasso RMSE is 0.081; an ensemble regressor gives 0.062. Auditability and feature-level explanation are mandatory. Select a model and give two ensemble disadvantages.

**Solution.** Recommend **lasso**, provided the audit constraint is binding. Its `L1` penalty can set irrelevant coefficients exactly to zero, matching the sparse-domain belief. The remaining linear coefficients give a reproducible equation and a direct audit trail. The ensemble's lower RMSE is attractive, but (1) many trees/interactions do not yield one transparent decision equation, and (2) feature importance or local explanations are approximations, not causal contributions, making verification and regulatory justification harder. State the performance trade-off explicitly and validate lasso with repeated/stratified folds and stability of selected features.

**Exam writing:** requirement -> mechanism -> fit -> two disadvantages. **Common mistake:** selecting the smallest RMSE while ignoring the non-negotiable constraint.

### ML-PYQ-02 - Gower distance-weighted KNN

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q2 | 6 marks  
**Topic/pattern/priority:** Mixed data, ordinal sensitivity; MUST DO.

**Given.** Query `Q=(Age 32, Spend 41000, Self-employed, Tier-3)` and five labeled customers. Use all records, equal attribute weights and `K(d)=1/d^2`.

**Required.** (a) Choose distance, compute R1/R2 scores and class. (b) Explain why the smaller class wins. (c) Treat tier as nominal and recompute.

**Method and calculation.** Mixed numeric, nominal and ordinal data implies **Gower distance**. Using training ranges Age `28..50` and Spend `38000..90000`, the official table is:

| ID | Class | age | spend | employment | tier ordinal | `d` | `1/d^2` |
|---|---|---:|---:|---:|---:|---:|---:|
| A2 | R1 | .0909 | .0577 | 0 | 0 | .03715 | 724.56 |
| A4 | R1 | .1818 | .0192 | 0 | .5 | .17526 | 32.56 |
| A0 | R2 | .1364 | .0192 | 1 | 0 | .28890 | 11.98 |
| A1 | R2 | .5909 | .5577 | 1 | .5 | .66215 | 2.28 |
| A3 | R2 | .8182 | .9423 | 1 | 1 | .94012 | 1.13 |

`S_R1=757.12`, `S_R2=15.39`; therefore **R1**. R1 wins because A2 is extremely close and inverse-square weighting makes its contribution dominant.

With tier nominal, the changed rows give A4 `d=.30026,w=11.09` and A1 `d=.78715,w=1.61`; other rows stay the same. New `S_R1=735.65`, `S_R2=14.72`; class remains R1. The assigned-class score decreases by `757.12-735.65=21.47`.

**Exam writing:** show the attribute table; it carries most method marks. **Common mistake:** report the winning margin change when the paper asks for the assigned-class score change.

### ML-PYQ-03 - AdaBoost learner weight and strategy

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q3 | 8 marks  
**Topic/pattern/priority:** AdaBoost; MUST DO.

**Given.** `w=(.1,.3,.15,.45)`, labels `(+,+,-,-)`, current predictions `(+,-,-,-)`.

**Solution.** Only sample 2 is wrong, hence `epsilon_3=.3`. Then

`alpha_3=0.5 ln((1-.3)/.3)=0.5 ln(2.3333)=0.42365 approximately 0.42`.

Sample 4 has the largest **incoming** weight, 0.45. This does not mean learner 3 misclassifies it; it means earlier learners likely found it difficult, so AdaBoost carried its importance into this round. The method sequentially focuses later learners on accumulated hard cases. Advantage: a combination of weak trees can reduce bias and improve accuracy. Limitation: repeatedly emphasizing mislabeled points/outliers can overfit noise.

**Exam writing:** distinguish old weights from the update caused by the current learner. **Common mistake:** inventing a weight-update subpart; this actual question does not request it.

### ML-PYQ-04 - Multinomial Naive Bayes

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q4 | 6 marks  
**Topic/pattern/priority:** Laplace-smoothed text NB; MUST DO.

**Given.** Vocabulary size 4. Complaint has 5 emails/17 tokens with `delay=8, refund=6`; Inquiry has 5 emails/15 tokens with `delay=1, refund=1`. Classify `delay refund refund`, `alpha=1`.

**Solution.** Priors are `P(C)=P(I)=.5`. Smoothed likelihoods:

`P(delay|C)=9/21`, `P(refund|C)=7/21`;  
`P(delay|I)=2/19`, `P(refund|I)=2/19`.

The repeated token is squared:

`S_C=.5(9/21)(7/21)^2=.02381`;  
`S_I=.5(2/19)(2/19)^2=.000583`.

Since `S_C >> S_I`, predict **Complaint**. Normalization is unnecessary because only the argmax is requested.

**Exam writing:** show vocabulary denominator and exponent. **Common mistake:** using number of emails rather than total class tokens in the likelihood denominator.

### ML-PYQ-05 - SVM diagnosis, prediction and margin

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q5 | 8 marks  
**Topic/pattern/priority:** SVM C/degree/geometry; MUST DO.

**Given.** Linear A: `C=.1`, train/test `85/84%`. Polynomial B: `C=100`, degree 6, train/test `98/72%`. For A, `w=(.5,-.3)`, `b=.2`, applicant `x=(2,1)`.

**Solution.** B overfits: very high training and much lower test performance. Large `C` makes violations costly; degree 6 supplies a highly flexible boundary. A's close train/test values support an approximately linear boundary with overlap. The results do **not** prove useful high-degree structure.

`f(x)=.5(2)-.3(1)+.2=.9`, hence positive/default under the paper's label convention. `||w||=sqrt(.25+.09)=sqrt(.34)=.5831`. Under canonical scaling, distance from boundary to either margin is `1/||w||=1.715`; the full margin band is `2/||w||=3.430`. The paper key calls the one-sided value the geometric margin, so state the convention. Soft margin is appropriate because real loan classes overlap and contain noise/outliers.

**Exam writing:** label one-sided versus full width. **Common mistake:** compute applicant distance `.9/.583=1.544` and call it the classifier margin.

### ML-PYQ-06 - K-means and GMM interpretation

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q6 | 6 marks  
**Topic/pattern/priority:** Hard versus soft clustering; MUST DO.

**Given.** `A(1,2),B(2,1),C(2,3),D(6,5),E(7,6),F(8,5)`, initial centers `(1,2),(8,5)`.

**Solution.** Euclidean assignment puts A/B/C in cluster 1 and D/E/F in cluster 2. Update simultaneously:

`mu_1=((1+2+2)/3,(2+1+3)/3)=(1.667,2)`;  
`mu_2=((6+7+8)/3,(5+6+5)/3)=(7,5.333)`.

K-means assigns C entirely to cluster 1. A GMM instead gives C a responsibility for each component based on mixture weight, distance and covariance; the second responsibility can be nonzero. GMM is preferable for overlapping or elliptical/unequal-covariance groups.

**Exam writing:** assignments first, both centroid coordinates second. **Common mistake:** update a centroid while still assigning later points.

### ML-PYQ-07 - Linear, logistic and tree behavior

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Regular, file dated 01-03-2026 | Q7 | 3 marks  
**Topic/pattern/priority:** Model behavior; HIGH return/hour.

**Solution.** (a) Linear regression outputs `w^Tx+b`, which is unbounded; logistic applies `sigma(.)`, mapping any score to `(0,1)`. (b) With less data, the depth-3 tree is most likely to overfit because its piecewise axis-aligned regions are more flexible/high variance; linear and logistic classifiers retain one global linear boundary. (c) The tree changes most abruptly: crossing a split threshold can flip the prediction. Such discontinuity reduces stability and can undermine trust/fairness in high-stakes decisions.

**Exam writing:** one mechanism-linked sentence per mark. **Common mistake:** say logistic has a nonlinear feature-space boundary; its probability is nonlinear but its `.5` boundary is linear.

## Latest EC3 Make-up - Mar 2026 bundle

### ML-PYQ-08 - Ridge lambda regimes

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q1 | 4 marks  
**Topic/pattern/priority:** Ridge/bias-variance; HIGH.

**Solution.** `lambda=0`: OLS, potentially large unstable coefficients, low bias/high variance. `lambda=.01`: mild shrinkage, correlated predictors share influence more smoothly, usually a better balance. `lambda=10^4`: penalty dominates, coefficients approach zero, high bias/low variance and underfit/near-constant prediction. Ridge uses the smooth `L2` penalty `lambda sum beta_j^2`; it shrinks continuously and normally does not create exact zeros. Lasso's `L1` geometry can.

**Exam writing:** coefficient behavior plus bias and variance for every case. **Common mistake:** claim a huge ridge penalty performs feature selection.

### ML-PYQ-09 - Gaussian plus categorical Naive Bayes

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q2 | 5 marks  
**Topic/pattern/priority:** Mixed NB; MUST DO.

**Given.** Pass hours `4.5,7,8,9`, Fail hours `2,4,2.5,3,8.3`; query `(3.5,male)`.

**Solution.** Priors `P(Pass)=4/9`, `P(Fail)=5/9`. Using the paper's ML-variance convention:

`mu_P=7.125`, `var_P=2.796875`; `mu_F=3.96`, `var_F=5.1464`.

Gaussian densities at 3.5 are approximately `.022769` and `.172278`. Gender likelihoods are `P(male|P)=2/4=.5`, `P(male|F)=3/5=.6`.

`S_P=(4/9)(.022769)(.5)=.005060`;  
`S_F=(5/9)(.172278)(.6)=.057426`.

Predict **Fail**. The calculation assumes study hours and gender are conditionally independent given result.

**Exam writing:** state population/ML variance convention. **Common mistake:** change denominator to `n-1` and silently disagree with the paper.

### ML-PYQ-10 - KNN regression versus one LWR update

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q3 | 6 marks  
**Topic/pattern/priority:** Local learning; MUST DO.

**Given.** Query `(Size 7, Warranty 18)`, min-max normalize, `k=4`, Gaussian `b=2`, initial `(w0,w1,w2)=(1.5,.8,.4)`, `alpha=.1`.

**Solution.** Training ranges are size `4..12`, warranty `6..24`; query becomes `(.375,.6667)`. Four nearest records are P7 (`d=.25,y=10`), P2 (`.3333,12`), P1 (`.3560,7.5`), P6 (`.4167,10.5`). Standard 4-NN estimate is `(10+12+7.5+10.5)/4=10`.

With `K=exp(-d^2/(2b^2))`, kernel values are approximately `.9922,.9862,.9843,.9785`. Under the paper's sum-gradient convention, `sum K e=31.2331`, `sum K e x1=10.8541`, `sum K e x2=24.9570`. Therefore

`w_new=(4.6233,1.8854,2.8957)` and  
`yhat_Q=4.6233+1.8854(.375)+2.8957(.6667)=7.2608`.

They differ because KNN uses a flat unweighted mean while LWR performs one incomplete local linear update with distance weights and the specified initialization.

**Exam writing:** declare the loss/gradient convention. **Common mistake:** divide the gradient by four when the key uses a sum.

### ML-PYQ-11 - Bagging, RF, AdaBoost and majority vote

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q4 | 6 marks  
**Topic/pattern/priority:** Ensemble mechanisms; MUST DO.

**Solution.** Bagging independently trains trees on bootstrap samples: diversity is data-sampling randomness. AdaBoost trains sequentially and reweights errors: diversity is error-driven focus. RF retains bootstrapping and, at each split, considers a random feature subset (about `sqrt(30)` in a common classification setting), preventing the same strong feature from dominating every tree and reducing correlation.

For three independent classifiers with `p=.7`, majority correctness is

`P(3)+P(exactly 2)=.7^3+3(.7^2)(.3)=.343+.441=.784`.

Thus the idealized gain is 8.4 percentage points over 0.7. Real gain can be smaller because errors are correlated.

**Exam writing:** explicitly distinguish bootstrap randomness, feature randomness and sequential reweighting. **Common mistake:** omit the independence assumption.

### ML-PYQ-12 - Full two-component GMM EM and K-means

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q5 | 6 marks  
**Topic/pattern/priority:** EM; MUST DO.

**Given.** `X={-4,-2,0,3}`, `pi=(.6,.4)`, `mu=(-3,2)`, variances `(1,1)`.

**Solution.** For each point compute `a_ik=pi_k N(x_i|mu_k,var_k)` and normalize across the two components. Rounded responsibilities are:

| x | gamma1 | gamma2 |
|---:|---:|---:|
| -4 | 1.0000 | 0.0000 |
| -2 | .9996 | .0004 |
| 0 | .1096 | .8904 |
| 3 | 0.0000 | 1.0000 |

The iteration-0 log-likelihood is `sum_i log(sum_k a_ik) approximately -9.9135`. Effective counts `N1=2.1093`, `N2=1.8907`; new weights `.5273,.4727`; means `-2.8443,1.5863`; ML variances `1.3915,2.2445` (rounding as in the key).

K-means with centers `-3,2` assigns `{-4,-2}` and `{0,3}`, giving centers `-3,1.5`. The means differ because GMM uses fractional responsibilities and models variance; K-means uses hard assignments.

**Exam writing:** show the responsibility denominator at least once and state all rows sum to 1. **Common mistake:** omit `pi_k` from the numerator.

### ML-PYQ-13 - Gradient boosting residual tree

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q6 | 3 marks  
**Topic/pattern/priority:** Gradient boosting; MUST DO.

**Given.** Targets `(34,52,28,46,40)`, squared loss, `eta=.2`. Tree leaves: Low traffic A; High and distance <=4 B; other High C.

**Solution.** `F0=mean(y)=40`. Residuals are `(-6,12,-12,6,0)`. Leaf averages: `L_A=(-12+6)/2=-3`; `L_B=-6`; `L_C=(12+0)/2=6`. J2 reaches C, so `F1(J2)=40+.2(6)=41.2`; new residual `52-41.2=10.8`.

**Exam writing:** table job -> residual -> leaf. **Common mistake:** update by 6 instead of `eta*6`.

### ML-PYQ-14 - Canonical SVM from support vectors

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q7 | 8 marks  
**Topic/pattern/priority:** SVM geometry/dual/kernel; MUST DO.

**Given.** Positive P2 `(2,3)`, negative P3 `(4,1)` are the support vectors.

**Solution.** Their midpoint is `(3,2)` and the joining vector is `(2,-2)`, so the boundary is perpendicular to it: `x2=x1-1`, equivalently `x1-x2-1=0`. Because P2 is labeled positive, choose the canonical orientation

`w=(-.5,.5)`, `b=.5`.

Check: `f(P2)=-1+1.5+.5=+1`; `f(P3)=-2+.5+.5=-1`, so `y_i f_i=1`. The decision function is `f(x)=-.5x1+.5x2+.5`. In the dual, support vectors have `alpha_i>0`; other `alpha_i=0`, hence only P2/P3 contribute to `w=sum alpha_i y_i x_i`. `||w||=sqrt(.5)=.7071`; total margin width `2/||w||=2.828`.

Kernel SVM can require an `N x N` Gram matrix: `O(N^2)` storage plus costly optimization.

**Exam writing:** solve the two active margin equations, verify both class labels, then state the boundary, norm and full margin separately. **Source correction:** the supplied key prints the opposite `w,b`, which preserves the same boundary but reverses the stated class labels. Use the verified orientation above. **Common mistake:** accept a boundary without checking the support labels.

### ML-PYQ-15 - Tree stopping and generalization

**[ACTUAL PYQ]** Subject: ML | Session: Latest EC3 Make-up, Mar 2026 | Q8 | 2 marks  
**Topic/pattern/priority:** Tree complexity; HIGH.

**Solution.** Model A (unlimited depth, one-sample leaves, train/test 99/71%) overfits. Model B (depth 4, minimum leaf 25, train/test 86/83%) generalizes better because the stopping conditions reduce the number of partitions, prevent isolation of noise and lower variance. The cost is higher training bias.

**Exam writing:** evidence -> cause -> bias/variance result. **Common mistake:** say lower training accuracy means the model is worse.

## Older recurring signals

### ML-PYQ-16 - Diagnostic Bayes

**[ACTUAL PYQ]** Subject: ML | Session: 2023-24 EC3 Regular | Q1 | 4 marks  
**Topic/pattern/priority:** Bayes theorem; SHOULD DO.

**Given.** `P(Symptom|Meningitis)=.8`, `P(Symptom|no Meningitis)=.1`, `P(Meningitis)=.05`.

**Solution.** `P(S)=.8(.05)+.1(.95)=.04+.095=.135`. Therefore

`P(M|S)=P(S|M)P(M)/P(S)=.04/.135=.2963`.

So the probability is about **29.63%**, despite 80% sensitivity, because prevalence is low and false positives arise from the much larger non-meningitis population.

**Exam writing:** expand the denominator by total probability. **Common mistake:** answer 80%.

### ML-PYQ-17 - Bayes optimal classifier vote

**[ACTUAL PYQ]** Subject: ML | Session: 2021 EC3 Regular | Q1 | 3 marks  
**Topic/pattern/priority:** Bayes optimal prediction; SHOULD DO.

**Given.** Posterior hypothesis weights are `.5,.3,.2`; `h1` predicts win and `h2,h3` predict lose.

**Solution.** Bayes-optimal class probability sums posterior mass of hypotheses producing each class: `P(win|D)=.5`, `P(lose|D)=.3+.2=.5`. The classes are tied. State a tie rule or abstain/request more information; do not invent a unique class.

**Exam writing:** show both weighted sums. **Common mistake:** select `h1` merely because it is the MAP hypothesis; Bayes optimal combines all hypotheses.

### ML-PYQ-18 - One-component GMM by EM

**[ACTUAL PYQ]** Subject: ML | Session: 2021 EC3 Regular | Q3 | 7 marks  
**Topic/pattern/priority:** EM limiting case; SHOULD DO.

**Given.** Data `{-4,-3,-2,-1,0,1,2,3,4}`, one Gaussian, initial `mu=10,var=1`.

**Solution.** With exactly one component, `pi_1=1` and every responsibility is `gamma_i1=1`; that completes the E-step. Thus `N_1=9`. The M-step gives

`mu_new=(sum x_i)/9=0`.

Using ML variance,

`var_new=sum_i (x_i-0)^2/9=(16+9+4+1+0+1+4+9+16)/9=60/9=6.6667`.

After this update, repeating EM changes nothing. The initial values do not trap the solution because there is no latent component ambiguity.

**Exam writing:** explain why all responsibilities are one. **Common mistake:** attempt a two-cluster E-step.

### ML-PYQ-19 - Bernoulli MLE from coin tosses

**[ACTUAL PYQ]** Subject: ML | Session: 2021 EC3 Regular | Q4 | 5 marks  
**Topic/pattern/priority:** MLE derivation; SHOULD DO.

**Given.** 100 tosses contain 30 heads and 70 tails.

**Solution.** Any ordered dataset with 30 head positions has likelihood `p^30(1-p)^70`; there are `C(100,30)` such sequences. For the observed sequence,

`ell(p)=30 ln p+70 ln(1-p)`.

`d ell/dp=30/p-70/(1-p)=0` implies `30(1-p)=70p`, so `p_hat=.3`. The second derivative `-30/p^2-70/(1-p)^2<0`, confirming a maximum.

**Exam writing:** distinguish number of same-count sequences from the likelihood of one ordered dataset. **Common mistake:** multiply the likelihood by the binomial coefficient when the question refers to the exact observed sequence.

### ML-PYQ-20 - KNN sensitivity to K

**[ACTUAL PYQ]** Subject: ML | Session: 2021 EC3 Make-up | Q1 | 5 marks  
**Topic/pattern/priority:** KNN and K sensitivity; SHOULD DO.

**Given.** Eight labeled 2-D points; classify query `(1,1)` using `K=3,5,7`, then combine the three K-results.

**Solution.** Distances: X2, X5, X6 are all 1 and positive; X3/X7 are `sqrt(2)` and negative; X1/X4 are 2 and negative; X8 is `sqrt(5)` and positive. Therefore:

- 3-NN: three positive -> **positive**.
- 5-NN: three positive, two negative -> **positive**.
- 7-NN: three positive, four negative -> **negative**.
- Majority over the three model outputs -> **positive**.

The tie at distance 2 does not affect 7-NN because both tied points are negative. The source key repeats X5 in its 7-neighbor list; the corrected neighbor accounting above preserves its final class.

**Exam writing:** sort distances and show class counts. **Common mistake:** vote over all eight points or ignore a distance tie.

## Bank completion rule

A question is mastered only when you can identify its pattern in 20 seconds, write the governing formula without lookup, obtain the numerical result, state a convention/assumption and locate the backup watermark page in under 30 seconds.

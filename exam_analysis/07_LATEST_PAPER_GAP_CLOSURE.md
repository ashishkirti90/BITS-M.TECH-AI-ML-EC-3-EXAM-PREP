# Latest-Paper Gap-Closure Pack — 20 Detailed Questions

These are original practice questions built from verified **question structures** in the latest regular papers. They do not claim future repetition. Use them after the 80-question bank. Each solution includes the exact method expected for partial and full marks.

## MFML — five gap-closing questions

### 1. Inner-product verification and induced norm

**Latest-paper link:** MFML latest regular Q3(a).

**Question.** Define `<u,v>_M=u^TMv`, where `M=[[3,1],[1,3]]`. Prove this is an inner product and find the induced norm of `(1,-1)`.

**Solution.** Bilinearity follows from matrix multiplication: `<au+bw,v>=a<u,v>+b<w,v>`. Symmetry requires `M=M^T`, which holds. Positive definiteness requires `u^TMu>0` for all nonzero `u`. The leading principal minors are `3>0` and `det(M)=9-1=8>0`; by Sylvester’s criterion, M is positive definite. Hence all inner-product axioms hold. The induced norm is

`||(1,-1)||_M=sqrt([1,-1]M[1,-1]^T)=sqrt(4)=2`.

**Scoring checklist:** linearity, symmetry, positive definiteness, norm calculation. **Trap:** symmetry alone is insufficient.

### 2. Full primal, Lagrangian, dual and KKT

**Latest-paper link:** MFML latest regular Q3(b–d).

**Question.** Minimize `f(x,y)=x²+y²` subject to `x+y>=2`. Derive the dual and solve using KKT.

**Solution.** Put the constraint in standard form `g(x,y)=2-x-y<=0`. Primal: `min x²+y²` subject to `g<=0`. Lagrangian:

`L=x²+y²+lambda(2-x-y)`, `lambda>=0`.

Stationarity for the dual infimum gives `2x-lambda=0`, `2y-lambda=0`, hence `x=y=lambda/2`. Substitute:

`q(lambda)=lambda²/4+lambda²/4+lambda(2-lambda)=2lambda-lambda²/2`.

Dual: maximize `2lambda-lambda²/2` subject to `lambda>=0`. Derivative `2-lambda=0`, so `lambda*=2`; therefore `x*=y*=1`. KKT checks: `2-1-1=0`; `lambda*=2>=0`; stationarity holds; complementarity `2(0)=0`. Primal and dual values are both 2.

**Trap:** choosing `x+y-2>=0` but still using the `g<=0, lambda>=0` convention creates a sign error.

### 3. Regression loss, Hessian and convexity

**Latest-paper link:** MFML latest regular Q4(a–b).

**Question.** For data `(x,y)={(1,2),(2,3)}`, model `yhat=w0+w1x` and `J=1/2 sum(yhat-y)²`. Write J, its gradient and Hessian; prove convexity.

**Solution.** Residuals are `r1=w0+w1-2`, `r2=w0+2w1-3`, so

`J=1/2[(w0+w1-2)²+(w0+2w1-3)²]`.

Gradient:

`dJ/dw0=r1+r2=2w0+3w1-5`,

`dJ/dw1=r1+2r2=3w0+5w1-8`.

Hessian `H=[[2,3],[3,5]]`. Its leading minors are `2>0` and `det(H)=10-9=1>0`, so H is positive definite. Therefore J is strictly convex and has one global minimizer.

### 4. Two GD steps with inverse-decay learning rate

**Latest-paper link:** MFML latest regular Q4(c).

**Question.** Continue Q3 from `(w0,w1)=(0,0)` using `eta_t=eta0/(1+k t)`, `eta0=.1`, `k=.5`, for `t=1,2`.

**Solution.** At step 1, gradient is `(-5,-8)` and `eta1=.1/1.5=.0666667`. Thus

`w^(1)=(0,0)-eta1(-5,-8)=(.333333,.533333)`.

At this point gradient is:

`g0=2(.333333)+3(.533333)-5=-2.733334`,

`g1=3(.333333)+5(.533333)-8=-4.333335`.

`eta2=.1/(1+1)=.05`, hence

`w^(2)=(.333333,.533333)-.05(-2.733334,-4.333335)=(.47,.75)` approximately.

**Exam rule:** calculate the iteration-specific learning rate before updating and retain at least four decimals until the end.

### 5. Rectangular rank versus determinant

**Latest-paper link:** MFML latest regular Q2(c).

**Question.** `B` is a `4x2` matrix with independent columns. State its rank and whether `det(B)` exists.

**Solution.** Independent columns imply column rank 2, the maximum possible because `min(4,2)=2`. A determinant is defined only for a square matrix, so `det(B)` is **not defined**, not zero. If asked about `det(B^TB)`, it is positive because full column rank makes `B^TB` positive definite.

## ISM — five gap-closing questions

### 6. Complete two-component GMM estimates

**Latest-paper link:** ISM latest regular GMM block.

**Question.** Component 1 observations are `{2,4,6}` and component 2 observations `{10,12}`. Using maximum-likelihood variance with divisor `n`, calculate means, variances and mixing coefficients.

**Solution.** `mu1=(2+4+6)/3=4`; squared deviations `4,0,4`, so `sigma1²=8/3=2.6667`. `mu2=11`; squared deviations `1,1`, so `sigma2²=2/2=1`. Total `N=5`, hence `pi1=3/5=.6`, `pi2=2/5=.4`. The fitted density is

`p(x)=.6 N(x|4,8/3)+.4 N(x|11,1)`.

**Trap:** GMM M-step uses ML variance divisor/effective count, not the unbiased sample divisor, unless the question explicitly asks sample variance.

### 7. Residual mean, variance and white noise

**Latest-paper link:** ISM latest regular residual block.

**Question.** Residuals are `{2,-1,0,1,-2,1,-1,0}`. Calculate mean and sample variance. Can white noise be concluded?

**Solution.** Sum is 0, so mean is 0. Sum of squared deviations is `4+1+0+1+4+1+1+0=12`. Sample variance is `12/(8-1)=12/7=1.7143`; population-style variance would be `12/8=1.5`, so state the convention. Zero mean and finite variance are consistent with white noise, but do not prove it. Inspect residual plot/ACF or apply a Ljung–Box-type check; white noise also requires no serial correlation and stable variance.

### 8. Full simple regression and adequacy

**Latest-paper link:** ISM latest regular irrigation regression block.

**Question.** Fit a line to `(x,y)={(1,2),(2,4),(3,5),(4,5)}`. Predict at x=3.5 and comment on adequacy if a residual plot bends systematically.

**Solution.** `xbar=2.5`, `ybar=4`. `Sxx=5`; `Sxy=(-1.5)(-2)+(-.5)(0)+(.5)(1)+(1.5)(1)=5`. Thus `b1=1`, `b0=4-2.5=1.5`; fitted line `yhat=1.5+x`. At 3.5, prediction is 5. A curved residual pattern violates linear-form adequacy even if correlation is high; consider a nonlinear term or a scientifically meaningful saturation model. Never infer causality from fit alone.

### 9. Water-use efficiency reasoning

**Latest-paper link:** ISM latest regular regression application.

**Question.** A fitted yield model is `yhat=1+.5x`, where x is water input. Find predicted yield per unit water and explain whether the model alone gives a finite optimum.

**Solution.** Efficiency is `E(x)=yhat/x=(1+.5x)/x=1/x+.5`, which decreases as x increases for `x>0`. The algebra would favor the smallest x, but extrapolating toward zero is physically invalid and crops require a minimum water threshold. Choose among observed/feasible values using predicted efficiency, yield requirement, uncertainty, and agronomic constraints. This is the contextual reasoning the paper awards marks for.

### 10. Two-way randomized-block decision

**Latest-paper link:** ISM latest regular ANOVA block.

**Question.** In a randomized-block ANOVA, `MS_treatment=18`, `MS_block=7`, `MS_error=2`; critical F values are 4.0 and 3.5 respectively. State both decisions.

**Solution.** `F_treatment=18/2=9>4`, so reject equality of treatment means. `F_block=7/2=3.5`; if rejection requires strictly exceeding the tabulated value, it lies exactly on the boundary—report it as critical/borderline according to the table convention. Treatment and block hypotheses must be tested separately; the no-interaction design uses residual variation after removing both effects.

## DNN — five gap-closing questions

### 11. Additive/Bahdanau attention numerical

**Latest-paper link:** DNN latest regular Q5(b).

**Question.** Use scalar additive scores `e_i=tanh(q+k_i)` with `q=1`, `k1=0`, `k2=1`, values `v1=2,v2=5`. Find context.

**Solution.** `e1=tanh(1)=.7616`; `e2=tanh(2)=.9640`. Stable softmax weights are proportional to `exp(0)` and `exp(.2024)`, giving approximately `.4496,.5504`. Context `=.4496(2)+.5504(5)=3.6512`. General Bahdanau form is `v_a^T tanh(W_q q+W_k k_i+b)`. Unlike dot product, it introduces learned nonlinear scoring parameters.

### 12. GRU gradient highway

**Latest-paper link:** DNN latest regular Q4(c).

**Question.** For `h_t=z_t h_{t-1}+(1-z_t)h_tilde`, ignore candidate-path derivatives. If `dL/dh3=1` and `z2=z3=.9`, find `dL/dh1`.

**Solution.** `dh3/dh2≈z3=.9` and `dh2/dh1≈z2=.9`. Chain rule gives `dL/dh1=1(.9)(.9)=.81`. A high update gate preserves an almost-linear gradient path, mitigating vanishing. Over extremely long sequences `.9^T` still decays, and GRUs may struggle with very distant dependencies.

### 13. Pre-LN versus Post-LN

**Latest-paper link:** DNN latest regular Q6(b)(iii).

**Question.** Compare Pre-LN and Post-LN transformer blocks.

**Solution.** Post-LN commonly computes `y=LN(x+Sublayer(x))`; normalization follows the residual addition. Pre-LN computes `y=x+Sublayer(LN(x))`; the residual stream provides a cleaner identity gradient path, usually making deep training more stable and reducing warm-up sensitivity. Post-LN can sometimes yield strong final representations but is harder to optimize at depth. State the exact ordering with a diagram; do not merely say “one is before.”

### 14. Learning-rate schedule identification

**Latest-paper link:** DNN latest regular Q7(b).

**Question.** Match: X rises sharply then oscillates/drops; Y rises steadily then plateaus early; Z rises, briefly dips, then recovers to best result. Choices: constant high LR, constant low LR, cosine annealing with warm restarts.

**Solution.** X is constant high LR: steps overshoot and oscillate. Y is constant low LR: stable but slow and may plateau within the epoch budget. Z is cosine annealing with warm restarts: periodic LR increases can cause a temporary dip, then exploration and decay reach a better basin. Match the observed mechanism, not just speed.

### 15. Full scenario architecture design

**Latest-paper link:** DNN latest regular Q2.

**Question.** Design a DFNN for four numeric behavioral variables plus one categorical contract feature with three categories, for binary churn.

**Solution.** One-hot contract produces 3 inputs, so total input width is 7 after scaling numeric features. A defensible compact design is `7 -> Dense(32,ReLU) -> Dense(16,LeakyReLU) -> Dense(1,Sigmoid)`, trained with BCE. ReLU is efficient; Leaky ReLU maintains gradient for negative activations; sigmoid models churn probability. Use class weights or resampling if churn recall is poor, and select threshold using business costs. Neuron counts are design choices—marks come from dimensional consistency and justified choices.

## ML — five gap-closing questions

### 16. Complete Gower distance

**Latest-paper link:** ML latest regular Q2.

**Question.** Training ranges are age 20–60 and spend 20–100. Query Q is `(age=30, spend=40, job=self, tier=3)`. A is `(34,52,self,tier=2)`. Treat tier ordinal with normalized ranks 1,2,3 and all four features equally. Find Gower distance.

**Solution.** Age difference `|34-30|/40=.1`; spend difference `|52-40|/80=.15`; job difference 0; ordinal-tier difference `|2-3|/(3-1)=.5`. Gower distance `(.1+.15+0+.5)/4=.1875`. With kernel `1/d²`, weight is `1/.1875²=28.444`. Compute each attribute contribution before averaging.

### 17. Ordinal-to-nominal Gower recomputation

**Latest-paper link:** ML latest regular Q2(c).

**Question.** Recompute Q16 if tier is nominal.

**Solution.** Different nominal categories contribute 1 instead of .5. New distance `(.1+.15+0+1)/4=.3125`; new weight `1/.3125²=10.24`. The neighbor’s influence falls by `28.444-10.24=18.204`. Recompute **class sums** before deciding whether the final prediction changes; one neighbor’s change alone does not establish the class.

### 18. Full multinomial NB document posterior

**Latest-paper link:** ML latest regular Q4.

**Question.** Equal priors. Vocabulary size 4. Class C total tokens 17 with counts delay 8, refund 6; class I total 15 with counts 1,1. With alpha 1, classify “delay refund refund.”

**Solution.** `P(delay|C)=9/21`, `P(refund|C)=7/21`; `P(delay|I)=2/19`, `P(refund|I)=2/19`. Scores:

`S_C=.5(9/21)(7/21)^2≈.02381`,

`S_I=.5(2/19)(2/19)^2≈.000583`.

Predict C. The repeated word squares its conditional probability. Normalization is unnecessary for argmax; use log scores for long documents.

### 19. SVM overfitting, C and polynomial degree

**Latest-paper link:** ML latest regular Q5.

**Question.** Model A is linear SVM with `C=.1`, train/test 85/84%. Model B uses degree-6 polynomial kernel and `C=100`, train/test 98/72%. Diagnose.

**Solution.** B overfits: its 26-point generalization gap is much larger. Large C strongly penalizes training errors, encouraging a tighter boundary sensitive to noise; degree 6 supplies highly flexible nonlinear interactions. A’s similar train/test scores suggest a simple boundary generalizes better and the data likely contains overlap rather than requiring extreme nonlinear separation. Prefer validation-based C/kernel selection, not training accuracy.

### 20. Tree discontinuity and high-stakes stability

**Latest-paper link:** ML latest regular Q7.

**Question.** Why can an input change from `x=4.999` to `x=5.001` abruptly change a tree prediction while logistic regression changes smoothly?

**Solution.** If a tree split is `x<=5`, the two inputs follow different branches and may reach leaves with very different predictions; its function is piecewise constant and discontinuous at thresholds. Logistic probability `sigmoid(wx+b)` is continuous, so a tiny input change ordinarily gives a tiny probability change. Abruptness can harm stability, fairness and user trust near policy thresholds; report sensitivity and consider pruning, ensembles, monotonic constraints or review bands.

## Required execution order

1. Finish the 80-question bank’s MUST DO items.
2. Solve these 20 questions closed-book.
3. For every error, locate and tab the corresponding authorized watermarked-slide example.
4. Solve the actual latest paper under time pressure without its key.
5. Use the key only for marking; redo every lost-mark subpart 24 hours later.

## Readiness standard

You are not ready merely because a solution looks familiar. For each pattern you must be able to: identify the method within 20 seconds, state assumptions, write the governing formula without searching, complete arithmetic accurately, interpret the result in context, and locate a backup example in the watermarked slides within 30 seconds.

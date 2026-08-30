# 80 Solved End-Sem Questions: MFML, ISM, DNN and ML

Use this bank actively: cover the solution, solve on paper, then compare every step. `PYQ pattern` means the structure is verified from the cited paper; the numbers below may be simplified original drills unless explicitly stated. Priority reflects recent papers, not a prediction or guarantee.

## MFML — 20 solved questions

### MFML 1 — RREF, rank and solution type [MUST DO | Original drill]

**Question.** Solve `x+y+z=3`, `2x+2y+2z=6`, `x-y+z=1`. State rank and whether the solution is unique.

**Solution.** Subtract twice row 1 from row 2, giving a zero row. Subtract row 3 from row 1: `2y=2`, so `y=1`. Row 1 then gives `x+z=2`. Let `z=t`; `x=2-t`. Thus `(x,y,z)=(2-t,1,t)`. There are two pivots, so `rank(A)=rank([A|b])=2<3`: infinitely many solutions with one free variable. **Trap:** a zero row does not imply inconsistency; `[0 0 0|c]`, `c!=0`, does.

### MFML 2 — Basis and nullity [MUST DO | 2026 PYQ pattern]

**Question.** For `A=[[1,2,3],[2,4,6]]`, find bases for row space, column space and null space.

**Solution.** RREF is `[[1,2,3],[0,0,0]]`; rank 1 and nullity `3-1=2`. Row-space basis: `{(1,2,3)}`. Pivot column is column 1, so column-space basis must use the **original** column: `{(1,2)^T}`. Solve `x1+2x2+3x3=0`: with `x2=s,x3=t`, `x=(-2s-3t,s,t)`, so null basis `{(-2,1,0),(-3,0,1)}`.

### MFML 3 — Subspace test [MUST DO | 2026 PYQ pattern]

**Question.** Is `W={(x,y,z):x+2y-z=0}` a subspace? Is `V={(x,y,z):x+2y-z=1}`?

**Solution.** `W` is the null space of a linear map, contains zero, and is closed under addition/scaling; hence a subspace. `V` excludes the zero vector and is affine, so it is not a subspace. A basis for `W`: set `y=s,z=t`, giving `x=-2s+t`; basis `{(-2,1,0),(1,0,1)}`.

### MFML 4 — Gram–Schmidt [SHOULD DO | Syllabus coverage]

**Question.** Orthonormalize `v1=(1,1,0)`, `v2=(1,0,1)`.

**Solution.** `e1=v1/||v1||=(1,1,0)/sqrt2`. Remove projection: `u2=v2-(v2·e1)e1=(1,0,1)-(1/2)(1,1,0)=(1/2,-1/2,1)`. Its norm is `sqrt(3/2)`, hence `e2=(1,-1,2)/sqrt6`. Check `e1·e2=0` and both norms are 1.

### MFML 5 — Eigenstructure and diagonalization [MUST DO | Feb/Mar-2026 pattern]

**Question.** Diagonalize `A=[[4,1],[0,2]]`.

**Solution.** `det(A-lambda I)=(4-lambda)(2-lambda)`, so eigenvalues 4 and 2. For 4, `(A-4I)v=0` gives `v1=(1,0)`. For 2, `2x+y=0`, choose `v2=(1,-2)`. Therefore `P=[[1,1],[0,-2]]`, `D=diag(4,2)`, and `A=PDP^-1`. Distinct eigenvalues guarantee independent eigenvectors. Verify quickly with `AP=PD`.

### MFML 6 — Repeated eigenvalue and diagonalizability [MUST DO | Recent pattern]

**Question.** Is `A=[[2,1],[0,2]]` diagonalizable?

**Solution.** Eigenvalue 2 has algebraic multiplicity 2. `A-2I=[[0,1],[0,0]]`, so `y=0` and the eigenspace is span`{(1,0)}`: geometric multiplicity 1. A 2x2 matrix needs two independent eigenvectors, so it is not diagonalizable. **Rule:** geometric multiplicity must equal algebraic multiplicity for every eigenvalue.

### MFML 7 — SVD [SHOULD DO | 2024 and Feb-2026 signal]

**Question.** Find a compact SVD of `A=[[3,0],[0,2],[0,0]]`.

**Solution.** `A^TA=diag(9,4)`. Its orthonormal eigenvectors are `e1,e2`, so `V=I`; singular values are `3,2`. `u1=Av1/3=(1,0,0)`, `u2=Av2/2=(0,1,0)`. Thus compact `U=[[1,0],[0,1],[0,0]]`, `Sigma=diag(3,2)`, `V=I`. **Trap:** singular values are square roots of eigenvalues of `A^TA`.

### MFML 8 — Best rank-one approximation [SHOULD DO | SVD/PCA bridge]

**Question.** For the SVD in Q7, find the best rank-one approximation and its Frobenius error.

**Solution.** Eckart–Young gives `A1=sigma1 u1 v1^T=[[3,0],[0,0],[0,0]]`. The discarded singular value is 2, so `||A-A1||_F=sqrt(sum discarded sigma_i^2)=2`; spectral-norm error is also 2. Keep the largest singular components, never arbitrary entries.

### MFML 9 — Matrix derivative [MUST DO | Recurring calculus pattern]

**Question.** Derive the gradient of `f(w)=||Xw-y||_2^2`.

**Solution.** Expand `(Xw-y)^T(Xw-y)=w^TX^TXw-2y^TXw+y^Ty`. Therefore `grad f=(X^TX+(X^TX)^T)w-2X^Ty=2X^T(Xw-y)`. If the loss is `1/2||Xw-y||^2`, the factor 2 disappears. Always inspect the stated loss convention.

### MFML 10 — Jacobian chain rule [MUST DO | Syllabus/older recurring]

**Question.** Let `z=Wx+b`, `a=sigmoid(z)`, `L=1/2||a-y||^2`. Find `dL/dx`.

**Solution.** Elementwise `dL/da=a-y` and `da/dz=a⊙(1-a)`. Hence `dL/dz=(a-y)⊙a⊙(1-a)`, and `dL/dx=W^T[dL/dz]`. This is backprop: upstream gradient times local derivative, with transposed weight due to dimensions.

### MFML 11 — Hessian classification [MUST DO | Feb-2026 Q4 pattern]

**Question.** Classify the stationary point of `f(x,y)=x^2+4xy+3y^2`.

**Solution.** Gradient `(2x+4y,4x+6y)` is zero only at `(0,0)`. Hessian `H=[[2,4],[4,6]]` has determinant `12-16=-4<0`, so it is indefinite. Therefore `(0,0)` is a saddle, not a minimum. For 2x2 symmetric Hessians: positive leading minor and positive determinant imply positive definite.

### MFML 12 — Taylor approximation [SHOULD DO | Syllabus coverage]

**Question.** Approximate `f(1.1,1.9)` for `f=x^2+y^2` around `(1,2)` using second-order Taylor.

**Solution.** `delta=(0.1,-0.1)`, `f(1,2)=5`, gradient `(2,4)`, Hessian `2I`. Approximation `5+(2,4)·delta+1/2 delta^T(2I)delta =5+(0.2-0.4)+(0.01+0.01)=4.82`. Because the function is quadratic, this is exact.

### MFML 13 — Two gradient-descent iterations [MUST DO | Both 2026 variants]

**Question.** Minimize `f=(x-2)^2+(y+1)^2`, start `(0,0)`, learning rate `.25`; give two iterates.

**Solution.** Gradient `(2(x-2),2(y+1))`. At `(0,0)`, gradient `(-4,2)`, so `(x1,y1)=(1,-.5)`. Next gradient `(-2,1)`, so `(x2,y2)=(1.5,-.75)`. Each coordinate halves its error. **Trap:** GD subtracts the gradient.

### MFML 14 — Momentum [MUST DO | Mar-2026 pattern]

**Question.** Using `v_t=beta v_{t-1}+grad f(theta_{t-1})`, `theta_t=theta_{t-1}-eta v_t`, solve Q13 for two steps with `beta=.5`, `eta=.25`, `v0=0`.

**Solution.** `g0=(-4,2)`, `v1=(-4,2)`, `theta1=(1,-.5)`. Then `g1=(-2,1)`, `v2=.5(-4,2)+(-2,1)=(-4,2)`, so `theta2=(2,-1)`, the optimum. State the convention because some texts put learning rate inside velocity.

### MFML 15 — Convexity [MUST DO | Feb-2026 pattern]

**Question.** Is `f(x,y)=e^x+y^2` convex?

**Solution.** Hessian is `diag(e^x,2)`, positive definite for every `(x,y)` because both diagonal entries are positive. Thus it is strictly convex, so any stationary point, if one exists, is the unique global minimizer. Here `df/dx=e^x` never vanishes, so no unconstrained finite minimizer exists.

### MFML 16 — Equality-constrained Lagrange method [MUST DO | Latest regular Q3 pattern]

**Question.** Minimize `x^2+y^2` subject to `x+y=2`.

**Solution.** `L=x^2+y^2+lambda(x+y-2)`. Stationarity: `2x+lambda=0`, `2y+lambda=0`, hence `x=y`. Feasibility gives `x=y=1`; `lambda=-2`. Convex objective plus affine constraint makes this the global optimum, value 2.

### MFML 17 — KKT inequality [MUST DO | Latest regular Q3]

**Question.** Minimize `(x-3)^2` subject to `x<=1`.

**Solution.** Write `g(x)=x-1<=0`, `L=(x-3)^2+lambda(x-1)`. KKT: feasibility `x<=1`; dual feasibility `lambda>=0`; stationarity `2(x-3)+lambda=0`; complementarity `lambda(x-1)=0`. Unconstrained optimum 3 is infeasible, so constraint is active: `x*=1`; stationarity gives `lambda*=4`, satisfying all conditions.

### MFML 18 — PCA [HIGH | Mar-2026/older recurring]

**Question.** Data points are `(1,1),(2,2),(3,3)`. Find the first principal direction and projected scores.

**Solution.** Mean `(2,2)`; centered rows `(-1,-1),(0,0),(1,1)`. Covariance is proportional to `[[1,1],[1,1]]`, whose top normalized eigenvector is `(1,1)/sqrt2`; the orthogonal eigenvalue is zero. Scores are `-sqrt2,0,sqrt2` (sign may reverse). PCA must be performed after centering.

### MFML 19 — Hard-margin SVM [MUST DO | Latest regular Q5]

**Question.** In one dimension, closest negative point is `x=1` and closest positive point is `x=3`. Find canonical `w,b`, boundary, support vectors and margin width.

**Solution.** With labels `-1,+1`, canonical support equations are `w(1)+b=-1`, `w(3)+b=1`. Subtract: `2w=2`, so `w=1`, `b=-2`. Boundary `wx+b=0` is `x=2`. Both points are support vectors. Margin width is `2/|w|=2`.

### MFML 20 — Hinge loss and kernel Gram matrix [MUST DO | 2024/2026 pattern]

**Question.** (a) For `w=1,b=-2`, compute hinge loss for `(x,y)=(2.5,+1)`. (b) For `x={0,1}`, compute the Gram matrix of `k(x,z)=(1+xz)^2`.

**Solution.** (a) Functional margin is `y(wx+b)=.5`, so hinge `max(0,1-.5)=.5`; correctly classified but inside margin. (b) `K=[[k(0,0),k(0,1)],[k(1,0),k(1,1)]]=[[1,1],[1,4]]`. It is symmetric PSD (determinant 3>0). A feature map is `[1,sqrt2 x,x^2]`.

## ISM — 20 solved questions

### ISM 1 — Conditional probability and Bayes [SHOULD DO | Syllabus coverage]

**Question.** Disease prevalence is 1%, sensitivity 95%, specificity 90%. Find `P(disease|positive)`.

**Solution.** `P(+)=.95(.01)+.10(.99)=.1085`. Bayes gives `.0095/.1085=.0876`. Despite good sensitivity, most positives are false because prevalence is low. **Trap:** do not confuse `P(+|D)` with `P(D|+)`.

### ISM 2 — Binomial distribution [SHOULD DO | Older recurring]

**Question.** If defect probability is `.1`, find probability of exactly two defects among five independent items.

**Solution.** `P(X=2)=C(5,2)(.1)^2(.9)^3=10(.01)(.729)=.0729`. Conditions: fixed trials, independent, two outcomes, constant probability.

### ISM 3 — CLT and standard error [HIGH | 2026 CI signal]

**Question.** A population has mean 50, SD 12. For `n=36`, approximate `P(48<sample mean<52)`.

**Solution.** By CLT, standard error `12/sqrt36=2`. Z bounds are `-1,+1`, so probability `Phi(1)-Phi(-1)=.6827`. CLT concerns the sampling distribution of the mean, not individual observations.

### ISM 4 — Confidence interval [HIGH | Both 2026]

**Question.** `n=100`, mean 20, known SD 5. Find a 95% CI for the population mean.

**Solution.** `20 ±1.96(5/sqrt100)=20±.98`, so `(19.02,20.98)`. Interpretation: the method captures the fixed population mean in 95% of repeated samples; it is not a 95% probability statement about this already-computed fixed interval.

### ISM 5 — One-sample z test [MUST DO | Latest papers]

**Question.** Test `H0:mu=100` vs `H1:mu<100` with `n=64`, mean 98, known SD 8, `alpha=.05`.

**Solution.** `z=(98-100)/(8/8)=-2`. Lower critical value `-1.645`; reject H0. There is evidence the mean is below 100. The one-sided p-value is about `.0228`. State the alternative before seeing the statistic.

### ISM 6 — One-sample t test [MUST DO | Mar-2026 pattern]

**Question.** `n=16`, mean 52, sample SD 4; test `mu=50` two-sided at 5%.

**Solution.** `t=(52-50)/(4/4)=2`, df 15. Critical magnitude is about 2.131, so fail to reject H0. Evidence is insufficient at 5%, even though the sample mean differs numerically.

### ISM 7 — Paired t test [MUST DO | Feb-2026 Q3]

**Question.** Before–after differences are `2,3,1,2,2`. Test whether mean improvement is positive.

**Solution.** Mean difference `2`; deviations `0,1,-1,0,0`, so sample variance `2/4=.5`, `s=.7071`. `SE=.7071/sqrt5=.3162`; `t=6.325`, df 4. This strongly supports positive improvement. Pair first, then analyze differences; never treat paired observations as independent samples.

### ISM 8 — Two independent means [MUST DO | Mar-2026 makeup]

**Question.** Two large independent samples: `n1=n2=50`, means 75 and 72, SDs 5 and 4. Test equality two-sided.

**Solution.** `SE=sqrt(25/50+16/50)=sqrt(.82)=.9055`; statistic `z≈3.313`. Since `|z|>1.96`, reject equality. A Welch t procedure is safer for smaller samples/unknown unequal variances.

### ISM 9 — Two proportions [MUST DO | Latest regular]

**Question.** Group 1 has 60 successes/100; group 2 has 45/100. Test equal proportions at 5%.

**Solution.** Pooled `p=(60+45)/200=.525`. `SE=sqrt(.525(.475)(.01+.01))=.07062`. `z=.15/.07062=2.124`, so reject two-sided at 5%. Pool under the null for the hypothesis test; unpooled SE is used for a confidence interval.

### ISM 10 — Chi-square independence [HIGH | Mar-2026 makeup]

**Question.** Observed table is `[[30,20],[20,30]]`. Test independence.

**Solution.** Every row and column total is 50; `N=100`, so all expected cells are 25. `chi²=4*(5²/25)=4`, df 1. Since 4>3.841, reject independence at 5%. Expected counts, not observed counts, go in the denominator.

### ISM 11 — Variance F test [HIGH | Latest regular]

**Question.** Test whether A is more variable than B: `sA²=16,nA=10`; `sB²=9,nB=12`.

**Solution.** `H1:sigmaA²>sigmaB²`; use `F=16/9=1.778`, df `(9,11)`, and compare with the **upper-tail** critical value from the permitted table. Do not automatically place the larger variance on top if the directional claim specifies the numerator; follow H1. Assume normal populations.

### ISM 12 — Pearson correlation [MUST DO | Every recent sitting]

**Question.** For `x=(1,2,3)`, `y=(2,4,5)`, find `r`.

**Solution.** Means are 2 and `11/3`. `Sxx=2`, `Syy=14/3`, `Sxy=3`. Thus `r=3/sqrt(2*14/3)=.982`. It indicates strong positive linear association, not causation.

### ISM 13 — Simple regression [MUST DO | Both 2026]

**Question.** Fit `y=b0+b1x` to the data in Q12 and predict at `x=4`.

**Solution.** `b1=Sxy/Sxx=1.5`; `b0=ybar-b1*xbar=11/3-3=2/3`. Prediction is `2/3+1.5(4)=6.667`. Do not use `r` itself as the slope unless standard deviations are equal.

### ISM 14 — One-way ANOVA [MUST DO | Mar-2026 makeup]

**Question.** Groups are A:`{1,2,3}`, B:`{4,5,6}`. Compute ANOVA F.

**Solution.** Group means 2 and 5; grand mean 3.5. Between SS `3(2-3.5)^2+3(5-3.5)^2=13.5`. Within SS is `(1+0+1)+(1+0+1)=4`. df `(1,4)`; `MSB=13.5`, `MSW=1`, so `F=13.5`. Compare with table and conclude group effect if significant.

### ISM 15 — Randomized-block ANOVA [MUST DO | Latest regular]

**Question.** Treatments A/B across three blocks are A:`8,9,7`, B:`5,6,4`. Explain the test calculation.

**Solution.** `N=6`, total `T=39`, correction `CF=T²/N=253.5`; total SS `sum x²-CF=271-253.5=17.5`. Treatment totals 24,15: `SS_tr=(24²+15²)/3-CF=13.5`. Block totals 13,15,11: `SS_bl=(13²+15²+11²)/2-CF=4`. Error SS `0`. Here treatment difference is perfectly constant across blocks, causing zero error and an effectively infinite treatment F; in real data nonzero error is expected. df treatment 1, blocks 2, error 2.

### ISM 16 — Moving average [MUST DO | Recurring forecasting]

**Question.** Values are `10,12,14,16,18`. Give the three-period forecast for period 6.

**Solution.** Average the latest three actuals: `(14+16+18)/3=16`. A moving average lags a trend; widening the window smooths more but reacts more slowly.

### ISM 17 — Simple exponential smoothing [MUST DO | Latest regular]

**Question.** Actuals are `10,14,13`; initial `F2=10`, `alpha=.5`. Find `F3,F4`.

**Solution.** `F3=.5Y2+.5F2=.5(14)+.5(10)=12`; `F4=.5Y3+.5F3=.5(13)+.5(12)=12.5`. Higher alpha reacts faster to recent observations. Maintain a period/actual/forecast/error table to prevent indexing mistakes.

### ISM 18 — Holt trend [HIGH | Forecasting family]

**Question.** State one Holt update and when to use it.

**Solution.** One convention: `L_t=alpha y_t+(1-alpha)(L_{t-1}+B_{t-1})`; `B_t=beta(L_t-L_{t-1})+(1-beta)B_{t-1}`; `h`-step forecast `L_t+hB_t`. Use for a trending, nonseasonal series. State initialization and convention because texts vary.

### ISM 19 — White-noise residual diagnosis and ARIMA [MUST/HIGH | 2026 + syllabus]

**Question.** Residual ACF has a large significant spike at lag 1. Is the model adequate? What does ARIMA(1,1,1) mean?

**Solution.** No: residual autocorrelation means predictable structure remains; residuals should resemble zero-mean, constant-variance, uncorrelated noise. ARIMA(1,1,1) uses one AR term, first differencing, and one MA error term. Do not confuse MA in ARIMA with a simple moving-average forecast.

### ISM 20 — GMM responsibility and MLE [HIGH | Latest regular + syllabus]

**Question.** Two Gaussian components at a point have densities `.2,.1` and weights `.6,.4`. Find posterior responsibility for component 1. Also state the Bernoulli MLE.

**Solution.** Weighted terms are `.12` and `.04`; responsibility `gamma1=.12/.16=.75`, `gamma2=.25`. EM uses these soft memberships in its M-step. For Bernoulli observations, log-likelihood differentiation gives `p_hat=(sum x_i)/n`, the sample proportion.

## DNN — 20 solved questions

### DNN 1 — Forward pass [MUST DO | Latest Q1/Q2]

**Question.** Inputs `(1,2)`, hidden neuron `z=2x1-x2+1`, ReLU, output sigmoid with weight 1 and bias 0. Find output.

**Solution.** Hidden preactivation `2(1)-2+1=1`; ReLU gives 1. Output `sigma(1)=1/(1+e^-1)=.7311`. Show preactivation and activation separately; this earns method marks and prevents applying activation twice.

### DNN 2 — Output/loss pairing [MUST DO | Recent stable]

**Question.** Choose outputs and losses for binary, mutually exclusive 5-class, and multilabel classification.

**Solution.** Binary: one sigmoid + BCE. Five mutually exclusive classes: five-way softmax + categorical cross-entropy. Multilabel: five independent sigmoids + summed/mean BCE. Softmax forces probabilities to compete and sum to one, so it is wrong for independent labels.

### DNN 3 — Backprop scalar [MUST DO | Latest papers]

**Question.** `yhat=sigmoid(wx)`, BCE loss, `x=2,y=1,w=0`. Find `dL/dw`.

**Solution.** For sigmoid+BCE, `dL/dz=yhat-y`. At `z=0`, `yhat=.5`, so `dL/dw=(.5-1)x=-1`. A GD step increases `w`, raising the positive-class probability. The simplified derivative avoids separately multiplying unstable BCE and sigmoid derivatives.

### DNN 4 — Vanishing/exploding gradients [MUST DO | Latest Q1]

**Question.** Explain causes and remedies.

**Solution.** Backprop multiplies many Jacobians; repeated singular values below 1 shrink gradients, above 1 enlarge them. Remedies: ReLU-family activations, Xavier/He initialization, batch/layer normalization, residual connections, gated LSTM/GRU states, gradient clipping for explosion, and appropriate learning rates. Sigmoid saturation particularly promotes vanishing gradients.

### DNN 5 — Dense parameter count [MUST DO]

**Question.** Count parameters in `20 -> 10 -> 3` dense network with biases.

**Solution.** First layer `20*10+10=210`; second `10*3+3=33`; total 243. Activations add no trainable parameters unless parameterized.

### DNN 6 — CNN shape and parameters [MUST DO | Latest Q3]

**Question.** Input `32x32x3`, conv `5x5`, 8 filters, stride 1, no padding. Find output and parameters.

**Solution.** Spatial output `floor((32-5)/1)+1=28`, so `28x28x8`. Parameters `(5*5*3)*8+8=608`. Parameter count does not multiply by spatial positions because weights are shared.

### DNN 7 — Pooling and receptive field [MUST DO | Latest]

**Question.** Two `3x3`, stride-1 convolutions with same padding are followed by `2x2`, stride-2 pooling. What is final receptive field?

**Solution.** Track receptive field `r` and jump `j`: initially `(1,1)`. Conv1: `r=1+2*1=3,j=1`; conv2: `r=3+2=5`; pool: `r=5+(2-1)*1=6,j=2`. A final unit sees `6x6` input area. Channels do not change receptive field.

### DNN 8 — GAP versus flatten [MUST DO | Latest Q3]

**Question.** Why can GAP reduce overfitting?

**Solution.** Flattening `H*W*C` into a dense layer can create millions of location-specific weights. Global average pooling converts each feature map to one scalar, yielding only `C` features and enforcing stronger spatial invariance. It reduces parameters and overfitting but may lose precise localization information.

### DNN 9 — Transfer learning [HIGH | Latest regular]

**Question.** How do you adapt an ImageNet CNN to 4-channel medical images and 3 output classes?

**Solution.** Replace/initialize the first convolution for 4 channels (e.g., copy RGB weights and initialize the extra channel), replace the classifier with 3 outputs, freeze backbone initially, train head, then fine-tune later blocks with small LR. Only the first layer is directly affected by input-channel count; output head follows class count.

### DNN 10 — Vanilla RNN step [MUST DO | Recent]

**Question.** Scalar RNN: `h_t=tanh(x_t+.5h_{t-1})`, `x_t=1,h_prev=0`. Find `h_t`.

**Solution.** Preactivation is 1; `h_t=tanh(1)=.7616`. For long sequences the recurrent derivative is repeatedly multiplied, causing vanishing/exploding gradients.

### DNN 11 — LSTM update [MUST DO | Makeup pattern]

**Question.** `c_prev=80,f=.85,i=.25,g=40,o=.5`. Find cell and hidden state.

**Solution.** `c=.85(80)+.25(40)=78`. Hidden `h=.5*tanh(78)≈.5`. The cell can preserve a large linear memory even though exposed hidden output is bounded by tanh and output gate.

### DNN 12 — GRU update [MUST DO | Latest Q4]

**Question.** Under `h=z h_prev+(1-z)h_tilde`, take `z=.7,h_prev=.4,h_tilde=.9`.

**Solution.** `h=.7(.4)+.3(.9)=.55`. Here larger update gate retains more old state under this convention. Some sources reverse the weighting; quote the equation used before substituting.

### DNN 13 — RNN/GRU/LSTM counts [MUST DO | Latest]

**Question.** With input size `d=5`, hidden size `h=4`, count one-bias parameters.

**Solution.** One recurrent affine block has `hd+h²+h=20+16+4=40`. Vanilla RNN: 40; GRU: `3*40=120`; LSTM: `4*40=160`. Output-layer parameters are additional. Frameworks may store two biases per gate; state convention.

### DNN 14 — Scaled dot-product attention [MUST DO | Latest Q5]

**Question.** `q=(1,0)`, keys `k1=(1,0),k2=(0,1)`, values `v1=(2,0),v2=(0,4)`. Compute attention.

**Solution.** Scaled scores are `(1/sqrt2,0)=(.7071,0)`. Softmax weights are approximately `(.6698,.3302)`. Context `=.6698(2,0)+.3302(0,4)=(1.3396,1.3208)`. Scaling prevents dot products from pushing softmax into saturation as dimension grows.

### DNN 15 — Masking [MUST DO]

**Question.** How is causal masking applied?

**Solution.** Before softmax, replace forbidden future-position scores with `-infinity`; their softmax weights become zero. Applying a mask after softmax breaks normalization. Padding masks hide padded tokens; causal masks prevent future leakage.

### DNN 16 — Multi-head attention [MUST DO | Transformer signal]

**Question.** Why multiple heads, and does head count multiply projection parameters?

**Solution.** Heads learn different relationships/subspaces. With fixed `d_model`, Q/K/V projections still total approximately `3d²` and output projection `d²`; splitting into heads does not multiply these totals. It changes reshape/computation organization. Extra parameters occur only if total projected width increases.

### DNN 17 — Transformer block count [MUST DO | Latest Q6]

**Question.** Ignoring biases, count encoder-block weights for `d=512,dff=2048`.

**Solution.** Attention projections: Q,K,V,O = `4d²=1,048,576`. FFN: `d*dff+dff*d=2,097,152`. Total `3,145,728`, plus small LayerNorm parameters and biases if requested. Complexity of full self-attention is `O(L²d)` time and `O(L²)` attention storage.

### DNN 18 — Positional encoding and architecture choice [MUST DO]

**Question.** Why positional information? Match BERT, GPT, encoder–decoder.

**Solution.** Self-attention alone is permutation-equivariant and has no inherent word order; positional vectors encode location. Encoder-only/BERT suits representations and classification; decoder-only/GPT suits autoregressive generation; encoder–decoder suits conditional transformations such as translation and summarization.

### DNN 19 — Optimizer comparison [MUST DO | Latest Q7]

**Question.** Contrast SGD, momentum, RMSProp and Adam.

**Solution.** SGD uses current gradient; momentum smooths directions with velocity; RMSProp scales each coordinate by a moving average of squared gradients; Adam combines momentum and RMS scaling with bias correction. Adam often learns quickly, while tuned SGD may generalize well. Know formulas from the authorized slides; in prose tie optimizer choice to noisy gradients, curvature and memory cost.

### DNN 20 — Diagnose training curves [MUST DO | Latest Q7]

**Question.** Training loss falls, validation loss falls then rises. Diagnose and prescribe.

**Solution.** This is overfitting after the validation minimum. Use early stopping at that epoch, data augmentation, L2/weight decay, dropout, smaller model, or more data. If both losses remain high, diagnose underfitting instead. Batch normalization primarily stabilizes optimization and is not identical to dropout.

## ML — 20 solved questions

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

### ML 5 — Entropy and information gain [HIGH | Tree syllabus/PYQs]

**Question.** A node has 4 positive, 4 negative cases. A split produces two pure children of size 4. Find information gain.

**Solution.** Parent entropy is 1 bit. Each pure child entropy is 0, so weighted child entropy is 0 and gain is 1. Real tree algorithms choose the split with largest gain (or related criterion); deep trees can overfit, controlled by depth/min-leaf/pruning.

### ML 6 — Distance-weighted KNN [MUST DO | Latest regular]

**Question.** Neighbors: class A at distances 1 and 2; class B at distance 1.5. Use `1/d²`.

**Solution.** A score `1+1/4=1.25`; B score `1/2.25=.444`; predict A. If distance is zero, return the exact neighbor label or use an explicit safeguard. Scale features and use type-aware distances for mixed data.

### ML 7 — KNN regression and LWR [MUST DO | Latest makeup]

**Question.** Neighbor targets 2,4,8 at distances 1,1,2; compute inverse-distance KNN regression. Why might LWR differ?

**Solution.** Weights `1,1,.5`; prediction `(2+4+4)/2.5=4`. LWR fits a local line/plane using distance weights, so it captures a local trend rather than merely averaging targets; it costs optimization per query.

### ML 8 — Gaussian Naive Bayes [MUST DO | Latest makeup]

**Question.** Equal priors; at observed x, class likelihoods are `.20` and `.05`. Predict and find posterior.

**Solution.** Unnormalized scores `.1` and `.025`; predict class 1. Normalized posterior for class 1 is `.1/.125=.8`. For many features use log probabilities to prevent underflow. NB’s conditional-independence assumption is about features given class.

### ML 9 — Multinomial NB with Laplace [MUST DO | Latest regular]

**Question.** In class C, word count is 2, total tokens 10, vocabulary size 5, alpha 1. Find probability.

**Solution.** `(2+1)/(10+1*5)=3/15=.2`. Smoothing prevents a single unseen word from making the entire document likelihood zero. Denominator uses total class-token count plus `alpha*V`.

### ML 10 — MLE versus MAP [SHOULD DO | Official]

**Question.** Distinguish them.

**Solution.** MLE maximizes `p(D|theta)`; MAP maximizes `p(D|theta)p(theta)` and incorporates a prior. In log form, a Gaussian prior on weights corresponds to an L2-like penalty; a Laplace prior corresponds to L1-like regularization. With abundant data the likelihood often dominates.

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

### ML 15 — K-means iteration [MUST DO | Both recent]

**Question.** Points `{1,2,8,9}`, initial centroids 1 and 8. Perform one iteration.

**Solution.** Assign `{1,2}` to cluster 1 and `{8,9}` to cluster 2; updated centroids are 1.5 and 8.5. Assign all points using old centroids before updating. K-means minimizes within-cluster squared Euclidean distance and is sensitive to scale/outliers/initialization.

### ML 16 — GMM EM M-step [MUST DO | Latest makeup]

**Question.** Points 0 and 2 have component-1 responsibilities `.8,.2`. Update its mixing weight and mean.

**Solution.** `N1=.8+.2=1`; with `N=2`, `pi1=.5`. `mu1=(.8*0+.2*2)/1=.4`. Variance is the responsibility-weighted squared deviation divided by `N1`. GMM membership is soft; K-means uses hard 0/1 assignments.

### ML 17 — Hard-margin SVM geometry [MUST DO | All extractable cycles]

**Question.** For `w=(3,4),b=-5`, classify `x=(1,1)` and find distance to boundary.

**Solution.** Score `3+4-5=2`, so positive. Distance `|2|/||w||=2/5=.4`. Decision uses score sign; geometric distance divides by norm. Canonical margin width is `2/||w||` only when support constraints equal ±1.

### ML 18 — Soft margin, C and support vectors [MUST DO | Latest]

**Question.** Explain effects of very large and small C.

**Solution.** Large C heavily penalizes violations, tends toward narrower margin/lower training error and greater variance. Small C tolerates violations for a wider, more regularized margin. In the dual, `alpha=0` points do not determine boundary; `0<alpha<C` typically lie on margin; `alpha=C` may lie within margin or be misclassified.

### ML 19 — Kernel reasoning [MUST DO | Latest]

**Question.** Give a feature map for `k(x,z)=(1+xz)^2` in one dimension and explain cost.

**Solution.** Expand `1+2xz+x²z²`; choose `phi(x)=(1,sqrt2x,x²)`, whose dot product equals the kernel. Kernel methods avoid explicit high-dimensional features, but storing an `N x N` Gram matrix costs `O(N²)` memory and training can be expensive for large N.

### ML 20 — Model selection, fairness and interpretability [HIGH | Latest scenario style]

**Question.** A slightly more accurate ensemble fails an auditability requirement; a sparse logistic model is close in performance. Choose and justify.

**Solution.** Select the sparse logistic model if auditability is a binding constraint, after validating calibration and subgroup metrics. Report the accuracy tradeoff explicitly. Interpretability does not guarantee fairness: compare error rates, recall/precision or other policy-appropriate metrics across relevant groups, inspect data/proxy leakage, and document threshold/cost choices.

## Mastery protocol

1. **Pass 1:** solve all MUST DO questions untimed; annotate the authorized watermarked page containing each method.
2. **Pass 2:** redo every incorrect numerical without viewing the solution.
3. **Pass 3:** create four 40-mark mixed mocks by sampling recent proportions of topics; solve each under the actual time limit.
4. A question is mastered only when you can identify the method in 20 seconds, write the formula from memory, solve cleanly, state assumptions, and give a contextual conclusion.
5. Keep an error log with four columns: question, error type, corrected rule, next retest time.

## Accuracy note

The bank covers every official major topic family at least once, but recent-paper weighting is deliberately unequal. It improves readiness; it cannot guarantee a particular score because the future paper and grading are not known. Verify table-dependent critical values and course-specific formula conventions against the authorized watermarked slides during practice.

After completing this bank, use [07_LATEST_PAPER_GAP_CLOSURE.md](07_LATEST_PAPER_GAP_CLOSURE.md) for the exact method gaps revealed by comparison with the latest regular papers.

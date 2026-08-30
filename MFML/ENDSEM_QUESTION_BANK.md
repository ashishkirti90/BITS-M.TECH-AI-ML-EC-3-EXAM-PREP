# MFML End-Sem Question Bank

**Course:** Mathematical Foundations for Machine Learning  
**Scope:** Comprehensive/end-semester examination  
**Format:** 20 core solved questions + 5 latest-paper gap-closing questions  
**Evidence:** Official course handout, audited repository material, and verified recent-paper structures

---

## How to use this bank

- Attempt every question before reading its solution.
- Prioritize items labelled MUST DO and latest-paper pattern.
- The numerical values in original drills are practice values; a PYQ-pattern label refers to verified structure, not a claim of verbatim reproduction.
- After each error, bookmark the matching worked example in the authorized watermarked slides.

---

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

---

# Latest-paper gap closure

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

---

## Mastery test

A pattern is mastered only when you can identify the method within 20 seconds, write the governing formula without searching, complete the calculation accurately, state assumptions, interpret the result, and locate a backup example in the watermarked slides within 30 seconds.
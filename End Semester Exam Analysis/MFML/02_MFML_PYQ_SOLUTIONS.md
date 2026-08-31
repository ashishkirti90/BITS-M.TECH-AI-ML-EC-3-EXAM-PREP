# MFML High-Value PYQ Solution Bank

All questions below are repository-evidenced. No invented question is labelled as a PYQ. Marks and question numbers appear only when visible in the paper/key. `Inferred depth` means the solution presentation is scaled from the verified marks because a matching marking scheme was unavailable.

## 1. [ACTUAL PYQ] Eigenstructure, diagonalization and singular values

**Subject:** MFML | **Paper:** EC-3 Regular, First Semester 2025-26, 01-03-2026 | **Question:** Q1 | **Marks:** 8  
**Priority/pattern:** MUST DO - eigenstructure to diagonalization; singular-value bridge.

**Question.** For `A=[[3,1,0],[1,3,0],[0,0,4]]`, find eigenvalues/eigenvectors, construct `AP=PD`, and obtain singular values of the supplied `B` for which `B^TB=A`.

**Solution.**

**Given/required.** Solve `det(A-lambda I)=0`, then each eigenspace.

`det(A-lambda I)=(4-lambda)[(3-lambda)^2-1]=(4-lambda)(lambda-2)(lambda-4)`.

Thus eigenvalues are `2,4,4`.

- `lambda=2`: `(A-2I)v=0` gives `x+y=0,z=0`; choose `v1=(1,-1,0)^T`.
- `lambda=4`: `-x+y=0`, with `z` free; choose `v2=(1,1,0)^T`, `v3=(0,0,1)^T`.

Therefore

`P=[[1,1,0],[-1,1,0],[0,0,1]]`, `D=diag(2,4,4)`, and direct column comparison gives `AP=PD`.

Since `B^TB=A`, its singular values are the square roots of the eigenvalues of `A`: `sqrt(2),2,2` (normally list descending: `2,2,sqrt(2)`).

**Exam writing:** show the repeated eigenvalue has a two-dimensional eigenspace; this is why diagonalization works.  
**Common mistake:** listing eigenvalue 4 once and producing only two eigenvectors.  
**Watermark:** viewer pp. 34-49; compact recap p. 129.

## 2. [ACTUAL PYQ] Independence, span, basis and rank

**Subject:** MFML | **Paper:** EC-3 Regular, First Semester 2025-26, 01-03-2026 | **Question:** Q2 | **Marks:** 8  
**Priority/pattern:** MUST DO - column reduction plus justification.

**Question.** For the four supplied vectors in `R^4`, decide independence; prove their span is a subspace and give basis/dimension; find rank and determinant of the column matrix.

**Solution.** Stack the vectors as columns:

`B=[[-3,0,0,-6],[1,2,1,3],[0,3,0,-3],[-1,4,0,-3]]`.

One valid echelon reduction is

`B ~ [[1,2,1,3],[0,6,3,3],[0,0,-3/2,-9/2],[0,0,0,3]]`.

There are four pivots, so the columns are linearly independent. Hence the four original vectors form a basis of their span `U`, and `dim(U)=4`.

To prove subspace: for `u=sum a_i v_i` and `w=sum b_i v_i`, `u+w=sum(a_i+b_i)v_i in U`; for scalar `c`, `cu=sum(ca_i)v_i in U`; zero is obtained by all coefficients zero. Thus `U` is a subspace.

`rank(B)=4`. Tracking the initial row swap in the displayed reduction gives `det(B)=27` (also verify directly). Because it is `4x4`, the determinant is defined.

**Exam writing:** explicitly use original vectors in the basis, not echelon columns.  
**Common mistake:** saying every span is a subspace without the requested closure justification.  
**Watermark:** viewer pp. 17-26 and 121-125.

## 3. [ACTUAL PYQ] Inner product, primal/dual and KKT

**Subject:** MFML | **Paper:** EC-3 Regular, First Semester 2025-26, 01-03-2026 | **Question:** Q3 | **Marks:** 8  
**Priority/pattern:** MUST DO - SPD plus complete constrained-optimization workflow.

**Question.** With `A=[[3,1],[1,3]]`, cost `C(x,y)=2||(x,y)||_A^2`, and `1<=x+y<=3`, establish the inner product, formulate primal and dual, and verify KKT at the optimum.

**Solution.** `A=A^T`. Its leading principal minors are `3>0` and `det(A)=8>0`; by Sylvester, `A` is positive definite. Hence `u^TAv` is an inner product.

`||(x,y)||_A^2=3x^2+2xy+3y^2`, so

`min f=6x^2+4xy+6y^2`, subject to `g1=1-x-y<=0`, `g2=x+y-3<=0`.

`L=f+lambda1(1-x-y)+lambda2(x+y-3)`, `lambda1,lambda2>=0`.

The dual is `max q(lambda1,lambda2)`, where

`q=lambda1-3lambda2-(lambda1-lambda2)^2/16`, `lambda1,lambda2>=0`.

Maximization gives `lambda1=8,lambda2=0`; stationarity gives `x=y=(lambda1-lambda2)/16=1/2`.

KKT at `(1/2,1/2,8,0)`:

- primal: `g1=0`, `g2=-2<=0`;
- dual: `8>=0`, `0>=0`;
- complementarity: `8(0)=0`, `0(-2)=0`;
- stationarity: `grad f=(8,8)^T`, `grad g1=(-1,-1)^T`, `grad g2=(1,1)^T`; therefore `(8,8)+8(-1,-1)+0(1,1)=0`.

The convex quadratic and affine constraints make KKT sufficient; the point is globally optimal.

**Exam writing:** display primal feasibility, dual feasibility, complementary slackness and stationarity as four separately labelled checks, then state why KKT proves global optimality here.  
**Common mistake:** writing `x+y-1>=0` while still attaching a nonnegative multiplier under the `g<=0` convention.  
**Watermark:** viewer pp. 27-33, 84-87 and 134-135.

## 4. [ACTUAL PYQ] Regression Hessian and inverse-decay GD

**Subject:** MFML | **Paper:** EC-3 Regular, First Semester 2025-26, 01-03-2026 | **Question:** Q4 | **Marks:** 8  
**Priority/pattern:** MUST DO - convexity proof plus two iteration numerical.

**Question.** For data `(5,3),(6,5)`, model `yhat=w0+w1x`, and half-squared error, formulate `J`, prove convexity and perform two inverse-decay GD iterations from zero with `eta0=.1,k=.4`.

**Solution.**

`J=1/2[(w0+5w1-3)^2+(w0+6w1-5)^2]`.

`grad J=(2w0+11w1-8, 11w0+61w1-45)^T` and `H=[[2,11],[11,61]]`.

Leading minors: `2>0`, `det(H)=122-121=1>0`; hence `H` is positive definite and `J` strictly convex.

`eta_t=.1/(1+.4t)`.

At `t=1`, `eta1=1/14`; `g(0,0)=(-8,-45)`. Thus

`w^(1)=(4/7,45/14)=(0.571429,3.214286)`.

At this point, `g=(399/14,2203/14)=(28.5,157.357143)`. With `eta2=1/18`,

`w^(2)=(-85/84,-1393/252)=(-1.011905,-5.527778)`.

The large oscillation is not an arithmetic contradiction: this chosen learning schedule is too aggressive for the high-curvature direction.

**Exam writing:** compute each `eta_t` first and retain fractions/four decimals.  
**Common mistake:** evaluating the second gradient at `(0,0)` again.  
**Watermark:** viewer pp. 65-73 and recap pp. 131-132.

## 5. [ACTUAL PYQ] Optimal hard-margin SVM

**Subject:** MFML | **Paper:** EC-3 Regular, First Semester 2025-26, 01-03-2026 | **Question:** Q5 | **Marks:** 8  
**Priority/pattern:** MUST DO - canonical margin and support vectors. **Inferred depth:** the bundled key answers different Q5 wording; this solution is independently recalculated from the official paper.

**Question.** Positive points are `(2,2),(4,4)` and negative points `(2,0),(4,0)`. Formulate hard-margin SVM and determine optimal boundary, `w,b`, and support vectors.

**Solution.**

Primal: `min_(w,b) 1/2(w1^2+w2^2)` subject to the four canonical inequalities:

`2w1+2w2+b>=1`, `4w1+4w2+b>=1`, `-(2w1+b)>=1`, `-(4w1+b)>=1`.

The classes are separated vertically. The nearest parallel class levels are `x2=0` and `x2=2`, so the maximum-margin decision boundary is their midpoint:

`x2=1`, equivalently `w=(0,1)^T`, `b=-1`.

Check functional margins:

- `(2,2),+1`: `1`;
- `(4,4),+1`: `3`;
- `(2,0),-1`: `1`;
- `(4,0),-1`: `1`.

All constraints hold. Support vectors are the equality points `(2,2)`, `(2,0)`, `(4,0)`. Half-margin is `1/||w||=1`; full margin width is `2`.

**Exam writing:** boundary, margin planes (`x2=0,2`), canonical parameters and equality checks are all distinct scoring steps.  
**Common mistake:** calling `(4,4)` a support vector simply because it is correctly classified.  
**Watermark:** viewer pp. 106-112 and 135-136.

## 6. [ACTUAL PYQ] Triangular eigenproblem and column independence

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q1 | **Marks:** 7  
**Priority/pattern:** MUST DO - exploit triangular structure, then solve eigenspace.

**Question.** For the supplied lower-triangular `4x4` matrix with diagonal `(-2,3,-1,5)`, find the largest-eigenvalue eigenspace and decide whether columns are independent.

**Solution.** A triangular matrix has eigenvalues equal to its diagonal: `-2,3,-1,5`. For `lambda=5`, row reduction of `A-5I` forces `x1=x2=x3=0`, with `x4` free. Thus `E_5=span{(0,0,0,1)^T}`, basis `{e4}`, dimension 1. The determinant is the diagonal product `(-2)(3)(-1)(5)=30!=0`; therefore all four columns are linearly independent.

**Exam writing:** use the triangular-matrix shortcut first, show the equations from `(A-5I)x=0`, and finish with the nonzero-determinant independence test.  
**Common mistake:** reporting the zero vector as the eigenvector rather than the one-dimensional eigenspace.  
**Watermark:** pp. 34-41.

## 7. [ACTUAL PYQ] SPD inner product and Gram-Schmidt

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q2 | **Marks:** 8  
**Priority/pattern:** HIGH - custom inner-product orthonormalization.

**Question.** With `A=[[3,1,0],[1,1,0],[0,0,2]]`, prove SPD, define the inner product, show `v1=(1,2,-1)`, `v2=(2,-1,0)` are not orthogonal, and orthonormalize them.

**Solution.** `A` is symmetric. Leading principal minors are `3,2,4`, all positive, so it is PD.

`<x,y>_A=x^TAy`. `Av2=(5,1,0)^T`, so `<v1,v2>_A=7!=0`.

`<v1,v1>_A=13`, hence `e1=v1/sqrt(13)`.

`u2=v2-(<v2,v1>_A/<v1,v1>_A)v1=v2-(7/13)v1=(1/13)(19,-27,7)^T`.

`<u2,u2>_A=884/169`, so `e2=(19,-27,7)^T/sqrt(884)`.

The final set `{e1,e2}` is `A`-orthonormal.

**Exam writing:** show `Av_i`, each `A`-inner product, the projection coefficient and the final normalization; end by stating both unit norm and mutual orthogonality.  
**Common mistake:** using Euclidean `v1^Tv2` in the projection coefficient.  
**Watermark:** pp. 27-33 and 126-127.

## 8. [ACTUAL PYQ] Binary line search

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q3 | **Marks:** 7  
**Priority/pattern:** MUST DO - reduce to one-dimensional search.

**Question.** For `L(w1,w2)=w1^4+w2^4-(w1+w2)`, start `(0,0)`, direction `d=-grad L(0,0)`, reduce `[0,2]` after two binary-search iterations, and find the exact minimizing step.

**Solution.** `grad L=(4w1^3-1,4w2^3-1)`, so `d=(1,1)`. Therefore `phi(alpha)=L(alpha,alpha)=2alpha^4-2alpha`, `phi'=8alpha^3-2`.

- midpoint 1: `phi'(1)=6>0`, so retain `[0,1]`;
- midpoint `.5`: `phi'(.5)=-1<0`, so retain `[.5,1]`.

Set `phi'=0`: `alpha^3=1/4`, so `alpha*=4^(-1/3)=0.629961`. Since `phi''=24alpha^2>0`, this is the minimum and lies in the retained interval.

**Exam writing:** write `d`, `phi(alpha)` and `phi'(alpha)` before the interval table; for each iteration record midpoint, derivative sign and retained interval.  
**Common mistake:** deciding the interval from the value of `phi(mid)` alone without a comparison or derivative.  
**Watermark:** pp. 69-72 and 132.

## 9. [ACTUAL PYQ] Two momentum iterations

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q4 | **Marks:** 4  
**Priority/pattern:** MUST DO - state convention and update every vector.

**Question.** Minimize `J=(w0-3)^2+(w1-3)^2` from `(2,2)` with `eta=.05`, `beta=.5`, `v0=0`; give two momentum iterates.

**Solution.** Use `v_t=beta v_(t-1)-eta grad J(w_(t-1))`, `w_t=w_(t-1)+v_t`.

`g0=(-2,-2)`, so `v1=(.1,.1)` and `w1=(2.1,2.1)`.

`g1=(-1.8,-1.8)`, so `v2=.5(.1,.1)-.05(-1.8,-1.8)=(.14,.14)` and `w2=(2.24,2.24)`.

**Exam writing:** state the momentum convention once, then show `gradient -> velocity -> parameter` for each numbered iteration.  
**Common mistake:** subtracting the velocity again after its sign already includes `-eta g`.  
**Watermark:** viewer p. 81 and recap p. 132.

## 10. [ACTUAL PYQ] Complete PCA calculation

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q5 | **Marks:** 7  
**Priority/pattern:** MUST DO - covariance to one-dimensional subspace.

**Question.** For observations `(0,3),(1,5),(2,7)`, compute covariance using the paper's `1/N` convention, eigenpairs and the one-dimensional principal subspace.

**Solution.** Mean is `(1,5)` and

`X_c=[[-1,-2],[0,0],[1,2]]`.

`S=(1/3)X_c^TX_c=[[2/3,4/3],[4/3,8/3]]`.

Characteristic polynomial is `lambda(lambda-10/3)`, so eigenvalues are `10/3` and `0`. For `10/3`, `y=2x`, giving unit direction `(1,2)^T/sqrt(5)`. For `0`, a unit orthogonal direction is `(-2,1)^T/sqrt(5)`.

The one-dimensional principal subspace is `span{(1,2)^T}`. Coordinates are `(-sqrt(5),0,sqrt(5))` up to the permitted sign reversal of the eigenvector.

**Exam writing:** present mean, centered matrix, covariance with its divisor, ordered eigenpairs, unit principal direction and projected coordinates in that order.  
**Common mistake:** reporting the eigenvector but not the subspace/normalization or forgetting centering.  
**Watermark:** pp. 88-100 and 133-134.

## 11. [ACTUAL PYQ] Soft-margin SVM and hinge objective

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** EC-3 Makeup, First Semester 2025-26, 08-03-2026 | **Question:** Q6 | **Marks:** 7  
**Priority/pattern:** MUST DO - primal to hinge form and pointwise arithmetic.

**Question.** For positive `(3,3),(5,5)` and negative `(3,0),(5,0)`, formulate soft-margin primal, derive hinge form, and evaluate `w=(1,-1),b=0,C=1`.

**Solution.**

`min 1/2||w||^2+C sum xi_i`, subject to `y_i(w^Tx_i+b)>=1-xi_i`, `xi_i>=0`.

At optimum for fixed `w,b`, `xi_i=max(0,1-y_i f_i)`, giving the unconstrained hinge objective.

For the proposed model, functional margins are `0,0,-3,-5`; hinge losses are `1,1,4,6`. The regularizer is `1/2(1^2+(-1)^2)=1`; total objective is `1+12=13`.

The two positive points lie on the decision boundary, while both negative points are misclassified. All four have positive hinge loss.

**Exam writing:** use a four-row table for score, functional margin and hinge loss, then add the regularizer separately and state the classification interpretation.  
**Common mistake:** computing `f_i` but forgetting multiplication by `y_i`.  
**Watermark:** pp. 106-112 and 135-136.

## 12. [ACTUAL PYQ] Rank, basis and nested subspace

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q1 | **Marks:** 7  
**Answer depth:** inferred from the verified 7 marks; no matching official key was verified.  
**Question.** For `A=[[1,0,0,1],[2,-1,0,1],[0,-2,-2,-4],[0,1,1,2]]`, find rank and a column-space basis; show `U=span{(1,1,-2,1)^T}` is a subspace of the column space.

**Solution.** Let columns be `c1,...,c4`. Directly `c4=c1+c2+c3`; `c1,c2,c3` are independent (their first three rows already give pivots). Thus `rank(A)=3`, a basis is `{c1,c2,c3}`, and `dim W=3`. The generator of `U` equals `c1+c2`, hence lies in `W`. Since the span of one vector in `W` is closed under addition/scaling and contains zero, `U` is a subspace of `W`.

**Exam writing:** state the column relation, identify the three original basis columns, and explicitly show the generator of `U` as their linear combination before invoking span closure.  
**Common mistake:** choosing all four columns as a basis despite the visible relation.  
**Watermark:** pp. 17-26.

## 13. [ACTUAL PYQ] SVD and PCA link

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q2 | **Marks:** 7  
**Answer depth:** inferred from the verified 7 marks; no matching official key was verified.  
**Question.** Find the SVD of `A=[[-2,0],[1,1],[1,-1]]`; treating rows as centered observations, find covariance eigenvalues and maximum-variance direction.

**Solution.** The columns are orthogonal with squared norms `6` and `2`, so `A^TA=diag(6,2)`. Take `V=I`, `sigma1=sqrt(6)`, `sigma2=sqrt(2)`,

`u1=(-2,1,1)^T/sqrt(6)`, `u2=(0,1,-1)^T/sqrt(2)`.

A completing unit vector is `u3=(-1,-1,-1)^T/sqrt(3)`. Therefore `A=U Sigma V^T`, with `Sigma=[[sqrt6,0],[0,sqrt2],[0,0]]`.

Both feature means are zero. With the paper/course `1/N` convention, `S=(1/3)A^TA=diag(2,2/3)`. The maximum-variance direction is `(1,0)^T`, eigenvalue `2`.

**Exam writing:** state row-observation orientation and zero centering, show `A^TA`, align `U,Sigma,V`, then scale by `1/N` for the PCA conclusion.  
**Common mistake:** computing covariance without checking data orientation/centering.  
**Watermark:** pp. 42-49 and 88-100.

## 14. [ACTUAL PYQ] Multivariate chain rule and dual formulation

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q3 | **Marks:** 6  
**Answer depth:** inferred from the verified 6 marks; no matching official key was verified.  
**Question.** For `w=xy+yz+xz`, `x=u+v`, `y=u^2-v`, `z=u-v^2`, find `dw/du,dw/dv`; formulate primal and Lagrangian dual for minimizing `3(x^2+y^2)` over `1<=x+y<=3`.

**Solution.** `w_x=y+z`, `w_y=x+z`, `w_z=x+y`. Hence

`w_u=(y+z)+2u(x+z)+(x+y)`,

`w_v=(y+z)-(x+z)-2v(x+y)`,

with `x,y,z` replaced by the stated functions if expansion is required.

For optimization, use `g1=1-x-y<=0`, `g2=x+y-3<=0`:

`L=3(x^2+y^2)+lambda1(1-x-y)+lambda2(x+y-3)`.

Stationarity gives `x=y=(lambda1-lambda2)/6`. Therefore

`q(lambda)=lambda1-3lambda2-(lambda1-lambda2)^2/6`, and the dual is `max q` subject to `lambda1,lambda2>=0`.

**Exam writing:** list local partial derivatives before applying the total chain rule; for the dual, standardize constraints, write `L`, eliminate primal variables and only then state `max q`.  
**Common mistake:** omitting indirect paths in the chain rule.  
**Watermark:** pp. 50-61 and 84-87.

## 15. [ACTUAL PYQ] Momentum versus plain GD

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q4 | **Marks:** 7  
**Answer depth:** inferred from the verified 7 marks; no matching official key was verified.  
**Question.** For `f=(x-1)^2+(y-1)^2`, start `(1.5,1.5)`, `alpha=.05`, `beta=.8`; compute two momentum and two plain-GD iterations and compare.

**Solution.** Use `v_t=beta v_(t-1)-alpha grad f(theta_(t-1))`, `theta_t=theta_(t-1)+v_t`, `v0=0`.

`g0=(1,1)`, so `v1=(-.05,-.05)`, momentum point `theta1=(1.45,1.45)`. Then `g1=(.9,.9)`, `v2=.8(-.05,-.05)-.05(.9,.9)=(-.085,-.085)`, so `theta2=(1.365,1.365)`.

Plain GD gives `a1=(1.45,1.45)` and `a2=(1.405,1.405)`.

After two steps momentum is closer to `(1,1)` (`.365` coordinate error versus `.405`). It can accelerate a consistent descent direction, though excessive momentum can overshoot.

**Exam writing:** tabulate iteration, gradient, velocity and new point for momentum, then the plain-GD points; base the comparison on the computed distance or objective.  
**Common mistake:** claiming universal superiority from only two steps; conclude only for this computation.  
**Watermark:** pp. 68-83 and 132-133.

## 16. [ACTUAL PYQ] Compare two soft-margin classifiers

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q5 | **Marks:** 7  
**Answer depth:** inferred from the verified 7 marks; no matching official key was verified.  
**Question.** For labelled points `(0,0)-,(2,2)+,(2,0)-,(0,2)+`, `C=1`, compare Model A `w=(1,1),b=-1.5` and Model B `w=(1,-1),b=0`.

**Solution.** Both regularizers are `1/2||w||^2=1`.

Model A functional margins are `1.5,2.5,-.5,.5`; hinges are `0,0,1.5,.5`, sum `2`, objective `3`.

Model B functional margins are `0,0,-2,-2`; hinges are `1,1,3,3`, sum `8`, objective `9`.

Model A is better. Under A, margin-error points are `(2,0)` and `(0,2)`; `(2,0)` is misclassified, while `(0,2)` is correctly classified but inside the margin. `(0,0)` and `(2,2)` are correctly classified with zero hinge loss.

**Exam writing:** give a model-wise table of regularizer, four functional margins, four hinge losses, loss sum and total objective, then interpret the better model's points.  
**Common mistake:** treating every positive hinge as misclassification.  
**Watermark:** pp. 135-136.

## 17. [ACTUAL PYQ] Feature map and `4x4` kernel matrix

**Subject:** MFML | **Paper:** EC-3 Regular, Second Semester 2024-25, 06-09-2025 | **Question:** Q6 | **Marks:** 6  
**Answer depth:** inferred from the verified 6 marks; no matching official key was verified.  
**Question.** For `phi(x)=[1,sqrt(2)x,x^2]` and inputs `[-1.5,-.5,.5,1.5]`, prove the kernel and compute the Gram matrix.

**Solution.**

`phi(x)^Tphi(z)=1+2xz+x^2z^2=(1+xz)^2`.

Using input order as given,

`K=(1/16)[[169,49,1,25],[49,25,9,1],[1,9,25,49],[25,1,49,169]]`.

It is symmetric as required; its construction as `Phi Phi^T` guarantees positive semidefiniteness.

**Exam writing:** expand the feature-space dot product first, state the input order, fill one triangle of `K`, mirror it, and add a symmetry/PSD check.  
**Common mistake:** omitting the `sqrt(2)` cross coefficient and obtaining `1+xz+x^2z^2`.  
**Watermark:** pp. 112 and 136.

## 18. [ACTUAL PYQ] Crout-style LU decomposition

**Subject:** MFML | **Source:** Comprehensive March 2025 solution key | **Question:** Q1 | **Marks:** 6  
**Priority/pattern:** SHOULD DO - older decomposition backup. Session/date beyond the filename is not verified.

**Question.** Factor `A=[[3,6,-9],[2,5,-3],[-4,1,10]]` as `LU` with `U` having unit diagonal.

**Solution.** Put

`L=[[l11,0,0],[l21,l22,0],[l31,l32,l33]]`, `U=[[1,u12,u13],[0,1,u23],[0,0,1]]`.

Equating `LU=A` gives successively:

`l11=3,u12=2,u13=-3,l21=2,l22=1,u23=3,l31=-4,l32=9,l33=-29`.

Thus

`L=[[3,0,0],[2,1,0],[-4,9,-29]]`, `U=[[1,2,-3],[0,1,3],[0,0,1]]`.

Multiplication reconstructs `A`; in particular the bottom-right entry is `(-4)(-3)+9(3)-29=10`.

**Exam writing:** state the Crout convention `diag(U)=1`, equate entries in top-left order, display both factors and verify at least one nontrivial product entry.  
**Common mistake:** switching to Doolittle halfway and setting the wrong diagonal to one.  
**Watermark:** p. 129 recap; detailed LU lookup in systems/decomposition material.

## 19. [ACTUAL PYQ] PCA variance retention and invertibility

**Subject:** MFML | **Source:** Comprehensive March 2025 solution key | **Question:** Q2 | **Marks:** 6  
**Priority/pattern:** HIGH - explained variance and rank logic. Session/date beyond the filename is not verified.

**Question.** If covariance eigenvectors are coordinate vectors and feature variances decrease, identify covariance; for `d=4`, `sigma_i^2=5-i`, retain 90% by eliminating one feature; decide invertibility if the first `d-1` PCs retain 100%.

**Solution.** With eigenvector matrix `P=I`, covariance is `S=P diag(sigma_1^2,...,sigma_d^2)P^-1=diag(sigma_1^2,...,sigma_d^2)`.

For `d=4`, eigenvalues are `4,3,2,1`, total `10`. Retaining first three keeps `9/10=90%`, so eliminate the fourth feature.

If the first `d-1` PCs retain 100%, then `lambda_d=0`. Hence `det(S)=product lambda_i=0`, so `S` is singular and has no inverse.

**Exam writing:** write the ordered eigenvalues and total variance, show the retained-variance fraction, identify the discarded feature, then connect zero residual variance to zero determinant.  
**Common mistake:** saying PCA always yields an invertible covariance; a zero-variance direction makes it singular.  
**Watermark:** pp. 88-100 and 133-134.

## 20. [ACTUAL PYQ] Explained-variance thresholds and projection

**Subject:** MFML/MFDS shared ZC416 family | **Paper:** I Semester 2023-24 regular, internally dated 07-04-2024 | **Question:** Q4(B) | **Marks:** 6  
**Priority/pattern:** HIGH - choose `k`, then compute coordinates.

**Question.** Covariance eigenvalues are `.014,.016,1,3.5,6.8,12`. Infer sample dimension; find minimum PCs for 95% and 99%; project the supplied six-vector onto two supplied components.

**Solution.** Six covariance eigenvalues imply six features.

Total variance is `23.33`. Sorted cumulative totals are `12`, `18.8`, `22.3`, `23.3`, ...

- 95% target is `22.1635`, reached by **3** PCs (`22.3/23.33=95.59%`).
- 99% target is `23.0967`, reached by **4** PCs (`23.3/23.33=99.87%`).

For `x=(-3,-2,2,1,2,4)`, dot products with the two supplied component columns are `-0.121` and `0.625`. Thus the two-dimensional PCA coordinate reported by the key is `(-0.121,0.625)`.

**Exam writing:** sort eigenvalues descending, show total and threshold products for 95%/99%, then display each projection dot product before the final coordinate.  
**Common mistake:** preserving eigenvalues in ascending order and selecting the smallest first.  
**Watermark:** pp. 93-100 and 133-134.

## Must-practice order

1. 2026 regular Q3-Q5.
2. 2026 regular Q1-Q2.
3. 2026 makeup Q2-Q6.
4. September 2025 Q2, Q5 and Q6.
5. The final three older items only after the recent set.

## Solution-bank audit

- [x] Exactly 20 high-value solved items, recent actual PYQs first.
- [x] Every item labelled `[ACTUAL PYQ]` and tied to a repository paper/key.
- [x] Marks omitted when not verified; no session invented for solution-only keys.
- [x] Numericals independently recalculated, including the conflicted 2026 regular Q5.
- [x] Each answer includes method, final conclusion, exam guidance/trap and watermark lookup.

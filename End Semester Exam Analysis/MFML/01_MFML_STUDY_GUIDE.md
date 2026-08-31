# MFML End-Sem Study Guide

Use this guide to learn the method. Use `02_MFML_PYQ_SOLUTIONS.md` to practise writing, `04_MFML_FORMULA_SHEET.md` during revision, and `06_MFML_WATERMARK_INDEX.md` to navigate the permitted PDF.

## Exam orientation

- **Current handout:** comprehensive exam is open book, 150 minutes, 40%, sessions 1-16. The printed date `06/12/2026` means **6 December 2026** under the repository's day/month convention.
- **Latest regular structure (1 March 2026):** five 8-mark questions.
- **Latest makeup structure (8 March 2026):** six questions, mostly 4-8 mark multi-step numericals.
- **Stable recent balance:** linear algebra + optimization + SVM dominate; PCA, inner products and SVD rotate through the remaining blocks.
- **Working rule:** recognize the workflow from memory, then use the watermark only to verify notation or a long formula.

## Priority map

| Topic | Priority | First outcome | Time |
|---|---|---|---:|
| rank/basis/eigen | MUST | solve recent Q1-Q2 without notes | 4 h |
| Hessian/GD/momentum/line search | MUST | compute two iterations cleanly | 4 h |
| Lagrange/dual/KKT | MUST | write four/five checks in correct sign convention | 2 h |
| SVM/hinge/margin | MUST | formulate, score points, identify support vectors | 2.5 h |
| PCA | HIGH | center -> covariance -> eigen -> project | 1.75 h |
| kernels | HIGH | derive feature-map dot product and Gram matrix | 1.25 h |
| SVD | HIGH | `A^T A -> V,sigma -> U` | 1.5 h |
| SPD inner product/Gram-Schmidt | HIGH | prove SPD and orthonormalize | 1.25 h |
| chain rule/matrix gradients | SHOULD | dimension-safe derivative | 1 h |

## Concept guide

### 1. Rank, span, basis and subspace

**What it is.** A span is every linear combination of a set. A basis is a spanning set with no redundancy. Rank is the number of pivot columns and equals the dimension of the column space. Nullity is `n-rank(A)` for an `m x n` matrix.

**Understand:** RREF identifies pivot positions, but a column-space basis must use the corresponding **original** columns. `span{v_i}` is automatically a subspace. A constraint `Ax=0` gives a subspace; `Ax=b` with nonzero `b` is usually affine, not a subspace.

**Memorize:**

`rank(A)=number of pivots`, `nullity(A)=n-rank(A)`.

**How tested:** dependence, basis/dimension, membership, rank, subspace proof.

**Common mistakes:** computing a determinant of a rectangular matrix; using RREF columns as a column-space basis; stating "span is a subspace" without showing the generated-vector form when justification is requested.

**1-MINUTE REVISION:** columns independent iff `Ax=0` has only zero solution; pivot original columns form a column-space basis; span is closed under addition/scaling.

### 2. Eigenstructure and diagonalization

**What it is.** `Av=lambda v` means `A` scales a nonzero direction `v`. Solve `det(A-lambda I)=0`, then `(A-lambda I)v=0`.

**Understand:** repeated eigenvalues need enough independent eigenvectors. `A=PDP^-1` requires `n` independent eigenvectors. Symmetric real matrices have an orthonormal eigenbasis.

**Memorize:** algebraic multiplicity is root multiplicity; geometric multiplicity is eigenspace dimension; diagonalizable iff total independent eigenvectors is `n`.

**How tested:** all eigenvalues/vectors, largest eigenspace, basis/dimension, construct `P,D`, justify diagonalizability.

**Common mistakes:** treating the zero vector as an eigenvector; forgetting free variables; mismatching the order of columns in `P` and diagonal entries in `D`.

**1-MINUTE REVISION:** characteristic polynomial -> eigenspaces -> count vectors -> `AP=PD` check.

### 3. SPD inner products and Gram-Schmidt

`<u,v>_A=u^TAv` defines an inner product when `A` is symmetric positive definite. For a symmetric matrix, Sylvester's criterion checks positive leading principal minors.

The induced norm is `||x||_A=sqrt(x^TAx)`. In Gram-Schmidt under this inner product:

`u2=v2-(<v2,v1>_A/<v1,v1>_A)v1`, then normalize with the `A`-norm.

**Common mistakes:** proving symmetry but not positivity; using the Euclidean dot product inside an `A`-inner-product question; normalizing before removing the projection.

**1-MINUTE REVISION:** symmetric + PD; compute every projection and norm with `u^TAv`.

### 4. SVD and low-rank approximation

Every `m x n` matrix has `A=U Sigma V^T`. Right singular vectors are orthonormal eigenvectors of `A^TA`; `sigma_i=sqrt(lambda_i)`; `u_i=Av_i/sigma_i` for nonzero singular values.

PCA connection: if centered observations are rows, covariance is `(1/N)X^TX`, so its eigenvectors are right singular vectors and eigenvalues are `sigma_i^2/N`.

**Common mistakes:** using eigenvalues directly as singular values; forgetting dimensions; not centering data for PCA; failing to order singular values.

**1-MINUTE REVISION:** `A^TA -> (lambda,V) -> sigma -> U`; keep top singular triplets for best low-rank approximation.

### 5. Gradient, Hessian and convexity

The gradient is the direction of steepest increase; GD moves opposite it. The Hessian contains second derivatives.

For a stationary point in two variables with `D=f_xx f_yy-f_xy^2`:

- `D>0, f_xx>0`: local minimum;
- `D>0, f_xx<0`: local maximum;
- `D<0`: saddle;
- `D=0`: inconclusive.

For a twice differentiable function, `H(x)` positive semidefinite everywhere implies convexity; positive definite implies strict convexity.

**Common mistakes:** classifying before solving `grad f=0`; confusing a local minimum with global without convexity; dropping the `1/2` convention in squared error.

**1-MINUTE REVISION:** derive gradient, solve stationarity, evaluate Hessian, state the conclusion.

### 6. GD, learning-rate decay, line search and momentum

Plain GD: `w^(t)=w^(t-1)-eta_t grad J(w^(t-1))`.

Inverse decay: `eta_t=eta_0/(1+kt)`. Compute `eta_t` before the gradient update. Line search reduces the multivariable problem to `phi(alpha)=J(w+alpha d)`; the sign of `phi'(mid)` tells which half contains the minimum.

Momentum convention used in recent keys:

`v_t=beta v_(t-1)-eta grad J(w_(t-1))`, `w_t=w_(t-1)+v_t`, `v_0=0`.

If the paper states another convention, use it and say so.

**Common mistakes:** reusing `eta_1` at iteration 2; evaluating the second gradient at the initial point; mixing velocity conventions; rounding too early.

**1-MINUTE REVISION:** rate -> gradient at current point -> velocity/update -> new point -> repeat.

### 7. Lagrangian duality and KKT

Write inequalities as `g_i(x)<=0`. Then

`L(x,lambda,nu)=f(x)+sum lambda_i g_i(x)+sum nu_j h_j(x)`, with `lambda_i>=0`.

KKT checklist:

1. primal feasibility;
2. dual feasibility;
3. complementary slackness `lambda_i g_i(x)=0`;
4. stationarity `grad_x L=0`.

For convex objectives/inequalities, affine equalities and a Slater point, KKT is sufficient and strong duality holds.

**Common mistakes:** using an `>=0` constraint with a nonnegative multiplier without converting signs; omitting complementarity; calling `L` itself the dual. The dual function is `q(lambda,nu)=inf_x L` and the dual problem maximizes `q`.

**1-MINUTE REVISION:** standardize signs -> Lagrangian -> minimize over primal variables -> maximize dual -> check four KKT groups.

### 8. PCA

PCA finds directions of maximum variance.

1. center each feature;
2. form `S=(1/N)X_c^TX_c` when observations are rows;
3. find eigenpairs, descending eigenvalues;
4. choose top eigenvectors;
5. coordinates `Z=X_c B`; reconstruction `X_hat=ZB^T+mean`.

Explained-variance ratio for top `k`: `sum_{i=1}^k lambda_i / sum_i lambda_i`.

**Common mistakes:** projecting uncentered data; using the smallest eigenvector; giving a vector without normalization when unit direction is asked; confusing coordinates with reconstructed points.

**1-MINUTE REVISION:** center -> covariance -> descending eigenpairs -> project -> variance ratio.

### 9. SVM, hinge loss and kernels

Hard margin:

`min_(w,b) 1/2||w||^2` subject to `y_i(w^Tx_i+b)>=1`.

The decision boundary is `w^Tx+b=0`; canonical margin planes are `=+1` and `=-1`; full width is `2/||w||`. Support vectors satisfy equality.

Soft margin introduces `xi_i>=0` and `C sum xi_i`, equivalent to hinge loss `max(0,1-y_i f_i)`.

Interpret functional margin `m_i=y_i f_i`:

- `m_i<0`: misclassified;
- `0<m_i<1`: correctly classified but inside margin;
- `m_i>=1`: no hinge loss.

A kernel is an inner product in feature space. Compute a Gram matrix entry-by-entry as `K_ij=k(x_i,x_j)`.

**Common mistakes:** calling every zero-hinge point a support vector; using `1/||w||` when the question asks full margin width; forgetting the regularizer in objective comparison.

**1-MINUTE REVISION:** score -> functional margin -> hinge; boundary and margin are different lines; kernels replace dot products in the dual.

## Numerical recognition templates

| If the question says... | Attack |
|---|---|
| rank/basis/dependence | stack vectors as columns -> RREF -> pivots/free variables -> original-column basis -> conclusion |
| eigen/diagonalize | characteristic polynomial -> eigenspaces -> independent eigenvectors -> `P,D` -> `AP=PD` |
| SVD | `A^TA` -> sorted eigenpairs -> square roots -> `u=Av/sigma` -> dimension check |
| two GD steps | write update convention -> compute rate -> gradient -> update -> repeat without early rounding |
| line search | form `phi(alpha)` -> differentiate -> test midpoint -> retain correct interval |
| PCA | center -> covariance using stated divisor -> eigenpairs -> principal direction -> coordinates/variance |
| KKT | standardize `g<=0` -> `L` -> four checks -> state optimality condition |
| hinge/objective | calculate `f_i`, `m_i`, hinge, sum, add `1/2||w||^2`, interpret points |
| kernel matrix | simplify `k` -> exploit symmetry -> fill diagonal and triangle -> PSD sanity check |

## Conceptual answer templates

**"Explain/define X"**  
Definition -> governing formula -> mechanism/property -> one consequence -> conclusion.

**"Justify"**  
Claim -> criterion/theorem -> substitute facts -> explicit conclusion. Never stop after the claim.

**"Compare"**  
State common objective -> table of rule/strength/weakness -> use-case conclusion.

**"Prove convex"**  
State differentiability -> compute Hessian -> show PSD/PD (principal minors/eigenvalues) -> conclude convex/strictly convex.

**"Describe an algorithm"**  
Input -> initialization -> repeated calculation/update -> stopping/output -> one failure mode.

## How to write BITS exam answers

### Numerical, 7-8 marks

Write **Given**, **Required**, **Method**, all intermediate matrices/vectors, a boxed final value, and one interpretation/check. Method marks survive an arithmetic slip only when the method is visible.

### Derivation

Start from the stated objective, name the convention, transform one line at a time, and end with the requested expression. Do not present a memorized result without the chain.

### Conceptual / justify

Use a criterion and apply it. Example: "`A` is symmetric. Its leading principal minors are positive. Hence `A` is positive definite by Sylvester, so `u^TAv` is an inner product."

### Comparison

Use a compact table, then make a decision tied to the data. For SVM `C`, say exactly what happens to penalty, margin and tolerance of violations.

### Diagram / geometry

Label axes, boundary `w^Tx+b=0`, margin lines `=+/-1`, classes and support vectors. A rough diagram without equations is not a complete answer.

## Common traps checklist

- Determinant is undefined for a non-square matrix.
- Pivot **positions** come from RREF; column-space basis vectors come from the original matrix.
- Singular values are nonnegative square roots.
- PCA needs centering and the divisor (`1/N` or `1/(N-1)`) specified by the paper.
- State row/column orientation of the data matrix.
- State the momentum convention.
- Keep four decimals through iterative calculations.
- Standardize all KKT inequalities to one sign convention.
- Support vector, margin error and misclassified point are not synonyms.
- Open-book lookup is for verification; do not search for a workflow you have not practised.

## 18-hour subject route

| Block | Work | Output |
|---:|---|---|
| 1-2 | rank/basis/subspace | redo 2026 regular Q2 |
| 3-4 | eigen/diagonalization + compact SVD | redo 2026 regular Q1 |
| 5 | SPD/Gram-Schmidt | redo makeup Q2 |
| 6-7 | gradient/Hessian/regression | derive 2026 regular Q4(a-b) |
| 8-9 | GD decay, line search, momentum | redo regular Q4(c), makeup Q3-Q4 |
| 10-11 | Lagrange/dual/KKT | redo regular Q3 |
| 12-13 | PCA | redo makeup Q5 and Sep-2025 Q2 |
| 14-16 | SVM hard/soft, hinge and kernel | redo regular Q5, makeup Q6, Sep-2025 Q6 |
| 17 | chain rule + adaptive optimizer skim | formula recall |
| 18 | closed-notes mini-paper + watermark lookup drill | error log and tabs |

# MFML End-Sem Study Guide

## Official syllabus map

Sessions 1–3: linear systems, vector spaces, rank/basis, norms/inner products/orthogonality. Sessions 4–5: determinant, trace, eigen, Cholesky, diagonalization, SVD, low-rank approximation. Sessions 6–8: derivatives, gradients/Jacobians, backprop, Hessian, Taylor, unconstrained extrema. Sessions 9–11: GD, constrained/convex optimization, SGD and adaptive optimizers. Sessions 12–13: PCA. Sessions 14–16: KKT, primal/dual SVM, kernels.

## Priority map

| Topic | Priority | Recent evidence | Typical form | Difficulty | Learn / practice / skip |
|---|---|---|---|---|---|
| Eigenvalues, eigenspaces, diagonalization | 🔴 | Feb-2026 Q1; Mar-2026 makeup Q1; 2024 regular Q2 | numerical + justification | medium | characteristic polynomial, multiplicity, basis of eigenspace, `A=PDP^-1`; practice repeated eigenvalues; skip long proofs |
| Rank, basis, subspace, independence | 🔴 | both 2026 variants; 2024 regular Q1 | numerical/proof | easy-medium | RREF, pivots/free variables, closure test, dimension; practice rectangular matrices |
| Matrix calculus & chain rule | 🔴 | Feb-2026 regression/GD; recurring 2022–24 | derivation/numerical | medium | standard gradients, Jacobian chain, least-squares gradient; skip formal differential notation beyond use |
| GD and momentum | 🔴 | Feb-2026 Q4; Mar-2026 Q4; 2024 regular Q4 | 2 iterations + compare | easy-medium | update convention, gradient, convergence intuition; practice arithmetic |
| SVM, hinge loss, kernels | 🔴 | Feb/Mar-2026 Q5–6; 2024 Q5–6; recurring older papers | numerical + theory | medium-hard | primal/dual, margin, support vectors, hinge, kernel matrix/map; skip deep generalization proofs |
| SVD | 🟡 | latest regular Q1(c) is only 1 mark; 2024 Q2 was larger | full decomposition or singular values | medium-hard | compute via `A^TA`; practice one small matrix; do not over-invest |
| PCA | 🟠 | Mar-2026 Q5; 2024 and older recurrence | covariance/eigen/projection | medium | center, covariance, direction, projection, explained variance; skip latent-variable proof |
| KKT/Lagrange/duality | 🔴 | latest original regular Q3 allocates 8 marks across inner-product/constrained primal/dual/KKT | formulation/check | hard | four KKT conditions, sign convention, dual function; practice one equality + inequalities |
| Inner products/norms/orthogonality | 🟡 | Feb-2026 Q3; older recurring | verify/compute | medium | positive definiteness, induced norm, Gram-Schmidt |
| Convexity/Taylor/Hessian | 🟡 | older strong; less explicit in both latest | proof/classification | medium | convex-set/function definitions, Hessian test, second-order Taylor |
| AdaGrad/RMSProp/Adam prose | 🟢 | syllabus, limited latest direct marks | compare/update | easy | know update idea and when useful; do not spend time on convergence proof |

Frequency note: after deduplicating QP/key copies, eigen/linear algebra, calculus/GD, and SVM occur across nearly every available 2022–26 sitting; SVD is less frequent but present in the latest regular paper. PCA remains historically strong but is less consistent across the two newest variants.

### Cross-paper frequency (8 identifiable regular/makeup sittings, 2022–2026)

| Topic family | Paper presence | Usual testing mode | Typical marks |
|---|---:|---|---:|
| Eigen/diagonalization | 8/8 | numerical + justification | 5–8 |
| Rank/vector spaces | 7/8 | numerical/proof | 5–8 |
| Calculus/gradients | 7/8 | derivation/numerical | 3–7 |
| GD/optimization | 6/8 | iteration/convergence | 5–8 |
| SVM/kernels | 7/8 | numerical + formulation | 6–10 |
| PCA | 5/8 | covariance/eigen/projection | 4–8 |
| KKT/Lagrange | 4/8 | formulation/verification | 4–8 |
| SVD | 3/8 | full decomposition/relationship | 4–7 |

Counts are conservative paper-presence counts, not number of subparts; a topic appearing twice in one paper counts once.

## Recent paper signal

- **Latest: Mar-2026 makeup:** eigen/eigenspace and independence; matrix property/proof; learning-rate/optimization reasoning; momentum; PCA; SVM/kernel. Strongly numerical, multi-step, and method-explicit.
- **Second-latest/current regular original (1 Mar 2026):** exactly five 8-mark blocks: (1) eigen/diagonalization plus a 1-mark singular-value part; (2) dependence/span/basis/rank; (3) induced inner product, constrained primal, Lagrange dual and KKT; (4) Hessian/convexity, gradient and two GD iterations with inverse-decay learning rate; (5) hard-margin SVM hyperplane, `w`, `b`, and support vectors. This is the clearest current blueprint.
- **In both:** linear algebra foundations, GD/momentum, and SVM. Stable style: 5–8 mark numerical blocks with intermediate marks.
- **Older but reduced:** long abstract proof-only questions and exotic complexity arguments. Keep definitions, but spend practice time on concrete calculations.

## Concepts from zero

### Linear systems and vector spaces

`Ax=b` asks whether `b` is a linear combination of columns of `A`. RREF reveals pivot columns and free variables. The column-space dimension is rank; the null-space dimension is `n-rank(A)`.

Subspace test: a nonempty set `W` is a subspace if `u+v in W` and `cu in W`. For a span, subspace is automatic. For a constraint set, homogeneous linear constraints (`Ax=0`) form a subspace; affine constraints (`Ax=b`, `b != 0`) usually do not.

### Eigen, SVD, PCA

An eigenvector keeps direction under `A`: `Av=lambda v`. A diagonalizable matrix has enough independent eigenvectors. For symmetric matrices, eigenvectors can be orthonormal.

SVD works for every matrix: `A=U Sigma V^T`. Right singular vectors are eigenvectors of `A^TA`; singular values are square roots of its eigenvalues. PCA is SVD/eigen-analysis applied to centered data: the top eigenvector of covariance is the maximum-variance direction.

### Calculus and optimization

The gradient points uphill; GD moves opposite. Hessian positive definite at a stationary point implies a strict local minimum. With constraints, the optimum balances the objective gradient against active constraint gradients—captured by Lagrange multipliers/KKT.

### SVM

SVM seeks a wide-margin separator. Hard margin demands all `y_i(w^Tx_i+b)>=1`; soft margin tolerates violations with hinge penalties. Only points with nonzero dual multipliers affect `w`; these are support vectors. Kernels replace inner products in the dual.

## Step-by-step numerical methods

### Eigen/diagonalization

1. Compute `det(A-lambda I)=0`.
2. For each eigenvalue solve `(A-lambda I)v=0`.
3. Count independent eigenvectors; if `n`, construct `P=[v1 ... vn]`, `D=diag(lambda_i)`.
4. Verify `AP=PD`.

### SVD

1. Form `A^TA` and find eigenpairs.
2. Sort eigenvalues descending; `sigma_i=sqrt(lambda_i)`.
3. Normalize right eigenvectors to obtain columns of `V`.
4. Obtain `u_i=Av_i/sigma_i`; complete orthonormal basis if required.
5. Check dimensions and reconstruct.

### GD/momentum

For `J=(w0-a)^2+(w1-b)^2`, gradient is `[2(w0-a),2(w1-b)]`.

Example: start `(1.5,1.5)`, target `(1,1)`, `eta=.05`. Plain GD: gradient `(1,1)`, so first point `(1.45,1.45)`; next gradient `(.9,.9)`, so `(1.405,1.405)`. With momentum, state the exact convention before calculating; papers award method marks when conventions differ.

### Soft-margin objective

For each proposed `(w,b)`:

1. Margin term `0.5||w||^2`.
2. Score `f_i=w^Tx_i+b`.
3. Functional margin `m_i=y_i f_i`.
4. Hinge `max(0,1-m_i)`.
5. Total `0.5||w||^2+C sum hinge_i`.
6. `m_i<=0` is misclassified; `0<m_i<1` correct but within margin; `m_i>=1` safely classified.

## Question patterns you must be able to solve

### Pattern 1: Eigenstructure to diagonalization

- Wording: “Find all eigenvalues/eigenvectors, eigenspace, basis/dimension; diagonalize.”
- Method: characteristic equation -> null spaces -> independence -> `P,D`.
- Reference: **Feb-2026 regular Q1**, **Mar-2026 makeup Q1**.
- Difficulty/priority: medium / 🔴.

### Pattern 2: SVD and maximum-variance direction

- Wording: “Find SVD; if A is data, determine covariance eigenvalues and maximum variance direction.”
- Method: `A^TA`; singular values; largest singular/eigenvector.
- Reference: **2024 regular Q2**, echoed in Feb-2026.
- Difficulty/priority: medium-hard / 🟠.

### Pattern 3: Two GD/momentum iterations

- Wording: “Given alpha, beta, initial point, calculate first two iterates and compare.”
- Method: gradient -> velocity -> update, showing every vector.
- Reference: **2024 regular Q4**, **Mar-2026 makeup Q4**.
- Difficulty/priority: easy-medium / 🔴.

### Pattern 4: Kernel matrix or feature map

- Wording: “Show `k(x,z)=phi(x)^Tphi(z)`; compute Gram matrix.”
- Example: `phi(x)=[1,sqrt(2)x,x^2]` gives `(1+xz)^2`.
- Reference: **2024 regular Q6**.
- Difficulty/priority: medium / 🔴.

### Pattern 5: Compare soft-margin classifiers

- Wording: “Compute margin, hinge losses, objective, identify errors.”
- Reference: **2024 regular Q5** and 2026 SVM blocks.
- Difficulty/priority: medium / 🔴.

### Pattern 6: KKT verification

- Wording: “Formulate primal/Lagrangian; verify point and multipliers satisfy KKT.”
- Checklist: primal feasibility; lambda>=0; stationarity; lambda_i g_i=0.
- Reference: **latest original regular (1 Mar 2026) Q3**, worth 8 marks with related subparts; also 2022–23 regular Q1(c).
- Difficulty/priority: hard / 🔴.

## Definitions worth memorizing

- Basis: linearly independent spanning set.
- Rank: dimension of column space.
- Positive definite: `x^TAx>0` for all nonzero `x` (for symmetric A).
- Convex function: `f(tx+(1-t)y)<=tf(x)+(1-t)f(y)`.
- Support vector: training point with active margin constraint/nonzero dual multiplier.
- Kernel: valid inner-product similarity in a feature space; Gram matrix must be PSD.

## Common mistakes

- Using original columns instead of pivot columns as a basis after row operations.
- Forgetting to center data for PCA.
- Treating eigenvalues as singular values rather than square roots of eigenvalues of `A^TA`.
- Losing the `1/2` factor in gradients/objectives.
- Mixing momentum conventions without stating one.
- Calling every point with hinge loss zero a support vector.
- Omitting KKT sign/feasibility checks.

## Open-book strategy

Memorize the workflow for RREF, eigen, SVD, GD, PCA and SVM; understand why each works. Look up only identities, long derivative tables, KKT sign conventions, and worked arithmetic examples. In the authorized `MFML watermark.pdf`, tab systems/RREF, eig/SVD, calculus, optimization, PCA and SVM. Do not browse all 136 pages in the exam.

## Final checklist

- [ ] Full eigen + diagonalization without help.
- [ ] Full SVD and PCA projection.
- [ ] Five matrix derivatives.
- [ ] Two momentum iterations with stated convention.
- [ ] Hinge-loss objective and kernel matrix.
- [ ] KKT four-condition check.
- [ ] Latest regular and makeup selected questions completed under 70 minutes each.

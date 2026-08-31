# MFML Question-Pattern Playbook

## Pattern dashboard

| Pattern | Examiner tests | Recognition cue | Priority | Difficulty | Representative evidence |
|---|---|---|---|---|---|
| rank/basis/subspace | pivot logic and proof | "basis, dimension, justify" | MUST | easy-medium | [ACTUAL PYQ] 2026 regular Q2; Sep-2025 Q1 |
| eigen/eigenspace/diagonalization | characteristic polynomial and multiplicity | "find all eigenvectors; AP=PD" | MUST | medium | [ACTUAL PYQ] 2026 regular Q1; makeup Q1 |
| SPD inner product/Gram-Schmidt | matrix-induced geometry | `u^TAv`, orthonormal set | HIGH | medium | [ACTUAL PYQ] 2026 regular Q3; makeup Q2 |
| SVD/PCA bridge | spectral decomposition and dimensions | "SVD; covariance direction" | HIGH | medium-hard | [ACTUAL PYQ] Sep-2025 Q2 |
| Hessian/convexity | second-order classification | "prove convex; critical point" | MUST | medium | [ACTUAL PYQ] 2026 regular Q4 |
| GD/decay/momentum | update discipline | "two iterations" | MUST | medium | [ACTUAL PYQ] both 2026 variants; Sep-2025 Q4 |
| line search | one-dimensional reduction | `phi(alpha)`, reduce interval | MUST | medium | [ACTUAL PYQ] 2026 makeup Q3 |
| Lagrange/dual/KKT | sign conventions and optimality | "formulate dual; verify KKT" | MUST | hard | [ACTUAL PYQ] 2026 regular Q3 |
| PCA | centering/eigen/projection | covariance, variance retained | HIGH | medium | [ACTUAL PYQ] 2026 makeup Q5; 2024 Q4(B) |
| hard/soft SVM | geometry and constraint arithmetic | margin/support/hinge | MUST | medium | [ACTUAL PYQ] 2026 regular Q5; makeup Q6 |
| kernel feature map/Gram matrix | inner-product expansion | `phi`, `K_ij` | HIGH | medium | [ACTUAL PYQ] Sep-2025 Q6 |
| chain rule/backprop | all computational paths | nested variables/graph | SHOULD | medium | [ACTUAL PYQ] Sep-2025 Q3 |

## 1. Rank, basis and subspace

**Typical wording:** determine dependence; prove a span is a subspace; find basis, dimension, rank.  
**Required concepts:** RREF, pivot columns, span, closure, rank-nullity.  
**Method:** vectors as columns -> row-reduce -> identify pivot positions -> return to original columns -> state basis/dimension -> prove closure if requested.  
**Fast checks:** more vectors than ambient dimension implies dependence; a nonzero determinant proves full independence only for square matrices.  
**Common mistakes:** determinant of rectangular matrix; basis from RREF columns; no justification after "dependent".

## 2. Eigenstructure and diagonalization

**Typical wording:** find eigenvalues/eigenvectors/eigenspace; basis and dimension; construct `P,D`; verify diagonalizable.  
**Formula:** `det(A-lambda I)=0`, `E_lambda=null(A-lambda I)`, `AP=PD`.  
**Method:** exploit triangular/block form -> solve each null space -> compare algebraic/geometric multiplicities -> align `P` columns with `D`.  
**Common mistakes:** only one vector for a repeated eigenvalue; failing to normalize only when the question actually asks; misordered `P,D`.

## 3. SPD inner products and Gram-Schmidt

**Typical wording:** prove `u^TAv` is an inner product; find distance/orthogonality; construct an orthonormal set.  
**Formula:** `<u,v>_A=u^TAv`; `proj_u(v)=(<v,u>_A/<u,u>_A)u`.  
**Method:** symmetry -> Sylvester/eigenvalue PD check -> compute every dot product and norm with `A` -> subtract projection -> normalize.  
**Common mistakes:** Euclidean projection in an `A`-geometry; checking all principal minors instead of the required leading minors without explanation; forgetting positive definiteness.

## 4. SVD and PCA bridge

**Typical wording:** find `U Sigma V^T`; if `A` is data, find covariance eigenvalues and maximum-variance direction.  
**Formula:** `A^TA v_i=sigma_i^2 v_i`, `u_i=Av_i/sigma_i`; for centered row-data, `S=A^TA/N`.  
**Method:** compute `A^TA` -> order eigenpairs -> build `V,Sigma,U` -> verify dimensions -> scale eigenvalues for covariance.  
**Common mistakes:** failing to center; mixing row-data and column-data conventions; using `lambda` rather than `sqrt(lambda)` as `sigma`.

## 5. Hessian, convexity and regression loss

**Typical wording:** formulate squared error; derive gradient/Hessian; prove convex; classify critical point.  
**Formula:** for `J=1/2||Xw-y||^2`, `grad J=X^T(Xw-y)`, `H=X^TX`.  
**Method:** write residuals -> expand only as needed -> differentiate -> show PSD/PD by `z^THz`, eigenvalues or principal minors -> conclude.  
**Common mistakes:** using a stationary-point Hessian test to claim global convexity without checking all points; dropping/adding factor 2.

## 6. GD, decay and momentum

**Typical wording:** perform the first two iterations; compare plain and momentum; use inverse/exponential decay.  
**Formula:** `w_t=w_(t-1)-eta_t g_(t-1)`; momentum convention must be stated.  
**Method:** write convention -> rate at current index -> gradient at current point -> update -> preserve four decimals -> repeat -> compare objective/distance.  
**Common mistakes:** update-rate off-by-one; second gradient at old point; sign duplicated inside velocity.

## 7. Line search

**Typical wording:** define `phi(alpha)` along the negative gradient; reduce an interval after two binary/golden steps; verify exact minimizer.  
**Formula:** `phi(alpha)=J(w+alpha d)`.  
**Method:** find `d` -> substitute to make a scalar function -> differentiate -> test midpoint derivative -> keep the side containing sign change -> solve `phi'=0` and check `phi''>0`.  
**Common mistakes:** differentiating the original multivariate function after substitution inconsistently; retaining the wrong half when derivative is positive.

## 8. Lagrangian dual and KKT

**Typical wording:** formulate constrained problem and dual; verify a supplied optimum/multipliers.  
**Required concepts:** standard `g<=0`, dual function, primal/dual feasibility, complementarity, stationarity, convex sufficiency.  
**Method:** normalize signs -> `L` -> solve `grad_x L=0` -> substitute for `q` -> state `max q` -> evaluate all KKT groups -> conclude global optimum if conditions allow.  
**Common mistakes:** calling `L` the dual; not minimizing over primal variables; missing `lambda>=0`; wrong sign on an originally `>=` constraint.

## 9. PCA covariance, projection and variance

**Typical wording:** compute covariance and principal direction; give coordinates/reconstruction; minimum components for a variance threshold.  
**Formula:** `S=X_c^TX_c/N`, `z=X_c b`, ratio `sum top lambda/sum all lambda`.  
**Method:** center -> state divisor -> symmetric covariance -> descending eigenpairs -> normalize -> project -> interpret.  
**Common mistakes:** choosing the smallest eigenvalue; not sorting before cumulative variance; confusing projected coordinate `z` with reconstructed point `zb^T+mean`.

## 10. Hard/soft SVM and hinge loss

**Typical wording:** formulate primal; determine hyperplane, margin and support vectors; compare candidate models; derive hinge form.  
**Formula:** `m_i=y_i(w^Tx_i+b)`; hinge `max(0,1-m_i)`; full margin `2/||w||`.  
**Method:** write constraints -> use nearest opposing points for canonical equalities -> solve `w,b` -> check all margins -> identify equality points -> for soft margin add hinge and regularizer.  
**Common mistakes:** using classification sign alone to identify support vectors; forgetting `C`; confusing geometric margin with functional margin.

## 11. Kernel map and Gram matrix

**Typical wording:** show a feature map produces a kernel; compute `K`; explain nonlinear separation.  
**Method:** expand `phi(x)^Tphi(z)` term by term -> simplify -> fill only the upper triangle -> mirror -> perform symmetry/PSD sanity check.  
**Common mistakes:** wrong square-root coefficient; applying labels inside `K` when only the Gram matrix is asked.

## 12. Chain rule and backprop

**Typical wording:** intermediate variables depend on `u,v`; compute total derivatives; draw computation graph and derive parameter/input gradients.  
**Formula:** `grad_x(f o g)=J_g^T grad f`; add contributions from every downstream path.  
**Method:** list local derivatives -> trace each path -> multiply along a path -> sum parallel paths -> check dimensions.  
**Common mistakes:** omitting a path; transposing by habit without a dimension check.

## Recent versus older emphasis

- **Growing/stable:** block-style calculations, two-iteration optimization, complete SVM formulations, explicit KKT checks.
- **Stable rotating:** PCA, SPD inner products, SVD.
- **Reduced recent return:** long abstract proofs and unusual complexity arguments from 2022-24. Learn definitions and one proof template, but do not let them displace recent numericals.
- **Insufficient evidence:** exact future split between hard and soft SVM; exact appearance of adaptive optimizers. Prepare the family, not an exact question.

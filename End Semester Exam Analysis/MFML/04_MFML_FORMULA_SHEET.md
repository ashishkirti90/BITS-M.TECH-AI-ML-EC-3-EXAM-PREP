# MFML Formula and Method Sheet

## Linear algebra

| Item | Formula / rule | Meaning / condition |
|---|---|---|
| rank | `rank(A)=# pivots` | dimension of row/column space |
| rank-nullity | `rank(A)+nullity(A)=n` | `A` is `m x n` |
| system consistency | `rank(A)=rank([A|b])` | otherwise no solution |
| unique solution | common rank `=n` | `n` unknowns |
| eigenpair | `Av=lambda v`, `v!=0` | solve `det(A-lambda I)=0` |
| eigenspace | `E_lambda=null(A-lambda I)` | dimension = geometric multiplicity |
| diagonalization | `A=PDP^-1`, equivalently `AP=PD` | columns of `P` are `n` independent eigenvectors |
| trace/determinant | `tr(A)=sum lambda_i`, `det(A)=product lambda_i` | eigenvalues counted with multiplicity |
| SPD | `x^TAx>0` for all `x!=0` | symmetric `A`; equivalent to all eigenvalues positive |
| Sylvester | all leading principal minors positive | test for symmetric PD |

## Inner product geometry

`<x,y>_A=x^TAy`, where `A` must be symmetric positive definite.

- norm: `||x||_A=sqrt(x^TAx)`;
- distance: `d_A(x,y)=sqrt((x-y)^TA(x-y))`;
- orthogonal: `x^TAy=0`;
- projection: `proj_u(v)=(<v,u>_A/<u,u>_A)u`;
- Gram-Schmidt: `u_k=v_k-sum_{j<k} proj_{u_j}(v_k)`, `e_k=u_k/||u_k||_A`.

## Matrix decompositions

### SVD

`A=U Sigma V^T`, for any `A in R^(m x n)`.

1. `A^TA v_i=lambda_i v_i`.
2. `sigma_i=sqrt(lambda_i)`, ordered decreasing and nonnegative.
3. `u_i=Av_i/sigma_i` for `sigma_i>0`.
4. Best rank-`k`: `A_k=sum_(i=1)^k sigma_i u_i v_i^T`.
5. Errors: `||A-A_k||_2=sigma_(k+1)`; `||A-A_k||_F=sqrt(sum_(i>k)sigma_i^2)`.

### LU / Cholesky

- `A=LU`; Doolittle sets `diag(L)=1`, Crout sets `diag(U)=1`.
- Cholesky for SPD: `A=LL^T`, `L_ii>0`.
- Solve `Ax=b`: first `Ly=b`, then `Ux=y` (or `L^Tx=y` for Cholesky).

## Calculus and matrix gradients

For scalar `f:R^n->R`, `grad f=(partial f/partial x_i)` and `H_ij=partial^2 f/(partial x_i partial x_j)`.

| Function | Gradient |
|---|---|
| `a^Tx` | `a` |
| `x^TAx` | `(A+A^T)x`; if symmetric, `2Ax` |
| `1/2||x-a||^2` | `x-a` |
| `||Ax-b||^2` | `2A^T(Ax-b)` |
| `1/2||Ax-b||^2` | `A^T(Ax-b)` |
| `tr(AX)` | `A^T` |

Chain rule with column gradients: `grad_x(f o g)=J_g(x)^T grad f(g(x))`.

Second-order Taylor about `x0`, `h=x-x0`:

`f(x0+h) approx f(x0)+grad f(x0)^T h+(1/2)h^T H(x0)h`.

Two-variable stationary classification, `D=f_xx f_yy-f_xy^2`:

- `D>0,f_xx>0`: minimum;
- `D>0,f_xx<0`: maximum;
- `D<0`: saddle;
- `D=0`: inconclusive.

## Gradient methods

### Plain and decayed GD

`w_t=w_(t-1)-eta_t grad J(w_(t-1))`.

- inverse decay: `eta_t=eta_0/(1+kt)`;
- exponential decay: `eta_t=eta_0 exp(-kt)`.

### Line search

`d_t=-grad J(w_t)`, `phi(alpha)=J(w_t+alpha d_t)`, `alpha_t=argmin phi(alpha)`.

Binary derivative rule: if `phi'(mid)>0`, minimum is left; if `<0`, minimum is right, assuming unimodality/convexity on the interval.

### Momentum and adaptive methods

State the convention. Recent keys use:

`v_t=beta v_(t-1)-eta grad J(w_(t-1))`, `w_t=w_(t-1)+v_t`.

- AdaGrad accumulator: `G_t=G_(t-1)+g_t^2`; update `w<-w-eta g_t/(sqrt(G_t)+eps)`.
- RMSProp: `G_t=rho G_(t-1)+(1-rho)g_t^2`; same scaled update.
- Adam: `m_t=beta1 m_(t-1)+(1-beta1)g_t`; `v_t=beta2 v_(t-1)+(1-beta2)g_t^2`; bias-correct and update `w<-w-eta mhat/(sqrt(vhat)+eps)`.

Symbols: `eta` learning rate, `beta/rho` decay or momentum coefficients, `g_t` current gradient, `eps` numerical stabilizer.

## Convex optimization, duality and KKT

Standard primal:

`min_x f(x)` subject to `g_i(x)<=0`, `h_j(x)=0`.

Lagrangian:

`L(x,lambda,nu)=f(x)+sum_i lambda_i g_i(x)+sum_j nu_j h_j(x)`, `lambda_i>=0`.

Dual function/problem:

`q(lambda,nu)=inf_x L(x,lambda,nu)`;

`max q(lambda,nu)` subject to `lambda>=0`.

KKT:

1. `g_i(x*)<=0`, `h_j(x*)=0` (primal feasibility);
2. `lambda_i*>=0` (dual feasibility);
3. `lambda_i* g_i(x*)=0` (complementary slackness);
4. `grad f+sum lambda_i grad g_i+sum nu_j grad h_j=0` (stationarity).

Convex `f,g_i`, affine `h_j`, and Slater feasibility imply strong duality; KKT is then necessary and sufficient.

Convex set: `theta x+(1-theta)y in C` for `theta in [0,1]`.  
Convex function: `f(theta x+(1-theta)y)<=theta f(x)+(1-theta)f(y)`.

## PCA

Let observations be rows of `X`, feature mean `mu`, centered matrix `X_c=X-1 mu^T`.

- covariance: `S=(1/N)X_c^T X_c` (use `1/(N-1)` only if stated);
- eigenpairs: `Sb_i=lambda_i b_i`, `lambda_1>=...>=lambda_D`;
- principal coordinates: `Z=X_c B_k`;
- reconstruction: `X_hat=ZB_k^T+1 mu^T`;
- explained variance: `EVR_k=(sum_(i=1)^k lambda_i)/(sum_(i=1)^D lambda_i)`;
- SVD relation: if `X_c=U Sigma V^T`, then `b_i=v_i`, `lambda_i=sigma_i^2/N`.

## SVM and kernels

### Hard margin

`min_(w,b) 1/2||w||^2` subject to `y_i(w^Tx_i+b)>=1`.

- decision boundary: `w^Tx+b=0`;
- margin planes: `w^Tx+b=+1` and `-1`;
- distance from point to boundary: `|w^Tx+b|/||w||`;
- half-margin `1/||w||`, full width `2/||w||`;
- support vectors satisfy `y_i(w^Tx_i+b)=1` in canonical scaling.

Dual:

`max_alpha sum alpha_i-(1/2)sum_ij alpha_i alpha_j y_i y_j x_i^T x_j`,

subject to `alpha_i>=0`, `sum alpha_i y_i=0`; `w=sum alpha_i y_i x_i`.

### Soft margin and hinge

`min 1/2||w||^2+C sum xi_i`, subject to `y_i f_i>=1-xi_i`, `xi_i>=0`.

Equivalent hinge: `1/2||w||^2+C sum max(0,1-y_i f_i)`.

Interpret `m_i=y_i f_i`:

| `m_i` | classification / margin |
|---:|---|
| `<0` | misclassified |
| `=0` | on decision boundary |
| `(0,1)` | correct, inside margin |
| `=1` | canonical margin / support candidate |
| `>1` | correct, zero hinge, outside margin |

Kernel: `k(x,z)=phi(x)^Tphi(z)`; Gram matrix `K_ij=k(x_i,x_j)` must be symmetric positive semidefinite.

Common polynomial identity: `phi(x)=[1,sqrt(2)x,x^2]` gives `k(x,z)=(1+xz)^2`.

## 30-second method recall

`RREF -> pivots -> original-column basis`  
`det(A-lambda I) -> eigenspaces -> P,D`  
`A^TA -> V,sigma -> U`  
`center -> covariance -> eigen -> project`  
`rate -> gradient -> update -> repeat`  
`g<=0 -> L -> q -> max -> KKT`  
`score -> y*score -> hinge -> regularizer`  
`feature-map dot product -> Gram matrix`

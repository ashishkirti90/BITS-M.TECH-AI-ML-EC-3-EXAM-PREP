# MFML Watermark Exam-Room Index

**Resource:** `MFML watermark.pdf`  
**Verified length:** 136 PDF viewer pages  
**Numbering rule:** every page below is the **PDF viewer page**, starting at the cover as viewer page 1. It is not the small printed slide number. Most viewer pages contain four reduced lecture slides, so printed numbers and viewer numbers do not match.

## Fast exam index

```text
MFML
  Linear systems / elimination       -> viewer pp. 2-16
  Vector spaces / rank / basis       -> viewer pp. 17-26
  Inner product / orthogonality      -> viewer pp. 27-33
  Determinant / eigenstructure       -> viewer pp. 34-41
  SVD / low-rank approximation       -> viewer pp. 42-49
  Derivatives / chain / backprop     -> viewer pp. 50-61
  Taylor / Hessian / extrema         -> viewer pp. 62-66
  GD / decay / line search / SGD     -> viewer pp. 67-73
  Nonlinear optimization challenges  -> viewer pp. 74-80
  Momentum / AdaGrad / RMSProp/Adam  -> viewer pp. 81-83
  Lagrange / primal-dual / convexity -> viewer pp. 84-87
  PCA full treatment                 -> viewer pp. 88-100
  SVM formulation/examples           -> viewer pp. 106-112
  Compact definitions/linear algebra -> viewer pp. 121-129
  Calculus/Hessian recap             -> viewer pp. 129-131
  Optimizer recap                    -> viewer pp. 132-133
  PCA recap                          -> viewer pp. 133-134
  KKT/strong duality recap           -> viewer pp. 134-135
  SVM/hinge/kernel recap             -> viewer pp. 135-136
```

Pages 101-105 and 113-120 are visually embedded/low-text portions of the optimization/SVM compilation. The high-value SVM pages 106-112 and recap 135-136 were visually verified. Use the recap instead of searching the low-text pages during the exam.

## Complete logical lookup map

| Topic | Viewer page(s) | What is there | Memorize | Understand |
|---|---:|---|---|---|
| systems and solution types | 2-5 | examples of zero/one/infinite solutions, geometry | rank consistency rule | what a free variable means |
| matrix operations / compact systems | 6-10 | matrix product and `Ax=b` representation | dimension compatibility | columns as linear combinations |
| Gaussian elimination | 11-16 | elementary operations, particular/homogeneous solutions | three row operations | pivot/free-variable workflow |
| vector spaces/subspaces | 17-20 | definitions, subspace conditions, span | closure criteria | span as generated space |
| independence/basis/rank | 21-26 | elimination tests, minimal generating set, dimension | pivot rules | original-column basis logic |
| inner products | 27-31 | SPD-induced inner product, Cauchy-Schwarz, angles | `x^TAy` conditions | geometry changes with `A` |
| orthonormal basis / transformations | 32-33 | orthonormal basis and elementary transformations | projection formula | Gram-Schmidt process |
| determinant/eigen | 34-41 | characteristic polynomial, eigenspaces, spectral theorem | eigen workflow | repeated roots and symmetry |
| diagonalization/SVD | 42-47 | `A=PDP^-1`, SVD construction example | `A^TA`, `u=Av/sigma` | dimensions/order |
| low-rank/norms | 48-49 | matrix approximation and spectral norm | truncation formula | discarded singular-value error |
| derivatives/Taylor/chain | 50-55 | univariate/multivariate rules and vector gradients | chain rule | local derivative composition |
| backprop/autodiff | 56-61 | computation graph, sigmoid/backprop examples | multiply along/add across paths | dimension-safe propagation |
| Taylor/Hessian | 62-66 | mean-value/Taylor development, Hessian extrema | 2D Hessian test | curvature interpretation |
| regression/GD | 67-69 | loss formulation and negative-gradient updates | basic GD | step-size effect |
| decay/line search | 70-72 | inverse/exponential decay, line/golden search | decay formulas | derivative sign narrows interval |
| SGD | 73 | stochastic update | batch vs stochastic distinction | noisy but cheap gradients |
| nonlinear optimization | 74-80 | preprocessing, local optima, cliffs/valleys, curvature | feature normalization purpose | why first-order methods struggle |
| momentum | 81 | momentum update and intuition | one chosen convention | smoothing/acceleration and overshoot |
| AdaGrad | 82 | accumulated squared-gradient scaling | accumulator idea | diminishing effective rate |
| RMSProp / Adam | 83 | exponential second moment, first+second moments | update ingredients | why decay fixes AdaGrad freezing |
| constrained optimization | 84-85 | multipliers, primal/dual, minimax, equality/inequality | Lagrangian setup | active constraints and sign |
| convex/linear/quadratic programs | 86-87 | convexity, LP/QP, Lagrangian formulation | convex definition | when dual/KKT is sufficient |
| PCA variance view | 88-94 | covariance, maximum-variance direction, components, projection | center/covariance/eigen | why largest eigenvalue wins |
| PCA low-rank/high-D/practice | 95-100 | SVD relation, high-dimensional method, practical steps | `lambda=sigma^2/N` | coordinates vs reconstruction |
| SVM primal and geometry | 106-111 | hard/soft formulation sequence and separating geometry | hard-margin primal | canonical scaling/margin |
| worked soft-margin setup | 112 | concrete two-class optimization example | constraint pattern | translate points into inequalities |
| definitions and matrix recap | 121-129 | compact algebra, RREF, spaces, inner-product definitions, decompositions | use for verification | not a substitute for practice |
| calculus/Hessian recap | 129-131 | Taylor, chain, Hessian, matrix identities | core gradient identities | choose only needed identity |
| optimizer recap | 132-133 | GD, line search, scaling, SGD, momentum, adaptive methods | iteration order | effect of each modification |
| PCA recap | 133-134 | covariance, projection, SVD relation, steps | PCA workflow | data orientation |
| KKT recap | 134-135 | primal/dual, Slater, KKT five displayed conditions | KKT checklist | strong duality conditions |
| SVM recap | 135 | hard/soft primal, dual, support vectors | margin objective | role of nonzero dual weights |
| hinge/kernel recap | 136 | hinge objective and feature-map kernel idea | hinge formula | kernel as feature-space inner product |

## Formula / derivation / algorithm index

| Need | Viewer page |
|---|---:|
| eigen/diagonalization derivation | 37-47; recap 129 |
| SVD construction | 45-47; recap 129 |
| low-rank approximation | 48; recap 129, 134 |
| chain rule/backprop | 52-61; recap 130-131 |
| Hessian classification | 65-66; recap 131 |
| inverse/exponential learning-rate decay | 70; recap 132 |
| line/binary/golden search | 71-72; recap 132 |
| momentum | 81; recap 132 |
| AdaGrad/RMSProp/Adam | 82-83; recap 133 |
| Lagrangian/primal-dual | 84-87; recap 134 |
| KKT/Slater/strong duality | 134-135 |
| PCA algorithm | 88-100; recap 133-134 |
| hard/soft SVM | 106-112; recap 135 |
| hinge loss/kernel | 136 |

## PYQ-to-watermark map

| Actual PYQ | Concept/method | Viewer page |
|---|---|---:|
| 2026 regular Q1 | eigenvectors, diagonalization, singular values | 34-49; 129 |
| 2026 regular Q2 | independence, span, basis, rank | 17-26; 123-125 |
| 2026 regular Q3 | SPD inner product, Lagrangian, dual, KKT | 27-33; 84-87; 134-135 |
| 2026 regular Q4 | Hessian, convexity, inverse-decay GD | 65-70; 131-132 |
| 2026 regular Q5 | hard-margin SVM, support vectors | 106-112; 135 |
| 2026 makeup Q2 | SPD Gram-Schmidt | 27-33; 126-127 |
| 2026 makeup Q3 | binary line search | 69-72; 132 |
| 2026 makeup Q4 | momentum | 81; 132 |
| 2026 makeup Q5 | PCA | 88-100; 133-134 |
| 2026 makeup Q6 | soft margin and hinge | 112; 135-136 |
| Sep-2025 Q2 | SVD/PCA relation | 42-49; 95-100; 129,134 |
| Sep-2025 Q4 | momentum versus GD | 68-83; 132 |
| Sep-2025 Q5 | hinge/objective comparison | 135-136 |
| Sep-2025 Q6 | feature map and Gram matrix | 136 |

## Know, understand, look up

### Know from memory

- recognition workflow for RREF, eigen, SVD, GD, KKT, PCA and hinge;
- KKT sign convention and four condition groups;
- decision boundary versus margin planes;
- centering before PCA;
- iteration indexing.

### Understand before the exam

- why original pivot columns form the basis;
- why singular values are square roots;
- why Hessian definiteness proves convexity/classifies a point;
- why complementarity identifies active constraints;
- why support vectors determine the SVM boundary.

### Look up quickly

- long matrix derivative identities: pp. 130-131;
- exact adaptive update: p. 133;
- Slater/strong-duality wording: pp. 134-135;
- SVM dual or feature-map reminder: pp. 135-136;
- decomposition convention: p. 129.

### Too slow to search during the exam

- a full worked SVD/PCA example;
- how to row-reduce;
- the meaning of hinge loss;
- how to carry out two GD iterations;
- the sequence of KKT checks.

Practise these until procedural; use the PDF only to verify.

## Physical/digital tab suggestion

If the permitted format supports tabs/bookmarks, use only eight labels:

`RREF 17`, `EIG 34`, `SVD 42`, `HESS/GD 65`, `MOM 81`, `PCA 88`, `KKT 134`, `SVM 135`.

This keeps lookup fast and avoids a tab on every page.

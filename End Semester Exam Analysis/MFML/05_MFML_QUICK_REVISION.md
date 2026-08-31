# MFML Final Revision and Exam-Hall Plan

## If MFML gets only 6 hours

| Time | Task | Output |
|---:|---|---|
| 0:00-0:50 | 2026 regular Q1-Q2 | eigen + basis workflows from memory |
| 0:50-1:45 | 2026 regular Q4 | Hessian and two decayed-GD steps |
| 1:45-2:35 | 2026 regular Q3 | complete KKT checklist |
| 2:35-3:25 | 2026 regular Q5 + makeup Q6 | hard/soft SVM and hinge |
| 3:25-4:15 | makeup Q5 | PCA start to finish |
| 4:15-5:00 | makeup Q3-Q4 | line search and momentum |
| 5:00-5:35 | Sep-2025 Q6 | kernel identity and matrix |
| 5:35-6:00 | formula + watermark lookup drill | reach each key page in under 30 seconds |

## Final 24-hour plan

Do not add a large new topic. Use three passes.

### Pass 1 - methods (2.5 hours)

- Write RREF/basis, eigen, SVD, PCA, GD, KKT and hinge workflows on blank paper.
- Check against `04_MFML_FORMULA_SHEET.md`.
- Correct missing steps in a different color; these omissions are the revision targets.

### Pass 2 - no-notes PYQs (4 hours)

Redo:

1. 2026 regular Q3, Q4, Q5.
2. 2026 makeup Q2, Q3, Q5, Q6.
3. Sep-2025 Q2 and Q6.

For every error, record only: wrong step -> correct trigger -> watermark page.

### Pass 3 - fast recall and lookup (90 minutes)

- 20 min: formulas below.
- 20 min: KKT and SVM sign checks.
- 20 min: eigen/SVD/PCA distinctions.
- 15 min: GD indexing and momentum convention.
- 15 min: open the watermark at the fast-index pages; do not reread chapters.

Sleep is higher return than a late first attempt at a low-priority proof.

## One-minute topic cards

### Rank/basis

Pivots give rank. Original pivot columns give column-space basis. `nullity=n-rank`. A span is a subspace. Determinant only for square matrices.

### Eigen/diagonalization

`det(A-lambda I)=0`; solve each null space; repeated eigenvalue needs enough independent vectors. Align `P` columns with `D`; verify `AP=PD`.

### SPD/inner product

`u^TAv` needs symmetric PD `A`. Use positive leading principal minors. All projections/norms use the same `A`-inner product.

### SVD

`A^TA -> eigenvectors V`; `sigma=sqrt(lambda)`; `u=Av/sigma`. Dimensions: `U m x m`, `Sigma m x n`, `V n x n`.

### Hessian/convexity

Find critical points first. In 2D use `D=f_xx f_yy-f_xy^2`. Hessian PSD everywhere -> convex; PD -> strictly convex.

### GD/momentum

Compute `eta_t`, then gradient at current point, then update. Momentum: state convention. Keep at least four decimals.

### KKT

Convert to `g<=0`. Check primal, dual, complementarity, stationarity. `q=inf_x L`; dual maximizes `q`, not `L` directly.

### PCA

Center, covariance, descending eigenpairs, top direction, coordinates, explained variance. If using SVD: `lambda=sigma^2/N`.

### SVM

Boundary `f=0`; margin planes `f=+/-1`; support vectors have functional margin 1. Hinge `max(0,1-yf)`. Full width `2/||w||`.

### Kernel

Expand `phi(x)^Tphi(z)`, then fill symmetric `K`. A valid Gram matrix is PSD.

## High-risk errors

- RREF column used instead of original pivot column.
- Zero vector reported as an eigenvector.
- Singular value not square-rooted.
- PCA done without centering.
- `1/N` changed to `1/(N-1)` despite the paper convention.
- GD iteration 2 uses gradient from iteration 0.
- Momentum sign convention not stated.
- `>=0` KKT constraint not converted before using `lambda>=0`.
- Lagrangian called the dual without taking `inf_x`.
- Hinge computed from `f_i` rather than `y_i f_i`.
- Support vector confused with every correctly classified point.
- Full margin and half-margin confused.

## Mark-aware answer skeletons

### Numerical

`Given -> Required -> formula/method -> substitution -> intermediate values -> boxed result -> interpretation/check`.

### Derivation

`Starting equation -> named rule/convention -> transformations -> final expression -> condition under which it holds`.

### Justify

`Claim -> criterion -> verified facts -> explicit therefore`.

### Algorithm

`Input -> initialization -> repeated update -> stopping/output -> one caveat`.

### Comparison

Use a table for objective, update/constraint, effect and conclusion. Tie the conclusion to computed evidence.

## Exam-hall strategy (150 minutes)

### First 7 minutes

1. Scan all questions and mark `A` (immediate), `B` (workable), `C` (lookup-heavy).
2. Circle multi-step numericals with method marks.
3. Write the momentum and KKT sign convention in the margin before arithmetic.

### Working allocation

- For a five-by-eight-mark paper: about 25 minutes per question = 125 minutes.
- Keep 7 minutes for scan and 18 minutes for checks/recovery.
- If structure differs, allocate roughly `3 minutes per mark`, with a cap; return later to a stalled subpart.

### When to use the watermark

Use it to verify a derivative identity, optimizer update, KKT convention, PCA/SVM formulation or a decomposition step. Do not search for a simple formula you should know, and do not browse sequentially. Use the viewer-page index.

### Securing method marks

- State dimensions and conventions.
- Show the matrix/vector at each stage.
- Box the requested quantity, not an intermediate.
- If arithmetic becomes doubtful, carry the symbolic expression forward and interpret it.
- For an uncertain proof, state the correct criterion and verify as many conditions as possible.

### Final 15-minute audit

- every subpart answered;
- signs in KKT/SVM checked;
- determinant only for square matrices;
- eigen/singular values ordered and labelled;
- GD rates match iteration indices;
- support-vector/hinge interpretations stated;
- assumptions and data orientation written.

## Must-know versus look-up

| Know from memory | Understand | Look up fast |
|---|---|---|
| RREF/eigen/SVD/PCA workflows | why pivots/eigenvectors define spaces | long matrix derivative identities |
| GD and momentum order | effect of rate/curvature | adaptive optimizer exact updates |
| four KKT groups | sign convention and active constraints | Slater/strong-duality wording |
| hard/soft SVM objectives | margin and hinge interpretation | dual expansion / feature-map examples |
| explained-variance ratio | centering and data orientation | unusual decomposition convention |

# MFML End-Sem Evidence and Priority Analysis

**Course:** AIMLC ZC416 - Mathematical Foundations for Machine Learning  
**Preparation objective:** maximize comprehensive-exam marks in about 18-20 focused hours  
**Evidence cut-off:** repository contents audited on 30 August 2026

## Executive decision

The shortest defensible route is:

1. rank/basis/eigenstructure;
2. Hessian, gradient descent, learning-rate schedules and momentum;
3. constrained optimization, Lagrangian duality and KKT;
4. PCA;
5. hard/soft-margin SVM, hinge loss and kernels;
6. one compact SVD and one matrix-chain-rule pass.

This order is not a prediction of exact questions. It follows the strongest recent **question-type** signals. The 1 March 2026 regular EC-3 used five 8-mark blocks: eigen/SVD; dependence/basis/rank; inner product plus KKT; Hessian plus decayed GD; hard-margin SVM. The 8 March makeup retained eigen/independence, optimization and SVM, and added Gram-Schmidt, line search, momentum and PCA.

## Source precedence and scope

When sources conflict, use this order:

1. **Current course handout, version 4, dated 19 November 2025** - authoritative syllabus and examination policy.
2. **Official question paper** - authoritative wording, marks and structure.
3. **Official/identified solution key** - marking intent, only when it matches the paper.
4. Current lecture slides and `MFML watermark.pdf` - course notation and methods.
5. Existing repository end-sem and mid-sem guides - reusable structure only; all claims rechecked.

The current handout makes the comprehensive examination open book, 150 minutes, 40%, and covers sessions 1-16. Its date `06/12/2026` is interpreted under the repository's day/month convention as **6 December 2026**, not 12 June and not part of an immediate 5-6 September exam block. It includes linear systems; vector spaces and analytic geometry; eigen/Cholesky/SVD; vector and matrix calculus; Hessian/Taylor; GD, line search, SGD and adaptive methods; constrained/convex optimization; PCA; KKT; linear/nonlinear SVM and kernels.

## Evidence register

| Evidence | Internal identification | Use | Reliability / caveat |
|---|---|---|---|
| `AIML ZC416 COURSE HANDOUT.docx` | v4, 19-11-2025 | syllabus, sessions, exam policy | primary authority |
| Latest EC-3 regular PDF | First Sem 2025-26, 01-03-2026, 3 pages | latest regular structure and marks | primary QP |
| `Feb 2026 ... QP & answer key.pdf` | EC-3 regular solution package, 14 pages | marking steps for Q1-Q4 | its Q5 wording differs from the official QP; not used as authority for Q5 |
| `Mar 2026 ... makeup ...pdf` | EC-3 makeup, 08-03-2026, 11 pages | latest sitting and solution detail | course number/title says DSECL/MFDS, but content is the shared ZC416 family; treated as related makeup evidence, not silently relabelled |
| Latest EC-2 regular PDF | First Sem 2025-26, 21-12-2025, 2 pages | current foundation signal | mid-sem signal only, not counted as EC-3 recurrence |
| `2024 EndSem Regular MFML.pdf` | Second Sem 2024-25, 06-09-2025 | recent complete EC-3 paper | filename year is misleading; internal date governs |
| March/April 2025 solution keys | comprehensive regular/makeup solution keys | recent patterns and marking depth | paper headers absent; session name inferred only from filenames, so references say "solution key" |
| 2023-24 regular/makeup PDFs and keys | internally dated 07-04-2024 | older recurrence | regular and makeup show the same printed date; recorded as a metadata conflict |
| 2022-23 regular/makeup PDFs and keys | regular internally dated 01-10-2022; makeup undated | older stable patterns | lower recency weight |
| `MFML watermark.pdf` | 136 PDF viewer pages | primary exam-room lookup | actual viewer pages verified; several pages are four-up slide images, so printed slide numbers differ |
| Lectures 9-13 and SVM course material | current lecture folders | GD, nonlinear optimization, PCA, SVM notation | supports methods; not PYQ evidence |
| existing end-sem guides and question bank | repository generated Markdown | structure and candidate drills | practice labels and frequency claims were re-audited before reuse |

## Duplicate handling

- `Comprehensive_Regular_AIML.pdf` / `Comprehensive_Regular_AK.pdf` are duplicate-content copies of the 2022 regular paper/key family; counted once.
- `Comprehensive_Makeup_AIML.pdf` / `Comprehensive_Makeup_AK.pdf` are duplicate-content copies of the 2022 makeup family; counted once.
- `2023-24 EC3R_solutions.pdf` and `2023-24 EC3M_solutions.pdf` duplicate the respective 2023-24 regular/makeup answer-key families; counted once.
- Question-paper and solution-key files are not separate sittings.
- The two 2024-named MFML/MFDS solution PDFs have no reliable internal session metadata and do not match the September 2025 official paper. They provide older pattern evidence only.

## Recent paper signal

### Latest sitting: 8 March 2026 makeup

- Seven-mark eigen/eigenspace plus independence block.
- Eight-mark SPD inner product plus Gram-Schmidt block.
- Seven-mark line-search block.
- Four-mark two-iteration momentum numerical.
- Seven-mark PCA calculation.
- Seven-mark soft-margin SVM/hinge-loss block.

**Signal:** concrete calculations, explicit intermediate work, and broad coverage. Optimization is tested as both method selection and arithmetic.

### Second latest: 1 March 2026 regular

- Exactly five questions, each worth 8 marks.
- Two full linear-algebra blocks.
- One inner-product/constrained-duality/KKT block.
- One Hessian/regression/decayed-GD block.
- One hard-margin SVM block.

**Signal:** a stable 8-mark block rewards a complete workflow, not a memorized final formula.

### Latest EC-2 foundation signal: 21 December 2025

Linear systems/rank, dependence/subspace/basis, SVD/diagonalizability, SPD inner products, gradient/Hessian/Taylor all appeared. This reinforces prerequisites but is not counted as comprehensive-exam frequency.

### Repeated recent structures

| Question type | Evidence | Confidence |
|---|---|---|
| eigenvalues/eigenspaces plus basis or diagonalization | Mar-2026 regular Q1; Mar-2026 makeup Q1; Sep-2025 Q1/Q2 bridge | **VERY HIGH** |
| rank, span, basis, subspace, independence | Mar-2026 regular Q2; makeup Q1; Sep-2025 Q1 | **VERY HIGH** |
| Hessian/convexity plus GD iterations | Mar-2026 regular Q4; makeup Q3-Q4; Sep-2025 Q4 | **VERY HIGH** |
| SVM primal/margin/hinge/kernel | both Mar-2026 sittings; Sep-2025 Q5-Q6; older recurrence | **VERY HIGH** |
| KKT/Lagrangian dual | Mar-2026 regular Q3; Sep-2025 Q3; older papers | **HIGH** |
| PCA covariance/eigen/projection | Mar-2026 makeup Q5; 2025 solution key; 2024 regular Q4 | **HIGH** |
| full SVD | Sep-2025 Q2; Dec-2025 EC2 Q3; only 1 mark in Mar-2026 EC3 Q1(c) | **MODERATE-HIGH** |
| long abstract proofs | more prominent in 2022-24 papers | **LOWER recent signal**, still skim definitions |

These are confidence labels, not probabilities.

## Priority and expected return per hour

| Topic | Priority | Recent evidence | Typical form | Difficulty | Focused time | Expected return |
|---|---|---|---|---|---:|---|
| rank, span, basis, subspace, independence | MUST DO | both 2026 variants; Sep-2025 Q1 | row-reduction + justification | easy-medium | 2.0 h | 6-8 marks and prerequisite value |
| eigenstructure and diagonalization | MUST DO | both 2026 variants | full numerical | medium | 2.0 h | 5-8 marks |
| gradient, Hessian, convexity, GD schedules | MUST DO | both 2026 variants; Sep-2025 | derivation + 2 iterations | medium | 2.5 h | 7-8 marks |
| momentum and line search | MUST DO | latest makeup Q3-Q4; Sep-2025 Q4 | iteration/search interval | medium | 1.5 h | 4-7 marks |
| hard/soft SVM, hinge loss, margin | MUST DO | both 2026 variants; Sep-2025 Q5 | formulation + arithmetic | medium | 2.5 h | 7-10 marks |
| Lagrangian dual and KKT | MUST DO | 2026 regular Q3; Sep-2025 Q3 | formulate + verify | hard | 2.0 h | 5-8 marks |
| PCA workflow | HIGH | latest makeup Q5; older recurrence | covariance/eigen/projection | medium | 1.75 h | 5-7 marks |
| kernels / Gram matrix | HIGH | Sep-2025 Q6; older SVM papers | feature-map proof + matrix | medium | 1.25 h | 3-6 marks |
| SVD and low-rank approximation | HIGH | Sep-2025 Q2; latest regular 1-mark link | decomposition | medium-hard | 1.5 h | 1-7 marks; supports PCA |
| SPD inner products and Gram-Schmidt | HIGH | latest regular Q3; latest makeup Q2 | proof + orthonormalization | medium | 1.25 h | 4-8 marks |
| chain rule / backprop / matrix gradients | SHOULD DO | Sep-2025 Q3; older recurrence | derivation | medium | 1.0 h | 3-5 marks |
| AdaGrad/RMSProp/Adam concepts | SHOULD DO | handout/lectures; weak direct latest signal | compare/update | easy | 0.5 h | low direct, cheap coverage |
| LU/Cholesky, Taylor, abstract convex proofs | SKIM after core | older papers / syllabus | numerical or proof | medium | 1.0 h | backup marks |

**Core total:** about 19 hours. A 12-hour emergency cut keeps the first seven rows plus kernel recognition.

## Learning dependencies

`RREF -> rank/basis/null space -> eigenvectors -> SVD -> PCA`

`gradient -> Hessian/convexity -> GD/line search -> momentum/adaptive methods`

`constraints -> Lagrangian -> dual function -> KKT -> SVM primal/dual`

## Marks-aware writing model

| Marks | Expected depth |
|---:|---|
| 1-2 | definition/formula, direct substitution, one clear conclusion |
| 3-4 | method, key intermediate values, short justification |
| 5-6 | complete workflow with checks and interpretation |
| 7-8 | full setup, all steps, conditions/assumptions, numerical result and conclusion |

Where an official marking scheme is absent, solution depth in this package is explicitly **inferred from the paper marks**.

## Evidence gaps and conflicts

1. The 2026 regular combined solution file changes Q5 from "find the optimum" to "compare two supplied lines". The official QP is authoritative; its optimum is independently recalculated in the solution bank.
2. The March 2026 makeup header uses DSECL ZC416 / MFDS rather than AIMLC ZC416 / MFML. Its shared subject content is relevant, but the mismatch is retained in citations.
3. Several older solution-only PDFs lack complete paper/session headers. They are never given an invented session or question mark allocation.
4. Some PDF equations extract poorly. Viewer rendering was used for the high-value recent matrices and watermark image-only pages; where reconstruction remained uncertain, the item was not promoted as an actual PYQ.

## Subject self-audit

- [x] Current handout and all sessions accounted for.
- [x] Latest regular and makeup papers analyzed separately.
- [x] EC2 foundation signal separated from EC3 recurrence.
- [x] Duplicate copies counted once.
- [x] Actual PYQs, variations and original practice are labelled separately.
- [x] Question numbers and marks included only when visible in paper/key.
- [x] Important numericals independently recalculated.
- [x] Formula notation and sign conventions stated.
- [x] Answer depth tied to marks; inferred depth identified.
- [x] Watermark references use PDF viewer pages.
- [x] Unsupported exact-question predictions avoided.
- [x] Conflicts and insufficient evidence recorded rather than hidden.

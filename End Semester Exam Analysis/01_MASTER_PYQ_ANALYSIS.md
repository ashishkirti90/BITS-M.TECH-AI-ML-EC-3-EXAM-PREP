# Master PYQ Analysis

## Scope and evidence rule

This index summarizes the four subject-specific analyses without transferring patterns from one subject to another. Every prediction remains anchored to that subject's own handout, question papers, answer keys, lectures, and watermark bundle.

Evidence was weighted in this order:

1. Current official course handout for scope and exam conditions.
2. Most recent regular and make-up end-semester papers and keys.
3. Older end-semester papers and keys for recurrence.
4. Lecture and watermark material for methods, notation, and lookup support.
5. Original practice only where a source gap would otherwise leave a high-value skill untested.

Question labels are literal:

- `[ACTUAL PYQ]`: reconstructed from an identifiable supplied question paper.
- `[PYQ VARIATION]`: a clearly marked variation of a supplied PYQ.
- `[ORIGINAL PRACTICE]`: newly written practice, never presented as historical evidence.

## Coverage dashboard

| Subject | Current exam | Solved actual PYQs | Additional practice | Main analysis |
|---|---:|---:|---:|---|
| ISM | 05 Sep 2026, FN | 20 | 0 | [ISM analysis](ISM/00_ISM_ANALYSIS.md) |
| ML | 06 Sep 2026, FN | 20 | 0 | [ML analysis](ML/00_ML_ANALYSIS.md) |
| DNN | 06 Sep 2026, AN | 20 | 3 | [DNN analysis](DNN/00_DNN_ANALYSIS.md) |
| MFML | 06 Dec 2026, FN | 20 | 0 | [MFML analysis](MFML/00_MFML_ANALYSIS.md) |
| **Total** |  | **80** | **3** |  |

The MFML handout prints `06/12/2026`; this repository interprets it as 06 December 2026 because the same handout uses day/month notation elsewhere. It is therefore kept outside the immediate five-day ISM/ML/DNN sprint.

## ISM

### Highest-yield pattern cluster

1. Select and execute the correct inferential test: one/two-sample mean, proportion, chi-square, or ANOVA.
2. Confidence intervals and CLT-based standardization.
3. Correlation and simple linear regression, including interpretation.
4. Moving averages, simple exponential smoothing, and Holt trend updates.
5. Time-series identification through ACF/PACF and ARIMA/SARIMA structure.
6. MLE and mixture-model/EM reasoning.

### Recent-paper signal

Recent ISM papers reward choosing the right procedure before calculation. A correct formula with the wrong test is not enough; state the hypotheses, assumptions, statistic, critical value or p-value rule, and conclusion in context. Forecasting questions similarly reward a visible update table rather than a final number alone.

### Priority drill set

Use the first twelve worked entries in [ISM PYQ solutions](ISM/02_ISM_PYQ_SOLUTIONS.md), then add the ANOVA and ACF/ARIMA entries before attempting a timed mixed set. The quick lookup map is [ISM watermark index](ISM/06_ISM_WATERMARK_INDEX.md).

### Source limitations

Some supplied papers have incomplete or inconsistent official-key detail. The subject package records those gaps instead of silently filling them from another subject or treating a reconstructed method as an official answer.

## ML

### Highest-yield pattern cluster

1. SVM geometry, margin, support vectors, dual/KKT logic, and soft-margin interpretation.
2. Naive Bayes posterior comparison and maximum-likelihood/MAP estimation.
3. Decision trees, impurity, pruning, and ensemble contrast.
4. AdaBoost weight updates and gradient-boosting residual logic.
5. K-means and GMM/EM updates.
6. KNN with mixed features/Gower distance, regularization, and classification metrics.

### Recent-paper signal

The latest supplied regular and make-up papers heavily reward short numerical pipelines: write the governing equation, substitute cleanly, compare candidates, and interpret the result. For SVM, either global sign orientation can describe the same boundary, but the class-label convention and final classifier must be internally consistent. One supplied make-up key reverses that orientation; the worked solution explicitly corrects it.

### Priority drill set

Complete the starred/high-priority entries in [ML PYQ solutions](ML/02_ML_PYQ_SOLUTIONS.md), especially SVM, Naive Bayes, AdaBoost, K-means/GMM, and Gower distance. Use [ML watermark index](ML/06_ML_WATERMARK_INDEX.md) for open-book retrieval.

### Source limitations

The current handout specifies a 2.5-hour exam, while older papers show 2 hours. Use the current handout for timing. A masked bundle header and a source filename also disagree on one paper date; the file identity and question content are retained without inventing certainty about the disputed header.

## DNN

### Highest-yield pattern cluster

1. CNN output shapes, parameter counts, receptive-field reasoning, and transfer learning.
2. Vanilla RNN limitations; GRU and LSTM gates, dimensions, and parameter counts.
3. Scaled dot-product attention, multi-head attention, masks, and cross-attention.
4. Transformer encoder/decoder flow and positional information.
5. Optimizer update rules, regularization, dropout, batch normalization, and layer normalization.
6. Backpropagation and dense-network parameter accounting.

### Recent-paper signal

DNN repeatedly combines a conceptual explanation with a compact calculation. High-scoring answers show tensor dimensions at each step and explain why the architecture or optimizer behaves as claimed. Attention answers should name `Q`, `K`, and `V`, include the `1/sqrt(d_k)` scaling, and state where masking applies.

### Priority drill set

Start with CNN, recurrent units, attention, and optimizer/regularization entries in [DNN PYQ solutions](DNN/02_DNN_PYQ_SOLUTIONS.md). The file contains 20 actual PYQ units plus two labeled variations and one labeled original-practice item. Use [DNN watermark index](DNN/06_DNN_WATERMARK_INDEX.md) for page lookup.

### Source limitations

Where a source key omits intermediate work or leaves a notation ambiguity, the package supplies a transparent derivation and flags the evidence boundary. Practice additions remain separately labeled and are excluded from recurrence counts.

## MFML

### Highest-yield pattern cluster

1. Rank, nullity, linear independence, eigenvalues/eigenvectors, and diagonalization.
2. SVD and PCA, including variance explained and projection/reconstruction.
3. Gradients, Hessians, convexity, gradient descent, and momentum updates.
4. Constrained optimization, Lagrangians, KKT conditions, and dual reasoning.
5. Linear SVM formulation and margin geometry.

### Recent-paper signal

MFML favors fully visible algebra. Marks are commonly earned for the setup even when arithmetic later slips: row operations, characteristic polynomial, gradient/Hessian, Lagrangian, KKT feasibility, and update equations should all be written before substitution. The highest-return revision path is linear algebra followed by optimization and then PCA/SVM.

### Priority drill set

The emergency core is the first twelve high-priority entries in [MFML PYQ solutions](MFML/02_MFML_PYQ_SOLUTIONS.md). Add remaining eigen/SVD, KKT, and PCA items for a fuller preparation cycle. Use [MFML watermark index](MFML/06_MFML_WATERMARK_INDEX.md) to pre-tab the open-book source.

### Source limitations

Some supplied MFML keys are terse or absent for individual subparts. The worked package distinguishes answer-key evidence from independently recomputed solutions and does not treat a missing key as confirmation.

## Return-on-time order

This table is a workload decision aid only. It does not use one subject's PYQs to predict another subject.

| Order | Subject-specific block | Why it returns marks quickly |
|---:|---|---|
| 1 | ISM test selection + confidence intervals | Reusable decision framework across many short/medium questions |
| 2 | ML SVM + Naive Bayes | Dense recent-paper presence and algorithmic scoring steps |
| 3 | DNN CNN + attention | Recurrent dimension/parameter patterns with predictable workings |
| 4 | ISM regression + smoothing | Formula-driven and easy to verify in an open-book exam |
| 5 | ML ensembles + clustering | Standard update tables and comparison questions |
| 6 | DNN RNN/GRU/LSTM + regularization | Repeated architecture and parameter-count patterns |
| 7 | MFML linear algebra + optimization | High value for the later MFML sprint |

## Self-audit result

- Four subject packages are isolated under their own directories.
- Every subject has 20 actual worked PYQ units.
- All non-historical additions are visibly labeled and excluded from frequency claims.
- Watermark indexes use actual PDF viewer page numbers, not printed slide numbers.
- Conflicting keys, date ambiguity, and missing solutions are disclosed in the relevant subject analysis.
- The current handouts, not older paper headers, control exam duration and scope.

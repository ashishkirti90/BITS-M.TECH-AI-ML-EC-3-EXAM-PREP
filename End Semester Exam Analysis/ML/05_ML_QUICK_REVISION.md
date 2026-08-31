# ML Quick Revision and Final 24 Hours

## 15 one-minute cards

1. **Ridge/lasso:** L2 smooth shrinkage, correlated-feature stability, usually no zeros. L1 corners create zeros and sparsity. Higher lambda -> higher bias/lower variance.
2. **Logistic:** `p=sigma(w^Tx+b)`; bounded probability, linear `.5` boundary, log loss.
3. **Tree:** axis-aligned piecewise regions; deeper/smaller leaves lower bias and raise variance; pruning/stopping regularize.
4. **Gower:** numeric by range, nominal 0/1, ordinal normalized rank, mean valid contributions.
5. **Weighted KNN:** compute all requested distances; `1/d^2` lets one close case dominate. Handle `d=0` explicitly.
6. **LWR:** local weighted regression around query; state loss and whether gradient is sum/mean.
7. **NB:** prior x class-conditional likelihoods; conditional independence. Gaussian for continuous, multinomial for counts.
8. **Laplace:** `(count+alpha)/(class token total+alpha V)`; repeated token -> power.
9. **Bagging/RF:** bootstrap parallel learners reduces variance; RF adds feature randomness to reduce correlation.
10. **AdaBoost:** `epsilon=sum wrong weights`; `alpha=.5 ln((1-e)/e)`; exponential update then normalize.
11. **Gradient boost:** `F0=mean(y)` for squared loss; fit residual; `Fnew=F+eta h`.
12. **K-means:** assign all, then update all means; hard, scale-sensitive, spherical preference.
13. **GMM:** responsibility rows sum to one; `N_k`, weight, mean, covariance; soft/elliptical.
14. **SVM geometry:** `f=w^Tx+b`; distance `|f|/||w||`; half margin `1/||w||`, full width `2/||w||`.
15. **SVM dual/kernel:** `alpha>0` support; `w=sum alpha y x`; large C punishes violations; Gram storage `O(N^2)`.

## Highest-risk traps

- Calling `1/||w||` and `2/||w||` both "the margin" without declaring convention.
- Failing to check that the sign of `f(x)` matches the stated support-vector label.
- Using sample variance when the question/key specifies ML variance.
- Dividing an LWR gradient by `n` without checking the loss convention.
- Treating ordinal categories as nominal, or vice versa.
- Forgetting to normalize AdaBoost weights when the updated weights are requested.
- Updating K-means centroids point by point rather than after the assignment pass.
- Omitting mixture weights from GMM responsibilities.
- Using old GMM means in the covariance update.
- Saying bagging primarily reduces bias or that boosting is parallel.
- Selecting a model by accuracy/RMSE while ignoring an auditability or recall constraint.
- Fitting scaling/encoding on the full dataset before splitting.

## Final 24-hour ML plan

| Time before finish | Task | Required output |
|---|---|---|
| 0:00-0:45 | Formula retrieval without notes | Write all five numerical skeletons and SVM margin conventions |
| 0:45-2:00 | Latest regular Q2 + Q4 | Full Gower table and multinomial NB score |
| 2:00-3:15 | Latest regular Q3 + Q5 | AdaBoost alpha; SVM score/norm/margin/soft-margin prose |
| 3:15-4:15 | Latest regular Q6 + Q7 | K-means cycle; three one-mark model explanations |
| Break/sleep | Protect recall and calculation accuracy | No new large topic |
| 4:15-5:30 | Latest make-up Q2 + Q3 | Gaussian NB and one LWR update |
| 5:30-6:45 | Latest make-up Q4 + Q6 | Majority probability and gradient-boost leaf update |
| 6:45-8:15 | Latest make-up Q5 | Complete GMM E/M table without notes |
| 8:15-9:15 | Latest make-up Q7 | Corrected canonical SVM, dual and kernel cost |
| 9:15-9:45 | Easy marks | Ridge/lasso, tree stopping, leakage, fairness/interpretability |
| 9:45-10:15 | Watermark retrieval drill | Locate every final cheat-index page within 30 seconds |
| 10:15-11:00 | Error-log redo | Redo only previously wrong calculations |

Do not learn RBF derivations, Bayesian linear regression or genetic algorithms from scratch in the final hours unless every MUST DO pattern is already secure.

## Questions to redo without notes

1. Latest regular Q2 - full Gower and nominal-tier change.
2. Latest regular Q4 - repeated-token multinomial NB.
3. Latest regular Q5 - margin convention.
4. Latest make-up Q3 - normalization + one LWR update.
5. Latest make-up Q5 - full GMM E/M.
6. Latest make-up Q7 - canonical SVM with label verification.

## Exam-hall strategy

### First 7 minutes

1. Scan every question and write a pattern tag.
2. Mark `M` for memory-solvable, `L` for one lookup, `H` for high calculation risk.
3. Start with a complete high-confidence 5-8 mark numerical.
4. Reserve the final 15-20 minutes for checking totals, signs and skipped subparts.

### Time budget

The current handout says 2.5 hours for 40 marks. After a 7-minute scan and 18-minute review reserve, about 125 minutes remain: roughly 3.1 minutes per mark. Use the official exam notice if it supersedes the handout.

### During numerical answers

- Put formulas before numbers.
- Use labeled intermediate tables for Gower, NB, EM and boosting.
- Carry four significant digits; round once.
- State the convention and final interpretation.
- If arithmetic stalls, leave the correct formula/substitution and continue; method marks matter.

### During conceptual answers

- Answer the scenario, not the textbook chapter.
- Write mechanism and trade-off.
- For "justify", include why the alternative is weaker under the stated constraint.
- Never claim fairness, causality or certainty solely from interpretability or test accuracy.

### Open-book use

- Solve from memory first.
- Use the watermark to verify an EM/SVM expression or a long worked pattern.
- Write the lookup page beside the question during the scan.
- If the target is not found within 30-40 seconds, continue from the known method and return later.

## Final readiness checklist

- [ ] I can complete a Gower table and a one-step LWR update.
- [ ] I can solve Gaussian and multinomial NB.
- [ ] I can compute AdaBoost alpha/update and a gradient-boost residual step.
- [ ] I can run K-means and one complete GMM EM iteration.
- [ ] I can solve canonical SVM geometry and distinguish distance/half/full margin.
- [ ] I can explain ridge/lasso, tree complexity, bagging/RF/boosting and leakage in one minute each.
- [ ] I can locate the 16 high-value watermark references in under 30 seconds each.


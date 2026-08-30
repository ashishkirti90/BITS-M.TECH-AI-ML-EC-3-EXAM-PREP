# Repository Audit and Evidence Register

## Audit outcome

The repository contains the four current S2-25 handouts, lecture/companion materials, subject watermark bundles, cheat sheets, instructor notes, sample papers, and historical regular/makeup papers. The study guides use the handouts as syllabus authority and prioritize identifiable comprehensive/end-sem sittings, particularly the two 2026 variants.

## Authoritative handouts

| Subject | File | Authority used |
|---|---|---|
| MFML | `Course Handouts/AIML ZC416 COURSE HANDOUT (1).docx` | sessions 1–16, evaluation, resources, exam date |
| ISM | `Course Handouts/Introduction to Statistical Methods (S2-25_AIMLCZC418) COURSE HANDOUT.docx` | sessions 1–16, evaluation, exam date |
| DNN | `Course Handouts/Deep Neural Networks (S2-25_AIMLCZG511) COURSE HANDOUT.docx` | modular/current session scope, evaluation, exam date |
| ML | `Course Handouts/Machine Learning (S2-25_AIMLCZG565) COURSE HANDOUT.docx` | sessions 1–16, evaluation, exam date |

Duplicate ML handout copies exist under `ML/`; the `Course Handouts/` version was used as the canonical repository location.

## Primary recent PYQ evidence

| Subject | Latest | Second-latest | Additional trend papers |
|---|---|---|---|
| MFML | `MFML/Question papers/Mar 2026 MFML makeup endsem QP & answer key.pdf` | `MFML/Question papers/Feb 2026 MFML regular endsem QP & answer key.pdf` | 2024 regular/makeup; 2023 and 2022 regular/makeup |
| ISM | `ISM/Question papers/Mar 2026 ISM endsem makeup QP & answer key.pdf` | `ISM/Question papers/Feb 2026 ISM endsem regular QP & answer key.pdf` | 2024 regular; 2023 regular/makeup; prior consolidated set |
| DNN | `DNN/Question papers/Mar 2026 DNN endsem makeup answer key.pdf` | `DNN/Question papers/Mar 2026 DNN endsem regular QP & answer key.pdf` | 2024/25 regular/makeup; 2023/2022 papers; separate answer-key archive |
| ML | `ML/Question papers/Mar 2026 ML endsem makeup QP & answer key.pdf` | `ML/Question papers/Mar 2026 ML endsem regular QP & answer key.pdf` | 2021 regular/makeup; 2023–24 end-sem keys under `Previous Question Papers/ML` |

## Newly added `LATEST QUESTION PAPERS` audit

| Subject | New EC3 original | Relationship to prior evidence | Refinement enabled |
|---|---|---|---|
| MFML | `...EC3_REGULAR_28-02-2026_AN.pdf` (internal page says 01-03-2026) | original QP corresponding to the Feb/Mar-2026 regular solution bundle | exact five-question, 8-marks-each blueprint; KKT raised to must-do; SVD only 1 mark in this sitting |
| ISM | `...EC3_REGULAR_28-02-2026_FN.docx` | original QP corresponding to Feb-2026 regular answer key | exact eight 5-mark blocks; reveals randomized-block ANOVA and directional F-test details |
| DNN | `...EC3_REGULAR_01-03-2026_AN.pdf` | original QP corresponding to Mar-2026 regular answer key | corrects structure to seven questions/120 marks and verifies exact block weights |
| ML | `...EC3_REGULAR_01-03-2026_FN.doc` | original legacy Word paper for the already analyzed Mar-2026 regular cycle | metadata confirms pairing; the existing QP/answer-key bundle supplies question-level searchable text |

The four EC2 files in the folder are mid-semester papers and are excluded from end-sem topic-frequency counts. These EC3 originals are not four additional sittings, so historical frequency denominators do not increase.

The “latest”/“second-latest” ordering treats makeup after regular within the same exam cycle. DNN makeup is an instructor solution manual containing the question structure and full marking rubric even where a separate question-only file is absent.

## Deduplication method

- A QP bundled with its answer key is one sitting.
- A separate answer-key file for the same named sitting is not a second appearance.
- Copies under `Previous Question Papers/` and subject `Question papers/` were not counted twice.
- “Past Papers.docx” compilations were used for discovery/context, not as independent frequency units.
- Sample/model papers support practice but do not count as historical examination frequency.

## Cross-paper trends (de-duplicated qualitative frequency)

Exact counts are constrained by scanned/compiled documents, so ranges below represent verified identifiable sittings rather than every physical file.

| Subject | Strongest recurrence | Moderate recurrence | Recent decline / insufficient evidence |
|---|---|---|---|
| MFML | eigen/linear algebra; gradients/GD; SVM/kernels | PCA, KKT, SVD | long abstract proofs reduced; adaptive optimizers weak recent direct evidence |
| ISM | regression/correlation and forecasting in all identifiable 2023–26 papers; hypothesis tests in most | CI, chi-square/ANOVA, probability | MLE and advanced ARIMA-family derivations have insufficient recent evidence |
| DNN | FFNN, CNN, RNN/gates, optimization/regularization in both 2026 and 2024/25; attention strong | transformers sharply strengthened in 2026 | NAS/federated/meta/online and detailed time-series modeling weak recent evidence |
| ML | SVM spans old and both latest; NB/ensembles/KNN/GMM appear in both 2026 | ridge/lasso/tree/evaluation | generic workflow/history low recent direct marks |

## Style change over time

- Older papers often used compact 1–5 mark proofs or definitions.
- 2024/25 begins mixing short conceptual checks with calculations.
- 2026 papers use realistic scenarios, multi-part computations, parameter/model comparisons, and explicit justifications. The original DNN regular totals 120 marks over seven questions; ML uses eight algorithm blocks; ISM uses eight equal 5-mark blocks; MFML uses five equal 8-mark blocks.
- Therefore, recent papers receive dominant priority. Older papers are used to retain recurring mathematical patterns, not to equal-weight frequency.

## Watermark inspection

| File | Verified pages | Verified opening contents | Assessment |
|---|---:|---|---|
| `MFML/MFML watermark.pdf` | 136 | starts with systems of linear equations/vector-space foundations; consolidated slide deck | useful worked-method bank after indexing |
| `ISM/ISM watermark.pdf` | 261 | modules 1–6, evaluation, descriptive statistics onward | comprehensive but far too large for live browsing |
| `DNN/DNNWaterMarked.pdf` | 196 | 11-module structure through transformer/optimization/regularization | highly aligned with recent core |
| `ML/ML WaterMark.pdf` | 178 | M1–M11 course plan, workflow through model evaluation | aligned with official modules |

No root-level file literally named `watermark.pdf` exists. The four subject-specific bundles above were inspected.

**Permission clarification (user, 30 Aug 2026):** university-watermarked slides are allowed. The four subject-specific watermark PDFs are therefore treated as the authorized slide resources in the revised strategy.

## Schedule anomaly

ISM, ML and DNN handouts use a March–September 2026 teaching/evaluation calendar and schedule the comprehensive for 5–6 September 2026. MFML is labeled Second Semester 2025–26 but lists assignments/quizzes from August–November 2026 and the comprehensive on 6 December 2026. This may be a different delivery calendar or a handout inconsistency. Verify the MFML date/time on eLearn before planning travel or final revision.

## Extraction limitations

- Formula extraction from PDFs can lose superscripts, fraction layout and diagrams. Question identities and marks were cross-checked from surrounding text; use the original PDF for exact matrices/figures.
- Several older DNN PDFs are image scans with minimal extractable text. They support only lower-confidence historical observations unless accompanied by answer-key text.
- There is insufficient PYQ evidence to predict specific questions from official-only topics such as DNN meta-learning or ISM VARMAX.

## Generated analysis files

The `exam_analysis/extracted/` directory contains page-delimited text used for searching. `topic_frequency.txt` contains raw keyword document hits; these include answer-key companions and must not be interpreted as de-duplicated sitting counts without the method above.

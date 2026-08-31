# DNN End-Sem Study Guide

## How to use this guide

Study one topic, close the notes, write its formula/template from memory, then solve the linked PYQ. Use `DNNWaterMarked.pdf` only to verify or recover detail; page references below are PDF viewer pages. The compact page map is in `06_DNN_WATERMARK_INDEX.md`.

## Exam orientation

- Current handout: comprehensive exam on **all sessions**, 6 Sep 2026 (AN), 150 minutes, 40%, open book.
- Latest regular pattern: 7 compulsory-looking scenario questions totalling 120 marks; the original paper does not show choice.
- Latest balance: calculations and applied design dominate; almost every numerical asks for interpretation or justification.
- Mark depth: exact marking schemes are unavailable for most regular subparts. Depth guidance below is inferred from the allocated marks unless an instructor rubric was present.

| Marks | Write this much |
|---:|---|
| 1-2 | formula/definition, substitution or one precise reason |
| 3-4 | method + working + result + one interpretation |
| 5-6 | complete calculation/architecture + 2-3 justified design points |
| 7-10 | labelled stages, all intermediate values, assumptions, conclusion/trade-off |
| 15-20 | split by subpart; never answer the scenario as one essay |

## Priority map

| Topic | Priority | Recent evidence | Form | Difficulty | Time | Expected return |
|---|---|---|---|---|---:|---|
| CNN dimensions/parameters/GAP/RF | MUST | 2026 R Q3, 2026 M Q5, both Sep-2025 Q3 | numerical/design | medium | 2 h | exceptional |
| RNN/GRU/LSTM | MUST | every recent sitting | numerical/selection | medium-hard | 2.5 h | exceptional |
| Attention | MUST | every recent sitting | numerical/compare | medium | 2 h | exceptional |
| Transformer | MUST | both 2026 sittings | dimensions/params/design | hard | 2 h | very high |
| Optimizers + regularization | MUST | latest 20-mark blocks | curve diagnosis | medium | 1.5 h | exceptional |
| FFNN/backprop/activations | MUST | 30 marks latest regular | forward/design | easy-medium | 1.5 h | very high |
| Transfer learning/deployment | HIGH | 2026 R Q3, Sep-2025 | justify | easy | 0.75 h | high |
| BPTT/BiRNN/gradient flow | HIGH | repeated sequence subparts | explain/derive | medium | 0.75 h | high |
| NAS/time-series | SHOULD | Sep-2025 and syllabus | short design | easy | 0.5 h | moderate |
| Federated/meta/online | SKIM | weak recent evidence | short concept | easy | 0.4 h | low-moderate |

## 1. FFNN, activations and backpropagation - MUST

### From near-zero

A dense layer first computes `z = Wa + b`; an activation turns `z` into the next representation. Multiple linear layers without nonlinear activations collapse into one linear map, so they cannot learn nonlinear boundaries such as XOR. Backpropagation applies the chain rule from the loss to each earlier layer.

Understand:

- ReLU creates nonlinearity cheaply; Leaky ReLU retains a small negative-side gradient.
- Sigmoid is a one-probability output; softmax creates a mutually exclusive class distribution.
- Binary: sigmoid + BCE. Mutually exclusive multiclass: softmax + categorical CE. Multilabel: independent sigmoids + BCE.
- Vanishing gradients come from repeated small Jacobian factors/saturation. Exploding gradients come from repeated large factors.
- Remedies: ReLU-family, He/Xavier initialization, residual connections, normalization; clip exploding gradients.

Memorize: activation/loss formulas, dense parameter count, `delta_output = yhat-y` for sigmoid+BCE or softmax+CE, and the gradient-descent sign.

Look up: full computational graph/backprop algorithm on viewer pp. 53-58; diagnosis and initialization pp. 60-62.

Common traps: softmax for multilabel; ReLU probability output; zero initialization; adding rather than subtracting the gradient; calling a deeper activation-free network more expressive.

### Numerical template

`x -> z1=xW1+b1 -> a1=f(z1) -> z2=a1W2+b2 -> yhat=g(z2) -> loss`.
Write matrix/vector dimensions. Do not round until the final line.

### 1-minute revision

`ReLU=max(0,z)`; `LeakyReLU=max(az,z)`; `sigmoid=1/(1+e^-z)`; softmax normalizes exponentials; BCE/CE pair with sigmoid/softmax; dense params `nin*nout+nout`; backprop is chain rule; GD subtracts the gradient.

## 2. CNN and transfer learning - MUST

### From near-zero

A CNN applies the same small kernel across spatial locations. Local connectivity and weight sharing make it efficient for images. The output shape of one spatial dimension is

`floor((N + 2P - D*(K-1) - 1)/S) + 1`.

For ordinary dilation `D=1`, this is `floor((N+2P-K)/S)+1`. A conv layer has `(Kh*Kw*Cin + 1)*Cout` parameters when each filter has one bias. Pooling has no trainable parameters.

Track `H x W x C` after every conv/pool. Flatten multiplies all three; Global Average Pooling (GAP) maps `H x W x C -> C` and often removes a huge fully connected layer.

Receptive-field recursion: start `r=1,j=1`; for each layer, `r_new=r+(K-1)j`, `j_new=j*S`. Channels do not change receptive field.

Transfer learning: reuse a pretrained backbone, replace the head, train the head, then selectively fine-tune with a small learning rate. If RGB becomes 4-channel, only the first convolution directly changes; if output classes change, the classifier head changes.

Memorize: output-size, conv/dense parameter and receptive-field formulas.

Look up: core CNN pp. 85-107; formulas/examples pp. 89-104; transfer learning pp. 110-111.

Common traps: multiplying conv parameters by output pixels; forgetting bias; using input channels rather than output channels as depth; assuming extra channels enlarge receptive field; dividing dimensions without applying floor.

### Numerical template

1. Make columns: layer, `(H,W,C)`, parameters, receptive field.
2. Apply shape formula independently to `H` and `W`.
3. For conv params use previous layer's `Cin`.
4. For flatten calculate `H*W*C` exactly.
5. State why the redesign helps and what it loses.

### 1-minute revision

Conv output `floor((N+2P-K)/S)+1`; params `(K^2*Cin+1)Cout`; dense `nin*nout+nout`; pooling 0 params; GAP maps each feature map to one scalar; channel count is not receptive field.

## 3. RNN, GRU, LSTM and BPTT - MUST

### From near-zero

A vanilla RNN updates a fixed-size state: `h_t=tanh(Wxh*x_t + Whh*h_(t-1) + b)`. The same parameters are reused at every time step. BPTT unrolls time, sums shared-parameter gradients and multiplies recurrent Jacobians, which causes vanishing/exploding gradients.

GRU uses reset and update gates with one hidden state. LSTM uses input, forget and output gates plus a separate cell state. Gated additive paths let a gradient travel with multipliers near 1.

Parameter counts with one bias vector per gate:

- RNN: `h*d + h^2 + h`.
- GRU: `3(h*d + h^2 + h)`.
- LSTM: `4(h*d + h^2 + h)`.
- Add output layer separately: `h*o + o`.

State the GRU convention before calculating. This guide uses `h_t=z*h_prev+(1-z)*h_tilde` where large `z` preserves old state, matching 2026 Regular Q4(c). Some course slides use the opposite naming/weighting convention.

Choose GRU for constrained compute and moderate dependencies; LSTM for explicit long memory; BiRNN only when future context is available at inference; vanilla RNN for very small causal streaming tasks where compute/memory dominates.

Look up: RNN/BPTT pp. 116-126; GRU pp. 127-129; LSTM pp. 130-134; worked parameter questions pp. 134-136.

Common traps: including sequence length in parameter count; mixing gate conventions; applying sigmoid to the candidate; using BiRNN for causal forecasting; forgetting output-layer parameters.

### Numerical template

Write each affine value first, then sigmoid/tanh, then combine gates. For gradient-highway questions, isolate the stated path: `dL/dh_old = dL/dh_new * z` under the convention above.

### 1-minute revision

RNN shares weights over time. BPTT multiplies Jacobians. GRU has 3 affine blocks; LSTM has 4. Gates are sigmoid; candidates are tanh. State convention. Sequence length never multiplies trainable parameters.

## 4. Attention - MUST

### From near-zero

A query asks what is relevant, keys advertise what each item contains, and values carry the information to combine. Scaled dot-product attention is

`scores = QK^T/sqrt(dk)`, `A=softmax(scores)`, `output=AV`.

Subtract the row maximum before exponentiating. Apply padding/causal masks to scores before softmax. Additive attention uses learned projections and a learned scoring vector, often `e_i=v^T tanh(Wq q + Wk k_i + b)`; without these parameters a unique numerical answer is impossible.

Multi-head attention splits a fixed `d_model` into `h` heads of dimension `d_model/h`, learns different relationships and concatenates them. With fixed total width, increasing heads does not multiply the total Q/K/V/O projection parameter count.

Look up: attention intuition and encoder-decoder pp. 137-145; attention calculations/masking pp. 148-150; detailed transformer attention pp. 154-166.

Common traps: masking after softmax; omitting `sqrt(dk)` when requested; softmaxing over the wrong row; treating values as keys; multiplying parameters by number of heads twice.

### Numerical template

`dot -> scale -> mask -> max-shift -> exponentials -> row-normalize -> weighted value sum -> interpret largest weight`.

### 1-minute revision

Q matches K; weights combine V. Scale by `sqrt(dk)`. Mask before softmax. Each attention row sums to 1. `d_head=d_model/h`. Cross-attention takes Q from decoder and K,V from encoder/external source.

## 5. Transformers - MUST

### From near-zero

An encoder block is self-attention -> residual/norm -> position-wise FFN -> residual/norm. A decoder adds causal masking and, in an encoder-decoder model, cross-attention. Attention alone has no sequence order, so positional encoding is added.

For model width `d` and FFN width `dff`, projection weights in one self-attention block are `4d^2` (Q,K,V,O); FFN weights are `2*d*dff`. Biases and normalization parameters count only if requested.

- Encoder-only/BERT: bidirectional representations, MLM-style pretraining; classification/NER.
- Decoder-only/GPT: causal next-token objective; generation.
- Encoder-decoder/T5: denoising/span corruption; translation/summarization.

Attention time is roughly `O(L^2*d)` and the score matrix is `O(L^2)` per head. Sliding/local/sparse attention reduces cost but may miss global dependencies.

Pre-LN normalizes before the sublayer and usually improves gradient flow/stability in deep models. Post-LN follows the original transformer ordering and may obtain strong final performance but is harder to optimize deeply.

Look up: block/norm pp. 151-155; encoder/decoder calculations pp. 154-166; BERT/GPT/T5 pp. 167-168.

Common traps: claiming heads multiply a fixed-width projection count; omitting output projection; confusing encoder-decoder cross-attention with causal self-attention; saying positional encoding changes tensor width.

### 1-minute revision

Encoder = MHA + FFN with two residual/norm stages. Decoder = masked self-attn + optional cross-attn + FFN. Params without bias `4d^2+2ddff`; self-attention is quadratic in sequence length.

## 6. Optimizers and regularization - MUST

### From near-zero

SGD follows the current gradient. Momentum accumulates a velocity. RMSProp scales each coordinate using a moving average of squared gradients. Adam combines first and second moments and bias correction.

Curve recognition: slow smooth descent -> SGD; fast oscillatory -> momentum; adaptive fast/low oscillation but possible plateau -> RMSProp; fastest smooth/low loss -> Adam in the latest paper's stylized curves. This is paper-specific matching, not a universal performance law.

Regularization diagnosis:

- train good, validation poor/rising loss -> overfit/too little regularization;
- both poor with small gap -> underfit/too much regularization or insufficient capacity;
- small gap and strong scores -> appropriate;
- noisy/unstable -> learning rate, aggressive dropout or poor normalization/initialization.

Dropout prevents co-adaptation; L2/weight decay discourages large weights; early stopping keeps the best validation epoch; data augmentation expands effective data; BatchNorm stabilizes batch-feature statistics; LayerNorm normalizes features within each token/example.

Look up: optimizer section pp. 169-183, especially equations pp. 177-179; regularization pp. 184-196; initialization/L1/L2 p. 188; dropout p. 189; BatchNorm p. 190; LayerNorm p. 191.

Common traps: using a plus sign in descent; omitting Adam bias correction; saying BatchNorm and dropout do the same thing; diagnosing underfit from a train-validation gap; using a high constant LR after validation deteriorates.

### 1-minute revision

Momentum = direction memory; RMSProp = squared-gradient scaling; Adam = both. Overfit means train-val gap. L2 shrinks weights; dropout drops activations; early stop at validation minimum; BN stabilizes training.

## 7. Lower-return official topics

### NAS - SHOULD

NAS has search space, search strategy and evaluation strategy. One-shot NAS trains a supernet and inherits shared weights to evaluate many subnets quickly; the ranking can be biased. Memorize one advantage and one limitation.

### Time-series CNN/LSTM - SHOULD

Univariate vs multivariate describes the number of input series; single-step vs multi-step describes the output horizon. CNN extracts local temporal patterns; LSTM/GRU models sequential dependence; CNN-LSTM combines both. Never use bidirectional recurrence for a causal forecast that cannot see future inputs.

### Federated/meta/online - SKIM

Federated learning keeps data at clients and aggregates model updates; it helps privacy/data-locality but has non-IID, communication and security issues. Meta-learning learns to adapt quickly across tasks. Online learning updates incrementally as data arrives and must handle drift/forgetting.

## How to write BITS exam answers

- Numerical: **Given -> Required -> Formula -> Substitution -> intermediate values -> boxed result -> one-line interpretation**.
- Derivation: define notation, state start equation, transform one line at a time, state the result and conditions.
- Concept: definition -> mechanism -> why it matters -> limitation/application.
- Comparison: use a table with mechanism, parameters/compute, gradient behaviour and best-use case.
- Justify: make the choice first, then connect each reason to the scenario constraint.
- Algorithm: input -> initialization -> repeated steps -> update -> output; show tensor dimensions.
- Architecture: draw labelled blocks and write input/output shape beside each.
- Interpretation: translate the number into behaviour; e.g. `z=.9` retains 90% of the old-state direct path.

## Open-book exam strategy

Memorize core formulas and recognition logic. Understand why the method applies. Look up long diagrams, optimizer details and worked examples at indexed pages. Do not search for sigmoid, conv output, parameter counts or the core attention equation; those should be immediate.

During the paper, spend 5-7 minutes scanning and mark: memory-solvable, one-page lookup, and long calculation. Start with the highest-confidence high-mark question. Budget approximately 1.1-1.2 minutes per mark, reserving 10-12 minutes for review. If a convention is unclear, state it and proceed consistently.

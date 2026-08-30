# DNN End-Sem Study Guide

## Official syllabus map

Fundamentals/perceptron/MLP; feedforward networks and backprop; optimization; regularization; CNN and transfer learning; RNN/BPTT/LSTM/GRU; attention and transformers; NAS; CNN/LSTM time-series forecasting; federated, meta and online learning. Comprehensive covers all topics, 40%, 150 minutes.

## Priority map

| Topic | Priority | Recent evidence | Form | Difficulty | Exact preparation |
|---|---|---|---|---|---|
| CNN shape/parameters/architecture | 🔴 | both Mar-2026; both 2024/25 | numerical + design | medium | output formula, conv/FC params, pooling/GAP, receptive field, transfer learning |
| RNN/LSTM/GRU | 🔴 | both Mar-2026; 2024/25 | state/gate numerical + selection | medium-hard | equations, parameter counts, vanishing gradients, edge tradeoffs |
| Attention | 🔴 | both Mar-2026; 2024/25 | score-softmax-context | medium | scaled dot-product, additive, masking, multi-head dimensions |
| Transformers | 🔴 | both Mar-2026 | architecture/params/complexity | hard | encoder/decoder, positional encoding, QKV, FFN, BERT/GPT/T5, O(L²) |
| Activations/loss/FFNN/backprop | 🟠 | both Mar-2026 and 2024/25 | forward + short theory | easy-medium | ReLU/leaky/sigmoid/softmax, CE, XOR, chain-rule gradient flow |
| Optimizers | 🟠 | both Mar-2026 and 2024/25 | curve matching + compare | medium | SGD/momentum/RMSProp/Adam, LR schedules |
| Regularization/normalization | 🟠 | both Mar-2026 and 2024/25 | diagnose curves | easy-medium | L1/L2, dropout, BN, initialization, residuals |
| Transfer learning/receptive field | 🟡 | Mar-2026 regular | parameter/design | medium | freeze/fine-tune reasons, input channels, RF recursion |
| NAS/federated/meta/online/time-series architectures | 🟢 | official but weak latest evidence | short concepts | medium | definition, one use/benefit/limitation; no deep algorithm detail |

### Cross-paper frequency (4 fully extractable recent regular/makeup sittings: 2024/25 and 2026)

| Topic family | Paper presence | Mode | Typical marks in 2026 |
|---|---:|---|---:|
| FFNN/activations/backprop | 4/4 | forward + concept | 15–18 |
| CNN | 4/4 | shapes/parameters/design | 18–20 |
| RNN/LSTM/GRU | 4/4 | state numerical + selection | 20 |
| Attention | 4/4 | numerical + concept | 15–20 |
| Optimization | 4/4 | curve/update reasoning | 8–10 |
| Regularization | 4/4 | diagnosis/remedy | 10–20 |
| Transformers | 3/4; both 2026 | architecture/parameters | 15–20 |
| NAS/federated/meta/time-series | 1/4 | short concept | low/variable |

Older scan-only papers were inspected but excluded from these exact counts because reliable question-level text was unavailable.

## Recent paper signal

- **Latest original regular (1 Mar 2026, 120 marks, 7 questions):** Q1 FFNN fundamentals 15; Q2 binary DFNN design 15; Q3 CNN/transfer/parameters 20; Q4 RNN/GRU 15; Q5 attention 15; Q6 transformers 20; Q7 optimization and regularization 20. The earlier “8 questions” description came from the solution manual splitting the final question into separate rubric sections; the original QP confirms seven.
- **Mar-2026 makeup (120 marks):** feedforward calculation; activation/loss/gradient flow; RNN/LSTM numericals; optimizers; overfit/dropout; CNN parameters; transformer parameters and translation reasoning.
- **Both:** essentially the same stable core—FFNN, CNN, sequence models, optimization/regularization, transformer. Every major core family carries at least 15 marks in the latest original, an unusually strong signal against skipping any of them.
- **Older fading pattern:** 2024/25 papers used many 1–2 sentence questions. Latest papers expand the same concepts into applied, multi-part numericals. NAS/federated/meta appear in official syllabus but have insufficient recent PYQ evidence.

## Concepts from zero

### Feedforward network

Each layer computes `z=Wa+b`, then activation. Nonlinear activations let stacked layers model nonlinear boundaries; stacking linear layers without activations remains one linear transformation. Binary output normally uses sigmoid + binary cross-entropy; mutually exclusive multiclass uses softmax + categorical cross-entropy.

Backprop applies the chain rule from loss to earlier parameters. Repeated derivatives below 1 cause vanishing gradients; above 1 cause exploding gradients. ReLU-family activations, suitable initialization, normalization, residual paths and gating help.

### CNN

A convolution shares a small kernel across space, exploiting locality and reducing parameters. Padding controls border/size; stride and pooling downsample. Channel count changes features, not spatial receptive field by itself. Flatten can create enormous FC layers; GAP reduces each feature map to one number.

### Sequence models

Vanilla RNN repeatedly mixes current input and prior state, but long products of Jacobians harm gradient flow. LSTM has input/forget/output gates plus cell state; GRU combines gates and is cheaper. Choose GRU for limited memory/compute and moderate dependencies; LSTM for explicit long memory; transformer for parallel long-range context when quadratic attention cost is acceptable.

### Attention and transformer

Attention scores how relevant keys are to a query, normalizes scores, and averages values. Self-attention uses Q/K/V from the same sequence. Causal masks prevent looking into future tokens. Transformers add residual connections, normalization and position-wise FFNs; positional encoding supplies order.

## Formula block

- ReLU `max(0,z)`; leaky ReLU `max(az,z)`.
- Sigmoid `1/(1+e^-z)`; softmax `e^{z_i}/sum_j e^{z_j}`.
- BCE `-[y log p+(1-y)log(1-p)]`; CE `-sum y_i log p_i`.
- Conv output `floor((N+2P-K)/S)+1`.
- Conv params `(K_h K_w C_in)C_out+C_out`; dense `n_in n_out+n_out`.
- RNN `h_t=tanh(W_xh x_t+W_hh h_{t-1}+b_h)`.
- LSTM: `f,i,o=sigma(...)`, candidate `g=tanh(...)`, `c_t=f*c_{t-1}+i*g`, `h_t=o*tanh(c_t)`.
- GRU (one convention): `z,r=sigma(...)`, `h~=tanh(Wx+U(r*h_prev))`, `h=z*h_prev+(1-z)h~`.
- Attention `A=softmax(QK^T/sqrt(d_k))`, output `AV`.
- Batch norm `xhat=(x-mu_B)/sqrt(var_B+eps)`, `y=gamma xhat+beta`.

## Question patterns you must solve

### 1. CNN shape and parameter count

Wording: architecture chain, new input channel, identify dominant layer, replace flatten with GAP.

Method: track `(H,W,C)` after each layer; count biases; flatten only after final spatial shape. If input channel changes 3->4, only first conv parameters change; later layers unchanged if its output channels stay fixed.

Reference: **Mar-2026 regular Q3**, makeup Q5. Difficulty medium, 🔴.

Mini-example: `32x32x3`, conv `5x5`, 8 filters, stride 1, no padding -> `28x28x8`; params `5*5*3*8+8=608`.

### 2. RNN/GRU/LSTM one-step computation

Wording: given matrices, `x_t`, `h_{t-1}`, gates; compute state and explain memory.

Method: compute affine vectors first; apply sigmoid/tanh elementwise; combine with exact convention. Round only final values.

Reference: **Mar-2026 regular Q4**, makeup Q2–3. Difficulty medium-hard, 🔴.

Makeup worked value: `c_prev=80,f=.85,i=.25,candidate=40` -> `c=.85*80+.25*40=78`.

### 3. Model parameter comparison

RNN parameters `hd+h²+h`. GRU `3(hd+h²+h)`. LSTM `4(hd+h²+h)` under one-bias-per-gate convention. State convention if framework uses two bias vectors.

Reference: **Mar-2026 regular Q4(a)**. Difficulty easy, 🔴.

### 4. Scaled dot-product attention

1. `s_i=q^Tk_i/sqrt(d_k)`.
2. Stabilize softmax by subtracting max.
3. `alpha_i=e^{s_i}/sum e^{s_j}`.
4. `context=sum alpha_i v_i`.
5. Apply mask before softmax when causal.

Reference: **Mar-2026 regular Q5**. Difficulty medium, 🔴.

### 5. Transformer parameter count

For `d=512,d_ff=2048`, Q/K/V/output weights contribute `4d²`; FFN weights `2dd_ff`; add biases if requested. Multi-head splitting does not automatically multiply total projection parameters when total `d_model` remains fixed—a common trap.

Reference: **Mar-2026 regular Q6**, makeup Q6. Difficulty hard, 🔴.

### 6. Diagnose curves

Large training–validation gap -> overfit; both poor -> underfit; validation loss rising while train falls -> overfit. Suggest a mechanism matched to cause: dropout/L2/data augmentation/early stopping; BN primarily stabilizes/accelerates; optimizer-level intervention could be learning-rate reduction or early stopping when architecture changes are disallowed.

Reference: **Mar-2026 regular Q7–8**, makeup Q3–4. Difficulty easy-medium, 🟠.

### 7. Architecture/task matching

- Encoder-only/BERT: representation and token/classification tasks.
- Decoder-only/GPT: autoregressive generation.
- Encoder-decoder/T5: conditional sequence transformation such as summarization/translation.

Reference: **Mar-2026 regular Q6**. Difficulty medium, 🔴.

## Important diagrams to reproduce

1. MLP: input -> dense/ReLU -> dense/ReLU -> output/softmax.
2. CNN block: conv -> activation -> pool repeated -> GAP/dense.
3. LSTM cell showing `f,i,g,o`, cell highway and hidden output.
4. Transformer encoder: MHA -> Add&Norm -> FFN -> Add&Norm.
5. Encoder-decoder showing masked self-attention and cross-attention.

## Common mistakes

- Softmax in hidden layers or ReLU for probability output.
- Forgetting biases in parameter counts.
- Confusing number of heads with a parameter-count multiplier.
- Claiming added input channels increase receptive field.
- Applying causal mask after softmax.
- Mixing GRU update conventions silently.
- Saying BN and dropout do the same job.
- Ignoring `O(L²)` memory/time in transformer recommendations.

## Open-book strategy

Memorize all forward equations and shape/parameter formulas; understand architecture selection and gradient problems. Look up full architecture diagrams, optimizer epsilon/details, and long transformer parameter tables. Tab a CNN shape example, a gated-state example, an attention example and a transformer block.

The authorized `DNNWaterMarked.pdf` has 196 pages and covers the core modules well. It is valuable only with tabs; broad search is too slow.

## Final checklist

- [ ] CNN shapes, parameters and receptive field.
- [ ] RNN/GRU/LSTM equations + counts + one numerical each.
- [ ] Scaled/additive attention and masking.
- [ ] Transformer diagram, dimensions, parameters, complexity.
- [ ] Activation/loss pairings.
- [ ] Optimizer/regularizer curve diagnoses.
- [ ] BERT/GPT/T5 task matching.
- [ ] Both 2026 papers solved selectively under time.

# DNN Question-Pattern Playbook

Use this file for recognition. Representative references are verified actual questions; probability language is deliberately avoided.

## Pattern matrix

| ID | Pattern | Examiner tests | Recognition words | Method | Representative evidence | Priority |
|---|---|---|---|---|---|---|
| P01 | Neuron/DFNN forward pass | affine vs activation order | input, weights, bias, infer | `z=Wx+b`, activate layer by layer | 2026 R Q1; 2026 M Q1 | MUST |
| P02 | Output/loss selection | task formulation | binary, multiclass, multilabel | identify label relation, then activation/loss | 2026 R Q1-Q2; latest EC2 | MUST |
| P03 | Gradient-flow diagnosis | chain rule and architecture | near input, vanishing/exploding | cause -> impact -> two matched fixes | 2026 R Q1; 2026 M Q1-Q2 | MUST |
| P04 | Architecture under constraints | capacity vs data/compute | design, justify, edge/mobile | encode input -> blocks -> output/loss -> constraint reasons | 2026 R Q2-Q4; Sep-2025 | HIGH |
| P05 | CNN dimension chain | exact floor arithmetic | kernel, stride, padding, pooling | table every `H,W,C` | 2026 R Q3; both Sep-2025 Q3 | MUST |
| P06 | CNN parameter audit | weight sharing/channels | parameters, biases, channel added | `(KhKwCin+1)Cout`; dense separately | 2026 R Q3; 2026 M Q5 | MUST |
| P07 | GAP/1x1/receptive field | efficient redesign | 99% parameters, RF, edge | count old/new; give one gain/loss | 2026 R Q3 | MUST |
| P08 | Transfer learning | data efficiency | pretrained, small/imbalanced dataset | replace head -> freeze -> train -> fine-tune | 2026 R Q3; Sep-2025 R Q2 | HIGH |
| P09 | Recurrent parameter count | gate structure | `d,h`, excluding output | base affine block x 1/3/4 | 2026 R Q4; 2024/2023 | MUST |
| P10 | RNN/GRU/LSTM state | gate order/convention | one step, matrices, states | affine -> gate activations -> combine | 2026 R Q4; 2026 M Q2-Q3 | MUST |
| P11 | Gradient highway/BPTT | long dependency | `dL/dh`, gate fixed | multiply direct-path factors; interpret | 2026 R Q4 | MUST |
| P12 | Recurrent model selection | causal context vs resources | edge, streaming, long text, bidirectional | choose first, map constraints to properties | 2026 R Q4; 2026 M Q2 | HIGH |
| P13 | Dot-product attention | exact score/softmax/context | Q,K,V, scale | dot -> scale -> mask -> softmax -> AV | 2026 R Q5; Sep-2025 R Q5 | MUST |
| P14 | Additive/cross/multi-head | attention taxonomy | external source, multiple relations | state scoring parameters; pick attention type | 2026 R Q5 | MUST |
| P15 | Transformer dimensions/params | tensor discipline | `d_model,d_ff,h,L` | dimensions then `4d^2+2ddff` | 2026 R Q6; 2026 M Q6 | MUST |
| P16 | Transformer family choice | objective/architecture/task | BERT/GPT/T5 | encoder vs decoder vs seq2seq table | 2026 R Q6 | MUST |
| P17 | Long-context mitigation | complexity/trade-off | `O(L^2)`, 2048 tokens | quantify matrix; propose sparse/local method + loss | 2026 R Q6; 2026 M Q7 | HIGH |
| P18 | Optimizer curve matching | update intuition | smooth, oscillates, plateaus | map only from stated behaviour; justify | 2026 R Q7; 2026 M Q3 | MUST |
| P19 | Regularization-run diagnosis | bias/variance behaviour | train/validation curves | diagnose -> evidence -> mechanism-specific fix | 2026 R Q7; 2026 M Q4 | MUST |
| P20 | NAS/time-series/federated | breadth and task fit | supernet, forecast, hospital data | definition -> why suitable -> one limitation | Sep-2025 Q6; Sep-2024 Q4 | SHOULD/SKIM |

## Fast solving templates

### CNN dimensions and parameters

1. Copy architecture and annotate `Cin` at every conv.
2. Compute `Hout` and `Wout` with floor; set output depth to filter count.
3. Count conv parameters from kernel and channels, not feature-map area.
4. Pooling changes shape, not trainable parameters.
5. Multiply final `H*W*C` only at flatten.
6. For a redesign, calculate the new pathway and state one deployment trade-off.

### RNN/GRU/LSTM

1. Write the exact recurrence/convention from the paper.
2. Compute gate affine values before applying sigmoid/tanh.
3. Preserve vector signs and use elementwise multiplication.
4. Round only after the final state.
5. Parameter count is independent of time steps.

### Attention

1. Determine which query row is requested.
2. Compute raw dots and scale by `sqrt(dk)` when specified.
3. Apply mask before softmax; max-shift for stability.
4. Check weights sum to 1.
5. Multiply weights by **values**, not keys.
6. Interpret the largest weight.

### Transformer parameters

`Q,K,V,O = 4d^2`; `FFN = d*dff+dff*d`; add biases only if requested; add LayerNorm only if explicitly included. Head count partitions fixed `d`; it does not create `h` copies of full `dxd` projections.

### Curves and diagnosis

Quote the observation first: “training falls, validation rises.” Then name the condition. Then prescribe a mechanism tied to the cause. Do not dump a list of every technique.

## Conceptual answer templates

- **Explain X (4 marks):** definition -> mechanism/equation -> why useful -> limitation/application.
- **Compare A and B (4-6 marks):** mechanism, parameters/compute, gradient/context behaviour, best-use scenario.
- **Justify a choice (3-5 marks):** choice in first sentence -> constraint 1 -> constraint 2 -> rejected alternative/trade-off.
- **Architecture (5-8 marks):** labelled block diagram -> tensor shapes -> activations/loss -> training choice -> scenario justification.
- **Algorithm (5-8 marks):** inputs -> initialization -> repeated computation -> update -> output -> complexity.

## Reusable diagrams

1. `Input -> Dense/ReLU -> Dense/LeakyReLU -> Sigmoid/Softmax`.
2. `Input -> [Conv -> ReLU -> Pool]xN -> GAP -> FC`.
3. RNN unrolled across three time steps with shared `Wxh,Whh`.
4. LSTM cell showing `f,i,g,o`, cell highway and hidden output.
5. `QK^T/sqrt(dk) -> mask -> softmax -> V`.
6. Encoder: `MHA -> Add&Norm -> FFN -> Add&Norm`.
7. Decoder: masked MHA -> cross-attention -> FFN, each with residual/norm.

## Common examiner traps

- “More layers” without activation does not add nonlinear expressiveness.
- A four-channel input changes only the first conv if its output channels stay fixed.
- Sequence length changes computation, not recurrent parameter count.
- GRU update conventions differ; equation earns protection against ambiguity.
- Additive attention needs learned scoring parameters; vectors alone may be insufficient.
- More heads with fixed `d_model` do not multiply total projection weights.
- BatchNorm stabilizes optimization; dropout directly randomizes activations for regularization.
- High overall accuracy can hide minority-class failure.
- Bidirectional recurrence leaks future information in causal forecasting.

## Evidence-aware practice labels

- **[ACTUAL PYQ]** requires a verified paper/session/question/marks reference.
- **[PYQ VARIATION]** keeps an evidenced pattern but changes numbers or context.
- **[ORIGINAL PRACTICE]** has no paper claim.

Do not promote an item from the repository's older unlabeled question bank to actual-PYQ status merely because its heading says “Latest Q”.

# DNN Final Revision and Exam-Hall Plan

## 90-minute emergency revision

| Minutes | Task | Output |
|---:|---|---|
| 0-15 | CNN formulas + one complete shape chain | no-note layer table |
| 15-30 | RNN/GRU/LSTM equations + counts | write all recurrences and 1/3/4 counts |
| 30-43 | attention calculation | dot -> scale -> mask -> softmax -> value sum |
| 43-55 | transformer block and params | diagram + `4d^2+2ddff` |
| 55-67 | optimizer/regularization curves | match 4 optimizer and 4 train/val cases |
| 67-77 | FFNN activations/loss/backprop | pairing table + forward chain |
| 77-90 | watermark tabs + traps | open every fast-index page once |

## One-page recall

### FFNN

`z=Wa+b`; nonlinear activation is essential. Binary = sigmoid+BCE. Exclusive multiclass = softmax+CCE. Multilabel = independent sigmoids+BCE. Dense params `nin*nout+nout`. Vanishing = products below 1; explosion = above 1. Remedies must match the problem.

### CNN

Output `floor((N+2P-K)/S)+1`. Params `(K^2 Cin+1)Cout`. Pooling 0 params. GAP converts `HxWxC` to `C`. Added input channel changes first conv only. RF depends on kernel/stride/dilation, not channels.

### Sequence

RNN `h=tanh(Wx+Uhprev+b)`. Base count `hd+h^2+h`; GRU x3; LSTM x4. Sequence length does not enter parameter count. State GRU convention. BiRNN cannot be used for causal future prediction.

### Attention

`softmax(QK^T/sqrt(dk))V`. Mask scores first. Max-shift softmax. `d_head=d_model/h`. Multi-head with fixed total width does not multiply projection parameters. External source = cross-attention.

### Transformer

Encoder: MHA, residual/norm, FFN, residual/norm. Decoder adds causal mask and cross-attention. One self-attn+FFN block weights `4d^2+2ddff`. Encoder-only=BERT/understanding; decoder-only=GPT/generation; encoder-decoder=T5/translation/summarization. Full attention is quadratic in `L`.

### Training

SGD current gradient; momentum direction memory; RMSProp squared-gradient scaling; Adam both plus bias correction. Train down/val up = overfit. Both high = underfit. Dropout randomizes activations; L2 shrinks weights; early stop at best validation; BN stabilizes batches; LN normalizes features/token.

## Highest-risk mistakes

1. Forgetting bias in parameter counts.
2. Counting spatial positions as separate conv weights.
3. Multiplying recurrent parameters by time steps.
4. Mixing GRU update conventions.
5. Applying a causal mask after softmax.
6. Multiplying transformer projections by head count twice.
7. Rounding recurrent/softmax intermediate values too early.
8. Recommending BiRNN for causal forecasting.
9. Calling BatchNorm identical to dropout.
10. Giving a result without interpretation in a 3+ mark numerical.

## Final 24-hour plan

### T-24 to T-18 hours

Redo without notes: 2025-26 EC3 Regular Q3, Q4 and Q5. Check every number against `02_DNN_PYQ_SOLUTIONS.md`. Patch only recurring errors.

### T-18 to T-12 hours

Study transformer Q6 and optimizer/regularization Q7. Draw encoder, decoder and LSTM diagrams once. Open viewer pp. 152-168 and 177-191; set physical/digital tabs.

### T-12 to T-8 hours

Redo 2026 Makeup Q1, Q2B and Q3A. Then one Sep-2025 CNN chain. Stop learning large new topics.

### T-8 to T-2 hours

Sleep/rest. On waking, read this file and the formula sheet. Skim NAS/time-series/federated definitions for insurance, no deep derivations.

### Final 2 hours

- Write from memory: conv output/params, recurrent counts, attention, transformer count, Adam.
- Visit each fast watermark page; confirm page navigation.
- Pack permitted material and verify the current centre rules.
- Do not start a new architecture family.

## Questions to redo without notes

1. 2025-26 EC3 R Q3(b): channel change and GAP.
2. 2025-26 EC3 R Q4(b-c): RNN/GRU state and gradient.
3. 2025-26 EC3 R Q5(a,c): scaled/multi-head attention.
4. 2025-26 EC3 R Q6(b): dimensions and parameters.
5. 2025-26 EC3 R Q7: curve diagnosis.
6. 2025-26 EC3 M Q2B and Q3A: LSTM/RNN calculations.

## Exam-hall strategy

### Before writing

Spend 5-7 minutes scanning. Label each question `M` (memory), `L` (one indexed lookup) or `C` (long calculation). Start with the highest-confidence high-mark `M/C` question. Check whether all questions are compulsory.

### Time

For 150 minutes and a 120-mark pattern, use about 1.1 minutes/mark and reserve 10-12 minutes. A 20-mark question gets roughly 22 minutes; a 15-mark question 16-17 minutes. Stop when its budget expires and return later.

### Numericals

Write Given, Required, Formula, Substitution, intermediate values, final result and interpretation. If the prompt is ambiguous, state the convention in one line and continue. Method marks require visible work.

### Concepts/design

Answer the choice first. Use scenario nouns in every reason: “8 GB memory”, “causal stream”, “600 melanoma examples”. A generic list is weaker than three constraint-linked reasons.

### Open-book use

Solve core equations from memory. Look up only full diagrams, exact optimizer details or a worked analogue. Use the viewer-page index; do not browse 196 pages linearly. If lookup exceeds 60-90 seconds, state a reasonable convention and proceed.

### Final check

Check dimensions, softmax weight sum, sign of gradient update, bias inclusion, GRU convention, units/percentage denominator, and whether every “justify” has an explicit reason.

## Five-minute confidence check

- [ ] I can calculate a full CNN chain.
- [ ] I can write RNN/GRU/LSTM counts without notes.
- [ ] I can perform one attention row.
- [ ] I can count a transformer block under stated bias convention.
- [ ] I can diagnose four train/validation patterns.
- [ ] I know exactly where those methods are in the watermark PDF.

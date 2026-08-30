# DNN End-Sem Question Bank

**Course:** Deep Neural Networks  
**Scope:** Comprehensive/end-semester examination  
**Format:** 20 core solved questions + 5 latest-paper gap-closing questions  
**Evidence:** Official course handout, audited repository material, and verified recent-paper structures

---

## How to use this bank

- Attempt every question before reading its solution.
- Prioritize items labelled MUST DO and latest-paper pattern.
- The numerical values in original drills are practice values; a PYQ-pattern label refers to verified structure, not a claim of verbatim reproduction.
- After each error, bookmark the matching worked example in the authorized watermarked slides.

---

## DNN — 20 solved questions

### DNN 1 — Forward pass [MUST DO | Latest Q1/Q2]

**Question.** Inputs `(1,2)`, hidden neuron `z=2x1-x2+1`, ReLU, output sigmoid with weight 1 and bias 0. Find output.

**Solution.** Hidden preactivation `2(1)-2+1=1`; ReLU gives 1. Output `sigma(1)=1/(1+e^-1)=.7311`. Show preactivation and activation separately; this earns method marks and prevents applying activation twice.

### DNN 2 — Output/loss pairing [MUST DO | Recent stable]

**Question.** Choose outputs and losses for binary, mutually exclusive 5-class, and multilabel classification.

**Solution.** Binary: one sigmoid + BCE. Five mutually exclusive classes: five-way softmax + categorical cross-entropy. Multilabel: five independent sigmoids + summed/mean BCE. Softmax forces probabilities to compete and sum to one, so it is wrong for independent labels.

### DNN 3 — Backprop scalar [MUST DO | Latest papers]

**Question.** `yhat=sigmoid(wx)`, BCE loss, `x=2,y=1,w=0`. Find `dL/dw`.

**Solution.** For sigmoid+BCE, `dL/dz=yhat-y`. At `z=0`, `yhat=.5`, so `dL/dw=(.5-1)x=-1`. A GD step increases `w`, raising the positive-class probability. The simplified derivative avoids separately multiplying unstable BCE and sigmoid derivatives.

### DNN 4 — Vanishing/exploding gradients [MUST DO | Latest Q1]

**Question.** Explain causes and remedies.

**Solution.** Backprop multiplies many Jacobians; repeated singular values below 1 shrink gradients, above 1 enlarge them. Remedies: ReLU-family activations, Xavier/He initialization, batch/layer normalization, residual connections, gated LSTM/GRU states, gradient clipping for explosion, and appropriate learning rates. Sigmoid saturation particularly promotes vanishing gradients.

### DNN 5 — Dense parameter count [MUST DO]

**Question.** Count parameters in `20 -> 10 -> 3` dense network with biases.

**Solution.** First layer `20*10+10=210`; second `10*3+3=33`; total 243. Activations add no trainable parameters unless parameterized.

### DNN 6 — CNN shape and parameters [MUST DO | Latest Q3]

**Question.** Input `32x32x3`, conv `5x5`, 8 filters, stride 1, no padding. Find output and parameters.

**Solution.** Spatial output `floor((32-5)/1)+1=28`, so `28x28x8`. Parameters `(5*5*3)*8+8=608`. Parameter count does not multiply by spatial positions because weights are shared.

### DNN 7 — Pooling and receptive field [MUST DO | Latest]

**Question.** Two `3x3`, stride-1 convolutions with same padding are followed by `2x2`, stride-2 pooling. What is final receptive field?

**Solution.** Track receptive field `r` and jump `j`: initially `(1,1)`. Conv1: `r=1+2*1=3,j=1`; conv2: `r=3+2=5`; pool: `r=5+(2-1)*1=6,j=2`. A final unit sees `6x6` input area. Channels do not change receptive field.

### DNN 8 — GAP versus flatten [MUST DO | Latest Q3]

**Question.** Why can GAP reduce overfitting?

**Solution.** Flattening `H*W*C` into a dense layer can create millions of location-specific weights. Global average pooling converts each feature map to one scalar, yielding only `C` features and enforcing stronger spatial invariance. It reduces parameters and overfitting but may lose precise localization information.

### DNN 9 — Transfer learning [HIGH | Latest regular]

**Question.** How do you adapt an ImageNet CNN to 4-channel medical images and 3 output classes?

**Solution.** Replace/initialize the first convolution for 4 channels (e.g., copy RGB weights and initialize the extra channel), replace the classifier with 3 outputs, freeze backbone initially, train head, then fine-tune later blocks with small LR. Only the first layer is directly affected by input-channel count; output head follows class count.

### DNN 10 — Vanilla RNN step [MUST DO | Recent]

**Question.** Scalar RNN: `h_t=tanh(x_t+.5h_{t-1})`, `x_t=1,h_prev=0`. Find `h_t`.

**Solution.** Preactivation is 1; `h_t=tanh(1)=.7616`. For long sequences the recurrent derivative is repeatedly multiplied, causing vanishing/exploding gradients.

### DNN 11 — LSTM update [MUST DO | Makeup pattern]

**Question.** `c_prev=80,f=.85,i=.25,g=40,o=.5`. Find cell and hidden state.

**Solution.** `c=.85(80)+.25(40)=78`. Hidden `h=.5*tanh(78)≈.5`. The cell can preserve a large linear memory even though exposed hidden output is bounded by tanh and output gate.

### DNN 12 — GRU update [MUST DO | Latest Q4]

**Question.** Under `h=z h_prev+(1-z)h_tilde`, take `z=.7,h_prev=.4,h_tilde=.9`.

**Solution.** `h=.7(.4)+.3(.9)=.55`. Here larger update gate retains more old state under this convention. Some sources reverse the weighting; quote the equation used before substituting.

### DNN 13 — RNN/GRU/LSTM counts [MUST DO | Latest]

**Question.** With input size `d=5`, hidden size `h=4`, count one-bias parameters.

**Solution.** One recurrent affine block has `hd+h²+h=20+16+4=40`. Vanilla RNN: 40; GRU: `3*40=120`; LSTM: `4*40=160`. Output-layer parameters are additional. Frameworks may store two biases per gate; state convention.

### DNN 14 — Scaled dot-product attention [MUST DO | Latest Q5]

**Question.** `q=(1,0)`, keys `k1=(1,0),k2=(0,1)`, values `v1=(2,0),v2=(0,4)`. Compute attention.

**Solution.** Scaled scores are `(1/sqrt2,0)=(.7071,0)`. Softmax weights are approximately `(.6698,.3302)`. Context `=.6698(2,0)+.3302(0,4)=(1.3396,1.3208)`. Scaling prevents dot products from pushing softmax into saturation as dimension grows.

### DNN 15 — Masking [MUST DO]

**Question.** How is causal masking applied?

**Solution.** Before softmax, replace forbidden future-position scores with `-infinity`; their softmax weights become zero. Applying a mask after softmax breaks normalization. Padding masks hide padded tokens; causal masks prevent future leakage.

### DNN 16 — Multi-head attention [MUST DO | Transformer signal]

**Question.** Why multiple heads, and does head count multiply projection parameters?

**Solution.** Heads learn different relationships/subspaces. With fixed `d_model`, Q/K/V projections still total approximately `3d²` and output projection `d²`; splitting into heads does not multiply these totals. It changes reshape/computation organization. Extra parameters occur only if total projected width increases.

### DNN 17 — Transformer block count [MUST DO | Latest Q6]

**Question.** Ignoring biases, count encoder-block weights for `d=512,dff=2048`.

**Solution.** Attention projections: Q,K,V,O = `4d²=1,048,576`. FFN: `d*dff+dff*d=2,097,152`. Total `3,145,728`, plus small LayerNorm parameters and biases if requested. Complexity of full self-attention is `O(L²d)` time and `O(L²)` attention storage.

### DNN 18 — Positional encoding and architecture choice [MUST DO]

**Question.** Why positional information? Match BERT, GPT, encoder–decoder.

**Solution.** Self-attention alone is permutation-equivariant and has no inherent word order; positional vectors encode location. Encoder-only/BERT suits representations and classification; decoder-only/GPT suits autoregressive generation; encoder–decoder suits conditional transformations such as translation and summarization.

### DNN 19 — Optimizer comparison [MUST DO | Latest Q7]

**Question.** Contrast SGD, momentum, RMSProp and Adam.

**Solution.** SGD uses current gradient; momentum smooths directions with velocity; RMSProp scales each coordinate by a moving average of squared gradients; Adam combines momentum and RMS scaling with bias correction. Adam often learns quickly, while tuned SGD may generalize well. Know formulas from the authorized slides; in prose tie optimizer choice to noisy gradients, curvature and memory cost.

### DNN 20 — Diagnose training curves [MUST DO | Latest Q7]

**Question.** Training loss falls, validation loss falls then rises. Diagnose and prescribe.

**Solution.** This is overfitting after the validation minimum. Use early stopping at that epoch, data augmentation, L2/weight decay, dropout, smaller model, or more data. If both losses remain high, diagnose underfitting instead. Batch normalization primarily stabilizes optimization and is not identical to dropout.

---

# Latest-paper gap closure

## DNN — five gap-closing questions

### 11. Additive/Bahdanau attention numerical

**Latest-paper link:** DNN latest regular Q5(b).

**Question.** Use scalar additive scores `e_i=tanh(q+k_i)` with `q=1`, `k1=0`, `k2=1`, values `v1=2,v2=5`. Find context.

**Solution.** `e1=tanh(1)=.7616`; `e2=tanh(2)=.9640`. Stable softmax weights are proportional to `exp(0)` and `exp(.2024)`, giving approximately `.4496,.5504`. Context `=.4496(2)+.5504(5)=3.6512`. General Bahdanau form is `v_a^T tanh(W_q q+W_k k_i+b)`. Unlike dot product, it introduces learned nonlinear scoring parameters.

### 12. GRU gradient highway

**Latest-paper link:** DNN latest regular Q4(c).

**Question.** For `h_t=z_t h_{t-1}+(1-z_t)h_tilde`, ignore candidate-path derivatives. If `dL/dh3=1` and `z2=z3=.9`, find `dL/dh1`.

**Solution.** `dh3/dh2≈z3=.9` and `dh2/dh1≈z2=.9`. Chain rule gives `dL/dh1=1(.9)(.9)=.81`. A high update gate preserves an almost-linear gradient path, mitigating vanishing. Over extremely long sequences `.9^T` still decays, and GRUs may struggle with very distant dependencies.

### 13. Pre-LN versus Post-LN

**Latest-paper link:** DNN latest regular Q6(b)(iii).

**Question.** Compare Pre-LN and Post-LN transformer blocks.

**Solution.** Post-LN commonly computes `y=LN(x+Sublayer(x))`; normalization follows the residual addition. Pre-LN computes `y=x+Sublayer(LN(x))`; the residual stream provides a cleaner identity gradient path, usually making deep training more stable and reducing warm-up sensitivity. Post-LN can sometimes yield strong final representations but is harder to optimize at depth. State the exact ordering with a diagram; do not merely say “one is before.”

### 14. Learning-rate schedule identification

**Latest-paper link:** DNN latest regular Q7(b).

**Question.** Match: X rises sharply then oscillates/drops; Y rises steadily then plateaus early; Z rises, briefly dips, then recovers to best result. Choices: constant high LR, constant low LR, cosine annealing with warm restarts.

**Solution.** X is constant high LR: steps overshoot and oscillate. Y is constant low LR: stable but slow and may plateau within the epoch budget. Z is cosine annealing with warm restarts: periodic LR increases can cause a temporary dip, then exploration and decay reach a better basin. Match the observed mechanism, not just speed.

### 15. Full scenario architecture design

**Latest-paper link:** DNN latest regular Q2.

**Question.** Design a DFNN for four numeric behavioral variables plus one categorical contract feature with three categories, for binary churn.

**Solution.** One-hot contract produces 3 inputs, so total input width is 7 after scaling numeric features. A defensible compact design is `7 -> Dense(32,ReLU) -> Dense(16,LeakyReLU) -> Dense(1,Sigmoid)`, trained with BCE. ReLU is efficient; Leaky ReLU maintains gradient for negative activations; sigmoid models churn probability. Use class weights or resampling if churn recall is poor, and select threshold using business costs. Neuron counts are design choices—marks come from dimensional consistency and justified choices.

---

## Mastery test

A pattern is mastered only when you can identify the method within 20 seconds, write the governing formula without searching, complete the calculation accurately, state assumptions, interpret the result, and locate a backup example in the watermarked slides within 30 seconds.
# DNN High-Value PYQ Solution Bank

## Labels and answer depth

Every item below is `[ACTUAL PYQ]`. No altered-number drill is presented as a BITS question. “Depth” is **inferred from marks** unless the source is the 2026 makeup instructor manual, which includes a rubric. Questions are paraphrased only to remove scenario prose; numerical data and task are preserved.

## S01 - DFNN inference, activations and gradient failure

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q1 | 15 marks | Priority: MUST  
**Pattern:** forward inference + definitions + perceptron limitation + vanishing gradient. **Depth:** inferred.

**Question.** For `x=[0.8,-0.5,0.2]`, `w=[0.4,0.1,-0.2]`, `b=0.5`, infer a ReLU neuron; define ReLU/Leaky ReLU/softmax; explain softmax for 10 classes, why a perceptron is inadequate, and the cause/impact/two fixes for vanishing gradients.

**Solution.**

Given `z=w^T x+b`:

`z=0.4(0.8)+0.1(-0.5)+(-0.2)(0.2)+0.5=0.32-0.05-0.04+0.5=0.73`.

Therefore `ReLU(z)=max(0,0.73)=0.73`.

`ReLU(z)=max(0,z)`; `LeakyReLU(z)=z` for `z>=0`, `az` otherwise (`0<a<1`); `softmax(z_i)=e^(z_i)/sum_j e^(z_j)`. Softmax is appropriate because ten mutually exclusive outputs become positive probabilities summing to 1.

A single perceptron creates only one linear decision boundary. Ten nonlinear class regions generally require multiple boundaries and nonlinear features; XOR is the canonical non-linearly-separable example that one perceptron cannot solve. For multiclass linear classification, several output units can create linear class scores, but the stated single-perceptron model is fundamentally insufficient for the nonlinear image task.

Vanishing gradients arise when backprop repeatedly multiplies small derivatives/Jacobians, especially saturated sigmoid/tanh derivatives. Early layers learn extremely slowly. Two architectural fixes: ReLU-family activations provide an unsaturated positive-side derivative; residual/skip connections provide short gradient paths. Normalization and He/Xavier initialization are also valid when justified.

**Exam writing:** show the four arithmetic terms; for the 4-mark explanations use cause -> effect -> justified fix.  
**Common mistake:** saying “perceptron cannot have 10 outputs” instead of addressing linear separability.  
**Watermark:** viewer pp. 15-18, 50-58, 61-62.

## S02 - Binary churn DFNN design

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q2 | 15 marks | Priority: MUST  
**Pattern:** output/loss pairing + threshold + architecture design. **Depth:** inferred.

**Question.** For a churn problem with three numeric variables and contract type, justify sigmoid with BCE, classify `p=0.73` at threshold `.5`, contrast a DFNN with logistic regression, compare ReLU/Leaky ReLU, and propose a small architecture while accounting for class imbalance.

**Solution.** Binary output uses `p=sigma(z)=1/(1+e^-z)` and `BCE=-[y ln p+(1-y)ln(1-p)]`. Their combination models a Bernoulli probability and yields a well-behaved output error `p-y`. At `p=0.73` and threshold `0.5`, predict churn (`1`); the threshold is the decision probability above which intervention is triggered.

A DFNN can learn nonlinear feature interactions (for example complaints matter differently by contract type) and hierarchical combinations that logistic regression's single linear boundary cannot.

ReLU is cheap and non-saturating for positive values. Leaky ReLU preserves gradient for negative pre-activations, reducing dying units.

One defensible architecture: one-hot encode contract type. If it has `K` categories, input dimension is `3+K` (or 4 only if contract is already one scalar); `Dense(16,ReLU) -> Dense(8,LeakyReLU) -> Dense(1,sigmoid)`, BCE, Adam/mini-batch training. Widths are design choices: they add nonlinear capacity while remaining modest for four behavioural variables. Standardize numeric inputs, validate width/dropout, and use class weighting or threshold tuning because recall is weak.

**Exam writing:** state the encoding assumption before the input dimension.  
**Common mistake:** softmax with two outputs when one sigmoid is requested, or claiming architecture alone fixes class imbalance.  
**Watermark:** viewer pp. 29-32, 50-60.

## S03 - Transfer-learning classifier parameter change

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q3(a) | 7 marks | Priority: MUST  
**Pattern:** transfer-learning choice + classifier parameter arithmetic. **Depth:** inferred.

**Question.** For a seven-class, imbalanced medical-image problem with 8,000 images, 8 GB memory and real-time inference, choose transfer learning or training from scratch; replace the ResNet-50 head `2048->1000` by `2048->512->7` and find the net parameter change.

**Solution.** Use transfer learning: only 8,000 images are available; pretrained ResNet features reduce data/compute need; the 8 GB/real-time constraint makes training from scratch risky; imbalance (600 melanoma) makes data-efficient features valuable. Replace and train the head, then fine-tune later blocks at a small learning rate with class-aware sampling/loss.

Assuming standard ImageNet ResNet-50 `2048 -> 1000`, parameters removed:

`2048*1000+1000=2,049,000`.

New `2048 -> 512 -> 7` head:

- first FC: `2048*512+512=1,049,088`;
- final FC: `512*7+7=3,591`;
- total added: `1,052,679`.

Net change: `1,052,679-2,049,000=-996,321`, a reduction of 996,321 parameters. Dropout has no trainable parameters.

**Exam writing:** separate parameters removed, parameters added and net change into three labelled lines, and include biases in every dense-layer count.  
**Common mistake:** forgetting the original 1,000 biases or counting dropout.  
**Watermark:** viewer pp. 102-104, 110-111.

## S04 - CNN input-channel change and GAP redesign

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q3(b) | 9 marks | Priority: MUST  
**Pattern:** conv/FC parameters + changed channel count + compression choice. **Depth:** inferred.

**Question.** Calculate the given first-convolution and large fully connected parameter counts, determine the effect of changing RGB input to RGB plus infrared, and assess a GAP-based redesign including one advantage and limitation.

**Solution.** Layer 1 `Conv(32,5x5,Cin=3)` has `(25*3+1)*32=2,432` parameters. Layer 8 `FC(100352 -> 256)` has `100352*256+256=25,690,368`.

With four input channels, Layer 1 becomes `(25*4+1)*32=3,232`. Increase is `800/2432*100=32.89%`. Layer 3 does not change because Layer 1 still outputs 32 channels; Layer 8 does not change because later spatial/channel dimensions are unchanged.

Choose Option A, GAP: `28x28x128 -> 128`, then `FC(128 -> 10)`. GAP has zero parameters and the FC has `128*10+10=1,290`, replacing the enormous dense pathway. Advantage: drastic memory/latency/overfitting reduction. Disadvantage: averaging can discard precise spatial localization.

**Exam writing:** show the old and new parameter formulas, compute percentage increase using the original biased count, then state one deployment advantage and one limitation.  
**Common mistake:** reporting a 33.33% increase by comparing input channels rather than actual biased parameter totals.  
**Watermark:** viewer pp. 93-104.

## S05 - CNN crop degradation and receptive field claim

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q3(c) | 4 marks | Priority: HIGH  
**Pattern:** architecture interpretation. **Depth:** inferred.

**Question.** Explain why accuracy can degrade when the CNN uses `128x128` crops, and evaluate the claim that adding an infrared channel increases the spatial receptive field of a later unit.

**Solution.** Accuracy can fall on 128x128 crops because the effective receptive field covers a different fraction of the image and may lose global lesion context; repeated stride/pooling can also shrink the already small crop so aggressively that discriminative detail is lost. A ResNet pretrained/trained on another input scale also sees shifted feature statistics.

The infrared-channel claim is false. Receptive field follows kernel/stride/dilation recursion, not channel count. Extra channels add information and first-layer weights, but do not enlarge the spatial area seen by a Layer-5 unit.

**Exam writing:** answer the claim as correct/incorrect first, then give two crop-related mechanisms and one receptive-field rule.  
**Common mistake:** confusing more input information or more channels with a larger spatial receptive field.  
**Watermark:** viewer pp. 88-99.

## S06 - RNN/GRU parameter count and edge choice

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q4(a) | 5 marks | Priority: MUST  
**Question.** For input size `d=10` and hidden size `h=20`, count vanilla-RNN and GRU recurrent parameters, excluding the output layer, and select a recurrent unit for anomaly detection on a constrained edge device.

**Solution.** For `d=10,h=20`, one recurrent affine block has `hd+h^2+h=200+400+20=620` parameters. Vanilla RNN: 620. GRU: `3*620=1,860`. Output layer is excluded as requested.

Choose GRU: gating retains recent pattern information better than vanilla RNN, while using fewer parameters/memory and less compute than LSTM. That matches recent-change anomalies and edge limits.

**Exam writing:** compute the shared base block once, multiply it by one or three, and connect the GRU choice explicitly to memory, compute and recent-pattern constraints.  
**Common mistake:** multiplying by sequence length.  
**Watermark:** viewer pp. 117, 127-134.

## S07 - Vanilla RNN and GRU one-step calculation

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q4(b) | 7 marks | Priority: MUST  
**Question.** Using the supplied `x`, previous hidden state and matrices, compute one vanilla-RNN state and one GRU state, then compare how much the first coordinate changes.

**Solution.**

Given `x=[2,1]^T`, `hprev=[0.5,-0.5]^T`, `Whh=0.6I`, `Whx=0.4I`:

`a=Whx*x+Whh*hprev=[0.8,0.4]+[0.3,-0.3]=[1.1,0.1]`.

`h_RNN=tanh(a)=[0.8005,0.0997]`.

For GRU, the paper supplies `Wz=I,Uz=0,Wh=0.5I,Uh=0` and the convention in Q4(c): `h=z*hprev+(1-z)*htilde`.

`z=sigma(x)=[sigma(2),sigma(1)]=[0.88,0.73]`.

`htilde=tanh(0.5x)=[tanh(1),tanh(0.5)]=[0.76,0.46]`.

`h=[0.88(0.5)+0.12(0.76), 0.73(-0.5)+0.27(0.46)] = [0.5312,-0.2408]`.

The first GRU coordinate changes by only `0.0312` from its old value, versus the RNN's `0.3005`; numerically, the update is more conservative.

**Exam writing:** state the GRU mixing equation before substitution and keep the RNN and GRU calculations in separate labelled blocks.  
**Common mistake:** silently switching to `h=(1-z)hprev+z htilde`.  
**Watermark:** viewer pp. 116-118, 127-129.

## S08 - GRU gradient highway and RNN vs transformer

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q4(c) | 3 marks | Priority: MUST  
**Question.** With update gates `z2=z3=.9` and unit upstream gradient, compute the direct GRU gradient from `h3` to `h1`; explain the gradient highway and give a case where an RNN is preferable to a transformer.

**Solution.** Ignoring candidate-path derivatives as stated, `dh_t/dh_(t-1)=z_t`. Hence `dL/dh1=1*z3*z2=0.9*0.9=0.81`. Gates near 1 preserve a direct gradient path. A GRU can still struggle with extremely long/noisy dependencies or insufficient hidden capacity.

Prefer an RNN to a transformer when data arrive online, only a bounded state may be stored, latency/power are tight, and the useful context is recent. Recurrent per-step work avoids storing an `LxL` attention matrix; full self-attention scales quadratically with sequence length.

**Exam writing:** show the two direct-path derivative factors explicitly, interpret `0.81`, then justify the architecture choice using causality, memory and complexity.  
**Common mistake:** adding candidate-path derivatives even though the question says to ignore them, or asserting that a transformer is always preferable.  
**Watermark:** viewer pp. 120-129, 159-163.

## S09 - Scaled dot-product attention and leakage

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q5(a) | 5 marks | Priority: MUST  
**Question.** Compute scaled dot-product attention for the supplied two-dimensional query, three keys and three values, then explain the leakage risk and remedy for next-purchase prediction.

**Solution.** `q=[2,7]`; `k1=k2=[3,1]`, `k3=[7,3]`; `dk=2`.

Raw dots: `[13,13,35]`. Scaled scores: `[13/sqrt2,13/sqrt2,35/sqrt2]=[9.1924,9.1924,24.7487]`.

After max-shift, softmax is approximately `[1.75e-7,1.75e-7,0.99999965]`. With `v1=v2=[3,1]`, `v3=[8,3]`, context is approximately `[7.999998,2.999999]`, effectively `v3`.

If training lets a position see future purchases, it leaks the target and memorizes logs. Apply a causal/look-ahead mask to forbidden future scores **before** softmax.

**Exam writing:** use a score/weight/value table, retain several decimals through softmax, verify that weights sum to one, and finish with the leakage interpretation.  
**Common mistake:** omitting the `sqrt(dk)` scale or applying the causal mask after softmax.  
**Watermark:** viewer pp. 141-150.

## S10 - Additive, cross and multi-head attention

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q5(b-c) | 10 marks | Priority: MUST  
**Question.** Evaluate the supplied additive-attention data under a declared scoring convention; choose cross- versus multi-head self-attention for the stated medical-record tasks, compare additive/dot-product attention, and calculate projection parameters for `d_model=512,h=8`.

**Evidence caution.** Extracted Q5(b) supplies `q,k,v` but no `Wq,Wk,v_score,b`; standard additive attention therefore has no unique numeric answer. State a convention and earn method marks.

Under the simple declared convention `e_i=sum_j tanh(q_j+k_ij)`, the three scores are `[1.75665,1.92806,1.96336]`, softmax weights `[0.29269,0.34741,0.35990]`, and with values `[1,0],[1,1],[3,1]`, context `[1.71979,0.70731]`. A different stated additive parameterization produces a different valid numerical result.

Patient records querying an external drug database require **cross-attention**. Diverse within-record relations require **multi-head self-attention**, so different heads can learn temporal, imaging-medication and lab-medication relations. Dot-product attention is highly parallel and efficient on matrix hardware; additive attention adds learned nonlinear scoring and can be expressive at small dimensions but is less parallel/simple.

For `d_model=512,h=8`, `d_head=64`. With fixed total width, single- and 8-head Q/K/V/O projection weights both total `4d^2=1,048,576` (biases excluded). A limitation is activation/attention memory; mitigate with fewer heads/smaller width, head pruning or local attention.

**Exam writing:** begin the additive numerical with the missing-parameter caveat and declared convention, then answer attention selection, comparison and head-count parts under separate labels.  
**Common mistake:** presenting the convention-dependent additive result as unique or multiplying fixed-width projection parameters by the number of heads.  
**Watermark:** viewer pp. 141-150, 154-158.

## S11 - Positional encoding and transformer family choice

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q6(a) | 7 marks | Priority: MUST  
**Question.** Explain why a transformer needs positional information, then choose encoder-only, decoder-only or encoder-decoder architectures for clinical NER, discharge-note generation and report summarization.

**Solution.** Self-attention without positions is order-insensitive up to permutation: “drug A before drug B” and the reversed order could receive the same content representation. Positional encoding injects absolute/relative order without changing width.

- Clinical NER: encoder-only, because every token benefits from bidirectional context.
- Discharge-note generation: decoder-only, because output is autoregressive.
- Report summarization: encoder-decoder, because the encoder represents the full note and the decoder generates a conditioned summary through cross-attention.

**Exam writing:** give positional encoding's failure mode first, then use a three-row task/architecture/justification table.  
**Common mistake:** selecting encoder-only BERT for free-form generation or claiming positional encoding changes the model width.  
**Watermark:** viewer pp. 150-168.

## S12 - Encoder dimensions and parameters

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q6(b) | 9 marks | Priority: MUST  
**Question.** For a transformer encoder with `L=128,d=512,h=8,dff=2048`, track all tensor dimensions, count attention and FFN parameters, and compare pre-LN with post-LN.

**Solution.** For `L=128,d=512,h=8,dff=2048`, input is `128x512`; each head has Q/K/V `128x64`; concatenated heads and output projection return `128x512`; first Add&Norm stays `128x512`; FFN expands to `128x2048` then contracts to `128x512`; final Add&Norm is `128x512`.

Weights only: attention `4d^2=4(512^2)=1,048,576`; FFN `2ddff=2(512)(2048)=2,097,152`; total `3,145,728`. If projection/FFN biases are included, add `4d+dff+d=4,608`, giving `3,150,336`. LayerNorm parameters are outside the requested two sublayers; if counted, two norms add `4d=2,048`.

Pre-LN applies norm before each sublayer, leaving a cleaner residual gradient path and usually stabilizing deep/early training. Post-LN applies norm after addition; it follows the original architecture and can have strong final quality but often needs more careful warm-up/initialization.

**Exam writing:** track tensor dimensions before counting parameters, and state clearly whether weights, biases and LayerNorm parameters are included.  
**Common mistake:** multiplying the four full-width projections by eight heads or silently mixing weights-only and bias-inclusive totals.  
**Watermark:** viewer pp. 151-159.

## S13 - BERT/GPT/T5 and long-context bottleneck

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q6(c) | 4 marks | Priority: MUST  
**Question.** Compare BERT, GPT and T5 for clinical summarization with 50,000 pairs and four A100 GPUs; quantify the `L=2048` attention bottleneck and give a mitigation with its trade-off.

**Solution.** BERT is encoder-only with masked-token-style pretraining: strong understanding, not naturally autoregressive summarization. GPT is decoder-only with causal next-token pretraining: fluent generation but no dedicated bidirectional source encoder. T5 is encoder-decoder with denoising/span-corruption pretraining: natural conditional summarization. With 50,000 pairs and four A100s, fine-tune a pretrained encoder-decoder; training T5-style from scratch is poorly justified.

At `L=2048`, one attention score matrix contains `2048^2=4,194,304` entries per head, creating major memory/compute cost. Sliding-window attention reduces roughly to `O(Lw)` but may miss distant global links; occasional global tokens can mitigate that trade-off.

**Exam writing:** compare BERT, GPT and T5 by architecture, pretraining objective and suitability, then quantify the attention matrix before naming a mitigation and trade-off.  
**Common mistake:** recommending training T5 from scratch on 50,000 pairs or stating self-attention is linear in sequence length.  
**Watermark:** viewer pp. 160-168.

## S14 - Optimizer and learning-rate curve matching

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q7(a-b-i/ii) | 11 marks | Priority: MUST  
**Question.** Match four supplied training curves to SGD, momentum, RMSProp and Adam; match three learning-rate behaviors to schedules; diagnose falling training loss with rising validation loss and propose an optimizer-level response.

**Solution.** Under the paper's stylized descriptions: A slow/smooth -> SGD; B fast with oscillations -> momentum; C adaptive/low oscillation but earlier higher plateau -> RMSProp; D fastest/smoothest/lowest -> Adam. These matches follow the given curves, not a universal ranking.

Schedule X sharp rise then drop/oscillation -> constant high LR. Y steady rise then early plateau -> constant low LR. Z steady, brief dip, best recovery -> cosine annealing with warm restarts.

Training loss falling while validation loss rises is overfitting. An optimizer-level response is to reduce learning rate on the validation plateau/deterioration and keep the checkpoint at minimum validation loss; early stopping is also defensible as a training-procedure intervention.

**Exam writing:** quote each curve's observed behavior before naming the optimizer or schedule, then keep the overfitting diagnosis and intervention as a separate part.  
**Common mistake:** treating the stylized curve mapping as a universal optimizer ranking or prescribing an architectural change when the prompt asks for an optimizer-level response.  
**Watermark:** viewer pp. 169-183, especially 177-179.

## S15 - Regularization-run diagnosis and BatchNorm

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, I Sem 2025-26, 1 Mar 2026 | Q7(b-iii/iv,c) | 9 marks | Priority: MUST  
**Question.** Diagnose four supplied train/validation outcomes, recommend two complementary regularizers for the severe-overfit run, and explain how BatchNorm changes training behavior.

**Solution.** Run 1 (98/71) is severe overfit/insufficient regularization. Run 2 (84/83, early suboptimal plateau) is underfit or excessive regularization. Run 3 (91/90, smooth) is well balanced. Run 4 (76/74, noisy/slow) indicates unstable training and likely overly aggressive stochastic regularization/poor normalization or LR; the observations alone do not identify a unique hyperparameter.

For Run 1 combine L2/weight decay, which penalizes large weights and smooths the function, with dropout, which prevents co-adaptation by training random subnetworks. Data augmentation or early stopping are alternatives when justified.

BatchNorm standardizes mini-batch activations then learns `gamma,beta`; it reduces activation-scale drift, improves gradient conditioning, permits larger learning rates and usually makes training faster/smoother. It is not a replacement for dropout.

**Exam writing:** diagnose every run in a compact table with observation, condition and reason; explain each chosen regularizer by its mechanism.  
**Common mistake:** equating BatchNorm with dropout or diagnosing overfitting merely from low accuracy without checking the train-validation gap.  
**Watermark:** viewer pp. 184-191.

## S16 - Makeup FFNN forward/activation/loss/gradient flow

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Makeup, I Sem 2025-26 | Q1 | 16 marks | Priority: MUST  
**Source note:** question/data verified from instructor manual; original QP absent. **Depth:** rubric-backed.

**Question.** Perform the supplied three-neuron FFNN forward pass, apply ReLU, define the requested activations, justify cross-entropy over MSE for classification, and identify where/why the smallest backpropagated gradient is expected.

`X=[0.1,0.3,0.5]` and the supplied first weight matrix give:

- neuron 1: `.1(.2)+.3(.3)+.5(.2)=.21`;
- neuron 2: `.1(.4)+.3(.7)+.5(.6)=.55`;
- neuron 3: `.1(.5)+.3(.1)+.5(.9)=.53`.

All are positive, so ReLU output is `[.21,.55,.53]`. Define ReLU, sigmoid and softmax as in S01. Multiclass cross-entropy is `L=-sum_i y_i ln p_i`; it matches probabilities and produces stronger useful gradients than MSE for classification. The largest direct loss gradient is near the output; the smallest tends to be in Hidden Layer 1 after repeated derivative multiplication. Saturated sigmoids amplify shrinkage.

**Exam writing:** show one line per neuron, write the activation vector, then answer activation, loss and gradient-flow subparts under their own headings.  
**Common mistake:** applying ReLU before the weighted sum or claiming the nearest-to-input layer always has the largest gradient.  
**Watermark:** viewer pp. 50-58.

## S17 - Makeup architecture selection and LSTM cell update

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Makeup, I Sem 2025-26 | Q2(A-B) | 20 marks | Priority: MUST  
**Depth:** rubric-backed.

**Question.** Explain vanishing gradients and the LSTM remedy, choose GRU or LSTM for edge and long-context cases, and update the LSTM cell for `Cprev=80,f=.85,i=.25,Ctilde=40`.

Vanishing gradients are products of recurrent derivatives smaller than 1. LSTM's additive cell-state path and input/forget/output gates preserve selected information. Choose GRU for a constrained edge device because it has fewer parameters and faster inference; choose LSTM for very long NLP context because the separate cell state gives explicit long-term memory.

For `Cprev=80,f=.85,i=.25,Ctilde=40`:

`C=.85(80)+.25(40)=68+10=78`.

Interpretation: the forget/retention term dominates; the cell retains most old memory while adding part of the candidate. Hidden state cannot be computed without the output gate, so do not invent it.

**Exam writing:** use cause -> gated remedy -> scenario choice for the conceptual part, then write the LSTM cell equation before the two numerical contributions.  
**Common mistake:** computing a hidden state without an output-gate value or confusing the cell candidate with the cell state.  
**Watermark:** viewer pp. 127-134.

## S18 - Makeup three-step RNN and optimizer curves

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Makeup, I Sem 2025-26 | Q3(A-B) | 20 marks | Priority: MUST  
**Depth:** rubric-backed.

**Question.** Compute three recurrent states for `h_t=tanh(.6x_t+.9h_(t-1))`, `x=[1,2,-1]`, `h0=0`, and match the companion optimizer curves to their algorithms.

Given scalar `h_t=tanh(.6x_t+.9h_(t-1))`, `x=[1,2,-1]`, `h0=0`:

`h1=tanh(.6)=.5370`.

`h2=tanh(1.2+.9(.5370))=tanh(1.6833)=.9333`.

`h3=tanh(-.6+.9(.9333))=tanh(.2400)=.2355`.

Carry at least four decimals between steps. Optimizer curves in the companion figure are rubric-matched A=SGD, B=SGD+Momentum, C=RMSProp, D=Adam.

**Exam writing:** display `h1`, `h2` and `h3` sequentially with the previous state substituted, then justify each optimizer label from the curve behavior.  
**Common mistake:** recomputing each step from `h0` rather than the preceding state.  
**Watermark:** viewer pp. 116-122, 169-179.

## S19 - Complete CNN chain and parameter audit

**[ACTUAL PYQ]** Subject: DNN | Paper: EC3 Regular, II Sem 2024-25, 7 Sep 2025 | Q3 | 10 marks | Priority: MUST  
**Depth:** rubric-backed in the combined paper/key.

**Question.** For the supplied CNN beginning with `192x256x1`, compute every output shape and trainable parameter count through the linear layer, then justify CNNs, ReLU, BatchNorm and dropout.

For input `192x256x1`:

| Layer | Output | Parameters |
|---|---:|---:|
| Conv `1->5,k3,s1,p1` | `192x256x5` | `5(3*3*1+1)=50` |
| Pool `k2,s2` | `96x128x5` | 0 |
| Conv `5->10,k5,s1,p0` | `92x124x10` | `10(5*5*5+1)=1,260` |
| Pool `k2,s2` | `46x62x10` | 0 |
| Conv `10->20,k2,s2,p0` | `23x31x20` | `20(2*2*10+1)=820` |
| Pool `k5,s2` | `10x14x20` | 0 |

Flatten size `10*14*20=2,800`, matching the declared linear input. `Linear(2800,6)` has `2800*6+6=16,806` parameters. CNNs exploit locality and shared weights. ReLU is cheap and avoids positive-side saturation. BatchNorm stabilizes conv activations; dropout before the FC reduces co-adaptation and is disabled at inference.

**Exam writing:** use one table containing every layer's output and parameters, explicitly verify flatten size, then answer each one-mark justification in one precise sentence.  
**Common mistake:** giving pooling layers trainable parameters or using the original image channels when counting later convolutions.  
**Watermark:** viewer pp. 89-104, 184-191.

## S20 - CNN mismatch repair and fully convolutional classifier

**[ACTUAL PYQ]** Subject: DNN | Paper: distinct EC3 sitting dated 14 Sep 2025 (file labelled Makeup; cover says Regular) | Q3 | 10 marks | Priority: MUST  
**Depth:** rubric-backed.

**Question.** For the supplied `32x32x1` CNN, calculate layer shapes and parameters, repair the declared linear-input mismatch, and give a fully convolutional classifier replacement.

Input `32x32x1`:

- Conv1 `k5,s1,p0,8`: `28x28x8`; params `8(25+1)=208`.
- AvgPool1 `k4,s4`: `7x7x8`.
- Conv2 `k4,s1,p1,16`: `6x6x16`; params `16(4*4*8+1)=2,064`.
- AvgPool2 `k2,s2`: `3x3x16`.
- Flatten size: `144`; therefore repair the linear layer to `Linear(144,10)` with `1,450` parameters.

A fully convolutional replacement is `Conv2d(16,10,kernel_size=3,stride=1,padding=0)`, producing `1x1x10`, then softmax. It also has `10(3*3*16+1)=1,450` parameters. Alternative: `1x1` conv to `3x3x10`, then global/3x3 average pooling to `1x1x10`.

**Exam writing:** show the complete shape chain until `3x3x16`, identify the required `144` linear input, and give the replacement layer with input/output channels, kernel and output size.  
**Common mistake:** applying ordinary division instead of the floor-based layer formula.  
**Watermark:** viewer pp. 89-104.

## Final practice variations

These are not actual papers.

### DNN-V01 - Opposite GRU update convention

**[PYQ VARIATION]** Source pattern: S07 | Marks: 4 (practice allocation) | Priority: HIGH  
**Question.** Recompute S07 under the alternative convention `h=(1-z) elementwise*hprev + z elementwise*htilde`. State the convention before calculating.

**Solution.** The source values remain `z=[0.8808,0.7311]`, `htilde=[0.7616,0.4621]`, and `hprev=[0.5,-0.5]`. Therefore

`h_1=(1-.8808)(.5)+(.8808)(.7616)=.7304`,

`h_2=(1-.7311)(-.5)+(.7311)(.4621)=.2034`.

Thus `h=[0.7304,0.2034]`. This differs from S07 because the same symbol `z` weights the candidate rather than the old state.  
**Exam writing:** declare the update equation before substitution; otherwise two internally valid conventions look like contradictory answers.  
**Common mistake:** changing the convention but reusing the original mixing weights.

### DNN-V02 - Transformer width variation

**[PYQ VARIATION]** Source pattern: S12 | Marks: 5 (practice allocation) | Priority: MUST  
**Question.** Repeat S12 for `L=128,d=768,dff=3072,h=12`; verify that a fixed-width multi-head block does not multiply projection weights by the number of heads.

**Solution.** Each head has `d_k=d/h=64`, so each Q/K/V head is `128x64`; concatenation restores `128x768`. Attention weights are `4d^2=4(768^2)=2,359,296`. FFN weights are `2d*dff=2(768)(3072)=4,718,592`. Total weights are `7,077,888`. Including projection and FFN biases adds `4d+dff+d=6,912`, giving `7,084,800`; two LayerNorms would add another `4d=3,072` if explicitly included.  
**Exam writing:** count the four full-width attention projections once; splitting them into 12 heads partitions dimensions, not the parameter matrices.  
**Common mistake:** multiplying `4d^2` by 12.

### DNN-P01 - Causal multihorizon design

**[ORIGINAL PRACTICE]** Source: original exam-style drill | Marks: 6 (practice allocation) | Priority: HIGH  
**Question.** With 16 input features, FP32 parameters, a 24-step input window and six direct forecast outputs, design a causal model under a 2 MiB parameter budget. Compare GRU, LSTM and CNN-GRU in six mark-aware sentences.

**Solution.**

1. A causal `GRU(input=16,hidden=128) -> Linear(128,6)` has `3(128*16+128^2+128)+(128*6+6)=56,454` parameters, about `0.216 MiB` in FP32, so it is comfortably within budget.
2. The direct six-unit head predicts all horizons together and avoids feeding unknown future values back into the recurrent state.
3. An otherwise identical LSTM has `4(128*16+128^2+128)+774=75,014` parameters, about `0.286 MiB`; its separate cell state may help longer dependencies but costs more compute and memory.
4. A causal CNN-GRU can use `Conv1d(16,32,k=3)` with left padding only, followed by `GRU(input=32,hidden=128)` and the same head: `1,568+61,824+774=64,166` parameters, about `0.245 MiB`.
5. The CNN-GRU can capture short local motifs before recurrent aggregation, but padding must be causal and the added stage needs validation against the simpler GRU.
6. Start with the GRU as the lowest-complexity compliant baseline, select by rolling-origin validation across all six horizons, and use the CNN-GRU only if it produces a meaningful error reduction.

**Exam writing:** keep the response to six numbered sentences, show the parameter-to-MiB check, and tie the final choice to causality, budget and validation evidence.  
**Common mistake:** using a bidirectional recurrent layer or symmetric convolution, either of which leaks future information in a causal forecast.  
**Watermark:** viewer pp. 116-133 for RNN/GRU/LSTM and pp. 95-104 for causal convolution mechanics.

## Bank self-check

- [x] 20 high-value solved units, newest papers first.
- [x] Every actual reference and mark value verified in an original paper or instructor manual.
- [x] All reported numerical results recomputed.
- [x] Ambiguous additive-attention and bias-count conventions stated.
- [x] Each solution gives exam-writing or trap guidance and a viewer-page lookup.
- [x] Two variations and one original drill are separately labelled and fully solved.

# DNNWaterMarked.pdf Exam-Room Index

## Page-number convention and verification

All references are **PDF viewer page numbers, 1-196**. They are not the small printed slide numbers inside each four-up page. For example, PDF viewer p. 137 contains printed slides 545-548. The 196-page count, module transitions and representative pages were verified by PDF extraction plus rendered-page visual inspection. The file contains watermarks and many four-up pages; use the large PDF viewer number in this index.

Some pages are image-heavy and yield little extracted text, but were kept in their verified module range. Do not convert a printed slide number into a viewer page by guessing.

## Full logical map

| Viewer pages | Topic/subtopic | What can be looked up | What must be memorized/understood |
|---:|---|---|---|
| 1-8 | DL definitions, tasks and learning framework | definitions/application framing | data-model-objective-algorithm distinction |
| 9-18 | neuron, perceptron, linear separability, XOR | diagrams and perceptron examples | why one linear boundary fails XOR |
| 19-27 | linear regression and GD foundation | worked loss/gradient examples | descent sign and matrix dimensions |
| 28-37 | binary classification, sigmoid/BCE, metrics | formulas and numerical examples | sigmoid+BCE pairing; precision/recall |
| 38-48 | softmax multiclass, CCE, mini-batch, confusion matrix | stable softmax and metrics examples | softmax axis; CCE; class metrics |
| 50-52 | MLP, XOR, activation functions | MLP/XOR diagram; activation comparison | nonlinearity and dying ReLU |
| 53-58 | DFNN forward/backprop/parameter update | full algorithms and derivatives | layer order; dense count; update sign |
| 59-63 | depth/width, architecture, initialization, diagnosis | design tables and issue diagnosis | connect capacity/data/overfit |
| 64-81 | image-heavy DFNN worked/review material | additional worked slides | do not search linearly during exam |
| 82-89 | CNN introduction, locality, sharing, architecture | canonical CNN diagram | why CNN suits images |
| 90-99 | convolution, RF, padding/stride/dilation/channels | worked convolution and RF/channel diagrams | output/parameter/RF formulas |
| 100-104 | 1x1 conv, ReLU, FC, softmax, parameter formulas | parameter reference | conv vs dense counting |
| 105-109 | CNN design patterns, bottlenecks, VGG/ResNet | architecture comparisons | GAP/1x1/depth-width trade-offs |
| 110-111 | transfer learning | freeze/fine-tune flow | which layers change and why |
| 112-115 | sequence motivation and autoregression | sequence/task diagrams | causal vs full-context reasoning |
| 116-122 | RNN equations, parameters, BPTT, vanishing gradient | forward/BPTT examples | RNN recurrence/count; gradient cause |
| 123-126 | BiRNN/deep RNN/selection | parameter examples and restrictions | no BiRNN for causal streaming |
| 127-129 | GRU gates, numerical, parameters | worked gate/state example | chosen GRU convention and x3 count |
| 130-134 | LSTM equations, parameters, GRU comparison | gate/cell diagrams | LSTM recurrence and x4 count |
| 134-136 | recurrent worked questions | RNN parameter/state examples | method and convention |
| 137 | encoder-decoder and training vs inference | architecture diagram | teacher forcing/exposure distinction at course level |
| 138-147 | transformer/attention foundations (image-heavy) | Q/K/V, attention types, alignment diagrams | query-key-value roles |
| 148-150 | attention worked example, positional encoding | numerical/masking/position reference | dot-scale-mask-softmax-values |
| 151 | BatchNorm vs LayerNorm in sequences | comparison | LN is per token/example across features |
| 152-159 | transformer, encoder-only, MHA/FFN numericals | dimensions and full block walkthrough | `4d^2+2ddff`, residual/norm order |
| 160-166 | causal decoder, encoder-decoder, cross-attention, translation | mask/cross-attention examples | decoder family and causal masking |
| 167-168 | BERT and pretraining families | BERT/GPT/encoder-decoder comparison | architecture-objective-task mapping |
| 169-176 | optimizer foundations and behaviour (image-heavy) | curves and update intuition | match mechanism, not a universal ranking |
| 177-179 | GD, momentum, AdaGrad, RMSProp, Adam equations | high-value formula pages | descent sign and Adam bias correction |
| 180-183 | optimizer continuation/schedules | supporting comparisons | high/low/cosine schedule behaviour |
| 184 | regularization overview and bias-variance visual | under/overfit picture | identify gap/underfit |
| 185 | taxonomy, model selection/cross-validation | technique map | explicit vs implicit regularization |
| 186 | vanishing, exploding, covariate shift, sensitivity | cause/remedy tables | match symptom to remedy |
| 187 | computational overhead, initialization, stability | Xavier/He overview | symmetry breaking and activation match |
| 188 | Xavier/He; L1/L2 and bias-variance | formulas/comparison | He-ReLU, Xavier-tanh; L1 vs L2 |
| 189 | model selection and dropout | dropout algorithm/variants | inverted dropout and inference behaviour |
| 190 | BatchNorm | forward algorithm and numerical | training vs running statistics |
| 191 | LayerNorm | formula/algorithm and BN comparison | normalization axis |
| 192 | early stopping and data augmentation | algorithm and examples | stop at best validation; train only |
| 193 | Mixup and hyperparameter tuning | equations/workflow | mixup is regularization; tune on validation |
| 194 | RNN/transformer/CNN-specific regularization | architecture-specific lists | choose technique appropriate to model |
| 195 | conflicts, mistakes, diagnostic plots, hierarchy | combined-strategy checklist | avoid over-regularization/conflicts |
| 196 | golden rules | final checklist | regularization must improve validation/test, not only stability |

## High-value lookup map

| Topic | Viewer page | Look up | Memorize | Understand |
|---|---:|---|---|---|
| Activation/loss pairing | 47-48, 52-54 | comparison table | formulas | task-label relation |
| Backprop | 56-58 | algorithm/derivatives | update sign | chain flow |
| CNN dimensions/params | 95-104 | examples/formulas | both formulas | channel flow |
| Receptive field | 93-99 | recursion/examples | recursion | channels do not affect RF |
| GAP/1x1/bottleneck | 100, 105-106 | diagrams | core effect | parameter trade-off |
| Transfer learning | 110-111 | workflow | freeze/head/fine-tune | data/compute reason |
| RNN/BPTT | 116-122 | worked flow | recurrence/count | shared time weights |
| GRU | 127-129 | gates/example | equation/count | update convention |
| LSTM | 131-133 | gates/count/comparison | equations/count | cell highway |
| Attention | 141-150 | QKV and examples | core formula | masks/types |
| Transformer block | 152-159 | full walkthrough | count formula | residual/norm/dimensions |
| Decoder/cross-attn | 160-166 | diagrams | mask rule | source-target roles |
| BERT/GPT/T5 | 167-168 | comparison | mapping | objective suitability |
| Optimizers | 177-179 | exact equations | mechanism/sign | curve behaviour |
| Regularization diagnosis | 184-196 | tables/algorithms | symptom map | mechanism-specific fix |

## PYQ -> method -> watermark

| Actual PYQ | Concept/method | Viewer reference |
|---|---|---:|
| 2025-26 EC3 R Q1-Q2 | affine/activation/loss/backprop/design | 50-62 |
| 2025-26 EC3 R Q3 | transfer, conv/dense counts, GAP, RF | 90-111 |
| 2025-26 EC3 R Q4 | RNN/GRU states, counts, gradient highway | 116-134 |
| 2025-26 EC3 R Q5 | scaled/additive/multi-head/cross attention | 141-158 |
| 2025-26 EC3 R Q6 | positions, block dims/params, Pre-LN, BERT/GPT/T5 | 150-168 |
| 2025-26 EC3 R Q7 | optimizer/schedule/regularization curves | 169-196 |
| 2025-26 EC3 M Q1 | FFNN calculation and gradient flow | 50-58 |
| 2025-26 EC3 M Q2-Q3 | LSTM/RNN calculation and optimizers | 116-134, 177-179 |
| 2025-26 EC3 M Q5 | CNN shapes/params | 90-104 |
| 2025-26 EC3 M Q6-Q7 | transformer params/translation/long context | 152-168 |
| 7 Sep 2025 EC3 R Q3 | complete CNN chain | 89-104 |
| 14 Sep 2025 sitting Q3 | CNN mismatch and full-conv classifier | 89-104 |

## What to memorize vs look up

### Memorize

Conv output/parameters; dense parameters; RNN/GRU/LSTM equations and x1/x3/x4 counts; attention equation; transformer block count; activation-loss pairings; optimizer mechanism; overfit/underfit diagnosis.

### Understand

Why GRU/LSTM gates help; why channel count is not receptive field; why masks precede softmax; why head count does not double-count fixed-width projections; how scenario constraints determine architecture.

### Look up quickly

Full LSTM/transformer diagrams, exact optimizer recurrences, LayerNorm/BatchNorm algorithms, detailed regularization combinations and worked numeric analogues.

### Too slow to search during the exam

Generic definitions across pp. 1-49; image-heavy pp. 64-81; broad architecture history. Learn the recognition rule now and tab only the target pages.

## Final exam-day cheat index

```text
DNN
|- FFNN/backprop ........ viewer 53-58
|- CNN shapes/params .... viewer 95-104
|- Transfer learning .... viewer 110-111
|- RNN/BPTT ............. viewer 116-122
|- GRU .................. viewer 127-129
|- LSTM ................. viewer 131-133
|- Attention ............ viewer 141-150
|- Transformer block .... viewer 152-159
|- Decoder/cross-attn ... viewer 160-166
|- BERT/GPT/T5 .......... viewer 167-168
|- Optimizer equations .. viewer 177-179
|- Regularization map ... viewer 184-196
|- Dropout / BN / LN .... viewer 189 / 190 / 191
```

Open each target page once before the exam. Searching is backup; recognition and setup should come from memory.

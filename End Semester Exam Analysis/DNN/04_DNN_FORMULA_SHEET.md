# DNN Formula and Method Sheet

## Notation

`d`: input width; `h`: hidden width; `o`: output width; `L`: sequence length; `d_model`: transformer width; `d_k`: key/query head width; `d_ff`: FFN width; `K,S,P,D`: kernel, stride, padding, dilation; `Cin,Cout`: channels.

## Activations and losses

- `ReLU(z)=max(0,z)`; derivative `1` for `z>0`, `0` for `z<0` (use 0 at `z=0` by convention).
- `LeakyReLU(z)=z` if `z>=0`, else `a*z`, `0<a<1`.
- `sigmoid(z)=1/(1+e^-z)`; derivative `s(1-s)`.
- `tanh'(z)=1-tanh^2(z)`.
- `softmax(z_i)=exp(z_i-m)/sum_j exp(z_j-m)`, `m=max(z)`.
- BCE: `-[y ln p+(1-y)ln(1-p)]`.
- CCE: `-sum_k y_k ln p_k`.
- Sigmoid+BCE or softmax+CE output error: `delta = yhat-y` under the usual averaged-loss convention.

## Dense network

- Layer: `Z=A_prev W+b`, `A=f(Z)` (row-batch convention).
- Parameters: `n_in*n_out+n_out`.
- Backprop: `dW=A_prev^T delta/B`; `db=sum_rows(delta)/B`; `delta_prev=(delta W^T) .* f'(Z_prev)`.
- Update: `theta <- theta-eta*gradient`.

## CNN

- Output: `floor((N+2P-D(K-1)-1)/S)+1`.
- Ordinary conv: `floor((N+2P-K)/S)+1`.
- Conv parameters: `(Kh*Kw*Cin+1)*Cout` with one bias/filter.
- Dense after flatten: `(H*W*C)*nout+nout`.
- GAP: `H*W*C -> C`; zero trainable parameters.
- Receptive field: initialize `r0=1,j0=1`; `r_l=r_(l-1)+(K_l-1)D_l*j_(l-1)`; `j_l=j_(l-1)S_l`.

## RNN and BPTT

- `h_t=tanh(Wxh x_t+Whh h_(t-1)+b_h)`.
- Optional output: `y_t=g(Who h_t+b_o)`.
- RNN recurrent parameters: `hd+h^2+h`.
- With output: add `ho+o`.
- Direct recurrent gradient contains products of `Whh` and activation derivatives across time.

## GRU

One common convention used for calculations here:

- `r_t=sigma(Wr x_t+Ur h_prev+b_r)`.
- `z_t=sigma(Wz x_t+Uz h_prev+b_z)`.
- `h_tilde=tanh(Wh x_t+Uh(r_t .* h_prev)+b_h)`.
- `h_t=z_t .* h_prev+(1-z_t).*h_tilde`.
- Parameters: `3(hd+h^2+h)`.
- Direct highway derivative, ignoring candidate path: `dh_t/dh_prev=z_t`.

Some material reverses the old/new weights. Always quote the paper equation.

## LSTM

- `f=sigma(Wf x+Uf hprev+b_f)`.
- `i=sigma(Wi x+Ui hprev+b_i)`.
- `g=tanh(Wg x+Ug hprev+b_g)`.
- `o=sigma(Wo x+Uo hprev+b_o)`.
- `c=f.*cprev+i.*g`.
- `h=o.*tanh(c)`.
- Parameters: `4(hd+h^2+h)` with one bias vector/gate.

## Attention

- `Q=XWQ`, `K=XWK`, `V=XWV`.
- Scores: `S=QK^T/sqrt(d_k)`.
- Mask: set forbidden scores to `-infinity` before softmax.
- `A=softmax_row(S)`; context `C=AV`.
- Additive attention: `e_i=v_a^T tanh(Wq q+Wk k_i+b_a)`; `alpha=softmax(e)`; `c=sum_i alpha_i v_i`.
- `d_head=d_model/num_heads` (must divide evenly in the standard design).
- Fixed-width MHA weights: Q,K,V,O = `4d_model^2` excluding biases.

## Transformer

- One self-attention + FFN block, weights only: `4d^2+2d*d_ff`.
- Projection/FFN biases: `4d+d_ff+d`.
- Two LayerNorms: `4d` trainable parameters (`gamma,beta` per norm).
- Tensor flow: `Lxd -> h copies of Lxd_head -> Lxd -> Lxd_ff -> Lxd`.
- Full self-attention time about `O(L^2 d)`; attention storage `O(L^2)` per head.
- Sinusoidal position: `PE(pos,2i)=sin(pos/10000^(2i/d))`; `PE(pos,2i+1)=cos(pos/10000^(2i/d))`.

## Normalization and regularization

- BatchNorm: `xhat=(x-mu_B)/sqrt(var_B+eps)`; `y=gamma*xhat+beta`.
- LayerNorm: same normalization form, but statistics are across features within one example/token.
- L2 objective: `J_reg=J+lambda/2 * sum w^2`; gradient adds `lambda*w`.
- Dropout (inverted): `h_drop=(m.*h)/(1-p)`, `m~Bernoulli(1-p)` during training; identity at inference.

## Optimizers

- SGD: `theta_t=theta_(t-1)-eta*g_t`.
- Momentum: `v_t=beta*v_(t-1)+eta*g_t`; `theta_t=theta_(t-1)-v_t`.
- AdaGrad: `s_t=s_(t-1)+g_t^2`; `theta_t=theta_(t-1)-eta*g_t/sqrt(s_t+eps)`.
- RMSProp: `s_t=beta*s_(t-1)+(1-beta)g_t^2`; `theta_t=theta_(t-1)-eta*g_t/sqrt(s_t+eps)`.
- Adam: `m_t=b1*m_(t-1)+(1-b1)g_t`; `v_t=b2*v_(t-1)+(1-b2)g_t^2`; `mhat=m_t/(1-b1^t)`; `vhat=v_t/(1-b2^t)`; `theta_t=theta_(t-1)-eta*mhat/(sqrt(vhat)+eps)`.

## Metrics often embedded in DNN scenarios

- Accuracy `(TP+TN)/N`.
- Precision `TP/(TP+FP)`.
- Recall `TP/(TP+FN)`.
- `F1=2PR/(P+R)`.

## Recognition checklist

- Shape question -> write a layer table.
- Gate question -> state convention.
- Attention question -> identify softmax axis and mask.
- Parameter question -> state whether bias/norm/output are included.
- Curve question -> quote observation before diagnosis.
- Architecture question -> connect each design choice to data, latency, memory or causality.

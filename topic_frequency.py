from pathlib import Path
import re, json
ROOT=Path(r"C:\Users\Admin\Downloads\Sem 1\exam_analysis\extracted")
maps={
"MFML":{
"linear systems/vector spaces":r"rank|basis|subspace|linear(?:ly)? independent|rref|linear system|null space",
"eigen/diagonalization":r"eigen|diagonali[sz]",
"SVD":r"singular value|\bsvd\b",
"calculus/gradients/Taylor":r"chain rule|gradient|hessian|taylor|backprop",
"optimization/KKT/Lagrange":r"lagrange|kkt|constrained optimi|convex",
"GD/optimizers":r"gradient descent|momentum|adagrad|rmsprop|adam|learning rate",
"PCA":r"principal component|\bpca\b|maximum variance",
"SVM/kernels":r"support vector|\bsvm\b|hinge loss|kernel"
},
"ISM":{
"probability/Bayes":r"probability|bayes",
"distributions/RV":r"binomial|poisson|normal distribution|random variable|expectation|variance",
"confidence intervals/CLT":r"confidence interval|central limit|\bclt\b",
"hypothesis tests":r"hypothesis|level of significance|z.test|t.test|proportion",
"chi-square/ANOVA":r"chi.square|anova|analysis of variance",
"correlation/regression":r"correlation|regression|least square|sse",
"time series/forecasting":r"time series|moving average|exponential smoothing|forecast|arima|sarima|white noise",
"MLE":r"maximum likelihood|\bmle\b",
"GMM/EM":r"gaussian mixture|\bgmm\b|expectation.maximization|\bem algorithm"
},
"DNN":{
"FFNN/backprop/activations":r"feedforward|perceptron|backprop|relu|softmax|cross.entropy|activation",
"optimization":r"optimizer|gradient descent|momentum|rmsprop|adam|learning rate",
"regularization":r"regulari[sz]|dropout|batch norm|overfit|underfit|initialization",
"CNN":r"\bcnn\b|convolution|pooling|receptive field|resnet|transfer learning",
"RNN/LSTM/GRU":r"\brnn\b|lstm|gru|recurrent|sequence",
"attention":r"attention|query|keys?|values?|multi.head",
"transformers/BERT":r"transformer|bert|gpt|positional encod|encoder.decoder",
"advanced/time series":r"federated|meta.learning|neural architecture search|time series forecast|online learning"
},
"ML":{
"linear regression/regularization":r"linear regression|ridge|lasso|bias.variance",
"logistic/classification":r"logistic regression|discriminant|decision theory",
"decision trees/MDL":r"decision tree|entropy|information gain|minimum description|\bmdl\b",
"KNN/LWR/RBF":r"\bknn\b|k.nearest|locally weighted|\blwr\b|radial basis",
"SVM/kernels":r"support vector|\bsvm\b|kernel|hinge",
"Bayesian/NB":r"na.ve bayes|bayes optimal|map hypothesis|maximum likelihood|\bmle\b",
"ensembles":r"ensemble|bagging|random forest|adaboost|gradient boost|xgboost",
"K-means/GMM/EM":r"k.means|gaussian mixture|\bgmm\b|expectation.maximization|\bem algorithm",
"evaluation/fairness":r"model evaluation|fairness|interpretability|confusion matrix|precision|recall|roc|f1"
}}

def papers(subj):
    fs=[]
    for p in ROOT.glob(f"{subj}_Question_papers_*"):
        n=p.name.lower()
        if "midsem" in n or "ec2" in n or "sample" in n or "past_papers" in n or "previous_batch" in n: continue
        if not any(x in n for x in ["endsem","comprehensive","compre","ec3"]): continue
        fs.append(p)
    return fs

for subj,topics in maps.items():
    fs=papers(subj)
    print('\n###',subj,'PAPERS',len(fs))
    for topic,pat in topics.items():
        hits=[]
        for p in fs:
            txt=p.read_text(encoding='utf-8',errors='ignore')
            if re.search(pat,txt,re.I): hits.append(p.name)
        recent=sum('2026' in x for x in hits)
        print(f"{topic}\t{len(hits)}/{len(fs)}\trecent={recent}\t"+'; '.join(hits))

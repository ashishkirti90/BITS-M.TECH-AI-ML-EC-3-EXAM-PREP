from pathlib import Path
import re
root=Path(r"C:\Users\Admin\Downloads\Sem 1\exam_analysis\extracted")
files={
'MFML':root/'MFML_MFML watermark.pdf.txt',
'ISM':root/'ISM_ISM_watermark.pdf.txt',
'DNN':root/'DNN_DNNWaterMarked.pdf.txt',
'ML':root/'ML_ML WaterMark.pdf.txt',
}
topics={
'MFML':{'systems/rank':r'linear systems?|rref|rank|basis|subspace','eigen/SVD':r'eigen|singular.value|\bsvd\b','calculus/Hessian':r'gradient|jacobian|hessian|chain rule','GD/optimizers':r'gradient descent|momentum|adagrad|rmsprop|adam','KKT/Lagrange':r'kkt|lagrang','PCA':r'principal component|\bpca\b','SVM/kernel':r'support vector|\bsvm\b|kernel'},
'ISM':{'probability/Bayes':r'probability|bayes','distributions':r'binomial|poisson|normal distribution|random variable','tests/CI':r'hypothesis|confidence interval|z.test|t.test','ANOVA/chi/F':r'anova|chi.square|f.test|variance ratio','correlation/regression':r'correlation|regression','time series/forecast':r'time.series|moving average|exponential smoothing|arima|forecast|white noise','GMM/EM':r'gaussian mixture|\bgmm\b|expectation.maximization'},
'DNN':{'FFNN/backprop':r'feedforward|perceptron|backprop|activation|cross.entropy','CNN':r'convolution|\bcnn\b|pooling|receptive field|resnet','RNN/LSTM/GRU':r'\brnn\b|lstm|gru|recurrent','attention':r'attention|query|key|value','transformer':r'transformer|bert|gpt|positional encoding','optimization':r'optimizer|momentum|rmsprop|adam|learning rate','regularization':r'regularization|dropout|batch norm|overfit'},
'ML':{'regression/reg':r'linear regression|ridge|lasso|regularization','logistic':r'logistic regression','tree':r'decision tree|information gain|entropy','KNN/LWR':r'\bknn\b|k.nearest|locally weighted|gower','NB':r'na.ve bayes|laplace smoothing','ensembles':r'bagging|random forest|adaboost|gradient boosting','Kmeans/GMM':r'k.means|gaussian mixture|expectation.maximization','SVM':r'support vector|\bsvm\b|kernel trick'},
}
for subj,p in files.items():
    txt=p.read_text(encoding='utf-8',errors='ignore').replace('\x00','')
    chunks=re.split(r'\n===== PAGE (\d+) =====\n',txt)
    pages={int(chunks[i]):chunks[i+1] for i in range(1,len(chunks),2)}
    print('\n###',subj)
    for name,pat in topics[subj].items():
        hits=[n for n,t in pages.items() if re.search(pat,t,re.I)]
        print(name,':',','.join(map(str,hits)))

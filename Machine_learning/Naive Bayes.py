from __future__ import division, print_function
import math
import numpy as np


# deal with continuous features
# assume the features subject to Gaussian Distribution
class NaiveBayes():
    def __init__(self):
        self.x = None
        self.y = None
        self.classes = None
        self.param = []
    def fit(self,x,y):
        self.x = x
        self.y = y
        self.classes = np.unique(self.y)
        for i in range(len(self.classes)):
            c = self.classes[i]
            x_c = x[np.where(y==c)]

            # calculate the means and variance of every feature for each class
            self.param.append([])
            for j in range(len(x_c[0,:])):
                col = x_c[:,j]
                param = {}
                param['mean']=col.mean()
                param['var']=col.var()
                self.param[i].append(param)

    def cal_gaussian_probability(self,mean,var,x):
        coef = (1.0/(math.sqrt((2*math.pi)*var)))
        expo = math.exp(-(math.pow(x-mean,2)/(2*var)))
        return coef*expo

    #calculate priori-probability
    def cal_pri_probability(self,c):
        x_c = self.x[np.where(y==c)]
        return (x_c.shape[0])/self.x.shape[0]

    # Classify using Bayes Rule, P(Y|X) = P(X|Y)*P(Y)/P(X)
    # P(X|Y) - Probability. Gaussian distribution (given by calculate_probability)
    # P(Y) - Prior (given by calculate_prior)
    # P(X) - Scales the posterior to the range 0 - 1 (ignored)
    # Classify the sample as the class that results in the largest P(Y|X)
    # classify the single sample
    def classify(self,sample):
        posteriors = []
        # iterate over all classes
        for i in range(len(self.classes)):
            c = self.classes[i]
            prior = self.cal_pri_probability(c)

            posterior = np.log(prior)
            # P(Y|X) = P(Y)*P(x1|Y)*P(x2|Y)*...*P(xN|Y)
            # iterate over features and cal p(x|c) for this sample
            for j,param in enumerate(self.param[i]):
                mean= param['mean']
                var = param['var']
                sample_feat = sample[j]
                prob = self.cal_gaussian_probability(mean,var,sample_feat)
                posterior+=np.log(prob)
            posteriors.append(posterior)

        idx = np.argmax(posteriors)
        return self.classes[idx]
    # classify the sample datasets
    def predict(self,x):
        pre = []
        for sample in x:
            out = self.classify(sample)
            pre.append(out)
        return np.array(pre)

if __name__=='__main__':
    x_train,y_train,x_test=[],[],[]
    clf = NaiveBayes()
    clf.fit(x_train,y_train)
    pre = clf.predict(x_test)

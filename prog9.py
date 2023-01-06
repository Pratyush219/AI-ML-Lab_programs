import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def kernel(xmat, point, k):
    m, n = xmat.shape
    w = np.eye(m)
    for i in range(m):
        diff = point - xmat[i]
        w[i][i] = np.exp((diff * diff)/(-2 * k ** 2))
    return w
def localWeight(xmat, ymat, point, k):
    wei = kernel(xmat, point, k)
    weights = (xmat.T * (wei * xmat)).I * (xmat.T * (wei * ymat))
    return weights
def localWeightedRegression(xmat, ymat, k):
    m, n = xmat.shape
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * localWeight(xmat, ymat, xmat[i], k)
    return ypred

def graphPlot(xmat, ypred):
    sortindex = xmat.argsort(0)
    xsort = np.array([item[0] for item in sorted(xmat)]).flatten()
    plt.figure()
    plt.scatter(bill, tip, color='green')
    plt.plot(xsort, ypred[sortindex].flatten(), color='red', linewidth=5)
    plt.show()
data = pd.read_csv('./tips.csv')
bill = np.array(data.total_bill)
tip = np.array(data.tip)
mbill = np.mat(bill)
mtip = np.mat(tip)
X = mbill.T
Y = mtip.T
ypred = localWeightedRegression(X, Y, 1.5)
graphPlot(X, ypred)
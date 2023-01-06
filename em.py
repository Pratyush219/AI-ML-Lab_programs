from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.mixture import GaussianMixture
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import plot_utils as utils

x, y, colormap = utils.x, utils.y, utils.colormap
scaler = preprocessing.StandardScaler()

scaler.fit(x)
print(scaler.mean_)
xsa = scaler.transform(x)
xs = pd.DataFrame(xsa, columns=x.columns)
# print(xs)
gmm = GaussianMixture(n_components=3)
gmm.fit(xs)
y_gmm = gmm.predict(xs)
# plt.figure(figsize=(14,7))
plt.subplot(223)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Target], s=40)
plt.title('Real')

plt.subplot(224)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y_gmm], s=40)
plt.title('EM')
print('accuracy score:\n', accuracy_score(y.Target, y_gmm))
print('confusion_matrix:\n', confusion_matrix(y.Target, y_gmm))
# plt.show()
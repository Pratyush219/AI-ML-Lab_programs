from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plot_utils as utils

model = KMeans(n_clusters=3)
model.fit(utils.x)

# plt.figure(figsize=(14, 7))
plt.subplot(223)
plt.scatter(utils.x.Petal_Length, utils.x.Petal_Width, c=utils.colormap[utils.y.Target], s=40)
plt.title('Real')

plt.subplot(224)
plt.scatter(utils.x.Petal_Length, utils.x.Petal_Width, c=utils.colormap[model.labels_], s=40)
plt.title('KMeans')
print('confusion matrix: ', confusion_matrix(utils.y.Target, model.labels_))
print('accuracy score:', accuracy_score(utils.y.Target, model.labels_) * 100)
plt.show()
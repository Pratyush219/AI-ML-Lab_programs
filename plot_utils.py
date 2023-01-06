import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = pd.DataFrame(iris.target, columns=['Target'])

colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(14, 7))
plt.subplot(221)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[y.Target], s=40)
plt.title('Sepal')

plt.subplot(222)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Target], s=40)
plt.title('Petal')
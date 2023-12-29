import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

X, _ = datasets.make_moons(n_samples=500, noise=0.1,
                           random_state=42)
kmeans = KMeans(n_clusters=2, random_state=42)
Y = kmeans.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()
#  Algoritmo DBSCAN
# O algoritmo k-means funciona bem para grupos esféricos e bem formados, mas
# pode ter problemas com agrupamentos em outros tipos de formatos. Como exemplo,
# considere o código que usa o k-means para agrupar dados em formato de
# lua. Podemos ver no resultado exibido na Figura desse exercício que, mesmo informando o número
# correto de agrupamentos, o k-means não funciona muito bem. Para esse tipo de conjunto
# de dados, é mais interessante utilizar outro tipo de algoritmo como o k-means.
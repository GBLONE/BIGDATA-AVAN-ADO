import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn import datasets

X, _ = datasets.make_moons(n_samples=500, noise=0.1,
                           random_state=42)
dbscan = DBSCAN()
Y = dbscan.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()
# O código mostra uma tentativa de execução do DBSCAN para
# agrupar dados em formato de lua. Contudo, como mostrado na Figura desse exercício, o algoritmo não
# consegue um bom resultado usando os valores padrões para seus parâmetros eps=0.5 e
# min_samples=5. O parâmetro eps é a distância máxima entre vizinhos e o parâmetro
# min_samples o número mínimo de pontos para a vizinhança a ser considerada densa.
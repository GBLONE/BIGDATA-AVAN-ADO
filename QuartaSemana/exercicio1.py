import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def executa_kmeans(X, k):
    # Inicializa algoritmo k-means com 4 grupos
    kmeans = KMeans(n_clusters=k, random_state=42)
    # Executa o algoritmo e armazena o grupo de cada elementos y_grupos
    y_grupos = kmeans.fit_predict(X)
    # Plota os elementos em seus grupos
    plt.scatter(X[:, 0], X[:, 1], c=y_grupos)
    plt.show()

# Gera dados para agrupamento
X, _ = make_blobs(n_samples=200, random_state=42, centers=4)
executa_kmeans(X, 3)
executa_kmeans(X, 4)
# A melhora da qualidade dos agrupamentos é feita com base nos erros quadráticos.
# O erro quadrático de um grupo é a soma das distâncias entre os elementos e o centroide
# do grupo. O cálculo do erro quadrático é dada pela fórmula da Equação (6), onde xi é um
# elemento do grupo e m é o centroide do grupo contendo n elementos. Durante a
# execução, o algoritmo k-means tenta minimizar essa soma.
#
# Durante a execução, o algoritmo k-means tenta minimizar a soma dos erros
# quadráticos de todos os grupos. A execução é interrompida quando essa soma estabiliza e
# não a mais mudanças de elementos entre grupos.
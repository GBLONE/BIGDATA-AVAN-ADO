import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

def busca_k(Algoritmo, X, max_k):
    # inicia melhor k com valor médio
    melhor_k = int((2 + max_k)/ 2)
    melhor_sil = float('-inf')
    # varia k (número de grupos)
    for k_atual in range(2, max_k+1):
        # executa algoritmo de agrupamento
        agrupador = Algoritmo(n_clusters=k_atual)
        pred = agrupador.fit_predict(X)
        if len(np.unique(pred)) > 1:
            # calcula silhueta
            sil_atual = silhouette_score(X, pred)
            # atualiza melhores valores
            if sil_atual > melhor_sil:
                melhor_sil = sil_atual
                melhor_k = k_atual
    return melhor_k, melhor_sil

def executa_k(Algoritmo, X, k):
    # executa algoritmo de agrupamentos
    agrupador = Algoritmo(n_clusters=k)
    y_grupos = agrupador.fit_predict(X)
    # plota resultados
    plt.scatter(X[:, 0], X[:, 1], c=y_grupos)
    plt.show()

# cria dados sintéticos
X, _ = datasets.make_blobs(n_samples=1200, random_state=11,
                           centers=4,
                           cluster_std=[0.5, 0.7, 1.1, 1.3])
Algoritmo = KMeans
melhor_k, silhueta = busca_k(Algoritmo, X, 10)
executa_k(Algoritmo, X, melhor_k)
print(f'Silhueta: {round(silhueta, 3)}')

Algoritmo = AgglomerativeClustering
melhor_k, silhueta = busca_k(Algoritmo, X, 10)
executa_k(Algoritmo, X, melhor_k)
print(f'Silhueta: {round(silhueta, 3)}')

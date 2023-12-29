import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets

# Para tentar automatizar a tarefa de seleção de parâmetros para o algoritmo
# AgglomerativeClustering, vamos, inicialmente, criar uma função que calcula a silhueta
# considerando um critério de ligação e variando o número de grupos. A função irá retornar o
# número de grupos com maior valor de silhueta e também a contagem de valores de
# silhueta negativos. O código com a importação das bibliotecas e a
# função busca() para para buscar número de agrupamentos considerando um critério de
# ligação.
# O código exibe também a função busca_k_link() que chama a função busca() e
# decide pelo melhor critério de ligação. O resultado retornado será o número de
# agrupamentos e o critério de ligação ideais. A última função apresentada no código é a
# executa_agg() que recebe uma base de dados e os parâmetros para o algoritmo
# AgglomerativeClustering. A função executa o algoritmo e plota um gráfico com o
# resultado do agrupamento.

def busca_cont_neg(X, max_k, link):
    # Inicia melhor k com valor médio
    melhor_k = int((2+max_k)/2)
    # contagem de silhuetas negativas
    cont_neg = 0
    melhor_sil = float('-inf')
    # varia k (número de grupos)
    for k_atual in range(2, max_k + 1):
        # executa algoritmo de agrupamento
        agg = AgglomerativeClustering(n_clusters=k_atual,
                                      linkage=link)
        pred = agg.fit_predict(X)
        if len(np.unique(pred)) > 1:
            # calcula silhueta
            sil_atual = silhouette_score(X, pred)
            # contagem de silhuetas negativas
            if sil_atual < 0:
                cont_neg += 1
            # atualiza melhoras valores
            if sil_atual > melhor_sil:
                melhor_sil = sil_atual
                melhor_k = k_atual
    return melhor_k, melhor_sil, cont_neg

def busca_k_link(X, max_k):
    # busca melhores valores (single)
    k_single, sil_single, neg_single = busca_cont_neg(X, max_k, 'single')
    # testa se houveram silhuetas negativas
    if neg_single > 0 and sil_single > 0:
        return k_single, 'single'
    # busca melhores valores (ward)
    k_ward, _, _ = busca_cont_neg(X, max_k, 'ward')
    return k_ward, 'ward'

def executa_agg(X, k, link):
    # executa algoritmo de agrupamento
    agg = AgglomerativeClustering(n_clusters=k,
                                  linkage=link)
    y_grupos = agg.fit_predict(X)
    # plota resultado
    plt.scatter(X[:, 0], X[:, 1], c=y_grupos)
    plt.show()

# O restante do código para executar o experimento completo nas
# bases de dados X1, X2 e X3. Após a geração dos dados, o laço de repetição chama a
# função busca_k_link() para encontrar os melhores valores de parâmetros. De posse
# desses valores, chamamos a função executa_agg() para execução do algoritmo. O
# resultado da execução do código é apresentado quando apertamos run. Podemos observar que,
# com a seleção dos parâmetros o algoritmo obteve um bom resultado para todas as bases
# de dados.

X1, _ = datasets.make_moons(n_samples=500, noise=0.1, random_state=42)
X2, _ = datasets.make_blobs(n_samples=200, random_state=42, centers=4)
X3, _ = datasets.make_blobs(n_samples=1500, random_state=1,
                            centers=5, cluster_std=0.6)

# testa cada base de dados
for cont, X in enumerate([X1,X2,X3]):
    print('X', cont+1, sep='')
    melhor_k, melhor_link = busca_k_link(X, 10)
    print(f'Melhor link: {melhor_link}')
    print(f'Melhor k: {melhor_k}')
    executa_agg(X, melhor_k, melhor_link)




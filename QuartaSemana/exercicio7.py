import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets

def executa_algomerativo(X):
    # Executa algoritmo
    agg = AgglomerativeClustering()
    y_grupos = agg.fit_predict(X)
    # Plota resultado
    plt.scatter(X[:, 0], X[:, 1], c=y_grupos)
    plt.show()

# Cria bases de dads
X1, _ = datasets.make_moons(n_samples=500, noise=0.1,
                            random_state=42)
X2, _ = datasets.make_blobs(n_samples=200, random_state=42,
                            centers=4)
X3, _ = datasets.make_blobs(n_samples=1500, random_state=1, centers=5,
                            cluster_std=0.6)
# Executa o algoritmo para cada base de dados
for cont, X in enumerate([X1, X2, X3]):
    executa_algomerativo(X)
    print('X', cont+1, sep='')

# Conforme já mencionamos, os algoritmos hierárquicos podem usar abordagens
# aglomerativa ou divisiva. Na prática, a abordagem aglomerativa é mais utilizada, então
# vamos focar nessa metodologia utilizando a classe AgglomerativeClustering do módulo
# sklearn.cluster.
# Os principais parâmetros do algoritmo AgglomerativeClustering são o número de
# grupos (n_clusters) e o critério de ligação (linkage). O critério de ligação determina qual
# distância usar entre grupos com possibilidade de junção. O algoritmo irá mesclar os pares
# de agrupamento que minimizem este critério. Os valores mais interessantes para o
# parâmetro linkage são 'single' (simples) e 'ward' (similaridade).
# No critério de ligação simples, a distância é definida como a distância mínima entre
# um objeto de um agrupamento e um objeto no outro agrupamento. O critério de
# similaridade tem como base a variância dos dois agrupamentos. Em vez de medir a
# distância diretamente, ele analisa a distância entre os pontos antes e depois da fusão. A
# ligação simples é indicada para manipular formas não elípticas, mas é bastante sensível a
# ruídos. Já a ligação por similaridade é menos prejudicada por ruídos e funciona melhor
# para agrupamentos esféricos e elípticos.
# O algoritmo AgglomerativeClustering usa por padrão n_clusters=2 e
# linkage='ward'. O código mostra a execução do algoritmo usando os
# parâmetros com valor padrão sobre três bases de dados distintas. As Figuras desse exercício mostra o
# resultado da execução do código. Podemos observar que o algoritmo não obteve um bom
# resultado para nenhuma das três bases de dados, pois o número de agrupamentos
# (n_clusters) não foi adequado para as bases X2 e X3 e o critério de ligação (linkage) não
# foi adequado para a base de dados X1.

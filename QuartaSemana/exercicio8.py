import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets

# Para melhorar o resultado do algoritmo vamos utilizar novamente a medida da
# silhueta, mas, dessa vez, temos que analisar o número de agrupamentos e o critério de
# ligação. Inicialmente, variar o critério de ligação e número de agrupamento para calcular a
# silhueta para cada variação.

def lista_silhueta(X, max_k):
    for link_atual in ['single', 'ward']:
        for k_atual in range(2, max_k + 1):
            agg = AgglomerativeClustering(n_clusters=k_atual,
                                          linkage= link_atual)
            pred = agg.fit_predict(X)
            if len(np.unique(pred)) > 1:
                sil_atual = silhouette_score(X, pred)
            else:
                sil_atual = float('nan')
            print(f'{link_atual}, {k_atual}, ', sil_atual, sep='')

# cria bases de dados
X1, _ = datasets.make_moons(n_samples=500, noise=0.1,
                            random_state=42)
X2, _ = datasets.make_blobs(n_samples=200, random_state=42,
                            centers=4)
X3, _ = datasets.make_blobs(n_samples=1500, random_state=1,
                            centers=5, cluster_std=0.6)
# executa o algoritmo para cada base de dados
for cont, X in enumerate([X1,X2,X3]):
    lista_silhueta(X, 6)
    print('X', cont+1, sep='')

# O resultado da execução do código para calcular a silhueta variando o número de
# grupos e o critério de ligação pode ser visto da Figura 128. Para cada critério de ligação,
# destacamos o melhor valor de silhueta encontrado. Na base X3, o maior valor de silhueta
# corresponde aos melhores valores para o critério de ligação e número de grupos. No caso
# da base X2, tivemos o mesmo valor de silhueta para os critérios de ligação 'single' e
# 'ward'. Como os agrupamentos estão bem separados nessa base, os dois critérios
# funcionam bem.
# A medida da silhueta não funciona muito bem para agrupamentos em formatos não
# esféricos como acontece na base de dados X1. Assim, todas as silhuetas para o critério de
# ligação 'ward' são maiores do que no 'single'. Contudo, o algoritmo
# AgglomerativeClustering não funciona muito bem em agrupamentos não esféricos
# utilizando tal critério de ligação. Portanto, simplesmente considerar o maior valor de
# silhueta não é o ideal para agrupamentos não esféricos.
# Se observarmos novamente os valores de silhueta na Figura 128 para a base de
# dados X1, percebemos que temos alguns valores negativos e outros positivos no critério
# de ligação 'single'. Os valores negativos indicam que o resultado do agrupamento está
# muito ruim. Porém, se temos valores negativos e positivos nesse critério de ligação, é
# provável que estejamos lidando com agrupamentos não esféricos e pode ser melhor
# manter o critério de ligação 'single'.
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN
from sklearn import datasets
from sklearn.neighbors import NearestNeighbors

def gera_lista_eps(X, min_k, max_k):
    # Calcula distâncias para os vizinhos mais próximos
    knn = NearestNeighbors(n_neighbors=max_k).fit(X)
    # self.knn_ = NearestNeighbors(n_neighbors=self.k).fit(X)
    lista_dist, _ = knn.kneighbors(X)
    # Considera apenas distâncias maiores do que zero
    lista_dist = lista_dist[lista_dist > 0]
    # Distâncias mínima e máxima
    min_dist, max_dist = np.min(lista_dist), np.max(lista_dist)
    # Retorna faixa de valores entre as distâncias mínima e máxima
    return np.linspace(min_dist, max_dist, num=X.shape[0]//min_k)

def busca_eps(X):
    # Valores mínimos e máximos para k
    min_k, max_k = X.shape[1] + 1, (X.shape[1] + 1) * 3
    # Gera faixa de valores se eps para teste
    lista_eps = gera_lista_eps(X, min_k, max_k)
    # Melhores silhuetas e eps
    melhor_sil = float('-inf')
    melhore_eps = np.mean(lista_eps)
    for eps_atual in lista_eps:
        # Executa DBSCAN para cada valor
        dbscan = DBSCAN(eps=eps_atual, min_samples=max_k)
        pred = dbscan.fit_predict(X)
        # teste encontrou mais de um agrupamento
        if len(np.unique(pred)) > 1:
            # Calcula silhueta
            sil_atual = silhouette_score(X, pred)
            # Verifica se a silhueta melhorou
            if sil_atual > melhor_sil:
                melhor_sil = sil_atual
                melhore_eps = eps_atual
    # Retorna eps relacionado com melhor silhueta
    return melhore_eps

def busca_k(X, eps):
    # Valores mínimos e máximos para k
    min_k, max_k = X.shape[1] + 1, (X.shape[1] + 1) * 2
    # Melhores silhueta e k
    melhor_sil = float('-inf')
    melhor_k = int((min_k + max_k) / 2)
    for k_atual in range(min_k, max_k + 1):
        # Executa DBSCAN variando k
        dbscan = DBSCAN(eps=eps, min_samples=k_atual)
        pred = dbscan.fit_predict(X)
        if len(np.unique(pred)) > 1:
            sil_atual = silhouette_score(X, pred)
            # atualiza silhueta e k
            if sil_atual > melhor_sil:
                melhor_sil = sil_atual
                melhor_k = k_atual
    return melhor_k

X, _ = datasets.make_moons(n_samples=500, noise=0.1,
                           random_state=42)
melhor_eps = busca_eps(X)
melhor_k = busca_k(X, melhor_eps)
print(f'Melhor eps: {melhor_eps}')
print(f'Melhor k: {melhor_k}')

# A definição dos melhores valores para os parâmetros eps e min_samples não é
# uma tarefa muito simples. Contudo, existem algumas técnicas que podem ajudar. Para
# encontrar um eps interessante, podemos utilizar como limites a distância mínima e
# distância máxima para os k vizinhos mais próximos e, depois, testar valores dentro desses
# limites. O código mostra como podemos gerar uma lista de possíveis valores
# de eps para teste.

# A técnica proposta depende fortemente do número de k vizinhos mais próximos
# considerados. Em nossos experimentos vamos considerar um mínimo (min_k) de L+1 e
# um máximo (max_k) de (L+1)*3 vizinhos, onde L é o número de atributos da base de
# dados. Em nosso código, utilizamos a classe NearestNeighbors do módulo neighbors
# para calcular as distâncias de cada ponto para o maior número de vizinhos (max_k). As
# distâncias iguais a zero são ignoradas. No final, usamos a menor e a maior de distância
# para gerar uma lista de possíveis valores de eps com a função linspace() da biblioteca
# numpy. A quantidade de valores da lista é calculada dividindo o número de registros da
# base de dados (X.shape[0]) pelo número mínimo de vizinhos (min_k). Os valores da lista
# são divididos em intervalos iguais.

# Após gerarmos uma lista de valores de eps, devemos fazer um experimento para
# verificar qual desses valores proporciona um agrupamento mais interessante dos dados.
# Em nossos, experimentos vamos avaliar a qualidade dos agrupamentos com a medida de
# silhueta. O valor da silhueta representa o quão semelhante um objeto é ao seu próprio
# agrupamento em comparação com outros agrupamentos. O valor da silhueta varia de -1 a
# +1, sendo que os valores mais altos indicam que o agrupamento está com melhor
# qualidade. Uma observação importante é que a silhueta só pode ser calculada quando
# temos mais de um agrupamento de dados.

# O código apresenta a função busca_eps() que procura pelo melhor valor para
# eps considerando a medida da silhueta. Observe que, no algoritmo DBSCAN, variamos o
# valor de eps e mantemos min_samples=max_k. Valores maiores de min_simples, em
# geral, são melhores quando estamos procurando o melhor para eps.

# Depois de encontrarmos o melhor valor para eps, podemos realizar outro
# experimento para tentar descobrir o melhor valor para o parâmetro min_samples.
# o código da função busca_k() responsável por esse experimento. Observe
# que, agora, utilizamos o valor de (L+1)*2 para número máximo de vizinho. Normalmente,
# no experimento de busca pelo melhor valor de min_samples, não é recomendável utilizar
# valores maiores do que esse.
# Assim, obtermos o valor de aproximado de 0.119 para o eps e o valor de 3 para o min_samples.
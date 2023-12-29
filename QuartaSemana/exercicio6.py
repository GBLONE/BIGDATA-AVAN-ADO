import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import datasets

# Com a obtenção dos melhores valores do último exercício (5) para os parâmetros do algoritmo,
# podemos fazer uma nova execução e analisar o gráfico da plotagem dos grupos.
# Nesse exercício (6) mostra o código para fazer essa execução.

X, _ = datasets.make_moons(n_samples=500, noise=0.1,
                           random_state=42)
dbscan = DBSCAN(eps=0.119, min_samples=3)
Y = dbscan.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()

grupos = np.unique(Y)
grupos = grupos[grupos != -1]
ruidos = Y[Y == -1]
print(f'Agrupamentos: {len(grupos)}')
print(f'Ruídos: {len(ruidos)}')

# A figura desse exercício (6) mostrará o resultado da execução do DBSCAN com os parâmetros
# otimizados. Podemos notar que, dessa vez, o algoritmo conseguiu agrupar melhor os dois
# agrupamentos em formato de lua. Os agrupamentos encontrados estão coloridos em
# amarelo e verde. Os pontos roxos são os ruídos, ou seja, aqueles pontos que não foram
# incluídos em nenhum agrupamento.

# É importante mencionar que, mesmo com os valores encontramos para os
# parâmetros nos experimentos executados, ainda podemos fazer ajustes nos mesmos para
# tentar melhorar o resultado. Com um valor de eps igual 0.2, por exemplo, conseguimos
# dois agrupamentos sem nenhum ruído. Esses ajustes manuais dependem de um bom
# conhecimento da base de dados e análise dos agrupamentos encontrados.
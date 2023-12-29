from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import f1_score

dados = datasets.load_digits()
X, Y = dados.data, dados.target
print('Diferentes profundidades:')
for profundidade in range(1, 16):
    arvore = tree.DecisionTreeClassifier(random_state=42,
                                         criterion='entropy',
                                         max_depth=profundidade)
    previsoes = cross_val_predict(arvore, X, Y, cv=10)
    f1score = f1_score(Y, previsoes, average='weighted')
    print(f'Profundidade {profundidade} :', round(f1score, 4))

# O parâmetro criterion é chamado de hiperparâmetro do algoritmo de classificação.
# Cada algoritmo de classificação pode possuir hiperparâmetros diferentes que podem afetar
# seu funcionamento e, principalmente, seu desempenho. No caso da árvore de decisão, um
# hiperparâmetro muito importante é a profundidade máxima da árvore, definida pelo
# parâmetro max_depth na instanciação da classe. O código mostra um experimento de
# teste na variação da profundidade máxima da árvore de decisão sobre uma base de dados
# de dígitos manuscritos digitalizados.
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Carrega a base de dados
X, Y = load_wine(return_X_y=True)
# Cria Classificador de árvore de decisão
arvore = DecisionTreeClassifier(random_state=42)
# Calcula acurácia sem divisão
arvore.fit(X, Y)
acuracia = arvore.score(X, Y)
print(f'Acurárcia sem divisão: {acuracia}')
# Divisão da base de dados
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, train_size=0.7, random_state=42)

# Acurárcia com divisão da base em treino e teste
arvore.fit(X_treino, Y_treino)
acuracia = arvore.score(X_teste, Y_teste)
print(f' Acurácia após divisão: {acuracia}')

# As duas estratégias básicas para avaliar o desempenho de métodos de
# classificação são a divisão e a validação cruzada. A estratégia de divisão, também
# chamada de holdout ou split-sample, divide a base de dados em uma partição de
# treinamento e outra de teste. Normalmente, a partição de treinamento é maior (cerca de
# 2/3 ou 70% do total de registros). O algoritmo faz o treinamento na partição maior e
# contabiliza a taxa de acerto classificando os registros da partição de teste. Como cada
# registro já possui sua classe, é possível verificar se o classificador acertou.
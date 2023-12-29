import numpy as np
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score

# Carrega a base de dados
X, Y = load_wine(return_X_y=True)
# Cria classificador de árvore de decisão
arvore = DecisionTreeClassifier(random_state=42)
# Divisão de dados
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, train_size=0.7, random_state=42)
# Acuracia com divisão da base em treino e teste
arvore.fit(X_treino, Y_treino)
acuracia = arvore.score(X_teste, Y_teste)
print(f'Acurácia com divisão: {acuracia}')
# Acurácia com validação cruzada
acuracia = np.mean(cross_val_score(arvore, X, Y, cv=10))
print(f'Acurácia com validação cruzada: {acuracia}')

# Quando temos uma base de dados pequena e retiramos 1/3 ou 30% dos dados,
# podem sobrar poucos dados para treinamento levando a um modelo de baixa precisão.
# Uma alternativa para essa situação é usar uma técnica de validação cruzada.
# Basicamente, na validação cruzada, a base de dados é particionada em subconjuntos
# mutuamente exclusivos para que alguns subconjuntos sejam usados para treinamento e os
# demais para teste. Dizemos que conjuntos são mutuamente exclusivos quando os
# elementos de um conjunto não aparecem em nenhum dos outros conjuntos.
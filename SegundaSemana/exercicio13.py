from sklearn import datasets
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

# Normalização
# Base de Dados de vinhos
dados = datasets.load_wine()
X = dados.data
Y = dados.target

# Classificador KNN
knn = KNeighborsClassifier()

# Classificação dos dados originais
knn.fit(X, Y)
acuracia = knn.score(X, Y)
print(f'Dados originais:')
print(f'Valor mínimo: {X.min()}')
print(f'Valor máximo: {X.max()}')
print(f'Acurárcia: {acuracia}')

# Normalização
X = preprocessing.normalize(X, axis=0)
# Classificação dos dados após seleção
knn.fit(X, Y)
acuracia = knn.score(X, Y)
print(f'\nDados normalizados:')
print(f'Valor mínimo: {X.min()}')
print(f'Valor máximo: {X.max()}')
print(f'Acurárcia: {acuracia}')

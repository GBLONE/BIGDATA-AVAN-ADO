from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import KBinsDiscretizer
from sklearn import datasets

# Discretização
# Base de dados de vinhos
dados = datasets.load_wine()
X, Y = dados.data, dados.target

# Classificador KNN
knn = KNeighborsClassifier()
# Classificação dos dados originais
knn.fit(X, Y)
acuracia = knn.score(X, Y)
print(f'Dados Originais:')
print(f'Acurárcia: {acuracia}')

# Discretização
discretizador = KBinsDiscretizer(n_bins=4)
X = discretizador.fit_transform(X)
# Classificação dos dados discretizados
knn.fit(X, Y)
acuracia = knn.score(X, Y)
print(f'Dados Discretizados:')
print(f'Acurárcia: {acuracia}')

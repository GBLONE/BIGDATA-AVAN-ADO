from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA

# Criação do conjunto de dados
X, Y = make_classification(n_samples=1000, n_informative=10,
                           n_redundant=10, random_state=42)
# Classificador Árvore de decisão
arvore = DecisionTreeClassifier(random_state=42, max_depth=7)

# Classificação dos dados Originais
arvore.fit(X, Y)
acuracia = arvore.score(X, Y)
print('Número de atributos originais:', X.shape[1])
print('Acurárcia (dados originais:', acuracia)

# Aplicação do PCA
pca = PCA(n_components=10)
X = pca.fit_transform(X, Y)

# Classificação dos dados PCA
arvore.fit(X, Y)
acuracia = arvore.score(X, Y)
print('\nNúmero de atributos PCA:', X.shape[1])
print('Acurárcia (dados PCA):', acuracia)
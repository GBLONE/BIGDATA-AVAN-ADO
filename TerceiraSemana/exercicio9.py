from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import f1_score

def varia_k(X, Y):
    for k in range(1, 16, 2):
        knn = KNeighborsClassifier(n_neighbors=k)
        previsoes = cross_val_predict(knn, X, Y, cv=10)
        f1score = f1_score(Y, previsoes, average='weighted')
        print(f'K= {k} :', round(f1score, 4))

dados = datasets.load_digits()
X, Y = dados.data, dados.target
print('Base de dados digits, f1-score variando k:')
varia_k(X, Y)

dados = datasets.load_iris()
X, Y = dados.data, dados.target
print('Base de dados iris, f1-score variando k:')
varia_k(X, Y)

# Ao utilizarmos um algoritmo KNN é importante fazer alguns experimentos variando o
# número de vizinhos mais próximos para encontramos o valor mais adequado.
# Esse código executa esse experimento para duas bases de dados.
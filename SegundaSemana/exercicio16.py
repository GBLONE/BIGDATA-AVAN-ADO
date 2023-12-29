from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import KBinsDiscretizer
from sklearn import datasets

def discretiza_classifica(classificador, X, Y, num_intervalos, estrategia):
    # Cria discretizador
    discretizador = KBinsDiscretizer(n_bins=num_intervalos,
                                     strategy=estrategia)
    # Discretiza
    X_discretizado = discretizador.fit_transform(X)
    # Classifica
    classificador.fit(X_discretizado, Y)
    return classificador.score(X_discretizado, Y)

def principal():
    dados = datasets.load_wine()
    X, Y = dados.data, dados.target
    # Listas de números de intervalos e de estratégias
    lista_intervalos = [n for n in range(2,8)]
    lista_estrategias = ['uniform', 'quantile', 'kmeans']
    # Classificador KNN
    knn = KNeighborsClassifier()
    knn.fit(X,Y)
    print('Acurárcias obtidas')
    print('Dados originais: ', knn.score(X,Y))
    # Percorre lista de números de intervalos e de estratégias
    for estrategias in lista_estrategias:
        for num_intervalos in lista_intervalos:
            acuracia = discretiza_classifica(knn, X, Y, num_intervalos, estrategias) #
            print(f'Estrategia {estrategias} ( {num_intervalos} ): {acuracia}', sep='')

if __name__ == '__main__':
    principal()



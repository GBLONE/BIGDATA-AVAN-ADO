from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier

#  Experimento com classificadores KNN e Árvore de decisão

def experimento_knn(atributos, classe):
    ''' Experimento com algoritmo KNN '''
    best_score = float('-inf')
    best_k = None
    print('Testando hiperparâmetros:')
    for k in range(1, 30, 2):
        knn = KNeighborsClassifier(n_neighbors=k)
        previsoes = cross_val_predict(knn, atributos, classe, cv=10)
        f1score = f1_score(classe, previsoes, average='weighted')
        print(round(f1score, 4), ' (k: ', k, ')', sep='')
        if f1score > best_score:
            best_score = f1score
            best_k = k
    return best_score, best_k

def experimento_arvore(atributos, classe):
    '''Experimento com árvore de decisão'''
    prof_max = atributos.shape[1]
    lista_medidas = ['gini', 'entropy']
    best_score = float('-inf')
    best_medida = None
    best_profundidade = None
    print('Testando hiperparâmetros:')
    for medida in lista_medidas:
        for profundidade in range(2, prof_max+2):
            arvore = DecisionTreeClassifier(random_state=42,
                                            max_depth=profundidade,
                                            criterion=medida)
            previsoes = cross_val_predict(arvore, atributos,
                                          classe, cv=10)
            f1score = f1_score(classe, previsoes,
                               average='weighted')
            print(round(f1score, 4), '(Medida:', medida,
                  ', Profundidade:', profundidade, ')')
    return best_score, best_medida, best_profundidade

def principal():
    '''Função principal'''
    dados = datasets.load_breast_cancer()
    atributos, classe = dados.data, dados.target
    print('\nExperimento com KNN')
    f1score_knn, k = experimento_knn(atributos, classe)
    print('\nExperimento com a árvore de decisão')
    f1score_arvore, medida, profundidade = experimento_arvore(atributos, classe)
    print(f'\nMelhor resultado para KNN:')
    print(f'K: {k}')
    print(f'F1-score:', round(f1score_knn, 4))
    print(f'\nMelhor resultado para árvore de decisão:')
    print(f'Medida: {medida}')
    print(f'Profundidade: {profundidade}')
    print(f'F1-Score: ', round(f1score_arvore, 4))

if __name__ == '__main__':
    principal()
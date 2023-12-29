from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_fscore_support

dados = datasets.load_wine()
X, Y = dados.data, dados.target
lista_medidas = ['gini', 'entropy']
for medida in lista_medidas:
    arvore = tree.DecisionTreeClassifier(random_state=42,
                                         criterion=medida)
    previsoes = cross_val_predict(arvore, X, Y, cv=10)
    precicao, revocacao, f1score, _ = precision_recall_fscore_support(Y, previsoes, average='weighted')

    print(f'Medida: {medida}')
    print('- Precisão:', round(precicao, 4))
    print('- Revocação:', round(revocacao, 4))
    print('- F1-score:', round(f1score, 4))

# A medida de ganho de informação utilizada por padrão é o índice de Gini ('gini').
# Além dela, a classe DecisionTreeClassifier permite a utilização da entropia ('entropy')
# com a utilização do parâmetro criterion na instanciação da classe. O cálculo da entropia é
# um pouco mais lento, mas, em geral, a árvore de decisão tende a apresentar resultados
# mais interessantes.
#
# O código que compara o desempenho das medidas de ganho.
# O resultado do código é apresentado quando executamos ele. 
# Como podemos, observar a árvore que utilizou a entropia, obteve melhor desempenho.
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier

# Carrega base de dados
dados = load_wine()
X, Y = dados.data, dados.target
# Cria classificador de árvore de decisão
arvore = DecisionTreeClassifier(max_depth=2, random_state=42)
# Classificação com validação cruzada
previsoes = cross_val_predict(arvore, X, Y, cv=10)
# Matriz de confusão
matriz = confusion_matrix(Y, previsoes)
for cont, linha in enumerate(matriz):
    print(linha, ':', dados.target_names[cont])
# Uma importante ferramenta para analisar classificadores é a chamada matriz de
# confusão que sumariza como os registros foram classificados. O número de classificações
# corretas fica na diagonal principal, enquanto o número de classificações incorretas fica nas
# demais posições.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A matriz de confusão também pode ser gerada para classificações envolvendo mais
# de uma classe (multi-classe). Como exemplo vamos considerar esse código que
# faz a classificação e extrai a matriz de confusão para a base de dados de vinhos.
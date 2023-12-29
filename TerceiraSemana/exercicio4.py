from sklearn.datasets import load_wine
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier

# Carrega a base de dados
data = load_wine()
X, Y= data.data, data.target
# Classificador e classificação
arvore = DecisionTreeClassifier(max_depth=2, random_state=42)
previsoes = cross_val_predict(arvore, X, Y, cv=10)

# Medidas para cada classe
precicao, revocacao, f1score, suporte = precision_recall_fscore_support(Y, previsoes)
for posicao, classe in enumerate(data.target_names):
    print(f'\n Classe: {classe} (suporte:', suporte[posicao], ')')
    print(f'- Precisão:', round(precicao[posicao], 4))
    print(f'- Revocação:', round(revocacao[posicao], 4))
    print(f'- F1-score:', round(f1score[posicao], 4))

# Média simples das medidas
precicao, revocacao, f1score, _ = precision_recall_fscore_support(Y, previsoes, average='macro')
print('\n Geral (média simples):')
print(f'- Precisão:', round(precicao, 4))
print(f'- Revocação:', round(revocacao, 4))
print(f'- F1-score:', round(f1score, 4))

# Média ponderada das medidas
precicao, revocacao, f1score, _ = precision_recall_fscore_support(Y, previsoes, average= 'macro')
print('\nGeral (média ponderada):')
print(f'- Precisão:', round(precicao, 4))
print(f'- Revocação:', round(revocacao, 4))
print(f'- F1-score:', round(f1score, 4))

# O cálculo das medidas para cada classe foi realizado com a função
# precision_recall_fscore_support(). Quando passamos apenas os parâmetros Y (valor
# real de cada classe) e previsoes (valor predito para cada classe), essa função retorna
# vetores com o valor de medida de cada classe. As medidas retornadas são precisão,
# revocação, f1-score e suporte. O suporte é apenas a contagem de cada valor de classe.
# Depois de calcularmos as medidas, fazemos um laço de repetição para exibir os valores
# para cada classe.
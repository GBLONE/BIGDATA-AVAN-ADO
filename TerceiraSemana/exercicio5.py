from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import tree

# Carrega base de dados
dados = datasets.load_iris()
X, Y = dados.data, dados.target
# Cria arvore
arvore = tree.DecisionTreeClassifier(max_depth=2, random_state=42)
arvore.fit(X, Y)
# Impreme árvore
print(tree.export_text(arvore))
# Árvore como figura
plt.figure(figsize=(12, 8))
tree.plot_tree(arvore,
               feature_names=dados.feature_names,
               class_names=dados.target_names,
               filled=True)
# Pág 86
# O código mostra um exemplo de criação de uma árvore de decisão para a base
# de dados íris. Depois da criação da árvore, utilizamos a função export_text() do módulo
# tree para mostrar um representação textual da árvore na tela. Em seguida, usamos a
# função plot_tree() do mesmo módulo para mostrar a representação gráfica da árvore no
# formato de uma figura. Como a função plot_tree() usa o módulo pytplot da biblioteca
# matplotlib, nós importamos também esse módulo para aumentar o tamanho da figura
# passando o parâmetro figsize para a função figure().

from sklearn import datasets
from sklearn import tree

# Carrega base de dados
dados = datasets.load_iris()
X, Y = dados.data, dados.target
# Criar árvore
arvore = tree.DecisionTreeClassifier(max_depth=2, random_state=42)
arvore.fit(X, Y)
# Faz classificação de registro
registro = [7, 3.2, 4.7, 1.4]
num_classe = arvore.predict([registro])[0]
classe = dados.target_names[num_classe]
print(f'Classificando registro: {registro}')
print(f'Classe: {classe}')

# Depois de criarmos uma árvore, podemos classificar novos registros usando o
# método predict(). A Figura 100 mostra um exemplo de código que realiza essa tarefa.
# O resultado da execução do código pode ser feito. O método predict() recebe
# uma vetor de registros para classificação e retorna um vetor com as classes de cada
# registro recebido. Como estamos classificando um único registro, devemos incluí-lo em
# uma lista ([registro] como parâmetro do método) e pegar a primeira classe do resultado
# ([0] no resultado do método).
import os
import pickle
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

ARQUIVO = 'arvore.pickle'

def linha(caractere='-'):
    '''Escreve linha caracteres'''
    print(caractere * 50)

def cria_arvore():
    '''Cria árvore e salva em arquivo'''
    # Carrega dados
    dados = datasets.load_iris()
    atributos, classe = dados.data, dados.target
    # Cria e treina a árvore
    arvore = DecisionTreeClassifier(random_state=42, max_depth=3)
    arvore.fit(atributos, classe)
    # Atribuí nomes das classes na árvore
    arvore.classes_ = dados.target_names
    # Salva árvore em arquivo
    pickle.dump(arvore, open(ARQUIVO, 'wb'))
    return arvore

def carrega_arvore():
    '''Carrega a árvore salva em arquivo'''
    if os.path.isfile(ARQUIVO):
        # Carrega árvore já criada em arquivo
        return pickle.load(open(ARQUIVO, 'rb'))
    return cria_arvore()

def classifica(arvore):
    '''Classifica um registro'''
    print('Informe os dados')
    sepala_comp = float(input('Comprimento da sépala (cm): '))
    sepala_larg = float(input('Largura da sépala (cm): '))
    petala_comp = float(input('Comprimento da pétala (cm): '))
    petala_larg = float(input('Largura da pépala (cm): '))
    # Registro a ser classificado
    registro = [[sepala_comp, sepala_larg, petala_comp, petala_larg]]
    # Classificação
    classe = arvore.predict(registro)[0]
    linha()
    print(f'\nClasse do registro: {classe}')
    linha()
    input()

def principal():
    '''Função principal'''
    arvore = carrega_arvore()
    while True:
        linha('=')
        print('Classificador de íris')
        linha('=')
        print('C) Classificar uma flor')
        print('S) Sair')
        linha()
        resp = input('Informe sua opção: ')
        if len(resp) >= 1 and resp[0].lower() == 'c':
            classifica(arvore)
        if len(resp) >= 1 and resp[0].lower() == 's':
            break
if __name__ == '__main__':
    principal()
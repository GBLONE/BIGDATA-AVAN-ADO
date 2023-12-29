import pandas as pd
from seaborn import load_dataset

def amostragem_classes(dados, atributo_classe, quantidade):
    '''Amostragem com quantidade por classe'''
    # Contagem das classes
    contagem_classes = dados[atributo_classe].value_counts()
    # Dataframe vazio para guardar amostras
    amostras = pd.DataFrame()
    for classe in contagem_classes.index:
        # Filtra os dados pela classe
        dados_classe = dados[dados[atributo_classe] == classe]
        if len(dados_classe) > quantidade:
            # Amostragem sem Substituição
            amostra_classe = dados_classe.sample(n=quantidade,
                                                 replace=True)
        else:
            # Amostragem com Substituição
            amostra_classe = dados_classe.sample(n=quantidade,
                                                 replace=True)
        # Inclui Amostras da classe no resultado
        amostras = amostras._append(amostra_classe)
    return amostras
# Teste com a Base de dados penguins
dados = load_dataset('penguins')
atributo_classe = 'species'
print(f'Dados Originais:\n', dados[atributo_classe].value_counts(),
      sep='')
amostra = amostragem_classes(dados, atributo_classe, 100)
print('\nAmostra:\n', amostra[atributo_classe].value_counts(),
      sep='')

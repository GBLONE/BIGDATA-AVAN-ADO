import pandas as pd
from seaborn import load_dataset

dados = load_dataset('penguins')
# Amostragem sem Substituição
print('Amostragem sem substituição')
amostra = dados.sample(frac=0.1)
print(amostra.index.value_counts().head())

# Amostragem com Substituição
print('Amostragem com substituição')
amostra = dados.sample(n=50, replace=True)
print(amostra.index.value_counts().head())

# Amostragem estratificada
print('Amostragem estratificada')
print('Contagem da base de dados original: ')
contagem = dados['species'].value_counts()
print(contagem)
amostra = pd.DataFrame()
for n in range(len(contagem)):
    especie = contagem.index[n]
    quantidade = int(contagem[n] * 0.1)
    amostra_especie = dados[dados['species'] == especie].sample(n=quantidade)
    amostra = amostra.append(amostra_especie)
print('Contagem da amostra')
print(amostra['species'].value_counts())

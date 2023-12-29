import pandas as pd

dados = pd.read_csv('produtos.csv')
print(f'\nDados lidos de arquivo: {dados}')
dados.sort_values(by='Estoque', ascending=False, inplace=True)
print(f'\nProdutos ordenados pelo estoque:\n {dados}')
dados.reset_index(inplace=True)
dados.drop(columns='index', inplace=True)
print(f'\n Produtos ordenados com índice atualizado:\n {dados}')
print(f'\n Terceiro produtos:\n ', dados.loc[2])
print(f'\n Posições com estoque maior que 100:\n', dados['Estoque'] > 100)
print(f'\n Produtos com estoque alto:\n',
      dados[dados['Estoque'] > 100])
print(f'\n Produtos com estoque e preços altos:\n',
      dados[(dados['Estoque'] > 100) & (dados['Preço'] > 20)])

import pandas as pd

dados = pd.DataFrame(
    {
        'Produto': ['Desodorante', 'Leite', 'Feijão', 'Doritos', 'Arroz'],
        'Preço': [10.5, 5.8, 9, 15.3, 21],
        'Estoque': [120, 100, 50, 150, 204]
    }
)

print(f'Produtos:\n {dados}')
print(f'\nTipos de dados:\n {dados.dtypes}')
print(f'\nColunas: {dados.columns}')
print(f'\nEstoque:\n ', dados['Estoque'])
print(f'\nSalvando dados em Arquivo')
dados.to_csv('produtos.csv', index=False)

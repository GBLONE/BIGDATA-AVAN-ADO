import pandas as pd

precos = pd.Series([10.5, 5.8, 9, 15.3, 21, 11.4, 4, 7])
print(f'Series com index automático:\n {precos}')

precos = pd.Series([10.5, 5.8, 9, 15.3, 21, 11.4, 4, 7],
                   index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print(f'\nSeries com index Rotulado:\n {precos}')

print('\nPreço do produto B: ', precos['B'])
print(f'\nPreço médio: {precos.mean()}')

print(f'\nPreços com 20% de aumento:\n {precos * 1.2}')

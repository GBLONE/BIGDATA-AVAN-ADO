import numpy as np

print('Matriz 5x5')
a = np.array(range(25)).reshape(5, 5)
print(a)
print(f'Elemento a linha 2 coluna 3: {a[2, 3]}')
print(f'Linhas 2 a 3:\n {a[2: 4]}')
print(f'Colunas 1 a 3:\n {a[:, 1:3]}')
print(f'Recorte (1,3) a (3,5):\n {a[1:3, 3:5]}')



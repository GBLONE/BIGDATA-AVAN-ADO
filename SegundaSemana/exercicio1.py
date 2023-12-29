import numpy as np

a = np.array([1,2,3,4])
print('\nVetor de inteiros\n', a)
print(a.dtype)

a = np.array([1,2,3,4], dtype='float64')
print('\nVetor de flutuantes\n', a)
print(a.dtype)

a.shape = (2, 2)
print(f'formato: {a.shape}')
print('\nVetor bidimensional', a)

print('\nMudando o formato do vetor')
a = np.array([1,2,3,4,5,6,7,8,9])
a = a.reshape(3, -1)
print(f'Dimensões: {a.ndim}')
print(a)

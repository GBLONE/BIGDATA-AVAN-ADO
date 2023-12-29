import numpy as np

print('Operações com vetores')
a = np.array([3, 4, 8, 2])
b = np.array([5, 7, 4, 1])
print(f'a = {a}')
print(f'b = {b}')
print(f'a + b = {a + b}')
print(f'a * b = {a * b}')
print(f'a * 3 = {a * 3}')

print('Mínimo, Máximo, Média')
a = np.arange(9).reshape(3,3)
print(a.min(), a.max(), a.mean())

print('Menor linha, Menor coluna, Média da coluna')
print(a.min(axis=0), a.min(axis=1), a[:, 2].min())

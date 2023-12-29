import numpy as np

print('Vetor com arange()')
a = np.arange(0, 2, 0.2)
print(a)

print('\nVetor com linspace()')
a = np.linspace(0, 1, 8)
for n in a.flat:
    print(n)

import math

n = float(input('Informe número: '))
x = n * math.pi #calculando PI
print('x = n * pi = ', n)
print('Teto de x =', math.ceil(x))
print('Piso de x =', math.floor(x))
print('Log de X na base 10 =', math.log(x, 10))
print('Raiz de x =', math.sqrt(x))

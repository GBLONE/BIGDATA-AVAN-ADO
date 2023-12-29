n1 = int(input('Informe seu número:'))
n2 = int(input('Informe mais um número:'))

p = (n1 > n2)
q = (n1 != n2)
r = not (p or q) and ( not p)

#Verdadeiro ou falso

print('p =', p)
print('q =', q)
print('r =', r)

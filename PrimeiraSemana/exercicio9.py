import math

#### ----- Tratamento de exceções ----- ####

while True:
    try:
        print('Informe dois números')
        n1 = float(input('N1 = '))
        n2 = float(input('N2 = '))
        r = n1 / n2
        break
    except:
        print('Ocorreu um erro!')

# print(n1, '/', n2, '=', r)
print(f"{n1} / {n2} = {r}")

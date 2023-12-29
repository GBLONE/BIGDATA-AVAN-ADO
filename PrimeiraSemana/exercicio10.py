
#### ----- Tratamento de exceções ----- ####

while True:
    try:
        print('Informe dois números')
        n1 = float(input('N1 = '))
        n2 = float(input('N2 = '))
        r = n1 / n2
        break
    except ValueError as e:
        print(e)
        print('Número Inválidos! Tente Novamente.')
    except ZeroDivisionError as e:
        print(e)
        print('Divisão por zero! Tente novamente.')

print(f"{n1} / {n2} = {r}")

# Página 35 E-Book Big DATA AVANÇADO
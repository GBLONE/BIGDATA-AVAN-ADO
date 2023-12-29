
soma = 0

while True:
    n = float(input('Informe um número: '))
    if n == 0:
        break
    else:
        soma = soma + n
    print('Soma dos números:', soma)
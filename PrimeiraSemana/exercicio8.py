
print('Informe dois números:')
n1 = int(input('N1: '))
n2 = int(input('N2: '))

# máximo divisor comum ou MDC; é encontrado quando multiplicamos
# os fatores que dividem simultaneamente os números fatorados.

if n1 < 1 or n2 < 1:
    print('Números inválidos para MDC')
else:
    while True:
        resto = n1 % n2
        print(n1, '/', n2, '-> resto:', resto)
        if resto == 0:
            break
        n1 = n2
        n2 = resto
    print('O MDC é', n2)





#### ----- Modularização ----- ####
def fat(num):
    if num <= 1:
        return 1
    return num * fat(num - 1)

def cubo(num):
    return num * num * num

n = int(input('Informe um número: '))
print(f'{n} ao cubo é: {cubo(n)}')
print(f'O fatorial de {n} é {fat(n)}')


#encontrando o seu sobre nome
nome_completo = input('Informe seu nome completo:')
sobrenome = input('Informe seu sobrenome:')

pos = nome_completo.find(sobrenome)

if pos != -1:
    print('Seu sobrenome começa na posição ', pos)
else:
    print('Sobrenome não encontrado')

n = float(input('Informe um número:'))
print('{n:.8f}'.format(n=n))


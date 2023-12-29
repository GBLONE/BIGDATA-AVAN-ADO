
#### ----- Coleções ----- ####

soma = 0
lista_precos = []

print('Informe o preço dos Produtos')
for cont in range(10):
    mensagem = 'Produto' + str(cont + 1) + ': '
    preco = float(input(mensagem))
    soma += preco
    lista_precos.append(preco)
media = soma / 10

print(f'O preço médio é {media}')
print(f'Os produtos com preço acima da media são:')

for cont, preco in enumerate(lista_precos):
    if preco > media:
        print(f'Produto {cont + 1}')
        print(f'Preço: {preco}')

# Médias dos preços, comparação dos preços de cada produto

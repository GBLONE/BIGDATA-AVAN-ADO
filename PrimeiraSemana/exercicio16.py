
print('Informe as datas')

print('Primeira data')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
data1 = (ano, mes, dia)

print('Segunda data')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
data2 = (ano, mes, dia)
recente = data1

if data2 > data1:
    recente = data2
print(f'Data mais recente: {recente}')





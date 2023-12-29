
#### ----- Modularização ----- ####

def juros(capital, taxa, tempo=12):
    return (capital * taxa * tempo) / 100

print('Cálculo de Juros')
cap = float(input('Capital: '))
tax = float(input('Taxa: '))
tem = input('Tempo (deixe em branco para o padrão de 12):')

if tem == '':
    jur = juros(cap, tax)
else:
    tem = float(tem)
    jur = juros(taxa=tax, capital=cap, tempo=tem)
print('O valor dos juros é', jur)


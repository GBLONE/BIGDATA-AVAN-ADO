import seaborn as sb

voos = sb.load_dataset('flights')
print(voos.head())
voos_anual = voos.groupby('year').sum()
print(voos_anual.head())

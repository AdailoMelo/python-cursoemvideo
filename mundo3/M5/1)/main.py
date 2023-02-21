import moeda
n = float(input('Digite o preço R$'))
print(f'{"RESULTADOS":^60}')
print('-='*30)
print(f'O dobro de {n:.2f} é {moeda.dobro(n):.2f}')
print(f'A metade de {n:.2f} é {moeda.metade(n):.2f}')
print(f'{n:.2f} aumentado em 10% é {moeda.aumentar(n):.2f}')
print(f'{n:.2f} diminuido em 5% é {moeda.diminuir(n, 5):.2f}')
print('-='*30)
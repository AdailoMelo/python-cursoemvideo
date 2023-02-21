import moeda
n = float(input(f'Digite o preço R$'))
print(f'{"RESULTADOS":^60}')
print('-='*30)
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'{moeda.moeda(n)} aumentado em 10% é {moeda.aumentar(n, 10, True)}')
print(f'{moeda.moeda(n)} reduzido em 10% é {moeda.diminuir(n, 10, True)}')
print('-='*30)
from moeda import aumentar, diminuir, metade, dobro, moeda
n = float(input(f'Digite o preço R$'))
print(f'{"RESULTADOS":^60}')
print('-='*30)
print(f'{moeda(n)} aumentado em 10% é {moeda(aumentar(n, 10))}')
print(f'{moeda(n)} aumentado em 10% é {moeda(diminuir(n, 10))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n), "R$")}')
print(f'A metade de {moeda(n)} é {moeda(metade(n), "R$")}')
print('-='*30)